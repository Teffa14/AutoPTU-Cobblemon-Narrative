import pytest

from tools.global_npc_ai import AgendaDecision, Decision, Handoff
from tools.global_npc_assistance_response_dispatch import schedule_assistance_response_from_action
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, SourceKind
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import CoordinatedDecision

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
REQUEST_ACTION_ID = "action:request-teo-pass426"
RESPONSE_ACTION_ID = "action:teo-response-pass426"
EVENT_ID = "event:teo-response-pass426"


def _record(ledger: WorldActionIntentLedger, *, action_id: str, agent_id: str, intent_id: str, kind: str, target_ref: str, minute: int, trigger_id: str):
    coordinated = CoordinatedDecision(
        agent_id=agent_id,
        trigger_ids=(trigger_id,),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(agent_id=agent_id, intent_id=intent_id, kind=kind, score=426, handoff=Handoff.NONE, target_ref=target_ref),
            source_type="SITUATIONAL_INTENT",
            source_ref=intent_id,
        ),
    )
    return ledger.record_from_replan(action_id=action_id, coordinated_decision=coordinated, semantic_minute=minute)


def _ledger(response_kind: str = "ACCEPT_ASSISTANCE_REQUEST") -> WorldActionIntentLedger:
    ledger = WorldActionIntentLedger()
    _record(ledger, action_id=REQUEST_ACTION_ID, agent_id=MARA, intent_id="intent:request-field-support-pass426", kind="REQUEST_ASSISTANCE", target_ref=TEO, minute=900, trigger_id="trigger:warning-pass426")
    _record(ledger, action_id=RESPONSE_ACTION_ID, agent_id=TEO, intent_id=f"intent:{response_kind.lower()}:pass426", kind=response_kind, target_ref=MARA, minute=902, trigger_id="replan:information:event:request-pass426")
    return ledger


def _queue(*, available: bool = True, local_ack: bool = False, latency: int = 5) -> InformationEventQueue:
    return InformationEventQueue(
        channels={"channel:field-radio": CommunicationChannel(channel_id="channel:field-radio", kind="RADIO", latency_minutes=latency, available=available, requires_local_projection=local_ack)},
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)},
    )


def _dispatch(ledger: WorldActionIntentLedger, queue: InformationEventQueue):
    return schedule_assistance_response_from_action(
        action_ledger=ledger,
        information_queue=queue,
        request_action_id=REQUEST_ACTION_ID,
        response_action_id=RESPONSE_ACTION_ID,
        event_id=EVENT_ID,
        message_id="message:teo-response-pass426",
        source_claim_id="claim:teo-response-pass426",
        receiver_claim_id="claim:mara-response-pass426",
        channel_id="channel:field-radio",
        created_minute=903,
        receiver_trust_in_sender=20,
    )


@pytest.mark.parametrize("kind", ["ACCEPT_ASSISTANCE_REQUEST", "DEFER_ASSISTANCE_REQUEST", "REJECT_ASSISTANCE_REQUEST", "COUNTERPROPOSE_ASSISTANCE_REQUEST"])
def test_all_durable_response_kinds_can_be_scheduled_back_to_requester(kind: str) -> None:
    ledger = _ledger(kind)
    queue = _queue()
    envelope = _dispatch(ledger, queue)
    source = queue.ledgers[TEO].claims["claim:teo-response-pass426"]

    assert envelope.sender_id == TEO
    assert envelope.receiver_id == MARA
    assert source.source_kind is SourceKind.AUTHORED_START
    assert source.subject == f"assistance_response:{REQUEST_ACTION_ID}:{RESPONSE_ACTION_ID}"
    assert source.value == kind
    assert source.provenance_root == RESPONSE_ACTION_ID
    assert queue.statuses[EVENT_ID] is DeliveryStatus.QUEUED
    assert queue.ledgers[MARA].claims == {}


def test_successful_delivery_preserves_response_action_provenance() -> None:
    queue = _queue(latency=0)
    envelope = _dispatch(_ledger("REJECT_ASSISTANCE_REQUEST"), queue)
    result = queue.process_due(903)

    assert result[0]["status"] == DeliveryStatus.DELIVERED.value
    received = queue.ledgers[MARA].claims[envelope.new_claim_id]
    assert received.source_kind is SourceKind.REPORT
    assert received.parent_claim_id == envelope.source_claim_id
    assert received.provenance_root == RESPONSE_ACTION_ID
    assert received.message_id == "message:teo-response-pass426"


