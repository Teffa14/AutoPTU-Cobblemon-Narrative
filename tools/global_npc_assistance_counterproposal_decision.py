from __future__ import annotations

import json
from dataclasses import dataclass

from tools.global_npc_ai import Handoff
from tools.global_npc_assistance_counterproposal import AssistanceCounterproposalLedger
from tools.global_npc_information_network import DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import SourceKind
from tools.global_npc_world_action_intent import WorldActionIntentLedger, WorldActionIntentRecord
from tools.global_npc_world_event_coordinator import CoordinatedDecision

REQUEST_KIND = "REQUEST_ASSISTANCE"
COUNTERPROPOSE_KIND = "COUNTERPROPOSE_ASSISTANCE_REQUEST"
SUPPORTED_DECISION_KINDS = frozenset(
    {
        "ACCEPT_ASSISTANCE_COUNTERPROPOSAL",
        "REJECT_ASSISTANCE_COUNTERPROPOSAL",
    }
)


@dataclass(frozen=True)
class AssistanceCounterproposalDecisionOutcome:
    proposal_id: str
    request_action_id: str
    response_action_id: str
    decision_action_id: str
    requester_id: str
    responder_id: str
    decision_kind: str
    semantic_minute: int
    trigger_ids: tuple[str, ...]
    record: WorldActionIntentRecord


def _expected_terms(record) -> dict[str, object]:
    return {
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


def _validate_delivered_terms(
    *,
    action_ledger: WorldActionIntentLedger,
    proposal_ledger: AssistanceCounterproposalLedger,
    information_queue: InformationEventQueue,
    proposal_id: str,
    terms_event_id: str,
):
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
        raise ValueError("counterproposal references a non-counterproposal response")
    if response.agent_id != proposal.responder_id or response.target_ref != proposal.requester_id:
        raise ValueError("counterproposal response actor binding mismatch")

    envelope = information_queue.envelope_provenance(terms_event_id)
    if envelope is None:
        raise KeyError(f"unknown counterproposal terms event: {terms_event_id}")
    if envelope.sender_id != proposal.responder_id or envelope.receiver_id != proposal.requester_id:
        raise ValueError("counterproposal terms envelope actor binding mismatch")
    if information_queue.statuses.get(terms_event_id) != DeliveryStatus.DELIVERED:
        raise ValueError("counterproposal decision requires terminal DELIVERED terms")

    sender_ledger = information_queue.ledgers.get(proposal.responder_id)
    requester_ledger = information_queue.ledgers.get(proposal.requester_id)
    if sender_ledger is None or requester_ledger is None:
        raise KeyError("counterproposal actors require knowledge ledgers")
    source_claim = sender_ledger.claims.get(envelope.source_claim_id)
    received_claim = requester_ledger.claims.get(envelope.new_claim_id)
    if source_claim is None or received_claim is None:
        raise ValueError("DELIVERED counterproposal terms require both source and requester claims")

    expected_subject = (
        f"assistance_counterproposal_terms:{proposal.request_action_id}:"
        f"{proposal.response_action_id}:{proposal.proposal_id}"
    )
    if source_claim.subject != expected_subject or received_claim.subject != expected_subject:
        raise ValueError("counterproposal terms subject mismatch")
    if source_claim.provenance_root != proposal.response_action_id:
        raise ValueError("counterproposal source claim provenance mismatch")
    if received_claim.provenance_root != proposal.response_action_id:
        raise ValueError("counterproposal requester claim provenance mismatch")
    if received_claim.source_kind is not SourceKind.REPORT:
        raise ValueError("counterproposal requester claim must be delivered REPORT evidence")
    if received_claim.parent_claim_id != source_claim.claim_id:
        raise ValueError("counterproposal requester claim parent mismatch")
    if received_claim.value != source_claim.value:
        raise ValueError("counterproposal delivered terms differ from authored terms")
    try:
        decoded = json.loads(received_claim.value)
    except json.JSONDecodeError as exc:
        raise ValueError("counterproposal delivered terms are not valid structured payload") from exc
    if decoded != _expected_terms(proposal):
        raise ValueError("counterproposal delivered terms do not match durable proposal")

    return proposal, request, response, envelope


def record_assistance_counterproposal_decision_from_replan(
    *,
    action_ledger: WorldActionIntentLedger,
    proposal_ledger: AssistanceCounterproposalLedger,
    information_queue: InformationEventQueue,
    proposal_id: str,
    terms_event_id: str,
    decision_action_id: str,
    coordinated_decision: CoordinatedDecision,
    semantic_minute: int,
) -> AssistanceCounterproposalDecisionOutcome:
    """Record the requester's explicit decision about one delivered proposal.

    The resulting world action names the exact proposal in source_ref. It does
    not create a commitment, reserve time or travel, allocate resources, mutate
    relationships, execute the proposed work, or invoke AutoPTU.
    """
    if not decision_action_id:
        raise ValueError("decision_action_id is required")
    if semantic_minute < 0:
        raise ValueError("semantic_minute must be non-negative")

    proposal, request, response, envelope = _validate_delivered_terms(
        action_ledger=action_ledger,
        proposal_ledger=proposal_ledger,
        information_queue=information_queue,
        proposal_id=proposal_id,
        terms_event_id=terms_event_id,
    )
    if decision_action_id in {request.action_id, response.action_id}:
        raise ValueError("counterproposal decision requires its own action identity")
    if semantic_minute < response.semantic_minute:
        raise ValueError("counterproposal decision cannot predate the proposal response")

    expected_trigger = f"replan:information:{envelope.event_id}"
    if coordinated_decision.agent_id != proposal.requester_id:
        raise ValueError("counterproposal decision actor must be the original requester")
    if expected_trigger not in coordinated_decision.trigger_ids:
        raise ValueError("counterproposal decision lacks the terms-delivery replan trigger")

    agenda = coordinated_decision.decision
    decision = agenda.decision
    if decision.agent_id != proposal.requester_id:
        raise ValueError("counterproposal decision identity mismatch")
    if decision.intent_id is None or not decision.intent_id:
        raise ValueError("counterproposal decision requires a selected intent")
    if decision.kind not in SUPPORTED_DECISION_KINDS:
        raise ValueError("unsupported assistance counterproposal decision kind")
    if decision.handoff != Handoff.NONE:
        raise ValueError("counterproposal decision cannot itself be an AutoPTU handoff")
    if decision.target_ref != proposal.responder_id:
        raise ValueError("counterproposal decision must target the proposal author")
    if agenda.source_ref != proposal.proposal_id:
        raise ValueError("counterproposal decision must name the exact proposal in source_ref")

    if (
        decision.kind == "ACCEPT_ASSISTANCE_COUNTERPROPOSAL"
        and proposal.expires_minute is not None
        and semantic_minute > proposal.expires_minute
    ):
        raise ValueError("expired assistance counterproposal cannot be accepted")

    record = action_ledger.record_from_replan(
        action_id=decision_action_id,
        coordinated_decision=coordinated_decision,
        semantic_minute=semantic_minute,
    )
    return AssistanceCounterproposalDecisionOutcome(
        proposal_id=proposal.proposal_id,
        request_action_id=request.action_id,
        response_action_id=response.action_id,
        decision_action_id=record.action_id,
        requester_id=proposal.requester_id,
        responder_id=proposal.responder_id,
        decision_kind=record.intent_kind,
        semantic_minute=record.semantic_minute,
        trigger_ids=record.trigger_ids,
        record=record,
    )
