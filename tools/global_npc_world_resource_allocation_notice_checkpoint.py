from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_resource_allocation_notice_checkpoint import (
    RESOURCE_CHECKPOINT_ALLOCATION_NOTICE_SCHEMA,
    restore_resource_state_with_allocation_notices,
    snapshot_resource_state_with_allocation_notices,
    validate_allocation_notice_checkpoint_time,
)
from tools.global_npc_resource_allocation_notices import ResourceAllocationNoticeLedger
from tools.global_npc_resource_allocation_application_checkpoint import snapshot_resource_state_with_allocation_applications
from tools.global_npc_world_resource_allocation_application_checkpoint import (
    WORLD_RESOURCE_ALLOCATION_APPLICATION_CHECKPOINT_SCHEMA,
    RestoredWorldResourceAllocationApplicationCheckpoint,
    build_world_resource_allocation_application_checkpoint,
    restore_world_resource_allocation_application_checkpoint,
)


WORLD_RESOURCE_ALLOCATION_NOTICE_CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V14"


@dataclass(frozen=True)
class RestoredWorldResourceAllocationNoticeCheckpoint:
    world_resource_allocation_application: RestoredWorldResourceAllocationApplicationCheckpoint
    notice_ledger: ResourceAllocationNoticeLedger


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _redigest(payload: Mapping[str, object]) -> dict:
    row = {str(key): value for key, value in payload.items() if key != "sha256"}
    return row | {"sha256": _digest_payload(row)}


def build_world_resource_allocation_notice_checkpoint(
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
    application_ledger,
    notice_ledger: ResourceAllocationNoticeLedger,
    **world_checkpoint_kwargs,
) -> dict:
    """Build one coherent checkpoint through Pass 350 allocation-notice ownership.

    V14 keeps the notice obligation and any notice-to-communication link in the
    same recovery instant as Communications, NPC state, Pass 347 conflict
    admission, Pass 348 resolution and Pass 349 application. Message transport
    remains owned by InformationEventQueue.
    """
    base = build_world_resource_allocation_application_checkpoint(
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
        application_ledger=application_ledger,
        **world_checkpoint_kwargs,
    )
    payload = {str(key): value for key, value in base.items() if key != "sha256"}
    if payload.get("schema") != WORLD_RESOURCE_ALLOCATION_APPLICATION_CHECKPOINT_SCHEMA:
        raise ValueError("unexpected world resource allocation application checkpoint schema")
    payload["schema"] = WORLD_RESOURCE_ALLOCATION_NOTICE_CHECKPOINT_SCHEMA
    payload["resource_state"] = snapshot_resource_state_with_allocation_notices(
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
        notice_ledger,
    )
    return payload | {"sha256": _digest_payload(payload)}


def _world_coordinator(restored: RestoredWorldResourceAllocationApplicationCheckpoint):
    return (
        restored.world_resource_allocation
        .world_resource_admission
        .world_resource
        .world
        .coordinator
    )


def _validate_notice_communication_bindings(
    notice_ledger: ResourceAllocationNoticeLedger,
    restored: RestoredWorldResourceAllocationApplicationCheckpoint,
) -> None:
    """Validate Pass 351/352 addressing against the transport owner.

    A preserved link proves which real envelope it references. Delivery remains a
    separate queue status: pending, waiting-local-ack, delivered and terminal
    failed envelopes can all retain valid provenance without being conflated.
    """
    queue = _world_coordinator(restored).information_queue
    obligation_by_id = {row.obligation_id: row for row in notice_ledger.obligations}
    for link in notice_ledger.links:
        obligation = obligation_by_id[link.obligation_id]
        envelope = queue.envelope_provenance(link.communication_event_id)
        if envelope is None:
            raise ValueError(f"allocation notice communication provenance unavailable: {link.link_id}")
        if link.communication_event_id not in queue.statuses:
            raise ValueError(f"allocation notice communication status unavailable: {link.link_id}")
        if envelope.sender_id != link.sender_actor_id:
            raise ValueError(f"allocation notice communication sender mismatch: {link.link_id}")
        if envelope.receiver_id != obligation.affected_actor_id:
            raise ValueError(f"allocation notice communication receiver mismatch: {link.link_id}")
        if link.linked_tick < envelope.created_minute:
            raise ValueError(f"allocation notice link precedes authored communication: {link.link_id}")


def restore_world_resource_allocation_notice_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels,
    agendas=None,
) -> RestoredWorldResourceAllocationNoticeCheckpoint:
    """Restore V14, or migrate V13 with deliberately empty notice history.

    Restore does not infer Pass 350 obligations or links from current bookings,
    message history, knowledge, custody or later behavior. V14 reuses V13 for all
    earlier owners, then validates every persisted link against the actual
    InformationEventQueue envelope retained by Pass 351/352.
    """
    schema = snapshot.get("schema")
    if schema != WORLD_RESOURCE_ALLOCATION_NOTICE_CHECKPOINT_SCHEMA:
        restored = restore_world_resource_allocation_application_checkpoint(
            snapshot,
            channels=channels,
            agendas=agendas,
        )
        return RestoredWorldResourceAllocationNoticeCheckpoint(
            world_resource_allocation_application=restored,
            notice_ledger=ResourceAllocationNoticeLedger(),
        )

    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world allocation notice checkpoint digest mismatch")

    raw_resource_state = payload.get("resource_state")
    if not isinstance(raw_resource_state, Mapping):
        raise ValueError("resource_state checkpoint is required")
    if raw_resource_state.get("schema") != RESOURCE_CHECKPOINT_ALLOCATION_NOTICE_SCHEMA:
        restore_resource_state_with_allocation_notices(raw_resource_state)
        raise ValueError("V14 world checkpoint requires allocation-notice-aware resource state")

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
        notice_ledger,
    ) = restore_resource_state_with_allocation_notices(raw_resource_state)

    semantic_minute = int(payload["semantic_minute"])
    validate_allocation_notice_checkpoint_time(notice_ledger, semantic_minute=semantic_minute)

    v13_payload = dict(payload)
    v13_payload["schema"] = WORLD_RESOURCE_ALLOCATION_APPLICATION_CHECKPOINT_SCHEMA
    v13_payload["resource_state"] = snapshot_resource_state_with_allocation_applications(
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
    restored = restore_world_resource_allocation_application_checkpoint(
        _redigest(v13_payload),
        channels=channels,
        agendas=agendas,
    )

    world_allocation = restored.world_resource_allocation
    world_admission = world_allocation.world_resource_admission
    world_resource = world_admission.world_resource
    if (
        world_resource.reservation_ledger != reservation_ledger
        or world_resource.request_ledger != request_ledger
        or world_resource.handoff_ledger != handoff_ledger
        or world_resource.attempt_ledger != attempt_ledger
        or world_resource.appointment_ledger != appointment_ledger
        or world_resource.reschedule_ledger != reschedule_ledger
        or world_admission.admission_ledger != admission_ledger
        or world_allocation.authority_evidence != authority_evidence
        or world_allocation.resolution_ledger != resolution_ledger
        or restored.application_ledger != application_ledger
    ):
        raise ValueError("world allocation notice checkpoint owner reconstruction mismatch")

    _validate_notice_communication_bindings(notice_ledger, restored)

    return RestoredWorldResourceAllocationNoticeCheckpoint(
        world_resource_allocation_application=restored,
        notice_ledger=notice_ledger,
    )
