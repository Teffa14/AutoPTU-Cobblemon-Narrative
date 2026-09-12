import pytest

from tools.global_npc_ai import AgentMode, NpcAgentState, ScheduledCommitment
from tools.global_npc_assistance_commitment_lineage import (
    assert_assistance_lineage_agenda_consistency,
    resolve_assistance_commitment_lineage,
    validate_assistance_commitment_lineage_graph,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)
from tools.global_npc_assistance_renegotiation_replacement_commitment import (
    AssistanceRenegotiationReplacementCommitmentLedger,
    AssistanceRenegotiationReplacementCommitmentRecord,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator

REQUESTER = "ouros.npc.requester.451"
RESPONDER = "ouros.npc.responder.451"
ROOT = "commitment:451:root"
SECOND = "commitment:451:second"
THIRD = "commitment:451:third"


def _initial():
    ledger = AssistanceCounterproposalCommitmentLedger()
    ledger.add(
        AssistanceCounterproposalCommitmentRecord(
            commitment_id=ROOT,
            proposal_id="proposal:451:root",
            request_action_id="request:451",
            response_action_id="counter:451",
            decision_action_id="accept:451:root",
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
            provenance_root="accept:451:root",
        )
    )
    return ledger


def _replacement(commitment_id, parent_id, parent_provenance, proposal_id, decision_id, start, end, location):
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
        location_ref=location,
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


def _two_replacements():
    ledger = AssistanceRenegotiationReplacementCommitmentLedger()
    ledger.add(_replacement(SECOND, ROOT, "accept:451:root", "proposal:451:second", "decision:451:second", 140, 160, "site:b"))
    ledger.add(_replacement(THIRD, SECOND, "decision:451:second", "proposal:451:third", "decision:451:third", 180, 205, "site:c"))
    return ledger


def _coordinator(active_id=THIRD):
    windows = {
        ROOT: (100, 120),
        SECOND: (140, 160),
        THIRD: (180, 205),
    }
    start, end = windows[active_id]
    active = ScheduledCommitment(
        commitment_id=active_id,
        intent_kind="ASSIST_SITE_SURVEY",
        start_minute=start,
        end_minute=end,
        priority=6,
        hard=True,
        grace_minutes=5,
        required_knowledge=frozenset({"claim:access"}),
        required_permissions=frozenset({"permit:survey"}),
        target_ref=REQUESTER,
        requires_local_projection=False,
        requires_structured_mechanics=False,
    )
    ledgers = {REQUESTER: KnowledgeLedger(REQUESTER), RESPONDER: KnowledgeLedger(RESPONDER)}
    queue = InformationEventQueue(
        channels={"radio": CommunicationChannel("radio", "REMOTE_MESSAGE", 0)},
        ledgers=ledgers,
    )
    agents = {
        REQUESTER: NpcAgentState(REQUESTER, AgentMode.OFFSCREEN_NAMED, "ouros", "site"),
        RESPONDER: NpcAgentState(RESPONDER, AgentMode.OFFSCREEN_NAMED, "ouros", "workshop"),
    }
    return GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents=agents,
        agendas={RESPONDER: AgentAgendaProfile(commitments=(active,))},
    )


def test_resolves_arbitrary_replacement_generations_and_active_leaf():
    view = resolve_assistance_commitment_lineage(
        initial_ledger=_initial(), replacement_ledger=_two_replacements(), root_commitment_id=ROOT
    )
    assert [node.commitment_id for node in view.nodes] == [ROOT, SECOND, THIRD]
    assert [node.generation for node in view.nodes] == [0, 1, 2]
    assert view.active_commitment_id == THIRD
    assert view.replacement_count == 2
    assert assert_assistance_lineage_agenda_consistency(view=view, coordinator=_coordinator()).commitment_id == THIRD


def test_rejects_branching_replacement_history():
    replacements = _two_replacements()
    replacements.add(
        _replacement(
            "commitment:451:sibling",
            ROOT,
            "accept:451:root",
            "proposal:451:sibling",
            "decision:451:sibling",
            150,
            170,
            "site:d",
        )
    )
    with pytest.raises(ValueError, match="branches"):
        validate_assistance_commitment_lineage_graph(initial_ledger=_initial(), replacement_ledger=replacements)


def test_rejects_orphan_cycle_and_parent_provenance_tampering():
    orphan = AssistanceRenegotiationReplacementCommitmentLedger()
    orphan.add(_replacement(SECOND, "missing", "missing:prov", "proposal:o", "decision:o", 140, 160, "site:b"))
    with pytest.raises(ValueError, match="unknown parent"):
        validate_assistance_commitment_lineage_graph(initial_ledger=_initial(), replacement_ledger=orphan)

    cycle = AssistanceRenegotiationReplacementCommitmentLedger()
    cycle.add(_replacement(SECOND, THIRD, "decision:451:third", "proposal:c1", "decision:c1", 140, 160, "site:b"))
    cycle.add(_replacement(THIRD, SECOND, "decision:c1", "proposal:c2", "decision:c2", 180, 205, "site:c"))
    with pytest.raises(ValueError, match="cycle"):
        validate_assistance_commitment_lineage_graph(initial_ledger=_initial(), replacement_ledger=cycle)

    tampered = AssistanceRenegotiationReplacementCommitmentLedger()
    tampered.add(_replacement(SECOND, ROOT, "wrong-root", "proposal:t", "decision:t", 140, 160, "site:b"))
    with pytest.raises(ValueError, match="parent provenance mismatch"):
        validate_assistance_commitment_lineage_graph(initial_ledger=_initial(), replacement_ledger=tampered)


def test_old_generation_cannot_reappear_as_executable_agenda_work():
    view = resolve_assistance_commitment_lineage(
        initial_ledger=_initial(), replacement_ledger=_two_replacements(), root_commitment_id=ROOT
    )
    stale = _coordinator(active_id=SECOND)
    with pytest.raises(ValueError, match="latest executable commitment"):
        assert_assistance_lineage_agenda_consistency(view=view, coordinator=stale)


def test_lineage_view_has_no_tactical_or_social_execution_surface():
    import inspect
    import tools.global_npc_assistance_commitment_lineage as module

    source = inspect.getsource(module)
    assert all(
        token not in source
        for token in (
            "REQUEST_AUTOPTU",
            "reserve_route",
            "allocate_resource",
            "move_actor",
            "relationship_delta",
            "grant_permission",
            "adjudicate_blame",
        )
    )
