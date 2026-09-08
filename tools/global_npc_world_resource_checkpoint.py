from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_resource_checkpoint import (
    restore_resource_state,
    restore_resource_state_with_handoffs,
    snapshot_resource_state,
    snapshot_resource_state_with_handoffs,
    validate_handoff_checkpoint_time,
    validate_resource_checkpoint_time,
)
from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_requests import ResourceRequestLedger
from tools.global_npc_resource_reservations import ReservationLedger
from tools.global_npc_world_checkpoint import (
    CHECKPOINT_SCHEMA as BASE_WORLD_CHECKPOINT_SCHEMA,
    RestoredWorldCheckpoint,
    build_checkpoint,
    restore_checkpoint,
)


LEGACY_WORLD_RESOURCE_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V6"
WORLD_RESOURCE_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V7"


@dataclass(frozen=True)
class RestoredWorldResourceCheckpoint:
    world: RestoredWorldCheckpoint
    reservation_ledger: ReservationLedger
    request_ledger: ResourceRequestLedger
    handoff_ledger: ResourceHandoffLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _redigest(payload: Mapping[str, object]) -> dict:
    row = {str(key): value for key, value in payload.items() if key != "sha256"}
    return row | {"sha256": _digest_payload(row)}


def build_world_resource_checkpoint(
    coordinator,
    *,
    semantic_minute: int,
    reservation_ledger: ReservationLedger,
    request_ledger: ResourceRequestLedger,
    handoff_ledger: ResourceHandoffLedger | None = None,
    **world_checkpoint_kwargs,
) -> dict:
    """Build the coherent world checkpoint containing Pass 339/342/343 history.

    The underlying world checkpoint remains owner of world-agent state. This
    adapter advances the serialized schema to V7 and embeds the validated Pass
    355 V2 resource bundle without replaying any resource operation.
    """
    base = build_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        **world_checkpoint_kwargs,
    )
    payload = {str(key): value for key, value in base.items() if key != "sha256"}
    if payload.get("schema") != BASE_WORLD_CHECKPOINT_SCHEMA:
        raise ValueError("unexpected base world checkpoint schema")
    payload["schema"] = WORLD_RESOURCE_CHECKPOINT_SCHEMA
    payload["resource_state"] = snapshot_resource_state_with_handoffs(
        reservation_ledger,
        request_ledger,
        handoff_ledger or ResourceHandoffLedger(),
    )
    return payload | {"sha256": _digest_payload(payload)}


def _restore_embedded_world(payload: Mapping[str, object], *, channels, agendas=None) -> RestoredWorldCheckpoint:
    base_payload = {str(key): value for key, value in payload.items() if key != "resource_state"}
    base_payload["schema"] = BASE_WORLD_CHECKPOINT_SCHEMA
    return restore_checkpoint(_redigest(base_payload), channels=channels, agendas=agendas)


def _validate_global_digest(snapshot: Mapping[str, object]) -> dict:
    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world checkpoint digest mismatch")
    return payload


def restore_world_resource_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldResourceCheckpoint:
    """Restore V7, V6 or older world checkpoints without inventing history.

    V7 restores the Pass 355 handoff bundle. V6 restores its original V1
    resource payload and an explicitly empty handoff ledger. Older world-only
    checkpoints restore all resource ledgers empty because that history was not
    serialized by those schemas.
    """
    schema = snapshot.get("schema")
    if schema not in {WORLD_RESOURCE_CHECKPOINT_SCHEMA, LEGACY_WORLD_RESOURCE_CHECKPOINT_SCHEMA}:
        world = restore_checkpoint(snapshot, channels=channels, agendas=agendas)
        return RestoredWorldResourceCheckpoint(
            world=world,
            reservation_ledger=ReservationLedger(),
            request_ledger=ResourceRequestLedger(),
            handoff_ledger=ResourceHandoffLedger(),
        )

    payload = _validate_global_digest(snapshot)
    raw_resource_state = payload.get("resource_state")
    if not isinstance(raw_resource_state, Mapping):
        raise ValueError("resource_state checkpoint is required")
    semantic_minute = int(payload["semantic_minute"])

    if schema == LEGACY_WORLD_RESOURCE_CHECKPOINT_SCHEMA:
        reservation_ledger, request_ledger = restore_resource_state(raw_resource_state)
        handoff_ledger = ResourceHandoffLedger()
    else:
        reservation_ledger, request_ledger, handoff_ledger = restore_resource_state_with_handoffs(raw_resource_state)
        validate_handoff_checkpoint_time(handoff_ledger, semantic_minute=semantic_minute)

    validate_resource_checkpoint_time(request_ledger, semantic_minute=semantic_minute)
    world = _restore_embedded_world(payload, channels=channels, agendas=agendas)
    return RestoredWorldResourceCheckpoint(
        world=world,
        reservation_ledger=reservation_ledger,
        request_ledger=request_ledger,
        handoff_ledger=handoff_ledger,
    )
