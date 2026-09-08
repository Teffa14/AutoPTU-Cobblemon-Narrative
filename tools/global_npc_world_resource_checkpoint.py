from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_resource_checkpoint import (
    restore_resource_state,
    snapshot_resource_state,
    validate_resource_checkpoint_time,
)
from tools.global_npc_resource_requests import ResourceRequestLedger
from tools.global_npc_resource_reservations import ReservationLedger
from tools.global_npc_world_checkpoint import (
    CHECKPOINT_SCHEMA as BASE_WORLD_CHECKPOINT_SCHEMA,
    RestoredWorldCheckpoint,
    build_checkpoint,
    restore_checkpoint,
)


WORLD_RESOURCE_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V6"


@dataclass(frozen=True)
class RestoredWorldResourceCheckpoint:
    world: RestoredWorldCheckpoint
    reservation_ledger: ReservationLedger
    request_ledger: ResourceRequestLedger


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
    **world_checkpoint_kwargs,
) -> dict:
    """Build the first global checkpoint schema that contains resource history.

    The underlying world checkpoint remains the owner of world-agent state. This
    adapter advances the serialized schema to V6 and adds the Pass 353 resource
    bundle without replaying any resource operation.
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
    payload["resource_state"] = snapshot_resource_state(reservation_ledger, request_ledger)
    return payload | {"sha256": _digest_payload(payload)}


def restore_world_resource_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldResourceCheckpoint:
    """Restore V6 resource-aware checkpoints or older world-only checkpoints.

    Older checkpoints cannot prove resource history that was never serialized,
    so they restore with empty resource ledgers instead of inferred records.
    """
    schema = snapshot.get("schema")
    if schema != WORLD_RESOURCE_CHECKPOINT_SCHEMA:
        world = restore_checkpoint(snapshot, channels=channels, agendas=agendas)
        return RestoredWorldResourceCheckpoint(
            world=world,
            reservation_ledger=ReservationLedger(),
            request_ledger=ResourceRequestLedger(),
        )

    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world checkpoint digest mismatch")

    raw_resource_state = payload.get("resource_state")
    if not isinstance(raw_resource_state, Mapping):
        raise ValueError("resource_state checkpoint is required")
    reservation_ledger, request_ledger = restore_resource_state(raw_resource_state)
    semantic_minute = int(payload["semantic_minute"])
    validate_resource_checkpoint_time(request_ledger, semantic_minute=semantic_minute)

    base_payload = {str(key): value for key, value in payload.items() if key != "resource_state"}
    base_payload["schema"] = BASE_WORLD_CHECKPOINT_SCHEMA
    world = restore_checkpoint(_redigest(base_payload), channels=channels, agendas=agendas)
    return RestoredWorldResourceCheckpoint(
        world=world,
        reservation_ledger=reservation_ledger,
        request_ledger=request_ledger,
    )
