from dataclasses import replace
from pathlib import Path

import pytest

from tools.global_npc_assistance_commitment_viability import (
    AssistanceCommitmentViabilityLedger,
    CommitmentConstraintKind,
    CommitmentViability,
    record_prestart_commitment_viability,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)
from tools.global_npc_replanning import NpcReplanQueue

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
COMMITMENT = "commitment:negotiated-help-pass437"
PROPOSAL = "proposal:pass437"


def _commitments():
    ledger = AssistanceCounterproposalCommitmentLedger()
    record = AssistanceCounterproposalCommitmentRecord(
        commitment_id=COMMITMENT,
        proposal_id=PROPOSAL,
        request_action_id="action:request-pass437",
        response_action_id="action:counter-pass437",
        decision_action_id="action:accept-pass437",
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
        provenance_root="action:accept-pass437",
    )
    ledger.add(record)
    return ledger, record


def _observe(commitments, viability, queue, **overrides):
    values = dict(
        commitment_ledger=commitments,
        viability_ledger=viability,
        replan_queue=queue,
        commitment_id=COMMITMENT,
        observation_id="viability:route-closed-pass437",
        observer_id=TEO,
        semantic_minute=1470,
        viability=CommitmentViability.BLOCKED,
        constraint_kind=CommitmentConstraintKind.ROUTE_UNAVAILABLE,
        constraint_ref="route-state:causeway-closed",
        evidence_ref="claim:field-notice-pass437",
        provenance_root="publication:route-closure-pass437",
        replan_priority=9,
    )
    values.update(overrides)
    return record_prestart_commitment_viability(**values)


def test_blocker_preserves_agreement_and_wakes_only_commitment_owner():
    commitments, original = _commitments()
    viability = AssistanceCommitmentViabilityLedger()
    queue = NpcReplanQueue()

    observation = _observe(commitments, viability, queue)

    assert commitments.records[COMMITMENT] == original
    assert observation.proposal_id == PROPOSAL
    assert observation.requester_id == MARA
    assert observation.responder_id == TEO
    assert observation.viability == "BLOCKED"
    assert observation.constraint_kind == "ROUTE_UNAVAILABLE"
    assert viability.latest_for(COMMITMENT) == observation

    batches = queue.process_due(1470)
    assert len(batches) == 1
    assert batches[0].agent_id == TEO
    assert batches[0].reasons == ("EXTERNAL_EVENT",)
    assert batches[0].source_refs == (observation.observation_id,)
    assert MARA not in {batch.agent_id for batch in batches}


def test_at_risk_then_restored_is_append_only_history_not_reschedule():
    commitments, original = _commitments()
    viability = AssistanceCommitmentViabilityLedger()
    queue = NpcReplanQueue()

    first = _observe(
        commitments,
        viability,
        queue,
        observation_id="viability:access-risk-pass437",
        semantic_minute=1460,
        viability=CommitmentViability.AT_RISK,
        constraint_kind=CommitmentConstraintKind.ACCESS_REVOKED,
        constraint_ref="access-state:permit-under-review",
    )
    restored = _observe(
        commitments,
        viability,
        queue,
        observation_id="viability:access-restored-pass437",
        semantic_minute=1480,
        viability=CommitmentViability.RESTORED,
        constraint_kind=CommitmentConstraintKind.CLEARED,
        constraint_ref="access-state:permit-restored",
        evidence_ref="claim:permit-restored-pass437",
        provenance_root="notice:permit-restored-pass437",
    )

    assert viability.history_for(COMMITMENT) == (first, restored)
    assert viability.latest_for(COMMITMENT) == restored
    assert commitments.records[COMMITMENT] == original
    assert original.start_minute == 1500
    assert original.end_minute == 1540


def test_restored_without_prior_blocker_fails_closed():
    commitments, _ = _commitments()
    with pytest.raises(ValueError, match="requires a prior"):
        _observe(
            commitments,
            AssistanceCommitmentViabilityLedger(),
            NpcReplanQueue(),
            viability=CommitmentViability.RESTORED,
            constraint_kind=CommitmentConstraintKind.CLEARED,
        )


def test_only_responder_can_record_execution_viability_and_only_before_start():
    commitments, _ = _commitments()
    with pytest.raises(ValueError, match="only the responder"):
        _observe(
            commitments,
            AssistanceCommitmentViabilityLedger(),
            NpcReplanQueue(),
            observer_id=MARA,
        )

    with pytest.raises(ValueError, match="before the negotiated start"):
        _observe(
            commitments,
            AssistanceCommitmentViabilityLedger(),
            NpcReplanQueue(),
            semantic_minute=1500,
        )


def test_unknown_commitment_and_invalid_restored_shape_fail_closed():
    commitments, _ = _commitments()
    with pytest.raises(KeyError, match="unknown negotiated assistance commitment"):
        _observe(
            commitments,
            AssistanceCommitmentViabilityLedger(),
            NpcReplanQueue(),
            commitment_id="commitment:missing",
        )

    with pytest.raises(ValueError, match="restored viability requires CLEARED"):
        _observe(
            commitments,
            AssistanceCommitmentViabilityLedger(),
            NpcReplanQueue(),
            viability=CommitmentViability.RESTORED,
            constraint_kind=CommitmentConstraintKind.ROUTE_UNAVAILABLE,
        )


def test_replay_is_idempotent_but_conflicting_identity_fails_closed():
    commitments, _ = _commitments()
    viability = AssistanceCommitmentViabilityLedger()
    queue = NpcReplanQueue()
    first = _observe(commitments, viability, queue)
    replay = _observe(commitments, viability, queue)
    assert replay == first
    assert len(viability.records) == 1
    assert len(queue.pending) == 1

    with pytest.raises(ValueError, match="conflicting content"):
        _observe(
            commitments,
            viability,
            queue,
            constraint_ref="route-state:different-closure",
        )


def test_history_cannot_move_backward_and_snapshot_round_trips():
    commitments, _ = _commitments()
    viability = AssistanceCommitmentViabilityLedger()
    queue = NpcReplanQueue()
    _observe(commitments, viability, queue, semantic_minute=1480)

    with pytest.raises(ValueError, match="cannot move backward"):
        _observe(
            commitments,
            viability,
            queue,
            observation_id="viability:older-pass437",
            semantic_minute=1470,
        )

    restored = AssistanceCommitmentViabilityLedger.from_snapshot(viability.snapshot())
    assert restored.snapshot() == viability.snapshot()

    tampered = restored.snapshot()
    tampered["records"][0]["viability"] = "RESTORED"
    with pytest.raises(ValueError, match="requires CLEARED"):
        AssistanceCommitmentViabilityLedger.from_snapshot(tampered)


def test_owner_contains_no_execution_or_commitment_mutation_path():
    source = Path("tools/global_npc_assistance_commitment_viability.py").read_text(
        encoding="utf-8"
    )
    forbidden = (
        "REQUEST_AUTOPTU",
        "reserve_route",
        "consume_item",
        "allocate_resource",
        "location_ref =",
        ".commitments =",
    )
    for token in forbidden:
        assert token not in source
