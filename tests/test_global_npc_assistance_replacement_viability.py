from pathlib import Path

import pytest

from tools.global_npc_assistance_commitment_viability import (
    AssistanceCommitmentViabilityLedger,
    CommitmentConstraintKind,
    CommitmentViability,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)
from tools.global_npc_assistance_renegotiation_replacement_commitment import (
    AssistanceRenegotiationReplacementCommitmentLedger,
    AssistanceRenegotiationReplacementCommitmentRecord,
)
from tools.global_npc_assistance_replacement_viability import (
    record_active_replacement_prestart_viability,
)
from tools.global_npc_replanning import NpcReplanQueue

REQUESTER = "ouros.npc.requester.452"
RESPONDER = "ouros.npc.responder.452"
ROOT = "commitment:452:root"
SECOND = "commitment:452:second"
THIRD = "commitment:452:third"


def _initial():
    ledger = AssistanceCounterproposalCommitmentLedger()
    ledger.add(
        AssistanceCounterproposalCommitmentRecord(
            commitment_id=ROOT,
            proposal_id="proposal:452:root",
            request_action_id="request:452",
            response_action_id="counter:452",
            decision_action_id="accept:452:root",
            requester_id=REQUESTER,
            responder_id=RESPONDER,
            intent_kind="ASSIST_SITE_SURVEY",
            start_minute=100,
            end_minute=120,
            location_ref="site:a",
            scope_ref="survey",
            alternative_ref=None,
            priority=6,
            hard=True,
            grace_minutes=5,
            required_knowledge=("claim:access",),
            required_permissions=("permit:survey",),
            requires_local_projection=False,
            requires_structured_mechanics=False,
            provenance_root="accept:452:root",
        )
    )
    return ledger


def _replacement(commitment_id, parent_id, parent_provenance, proposal_id, decision_id, start, end):
    return AssistanceRenegotiationReplacementCommitmentRecord(
        commitment_id=commitment_id,
        supersedes_commitment_id=parent_id,
        replacement_proposal_id=proposal_id,
        proposal_decision_id=decision_id,
        decision_reply_event_id=f"event:{decision_id}",
        requester_id=REQUESTER,
        responder_id=RESPONDER,
        intent_kind="ASSIST_SITE_SURVEY",
        start_minute=start,
        end_minute=end,
        location_ref=f"site:{commitment_id.rsplit(':', 1)[-1]}",
        scope_ref="survey",
        alternative_ref=None,
        priority=6,
        hard=True,
        grace_minutes=5,
        required_knowledge=("claim:access",),
        required_permissions=("permit:survey",),
        requires_local_projection=False,
        requires_structured_mechanics=False,
        superseded_provenance_root=parent_provenance,
        proposal_provenance_root=proposal_id,
        provenance_root=decision_id,
    )


def _replacements(two=False):
    ledger = AssistanceRenegotiationReplacementCommitmentLedger()
    ledger.add(_replacement(SECOND, ROOT, "accept:452:root", "proposal:452:second", "decision:452:second", 140, 160))
    if two:
        ledger.add(_replacement(THIRD, SECOND, "decision:452:second", "proposal:452:third", "decision:452:third", 180, 205))
    return ledger


def _record(*, initial=None, replacements=None, viability_ledger=None, queue=None, commitment_id=SECOND, **overrides):
    values = dict(
        initial_ledger=initial or _initial(),
        replacement_ledger=replacements or _replacements(),
        viability_ledger=viability_ledger or AssistanceCommitmentViabilityLedger(),
        replan_queue=queue or NpcReplanQueue(),
        commitment_id=commitment_id,
        observation_id="viability:452:blocker",
        observer_id=RESPONDER,
        semantic_minute=130,
        viability=CommitmentViability.BLOCKED,
        constraint_kind=CommitmentConstraintKind.ROUTE_UNAVAILABLE,
        constraint_ref="route-state:washed-out",
        evidence_ref="claim:bridge-inspection",
        provenance_root="publication:bridge-inspection",
        replan_priority=9,
    )
    values.update(overrides)
    return record_active_replacement_prestart_viability(**values)


