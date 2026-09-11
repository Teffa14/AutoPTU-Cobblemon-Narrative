import pytest

from tools.global_npc_ai import AgentMode, AgendaDecision, Decision, Handoff, NpcAgentState, NpcIntent
from tools.global_npc_assistance_request_dispatch import schedule_assistance_request_from_action
from tools.global_npc_assistance_request_replanning import (
    acknowledge_assistance_request_for_replanning,
    advance_assistance_request_for_replanning,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import (
    AgentAgendaProfile,
    CoordinatedDecision,
    GlobalNpcWorldEventCoordinator,
)


MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
OREN = "ouros.npc.oren_vale"
ACTION_ID = "action:request-teo-pass424"
EVENT_ID = "event:request-teo-pass424"
RECEIVER_CLAIM = "claim:teo-request-pass424"


def _action_ledger() -> WorldActionIntentLedger:
    ledger = WorldActionIntentLedger()
    coordinated = CoordinatedDecision(
        agent_id=MARA,
        trigger_ids=("trigger:warning-pass424",),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(
                agent_id=MARA,
                intent_id="intent:request-field-support-pass424",
                kind="REQUEST_ASSISTANCE",
                score=420,
                handoff=Handoff.NONE,
                target_ref=TEO,
            ),
            source_type="SITUATIONAL_INTENT",
            source_ref="intent:request-field-support-pass424",
        ),
    )
    ledger.record_from_replan(
        action_id=ACTION_ID,
        coordinated_decision=coordinated,
        semantic_minute=700,
    )
    return ledger


def _system(*, latency: int = 2, available: bool = True, local_ack: bool = False):
    queue = InformationEventQueue(
        channels={
            "channel:field-radio": CommunicationChannel(
                channel_id="channel:field-radio",
                kind="RADIO",
                latency_minutes=latency,
                available=available,
                requires_local_projection=local_ack,
            )
        },
        ledgers={
            MARA: KnowledgeLedger(MARA),
            TEO: KnowledgeLedger(TEO),
            OREN: KnowledgeLedger(OREN),
        },
    )
    agents = {
        TEO: NpcAgentState(
            agent_id=TEO,
            mode=AgentMode.OFFSCREEN_NAMED,
            region_ref="marea-interior",
            location_ref="marea-workshop",
        ),
        OREN: NpcAgentState(
            agent_id=OREN,
            mode=AgentMode.OFFSCREEN_NAMED,
            region_ref="marea-interior",
            location_ref="marea-field-office",
        ),
    }
    consider_request = NpcIntent(
        intent_id="intent:teo-consider-request-pass424",
        kind="CONSIDER_ASSISTANCE_REQUEST",
        base_priority=10,
        urgency=7,
        required_knowledge=frozenset({RECEIVER_CLAIM}),
        target_ref="assignment:field-support-pass424",
    )
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents=agents,
        agendas={
            TEO: AgentAgendaProfile(situational_intents=(consider_request,)),
            OREN: AgentAgendaProfile(situational_intents=(consider_request,)),
        },
    )
    action_ledger = _action_ledger()
    envelope = schedule_assistance_request_from_action(
        action_ledger=action_ledger,
        information_queue=queue,
        action_id=ACTION_ID,
        event_id=EVENT_ID,
        message_id="message:request-teo-pass424",
        source_claim_id="claim:mara-request-teo-pass424",
        receiver_claim_id=RECEIVER_CLAIM,
        channel_id="channel:field-radio",
        created_minute=701,
        receiver_trust_in_sender=20,
    )
    return action_ledger, coordinator, envelope


def test_only_selected_recipient_wakes_after_delivered_request() -> None:
    action_ledger, coordinator, _ = _system()

    outcome = advance_assistance_request_for_replanning(
        action_ledger=action_ledger,
        coordinator=coordinator,
        action_id=ACTION_ID,
        event_id=EVENT_ID,
        semantic_minute=703,
    )

    assert outcome.delivery_status == "DELIVERED"
    assert outcome.wake_status == "WAKE_SCHEDULED"
    assert outcome.provenance_root == ACTION_ID
    assert len(outcome.decisions) == 1
    assert outcome.decisions[0].agent_id == TEO
    assert outcome.decisions[0].decision.decision.kind == "CONSIDER_ASSISTANCE_REQUEST"
    assert RECEIVER_CLAIM in coordinator.agents[TEO].knowledge
    assert ACTION_ID in coordinator.agents[TEO].memory_refs
    assert coordinator.agents[OREN].knowledge == frozenset()
    assert coordinator.agents[OREN].memory_refs == ()


