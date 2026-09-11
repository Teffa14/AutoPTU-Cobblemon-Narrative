import pytest

from tools.global_npc_ai import AgentMode, AgendaDecision, Decision, Handoff, NpcAgentState, NpcIntent
from tools.global_npc_assistance_request_dispatch import schedule_assistance_request_from_action
from tools.global_npc_assistance_request_replanning import advance_assistance_request_for_replanning
from tools.global_npc_assistance_response import record_assistance_response_from_replan
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
REQUEST_ACTION_ID = "action:request-teo-pass425"
REQUEST_EVENT_ID = "event:request-teo-pass425"
RECEIVER_CLAIM_ID = "claim:teo-request-pass425"
RESPONSE_ACTION_ID = "action:teo-response-pass425"


def _request_action_ledger() -> WorldActionIntentLedger:
    ledger = WorldActionIntentLedger()
    coordinated = CoordinatedDecision(
        agent_id=MARA,
        trigger_ids=("trigger:field-warning-pass425",),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(
                agent_id=MARA,
                intent_id="intent:request-field-support-pass425",
                kind="REQUEST_ASSISTANCE",
                score=425,
                handoff=Handoff.NONE,
                target_ref=TEO,
            ),
            source_type="SITUATIONAL_INTENT",
            source_ref="intent:request-field-support-pass425",
        ),
    )
    ledger.record_from_replan(
        action_id=REQUEST_ACTION_ID,
        coordinated_decision=coordinated,
        semantic_minute=800,
    )
    return ledger


def _system(*, deliver: bool = True):
    queue = InformationEventQueue(
        channels={
            "channel:field-radio": CommunicationChannel(
                channel_id="channel:field-radio",
                kind="RADIO",
                latency_minutes=0 if deliver else 10,
                available=True,
            )
        },
        ledgers={
            MARA: KnowledgeLedger(MARA),
            TEO: KnowledgeLedger(TEO),
        },
    )
    agents = {
        TEO: NpcAgentState(
            agent_id=TEO,
            mode=AgentMode.OFFSCREEN_NAMED,
            region_ref="marea-interior",
            location_ref="marea-workshop",
        )
    }
    consider = NpcIntent(
        intent_id="intent:teo-consider-request-pass425",
        kind="CONSIDER_ASSISTANCE_REQUEST",
        base_priority=10,
        urgency=7,
        required_knowledge=frozenset({RECEIVER_CLAIM_ID}),
        target_ref=REQUEST_ACTION_ID,
    )
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents=agents,
        agendas={TEO: AgentAgendaProfile(situational_intents=(consider,))},
    )
    ledger = _request_action_ledger()
    schedule_assistance_request_from_action(
        action_ledger=ledger,
        information_queue=queue,
        action_id=REQUEST_ACTION_ID,
        event_id=REQUEST_EVENT_ID,
        message_id="message:request-teo-pass425",
        source_claim_id="claim:mara-request-teo-pass425",
        receiver_claim_id=RECEIVER_CLAIM_ID,
        channel_id="channel:field-radio",
        created_minute=801,
        receiver_trust_in_sender=20,
    )
    if deliver:
        outcome = advance_assistance_request_for_replanning(
            action_ledger=ledger,
            coordinator=coordinator,
            action_id=REQUEST_ACTION_ID,
            event_id=REQUEST_EVENT_ID,
            semantic_minute=801,
        )
        assert outcome.delivery_status == "DELIVERED"
    return ledger, coordinator


def _response_decision(
    kind: str,
    *,
    agent_id: str = TEO,
    target_ref: str | None = MARA,
    trigger_id: str = f"replan:information:{REQUEST_EVENT_ID}",
    handoff: Handoff = Handoff.NONE,
) -> CoordinatedDecision:
    intent_id = f"intent:{kind.lower()}:pass425"
    return CoordinatedDecision(
        agent_id=agent_id,
        trigger_ids=(trigger_id,),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(
                agent_id=agent_id,
                intent_id=intent_id,
                kind=kind,
                score=425,
                handoff=handoff,
                target_ref=target_ref,
            ),
            source_type="SITUATIONAL_INTENT",
            source_ref=intent_id,
        ),
    )


