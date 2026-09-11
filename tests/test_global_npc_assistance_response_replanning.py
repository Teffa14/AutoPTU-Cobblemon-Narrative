import pytest

from tools.global_npc_ai import AgentMode, AgendaDecision, Decision, Handoff, NpcAgentState, NpcIntent
from tools.global_npc_assistance_response_dispatch import schedule_assistance_response_from_action
from tools.global_npc_assistance_response_replanning import (
    acknowledge_assistance_response_for_replanning,
    advance_assistance_response_for_replanning,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, CoordinatedDecision, GlobalNpcWorldEventCoordinator

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
OREN = "ouros.npc.oren_vale"
REQUEST_ACTION_ID = "action:request-teo-pass427"
RESPONSE_ACTION_ID = "action:teo-response-pass427"
EVENT_ID = "event:teo-response-pass427"
RECEIVER_CLAIM = "claim:mara-response-pass427"


def _record(ledger: WorldActionIntentLedger, *, action_id: str, agent_id: str, intent_id: str, kind: str, target_ref: str, minute: int, trigger_id: str):
    coordinated = CoordinatedDecision(
        agent_id=agent_id,
        trigger_ids=(trigger_id,),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(agent_id=agent_id, intent_id=intent_id, kind=kind, score=427, handoff=Handoff.NONE, target_ref=target_ref),
            source_type="SITUATIONAL_INTENT",
            source_ref=intent_id,
        ),
    )
    return ledger.record_from_replan(action_id=action_id, coordinated_decision=coordinated, semantic_minute=minute)


def _system(*, response_kind: str = "ACCEPT_ASSISTANCE_REQUEST", latency: int = 2, available: bool = True, local_ack: bool = False):
    action_ledger = WorldActionIntentLedger()
    _record(action_ledger, action_id=REQUEST_ACTION_ID, agent_id=MARA, intent_id="intent:request-field-support-pass427", kind="REQUEST_ASSISTANCE", target_ref=TEO, minute=1000, trigger_id="trigger:warning-pass427")
    _record(action_ledger, action_id=RESPONSE_ACTION_ID, agent_id=TEO, intent_id=f"intent:{response_kind.lower()}:pass427", kind=response_kind, target_ref=MARA, minute=1002, trigger_id="replan:information:event:request-pass427")

    queue = InformationEventQueue(
        channels={"channel:field-radio": CommunicationChannel(channel_id="channel:field-radio", kind="RADIO", latency_minutes=latency, available=available, requires_local_projection=local_ack)},
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO), OREN: KnowledgeLedger(OREN)},
    )
    consider_response = NpcIntent(
        intent_id="intent:mara-consider-response-pass427",
        kind="CONSIDER_ASSISTANCE_RESPONSE",
        base_priority=10,
        urgency=8,
        required_knowledge=frozenset({RECEIVER_CLAIM}),
        target_ref="assignment:field-support-pass427",
    )
    agents = {
        MARA: NpcAgentState(agent_id=MARA, mode=AgentMode.OFFSCREEN_NAMED, region_ref="marea-interior", location_ref="marea-field-office"),
        OREN: NpcAgentState(agent_id=OREN, mode=AgentMode.OFFSCREEN_NAMED, region_ref="marea-interior", location_ref="marea-field-office"),
    }
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents=agents,
        agendas={
            MARA: AgentAgendaProfile(situational_intents=(consider_response,)),
            OREN: AgentAgendaProfile(situational_intents=(consider_response,)),
        },
    )
    schedule_assistance_response_from_action(
        action_ledger=action_ledger,
        information_queue=queue,
        request_action_id=REQUEST_ACTION_ID,
        response_action_id=RESPONSE_ACTION_ID,
        event_id=EVENT_ID,
        message_id="message:teo-response-pass427",
        source_claim_id="claim:teo-response-pass427",
        receiver_claim_id=RECEIVER_CLAIM,
        channel_id="channel:field-radio",
        created_minute=1003,
        receiver_trust_in_sender=20,
    )
    return action_ledger, coordinator


@pytest.mark.parametrize("kind", ["ACCEPT_ASSISTANCE_REQUEST", "DEFER_ASSISTANCE_REQUEST", "REJECT_ASSISTANCE_REQUEST", "COUNTERPROPOSE_ASSISTANCE_REQUEST"])
def test_delivered_response_wakes_only_original_requester(kind: str) -> None:
    action_ledger, coordinator = _system(response_kind=kind)
    outcome = advance_assistance_response_for_replanning(
        action_ledger=action_ledger,
        coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID,
        response_action_id=RESPONSE_ACTION_ID,
        event_id=EVENT_ID,
        semantic_minute=1005,
    )

    assert outcome.delivery_status == "DELIVERED"
    assert outcome.wake_status == "WAKE_SCHEDULED"
    assert outcome.provenance_root == RESPONSE_ACTION_ID
    assert outcome.response_kind == kind
    assert len(outcome.decisions) == 1
    assert outcome.decisions[0].agent_id == MARA
    assert outcome.decisions[0].decision.decision.kind == "CONSIDER_ASSISTANCE_RESPONSE"
    assert RECEIVER_CLAIM in coordinator.agents[MARA].knowledge
    assert RESPONSE_ACTION_ID in coordinator.agents[MARA].memory_refs
    assert coordinator.agents[OREN].knowledge == frozenset()
    assert coordinator.agents[OREN].memory_refs == ()


