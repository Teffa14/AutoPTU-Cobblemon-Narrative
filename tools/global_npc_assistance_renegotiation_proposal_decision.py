from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Mapping

from tools.global_npc_assistance_renegotiation_proposal import AssistanceRenegotiationProposalLedger
from tools.global_npc_information_network import DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import SourceKind

SCHEMA_VERSION = "OUROS_ASSISTANCE_RENEGOTIATION_PROPOSAL_DECISION_LEDGER_V1"


class AssistanceRenegotiationProposalOutcome(str, Enum):
    ACCEPT = "ACCEPT_REPLACEMENT_TERMS"
    REJECT = "REJECT_REPLACEMENT_TERMS"
    EXPIRED = "EXPIRED_UNANSWERED"


@dataclass(frozen=True)
class AssistanceRenegotiationProposalDecisionRecord:
    decision_id: str
    proposal_id: str
    supersedes_commitment_id: str
    supersedes_proposal_id: str
    proposal_event_id: str
    requester_id: str
    responder_id: str
    outcome: str
    semantic_minute: int
    rationale_ref: str | None
    proposal_provenance_root: str
    provenance_root: str


class AssistanceRenegotiationProposalDecisionLedger:
    """Durable requester outcome for one delivered replacement assistance offer.

    The ledger records acceptance, refusal, or observed expiry of exact received
    terms. It does not create a replacement commitment, mutate the old
    commitment, reserve travel/resources, change relationships, or invoke
    AutoPTU.
    """

    def __init__(self) -> None:
        self.records: dict[str, AssistanceRenegotiationProposalDecisionRecord] = {}

    def add(
        self, record: AssistanceRenegotiationProposalDecisionRecord
    ) -> AssistanceRenegotiationProposalDecisionRecord:
        existing = self.records.get(record.decision_id)
        if existing is not None:
            if existing != record:
                raise ValueError("replacement-offer decision id reused with conflicting content")
            return existing
        _validate_record(record)
        self.records[record.decision_id] = record
        return record

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "records": [asdict(self.records[key]) for key in sorted(self.records)],
        }

    @classmethod
    def from_snapshot(
        cls, payload: Mapping[str, object]
    ) -> "AssistanceRenegotiationProposalDecisionLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported replacement-offer decision ledger schema")
        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("replacement-offer decision snapshot records must be a list")
        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("replacement-offer decision snapshot row must be an object")
            ledger.add(
                AssistanceRenegotiationProposalDecisionRecord(
                    decision_id=str(raw["decision_id"]),
                    proposal_id=str(raw["proposal_id"]),
                    supersedes_commitment_id=str(raw["supersedes_commitment_id"]),
                    supersedes_proposal_id=str(raw["supersedes_proposal_id"]),
                    proposal_event_id=str(raw["proposal_event_id"]),
                    requester_id=str(raw["requester_id"]),
                    responder_id=str(raw["responder_id"]),
                    outcome=str(raw["outcome"]),
                    semantic_minute=int(raw["semantic_minute"]),
                    rationale_ref=None if raw.get("rationale_ref") is None else str(raw["rationale_ref"]),
                    proposal_provenance_root=str(raw["proposal_provenance_root"]),
                    provenance_root=str(raw["provenance_root"]),
                )
            )
        return ledger


def _validate_record(record: AssistanceRenegotiationProposalDecisionRecord) -> None:
    if not all(
        (
            record.decision_id,
            record.proposal_id,
            record.supersedes_commitment_id,
            record.supersedes_proposal_id,
            record.proposal_event_id,
            record.requester_id,
            record.responder_id,
            record.proposal_provenance_root,
            record.provenance_root,
        )
    ):
        raise ValueError("invalid replacement-offer decision identity")
    if record.requester_id == record.responder_id:
        raise ValueError("replacement-offer decision requires two distinct actors")
    if record.outcome not in {choice.value for choice in AssistanceRenegotiationProposalOutcome}:
        raise ValueError("unsupported replacement-offer outcome")
    if record.semantic_minute < 0:
        raise ValueError("replacement-offer decision semantic_minute must be non-negative")
    if record.rationale_ref is not None and not record.rationale_ref.strip():
        raise ValueError("rationale_ref cannot be blank")


