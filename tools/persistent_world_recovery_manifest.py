from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_world_action_interruption_provenance_checkpoint import (
    WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
)
from tools.holder_history_coverage_baseline_checkpoint import (
    HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_SCHEMA,
)
from tools.persistent_world_evidence_checkpoint import (
    PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
)
from tools.resource_holder_transition_checkpoint import (
    RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA,
)
from tools.world_resource_catalog_checkpoint import (
    WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
)


PERSISTENT_WORLD_RECOVERY_MANIFEST_V1_SCHEMA = "OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V1"
PERSISTENT_WORLD_RECOVERY_MANIFEST_V2_SCHEMA = "OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V2"
PERSISTENT_WORLD_RECOVERY_MANIFEST_V3_SCHEMA = "OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V3"
PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA = "OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V4"


@dataclass(frozen=True)
class ReconciledPersistentWorldRecoveryManifest:
    semantic_minute: int
    global_npc_checkpoint_sha256: str
    persistent_world_evidence_checkpoint_sha256: str
    world_resource_catalog_checkpoint_sha256: str | None
    resource_holder_transition_checkpoint_sha256: str | None = None
    holder_history_coverage_baseline_checkpoint_sha256: str | None = None


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _verified_checkpoint_identity(
    snapshot: Mapping[str, object],
    *,
    expected_schema: str,
    label: str,
) -> tuple[int, str]:
    if snapshot.get("schema") != expected_schema:
        raise ValueError(f"{label} checkpoint requires schema {expected_schema}")

    supplied_digest = snapshot.get("sha256")
    if not isinstance(supplied_digest, str) or not supplied_digest:
        raise ValueError(f"{label} checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest(payload) != supplied_digest:
        raise ValueError(f"{label} checkpoint digest mismatch")

    raw_minute = payload.get("semantic_minute")
    if not isinstance(raw_minute, int) or isinstance(raw_minute, bool) or raw_minute < 0:
        raise ValueError(f"{label} checkpoint semantic_minute must be a non-negative integer")
    return raw_minute, supplied_digest


def build_persistent_world_recovery_manifest(
    *,
    global_npc_checkpoint: Mapping[str, object],
    persistent_world_evidence_checkpoint: Mapping[str, object],
    world_resource_catalog_checkpoint: Mapping[str, object],
    resource_holder_transition_checkpoint: Mapping[str, object],
    holder_history_coverage_baseline_checkpoint: Mapping[str, object],
) -> dict:
    """Bind one coherent generation across the current persistent-world recovery owners.

    V4 adds the independently recoverable holder-history coverage baseline owner to generation
    selection. The manifest owns selection only: every owner still performs its own restore-time
    semantic checks. A selected baseline generation remains future-facing evidence from its own cut;
    selection does not let that baseline validate or complete history before that cut.
    """
    global_minute, global_digest = _verified_checkpoint_identity(
        global_npc_checkpoint,
        expected_schema=WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
        label="global NPC",
    )
    evidence_minute, evidence_digest = _verified_checkpoint_identity(
        persistent_world_evidence_checkpoint,
        expected_schema=PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
        label="persistent world evidence",
    )
    resource_minute, resource_digest = _verified_checkpoint_identity(
        world_resource_catalog_checkpoint,
        expected_schema=WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
        label="world resource catalog",
    )
    holder_minute, holder_digest = _verified_checkpoint_identity(
        resource_holder_transition_checkpoint,
        expected_schema=RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA,
        label="resource holder transition",
    )
    baseline_minute, baseline_digest = _verified_checkpoint_identity(
        holder_history_coverage_baseline_checkpoint,
        expected_schema=HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_SCHEMA,
        label="holder history coverage baseline",
    )
    if len({global_minute, evidence_minute, resource_minute, holder_minute, baseline_minute}) != 1:
        raise ValueError("recovery manifest requires checkpoints from the same semantic minute")

    payload = {
        "schema": PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA,
        "semantic_minute": global_minute,
        "global_npc_checkpoint_sha256": global_digest,
        "persistent_world_evidence_checkpoint_sha256": evidence_digest,
        "world_resource_catalog_checkpoint_sha256": resource_digest,
        "resource_holder_transition_checkpoint_sha256": holder_digest,
        "holder_history_coverage_baseline_checkpoint_sha256": baseline_digest,
    }
    return payload | {"sha256": _digest(payload)}


def reconcile_persistent_world_recovery_manifest(
    snapshot: Mapping[str, object],
    *,
    global_npc_checkpoint: Mapping[str, object],
    persistent_world_evidence_checkpoint: Mapping[str, object],
    world_resource_catalog_checkpoint: Mapping[str, object] | None = None,
    resource_holder_transition_checkpoint: Mapping[str, object] | None = None,
    holder_history_coverage_baseline_checkpoint: Mapping[str, object] | None = None,
) -> ReconciledPersistentWorldRecoveryManifest:
    """Verify candidate checkpoints against exactly one selected recovery generation.

    V1 remains readable for legacy two-owner recovery. V2 remains readable for legacy three-owner
    recovery. V3 remains readable for legacy four-owner recovery. None fabricates newer owners.
    V4 requires all five current owners.
    """
    schema = snapshot.get("schema")
    supported = {
        PERSISTENT_WORLD_RECOVERY_MANIFEST_V1_SCHEMA,
        PERSISTENT_WORLD_RECOVERY_MANIFEST_V2_SCHEMA,
        PERSISTENT_WORLD_RECOVERY_MANIFEST_V3_SCHEMA,
        PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA,
    }
    if schema not in supported:
        raise ValueError("unsupported persistent world recovery manifest schema")

    supplied_digest = snapshot.get("sha256")
    if not isinstance(supplied_digest, str) or not supplied_digest:
        raise ValueError("persistent world recovery manifest sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest(payload) != supplied_digest:
        raise ValueError("persistent world recovery manifest digest mismatch")

    raw_minute = payload.get("semantic_minute")
    if not isinstance(raw_minute, int) or isinstance(raw_minute, bool) or raw_minute < 0:
        raise ValueError("persistent world recovery manifest semantic_minute must be a non-negative integer")

    global_minute, global_digest = _verified_checkpoint_identity(
        global_npc_checkpoint,
        expected_schema=WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
        label="global NPC",
    )
    evidence_minute, evidence_digest = _verified_checkpoint_identity(
        persistent_world_evidence_checkpoint,
        expected_schema=PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
        label="persistent world evidence",
    )
    if global_minute != raw_minute or evidence_minute != raw_minute:
        raise ValueError("recovery manifest candidate checkpoint semantic minute mismatch")
    if payload.get("global_npc_checkpoint_sha256") != global_digest:
        raise ValueError("recovery manifest global NPC checkpoint digest mismatch")
    if payload.get("persistent_world_evidence_checkpoint_sha256") != evidence_digest:
        raise ValueError("recovery manifest persistent world evidence checkpoint digest mismatch")

    if schema == PERSISTENT_WORLD_RECOVERY_MANIFEST_V1_SCHEMA:
        if holder_history_coverage_baseline_checkpoint is not None:
            raise ValueError("legacy recovery manifest did not select holder history coverage baseline")
        return ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=raw_minute,
            global_npc_checkpoint_sha256=global_digest,
            persistent_world_evidence_checkpoint_sha256=evidence_digest,
            world_resource_catalog_checkpoint_sha256=None,
        )

    if world_resource_catalog_checkpoint is None:
        raise ValueError("V2/V3/V4 recovery manifest requires world resource catalog checkpoint")
    resource_minute, resource_digest = _verified_checkpoint_identity(
        world_resource_catalog_checkpoint,
        expected_schema=WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
        label="world resource catalog",
    )
    if resource_minute != raw_minute:
        raise ValueError("recovery manifest candidate checkpoint semantic minute mismatch")
    if payload.get("world_resource_catalog_checkpoint_sha256") != resource_digest:
        raise ValueError("recovery manifest world resource catalog checkpoint digest mismatch")

    if schema == PERSISTENT_WORLD_RECOVERY_MANIFEST_V2_SCHEMA:
        if holder_history_coverage_baseline_checkpoint is not None:
            raise ValueError("legacy recovery manifest did not select holder history coverage baseline")
        return ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=raw_minute,
            global_npc_checkpoint_sha256=global_digest,
            persistent_world_evidence_checkpoint_sha256=evidence_digest,
            world_resource_catalog_checkpoint_sha256=resource_digest,
        )

    if resource_holder_transition_checkpoint is None:
        raise ValueError("V3/V4 recovery manifest requires resource holder transition checkpoint")
    holder_minute, holder_digest = _verified_checkpoint_identity(
        resource_holder_transition_checkpoint,
        expected_schema=RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA,
        label="resource holder transition",
    )
    if holder_minute != raw_minute:
        raise ValueError("recovery manifest candidate checkpoint semantic minute mismatch")
    if payload.get("resource_holder_transition_checkpoint_sha256") != holder_digest:
        raise ValueError("recovery manifest resource holder transition checkpoint digest mismatch")

    if schema == PERSISTENT_WORLD_RECOVERY_MANIFEST_V3_SCHEMA:
        if holder_history_coverage_baseline_checkpoint is not None:
            raise ValueError("V3 recovery manifest did not select holder history coverage baseline")
        return ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=raw_minute,
            global_npc_checkpoint_sha256=global_digest,
            persistent_world_evidence_checkpoint_sha256=evidence_digest,
            world_resource_catalog_checkpoint_sha256=resource_digest,
            resource_holder_transition_checkpoint_sha256=holder_digest,
        )

    if holder_history_coverage_baseline_checkpoint is None:
        raise ValueError("V4 recovery manifest requires holder history coverage baseline checkpoint")
    baseline_minute, baseline_digest = _verified_checkpoint_identity(
        holder_history_coverage_baseline_checkpoint,
        expected_schema=HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_SCHEMA,
        label="holder history coverage baseline",
    )
    if baseline_minute != raw_minute:
        raise ValueError("recovery manifest candidate checkpoint semantic minute mismatch")
    if payload.get("holder_history_coverage_baseline_checkpoint_sha256") != baseline_digest:
        raise ValueError("recovery manifest holder history coverage baseline checkpoint digest mismatch")

    return ReconciledPersistentWorldRecoveryManifest(
        semantic_minute=raw_minute,
        global_npc_checkpoint_sha256=global_digest,
        persistent_world_evidence_checkpoint_sha256=evidence_digest,
        world_resource_catalog_checkpoint_sha256=resource_digest,
        resource_holder_transition_checkpoint_sha256=holder_digest,
        holder_history_coverage_baseline_checkpoint_sha256=baseline_digest,
    )
