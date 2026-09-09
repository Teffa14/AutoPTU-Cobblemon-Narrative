from __future__ import annotations

from typing import Mapping

from tools.global_npc_resource_allocation_application import (
    AllocationApplicationKind,
    ResourceAllocationApplication,
    ResourceAllocationApplicationLedger,
)
from tools.global_npc_resource_allocation_checkpoint import (
    RESOURCE_CHECKPOINT_ALLOCATION_SCHEMA,
    restore_resource_state_with_allocations,
    snapshot_resource_state_with_allocations,
)
from tools.global_npc_resource_allocation_resolution import (
    AllocationResolutionKind,
    ResourceAllocationResolutionLedger,
)


RESOURCE_CHECKPOINT_ALLOCATION_APPLICATION_SCHEMA = "OUROS_NPC_RESOURCE_CHECKPOINT_V8"


def snapshot_resource_state_with_allocation_applications(
    reservation_ledger,
    request_ledger,
    handoff_ledger,
    attempt_ledger,
    appointment_ledger,
    reschedule_ledger,
    admission_ledger,
    authority_evidence,
    resolution_ledger: ResourceAllocationResolutionLedger,
    application_ledger: ResourceAllocationApplicationLedger,
) -> dict:
    snapshot = snapshot_resource_state_with_allocations(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
        admission_ledger,
        authority_evidence,
        resolution_ledger,
    )
    snapshot["schema"] = RESOURCE_CHECKPOINT_ALLOCATION_APPLICATION_SCHEMA
    snapshot["allocation_applications"] = [
        {
            "application_id": row.application_id,
            "resolution_id": row.resolution_id,
            "resource_id": row.resource_id,
            "application_kind": row.application_kind.value,
            "applied_tick": row.applied_tick,
            "displaced_reservation_ids": list(row.displaced_reservation_ids),
            "retained_reservation_id": row.retained_reservation_id,
            "basis_refs": list(row.basis_refs),
        }
        for row in sorted(application_ledger.applications, key=lambda item: (item.applied_tick, item.application_id))
    ]
    return snapshot


def restore_resource_state_with_allocation_applications(snapshot: Mapping[str, object]):
    schema = snapshot.get("schema")
    if schema != RESOURCE_CHECKPOINT_ALLOCATION_APPLICATION_SCHEMA:
        base = restore_resource_state_with_allocations(snapshot)
        return (*base, ResourceAllocationApplicationLedger())

    base_snapshot = dict(snapshot)
    base_snapshot["schema"] = RESOURCE_CHECKPOINT_ALLOCATION_SCHEMA
    base_snapshot.pop("allocation_applications", None)
    base = restore_resource_state_with_allocations(base_snapshot)
    reservation_ledger = base[0]
    resolution_ledger = base[8]

    raw_applications = snapshot.get("allocation_applications", [])
    if not isinstance(raw_applications, list):
        raise ValueError("allocation application checkpoint collection must be a list")

    applications = []
    for raw in raw_applications:
        if not isinstance(raw, Mapping):
            raise ValueError("allocation application checkpoint row must be a mapping")
        displaced = raw.get("displaced_reservation_ids", [])
        basis = raw.get("basis_refs", [])
        if not isinstance(displaced, list) or not isinstance(basis, list):
            raise ValueError("allocation application references must be lists")
        retained = raw.get("retained_reservation_id")
        applications.append(ResourceAllocationApplication(
            application_id=str(raw["application_id"]),
            resolution_id=str(raw["resolution_id"]),
            resource_id=str(raw["resource_id"]),
            application_kind=AllocationApplicationKind(str(raw["application_kind"])),
            applied_tick=int(raw["applied_tick"]),
            displaced_reservation_ids=tuple(sorted(str(value) for value in displaced)),
            retained_reservation_id=None if retained is None else str(retained),
            basis_refs=tuple(str(value) for value in basis),
        ))

    ledger = ResourceAllocationApplicationLedger(
        tuple(sorted(applications, key=lambda item: item.application_id))
    )
    _validate_allocation_application_history(ledger, resolution_ledger, reservation_ledger)
    return (*base, ledger)


def _validate_allocation_application_history(application_ledger, resolution_ledger, reservation_ledger) -> None:
    application_ids = [row.application_id for row in application_ledger.applications]
    if len(application_ids) != len(set(application_ids)):
        raise ValueError("resource checkpoint contains duplicate allocation application IDs")

    applied_resolution_ids = [row.resolution_id for row in application_ledger.applications]
    if len(applied_resolution_ids) != len(set(applied_resolution_ids)):
        raise ValueError("resource checkpoint applies an allocation resolution more than once")

    resolution_by_id = {row.resolution_id: row for row in resolution_ledger.resolutions}
    reservation_by_id = {row.reservation_id: row for row in reservation_ledger.reservations}

    for row in application_ledger.applications:
        resolution = resolution_by_id.get(row.resolution_id)
        if resolution is None:
            raise ValueError(f"allocation application references missing resolution: {row.application_id}")
        if row.resource_id != resolution.resource_id:
            raise ValueError(f"allocation application resource mismatch: {row.application_id}")
        if row.applied_tick < resolution.decided_tick:
            raise ValueError(f"allocation application precedes decision: {row.application_id}")

        conflicts = tuple(sorted(resolution.conflicting_reservation_ids))
        for reservation_id in conflicts:
            reservation = reservation_by_id.get(reservation_id)
            if reservation is None:
                raise ValueError(f"allocation application conflict reservation missing: {row.application_id}")
            if reservation.resource_id != row.resource_id:
                raise ValueError(f"allocation application conflict resource mismatch: {row.application_id}")

        if resolution.resolution_kind == AllocationResolutionKind.SELECT_PROPOSED_WINDOW:
            if row.application_kind != AllocationApplicationKind.DISPLACE_CONFLICTING_RESERVATIONS:
                raise ValueError(f"allocation application kind contradicts resolution: {row.application_id}")
            if tuple(sorted(row.displaced_reservation_ids)) != conflicts or row.retained_reservation_id is not None:
                raise ValueError(f"allocation application displacement set contradicts resolution: {row.application_id}")
        elif resolution.resolution_kind == AllocationResolutionKind.SELECT_EXISTING_RESERVATION:
            if row.application_kind != AllocationApplicationKind.PRESERVE_SELECTED_RESERVATION:
                raise ValueError(f"allocation application kind contradicts resolution: {row.application_id}")
            if row.displaced_reservation_ids or row.retained_reservation_id != resolution.selected_reservation_id:
                raise ValueError(f"allocation application retained reservation contradicts resolution: {row.application_id}")
        else:
            if row.application_kind != AllocationApplicationKind.DEFER_NO_CHANGE:
                raise ValueError(f"allocation application kind contradicts resolution: {row.application_id}")
            if row.displaced_reservation_ids or row.retained_reservation_id is not None:
                raise ValueError(f"allocation application defer payload is not empty: {row.application_id}")


def validate_allocation_application_checkpoint_time(
    ledger: ResourceAllocationApplicationLedger,
    *,
    semantic_minute: int,
) -> None:
    for row in ledger.applications:
        if row.applied_tick > semantic_minute:
            raise ValueError(f"allocation application comes from the future: {row.application_id}")
