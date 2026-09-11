from __future__ import annotations

from dataclasses import dataclass

from tools.global_npc_assistance_response_dispatch import SUPPORTED_RESPONSE_KINDS
from tools.global_npc_information_network import DeliveryStatus, InformationEnvelope
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import (
    CoordinatedDecision,
    GlobalNpcWorldEventCoordinator,
    MaterializedDelivery,
)

REQUEST_INTENT_KIND = "REQUEST_ASSISTANCE"


@dataclass(frozen=True)
class AssistanceResponseReplanningOutcome:
    request_action_id: str
    response_action_id: str
    delivery_event_id: str
    responder_id: str
    requester_id: str
    response_kind: str
    delivery_status: str
    wake_status: str
    provenance_root: str | None
    decisions: tuple[CoordinatedDecision, ...]


def _validate_response_binding(
    *,
    action_ledger: WorldActionIntentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    request_action_id: str,
    response_action_id: str,
    event_id: str,
) -> tuple[object, object, InformationEnvelope]:
    request = action_ledger.records.get(request_action_id)
    if request is None:
        raise KeyError(f"unknown assistance request action: {request_action_id}")
    if request.status != "PLANNED" or request.intent_kind != REQUEST_INTENT_KIND:
        raise ValueError("referenced action is not a PLANNED assistance request")
    if request.target_ref is None or not request.target_ref:
        raise ValueError("assistance request requires an explicit recipient")

    response = action_ledger.records.get(response_action_id)
    if response is None:
        raise KeyError(f"unknown assistance response action: {response_action_id}")
    if response.status != "PLANNED":
        raise ValueError("assistance response replanning requires a PLANNED response")
    if response.intent_kind not in SUPPORTED_RESPONSE_KINDS:
        raise ValueError("world action intent is not a supported assistance response")
    if response.agent_id != request.target_ref:
        raise ValueError("assistance response sender is not the original request recipient")
    if response.target_ref != request.agent_id:
        raise ValueError("assistance response target is not the original requester")
    if response.semantic_minute < request.semantic_minute:
        raise ValueError("assistance response cannot predate its request")

    envelope = coordinator.information_queue.envelope_provenance(event_id)
    if envelope is None:
        raise KeyError(f"unknown assistance response delivery event: {event_id}")
    if envelope.sender_id != response.agent_id:
        raise ValueError("assistance response envelope sender mismatch")
    if envelope.receiver_id != request.agent_id:
        raise ValueError("assistance response envelope receiver mismatch")

    sender_ledger = coordinator.information_queue.ledgers.get(response.agent_id)
    if sender_ledger is None:
        raise KeyError("assistance response sender has no knowledge ledger")
    source_claim = sender_ledger.claims.get(envelope.source_claim_id)
    if source_claim is None:
        raise KeyError("assistance response source claim is missing")
    if source_claim.provenance_root != response.action_id:
        raise ValueError("assistance response provenance root mismatch")
    if source_claim.subject != f"assistance_response:{request.action_id}:{response.action_id}":
        raise ValueError("assistance response source claim subject mismatch")
    if source_claim.value != response.intent_kind:
        raise ValueError("assistance response source claim value mismatch")

    return request, response, envelope


def _requester_decisions(
    decisions: tuple[CoordinatedDecision, ...],
    *,
    requester_id: str,
    event_id: str,
) -> tuple[CoordinatedDecision, ...]:
    trigger_id = f"replan:information:{event_id}"
    return tuple(
        decision
        for decision in decisions
        if decision.agent_id == requester_id and trigger_id in decision.trigger_ids
    )


def _outcome(
    *,
    request: object,
    response: object,
    envelope: InformationEnvelope,
    delivery_status: str,
    wake_status: str,
    provenance_root: object | None,
    decisions: tuple[CoordinatedDecision, ...],
) -> AssistanceResponseReplanningOutcome:
    if delivery_status != DeliveryStatus.DELIVERED.value and decisions:
        raise ValueError("non-delivered assistance response triggered replanning")
    if delivery_status == DeliveryStatus.DELIVERED.value and wake_status == "WAKE_SCHEDULED" and not decisions:
        raise ValueError("delivered assistance response woke requester without a replanning decision")
    return AssistanceResponseReplanningOutcome(
        request_action_id=request.action_id,
        response_action_id=response.action_id,
        delivery_event_id=envelope.event_id,
        responder_id=envelope.sender_id,
        requester_id=envelope.receiver_id,
        response_kind=response.intent_kind,
        delivery_status=delivery_status,
        wake_status=wake_status,
        provenance_root=None if provenance_root is None else str(provenance_root),
        decisions=decisions,
    )


