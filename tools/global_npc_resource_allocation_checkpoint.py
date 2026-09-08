from __future__ import annotations

from typing import Mapping

from tools.global_npc_resource_admission_checkpoint import (
    RESOURCE_CHECKPOINT_ADMISSION_SCHEMA,
    restore_resource_state_with_admissions,
    snapshot_resource_state_with_admissions,
)
from tools.global_npc_resource_allocation_resolution import (
    AllocationAuthorityEvidence,
    AllocationAuthorityState,
    AllocationResolutionKind,
    ResourceAllocationResolution,
    ResourceAllocationResolutionLedger,
)
from tools.global_npc_resource_handoff_reschedule_admission import RescheduleAdmissionState


RESOURCE_CHECKPOINT_ALLOCATION_SCHEMA = "OUROS_NPC_RESOURCE_CHECKPOINT_V7"


def snapshot_resource_state_with_allocations(
    reservation_ledger,
    request_ledger,
    handoff_ledger,
    attempt_ledger,
    appointment_ledger,
    reschedule_ledger,
    admission_ledger,
    authority_evidence: tuple[AllocationAuthorityEvidence, ...],
    resolution_ledger: ResourceAllocationResolutionLedger,
) -> dict:
    snapshot = snapshot_resource_state_with_admissions(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
        admission_ledger,
    )
    snapshot["schema"] = RESOURCE_CHECKPOINT_ALLOCATION_SCHEMA
    snapshot["allocation_authority_evidence"] = [
        {
            "authority_check_id": row.authority_check_id,
            "actor_id": row.actor_id,
            "action_ref": row.action_ref,
            "target_resource_id": row.target_resource_id,
            "state": row.state.value,
            "checked_tick": row.checked_tick,
            "valid_until_tick": row.valid_until_tick,
        }
        for row in sorted(authority_evidence, key=lambda item: item.authority_check_id)
    ]
    snapshot["allocation_resolutions"] = [
        {
            "resolution_id": row.resolution_id,
            "proposal_id": row.proposal_id,
            "resource_id": row.resource_id,
            "decision_actor_id": row.decision_actor_id,
            "authority_check_id": row.authority_check_id,
            "resolution_kind": row.resolution_kind.value,
            "decided_tick": row.decided_tick,
            "conflicting_reservation_ids": list(row.conflicting_reservation_ids),
            "selected_reservation_id": row.selected_reservation_id,
            "basis_refs": list(row.basis_refs),
        }
        for row in sorted(resolution_ledger.resolutions, key=lambda item: (item.decided_tick, item.resolution_id))
    ]
    return snapshot


def restore_resource_state_with_allocations(snapshot: Mapping[str, object]):
    schema = snapshot.get("schema")
    if schema != RESOURCE_CHECKPOINT_ALLOCATION_SCHEMA:
        base = restore_resource_state_with_admissions(snapshot)
        return (*base, (), ResourceAllocationResolutionLedger())

    base_snapshot = dict(snapshot)
    base_snapshot["schema"] = RESOURCE_CHECKPOINT_ADMISSION_SCHEMA
    base_snapshot.pop("allocation_authority_evidence", None)
    base_snapshot.pop("allocation_resolutions", None)
    base = restore_resource_state_with_admissions(base_snapshot)
    admission_ledger = base[6]

    raw_authorities = snapshot.get("allocation_authority_evidence", [])
    raw_resolutions = snapshot.get("allocation_resolutions", [])
    if not isinstance(raw_authorities, list) or not isinstance(raw_resolutions, list):
        raise ValueError("allocation checkpoint collections must be lists")

    authorities = []
    for raw in raw_authorities:
        if not isinstance(raw, Mapping):
            raise ValueError("allocation authority checkpoint row must be a mapping")
        authorities.append(AllocationAuthorityEvidence(
            authority_check_id=str(raw["authority_check_id"]),
            actor_id=str(raw["actor_id"]),
            action_ref=str(raw["action_ref"]),
            target_resource_id=str(raw["target_resource_id"]),
            state=AllocationAuthorityState(str(raw["state"])),
            checked_tick=int(raw["checked_tick"]),
            valid_until_tick=None if raw.get("valid_until_tick") is None else int(raw["valid_until_tick"]),
        ))

    resolutions = []
    for raw in raw_resolutions:
        if not isinstance(raw, Mapping):
            raise ValueError("allocation resolution checkpoint row must be a mapping")
        conflicts = raw.get("conflicting_reservation_ids", [])
        basis = raw.get("basis_refs", [])
        if not isinstance(conflicts, list) or not isinstance(basis, list):
            raise ValueError("allocation resolution references must be lists")
        selected = raw.get("selected_reservation_id")
        resolutions.append(ResourceAllocationResolution(
            resolution_id=str(raw["resolution_id"]),
            proposal_id=str(raw["proposal_id"]),
            resource_id=str(raw["resource_id"]),
            decision_actor_id=str(raw["decision_actor_id"]),
            authority_check_id=str(raw["authority_check_id"]),
            resolution_kind=AllocationResolutionKind(str(raw["resolution_kind"])),
            decided_tick=int(raw["decided_tick"]),
            conflicting_reservation_ids=tuple(sorted(str(value) for value in conflicts)),
            selected_reservation_id=None if selected is None else str(selected),
            basis_refs=tuple(str(value) for value in basis),
        ))

    authority_tuple = tuple(sorted(authorities, key=lambda item: item.authority_check_id))
    ledger = ResourceAllocationResolutionLedger(
        tuple(sorted(resolutions, key=lambda item: item.resolution_id))
    )
    _validate_allocation_history(authority_tuple, ledger, admission_ledger)
    return (*base, authority_tuple, ledger)


