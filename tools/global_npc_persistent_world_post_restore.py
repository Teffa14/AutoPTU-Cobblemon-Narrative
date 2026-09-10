from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_holder_history_baseline_issuance import (
    issue_holder_history_coverage_baselines_from_catalog_checkpoint,
)
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
    """Run cross-owner checks after coherent checkpoint selection and owner restore.

    V3 recovery must provide the exact WorldResource catalog checkpoint selected by the
    outer manifest. This stage validates that generation, verifies that its restored
    catalog is the catalog being activated, and reissues bounded holder-history
    baselines directly from that checkpoint. Callers cannot author those provenance
    certificates themselves.

    Explicit conflicts fail closed. Indeterminate findings remain visible and do not
    authorize rewriting catalog state or inventing missing resource history. Legacy
    complete-holder declarations remain a compatibility input and must still be backed
    by restored holder transitions.
    """
    if resource_catalog.semantic_minute != recovery_manifest.semantic_minute:
        raise ValueError("post-restore resource catalog semantic minute mismatch")
    catalog_digest = recovery_manifest.world_resource_catalog_checkpoint_sha256
    if catalog_digest is None:
        raise ValueError("post-restore resource validation requires a V2 recovery manifest")

    holder_digest = recovery_manifest.resource_holder_transition_checkpoint_sha256
    holder_history_coverage_baselines = ()
    if holder_digest is not None:
        if holder_transitions is None:
            raise ValueError("V3 post-restore validation requires restored holder transitions")
        if holder_transitions.semantic_minute != recovery_manifest.semantic_minute:
            raise ValueError("post-restore holder transition semantic minute mismatch")
        if resource_catalog_checkpoint_snapshot is None:
            raise ValueError("V3 post-restore validation requires selected resource catalog checkpoint")

        selected_catalog = restore_world_resource_catalog(
            resource_catalog_checkpoint_snapshot,
            recovery_semantic_minute=recovery_manifest.semantic_minute,
        )
        supplied_digest = resource_catalog_checkpoint_snapshot.get("sha256")
        if supplied_digest != catalog_digest:
            raise ValueError("post-restore resource catalog checkpoint digest does not match recovery manifest")
        if selected_catalog != resource_catalog:
            raise ValueError("post-restore resource catalog does not match selected checkpoint generation")

        holder_history_coverage_baselines = (
            issue_holder_history_coverage_baselines_from_catalog_checkpoint(
                resource_catalog_checkpoint_snapshot,
                expected_catalog_sha256=catalog_digest,
                recovery_semantic_minute=recovery_manifest.semantic_minute,
            )
        )
    else:
        if holder_transitions is not None:
            raise ValueError("legacy recovery manifest did not select holder transitions")
        if resource_catalog_checkpoint_snapshot is not None:
            raise ValueError("legacy recovery path does not consume holder-history baseline issuance")

    if complete_holder_history_resource_ids and holder_transitions is None:
        raise ValueError("complete holder history requires restored holder transitions")
    if complete_holder_history_resource_ids and holder_history_coverage_baselines:
        raise ValueError("cannot mix complete holder journal claims with checkpoint-derived bounded baselines")

    report = reconcile_world_resource_history(
        resource_catalog.resources,
        reservation_ledger=reservation_ledger,
        handoff_ledger=handoff_ledger,
        semantic_minute=recovery_manifest.semantic_minute,
        holder_transition_ledger=(holder_transitions.ledger if holder_transitions is not None else None),
        complete_holder_history_resource_ids=complete_holder_history_resource_ids,
        holder_history_coverage_baselines=holder_history_coverage_baselines,
    )
    if not report.safe_to_restore:
        reason_codes = ",".join(
            sorted({finding.reason_code for finding in report.conflicts})
        )
        raise ValueError(f"post-restore world resource conflict: {reason_codes}")

    return PersistentWorldPostRestoreValidation(
        semantic_minute=recovery_manifest.semantic_minute,
        resource_report=report,
    )
