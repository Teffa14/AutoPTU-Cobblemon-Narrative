from __future__ import annotations

from tools.global_npc_information_network import InformationEnvelope, InformationEventQueue
from tools.global_npc_memory import Claim, SourceKind
from tools.global_npc_world_action_intent import WorldActionIntentLedger

REQUEST_INTENT_KIND = "REQUEST_ASSISTANCE"
SUPPORTED_RESPONSE_KINDS = frozenset({"ACCEPT_ASSISTANCE_REQUEST", "DEFER_ASSISTANCE_REQUEST", "REJECT_ASSISTANCE_REQUEST", "COUNTERPROPOSE_ASSISTANCE_REQUEST"})


def schedule_assistance_response_from_action(
    *, action_ledger: WorldActionIntentLedger, information_queue: InformationEventQueue,
    request_action_id: str, response_action_id: str, event_id: str, message_id: str,
    source_claim_id: str, receiver_claim_id: str, channel_id: str, created_minute: int,
    receiver_trust_in_sender: int = 0,
) -> InformationEnvelope:
    """Schedule one durable recipient-owned assistance response back to its requester."""
    for value, name in ((request_action_id, "request_action_id"), (response_action_id, "response_action_id"), (event_id, "event_id"), (message_id, "message_id"), (source_claim_id, "source_claim_id"), (receiver_claim_id, "receiver_claim_id"), (channel_id, "channel_id")):
        if not value:
            raise ValueError(f"{name} is required")
    if created_minute < 0:
        raise ValueError("created_minute must be non-negative")
    if response_action_id == request_action_id:
        raise ValueError("response action must have its own identity")

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
        raise ValueError("assistance response dispatch requires a PLANNED response")
    if response.intent_kind not in SUPPORTED_RESPONSE_KINDS:
        raise ValueError("world action intent is not a supported assistance response")
    if response.agent_id != request.target_ref:
        raise ValueError("assistance response sender is not the original request recipient")
    if response.target_ref != request.agent_id:
        raise ValueError("assistance response target is not the original requester")
    if response.semantic_minute < request.semantic_minute:
        raise ValueError("assistance response cannot predate its request")
    if created_minute < response.semantic_minute:
        raise ValueError("assistance response cannot be authored before its world action intent")

    sender_ledger = information_queue.ledgers.get(response.agent_id)
    receiver_ledger = information_queue.ledgers.get(request.agent_id)
    if sender_ledger is None or receiver_ledger is None:
        raise KeyError("response sender and requester must have knowledge ledgers")
    channel = information_queue.channels.get(channel_id)
    if channel is None:
        raise KeyError(f"unknown communication channel: {channel_id}")

    expected_envelope = InformationEnvelope(event_id=event_id, message_id=message_id, sender_id=response.agent_id, receiver_id=request.agent_id, source_claim_id=source_claim_id, new_claim_id=receiver_claim_id, channel_id=channel_id, created_minute=created_minute, delivery_minute=created_minute + channel.latency_minutes, receiver_trust_in_sender=receiver_trust_in_sender)
    existing_envelope = information_queue.envelope_provenance(event_id)
    if existing_envelope is not None and existing_envelope != expected_envelope:
        raise ValueError("assistance response event id reused with conflicting envelope")
    if event_id in information_queue.statuses and existing_envelope is None:
        raise ValueError("assistance response event has status without envelope provenance")

    sender_ledger.add(Claim(claim_id=source_claim_id, subject=f"assistance_response:{request.action_id}:{response.action_id}", value=response.intent_kind, source_kind=SourceKind.AUTHORED_START, source_agent_id=response.agent_id, semantic_minute=created_minute, confidence=100, provenance_root=response.action_id))
    if existing_envelope is not None:
        return existing_envelope

    envelope = information_queue.schedule(event_id=event_id, message_id=message_id, sender_id=response.agent_id, receiver_id=request.agent_id, source_claim_id=source_claim_id, new_claim_id=receiver_claim_id, channel_id=channel_id, created_minute=created_minute, receiver_trust_in_sender=receiver_trust_in_sender)
    if envelope != expected_envelope:
        raise RuntimeError("information queue produced unexpected assistance response envelope")
    return envelope
