from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping

from tools.global_npc_assessment_decision_dependency import AssessmentDecisionDependencyRegistry
from tools.global_npc_assessment_decision_review import (
    AssessmentDecisionReviewRegistry,
    DecisionReviewOutcome,
)


DECISION_CONSEQUENCE_REPAIR_SNAPSHOT_SCHEMA = "OUROS_NPC_DECISION_CONSEQUENCE_REPAIR_V1"


class ConsequenceState(str, Enum):
    ACTIVE = "ACTIVE"
    AMENDED = "AMENDED"
    CEASED = "CEASED"


class ConsequenceRepairAction(str, Enum):
    RETAIN = "RETAIN"
    AMEND = "AMEND"
    CEASE = "CEASE"


@dataclass(frozen=True)
class DecisionConsequence:
    consequence_id: str
    decision_id: str
    consequence_kind: str
    subject_ref: str
    applied_semantic_minute: int
    value_ref: str

    def __post_init__(self) -> None:
        if not self.consequence_id or not self.decision_id:
            raise ValueError("consequence identity and source decision are required")
        if not self.consequence_kind or not self.subject_ref or not self.value_ref:
            raise ValueError("consequence kind, subject and value reference are required")
        if self.applied_semantic_minute < 0:
            raise ValueError("consequence time cannot be negative")

    def to_snapshot(self) -> dict:
        return {
            "consequence_id": self.consequence_id,
            "decision_id": self.decision_id,
            "consequence_kind": self.consequence_kind,
            "subject_ref": self.subject_ref,
            "applied_semantic_minute": self.applied_semantic_minute,
            "value_ref": self.value_ref,
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "DecisionConsequence":
        return cls(
            consequence_id=str(raw["consequence_id"]),
            decision_id=str(raw["decision_id"]),
            consequence_kind=str(raw["consequence_kind"]),
            subject_ref=str(raw["subject_ref"]),
            applied_semantic_minute=int(raw["applied_semantic_minute"]),
            value_ref=str(raw["value_ref"]),
        )


@dataclass(frozen=True)
class ConsequenceRepair:
    repair_id: str
    consequence_id: str
    review_id: str
    actor_id: str
    action: ConsequenceRepairAction
    rationale_ref: str
    semantic_minute: int
    amended_value_ref: str | None = None
    independent_basis_ref: str | None = None

    def __post_init__(self) -> None:
        if not self.repair_id or not self.consequence_id or not self.review_id or not self.actor_id:
            raise ValueError("repair identity, consequence, review and actor are required")
        if not self.rationale_ref:
            raise ValueError("repair rationale reference is required")
        if self.semantic_minute < 0:
            raise ValueError("repair time cannot be negative")
        if self.action is ConsequenceRepairAction.AMEND and not self.amended_value_ref:
            raise ValueError("amended consequence requires a replacement value reference")
        if self.action is not ConsequenceRepairAction.AMEND and self.amended_value_ref is not None:
            raise ValueError("replacement value is only valid for AMEND")

    def to_snapshot(self) -> dict:
        return {
            "repair_id": self.repair_id,
            "consequence_id": self.consequence_id,
            "review_id": self.review_id,
            "actor_id": self.actor_id,
            "action": self.action.value,
            "rationale_ref": self.rationale_ref,
            "semantic_minute": self.semantic_minute,
            "amended_value_ref": self.amended_value_ref,
            "independent_basis_ref": self.independent_basis_ref,
        }

    @classmethod
    def from_snapshot(cls, raw: Mapping[str, object]) -> "ConsequenceRepair":
        return cls(
            repair_id=str(raw["repair_id"]),
            consequence_id=str(raw["consequence_id"]),
            review_id=str(raw["review_id"]),
            actor_id=str(raw["actor_id"]),
            action=ConsequenceRepairAction(str(raw["action"])),
            rationale_ref=str(raw["rationale_ref"]),
            semantic_minute=int(raw["semantic_minute"]),
            amended_value_ref=None if raw.get("amended_value_ref") is None else str(raw["amended_value_ref"]),
            independent_basis_ref=None if raw.get("independent_basis_ref") is None else str(raw["independent_basis_ref"]),
        )


@dataclass(frozen=True)
class EffectiveConsequence:
    consequence_id: str
    state: ConsequenceState
    value_ref: str
    last_repair_id: str | None


@dataclass
class DecisionConsequenceRepairRegistry:
    consequences: dict[str, DecisionConsequence] = field(default_factory=dict)
    repairs: dict[str, ConsequenceRepair] = field(default_factory=dict)

    def add_consequence(self, consequence: DecisionConsequence) -> None:
        existing = self.consequences.get(consequence.consequence_id)
        if existing is not None:
            if existing != consequence:
                raise ValueError(f"decision consequence collision: {consequence.consequence_id}")
            return
        self.consequences[consequence.consequence_id] = consequence

    def add_repair(self, repair: ConsequenceRepair) -> None:
        existing = self.repairs.get(repair.repair_id)
        if existing is not None:
            if existing != repair:
                raise ValueError(f"consequence repair collision: {repair.repair_id}")
            return
        self.repairs[repair.repair_id] = repair

    def repairs_for_consequence(self, consequence_id: str) -> tuple[ConsequenceRepair, ...]:
        return tuple(sorted(
            (row for row in self.repairs.values() if row.consequence_id == consequence_id),
            key=lambda row: (row.semantic_minute, row.repair_id),
        ))

    def effective_consequence(self, consequence_id: str) -> EffectiveConsequence:
        consequence = self.consequences[consequence_id]
        state = ConsequenceState.ACTIVE
        value_ref = consequence.value_ref
        last_repair_id = None
        for repair in self.repairs_for_consequence(consequence_id):
            last_repair_id = repair.repair_id
            if repair.action is ConsequenceRepairAction.CEASE:
                state = ConsequenceState.CEASED
            elif repair.action is ConsequenceRepairAction.AMEND:
                state = ConsequenceState.AMENDED
                value_ref = str(repair.amended_value_ref)
            elif repair.action is ConsequenceRepairAction.RETAIN:
                pass
        return EffectiveConsequence(consequence_id, state, value_ref, last_repair_id)

    def snapshot(self) -> dict:
        return {
            "schema": DECISION_CONSEQUENCE_REPAIR_SNAPSHOT_SCHEMA,
            "consequences": [self.consequences[key].to_snapshot() for key in sorted(self.consequences)],
            "repairs": [self.repairs[key].to_snapshot() for key in sorted(self.repairs)],
        }

    @classmethod
    def restore(cls, snapshot: Mapping[str, object]) -> "DecisionConsequenceRepairRegistry":
        if snapshot.get("schema") != DECISION_CONSEQUENCE_REPAIR_SNAPSHOT_SCHEMA:
            raise ValueError("unsupported decision consequence repair snapshot schema")
        registry = cls()
        for raw in snapshot.get("consequences", []):
            if not isinstance(raw, Mapping):
                raise ValueError("decision consequence row must be a mapping")
            registry.add_consequence(DecisionConsequence.from_snapshot(raw))
        for raw in snapshot.get("repairs", []):
            if not isinstance(raw, Mapping):
                raise ValueError("consequence repair row must be a mapping")
            repair = ConsequenceRepair.from_snapshot(raw)
            if repair.consequence_id not in registry.consequences:
                raise ValueError("repair references unknown consequence")
            registry.add_repair(repair)
        return registry


def record_decision_consequence(
    registry: DecisionConsequenceRepairRegistry,
    dependencies: AssessmentDecisionDependencyRegistry,
    *,
    consequence_id: str,
    decision_id: str,
    consequence_kind: str,
    subject_ref: str,
    applied_semantic_minute: int,
    value_ref: str,
) -> DecisionConsequence:
    decision = dependencies.decisions[decision_id]
    if applied_semantic_minute < decision.semantic_minute:
        raise ValueError("consequence cannot predate its source decision")
    consequence = DecisionConsequence(
        consequence_id=consequence_id,
        decision_id=decision_id,
        consequence_kind=consequence_kind,
        subject_ref=subject_ref,
        applied_semantic_minute=applied_semantic_minute,
        value_ref=value_ref,
    )
    registry.add_consequence(consequence)
    return consequence


def record_consequence_repair(
    registry: DecisionConsequenceRepairRegistry,
    reviews: AssessmentDecisionReviewRegistry,
    *,
    repair_id: str,
    consequence_id: str,
    review_id: str,
    action: ConsequenceRepairAction,
    rationale_ref: str,
    semantic_minute: int,
    amended_value_ref: str | None = None,
    independent_basis_ref: str | None = None,
) -> ConsequenceRepair:
    consequence = registry.consequences[consequence_id]
    review = reviews.reviews[review_id]
    if review.decision_id != consequence.decision_id:
        raise ValueError("repair review does not belong to consequence source decision")
    if semantic_minute < max(consequence.applied_semantic_minute, review.semantic_minute):
        raise ValueError("repair cannot predate the consequence or review")
    if registry.effective_consequence(consequence_id).state is ConsequenceState.CEASED:
        raise ValueError("ceased consequence cannot be repaired again")

    if review.outcome is DecisionReviewOutcome.DEFER:
        raise ValueError("deferred review cannot change downstream consequences")
    if review.outcome is DecisionReviewOutcome.MAINTAIN and action is not ConsequenceRepairAction.RETAIN:
        raise ValueError("maintained decision may only retain its consequence")
    if review.outcome is DecisionReviewOutcome.AMEND and action is ConsequenceRepairAction.CEASE:
        raise ValueError("amended decision cannot cease a consequence through this seam")
    if review.outcome is DecisionReviewOutcome.RESCIND and action is ConsequenceRepairAction.AMEND:
        raise ValueError("rescinded decision cannot amend a consequence through this seam")
    if review.outcome is DecisionReviewOutcome.RESCIND and action is ConsequenceRepairAction.RETAIN and not independent_basis_ref:
        raise ValueError("retaining a consequence after rescission requires an independent basis")

    repair = ConsequenceRepair(
        repair_id=repair_id,
        consequence_id=consequence_id,
        review_id=review_id,
        actor_id=review.actor_id,
        action=action,
        rationale_ref=rationale_ref,
        semantic_minute=semantic_minute,
        amended_value_ref=amended_value_ref,
        independent_basis_ref=independent_basis_ref,
    )
    registry.add_repair(repair)
    return repair
