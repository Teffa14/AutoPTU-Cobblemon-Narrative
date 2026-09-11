import pytest

from tools.global_npc_ai import AgendaDecision, AgentMode, Decision, Handoff, NpcAgentState, PlanningContext, choose_agenda_intent, schedule_state
from tools.global_npc_assistance_acceptance_commitment import AssistanceCommitmentLedger, materialize_assistance_commitment
from tools.global_npc_assistance_response_dispatch import schedule_assistance_response_from_action
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, CoordinatedDecision, GlobalNpcWorldEventCoordinator

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
REQUEST = "action:request-pass428"
RESPONSE = "action:accept-pass428"
EVENT = "event:accept-pass428"


def _record(ledger, *, action_id, agent_id, kind, target_ref, minute, trigger):
    intent_id = f"intent:{kind.lower()}:pass428"
    decision = CoordinatedDecision(
        agent_id=agent_id,
        trigger_ids=(trigger,),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(agent_id, intent_id, kind, 428, Handoff.NONE, target_ref=target_ref),
            source_type="SITUATIONAL_INTENT",
            source_ref=intent_id,
        ),
    )
    return ledger.record_from_replan(action_id=action_id, coordinated_decision=decision, semantic_minute=minute)


def _system(*, response_kind="ACCEPT_ASSISTANCE_REQUEST", delivered=True):
    actions = WorldActionIntentLedger()
    _record(actions, action_id=REQUEST, agent_id=MARA, kind="REQUEST_ASSISTANCE", target_ref=TEO, minute=1000, trigger="trigger:need-help")
    _record(actions, action_id=RESPONSE, agent_id=TEO, kind=response_kind, target_ref=MARA, minute=1002, trigger="replan:information:event:request-pass428")
    queue = InformationEventQueue(
        channels={"channel:radio": CommunicationChannel("channel:radio", "RADIO", 0, True)},
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)},
    )
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents={
            MARA: NpcAgentState(MARA, AgentMode.OFFSCREEN_NAMED, "marea-interior", "marea-field-office"),
            TEO: NpcAgentState(TEO, AgentMode.OFFSCREEN_NAMED, "marea-interior", "marea-workshop"),
        },
        agendas={TEO: AgentAgendaProfile()},
    )
    schedule_assistance_response_from_action(
        action_ledger=actions,
        information_queue=queue,
        request_action_id=REQUEST,
        response_action_id=RESPONSE,
        event_id=EVENT,
        message_id="message:accept-pass428",
        source_claim_id="claim:teo-accept-pass428",
        receiver_claim_id="claim:mara-accept-pass428",
        channel_id="channel:radio",
        created_minute=1003,
    )
    if delivered:
        queue.process_due(1003)
    return actions, coordinator


def _materialize(actions, coordinator, ledger=None, **overrides):
    ledger = ledger or AssistanceCommitmentLedger()
    values = dict(
        action_ledger=actions,
        commitment_ledger=ledger,
        coordinator=coordinator,
        request_action_id=REQUEST,
        response_action_id=RESPONSE,
        response_event_id=EVENT,
        commitment_id="commitment:teo-help-pass428",
        intent_kind="FULFILL_ASSISTANCE_REQUEST",
        materialized_minute=1004,
        start_minute=1010,
        end_minute=1030,
        priority=7,
        hard=False,
        grace_minutes=5,
    )
    values.update(overrides)
    return ledger, materialize_assistance_commitment(**values)


def test_delivered_acceptance_creates_responder_owned_scheduled_commitment():
    actions, coordinator = _system()
    ledger, outcome = _materialize(actions, coordinator)

    assert outcome.record.provenance_root == RESPONSE
    assert outcome.record.responder_id == TEO
    assert outcome.record.requester_id == MARA
    assert outcome.commitment.target_ref == MARA
    assert coordinator.agendas[TEO].commitments == (outcome.commitment,)
    assert schedule_state(outcome.commitment, 1005) == "UPCOMING"
    assert schedule_state(outcome.commitment, 1015) == "DUE"
    assert ledger.records[outcome.record.commitment_id] == outcome.record


