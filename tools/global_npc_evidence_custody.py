from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

from tools.global_npc_memory import KnowledgeLedger


EVIDENCE_CUSTODY_SNAPSHOT_SCHEMA = "OUROS_NPC_EVIDENCE_CUSTODY_V1"


class CustodyAction(str, Enum):
    COLLECTED = "COLLECTED"
    TRANSFERRED = "TRANSFERRED"
    STORED = "STORED"
    EXAMINED = "EXAMINED"
    RELEASED = "RELEASED"


class CustodyIntegrityStatus(str, Enum):
    UNASSESSED = "UNASSESSED"
    CONTINUITY_SUPPORTED = "CONTINUITY_SUPPORTED"
    DOCUMENTATION_GAP = "DOCUMENTATION_GAP"
    RECORD_CONFLICT = "RECORD_CONFLICT"
    COMPROMISE_CORROBORATED = "COMPROMISE_CORROBORATED"


@dataclass(frozen=True)
class PhysicalEvidenceArtifact:
    evidence_id: str
    subject_ref: str
    created_semantic_minute: int
    provenance_ref: str

    def __post_init__(self) -> None:
        if not self.evidence_id or not self.subject_ref or not self.provenance_ref:
            raise ValueError("evidence artifact identity and provenance are required")
        if self.created_semantic_minute < 0:
            raise ValueError("evidence artifact time cannot be negative")