@pytest.mark.parametrize(
    "kind",
    [
        "ACCEPT_ASSISTANCE_REQUEST",
        "DEFER_ASSISTANCE_REQUEST",
        "REJECT_ASSISTANCE_REQUEST",
        "COUNTERPROPOSE_ASSISTANCE_REQUEST",
    ],
)
def test_each_recipient_response_becomes_its_own_durable_world_action(kind: str) -> None:
    ledger, coordinator = _system()
    coordinated = _response_decision(kind)

    outcome = record_assistance_response_from_replan(
        action_ledger=ledger,
        coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID,
        request_event_id=REQUEST_EVENT_ID,
        response_action_id=RESPONSE_ACTION_ID,
        coordinated_decision=coordinated,
        semantic_minute=802,
    )

    assert outcome.request_action_id == REQUEST_ACTION_ID
    assert outcome.requester_id == MARA
    assert outcome.responder_id == TEO
    assert outcome.response_kind == kind
    assert outcome.record.target_ref == MARA
    assert outcome.record.status == "PLANNED"
    assert ledger.records[REQUEST_ACTION_ID].status == "PLANNED"
    assert ledger.records[RESPONSE_ACTION_ID] == outcome.record


def test_response_recording_is_idempotent_and_snapshot_durable() -> None:
    ledger, coordinator = _system()
    coordinated = _response_decision("ACCEPT_ASSISTANCE_REQUEST")

    first = record_assistance_response_from_replan(
        action_ledger=ledger,
        coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID,
        request_event_id=REQUEST_EVENT_ID,
        response_action_id=RESPONSE_ACTION_ID,
        coordinated_decision=coordinated,
        semantic_minute=802,
    )
    second = record_assistance_response_from_replan(
        action_ledger=ledger,
        coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID,
        request_event_id=REQUEST_EVENT_ID,
        response_action_id=RESPONSE_ACTION_ID,
        coordinated_decision=coordinated,
        semantic_minute=802,
    )

    assert first.record == second.record
    restored = WorldActionIntentLedger.from_snapshot(ledger.snapshot())
    assert restored.records[REQUEST_ACTION_ID] == ledger.records[REQUEST_ACTION_ID]
    assert restored.records[RESPONSE_ACTION_ID] == first.record


def test_same_response_action_id_cannot_be_reused_for_a_different_choice() -> None:
    ledger, coordinator = _system()
    record_assistance_response_from_replan(
        action_ledger=ledger,
        coordinator=coordinator,
        request_action_id=REQUEST_ACTION_ID,
        request_event_id=REQUEST_EVENT_ID,
        response_action_id=RESPONSE_ACTION_ID,
        coordinated_decision=_response_decision("ACCEPT_ASSISTANCE_REQUEST"),
        semantic_minute=802,
    )

    with pytest.raises(ValueError, match="conflicting content"):
        record_assistance_response_from_replan(
            action_ledger=ledger,
            coordinator=coordinator,
            request_action_id=REQUEST_ACTION_ID,
            request_event_id=REQUEST_EVENT_ID,
            response_action_id=RESPONSE_ACTION_ID,
            coordinated_decision=_response_decision("REJECT_ASSISTANCE_REQUEST"),
            semantic_minute=802,
        )


def test_response_requires_terminal_delivery_and_recipient_claim() -> None:
    ledger, coordinator = _system(deliver=False)
    with pytest.raises(ValueError, match="terminal DELIVERED"):
        record_assistance_response_from_replan(
            action_ledger=ledger,
            coordinator=coordinator,
            request_action_id=REQUEST_ACTION_ID,
            request_event_id=REQUEST_EVENT_ID,
            response_action_id=RESPONSE_ACTION_ID,
            coordinated_decision=_response_decision("DEFER_ASSISTANCE_REQUEST"),
            semantic_minute=802,
        )