def test_commitment_enters_existing_agenda_without_implying_travel_or_completion():
    actions, coordinator = _system()
    before_location = coordinator.agents[TEO].location_ref
    _, outcome = _materialize(actions, coordinator, hard=True)
    decision = choose_agenda_intent(
        coordinator.agents[TEO],
        commitments=coordinator.agendas[TEO].commitments,
        context=PlanningContext(1015),
    )

    assert decision.source_type == "COMMITMENT"
    assert decision.decision.kind == "FULFILL_ASSISTANCE_REQUEST"
    assert decision.decision.handoff is Handoff.NONE
    assert coordinator.agents[TEO].location_ref == before_location
    assert outcome.record.start_minute == 1010


def test_structured_commitment_requests_autoptu_only_when_it_becomes_agenda_work():
    actions, coordinator = _system()
    _, _ = _materialize(actions, coordinator, requires_structured_mechanics=True)
    decision = choose_agenda_intent(
        coordinator.agents[TEO],
        commitments=coordinator.agendas[TEO].commitments,
        context=PlanningContext(1015),
    )
    assert decision.decision.handoff is Handoff.REQUEST_AUTOPTU


def test_non_accept_and_non_delivered_response_cannot_create_commitment():
    actions, coordinator = _system(response_kind="DEFER_ASSISTANCE_REQUEST")
    with pytest.raises(ValueError, match="only ACCEPT_ASSISTANCE_REQUEST"):
        _materialize(actions, coordinator)

    actions, coordinator = _system(delivered=False)
    with pytest.raises(ValueError, match="terminal DELIVERED"):
        _materialize(actions, coordinator)


def test_commitment_cannot_reserve_past_window_or_reverse_time():
    actions, coordinator = _system()
    with pytest.raises(ValueError, match="window in the past"):
        _materialize(actions, coordinator, materialized_minute=1012, start_minute=1010)
    with pytest.raises(ValueError, match="cannot precede"):
        _materialize(actions, coordinator, start_minute=1040, end_minute=1030)


def test_exact_replay_is_idempotent_and_conflicting_reuse_fails_closed():
    actions, coordinator = _system()
    ledger = AssistanceCommitmentLedger()
    _, first = _materialize(actions, coordinator, ledger=ledger)
    _, second = _materialize(actions, coordinator, ledger=ledger)
    assert first == second
    assert len(coordinator.agendas[TEO].commitments) == 1

    with pytest.raises(ValueError, match="conflicting"):
        _materialize(actions, coordinator, ledger=ledger, end_minute=1040)


def test_commitment_ledger_snapshot_preserves_acceptance_provenance():
    actions, coordinator = _system()
    ledger, outcome = _materialize(actions, coordinator)
    restored = AssistanceCommitmentLedger.from_snapshot(ledger.snapshot())
    assert restored.records[outcome.record.commitment_id] == outcome.record


def test_tampered_acceptance_provenance_fails_closed():
    actions, coordinator = _system()
    envelope = coordinator.information_queue.envelope_provenance(EVENT)
    claim = coordinator.information_queue.ledgers[TEO].claims[envelope.source_claim_id]
    coordinator.information_queue.ledgers[TEO].claims[envelope.source_claim_id] = claim.__class__(
        claim_id=claim.claim_id,
        subject=claim.subject,
        value=claim.value,
        source_kind=claim.source_kind,
        source_agent_id=claim.source_agent_id,
        semantic_minute=claim.semantic_minute,
        confidence=claim.confidence,
        provenance_root="action:tampered-pass428",
        parent_claim_id=claim.parent_claim_id,
        message_id=claim.message_id,
    )
    with pytest.raises(ValueError, match="lost response provenance"):
        _materialize(actions, coordinator)
