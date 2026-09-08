from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_replanning import NpcReplanQueue
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
)
from tools.global_npc_resource_reservations import ReservationLedger, ResourceReservation
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator


def _application() -> ResourceAllocationApplication:
    return ResourceAllocationApplication(
        application_id="application:meter-window",
        resolution_id="resolution:meter-window",
        resource_id="resource:meter-a",
        application_kind=AllocationApplicationKind.DISPLACE_CONFLICTING_RESERVATIONS,
        applied_tick=50,
        displaced_reservation_ids=("reservation:team-a",),
    )


def _reservations() -> ReservationLedger:
    return ReservationLedger(
        reservations=(
            ResourceReservation("reservation:team-a", "resource:meter-a", "npc:team-a-lead", 70, 90),
        )
    )


def _queue(*, local_ack: bool = False) -> InformationEventQueue:
    actors = ("npc:allocator", "npc:team-a-lead", "npc:team-b-lead")
    return InformationEventQueue(
        channels={
            "channel:radio": CommunicationChannel(
                "channel:radio", "RADIO", 5, requires_local_projection=local_ack
            )
        },
        ledgers={actor_id: KnowledgeLedger(actor_id) for actor_id in actors},
    )


def _ledger() -> ResourceAllocationNoticeLedger:
    return derive_displacement_notice_obligations(
        ResourceAllocationNoticeLedger(),
        _application(),
        _reservations(),
        obligation_id_prefix="notice-obligation",
        created_tick=51,
    )


def _schedule(
    queue: InformationEventQueue,
    *,
    event_id: str = "delivery:team-a",
    sender: str = "npc:allocator",
    receiver: str = "npc:team-a-lead",
    minute: int = 55,
) -> None:
    claim_id = f"claim:{event_id}"
    record_direct_observation(
        queue.ledgers[sender],
        claim_id=claim_id,
        subject="resource:meter-a:allocation-update",
        value="reservation:team-a displaced",
        semantic_minute=minute,
        confidence=100,
    )
    queue.schedule(
        event_id=event_id,
        message_id=f"message:{event_id}",
        sender_id=sender,
        receiver_id=receiver,
        source_claim_id=claim_id,
        new_claim_id=f"received:{event_id}",
        channel_id="channel:radio",
        created_minute=minute,
    )


def _link(*, sender: str = "npc:allocator", linked_tick: int = 55) -> ResourceAllocationNoticeLink:
    return ResourceAllocationNoticeLink(
        link_id="notice-link:team-a",
        obligation_id="notice-obligation:reservation:team-a",
        sender_actor_id=sender,
        communication_event_id="delivery:team-a",
        linked_tick=linked_tick,
    )


def _agent(actor_id: str) -> NpcAgentState:
    return NpcAgentState(
        agent_id=actor_id,
        mode=AgentMode.OFFSCREEN_NAMED,
        region_ref="region:test",
        location_ref="site:test",
    )


def test_notice_link_rejects_delivery_addressed_to_wrong_holder() -> None:
    queue = _queue()
    ledger = _ledger()
    _schedule(queue, receiver="npc:team-b-lead")

    try:
        link_notice_communication(ledger, queue, _link())
        assert False, "expected recipient binding validation"
    except ValueError as exc:
        assert "receiver" in str(exc)

    assert notice_state(ledger, queue, "notice-obligation:reservation:team-a") == AllocationNoticeState.REQUIRED


def test_notice_link_rejects_declared_sender_that_does_not_match_envelope() -> None:
    queue = _queue()
    ledger = _ledger()
    _schedule(queue)

    try:
        link_notice_communication(ledger, queue, _link(sender="npc:team-b-lead"))
        assert False, "expected sender binding validation"
    except ValueError as exc:
        assert "sender" in str(exc)


def test_notice_link_rejects_timestamp_before_message_was_authored() -> None:
    queue = _queue()
    ledger = _ledger()
    _schedule(queue, minute=55)

    try:
        link_notice_communication(ledger, queue, _link(linked_tick=54))
        assert False, "expected authored-time validation"
    except ValueError as exc:
        assert "authored" in str(exc)


def test_local_ack_envelope_remains_bindable_before_acknowledgement() -> None:
    queue = _queue(local_ack=True)
    ledger = _ledger()
    _schedule(queue)
    queue.process_due(60)

    linked = link_notice_communication(ledger, queue, _link(linked_tick=60))
    assert notice_state(linked, queue, "notice-obligation:reservation:team-a") == AllocationNoticeState.WAITING_LOCAL_ACK


def test_post_delivery_retroactive_link_fails_closed_when_address_provenance_is_gone() -> None:
    queue = _queue()
    ledger = _ledger()
    _schedule(queue)
    queue.process_due(60)

    try:
        link_notice_communication(ledger, queue, _link(linked_tick=60))
        assert False, "expected metadata provenance validation"
    except ValueError as exc:
        assert "metadata unavailable" in str(exc)


def test_correctly_bound_notice_delivery_uses_existing_coordinator_to_wake_only_holder() -> None:
    queue = _queue()
    ledger = _ledger()
    _schedule(queue)
    ledger = link_notice_communication(ledger, queue, _link())

    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents={
            "npc:team-a-lead": _agent("npc:team-a-lead"),
            "npc:team-b-lead": _agent("npc:team-b-lead"),
        },
    )
    cycle = coordinator.process_cycle(60, delivery_budget=10)

    assert notice_state(ledger, queue, "notice-obligation:reservation:team-a") == AllocationNoticeState.DELIVERED
    assert [item.receiver_id for item in cycle.materialized] == ["npc:team-a-lead"]
    assert [item.wake_status for item in cycle.materialized] == ["WAKE_SCHEDULED"]
    assert "received:delivery:team-a" in coordinator.agents["npc:team-a-lead"].knowledge
    assert "received:delivery:team-a" not in coordinator.agents["npc:team-b-lead"].knowledge
