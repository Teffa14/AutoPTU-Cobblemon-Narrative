from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentCoordinationState,
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffAppointmentNotice,
    actors_unaware_of_authored_cancellation,
    coordination_state,
    delivered_notices_for_actor,
    known_notices_for_actor,
    notice_delivery_status,
    register_handoff_appointment_notice,
)
from tools.global_npc_resource_handoffs import (
    HandoffMode,
    ResourceHandoffAuthorization,
    ResourceHandoffLedger,
    register_handoff_authorization,
)
from tools.global_npc_information_network import DeliveryStatus


def _handoff_ledger() -> ResourceHandoffLedger:
    authorization = ResourceHandoffAuthorization(
        authorization_id="handoff-auth:meter",
        request_id="request:meter",
        provider_actor_id="npc:technician",
        accountable_actor_id="npc:surveyor",
        receiving_actor_id="npc:assistant",
        resource_id="resource:meter-a",
        mode=HandoffMode.PICKUP,
        handoff_location_ref="place:field-office",
        valid_from_tick=30,
        valid_until_tick=90,
        authority_ref="request-event:accept",
    )
    return register_handoff_authorization(ResourceHandoffLedger(), authorization)


def _queue() -> InformationEventQueue:
    ledgers = {
        actor_id: KnowledgeLedger(actor_id)
        for actor_id in ("npc:technician", "npc:surveyor", "npc:assistant")
    }
    return InformationEventQueue(
        channels={"channel:phone": CommunicationChannel("channel:phone", "PHONE", 5)},
        ledgers=ledgers,
    )


def _schedule_notice(
    queue: InformationEventQueue,
    *,
    notice_id: str,
    sender: str,
    receiver: str,
    kind: HandoffAppointmentNoticeKind,
    created_tick: int,
) -> ResourceHandoffAppointmentNotice:
    source_claim_id = f"claim:{notice_id}"
    record_direct_observation(
        queue.ledgers[sender],
        claim_id=source_claim_id,
        subject="handoff-auth:meter:appointment-update",
        value=kind.value,
        semantic_minute=created_tick,
        confidence=100,
    )
    communication_event_id = f"delivery:{notice_id}"
    queue.schedule(
        event_id=communication_event_id,
        message_id=f"message:{notice_id}",
        sender_id=sender,
        receiver_id=receiver,
        source_claim_id=source_claim_id,
        new_claim_id=f"received:{notice_id}",
        channel_id="channel:phone",
        created_minute=created_tick,
    )
    return ResourceHandoffAppointmentNotice(
        notice_id=notice_id,
        authorization_id="handoff-auth:meter",
        sender_actor_id=sender,
        receiver_actor_id=receiver,
        kind=kind,
        source_claim_id=source_claim_id,
        communication_event_id=communication_event_id,
        created_tick=created_tick,
    )


def test_queued_cancellation_does_not_become_receiver_knowledge() -> None:
    handoffs = _handoff_ledger()
    queue = _queue()
    notice = _schedule_notice(
        queue,
        notice_id="cancel:1",
        sender="npc:technician",
        receiver="npc:assistant",
        kind=HandoffAppointmentNoticeKind.CANCEL,
        created_tick=40,
    )
    ledger = register_handoff_appointment_notice(ResourceHandoffAppointmentLedger(), handoffs, notice)

    assert notice_delivery_status(queue, notice) == DeliveryStatus.QUEUED
    assert delivered_notices_for_actor(ledger, queue, notice.authorization_id, "npc:assistant") == ()
    assert [item.notice_id for item in known_notices_for_actor(ledger, queue, notice.authorization_id, "npc:technician")] == ["cancel:1"]
    assert known_notices_for_actor(ledger, queue, notice.authorization_id, "npc:assistant") == ()
    assert coordination_state(ledger, queue, handoffs, notice.authorization_id) == HandoffAppointmentCoordinationState.CANCELLATION_AUTHORED
    assert actors_unaware_of_authored_cancellation(ledger, queue, handoffs, notice.authorization_id) == (
        "npc:assistant",
        "npc:surveyor",
    )


def test_delivered_cancellation_updates_only_actual_receiver() -> None:
    handoffs = _handoff_ledger()
    queue = _queue()
    notice = _schedule_notice(
        queue,
        notice_id="cancel:2",
        sender="npc:technician",
        receiver="npc:assistant",
        kind=HandoffAppointmentNoticeKind.CANCEL,
        created_tick=40,
    )
    ledger = register_handoff_appointment_notice(ResourceHandoffAppointmentLedger(), handoffs, notice)
    queue.process_due(45)

    assert notice_delivery_status(queue, notice) == DeliveryStatus.DELIVERED
    assert [item.notice_id for item in delivered_notices_for_actor(ledger, queue, notice.authorization_id, "npc:assistant")] == ["cancel:2"]
    assert coordination_state(ledger, queue, handoffs, notice.authorization_id) == HandoffAppointmentCoordinationState.CANCELLATION_DELIVERED
    assert actors_unaware_of_authored_cancellation(ledger, queue, handoffs, notice.authorization_id) == ("npc:surveyor",)


