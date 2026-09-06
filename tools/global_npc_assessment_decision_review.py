from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

from tools.global_npc_assessment_decision_dependency import (
    AssessmentDecisionDependencyRegistry,
    DecisionReviewStatus,
    evaluate_decision_review_status,
)
from tools.global_npc_evidence_custody import EvidenceCustodyRegistry
from tools.global_npc_memory import KnowledgeLedger


DECISION_REVIEW_SNAPSHOT_SCHEMA = "OUROS_NPC_ASSESSMENT_DECISION_REVIEW_V1"


class DecisionReviewOutcome(str, Enum):
    MAINTAIN = "MAINTAIN"
    AMEND = "AMEND"
    RESCIND = "RESCIND"
    DEFER = "DEFER"


@dataclass(frozen=True)
class AssessmentDecisionReview:
    review_id: str
    decision_id: str
    actor_id: str
    superseding_assessment_id: str
    superseding_claim_id: str
    outcome: DecisionReviewOutcome
    rationale_ref: str
    semantic_minute: int

    def __post_init__(self) -> None:
        if not self.review_id or not self.decision_id or not self.actor_id:
            raise ValueError("review identity, decision and actor are required")
        if not self.superseding_assessment_id or not self.superseding_claim_id:
            raise ValueError("review requires an explicit superseding assessment claim")
        if not self.rationale_ref:
            raise ValueError("review rationale reference is required")
        if self.semantic_minute < 0:
            raise ValueError("review time cannot be negative")

    def to_snapshot(self) -> dict:
        return {
            "review_id": self.review_id,
            "decision_id": self.decision_id,
            "actor_id": self.actor_id,
            "superseding_assessment_id": self.superseding_assessment_id,
            "superseding_claim_id": self.superseding_claim_id,
            "outcome": self.outcome.value,
            "rationale_ref": self.rationale_ref,
            "semantic_minute": self.semantic_minute,
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "AssessmentDecisionReview":
        return cls(
            review_id=str(raw["review_id"]),
            decision_id=str(raw["decision_id"]),
            actor_id=str(raw["actor_id"]),
            superseding_assessment_id=str(raw["superseding_assessment_id"]),
            superseding_claim_id=str(raw["superseding_claim_id"]),
            outcome=DecisionReviewOutcome(str(raw["outcome"])),
            rationale_ref=str(raw["rationale_ref"]),
            semantic_minute=int(raw["semantic_minute"]),
        )


@dataclass
class AssessmentDecisionReviewRegistry:
    reviews: dict[str, AssessmentDecisionReview] = field(default_factory=dict)

    def add(self, review: AssessmentDecisionReview) -> None:
        existing = self.reviews.get(review.review_id)
        if existing is not None:
            if existing != review:
                raise ValueError(f"assessment decision review collision: {review.review_id}")
            return
        self.reviews[review.review_id] = review

    def reviews_for_decision(self, decision_id: str) -> tuple[AssessmentDecisionReview, ...]:
        return tuple(
            sorted(
                (review for review in self.reviews.values() if review.decision_id == decision_id),
                key=lambda review: (review.semantic_minute, review.review_id),
            )
        )

    def snapshot(self) -> dict:
        return {
            "schema": DECISION_REVIEW_SNAPSHOT_SCHEMA,
            "reviews": [self.reviews[key].to_snapshot() for key in sorted(self.reviews)],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "AssessmentDecisionReviewRegistry":
        if snapshot.get("schema") != DECISION_REVIEW_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported assessment decision review snapshot schema")
        registry = cls()
        for raw in snapshot.get("reviews", []):
            if not isinstance(raw, Mapping):
                raise ValueError("assessment decision review row must be a mapping")
            registry.add(AssessmentDecisionReview.from_snapshot(raw))
        return registry


def record_assessment_decision_review(
    registry: AssessmentDecisionReviewRegistry,
    dependencies: AssessmentDecisionDependencyRegistry,
    custody: EvidenceCustodyRegistry,
    actor: KnowledgeLedger,
    *,
    review_id: str,
    decision_id: str,
    superseding_assessment_id: str,
    superseding_claim_id: str,
    outcome: DecisionReviewOutcome,
    rationale_ref: str,
    semantic_minute: int,
) -> AssessmentDecisionReview:
    """Record a review event without mutating or repairing downstream consequences."""
    decision = dependencies.decisions[decision_id]
    if actor.agent_id != decision.actor_id:
        raise ValueError("decision review actor must match original decision actor")
    status = evaluate_decision_review_status(
        dependencies,
        custody,
        actor,
        decision_id=decision_id,
        as_of_minute=semantic_minute,
    )
    if status is not DecisionReviewStatus.REVIEW_ELIGIBLE:
        raise ValueError("decision is not review eligible for this actor at this time")

    assessment = custody.assessments[superseding_assessment_id]
    lineage_ids = tuple(row.assessment_id for row in custody.assessment_lineage(superseding_assessment_id))
    if decision.basis_assessment_id not in lineage_ids[:-1]:
        raise ValueError("review assessment does not supersede decision basis")

    claim = actor.claims[superseding_claim_id]
    if claim.semantic_minute > semantic_minute:
        raise ValueError("review basis cannot come from the future")
    if claim.provenance_root != f"custody-assessment:{assessment.assessment_id}":
        raise ValueError("review basis claim does not belong to superseding assessment")
    if claim.subject != f"custody:{assessment.evidence_id}" or claim.value != assessment.status.value:
        raise ValueError("review basis claim does not preserve superseding assessment conclusion")

    review = AssessmentDecisionReview(
        review_id=review_id,
        decision_id=decision_id,
        actor_id=actor.agent_id,
        superseding_assessment_id=superseding_assessment_id,
        superseding_claim_id=superseding_claim_id,
        outcome=outcome,
        rationale_ref=rationale_ref,
        semantic_minute=semantic_minute,
    )
    registry.add(review)
    return review
