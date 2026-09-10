from __future__ import annotations

from dataclasses import dataclass

from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_reservations import ReservationLedger
from tools.persistent_world_recovery_manifest import ReconciledPersistentWorldRecoveryManifest
from tools.resource_holder_transition_checkpoint import RestoredResourceHolderTransitions
from tools.world_resource_catalog_checkpoint import RestoredWorldResourceCatalog
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
    complete_holder_history_resource_ids: frozenset[str] = frozenset(),
) -> PersistentWorldPostRestoreValidation:
    """Run cross-owner checks after coherent checkpoint selection and owner restore.

    The recovery manifest has already selected one generation. The resource catalog and
    historical ledgers have already restored under their own owners. V3 additionally
    selects a holder-transition checkpoint; when present, this stage requires the
    corresponding restored owner before it can use holder evidence.

    Explicit conflicts fail closed. Indeterminate findings remain visible and do not
    authorize rewriting catalog state or inventing missing resource history. Holder
    history becomes conflict-grade evidence only for resource ids whose mutation paths
    the caller has explicitly audited as complete.
    """
    if resource_catalog.semantic_minute != recovery_manifest.semantic_minute:
        raise ValueError("post-restore resource catalog semantic minute mismatch")
    if recovery_manifest.world_resource_catalog_checkpoint_sha256 is None:
        raise ValueError("post-restore resource validation requires a V2 recovery manifest")

    holder_digest = recovery_manifest.resource_holder_transition_checkpoint_sha256
    if holder_digest is not None:
        if holder_transitions is None:
            raise ValueError("V3 post-restore validation requires restored holder transitions")
        if holder_transitions.semantic_minute != recovery_manifest.semantic_minute:
            raise ValueError("post-restore holder transition semantic minute mismatch")
    elif holder_transitions is not None:
        raise ValueError("legacy recovery manifest did not select holder transitions")
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

    return PersistentWorldPostRestoreValidation(
        semantic_minute=recovery_manifest.semantic_minute,
        resource_report=report,
    )
