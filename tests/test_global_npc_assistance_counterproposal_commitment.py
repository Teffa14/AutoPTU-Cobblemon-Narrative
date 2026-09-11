from dataclasses import replace

import pytest

from tools.global_npc_ai import (
    AgendaDecision,
    AgentMode,
    Decision,
    Handoff,
    NpcAgentState,
    PlanningContext,
    choose_agenda_intent,
    schedule_state,
)
from tools.global_npc_assistance_counterproposal import (
    AssistanceCounterproposalLedger,
    record_assistance_counterproposal_terms,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    materialize_counterproposal_assistance_commitment,
)
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import (
    AgentAgendaProfile,
    CoordinatedDecision,
    GlobalNpcWorldEventCoordinator,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
REQUEST = "action:request-pass435"
RESPONSE = "action:counter-pass435"
DECISION = "action:accept-counter-pass435"
PROPOSAL = "proposal:pass435"
REQUEST_TRIGGER = "replan:information:event:request-pass435"
TERMS_TRIGGER = "replan:information:event:terms-pass435"
COMMITMENT = "commitment:negotiated-help-pass435"


def _record(
    ledger,
    *,
    action_id,
    agent_id,
    kind,
    target_ref,
    minute,
    trigger,
    source_ref=None,
):
    intent_id = f"intent:{kind.lower()}:pass435"
    coordinated = CoordinatedDecision(
        agent_id=agent_id,
        trigger_ids=(trigger,),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(
                agent_id=agent_id,
                intent_id=intent_id,
                kind=kind,
                score=435,
                handoff=Handoff.NONE,
                target_ref=target_ref,
            ),
            source_type="SITUATIONAL_INTENT",
            source_ref=source_ref if source_ref is not None else intent_id,
        ),
    )
    return ledger.record_from_replan(
        action_id=action_id,
        coordinated_decision=coordinated,
        semantic_minute=minute,
    )


def _system(*, decision_kind="ACCEPT_ASSISTANCE_COUNTERPROPOSAL", with_end=True):
    actions = WorldActionIntentLedger()
    _record(
        actions,
        action_id=REQUEST,
        agent_id=MARA,
        kind="REQUEST_ASSISTANCE",
        target_ref=TEO,
        minute=1300,
        trigger="trigger:field-need-pass435",
    )
    _record(
        actions,
        action_id=RESPONSE,
        agent_id=TEO,
        kind="COUNTERPROPOSE_ASSISTANCE_REQUEST",
        target_ref=MARA,
        minute=1303,
        trigger=REQUEST_TRIGGER,
    )

    proposals = AssistanceCounterproposalLedger()
    record_assistance_counterproposal_terms(
        action_ledger=actions,
        proposal_ledger=proposals,
        request_action_id=REQUEST,
        response_action_id=RESPONSE,
        proposal_id=PROPOSAL,
        request_delivery_trigger_id=REQUEST_TRIGGER,
        proposed_start_minute=1330,
        proposed_end_minute=1360 if with_end else None,
        location_ref="ouros.marea.field_office",
        scope_ref="diagnose_pump_only",
        alternative_ref="remote_parts_list",
        expires_minute=1325,
    )
    _record(
        actions,
        action_id=DECISION,
        agent_id=MARA,
        kind=decision_kind,
        target_ref=TEO,
        minute=1310,
        trigger=TERMS_TRIGGER,
        source_ref=PROPOSAL,
    )

    queue = InformationEventQueue(
        channels={
            "channel:radio": CommunicationChannel(
                channel_id="channel:radio",
                kind="RADIO",
                latency_minutes=0,
                available=True,
            )
        },
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)},
    )
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents={
            MARA: NpcAgentState(
                MARA,
                AgentMode.OFFSCREEN_NAMED,
                "marea-interior",
                "marea-field-office",
            ),
            TEO: NpcAgentState(
                TEO,
                AgentMode.OFFSCREEN_NAMED,
                "marea-interior",
                "marea-workshop",
            ),
        },
        agendas={TEO: AgentAgendaProfile()},
    )
    return actions, proposals, coordinator


def _materialize(actions, proposals, coordinator, ledger=None, **overrides):
    ledger = ledger or AssistanceCounterproposalCommitmentLedger()
    values = dict(
        action_ledger=actions,
        proposal_ledger=proposals,
        commitment_ledger=ledger,
        coordinator=coordinator,
        proposal_id=PROPOSAL,
        decision_action_id=DECISION,
        commitment_id=COMMITMENT,
        intent_kind="FULFILL_NEGOTIATED_ASSISTANCE",
        materialized_minute=1311,
        priority=8,
        hard=False,
        grace_minutes=5,
    )
    values.update(overrides)
    return ledger, materialize_counterproposal_assistance_commitment(**values)


