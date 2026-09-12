from pathlib import Path

import pytest

from tools.global_npc_assistance_commitment_start import AssistanceCommitmentStartLedger, CommitmentStartCondition
from tools.global_npc_assistance_commitment_viability import AssistanceCommitmentViabilityLedger, CommitmentConstraintKind, CommitmentViability
from tools.global_npc_assistance_counterproposal_commitment import AssistanceCounterproposalCommitmentLedger, AssistanceCounterproposalCommitmentRecord
from tools.global_npc_assistance_renegotiation_replacement_commitment import AssistanceRenegotiationReplacementCommitmentLedger, AssistanceRenegotiationReplacementCommitmentRecord
from tools.global_npc_assistance_replacement_start import arm_active_replacement_start_watch, assess_active_replacement_start
from tools.global_npc_assistance_replacement_viability import record_active_replacement_prestart_viability
from tools.global_npc_replanning import NpcReplanQueue

REQUESTER = "ouros.npc.requester.453"
RESPONDER = "ouros.npc.responder.453"
ROOT = "commitment:453:root"
SECOND = "commitment:453:second"
THIRD = "commitment:453:third"


def _initial():
    ledger = AssistanceCounterproposalCommitmentLedger()
    ledger.add(AssistanceCounterproposalCommitmentRecord(
        commitment_id=ROOT, proposal_id="proposal:453:root", request_action_id="request:453", response_action_id="counter:453", decision_action_id="accept:453:root",
        requester_id=REQUESTER, responder_id=RESPONDER, intent_kind="ASSIST_SITE_SURVEY", start_minute=100, end_minute=120,
        location_ref="site:a", scope_ref="survey", alternative_ref=None, priority=6, hard=True, grace_minutes=5,
        required_knowledge=("claim:access",), required_permissions=("permit:survey",), requires_local_projection=False,
        requires_structured_mechanics=False, provenance_root="accept:453:root",
    ))
    return ledger


def _replacement(commitment_id, parent_id, parent_provenance, proposal_id, decision_id, start, end):
    return AssistanceRenegotiationReplacementCommitmentRecord(
        commitment_id=commitment_id, supersedes_commitment_id=parent_id, replacement_proposal_id=proposal_id,
        proposal_decision_id=decision_id, decision_reply_event_id=f"event:{decision_id}", requester_id=REQUESTER, responder_id=RESPONDER,
        intent_kind="ASSIST_SITE_SURVEY", start_minute=start, end_minute=end, location_ref=f"site:{commitment_id.rsplit(':', 1)[-1]}",
        scope_ref="survey", alternative_ref=None, priority=6, hard=True, grace_minutes=5, required_knowledge=("claim:access",),
        required_permissions=("permit:survey",), requires_local_projection=False, requires_structured_mechanics=False,
        superseded_provenance_root=parent_provenance, proposal_provenance_root=proposal_id, provenance_root=decision_id,
    )


def _replacements(two=False):
    ledger = AssistanceRenegotiationReplacementCommitmentLedger()
    ledger.add(_replacement(SECOND, ROOT, "accept:453:root", "proposal:453:second", "decision:453:second", 140, 160))
    if two:
        ledger.add(_replacement(THIRD, SECOND, "decision:453:second", "proposal:453:third", "decision:453:third", 180, 205))
    return ledger


def _blocked(initial, replacements, viability, queue, commitment_id=SECOND, minute=130):
    return record_active_replacement_prestart_viability(
        initial_ledger=initial, replacement_ledger=replacements, viability_ledger=viability, replan_queue=queue,
        commitment_id=commitment_id, observation_id=f"viability:453:{commitment_id}", observer_id=RESPONDER, semantic_minute=minute,
        viability=CommitmentViability.BLOCKED, constraint_kind=CommitmentConstraintKind.ROUTE_UNAVAILABLE,
        constraint_ref="route:closed", evidence_ref="claim:inspection", provenance_root="publication:inspection",
    )


