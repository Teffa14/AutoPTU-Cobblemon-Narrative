from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable, Mapping

from tools.global_npc_publication import PublicPublication, publication_from_dict


SNAPSHOT_SCHEMA = "OUROS_NPC_PUBLICATION_REVISION_V1"


class RevisionKind(str, Enum):
    ORIGINAL = "ORIGINAL"
    UPDATE = "UPDATE"
    CORRECTION = "CORRECTION"
    RETRACTION = "RETRACTION"


@dataclass(frozen=True)
class PublicationRevision:
    publication: PublicPublication
    kind: RevisionKind
    rationale: str | None = None

    def __post_init__(self) -> None:
        predecessor = self.publication.supersedes_publication_id
        if self.kind is RevisionKind.ORIGINAL and predecessor is not None:
            raise ValueError("ORIGINAL publication cannot supersede another publication")
        if self.kind is not RevisionKind.ORIGINAL and predecessor is None:
            raise ValueError("publication revision requires supersedes_publication_id")


@dataclass(frozen=True)
class ReceivedLineageState:
    root_publication_id: str
    current_publication_id: str
    received_publication_ids: tuple[str, ...]
    latest_received_publication_id: str | None
    latest_received_kind: RevisionKind | None
    current_revision_received: bool


class PublicationRevisionRegistry:
    def __init__(self) -> None:
        self.revisions: dict[str, PublicationRevision] = {}
        self.successor_by_publication_id: dict[str, str] = {}

    def register(self, revision: PublicationRevision) -> None:
        publication = revision.publication
        publication_id = publication.publication_id
        existing = self.revisions.get(publication_id)
        if existing is not None:
            if existing != revision:
                raise ValueError(f"publication_id collision: {publication_id}")
            return

        predecessor_id = publication.supersedes_publication_id
        if predecessor_id is None:
            if revision.kind is not RevisionKind.ORIGINAL:
                raise ValueError("root publication must use ORIGINAL kind")
        else:
            if predecessor_id == publication_id:
                raise ValueError("publication cannot supersede itself")
            predecessor = self.revisions.get(predecessor_id)
            if predecessor is None:
                raise KeyError(f"unknown superseded publication: {predecessor_id}")
            if predecessor_id in self.successor_by_publication_id:
                raise ValueError(f"publication revision fork is not allowed: {predecessor_id}")
            if publication.published_minute < predecessor.publication.published_minute:
                raise ValueError("revision cannot precede superseded publication")
            if publication.publisher_id != predecessor.publication.publisher_id:
                raise ValueError("revision must retain publisher identity")
            if publication.service_id != predecessor.publication.service_id:
                raise ValueError("revision must retain service identity")
            if publication.topic_id != predecessor.publication.topic_id:
                raise ValueError("revision must retain topic identity")

        self.revisions[publication_id] = revision
        if predecessor_id is not None:
            self.successor_by_publication_id[predecessor_id] = publication_id

    def lineage(self, publication_id: str) -> tuple[str, ...]:
        if publication_id not in self.revisions:
            raise KeyError(publication_id)
        chain: list[str] = []
        cursor: str | None = publication_id
        seen: set[str] = set()
        while cursor is not None:
            if cursor in seen:
                raise ValueError("publication revision cycle detected")
            seen.add(cursor)
            chain.append(cursor)
            cursor = self.revisions[cursor].publication.supersedes_publication_id
        chain.reverse()
        return tuple(chain)

    def root_publication_id(self, publication_id: str) -> str:
        return self.lineage(publication_id)[0]

    def current_publication_id(self, publication_id: str) -> str:
        root_id = self.root_publication_id(publication_id)
        cursor = root_id
        seen: set[str] = set()
        while cursor in self.successor_by_publication_id:
            if cursor in seen:
                raise ValueError("publication revision cycle detected")
            seen.add(cursor)
            cursor = self.successor_by_publication_id[cursor]
        return cursor

    def received_state(self, publication_id: str, received_publication_ids: Iterable[str]) -> ReceivedLineageState:
        root_id = self.root_publication_id(publication_id)
        current_id = self.current_publication_id(publication_id)
        full_lineage = self.lineage(current_id)
        received = frozenset(str(value) for value in received_publication_ids)
        received_in_lineage = tuple(value for value in full_lineage if value in received)
        latest_id = received_in_lineage[-1] if received_in_lineage else None
        latest_kind = self.revisions[latest_id].kind if latest_id is not None else None
        return ReceivedLineageState(
            root_publication_id=root_id,
            current_publication_id=current_id,
            received_publication_ids=received_in_lineage,
            latest_received_publication_id=latest_id,
            latest_received_kind=latest_kind,
            current_revision_received=current_id in received,
        )

    def snapshot(self) -> dict:
        rows = []
        for publication_id in sorted(self.revisions):
            revision = self.revisions[publication_id]
            publication = revision.publication
            rows.append({
                "publication": {
                    "publication_id": publication.publication_id,
                    "publisher_id": publication.publisher_id,
                    "source_claim_id": publication.source_claim_id,
                    "service_id": publication.service_id,
                    "channel_id": publication.channel_id,
                    "published_minute": publication.published_minute,
                    "scope_ids": sorted(publication.scope_ids),
                    "topic_id": publication.topic_id,
                    "retention_until_minute": publication.retention_until_minute,
                    "supersedes_publication_id": publication.supersedes_publication_id,
                },
                "kind": revision.kind.value,
                "rationale": revision.rationale,
            })
        return {"schema": SNAPSHOT_SCHEMA, "revisions": rows}

    @classmethod
    def restore(cls, data: Mapping[str, object]) -> "PublicationRevisionRegistry":
        if data.get("schema") != SNAPSHOT_SCHEMA:
            raise ValueError("unsupported publication revision snapshot schema")
        registry = cls()
        pending = list(data.get("revisions", []))
        while pending:
            progress = False
            deferred = []
            for row in pending:
                publication = publication_from_dict(row["publication"])
                revision = PublicationRevision(
                    publication=publication,
                    kind=RevisionKind(str(row["kind"])),
                    rationale=str(row["rationale"]) if row.get("rationale") is not None else None,
                )
                predecessor_id = publication.supersedes_publication_id
                if predecessor_id is not None and predecessor_id not in registry.revisions:
                    deferred.append(row)
                    continue
                registry.register(revision)
                progress = True
            if not progress:
                raise ValueError("snapshot contains unresolved or cyclic publication revision lineage")
            pending = deferred
        return registry


