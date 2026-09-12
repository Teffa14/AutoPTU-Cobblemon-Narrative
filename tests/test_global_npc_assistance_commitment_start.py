from dataclasses import replace
from pathlib import Path

import pytest

from tools.global_npc_assistance_commitment_start import (
    AssistanceCommitmentStartLedger,
    CommitmentStartCondition,
    arm_commitment_start_watch,
    assess_commitment_start,
)
from tools.global_npc_assistance_commitment_viability import (
    AssistanceCommitmentViabilityLedger,
    AssistanceCommitmentViabilityObservation,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)
from tools.global_npc_replanning import NpcReplanQueue

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
COMMITMENT = "commitment:negotiated-help-pass439"
PROPOSAL = "proposal:pass439"
WATCH = "start-watch:pass439"
ASSESSMENT = "start-assessment:pass439"


def _commitments():
    ledger = AssistanceCounterproposalCommitmentLedger()
    record = AssistanceCounterproposalCommitmentRecord(
        commitment_id=COMMITMENT,
        proposal_id=PROPOSAL,
        request_action_id="action:request-pass439",
        response_action_id="action:counter-pass439",
        decision_action_id="action:accept-pass439",
        requester_id=MARA,
        responder_id=TEO,
        intent_kind="FULFILL_NEGOTIATED_ASSISTANCE",
        start_minute=1500,
        end_minute=1540,
        location_ref="ouros.route.causeway-survey",
        scope_ref="survey_only",
        alternative_ref="remote_report",
        priority=8,
        hard=False,
        grace_minutes=5,
        required_knowledge=(),
        required_permissions=(),
        requires_local_projection=False,
        requires_structured_mechanics=False,
        provenance_root="action:accept-pass439",
    )
    ledger.add(record)
    return ledger, record


def _viability(state="BLOCKED"):
    ledger = AssistanceCommitmentViabilityLedger()
    observation = AssistanceCommitmentViabilityObservation(
        observation_id="viability:route-closed-pass439",
        commitment_id=COMMITMENT,
        proposal_id=PROPOSAL,
        requester_id=MARA,
        responder_id=TEO,
        observer_id=TEO,
        semantic_minute=1470,
        viability=state,
        constraint_kind="ROUTE_UNAVAILABLE" if state != "RESTORED" else "CLEARED",
        constraint_ref="route-state:causeway-closed",
        evidence_ref="claim:closure-pass439",
        provenance_root="notice:closure-pass439",
    )
    ledger.add(observation)
    return ledger, observation


def _arm(commitments, start_ledger, queue, **overrides):
    values = dict(
        commitment_ledger=commitments,
        start_ledger=start_ledger,
        replan_queue=queue,
        commitment_id=COMMITMENT,
        watch_id=WATCH,
        armed_minute=1480,
        provenance_root="action:accept-pass439",
        priority=9,
    )
    values.update(overrides)
    return arm_commitment_start_watch(**values)


def test_watch_wakes_only_commitment_owner_at_exact_start():
    commitments, original = _commitments()
    starts = AssistanceCommitmentStartLedger()
    queue = NpcReplanQueue()

    watch = _arm(commitments, starts, queue)
    assert commitments.records[COMMITMENT] == original
    assert watch.start_minute == 1500
    assert queue.process_due(1499) == []
    batches = queue.process_due(1500)
    assert len(batches) == 1
    assert batches[0].agent_id == TEO
    assert batches[0].reasons == ("SCHEDULE_DUE",)
    assert batches[0].source_refs == (WATCH,)
    assert MARA not in {batch.agent_id for batch in batches}


def test_blocked_at_start_records_fact_without_mutating_agreement():
    commitments, original = _commitments()
    viability, observation = _viability("BLOCKED")
    starts = AssistanceCommitmentStartLedger()
    _arm(commitments, starts, NpcReplanQueue())

    assessment = assess_commitment_start(
        commitment_ledger=commitments,
        viability_ledger=viability,
        start_ledger=starts,
        commitment_id=COMMITMENT,
        watch_id=WATCH,
        assessment_id=ASSESSMENT,
        semantic_minute=1500,
    )

    assert assessment is not None
    assert assessment.condition == CommitmentStartCondition.BLOCKED_AT_START.value
    assert assessment.viability_observation_id == observation.observation_id
    assert assessment.constraint_ref == observation.constraint_ref
    assert assessment.evidence_ref == observation.evidence_ref
    assert commitments.records[COMMITMENT] == original


