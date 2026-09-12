from dataclasses import replace

import pytest

from tools.global_npc_assistance_commitment_disposition import (
    AssistanceCommitmentDisposition,
    AssistanceCommitmentDispositionLedger,
    CommitmentStartDisposition,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)
from tools.global_npc_assistance_renegotiation_decision import (
    AssistanceRenegotiationDecision,
    AssistanceRenegotiationDecisionLedger,
    record_assistance_renegotiation_decision,
)
from tools.global_npc_assistance_renegotiation_decision_dispatch import (
    schedule_assistance_renegotiation_decision_reply,
)
from tools.global_npc_assistance_renegotiation_dispatch import schedule_assistance_renegotiation_request
from tools.global_npc_assistance_renegotiation_proposal import (
    AssistanceRenegotiationProposalLedger,
    record_assistance_renegotiation_proposal,
)
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
COMMITMENT = "commitment:negotiated-help-pass445"
OLD_PROPOSAL = "proposal:pass445-old"
DISPOSITION = "start-disposition:pass445"
REQUEST_EVENT = "event:renegotiation-request-pass445"
DECISION = "renegotiation-decision:pass445"
REPLY_EVENT = "event:renegotiation-decision-reply-pass445"
NEW_PROPOSAL = "proposal:pass445-replacement"


def _state(*, reply_latency=0, deliver_reply=True):
    commitments = AssistanceCounterproposalCommitmentLedger()
    commitments.add(
        AssistanceCounterproposalCommitmentRecord(
            commitment_id=COMMITMENT,
            proposal_id=OLD_PROPOSAL,
            request_action_id="action:request-pass445",
            response_action_id="action:counter-pass445",
            decision_action_id="action:accept-pass445",
            requester_id=MARA,
            responder_id=TEO,
            intent_kind="FULFILL_NEGOTIATED_ASSISTANCE",
            start_minute=1500,
            end_minute=1540,
            location_ref="ouros.route.causeway-survey",
            scope_ref="survey_only",
            alternative_ref="remote_report",
            priority=8,
            hard=False,
            grace_minutes=5,
            required_knowledge=(),
            required_permissions=(),
            requires_local_projection=False,
            requires_structured_mechanics=False,
            provenance_root="action:accept-pass445",
        )
    )
    dispositions = AssistanceCommitmentDispositionLedger()
    dispositions.add(
        AssistanceCommitmentDisposition(
            disposition_id=DISPOSITION,
            commitment_id=COMMITMENT,
            proposal_id=OLD_PROPOSAL,
            assessment_id="start-assessment:pass445",
            requester_id=MARA,
            responder_id=TEO,
            actor_id=TEO,
            semantic_minute=1501,
            disposition=CommitmentStartDisposition.REQUEST_RENEGOTIATION.value,
            rationale_ref="reason:route-still-closed",
            provenance_root="decision:teo-renegotiate-pass445",
        )
    )
    queue = InformationEventQueue(
        channels={
            "channel:request": CommunicationChannel("channel:request", "RADIO", 0),
            "channel:reply": CommunicationChannel("channel:reply", "RADIO", reply_latency),
        },
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)},
    )
    schedule_assistance_renegotiation_request(
        commitment_ledger=commitments,
        disposition_ledger=dispositions,
        information_queue=queue,
        disposition_id=DISPOSITION,
        event_id=REQUEST_EVENT,
        message_id="message:request-pass445",
        source_claim_id="claim:teo-request-pass445",
        receiver_claim_id="claim:mara-request-pass445",
        channel_id="channel:request",
        created_minute=1502,
    )
    queue.process_due(1502)
    decisions = AssistanceRenegotiationDecisionLedger()
    record_assistance_renegotiation_decision(
        commitment_ledger=commitments,
        disposition_ledger=dispositions,
        information_queue=queue,
        decision_ledger=decisions,
        request_event_id=REQUEST_EVENT,
        decision_id=DECISION,
        decision=AssistanceRenegotiationDecision.ACCEPT_REOPENING,
        requester_id=MARA,
        semantic_minute=1503,
        rationale_ref="reason:open-to-new-window",
    )
    schedule_assistance_renegotiation_decision_reply(
        commitment_ledger=commitments,
        disposition_ledger=dispositions,
        decision_ledger=decisions,
        information_queue=queue,
        decision_id=DECISION,
        event_id=REPLY_EVENT,
        message_id="message:reply-pass445",
        source_claim_id="claim:mara-reply-pass445",
        receiver_claim_id="claim:teo-reply-pass445",
        channel_id="channel:reply",
        created_minute=1504,
    )
    if deliver_reply:
        queue.process_due(1504 + reply_latency)
    return commitments, decisions, queue


