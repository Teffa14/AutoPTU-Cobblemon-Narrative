from __future__ import annotations

from dataclasses import dataclass

from tools.global_npc_information_network import DeliveryStatus, InformationEnvelope
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import (
    CoordinatedDecision,
    GlobalNpcWorldEventCoordinator,
    MaterializedDelivery,
)


SUPPORTED_INTENT_KIND = "REQUEST_ASSISTANCE"


@dataclass(frozen=True)
class AssistanceRequestReplanningOutcome:
    action_id: str
    delivery_event_id: str
    requester_id: str
    recipient_id: str
    delivery_status: str
    wake_status: str
    provenance_root: str | None
    decisions: tuple[CoordinatedDecision, ...]


def _validate_request_binding(
    *,
    action_ledger: WorldActionIntentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    action_id: str,
    event_id: str,
) -> tuple[object, InformationEnvelope]:
    action = action_ledger.records.get(action_id)
    if action is None:
        raise KeyError(f"unknown world action intent: {action_id}")
    if action.status != "PLANNED":
        raise ValueError("assistance request replanning requires a PLANNED world action intent")
    if action.intent_kind != SUPPORTED_INTENT_KIND:
        raise ValueError("world action intent is not an assistance request")
    if action.target_ref is None or not action.target_ref:
        raise ValueError("assistance request requires an explicit target")
    if action.target_ref == action.agent_id:
        raise ValueError("assistance request target must be another actor")

    envelope = coordinator.information_queue.envelope_provenance(event_id)
    if envelope is None:
        raise KeyError(f"unknown assistance request delivery event: {event_id}")
    if envelope.sender_id != action.agent_id:
        raise ValueError("assistance request envelope sender does not match deciding actor")
    if envelope.receiver_id != action.target_ref:
        raise ValueError("assistance request envelope receiver does not match selected target")

    sender_ledger = coordinator.information_queue.ledgers.get(envelope.sender_id)
    if sender_ledger is None:
        raise KeyError("assistance request sender has no knowledge ledger")
    source_claim = sender_ledger.claims.get(envelope.source_claim_id)
    if source_claim is None:
        raise KeyError("assistance request source claim is missing")
    if source_claim.provenance_root != action.action_id:
        raise ValueError("assistance request provenance root mismatch")
    if source_claim.subject != f"assistance_request:{action.action_id}":
        raise ValueError("assistance request source claim subject mismatch")
    if source_claim.value != action.intent_id:
        raise ValueError("assistance request source claim intent mismatch")

    return action, envelope


def _target_decisions(
    decisions: tuple[CoordinatedDecision, ...],
    *,
    recipient_id: str,
    event_id: str,
) -> tuple[CoordinatedDecision, ...]:
    trigger_id = f"replan:information:{event_id}"
    return tuple(
        decision
        for decision in decisions
        if decision.agent_id == recipient_id and trigger_id in decision.trigger_ids
    )


def _outcome(
    *,
    action_id: str,
    envelope: InformationEnvelope,
    delivery_status: str,
    wake_status: str,
    provenance_root: object | None,
    decisions: tuple[CoordinatedDecision, ...],
) -> AssistanceRequestReplanningOutcome:
    if delivery_status != DeliveryStatus.DELIVERED.value and decisions:
        raise ValueError("non-delivered assistance request triggered replanning")
    if delivery_status == DeliveryStatus.DELIVERED.value and wake_status == "WAKE_SCHEDULED" and not decisions:
        raise ValueError("delivered assistance request woke recipient without a replanning decision")
    return AssistanceRequestReplanningOutcome(
        action_id=action_id,
        delivery_event_id=envelope.event_id,
        requester_id=envelope.sender_id,
        recipient_id=envelope.receiver_id,
        delivery_status=delivery_status,
        wake_status=wake_status,
        provenance_root=None if provenance_root is None else str(provenance_root),
        decisions=decisions,
    )


