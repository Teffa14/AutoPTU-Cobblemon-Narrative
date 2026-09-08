from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum

from tools.global_npc_resource_allocation_resolution import (
    AllocationResolutionKind,
    ResourceAllocationResolution,
)
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    ReservationState,
    ResourceReservation,
)


class AllocationApplicationKind(str, Enum):
    DISPLACE_CONFLICTING_RESERVATIONS = "DISPLACE_CONFLICTING_RESERVATIONS"
    PRESERVE_SELECTED_RESERVATION = "PRESERVE_SELECTED_RESERVATION"
    DEFER_NO_CHANGE = "DEFER_NO_CHANGE"


@dataclass(frozen=True)
class ResourceAllocationApplication:
    application_id: str
    resolution_id: str
    resource_id: str
    application_kind: AllocationApplicationKind
    applied_tick: int
    displaced_reservation_ids: tuple[str, ...] = ()
    retained_reservation_id: str | None = None
    basis_refs: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.application_id.strip():
            raise ValueError("application_id is required")
        if not self.resolution_id.strip():
            raise ValueError("resolution_id is required")
        if not self.resource_id.strip():
            raise ValueError("resource_id is required")
        if self.applied_tick < 0:
            raise ValueError("applied_tick must be non-negative")


@dataclass(frozen=True)
class ResourceAllocationApplicationLedger:
    applications: tuple[ResourceAllocationApplication, ...] = ()


@dataclass(frozen=True)
class AllocationApplicationResult:
    accepted: bool
    ledger: ResourceAllocationApplicationLedger
    application: ResourceAllocationApplication | None = None
    reason_code: str = "ALLOCATION_APPLICATION_RECORDED"


def _reservation_map(ledger: ReservationLedger) -> dict[str, ResourceReservation]:
    return {item.reservation_id: item for item in ledger.reservations}


def apply_allocation_resolution(
    application_ledger: ResourceAllocationApplicationLedger,
    reservation_ledger: ReservationLedger,
    resolution: ResourceAllocationResolution,
    *,
    application_id: str,
    applied_tick: int,
    basis_refs: tuple[str, ...] = (),
) -> AllocationApplicationResult:
    """Materialize the operational consequence of a Pass 348 allocation decision.

    The base reservation ledger remains historical evidence. Displacement is stored
    separately and can be projected for planning without pretending the reservation
    holder personally cancelled the booking.
    """
    if any(item.application_id == application_id for item in application_ledger.applications):
        return AllocationApplicationResult(False, application_ledger, reason_code="DUPLICATE_APPLICATION_ID")
    if any(item.resolution_id == resolution.resolution_id for item in application_ledger.applications):
        return AllocationApplicationResult(False, application_ledger, reason_code="RESOLUTION_ALREADY_APPLIED")
    if applied_tick < resolution.decided_tick:
        return AllocationApplicationResult(False, application_ledger, reason_code="APPLICATION_PRECEDES_DECISION")

    reservations = _reservation_map(reservation_ledger)
    conflicts = tuple(sorted(resolution.conflicting_reservation_ids))
    for reservation_id in conflicts:
        reservation = reservations.get(reservation_id)
        if reservation is None:
            return AllocationApplicationResult(False, application_ledger, reason_code="CONFLICT_RESERVATION_MISSING")
        if reservation.resource_id != resolution.resource_id:
            return AllocationApplicationResult(False, application_ledger, reason_code="CONFLICT_RESOURCE_MISMATCH")
        if reservation.state != ReservationState.ACTIVE:
            return AllocationApplicationResult(False, application_ledger, reason_code="CONFLICT_RESERVATION_NOT_ACTIVE")

    if resolution.resolution_kind == AllocationResolutionKind.SELECT_PROPOSED_WINDOW:
        kind = AllocationApplicationKind.DISPLACE_CONFLICTING_RESERVATIONS
        displaced = conflicts
        retained = None
    elif resolution.resolution_kind == AllocationResolutionKind.SELECT_EXISTING_RESERVATION:
        if resolution.selected_reservation_id not in conflicts:
            return AllocationApplicationResult(False, application_ledger, reason_code="SELECTED_RESERVATION_NOT_CURRENT_CONFLICT")
        kind = AllocationApplicationKind.PRESERVE_SELECTED_RESERVATION
        displaced = ()
        retained = resolution.selected_reservation_id
    else:
        kind = AllocationApplicationKind.DEFER_NO_CHANGE
        displaced = ()
        retained = None

    application = ResourceAllocationApplication(
        application_id=application_id,
        resolution_id=resolution.resolution_id,
        resource_id=resolution.resource_id,
        application_kind=kind,
        applied_tick=applied_tick,
        displaced_reservation_ids=displaced,
        retained_reservation_id=retained,
        basis_refs=tuple(basis_refs),
    )
    updated = ResourceAllocationApplicationLedger(
        applications=tuple(sorted((*application_ledger.applications, application), key=lambda item: item.application_id))
    )
    return AllocationApplicationResult(True, updated, application=application)


def displaced_reservation_ids(
    ledger: ResourceAllocationApplicationLedger,
) -> tuple[str, ...]:
    return tuple(sorted({reservation_id for app in ledger.applications for reservation_id in app.displaced_reservation_ids}))


def project_allocation_onto_reservations(
    reservation_ledger: ReservationLedger,
    application_ledger: ResourceAllocationApplicationLedger,
) -> ReservationLedger:
    """Return an operational planning view while preserving the source ledger.

    A displaced reservation is represented as CANCELLED only in this derived view.
    The append-only application record retains the actual reason and decision provenance.
    """
    displaced = set(displaced_reservation_ids(application_ledger))
    projected = tuple(
        replace(item, state=ReservationState.CANCELLED)
        if item.reservation_id in displaced and item.state == ReservationState.ACTIVE
        else item
        for item in reservation_ledger.reservations
    )
    return ReservationLedger(tuple(sorted(projected, key=lambda item: item.reservation_id)))
