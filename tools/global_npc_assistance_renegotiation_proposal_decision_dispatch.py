from __future__ import annotations

import json

from tools.global_npc_assistance_renegotiation_proposal import AssistanceRenegotiationProposalLedger
from tools.global_npc_assistance_renegotiation_proposal_decision import (
    AssistanceRenegotiationProposalDecisionLedger,
    AssistanceRenegotiationProposalOutcome,
)
from tools.global_npc_information_network import DeliveryStatus, InformationEnvelope, InformationEventQueue
from tools.global_npc_memory import Claim, SourceKind


def _decision_value(proposal, decision) -> str:
    payload = {
        "decision_id": decision.decision_id,
        "proposal_id": proposal.proposal_id,
        "supersedes_commitment_id": proposal.supersedes_commitment_id,
        "supersedes_proposal_id": proposal.supersedes_proposal_id,
        "proposal_event_id": decision.proposal_event_id,
        "requester_id": proposal.requester_id,
        "responder_id": proposal.responder_id,
        "outcome": decision.outcome,
        "decision_rationale_ref": decision.rationale_ref,
        "decision_minute": decision.semantic_minute,
        "proposed_start_minute": proposal.proposed_start_minute,
        "proposed_end_minute": proposal.proposed_end_minute,
        "location_ref": proposal.location_ref,
        "scope_ref": proposal.scope_ref,
        "alternative_ref": proposal.alternative_ref,
        "expires_minute": proposal.expires_minute,
        "proposal_provenance_root": proposal.provenance_root,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def schedule_assistance_renegotiation_proposal_decision_reply(
    *,
    proposal_ledger: AssistanceRenegotiationProposalLedger,
    decision_ledger: AssistanceRenegotiationProposalDecisionLedger,
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
    """Send the requester's explicit answer to one replacement offer.

    Transport communicates acceptance or rejection only. It does not create a
    replacement commitment, mutate the old commitment or proposal, reserve
    travel/resources, change relationships, move actors, or invoke AutoPTU.
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
        raise KeyError(f"unknown replacement-offer decision: {decision_id}")
    if decision.outcome == AssistanceRenegotiationProposalOutcome.EXPIRED.value:
        raise ValueError("EXPIRED_UNANSWERED is an observed timeout, not a requester reply")
    if decision.outcome not in {
        AssistanceRenegotiationProposalOutcome.ACCEPT.value,
        AssistanceRenegotiationProposalOutcome.REJECT.value,
    }:
        raise ValueError("unsupported replacement-offer reply outcome")

    proposal = proposal_ledger.records.get(decision.proposal_id)
    if proposal is None:
        raise KeyError(f"unknown assistance renegotiation proposal: {decision.proposal_id}")
    if decision.supersedes_commitment_id != proposal.supersedes_commitment_id:
        raise ValueError("replacement-offer reply commitment lineage mismatch")
    if decision.supersedes_proposal_id != proposal.supersedes_proposal_id:
        raise ValueError("replacement-offer reply proposal lineage mismatch")
    if decision.requester_id != proposal.requester_id or decision.responder_id != proposal.responder_id:
        raise ValueError("replacement-offer reply actor binding mismatch")
    if decision.proposal_provenance_root != proposal.provenance_root:
        raise ValueError("replacement-offer reply proposal provenance mismatch")
    if created_minute < decision.semantic_minute:
        raise ValueError("replacement-offer reply cannot be authored before requester decision")

    proposal_envelope = information_queue.envelope_provenance(decision.proposal_event_id)
    if proposal_envelope is None:
        raise KeyError(f"unknown replacement-offer event: {decision.proposal_event_id}")
    if information_queue.statuses.get(decision.proposal_event_id) != DeliveryStatus.DELIVERED:
        raise ValueError("replacement-offer reply requires delivered proposal")
    if proposal_envelope.sender_id != proposal.responder_id or proposal_envelope.receiver_id != proposal.requester_id:
        raise ValueError("replacement-offer reply original offer actor binding mismatch")

    requester_ledger = information_queue.ledgers.get(proposal.requester_id)
    responder_ledger = information_queue.ledgers.get(proposal.responder_id)
    if requester_ledger is None or responder_ledger is None:
        raise KeyError("replacement-offer reply actors require knowledge ledgers")
    received_offer = requester_ledger.claims.get(proposal_envelope.new_claim_id)
    if received_offer is None or received_offer.source_kind is not SourceKind.REPORT:
        raise ValueError("replacement-offer reply requires requester REPORT evidence of proposal")
    if received_offer.provenance_root != decision.provenance_root:
        raise ValueError("replacement-offer reply decision/proposal provenance mismatch")
    if decision.semantic_minute < received_offer.semantic_minute:
        raise ValueError("replacement-offer decision predates requester receipt")

    channel = information_queue.channels.get(channel_id)
    if channel is None:
        raise KeyError(f"unknown communication channel: {channel_id}")

    subject = f"assistance_renegotiation_proposal_decision:{proposal.proposal_id}:{decision.decision_id}"
    value = _decision_value(proposal, decision)
    expected_envelope = InformationEnvelope(
        event_id=event_id,
        message_id=message_id,
        sender_id=proposal.requester_id,
        receiver_id=proposal.responder_id,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        delivery_minute=created_minute + channel.latency_minutes,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )

    existing_envelope = information_queue.envelope_provenance(event_id)
    if existing_envelope is not None and existing_envelope != expected_envelope:
        raise ValueError("replacement-offer decision reply event id reused with conflicting envelope")
    if event_id in information_queue.statuses and existing_envelope is None:
        raise ValueError("replacement-offer decision reply event has status without envelope provenance")

    requester_ledger.add(
        Claim(
            claim_id=source_claim_id,
            subject=subject,
            value=value,
            source_kind=SourceKind.AUTHORED_START,
            source_agent_id=proposal.requester_id,
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
        sender_id=proposal.requester_id,
        receiver_id=proposal.responder_id,
        source_claim_id=source_claim_id,
        new_claim_id=receiver_claim_id,
        channel_id=channel_id,
        created_minute=created_minute,
        receiver_trust_in_sender=receiver_trust_in_sender,
    )
    if envelope != expected_envelope:
        raise RuntimeError("information queue produced unexpected replacement-offer decision envelope")
    return envelope
