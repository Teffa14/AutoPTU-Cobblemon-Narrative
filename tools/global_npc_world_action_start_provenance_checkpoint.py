from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_action_start_provenance import (
    ACTION_START_SCHEMA,
    ActionStartProvenanceLedger,
)
from tools.global_npc_world_plan_selection_provenance_checkpoint import (
    WORLD_PLAN_SELECTION_PROVENANCE_CHECKPOINT_SCHEMA,
    RestoredWorldPlanSelectionProvenanceCheckpoint,
    build_world_plan_selection_provenance_checkpoint,
    restore_world_plan_selection_provenance_checkpoint,
)


WORLD_ACTION_START_PROVENANCE_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V17"


@dataclass(frozen=True)
class RestoredWorldActionStartProvenanceCheckpoint:
    world_plan_selection_provenance: RestoredWorldPlanSelectionProvenanceCheckpoint
    action_start_provenance: ActionStartProvenanceLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _redigest(payload: Mapping[str, object]) -> dict:
    row = {str(key): value for key, value in payload.items() if key != "sha256"}
    return row | {"sha256": _digest_payload(row)}


def build_world_action_start_provenance_checkpoint(
    coordinator,
    *,
    semantic_minute: int,
    delivery_replan_provenance,
    plan_selection_provenance,
    action_start_provenance: ActionStartProvenanceLedger,
    **v16_kwargs,
) -> dict:
    """Build one coherent checkpoint through replayable action start.

    V17 places action-start provenance under the same digest as the V16
    delivery/materialization/replan/plan-selection history that each start
    depends on. It does not infer action completion, AutoPTU resolution,
    Minecraft playback or success from a proven start transition.
    """
    action_start_provenance.validate_against_plan_selections(
        plan_selection_provenance,
        semantic_minute=semantic_minute,
    )
    base = build_world_plan_selection_provenance_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        delivery_replan_provenance=delivery_replan_provenance,
        plan_selection_provenance=plan_selection_provenance,
        **v16_kwargs,
    )
    payload = {str(key): value for key, value in base.items() if key != "sha256"}
    if payload.get("schema") != WORLD_PLAN_SELECTION_PROVENANCE_CHECKPOINT_SCHEMA:
        raise ValueError("unexpected V16 world checkpoint schema")
    payload["schema"] = WORLD_ACTION_START_PROVENANCE_CHECKPOINT_SCHEMA
    payload["action_start_provenance"] = action_start_provenance.snapshot()
    return payload | {"sha256": _digest_payload(payload)}


def restore_world_action_start_provenance_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldActionStartProvenanceCheckpoint:
    """Restore V17, or migrate V16 and earlier with empty start provenance.

    Migration never reconstructs a historical start from current location,
    active travel, current AutoPTU binding, encounter state or later outcomes.
    """
    schema = snapshot.get("schema")
    if schema != WORLD_ACTION_START_PROVENANCE_CHECKPOINT_SCHEMA:
        restored = restore_world_plan_selection_provenance_checkpoint(
            snapshot,
            channels=channels,
            agendas=agendas,
        )
        return RestoredWorldActionStartProvenanceCheckpoint(
            world_plan_selection_provenance=restored,
            action_start_provenance=ActionStartProvenanceLedger(),
        )

    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world action-start provenance checkpoint digest mismatch")

    raw_action_start = payload.get("action_start_provenance")
    if not isinstance(raw_action_start, Mapping):
        raise ValueError("action_start_provenance checkpoint is required")
    if raw_action_start.get("schema") != ACTION_START_SCHEMA:
        raise ValueError("V17 world checkpoint requires action-start provenance V1")
    action_start_provenance = ActionStartProvenanceLedger.restore(raw_action_start)

    v16_payload = dict(payload)
    v16_payload.pop("action_start_provenance", None)
    v16_payload["schema"] = WORLD_PLAN_SELECTION_PROVENANCE_CHECKPOINT_SCHEMA
    restored = restore_world_plan_selection_provenance_checkpoint(
        _redigest(v16_payload),
        channels=channels,
        agendas=agendas,
    )
    semantic_minute = int(payload["semantic_minute"])
    action_start_provenance.validate_against_plan_selections(
        restored.plan_selection_provenance,
        semantic_minute=semantic_minute,
    )

    return RestoredWorldActionStartProvenanceCheckpoint(
        world_plan_selection_provenance=restored,
        action_start_provenance=action_start_provenance,
    )
