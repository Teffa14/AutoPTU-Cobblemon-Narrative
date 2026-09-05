from __future__ import annotations

import heapq
import json
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from tools.global_npc_memory import (
    KnowledgeLedger,
    evaluate_belief,
    record_direct_observation,
    transmit_claim,
)


class DeliveryStatus(str, Enum):
    QUEUED = "QUEUED"
    WAITING_LOCAL_ACK = "WAITING_LOCAL_ACK"
    DELIVERED = "DELIVERED"
    FAILED_CHANNEL_UNAVAILABLE = "FAILED_CHANNEL_UNAVAILABLE"


@dataclass(frozen=True)
class CommunicationChannel:
    channel_id: str
    kind: str
    latency_minutes: int
    available: bool = True
    requires_local_projection: bool = False

    def __post_init__(self) -> None:
        if self.latency_minutes < 0:
            raise ValueError("latency_minutes must be non-negative")


@dataclass(frozen=True)
class InformationEnvelope:
    event_id: str
    message_id: str
    sender_id: str
    receiver_id: str
    source_claim_id: str
    new_claim_id: str
    channel_id: str
    created_minute: int
    delivery_minute: int
    receiver_trust_in_sender: int = 0


@dataclass
class InformationEventQueue:
    channels: dict[str, CommunicationChannel]
    ledgers: dict[str, KnowledgeLedger]
    pending: list[tuple[int, str, InformationEnvelope]] = field(default_factory=list)
    statuses: dict[str, DeliveryStatus] = field(default_factory=dict)
    delivered_event_ids: set[str] = field(default_factory=set)
    awaiting_local_ack: dict[str, InformationEnvelope] = field(default_factory=dict)

    def schedule(
        self,
        *,
        event_id: str,
        message_id: str,
        sender_id: str,
        receiver_id: str,
        source_claim_id: str,
        new_claim_id: str,
        channel_id: str,
        created_minute: int,
        receiver_trust_in_sender: int = 0,
    ) -> InformationEnvelope:
        if event_id in self.statuses or event_id in self.delivered_event_ids:
            raise ValueError(f"event_id already exists: {event_id}")
        if sender_id not in self.ledgers or receiver_id not in self.ledgers:
            raise KeyError("sender and receiver must have ledgers")
        if source_claim_id not in self.ledgers[sender_id].claims:
            raise KeyError(f"sender does not know claim: {source_claim_id}")
        channel = self.channels[channel_id]
        envelope = InformationEnvelope(
            event_id=event_id,
            message_id=message_id,
            sender_id=sender_id,
            receiver_id=receiver_id,
            source_claim_id=source_claim_id,
            new_claim_id=new_claim_id,
            channel_id=channel_id,
            created_minute=created_minute,
            delivery_minute=created_minute + channel.latency_minutes,
            receiver_trust_in_sender=receiver_trust_in_sender,
        )
        heapq.heappush(self.pending, (envelope.delivery_minute, envelope.event_id, envelope))
        self.statuses[event_id] = DeliveryStatus.QUEUED
        return envelope

    def process_due(self, semantic_minute: int) -> list[dict]:
        results: list[dict] = []
        while self.pending and self.pending[0][0] <= semantic_minute:
            _, _, envelope = heapq.heappop(self.pending)
            if envelope.event_id in self.delivered_event_ids:
                continue
            channel = self.channels[envelope.channel_id]
            if not channel.available:
                self.statuses[envelope.event_id] = DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE
                results.append({
                    "event_id": envelope.event_id,
                    "receiver_id": envelope.receiver_id,
                    "status": DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value,
                })
                continue
            if channel.requires_local_projection:
                self.statuses[envelope.event_id] = DeliveryStatus.WAITING_LOCAL_ACK
                self.awaiting_local_ack[envelope.event_id] = envelope
                results.append({
                    "event_id": envelope.event_id,
                    "receiver_id": envelope.receiver_id,
                    "status": DeliveryStatus.WAITING_LOCAL_ACK.value,
                })
                continue
            results.append(self._deliver(envelope, semantic_minute))
        return results

    def acknowledge_local_delivery(self, event_id: str, semantic_minute: int, *, accepted: bool) -> dict:
        envelope = self.awaiting_local_ack.pop(event_id)
        if not accepted:
            self.statuses[event_id] = DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE
            return {
                "event_id": event_id,
                "receiver_id": envelope.receiver_id,
                "status": DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value,
            }
        return self._deliver(envelope, semantic_minute)

    def _deliver(self, envelope: InformationEnvelope, semantic_minute: int) -> dict:
        if envelope.event_id in self.delivered_event_ids:
            return {
                "event_id": envelope.event_id,
                "receiver_id": envelope.receiver_id,
                "status": DeliveryStatus.DELIVERED.value,
                "duplicate": True,
            }
        claim = transmit_claim(
            self.ledgers[envelope.sender_id],
            self.ledgers[envelope.receiver_id],
            source_claim_id=envelope.source_claim_id,
            new_claim_id=envelope.new_claim_id,
            message_id=envelope.message_id,
            semantic_minute=semantic_minute,
            receiver_trust_in_sender=envelope.receiver_trust_in_sender,
        )
        self.delivered_event_ids.add(envelope.event_id)
        self.statuses[envelope.event_id] = DeliveryStatus.DELIVERED
        return {
            "event_id": envelope.event_id,
            "sender_id": envelope.sender_id,
            "receiver_id": envelope.receiver_id,
            "status": DeliveryStatus.DELIVERED.value,
            "claim_id": claim.claim_id,
            "provenance_root": claim.provenance_root,
        }


