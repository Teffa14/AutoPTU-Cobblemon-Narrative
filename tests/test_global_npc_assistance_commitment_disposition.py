from pathlib import Path

import pytest

from tools.global_npc_assistance_commitment_disposition import (
    AssistanceCommitmentDispositionLedger,
    CommitmentStartDisposition,
    record_commitment_start_disposition,
)
from tools.global_npc_assistance_commitment_start import (
    AssistanceCommitmentStartAssessment,
    AssistanceCommitmentStartLedger,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
COMMITMENT = "commitment:negotiated-help-pass440"
PROPOSAL = "proposal:pass440"
ASSESSMENT = "start-assessment:pass440"
DISPOSITION = "start-disposition:pass440"


def _commitments():
    ledger = AssistanceCounterproposalCommitmentLedger()
    record = AssistanceCounterproposalCommitmentRecord(
        commitment_id=COMMITMENT,
        proposal_id=PROPOSAL,
        request_action_id="action:request-pass440",
        response_action_id="action:counter-pass440",
        decision_action_id="action:accept-pass440",
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
        provenance_root="action:accept-pass440",
    )
    ledger.add(record)
    return ledger, record


def _starts(condition="BLOCKED_AT_START"):
    ledger = AssistanceCommitmentStartLedger()
    assessment = AssistanceCommitmentStartAssessment(
        assessment_id=ASSESSMENT,
        watch_id="start-watch:pass440",
        commitment_id=COMMITMENT,
        proposal_id=PROPOSAL,
        requester_id=MARA,
        responder_id=TEO,
        semantic_minute=1500,
        condition=condition,
        viability_observation_id="viability:pass440",
        constraint_kind="ROUTE_UNAVAILABLE",
        constraint_ref="route-state:causeway-closed",
        evidence_ref="claim:closure-pass440",
        provenance_root="notice:closure-pass440",
    )
    ledger.assessments[assessment.assessment_id] = assessment
    return ledger, assessment


def _record(commitments, starts, dispositions, **overrides):
    values = dict(
        commitment_ledger=commitments,
        start_ledger=starts,
        disposition_ledger=dispositions,
        commitment_id=COMMITMENT,
        assessment_id=ASSESSMENT,
        disposition_id=DISPOSITION,
        actor_id=TEO,
        semantic_minute=1501,
        disposition=CommitmentStartDisposition.WAIT_FOR_CLEARANCE,
        rationale_ref="reason:route-still-closed",
        provenance_root="decision:teo-pass440",
    )
    values.update(overrides)
    return record_commitment_start_disposition(**values)


def test_responder_can_record_each_world_level_start_disposition_without_mutating_commitment():
    for choice in CommitmentStartDisposition:
        commitments, original = _commitments()
        starts, assessment = _starts()
        dispositions = AssistanceCommitmentDispositionLedger()
        row = _record(commitments, starts, dispositions, disposition=choice)
        assert row.disposition == choice.value
        assert row.assessment_id == assessment.assessment_id
        assert commitments.records[COMMITMENT] == original


def test_only_commitment_owner_can_choose_disposition():
    commitments, _ = _commitments()
    starts, _ = _starts()
    with pytest.raises(ValueError, match="only the responder"):
        _record(commitments, starts, AssistanceCommitmentDispositionLedger(), actor_id=MARA)


def test_disposition_requires_matching_adverse_start_assessment():
    commitments, _ = _commitments()
    starts, _ = _starts()
    with pytest.raises(KeyError, match="unknown assistance commitment start assessment"):
        _record(
            commitments,
            starts,
            AssistanceCommitmentDispositionLedger(),
            assessment_id="assessment:missing",
        )

    starts.assessments[ASSESSMENT] = AssistanceCommitmentStartAssessment(
        assessment_id=ASSESSMENT,
        watch_id="start-watch:pass440",
        commitment_id="commitment:other",
        proposal_id=PROPOSAL,
        requester_id=MARA,
        responder_id=TEO,
        semantic_minute=1500,
        condition="BLOCKED_AT_START",
        viability_observation_id="viability:pass440",
        constraint_kind="ROUTE_UNAVAILABLE",
        constraint_ref="route-state:causeway-closed",
        evidence_ref="claim:closure-pass440",
        provenance_root="notice:closure-pass440",
    )
    with pytest.raises(ValueError, match="commitment binding mismatch"):
        _record(commitments, starts, AssistanceCommitmentDispositionLedger())


def test_disposition_cannot_predate_start_or_arrive_after_accepted_window():
    commitments, _ = _commitments()
    starts, _ = _starts()
    with pytest.raises(ValueError, match="cannot predate"):
        _record(commitments, starts, AssistanceCommitmentDispositionLedger(), semantic_minute=1499)
    with pytest.raises(ValueError, match="within the accepted assistance window"):
        _record(commitments, starts, AssistanceCommitmentDispositionLedger(), semantic_minute=1541)


def test_replay_is_idempotent_and_second_or_conflicting_start_choice_fails_closed():
    commitments, _ = _commitments()
    starts, _ = _starts()
    dispositions = AssistanceCommitmentDispositionLedger()
    first = _record(commitments, starts, dispositions)
    assert _record(commitments, starts, dispositions) == first

    with pytest.raises(ValueError, match="conflicting content"):
        _record(commitments, starts, dispositions, rationale_ref="reason:different")

    with pytest.raises(ValueError, match="already has a start disposition"):
        _record(commitments, starts, dispositions, disposition_id="start-disposition:second")


def test_snapshot_round_trip_preserves_choice_and_provenance():
    commitments, _ = _commitments()
    starts, _ = _starts()
    dispositions = AssistanceCommitmentDispositionLedger()
    original = _record(commitments, starts, dispositions)
    restored = AssistanceCommitmentDispositionLedger.from_snapshot(dispositions.snapshot())
    assert restored.records[DISPOSITION] == original
    assert restored.snapshot() == dispositions.snapshot()


def test_owner_contains_no_execution_communication_or_fault_adjudication_path():
    source = Path("tools/global_npc_assistance_commitment_disposition.py").read_text(encoding="utf-8")
    forbidden = (
        "REQUEST_AUTOPTU",
        "reserve_route",
        "consume_item",
        "allocate_resource",
        "send_message",
        "cancel_commitment",
        "reschedule_commitment",
        "MISSED_OBLIGATION",
        "relationship_delta",
    )
    for token in forbidden:
        assert token not in source
