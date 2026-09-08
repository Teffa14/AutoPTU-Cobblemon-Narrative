from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from tools.global_npc_replanning import NpcReplanQueue, ReplanReason, ReplanTrigger
from tools.global_npc_resource_handoffs import ResourceHandoffAuthorization, ResourceHandoffLedger


class HandoffAttemptOutcome(str, Enum):
    PROVIDER_ABSENT = "PROVIDER_ABSENT"
    RECIPIENT_ABSENT = "RECIPIENT_ABSENT"
    RESOURCE_ABSENT = "RESOURCE_ABSENT"
    PROVIDER_REFUSED = "PROVIDER_REFUSED"
    RECIPIENT_REFUSED = "RECIPIENT_REFUSED"
    LOCATION_BLOCKED = "LOCATION_BLOCKED"


class HandoffAuthorizationState(str, Enum):
    SCHEDULED = "SCHEDULED"
    ACTIVE = "ACTIVE"
    REFUSED = "REFUSED"
    COMPLETED = "COMPLETED"
    EXPIRED = "EXPIRED"


@dataclass(frozen=True)
class ResourceHandoffAttempt:
    attempt_id: str
    authorization_id: str
    actor_id: str
    location_ref: str
    at_tick: int
    outcome: HandoffAttemptOutcome
    observation_ref: str | None = None

    def __post_init__(self) -> None:
        if not self.attempt_id.strip():
            raise ValueError("attempt_id is required")
        if not self.authorization_id.strip():
            raise ValueError("authorization_id is required")
        if not self.actor_id.strip():
            raise ValueError("actor_id is required")
        if not self.location_ref.strip():
            raise ValueError("location_ref is required")
        if self.at_tick < 0:
            raise ValueError("at_tick must be non-negative")


@dataclass(frozen=True)
class ResourceHandoffAttemptLedger:
    attempts: tuple[ResourceHandoffAttempt, ...] = ()


def _authorization_by_id(
    handoff_ledger: ResourceHandoffLedger,
    authorization_id: str,
) -> ResourceHandoffAuthorization | None:
    return next(
        (item for item in handoff_ledger.authorizations if item.authorization_id == authorization_id),
        None,
    )


def record_handoff_attempt(
    ledger: ResourceHandoffAttemptLedger,
    handoff_ledger: ResourceHandoffLedger,
    attempt: ResourceHandoffAttempt,
) -> ResourceHandoffAttemptLedger:
    if any(item.attempt_id == attempt.attempt_id for item in ledger.attempts):
        raise ValueError("duplicate handoff attempt id")

    authorization = _authorization_by_id(handoff_ledger, attempt.authorization_id)
    if authorization is None:
        raise ValueError("unknown handoff authorization")
    if any(item.authorization_id == attempt.authorization_id for item in handoff_ledger.transfers):
        raise ValueError("handoff authorization already completed")
    if attempt.location_ref != authorization.handoff_location_ref:
        raise ValueError("handoff attempt location mismatch")
    if attempt.at_tick < authorization.valid_from_tick:
        raise ValueError("handoff attempt is too early")
    if authorization.valid_until_tick is not None and attempt.at_tick >= authorization.valid_until_tick:
        raise ValueError("handoff authorization expired")

    participants = {
        authorization.provider_actor_id,
        authorization.receiving_actor_id,
        authorization.accountable_actor_id,
    }
    if attempt.actor_id not in participants:
        raise ValueError("handoff attempt actor is not authorized participant")

    if attempt.outcome == HandoffAttemptOutcome.PROVIDER_REFUSED and attempt.actor_id != authorization.provider_actor_id:
        raise ValueError("provider refusal must be recorded by provider")
    if attempt.outcome == HandoffAttemptOutcome.RECIPIENT_REFUSED and attempt.actor_id != authorization.receiving_actor_id:
        raise ValueError("recipient refusal must be recorded by recipient")

    return ResourceHandoffAttemptLedger(
        attempts=tuple(sorted((*ledger.attempts, attempt), key=lambda item: (item.at_tick, item.attempt_id)))
    )


def authorization_state(
    handoff_ledger: ResourceHandoffLedger,
    attempt_ledger: ResourceHandoffAttemptLedger,
    authorization_id: str,
    at_tick: int,
) -> HandoffAuthorizationState | None:
    authorization = _authorization_by_id(handoff_ledger, authorization_id)
    if authorization is None:
        return None
    if any(item.authorization_id == authorization_id for item in handoff_ledger.transfers):
        return HandoffAuthorizationState.COMPLETED
    if any(
        item.authorization_id == authorization_id
        and item.at_tick <= at_tick
        and item.outcome in {HandoffAttemptOutcome.PROVIDER_REFUSED, HandoffAttemptOutcome.RECIPIENT_REFUSED}
        for item in attempt_ledger.attempts
    ):
        return HandoffAuthorizationState.REFUSED
    if at_tick < authorization.valid_from_tick:
        return HandoffAuthorizationState.SCHEDULED
    if authorization.valid_until_tick is not None and at_tick >= authorization.valid_until_tick:
        return HandoffAuthorizationState.EXPIRED
    return HandoffAuthorizationState.ACTIVE


def schedule_handoff_attempt_replans(
    queue: NpcReplanQueue,
    handoff_ledger: ResourceHandoffLedger,
    attempt: ResourceHandoffAttempt,
    *,
    priority: int = 4,
) -> tuple[ReplanTrigger, ...]:
    authorization = _authorization_by_id(handoff_ledger, attempt.authorization_id)
    if authorization is None:
        raise ValueError("unknown handoff authorization")

    actor_ids = sorted(
        {
            authorization.provider_actor_id,
            authorization.receiving_actor_id,
            authorization.accountable_actor_id,
        }
    )
    triggers: list[ReplanTrigger] = []
    for actor_id in actor_ids:
        trigger = ReplanTrigger(
            trigger_id=f"replan:handoff-attempt:{attempt.attempt_id}:{actor_id}",
            agent_id=actor_id,
            reason=ReplanReason.EXTERNAL_EVENT,
            due_minute=attempt.at_tick,
            source_ref=attempt.attempt_id,
            priority=priority,
        )
        queue.schedule(trigger)
        triggers.append(trigger)
    return tuple(triggers)


def attempts_for_authorization(
    ledger: ResourceHandoffAttemptLedger,
    authorization_id: str,
) -> tuple[ResourceHandoffAttempt, ...]:
    return tuple(
        sorted(
            (item for item in ledger.attempts if item.authorization_id == authorization_id),
            key=lambda item: (item.at_tick, item.attempt_id),
        )
    )
