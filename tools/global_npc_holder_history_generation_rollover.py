from __future__ import annotations

from typing import Mapping

from tools.global_npc_persistent_world_post_restore import PersistentWorldPostRestoreValidation
from tools.holder_history_coverage_baseline_checkpoint import (
    snapshot_holder_history_coverage_baselines,
)


def carry_forward_issued_holder_history_baselines(
    validation: PersistentWorldPostRestoreValidation,
    *,
    checkpoint_semantic_minute: int,
) -> Mapping[str, object]:
    """Persist safe post-restore holder certificates for a later recovery generation.

    A successful recovery at semantic minute T may issue a fresh baseline from the exact
    WorldResource catalog generation that was selected and reconciled at T. This helper
    carries those certificates into a holder-history baseline owner checkpoint at T+N.

    The checkpoint does not certify holder state at T+N. Every contained baseline keeps
    its original ``at_tick == T`` and must still be replayed through all later holder
    transitions before it can prove a catalog recovered at T+N.
    """
    if not validation.safe_to_activate:
        raise ValueError("cannot carry holder history baselines from unsafe post-restore validation")
    if not validation.issued_holder_history_coverage_baselines:
        raise ValueError("post-restore validation issued no holder history coverage baselines")
    if (
        isinstance(checkpoint_semantic_minute, bool)
        or not isinstance(checkpoint_semantic_minute, int)
        or checkpoint_semantic_minute < validation.semantic_minute
    ):
        raise ValueError(
            "checkpoint_semantic_minute must be an integer at or after the validated recovery cut"
        )

    for baseline in validation.issued_holder_history_coverage_baselines:
        if baseline.at_tick != validation.semantic_minute:
            raise ValueError("issued holder history baseline must begin at the validated recovery cut")

    return snapshot_holder_history_coverage_baselines(
        validation.issued_holder_history_coverage_baselines,
        semantic_minute=checkpoint_semantic_minute,
    )
