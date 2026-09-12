from __future__ import annotations

import json

from tools.global_npc_assistance_commitment_disposition import AssistanceCommitmentDispositionLedger
from tools.global_npc_assistance_counterproposal_commitment import AssistanceCounterproposalCommitmentLedger
from tools.global_npc_assistance_renegotiation_decision import AssistanceRenegotiationDecisionLedger
from tools.global_npc_information_network import DeliveryStatus, InformationEnvelope, InformationEventQueue
from tools.global_npc_memory import Claim, SourceKind


def _decision_value(commitment, disposition, decision) -> str:
    payload = {
        "commitment_id": commitment.commitment_id,
        "proposal_id": commitment.proposal_id,
        "disposition_id": disposition.disposition_id,
        "request_event_id": decision.request_event_id,
        "decision_id": decision.decision_id,
        "decision": decision.decision,
        "decision_rationale_ref": decision.rationale_ref,
        "decision_minute": decision.semantic_minute,
        "accepted_start_minute": commitment.start_minute,
        "accepted_end_minute": commitment.end_minute,
        "location_ref": commitment.location_ref,
        "scope_ref": commitment.scope_ref,
        "alternative_ref": commitment.alternative_ref,
        "request_provenance_root": decision.provenance_root,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def schedule_assistance_renegotiation_decision_reply(
    *,
    commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    disposition_ledger: AssistanceCommitmentDispositionLedger,
    decision_ledger: AssistanceRenegotiationDecisionLedger,
    information_queue: InformationEventQueue,
    decision_id: str,
    event_id: str,
    message_id: str,
    source_claim_id: str,
    receiver_claim_id: str,
    channel_id: str,
    created_minute: int,
    receiver_trust_in_sender: int = 0,
) -> InformationEnvelope:
    """Send the requester's explicit renegotiation answer to the responder.

    The reply communicates consent or refusal only. It does not create new
    terms, alter the old commitment, reserve travel/resources, change social
    state, or invoke AutoPTU.
    """
    for value, name in (
        (decision_id, "decision_id"),
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

    decision = decision_ledger.records.get(decision_id)
    if decision is None:
        raise KeyError(f"unknown assistance renegotiation decision: {decision_id}")
    commitment = commitment_ledger.records.get(decision.commitment_id)
    if commitment is None:
        raise KeyError(f"unknown negotiated assistance commitment: {decision.commitment_id}")
    disposition = disposition_ledger.records.get(decision.disposition_id)
    if disposition is None:
        raise KeyError(f"unknown assistance commitment disposition: {decision.disposition_id}")

    if decision.proposal_id != commitment.proposal_id or disposition.proposal_id != commitment.proposal_id:
        raise ValueError("renegotiation reply proposal binding mismatch")
    if disposition.commitment_id != commitment.commitment_id:
        raise ValueError("renegotiation reply disposition commitment mismatch")
    if decision.requester_id != commitment.requester_id or decision.responder_id != commitment.responder_id:
        raise ValueError("renegotiation reply decision actor binding mismatch")
    if disposition.requester_id != commitment.requester_id or disposition.responder_id != commitment.responder_id:
        raise ValueError("renegotiation reply disposition actor binding mismatch")
    if created_minute < decision.semantic_minute:
        raise ValueError("renegotiation decision reply cannot be authored before requester decision")

    request_envelope = information_queue.envelope_provenance(decision.request_event_id)
    if request_envelope is None:
        raise KeyError(f"unknown renegotiation request event: {decision.request_event_id}")
    if information_queue.statuses.get(decision.request_event_id) != DeliveryStatus.DELIVERED:
        raise ValueError("renegotiation decision reply requires delivered original request")
    if request_envelope.sender_id != commitment.responder_id or request_envelope.receiver_id != commitment.requester_id:
        raise ValueError("renegotiation reply original request actor binding mismatch")

    requester_ledger = information_queue.ledgers.get(commitment.requester_id)
    responder_ledger = information_queue.ledgers.get(commitment.responder_id)
    if requester_ledger is None or responder_ledger is None:
        raise KeyError("renegotiation reply actors require knowledge ledgers")
    received_request = requester_ledger.claims.get(request_envelope.new_claim_id)
    if received_request is None or received_request.source_kind is not SourceKind.REPORT:
        raise ValueError("renegotiation reply requires requester REPORT evidence of original request")
    if received_request.provenance_root != decision.provenance_root:
        raise ValueError("renegotiation reply decision/request provenance mismatch")
    if decision.semantic_minute < received_request.semantic_minute:
        raise ValueError("renegotiation decision predates requester receipt")

    channel = information_queue.channels.get(channel_id)
    if channel is None:
        raise KeyError(f"unknown communication channel: {channel_id}")

    subject = f"assistance_renegotiation_decision:{commitment.commitment_id}:{decision.decision_id}"
    value = _decision_value(commitment, disposition, decision)
    expected_envelope = InformationEnvelope(
        event_id=event_id,
        message_id=message_id,
        sender_id=commitment.requester_id,
        receiver_id=commitment.responder_id,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        delivery_minute=created_minute + channel.latency_minutes,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )

    existing_envelope = information_queue.envelope_provenance(event_id)
    if existing_envelope is not None and existing_envelope != expected_envelope:
        raise ValueError("renegotiation decision reply event id reused with conflicting envelope")
    if event_id in information_queue.statuses and existing_envelope is None:
        raise ValueError("renegotiation decision reply event has status without envelope provenance")

    requester_ledger.add(
        Claim(
            claim_id=source_claim_id,
            subject=subject,
            value=value,
            source_kind=SourceKind.AUTHORED_START,
            source_agent_id=commitment.requester_id,
            semantic_minute=created_minute,
            confidence=100,
            provenance_root=decision.decision_id,
        )
    )
    if existing_envelope is not None:
        return existing_envelope

    envelope = information_queue.schedule(
        event_id=event_id,
        message_id=message_id,
        sender_id=commitment.requester_id,
        receiver_id=commitment.responder_id,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )
    if envelope != expected_envelope:
        raise RuntimeError("information queue produced unexpected renegotiation decision envelope")
    return envelope