def test_exact_accepted_window_becomes_responder_owned_commitment():
    actions, proposals, coordinator = _system()
    ledger, outcome = _materialize(actions, proposals, coordinator)

    assert outcome.record.proposal_id == PROPOSAL
    assert outcome.record.provenance_root == DECISION
    assert outcome.record.requester_id == MARA
    assert outcome.record.responder_id == TEO
    assert outcome.record.start_minute == 1330
    assert outcome.record.end_minute == 1360
    assert outcome.record.location_ref == "ouros.marea.field_office"
    assert outcome.record.scope_ref == "diagnose_pump_only"
    assert outcome.record.alternative_ref == "remote_parts_list"
    assert outcome.commitment.target_ref == MARA
    assert coordinator.agendas[TEO].commitments == (outcome.commitment,)
    assert schedule_state(outcome.commitment, 1320) == "UPCOMING"
    assert schedule_state(outcome.commitment, 1340) == "DUE"
    assert ledger.records[COMMITMENT] == outcome.record


def test_terms_are_metadata_not_travel_or_tactical_permission():
    actions, proposals, coordinator = _system()
    before_location = coordinator.agents[TEO].location_ref
    _, outcome = _materialize(actions, proposals, coordinator, hard=True)

    assert coordinator.agents[TEO].location_ref == before_location
    assert outcome.commitment.required_permissions == frozenset()
    assert outcome.commitment.requires_structured_mechanics is False
    assert not hasattr(outcome.commitment, "location_ref")
    assert not hasattr(outcome.commitment, "scope_ref")


def test_structured_mechanics_handoff_appears_only_when_commitment_is_due():
    actions, proposals, coordinator = _system()
    _materialize(
        actions,
        proposals,
        coordinator,
        hard=True,
        requires_structured_mechanics=True,
    )
    decision = choose_agenda_intent(
        coordinator.agents[TEO],
        commitments=coordinator.agendas[TEO].commitments,
        context=PlanningContext(1340),
    )
    assert decision.source_type == "COMMITMENT"
    assert decision.decision.kind == "FULFILL_NEGOTIATED_ASSISTANCE"
    assert decision.decision.handoff is Handoff.REQUEST_AUTOPTU


def test_rejection_or_wrong_proposal_binding_cannot_create_commitment():
    actions, proposals, coordinator = _system(
        decision_kind="REJECT_ASSISTANCE_COUNTERPROPOSAL"
    )
    with pytest.raises(ValueError, match="requires requester acceptance"):
        _materialize(actions, proposals, coordinator)

    actions, proposals, coordinator = _system()
    actions.records[DECISION] = replace(actions.records[DECISION], source_ref="proposal:wrong")
    with pytest.raises(ValueError, match="exact proposal"):
        _materialize(actions, proposals, coordinator)


def test_incomplete_or_elapsed_negotiated_window_fails_closed():
    actions, proposals, coordinator = _system(with_end=False)
    with pytest.raises(ValueError, match="complete scheduled window"):
        _materialize(actions, proposals, coordinator)

    actions, proposals, coordinator = _system()
    with pytest.raises(ValueError, match="already in the past"):
        _materialize(
            actions,
            proposals,
            coordinator,
            materialized_minute=1331,
        )


def test_expired_or_tampered_chain_cannot_materialize():
    actions, proposals, coordinator = _system()
    actions.records[DECISION] = replace(actions.records[DECISION], semantic_minute=1326)
    with pytest.raises(ValueError, match="expired"):
        _materialize(actions, proposals, coordinator, materialized_minute=1326)

    actions, proposals, coordinator = _system()
    original = proposals.records[PROPOSAL]
    proposals.records[PROPOSAL] = replace(original, provenance_root="action:tampered")
    with pytest.raises(ValueError, match="provenance"):
        _materialize(actions, proposals, coordinator)


def test_replay_snapshot_and_conflicting_commitment_identity():
    actions, proposals, coordinator = _system()
    ledger = AssistanceCounterproposalCommitmentLedger()
    _, first = _materialize(actions, proposals, coordinator, ledger=ledger)
    _, replay = _materialize(actions, proposals, coordinator, ledger=ledger)
    assert replay == first
    assert len(coordinator.agendas[TEO].commitments) == 1

    restored = AssistanceCounterproposalCommitmentLedger.from_snapshot(ledger.snapshot())
    assert restored.records[COMMITMENT] == first.record

    with pytest.raises(ValueError, match="conflicting"):
        _materialize(actions, proposals, coordinator, ledger=ledger, priority=9)
