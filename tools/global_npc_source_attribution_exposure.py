from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

from tools.global_npc_deception import DeceptionKind, DeceptiveStatement, SourceAttributionStore
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_social import RelationshipState, apply_relationship_event

SOURCE_EXPOSURE_SNAPSHOT_SCHEMA = "OUROS_NPC_SOURCE_ATTRIBUTION_EXPOSURE_V1"


class SourceVerificationKind(str, Enum):
    NAMED_SOURCE_DENIAL = "NAMED_SOURCE_DENIAL"
    AUTHORSHIP_RECORD = "AUTHORSHIP_RECORD"
    SPEAKER_ADMISSION = "SPEAKER_ADMISSION"


class SourceExposureStatus(str, Enum):
    SOURCE_DISPUTED = "SOURCE_DISPUTED"
    FALSE_ATTRIBUTION_CORROBORATED = "FALSE_ATTRIBUTION_CORROBORATED"
    INTENT_ATTRIBUTED = "INTENT_ATTRIBUTED"


@dataclass(frozen=True)
class SourceVerificationEvidence:
    claim_id: str
    kind: SourceVerificationKind
    alleged_source_agent_id: str
    actual_source_agent_id: str | None = None


@dataclass(frozen=True)
class SourceAttributionExposureFinding:
    finding_id: str
    discoverer_id: str
    speaker_id: str
    statement_id: str
    deceptive_claim_id: str
    alleged_source_agent_id: str
    evidence_claim_ids: tuple[str, ...]
    semantic_minute: int
    status: SourceExposureStatus

    def to_snapshot(self) -> dict:
        return {
            "finding_id": self.finding_id,
            "discoverer_id": self.discoverer_id,
            "speaker_id": self.speaker_id,
            "statement_id": self.statement_id,
            "deceptive_claim_id": self.deceptive_claim_id,
            "alleged_source_agent_id": self.alleged_source_agent_id,
            "evidence_claim_ids": list(self.evidence_claim_ids),
            "semantic_minute": self.semantic_minute,
            "status": self.status.value,
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "SourceAttributionExposureFinding":
        return cls(
            finding_id=str(raw["finding_id"]),
            discoverer_id=str(raw["discoverer_id"]),
            speaker_id=str(raw["speaker_id"]),
            statement_id=str(raw["statement_id"]),
            deceptive_claim_id=str(raw["deceptive_claim_id"]),
            alleged_source_agent_id=str(raw["alleged_source_agent_id"]),
            evidence_claim_ids=tuple(str(v) for v in raw.get("evidence_claim_ids", [])),
            semantic_minute=int(raw["semantic_minute"]),
            status=SourceExposureStatus(str(raw["status"])),
        )


@dataclass
class SourceAttributionExposureRegistry:
    findings: dict[str, SourceAttributionExposureFinding] = field(default_factory=dict)

    def add(self, finding: SourceAttributionExposureFinding) -> None:
        existing = self.findings.get(finding.finding_id)
        if existing is not None and existing != finding:
            raise ValueError(f"finding_id collision: {finding.finding_id}")
        self.findings[finding.finding_id] = finding

    def snapshot(self) -> dict:
        return {
            "schema": SOURCE_EXPOSURE_SNAPSHOT_SCHEMA,
            "findings": [self.findings[key].to_snapshot() for key in sorted(self.findings)],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "SourceAttributionExposureRegistry":
        if snapshot.get("schema") != SOURCE_EXPOSURE_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported source attribution exposure snapshot schema")
        registry = cls()
        for raw in snapshot.get("findings", []):
            if not isinstance(raw, Mapping):
                raise ValueError("source attribution exposure row must be a mapping")
            registry.add(SourceAttributionExposureFinding.from_snapshot(raw))
        return registry


def assess_false_source_exposure(
    discoverer: KnowledgeLedger,
    attribution_store: SourceAttributionStore,
    *,
    finding_id: str,
    statement: DeceptiveStatement,
    deceptive_claim_id: str,
    evidence: tuple[SourceVerificationEvidence, ...],
    semantic_minute: int,
    minimum_evidence_confidence: int = 60,
) -> SourceAttributionExposureFinding:
    if statement.kind not in (DeceptionKind.FALSE_SOURCE, DeceptionKind.FALSE_CONTENT_AND_SOURCE):
        raise ValueError("source exposure requires a false-source statement")
    if statement.declared_source_agent_id is None:
        raise ValueError("false-source statement requires a declared source")
    deceptive = discoverer.claims[deceptive_claim_id]
    if deceptive.provenance_root != f"deception:{statement.statement_id}":
        raise ValueError("deceptive claim does not belong to statement")
    if deceptive.source_agent_id != statement.speaker_id:
        raise ValueError("deceptive claim immediate source does not match speaker")
    if semantic_minute < max(deceptive.semantic_minute, statement.semantic_minute):
        raise ValueError("source exposure cannot precede the statement or received claim")

    records = tuple(
        record for record in attribution_store.for_claim(discoverer.agent_id, deceptive_claim_id)
        if record.statement_id == statement.statement_id
    )
    if not records:
        raise ValueError("discoverer has no source-attribution record for statement")
    presented = records[-1]
    if presented.actual_source_agent_id != statement.speaker_id:
        raise ValueError("attribution record actual source does not match speaker")
    if presented.perceived_source_agent_id != statement.declared_source_agent_id:
        raise ValueError("attribution record does not match declared source")

    if not evidence:
        raise ValueError("source exposure requires verification evidence")

    roots: set[str] = set()
    ordered_ids: list[str] = []
    has_denial = False
    has_record = False
    has_admission = False
    for ref in sorted(evidence, key=lambda item: (item.claim_id, item.kind.value)):
        claim = discoverer.claims[ref.claim_id]
        if claim.semantic_minute > semantic_minute:
            raise ValueError("source verification evidence cannot come from the future")
        if claim.confidence < minimum_evidence_confidence:
            raise ValueError("source verification evidence below threshold")
        if ref.alleged_source_agent_id != statement.declared_source_agent_id:
            raise ValueError("source verification evidence targets a different alleged source")
        if claim.provenance_root == deceptive.provenance_root:
            raise ValueError("deception-root echo cannot verify source attribution")
        if claim.provenance_root in roots:
            continue
        roots.add(claim.provenance_root)
        ordered_ids.append(ref.claim_id)
        if ref.kind is SourceVerificationKind.NAMED_SOURCE_DENIAL:
            if claim.source_agent_id != statement.declared_source_agent_id:
                raise ValueError("named-source denial must come from the named source")
            has_denial = True
        elif ref.kind is SourceVerificationKind.AUTHORSHIP_RECORD:
            if ref.actual_source_agent_id is None or ref.actual_source_agent_id == statement.declared_source_agent_id:
                raise ValueError("authorship record must identify a different source")
            has_record = True
        elif ref.kind is SourceVerificationKind.SPEAKER_ADMISSION:
            if claim.source_agent_id != statement.speaker_id:
                raise ValueError("speaker admission must come from the speaker")
            if ref.actual_source_agent_id != statement.speaker_id:
                raise ValueError("speaker admission must identify the speaker as actual source")
            has_admission = True

    if not ordered_ids:
        raise ValueError("no independent source verification evidence remains")
    if has_admission:
        status = SourceExposureStatus.INTENT_ATTRIBUTED
    elif has_record:
        status = SourceExposureStatus.FALSE_ATTRIBUTION_CORROBORATED
    elif has_denial:
        status = SourceExposureStatus.SOURCE_DISPUTED
    else:
        raise ValueError("unsupported source verification evidence")

    return SourceAttributionExposureFinding(
        finding_id=finding_id,
        discoverer_id=discoverer.agent_id,
        speaker_id=statement.speaker_id,
        statement_id=statement.statement_id,
        deceptive_claim_id=deceptive_claim_id,
        alleged_source_agent_id=statement.declared_source_agent_id,
        evidence_claim_ids=tuple(ordered_ids),
        semantic_minute=semantic_minute,
        status=status,
    )


def apply_false_source_trust_consequence(
    relationship: RelationshipState,
    finding: SourceAttributionExposureFinding,
    *,
    trust_delta: int = -15,
) -> RelationshipState:
    if finding.status is not SourceExposureStatus.INTENT_ATTRIBUTED:
        raise ValueError("trust consequence requires attributed false-source intent")
    if relationship.source_agent_id != finding.discoverer_id or relationship.target_agent_id != finding.speaker_id:
        raise ValueError("relationship direction must be discoverer -> speaker")
    if trust_delta >= 0:
        raise ValueError("false-source discovery trust delta must be negative")
    provenance_ref = f"source-attribution-exposure:{finding.finding_id}"
    if provenance_ref in relationship.provenance_refs:
        return relationship
    return apply_relationship_event(
        relationship,
        provenance_ref=provenance_ref,
        semantic_minute=finding.semantic_minute,
        trust_delta=trust_delta,
    )
