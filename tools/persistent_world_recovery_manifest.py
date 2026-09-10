from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_world_action_interruption_provenance_checkpoint import (
    WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
)
from tools.persistent_world_evidence_checkpoint import (
    PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
)
from tools.world_resource_catalog_checkpoint import (
    WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
)


PERSISTENT_WORLD_RECOVERY_MANIFEST_V1_SCHEMA = "OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V1"
PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA = "OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V2"


@dataclass(frozen=True)
class ReconciledPersistentWorldRecoveryManifest:
    semantic_minute: int
    global_npc_checkpoint_sha256: str
    persistent_world_evidence_checkpoint_sha256: str
    world_resource_catalog_checkpoint_sha256: str | None


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
) -> dict:
    """Bind one coherent generation across the current persistent-world recovery owners.

    The manifest owns generation selection only. It stores owner digests and one semantic minute, not
    copies of owner payloads. Each owner must still run its own restore-time semantic validation.
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
    if len({global_minute, evidence_minute, resource_minute}) != 1:
        raise ValueError("recovery manifest requires checkpoints from the same semantic minute")

    payload = {
        "schema": PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA,
        "semantic_minute": global_minute,
        "global_npc_checkpoint_sha256": global_digest,
        "persistent_world_evidence_checkpoint_sha256": evidence_digest,
        "world_resource_catalog_checkpoint_sha256": resource_digest,
    }
    return payload | {"sha256": _digest(payload)}


def reconcile_persistent_world_recovery_manifest(
    snapshot: Mapping[str, object],
    *,
    global_npc_checkpoint: Mapping[str, object],
    persistent_world_evidence_checkpoint: Mapping[str, object],
    world_resource_catalog_checkpoint: Mapping[str, object] | None = None,
) -> ReconciledPersistentWorldRecoveryManifest:
    """Verify that candidate owner checkpoints exactly match the selected recovery generation.

    V1 manifests remain readable for legacy two-owner recovery. V2 requires the resource catalog
    checkpoint as a third owner at the same semantic minute. Domain-specific owner restores still run
    after this selection step.
    """
    schema = snapshot.get("schema")
    if schema not in {PERSISTENT_WORLD_RECOVERY_MANIFEST_V1_SCHEMA, PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA}:
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
        return ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=raw_minute,
            global_npc_checkpoint_sha256=global_digest,
            persistent_world_evidence_checkpoint_sha256=evidence_digest,
            world_resource_catalog_checkpoint_sha256=None,
        )

    if world_resource_catalog_checkpoint is None:
        raise ValueError("V2 recovery manifest requires world resource catalog checkpoint")
    resource_minute, resource_digest = _verified_checkpoint_identity(
        world_resource_catalog_checkpoint,
        expected_schema=WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
        label="world resource catalog",
    )
    if resource_minute != raw_minute:
        raise ValueError("recovery manifest candidate checkpoint semantic minute mismatch")
    if payload.get("world_resource_catalog_checkpoint_sha256") != resource_digest:
        raise ValueError("recovery manifest world resource catalog checkpoint digest mismatch")

    return ReconciledPersistentWorldRecoveryManifest(
        semantic_minute=raw_minute,
        global_npc_checkpoint_sha256=global_digest,
        persistent_world_evidence_checkpoint_sha256=evidence_digest,
        world_resource_catalog_checkpoint_sha256=resource_digest,
    )