def test_response_must_be_the_delivered_recipient_own_decision() -> None:
    ledger, coordinator = _system()
    with pytest.raises(ValueError, match="actor is not the delivered recipient"):
        record_assistance_response_from_replan(
            action_ledger=ledger,
            coordinator=coordinator,
            request_action_id=REQUEST_ACTION_ID,
            request_event_id=REQUEST_EVENT_ID,
            response_action_id=RESPONSE_ACTION_ID,
            coordinated_decision=_response_decision("REJECT_ASSISTANCE_REQUEST", agent_id=MARA),
            semantic_minute=802,
        )


def test_response_requires_exact_delivery_replan_trigger() -> None:
    ledger, coordinator = _system()
    with pytest.raises(ValueError, match="request-delivery replan trigger"):
        record_assistance_response_from_replan(
            action_ledger=ledger,
            coordinator=coordinator,
            request_action_id=REQUEST_ACTION_ID,
            request_event_id=REQUEST_EVENT_ID,
            response_action_id=RESPONSE_ACTION_ID,
            coordinated_decision=_response_decision(
                "DEFER_ASSISTANCE_REQUEST",
                trigger_id="replan:information:event:other",
            ),
            semantic_minute=802,
        )


def test_response_kind_and_reply_target_are_closed_sets() -> None:
    ledger, coordinator = _system()
    with pytest.raises(ValueError, match="unsupported assistance response kind"):
        record_assistance_response_from_replan(
            action_ledger=ledger,
            coordinator=coordinator,
            request_action_id=REQUEST_ACTION_ID,
            request_event_id=REQUEST_EVENT_ID,
            response_action_id=RESPONSE_ACTION_ID,
            coordinated_decision=_response_decision("IGNORE_ASSISTANCE_REQUEST"),
            semantic_minute=802,
        )

    with pytest.raises(ValueError, match="original requester"):
        record_assistance_response_from_replan(
            action_ledger=ledger,
            coordinator=coordinator,
            request_action_id=REQUEST_ACTION_ID,
            request_event_id=REQUEST_EVENT_ID,
            response_action_id=RESPONSE_ACTION_ID,
            coordinated_decision=_response_decision(
                "COUNTERPROPOSE_ASSISTANCE_REQUEST",
                target_ref="ouros.npc.oren_vale",
            ),
            semantic_minute=802,
        )


def test_response_choice_cannot_hide_an_autoptu_handoff() -> None:
    ledger, coordinator = _system()
    with pytest.raises(ValueError, match="cannot itself be an AutoPTU handoff"):
        record_assistance_response_from_replan(
            action_ledger=ledger,
            coordinator=coordinator,
            request_action_id=REQUEST_ACTION_ID,
            request_event_id=REQUEST_EVENT_ID,
            response_action_id=RESPONSE_ACTION_ID,
            coordinated_decision=_response_decision(
                "ACCEPT_ASSISTANCE_REQUEST",
                handoff=Handoff.REQUEST_AUTOPTU,
            ),
            semantic_minute=802,
        )


def test_tampered_recipient_provenance_fails_closed() -> None:
    ledger, coordinator = _system()
    claim = coordinator.information_queue.ledgers[TEO].claims[RECEIVER_CLAIM_ID]
    coordinator.information_queue.ledgers[TEO].claims[RECEIVER_CLAIM_ID] = claim.__class__(
        claim_id=claim.claim_id,
        subject=claim.subject,
        value=claim.value,
        source_kind=claim.source_kind,
        source_agent_id=claim.source_agent_id,
        semantic_minute=claim.semantic_minute,
        confidence=claim.confidence,
        provenance_root="action:tampered-pass425",
        parent_claim_id=claim.parent_claim_id,
        message_id=claim.message_id,
    )

    with pytest.raises(ValueError, match="lost request provenance"):
        record_assistance_response_from_replan(
            action_ledger=ledger,
            coordinator=coordinator,
            request_action_id=REQUEST_ACTION_ID,
            request_event_id=REQUEST_EVENT_ID,
            response_action_id=RESPONSE_ACTION_ID,
            coordinated_decision=_response_decision("REJECT_ASSISTANCE_REQUEST"),
            semantic_minute=802,
        )
