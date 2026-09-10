from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_holder_history_baseline_issuance import (
    issue_holder_history_coverage_baselines_from_catalog_checkpoint,
)
from tools.global_npc_holder_history_coverage import HolderHistoryCoverageBaseline
from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_reservations import ReservationLedger
from tools.persistent_world_recovery_manifest import ReconciledPersistentWorldRecoveryManifest
from tools.resource_holder_transition_checkpoint import RestoredResourceHolderTransitions
from tools.world_resource_catalog_checkpoint import (
    RestoredWorldResourceCatalog,
    restore_world_resource_catalog,
)
from tools.world_resource_history_reconciliation import (
    WorldResourceReconciliationReport,
    reconcile_world_resource_history,
)


@dataclass(frozen=True)
class PersistentWorldPostRestoreValidation:
    semantic_minute: int
    resource_report: WorldResourceReconciliationReport
    issued_holder_history_coverage_baselines: tuple[HolderHistoryCoverageBaseline, ...] = ()

    @property
    def safe_to_activate(self) -> bool:
        return self.resource_report.safe_to_restore


def validate_persistent_world_post_restore(
    recovery_manifest: ReconciledPersistentWorldRecoveryManifest,
    resource_catalog: RestoredWorldResourceCatalog,
    *,
    reservation_ledger: ReservationLedger,
    handoff_ledger: ResourceHandoffLedger,
    holder_transitions: RestoredResourceHolderTransitions | None = None,
    resource_catalog_checkpoint_snapshot: Mapping[str, object] | None = None,
    complete_holder_history_resource_ids: frozenset[str] = frozenset(),
) -> PersistentWorldPostRestoreValidation:
    """Run cross-owner checks, then optionally issue a future-facing holder baseline.

    When a V3 recovery caller supplies the exact WorldResource catalog checkpoint selected
    by the outer manifest, this stage validates that generation against the manifest digest
    and restored catalog. Only after historical reconciliation succeeds does it reissue
    bounded holder-history baselines from that checkpoint.

    Those baselines are an authoritative starting cut for future holder continuity. They
    are never fed back into reconciliation of the same cut, because doing so would make
    current catalog state prove itself and could hide incomplete pre-checkpoint history.

    A V3 caller that does not retain the raw selected catalog checkpoint can still perform
    the older conservative reconciliation, but receives no baseline certificates. Callers
    can no longer inject authored bounded-baseline objects into this activation boundary.
    """
    if resource_catalog.semantic_minute != recovery_manifest.semantic_minute:
        raise ValueError("post-restore resource catalog semantic minute mismatch")
    catalog_digest = recovery_manifest.world_resource_catalog_checkpoint_sha256
    if catalog_digest is None:
        raise ValueError("post-restore resource validation requires a V2 recovery manifest")

    holder_digest = recovery_manifest.resource_holder_transition_checkpoint_sha256
    if holder_digest is not None:
        if holder_transitions is None:
            raise ValueError("V3 post-restore validation requires restored holder transitions")
        if holder_transitions.semantic_minute != recovery_manifest.semantic_minute:
            raise ValueError("post-restore holder transition semantic minute mismatch")

        if resource_catalog_checkpoint_snapshot is not None:
            selected_catalog = restore_world_resource_catalog(
                resource_catalog_checkpoint_snapshot,
                recovery_semantic_minute=recovery_manifest.semantic_minute,
            )
            supplied_digest = resource_catalog_checkpoint_snapshot.get("sha256")
            if supplied_digest != catalog_digest:
                raise ValueError("post-restore resource catalog checkpoint digest does not match recovery manifest")
            if selected_catalog != resource_catalog:
                raise ValueError("post-restore resource catalog does not match selected checkpoint generation")
    else:
        if holder_transitions is not None:
            raise ValueError("legacy recovery manifest did not select holder transitions")
        if resource_catalog_checkpoint_snapshot is not None:
            raise ValueError("legacy recovery path does not issue holder-history baselines")

    if complete_holder_history_resource_ids and holder_transitions is None:
        raise ValueError("complete holder history requires restored holder transitions")

    report = reconcile_world_resource_history(
        resource_catalog.resources,
        reservation_ledger=reservation_ledger,
        handoff_ledger=handoff_ledger,
        semantic_minute=recovery_manifest.semantic_minute,
        holder_transition_ledger=(holder_transitions.ledger if holder_transitions is not None else None),
        complete_holder_history_resource_ids=complete_holder_history_resource_ids,
    )
    if not report.safe_to_restore:
        reason_codes = ",".join(
            sorted({finding.reason_code for finding in report.conflicts})
        )
        raise ValueError(f"post-restore world resource conflict: {reason_codes}")

    issued_baselines: tuple[HolderHistoryCoverageBaseline, ...] = ()
    if holder_digest is not None and resource_catalog_checkpoint_snapshot is not None:
        issued_baselines = issue_holder_history_coverage_baselines_from_catalog_checkpoint(
            resource_catalog_checkpoint_snapshot,
            expected_catalog_sha256=catalog_digest,
            recovery_semantic_minute=recovery_manifest.semantic_minute,
        )

    return PersistentWorldPostRestoreValidation(
        semantic_minute=recovery_manifest.semantic_minute,
        resource_report=report,
        issued_holder_history_coverage_baselines=issued_baselines,
    )
