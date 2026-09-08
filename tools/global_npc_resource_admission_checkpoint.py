from __future__ import annotations

from typing import Mapping

from tools.global_npc_resource_handoff_attempts import ResourceHandoffAttemptLedger
from tools.global_npc_resource_handoff_appointments import ResourceHandoffAppointmentLedger
from tools.global_npc_resource_handoff_reschedule_admission import RescheduleAdmissionState
from tools.global_npc_resource_handoff_reschedule_admission_history import (
    ResourceRescheduleAdmissionLedger,
    ResourceRescheduleAdmissionRecord,
)
from tools.global_npc_resource_handoff_rescheduling import ResourceHandoffRescheduleLedger
from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_requests import ResourceRequestLedger
from tools.global_npc_resource_reservations import ReservationLedger
from tools.global_npc_resource_reschedule_checkpoint import (
    RESOURCE_CHECKPOINT_RESCHEDULE_SCHEMA,
    restore_resource_state_with_reschedules,
    snapshot_resource_state_with_reschedules,
)


RESOURCE_CHECKPOINT_ADMISSION_SCHEMA = "OUROS_NPC_RESOURCE_CHECKPOINT_V6"


def snapshot_resource_state_with_admissions(
    reservation_ledger: ReservationLedger,
    request_ledger: ResourceRequestLedger,
    handoff_ledger: ResourceHandoffLedger,
    attempt_ledger: ResourceHandoffAttemptLedger,
    appointment_ledger: ResourceHandoffAppointmentLedger,
    reschedule_ledger: ResourceHandoffRescheduleLedger,
    admission_ledger: ResourceRescheduleAdmissionLedger,
) -> dict:
    snapshot = snapshot_resource_state_with_reschedules(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
    )
    snapshot["schema"] = RESOURCE_CHECKPOINT_ADMISSION_SCHEMA
    snapshot["reschedule_admission_records"] = [
        {
            "record_id": row.record_id,
            "proposal_id": row.proposal_id,
            "resource_id": row.resource_id,
            "state": row.state.value,
            "assessed_tick": row.assessed_tick,
            "conflicting_reservation_ids": list(row.conflicting_reservation_ids),
            "matched_same_purpose_reservation_ids": list(row.matched_same_purpose_reservation_ids),
        }
        for row in sorted(admission_ledger.records, key=lambda item: (item.assessed_tick, item.record_id))
    ]
    return snapshot


def restore_resource_state_with_admissions(
    snapshot: Mapping[str, object],
) -> tuple[
    ReservationLedger,
    ResourceRequestLedger,
    ResourceHandoffLedger,
    ResourceHandoffAttemptLedger,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffRescheduleLedger,
    ResourceRescheduleAdmissionLedger,
]:
    schema = snapshot.get("schema")
    if schema != RESOURCE_CHECKPOINT_ADMISSION_SCHEMA:
        reservations, requests, handoffs, attempts, appointments, reschedules = restore_resource_state_with_reschedules(snapshot)
        return reservations, requests, handoffs, attempts, appointments, reschedules, ResourceRescheduleAdmissionLedger()

    base_snapshot = dict(snapshot)
    base_snapshot["schema"] = RESOURCE_CHECKPOINT_RESCHEDULE_SCHEMA
    base_snapshot.pop("reschedule_admission_records", None)
    reservations, requests, handoffs, attempts, appointments, reschedules = restore_resource_state_with_reschedules(base_snapshot)

    raw_records = snapshot.get("reschedule_admission_records", [])
    if not isinstance(raw_records, list):
        raise ValueError("reschedule admission checkpoint collection must be a list")

    records: list[ResourceRescheduleAdmissionRecord] = []
    for raw in raw_records:
        if not isinstance(raw, Mapping):
            raise ValueError("reschedule admission checkpoint row must be a mapping")
        conflicts = raw.get("conflicting_reservation_ids", [])
        matched = raw.get("matched_same_purpose_reservation_ids", [])
        if not isinstance(conflicts, list) or not isinstance(matched, list):
            raise ValueError("reschedule admission reservation IDs must be lists")
        records.append(
            ResourceRescheduleAdmissionRecord(
                record_id=str(raw["record_id"]),
                proposal_id=str(raw["proposal_id"]),
                resource_id=str(raw["resource_id"]),
                state=RescheduleAdmissionState(str(raw["state"])),
                assessed_tick=int(raw["assessed_tick"]),
                conflicting_reservation_ids=tuple(sorted(str(value) for value in conflicts)),
                matched_same_purpose_reservation_ids=tuple(sorted(str(value) for value in matched)),
            )
        )

    ledger = ResourceRescheduleAdmissionLedger(
        tuple(sorted(records, key=lambda item: (item.assessed_tick, item.record_id)))
    )
    _validate_admission_history(ledger, reservations, handoffs, reschedules)
    return reservations, requests, handoffs, attempts, appointments, reschedules, ledger