@dataclass(frozen=True)
class CustodyRecord:
    record_id: str
    evidence_id: str
    action: CustodyAction
    holder_id: str
    semantic_minute: int
    documentation_claim_id: str
    previous_record_id: str | None = None

    def __post_init__(self) -> None:
        if not self.record_id or not self.evidence_id or not self.holder_id or not self.documentation_claim_id:
            raise ValueError("custody record identity, holder and documentation are required")
        if self.semantic_minute < 0:
            raise ValueError("custody record time cannot be negative")

    def to_snapshot(self) -> dict:
        return {
            "record_id": self.record_id,
            "evidence_id": self.evidence_id,
            "action": self.action.value,
            "holder_id": self.holder_id,
            "semantic_minute": self.semantic_minute,
            "documentation_claim_id": self.documentation_claim_id,
            "previous_record_id": self.previous_record_id,
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "CustodyRecord":
        return cls(
            record_id=str(raw["record_id"]),
            evidence_id=str(raw["evidence_id"]),
            action=CustodyAction(str(raw["action"])),
            holder_id=str(raw["holder_id"]),
            semantic_minute=int(raw["semantic_minute"]),
            documentation_claim_id=str(raw["documentation_claim_id"]),
            previous_record_id=None if raw.get("previous_record_id") is None else str(raw["previous_record_id"]),
        )


@dataclass(frozen=True)
class CustodyAssessment:
    assessment_id: str
    investigator_id: str
    evidence_id: str
    semantic_minute: int
    status: CustodyIntegrityStatus
    known_record_ids: tuple[str, ...]
    support_claim_ids: tuple[str, ...]
    compromise_claim_ids: tuple[str, ...] = ()

    def to_snapshot(self) -> dict:
        return {
            "assessment_id": self.assessment_id,
            "investigator_id": self.investigator_id,
            "evidence_id": self.evidence_id,
            "semantic_minute": self.semantic_minute,
            "status": self.status.value,
            "known_record_ids": list(self.known_record_ids),
            "support_claim_ids": list(self.support_claim_ids),
            "compromise_claim_ids": list(self.compromise_claim_ids),
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "CustodyAssessment":
        return cls(
            assessment_id=str(raw["assessment_id"]),
            investigator_id=str(raw["investigator_id"]),
            evidence_id=str(raw["evidence_id"]),
            semantic_minute=int(raw["semantic_minute"]),
            status=CustodyIntegrityStatus(str(raw["status"])),
            known_record_ids=tuple(str(value) for value in raw.get("known_record_ids", [])),
            support_claim_ids=tuple(str(value) for value in raw.get("support_claim_ids", [])),
            compromise_claim_ids=tuple(str(value) for value in raw.get("compromise_claim_ids", [])),
        )


@dataclass
class EvidenceCustodyRegistry:
    records: dict[str, CustodyRecord] = field(default_factory=dict)
    assessments: dict[str, CustodyAssessment] = field(default_factory=dict)

    def add_record(self, record: CustodyRecord) -> None:
        existing = self.records.get(record.record_id)
        if existing is not None and existing != record:
            raise ValueError(f"custody record_id collision: {record.record_id}")
        self.records[record.record_id] = record

    def add_assessment(self, assessment: CustodyAssessment) -> None:
        existing = self.assessments.get(assessment.assessment_id)
        if existing is not None and existing != assessment:
            raise ValueError(f"custody assessment_id collision: {assessment.assessment_id}")
        self.assessments[assessment.assessment_id] = assessment

    def snapshot(self) -> dict:
        return {
            "schema": EVIDENCE_CUSTODY_SNAPSHOT_SCHEMA,
            "records": [self.records[key].to_snapshot() for key in sorted(self.records)],
            "assessments": [self.assessments[key].to_snapshot() for key in sorted(self.assessments)],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "EvidenceCustodyRegistry":
        if snapshot.get("schema") != EVIDENCE_CUSTODY_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported evidence custody snapshot schema")
        registry = cls()
        for raw in snapshot.get("records", []):
            if not isinstance(raw, Mapping):
                raise ValueError("custody record row must be a mapping")
            registry.add_record(CustodyRecord.from_snapshot(raw))
        for raw in snapshot.get("assessments", []):
            if not isinstance(raw, Mapping):
                raise ValueError("custody assessment row must be a mapping")
            registry.add_assessment(CustodyAssessment.from_snapshot(raw))
        return registry


def assess_evidence_custody(
    investigator: KnowledgeLedger,
    artifact: PhysicalEvidenceArtifact,
    registry: EvidenceCustodyRegistry,
    *,
    assessment_id: str,
    known_record_ids: tuple[str, ...],
    compromise_claim_ids: tuple[str, ...] = (),
    semantic_minute: int,
    minimum_confidence: int = 60,
) -> CustodyAssessment:
    """Assess handling continuity from records the investigator actually possesses.

    A missing handoff creates a documentation gap, not proof of tampering. A conflicting
    record creates a record conflict, not sabotage intent. Compromise requires independent,
    provenance-backed evidence. Custody continuity also does not prove that the artifact's
    substantive interpretation is correct.
    """
    if semantic_minute < artifact.created_semantic_minute:
        raise ValueError("custody assessment cannot precede evidence creation")

    records: list[CustodyRecord] = []
    support_claim_ids: list[str] = []
    roots: set[str] = set()
    for record_id in sorted(set(known_record_ids)):
        record = registry.records[record_id]
        if record.evidence_id != artifact.evidence_id:
            raise ValueError("custody record targets a different evidence artifact")
        claim = investigator.claims[record.documentation_claim_id]
        if claim.semantic_minute > semantic_minute or record.semantic_minute > semantic_minute:
            raise ValueError("custody evidence cannot come from the future")
        if claim.confidence < minimum_confidence:
            raise ValueError("custody documentation below threshold")
        if claim.provenance_root in roots:
            continue
        roots.add(claim.provenance_root)
        records.append(record)
        support_claim_ids.append(claim.claim_id)

    compromise_ids: list[str] = []
    compromise_roots: set[str] = set()
    for claim_id in sorted(set(compromise_claim_ids)):
        claim = investigator.claims[claim_id]
        if claim.semantic_minute > semantic_minute:
            raise ValueError("compromise evidence cannot come from the future")
        if claim.confidence < minimum_confidence:
            raise ValueError("compromise evidence below threshold")
        if claim.provenance_root in roots or claim.provenance_root in compromise_roots:
            continue
        compromise_roots.add(claim.provenance_root)
        compromise_ids.append(claim_id)

    status = CustodyIntegrityStatus.UNASSESSED
    if compromise_ids:
        status = CustodyIntegrityStatus.COMPROMISE_CORROBORATED
    elif records:
        by_previous: dict[str | None, set[str]] = {}
        for record in records:
            by_previous.setdefault(record.previous_record_id, set()).add(record.record_id)
        if any(len(children) > 1 for children in by_previous.values()):
            status = CustodyIntegrityStatus.RECORD_CONFLICT
        else:
            known_ids = {record.record_id for record in records}
            gap = any(record.previous_record_id is not None and record.previous_record_id not in known_ids for record in records)
            if gap:
                status = CustodyIntegrityStatus.DOCUMENTATION_GAP
            else:
                ordered = sorted(records, key=lambda row: (row.semantic_minute, row.record_id))
                if ordered[0].previous_record_id is not None:
                    status = CustodyIntegrityStatus.DOCUMENTATION_GAP
                else:
                    previous_id: str | None = None
                    previous_minute = artifact.created_semantic_minute
                    continuous = True
                    for record in ordered:
                        if record.previous_record_id != previous_id or record.semantic_minute < previous_minute:
                            continuous = False
                            break
                        previous_id = record.record_id
                        previous_minute = record.semantic_minute
                    status = CustodyIntegrityStatus.CONTINUITY_SUPPORTED if continuous else CustodyIntegrityStatus.RECORD_CONFLICT

    assessment = CustodyAssessment(
        assessment_id=assessment_id,
        investigator_id=investigator.agent_id,
        evidence_id=artifact.evidence_id,
        semantic_minute=semantic_minute,
        status=status,
        known_record_ids=tuple(record.record_id for record in records),
        support_claim_ids=tuple(support_claim_ids),
        compromise_claim_ids=tuple(compromise_ids),
    )
    registry.add_assessment(assessment)
    return assessment