def _expected_proposal_payload(proposal) -> dict[str, object]:
    return {
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


def record_assistance_renegotiation_proposal_decision(
    *,
    proposal_ledger: AssistanceRenegotiationProposalLedger,
    information_queue: InformationEventQueue,
    decision_ledger: AssistanceRenegotiationProposalDecisionLedger,
    proposal_event_id: str,
    decision_id: str,
    requester_id: str,
    outcome: AssistanceRenegotiationProposalOutcome | str,
    semantic_minute: int,
    rationale_ref: str | None = None,
) -> AssistanceRenegotiationProposalDecisionRecord:
    """Record requester disposition of the exact replacement terms actually received."""

    if not proposal_event_id or not decision_id or not requester_id:
        raise ValueError("proposal_event_id, decision_id and requester_id are required")
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")
    if rationale_ref is not None:
        rationale_ref = rationale_ref.strip()
        if not rationale_ref:
            raise ValueError("rationale_ref cannot be blank")
    outcome_value = outcome.value if isinstance(outcome, AssistanceRenegotiationProposalOutcome) else str(outcome)
    if outcome_value not in {choice.value for choice in AssistanceRenegotiationProposalOutcome}:
        raise ValueError("unsupported replacement-offer outcome")

    envelope = information_queue.envelope_provenance(proposal_event_id)
    if envelope is None:
        raise KeyError(f"unknown replacement-offer event: {proposal_event_id}")
    if information_queue.statuses.get(proposal_event_id) != DeliveryStatus.DELIVERED:
        raise ValueError("replacement-offer decision requires terminal DELIVERED proposal")
    if envelope.receiver_id != requester_id:
        raise ValueError("replacement-offer decision actor must be the delivered requester")

    requester_ledger = information_queue.ledgers.get(envelope.receiver_id)
    responder_ledger = information_queue.ledgers.get(envelope.sender_id)
    if requester_ledger is None or responder_ledger is None:
        raise KeyError("replacement-offer actors require knowledge ledgers")
    source_claim = responder_ledger.claims.get(envelope.source_claim_id)
    received_claim = requester_ledger.claims.get(envelope.new_claim_id)
    if source_claim is None or received_claim is None:
        raise ValueError("DELIVERED replacement offer requires source and requester claims")
    if received_claim.source_kind is not SourceKind.REPORT:
        raise ValueError("replacement-offer requester claim must be delivered REPORT evidence")
    if received_claim.parent_claim_id != source_claim.claim_id:
        raise ValueError("replacement-offer requester claim parent mismatch")
    if received_claim.provenance_root != source_claim.provenance_root:
        raise ValueError("replacement-offer provenance mismatch")
    if received_claim.subject != source_claim.subject or received_claim.value != source_claim.value:
        raise ValueError("delivered replacement offer differs from authored proposal")

    try:
        payload = json.loads(received_claim.value)
    except json.JSONDecodeError as exc:
        raise ValueError("delivered replacement offer is not valid structured payload") from exc
    if not isinstance(payload, dict):
        raise ValueError("delivered replacement-offer payload must be an object")

    proposal_id = str(payload.get("proposal_id", ""))
    proposal = proposal_ledger.records.get(proposal_id)
    if proposal is None:
        raise KeyError(f"unknown assistance renegotiation proposal: {proposal_id}")
    expected_subject = (
        f"assistance_renegotiation_proposal:{proposal.supersedes_commitment_id}:{proposal.proposal_id}"
    )
    if source_claim.subject != expected_subject:
        raise ValueError("replacement-offer subject mismatch")
    if payload != _expected_proposal_payload(proposal):
        raise ValueError("delivered replacement offer does not match durable proposal")
    if envelope.sender_id != proposal.responder_id or envelope.receiver_id != proposal.requester_id:
        raise ValueError("replacement-offer actor binding mismatch")
    if semantic_minute < received_claim.semantic_minute:
        raise ValueError("replacement-offer decision cannot predate requester receipt")

    expired = proposal.expires_minute is not None and semantic_minute > proposal.expires_minute
    if outcome_value == AssistanceRenegotiationProposalOutcome.EXPIRED.value:
        if proposal.expires_minute is None:
            raise ValueError("replacement offer without expiry cannot become EXPIRED_UNANSWERED")
        if not expired:
            raise ValueError("replacement offer cannot expire before its expiry minute passes")
    elif expired:
        raise ValueError("expired replacement offer cannot be accepted or rejected")

    record = AssistanceRenegotiationProposalDecisionRecord(
        decision_id=decision_id,
        proposal_id=proposal.proposal_id,
        supersedes_commitment_id=proposal.supersedes_commitment_id,
        supersedes_proposal_id=proposal.supersedes_proposal_id,
        proposal_event_id=proposal_event_id,
        requester_id=proposal.requester_id,
        responder_id=proposal.responder_id,
        outcome=outcome_value,
        semantic_minute=semantic_minute,
        rationale_ref=rationale_ref,
        proposal_provenance_root=proposal.provenance_root,
        provenance_root=received_claim.provenance_root,
    )
    return decision_ledger.add(record)