def _windows_overlap(start_a: int, end_a: int, start_b: int, end_b: int) -> bool:
    return start_a < end_b and start_b < end_a


def _validate_admission_history(
    ledger: ResourceRescheduleAdmissionLedger,
    reservations: ReservationLedger,
    handoffs: ResourceHandoffLedger,
    reschedules: ResourceHandoffRescheduleLedger,
) -> None:
    record_ids = [row.record_id for row in ledger.records]
    if len(record_ids) != len(set(record_ids)):
        raise ValueError("resource checkpoint contains duplicate reschedule admission record IDs")

    proposals = {row.proposal_id: row for row in reschedules.proposals}
    authorizations = {row.authorization_id: row for row in handoffs.authorizations}
    reservation_by_id = {row.reservation_id: row for row in reservations.reservations}

    for row in ledger.records:
        proposal = proposals.get(row.proposal_id)
        if proposal is None:
            raise ValueError(f"reschedule admission references missing proposal: {row.record_id}")
        authorization = authorizations.get(proposal.authorization_id)
        if authorization is None:
            raise ValueError(f"reschedule admission references missing authorization: {row.record_id}")
        if row.resource_id != authorization.resource_id:
            raise ValueError(f"reschedule admission resource mismatch: {row.record_id}")
        if row.assessed_tick < proposal.created_tick:
            raise ValueError(f"reschedule admission predates proposal: {row.record_id}")
        if proposal.proposed_valid_until_tick is None:
            raise ValueError(f"resolved reschedule admission cannot reference unbounded window: {row.record_id}")
        if row.state == RescheduleAdmissionState.CONFLICT and not row.conflicting_reservation_ids:
            raise ValueError(f"conflict admission lacks conflict evidence: {row.record_id}")
        if row.state == RescheduleAdmissionState.CLEAR and row.conflicting_reservation_ids:
            raise ValueError(f"clear admission contains conflict evidence: {row.record_id}")

        same_purpose_refs = {authorization.authorization_id, authorization.request_id, proposal.proposal_id}
        seen = set(row.conflicting_reservation_ids) | set(row.matched_same_purpose_reservation_ids)
        if len(seen) != len(row.conflicting_reservation_ids) + len(row.matched_same_purpose_reservation_ids):
            raise ValueError(f"reschedule admission classifies one reservation twice: {row.record_id}")

        for reservation_id in row.conflicting_reservation_ids:
            reservation = reservation_by_id.get(reservation_id)
            if reservation is None:
                raise ValueError(f"reschedule admission references missing conflict reservation: {row.record_id}")
            if reservation.resource_id != row.resource_id or reservation.purpose_ref in same_purpose_refs:
                raise ValueError(f"reschedule admission conflict evidence mismatch: {row.record_id}")
            if not _windows_overlap(
                proposal.proposed_valid_from_tick,
                proposal.proposed_valid_until_tick,
                reservation.start_tick,
                reservation.end_tick,
            ):
                raise ValueError(f"reschedule admission conflict window mismatch: {row.record_id}")

        for reservation_id in row.matched_same_purpose_reservation_ids:
            reservation = reservation_by_id.get(reservation_id)
            if reservation is None:
                raise ValueError(f"reschedule admission references missing same-purpose reservation: {row.record_id}")
            if reservation.resource_id != row.resource_id or reservation.purpose_ref not in same_purpose_refs:
                raise ValueError(f"reschedule admission same-purpose evidence mismatch: {row.record_id}")
            if not _windows_overlap(
                proposal.proposed_valid_from_tick,
                proposal.proposed_valid_until_tick,
                reservation.start_tick,
                reservation.end_tick,
            ):
                raise ValueError(f"reschedule admission same-purpose window mismatch: {row.record_id}")


def validate_admission_checkpoint_time(
    ledger: ResourceRescheduleAdmissionLedger,
    *,
    semantic_minute: int,
) -> None:
    for row in ledger.records:
        if row.assessed_tick > semantic_minute:
            raise ValueError(f"reschedule admission assessment comes from the future: {row.record_id}")
