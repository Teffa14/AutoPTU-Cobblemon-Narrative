from __future__ import annotations

from dataclasses import dataclass

from tools.global_npc_ai import Handoff
from tools.global_npc_information_network import DeliveryStatus
from tools.global_npc_world_action_intent import (
    WorldActionIntentLedger,
    WorldActionIntentRecord,
)
from tools.global_npc_world_event_coordinator import (
    CoordinatedDecision,
    GlobalNpcWorldEventCoordinator,
)


REQUEST_INTENT_KIND = "REQUEST_ASSISTANCE"
SUPPORTED_RESPONSE_KINDS = frozenset(
    {
        "ACCEPT_ASSISTANCE_REQUEST",
        "DEFER_ASSISTANCE_REQUEST",
        "REJECT_ASSISTANCE_REQUEST",
        "COUNTERPROPOSE_ASSISTANCE_REQUEST",
    }
)


@dataclass(frozen=True)
class AssistanceResponseOutcome:
    request_action_id: str
    request_event_id: str
    response_action_id: str
    requester_id: str
    responder_id: str
    response_kind: str
    response_intent_id: str
    semantic_minute: int
    trigger_ids: tuple[str, ...]
    record: WorldActionIntentRecord


def _validate_delivered_request(
    *,
    action_ledger: WorldActionIntentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    request_action_id: str,
    request_event_id: str,
):
    request = action_ledger.records.get(request_action_id)
    if request is None:
        raise KeyError(f"unknown assistance request action: {request_action_id}")
    if request.status != "PLANNED":
        raise ValueError("assistance request must remain a PLANNED world action intent")
    if request.intent_kind != REQUEST_INTENT_KIND:
        raise ValueError("referenced world action is not an assistance request")
    if request.target_ref is None or not request.target_ref:
        raise ValueError("assistance request requires an explicit recipient")
    if request.target_ref == request.agent_id:
        raise ValueError("assistance request recipient must be another actor")

    envelope = coordinator.information_queue.envelope_provenance(request_event_id)
    if envelope is None:
        raise KeyError(f"unknown assistance request delivery event: {request_event_id}")
    if envelope.sender_id != request.agent_id:
        raise ValueError("assistance request sender does not match requester")
    if envelope.receiver_id != request.target_ref:
        raise ValueError("assistance request receiver does not match selected recipient")

    status = coordinator.information_queue.statuses.get(request_event_id)
    if status != DeliveryStatus.DELIVERED:
        raise ValueError("assistance response requires a terminal DELIVERED request")

    sender_ledger = coordinator.information_queue.ledgers.get(request.agent_id)
    if sender_ledger is None:
        raise KeyError("assistance requester has no knowledge ledger")
    source_claim = sender_ledger.claims.get(envelope.source_claim_id)
    if source_claim is None:
        raise KeyError("assistance request source claim is missing")
    if source_claim.provenance_root != request.action_id:
        raise ValueError("assistance request source provenance mismatch")
    if source_claim.subject != f"assistance_request:{request.action_id}":
        raise ValueError("assistance request source subject mismatch")
    if source_claim.value != request.intent_id:
        raise ValueError("assistance request source intent mismatch")

    receiver_ledger = coordinator.information_queue.ledgers.get(request.target_ref)
    if receiver_ledger is None:
        raise KeyError("assistance recipient has no knowledge ledger")
    received_claim = receiver_ledger.claims.get(envelope.new_claim_id)
    if received_claim is None:
        raise ValueError("DELIVERED assistance request lacks the recipient claim")
    if received_claim.provenance_root != request.action_id:
        raise ValueError("assistance recipient claim lost request provenance")

    return request, envelope


def record_assistance_response_from_replan(
    *,
    action_ledger: WorldActionIntentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    request_action_id: str,
    request_event_id: str,
    response_action_id: str,
    coordinated_decision: CoordinatedDecision,
    semantic_minute: int,
) -> AssistanceResponseOutcome:
    """Record the recipient's own response after an assistance request is delivered.

    This owner records choice only. It does not create a commitment, schedule
    travel, mutate the requester, dispatch the reply, or resolve PTU mechanics.
    """

    if not response_action_id:
        raise ValueError("response_action_id is required")
    if response_action_id == request_action_id:
        raise ValueError("response action must have its own identity")
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")

    request, envelope = _validate_delivered_request(
        action_ledger=action_ledger,
        coordinator=coordinator,
        request_action_id=request_action_id,
        request_event_id=request_event_id,
    )
    if semantic_minute < request.semantic_minute:
        raise ValueError("assistance response cannot predate the request decision")

    expected_trigger = f"replan:information:{envelope.event_id}"
    if coordinated_decision.agent_id != request.target_ref:
        raise ValueError("assistance response actor is not the delivered recipient")
    if expected_trigger not in coordinated_decision.trigger_ids:
        raise ValueError("assistance response lacks the request-delivery replan trigger")

    decision = coordinated_decision.decision.decision
    if decision.agent_id != request.target_ref:
        raise ValueError("assistance response decision identity mismatch")
    if decision.intent_id is None or not decision.intent_id:
        raise ValueError("assistance response requires a selected response intent")
    if decision.kind not in SUPPORTED_RESPONSE_KINDS:
        raise ValueError("unsupported assistance response kind")
    if decision.handoff != Handoff.NONE:
        raise ValueError("assistance response choice cannot itself be an AutoPTU handoff")
    if decision.target_ref != request.agent_id:
        raise ValueError("assistance response must target the original requester")

    record = action_ledger.record_from_replan(
        action_id=response_action_id,
        coordinated_decision=coordinated_decision,
        semantic_minute=semantic_minute,
    )
    return AssistanceResponseOutcome(
        request_action_id=request.action_id,
        request_event_id=envelope.event_id,
        response_action_id=record.action_id,
        requester_id=request.agent_id,
        responder_id=record.agent_id,
        response_kind=record.intent_kind,
        response_intent_id=record.intent_id,
        semantic_minute=record.semantic_minute,
        trigger_ids=record.trigger_ids,
        record=record,
    )