def test_queued_or_failed_request_does_not_wake_target() -> None:
    action_ledger, coordinator, _ = _system(latency=5)
    queued = advance_assistance_request_for_replanning(
        action_ledger=action_ledger,
        coordinator=coordinator,
        action_id=ACTION_ID,
        event_id=EVENT_ID,
        semantic_minute=704,
    )
    assert queued.delivery_status == "QUEUED"
    assert queued.decisions == ()
    assert coordinator.agents[TEO].knowledge == frozenset()

    action_ledger, coordinator, _ = _system(latency=0, available=False)
    failed = advance_assistance_request_for_replanning(
        action_ledger=action_ledger,
        coordinator=coordinator,
        action_id=ACTION_ID,
        event_id=EVENT_ID,
        semantic_minute=701,
    )
    assert failed.delivery_status == "FAILED_CHANNEL_UNAVAILABLE"
    assert failed.decisions == ()
    assert coordinator.agents[TEO].knowledge == frozenset()


def test_local_ack_wakes_only_after_acceptance() -> None:
    action_ledger, coordinator, _ = _system(latency=0, local_ack=True)
    waiting = advance_assistance_request_for_replanning(
        action_ledger=action_ledger,
        coordinator=coordinator,
        action_id=ACTION_ID,
        event_id=EVENT_ID,
        semantic_minute=701,
    )
    assert waiting.delivery_status == "WAITING_LOCAL_ACK"
    assert waiting.decisions == ()

    accepted = acknowledge_assistance_request_for_replanning(
        action_ledger=action_ledger,
        coordinator=coordinator,
        action_id=ACTION_ID,
        event_id=EVENT_ID,
        semantic_minute=702,
        accepted=True,
    )
    assert accepted.delivery_status == "DELIVERED"
    assert accepted.wake_status == "WAKE_SCHEDULED"
    assert accepted.provenance_root == ACTION_ID
    assert len(accepted.decisions) == 1
    assert accepted.decisions[0].agent_id == TEO


def test_rejected_local_ack_does_not_replan() -> None:
    action_ledger, coordinator, _ = _system(latency=0, local_ack=True)
    advance_assistance_request_for_replanning(
        action_ledger=action_ledger,
        coordinator=coordinator,
        action_id=ACTION_ID,
        event_id=EVENT_ID,
        semantic_minute=701,
    )
    rejected = acknowledge_assistance_request_for_replanning(
        action_ledger=action_ledger,
        coordinator=coordinator,
        action_id=ACTION_ID,
        event_id=EVENT_ID,
        semantic_minute=702,
        accepted=False,
    )
    assert rejected.delivery_status == "FAILED_CHANNEL_UNAVAILABLE"
    assert rejected.decisions == ()
    assert coordinator.agents[TEO].knowledge == frozenset()


def test_zero_delivery_budget_defers_without_false_wake() -> None:
    action_ledger, coordinator, _ = _system(latency=0)
    outcome = advance_assistance_request_for_replanning(
        action_ledger=action_ledger,
        coordinator=coordinator,
        action_id=ACTION_ID,
        event_id=EVENT_ID,
        semantic_minute=701,
        delivery_budget=0,
    )
    assert outcome.delivery_status == "QUEUED"
    assert outcome.decisions == ()


def test_tampered_source_provenance_fails_before_delivery() -> None:
    action_ledger, coordinator, envelope = _system()
    source = coordinator.information_queue.ledgers[MARA].claims[envelope.source_claim_id]
    coordinator.information_queue.ledgers[MARA].claims[envelope.source_claim_id] = source.__class__(
        claim_id=source.claim_id,
        subject=source.subject,
        value=source.value,
        source_kind=source.source_kind,
        source_agent_id=source.source_agent_id,
        semantic_minute=source.semantic_minute,
        confidence=source.confidence,
        provenance_root="action:tampered",
        parent_claim_id=source.parent_claim_id,
        message_id=source.message_id,
    )

    with pytest.raises(ValueError, match="provenance root mismatch"):
        advance_assistance_request_for_replanning(
            action_ledger=action_ledger,
            coordinator=coordinator,
            action_id=ACTION_ID,
            event_id=EVENT_ID,
            semantic_minute=703,
        )
    assert coordinator.agents[TEO].knowledge == frozenset()
