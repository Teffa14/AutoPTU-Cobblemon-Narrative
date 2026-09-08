from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_resource_allocation_application import (
    AllocationApplicationKind,
    ResourceAllocationApplication,
)
from tools.global_npc_resource_allocation_notices import (
    AllocationNoticeState,
    ResourceAllocationNoticeLedger,
    ResourceAllocationNoticeLink,
    derive_displacement_notice_obligations,
    link_notice_communication,
    notice_state,
    outstanding_notice_obligations,
)
from tools.global_npc_resource_reservations import ReservationLedger, ResourceReservation


def _application() -> ResourceAllocationApplication:
    return ResourceAllocationApplication(
        application_id="application:meter-window",
        resolution_id="resolution:meter-window",
        resource_id="resource:meter-a",
        application_kind=AllocationApplicationKind.DISPLACE_CONFLICTING_RESERVATIONS,
        applied_tick=50,
        displaced_reservation_ids=("reservation:team-b", "reservation:team-a"),
    )


def _reservations() -> ReservationLedger:
    return ReservationLedger(
        reservations=(
            ResourceReservation("reservation:team-a", "resource:meter-a", "npc:team-a-lead", 70, 90),
            ResourceReservation("reservation:team-b", "resource:meter-a", "npc:team-b-lead", 72, 88),
        )
    )


def _queue() -> InformationEventQueue:
    return InformationEventQueue(
        channels={"channel:radio": CommunicationChannel("channel:radio", "RADIO", 5)},
        ledgers={
            actor_id: KnowledgeLedger(actor_id)
            for actor_id in ("npc:allocator", "npc:team-a-lead", "npc:team-b-lead")
        },
    )


def _schedule(queue: InformationEventQueue, *, event_id: str, receiver: str, minute: int = 55) -> None:
    claim_id = f"claim:{event_id}"
    record_direct_observation(
        queue.ledgers["npc:allocator"],
        claim_id=claim_id,
        subject="resource:meter-a:allocation-update",
        value="reservation displaced",
        semantic_minute=minute,
        confidence=100,
    )
    queue.schedule(
        event_id=event_id,
        message_id=f"message:{event_id}",
        sender_id="npc:allocator",
        receiver_id=receiver,
        source_claim_id=claim_id,
        new_claim_id=f"received:{event_id}",
        channel_id="channel:radio",
        created_minute=minute,
    )


def test_derives_one_obligation_per_displaced_reservation_with_holder_provenance() -> None:
    ledger = derive_displacement_notice_obligations(
        ResourceAllocationNoticeLedger(),
        _application(),
        _reservations(),
        obligation_id_prefix="notice-obligation",
        created_tick=51,
        basis_refs=("policy:shared-meter",),
    )

    assert [item.displaced_reservation_id for item in ledger.obligations] == [
        "reservation:team-a",
        "reservation:team-b",
    ]
    assert [item.affected_actor_id for item in ledger.obligations] == [
        "npc:team-a-lead",
        "npc:team-b-lead",
    ]
    assert all(item.basis_refs == ("policy:shared-meter",) for item in ledger.obligations)


def test_notice_required_does_not_imply_message_authored_or_delivered() -> None:
    queue = _queue()
    ledger = derive_displacement_notice_obligations(
        ResourceAllocationNoticeLedger(), _application(), _reservations(),
        obligation_id_prefix="notice-obligation", created_tick=51,
    )
    obligation_id = "notice-obligation:reservation:team-a"

    assert notice_state(ledger, queue, obligation_id) == AllocationNoticeState.REQUIRED
    assert [item.obligation_id for item in outstanding_notice_obligations(ledger, queue)] == [
        "notice-obligation:reservation:team-a",
        "notice-obligation:reservation:team-b",
    ]


