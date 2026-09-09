from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_delivery_replan_provenance import (
    DeliveryReplanProvenanceLedger,
    PROVENANCE_SCHEMA,
)
from tools.global_npc_world_resource_allocation_notice_checkpoint import (
    WORLD_RESOURCE_ALLOCATION_NOTICE_CHECKPOINT_SCHEMA,
    RestoredWorldResourceAllocationNoticeCheckpoint,
    build_world_resource_allocation_notice_checkpoint,
    restore_world_resource_allocation_notice_checkpoint,
)


WORLD_DELIVERY_REPLAN_PROVENANCE_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V15"


@dataclass(frozen=True)
class RestoredWorldDeliveryReplanProvenanceCheckpoint:
    world_resource_allocation_notice: RestoredWorldResourceAllocationNoticeCheckpoint
    delivery_replan_provenance: DeliveryReplanProvenanceLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _redigest(payload: Mapping[str, object]) -> dict:
    row = {str(key): value for key, value in payload.items() if key != "sha256"}
    return row | {"sha256": _digest_payload(row)}


def build_world_delivery_replan_provenance_checkpoint(
    coordinator,
    *,
    semantic_minute: int,
    delivery_replan_provenance: DeliveryReplanProvenanceLedger,
    **v14_kwargs,
) -> dict:
    """Build one coherent checkpoint through delivery-to-replan provenance.

    V15 keeps the append-only materialization and consumed-trigger history in the
    same digest as the V14 world state it validates against. It does not infer
    acknowledgement, plan selection, execution or tactical ownership.
    """
    delivery_replan_provenance.validate_against(
        coordinator,
        semantic_minute=semantic_minute,
    )
    base = build_world_resource_allocation_notice_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        **v14_kwargs,
    )
    payload = {str(key): value for key, value in base.items() if key != "sha256"}
    if payload.get("schema") != WORLD_RESOURCE_ALLOCATION_NOTICE_CHECKPOINT_SCHEMA:
        raise ValueError("unexpected V14 world checkpoint schema")
    payload["schema"] = WORLD_DELIVERY_REPLAN_PROVENANCE_CHECKPOINT_SCHEMA
    payload["delivery_replan_provenance"] = delivery_replan_provenance.snapshot()
    return payload | {"sha256": _digest_payload(payload)}


def _world_coordinator(restored: RestoredWorldResourceAllocationNoticeCheckpoint):
    return (
        restored.world_resource_allocation_application
        .world_resource_allocation
        .world_resource_admission
        .world_resource
        .world
        .coordinator
    )


def restore_world_delivery_replan_provenance_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldDeliveryReplanProvenanceCheckpoint:
    """Restore V15, or migrate V14 and earlier with empty new provenance.

    Migration never reconstructs materialization or trigger-consumption history
    from delivered IDs, knowledge contents, completed-trigger IDs or later plans.
    """
    schema = snapshot.get("schema")
    if schema != WORLD_DELIVERY_REPLAN_PROVENANCE_CHECKPOINT_SCHEMA:
        restored = restore_world_resource_allocation_notice_checkpoint(
            snapshot,
            channels=channels,
            agendas=agendas,
        )
        return RestoredWorldDeliveryReplanProvenanceCheckpoint(
            world_resource_allocation_notice=restored,
            delivery_replan_provenance=DeliveryReplanProvenanceLedger(),
        )

    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world delivery/replan provenance checkpoint digest mismatch")

    raw_provenance = payload.get("delivery_replan_provenance")
    if not isinstance(raw_provenance, Mapping):
        raise ValueError("delivery_replan_provenance checkpoint is required")
    if raw_provenance.get("schema") != PROVENANCE_SCHEMA:
        raise ValueError("V15 world checkpoint requires delivery/replan provenance V1")
    provenance = DeliveryReplanProvenanceLedger.restore(raw_provenance)

    v14_payload = dict(payload)
    v14_payload.pop("delivery_replan_provenance", None)
    v14_payload["schema"] = WORLD_RESOURCE_ALLOCATION_NOTICE_CHECKPOINT_SCHEMA
    restored = restore_world_resource_allocation_notice_checkpoint(
        _redigest(v14_payload),
        channels=channels,
        agendas=agendas,
    )
    coordinator = _world_coordinator(restored)
    semantic_minute = int(payload["semantic_minute"])
    provenance.validate_against(coordinator, semantic_minute=semantic_minute)

    return RestoredWorldDeliveryReplanProvenanceCheckpoint(
        world_resource_allocation_notice=restored,
        delivery_replan_provenance=provenance,
    )
