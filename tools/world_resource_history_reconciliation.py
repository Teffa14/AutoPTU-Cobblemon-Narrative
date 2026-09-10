from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from tools.global_npc_holder_history_coverage import (
    HolderHistoryCoverageBaseline,
    derive_complete_holder_history_resource_ids,
)
from tools.global_npc_resource_handoffs import ResourceHandoffLedger, custody_history
from tools.global_npc_resource_holder_transitions import (
    ResourceHolderTransitionLedger,
    holder_history,
)
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
    holder_transition_ledger: ResourceHolderTransitionLedger | None = None,
    complete_holder_history_resource_ids: frozenset[str] = frozenset(),
    holder_history_coverage_baselines: tuple[HolderHistoryCoverageBaseline, ...] = (),
) -> WorldResourceReconciliationReport:
    """Compare current resource state with historical ledgers conservatively.

    The current catalog remains authoritative for present operational state. Historical
    reservation, custody and holder-transition ledgers can confirm compatible facts or
    prove narrow contradictions. Holder history becomes conflict-grade evidence only
    when completeness is supplied by a bounded authoritative baseline or by the legacy
    explicit audited-id argument. Missing or unaudited transitions stay indeterminate.
    """
    if isinstance(semantic_minute, bool) or not isinstance(semantic_minute, int):
        raise ValueError("semantic_minute must be an integer")
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")
    if complete_holder_history_resource_ids and holder_history_coverage_baselines:
        raise ValueError("use holder history coverage baselines or explicit complete ids, not both")
    if (complete_holder_history_resource_ids or holder_history_coverage_baselines) and holder_transition_ledger is None:
        raise ValueError("complete holder history requires a holder transition ledger")

    catalog: dict[str, WorldResource] = {}
    for resource in sorted(resources, key=lambda item: item.resource_id):
        if resource.resource_id in catalog:
            raise ValueError("duplicate world resource id")
        catalog[resource.resource_id] = resource

    if holder_history_coverage_baselines:
        effective_complete_ids = derive_complete_holder_history_resource_ids(
            catalog.values(),
            holder_history_coverage_baselines,
            holder_transition_ledger,
            through_tick=semantic_minute,
        )
    else:
        effective_complete_ids = complete_holder_history_resource_ids

    unknown_complete_ids = effective_complete_ids - set(catalog)
    if unknown_complete_ids:
        raise ValueError("complete holder history references resource absent from current catalog")

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

        if holder_transition_ledger is not None:
            transitions = holder_history(
                holder_transition_ledger,
                resource_id,
                through_tick=semantic_minute,
            )
            history_is_complete = resource_id in effective_complete_ids
            if transitions:
                latest_transition = transitions[-1]
                if history_is_complete:
                    if resource.holder_actor_id == latest_transition.to_actor_id:
                        findings.append(
                            _finding(
                                resource_id,
                                ReconciliationStatus.CONFIRMED,
                                "CURRENT_HOLDER_MATCHES_COMPLETE_HOLDER_JOURNAL",
                                latest_transition.transition_id,
                            )
                        )
                    else:
                        findings.append(
                            _finding(
                                resource_id,
                                ReconciliationStatus.CONFLICT,
                                "CURRENT_HOLDER_CONFLICTS_COMPLETE_HOLDER_JOURNAL",
                                latest_transition.transition_id,
                            )
                        )
                else:
                    findings.append(
                        _finding(
                            resource_id,
                            ReconciliationStatus.INDETERMINATE,
                            "HOLDER_JOURNAL_COVERAGE_NOT_AUDITED_COMPLETE",
                            latest_transition.transition_id,
                        )
                    )
            elif history_is_complete:
                if resource.holder_actor_id is None:
                    findings.append(
                        _finding(
                            resource_id,
                            ReconciliationStatus.CONFIRMED,
                            "CURRENT_UNHELD_STATE_MATCHES_COMPLETE_EMPTY_HOLDER_JOURNAL",
                        )
                    )
                else:
                    findings.append(
                        _finding(
                            resource_id,
                            ReconciliationStatus.CONFLICT,
                            "CURRENT_HOLDER_LACKS_COMPLETE_HOLDER_JOURNAL_TRANSITION",
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
    referenced_transition_ids: dict[str, list[str]] = {}
    if holder_transition_ledger is not None:
        for transition in holder_transition_ledger.transitions:
            if transition.at_tick <= semantic_minute:
                referenced_transition_ids.setdefault(transition.resource_id, []).append(
                    transition.transition_id
                )

    missing_ids = sorted(
        (
            set(referenced_reservation_ids)
            | set(referenced_transfer_ids)
            | set(referenced_transition_ids)
        )
        - set(catalog)
    )
    for resource_id in missing_ids:
        findings.append(
            _finding(
                resource_id,
                ReconciliationStatus.INDETERMINATE,
                "HISTORY_REFERENCES_RESOURCE_ABSENT_FROM_CURRENT_CATALOG",
                *referenced_reservation_ids.get(resource_id, []),
                *referenced_transfer_ids.get(resource_id, []),
                *referenced_transition_ids.get(resource_id, []),
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