def advance_assistance_request_for_replanning(
    *,
    action_ledger: WorldActionIntentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    action_id: str,
    event_id: str,
    semantic_minute: int,
    delivery_budget: int = 1,
    replan_priority: int = 5,
) -> AssistanceRequestReplanningOutcome:
    """Advance one already-dispatched assistance request into selective replanning.

    Delivery grants the selected target an opportunity to reconsider its own
    agenda. This bridge never creates an obligation, reservation, route or
    acceptance on behalf of that actor.
    """

    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")
    if delivery_budget < 0:
        raise ValueError("delivery_budget must be non-negative")

    action, envelope = _validate_request_binding(
        action_ledger=action_ledger,
        coordinator=coordinator,
        action_id=action_id,
        event_id=event_id,
    )

    cycle = coordinator.process_cycle(
        semantic_minute,
        delivery_budget=delivery_budget,
        replan_priority=replan_priority,
    )
    delivery = next(
        (row for row in cycle.deliveries if str(row.get("event_id")) == envelope.event_id),
        None,
    )
    materialized = next(
        (row for row in cycle.materialized if row.event_id == envelope.event_id),
        None,
    )

    if delivery is None:
        status = coordinator.information_queue.statuses.get(envelope.event_id)
        status_value = DeliveryStatus.QUEUED.value if status is None else status.value
        return _outcome(
            action_id=action.action_id,
            envelope=envelope,
            delivery_status=status_value,
            wake_status="NO_DELIVERY_THIS_CYCLE",
            provenance_root=None,
            decisions=(),
        )

    delivery_status = str(delivery.get("status"))
    if str(delivery.get("receiver_id")) != action.target_ref:
        raise ValueError("assistance request delivery receiver mismatch")
    provenance_root = delivery.get("provenance_root")
    if delivery_status == DeliveryStatus.DELIVERED.value:
        if provenance_root != action.action_id:
            raise ValueError("delivered assistance request lost action provenance")
    elif provenance_root is not None:
        raise ValueError("non-delivered assistance request unexpectedly exposes provenance root")

    wake_status = "NO_WAKE_NON_DELIVERY" if materialized is None else materialized.wake_status
    decisions = _target_decisions(
        cycle.decisions,
        recipient_id=action.target_ref,
        event_id=envelope.event_id,
    )
    return _outcome(
        action_id=action.action_id,
        envelope=envelope,
        delivery_status=delivery_status,
        wake_status=wake_status,
        provenance_root=provenance_root,
        decisions=decisions,
    )


def acknowledge_assistance_request_for_replanning(
    *,
    action_ledger: WorldActionIntentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    action_id: str,
    event_id: str,
    semantic_minute: int,
    accepted: bool,
    replan_priority: int = 5,
) -> AssistanceRequestReplanningOutcome:
    """Resolve one local delivery ACK and selectively wake only on acceptance."""

    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")
    action, envelope = _validate_request_binding(
        action_ledger=action_ledger,
        coordinator=coordinator,
        action_id=action_id,
        event_id=event_id,
    )

    delivery = coordinator.information_queue.acknowledge_local_delivery(
        envelope.event_id,
        semantic_minute,
        accepted=accepted,
    )
    if str(delivery.get("receiver_id")) != action.target_ref:
        raise ValueError("assistance request local ACK receiver mismatch")

    status = str(delivery.get("status"))
    provenance_root = delivery.get("provenance_root")
    if status == DeliveryStatus.DELIVERED.value:
        if provenance_root != action.action_id:
            raise ValueError("acknowledged assistance request lost action provenance")
    elif provenance_root is not None:
        raise ValueError("rejected assistance request ACK unexpectedly exposes provenance root")

    materialized: MaterializedDelivery = coordinator.materialize_delivery(
        delivery,
        semantic_minute=semantic_minute,
        replan_priority=replan_priority,
    )
    followup = coordinator.process_cycle(
        semantic_minute,
        delivery_budget=0,
        replan_priority=replan_priority,
    )
    decisions = _target_decisions(
        followup.decisions,
        recipient_id=action.target_ref,
        event_id=envelope.event_id,
    )
    return _outcome(
        action_id=action.action_id,
        envelope=envelope,
        delivery_status=status,
        wake_status=materialized.wake_status,
        provenance_root=provenance_root,
        decisions=decisions,
    )
