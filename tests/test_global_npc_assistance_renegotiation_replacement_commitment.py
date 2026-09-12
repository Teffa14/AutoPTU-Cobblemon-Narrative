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

REQUESTER = "ouros.npc.mara_veyra"
RESPONDER = "ouros.npc.teo_lark"
OLD = "commitment:pass449-old"
OLD_PROPOSAL = "proposal:pass449-old"
PROPOSAL = "proposal:pass449-new"
DECISION = "decision:pass449-new"
REPLY = "event:pass449-answer"
NEW = "commitment:pass449-new"


def _fixture(*, outcome=AssistanceRenegotiationProposalOutcome.ACCEPT, deliver=True):
    old_ledger = AssistanceCounterproposalCommitmentLedger()
    old = AssistanceCounterproposalCommitmentRecord(
        commitment_id=OLD,
        proposal_id=OLD_PROPOSAL,
        request_action_id="request:449",
        response_action_id="counter:449",
        decision_action_id="accept:449-old",
        requester_id=REQUESTER,
        responder_id=RESPONDER,
        intent_kind="ASSIST_ROUTE_INSPECTION",
        start_minute=1540,
        end_minute=1580,
        location_ref="ouros.route.old",
        scope_ref="survey_only",
        alternative_ref=None,
        priority=7,
        hard=True,
        grace_minutes=5,
        required_knowledge=("claim:access",),
        required_permissions=("permit:survey",),
        requires_local_projection=False,
        requires_structured_mechanics=False,
        provenance_root="accept:449-old",
    )
    old_ledger.add(old)

    proposals = AssistanceRenegotiationProposalLedger()
    proposal = AssistanceRenegotiationProposalRecord(
        proposal_id=PROPOSAL,
        supersedes_commitment_id=OLD,
        supersedes_proposal_id=OLD_PROPOSAL,
        decision_id="decision:449-reopen",
        decision_reply_event_id="event:449-reopen",
        requester_id=REQUESTER,
        responder_id=RESPONDER,
        proposed_start_minute=1620,
        proposed_end_minute=1665,
        location_ref="ouros.route.new",
        scope_ref="survey_only",
        alternative_ref="remote_report",
        expires_minute=1600,
        semantic_minute=1510,
        decision_provenance_root="decision:449-reopen",
        provenance_root=PROPOSAL,
    )
    proposals.add(proposal)

    decisions = AssistanceRenegotiationProposalDecisionLedger()
    decision = AssistanceRenegotiationProposalDecisionRecord(
        decision_id=DECISION,
        proposal_id=PROPOSAL,
        supersedes_commitment_id=OLD,
        supersedes_proposal_id=OLD_PROPOSAL,
        proposal_event_id="event:449-offer",
        requester_id=REQUESTER,
        responder_id=RESPONDER,
        outcome=outcome.value,
        semantic_minute=1514,
        rationale_ref="reason:449-answer",
        proposal_provenance_root=PROPOSAL,
        provenance_root=PROPOSAL,
    )
    decisions.add(decision)

    payload = json.dumps(
        {
            "decision_id": DECISION,
            "proposal_id": PROPOSAL,
            "supersedes_commitment_id": OLD,
            "supersedes_proposal_id": OLD_PROPOSAL,
            "proposal_event_id": decision.proposal_event_id,
            "requester_id": REQUESTER,
            "responder_id": RESPONDER,
            "outcome": decision.outcome,
            "decision_rationale_ref": decision.rationale_ref,
            "decision_minute": decision.semantic_minute,
            "proposed_start_minute": proposal.proposed_start_minute,
            "proposed_end_minute": proposal.proposed_end_minute,
            "location_ref": proposal.location_ref,
            "scope_ref": proposal.scope_ref,
            "alternative_ref": proposal.alternative_ref,
            "expires_minute": proposal.expires_minute,
            "proposal_provenance_root": PROPOSAL,
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    ledgers = {REQUESTER: KnowledgeLedger(REQUESTER), RESPONDER: KnowledgeLedger(RESPONDER)}
    queue = InformationEventQueue(
        channels={"radio": CommunicationChannel("radio", "REMOTE_MESSAGE", 0)},
        ledgers=ledgers,
    )
    ledgers[REQUESTER].add(
        Claim(
            claim_id="claim:requester:449-answer",
            subject=f"assistance_renegotiation_proposal_decision:{PROPOSAL}:{DECISION}",
            value=payload,
            source_kind=SourceKind.AUTHORED_START,
            source_agent_id=REQUESTER,
            semantic_minute=1515,
            confidence=100,
            provenance_root=DECISION,
        )
    )
    queue.schedule(
        event_id=REPLY,
        message_id="message:449-answer",
        sender_id=REQUESTER,
        receiver_id=RESPONDER,
        source_claim_id="claim:requester:449-answer",
        new_claim_id="claim:responder:449-answer",
        channel_id="radio",
        created_minute=1515,
    )
    if deliver:
        queue.process_due(1515)

    old_schedule = ScheduledCommitment(
        commitment_id=OLD,
        intent_kind=old.intent_kind,
        start_minute=old.start_minute,
        end_minute=old.end_minute,
        priority=old.priority,
        hard=old.hard,
        grace_minutes=old.grace_minutes,
        required_knowledge=frozenset(old.required_knowledge),
        required_permissions=frozenset(old.required_permissions),
        target_ref=REQUESTER,
        requires_local_projection=False,
        requires_structured_mechanics=False,
    )
    agents = {
        REQUESTER: NpcAgentState(REQUESTER, AgentMode.OFFSCREEN_NAMED, "ouros", "site"),
        RESPONDER: NpcAgentState(RESPONDER, AgentMode.OFFSCREEN_NAMED, "ouros", "workshop"),
    }
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents=agents,
        agendas={RESPONDER: AgentAgendaProfile(commitments=(old_schedule,))},
    )
    return old_ledger, proposals, decisions, queue, coordinator, old


def _materialize(state, ledger=None):
    old, proposals, decisions, queue, coordinator, _ = state
    ledger = ledger or AssistanceRenegotiationReplacementCommitmentLedger()
    outcome = materialize_assistance_renegotiation_replacement_commitment(
        old_commitment_ledger=old,
        proposal_ledger=proposals,
        decision_ledger=decisions,
        replacement_ledger=ledger,
        information_queue=queue,
        coordinator=coordinator,
        proposal_decision_id=DECISION,
        decision_reply_event_id=REPLY,
        commitment_id=NEW,
        materialized_minute=1516,
    )
    return ledger, outcome


def test_delivered_acceptance_replaces_only_future_schedule_and_keeps_history():
    state = _fixture()
    ledger, outcome = _materialize(state)
    agenda = state[4].agendas[RESPONDER].commitments
    assert [row.commitment_id for row in agenda] == [NEW]
    assert (agenda[0].start_minute, agenda[0].end_minute) == (1620, 1665)
    assert agenda[0].priority == state[5].priority
    assert state[0].records[OLD] == state[5]
    assert outcome.record.supersedes_commitment_id == OLD
    assert outcome.record.provenance_root == DECISION
    assert AssistanceRenegotiationReplacementCommitmentLedger.from_snapshot(
        ledger.snapshot()
    ).records[NEW] == outcome.record
    assert _materialize(state, ledger=ledger)[1] == outcome


def test_missing_delivery_or_rejection_cannot_replace_schedule():
    state = _fixture(deliver=False)
    with pytest.raises(ValueError, match="delivered acceptance reply"):
        _materialize(state)
    assert [row.commitment_id for row in state[4].agendas[RESPONDER].commitments] == [OLD]

    state = _fixture(outcome=AssistanceRenegotiationProposalOutcome.REJECT)
    with pytest.raises(ValueError, match="ACCEPT_REPLACEMENT_TERMS"):
        _materialize(state)
    assert [row.commitment_id for row in state[4].agendas[RESPONDER].commitments] == [OLD]


def test_owner_has_no_tactical_or_social_execution_surface():
    import inspect
    import tools.global_npc_assistance_renegotiation_replacement_commitment as module

    source = inspect.getsource(module)
    assert all(
        token not in source
        for token in (
            "REQUEST_AUTOPTU",
            "reserve_route",
            "allocate_resource",
            "move_actor",
            "relationship_delta",
            "grant_permission",
            "adjudicate_blame",
        )
    )
