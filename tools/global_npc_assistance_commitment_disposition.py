from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Mapping

from tools.global_npc_assistance_commitment_start import (
    AssistanceCommitmentStartLedger,
    CommitmentStartCondition,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
)

SCHEMA_VERSION = "OUROS_ASSISTANCE_COMMITMENT_DISPOSITION_LEDGER_V1"


class CommitmentStartDisposition(str, Enum):
    ATTEMPT_FULFILLMENT = "ATTEMPT_FULFILLMENT"
    WAIT_FOR_CLEARANCE = "WAIT_FOR_CLEARANCE"
    REQUEST_RENEGOTIATION = "REQUEST_RENEGOTIATION"
    ABANDON_OBLIGATION = "ABANDON_OBLIGATION"


@dataclass(frozen=True)
class AssistanceCommitmentDisposition:
    disposition_id: str
    commitment_id: str
    proposal_id: str
    assessment_id: str
    requester_id: str
    responder_id: str
    actor_id: str
    semantic_minute: int
    disposition: str
    rationale_ref: str
    provenance_root: str


class AssistanceCommitmentDispositionLedger:
    """Durable responder decision after an adverse negotiated-assistance start.

    The record says what the commitment owner decided to do about a start-time
    risk or blocker. It does not execute that decision, alter the accepted
    commitment, communicate with the requester, reserve travel/resources,
    adjudicate fault, record a missed obligation, or invoke AutoPTU.
    """

    def __init__(self) -> None:
        self.records: dict[str, AssistanceCommitmentDisposition] = {}

    def add(self, record: AssistanceCommitmentDisposition) -> AssistanceCommitmentDisposition:
        existing = self.records.get(record.disposition_id)
        if existing is not None:
            if existing != record:
                raise ValueError("commitment disposition id reused with conflicting content")
            return existing
        if any(row.commitment_id == record.commitment_id for row in self.records.values()):
            raise ValueError("commitment already has a start disposition")
        self.records[record.disposition_id] = record
        return record

    def for_commitment(self, commitment_id: str) -> AssistanceCommitmentDisposition | None:
        rows = [row for row in self.records.values() if row.commitment_id == commitment_id]
        if not rows:
            return None
        if len(rows) != 1:
            raise ValueError("commitment has multiple start dispositions")
        return rows[0]

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "records": [asdict(self.records[key]) for key in sorted(self.records)],
        }

    @classmethod
    def from_snapshot(cls, payload: Mapping[str, object]) -> "AssistanceCommitmentDispositionLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported assistance commitment disposition ledger schema")
        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("assistance commitment disposition records must be a list")
        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("assistance commitment disposition row must be an object")
            record = AssistanceCommitmentDisposition(
                disposition_id=str(raw["disposition_id"]),
                commitment_id=str(raw["commitment_id"]),
                proposal_id=str(raw["proposal_id"]),
                assessment_id=str(raw["assessment_id"]),
                requester_id=str(raw["requester_id"]),
                responder_id=str(raw["responder_id"]),
                actor_id=str(raw["actor_id"]),
                semantic_minute=int(raw["semantic_minute"]),
                disposition=str(raw["disposition"]),
                rationale_ref=str(raw["rationale_ref"]),
                provenance_root=str(raw["provenance_root"]),
            )
            _validate_shape(record)
            ledger.add(record)
        return ledger


def _validate_shape(record: AssistanceCommitmentDisposition) -> None:
    required = (
        record.disposition_id,
        record.commitment_id,
        record.proposal_id,
        record.assessment_id,
        record.requester_id,
        record.responder_id,
        record.actor_id,
        record.rationale_ref,
        record.provenance_root,
    )
    if any(not value for value in required):
        raise ValueError("assistance commitment disposition requires non-empty references")
    if record.semantic_minute < 0:
        raise ValueError("assistance commitment disposition minute must be non-negative")
    CommitmentStartDisposition(record.disposition)


def record_commitment_start_disposition(
    *,
    commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    start_ledger: AssistanceCommitmentStartLedger,
    disposition_ledger: AssistanceCommitmentDispositionLedger,
    commitment_id: str,
    assessment_id: str,
    disposition_id: str,
    actor_id: str,
    semantic_minute: int,
    disposition: CommitmentStartDisposition,
    rationale_ref: str,
    provenance_root: str,
) -> AssistanceCommitmentDisposition:
    """Record the responder's immediate world-level choice after an adverse start.

    The accepted promise and start assessment remain unchanged. Any later
    communication, renegotiation, travel, resource handling, missed-obligation
    accounting or structured mechanics require their existing dedicated owners.
    """
    commitment = commitment_ledger.records.get(commitment_id)
    if commitment is None:
        raise KeyError(f"unknown negotiated assistance commitment: {commitment_id}")
    assessment = start_ledger.assessments.get(assessment_id)
    if assessment is None:
        raise KeyError(f"unknown assistance commitment start assessment: {assessment_id}")
    if assessment.commitment_id != commitment.commitment_id:
        raise ValueError("start assessment commitment binding mismatch")
    if assessment.proposal_id != commitment.proposal_id:
        raise ValueError("start assessment proposal binding mismatch")
    if assessment.requester_id != commitment.requester_id or assessment.responder_id != commitment.responder_id:
        raise ValueError("start assessment actor binding mismatch")
    if assessment.condition not in {
        CommitmentStartCondition.AT_RISK_AT_START.value,
        CommitmentStartCondition.BLOCKED_AT_START.value,
    }:
        raise ValueError("start disposition requires an adverse start assessment")
    if actor_id != commitment.responder_id:
        raise ValueError("only the responder owning the commitment can choose its start disposition")
    if semantic_minute < assessment.semantic_minute:
        raise ValueError("start disposition cannot predate the start assessment")
    if semantic_minute > commitment.end_minute:
        raise ValueError("start disposition must occur within the accepted assistance window")
    if not disposition_id or not rationale_ref or not provenance_root:
        raise ValueError("disposition, rationale and provenance references are required")

    record = AssistanceCommitmentDisposition(
        disposition_id=disposition_id,
        commitment_id=commitment.commitment_id,
        proposal_id=commitment.proposal_id,
        assessment_id=assessment.assessment_id,
        requester_id=commitment.requester_id,
        responder_id=commitment.responder_id,
        actor_id=actor_id,
        semantic_minute=semantic_minute,
        disposition=disposition.value,
        rationale_ref=rationale_ref,
        provenance_root=provenance_root,
    )
    _validate_shape(record)
    return disposition_ledger.add(record)
