from __future__ import annotations

from dataclasses import dataclass

from tools.global_npc_resource_handoff_reschedule_admission import (
    RescheduleAdmissionAssessment,
    RescheduleAdmissionState,
)


@dataclass(frozen=True)
class ResourceRescheduleAdmissionRecord:
    record_id: str
    proposal_id: str
    resource_id: str
    state: RescheduleAdmissionState
    assessed_tick: int
    conflicting_reservation_ids: tuple[str, ...] = ()
    matched_same_purpose_reservation_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.record_id.strip():
            raise ValueError("record_id is required")
        if not self.proposal_id.strip():
            raise ValueError("proposal_id is required")
        if not self.resource_id.strip():
            raise ValueError("resource_id is required")
        if self.assessed_tick < 0:
            raise ValueError("assessed_tick must be non-negative")
        if self.state not in {RescheduleAdmissionState.CLEAR, RescheduleAdmissionState.CONFLICT}:
            raise ValueError("only resolved CLEAR or CONFLICT admissions can be recorded")


@dataclass(frozen=True)
class ResourceRescheduleAdmissionLedger:
    records: tuple[ResourceRescheduleAdmissionRecord, ...] = ()


def record_reschedule_admission(
    ledger: ResourceRescheduleAdmissionLedger,
    assessment: RescheduleAdmissionAssessment,
    *,
    record_id: str,
    assessed_tick: int,
) -> ResourceRescheduleAdmissionLedger:
    """Capture a Pass 347 read assessment as historical evidence.

    The record freezes what the admission layer saw at one semantic moment. It does
    not decide priority or mutate reservations, reschedules, custody or authority.
    """
    if any(row.record_id == record_id for row in ledger.records):
        raise ValueError("duplicate reschedule admission record ID")
    if assessment.state not in {RescheduleAdmissionState.CLEAR, RescheduleAdmissionState.CONFLICT}:
        raise ValueError("unresolved admission assessment cannot be recorded")
    if not assessment.resource_id:
        raise ValueError("resolved admission assessment requires resource_id")

    record = ResourceRescheduleAdmissionRecord(
        record_id=record_id,
        proposal_id=assessment.proposal_id,
        resource_id=assessment.resource_id,
        state=assessment.state,
        assessed_tick=assessed_tick,
        conflicting_reservation_ids=tuple(sorted(assessment.conflicting_reservation_ids)),
        matched_same_purpose_reservation_ids=tuple(sorted(assessment.matched_same_purpose_reservation_ids)),
    )
    return ResourceRescheduleAdmissionLedger(
        tuple(sorted((*ledger.records, record), key=lambda item: (item.assessed_tick, item.record_id)))
    )