def test_active_replacement_accepts_prestart_blocker_and_wakes_owner():
    initial = _initial()
    replacements = _replacements()
    ledger = AssistanceCommitmentViabilityLedger()
    queue = NpcReplanQueue()

    observation = _record(initial=initial, replacements=replacements, viability_ledger=ledger, queue=queue)

    assert observation.commitment_id == SECOND
    assert observation.proposal_id == "proposal:452:second"
    assert observation.requester_id == REQUESTER
    assert observation.responder_id == RESPONDER
    assert replacements.records[SECOND].start_minute == 140
    assert initial.records[ROOT].start_minute == 100

    batches = queue.process_due(130)
    assert len(batches) == 1
    assert batches[0].agent_id == RESPONDER
    assert batches[0].source_refs == (observation.observation_id,)


def test_superseded_replacement_cannot_receive_new_viability_evidence():
    with pytest.raises(ValueError, match="active replacement"):
        _record(replacements=_replacements(two=True), commitment_id=SECOND)


def test_latest_generation_can_receive_viability_evidence():
    observation = _record(
        replacements=_replacements(two=True),
        commitment_id=THIRD,
        semantic_minute=170,
        observation_id="viability:452:third",
    )
    assert observation.commitment_id == THIRD
    assert observation.proposal_id == "proposal:452:third"


def test_original_commitment_stays_owned_by_pass_437():
    with pytest.raises(KeyError, match="unknown replacement assistance commitment"):
        _record(commitment_id=ROOT)


def test_wrong_actor_past_start_and_orphan_lineage_fail_closed():
    with pytest.raises(ValueError, match="only the responder"):
        _record(observer_id=REQUESTER)
    with pytest.raises(ValueError, match="before the active start"):
        _record(semantic_minute=140)

    orphan = AssistanceRenegotiationReplacementCommitmentLedger()
    orphan.add(_replacement(SECOND, "missing", "missing:root", "proposal:o", "decision:o", 140, 160))
    with pytest.raises(ValueError, match="lacks an original assistance root"):
        _record(replacements=orphan)


def test_restoration_requires_prior_blocker_on_same_active_generation():
    initial = _initial()
    replacements = _replacements()
    ledger = AssistanceCommitmentViabilityLedger()
    queue = NpcReplanQueue()

    with pytest.raises(ValueError, match="requires a prior"):
        _record(
            initial=initial,
            replacements=replacements,
            viability_ledger=ledger,
            queue=queue,
            viability=CommitmentViability.RESTORED,
            constraint_kind=CommitmentConstraintKind.CLEARED,
        )

    _record(initial=initial, replacements=replacements, viability_ledger=ledger, queue=queue)
    restored = _record(
        initial=initial,
        replacements=replacements,
        viability_ledger=ledger,
        queue=queue,
        observation_id="viability:452:restored",
        semantic_minute=135,
        viability=CommitmentViability.RESTORED,
        constraint_kind=CommitmentConstraintKind.CLEARED,
        constraint_ref="route-state:temporary-crossing-open",
        evidence_ref="claim:crossing-open",
        provenance_root="notice:crossing-open",
    )
    assert ledger.history_for(SECOND)[-1] == restored


def test_replay_is_idempotent_and_conflicting_identity_fails_closed():
    initial = _initial()
    replacements = _replacements()
    ledger = AssistanceCommitmentViabilityLedger()
    queue = NpcReplanQueue()
    first = _record(initial=initial, replacements=replacements, viability_ledger=ledger, queue=queue)
    replay = _record(initial=initial, replacements=replacements, viability_ledger=ledger, queue=queue)
    assert replay == first
    assert len(queue.pending) == 1

    with pytest.raises(ValueError, match="conflicting content"):
        _record(
            initial=initial,
            replacements=replacements,
            viability_ledger=ledger,
            queue=queue,
            constraint_ref="route-state:different",
        )


def test_bridge_has_no_execution_or_social_side_effect_surface():
    source = Path("tools/global_npc_assistance_replacement_viability.py").read_text(encoding="utf-8")
    forbidden = (
        "REQUEST_AUTOPTU",
        "reserve_route",
        "allocate_resource",
        "move_actor",
        "relationship_delta",
        "grant_permission",
        ".commitments =",
    )
    for token in forbidden:
        assert token not in source
