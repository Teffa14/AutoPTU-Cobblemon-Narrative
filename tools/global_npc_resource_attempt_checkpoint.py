from __future__ import annotations

from typing import Mapping

from tools.global_npc_resource_checkpoint import (
    RESOURCE_CHECKPOINT_HANDOFF_SCHEMA,
    RESOURCE_CHECKPOINT_SCHEMA,
    restore_resource_state_with_handoffs,
    snapshot_resource_state_with_handoffs,
)
from tools.global_npc_resource_handoff_attempts import (
    HandoffAttemptOutcome,
    ResourceHandoffAttempt,
    ResourceHandoffAttemptLedger,
)
from tools.global_npc_resource_handoffs import ResourceHandoffAuthorization, ResourceHandoffLedger
from tools.global_npc_resource_requests import ResourceRequestLedger
from tools.global_npc_resource_reservations import ReservationLedger


RESOURCE_CHECKPOINT_ATTEMPT_SCHEMA = "OUROS_NPC_RESOURCE_CHECKPOINT_V3"


def snapshot_resource_state_with_attempts(
    reservation_ledger: ReservationLedger,
    request_ledger: ResourceRequestLedger,
    handoff_ledger: ResourceHandoffLedger,
    attempt_ledger: ResourceHandoffAttemptLedger,
) -> dict:
    """Serialize Pass 339/342/343 state plus Pass 344 failed handoff history."""
    snapshot = snapshot_resource_state_with_handoffs(reservation_ledger, request_ledger, handoff_ledger)
    snapshot["schema"] = RESOURCE_CHECKPOINT_ATTEMPT_SCHEMA
    snapshot["handoff_attempts"] = [
        {
            "attempt_id": row.attempt_id,
            "authorization_id": row.authorization_id,
            "actor_id": row.actor_id,
            "location_ref": row.location_ref,
            "at_tick": row.at_tick,
            "outcome": row.outcome.value,
            "observation_ref": row.observation_ref,
        }
        for row in sorted(attempt_ledger.attempts, key=lambda item: (item.at_tick, item.attempt_id))
    ]
    return snapshot


def restore_resource_state_with_attempts(
    snapshot: Mapping[str, object],
) -> tuple[ReservationLedger, ResourceRequestLedger, ResourceHandoffLedger, ResourceHandoffAttemptLedger]:
    """Restore V3 failed-attempt history; older checkpoints get no invented attempts."""
    schema = snapshot.get("schema")
    if schema in {RESOURCE_CHECKPOINT_SCHEMA, RESOURCE_CHECKPOINT_HANDOFF_SCHEMA}:
        reservations, requests, handoffs = restore_resource_state_with_handoffs(snapshot)
        return reservations, requests, handoffs, ResourceHandoffAttemptLedger()
    if schema != RESOURCE_CHECKPOINT_ATTEMPT_SCHEMA:
        raise ValueError("unsupported resource attempt checkpoint schema")

    base_snapshot = dict(snapshot)
    base_snapshot["schema"] = RESOURCE_CHECKPOINT_HANDOFF_SCHEMA
    base_snapshot.pop("handoff_attempts", None)
    reservations, requests, handoffs = restore_resource_state_with_handoffs(base_snapshot)

    raw_attempts = snapshot.get("handoff_attempts", [])
    if not isinstance(raw_attempts, list):
        raise ValueError("handoff attempt checkpoint collection must be a list")

    attempts: list[ResourceHandoffAttempt] = []
    for raw in raw_attempts:
        if not isinstance(raw, Mapping):
            raise ValueError("handoff attempt checkpoint row must be a mapping")
        attempts.append(
            ResourceHandoffAttempt(
                attempt_id=str(raw["attempt_id"]),
                authorization_id=str(raw["authorization_id"]),
                actor_id=str(raw["actor_id"]),
                location_ref=str(raw["location_ref"]),
                at_tick=int(raw["at_tick"]),
                outcome=HandoffAttemptOutcome(str(raw["outcome"])),
                observation_ref=None if raw.get("observation_ref") is None else str(raw["observation_ref"]),
            )
        )

    attempt_ids = [row.attempt_id for row in attempts]
    if len(set(attempt_ids)) != len(attempt_ids):
        raise ValueError("resource checkpoint contains duplicate handoff attempt IDs")

    authorizations_by_id = {row.authorization_id: row for row in handoffs.authorizations}
    transfers_by_authorization = {row.authorization_id: row for row in handoffs.transfers}
    for attempt in attempts:
        authorization = authorizations_by_id.get(attempt.authorization_id)
        if authorization is None:
            raise ValueError(f"handoff attempt references missing authorization: {attempt.attempt_id}")
        _validate_attempt_against_authorization(attempt, authorization)

        transfer = transfers_by_authorization.get(attempt.authorization_id)
        if transfer is not None and attempt.at_tick > transfer.at_tick:
            raise ValueError(f"handoff attempt occurs after completed transfer: {attempt.attempt_id}")
        if (
            transfer is not None
            and attempt.at_tick <= transfer.at_tick
            and attempt.outcome in {HandoffAttemptOutcome.PROVIDER_REFUSED, HandoffAttemptOutcome.RECIPIENT_REFUSED}
        ):
            raise ValueError(f"custody transfer follows terminal refusal: {attempt.attempt_id}")

    return (
        reservations,
        requests,
        handoffs,
        ResourceHandoffAttemptLedger(
            attempts=tuple(sorted(attempts, key=lambda item: (item.at_tick, item.attempt_id)))
        ),
    )


def _validate_attempt_against_authorization(
    attempt: ResourceHandoffAttempt,
    authorization: ResourceHandoffAuthorization,
) -> None:
    if attempt.location_ref != authorization.handoff_location_ref:
        raise ValueError(f"handoff attempt location mismatches authorization: {attempt.attempt_id}")
    if attempt.at_tick < authorization.valid_from_tick:
        raise ValueError(f"handoff attempt predates authorization window: {attempt.attempt_id}")
    if authorization.valid_until_tick is not None and attempt.at_tick >= authorization.valid_until_tick:
        raise ValueError(f"handoff attempt occurs after authorization expiry: {attempt.attempt_id}")

    participants = {
        authorization.provider_actor_id,
        authorization.receiving_actor_id,
        authorization.accountable_actor_id,
    }
    if attempt.actor_id not in participants:
        raise ValueError(f"handoff attempt actor is not an authorized participant: {attempt.attempt_id}")
    if attempt.outcome == HandoffAttemptOutcome.PROVIDER_REFUSED and attempt.actor_id != authorization.provider_actor_id:
        raise ValueError(f"provider refusal attributed to wrong actor: {attempt.attempt_id}")
    if attempt.outcome == HandoffAttemptOutcome.RECIPIENT_REFUSED and attempt.actor_id != authorization.receiving_actor_id:
        raise ValueError(f"recipient refusal attributed to wrong actor: {attempt.attempt_id}")


def validate_attempt_checkpoint_time(
    attempt_ledger: ResourceHandoffAttemptLedger,
    *,
    semantic_minute: int,
) -> None:
    """Attempts are completed observations and cannot originate in the future."""
    for attempt in attempt_ledger.attempts:
        if attempt.at_tick > semantic_minute:
            raise ValueError(f"handoff attempt comes from the future: {attempt.attempt_id}")
