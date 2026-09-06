from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind, clamp


ATTRIBUTION_SNAPSHOT_SCHEMA = "OUROS_NPC_SOURCE_ATTRIBUTION_V1"


class DeceptionKind(str, Enum):
    FALSE_CONTENT = "FALSE_CONTENT"
    FALSE_SOURCE = "FALSE_SOURCE"
    FALSE_CONTENT_AND_SOURCE = "FALSE_CONTENT_AND_SOURCE"


class AttributionKind(str, Enum):
    SPEAKER_DECLARATION = "SPEAKER_DECLARATION"
    MEMORY_CONFUSION = "MEMORY_CONFUSION"


@dataclass(frozen=True)
class DeceptiveStatement:
    statement_id: str
    speaker_id: str
    basis_claim_id: str
    subject: str
    basis_value: str
    asserted_value: str
    basis_source_agent_id: str | None
    declared_source_agent_id: str | None
    semantic_minute: int
    kind: DeceptionKind


@dataclass(frozen=True)
class SourceAttributionRecord:
    attribution_id: str
    agent_id: str
    claim_id: str
    actual_source_agent_id: str | None
    perceived_source_agent_id: str | None
    semantic_minute: int
    kind: AttributionKind
    statement_id: str | None = None

    def to_snapshot(self) -> dict:
        return {
            "attribution_id": self.attribution_id,
            "agent_id": self.agent_id,
            "claim_id": self.claim_id,
            "actual_source_agent_id": self.actual_source_agent_id,
            "perceived_source_agent_id": self.perceived_source_agent_id,
            "semantic_minute": self.semantic_minute,
            "kind": self.kind.value,
            "statement_id": self.statement_id,
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "SourceAttributionRecord":
        return cls(
            attribution_id=str(raw["attribution_id"]),
            agent_id=str(raw["agent_id"]),
            claim_id=str(raw["claim_id"]),
            actual_source_agent_id=None if raw.get("actual_source_agent_id") is None else str(raw["actual_source_agent_id"]),
            perceived_source_agent_id=None if raw.get("perceived_source_agent_id") is None else str(raw["perceived_source_agent_id"]),
            semantic_minute=int(raw["semantic_minute"]),
            kind=AttributionKind(str(raw["kind"])),
            statement_id=None if raw.get("statement_id") is None else str(raw["statement_id"]),
        )


@dataclass
class SourceAttributionStore:
    records: dict[str, SourceAttributionRecord] = field(default_factory=dict)

    def add(self, record: SourceAttributionRecord) -> None:
        existing = self.records.get(record.attribution_id)
        if existing is not None and existing != record:
            raise ValueError(f"attribution_id collision: {record.attribution_id}")
        self.records[record.attribution_id] = record

    def for_claim(self, agent_id: str, claim_id: str) -> tuple[SourceAttributionRecord, ...]:
        return tuple(sorted(
            (
                record
                for record in self.records.values()
                if record.agent_id == agent_id and record.claim_id == claim_id
            ),
            key=lambda record: (record.semantic_minute, record.attribution_id),
        ))

    def snapshot(self) -> dict:
        return {
            "schema": ATTRIBUTION_SNAPSHOT_SCHEMA,
            "records": [self.records[key].to_snapshot() for key in sorted(self.records)],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "SourceAttributionStore":
        if snapshot.get("schema") != ATTRIBUTION_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported source attribution snapshot schema")
        rows = snapshot.get("records", [])
        if not isinstance(rows, list):
            raise ValueError("source attribution records must be a list")
        store = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("source attribution row must be a mapping")
            store.add(SourceAttributionRecord.from_snapshot(raw))
        return store


def author_deceptive_statement(
    speaker: KnowledgeLedger,
    *,
    statement_id: str,
    basis_claim_id: str,
    asserted_value: str,
    semantic_minute: int,
    declared_source_agent_id: str | None = None,
) -> DeceptiveStatement:
    if not statement_id:
        raise ValueError("statement_id is required")
    basis = speaker.claims[basis_claim_id]
    if semantic_minute < basis.semantic_minute:
        raise ValueError("statement cannot precede its basis claim")

    false_content = asserted_value != basis.value
    false_source = (
        declared_source_agent_id is not None
        and declared_source_agent_id != basis.source_agent_id
    )
    if not false_content and not false_source:
        raise ValueError("deceptive statement must alter content, source attribution, or both")

    if false_content and false_source:
        kind = DeceptionKind.FALSE_CONTENT_AND_SOURCE
    elif false_content:
        kind = DeceptionKind.FALSE_CONTENT
    else:
        kind = DeceptionKind.FALSE_SOURCE

    return DeceptiveStatement(
        statement_id=statement_id,
        speaker_id=speaker.agent_id,
        basis_claim_id=basis.claim_id,
        subject=basis.subject,
        basis_value=basis.value,
        asserted_value=asserted_value,
        basis_source_agent_id=basis.source_agent_id,
        declared_source_agent_id=declared_source_agent_id,
        semantic_minute=semantic_minute,
        kind=kind,
    )


def materialize_deceptive_report(
    receiver: KnowledgeLedger,
    attribution_store: SourceAttributionStore,
    *,
    statement: DeceptiveStatement,
    claim_id: str,
    message_id: str,
    semantic_minute: int,
    confidence: int,
) -> Claim:
    if semantic_minute < statement.semantic_minute:
        raise ValueError("report cannot arrive before the statement")
    claim = Claim(
        claim_id=claim_id,
        subject=statement.subject,
        value=statement.asserted_value,
        source_kind=SourceKind.REPORT,
        source_agent_id=statement.speaker_id,
        semantic_minute=semantic_minute,
        confidence=clamp(confidence),
        provenance_root=f"deception:{statement.statement_id}",
        parent_claim_id=statement.basis_claim_id,
        message_id=message_id,
    )
    receiver.add(claim)

    if statement.declared_source_agent_id is not None:
        attribution_store.add(SourceAttributionRecord(
            attribution_id=f"statement:{statement.statement_id}:{receiver.agent_id}:{claim_id}",
            agent_id=receiver.agent_id,
            claim_id=claim_id,
            actual_source_agent_id=statement.speaker_id,
            perceived_source_agent_id=statement.declared_source_agent_id,
            semantic_minute=semantic_minute,
            kind=AttributionKind.SPEAKER_DECLARATION,
            statement_id=statement.statement_id,
        ))
    return claim


def record_source_confusion(
    ledger: KnowledgeLedger,
    attribution_store: SourceAttributionStore,
    *,
    attribution_id: str,
    claim_id: str,
    perceived_source_agent_id: str | None,
    semantic_minute: int,
) -> SourceAttributionRecord:
    claim = ledger.claims[claim_id]
    if semantic_minute < claim.semantic_minute:
        raise ValueError("source confusion cannot precede the claim")
    if perceived_source_agent_id == claim.source_agent_id:
        raise ValueError("source confusion must differ from the actual immediate source")
    record = SourceAttributionRecord(
        attribution_id=attribution_id,
        agent_id=ledger.agent_id,
        claim_id=claim_id,
        actual_source_agent_id=claim.source_agent_id,
        perceived_source_agent_id=perceived_source_agent_id,
        semantic_minute=semantic_minute,
        kind=AttributionKind.MEMORY_CONFUSION,
    )
    attribution_store.add(record)
    return record


def perceived_source(
    ledger: KnowledgeLedger,
    attribution_store: SourceAttributionStore,
    claim_id: str,
) -> str | None:
    claim = ledger.claims[claim_id]
    records = attribution_store.for_claim(ledger.agent_id, claim_id)
    if not records:
        return claim.source_agent_id
    return records[-1].perceived_source_agent_id