def test_confirmation_requires_receipt_in_both_directions() -> None:
    handoffs = _handoff_ledger()
    queue = _queue()
    provider_notice = _schedule_notice(
        queue,
        notice_id="confirm:provider",
        sender="npc:technician",
        receiver="npc:assistant",
        kind=HandoffAppointmentNoticeKind.CONFIRM,
        created_tick=35,
    )
    receiver_notice = _schedule_notice(
        queue,
        notice_id="confirm:receiver",
        sender="npc:assistant",
        receiver="npc:technician",
        kind=HandoffAppointmentNoticeKind.CONFIRM,
        created_tick=36,
    )
    ledger = ResourceHandoffAppointmentLedger()
    ledger = register_handoff_appointment_notice(ledger, handoffs, provider_notice)
    ledger = register_handoff_appointment_notice(ledger, handoffs, receiver_notice)

    assert coordination_state(ledger, queue, handoffs, "handoff-auth:meter") == HandoffAppointmentCoordinationState.NO_UPDATE
    queue.process_due(40)
    assert coordination_state(ledger, queue, handoffs, "handoff-auth:meter") == HandoffAppointmentCoordinationState.PARTIAL_CONFIRMATION
    queue.process_due(41)
    assert coordination_state(ledger, queue, handoffs, "handoff-auth:meter") == HandoffAppointmentCoordinationState.MUTUALLY_CONFIRMED


def test_reschedule_request_remains_distinct_from_cancellation() -> None:
    handoffs = _handoff_ledger()
    queue = _queue()
    notice = _schedule_notice(
        queue,
        notice_id="reschedule:1",
        sender="npc:assistant",
        receiver="npc:technician",
        kind=HandoffAppointmentNoticeKind.RESCHEDULE_REQUEST,
        created_tick=40,
    )
    ledger = register_handoff_appointment_notice(ResourceHandoffAppointmentLedger(), handoffs, notice)

    assert coordination_state(ledger, queue, handoffs, "handoff-auth:meter") == HandoffAppointmentCoordinationState.RESCHEDULE_REQUESTED


def test_notice_requires_real_authorization_participants_and_live_window() -> None:
    handoffs = _handoff_ledger()
    queue = _queue()
    outsider = ResourceHandoffAppointmentNotice(
        notice_id="bad:outsider",
        authorization_id="handoff-auth:meter",
        sender_actor_id="npc:bystander",
        receiver_actor_id="npc:assistant",
        kind=HandoffAppointmentNoticeKind.CONFIRM,
        source_claim_id="claim:bad",
        communication_event_id="delivery:bad",
        created_tick=40,
    )
    try:
        register_handoff_appointment_notice(ResourceHandoffAppointmentLedger(), handoffs, outsider)
        assert False, "expected participant validation"
    except ValueError as exc:
        assert "participants" in str(exc)

    expired = _schedule_notice(
        queue,
        notice_id="late:1",
        sender="npc:technician",
        receiver="npc:assistant",
        kind=HandoffAppointmentNoticeKind.CONFIRM,
        created_tick=90,
    )
    try:
        register_handoff_appointment_notice(ResourceHandoffAppointmentLedger(), handoffs, expired)
        assert False, "expected expiry validation"
    except ValueError as exc:
        assert "expiry" in str(exc)


def test_notice_history_is_append_only_deterministic_and_event_ids_are_unique() -> None:
    handoffs = _handoff_ledger()
    queue = _queue()
    later = _schedule_notice(
        queue,
        notice_id="notice:z",
        sender="npc:technician",
        receiver="npc:assistant",
        kind=HandoffAppointmentNoticeKind.CONFIRM,
        created_tick=45,
    )
    earlier = _schedule_notice(
        queue,
        notice_id="notice:a",
        sender="npc:assistant",
        receiver="npc:technician",
        kind=HandoffAppointmentNoticeKind.CONFIRM,
        created_tick=40,
    )
    ledger = register_handoff_appointment_notice(ResourceHandoffAppointmentLedger(), handoffs, later)
    ledger = register_handoff_appointment_notice(ledger, handoffs, earlier)
    assert [item.notice_id for item in ledger.notices] == ["notice:a", "notice:z"]

    try:
        register_handoff_appointment_notice(ledger, handoffs, earlier)
        assert False, "expected duplicate validation"
    except ValueError as exc:
        assert "duplicate" in str(exc)
