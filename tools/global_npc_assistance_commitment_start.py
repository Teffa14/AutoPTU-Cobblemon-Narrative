from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Mapping

from tools.global_npc_assistance_commitment_viability import (
    AssistanceCommitmentViabilityLedger,
    CommitmentViability,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
)
from tools.global_npc_replanning import NpcReplanQueue, ReplanReason, ReplanTrigger

SCHEMA_VERSION = "OUROS_ASSISTANCE_COMMITMENT_START_LEDGER_V1"


class CommitmentStartCondition(str, Enum):
    AT_RISK_AT_START = "AT_RISK_AT_START"
    BLOCKED_AT_START = "BLOCKED_AT_START"


@dataclass(frozen=True)
class AssistanceCommitmentStartWatch:
    watch_id: str
    commitment_id: str
    proposal_id: str
    requester_id: str
    responder_id: str
    start_minute: int
    armed_minute: int
    provenance_root: str
    trigger_id: str


@dataclass(frozen=True)
class AssistanceCommitmentStartAssessment:
    assessment_id: str
    watch_id: str
    commitment_id: str
    proposal_id: str
    requester_id: str
    responder_id: str
    semantic_minute: int
    condition: str
    viability_observation_id: str
    constraint_kind: str
    constraint_ref: str
    evidence_ref: str
    provenance_root: str


class AssistanceCommitmentStartLedger:
    """Durable start-time watch and factual assessment for negotiated assistance.

    This owner preserves whether a pre-start risk/blocker is still present when
    the accepted window begins. It does not cancel, reschedule, abandon, travel,
    reserve routes/resources, grant access, notify another actor, complete work,
    or invoke AutoPTU.
    """

    def __init__(self) -> None:
        self.watches: dict[str, AssistanceCommitmentStartWatch] = {}
        self.assessments: dict[str, AssistanceCommitmentStartAssessment] = {}

    def add_watch(self, watch: AssistanceCommitmentStartWatch) -> AssistanceCommitmentStartWatch:
        existing = self.watches.get(watch.watch_id)
        if existing is not None:
            if existing != watch:
                raise ValueError("commitment start watch id reused with conflicting content")
            return existing
        self.watches[watch.watch_id] = watch
        return watch

    def add_assessment(
        self, assessment: AssistanceCommitmentStartAssessment
    ) -> AssistanceCommitmentStartAssessment:
        existing = self.assessments.get(assessment.assessment_id)
        if existing is not None:
            if existing != assessment:
                raise ValueError("commitment start assessment id reused with conflicting content")
            return existing
        if any(
            row.commitment_id == assessment.commitment_id
            for row in self.assessments.values()
        ):
            raise ValueError("commitment already has a start assessment")
        self.assessments[assessment.assessment_id] = assessment
        return assessment

    def assessment_for(self, commitment_id: str) -> AssistanceCommitmentStartAssessment | None:
        rows = [
            row for row in self.assessments.values() if row.commitment_id == commitment_id
        ]
        if not rows:
            return None
        if len(rows) != 1:
            raise ValueError("commitment has multiple start assessments")
        return rows[0]

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "watches": [asdict(self.watches[key]) for key in sorted(self.watches)],
            "assessments": [
                asdict(self.assessments[key]) for key in sorted(self.assessments)
            ],
        }

    @classmethod
    def from_snapshot(cls, payload: Mapping[str, object]) -> "AssistanceCommitmentStartLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported assistance commitment start ledger schema")
        raw_watches = payload.get("watches")
        raw_assessments = payload.get("assessments")
        if not isinstance(raw_watches, list) or not isinstance(raw_assessments, list):
            raise ValueError("commitment start snapshot collections must be lists")
        ledger = cls()
        for raw in raw_watches:
            if not isinstance(raw, Mapping):
                raise ValueError("commitment start watch must be an object")
            watch = AssistanceCommitmentStartWatch(
                watch_id=str(raw["watch_id"]),
                commitment_id=str(raw["commitment_id"]),
                proposal_id=str(raw["proposal_id"]),
                requester_id=str(raw["requester_id"]),
                responder_id=str(raw["responder_id"]),
                start_minute=int(raw["start_minute"]),
                armed_minute=int(raw["armed_minute"]),
                provenance_root=str(raw["provenance_root"]),
                trigger_id=str(raw["trigger_id"]),
            )
            _validate_watch_shape(watch)
            ledger.add_watch(watch)
        for raw in raw_assessments:
            if not isinstance(raw, Mapping):
                raise ValueError("commitment start assessment must be an object")
            assessment = AssistanceCommitmentStartAssessment(
                assessment_id=str(raw["assessment_id"]),
                watch_id=str(raw["watch_id"]),
                commitment_id=str(raw["commitment_id"]),
                proposal_id=str(raw["proposal_id"]),
                requester_id=str(raw["requester_id"]),
                responder_id=str(raw["responder_id"]),
                semantic_minute=int(raw["semantic_minute"]),
                condition=str(raw["condition"]),
                viability_observation_id=str(raw["viability_observation_id"]),
                constraint_kind=str(raw["constraint_kind"]),
                constraint_ref=str(raw["constraint_ref"]),
                evidence_ref=str(raw["evidence_ref"]),
                provenance_root=str(raw["provenance_root"]),
            )
            _validate_assessment_shape(assessment)
            watch = ledger.watches.get(assessment.watch_id)
            if watch is None or watch.commitment_id != assessment.commitment_id:
                raise ValueError("start assessment requires its matching durable watch")
            ledger.add_assessment(assessment)
        return ledger