def test_queued_failed_or_zero_budget_response_cannot_wake_requester() -> None:
    action_ledger, coordinator = _system(latency=5)
    queued = advance_assistance_response_for_replanning(
        action_ledger=action_ledger, coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID, response_action_id=RESPONSE_ACTION_ID,
        event_id=EVENT_ID, semantic_minute=1004,
    )
    assert queued.delivery_status == "QUEUED"
    assert queued.decisions == ()
    assert coordinator.agents[MARA].knowledge == frozenset()

    action_ledger, coordinator = _system(latency=0, available=False)
    failed = advance_assistance_response_for_replanning(
        action_ledger=action_ledger, coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID, response_action_id=RESPONSE_ACTION_ID,
        event_id=EVENT_ID, semantic_minute=1003,
    )
    assert failed.delivery_status == "FAILED_CHANNEL_UNAVAILABLE"
    assert failed.decisions == ()

    action_ledger, coordinator = _system(latency=0)
    deferred = advance_assistance_response_for_replanning(
        action_ledger=action_ledger, coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID, response_action_id=RESPONSE_ACTION_ID,
        event_id=EVENT_ID, semantic_minute=1003, delivery_budget=0,
    )
    assert deferred.delivery_status == "QUEUED"
    assert deferred.decisions == ()


def test_local_ack_requires_acceptance_before_requester_replans() -> None:
    action_ledger, coordinator = _system(latency=0, local_ack=True)
    waiting = advance_assistance_response_for_replanning(
        action_ledger=action_ledger, coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID, response_action_id=RESPONSE_ACTION_ID,
        event_id=EVENT_ID, semantic_minute=1003,
    )
    assert waiting.delivery_status == "WAITING_LOCAL_ACK"
    assert waiting.decisions == ()

    accepted = acknowledge_assistance_response_for_replanning(
        action_ledger=action_ledger, coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID, response_action_id=RESPONSE_ACTION_ID,
        event_id=EVENT_ID, semantic_minute=1004, accepted=True,
    )
    assert accepted.delivery_status == "DELIVERED"
    assert accepted.wake_status == "WAKE_SCHEDULED"
    assert accepted.provenance_root == RESPONSE_ACTION_ID
    assert len(accepted.decisions) == 1
    assert accepted.decisions[0].agent_id == MARA


def test_rejected_local_ack_leaves_requester_unchanged() -> None:
    action_ledger, coordinator = _system(latency=0, local_ack=True)
    advance_assistance_response_for_replanning(
        action_ledger=action_ledger, coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID, response_action_id=RESPONSE_ACTION_ID,
        event_id=EVENT_ID, semantic_minute=1003,
    )
    rejected = acknowledge_assistance_response_for_replanning(
        action_ledger=action_ledger, coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID, response_action_id=RESPONSE_ACTION_ID,
        event_id=EVENT_ID, semantic_minute=1004, accepted=False,
    )
    assert rejected.delivery_status == "FAILED_CHANNEL_UNAVAILABLE"
    assert rejected.decisions == ()
    assert coordinator.agents[MARA].knowledge == frozenset()


def test_tampered_response_provenance_fails_before_delivery() -> None:
    action_ledger, coordinator = _system()
    envelope = coordinator.information_queue.envelope_provenance(EVENT_ID)
    source = coordinator.information_queue.ledgers[TEO].claims[envelope.source_claim_id]
    coordinator.information_queue.ledgers[TEO].claims[envelope.source_claim_id] = source.__class__(
        claim_id=source.claim_id, subject=source.subject, value=source.value,
        source_kind=source.source_kind, source_agent_id=source.source_agent_id,
        semantic_minute=source.semantic_minute, confidence=source.confidence,
        provenance_root="action:tampered-pass427", parent_claim_id=source.parent_claim_id,
        message_id=source.message_id,
    )
    with pytest.raises(ValueError, match="provenance root mismatch"):
        advance_assistance_response_for_replanning(
            action_ledger=action_ledger, coordinator=coordinator,
            request_action_id=REQUEST_ACTION_ID, response_action_id=RESPONSE_ACTION_ID,
            event_id=EVENT_ID, semantic_minute=1005,
        )
    assert coordinator.agents[MARA].knowledge == frozenset()
