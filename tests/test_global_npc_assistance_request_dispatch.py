import pytest

from tools.global_npc_ai import AgendaDecision, Decision, Handoff
from tools.global_npc_assistance_request_dispatch import schedule_assistance_request_from_action
from tools.global_npc_information_network import (
    CommunicationChannel,
    DeliveryStatus,
    InformationEventQueue,
)
from tools.global_npc_memory import KnowledgeLedger, SourceKind
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import CoordinatedDecision


MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"


def _action_ledger(
    *,
    kind: str = "REQUEST_ASSISTANCE",
    target_ref: str | None = TEO,
    action_id: str = "action:request-teo-001",
) -> WorldActionIntentLedger:
    ledger = WorldActionIntentLedger()
    coordinated = CoordinatedDecision(
        agent_id=MARA,
        trigger_ids=("trigger:warning-delivered",),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(
                agent_id=MARA,
                intent_id="intent:request-specialist",
                kind=kind,
                score=420,
                handoff=Handoff.NONE,
                target_ref=target_ref,
            ),
            source_type="SITUATIONAL_INTENT",
            source_ref="intent:request-specialist",
        ),
    )
    ledger.record_from_replan(
        action_id=action_id,
        coordinated_decision=coordinated,
        semantic_minute=615,
    )
    return ledger


def _queue(*, available: bool = True, local_ack: bool = False, latency: int = 10) -> InformationEventQueue:
    return InformationEventQueue(
        channels={
            "channel:field-radio": CommunicationChannel(
                channel_id="channel:field-radio",
                kind="RADIO",
                latency_minutes=latency,
                available=available,
                requires_local_projection=local_ack,
            )
        },
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)},
    )


def _dispatch(action_ledger: WorldActionIntentLedger, queue: InformationEventQueue):
    return schedule_assistance_request_from_action(
        action_ledger=action_ledger,
        information_queue=queue,
        action_id="action:request-teo-001",
        event_id="event:request-teo-001",
        message_id="message:request-teo-001",
        source_claim_id="claim:mara-request-teo-001",
        receiver_claim_id="claim:teo-received-request-001",
        channel_id="channel:field-radio",
        created_minute=616,
        receiver_trust_in_sender=20,
    )


def test_request_is_authored_and_queued_without_mutating_receiver_knowledge() -> None:
    action_ledger = _action_ledger()
    queue = _queue()

    envelope = _dispatch(action_ledger, queue)

    source = queue.ledgers[MARA].claims["claim:mara-request-teo-001"]
    assert source.source_kind is SourceKind.AUTHORED_START
    assert source.provenance_root == "action:request-teo-001"
    assert source.subject == "assistance_request:action:request-teo-001"
    assert source.value == "intent:request-specialist"
    assert envelope.receiver_id == TEO
    assert envelope.delivery_minute == 626
    assert queue.statuses[envelope.event_id] is DeliveryStatus.QUEUED
    assert queue.ledgers[TEO].claims == {}


def test_successful_delivery_preserves_action_provenance_for_receiver() -> None:
    action_ledger = _action_ledger()
    queue = _queue()
    envelope = _dispatch(action_ledger, queue)

    assert queue.process_due(625) == []
    results = queue.process_due(626)

    assert results[0]["status"] == DeliveryStatus.DELIVERED.value
    received = queue.ledgers[TEO].claims[envelope.new_claim_id]
    assert received.source_kind is SourceKind.REPORT
    assert received.parent_claim_id == envelope.source_claim_id
    assert received.provenance_root == "action:request-teo-001"
    assert received.message_id == "message:request-teo-001"


def test_failed_or_unacknowledged_request_does_not_create_receiver_knowledge() -> None:
    unavailable = _queue(available=False, latency=0)
    envelope = _dispatch(_action_ledger(), unavailable)
    failed = unavailable.process_due(616)
    assert failed[0]["status"] == DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value
    assert envelope.new_claim_id not in unavailable.ledgers[TEO].claims

    local = _queue(local_ack=True, latency=0)
    local_envelope = _dispatch(_action_ledger(), local)
    waiting = local.process_due(616)
    assert waiting[0]["status"] == DeliveryStatus.WAITING_LOCAL_ACK.value
    assert local_envelope.new_claim_id not in local.ledgers[TEO].claims

    rejected = local.acknowledge_local_delivery(local_envelope.event_id, 617, accepted=False)
    assert rejected["status"] == DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value
    assert local_envelope.new_claim_id not in local.ledgers[TEO].claims


def test_exact_replay_is_idempotent_even_after_terminal_delivery() -> None:
    action_ledger = _action_ledger()
    queue = _queue(latency=0)
    first = _dispatch(action_ledger, queue)
    queue.process_due(616)

    replay = _dispatch(action_ledger, queue)

    assert replay == first
    assert len(queue.ledgers[MARA].claims) == 1
    assert len(queue.ledgers[TEO].claims) == 1


def test_conflicting_event_reuse_fails_before_new_request_is_authored() -> None:
    queue = _queue()
    first_ledger = _action_ledger()
    _dispatch(first_ledger, queue)

    other = _action_ledger(action_id="action:request-teo-002")
    with pytest.raises(ValueError, match="conflicting envelope"):
        schedule_assistance_request_from_action(
            action_ledger=other,
            information_queue=queue,
            action_id="action:request-teo-002",
            event_id="event:request-teo-001",
            message_id="message:request-teo-002",
            source_claim_id="claim:mara-request-teo-002",
            receiver_claim_id="claim:teo-received-request-002",
            channel_id="channel:field-radio",
            created_minute=617,
        )

    assert "claim:mara-request-teo-002" not in queue.ledgers[MARA].claims


def test_only_planned_assistance_requests_with_explicit_other_target_are_admitted() -> None:
    queue = _queue()

    with pytest.raises(ValueError, match="not an assistance request"):
        _dispatch(_action_ledger(kind="TRAVEL_TO_SITE"), queue)

    with pytest.raises(ValueError, match="explicit target"):
        _dispatch(_action_ledger(target_ref=None), _queue())

    with pytest.raises(ValueError, match="another actor"):
        _dispatch(_action_ledger(target_ref=MARA), _queue())


def test_request_cannot_predate_decision_and_unknown_action_fails_closed() -> None:
    action_ledger = _action_ledger()
    queue = _queue()

    with pytest.raises(ValueError, match="cannot be authored before"):
        schedule_assistance_request_from_action(
            action_ledger=action_ledger,
            information_queue=queue,
            action_id="action:request-teo-001",
            event_id="event:early",
            message_id="message:early",
            source_claim_id="claim:early",
            receiver_claim_id="claim:early-receiver",
            channel_id="channel:field-radio",
            created_minute=614,
        )

    with pytest.raises(KeyError, match="unknown world action intent"):
        schedule_assistance_request_from_action(
            action_ledger=action_ledger,
            information_queue=queue,
            action_id="action:missing",
            event_id="event:missing",
            message_id="message:missing",
            source_claim_id="claim:missing",
            receiver_claim_id="claim:missing-receiver",
            channel_id="channel:field-radio",
            created_minute=616,
        )
