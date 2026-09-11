from __future__ import annotations

from tools.global_npc_information_network import InformationEnvelope, InformationEventQueue
from tools.global_npc_memory import Claim, SourceKind
from tools.global_npc_world_action_intent import WorldActionIntentLedger


SUPPORTED_INTENT_KIND = "REQUEST_ASSISTANCE"


def schedule_assistance_request_from_action(
    *,
    action_ledger: WorldActionIntentLedger,
    information_queue: InformationEventQueue,
    action_id: str,
    event_id: str,
    message_id: str,
    source_claim_id: str,
    receiver_claim_id: str,
    channel_id: str,
    created_minute: int,
    receiver_trust_in_sender: int = 0,
) -> InformationEnvelope:
    """Turn one durable assistance-request intent into one explicit message.

    This seam authors a request claim for the deciding actor and schedules the
    ordinary information envelope to the exact target selected by that action.
    It does not deliver the request, replan the receiver, create an obligation,
    reserve travel, or grant any PTU capability.
    """

    for value, name in (
        (action_id, "action_id"),
        (event_id, "event_id"),
        (message_id, "message_id"),
        (source_claim_id, "source_claim_id"),
        (receiver_claim_id, "receiver_claim_id"),
        (channel_id, "channel_id"),
    ):
        if not value:
            raise ValueError(f"{name} is required")
    if created_minute < 0:
        raise ValueError("created_minute must be non-negative")

    action = action_ledger.records.get(action_id)
    if action is None:
        raise KeyError(f"unknown world action intent: {action_id}")
    if action.status != "PLANNED":
        raise ValueError("assistance request dispatch requires a PLANNED world action intent")
    if action.intent_kind != SUPPORTED_INTENT_KIND:
        raise ValueError("world action intent is not an assistance request")
    if action.target_ref is None or not action.target_ref:
        raise ValueError("assistance request requires an explicit target")
    if action.target_ref == action.agent_id:
        raise ValueError("assistance request target must be another actor")
    if created_minute < action.semantic_minute:
        raise ValueError("assistance request cannot be authored before its world action intent")

    sender_ledger = information_queue.ledgers.get(action.agent_id)
    receiver_ledger = information_queue.ledgers.get(action.target_ref)
    if sender_ledger is None or receiver_ledger is None:
        raise KeyError("request sender and receiver must have knowledge ledgers")
    channel = information_queue.channels.get(channel_id)
    if channel is None:
        raise KeyError(f"unknown communication channel: {channel_id}")

    expected_envelope = InformationEnvelope(
        event_id=event_id,
        message_id=message_id,
        sender_id=action.agent_id,
        receiver_id=action.target_ref,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        delivery_minute=created_minute + channel.latency_minutes,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )

    existing_envelope = information_queue.envelope_provenance(event_id)
    if existing_envelope is not None and existing_envelope != expected_envelope:
        raise ValueError("assistance request event id reused with conflicting envelope")
    if event_id in information_queue.statuses and existing_envelope is None:
        raise ValueError("assistance request event has status without envelope provenance")

    request_claim = Claim(
        claim_id=source_claim_id,
        subject=f"assistance_request:{action.action_id}",
        value=action.intent_id,
        source_kind=SourceKind.AUTHORED_START,
        source_agent_id=action.agent_id,
        semantic_minute=created_minute,
        confidence=100,
        provenance_root=action.action_id,
    )
    sender_ledger.add(request_claim)

    if existing_envelope is not None:
        return existing_envelope

    envelope = information_queue.schedule(
        event_id=event_id,
        message_id=message_id,
        sender_id=action.agent_id,
        receiver_id=action.target_ref,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )
    if envelope != expected_envelope:
        raise RuntimeError("information queue produced unexpected assistance request envelope")
    return envelope
