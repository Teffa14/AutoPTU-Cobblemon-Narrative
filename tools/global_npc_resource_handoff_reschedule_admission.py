from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from tools.global_npc_resource_handoff_rescheduling import (
    ResourceHandoffRescheduleLedger,
    ResourceHandoffRescheduleProposal,
)
from tools.global_npc_resource_handoffs import ResourceHandoffAuthorization, ResourceHandoffLedger
from tools.global_npc_resource_reservations import ReservationLedger, ReservationState


class RescheduleAdmissionState(str, Enum):
    CLEAR = "CLEAR"
    CONFLICT = "CONFLICT"
    UNKNOWN_PROPOSAL = "UNKNOWN_PROPOSAL"
    UNKNOWN_AUTHORIZATION = "UNKNOWN_AUTHORIZATION"
    UNBOUNDED_WINDOW = "UNBOUNDED_WINDOW"


@dataclass(frozen=True)
class RescheduleAdmissionAssessment:
    state: RescheduleAdmissionState
    proposal_id: str
    resource_id: str | None = None
    conflicting_reservation_ids: tuple[str, ...] = ()
    matched_same_purpose_reservation_ids: tuple[str, ...] = ()

    @property
    def admissible(self) -> bool:
        return self.state == RescheduleAdmissionState.CLEAR


def _proposal_by_id(
    ledger: ResourceHandoffRescheduleLedger,
    proposal_id: str,
) -> ResourceHandoffRescheduleProposal | None:
    return next((item for item in ledger.proposals if item.proposal_id == proposal_id), None)


def _authorization_by_id(
    ledger: ResourceHandoffLedger,
    authorization_id: str,
) -> ResourceHandoffAuthorization | None:
    return next((item for item in ledger.authorizations if item.authorization_id == authorization_id), None)


def _windows_overlap(start_a: int, end_a: int, start_b: int, end_b: int) -> bool:
    return start_a < end_b and start_b < end_a


def assess_reschedule_resource_window(
    reschedule_ledger: ResourceHandoffRescheduleLedger,
    handoff_ledger: ResourceHandoffLedger,
    reservation_ledger: ReservationLedger,
    *,
    proposal_id: str,
) -> RescheduleAdmissionAssessment:
    """Screen a proposed successor handoff window against known reservations.

    This is an admission/read model only. It does not accept a proposal, move a
    resource, create or cancel a reservation, or choose whose work has priority.
    """
    proposal = _proposal_by_id(reschedule_ledger, proposal_id)
    if proposal is None:
        return RescheduleAdmissionAssessment(RescheduleAdmissionState.UNKNOWN_PROPOSAL, proposal_id)

    authorization = _authorization_by_id(handoff_ledger, proposal.authorization_id)
    if authorization is None:
        return RescheduleAdmissionAssessment(
            RescheduleAdmissionState.UNKNOWN_AUTHORIZATION,
            proposal_id,
        )

    if proposal.proposed_valid_until_tick is None:
        return RescheduleAdmissionAssessment(
            RescheduleAdmissionState.UNBOUNDED_WINDOW,
            proposal_id,
            resource_id=authorization.resource_id,
        )

    same_purpose_refs = {
        authorization.authorization_id,
        authorization.request_id,
        proposal.proposal_id,
    }
    conflicts: list[str] = []
    matched: list[str] = []
    for reservation in sorted(reservation_ledger.reservations, key=lambda item: item.reservation_id):
        if reservation.state != ReservationState.ACTIVE:
            continue
        if reservation.resource_id != authorization.resource_id:
            continue
        if not _windows_overlap(
            proposal.proposed_valid_from_tick,
            proposal.proposed_valid_until_tick,
            reservation.start_tick,
            reservation.end_tick,
        ):
            continue
        if reservation.purpose_ref in same_purpose_refs:
            matched.append(reservation.reservation_id)
        else:
            conflicts.append(reservation.reservation_id)

    state = RescheduleAdmissionState.CONFLICT if conflicts else RescheduleAdmissionState.CLEAR
    return RescheduleAdmissionAssessment(
        state,
        proposal_id,
        resource_id=authorization.resource_id,
        conflicting_reservation_ids=tuple(conflicts),
        matched_same_purpose_reservation_ids=tuple(matched),
    )
