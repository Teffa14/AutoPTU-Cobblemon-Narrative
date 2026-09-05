from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from tools.global_npc_audience import (
    AudienceCandidate,
    AudiencePolicy,
    AudienceSelection,
    candidate_from_dict,
    resolve_audience,
)
from tools.global_npc_information_network import (
    CommunicationChannel,
    InformationEventQueue,
)
from tools.global_npc_memory import KnowledgeLedger, evaluate_belief, record_direct_observation
from tools.global_npc_social import FactionMembership, RelationshipState


@dataclass(frozen=True)
class DispatchResult:
    selection: AudienceSelection
    scheduled: tuple[dict, ...]
    unscheduled: tuple[tuple[str, str], ...]


def choose_channel(
    candidate: AudienceCandidate,
    channels: Mapping[str, CommunicationChannel],
) -> CommunicationChannel | None:
    known = [channels[channel_id] for channel_id in candidate.reachable_channel_ids if channel_id in channels]
    if not known:
        return None
    known.sort(key=lambda channel: (not channel.available, channel.latency_minutes, channel.channel_id))
    return known[0]


def dispatch_to_audience(
    *,
    dispatch_id: str,
    sender_id: str,
    source_claim_id: str,
    semantic_minute: int,
    queue: InformationEventQueue,
    candidates: Iterable[AudienceCandidate],
    relationships: Iterable[RelationshipState] = (),
    memberships: Iterable[FactionMembership] = (),
    required_obligation_tag: str | None = None,
    policy: AudiencePolicy = AudiencePolicy(),
    receiver_trust_in_sender: Mapping[str, int] | None = None,
) -> DispatchResult:
    candidate_list = tuple(candidates)
    candidate_by_id = {candidate.agent_id: candidate for candidate in candidate_list}
    selection = resolve_audience(
        sender_id=sender_id,
        candidates=candidate_list,
        relationships=relationships,
        memberships=memberships,
        required_obligation_tag=required_obligation_tag,
        policy=policy,
    )
    trust = receiver_trust_in_sender or {}
    scheduled: list[dict] = []
    unscheduled: list[tuple[str, str]] = []

    for receiver_id in selection.selected_agent_ids:
        candidate = candidate_by_id[receiver_id]
        channel = choose_channel(candidate, queue.channels)
        if channel is None:
            unscheduled.append((receiver_id, "NO_KNOWN_CHANNEL"))
            continue
        event_id = f"{dispatch_id}:delivery:{receiver_id}"
        envelope = queue.schedule(
            event_id=event_id,
            message_id=f"{dispatch_id}:message:{receiver_id}",
            sender_id=sender_id,
            receiver_id=receiver_id,
            source_claim_id=source_claim_id,
            new_claim_id=f"{dispatch_id}:claim:{receiver_id}",
            channel_id=channel.channel_id,
            created_minute=semantic_minute,
            receiver_trust_in_sender=int(trust.get(receiver_id, 0)),
        )
        scheduled.append({
            "receiver_id": receiver_id,
            "event_id": event_id,
            "channel_id": channel.channel_id,
            "delivery_minute": envelope.delivery_minute,
        })

    return DispatchResult(selection, tuple(scheduled), tuple(sorted(unscheduled)))


def _relationship_from_dict(data: Mapping[str, object]) -> RelationshipState:
    return RelationshipState(
        source_agent_id=str(data["source_agent_id"]),
        target_agent_id=str(data["target_agent_id"]),
        affinity=int(data.get("affinity", 0)),
        trust=int(data.get("trust", 0)),
        respect=int(data.get("respect", 0)),
        fear=int(data.get("fear", 0)),
        rivalry=int(data.get("rivalry", 0)),
        debt=int(data.get("debt", 0)),
    )


def _membership_from_dict(data: Mapping[str, object]) -> FactionMembership:
    return FactionMembership(
        agent_id=str(data["agent_id"]),
        faction_id=str(data["faction_id"]),
        role_id=str(data["role_id"]),
        commitment=int(data.get("commitment", 0)),
        standing=int(data.get("standing", 0)),
        active=bool(data.get("active", True)),
        obligation_tags=frozenset(str(v) for v in data.get("obligation_tags", [])),
        permission_tags=frozenset(str(v) for v in data.get("permission_tags", [])),
    )


def replay_fixture(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    ledgers = {row["agent_id"]: KnowledgeLedger(row["agent_id"]) for row in data["agents"]}
    channels = {
        row["channel_id"]: CommunicationChannel(
            channel_id=row["channel_id"],
            kind=row["kind"],
            latency_minutes=int(row["latency_minutes"]),
            available=bool(row.get("available", True)),
            requires_local_projection=bool(row.get("requires_local_projection", False)),
        )
        for row in data["channels"]
    }
    relationships = tuple(_relationship_from_dict(row) for row in data.get("relationships", []))
    memberships = tuple(_membership_from_dict(row) for row in data.get("memberships", []))
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
                semantic_minute=int(event["semantic_minute"]),
                confidence=int(event["confidence"]),
            )
            results.append({"event_id": event["event_id"], "claim_id": claim.claim_id})
        elif kind == "dispatch":
            policy_data = event.get("policy", {})
            result = dispatch_to_audience(
                dispatch_id=event["dispatch_id"],
                sender_id=event["sender_id"],
                source_claim_id=event["source_claim_id"],
                semantic_minute=int(event["semantic_minute"]),
                queue=queue,
                candidates=tuple(candidate_from_dict(row) for row in event["candidates"]),
                relationships=relationships,
                memberships=memberships,
                required_obligation_tag=event.get("required_obligation_tag"),
                policy=AudiencePolicy(
                    max_recipients=int(policy_data.get("max_recipients", 3)),
                    min_score=int(policy_data.get("min_score", 1)),
                    require_reachable_channel=bool(policy_data.get("require_reachable_channel", True)),
                    faction_broadcast_allowed=False,
                ),
                receiver_trust_in_sender={str(k): int(v) for k, v in event.get("receiver_trust_in_sender", {}).items()},
            )
            results.append({
                "event_id": event["event_id"],
                "selected_agent_ids": list(result.selection.selected_agent_ids),
                "scheduled": list(result.scheduled),
                "unscheduled": [list(row) for row in result.unscheduled],
            })
        elif kind == "restart":
            queue = InformationEventQueue.restore(queue.snapshot(), channels=channels, ledgers=ledgers)
            results.append({"event_id": event["event_id"], "status": "RESTORED"})
        elif kind == "advance_budgeted":
            outcome = queue.process_due_budgeted(
                int(event["semantic_minute"]),
                max_events=int(event["max_events"]),
            )
            results.append({"event_id": event["event_id"]} | outcome)
        elif kind == "assess":
            assessment = evaluate_belief(ledgers[event["agent_id"]], event["subject"])
            results.append({
                "event_id": event["event_id"],
                "status": assessment.status.value,
                "preferred_value": assessment.preferred_value,
            })
        else:
            raise ValueError(f"unsupported fixture event kind: {kind}")

    return {"fixture_id": data["fixture_id"], "results": results}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m tools.global_npc_communication_runtime <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
