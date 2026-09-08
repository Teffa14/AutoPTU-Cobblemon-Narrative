from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from tools.global_npc_resource_handoff_reschedule_admission import (
    RescheduleAdmissionAssessment,
    RescheduleAdmissionState,
)


class AllocationAuthorityState(str, Enum):
    AUTHORIZED = "AUTHORIZED"
    NOT_AUTHORIZED = "NOT_AUTHORIZED"
    NEEDS_VERIFICATION = "NEEDS_VERIFICATION"
    AMBIGUOUS = "AMBIGUOUS"


class AllocationResolutionKind(str, Enum):
    SELECT_PROPOSED_WINDOW = "SELECT_PROPOSED_WINDOW"
    SELECT_EXISTING_RESERVATION = "SELECT_EXISTING_RESERVATION"
    DEFER = "DEFER"


@dataclass(frozen=True)
class AllocationAuthorityEvidence:
    authority_check_id: str
    actor_id: str
    action_ref: str
    target_resource_id: str
    state: AllocationAuthorityState
    checked_tick: int
    valid_until_tick: int | None = None

    def __post_init__(self) -> None:
        if not self.authority_check_id.strip():
            raise ValueError("authority_check_id is required")
        if not self.actor_id.strip():
            raise ValueError("actor_id is required")
        if not self.action_ref.strip():
            raise ValueError("action_ref is required")
        if not self.target_resource_id.strip():
            raise ValueError("target_resource_id is required")
        if self.checked_tick < 0:
            raise ValueError("checked_tick must be non-negative")
        if self.valid_until_tick is not None and self.valid_until_tick <= self.checked_tick:
            raise ValueError("valid_until_tick must be greater than checked_tick")

    def is_current_at(self, at_tick: int) -> bool:
        if at_tick < self.checked_tick:
            return False
        if self.valid_until_tick is not None and at_tick >= self.valid_until_tick:
            return False
        return True


@dataclass(frozen=True)
class ResourceAllocationResolution:
    resolution_id: str
    proposal_id: str
    resource_id: str
    decision_actor_id: str
    authority_check_id: str
    resolution_kind: AllocationResolutionKind
    decided_tick: int
    conflicting_reservation_ids: tuple[str, ...]
    selected_reservation_id: str | None = None
    basis_refs: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.resolution_id.strip():
            raise ValueError("resolution_id is required")
        if not self.proposal_id.strip():
            raise ValueError("proposal_id is required")
        if not self.resource_id.strip():
            raise ValueError("resource_id is required")
        if not self.decision_actor_id.strip():
            raise ValueError("decision_actor_id is required")
        if not self.authority_check_id.strip():
            raise ValueError("authority_check_id is required")
        if self.decided_tick < 0:
            raise ValueError("decided_tick must be non-negative")


@dataclass(frozen=True)
class ResourceAllocationResolutionLedger:
    resolutions: tuple[ResourceAllocationResolution, ...] = ()


@dataclass(frozen=True)
class AllocationResolutionResult:
    accepted: bool
    ledger: ResourceAllocationResolutionLedger
    resolution: ResourceAllocationResolution | None = None
    reason_code: str = "ALLOCATION_RESOLUTION_RECORDED"


def _existing_resolution(
    ledger: ResourceAllocationResolutionLedger,
    resolution_id: str,
) -> ResourceAllocationResolution | None:
    return next((item for item in ledger.resolutions if item.resolution_id == resolution_id), None)


def record_allocation_resolution(
    ledger: ResourceAllocationResolutionLedger,
    assessment: RescheduleAdmissionAssessment,
    authority: AllocationAuthorityEvidence,
    *,
    resolution_id: str,
    decision_actor_id: str,
    resolution_kind: AllocationResolutionKind,
    decided_tick: int,
    selected_reservation_id: str | None = None,
    basis_refs: tuple[str, ...] = (),
) -> AllocationResolutionResult:
    """Record a provenance-backed response to a real resource-window conflict.

    The result is an institutional/world decision record only. It does not cancel
    reservations, accept a handoff reschedule, transfer custody, or create a global
    priority rule.
    """
    if _existing_resolution(ledger, resolution_id) is not None:
        return AllocationResolutionResult(False, ledger, reason_code="DUPLICATE_RESOLUTION_ID")

    if assessment.state != RescheduleAdmissionState.CONFLICT or not assessment.resource_id:
        return AllocationResolutionResult(False, ledger, reason_code="NO_RESOURCE_CONFLICT_TO_RESOLVE")

    if authority.actor_id != decision_actor_id:
        return AllocationResolutionResult(False, ledger, reason_code="AUTHORITY_ACTOR_MISMATCH")
    if authority.action_ref != "ALLOCATE_RESOURCE_WINDOW":
        return AllocationResolutionResult(False, ledger, reason_code="AUTHORITY_ACTION_MISMATCH")
    if authority.target_resource_id != assessment.resource_id:
        return AllocationResolutionResult(False, ledger, reason_code="AUTHORITY_RESOURCE_MISMATCH")
    if authority.state != AllocationAuthorityState.AUTHORIZED:
        return AllocationResolutionResult(False, ledger, reason_code="ALLOCATION_AUTHORITY_NOT_ESTABLISHED")
    if not authority.is_current_at(decided_tick):
        return AllocationResolutionResult(False, ledger, reason_code="ALLOCATION_AUTHORITY_NOT_CURRENT")

    conflicts = tuple(sorted(assessment.conflicting_reservation_ids))
    if resolution_kind == AllocationResolutionKind.SELECT_EXISTING_RESERVATION:
        if selected_reservation_id not in conflicts:
            return AllocationResolutionResult(False, ledger, reason_code="SELECTED_RESERVATION_NOT_IN_CONFLICT_SET")
    elif selected_reservation_id is not None:
        return AllocationResolutionResult(False, ledger, reason_code="UNEXPECTED_SELECTED_RESERVATION")

    resolution = ResourceAllocationResolution(
        resolution_id=resolution_id,
        proposal_id=assessment.proposal_id,
        resource_id=assessment.resource_id,
        decision_actor_id=decision_actor_id,
        authority_check_id=authority.authority_check_id,
        resolution_kind=resolution_kind,
        decided_tick=decided_tick,
        conflicting_reservation_ids=conflicts,
        selected_reservation_id=selected_reservation_id,
        basis_refs=tuple(basis_refs),
    )
    updated = ResourceAllocationResolutionLedger(
        resolutions=tuple(sorted((*ledger.resolutions, resolution), key=lambda item: item.resolution_id))
    )
    return AllocationResolutionResult(True, updated, resolution=resolution)
