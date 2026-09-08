from tools.global_npc_resource_allocation_application import (
    AllocationApplicationKind,
    ResourceAllocationApplicationLedger,
    apply_allocation_resolution,
    project_allocation_onto_reservations,
)
from tools.global_npc_resource_allocation_resolution import (
    AllocationResolutionKind,
    ResourceAllocationResolution,
)
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    ReservationState,
    ResourceReservation,
)


def _reservation(reservation_id: str, actor_id: str = "actor-a") -> ResourceReservation:
    return ResourceReservation(
        reservation_id=reservation_id,
        resource_id="meter-1",
        actor_id=actor_id,
        start_tick=100,
        end_tick=200,
        purpose_ref=f"purpose-{reservation_id}",
    )


def _resolution(kind: AllocationResolutionKind, selected: str | None = None) -> ResourceAllocationResolution:
    return ResourceAllocationResolution(
        resolution_id="resolution-1",
        proposal_id="proposal-1",
        resource_id="meter-1",
        decision_actor_id="allocator-1",
        authority_check_id="authority-1",
        resolution_kind=kind,
        decided_tick=90,
        conflicting_reservation_ids=("reservation-b", "reservation-a"),
        selected_reservation_id=selected,
        basis_refs=("policy-local-1",),
    )


def test_select_proposed_window_displaces_conflicts_without_mutating_source_ledger():
    source = ReservationLedger((_reservation("reservation-a"), _reservation("reservation-b", "actor-b")))
    result = apply_allocation_resolution(
        ResourceAllocationApplicationLedger(),
        source,
        _resolution(AllocationResolutionKind.SELECT_PROPOSED_WINDOW),
        application_id="application-1",
        applied_tick=95,
    )
    assert result.accepted
    assert result.application.application_kind == AllocationApplicationKind.DISPLACE_CONFLICTING_RESERVATIONS
    assert result.application.displaced_reservation_ids == ("reservation-a", "reservation-b")
    assert all(item.state == ReservationState.ACTIVE for item in source.reservations)

    projected = project_allocation_onto_reservations(source, result.ledger)
    assert all(item.state == ReservationState.CANCELLED for item in projected.reservations)
    assert all(item.state == ReservationState.ACTIVE for item in source.reservations)


def test_select_existing_reservation_preserves_current_bookings():
    source = ReservationLedger((_reservation("reservation-a"), _reservation("reservation-b")))
    result = apply_allocation_resolution(
        ResourceAllocationApplicationLedger(),
        source,
        _resolution(AllocationResolutionKind.SELECT_EXISTING_RESERVATION, "reservation-b"),
        application_id="application-1",
        applied_tick=95,
    )
    assert result.accepted
    assert result.application.application_kind == AllocationApplicationKind.PRESERVE_SELECTED_RESERVATION
    assert result.application.retained_reservation_id == "reservation-b"
    projected = project_allocation_onto_reservations(source, result.ledger)
    assert all(item.state == ReservationState.ACTIVE for item in projected.reservations)


def test_defer_records_no_operational_change():
    source = ReservationLedger((_reservation("reservation-a"), _reservation("reservation-b")))
    result = apply_allocation_resolution(
        ResourceAllocationApplicationLedger(),
        source,
        _resolution(AllocationResolutionKind.DEFER),
        application_id="application-1",
        applied_tick=95,
    )
    assert result.accepted
    assert result.application.application_kind == AllocationApplicationKind.DEFER_NO_CHANGE
    assert project_allocation_onto_reservations(source, result.ledger) == source


def test_application_fails_if_conflict_reservation_is_missing():
    source = ReservationLedger((_reservation("reservation-a"),))
    result = apply_allocation_resolution(
        ResourceAllocationApplicationLedger(),
        source,
        _resolution(AllocationResolutionKind.SELECT_PROPOSED_WINDOW),
        application_id="application-1",
        applied_tick=95,
    )
    assert not result.accepted
    assert result.reason_code == "CONFLICT_RESERVATION_MISSING"


def test_application_fails_if_conflict_was_already_closed():
    closed = ResourceReservation(
        reservation_id="reservation-b",
        resource_id="meter-1",
        actor_id="actor-b",
        start_tick=100,
        end_tick=200,
        state=ReservationState.RELEASED,
    )
    source = ReservationLedger((_reservation("reservation-a"), closed))
    result = apply_allocation_resolution(
        ResourceAllocationApplicationLedger(),
        source,
        _resolution(AllocationResolutionKind.SELECT_PROPOSED_WINDOW),
        application_id="application-1",
        applied_tick=95,
    )
    assert not result.accepted
    assert result.reason_code == "CONFLICT_RESERVATION_NOT_ACTIVE"


def test_same_resolution_cannot_be_applied_twice():
    source = ReservationLedger((_reservation("reservation-a"), _reservation("reservation-b")))
    first = apply_allocation_resolution(
        ResourceAllocationApplicationLedger(),
        source,
        _resolution(AllocationResolutionKind.SELECT_PROPOSED_WINDOW),
        application_id="application-1",
        applied_tick=95,
    )
    second = apply_allocation_resolution(
        first.ledger,
        source,
        _resolution(AllocationResolutionKind.SELECT_PROPOSED_WINDOW),
        application_id="application-2",
        applied_tick=96,
    )
    assert not second.accepted
    assert second.reason_code == "RESOLUTION_ALREADY_APPLIED"


def test_application_cannot_precede_institutional_decision():
    source = ReservationLedger((_reservation("reservation-a"), _reservation("reservation-b")))
    result = apply_allocation_resolution(
        ResourceAllocationApplicationLedger(),
        source,
        _resolution(AllocationResolutionKind.SELECT_PROPOSED_WINDOW),
        application_id="application-1",
        applied_tick=89,
    )
    assert not result.accepted
    assert result.reason_code == "APPLICATION_PRECEDES_DECISION"
