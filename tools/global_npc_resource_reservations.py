from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Iterable

from tools.global_npc_resources import ResourceState, WorldResource


class ReservationState(str, Enum):
    ACTIVE = "ACTIVE"
    RELEASED = "RELEASED"
    CANCELLED = "CANCELLED"


@dataclass(frozen=True)
class ResourceReservation:
    reservation_id: str
    resource_id: str
    actor_id: str
    start_tick: int
    end_tick: int
    state: ReservationState = ReservationState.ACTIVE
    purpose_ref: str | None = None

    def __post_init__(self) -> None:
        if not self.reservation_id.strip():
            raise ValueError("reservation_id is required")
        if not self.resource_id.strip():
            raise ValueError("resource_id is required")
        if not self.actor_id.strip():
            raise ValueError("actor_id is required")
        if self.start_tick < 0:
            raise ValueError("start_tick must be non-negative")
        if self.end_tick <= self.start_tick:
            raise ValueError("end_tick must be greater than start_tick")


@dataclass(frozen=True)
class ReservationLedger:
    reservations: tuple[ResourceReservation, ...] = ()


@dataclass(frozen=True)
class ReservationResult:
    accepted: bool
    ledger: ReservationLedger
    reservation: ResourceReservation | None = None
    reason_code: str = "RESERVATION_ACCEPTED"
    conflicting_reservation_ids: tuple[str, ...] = ()


def _overlaps(left: ResourceReservation, right: ResourceReservation) -> bool:
    return left.start_tick < right.end_tick and right.start_tick < left.end_tick


def is_effectively_active(reservation: ResourceReservation, at_tick: int) -> bool:
    return (
        reservation.state == ReservationState.ACTIVE
        and reservation.start_tick <= at_tick < reservation.end_tick
    )


def effective_state(reservation: ResourceReservation, at_tick: int) -> str:
    if reservation.state != ReservationState.ACTIVE:
        return reservation.state.value
    if at_tick >= reservation.end_tick:
        return "EXPIRED"
    if at_tick < reservation.start_tick:
        return "SCHEDULED"
    return "ACTIVE"


def reserve_resource(
    ledger: ReservationLedger,
    reservation: ResourceReservation,
) -> ReservationResult:
    """Create an indivisible-resource reservation when its time window is free.

    V1 intentionally treats one WorldResource ID as one reservable unit. Quantity pools,
    substitution grades and institutional borrowing are later layers rather than hidden
    assumptions in this contract.
    """
    if any(
        existing.reservation_id == reservation.reservation_id
        for existing in ledger.reservations
    ):
        return ReservationResult(
            False,
            ledger,
            reason_code="DUPLICATE_RESERVATION_ID",
        )

    conflicts = tuple(
        existing.reservation_id
        for existing in sorted(ledger.reservations, key=lambda item: item.reservation_id)
        if existing.resource_id == reservation.resource_id
        and existing.state == ReservationState.ACTIVE
        and _overlaps(existing, reservation)
    )
    if conflicts:
        return ReservationResult(
            False,
            ledger,
            reason_code="RESOURCE_WINDOW_CONFLICT",
            conflicting_reservation_ids=conflicts,
        )

    updated = ReservationLedger(
        tuple(sorted((*ledger.reservations, reservation), key=lambda item: item.reservation_id))
    )
    return ReservationResult(True, updated, reservation)


def release_reservation(
    ledger: ReservationLedger,
    reservation_id: str,
    actor_id: str,
) -> ReservationResult:
    return _close_reservation(
        ledger,
        reservation_id,
        actor_id,
        ReservationState.RELEASED,
        "RESERVATION_RELEASED",
    )


def cancel_reservation(
    ledger: ReservationLedger,
    reservation_id: str,
    actor_id: str,
) -> ReservationResult:
    return _close_reservation(
        ledger,
        reservation_id,
        actor_id,
        ReservationState.CANCELLED,
        "RESERVATION_CANCELLED",
    )


def _close_reservation(
    ledger: ReservationLedger,
    reservation_id: str,
    actor_id: str,
    target_state: ReservationState,
    success_code: str,
) -> ReservationResult:
    found: ResourceReservation | None = None
    updated: list[ResourceReservation] = []
    for reservation in ledger.reservations:
        if reservation.reservation_id != reservation_id:
            updated.append(reservation)
            continue
        found = reservation
        if reservation.actor_id != actor_id:
            return ReservationResult(False, ledger, reason_code="RESERVATION_ACTOR_MISMATCH")
        if reservation.state != ReservationState.ACTIVE:
            return ReservationResult(False, ledger, reservation, "RESERVATION_ALREADY_CLOSED")
        closed = replace(reservation, state=target_state)
        updated.append(closed)
        found = closed

    if found is None:
        return ReservationResult(False, ledger, reason_code="UNKNOWN_RESERVATION")

    return ReservationResult(
        True,
        ReservationLedger(tuple(sorted(updated, key=lambda item: item.reservation_id))),
        found,
        success_code,
    )


def active_reservations_for_resource(
    ledger: ReservationLedger,
    resource_id: str,
    at_tick: int,
) -> tuple[ResourceReservation, ...]:
    return tuple(
        reservation
        for reservation in sorted(ledger.reservations, key=lambda item: item.reservation_id)
        if reservation.resource_id == resource_id
        and is_effectively_active(reservation, at_tick)
    )


def project_reservations_onto_resources(
    resources: Iterable[WorldResource],
    ledger: ReservationLedger,
    at_tick: int,
) -> tuple[WorldResource, ...]:
    """Project active temporal claims into Pass 338's resource gate without mutation."""
    projected: list[WorldResource] = []
    for resource in sorted(resources, key=lambda item: item.resource_id):
        active = active_reservations_for_resource(ledger, resource.resource_id, at_tick)
        if len(active) > 1:
            raise ValueError("reservation ledger contains overlapping active claims")
        if not active:
            projected.append(resource)
            continue
        reservation = active[0]
        if resource.state in {ResourceState.DEPLETED, ResourceState.RETIRED, ResourceState.UNAVAILABLE}:
            projected.append(resource)
            continue
        projected.append(
            replace(
                resource,
                state=ResourceState.RESERVED if resource.holder_actor_id is None else resource.state,
                reserved_for_actor_id=reservation.actor_id,
            )
        )
    return tuple(projected)


def checkout_reserved_resource(
    resource: WorldResource,
    ledger: ReservationLedger,
    actor_id: str,
    at_tick: int,
) -> WorldResource:
    active = active_reservations_for_resource(ledger, resource.resource_id, at_tick)
    if len(active) != 1 or active[0].actor_id != actor_id:
        raise ValueError("actor lacks an active reservation for this resource")
    if resource.state in {ResourceState.DEPLETED, ResourceState.RETIRED, ResourceState.UNAVAILABLE}:
        raise ValueError("resource is not serviceable")
    if resource.holder_actor_id not in {None, actor_id}:
        raise ValueError("resource is held by another actor")
    return replace(
        resource,
        state=ResourceState.IN_USE,
        holder_actor_id=actor_id,
        reserved_for_actor_id=actor_id,
    )


def return_resource(
    resource: WorldResource,
    actor_id: str,
    return_location_ref: str,
) -> WorldResource:
    if resource.holder_actor_id != actor_id:
        raise ValueError("actor does not hold this resource")
    if not return_location_ref.strip():
        raise ValueError("return_location_ref is required")
    return replace(
        resource,
        state=ResourceState.AVAILABLE,
        holder_actor_id=None,
        reserved_for_actor_id=None,
        location_ref=return_location_ref,
    )
