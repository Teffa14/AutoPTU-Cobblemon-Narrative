from __future__ import annotations

import json

from tools.global_npc_assistance_counterproposal import AssistanceCounterproposalLedger
from tools.global_npc_information_network import InformationEnvelope, InformationEventQueue
from tools.global_npc_memory import Claim, SourceKind
from tools.global_npc_world_action_intent import WorldActionIntentLedger

REQUEST_KIND = "REQUEST_ASSISTANCE"
COUNTERPROPOSE_KIND = "COUNTERPROPOSE_ASSISTANCE_REQUEST"


def _terms_value(record) -> str:
    """Encode authored terms deterministically for the existing string Claim contract."""
    payload = {
        "proposal_id": record.proposal_id,
        "request_action_id": record.request_action_id,
        "response_action_id": record.response_action_id,
        "proposed_start_minute": record.proposed_start_minute,
        "proposed_end_minute": record.proposed_end_minute,
        "location_ref": record.location_ref,
        "scope_ref": record.scope_ref,
        "alternative_ref": record.alternative_ref,
        "expires_minute": record.expires_minute,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def schedule_assistance_counterproposal_terms(
    *,
    action_ledger: WorldActionIntentLedger,
    proposal_ledger: AssistanceCounterproposalLedger,
    information_queue: InformationEventQueue,
    proposal_id: str,
    event_id: str,
    message_id: str,
    source_claim_id: str,
    receiver_claim_id: str,
    channel_id: str,
    created_minute: int,
    receiver_trust_in_sender: int = 0,
) -> InformationEnvelope:
    """Send one responder-authored counterproposal payload to its requester.

    Persistence of terms and receipt of terms are separate facts. This function
    authors an explicit information claim and schedules it through the ordinary
    information queue. It does not accept the terms, create a commitment,
    reserve time or travel, allocate resources, mutate relationships, or invoke
    AutoPTU.
    """
    for value, name in (
        (proposal_id, "proposal_id"),
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

    proposal = proposal_ledger.records.get(proposal_id)
    if proposal is None:
        raise KeyError(f"unknown assistance counterproposal: {proposal_id}")
    if proposal.provenance_root != proposal.response_action_id:
        raise ValueError("counterproposal provenance must match its response action")

    request = action_ledger.records.get(proposal.request_action_id)
    if request is None:
        raise KeyError(f"unknown assistance request action: {proposal.request_action_id}")
    if request.status != "PLANNED" or request.intent_kind != REQUEST_KIND:
        raise ValueError("counterproposal references a non-assistance request")
    if request.agent_id != proposal.requester_id or request.target_ref != proposal.responder_id:
        raise ValueError("counterproposal request actor binding mismatch")

    response = action_ledger.records.get(proposal.response_action_id)
    if response is None:
        raise KeyError(f"unknown assistance response action: {proposal.response_action_id}")
    if response.status != "PLANNED" or response.intent_kind != COUNTERPROPOSE_KIND:
        raise ValueError("counterproposal terms require a PLANNED counterproposal response")
    if response.agent_id != proposal.responder_id or response.target_ref != proposal.requester_id:
        raise ValueError("counterproposal response actor binding mismatch")
    if response.semantic_minute < request.semantic_minute:
        raise ValueError("counterproposal response cannot predate its request")
    if created_minute < response.semantic_minute:
        raise ValueError("counterproposal terms cannot be authored before the response")

    sender_ledger = information_queue.ledgers.get(proposal.responder_id)
    receiver_ledger = information_queue.ledgers.get(proposal.requester_id)
    if sender_ledger is None or receiver_ledger is None:
        raise KeyError("counterproposal sender and requester must have knowledge ledgers")
    channel = information_queue.channels.get(channel_id)
    if channel is None:
        raise KeyError(f"unknown communication channel: {channel_id}")

    subject = f"assistance_counterproposal_terms:{proposal.request_action_id}:{proposal.response_action_id}:{proposal.proposal_id}"
    value = _terms_value(proposal)
    expected_envelope = InformationEnvelope(
        event_id=event_id,
        message_id=message_id,
        sender_id=proposal.responder_id,
        receiver_id=proposal.requester_id,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        delivery_minute=created_minute + channel.latency_minutes,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )

    existing_envelope = information_queue.envelope_provenance(event_id)
    if existing_envelope is not None and existing_envelope != expected_envelope:
        raise ValueError("counterproposal terms event id reused with conflicting envelope")
    if event_id in information_queue.statuses and existing_envelope is None:
        raise ValueError("counterproposal terms event has status without envelope provenance")

    sender_ledger.add(
        Claim(
            claim_id=source_claim_id,
            subject=subject,
            value=value,
            source_kind=SourceKind.AUTHORED_START,
            source_agent_id=proposal.responder_id,
            semantic_minute=created_minute,
            confidence=100,
            provenance_root=proposal.response_action_id,
        )
    )
    if existing_envelope is not None:
        return existing_envelope

    envelope = information_queue.schedule(
        event_id=event_id,
        message_id=message_id,
        sender_id=proposal.responder_id,
        receiver_id=proposal.requester_id,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )
    if envelope != expected_envelope:
        raise RuntimeError("information queue produced unexpected counterproposal terms envelope")
    return envelope
