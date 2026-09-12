from dataclasses import replace
import json

import pytest

from tools.global_npc_ai import AgentMode, NpcAgentState, ScheduledCommitment
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)
from tools.global_npc_assistance_renegotiation_proposal import (
    AssistanceRenegotiationProposalLedger,
    AssistanceRenegotiationProposalRecord,
)
from tools.global_npc_assistance_renegotiation_proposal_decision import (
    AssistanceRenegotiationProposalDecisionLedger,
    AssistanceRenegotiationProposalDecisionRecord,
    AssistanceRenegotiationProposalOutcome,
)
from tools.global_npc_assistance_renegotiation_replacement_commitment import (
    AssistanceRenegotiationReplacementCommitmentLedger,
    materialize_assistance_renegotiation_replacement_commitment,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
OLD_COMMITMENT = "commitment:pass449-original"
OLD_PROPOSAL = "proposal:pass449-original"
NEW_PROPOSAL = "proposal:pass449-replacement"
DECISION = "decision:pass449-replacement"
REPLY_EVENT = "event:pass449-replacement-decision"
NEW_COMMITMENT = "commitment:pass449-replacement"


def _reply_payload(proposal, decision):
    return json.dumps(
        {
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
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _state(*, outcome=AssistanceRenegotiationProposalOutcome.ACCEPT, deliver=True):
    old = AssistanceCounterproposalCommitmentLedger()
    old_record = AssistanceCounterproposalCommitmentRecord(
        commitment_id=OLD_COMMITMENT,
        proposal_id=OLD_PROPOSAL,
        request_action_id="request:pass449",
        response_action_id="counterproposal:pass449",
        decision_action_id="accept:pass449-original",
        requester_id=MARA,
        responder_id=TEO,
        intent_kind="ASSIST_ROUTE_INSPECTION",
        start_minute=1540,
        end_minute=1580,
        location_ref="ouros.route.old-causeway",
        scope_ref="survey_only",
        alternative_ref=None,
        priority=7,
        hard=True,
        grace_minutes=5,
        required_knowledge=("claim:site-access",),
        required_permissions=("permit:survey",),
        requires_local_projection=False,
        requires_structured_mechanics=False,
        provenance_root="accept:pass449-original",
    )
    old.add(old_record)

    proposals = AssistanceRenegotiationProposalLedger()
    proposal = AssistanceRenegotiationProposalRecord(
        proposal_id=NEW_PROPOSAL,
        supersedes_commitment_id=OLD_COMMITMENT,
        supersedes_proposal_id=OLD_PROPOSAL,
        decision_id="decision:allow-reopening-pass449",
        decision_reply_event_id="event:allow-reopening-pass449",
        requester_id=MARA,
        responder_id=TEO,
        proposed_start_minute=1620,
        proposed_end_minute=1665,
        location_ref="ouros.route.new-causeway",
        scope_ref="survey_only",
        alternative_ref="remote_report",
        expires_minute=1600,
        semantic_minute=1510,
        decision_provenance_root="decision:allow-reopening-pass449",
        provenance_root=NEW_PROPOSAL,
    )
    proposals.add(proposal)

    decisions = AssistanceRenegotiationProposalDecisionLedger()
    decision = AssistanceRenegotiationProposalDecisionRecord(
        decision_id=DECISION,
        proposal_id=NEW_PROPOSAL,
        supersedes_commitment_id=OLD_COMMITMENT,
        supersedes_proposal_id=OLD_PROPOSAL,
        proposal_event_id="event:replacement-offer-pass449",
        requester_id=MARA,
        responder_id=TEO,
        outcome=outcome.value,
        semantic_minute=1514,
        rationale_ref="reason:pass449-answer",
        proposal_provenance_root=NEW_PROPOSAL,
        provenance_root=NEW_PROPOSAL,
    )
    decisions.add(decision)

    ledgers = {MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)}
    queue = InformationEventQueue(
        channels={"radio": CommunicationChannel("radio", "REMOTE_MESSAGE", 0)},
        ledgers=ledgers,
    )
    subject = f"assistance_renegotiation_proposal_decision:{NEW_PROPOSAL}:{DECISION}"
    ledgers[MARA].add(
        Claim(
            claim_id="claim:mara-pass449-decision",
            subject=subject,
            value=_reply_payload(proposal, decision),
            source_kind=SourceKind.AUTHORED_START,
            source_agent_id=MARA,
            semantic_minute=1515,
            confidence=100,
            provenance_root=DECISION,
        )
    )
    queue.schedule(
        event_id=REPLY_EVENT,
        message_id="message:pass449-decision",
        sender_id=MARA,
        receiver_id=TEO,
        source_claim_id="claim:mara-pass449-decision",
        new_claim_id="claim:teo-pass449-decision",
        channel_id="radio",
        created_minute=1515,
    )
    if deliver:
        queue.process_due(1515)

    old_schedule = ScheduledCommitment(
        commitment_id=OLD_COMMITMENT,
        intent_kind=old_record.intent_kind,
        start_minute=old_record.start_minute,
        end_minute=old_record.end_minute,
        priority=old_record.priority,
        hard=old_record.hard,
        grace_minutes=old_record.grace_minutes,
        required_knowledge=frozenset(old_record.required_knowledge),
        required_permissions=frozenset(old_record.required_permissions),
        target_ref=MARA,
        requires_local_projection=False,
        requires_structured_mechanics=False,
    )
    agents = {
        MARA: NpcAgentState(MARA, AgentMode.OFFSCREEN_NAMED, "ouros", "requester-site"),
        TEO: NpcAgentState(TEO, AgentMode.OFFSCREEN_NAMED, "ouros", "workshop"),
    }
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents=agents,
        agendas={TEO: AgentAgendaProfile(commitments=(old_schedule,))},
    )
    return old, proposals, decisions, queue, coordinator, proposal, decision, old_record


def _materialize(state, ledger=None, **overrides):
    old, proposals, decisions, queue, coordinator, *_ = state
    ledger = ledger or AssistanceRenegotiationReplacementCommitmentLedger()
    values = dict(
        old_commitment_ledger=old,
        proposal_ledger=proposals,
        decision_ledger=decisions,
        replacement_ledger=ledger,
        information_queue=queue,
        coordinator=coordinator,
        proposal_decision_id=DECISION,
        decision_reply_event_id=REPLY_EVENT,
        commitment_id=NEW_COMMITMENT,
        materialized_minute=1516,
    )
    values.update(overrides)
    return ledger, materialize_assistance_renegotiation_replacement_commitment(**values)


def test_delivered_acceptance_replaces_future_agenda_entry_and_preserves_old_history():
    state = _state()
    old, proposals, decisions, _, coordinator, proposal, decision, old_record = state
    ledger, outcome = _materialize(state)

    agenda = coordinator.agendas[TEO]
    assert [row.commitment_id for row in agenda.commitments] == [NEW_COMMITMENT]
    replacement = agenda.commitments[0]
    assert replacement.start_minute == 1620
    assert replacement.end_minute == 1665
    assert replacement.intent_kind == old_record.intent_kind
    assert replacement.priority == old_record.priority
    assert replacement.target_ref == MARA
    assert old.records[OLD_COMMITMENT] == old_record
    assert proposals.records[NEW_PROPOSAL] == proposal
    assert decisions.records[DECISION] == decision
    assert outcome.record.supersedes_commitment_id == OLD_COMMITMENT
    assert outcome.record.provenance_root == DECISION
    assert ledger.records[NEW_COMMITMENT] == outcome.record


def test_acceptance_must_reach_responder_before_replacement_exists():
    state = _state(deliver=False)
    with pytest.raises(ValueError, match="delivered acceptance reply"):
        _materialize(state)
    assert [row.commitment_id for row in state[4].agendas[TEO].commitments] == [OLD_COMMITMENT]


def test_rejection_cannot_create_replacement_commitment():
    state = _state(outcome=AssistanceRenegotiationProposalOutcome.REJECT)
    with pytest.raises(ValueError, match="ACCEPT_REPLACEMENT_TERMS"):
        _materialize(state)
    assert [row.commitment_id for row in state[4].agendas[TEO].commitments] == [OLD_COMMITMENT]


def test_tampered_lineage_or_reply_payload_fails_closed():
    state = _state()
    decisions = state[2]
    original = decisions.records[DECISION]
    decisions.records[DECISION] = replace(original, supersedes_commitment_id="commitment:other")
    with pytest.raises(ValueError, match="old commitment lineage"):
        _materialize(state)

    state = _state()
    queue = state[3]
    claim = queue.ledgers[TEO].claims["claim:teo-pass449-decision"]
    queue.ledgers[TEO].claims[claim.claim_id] = replace(claim, value='{"tampered":true}')
    with pytest.raises(ValueError, match="differs from authored reply|does not match durable history"):
        _materialize(state)


def test_replacement_window_cannot_already_be_in_the_past():
    state = _state()
    with pytest.raises(ValueError, match="already in the past"):
        _materialize(state, materialized_minute=1621)


def test_exact_replay_is_idempotent_but_conflicting_reuse_fails():
    state = _state()
    ledger, first = _materialize(state)
    _, second = _materialize(state, ledger=ledger)
    assert second == first

    with pytest.raises(ValueError, match="conflicting content"):
        _materialize(state, ledger=ledger, commitment_id=NEW_COMMITMENT, materialized_minute=1517)


def test_snapshot_round_trip_keeps_lineage():
    state = _state()
    ledger, first = _materialize(state)
    restored = AssistanceRenegotiationReplacementCommitmentLedger.from_snapshot(ledger.snapshot())
    assert restored.records[NEW_COMMITMENT] == first.record


def test_replacement_owner_has_no_tactical_or_social_execution_surface():
    import inspect
    import tools.global_npc_assistance_renegotiation_replacement_commitment as module

    source = inspect.getsource(module)
    forbidden = (
        "REQUEST_AUTOPTU",
        "reserve_route",
        "allocate_resource",
        "move_actor",
        "relationship_delta",
        "grant_permission",
        "adjudicate_blame",
    )
    assert all(token not in source for token in forbidden)
