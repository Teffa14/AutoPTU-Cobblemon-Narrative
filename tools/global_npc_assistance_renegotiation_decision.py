from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Mapping

from tools.global_npc_assistance_commitment_disposition import AssistanceCommitmentDispositionLedger
from tools.global_npc_assistance_counterproposal_commitment import AssistanceCounterproposalCommitmentLedger
from tools.global_npc_information_network import DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import SourceKind

SCHEMA_VERSION = "OUROS_ASSISTANCE_RENEGOTIATION_DECISION_LEDGER_V1"


class AssistanceRenegotiationDecision(str, Enum):
    ACCEPT_REOPENING = "ACCEPT_RENEGOTIATION_REQUEST"
    REJECT_REOPENING = "REJECT_RENEGOTIATION_REQUEST"


@dataclass(frozen=True)
class AssistanceRenegotiationDecisionRecord:
    decision_id: str
    commitment_id: str
    proposal_id: str
    disposition_id: str
    request_event_id: str
    requester_id: str
    responder_id: str
    decision: str
    semantic_minute: int
    rationale_ref: str | None
    provenance_root: str


class AssistanceRenegotiationDecisionLedger:
    """Durable requester decisions about reopening accepted assistance terms.

    This ledger records consent or refusal to reopen negotiations. It does not
    alter the accepted commitment, create replacement terms, send a reply,
    reserve travel/resources, change relationships, or invoke AutoPTU.
    """

    def __init__(self) -> None:
        self.records: dict[str, AssistanceRenegotiationDecisionRecord] = {}

    def add(self, record: AssistanceRenegotiationDecisionRecord) -> AssistanceRenegotiationDecisionRecord:
        existing = self.records.get(record.decision_id)
        if existing is not None:
            if existing != record:
                raise ValueError("renegotiation decision id reused with conflicting content")
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
    def from_snapshot(cls, payload: Mapping[str, object]) -> "AssistanceRenegotiationDecisionLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported assistance renegotiation decision ledger schema")
        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("assistance renegotiation decision snapshot records must be a list")
        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("assistance renegotiation decision snapshot row must be an object")
            ledger.add(
                AssistanceRenegotiationDecisionRecord(
                    decision_id=str(raw["decision_id"]),
                    commitment_id=str(raw["commitment_id"]),
                    proposal_id=str(raw["proposal_id"]),
                    disposition_id=str(raw["disposition_id"]),
                    request_event_id=str(raw["request_event_id"]),
                    requester_id=str(raw["requester_id"]),
                    responder_id=str(raw["responder_id"]),
                    decision=str(raw["decision"]),
                    semantic_minute=int(raw["semantic_minute"]),
                    rationale_ref=None if raw.get("rationale_ref") is None else str(raw["rationale_ref"]),
                    provenance_root=str(raw["provenance_root"]),
                )
            )
        return ledger


def _validate_record(record: AssistanceRenegotiationDecisionRecord) -> None:
    if not all(
        (
            record.decision_id,
            record.commitment_id,
            record.proposal_id,
            record.disposition_id,
            record.request_event_id,
            record.requester_id,
            record.responder_id,
            record.provenance_root,
        )
    ):
        raise ValueError("invalid assistance renegotiation decision identity")
    if record.requester_id == record.responder_id:
        raise ValueError("renegotiation decision requires two distinct actors")
    if record.decision not in {choice.value for choice in AssistanceRenegotiationDecision}:
        raise ValueError("unsupported assistance renegotiation decision")
    if record.semantic_minute < 0:
        raise ValueError("renegotiation decision semantic_minute must be non-negative")
    if record.rationale_ref is not None and not record.rationale_ref.strip():
        raise ValueError("rationale_ref cannot be blank")


