from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Mapping

from tools.global_npc_ai import ScheduledCommitment
from tools.global_npc_assistance_counterproposal_commitment import AssistanceCounterproposalCommitmentLedger
from tools.global_npc_assistance_renegotiation_proposal import AssistanceRenegotiationProposalLedger
from tools.global_npc_assistance_renegotiation_proposal_decision import (
    AssistanceRenegotiationProposalDecisionLedger,
    AssistanceRenegotiationProposalOutcome,
)
from tools.global_npc_information_network import DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import SourceKind
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator

SCHEMA_VERSION = "OUROS_ASSISTANCE_RENEGOTIATION_REPLACEMENT_COMMITMENT_LEDGER_V1"


@dataclass(frozen=True)
class AssistanceRenegotiationReplacementCommitmentRecord:
    commitment_id: str
    supersedes_commitment_id: str
    replacement_proposal_id: str
    proposal_decision_id: str
    decision_reply_event_id: str
    requester_id: str
    responder_id: str
    intent_kind: str
    start_minute: int
    end_minute: int
    location_ref: str | None
    scope_ref: str | None
    alternative_ref: str | None
    priority: int
    hard: bool
    grace_minutes: int
    required_knowledge: tuple[str, ...]
    required_permissions: tuple[str, ...]
    requires_local_projection: bool
    requires_structured_mechanics: bool
    superseded_provenance_root: str
    proposal_provenance_root: str
    provenance_root: str


class AssistanceRenegotiationReplacementCommitmentLedger:
    """Historical link from delivered accepted replacement terms to a new agenda commitment."""

    def __init__(self) -> None:
        self.records: dict[str, AssistanceRenegotiationReplacementCommitmentRecord] = {}

    def add(
        self, record: AssistanceRenegotiationReplacementCommitmentRecord
    ) -> AssistanceRenegotiationReplacementCommitmentRecord:
        existing = self.records.get(record.commitment_id)
        if existing is not None:
            if existing != record:
                raise ValueError("replacement commitment id reused with conflicting content")
            return existing
        _validate_record(record)
        self.records[record.commitment_id] = record
        return record

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "records": [asdict(self.records[key]) for key in sorted(self.records)],
        }

    @classmethod
    def from_snapshot(
        cls, payload: Mapping[str, object]
    ) -> "AssistanceRenegotiationReplacementCommitmentLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported replacement commitment ledger schema")
        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("replacement commitment snapshot records must be a list")
        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("replacement commitment snapshot row must be an object")
            ledger.add(
                AssistanceRenegotiationReplacementCommitmentRecord(
                    commitment_id=str(raw["commitment_id"]),
                    supersedes_commitment_id=str(raw["supersedes_commitment_id"]),
                    replacement_proposal_id=str(raw["replacement_proposal_id"]),
                    proposal_decision_id=str(raw["proposal_decision_id"]),
                    decision_reply_event_id=str(raw["decision_reply_event_id"]),
                    requester_id=str(raw["requester_id"]),
                    responder_id=str(raw["responder_id"]),
                    intent_kind=str(raw["intent_kind"]),
                    start_minute=int(raw["start_minute"]),
                    end_minute=int(raw["end_minute"]),
                    location_ref=None if raw.get("location_ref") is None else str(raw["location_ref"]),
                    scope_ref=None if raw.get("scope_ref") is None else str(raw["scope_ref"]),
                    alternative_ref=None if raw.get("alternative_ref") is None else str(raw["alternative_ref"]),
                    priority=int(raw["priority"]),
                    hard=bool(raw["hard"]),
                    grace_minutes=int(raw["grace_minutes"]),
                    required_knowledge=tuple(str(v) for v in raw.get("required_knowledge", [])),
                    required_permissions=tuple(str(v) for v in raw.get("required_permissions", [])),
                    requires_local_projection=bool(raw["requires_local_projection"]),
                    requires_structured_mechanics=bool(raw["requires_structured_mechanics"]),
                    superseded_provenance_root=str(raw["superseded_provenance_root"]),
                    proposal_provenance_root=str(raw["proposal_provenance_root"]),
                    provenance_root=str(raw["provenance_root"]),
                )
            )
        return ledger


@dataclass(frozen=True)
class AssistanceRenegotiationReplacementCommitmentOutcome:
    record: AssistanceRenegotiationReplacementCommitmentRecord
    commitment: ScheduledCommitment


