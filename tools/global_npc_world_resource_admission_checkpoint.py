from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_resource_admission_checkpoint import (
    RESOURCE_CHECKPOINT_ADMISSION_SCHEMA,
    restore_resource_state_with_admissions,
    snapshot_resource_state_with_admissions,
    validate_admission_checkpoint_time,
)
from tools.global_npc_resource_handoff_reschedule_admission_history import ResourceRescheduleAdmissionLedger
from tools.global_npc_resource_reschedule_checkpoint import snapshot_resource_state_with_reschedules
from tools.global_npc_world_resource_checkpoint import (
    WORLD_RESOURCE_CHECKPOINT_SCHEMA,
    RestoredWorldResourceCheckpoint,
    build_world_resource_checkpoint,
    restore_world_resource_checkpoint,
)


WORLD_RESOURCE_ADMISSION_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V11"


@dataclass(frozen=True)
class RestoredWorldResourceAdmissionCheckpoint:
    world_resource: RestoredWorldResourceCheckpoint
    admission_ledger: ResourceRescheduleAdmissionLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _redigest(payload: Mapping[str, object]) -> dict:
    row = {str(key): value for key, value in payload.items() if key != "sha256"}
    return row | {"sha256": _digest_payload(row)}


def build_world_resource_admission_checkpoint(
    coordinator,
    *,
    semantic_minute: int,
    reservation_ledger,
    request_ledger,
    handoff_ledger,
    attempt_ledger,
    appointment_ledger,
    reschedule_ledger,
    admission_ledger: ResourceRescheduleAdmissionLedger,
    **world_checkpoint_kwargs,
) -> dict:
    """Build one coherent checkpoint through Pass 347 resource-conflict admission.

    Pass 362 remains responsible for validating appointment communication provenance
    and delivered reschedule requests. V11 extends that same globally digested recovery
    instant with the historical read-model result recorded by Pass 363.
    """
    base = build_world_resource_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        reservation_ledger=reservation_ledger,
        request_ledger=request_ledger,
        handoff_ledger=handoff_ledger,
        attempt_ledger=attempt_ledger,
        appointment_ledger=appointment_ledger,
        reschedule_ledger=reschedule_ledger,
        **world_checkpoint_kwargs,
    )
    payload = {str(key): value for key, value in base.items() if key != "sha256"}
    if payload.get("schema") != WORLD_RESOURCE_CHECKPOINT_SCHEMA:
        raise ValueError("unexpected world resource checkpoint schema")
    payload["schema"] = WORLD_RESOURCE_ADMISSION_CHECKPOINT_SCHEMA
    payload["resource_state"] = snapshot_resource_state_with_admissions(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
        admission_ledger,
    )
    return payload | {"sha256": _digest_payload(payload)}


def restore_world_resource_admission_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldResourceAdmissionCheckpoint:
    """Restore V11, or migrate V10 with deliberately empty admission history.

    V11 validates admission history against the historical reservation and reschedule
    owners embedded in the same digest. It then delegates world, appointment and
    communication validation to the existing V10 recovery path. No current calendar,
    memory state, dialogue or later allocation result is used to synthesize an older
    admission assessment.
    """
    schema = snapshot.get("schema")
    if schema != WORLD_RESOURCE_ADMISSION_CHECKPOINT_SCHEMA:
        restored = restore_world_resource_checkpoint(snapshot, channels=channels, agendas=agendas)
        return RestoredWorldResourceAdmissionCheckpoint(
            world_resource=restored,
            admission_ledger=ResourceRescheduleAdmissionLedger(),
        )

    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world admission checkpoint digest mismatch")

    raw_resource_state = payload.get("resource_state")
    if not isinstance(raw_resource_state, Mapping):
        raise ValueError("resource_state checkpoint is required")
    if raw_resource_state.get("schema") != RESOURCE_CHECKPOINT_ADMISSION_SCHEMA:
        restore_resource_state_with_admissions(raw_resource_state)
        raise ValueError("V11 world checkpoint requires admission-aware resource state")

    (
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
        admission_ledger,
    ) = restore_resource_state_with_admissions(raw_resource_state)

    semantic_minute = int(payload["semantic_minute"])
    validate_admission_checkpoint_time(admission_ledger, semantic_minute=semantic_minute)

    v10_payload = dict(payload)
    v10_payload["schema"] = WORLD_RESOURCE_CHECKPOINT_SCHEMA
    v10_payload["resource_state"] = snapshot_resource_state_with_reschedules(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
    )
    restored = restore_world_resource_checkpoint(
        _redigest(v10_payload),
        channels=channels,
        agendas=agendas,
    )

    if (
        restored.reservation_ledger != reservation_ledger
        or restored.request_ledger != request_ledger
        or restored.handoff_ledger != handoff_ledger
        or restored.attempt_ledger != attempt_ledger
        or restored.appointment_ledger != appointment_ledger
        or restored.reschedule_ledger != reschedule_ledger
    ):
        raise ValueError("world admission checkpoint owner reconstruction mismatch")

    return RestoredWorldResourceAdmissionCheckpoint(
        world_resource=restored,
        admission_ledger=admission_ledger,
    )