def test_queued_message_remains_outstanding_until_existing_runtime_delivers_it() -> None:
    queue = _queue()
    ledger = derive_displacement_notice_obligations(
        ResourceAllocationNoticeLedger(), _application(), _reservations(),
        obligation_id_prefix="notice-obligation", created_tick=51,
    )
    obligation_id = "notice-obligation:reservation:team-a"
    _schedule(queue, event_id="delivery:team-a", receiver="npc:team-a-lead")
    ledger = link_notice_communication(
        ledger,
        queue,
        ResourceAllocationNoticeLink(
            link_id="notice-link:team-a",
            obligation_id=obligation_id,
            sender_actor_id="npc:allocator",
            communication_event_id="delivery:team-a",
            linked_tick=55,
        ),
    )

    assert notice_state(ledger, queue, obligation_id) == AllocationNoticeState.QUEUED
    assert obligation_id in {item.obligation_id for item in outstanding_notice_obligations(ledger, queue)}

    queue.process_due(60)
    assert notice_state(ledger, queue, obligation_id) == AllocationNoticeState.DELIVERED
    assert obligation_id not in {item.obligation_id for item in outstanding_notice_obligations(ledger, queue)}


def test_delivery_to_one_holder_does_not_inform_another_holder() -> None:
    queue = _queue()
    ledger = derive_displacement_notice_obligations(
        ResourceAllocationNoticeLedger(), _application(), _reservations(),
        obligation_id_prefix="notice-obligation", created_tick=51,
    )
    _schedule(queue, event_id="delivery:team-a", receiver="npc:team-a-lead")
    ledger = link_notice_communication(
        ledger,
        queue,
        ResourceAllocationNoticeLink(
            link_id="notice-link:team-a",
            obligation_id="notice-obligation:reservation:team-a",
            sender_actor_id="npc:allocator",
            communication_event_id="delivery:team-a",
            linked_tick=55,
        ),
    )
    queue.process_due(60)

    assert notice_state(ledger, queue, "notice-obligation:reservation:team-a") == AllocationNoticeState.DELIVERED
    assert notice_state(ledger, queue, "notice-obligation:reservation:team-b") == AllocationNoticeState.REQUIRED


def test_non_displacement_application_cannot_create_holder_notice_obligations() -> None:
    application = ResourceAllocationApplication(
        application_id="application:preserve",
        resolution_id="resolution:preserve",
        resource_id="resource:meter-a",
        application_kind=AllocationApplicationKind.PRESERVE_SELECTED_RESERVATION,
        applied_tick=50,
        retained_reservation_id="reservation:team-a",
    )
    try:
        derive_displacement_notice_obligations(
            ResourceAllocationNoticeLedger(), application, _reservations(),
            obligation_id_prefix="notice-obligation", created_tick=51,
        )
        assert False, "expected displacement validation"
    except ValueError as exc:
        assert "does not displace" in str(exc)


def test_missing_or_wrong_resource_reservation_fails_closed() -> None:
    application = _application()
    missing = ReservationLedger((_reservations().reservations[0],))
    try:
        derive_displacement_notice_obligations(
            ResourceAllocationNoticeLedger(), application, missing,
            obligation_id_prefix="notice-obligation", created_tick=51,
        )
        assert False, "expected missing reservation validation"
    except ValueError as exc:
        assert "missing" in str(exc)


def test_duplicate_obligation_and_communication_link_are_rejected() -> None:
    queue = _queue()
    ledger = derive_displacement_notice_obligations(
        ResourceAllocationNoticeLedger(), _application(), _reservations(),
        obligation_id_prefix="notice-obligation", created_tick=51,
    )
    try:
        derive_displacement_notice_obligations(
            ledger, _application(), _reservations(),
            obligation_id_prefix="notice-obligation", created_tick=52,
        )
        assert False, "expected duplicate obligation validation"
    except ValueError as exc:
        assert "already exists" in str(exc)

    _schedule(queue, event_id="delivery:team-a", receiver="npc:team-a-lead")
    link = ResourceAllocationNoticeLink(
        link_id="notice-link:team-a",
        obligation_id="notice-obligation:reservation:team-a",
        sender_actor_id="npc:allocator",
        communication_event_id="delivery:team-a",
        linked_tick=55,
    )
    ledger = link_notice_communication(ledger, queue, link)
    try:
        link_notice_communication(ledger, queue, link)
        assert False, "expected duplicate link validation"
    except ValueError as exc:
        assert "duplicate" in str(exc) or "already" in str(exc)
