from __future__ import annotations

from typing import Mapping

from tools.global_npc_resource_handoffs import (
    HandoffMode,
    ResourceCustodyTransfer,
    ResourceHandoffAuthorization,
    ResourceHandoffLedger,
)
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
RESOURCE_CHECKPOINT_HANDOFF_SCHEMA = "OUROS_NPC_RESOURCE_CHECKPOINT_V2"


def snapshot_resource_state(
    reservation_ledger: ReservationLedger,
    request_ledger: ResourceRequestLedger,
) -> dict:
    """Serialize the Pass 353 reservation/request boundary unchanged."""
    return {
        "schema": RESOURCE_CHECKPOINT_SCHEMA,
        "reservations": _snapshot_reservations(reservation_ledger),
        "requests": _snapshot_requests(request_ledger),
        "request_events": _snapshot_request_events(request_ledger),
    }


def snapshot_resource_state_with_handoffs(
    reservation_ledger: ReservationLedger,
    request_ledger: ResourceRequestLedger,
    handoff_ledger: ResourceHandoffLedger,
) -> dict:
    """Serialize reservation, request, authorization and custody-transfer history.

    This extends the resource checkpoint without changing any owner semantics.
    Restore reconstructs historical facts only; it never executes a transfer.
    """
    return {
        "schema": RESOURCE_CHECKPOINT_HANDOFF_SCHEMA,
        "reservations": _snapshot_reservations(reservation_ledger),
        "requests": _snapshot_requests(request_ledger),
        "request_events": _snapshot_request_events(request_ledger),
        "handoff_authorizations": [
            {
                "authorization_id": row.authorization_id,
                "request_id": row.request_id,
                "provider_actor_id": row.provider_actor_id,
                "accountable_actor_id": row.accountable_actor_id,
                "receiving_actor_id": row.receiving_actor_id,
                "resource_id": row.resource_id,
                "mode": row.mode.value,
                "handoff_location_ref": row.handoff_location_ref,
                "valid_from_tick": row.valid_from_tick,
                "valid_until_tick": row.valid_until_tick,
                "authority_ref": row.authority_ref,
            }
            for row in sorted(handoff_ledger.authorizations, key=lambda item: item.authorization_id)
        ],
        "custody_transfers": [
            {
                "transfer_id": row.transfer_id,
                "authorization_id": row.authorization_id,
                "request_id": row.request_id,
                "resource_id": row.resource_id,
                "from_actor_id": row.from_actor_id,
                "to_actor_id": row.to_actor_id,
                "accountable_actor_id": row.accountable_actor_id,
                "location_ref": row.location_ref,
                "at_tick": row.at_tick,
                "condition_ref": row.condition_ref,
            }
            for row in sorted(handoff_ledger.transfers, key=lambda item: (item.at_tick, item.transfer_id))
        ],
    }


def _snapshot_reservations(ledger: ReservationLedger) -> list[dict]:
    return [
        {
            "reservation_id": row.reservation_id,
            "resource_id": row.resource_id,
            "actor_id": row.actor_id,
            "start_tick": row.start_tick,
            "end_tick": row.end_tick,
            "state": row.state.value,
            "purpose_ref": row.purpose_ref,
        }
        for row in sorted(ledger.reservations, key=lambda item: item.reservation_id)
    ]


def _snapshot_requests(ledger: ResourceRequestLedger) -> list[dict]:
    return [
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
        for row in sorted(ledger.requests, key=lambda item: item.request_id)
    ]


def _snapshot_request_events(ledger: ResourceRequestLedger) -> list[dict]:
    return [
        {
            "event_id": row.event_id,
            "request_id": row.request_id,
            "actor_id": row.actor_id,
            "kind": row.kind.value,
            "at_tick": row.at_tick,
            "offered_resource_id": row.offered_resource_id,
            "reason_ref": row.reason_ref,
        }
        for row in sorted(ledger.events, key=lambda item: (item.request_id, item.at_tick, item.event_id))
    ]


def restore_resource_state(snapshot: Mapping[str, object]) -> tuple[ReservationLedger, ResourceRequestLedger]:
    if snapshot.get("schema") != RESOURCE_CHECKPOINT_SCHEMA:
        raise ValueError("unsupported resource checkpoint schema")
    return _restore_reservations_requests(snapshot)


