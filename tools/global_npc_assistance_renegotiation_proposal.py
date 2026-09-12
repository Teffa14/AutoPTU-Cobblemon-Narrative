from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Mapping

from tools.global_npc_assistance_counterproposal_commitment import AssistanceCounterproposalCommitmentLedger
from tools.global_npc_assistance_renegotiation_decision import (
    AssistanceRenegotiationDecision,
    AssistanceRenegotiationDecisionLedger,
)
from tools.global_npc_information_network import DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import SourceKind

SCHEMA_VERSION = "OUROS_ASSISTANCE_RENEGOTIATION_PROPOSAL_LEDGER_V1"


@dataclass(frozen=True)
class AssistanceRenegotiationProposalRecord:
    proposal_id: str
    supersedes_commitment_id: str
    supersedes_proposal_id: str
    decision_id: str
    decision_reply_event_id: str
    requester_id: str
    responder_id: str
    proposed_start_minute: int
    proposed_end_minute: int
    location_ref: str | None
    scope_ref: str | None
    alternative_ref: str | None
    expires_minute: int | None
    semantic_minute: int
    decision_provenance_root: str
    provenance_root: str


class AssistanceRenegotiationProposalLedger:
    """Responder-authored replacement terms after delivered permission to renegotiate.

    Records are offers only. They do not mutate the old commitment, create a
    replacement commitment, reserve a route, grant access, allocate resources,
    move an actor, change relationships, or invoke AutoPTU.
    """

    def __init__(self) -> None:
        self.records: dict[str, AssistanceRenegotiationProposalRecord] = {}

    def add(self, record: AssistanceRenegotiationProposalRecord) -> AssistanceRenegotiationProposalRecord:
        existing = self.records.get(record.proposal_id)
        if existing is not None:
            if existing != record:
                raise ValueError("renegotiation proposal id reused with conflicting content")
            return existing
        _validate_record(record)
        self.records[record.proposal_id] = record
        return record

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "records": [asdict(self.records[key]) for key in sorted(self.records)],
        }

    @classmethod
    def from_snapshot(cls, payload: Mapping[str, object]) -> "AssistanceRenegotiationProposalLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported assistance renegotiation proposal ledger schema")
        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("assistance renegotiation proposal snapshot records must be a list")
        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("assistance renegotiation proposal snapshot row must be an object")
            ledger.add(
                AssistanceRenegotiationProposalRecord(
                    proposal_id=str(raw["proposal_id"]),
                    supersedes_commitment_id=str(raw["supersedes_commitment_id"]),
                    supersedes_proposal_id=str(raw["supersedes_proposal_id"]),
                    decision_id=str(raw["decision_id"]),
                    decision_reply_event_id=str(raw["decision_reply_event_id"]),
                    requester_id=str(raw["requester_id"]),
                    responder_id=str(raw["responder_id"]),
                    proposed_start_minute=int(raw["proposed_start_minute"]),
                    proposed_end_minute=int(raw["proposed_end_minute"]),
                    location_ref=None if raw.get("location_ref") is None else str(raw["location_ref"]),
                    scope_ref=None if raw.get("scope_ref") is None else str(raw["scope_ref"]),
                    alternative_ref=None if raw.get("alternative_ref") is None else str(raw["alternative_ref"]),
                    expires_minute=None if raw.get("expires_minute") is None else int(raw["expires_minute"]),
                    semantic_minute=int(raw["semantic_minute"]),
                    decision_provenance_root=str(raw["decision_provenance_root"]),
                    provenance_root=str(raw["provenance_root"]),
                )
            )
        return ledger


def _clean_optional(value: str | None, name: str) -> str | None:
    if value is None:
        return None
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{name} cannot be blank")
    return cleaned


def _validate_record(record: AssistanceRenegotiationProposalRecord) -> None:
    if not all((record.proposal_id, record.supersedes_commitment_id, record.supersedes_proposal_id,
                record.decision_id, record.decision_reply_event_id, record.requester_id,
                record.responder_id, record.decision_provenance_root, record.provenance_root)):
        raise ValueError("invalid assistance renegotiation proposal identity")
    if record.requester_id == record.responder_id:
        raise ValueError("renegotiation proposal requires two distinct actors")
    if record.provenance_root != record.proposal_id:
        raise ValueError("renegotiation proposal provenance must begin at the new proposal")
    if record.semantic_minute < 0 or record.proposed_start_minute < 0:
        raise ValueError("renegotiation proposal minutes must be non-negative")
    if record.proposed_end_minute < record.proposed_start_minute:
        raise ValueError("renegotiation proposal end cannot precede start")
    if record.proposed_start_minute < record.semantic_minute:
        raise ValueError("renegotiation proposal cannot start in the past")
    if record.expires_minute is not None and record.expires_minute < record.semantic_minute:
        raise ValueError("renegotiation proposal cannot already be expired")
    for value, name in ((record.location_ref, "location_ref"), (record.scope_ref, "scope_ref"),
                        (record.alternative_ref, "alternative_ref")):
        if value is not None and not value.strip():
            raise ValueError(f"{name} cannot be blank")