def revision_from_dict(data: Mapping[str, object]) -> PublicationRevision:
    return PublicationRevision(
        publication=publication_from_dict(data),
        kind=RevisionKind(str(data.get("revision_kind", "ORIGINAL"))),
        rationale=str(data["revision_rationale"]) if data.get("revision_rationale") is not None else None,
    )


def replay_fixture(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    registry = PublicationRevisionRegistry()
    received: dict[str, set[str]] = {str(row["agent_id"]): set() for row in data["agents"]}
    results: list[dict] = []

    for event in data["events"]:
        kind = event["kind"]
        if kind == "register":
            revision = revision_from_dict(event["publication"])
            registry.register(revision)
            results.append({"event_id": event["event_id"], "publication_id": revision.publication.publication_id})
        elif kind == "receive":
            agent_id = str(event["agent_id"])
            publication_id = str(event["publication_id"])
            if publication_id not in registry.revisions:
                raise KeyError(publication_id)
            received[agent_id].add(publication_id)
            results.append({"event_id": event["event_id"], "received": sorted(received[agent_id])})
        elif kind == "assess":
            agent_id = str(event["agent_id"])
            state = registry.received_state(str(event["publication_id"]), received[agent_id])
            results.append({
                "event_id": event["event_id"],
                "root_publication_id": state.root_publication_id,
                "current_publication_id": state.current_publication_id,
                "received_publication_ids": list(state.received_publication_ids),
                "latest_received_publication_id": state.latest_received_publication_id,
                "latest_received_kind": state.latest_received_kind.value if state.latest_received_kind else None,
                "current_revision_received": state.current_revision_received,
            })
        elif kind == "restart":
            registry = PublicationRevisionRegistry.restore(registry.snapshot())
            results.append({"event_id": event["event_id"], "revision_count": len(registry.revisions)})
        else:
            raise ValueError(f"unsupported fixture event kind: {kind}")

    return {"fixture_id": data["fixture_id"], "results": results}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m tools.global_npc_publication_revision <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