def restore_resource_state_with_handoffs(
    snapshot: Mapping[str, object],
) -> tuple[ReservationLedger, ResourceRequestLedger, ResourceHandoffLedger]:
    """Restore V2 handoff history, or V1 with an explicitly empty handoff ledger."""
    schema = snapshot.get("schema")
    if schema == RESOURCE_CHECKPOINT_SCHEMA:
        reservations, requests = _restore_reservations_requests(snapshot)
        return reservations, requests, ResourceHandoffLedger()
    if schema != RESOURCE_CHECKPOINT_HANDOFF_SCHEMA:
        raise ValueError("unsupported resource checkpoint schema")

    reservations, requests = _restore_reservations_requests(snapshot, accepted_schemas={RESOURCE_CHECKPOINT_HANDOFF_SCHEMA})
    raw_authorizations = snapshot.get("handoff_authorizations", [])
    raw_transfers = snapshot.get("custody_transfers", [])
    if not isinstance(raw_authorizations, list) or not isinstance(raw_transfers, list):
        raise ValueError("handoff checkpoint collections must be lists")

    authorizations: list[ResourceHandoffAuthorization] = []
    for raw in raw_authorizations:
        if not isinstance(raw, Mapping):
            raise ValueError("handoff authorization checkpoint row must be a mapping")
        authorizations.append(
            ResourceHandoffAuthorization(
                authorization_id=str(raw["authorization_id"]),
                request_id=str(raw["request_id"]),
                provider_actor_id=str(raw["provider_actor_id"]),
                accountable_actor_id=str(raw["accountable_actor_id"]),
                receiving_actor_id=str(raw["receiving_actor_id"]),
                resource_id=str(raw["resource_id"]),
                mode=HandoffMode(str(raw["mode"])),
                handoff_location_ref=str(raw["handoff_location_ref"]),
                valid_from_tick=int(raw["valid_from_tick"]),
                valid_until_tick=None if raw.get("valid_until_tick") is None else int(raw["valid_until_tick"]),
                authority_ref=None if raw.get("authority_ref") is None else str(raw["authority_ref"]),
            )
        )

    transfers: list[ResourceCustodyTransfer] = []
    for raw in raw_transfers:
        if not isinstance(raw, Mapping):
            raise ValueError("custody transfer checkpoint row must be a mapping")
        transfers.append(
            ResourceCustodyTransfer(
                transfer_id=str(raw["transfer_id"]),
                authorization_id=str(raw["authorization_id"]),
                request_id=str(raw["request_id"]),
                resource_id=str(raw["resource_id"]),
                from_actor_id=str(raw["from_actor_id"]),
                to_actor_id=str(raw["to_actor_id"]),
                accountable_actor_id=str(raw["accountable_actor_id"]),
                location_ref=str(raw["location_ref"]),
                at_tick=int(raw["at_tick"]),
                condition_ref=None if raw.get("condition_ref") is None else str(raw["condition_ref"]),
            )
        )

    authorization_ids = [row.authorization_id for row in authorizations]
    transfer_ids = [row.transfer_id for row in transfers]
    if len(set(authorization_ids)) != len(authorization_ids):
        raise ValueError("resource checkpoint contains duplicate handoff authorization IDs")
    if len(set(transfer_ids)) != len(transfer_ids):
        raise ValueError("resource checkpoint contains duplicate custody transfer IDs")

    requests_by_id = {row.request_id: row for row in requests.requests}
    authorizations_by_id = {row.authorization_id: row for row in authorizations}
    used_authorizations: set[str] = set()
    for authorization in authorizations:
        request = requests_by_id.get(authorization.request_id)
        if request is None:
            raise ValueError(f"handoff authorization references missing request: {authorization.authorization_id}")
        if authorization.provider_actor_id != request.provider_actor_id:
            raise ValueError(f"handoff authorization provider mismatches request: {authorization.authorization_id}")
        expected_resource = _accepted_resource_id(requests, authorization.request_id) or request.resource_id
        if authorization.resource_id != expected_resource:
            raise ValueError(f"handoff authorization resource mismatches accepted request: {authorization.authorization_id}")
        if authorization.valid_from_tick < request.created_tick:
            raise ValueError(f"handoff authorization predates request: {authorization.authorization_id}")

    for transfer in transfers:
        authorization = authorizations_by_id.get(transfer.authorization_id)
        if authorization is None:
            raise ValueError(f"custody transfer references missing authorization: {transfer.transfer_id}")
        if transfer.authorization_id in used_authorizations:
            raise ValueError(f"multiple custody transfers use one authorization: {transfer.authorization_id}")
        used_authorizations.add(transfer.authorization_id)
        expected = (
            transfer.request_id == authorization.request_id
            and transfer.resource_id == authorization.resource_id
            and transfer.from_actor_id == authorization.provider_actor_id
            and transfer.to_actor_id == authorization.receiving_actor_id
            and transfer.accountable_actor_id == authorization.accountable_actor_id
            and transfer.location_ref == authorization.handoff_location_ref
        )
        if not expected:
            raise ValueError(f"custody transfer mismatches authorization: {transfer.transfer_id}")
        if transfer.at_tick < authorization.valid_from_tick:
            raise ValueError(f"custody transfer predates authorization window: {transfer.transfer_id}")
        if authorization.valid_until_tick is not None and transfer.at_tick >= authorization.valid_until_tick:
            raise ValueError(f"custody transfer occurs after authorization expiry: {transfer.transfer_id}")

    return (
        reservations,
        requests,
        ResourceHandoffLedger(
            authorizations=tuple(sorted(authorizations, key=lambda item: item.authorization_id)),
            transfers=tuple(sorted(transfers, key=lambda item: (item.at_tick, item.transfer_id))),
        ),
    )


def _accepted_resource_id(ledger: ResourceRequestLedger, request_id: str) -> str | None:
    accepted = [
        event for event in ledger.events
        if event.request_id == request_id and event.kind == ResourceRequestEventKind.ACCEPTED
    ]
    if not accepted:
        return None
    event = sorted(accepted, key=lambda item: (item.at_tick, item.event_id))[-1]
    return event.offered_resource_id


def _restore_reservations_requests(
    snapshot: Mapping[str, object],
    *,
    accepted_schemas: set[str] | None = None,
) -> tuple[ReservationLedger, ResourceRequestLedger]:
    accepted_schemas = accepted_schemas or {RESOURCE_CHECKPOINT_SCHEMA}
    if snapshot.get("schema") not in accepted_schemas:
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


def validate_handoff_checkpoint_time(
    handoff_ledger: ResourceHandoffLedger,
    *,
    semantic_minute: int,
) -> None:
    """Future authorization windows are allowed; completed custody transfers are not."""
    for transfer in handoff_ledger.transfers:
        if transfer.at_tick > semantic_minute:
            raise ValueError(f"custody transfer comes from the future: {transfer.transfer_id}")