def _validate_allocation_history(authorities, ledger, admission_ledger) -> None:
    authority_ids = [row.authority_check_id for row in authorities]
    if len(authority_ids) != len(set(authority_ids)):
        raise ValueError("resource checkpoint contains duplicate allocation authority check IDs")
    resolution_ids = [row.resolution_id for row in ledger.resolutions]
    if len(resolution_ids) != len(set(resolution_ids)):
        raise ValueError("resource checkpoint contains duplicate allocation resolution IDs")

    authority_by_id = {row.authority_check_id: row for row in authorities}
    conflict_records = [row for row in admission_ledger.records if row.state == RescheduleAdmissionState.CONFLICT]

    for row in ledger.resolutions:
        candidates = [
            admission for admission in conflict_records
            if admission.proposal_id == row.proposal_id
            and admission.resource_id == row.resource_id
            and tuple(sorted(admission.conflicting_reservation_ids)) == tuple(sorted(row.conflicting_reservation_ids))
            and admission.assessed_tick <= row.decided_tick
        ]
        if not candidates:
            raise ValueError(f"allocation resolution lacks matching historical conflict admission: {row.resolution_id}")

        authority = authority_by_id.get(row.authority_check_id)
        if authority is None:
            raise ValueError(f"allocation resolution references missing authority evidence: {row.resolution_id}")
        if authority.actor_id != row.decision_actor_id:
            raise ValueError(f"allocation resolution authority actor mismatch: {row.resolution_id}")
        if authority.action_ref != "ALLOCATE_RESOURCE_WINDOW":
            raise ValueError(f"allocation resolution authority action mismatch: {row.resolution_id}")
        if authority.target_resource_id != row.resource_id:
            raise ValueError(f"allocation resolution authority resource mismatch: {row.resolution_id}")
        if authority.state != AllocationAuthorityState.AUTHORIZED or not authority.is_current_at(row.decided_tick):
            raise ValueError(f"allocation resolution authority not current: {row.resolution_id}")

        conflicts = set(row.conflicting_reservation_ids)
        if row.resolution_kind == AllocationResolutionKind.SELECT_EXISTING_RESERVATION:
            if row.selected_reservation_id not in conflicts:
                raise ValueError(f"allocation resolution selected reservation mismatch: {row.resolution_id}")
        elif row.selected_reservation_id is not None:
            raise ValueError(f"allocation resolution unexpectedly selects reservation: {row.resolution_id}")


def validate_allocation_checkpoint_time(
    authorities: tuple[AllocationAuthorityEvidence, ...],
    ledger: ResourceAllocationResolutionLedger,
    *,
    semantic_minute: int,
) -> None:
    for row in authorities:
        if row.checked_tick > semantic_minute:
            raise ValueError(f"allocation authority evidence comes from the future: {row.authority_check_id}")
    for row in ledger.resolutions:
        if row.decided_tick > semantic_minute:
            raise ValueError(f"allocation resolution comes from the future: {row.resolution_id}")