def test_queued_failed_or_waiting_response_does_not_change_requester_knowledge() -> None:
    queued = _queue(latency=5)
    envelope = _dispatch(_ledger(), queued)
    assert queued.process_due(904) == []
    assert envelope.new_claim_id not in queued.ledgers[MARA].claims

    failed = _queue(available=False, latency=0)
    envelope = _dispatch(_ledger(), failed)
    assert failed.process_due(903)[0]["status"] == DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value
    assert envelope.new_claim_id not in failed.ledgers[MARA].claims

    local = _queue(local_ack=True, latency=0)
    envelope = _dispatch(_ledger(), local)
    assert local.process_due(903)[0]["status"] == DeliveryStatus.WAITING_LOCAL_ACK.value
    assert envelope.new_claim_id not in local.ledgers[MARA].claims


def test_exact_replay_is_idempotent_even_after_terminal_delivery() -> None:
    ledger = _ledger("COUNTERPROPOSE_ASSISTANCE_REQUEST")
    queue = _queue(latency=0)
    first = _dispatch(ledger, queue)
    queue.process_due(903)
    replay = _dispatch(ledger, queue)

    assert replay == first
    assert len(queue.ledgers[TEO].claims) == 1
    assert len(queue.ledgers[MARA].claims) == 1


def test_request_response_binding_and_chronology_fail_closed() -> None:
    queue = _queue()
    ledger = _ledger()
    bad = ledger.records[RESPONSE_ACTION_ID]
    ledger.records[RESPONSE_ACTION_ID] = bad.__class__(
        action_id=bad.action_id, agent_id=MARA, intent_id=bad.intent_id, intent_kind=bad.intent_kind,
        target_ref=MARA, semantic_minute=bad.semantic_minute, trigger_ids=bad.trigger_ids,
        reason_codes=bad.reason_codes, source_type=bad.source_type, source_ref=bad.source_ref, status=bad.status,
    )
    with pytest.raises(ValueError, match="original request recipient"):
        _dispatch(ledger, queue)

    early = _ledger()
    with pytest.raises(ValueError, match="cannot be authored before"):
        schedule_assistance_response_from_action(
            action_ledger=early, information_queue=_queue(), request_action_id=REQUEST_ACTION_ID,
            response_action_id=RESPONSE_ACTION_ID, event_id="event:early-pass426", message_id="message:early-pass426",
            source_claim_id="claim:early-source-pass426", receiver_claim_id="claim:early-receiver-pass426",
            channel_id="channel:field-radio", created_minute=901,
        )


def test_unsupported_response_kind_and_conflicting_event_reuse_fail_closed() -> None:
    ledger = _ledger()
    queue = _queue()
    _dispatch(ledger, queue)

    with pytest.raises(ValueError, match="conflicting envelope"):
        schedule_assistance_response_from_action(
            action_ledger=ledger, information_queue=queue, request_action_id=REQUEST_ACTION_ID,
            response_action_id=RESPONSE_ACTION_ID, event_id=EVENT_ID, message_id="message:conflict-pass426",
            source_claim_id="claim:other-source-pass426", receiver_claim_id="claim:other-receiver-pass426",
            channel_id="channel:field-radio", created_minute=904,
        )

    unsupported = _ledger()
    row = unsupported.records[RESPONSE_ACTION_ID]
    unsupported.records[RESPONSE_ACTION_ID] = row.__class__(
        action_id=row.action_id, agent_id=row.agent_id, intent_id=row.intent_id, intent_kind="IGNORE_ASSISTANCE_REQUEST",
        target_ref=row.target_ref, semantic_minute=row.semantic_minute, trigger_ids=row.trigger_ids,
        reason_codes=row.reason_codes, source_type=row.source_type, source_ref=row.source_ref, status=row.status,
    )
    with pytest.raises(ValueError, match="not a supported assistance response"):
        _dispatch(unsupported, _queue())
