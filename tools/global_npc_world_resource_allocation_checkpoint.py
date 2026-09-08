from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_resource_admission_checkpoint import snapshot_resource_state_with_admissions
from tools.global_npc_resource_allocation_checkpoint import (
    RESOURCE_CHECKPOINT_ALLOCATION_SCHEMA,
    restore_resource_state_with_allocations,
    snapshot_resource_state_with_allocations,
    validate_allocation_checkpoint_time,
)
from tools.global_npc_resource_allocation_resolution import (
    AllocationAuthorityEvidence,
    ResourceAllocationResolutionLedger,
)
from tools.global_npc_world_resource_admission_checkpoint import (
    WORLD_RESOURCE_ADMISSION_CHECKPOINT_SCHEMA,
    RestoredWorldResourceAdmissionCheckpoint,
    build_world_resource_admission_checkpoint,
    restore_world_resource_admission_checkpoint,
)


WORLD_RESOURCE_ALLOCATION_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V12"


@dataclass(frozen=True)
class RestoredWorldResourceAllocationCheckpoint:
    world_resource_admission: RestoredWorldResourceAdmissionCheckpoint
    authority_evidence: tuple[AllocationAuthorityEvidence, ...]
    resolution_ledger: ResourceAllocationResolutionLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _redigest(payload: Mapping[str, object]) -> dict:
    row = {str(key): value for key, value in payload.items() if key != "sha256"}
    return row | {"sha256": _digest_payload(row)}


def build_world_resource_allocation_checkpoint(
    coordinator,
    *,
    semantic_minute: int,
    reservation_ledger,
    request_ledger,
    handoff_ledger,
    attempt_ledger,
    appointment_ledger,
    reschedule_ledger,
    admission_ledger,
    authority_evidence: tuple[AllocationAuthorityEvidence, ...],
    resolution_ledger: ResourceAllocationResolutionLedger,
    **world_checkpoint_kwargs,
) -> dict:
    """Build one coherent checkpoint through Pass 348 allocation resolution.

    V12 keeps Pass 348 decision provenance in the same digest as the historical
    Pass 347 conflict, resource owners, communications, NPC state and semantic time.
    It deliberately does not apply the decision; operational displacement remains
    owned by Pass 349.
    """
    base = build_world_resource_admission_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        reservation_ledger=reservation_ledger,
        request_ledger=request_ledger,
        handoff_ledger=handoff_ledger,
        attempt_ledger=attempt_ledger,
        appointment_ledger=appointment_ledger,
        reschedule_ledger=reschedule_ledger,
        admission_ledger=admission_ledger,
        **world_checkpoint_kwargs,
    )
    payload = {str(key): value for key, value in base.items() if key != "sha256"}
    if payload.get("schema") != WORLD_RESOURCE_ADMISSION_CHECKPOINT_SCHEMA:
        raise ValueError("unexpected world resource admission checkpoint schema")
    payload["schema"] = WORLD_RESOURCE_ALLOCATION_CHECKPOINT_SCHEMA
    payload["resource_state"] = snapshot_resource_state_with_allocations(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
        admission_ledger,
        authority_evidence,
        resolution_ledger,
    )
    return payload | {"sha256": _digest_payload(payload)}


def restore_world_resource_allocation_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldResourceAllocationCheckpoint:
    """Restore V12, or migrate V11 with deliberately empty allocation history.

    Current reservation state, downstream application, memory and dialogue never
    synthesize an earlier Pass 348 decision. V12 restores the persisted decision
    and authority evidence, validates their time, then delegates all earlier world
    and cross-owner checks to V11.
    """
    schema = snapshot.get("schema")
    if schema != WORLD_RESOURCE_ALLOCATION_CHECKPOINT_SCHEMA:
        restored = restore_world_resource_admission_checkpoint(snapshot, channels=channels, agendas=agendas)
        return RestoredWorldResourceAllocationCheckpoint(
            world_resource_admission=restored,
            authority_evidence=(),
            resolution_ledger=ResourceAllocationResolutionLedger(),
        )

    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world allocation checkpoint digest mismatch")

    raw_resource_state = payload.get("resource_state")
    if not isinstance(raw_resource_state, Mapping):
        raise ValueError("resource_state checkpoint is required")
    if raw_resource_state.get("schema") != RESOURCE_CHECKPOINT_ALLOCATION_SCHEMA:
        restore_resource_state_with_allocations(raw_resource_state)
        raise ValueError("V12 world checkpoint requires allocation-aware resource state")

    (
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
        admission_ledger,
        authority_evidence,
        resolution_ledger,
    ) = restore_resource_state_with_allocations(raw_resource_state)

    semantic_minute = int(payload["semantic_minute"])
    validate_allocation_checkpoint_time(
        authority_evidence,
        resolution_ledger,
        semantic_minute=semantic_minute,
    )

    v11_payload = dict(payload)
    v11_payload["schema"] = WORLD_RESOURCE_ADMISSION_CHECKPOINT_SCHEMA
    v11_payload["resource_state"] = snapshot_resource_state_with_admissions(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
        admission_ledger,
    )
    restored = restore_world_resource_admission_checkpoint(
        _redigest(v11_payload),
        channels=channels,
        agendas=agendas,
    )

    world_resource = restored.world_resource
    if (
        world_resource.reservation_ledger != reservation_ledger
        or world_resource.request_ledger != request_ledger
        or world_resource.handoff_ledger != handoff_ledger
        or world_resource.attempt_ledger != attempt_ledger
        or world_resource.appointment_ledger != appointment_ledger
        or world_resource.reschedule_ledger != reschedule_ledger
        or restored.admission_ledger != admission_ledger
    ):
        raise ValueError("world allocation checkpoint owner reconstruction mismatch")

    return RestoredWorldResourceAllocationCheckpoint(
        world_resource_admission=restored,
        authority_evidence=authority_evidence,
        resolution_ledger=resolution_ledger,
    )
