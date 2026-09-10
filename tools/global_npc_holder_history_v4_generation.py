from __future__ import annotations

from typing import Mapping

from tools.global_npc_persistent_world_post_restore import (
    PersistentWorldPostRestoreValidation,
    validate_persistent_world_post_restore,
)
from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_reservations import ReservationLedger
from tools.persistent_world_recovery_manifest import reconcile_persistent_world_recovery_manifest
from tools.resource_holder_transition_checkpoint import restore_resource_holder_transitions
from tools.world_resource_catalog_checkpoint import restore_world_resource_catalog


def validate_exact_v4_holder_history_generation(
    recovery_manifest_snapshot: Mapping[str, object],
    *,
    global_npc_checkpoint: Mapping[str, object],
    persistent_world_evidence_checkpoint: Mapping[str, object],
    world_resource_catalog_checkpoint: Mapping[str, object],
    resource_holder_transition_checkpoint: Mapping[str, object],
    holder_history_coverage_baseline_checkpoint: Mapping[str, object],
    reservation_ledger: ReservationLedger,
    handoff_ledger: ResourceHandoffLedger,
) -> PersistentWorldPostRestoreValidation:
    """Validate one exact V4 owner generation before issuing future holder evidence.

    This coordinator keeps generation selection, owner restore and post-restore holder
    reconciliation in one fail-closed path. The outer manifest first proves which five
    checkpoint digests belong together. Only that selected catalog, holder-transition
    journal and baseline owner are then admitted to bounded holder-history replay.

    A successful result may contain fresh same-cut holder baselines for a later recovery
    generation. Those certificates cannot validate the catalog that produced them.
    """
    reconciled_manifest = reconcile_persistent_world_recovery_manifest(
        recovery_manifest_snapshot,
        global_npc_checkpoint=global_npc_checkpoint,
        persistent_world_evidence_checkpoint=persistent_world_evidence_checkpoint,
        world_resource_catalog_checkpoint=world_resource_catalog_checkpoint,
        resource_holder_transition_checkpoint=resource_holder_transition_checkpoint,
        holder_history_coverage_baseline_checkpoint=holder_history_coverage_baseline_checkpoint,
    )
    if reconciled_manifest.holder_history_coverage_baseline_checkpoint_sha256 is None:
        raise ValueError("exact holder history generation validation requires a V4 recovery manifest")

    semantic_minute = reconciled_manifest.semantic_minute
    restored_catalog = restore_world_resource_catalog(
        world_resource_catalog_checkpoint,
        recovery_semantic_minute=semantic_minute,
    )
    restored_holder_transitions = restore_resource_holder_transitions(
        resource_holder_transition_checkpoint,
        recovery_semantic_minute=semantic_minute,
    )

    return validate_persistent_world_post_restore(
        reconciled_manifest,
        restored_catalog,
        reservation_ledger=reservation_ledger,
        handoff_ledger=handoff_ledger,
        holder_transitions=restored_holder_transitions,
        resource_catalog_checkpoint_snapshot=world_resource_catalog_checkpoint,
        holder_history_coverage_baseline_checkpoint_snapshot=holder_history_coverage_baseline_checkpoint,
    )