def _validate_watch_shape(watch: AssistanceCommitmentStartWatch) -> None:
    required = (
        watch.watch_id,
        watch.commitment_id,
        watch.proposal_id,
        watch.requester_id,
        watch.responder_id,
        watch.provenance_root,
        watch.trigger_id,
    )
    if any(not value for value in required):
        raise ValueError("commitment start watch requires non-empty references")
    if watch.start_minute < 0 or watch.armed_minute < 0:
        raise ValueError("commitment start watch minutes must be non-negative")
    if watch.armed_minute >= watch.start_minute:
        raise ValueError("commitment start watch must be armed before start")


def _validate_assessment_shape(assessment: AssistanceCommitmentStartAssessment) -> None:
    required = (
        assessment.assessment_id,
        assessment.watch_id,
        assessment.commitment_id,
        assessment.proposal_id,
        assessment.requester_id,
        assessment.responder_id,
        assessment.viability_observation_id,
        assessment.constraint_kind,
        assessment.constraint_ref,
        assessment.evidence_ref,
        assessment.provenance_root,
    )
    if any(not value for value in required):
        raise ValueError("commitment start assessment requires non-empty references")
    if assessment.semantic_minute < 0:
        raise ValueError("commitment start assessment minute must be non-negative")
    CommitmentStartCondition(assessment.condition)


def arm_commitment_start_watch(
    *,
    commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    start_ledger: AssistanceCommitmentStartLedger,
    replan_queue: NpcReplanQueue,
    commitment_id: str,
    watch_id: str,
    armed_minute: int,
    provenance_root: str,
    priority: int = 9,
) -> AssistanceCommitmentStartWatch:
    """Arm one responder-only semantic-time wake for the accepted start minute."""
    if priority < 0:
        raise ValueError("start watch priority must be non-negative")
    commitment = commitment_ledger.records.get(commitment_id)
    if commitment is None:
        raise KeyError(f"unknown negotiated assistance commitment: {commitment_id}")
    if not watch_id or not provenance_root:
        raise ValueError("watch_id and provenance_root are required")
    trigger_id = f"replan:assistance-start:{watch_id}"
    watch = AssistanceCommitmentStartWatch(
        watch_id=watch_id,
        commitment_id=commitment.commitment_id,
        proposal_id=commitment.proposal_id,
        requester_id=commitment.requester_id,
        responder_id=commitment.responder_id,
        start_minute=commitment.start_minute,
        armed_minute=armed_minute,
        provenance_root=provenance_root,
        trigger_id=trigger_id,
    )
    _validate_watch_shape(watch)

    existing = start_ledger.watches.get(watch_id)
    if existing is not None:
        if existing != watch:
            raise ValueError("commitment start watch id reused with conflicting content")
        return existing

    stored = start_ledger.add_watch(watch)
    replan_queue.schedule(
        ReplanTrigger(
            trigger_id=trigger_id,
            agent_id=commitment.responder_id,
            reason=ReplanReason.SCHEDULE_DUE,
            due_minute=commitment.start_minute,
            source_ref=watch_id,
            priority=priority,
        )
    )
    return stored


def assess_commitment_start(
    *,
    commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    viability_ledger: AssistanceCommitmentViabilityLedger,
    start_ledger: AssistanceCommitmentStartLedger,
    commitment_id: str,
    watch_id: str,
    assessment_id: str,
    semantic_minute: int,
) -> AssistanceCommitmentStartAssessment | None:
    """Record the factual blocker/risk that still exists at the promised start.

    A cleared/no-observation start returns None. Policy such as renegotiation,
    abandonment or missed-obligation handling remains a later planner decision.
    """
    commitment = commitment_ledger.records.get(commitment_id)
    if commitment is None:
        raise KeyError(f"unknown negotiated assistance commitment: {commitment_id}")
    watch = start_ledger.watches.get(watch_id)
    if watch is None:
        raise KeyError(f"unknown assistance commitment start watch: {watch_id}")
    if watch.commitment_id != commitment.commitment_id:
        raise ValueError("start watch commitment binding mismatch")
    if semantic_minute != commitment.start_minute:
        raise ValueError("commitment start assessment must occur at the negotiated start minute")
    if start_ledger.assessment_for(commitment_id) is not None:
        existing = start_ledger.assessments.get(assessment_id)
        if existing is not None:
            return existing
        raise ValueError("commitment already has a start assessment")

    latest = viability_ledger.latest_for(commitment_id)
    if latest is None or latest.viability == CommitmentViability.RESTORED.value:
        return None
    if latest.semantic_minute >= commitment.start_minute:
        raise ValueError("start assessment requires a pre-start viability observation")
    if latest.proposal_id != commitment.proposal_id:
        raise ValueError("viability proposal binding mismatch at commitment start")
    if latest.requester_id != commitment.requester_id or latest.responder_id != commitment.responder_id:
        raise ValueError("viability actor binding mismatch at commitment start")

    if latest.viability == CommitmentViability.BLOCKED.value:
        condition = CommitmentStartCondition.BLOCKED_AT_START
    elif latest.viability == CommitmentViability.AT_RISK.value:
        condition = CommitmentStartCondition.AT_RISK_AT_START
    else:
        raise ValueError("unsupported viability state at commitment start")

    assessment = AssistanceCommitmentStartAssessment(
        assessment_id=assessment_id,
        watch_id=watch.watch_id,
        commitment_id=commitment.commitment_id,
        proposal_id=commitment.proposal_id,
        requester_id=commitment.requester_id,
        responder_id=commitment.responder_id,
        semantic_minute=semantic_minute,
        condition=condition.value,
        viability_observation_id=latest.observation_id,
        constraint_kind=latest.constraint_kind,
        constraint_ref=latest.constraint_ref,
        evidence_ref=latest.evidence_ref,
        provenance_root=latest.provenance_root,
    )
    _validate_assessment_shape(assessment)
    return start_ledger.add_assessment(assessment)
