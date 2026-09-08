from __future__ import annotations

from typing import Mapping

from tools.global_npc_resource_attempt_checkpoint import (
    RESOURCE_CHECKPOINT_ATTEMPT_SCHEMA,
    restore_resource_state_with_attempts,
    snapshot_resource_state_with_attempts,
)
from tools.global_npc_resource_checkpoint import (
    RESOURCE_CHECKPOINT_HANDOFF_SCHEMA,
    RESOURCE_CHECKPOINT_SCHEMA,
)
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffAppointmentNotice,
)
from tools.global_npc_resource_handoff_attempts import ResourceHandoffAttemptLedger
from tools.global_npc_resource_handoffs import ResourceHandoffAuthorization, ResourceHandoffLedger
from tools.global_npc_resource_requests import ResourceRequestLedger
from tools.global_npc_resource_reservations import ReservationLedger


RESOURCE_CHECKPOINT_APPOINTMENT_SCHEMA = "OUROS_NPC_RESOURCE_CHECKPOINT_V4"


def snapshot_resource_state_with_appointment_notices(
    reservation_ledger: ReservationLedger,
    request_ledger: ResourceRequestLedger,
    handoff_ledger: ResourceHandoffLedger,
    attempt_ledger: ResourceHandoffAttemptLedger,
    appointment_ledger: ResourceHandoffAppointmentLedger,
) -> dict:
    """Serialize Pass 339/342/343/344 state plus Pass 345 authored appointment notices.

    Delivery remains owned by InformationEventQueue and is deliberately not duplicated here.
    """
    snapshot = snapshot_resource_state_with_attempts(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
    )
    snapshot["schema"] = RESOURCE_CHECKPOINT_APPOINTMENT_SCHEMA
    snapshot["handoff_appointment_notices"] = [
        {
            "notice_id": row.notice_id,
            "authorization_id": row.authorization_id,
            "sender_actor_id": row.sender_actor_id,
            "receiver_actor_id": row.receiver_actor_id,
            "kind": row.kind.value,
            "source_claim_id": row.source_claim_id,
            "communication_event_id": row.communication_event_id,
            "created_tick": row.created_tick,
            "reason_ref": row.reason_ref,
        }
        for row in sorted(appointment_ledger.notices, key=lambda item: (item.created_tick, item.notice_id))
    ]
    return snapshot


def restore_resource_state_with_appointment_notices(
    snapshot: Mapping[str, object],
) -> tuple[
    ReservationLedger,
    ResourceRequestLedger,
    ResourceHandoffLedger,
    ResourceHandoffAttemptLedger,
    ResourceHandoffAppointmentLedger,
]:
    """Restore V4 authored appointment history; V1-V3 never infer missing notices."""
    schema = snapshot.get("schema")
    if schema in {
        RESOURCE_CHECKPOINT_SCHEMA,
        RESOURCE_CHECKPOINT_HANDOFF_SCHEMA,
        RESOURCE_CHECKPOINT_ATTEMPT_SCHEMA,
    }:
        reservations, requests, handoffs, attempts = restore_resource_state_with_attempts(snapshot)
        return reservations, requests, handoffs, attempts, ResourceHandoffAppointmentLedger()
    if schema != RESOURCE_CHECKPOINT_APPOINTMENT_SCHEMA:
        raise ValueError("unsupported resource appointment checkpoint schema")

    base_snapshot = dict(snapshot)
    base_snapshot["schema"] = RESOURCE_CHECKPOINT_ATTEMPT_SCHEMA
    base_snapshot.pop("handoff_appointment_notices", None)
    reservations, requests, handoffs, attempts = restore_resource_state_with_attempts(base_snapshot)

    raw_notices = snapshot.get("handoff_appointment_notices", [])
    if not isinstance(raw_notices, list):
        raise ValueError("handoff appointment checkpoint collection must be a list")

    notices: list[ResourceHandoffAppointmentNotice] = []
    for raw in raw_notices:
        if not isinstance(raw, Mapping):
            raise ValueError("handoff appointment checkpoint row must be a mapping")
        notices.append(
            ResourceHandoffAppointmentNotice(
                notice_id=str(raw["notice_id"]),
                authorization_id=str(raw["authorization_id"]),
                sender_actor_id=str(raw["sender_actor_id"]),
                receiver_actor_id=str(raw["receiver_actor_id"]),
                kind=HandoffAppointmentNoticeKind(str(raw["kind"])),
                source_claim_id=str(raw["source_claim_id"]),
                communication_event_id=str(raw["communication_event_id"]),
                created_tick=int(raw["created_tick"]),
                reason_ref=None if raw.get("reason_ref") is None else str(raw["reason_ref"]),
            )
        )

    notice_ids = [row.notice_id for row in notices]
    if len(set(notice_ids)) != len(notice_ids):
        raise ValueError("resource checkpoint contains duplicate handoff appointment notice IDs")
    communication_event_ids = [row.communication_event_id for row in notices]
    if len(set(communication_event_ids)) != len(communication_event_ids):
        raise ValueError("resource checkpoint contains duplicate handoff appointment communication event IDs")

    authorizations_by_id = {row.authorization_id: row for row in handoffs.authorizations}
    transfers_by_authorization = {row.authorization_id: row for row in handoffs.transfers}
    for notice in notices:
        authorization = authorizations_by_id.get(notice.authorization_id)
        if authorization is None:
            raise ValueError(f"handoff appointment notice references missing authorization: {notice.notice_id}")
        _validate_notice_against_authorization(notice, authorization)

        transfer = transfers_by_authorization.get(notice.authorization_id)
        if transfer is not None and notice.created_tick >= transfer.at_tick:
            raise ValueError(f"handoff appointment notice occurs after completed transfer: {notice.notice_id}")

    return (
        reservations,
        requests,
        handoffs,
        attempts,
        ResourceHandoffAppointmentLedger(
            notices=tuple(sorted(notices, key=lambda item: (item.created_tick, item.notice_id)))
        ),
    )


def _validate_notice_against_authorization(
    notice: ResourceHandoffAppointmentNotice,
    authorization: ResourceHandoffAuthorization,
) -> None:
    participants = {
        authorization.provider_actor_id,
        authorization.receiving_actor_id,
        authorization.accountable_actor_id,
    }
    if notice.sender_actor_id not in participants or notice.receiver_actor_id not in participants:
        raise ValueError(f"handoff appointment notice actors are not authorization participants: {notice.notice_id}")
    if authorization.valid_until_tick is not None and notice.created_tick >= authorization.valid_until_tick:
        raise ValueError(f"handoff appointment notice occurs after authorization expiry: {notice.notice_id}")


def validate_appointment_checkpoint_time(
    appointment_ledger: ResourceHandoffAppointmentLedger,
    *,
    semantic_minute: int,
) -> None:
    """Authored notices are completed communicative acts and cannot originate in the future."""
    for notice in appointment_ledger.notices:
        if notice.created_tick > semantic_minute:
            raise ValueError(f"handoff appointment notice comes from the future: {notice.notice_id}")