def _validate_record(record: AssistanceRenegotiationReplacementCommitmentRecord) -> None:
    required = (
        record.commitment_id,
        record.supersedes_commitment_id,
        record.replacement_proposal_id,
        record.proposal_decision_id,
        record.decision_reply_event_id,
        record.requester_id,
        record.responder_id,
        record.intent_kind,
        record.superseded_provenance_root,
        record.proposal_provenance_root,
        record.provenance_root,
    )
    if not all(required):
        raise ValueError("invalid replacement commitment identity")
    if record.commitment_id == record.supersedes_commitment_id:
        raise ValueError("replacement commitment requires a new commitment id")
    if record.requester_id == record.responder_id:
        raise ValueError("replacement commitment requires distinct actors")
    if min(record.start_minute, record.end_minute, record.priority, record.grace_minutes) < 0:
        raise ValueError("replacement commitment values must be non-negative")
    if record.end_minute < record.start_minute:
        raise ValueError("replacement commitment end cannot precede start")
    if record.provenance_root != record.proposal_decision_id:
        raise ValueError("replacement commitment provenance must begin at accepted replacement terms")


def _expected_reply_payload(proposal, decision) -> dict[str, object]:
    return {
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


def _scheduled_from_old(record) -> ScheduledCommitment:
    return ScheduledCommitment(
        commitment_id=record.commitment_id,
        intent_kind=record.intent_kind,
        start_minute=record.start_minute,
        end_minute=record.end_minute,
        priority=record.priority,
        hard=record.hard,
        grace_minutes=record.grace_minutes,
        required_knowledge=frozenset(record.required_knowledge),
        required_permissions=frozenset(record.required_permissions),
        target_ref=record.requester_id,
        requires_local_projection=record.requires_local_projection,
        requires_structured_mechanics=record.requires_structured_mechanics,
    )


def materialize_assistance_renegotiation_replacement_commitment(
    *,
    old_commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    proposal_ledger: AssistanceRenegotiationProposalLedger,
    decision_ledger: AssistanceRenegotiationProposalDecisionLedger,
    replacement_ledger: AssistanceRenegotiationReplacementCommitmentLedger,
    information_queue: InformationEventQueue,
    coordinator: GlobalNpcWorldEventCoordinator,
    proposal_decision_id: str,
    decision_reply_event_id: str,
    commitment_id: str,
    materialized_minute: int,
) -> AssistanceRenegotiationReplacementCommitmentOutcome:
    """Replace future agenda execution after the responder actually receives accepted new terms.

    Historical ledgers remain immutable. This owner only swaps the responder's
    executable schedule entry. It does not move an actor, reserve travel/resources,
    grant permissions, alter relationships, adjudicate blame, complete assistance,
    or invoke AutoPTU.
    """

    if not proposal_decision_id or not decision_reply_event_id or not commitment_id:
        raise ValueError("decision, reply event and replacement commitment ids are required")
    if materialized_minute < 0:
        raise ValueError("materialized_minute must be non-negative")

    decision = decision_ledger.records.get(proposal_decision_id)
    if decision is None:
        raise KeyError(f"unknown replacement-offer decision: {proposal_decision_id}")
    if decision.outcome != AssistanceRenegotiationProposalOutcome.ACCEPT.value:
        raise ValueError("replacement commitment requires ACCEPT_REPLACEMENT_TERMS")

    proposal = proposal_ledger.records.get(decision.proposal_id)
    if proposal is None:
        raise KeyError(f"unknown assistance renegotiation proposal: {decision.proposal_id}")
    if decision.supersedes_commitment_id != proposal.supersedes_commitment_id:
        raise ValueError("replacement commitment old commitment lineage mismatch")
    if decision.supersedes_proposal_id != proposal.supersedes_proposal_id:
        raise ValueError("replacement commitment old proposal lineage mismatch")
    if decision.requester_id != proposal.requester_id or decision.responder_id != proposal.responder_id:
        raise ValueError("replacement commitment actor binding mismatch")
    if decision.proposal_provenance_root != proposal.provenance_root:
        raise ValueError("replacement commitment proposal provenance mismatch")

    old = old_commitment_ledger.records.get(proposal.supersedes_commitment_id)
    if old is None:
        raise KeyError(f"unknown superseded assistance commitment: {proposal.supersedes_commitment_id}")
    if old.proposal_id != proposal.supersedes_proposal_id:
        raise ValueError("replacement commitment superseded proposal mismatch")
    if old.requester_id != proposal.requester_id or old.responder_id != proposal.responder_id:
        raise ValueError("replacement commitment superseded actor binding mismatch")

    envelope = information_queue.envelope_provenance(decision_reply_event_id)
    if envelope is None:
        raise KeyError(f"unknown replacement-offer decision reply: {decision_reply_event_id}")
    if information_queue.statuses.get(decision_reply_event_id) != DeliveryStatus.DELIVERED:
        raise ValueError("replacement commitment requires delivered acceptance reply")
    if envelope.sender_id != proposal.requester_id or envelope.receiver_id != proposal.responder_id:
        raise ValueError("replacement commitment acceptance reply actor binding mismatch")

    requester_ledger = information_queue.ledgers.get(proposal.requester_id)
    responder_ledger = information_queue.ledgers.get(proposal.responder_id)
    if requester_ledger is None or responder_ledger is None:
        raise KeyError("replacement commitment actors require knowledge ledgers")
    source_claim = requester_ledger.claims.get(envelope.source_claim_id)
    received_claim = responder_ledger.claims.get(envelope.new_claim_id)
    if source_claim is None or received_claim is None:
        raise ValueError("delivered replacement acceptance requires source and responder claims")
    if received_claim.source_kind is not SourceKind.REPORT:
        raise ValueError("replacement acceptance must be responder REPORT evidence")
    if received_claim.parent_claim_id != source_claim.claim_id:
        raise ValueError("replacement acceptance parent claim mismatch")
    if received_claim.provenance_root != decision.decision_id:
        raise ValueError("replacement acceptance provenance mismatch")
    if source_claim.subject != received_claim.subject or source_claim.value != received_claim.value:
        raise ValueError("replacement acceptance differs from authored reply")
    expected_subject = f"assistance_renegotiation_proposal_decision:{proposal.proposal_id}:{decision.decision_id}"
    if source_claim.subject != expected_subject:
        raise ValueError("replacement acceptance subject mismatch")
    try:
        payload = json.loads(received_claim.value)
    except json.JSONDecodeError as exc:
        raise ValueError("replacement acceptance reply is not structured payload") from exc
    if payload != _expected_reply_payload(proposal, decision):
        raise ValueError("replacement acceptance payload does not match durable history")
    if materialized_minute < received_claim.semantic_minute:
        raise ValueError("replacement commitment cannot predate responder receipt")
    if proposal.proposed_start_minute < materialized_minute:
        raise ValueError("accepted replacement window is already in the past")

    replacement = ScheduledCommitment(
        commitment_id=commitment_id,
        intent_kind=old.intent_kind,
        start_minute=proposal.proposed_start_minute,
        end_minute=proposal.proposed_end_minute,
        priority=old.priority,
        hard=old.hard,
        grace_minutes=old.grace_minutes,
        required_knowledge=frozenset(old.required_knowledge),
        required_permissions=frozenset(old.required_permissions),
        target_ref=old.requester_id,
        requires_local_projection=old.requires_local_projection,
        requires_structured_mechanics=old.requires_structured_mechanics,
    )
    record = AssistanceRenegotiationReplacementCommitmentRecord(
        commitment_id=commitment_id,
        supersedes_commitment_id=old.commitment_id,
        replacement_proposal_id=proposal.proposal_id,
        proposal_decision_id=decision.decision_id,
        decision_reply_event_id=decision_reply_event_id,
        requester_id=old.requester_id,
        responder_id=old.responder_id,
        intent_kind=old.intent_kind,
        start_minute=proposal.proposed_start_minute,
        end_minute=proposal.proposed_end_minute,
        location_ref=proposal.location_ref,
        scope_ref=proposal.scope_ref,
        alternative_ref=proposal.alternative_ref,
        priority=old.priority,
        hard=old.hard,
        grace_minutes=old.grace_minutes,
        required_knowledge=tuple(old.required_knowledge),
        required_permissions=tuple(old.required_permissions),
        requires_local_projection=old.requires_local_projection,
        requires_structured_mechanics=old.requires_structured_mechanics,
        superseded_provenance_root=old.provenance_root,
        proposal_provenance_root=proposal.provenance_root,
        provenance_root=decision.decision_id,
    )
    _validate_record(record)

    profile = coordinator.agendas.get(old.responder_id, AgentAgendaProfile())
    old_scheduled = _scheduled_from_old(old)
    old_matches = [row for row in profile.commitments if row.commitment_id == old.commitment_id]
    new_matches = [row for row in profile.commitments if row.commitment_id == commitment_id]

    existing = replacement_ledger.records.get(commitment_id)
    if existing is not None:
        if existing != record:
            raise ValueError("replacement commitment id reused with conflicting content")
        if old_matches:
            raise ValueError("replayed replacement commitment found superseded schedule still executable")
        if new_matches != [replacement]:
            raise ValueError("replayed replacement commitment agenda state mismatch")
        return AssistanceRenegotiationReplacementCommitmentOutcome(existing, replacement)

    if commitment_id == old.commitment_id:
        raise ValueError("replacement commitment requires a new commitment id")
    if old_matches != [old_scheduled]:
        raise ValueError("superseded commitment must exist exactly once in responder agenda")
    if new_matches:
        raise ValueError("agenda already contains replacement commitment id")

    replacement_ledger.add(record)
    coordinator.agendas[old.responder_id] = AgentAgendaProfile(
        goals=profile.goals,
        needs=profile.needs,
        commitments=tuple(
            replacement if row.commitment_id == old.commitment_id else row
            for row in profile.commitments
        ),
        situational_intents=profile.situational_intents,
        active_intent_id=profile.active_intent_id,
        continuity_bonus=profile.continuity_bonus,
    )
    return AssistanceRenegotiationReplacementCommitmentOutcome(record, replacement)