def test_at_risk_at_start_remains_distinct_from_blocked():
    commitments, _ = _commitments()
    viability, _ = _viability("AT_RISK")
    starts = AssistanceCommitmentStartLedger()
    _arm(commitments, starts, NpcReplanQueue())

    assessment = assess_commitment_start(
        commitment_ledger=commitments,
        viability_ledger=viability,
        start_ledger=starts,
        commitment_id=COMMITMENT,
        watch_id=WATCH,
        assessment_id=ASSESSMENT,
        semantic_minute=1500,
    )
    assert assessment is not None
    assert assessment.condition == CommitmentStartCondition.AT_RISK_AT_START.value


def test_restored_or_never_blocked_start_creates_no_failure_fact():
    commitments, _ = _commitments()
    starts = AssistanceCommitmentStartLedger()
    _arm(commitments, starts, NpcReplanQueue())

    assert assess_commitment_start(
        commitment_ledger=commitments,
        viability_ledger=AssistanceCommitmentViabilityLedger(),
        start_ledger=starts,
        commitment_id=COMMITMENT,
        watch_id=WATCH,
        assessment_id=ASSESSMENT,
        semantic_minute=1500,
    ) is None

    viability, blocked = _viability("BLOCKED")
    viability.add(
        replace(
            blocked,
            observation_id="viability:restored-pass439",
            semantic_minute=1490,
            viability="RESTORED",
            constraint_kind="CLEARED",
            constraint_ref="route-state:causeway-open",
            evidence_ref="claim:open-pass439",
            provenance_root="notice:open-pass439",
        )
    )
    assert assess_commitment_start(
        commitment_ledger=commitments,
        viability_ledger=viability,
        start_ledger=starts,
        commitment_id=COMMITMENT,
        watch_id=WATCH,
        assessment_id=ASSESSMENT,
        semantic_minute=1500,
    ) is None


def test_assessment_requires_exact_start_and_known_commitment():
    commitments, _ = _commitments()
    viability, _ = _viability()
    starts = AssistanceCommitmentStartLedger()
    _arm(commitments, starts, NpcReplanQueue())

    with pytest.raises(ValueError, match="negotiated start minute"):
        assess_commitment_start(
            commitment_ledger=commitments,
            viability_ledger=viability,
            start_ledger=starts,
            commitment_id=COMMITMENT,
            watch_id=WATCH,
            assessment_id=ASSESSMENT,
            semantic_minute=1501,
        )

    with pytest.raises(KeyError, match="unknown negotiated assistance commitment"):
        assess_commitment_start(
            commitment_ledger=AssistanceCounterproposalCommitmentLedger(),
            viability_ledger=viability,
            start_ledger=starts,
            commitment_id=COMMITMENT,
            watch_id=WATCH,
            assessment_id=ASSESSMENT,
            semantic_minute=1500,
        )


def test_watch_replay_is_idempotent_and_conflicting_reuse_fails_closed():
    commitments, _ = _commitments()
    starts = AssistanceCommitmentStartLedger()
    queue = NpcReplanQueue()
    first = _arm(commitments, starts, queue)
    replay = _arm(commitments, starts, queue)
    assert replay == first
    assert len(starts.watches) == 1
    assert len(queue.pending) == 1

    with pytest.raises(ValueError, match="conflicting content"):
        _arm(commitments, starts, queue, provenance_root="different-root")


def test_start_ledger_snapshot_round_trips_with_assessment():
    commitments, _ = _commitments()
    viability, _ = _viability()
    starts = AssistanceCommitmentStartLedger()
    _arm(commitments, starts, NpcReplanQueue())
    assess_commitment_start(
        commitment_ledger=commitments,
        viability_ledger=viability,
        start_ledger=starts,
        commitment_id=COMMITMENT,
        watch_id=WATCH,
        assessment_id=ASSESSMENT,
        semantic_minute=1500,
    )

    restored = AssistanceCommitmentStartLedger.from_snapshot(starts.snapshot())
    assert restored.snapshot() == starts.snapshot()

    tampered = restored.snapshot()
    tampered["assessments"][0]["watch_id"] = "watch:missing"
    with pytest.raises(ValueError, match="matching durable watch"):
        AssistanceCommitmentStartLedger.from_snapshot(tampered)


def test_owner_contains_no_policy_or_execution_path():
    source = Path("tools/global_npc_assistance_commitment_start.py").read_text(
        encoding="utf-8"
    )
    forbidden = (
        "REQUEST_AUTOPTU",
        "reserve_route",
        "consume_item",
        "allocate_resource",
        "cancel_commitment",
        "reschedule_commitment",
        "ABANDONED",
        "RENEGOTIATED",
    )
    for token in forbidden:
        assert token not in source
