from __future__ import annotations

import hashlib
from typing import Mapping

from tools.global_npc_holder_history_coverage import HolderHistoryCoverageBaseline
from tools.world_resource_catalog_checkpoint import (
    WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
    restore_world_resource_catalog,
)


def _baseline_id(*, catalog_sha256: str, resource_id: str, semantic_minute: int) -> str:
    material = f"{WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA}|{catalog_sha256}|{semantic_minute}|{resource_id}"
    return "holder-baseline-" + hashlib.sha256(material.encode("utf-8")).hexdigest()


def issue_holder_history_coverage_baselines_from_catalog_checkpoint(
    snapshot: Mapping[str, object],
    *,
    expected_catalog_sha256: str | None = None,
    recovery_semantic_minute: int | None = None,
) -> tuple[HolderHistoryCoverageBaseline, ...]:
    """Issue deterministic bounded holder-history baselines from one validated catalog generation.

    The catalog checkpoint remains the authority for current operational resource state at its
    semantic cut. This function only derives baseline certificates that bind each resource holder
    to that exact checkpoint digest. It does not claim completeness before the checkpoint.
    """
    supplied_digest = snapshot.get("sha256")
    if not isinstance(supplied_digest, str) or not supplied_digest.strip():
        raise ValueError("world resource catalog checkpoint sha256 is required")
    supplied_digest = supplied_digest.strip()

    if expected_catalog_sha256 is not None:
        if not isinstance(expected_catalog_sha256, str) or not expected_catalog_sha256.strip():
            raise ValueError("expected_catalog_sha256 must be a non-empty string when present")
        if supplied_digest != expected_catalog_sha256.strip():
            raise ValueError("world resource catalog checkpoint digest does not match expected generation")

    restored = restore_world_resource_catalog(
        snapshot,
        recovery_semantic_minute=recovery_semantic_minute,
    )
    source_ref = f"{WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA}:{supplied_digest}"

    return tuple(
        HolderHistoryCoverageBaseline(
            baseline_id=_baseline_id(
                catalog_sha256=supplied_digest,
                resource_id=resource.resource_id,
                semantic_minute=restored.semantic_minute,
            ),
            resource_id=resource.resource_id,
            at_tick=restored.semantic_minute,
            holder_actor_id=resource.holder_actor_id,
            source_ref=source_ref,
        )
        for resource in restored.resources
    )
