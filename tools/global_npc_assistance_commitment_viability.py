from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Mapping

from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
)
from tools.global_npc_replanning import NpcReplanQueue, ReplanReason, ReplanTrigger

SCHEMA_VERSION = "OUROS_ASSISTANCE_COMMITMENT_VIABILITY_LEDGER_V1"


class CommitmentViability(str, Enum):
    AT_RISK = "AT_RISK"
    BLOCKED = "BLOCKED"
    RESTORED = "RESTORED"


class CommitmentConstraintKind(str, Enum):
    ROUTE_UNAVAILABLE = "ROUTE_UNAVAILABLE"
    ACCESS_REVOKED = "ACCESS_REVOKED"
    ACTOR_UNAVAILABLE = "ACTOR_UNAVAILABLE"
    REQUIRED_RESOURCE_UNAVAILABLE = "REQUIRED_RESOURCE_UNAVAILABLE"
    PREMISE_INVALIDATED = "PREMISE_INVALIDATED"
    OTHER_EVIDENCED_CONSTRAINT = "OTHER_EVIDENCED_CONSTRAINT"
    CLEARED = "CLEARED"


@dataclass(frozen=True)
class AssistanceCommitmentViabilityObservation:
    observation_id: str
    commitment_id: str
    proposal_id: str
    requester_id: str
    responder_id: str
    observer_id: str
    semantic_minute: int
    viability: str
    constraint_kind: str
    constraint_ref: str
    evidence_ref: str
    provenance_root: str


class AssistanceCommitmentViabilityLedger:
    """Append-only pre-start observations about negotiated assistance viability.

    The original agreement remains owned by the negotiated commitment ledger.
    This ledger records later evidence that may make fulfillment risky, blocked,
    or viable again. It does not cancel, rewrite, reschedule, travel, reserve a
    route/resource, grant access, complete work, or execute AutoPTU.
    """

    def __init__(self) -> None:
        self.records: dict[str, AssistanceCommitmentViabilityObservation] = {}

    def add(
        self, observation: AssistanceCommitmentViabilityObservation
    ) -> AssistanceCommitmentViabilityObservation:
        existing = self.records.get(observation.observation_id)
        if existing is not None:
            if existing != observation:
                raise ValueError("viability observation id reused with conflicting content")
            return existing
        self.records[observation.observation_id] = observation
        return observation

    def history_for(self, commitment_id: str) -> tuple[AssistanceCommitmentViabilityObservation, ...]:
        return tuple(
            sorted(
                (row for row in self.records.values() if row.commitment_id == commitment_id),
                key=lambda row: (row.semantic_minute, row.observation_id),
            )
        )

    def latest_for(self, commitment_id: str) -> AssistanceCommitmentViabilityObservation | None:
        history = self.history_for(commitment_id)
        return history[-1] if history else None

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "records": [asdict(self.records[key]) for key in sorted(self.records)],
        }

    @classmethod
    def from_snapshot(
        cls, payload: Mapping[str, object]
    ) -> "AssistanceCommitmentViabilityLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported assistance commitment viability ledger schema")
        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("assistance commitment viability records must be a list")
        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("assistance commitment viability row must be an object")
            observation = AssistanceCommitmentViabilityObservation(
                observation_id=str(raw["observation_id"]),
                commitment_id=str(raw["commitment_id"]),
                proposal_id=str(raw["proposal_id"]),
                requester_id=str(raw["requester_id"]),
                responder_id=str(raw["responder_id"]),
                observer_id=str(raw["observer_id"]),
                semantic_minute=int(raw["semantic_minute"]),
                viability=str(raw["viability"]),
                constraint_kind=str(raw["constraint_kind"]),
                constraint_ref=str(raw["constraint_ref"]),
                evidence_ref=str(raw["evidence_ref"]),
                provenance_root=str(raw["provenance_root"]),
            )
            _validate_observation_shape(observation)
            ledger.add(observation)
        return ledger