def _record(commitments, decisions, queue, ledger=None, **overrides):
    ledger = ledger or AssistanceRenegotiationProposalLedger()
    values = dict(
        commitment_ledger=commitments,
        decision_ledger=decisions,
        information_queue=queue,
        proposal_ledger=ledger,
        decision_id=DECISION,
        decision_reply_event_id=REPLY_EVENT,
        proposal_id=NEW_PROPOSAL,
        responder_id=TEO,
        semantic_minute=1505,
        proposed_start_minute=1600,
        proposed_end_minute=1640,
        location_ref="ouros.route.causeway-survey",
        scope_ref="survey_only",
        alternative_ref="remote_report",
        expires_minute=1550,
    )
    values.update(overrides)
    return ledger, record_assistance_renegotiation_proposal(**values)


def test_delivered_acceptance_allows_new_terms_without_mutating_old_commitment():
    commitments, decisions, queue = _state()
    old = commitments.records[COMMITMENT]
    ledger, record = _record(commitments, decisions, queue)
    assert record.supersedes_commitment_id == COMMITMENT
    assert record.supersedes_proposal_id == OLD_PROPOSAL
    assert record.decision_id == DECISION
    assert record.decision_reply_event_id == REPLY_EVENT
    assert record.provenance_root == NEW_PROPOSAL
    assert record.decision_provenance_root == DECISION
    assert commitments.records[COMMITMENT] == old
    assert len(commitments.records) == 1
    assert set(ledger.records) == {NEW_PROPOSAL}


def test_queued_acceptance_does_not_authorize_replacement_terms():
    commitments, decisions, queue = _state(reply_latency=3, deliver_reply=False)
    assert queue.statuses[REPLY_EVENT] == DeliveryStatus.QUEUED
    with pytest.raises(ValueError, match="terminal DELIVERED"):
        _record(commitments, decisions, queue)


def test_rejection_does_not_authorize_replacement_terms_even_if_reply_is_delivered():
    commitments, decisions, queue = _state()
    decision = decisions.records[DECISION]
    decisions.records[DECISION] = replace(
        decision,
        decision=AssistanceRenegotiationDecision.REJECT_REOPENING.value,
    )
    with pytest.raises(ValueError, match="explicit ACCEPT"):
        _record(commitments, decisions, queue)


def test_only_original_responder_can_author_and_terms_cannot_predate_received_acceptance():
    commitments, decisions, queue = _state()
    with pytest.raises(ValueError, match="original responder"):
        _record(commitments, decisions, queue, responder_id=MARA)
    with pytest.raises(ValueError, match="predate responder receipt"):
        _record(commitments, decisions, queue, semantic_minute=1503)


def test_tampered_received_acceptance_fails_closed():
    commitments, decisions, queue = _state()
    claim = queue.ledgers[TEO].claims["claim:teo-reply-pass445"]
    queue.ledgers[TEO].claims[claim.claim_id] = replace(claim, value='{"tampered":true}')
    with pytest.raises(ValueError, match="differs from authored reply"):
        _record(commitments, decisions, queue)


def test_identical_terms_do_not_create_fake_replacement_and_exact_replay_is_idempotent():
    commitments, decisions, queue = _state()
    with pytest.raises(ValueError, match="change at least one accepted term"):
        _record(
            commitments,
            decisions,
            queue,
            proposed_start_minute=1500,
            proposed_end_minute=1540,
        )

    ledger = AssistanceRenegotiationProposalLedger()
    _, first = _record(commitments, decisions, queue, ledger=ledger)
    _, second = _record(commitments, decisions, queue, ledger=ledger)
    assert second == first
    with pytest.raises(ValueError, match="conflicting content"):
        _record(commitments, decisions, queue, ledger=ledger, proposed_end_minute=1650)


def test_snapshot_round_trip_preserves_lineage():
    commitments, decisions, queue = _state()
    ledger, record = _record(commitments, decisions, queue)
    restored = AssistanceRenegotiationProposalLedger.from_snapshot(ledger.snapshot())
    assert restored.records[NEW_PROPOSAL] == record