def advance_assistance_response_for_replanning(
    *,
    action_ledger: WorldActionIntentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    request_action_id: str,
    response_action_id: str,
    event_id: str,
    semantic_minute: int,
    delivery_budget: int = 1,
    replan_priority: int = 5,
) -> AssistanceResponseReplanningOutcome:
    """Advance one dispatched assistance response into requester-only replanning.

    A delivered response changes what the requester knows. It does not itself
    reserve time, create a commitment, start travel, alter a relationship or
    execute the responder's proposed assistance.
    """
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")
    if delivery_budget < 0:
        raise ValueError("delivery_budget must be non-negative")

    request, response, envelope = _validate_response_binding(
        action_ledger=action_ledger,
        coordinator=coordinator,
        request_action_id=request_action_id,
        response_action_id=response_action_id,
        event_id=event_id,
    )
    cycle = coordinator.process_cycle(
        semantic_minute,
        delivery_budget=delivery_budget,
        replan_priority=replan_priority,
    )
    delivery = next((row for row in cycle.deliveries if str(row.get("event_id")) == event_id), None)
    materialized = next((row for row in cycle.materialized if row.event_id == event_id), None)

    if delivery is None:
        status = coordinator.information_queue.statuses.get(event_id)
        status_value = DeliveryStatus.QUEUED.value if status is None else status.value
        return _outcome(
            request=request,
            response=response,
            envelope=envelope,
            delivery_status=status_value,
            wake_status="NO_DELIVERY_THIS_CYCLE",
            provenance_root=None,
            decisions=(),
        )

    delivery_status = str(delivery.get("status"))
    if str(delivery.get("receiver_id")) != request.agent_id:
        raise ValueError("assistance response delivery receiver mismatch")
    provenance_root = delivery.get("provenance_root")
    if delivery_status == DeliveryStatus.DELIVERED.value:
        if provenance_root != response.action_id:
            raise ValueError("delivered assistance response lost response provenance")
    elif provenance_root is not None:
        raise ValueError("non-delivered assistance response unexpectedly exposes provenance root")

    wake_status = "NO_WAKE_NON_DELIVERY" if materialized is None else materialized.wake_status
    decisions = _requester_decisions(cycle.decisions, requester_id=request.agent_id, event_id=event_id)
    return _outcome(
        request=request,
        response=response,
        envelope=envelope,
        delivery_status=delivery_status,
        wake_status=wake_status,
        provenance_root=provenance_root,
        decisions=decisions,
    )


def acknowledge_assistance_response_for_replanning(
    *,
    action_ledger: WorldActionIntentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    request_action_id: str,
    response_action_id: str,
    event_id: str,
    semantic_minute: int,
    accepted: bool,
    replan_priority: int = 5,
) -> AssistanceResponseReplanningOutcome:
    """Resolve one local response-delivery ACK and wake only the requester on acceptance."""
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")

    request, response, envelope = _validate_response_binding(
        action_ledger=action_ledger,
        coordinator=coordinator,
        request_action_id=request_action_id,
        response_action_id=response_action_id,
        event_id=event_id,
    )
    delivery = coordinator.information_queue.acknowledge_local_delivery(
        event_id,
        semantic_minute,
        accepted=accepted,
    )
    if str(delivery.get("receiver_id")) != request.agent_id:
        raise ValueError("assistance response local ACK receiver mismatch")

    status = str(delivery.get("status"))
    provenance_root = delivery.get("provenance_root")
    if status == DeliveryStatus.DELIVERED.value:
        if provenance_root != response.action_id:
            raise ValueError("acknowledged assistance response lost response provenance")
    elif provenance_root is not None:
        raise ValueError("rejected assistance response ACK unexpectedly exposes provenance root")

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
    decisions = _requester_decisions(
        followup.decisions,
        requester_id=request.agent_id,
        event_id=event_id,
    )
    return _outcome(
        request=request,
        response=response,
        envelope=envelope,
        delivery_status=status,
        wake_status=materialized.wake_status,
        provenance_root=provenance_root,
        decisions=decisions,
    )
