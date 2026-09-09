from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_resource_allocation_application import ResourceAllocationApplicationLedger
from tools.global_npc_resource_allocation_application_checkpoint import (
    RESOURCE_CHECKPOINT_ALLOCATION_APPLICATION_SCHEMA,
    restore_resource_state_with_allocation_applications,
    snapshot_resource_state_with_allocation_applications,
    validate_allocation_application_checkpoint_time,
)
from tools.global_npc_resource_allocation_checkpoint import snapshot_resource_state_with_allocations
from tools.global_npc_world_resource_allocation_checkpoint import (
    WORLD_RESOURCE_ALLOCATION_CHECKPOINT_SCHEMA,
    RestoredWorldResourceAllocationCheckpoint,
    build_world_resource_allocation_checkpoint,
    restore_world_resource_allocation_checkpoint,
)


WORLD_RESOURCE_ALLOCATION_APPLICATION_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V13"


@dataclass(frozen=True)
class RestoredWorldResourceAllocationApplicationCheckpoint:
    world_resource_allocation: RestoredWorldResourceAllocationCheckpoint
    application_ledger: ResourceAllocationApplicationLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _redigest(payload: Mapping[str, object]) -> dict:
    row = {str(key): value for key, value in payload.items() if key != "sha256"}
    return row | {"sha256": _digest_payload(row)}


def build_world_resource_allocation_application_checkpoint(
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
    authority_evidence,
    resolution_ledger,
    application_ledger: ResourceAllocationApplicationLedger,
    **world_checkpoint_kwargs,
) -> dict:
    """Build one coherent checkpoint through Pass 349 allocation application.

    V13 places the operational application in the same recovery instant as the
    Pass 348 decision, Pass 347 historical conflict, communications, NPC state
    and semantic time. It does not create Pass 350 notice obligations or deliver
    any communication.
    """
    base = build_world_resource_allocation_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        reservation_ledger=reservation_ledger,
        request_ledger=request_ledger,
        handoff_ledger=handoff_ledger,
        attempt_ledger=attempt_ledger,
        appointment_ledger=appointment_ledger,
        reschedule_ledger=reschedule_ledger,
        admission_ledger=admission_ledger,
        authority_evidence=authority_evidence,
        resolution_ledger=resolution_ledger,
        **world_checkpoint_kwargs,
    )
    payload = {str(key): value for key, value in base.items() if key != "sha256"}
    if payload.get("schema") != WORLD_RESOURCE_ALLOCATION_CHECKPOINT_SCHEMA:
        raise ValueError("unexpected world resource allocation checkpoint schema")
    payload["schema"] = WORLD_RESOURCE_ALLOCATION_APPLICATION_CHECKPOINT_SCHEMA
    payload["resource_state"] = snapshot_resource_state_with_allocation_applications(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
        admission_ledger,
        authority_evidence,
        resolution_ledger,
        application_ledger,
    )
    return payload | {"sha256": _digest_payload(payload)}


def restore_world_resource_allocation_application_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldResourceAllocationApplicationCheckpoint:
    """Restore V13, or migrate V12 with deliberately empty application history.

    Restore never infers Pass 349 application from current reservation state,
    a later notice, custody, memory or dialogue. When V13 is present, the
    application must validate against the persisted Pass 348 decision before the
    earlier V12 world boundary is reconstructed and checked.
    """
    schema = snapshot.get("schema")
    if schema != WORLD_RESOURCE_ALLOCATION_APPLICATION_CHECKPOINT_SCHEMA:
        restored = restore_world_resource_allocation_checkpoint(snapshot, channels=channels, agendas=agendas)
        return RestoredWorldResourceAllocationApplicationCheckpoint(
            world_resource_allocation=restored,
            application_ledger=ResourceAllocationApplicationLedger(),
        )

    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world allocation application checkpoint digest mismatch")

    raw_resource_state = payload.get("resource_state")
    if not isinstance(raw_resource_state, Mapping):
        raise ValueError("resource_state checkpoint is required")
    if raw_resource_state.get("schema") != RESOURCE_CHECKPOINT_ALLOCATION_APPLICATION_SCHEMA:
        restore_resource_state_with_allocation_applications(raw_resource_state)
        raise ValueError("V13 world checkpoint requires allocation-application-aware resource state")

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
        application_ledger,
    ) = restore_resource_state_with_allocation_applications(raw_resource_state)

    semantic_minute = int(payload["semantic_minute"])
    validate_allocation_application_checkpoint_time(
        application_ledger,
        semantic_minute=semantic_minute,
    )

    v12_payload = dict(payload)
    v12_payload["schema"] = WORLD_RESOURCE_ALLOCATION_CHECKPOINT_SCHEMA
    v12_payload["resource_state"] = snapshot_resource_state_with_allocations(
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
    restored = restore_world_resource_allocation_checkpoint(
        _redigest(v12_payload),
        channels=channels,
        agendas=agendas,
    )

    world_resource_admission = restored.world_resource_admission
    world_resource = world_resource_admission.world_resource
    if (
        world_resource.reservation_ledger != reservation_ledger
        or world_resource.request_ledger != request_ledger
        or world_resource.handoff_ledger != handoff_ledger
        or world_resource.attempt_ledger != attempt_ledger
        or world_resource.appointment_ledger != appointment_ledger
        or world_resource.reschedule_ledger != reschedule_ledger
        or world_resource_admission.admission_ledger != admission_ledger
        or restored.authority_evidence != authority_evidence
        or restored.resolution_ledger != resolution_ledger
    ):
        raise ValueError("world allocation application checkpoint owner reconstruction mismatch")

    return RestoredWorldResourceAllocationApplicationCheckpoint(
        world_resource_allocation=restored,
        application_ledger=application_ledger,
    )
