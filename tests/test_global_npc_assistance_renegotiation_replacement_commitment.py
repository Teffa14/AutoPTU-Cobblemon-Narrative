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
OLD = "commitment:pass449-old"
OLD_PROPOSAL = "proposal:pass449-old"
PROPOSAL = "proposal:pass449-new"
DECISION = "decision:pass449-new"
REPLY = "event:pass449-new-decision"
NEW = "commitment:pass449-new"


def _state(*, outcome=AssistanceRenegotiationProposalOutcome.ACCEPT, deliver=True):
    old_ledger = AssistanceCounterproposalCommitmentLedger()
    old = AssistanceCounterproposalCommitmentRecord(
        commitment_id=OLD,
        proposal_id=OLD_PROPOSAL,
        request_action_id="request:449",
        response_action_id="counter:449",
        decision_action_id="accept:449-old",
        requester_id=MARA,
        responder_id=TEO,
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

    proposal_ledger = AssistanceRenegotiationProposalLedger()
    proposal = AssistanceRenegotiationProposalRecord(
        proposal_id=PROPOSAL,
        supersedes_commitment_id=OLD,
        supersedes_proposal_id=OLD_PROPOSAL,
        decision_id="decision:449-reopen",
        decision_reply_event_id="event:449-reopen",
        requester_id=MARA,
        responder_id=TEO,
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
    proposal_ledger.add(proposal)

    decision_ledger = AssistanceRenegotiationProposalDecisionLedger()
    decision = AssistanceRenegotiationProposalDecisionRecord(
        decision_id=DECISION,
        proposal_id=PROPOSAL,
        supersedes_commitment_id=OLD,
        supersedes_proposal_id=OLD_PROPOSAL,
        proposal_event_id="event:449-offer",
        requester_id=MARA,
        responder_id=TEO,
        outcome=outcome.value,
        semantic_minute=1514,
        rationale_ref="reason:449-answer",
        proposal_provenance_root=PROPOSAL,
        provenance_root=PROPOSAL,
    )
    decision_ledger.add(decision)

    payload = json.dumps(
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
    ledgers = {MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)}
    queue = InformationEventQueue(
        channels={"radio": CommunicationChannel("radio", "REMOTE_MESSAGE", 0)},
        ledgers=ledgers,
    )
    subject = f"assistance_renegotiation_proposal_decision:{PROPOSAL}:{DECISION}"
    ledgers[MARA].add(
        Claim(
            claim_id="claim:mara:449-answer",
            subject=subject,
            value=payload,
            source_kind=SourceKind.AUTHORED_START,
            source_agent_id=MARA,
            semantic_minute=1515,
            confidence=100,
            provenance_root=DECISION,
        )
    )
    queue.schedule(
        event_id=REPLY,
        message_id="message:449-answer",
        sender_id=MARA,
        receiver_id=TEO,
        source_claim_id="claim:mara:449-answer",
        new_claim_id="claim:teo:449-answer",
        channel_id="radio",
        created_minute=1515,
    )
    if deliver:
        queue.process_due(1515)

    scheduled_old = ScheduledCommitment(
        commitment_id=OLD,
        intent_kind=old.intent_kind,
        start_minute=old.start_minute,
        end_minute=old.end_minute,
        priority=old.priority,
        hard=old.hard,
        grace_minutes=old.grace_minutes,
        required_knowledge=frozenset(old.required_knowledge),
        required_permissions=frozenset(old.required_permissions),
        target_ref=MARA,
        requires_local_projection=False,
        requires_structured_mechanics=False,
    )
    agents = {
        MARA: NpcAgentState(MARA, AgentMode.OFFSCREEN_NAMED, "ouros", "site"),
        TEO: NpcAgentState(TEO, AgentMode.OFFSCREEN_NAMED, "ouros", "workshop"),
    }
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents=agents,
        agendas={TEO: AgentAgendaProfile(commitments=(scheduled_old,))},
    )
    return old_ledger, proposal_ledger, decision_ledger, queue, coordinator, old, proposal


def _run(state, ledger=None, **overrides):
    old, proposals, decisions, queue, coordinator, *_ = state
    replacement_ledger = ledger or AssistanceRenegotiationReplacementCommitmentLedger()
    args = dict(
        old_commitment_ledger=old,
        proposal_ledger=proposals,
        decision_ledger=decisions,
        replacement_ledger=replacement_ledger,
        information_queue=queue,
        coordinator=coordinator,
        proposal_decision_id=DECISION,
        decision_reply_event_id=REPLY,
        commitment_id=NEW,
        materialized_minute=1516,
    )
    args.update(overrides)
    return replacement_ledger, materialize_assistance_renegotiation_replacement_commitment(**args)


def test_delivered_acceptance_swaps_executable_schedule_but_keeps_old_history():
    state = _state()
    old_ledger, proposal_ledger, decision_ledger, _, coordinator, old, proposal = state
    ledger, outcome = _run(state)

    agenda = coordinator.agendas[TEO].commitments
    assert [row.commitment_id for row in agenda] == [NEW]
    assert agenda[0].start_minute == 1620
    assert agenda[0].end_minute == 1665
    assert agenda[0].priority == old.priority
    assert old_ledger.records[OLD] == old
    assert proposal_ledger.records[PROPOSAL] == proposal
    assert decision_ledger.records[DECISION].outcome == "ACCEPT_REPLACEMENT_TERMS"
    assert outcome.record.supersedes_commitment_id == OLD
    assert outcome.record.provenance_root == DECISION
    assert ledger.records[NEW] == outcome.record


def test_delivery_and_acceptance_are_both_required():
    state = _state(deliver=False)
    with pytest.raises(ValueError, match="delivered acceptance reply"):
        _run(state)
    assert [row.commitment_id for row in state[4].agendas[TEO].commitments] == [OLD]

    state = _state(outcome=AssistanceRenegotiationProposalOutcome.REJECT)
    with pytest.raises(ValueError, match="ACCEPT_REPLACEMENT_TERMS"):
        _run(state)
    assert [row.commitment_id for row in state[4].agendas[TEO].commitments] == [OLD]


def test_lineage_payload_and_time_tampering_fail_closed():
    state = _state()
    original = state[2].records[DECISION]
    state[2].records[DECISION] = replace(original, supersedes_commitment_id="commitment:other")
    with pytest.raises(ValueError, match="old commitment lineage"):
        _run(state)

    state = _state()
    claim = state[3].ledgers[TEO].claims["claim:teo:449-answer"]
    state[3].ledgers[TEO].claims[claim.claim_id] = replace(claim, value='{"tampered":true}')
    with pytest.raises(ValueError, match="differs from authored reply|does not match durable history"):
        _run(state)

    state = _state()
    with pytest.raises(ValueError, match="already in the past"):
        _run(state, materialized_minute=1621)


def test_replay_snapshot_and_conflicting_reuse_are_deterministic():
    state = _state()
    ledger, first = _run(state)
    _, second = _run(state, ledger=ledger)
    assert second == first
    restored = AssistanceRenegotiationReplacementCommitmentLedger.from_snapshot(ledger.snapshot())
    assert restored.records[NEW] == first.record

    state[1].records[PROPOSAL] = replace(state[1].records[PROPOSAL], proposed_start_minute=1630)
    with pytest.raises(ValueError, match="conflicting content|agenda state mismatch"):
        _run(state, ledger=ledger)


def test_owner_does_not_execute_tactics_or_social_consequences():
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
