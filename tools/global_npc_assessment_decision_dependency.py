from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

from tools.global_npc_evidence_custody import EvidenceCustodyRegistry
from tools.global_npc_memory import KnowledgeLedger


DECISION_DEPENDENCY_SNAPSHOT_SCHEMA = "OUROS_NPC_ASSESSMENT_DECISION_DEPENDENCY_V1"


class DecisionReviewStatus(str, Enum):
    BASIS_CURRENT = "BASIS_CURRENT"
    SUPERSEDED_NOT_RECEIVED = "SUPERSEDED_NOT_RECEIVED"
    REVIEW_ELIGIBLE = "REVIEW_ELIGIBLE"


@dataclass(frozen=True)
class AssessmentDependentDecision:
    decision_id: str
    actor_id: str
    basis_assessment_id: str
    basis_claim_id: str
    decision_kind: str
    subject_ref: str
    semantic_minute: int

    def __post_init__(self) -> None:
        if not self.decision_id or not self.actor_id or not self.basis_assessment_id:
            raise ValueError("decision identity, actor and basis assessment are required")
        if not self.basis_claim_id or not self.decision_kind or not self.subject_ref:
            raise ValueError("decision basis claim, kind and subject are required")
        if self.semantic_minute < 0:
            raise ValueError("decision time cannot be negative")

    def to_snapshot(self) -> dict:
        return {
            "decision_id": self.decision_id,
            "actor_id": self.actor_id,
            "basis_assessment_id": self.basis_assessment_id,
            "basis_claim_id": self.basis_claim_id,
            "decision_kind": self.decision_kind,
            "subject_ref": self.subject_ref,
            "semantic_minute": self.semantic_minute,
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "AssessmentDependentDecision":
        return cls(
            decision_id=str(raw["decision_id"]),
            actor_id=str(raw["actor_id"]),
            basis_assessment_id=str(raw["basis_assessment_id"]),
            basis_claim_id=str(raw["basis_claim_id"]),
            decision_kind=str(raw["decision_kind"]),
            subject_ref=str(raw["subject_ref"]),
            semantic_minute=int(raw["semantic_minute"]),
        )


@dataclass
class AssessmentDecisionDependencyRegistry:
    decisions: dict[str, AssessmentDependentDecision] = field(default_factory=dict)

    def add(self, decision: AssessmentDependentDecision) -> None:
        existing = self.decisions.get(decision.decision_id)
        if existing is not None:
            if existing != decision:
                raise ValueError(f"assessment-dependent decision collision: {decision.decision_id}")
            return
        self.decisions[decision.decision_id] = decision

    def snapshot(self) -> dict:
        return {
            "schema": DECISION_DEPENDENCY_SNAPSHOT_SCHEMA,
            "decisions": [self.decisions[key].to_snapshot() for key in sorted(self.decisions)],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "AssessmentDecisionDependencyRegistry":
        if snapshot.get("schema") != DECISION_DEPENDENCY_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported assessment decision dependency snapshot schema")
        registry = cls()
        for raw in snapshot.get("decisions", []):
            if not isinstance(raw, Mapping):
                raise ValueError("assessment-dependent decision row must be a mapping")
            registry.add(AssessmentDependentDecision.from_snapshot(raw))
        return registry


def record_assessment_dependent_decision(
    registry: AssessmentDecisionDependencyRegistry,
    custody: EvidenceCustodyRegistry,
    actor: KnowledgeLedger,
    *,
    decision_id: str,
    basis_assessment_id: str,
    basis_claim_id: str,
    decision_kind: str,
    subject_ref: str,
    semantic_minute: int,
) -> AssessmentDependentDecision:
    """Record a consequential world decision against the assessment actually known then.

    Recording provenance does not judge whether the decision was reasonable and does not
    execute, reverse or repair its consequences.
    """
    assessment = custody.assessments[basis_assessment_id]
    claim = actor.claims[basis_claim_id]
    if claim.semantic_minute > semantic_minute:
        raise ValueError("decision basis cannot come from the future")
    if claim.provenance_root != f"custody-assessment:{assessment.assessment_id}":
        raise ValueError("decision basis claim does not belong to assessment")
    if claim.subject != f"custody:{assessment.evidence_id}":
        raise ValueError("decision basis claim targets the wrong evidence")
    if claim.value != assessment.status.value:
        raise ValueError("decision basis claim does not preserve assessment conclusion")

    decision = AssessmentDependentDecision(
        decision_id=decision_id,
        actor_id=actor.agent_id,
        basis_assessment_id=basis_assessment_id,
        basis_claim_id=basis_claim_id,
        decision_kind=decision_kind,
        subject_ref=subject_ref,
        semantic_minute=semantic_minute,
    )
    registry.add(decision)
    return decision


def superseding_assessments(
    custody: EvidenceCustodyRegistry,
    *,
    basis_assessment_id: str,
    as_of_minute: int,
) -> tuple[str, ...]:
    """Return later assessments whose validated lineage descends from the decision basis."""
    result: list[tuple[int, str]] = []
    for assessment in custody.assessments.values():
        if assessment.semantic_minute > as_of_minute or assessment.assessment_id == basis_assessment_id:
            continue
        lineage_ids = tuple(row.assessment_id for row in custody.assessment_lineage(assessment.assessment_id))
        if basis_assessment_id in lineage_ids[:-1]:
            result.append((assessment.semantic_minute, assessment.assessment_id))
    return tuple(assessment_id for _, assessment_id in sorted(result))


def affected_decisions(
    registry: AssessmentDecisionDependencyRegistry,
    custody: EvidenceCustodyRegistry,
    *,
    superseding_assessment_id: str,
) -> tuple[AssessmentDependentDecision, ...]:
    lineage = custody.assessment_lineage(superseding_assessment_id)
    ancestor_ids = {assessment.assessment_id for assessment in lineage[:-1]}
    return tuple(
        registry.decisions[key]
        for key in sorted(registry.decisions)
        if registry.decisions[key].basis_assessment_id in ancestor_ids
    )


def evaluate_decision_review_status(
    registry: AssessmentDecisionDependencyRegistry,
    custody: EvidenceCustodyRegistry,
    actor: KnowledgeLedger,
    *,
    decision_id: str,
    as_of_minute: int,
) -> DecisionReviewStatus:
    """Evaluate whether the actor has actually received a correction relevant to a decision.

    Global lineage can establish that a newer assessment exists. It cannot grant that knowledge
    to the actor. Review becomes eligible only when the actor ledger contains a claim rooted in
    a superseding assessment at or before the review time.
    """
    decision = registry.decisions[decision_id]
    if actor.agent_id != decision.actor_id:
        raise ValueError("decision review actor must match decision actor")
    newer_ids = superseding_assessments(
        custody,
        basis_assessment_id=decision.basis_assessment_id,
        as_of_minute=as_of_minute,
    )
    if not newer_ids:
        return DecisionReviewStatus.BASIS_CURRENT

    known_roots = {
        claim.provenance_root
        for claim in actor.claims.values()
        if claim.semantic_minute <= as_of_minute
    }
    if any(f"custody-assessment:{assessment_id}" in known_roots for assessment_id in newer_ids):
        return DecisionReviewStatus.REVIEW_ELIGIBLE
    return DecisionReviewStatus.SUPERSEDED_NOT_RECEIVED
