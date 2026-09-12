from __future__ import annotations

import json

from tools.global_npc_assistance_renegotiation_proposal import (
    AssistanceRenegotiationProposalLedger,
)
from tools.global_npc_information_network import InformationEnvelope, InformationEventQueue
from tools.global_npc_memory import Claim, SourceKind


def _proposal_value(proposal) -> str:
    payload = {
        "proposal_id": proposal.proposal_id,
        "supersedes_commitment_id": proposal.supersedes_commitment_id,
        "supersedes_proposal_id": proposal.supersedes_proposal_id,
        "decision_id": proposal.decision_id,
        "decision_reply_event_id": proposal.decision_reply_event_id,
        "requester_id": proposal.requester_id,
        "responder_id": proposal.responder_id,
        "proposed_start_minute": proposal.proposed_start_minute,
        "proposed_end_minute": proposal.proposed_end_minute,
        "location_ref": proposal.location_ref,
        "scope_ref": proposal.scope_ref,
        "alternative_ref": proposal.alternative_ref,
        "expires_minute": proposal.expires_minute,
        "proposal_minute": proposal.semantic_minute,
        "decision_provenance_root": proposal.decision_provenance_root,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def schedule_assistance_renegotiation_proposal(
    *,
    proposal_ledger: AssistanceRenegotiationProposalLedger,
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
    """Send one replacement assistance offer from responder to requester.

    Dispatch transports already-authored terms. It does not accept them, create
    a replacement commitment, mutate the superseded commitment, reserve travel
    or resources, change relationships, or invoke AutoPTU.
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
        raise KeyError(f"unknown assistance renegotiation proposal: {proposal_id}")
    if created_minute < proposal.semantic_minute:
        raise ValueError("replacement offer cannot be authored before its proposal")
    if proposal.expires_minute is not None and created_minute > proposal.expires_minute:
        raise ValueError("expired replacement offer cannot be dispatched")

    sender_ledger = information_queue.ledgers.get(proposal.responder_id)
    receiver_ledger = information_queue.ledgers.get(proposal.requester_id)
    if sender_ledger is None or receiver_ledger is None:
        raise KeyError("replacement-offer sender and requester require knowledge ledgers")
    channel = information_queue.channels.get(channel_id)
    if channel is None:
        raise KeyError(f"unknown communication channel: {channel_id}")

    subject = f"assistance_renegotiation_proposal:{proposal.supersedes_commitment_id}:{proposal.proposal_id}"
    value = _proposal_value(proposal)
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
        raise ValueError("replacement-offer event id reused with conflicting envelope")
    if event_id in information_queue.statuses and existing_envelope is None:
        raise ValueError("replacement-offer event has status without envelope provenance")

    sender_ledger.add(
        Claim(
            claim_id=source_claim_id,
            subject=subject,
            value=value,
            source_kind=SourceKind.AUTHORED_START,
            source_agent_id=proposal.responder_id,
            semantic_minute=created_minute,
            confidence=100,
            provenance_root=proposal.provenance_root,
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
        raise RuntimeError("information queue produced unexpected replacement-offer envelope")
    return envelope