def test_active_replacement_can_be_watched_and_assessed_at_exact_start():
    initial, replacements = _initial(), _replacements()
    viability, starts, queue = AssistanceCommitmentViabilityLedger(), AssistanceCommitmentStartLedger(), NpcReplanQueue()
    blocker = _blocked(initial, replacements, viability, queue)
    watch = arm_active_replacement_start_watch(initial_ledger=initial, replacement_ledger=replacements, start_ledger=starts, replan_queue=queue,
        commitment_id=SECOND, watch_id="watch:453:second", armed_minute=131, provenance_root="schedule:453:second")
    assessment = assess_active_replacement_start(initial_ledger=initial, replacement_ledger=replacements, viability_ledger=viability,
        start_ledger=starts, commitment_id=SECOND, watch_id=watch.watch_id, assessment_id="assessment:453:second", semantic_minute=140)
    assert assessment.condition == CommitmentStartCondition.BLOCKED_AT_START.value
    assert assessment.viability_observation_id == blocker.observation_id
    assert assessment.proposal_id == "proposal:453:second"
    assert initial.records[ROOT].start_minute == 100


def test_latest_generation_only_can_receive_start_watch():
    initial, replacements = _initial(), _replacements(two=True)
    with pytest.raises(ValueError, match="active replacement"):
        arm_active_replacement_start_watch(initial_ledger=initial, replacement_ledger=replacements, start_ledger=AssistanceCommitmentStartLedger(),
            replan_queue=NpcReplanQueue(), commitment_id=SECOND, watch_id="watch:old", armed_minute=130, provenance_root="p")


def test_restored_viability_creates_no_adverse_assessment():
    initial, replacements = _initial(), _replacements()
    viability, starts, queue = AssistanceCommitmentViabilityLedger(), AssistanceCommitmentStartLedger(), NpcReplanQueue()
    _blocked(initial, replacements, viability, queue)
    record_active_replacement_prestart_viability(initial_ledger=initial, replacement_ledger=replacements, viability_ledger=viability, replan_queue=queue,
        commitment_id=SECOND, observation_id="viability:453:restored", observer_id=RESPONDER, semantic_minute=135,
        viability=CommitmentViability.RESTORED, constraint_kind=CommitmentConstraintKind.CLEARED, constraint_ref="route:open",
        evidence_ref="claim:open", provenance_root="notice:open")
    watch = arm_active_replacement_start_watch(initial_ledger=initial, replacement_ledger=replacements, start_ledger=starts, replan_queue=queue,
        commitment_id=SECOND, watch_id="watch:453:restored", armed_minute=136, provenance_root="schedule:restored")
    assert assess_active_replacement_start(initial_ledger=initial, replacement_ledger=replacements, viability_ledger=viability, start_ledger=starts,
        commitment_id=SECOND, watch_id=watch.watch_id, assessment_id="assessment:none", semantic_minute=140) is None


def test_watch_replay_is_idempotent_and_exact_start_is_enforced():
    initial, replacements = _initial(), _replacements()
    starts, queue = AssistanceCommitmentStartLedger(), NpcReplanQueue()
    kwargs = dict(initial_ledger=initial, replacement_ledger=replacements, start_ledger=starts, replan_queue=queue,
        commitment_id=SECOND, watch_id="watch:453:replay", armed_minute=130, provenance_root="schedule:replay")
    assert arm_active_replacement_start_watch(**kwargs) == arm_active_replacement_start_watch(**kwargs)
    with pytest.raises(ValueError, match="active start minute"):
        assess_active_replacement_start(initial_ledger=initial, replacement_ledger=replacements, viability_ledger=AssistanceCommitmentViabilityLedger(),
            start_ledger=starts, commitment_id=SECOND, watch_id="watch:453:replay", assessment_id="assessment:bad", semantic_minute=139)


def test_bridge_has_no_execution_or_social_side_effect_surface():
    source = Path("tools/global_npc_assistance_replacement_start.py").read_text(encoding="utf-8")
    for token in ("REQUEST_AUTOPTU", "reserve_route", "allocate_resource", "move_actor", "relationship_delta", "grant_permission", ".commitments ="):
        assert token not in source
