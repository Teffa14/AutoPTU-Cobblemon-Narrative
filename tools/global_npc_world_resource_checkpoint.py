from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_resource_appointment_checkpoint import (
    RESOURCE_CHECKPOINT_APPOINTMENT_SCHEMA,
    restore_resource_state_with_appointment_notices,
    snapshot_resource_state_with_appointment_notices,
    validate_appointment_checkpoint_time,
)
from tools.global_npc_resource_attempt_checkpoint import (
    RESOURCE_CHECKPOINT_ATTEMPT_SCHEMA,
    restore_resource_state_with_attempts,
    snapshot_resource_state_with_attempts,
    validate_attempt_checkpoint_time,
)
from tools.global_npc_resource_checkpoint import (
    restore_resource_state,
    restore_resource_state_with_handoffs,
    validate_handoff_checkpoint_time,
    validate_resource_checkpoint_time,
)
from tools.global_npc_resource_handoff_appointments import ResourceHandoffAppointmentLedger
from tools.global_npc_resource_handoff_attempts import ResourceHandoffAttemptLedger
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
LEGACY_WORLD_RESOURCE_HANDOFF_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V7"
LEGACY_WORLD_RESOURCE_ATTEMPT_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V8"
WORLD_RESOURCE_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V9"


@dataclass(frozen=True)
class RestoredWorldResourceCheckpoint:
    world: RestoredWorldCheckpoint
    reservation_ledger: ReservationLedger
    request_ledger: ResourceRequestLedger
    handoff_ledger: ResourceHandoffLedger
    attempt_ledger: ResourceHandoffAttemptLedger
    appointment_ledger: ResourceHandoffAppointmentLedger


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
    attempt_ledger: ResourceHandoffAttemptLedger | None = None,
    appointment_ledger: ResourceHandoffAppointmentLedger | None = None,
    **world_checkpoint_kwargs,
) -> dict:
    """Build one coherent world checkpoint through optional Pass 345 appointment history.

    The underlying world checkpoint remains owner of world-agent and communication
    state. When an appointment ledger is supplied, V9 embeds the validated Pass 359
    V4 resource bundle. Callers that intentionally omit that owner retain the V3
    resource shape and restore an explicit empty appointment ledger.
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
    handoffs = handoff_ledger or ResourceHandoffLedger()
    attempts = attempt_ledger or ResourceHandoffAttemptLedger()
    if appointment_ledger is None:
        payload["resource_state"] = snapshot_resource_state_with_attempts(
            reservation_ledger,
            request_ledger,
            handoffs,
            attempts,
        )
    else:
        payload["resource_state"] = snapshot_resource_state_with_appointment_notices(
            reservation_ledger,
            request_ledger,
            handoffs,
            attempts,
            appointment_ledger,
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


def _validate_appointment_communication_bindings(
    appointment_ledger: ResourceHandoffAppointmentLedger,
    world: RestoredWorldCheckpoint,
) -> None:
    queue = world.coordinator.information_queue
    for notice in appointment_ledger.notices:
        envelope = queue.envelope_provenance(notice.communication_event_id)
        if envelope is None:
            raise ValueError(
                f"handoff appointment notice communication provenance unavailable: {notice.notice_id}"
            )
        if envelope.sender_id != notice.sender_actor_id:
            raise ValueError(f"handoff appointment notice sender mismatch: {notice.notice_id}")
        if envelope.receiver_id != notice.receiver_actor_id:
            raise ValueError(f"handoff appointment notice receiver mismatch: {notice.notice_id}")
        if envelope.source_claim_id != notice.source_claim_id:
            raise ValueError(f"handoff appointment notice source claim mismatch: {notice.notice_id}")
        if envelope.created_minute != notice.created_tick:
            raise ValueError(f"handoff appointment notice timestamp mismatch: {notice.notice_id}")


def restore_world_resource_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldResourceCheckpoint:
    """Restore V9 and older checkpoints without inventing absent history.

    V9 accepts either its V4 appointment-aware resource bundle or an intentional V3
    bundle from callers that did not supply appointment history. V8 restores its V3
    failed-attempt bundle with an empty appointment ledger. V7 restores handoff
    history with empty attempt/appointment ledgers. V6 restores reservation/request
    history only. Older world-only checkpoints restore all resource ledgers empty.
    """
    schema = snapshot.get("schema")
    supported = {
        WORLD_RESOURCE_CHECKPOINT_SCHEMA,
        LEGACY_WORLD_RESOURCE_ATTEMPT_CHECKPOINT_SCHEMA,
        LEGACY_WORLD_RESOURCE_HANDOFF_CHECKPOINT_SCHEMA,
        LEGACY_WORLD_RESOURCE_CHECKPOINT_SCHEMA,
    }
    if schema not in supported:
        world = restore_checkpoint(snapshot, channels=channels, agendas=agendas)
        return RestoredWorldResourceCheckpoint(
            world=world,
            reservation_ledger=ReservationLedger(),
            request_ledger=ResourceRequestLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            attempt_ledger=ResourceHandoffAttemptLedger(),
            appointment_ledger=ResourceHandoffAppointmentLedger(),
        )

    payload = _validate_global_digest(snapshot)
    raw_resource_state = payload.get("resource_state")
    if not isinstance(raw_resource_state, Mapping):
        raise ValueError("resource_state checkpoint is required")
    semantic_minute = int(payload["semantic_minute"])

    if schema == LEGACY_WORLD_RESOURCE_CHECKPOINT_SCHEMA:
        reservation_ledger, request_ledger = restore_resource_state(raw_resource_state)
        handoff_ledger = ResourceHandoffLedger()
        attempt_ledger = ResourceHandoffAttemptLedger()
        appointment_ledger = ResourceHandoffAppointmentLedger()
    elif schema == LEGACY_WORLD_RESOURCE_HANDOFF_CHECKPOINT_SCHEMA:
        reservation_ledger, request_ledger, handoff_ledger = restore_resource_state_with_handoffs(raw_resource_state)
        attempt_ledger = ResourceHandoffAttemptLedger()
        appointment_ledger = ResourceHandoffAppointmentLedger()
        validate_handoff_checkpoint_time(handoff_ledger, semantic_minute=semantic_minute)
    elif schema == LEGACY_WORLD_RESOURCE_ATTEMPT_CHECKPOINT_SCHEMA:
        reservation_ledger, request_ledger, handoff_ledger, attempt_ledger = restore_resource_state_with_attempts(
            raw_resource_state
        )
        appointment_ledger = ResourceHandoffAppointmentLedger()
        validate_handoff_checkpoint_time(handoff_ledger, semantic_minute=semantic_minute)
        validate_attempt_checkpoint_time(attempt_ledger, semantic_minute=semantic_minute)
    else:
        nested_schema = raw_resource_state.get("schema")
        if nested_schema == RESOURCE_CHECKPOINT_ATTEMPT_SCHEMA:
            reservation_ledger, request_ledger, handoff_ledger, attempt_ledger = restore_resource_state_with_attempts(
                raw_resource_state
            )
            appointment_ledger = ResourceHandoffAppointmentLedger()
        elif nested_schema == RESOURCE_CHECKPOINT_APPOINTMENT_SCHEMA:
            (
                reservation_ledger,
                request_ledger,
                handoff_ledger,
                attempt_ledger,
                appointment_ledger,
            ) = restore_resource_state_with_appointment_notices(raw_resource_state)
        else:
            restore_resource_state_with_attempts(raw_resource_state)
            raise AssertionError("unreachable nested resource schema")
        validate_handoff_checkpoint_time(handoff_ledger, semantic_minute=semantic_minute)
        validate_attempt_checkpoint_time(attempt_ledger, semantic_minute=semantic_minute)
        validate_appointment_checkpoint_time(appointment_ledger, semantic_minute=semantic_minute)

    validate_resource_checkpoint_time(request_ledger, semantic_minute=semantic_minute)
    world = _restore_embedded_world(payload, channels=channels, agendas=agendas)
    if appointment_ledger.notices:
        _validate_appointment_communication_bindings(appointment_ledger, world)
    return RestoredWorldResourceCheckpoint(
        world=world,
        reservation_ledger=reservation_ledger,
        request_ledger=request_ledger,
        handoff_ledger=handoff_ledger,
        attempt_ledger=attempt_ledger,
        appointment_ledger=appointment_ledger,
    )