def _validate_observation_shape(observation: AssistanceCommitmentViabilityObservation) -> None:
    required = (
        observation.observation_id,
        observation.commitment_id,
        observation.proposal_id,
        observation.requester_id,
        observation.responder_id,
        observation.observer_id,
        observation.constraint_ref,
        observation.evidence_ref,
        observation.provenance_root,
    )
    if any(not value for value in required):
        raise ValueError("assistance commitment viability observation requires non-empty references")
    if observation.semantic_minute < 0:
        raise ValueError("assistance commitment viability minute must be non-negative")
    CommitmentViability(observation.viability)
    kind = CommitmentConstraintKind(observation.constraint_kind)
    if observation.viability == CommitmentViability.RESTORED.value:
        if kind is not CommitmentConstraintKind.CLEARED:
            raise ValueError("restored viability requires CLEARED constraint kind")
    elif kind is CommitmentConstraintKind.CLEARED:
        raise ValueError("CLEARED constraint kind is reserved for restored viability")


def record_prestart_commitment_viability(
    *,
    commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    viability_ledger: AssistanceCommitmentViabilityLedger,
    replan_queue: NpcReplanQueue,
    commitment_id: str,
    observation_id: str,
    observer_id: str,
    semantic_minute: int,
    viability: CommitmentViability,
    constraint_kind: CommitmentConstraintKind,
    constraint_ref: str,
    evidence_ref: str,
    provenance_root: str,
    replan_priority: int = 8,
) -> AssistanceCommitmentViabilityObservation:
    """Record one responder-owned pre-start viability observation.

    Every new observation wakes only the responder who owns the accepted
    commitment. The wake-up asks the existing planner to reconsider current
    world state; it does not imply cancellation, rescheduling, travel, resource
    allocation, access, completion, or tactical execution.
    """
    if replan_priority < 0:
        raise ValueError("replan_priority must be non-negative")
    commitment = commitment_ledger.records.get(commitment_id)
    if commitment is None:
        raise KeyError(f"unknown negotiated assistance commitment: {commitment_id}")
    if observer_id != commitment.responder_id:
        raise ValueError("only the responder owning the commitment can record execution viability")
    if semantic_minute < 0 or semantic_minute >= commitment.start_minute:
        raise ValueError("viability observation must occur before the negotiated start minute")
    if not constraint_ref or not evidence_ref or not provenance_root:
        raise ValueError("constraint, evidence and provenance references are required")

    observation = AssistanceCommitmentViabilityObservation(
        observation_id=observation_id,
        commitment_id=commitment.commitment_id,
        proposal_id=commitment.proposal_id,
        requester_id=commitment.requester_id,
        responder_id=commitment.responder_id,
        observer_id=observer_id,
        semantic_minute=semantic_minute,
        viability=viability.value,
        constraint_kind=constraint_kind.value,
        constraint_ref=constraint_ref,
        evidence_ref=evidence_ref,
        provenance_root=provenance_root,
    )
    _validate_observation_shape(observation)

    existing = viability_ledger.records.get(observation_id)
    if existing is not None:
        if existing != observation:
            raise ValueError("viability observation id reused with conflicting content")
        return existing

    previous = viability_ledger.latest_for(commitment_id)
    if previous is not None and semantic_minute < previous.semantic_minute:
        raise ValueError("viability history cannot move backward in semantic time")
    if viability is CommitmentViability.RESTORED:
        if previous is None or previous.viability == CommitmentViability.RESTORED.value:
            raise ValueError("restored viability requires a prior at-risk or blocked observation")

    stored = viability_ledger.add(observation)
    replan_queue.schedule(
        ReplanTrigger(
            trigger_id=f"replan:assistance-viability:{observation_id}",
            agent_id=commitment.responder_id,
            reason=ReplanReason.EXTERNAL_EVENT,
            due_minute=semantic_minute,
            source_ref=observation_id,
            priority=replan_priority,
        )
    )
    return stored
