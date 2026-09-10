from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from tools.global_npc_resource_handoffs import ResourceHandoffLedger, custody_history
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    active_reservations_for_resource,
)
from tools.global_npc_resources import ResourceState, WorldResource


class ReconciliationStatus(str, Enum):
    CONFIRMED = "CONFIRMED"
    INDETERMINATE = "INDETERMINATE"
    CONFLICT = "CONFLICT"


@dataclass(frozen=True)
class ResourceReconciliationFinding:
    resource_id: str
    status: ReconciliationStatus
    reason_code: str
    evidence_refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class WorldResourceReconciliationReport:
    semantic_minute: int
    findings: tuple[ResourceReconciliationFinding, ...]

    @property
    def safe_to_restore(self) -> bool:
        return not any(
            finding.status == ReconciliationStatus.CONFLICT
            for finding in self.findings
        )

    @property
    def conflicts(self) -> tuple[ResourceReconciliationFinding, ...]:
        return tuple(
            finding
            for finding in self.findings
            if finding.status == ReconciliationStatus.CONFLICT
        )

    @property
    def indeterminate(self) -> tuple[ResourceReconciliationFinding, ...]:
        return tuple(
            finding
            for finding in self.findings
            if finding.status == ReconciliationStatus.INDETERMINATE
        )

    @property
    def confirmed(self) -> tuple[ResourceReconciliationFinding, ...]:
        return tuple(
            finding
            for finding in self.findings
            if finding.status == ReconciliationStatus.CONFIRMED
        )


def _finding(
    resource_id: str,
    status: ReconciliationStatus,
    reason_code: str,
    *evidence_refs: str,
) -> ResourceReconciliationFinding:
    return ResourceReconciliationFinding(
        resource_id=resource_id,
        status=status,
        reason_code=reason_code,
        evidence_refs=tuple(sorted(evidence_refs)),
    )


def reconcile_world_resource_history(
    resources: Iterable[WorldResource],
    *,
    reservation_ledger: ReservationLedger,
    handoff_ledger: ResourceHandoffLedger,
    semantic_minute: int,
) -> WorldResourceReconciliationReport:
    """Compare current resource state with historical ledgers conservatively.

    The current catalog remains authoritative for present operational state. Historical
    reservation and custody ledgers can confirm compatible facts or prove narrow
    contradictions, but they do not form a complete event stream for every mutation of
    ``WorldResource``. In particular, checkout, return, service-state changes and other
    legal operations may change current holder/state without creating a custody
    transfer. A mismatch with the latest known handoff is therefore indeterminate, not
    automatically corruption.
    """
    if isinstance(semantic_minute, bool) or not isinstance(semantic_minute, int):
        raise ValueError("semantic_minute must be an integer")
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")

    catalog: dict[str, WorldResource] = {}
    for resource in sorted(resources, key=lambda item: item.resource_id):
        if resource.resource_id in catalog:
            raise ValueError("duplicate world resource id")
        catalog[resource.resource_id] = resource

    findings: list[ResourceReconciliationFinding] = []

    for resource_id, resource in catalog.items():
        active = active_reservations_for_resource(
            reservation_ledger,
            resource_id,
            semantic_minute,
        )
        if len(active) > 1:
            findings.append(
                _finding(
                    resource_id,
                    ReconciliationStatus.CONFLICT,
                    "MULTIPLE_ACTIVE_RESERVATIONS",
                    *(reservation.reservation_id for reservation in active),
                )
            )
        elif active:
            reservation = active[0]
            if (
                resource.reserved_for_actor_id is not None
                and resource.reserved_for_actor_id != reservation.actor_id
            ):
                findings.append(
                    _finding(
                        resource_id,
                        ReconciliationStatus.CONFLICT,
                        "CURRENT_RESERVATION_ACTOR_CONFLICT",
                        reservation.reservation_id,
                    )
                )
            elif resource.reserved_for_actor_id == reservation.actor_id:
                findings.append(
                    _finding(
                        resource_id,
                        ReconciliationStatus.CONFIRMED,
                        "CURRENT_RESERVATION_MATCHES_ACTIVE_HISTORY",
                        reservation.reservation_id,
                    )
                )
            else:
                findings.append(
                    _finding(
                        resource_id,
                        ReconciliationStatus.INDETERMINATE,
                        "ACTIVE_RESERVATION_NOT_PROJECTED_IN_CURRENT_CATALOG",
                        reservation.reservation_id,
                    )
                )
        elif resource.reserved_for_actor_id is not None:
            findings.append(
                _finding(
                    resource_id,
                    ReconciliationStatus.INDETERMINATE,
                    "CURRENT_RESERVATION_LACKS_ACTIVE_LEDGER_PROOF",
                )
            )

        if (
            resource.state == ResourceState.RESERVED
            and resource.reserved_for_actor_id is None
        ):
            findings.append(
                _finding(
                    resource_id,
                    ReconciliationStatus.CONFLICT,
                    "RESERVED_STATE_WITHOUT_RESERVED_ACTOR",
                )
            )

        transfers = tuple(
            transfer
            for transfer in custody_history(handoff_ledger, resource_id)
            if transfer.at_tick <= semantic_minute
        )
        if transfers:
            latest = transfers[-1]
            if resource.holder_actor_id == latest.to_actor_id:
                findings.append(
                    _finding(
                        resource_id,
                        ReconciliationStatus.CONFIRMED,
                        "CURRENT_HOLDER_MATCHES_LATEST_KNOWN_HANDOFF",
                        latest.transfer_id,
                    )
                )
            else:
                findings.append(
                    _finding(
                        resource_id,
                        ReconciliationStatus.INDETERMINATE,
                        "CURRENT_HOLDER_NOT_DERIVABLE_FROM_HANDOFF_HISTORY",
                        latest.transfer_id,
                    )
                )

    referenced_reservation_ids: dict[str, list[str]] = {}
    for reservation in reservation_ledger.reservations:
        referenced_reservation_ids.setdefault(reservation.resource_id, []).append(
            reservation.reservation_id
        )
    referenced_transfer_ids: dict[str, list[str]] = {}
    for transfer in handoff_ledger.transfers:
        if transfer.at_tick <= semantic_minute:
            referenced_transfer_ids.setdefault(transfer.resource_id, []).append(
                transfer.transfer_id
            )

    missing_ids = sorted(
        (set(referenced_reservation_ids) | set(referenced_transfer_ids)) - set(catalog)
    )
    for resource_id in missing_ids:
        findings.append(
            _finding(
                resource_id,
                ReconciliationStatus.INDETERMINATE,
                "HISTORY_REFERENCES_RESOURCE_ABSENT_FROM_CURRENT_CATALOG",
                *referenced_reservation_ids.get(resource_id, []),
                *referenced_transfer_ids.get(resource_id, []),
            )
        )

    findings.sort(
        key=lambda finding: (
            finding.resource_id,
            finding.status.value,
            finding.reason_code,
            finding.evidence_refs,
        )
    )
    return WorldResourceReconciliationReport(
        semantic_minute=semantic_minute,
        findings=tuple(findings),
    )
