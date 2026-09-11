from __future__ import annotations

from dataclasses import dataclass

from tools.autoptu_world_observation_delivery import ScheduledObservationDelivery
from tools.global_npc_information_network import DeliveryStatus
from tools.global_npc_world_event_coordinator import (
    CoordinatedDecision,
    GlobalNpcWorldEventCoordinator,
    MaterializedDelivery,
)


@dataclass(frozen=True)
class ObservationReplanningOutcome:
    observation_transaction_id: str
    delivery_event_id: str
    recipient_id: str
    delivery_status: str
    wake_status: str
    provenance_root: str | None
    decisions: tuple[CoordinatedDecision, ...]


def _validate_scheduled_delivery(
    scheduled: ScheduledObservationDelivery,
    coordinator: GlobalNpcWorldEventCoordinator,
) -> None:
    envelope = scheduled.envelope
    current = coordinator.information_queue.envelope_provenance(envelope.event_id)
    if current is None:
        raise ValueError("scheduled observation delivery has no queue provenance")
    if current != envelope:
        raise ValueError("scheduled observation delivery envelope does not match queue provenance")

    sender_ledger = coordinator.information_queue.ledgers.get(envelope.sender_id)
    if sender_ledger is None:
        raise KeyError("observation delivery sender has no knowledge ledger")
    source_claim = sender_ledger.claims.get(scheduled.source_claim_id)
    if source_claim is None:
        raise KeyError("observation delivery source claim is missing")
    if source_claim.provenance_root != scheduled.observation_transaction_id:
        raise ValueError("observation delivery provenance root mismatch")


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


def advance_observation_delivery_for_replanning(
    scheduled: ScheduledObservationDelivery,
    *,
    coordinator: GlobalNpcWorldEventCoordinator,
    semantic_minute: int,
    delivery_budget: int = 1,
    replan_priority: int = 5,
) -> ObservationReplanningOutcome:
    """Advance one AutoPTU-derived observation through delivery into replanning.

    Only the committed delivery envelope and its provenance identity are used.
    The original AutoPTU result payload is never read by this bridge.
    """

    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")
    if delivery_budget < 0:
        raise ValueError("delivery_budget must be non-negative")
    _validate_scheduled_delivery(scheduled, coordinator)

    envelope = scheduled.envelope
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
        return ObservationReplanningOutcome(
            observation_transaction_id=scheduled.observation_transaction_id,
            delivery_event_id=envelope.event_id,
            recipient_id=envelope.receiver_id,
            delivery_status=status_value,
            wake_status="NO_DELIVERY_THIS_CYCLE",
            provenance_root=None,
            decisions=(),
        )

    delivery_status = str(delivery.get("status"))
    if str(delivery.get("receiver_id")) != envelope.receiver_id:
        raise ValueError("observation delivery receiver mismatch")

    provenance_root = delivery.get("provenance_root")
    if delivery_status == DeliveryStatus.DELIVERED.value:
        if provenance_root != scheduled.observation_transaction_id:
            raise ValueError("delivered observation lost its committed provenance root")
    elif provenance_root is not None:
        raise ValueError("non-delivered observation unexpectedly exposes provenance root")

    wake_status = "NO_WAKE_NON_DELIVERY" if materialized is None else materialized.wake_status
    decisions = _target_decisions(
        cycle.decisions,
        recipient_id=envelope.receiver_id,
        event_id=envelope.event_id,
    )
    if delivery_status != DeliveryStatus.DELIVERED.value and decisions:
        raise ValueError("non-delivered observation triggered replanning")
    if delivery_status == DeliveryStatus.DELIVERED.value and wake_status == "WAKE_SCHEDULED" and not decisions:
        raise ValueError("successful observation delivery woke recipient without a replanning decision")

    return ObservationReplanningOutcome(
        observation_transaction_id=scheduled.observation_transaction_id,
        delivery_event_id=envelope.event_id,
        recipient_id=envelope.receiver_id,
        delivery_status=delivery_status,
        wake_status=wake_status,
        provenance_root=None if provenance_root is None else str(provenance_root),
        decisions=decisions,
    )


def acknowledge_observation_delivery_for_replanning(
    scheduled: ScheduledObservationDelivery,
    *,
    coordinator: GlobalNpcWorldEventCoordinator,
    semantic_minute: int,
    accepted: bool,
    replan_priority: int = 5,
) -> ObservationReplanningOutcome:
    """Resolve a local-projection ACK and selectively replan only after delivery."""

    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")
    _validate_scheduled_delivery(scheduled, coordinator)
    envelope = scheduled.envelope

    delivery = coordinator.information_queue.acknowledge_local_delivery(
        envelope.event_id,
        semantic_minute,
        accepted=accepted,
    )
    if str(delivery.get("receiver_id")) != envelope.receiver_id:
        raise ValueError("observation local ACK receiver mismatch")

    status = str(delivery.get("status"))
    provenance_root = delivery.get("provenance_root")
    if status == DeliveryStatus.DELIVERED.value:
        if provenance_root != scheduled.observation_transaction_id:
            raise ValueError("acknowledged observation lost its committed provenance root")
    elif provenance_root is not None:
        raise ValueError("rejected observation ACK unexpectedly exposes provenance root")

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
        recipient_id=envelope.receiver_id,
        event_id=envelope.event_id,
    )
    if status != DeliveryStatus.DELIVERED.value and decisions:
        raise ValueError("rejected observation ACK triggered replanning")
    if status == DeliveryStatus.DELIVERED.value and materialized.wake_status == "WAKE_SCHEDULED" and not decisions:
        raise ValueError("acknowledged observation woke recipient without a replanning decision")

    return ObservationReplanningOutcome(
        observation_transaction_id=scheduled.observation_transaction_id,
        delivery_event_id=envelope.event_id,
        recipient_id=envelope.receiver_id,
        delivery_status=status,
        wake_status=materialized.wake_status,
        provenance_root=None if provenance_root is None else str(provenance_root),
        decisions=decisions,
    )
