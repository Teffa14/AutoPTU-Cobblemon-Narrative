from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

from tools.global_npc_deception import DeceptiveStatement
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_social import RelationshipState, apply_relationship_event


EXPOSURE_SNAPSHOT_SCHEMA = "OUROS_NPC_DECEPTION_EXPOSURE_V1"


class ExposureStatus(str, Enum):
    FALSEHOOD_CORROBORATED = "FALSEHOOD_CORROBORATED"
    INTENT_ATTRIBUTED = "INTENT_ATTRIBUTED"


@dataclass(frozen=True)
class DeceptionExposureFinding:
    finding_id: str
    discoverer_id: str
    speaker_id: str
    statement_id: str
    deceptive_claim_id: str
    contradiction_claim_id: str
    intent_evidence_claim_ids: tuple[str, ...]
    semantic_minute: int
    status: ExposureStatus

    def to_snapshot(self) -> dict:
        return {
            "finding_id": self.finding_id,
            "discoverer_id": self.discoverer_id,
            "speaker_id": self.speaker_id,
            "statement_id": self.statement_id,
            "deceptive_claim_id": self.deceptive_claim_id,
            "contradiction_claim_id": self.contradiction_claim_id,
            "intent_evidence_claim_ids": list(self.intent_evidence_claim_ids),
            "semantic_minute": self.semantic_minute,
            "status": self.status.value,
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "DeceptionExposureFinding":
        return cls(
            finding_id=str(raw["finding_id"]),
            discoverer_id=str(raw["discoverer_id"]),
            speaker_id=str(raw["speaker_id"]),
            statement_id=str(raw["statement_id"]),
            deceptive_claim_id=str(raw["deceptive_claim_id"]),
            contradiction_claim_id=str(raw["contradiction_claim_id"]),
            intent_evidence_claim_ids=tuple(str(v) for v in raw.get("intent_evidence_claim_ids", [])),
            semantic_minute=int(raw["semantic_minute"]),
            status=ExposureStatus(str(raw["status"])),
        )


@dataclass
class DeceptionExposureRegistry:
    findings: dict[str, DeceptionExposureFinding] = field(default_factory=dict)

    def add(self, finding: DeceptionExposureFinding) -> None:
        existing = self.findings.get(finding.finding_id)
        if existing is not None and existing != finding:
            raise ValueError(f"finding_id collision: {finding.finding_id}")
        self.findings[finding.finding_id] = finding

    def snapshot(self) -> dict:
        return {
            "schema": EXPOSURE_SNAPSHOT_SCHEMA,
            "findings": [self.findings[key].to_snapshot() for key in sorted(self.findings)],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "DeceptionExposureRegistry":
        if snapshot.get("schema") != EXPOSURE_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported deception exposure snapshot schema")
        registry = cls()
        for raw in snapshot.get("findings", []):
            if not isinstance(raw, Mapping):
                raise ValueError("deception exposure row must be a mapping")
            registry.add(DeceptionExposureFinding.from_snapshot(raw))
        return registry


def assess_false_content_exposure(
    discoverer: KnowledgeLedger,
    *,
    finding_id: str,
    statement: DeceptiveStatement,
    deceptive_claim_id: str,
    contradiction_claim_id: str,
    semantic_minute: int,
    intent_evidence_claim_ids: tuple[str, ...] = (),
    minimum_contradiction_confidence: int = 60,
) -> DeceptionExposureFinding:
    deceptive = discoverer.claims[deceptive_claim_id]
    contradiction = discoverer.claims[contradiction_claim_id]
    if statement.asserted_value == statement.basis_value:
        raise ValueError("false-content exposure requires a false-content statement")
    if deceptive.provenance_root != f"deception:{statement.statement_id}":
        raise ValueError("deceptive claim does not belong to statement")
    if deceptive.source_agent_id != statement.speaker_id:
        raise ValueError("deceptive claim immediate source does not match speaker")
    if deceptive.subject != statement.subject or deceptive.value != statement.asserted_value:
        raise ValueError("deceptive claim content does not match statement")
    if contradiction.subject != statement.subject or contradiction.value == statement.asserted_value:
        raise ValueError("contradiction must concern the same subject and disagree with the assertion")
    if contradiction.provenance_root == deceptive.provenance_root:
        raise ValueError("same-root evidence cannot corroborate a contradiction")
    if contradiction.confidence < minimum_contradiction_confidence:
        raise ValueError("contradiction confidence below exposure threshold")
    if semantic_minute < max(deceptive.semantic_minute, contradiction.semantic_minute, statement.semantic_minute):
        raise ValueError("exposure cannot precede its evidence")

    ordered_intent_ids = tuple(sorted(set(intent_evidence_claim_ids)))
    for claim_id in ordered_intent_ids:
        evidence = discoverer.claims[claim_id]
        if evidence.semantic_minute > semantic_minute:
            raise ValueError("intent evidence cannot come from the future")

    status = ExposureStatus.INTENT_ATTRIBUTED if ordered_intent_ids else ExposureStatus.FALSEHOOD_CORROBORATED
    return DeceptionExposureFinding(
        finding_id=finding_id,
        discoverer_id=discoverer.agent_id,
        speaker_id=statement.speaker_id,
        statement_id=statement.statement_id,
        deceptive_claim_id=deceptive_claim_id,
        contradiction_claim_id=contradiction_claim_id,
        intent_evidence_claim_ids=ordered_intent_ids,
        semantic_minute=semantic_minute,
        status=status,
    )


def apply_deception_trust_consequence(
    relationship: RelationshipState,
    finding: DeceptionExposureFinding,
    *,
    trust_delta: int = -20,
) -> RelationshipState:
    if finding.status != ExposureStatus.INTENT_ATTRIBUTED:
        raise ValueError("trust consequence requires attributed deceptive intent")
    if relationship.source_agent_id != finding.discoverer_id or relationship.target_agent_id != finding.speaker_id:
        raise ValueError("relationship direction must be discoverer -> speaker")
    if trust_delta >= 0:
        raise ValueError("deception discovery trust delta must be negative")
    provenance_ref = f"deception-exposure:{finding.finding_id}"
    if provenance_ref in relationship.provenance_refs:
        return relationship
    return apply_relationship_event(
        relationship,
        provenance_ref=provenance_ref,
        semantic_minute=finding.semantic_minute,
        trust_delta=trust_delta,
    )
