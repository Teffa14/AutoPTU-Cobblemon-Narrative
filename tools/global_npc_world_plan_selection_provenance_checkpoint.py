from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_plan_selection_provenance import (
    PLAN_SELECTION_SCHEMA,
    PlanSelectionProvenanceLedger,
)
from tools.global_npc_world_delivery_replan_provenance_checkpoint import (
    WORLD_DELIVERY_REPLAN_PROVENANCE_CHECKPOINT_SCHEMA,
    RestoredWorldDeliveryReplanProvenanceCheckpoint,
    build_world_delivery_replan_provenance_checkpoint,
    restore_world_delivery_replan_provenance_checkpoint,
)


WORLD_PLAN_SELECTION_PROVENANCE_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V16"


@dataclass(frozen=True)
class RestoredWorldPlanSelectionProvenanceCheckpoint:
    world_delivery_replan_provenance: RestoredWorldDeliveryReplanProvenanceCheckpoint
    plan_selection_provenance: PlanSelectionProvenanceLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _redigest(payload: Mapping[str, object]) -> dict:
    row = {str(key): value for key, value in payload.items() if key != "sha256"}
    return row | {"sha256": _digest_payload(row)}


def build_world_plan_selection_provenance_checkpoint(
    coordinator,
    *,
    semantic_minute: int,
    delivery_replan_provenance,
    plan_selection_provenance: PlanSelectionProvenanceLedger,
    **v15_kwargs,
) -> dict:
    """Build one coherent checkpoint through replayable plan selection.

    V16 places plan-selection provenance under the same digest as the V15
    delivery/materialization/replan history that each selection depends on.
    It does not infer acknowledgement, action start, AutoPTU ownership or
    successful completion from a selected agenda decision.
    """
    plan_selection_provenance.validate_against_replan_provenance(
        delivery_replan_provenance,
        semantic_minute=semantic_minute,
    )
    base = build_world_delivery_replan_provenance_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        delivery_replan_provenance=delivery_replan_provenance,
        **v15_kwargs,
    )
    payload = {str(key): value for key, value in base.items() if key != "sha256"}
    if payload.get("schema") != WORLD_DELIVERY_REPLAN_PROVENANCE_CHECKPOINT_SCHEMA:
        raise ValueError("unexpected V15 world checkpoint schema")
    payload["schema"] = WORLD_PLAN_SELECTION_PROVENANCE_CHECKPOINT_SCHEMA
    payload["plan_selection_provenance"] = plan_selection_provenance.snapshot()
    return payload | {"sha256": _digest_payload(payload)}


def restore_world_plan_selection_provenance_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldPlanSelectionProvenanceCheckpoint:
    """Restore V16, or migrate V15 and earlier with empty plan provenance.

    Migration never reconstructs a historical selection from the current
    agenda, current location, active intent, completed triggers or later acts.
    """
    schema = snapshot.get("schema")
    if schema != WORLD_PLAN_SELECTION_PROVENANCE_CHECKPOINT_SCHEMA:
        restored = restore_world_delivery_replan_provenance_checkpoint(
            snapshot,
            channels=channels,
            agendas=agendas,
        )
        return RestoredWorldPlanSelectionProvenanceCheckpoint(
            world_delivery_replan_provenance=restored,
            plan_selection_provenance=PlanSelectionProvenanceLedger(),
        )

    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world plan-selection provenance checkpoint digest mismatch")

    raw_plan = payload.get("plan_selection_provenance")
    if not isinstance(raw_plan, Mapping):
        raise ValueError("plan_selection_provenance checkpoint is required")
    if raw_plan.get("schema") != PLAN_SELECTION_SCHEMA:
        raise ValueError("V16 world checkpoint requires plan-selection provenance V1")
    plan_provenance = PlanSelectionProvenanceLedger.restore(raw_plan)

    v15_payload = dict(payload)
    v15_payload.pop("plan_selection_provenance", None)
    v15_payload["schema"] = WORLD_DELIVERY_REPLAN_PROVENANCE_CHECKPOINT_SCHEMA
    restored = restore_world_delivery_replan_provenance_checkpoint(
        _redigest(v15_payload),
        channels=channels,
        agendas=agendas,
    )
    semantic_minute = int(payload["semantic_minute"])
    plan_provenance.validate_against_replan_provenance(
        restored.delivery_replan_provenance,
        semantic_minute=semantic_minute,
    )

    return RestoredWorldPlanSelectionProvenanceCheckpoint(
        world_delivery_replan_provenance=restored,
        plan_selection_provenance=plan_provenance,
    )
