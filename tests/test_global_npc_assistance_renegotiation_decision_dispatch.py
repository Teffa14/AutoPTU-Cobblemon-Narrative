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
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, SourceKind

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
COMMITMENT = "commitment:negotiated-help-pass444"
PROPOSAL = "proposal:pass444"
DISPOSITION = "start-disposition:pass444"
REQUEST_EVENT = "event:renegotiation-request-pass444"
DECISION = "renegotiation-decision:pass444"
REPLY_EVENT = "event:renegotiation-decision-reply-pass444"


def _state(*, reply_latency=0, reply_available=True):
    commitments = AssistanceCounterproposalCommitmentLedger()
    commitments.add(
        AssistanceCounterproposalCommitmentRecord(
            commitment_id=COMMITMENT,
            proposal_id=PROPOSAL,
            request_action_id="action:request-pass444",
            response_action_id="action:counter-pass444",
            decision_action_id="action:accept-pass444",
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
            provenance_root="action:accept-pass444",
        )
    )
    dispositions = AssistanceCommitmentDispositionLedger()
    dispositions.add(
        AssistanceCommitmentDisposition(
            disposition_id=DISPOSITION,
            commitment_id=COMMITMENT,
            proposal_id=PROPOSAL,
            assessment_id="start-assessment:pass444",
            requester_id=MARA,
            responder_id=TEO,
            actor_id=TEO,
            semantic_minute=1501,
            disposition=CommitmentStartDisposition.REQUEST_RENEGOTIATION.value,
            rationale_ref="reason:route-still-closed",
            provenance_root="decision:teo-renegotiate-pass444",
        )
    )
    queue = InformationEventQueue(
        channels={
            "channel:request": CommunicationChannel("channel:request", "RADIO", 0),
            "channel:reply": CommunicationChannel(
                "channel:reply", "RADIO", reply_latency, available=reply_available
            ),
        },
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)},
    )
    schedule_assistance_renegotiation_request(
        commitment_ledger=commitments,
        disposition_ledger=dispositions,
        information_queue=queue,
        disposition_id=DISPOSITION,
        event_id=REQUEST_EVENT,
        message_id="message:request-pass444",
        source_claim_id="claim:teo-request-pass444",
        receiver_claim_id="claim:mara-request-pass444",
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
    return commitments, dispositions, decisions, queue


def _dispatch(commitments, dispositions, decisions, queue, **overrides):
    values = dict(
        commitment_ledger=commitments,
        disposition_ledger=dispositions,
        decision_ledger=decisions,
        information_queue=queue,
        decision_id=DECISION,
        event_id=REPLY_EVENT,
        message_id="message:decision-reply-pass444",
        source_claim_id="claim:mara-decision-pass444",
        receiver_claim_id="claim:teo-decision-pass444",
        channel_id="channel:reply",
        created_minute=1504,
        receiver_trust_in_sender=15,
    )
    values.update(overrides)
    return schedule_assistance_renegotiation_decision_reply(**values)


def test_requester_answer_requires_delivery_before_responder_knows_it_and_preserves_old_commitment():
    commitments, dispositions, decisions, queue = _state(reply_latency=3)
    original = commitments.records[COMMITMENT]

    envelope = _dispatch(commitments, dispositions, decisions, queue)
    assert envelope.sender_id == MARA
    assert envelope.receiver_id == TEO
    assert queue.statuses[REPLY_EVENT] == DeliveryStatus.QUEUED
    assert "claim:teo-decision-pass444" not in queue.ledgers[TEO].claims

    assert queue.process_due(1506) == []
    result = queue.process_due(1507)
    assert result[0]["status"] == DeliveryStatus.DELIVERED.value
    received = queue.ledgers[TEO].claims["claim:teo-decision-pass444"]
    assert received.source_kind is SourceKind.REPORT
    assert received.parent_claim_id == "claim:mara-decision-pass444"
    assert received.provenance_root == DECISION
    assert commitments.records[COMMITMENT] == original
    assert len(commitments.records) == 1


def test_reply_payload_reports_choice_but_does_not_create_replacement_terms():
    commitments, dispositions, decisions, queue = _state()
    _dispatch(commitments, dispositions, decisions, queue)
    queue.process_due(1504)
    source = queue.ledgers[MARA].claims["claim:mara-decision-pass444"]
    assert '"decision":"ACCEPT_RENEGOTIATION_REQUEST"' in source.value
    assert '"accepted_start_minute":1500' in source.value
    assert '"accepted_end_minute":1540' in source.value
    assert source.provenance_root == DECISION
    assert set(commitments.records) == {COMMITMENT}


def test_unavailable_reply_channel_does_not_create_responder_knowledge():
    commitments, dispositions, decisions, queue = _state(reply_available=False)
    _dispatch(commitments, dispositions, decisions, queue)
    result = queue.process_due(1504)
    assert result[0]["status"] == DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value
    assert "claim:teo-decision-pass444" not in queue.ledgers[TEO].claims


def test_tampered_actor_or_provenance_fails_closed():
    commitments, dispositions, decisions, queue = _state()
    original = decisions.records[DECISION]
    decisions.records[DECISION] = replace(original, requester_id=TEO)
    with pytest.raises(ValueError, match="decision actor binding"):
        _dispatch(commitments, dispositions, decisions, queue)

    decisions.records[DECISION] = replace(original, provenance_root="other-root")
    with pytest.raises(ValueError, match="decision/request provenance"):
        _dispatch(commitments, dispositions, decisions, queue)


def test_reply_cannot_be_authored_before_decision_and_exact_replay_is_idempotent():
    commitments, dispositions, decisions, queue = _state()
    with pytest.raises(ValueError, match="before requester decision"):
        _dispatch(commitments, dispositions, decisions, queue, created_minute=1502)

    first = _dispatch(commitments, dispositions, decisions, queue)
    assert _dispatch(commitments, dispositions, decisions, queue) == first
    with pytest.raises(ValueError, match="conflicting envelope"):
        _dispatch(commitments, dispositions, decisions, queue, message_id="message:other")


def test_rejection_can_be_dispatched_as_a_distinct_answer():
    commitments, dispositions, decisions, queue = _state()
    accepted = decisions.records[DECISION]
    decisions.records[DECISION] = replace(
        accepted,
        decision=AssistanceRenegotiationDecision.REJECT_REOPENING.value,
        rationale_ref="reason:original-window-required",
    )
    _dispatch(commitments, dispositions, decisions, queue)
    queue.process_due(1504)
    source = queue.ledgers[MARA].claims["claim:mara-decision-pass444"]
    assert '"decision":"REJECT_RENEGOTIATION_REQUEST"' in source.value
