from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, evaluate_belief, record_direct_observation


@dataclass(frozen=True)
class PublicAudienceMember:
    agent_id: str
    scope_ids: frozenset[str] = frozenset()
    service_ids: frozenset[str] = frozenset()
    topic_ids: frozenset[str] = frozenset()
    receiving_enabled: bool = True


@dataclass(frozen=True)
class PublicPublication:
    publication_id: str
    publisher_id: str
    source_claim_id: str
    service_id: str
    channel_id: str
    published_minute: int
    scope_ids: frozenset[str] = frozenset()
    topic_id: str | None = None
    retention_until_minute: int | None = None
    supersedes_publication_id: str | None = None

    def __post_init__(self) -> None:
        if self.retention_until_minute is not None and self.retention_until_minute < self.published_minute:
            raise ValueError("retention_until_minute cannot precede published_minute")


@dataclass(frozen=True)
class ExpansionResult:
    publication_id: str
    scheduled_agent_ids: tuple[str, ...]
    next_cursor: str | None
    eligible_remaining: int


def _eligible(publication: PublicPublication, member: PublicAudienceMember, semantic_minute: int) -> bool:
    if not member.receiving_enabled:
        return False
    if publication.retention_until_minute is not None and semantic_minute > publication.retention_until_minute:
        return False
    if publication.service_id not in member.service_ids:
        return False
    if publication.scope_ids and not publication.scope_ids.intersection(member.scope_ids):
        return False
    if publication.topic_id is not None and member.topic_ids and publication.topic_id not in member.topic_ids:
        return False
    return True


def resolve_public_audience(
    publication: PublicPublication,
    members: Iterable[PublicAudienceMember],
    *,
    semantic_minute: int,
) -> tuple[str, ...]:
    return tuple(sorted(member.agent_id for member in members if _eligible(publication, member, semantic_minute)))


def expand_publication_bounded(
    *,
    publication: PublicPublication,
    members: Iterable[PublicAudienceMember],
    semantic_minute: int,
    max_receivers: int,
    queue: InformationEventQueue,
    cursor_after_agent_id: str | None = None,
    receiver_trust_in_publisher: Mapping[str, int] | None = None,
) -> ExpansionResult:
    if max_receivers < 0:
        raise ValueError("max_receivers must be non-negative")
    if publication.publisher_id not in queue.ledgers:
        raise KeyError("publisher must have a knowledge ledger")
    if publication.source_claim_id not in queue.ledgers[publication.publisher_id].claims:
        raise KeyError("publisher does not know source claim")
    if publication.channel_id not in queue.channels:
        raise KeyError("publication references unknown channel")

    eligible = list(resolve_public_audience(publication, members, semantic_minute=semantic_minute))
    if cursor_after_agent_id is not None:
        eligible = [agent_id for agent_id in eligible if agent_id > cursor_after_agent_id]

    batch = eligible[:max_receivers]
    trust = receiver_trust_in_publisher or {}
    for receiver_id in batch:
        if receiver_id not in queue.ledgers:
            raise KeyError(f"public audience member has no knowledge ledger: {receiver_id}")
        event_id = f"{publication.publication_id}:receipt:{receiver_id}"
        queue.schedule(
            event_id=event_id,
            message_id=f"{publication.publication_id}:public-message:{receiver_id}",
            sender_id=publication.publisher_id,
            receiver_id=receiver_id,
            source_claim_id=publication.source_claim_id,
            new_claim_id=f"{publication.publication_id}:public-claim:{receiver_id}",
            channel_id=publication.channel_id,
            created_minute=semantic_minute,
            receiver_trust_in_sender=int(trust.get(receiver_id, 0)),
        )

    remaining = max(0, len(eligible) - len(batch))
    next_cursor = batch[-1] if remaining and batch else None
    return ExpansionResult(
        publication_id=publication.publication_id,
        scheduled_agent_ids=tuple(batch),
        next_cursor=next_cursor,
        eligible_remaining=remaining,
    )


def member_from_dict(data: Mapping[str, object]) -> PublicAudienceMember:
    return PublicAudienceMember(
        agent_id=str(data["agent_id"]),
        scope_ids=frozenset(str(v) for v in data.get("scope_ids", [])),
        service_ids=frozenset(str(v) for v in data.get("service_ids", [])),
        topic_ids=frozenset(str(v) for v in data.get("topic_ids", [])),
        receiving_enabled=bool(data.get("receiving_enabled", True)),
    )


def publication_from_dict(data: Mapping[str, object]) -> PublicPublication:
    return PublicPublication(
        publication_id=str(data["publication_id"]),
        publisher_id=str(data["publisher_id"]),
        source_claim_id=str(data["source_claim_id"]),
        service_id=str(data["service_id"]),
        channel_id=str(data["channel_id"]),
        published_minute=int(data["published_minute"]),
        scope_ids=frozenset(str(v) for v in data.get("scope_ids", [])),
        topic_id=str(data["topic_id"]) if data.get("topic_id") is not None else None,
        retention_until_minute=int(data["retention_until_minute"]) if data.get("retention_until_minute") is not None else None,
        supersedes_publication_id=str(data["supersedes_publication_id"]) if data.get("supersedes_publication_id") is not None else None,
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
    queue = InformationEventQueue(channels=channels, ledgers=ledgers)
    publications = {row["publication_id"]: publication_from_dict(row) for row in data["publications"]}
    members = tuple(member_from_dict(row) for row in data["audience_members"])
    cursors: dict[str, str | None] = {}
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
        elif kind == "expand":
            publication = publications[event["publication_id"]]
            result = expand_publication_bounded(
                publication=publication,
                members=members,
                semantic_minute=int(event["semantic_minute"]),
                max_receivers=int(event["max_receivers"]),
                queue=queue,
                cursor_after_agent_id=cursors.get(publication.publication_id),
            )
            cursors[publication.publication_id] = result.next_cursor
            results.append({
                "event_id": event["event_id"],
                "scheduled_agent_ids": list(result.scheduled_agent_ids),
                "next_cursor": result.next_cursor,
                "eligible_remaining": result.eligible_remaining,
            })
        elif kind == "advance":
            results.append({"event_id": event["event_id"], "deliveries": queue.process_due(int(event["semantic_minute"]))})
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
        print("usage: python -m tools.global_npc_publication <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
