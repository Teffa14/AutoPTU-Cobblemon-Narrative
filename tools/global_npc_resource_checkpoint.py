from __future__ import annotations

from typing import Mapping

from tools.global_npc_resource_requests import (
    ResourceRequest,
    ResourceRequestEvent,
    ResourceRequestEventKind,
    ResourceRequestLedger,
)
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    ReservationState,
    ResourceReservation,
)


RESOURCE_CHECKPOINT_SCHEMA = "OUROS_NPC_RESOURCE_CHECKPOINT_V1"


def snapshot_resource_state(
    reservation_ledger: ReservationLedger,
    request_ledger: ResourceRequestLedger,
) -> dict:
    """Serialize resource ledgers without changing their ownership semantics."""
    return {
        "schema": RESOURCE_CHECKPOINT_SCHEMA,
        "reservations": [
            {
                "reservation_id": row.reservation_id,
                "resource_id": row.resource_id,
                "actor_id": row.actor_id,
                "start_tick": row.start_tick,
                "end_tick": row.end_tick,
                "state": row.state.value,
                "purpose_ref": row.purpose_ref,
            }
            for row in sorted(reservation_ledger.reservations, key=lambda item: item.reservation_id)
        ],
        "requests": [
            {
                "request_id": row.request_id,
                "requester_actor_id": row.requester_actor_id,
                "provider_actor_id": row.provider_actor_id,
                "resource_id": row.resource_id,
                "created_tick": row.created_tick,
                "quantity": row.quantity,
                "expires_at_tick": row.expires_at_tick,
                "purpose_ref": row.purpose_ref,
            }
            for row in sorted(request_ledger.requests, key=lambda item: item.request_id)
        ],
        "request_events": [
            {
                "event_id": row.event_id,
                "request_id": row.request_id,
                "actor_id": row.actor_id,
                "kind": row.kind.value,
                "at_tick": row.at_tick,
                "offered_resource_id": row.offered_resource_id,
                "reason_ref": row.reason_ref,
            }
            for row in sorted(
                request_ledger.events,
                key=lambda item: (item.request_id, item.at_tick, item.event_id),
            )
        ],
    }


def restore_resource_state(snapshot: Mapping[str, object]) -> tuple[ReservationLedger, ResourceRequestLedger]:
    if snapshot.get("schema") != RESOURCE_CHECKPOINT_SCHEMA:
        raise ValueError("unsupported resource checkpoint schema")

    raw_reservations = snapshot.get("reservations", [])
    raw_requests = snapshot.get("requests", [])
    raw_events = snapshot.get("request_events", [])
    if not isinstance(raw_reservations, list) or not isinstance(raw_requests, list) or not isinstance(raw_events, list):
        raise ValueError("resource checkpoint collections must be lists")

    reservations: list[ResourceReservation] = []
    for raw in raw_reservations:
        if not isinstance(raw, Mapping):
            raise ValueError("resource reservation checkpoint row must be a mapping")
        reservations.append(
            ResourceReservation(
                reservation_id=str(raw["reservation_id"]),
                resource_id=str(raw["resource_id"]),
                actor_id=str(raw["actor_id"]),
                start_tick=int(raw["start_tick"]),
                end_tick=int(raw["end_tick"]),
                state=ReservationState(str(raw.get("state", ReservationState.ACTIVE.value))),
                purpose_ref=None if raw.get("purpose_ref") is None else str(raw["purpose_ref"]),
            )
        )

    requests: list[ResourceRequest] = []
    for raw in raw_requests:
        if not isinstance(raw, Mapping):
            raise ValueError("resource request checkpoint row must be a mapping")
        requests.append(
            ResourceRequest(
                request_id=str(raw["request_id"]),
                requester_actor_id=str(raw["requester_actor_id"]),
                provider_actor_id=str(raw["provider_actor_id"]),
                resource_id=str(raw["resource_id"]),
                created_tick=int(raw["created_tick"]),
                quantity=int(raw.get("quantity", 1)),
                expires_at_tick=None if raw.get("expires_at_tick") is None else int(raw["expires_at_tick"]),
                purpose_ref=None if raw.get("purpose_ref") is None else str(raw["purpose_ref"]),
            )
        )

    events: list[ResourceRequestEvent] = []
    for raw in raw_events:
        if not isinstance(raw, Mapping):
            raise ValueError("resource request event checkpoint row must be a mapping")
        events.append(
            ResourceRequestEvent(
                event_id=str(raw["event_id"]),
                request_id=str(raw["request_id"]),
                actor_id=str(raw["actor_id"]),
                kind=ResourceRequestEventKind(str(raw["kind"])),
                at_tick=int(raw["at_tick"]),
                offered_resource_id=None if raw.get("offered_resource_id") is None else str(raw["offered_resource_id"]),
                reason_ref=None if raw.get("reason_ref") is None else str(raw["reason_ref"]),
            )
        )

    reservation_ids = [row.reservation_id for row in reservations]
    request_ids = [row.request_id for row in requests]
    event_ids = [row.event_id for row in events]
    if len(set(reservation_ids)) != len(reservation_ids):
        raise ValueError("resource checkpoint contains duplicate reservation IDs")
    if len(set(request_ids)) != len(request_ids):
        raise ValueError("resource checkpoint contains duplicate request IDs")
    if len(set(event_ids)) != len(event_ids):
        raise ValueError("resource checkpoint contains duplicate request event IDs")

    request_by_id = {row.request_id: row for row in requests}
    for event in events:
        request = request_by_id.get(event.request_id)
        if request is None:
            raise ValueError(f"resource request event references missing request: {event.event_id}")
        if event.at_tick < request.created_tick:
            raise ValueError(f"resource request event predates request: {event.event_id}")
        if event.actor_id not in {request.requester_actor_id, request.provider_actor_id}:
            raise ValueError(f"resource request event actor is not a participant: {event.event_id}")

    return (
        ReservationLedger(tuple(sorted(reservations, key=lambda item: item.reservation_id))),
        ResourceRequestLedger(
            requests=tuple(sorted(requests, key=lambda item: item.request_id)),
            events=tuple(sorted(events, key=lambda item: (item.request_id, item.at_tick, item.event_id))),
        ),
    )


def validate_resource_checkpoint_time(
    request_ledger: ResourceRequestLedger,
    *,
    semantic_minute: int,
) -> None:
    for request in request_ledger.requests:
        if request.created_tick > semantic_minute:
            raise ValueError(f"resource request comes from the future: {request.request_id}")
    for event in request_ledger.events:
        if event.at_tick > semantic_minute:
            raise ValueError(f"resource request event comes from the future: {event.event_id}")