def replay_fixture(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    ledgers = {entry["agent_id"]: KnowledgeLedger(entry["agent_id"]) for entry in data["agents"]}
    channels = {
        entry["channel_id"]: CommunicationChannel(
            channel_id=entry["channel_id"],
            kind=entry["kind"],
            latency_minutes=entry["latency_minutes"],
            available=entry.get("available", True),
            requires_local_projection=entry.get("requires_local_projection", False),
        )
        for entry in data["channels"]
    }
    queue = InformationEventQueue(channels=channels, ledgers=ledgers)
    results: list[dict] = []

    for event in data["events"]:
        kind = event["kind"]
        if kind == "observe":
            claim = record_direct_observation(
                ledgers[event["agent_id"]],
                claim_id=event["claim_id"],
                subject=event["subject"],
                value=event["value"],
                semantic_minute=event["semantic_minute"],
                confidence=event["confidence"],
            )
            results.append({"event_id": event["event_id"], "claim_id": claim.claim_id})
        elif kind == "schedule":
            envelope = queue.schedule(
                event_id=event["event_id"],
                message_id=event["message_id"],
                sender_id=event["sender_id"],
                receiver_id=event["receiver_id"],
                source_claim_id=event["source_claim_id"],
                new_claim_id=event["claim_id"],
                channel_id=event["channel_id"],
                created_minute=event["semantic_minute"],
                receiver_trust_in_sender=event.get("receiver_trust_in_sender", 0),
            )
            results.append({"event_id": event["event_id"], "status": DeliveryStatus.QUEUED.value, "delivery_minute": envelope.delivery_minute})
        elif kind == "advance":
            results.append({"event_id": event["event_id"], "deliveries": queue.process_due(event["semantic_minute"])})
        elif kind == "ack":
            results.append(queue.acknowledge_local_delivery(event["target_event_id"], event["semantic_minute"], accepted=event["accepted"]) | {"fixture_event_id": event["event_id"]})
        elif kind == "assess":
            assessment = evaluate_belief(ledgers[event["agent_id"]], event["subject"])
            results.append({
                "event_id": event["event_id"],
                "status": assessment.status.value,
                "preferred_value": assessment.preferred_value,
                "independent_roots_by_value": {key: list(value) for key, value in assessment.independent_roots_by_value.items()},
            })
        else:
            raise ValueError(f"unsupported fixture event kind: {kind}")

    return {"fixture_id": data["fixture_id"], "results": results}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m tools.global_npc_information_network <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