def _expected_request_payload(commitment, disposition) -> dict[str, object]:
    return {
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


def record_assistance_renegotiation_decision(
    *,
    commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    disposition_ledger: AssistanceCommitmentDispositionLedger,
    information_queue: InformationEventQueue,
    decision_ledger: AssistanceRenegotiationDecisionLedger,
    request_event_id: str,
    decision_id: str,
    decision: AssistanceRenegotiationDecision | str,
    requester_id: str,
    semantic_minute: int,
    rationale_ref: str | None = None,
) -> AssistanceRenegotiationDecisionRecord:
    """Record explicit requester consent/refusal after a delivered reopen request."""

    if not request_event_id or not decision_id or not requester_id:
        raise ValueError("request_event_id, decision_id and requester_id are required")
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")
    if rationale_ref is not None:
        rationale_ref = rationale_ref.strip()
        if not rationale_ref:
            raise ValueError("rationale_ref cannot be blank")
    decision_value = decision.value if isinstance(decision, AssistanceRenegotiationDecision) else str(decision)
    if decision_value not in {choice.value for choice in AssistanceRenegotiationDecision}:
        raise ValueError("unsupported assistance renegotiation decision")

    envelope = information_queue.envelope_provenance(request_event_id)
    if envelope is None:
        raise KeyError(f"unknown assistance renegotiation request event: {request_event_id}")
    if information_queue.statuses.get(request_event_id) != DeliveryStatus.DELIVERED:
        raise ValueError("renegotiation decision requires terminal DELIVERED request")
    if envelope.receiver_id != requester_id:
        raise ValueError("renegotiation decision actor must be the delivered requester")

    requester_ledger = information_queue.ledgers.get(envelope.receiver_id)
    responder_ledger = information_queue.ledgers.get(envelope.sender_id)
    if requester_ledger is None or responder_ledger is None:
        raise KeyError("renegotiation actors require knowledge ledgers")
    source_claim = responder_ledger.claims.get(envelope.source_claim_id)
    received_claim = requester_ledger.claims.get(envelope.new_claim_id)
    if source_claim is None or received_claim is None:
        raise ValueError("DELIVERED renegotiation request requires source and requester claims")
    if received_claim.source_kind is not SourceKind.REPORT:
        raise ValueError("renegotiation requester claim must be delivered REPORT evidence")
    if received_claim.parent_claim_id != source_claim.claim_id:
        raise ValueError("renegotiation requester claim parent mismatch")
    if received_claim.provenance_root != source_claim.provenance_root:
        raise ValueError("renegotiation request provenance mismatch")
    if received_claim.subject != source_claim.subject or received_claim.value != source_claim.value:
        raise ValueError("renegotiation delivered request differs from authored request")

    try:
        payload = json.loads(received_claim.value)
    except json.JSONDecodeError as exc:
        raise ValueError("renegotiation delivered request is not valid structured payload") from exc
    if not isinstance(payload, dict):
        raise ValueError("renegotiation delivered request payload must be an object")

    commitment_id = str(payload.get("commitment_id", ""))
    disposition_id = str(payload.get("disposition_id", ""))
    commitment = commitment_ledger.records.get(commitment_id)
    if commitment is None:
        raise KeyError(f"unknown negotiated assistance commitment: {commitment_id}")
    disposition = disposition_ledger.records.get(disposition_id)
    if disposition is None:
        raise KeyError(f"unknown assistance commitment disposition: {disposition_id}")

    expected_subject = f"assistance_renegotiation_request:{commitment.commitment_id}:{disposition.disposition_id}"
    if source_claim.subject != expected_subject:
        raise ValueError("renegotiation request subject mismatch")
    if payload != _expected_request_payload(commitment, disposition):
        raise ValueError("renegotiation delivered request does not match durable commitment/disposition")
    if envelope.sender_id != commitment.responder_id or envelope.receiver_id != commitment.requester_id:
        raise ValueError("renegotiation request actor binding mismatch")
    if disposition.commitment_id != commitment.commitment_id or disposition.proposal_id != commitment.proposal_id:
        raise ValueError("renegotiation disposition commitment/proposal mismatch")
    if disposition.requester_id != commitment.requester_id or disposition.responder_id != commitment.responder_id:
        raise ValueError("renegotiation disposition actor binding mismatch")
    if semantic_minute < received_claim.semantic_minute:
        raise ValueError("renegotiation decision cannot predate requester receipt")

    record = AssistanceRenegotiationDecisionRecord(
        decision_id=decision_id,
        commitment_id=commitment.commitment_id,
        proposal_id=commitment.proposal_id,
        disposition_id=disposition.disposition_id,
        request_event_id=request_event_id,
        requester_id=commitment.requester_id,
        responder_id=commitment.responder_id,
        decision=decision_value,
        semantic_minute=semantic_minute,
        rationale_ref=rationale_ref,
        provenance_root=received_claim.provenance_root,
    )
    return decision_ledger.add(record)
