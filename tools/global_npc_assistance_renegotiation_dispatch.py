from __future__ import annotations

import json

from tools.global_npc_assistance_commitment_disposition import (
    AssistanceCommitmentDispositionLedger,
    CommitmentStartDisposition,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
)
from tools.global_npc_information_network import InformationEnvelope, InformationEventQueue
from tools.global_npc_memory import Claim, SourceKind


def _request_value(commitment, disposition) -> str:
    payload = {
        "commitment_id": commitment.commitment_id,
        "proposal_id": commitment.proposal_id,
        "assessment_id": disposition.assessment_id,
        "disposition_id": disposition.disposition_id,
        "rationale_ref": disposition.rationale_ref,
        "accepted_start_minute": commitment.start_minute,
        "accepted_end_minute": commitment.end_minute,
        "location_ref": commitment.location_ref,
        "scope_ref": commitment.scope_ref,
        "alternative_ref": commitment.alternative_ref,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def schedule_assistance_renegotiation_request(
    *,
    commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    disposition_ledger: AssistanceCommitmentDispositionLedger,
    information_queue: InformationEventQueue,
    disposition_id: str,
    event_id: str,
    message_id: str,
    source_claim_id: str,
    receiver_claim_id: str,
    channel_id: str,
    created_minute: int,
    receiver_trust_in_sender: int = 0,
) -> InformationEnvelope:
    """Send one explicit renegotiation request from responder to requester.

    The message reports that the responder wants to reopen the accepted terms.
    It does not create replacement terms, mutate the original commitment,
    reserve travel or resources, alter relationships, or invoke AutoPTU.
    """
    for value, name in (
        (disposition_id, "disposition_id"),
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

    disposition = disposition_ledger.records.get(disposition_id)
    if disposition is None:
        raise KeyError(f"unknown assistance commitment disposition: {disposition_id}")
    if disposition.disposition != CommitmentStartDisposition.REQUEST_RENEGOTIATION.value:
        raise ValueError("renegotiation dispatch requires REQUEST_RENEGOTIATION disposition")

    commitment = commitment_ledger.records.get(disposition.commitment_id)
    if commitment is None:
        raise KeyError(f"unknown negotiated assistance commitment: {disposition.commitment_id}")
    if disposition.proposal_id != commitment.proposal_id:
        raise ValueError("renegotiation disposition proposal binding mismatch")
    if disposition.requester_id != commitment.requester_id or disposition.responder_id != commitment.responder_id:
        raise ValueError("renegotiation disposition actor binding mismatch")
    if disposition.actor_id != commitment.responder_id:
        raise ValueError("renegotiation disposition must belong to the commitment responder")
    if disposition.semantic_minute < commitment.start_minute or disposition.semantic_minute > commitment.end_minute:
        raise ValueError("renegotiation disposition falls outside accepted assistance window")
    if created_minute < disposition.semantic_minute:
        raise ValueError("renegotiation request cannot be authored before its disposition")

    sender_ledger = information_queue.ledgers.get(commitment.responder_id)
    receiver_ledger = information_queue.ledgers.get(commitment.requester_id)
    if sender_ledger is None or receiver_ledger is None:
        raise KeyError("renegotiation sender and requester must have knowledge ledgers")
    channel = information_queue.channels.get(channel_id)
    if channel is None:
        raise KeyError(f"unknown communication channel: {channel_id}")

    subject = f"assistance_renegotiation_request:{commitment.commitment_id}:{disposition.disposition_id}"
    value = _request_value(commitment, disposition)
    expected_envelope = InformationEnvelope(
        event_id=event_id,
        message_id=message_id,
        sender_id=commitment.responder_id,
        receiver_id=commitment.requester_id,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        delivery_minute=created_minute + channel.latency_minutes,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )

    existing_envelope = information_queue.envelope_provenance(event_id)
    if existing_envelope is not None and existing_envelope != expected_envelope:
        raise ValueError("renegotiation event id reused with conflicting envelope")
    if event_id in information_queue.statuses and existing_envelope is None:
        raise ValueError("renegotiation event has status without envelope provenance")

    sender_ledger.add(
        Claim(
            claim_id=source_claim_id,
            subject=subject,
            value=value,
            source_kind=SourceKind.AUTHORED_START,
            source_agent_id=commitment.responder_id,
            semantic_minute=created_minute,
            confidence=100,
            provenance_root=disposition.provenance_root,
        )
    )
    if existing_envelope is not None:
        return existing_envelope

    envelope = information_queue.schedule(
        event_id=event_id,
        message_id=message_id,
        sender_id=commitment.responder_id,
        receiver_id=commitment.requester_id,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )
    if envelope != expected_envelope:
        raise RuntimeError("information queue produced unexpected renegotiation envelope")
    return envelope