def _expected_reply_payload(commitment, decision) -> dict[str, object]:
    return {
        "commitment_id": commitment.commitment_id,
        "proposal_id": commitment.proposal_id,
        "disposition_id": decision.disposition_id,
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


def record_assistance_renegotiation_proposal(
    *,
    commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    decision_ledger: AssistanceRenegotiationDecisionLedger,
    information_queue: InformationEventQueue,
    proposal_ledger: AssistanceRenegotiationProposalLedger,
    decision_id: str,
    decision_reply_event_id: str,
    proposal_id: str,
    responder_id: str,
    semantic_minute: int,
    proposed_start_minute: int,
    proposed_end_minute: int,
    location_ref: str | None,
    scope_ref: str | None,
    alternative_ref: str | None,
    expires_minute: int | None = None,
) -> AssistanceRenegotiationProposalRecord:
    """Persist new responder-authored terms after delivered permission to reopen negotiation."""

    if not all((decision_id, decision_reply_event_id, proposal_id, responder_id)):
        raise ValueError("decision, reply event, proposal and responder ids are required")
    location_ref = _clean_optional(location_ref, "location_ref")
    scope_ref = _clean_optional(scope_ref, "scope_ref")
    alternative_ref = _clean_optional(alternative_ref, "alternative_ref")

    decision = decision_ledger.records.get(decision_id)
    if decision is None:
        raise KeyError(f"unknown assistance renegotiation decision: {decision_id}")
    if decision.decision != AssistanceRenegotiationDecision.ACCEPT_REOPENING.value:
        raise ValueError("replacement terms require explicit ACCEPT_RENEGOTIATION_REQUEST")
    commitment = commitment_ledger.records.get(decision.commitment_id)
    if commitment is None:
        raise KeyError(f"unknown negotiated assistance commitment: {decision.commitment_id}")
    if decision.proposal_id != commitment.proposal_id:
        raise ValueError("renegotiation proposal old proposal binding mismatch")
    if decision.requester_id != commitment.requester_id or decision.responder_id != commitment.responder_id:
        raise ValueError("renegotiation proposal decision actor binding mismatch")
    if responder_id != commitment.responder_id:
        raise ValueError("only the original responder may author replacement terms")

    envelope = information_queue.envelope_provenance(decision_reply_event_id)
    if envelope is None:
        raise KeyError(f"unknown renegotiation decision reply event: {decision_reply_event_id}")
    if information_queue.statuses.get(decision_reply_event_id) != DeliveryStatus.DELIVERED:
        raise ValueError("replacement terms require terminal DELIVERED acceptance reply")
    if envelope.sender_id != commitment.requester_id or envelope.receiver_id != commitment.responder_id:
        raise ValueError("renegotiation acceptance reply actor binding mismatch")

    requester_ledger = information_queue.ledgers.get(commitment.requester_id)
    responder_ledger = information_queue.ledgers.get(commitment.responder_id)
    if requester_ledger is None or responder_ledger is None:
        raise KeyError("renegotiation proposal actors require knowledge ledgers")
    source_claim = requester_ledger.claims.get(envelope.source_claim_id)
    received_claim = responder_ledger.claims.get(envelope.new_claim_id)
    if source_claim is None or received_claim is None:
        raise ValueError("DELIVERED acceptance reply requires source and responder claims")
    if received_claim.source_kind is not SourceKind.REPORT:
        raise ValueError("renegotiation acceptance must be responder REPORT evidence")
    if received_claim.parent_claim_id != source_claim.claim_id:
        raise ValueError("renegotiation acceptance parent claim mismatch")
    if received_claim.provenance_root != decision.decision_id:
        raise ValueError("renegotiation acceptance provenance mismatch")
    if received_claim.subject != source_claim.subject or received_claim.value != source_claim.value:
        raise ValueError("renegotiation acceptance differs from authored reply")
    expected_subject = f"assistance_renegotiation_decision:{commitment.commitment_id}:{decision.decision_id}"
    if source_claim.subject != expected_subject:
        raise ValueError("renegotiation acceptance subject mismatch")
    try:
        payload = json.loads(received_claim.value)
    except json.JSONDecodeError as exc:
        raise ValueError("renegotiation acceptance reply is not structured payload") from exc
    if payload != _expected_reply_payload(commitment, decision):
        raise ValueError("renegotiation acceptance payload does not match durable history")
    if semantic_minute < received_claim.semantic_minute:
        raise ValueError("replacement terms cannot predate responder receipt of acceptance")

    replacement_tuple = (
        proposed_start_minute, proposed_end_minute, location_ref, scope_ref, alternative_ref
    )
    old_tuple = (
        commitment.start_minute, commitment.end_minute, commitment.location_ref,
        commitment.scope_ref, commitment.alternative_ref
    )
    if replacement_tuple == old_tuple:
        raise ValueError("replacement proposal must change at least one accepted term")

    record = AssistanceRenegotiationProposalRecord(
        proposal_id=proposal_id,
        supersedes_commitment_id=commitment.commitment_id,
        supersedes_proposal_id=commitment.proposal_id,
        decision_id=decision.decision_id,
        decision_reply_event_id=decision_reply_event_id,
        requester_id=commitment.requester_id,
        responder_id=commitment.responder_id,
        proposed_start_minute=proposed_start_minute,
        proposed_end_minute=proposed_end_minute,
        location_ref=location_ref,
        scope_ref=scope_ref,
        alternative_ref=alternative_ref,
        expires_minute=expires_minute,
        semantic_minute=semantic_minute,
        decision_provenance_root=decision.decision_id,
        provenance_root=proposal_id,
    )
    return proposal_ledger.add(record)
