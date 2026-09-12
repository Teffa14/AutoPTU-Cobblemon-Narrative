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
from tools.global_npc_assistance_renegotiation_dispatch import schedule_assistance_renegotiation_request
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
COMMITMENT = "commitment:negotiated-help-pass443"
PROPOSAL = "proposal:pass443"
DISPOSITION = "start-disposition:pass443"
EVENT = "event:renegotiation-pass443"
DECISION = "renegotiation-decision:pass443"


def _state(*, latency=0):
    commitments = AssistanceCounterproposalCommitmentLedger()
    commitments.add(
        AssistanceCounterproposalCommitmentRecord(
            commitment_id=COMMITMENT,
            proposal_id=PROPOSAL,
            request_action_id="action:request-pass443",
            response_action_id="action:counter-pass443",
            decision_action_id="action:accept-pass443",
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
            provenance_root="action:accept-pass443",
        )
    )
    dispositions = AssistanceCommitmentDispositionLedger()
    dispositions.add(
        AssistanceCommitmentDisposition(
            disposition_id=DISPOSITION,
            commitment_id=COMMITMENT,
            proposal_id=PROPOSAL,
            assessment_id="start-assessment:pass443",
            requester_id=MARA,
            responder_id=TEO,
            actor_id=TEO,
            semantic_minute=1501,
            disposition=CommitmentStartDisposition.REQUEST_RENEGOTIATION.value,
            rationale_ref="reason:route-still-closed",
            provenance_root="decision:teo-renegotiate-pass443",
        )
    )
    queue = InformationEventQueue(
        channels={
            "channel:field-radio": CommunicationChannel(
                channel_id="channel:field-radio",
                kind="RADIO",
                latency_minutes=latency,
                available=True,
                requires_local_projection=False,
            )
        },
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)},
    )
    schedule_assistance_renegotiation_request(
        commitment_ledger=commitments,
        disposition_ledger=dispositions,
        information_queue=queue,
        disposition_id=DISPOSITION,
        event_id=EVENT,
        message_id="message:renegotiation-pass443",
        source_claim_id="claim:teo-renegotiation-pass443",
        receiver_claim_id="claim:mara-renegotiation-pass443",
        channel_id="channel:field-radio",
        created_minute=1502,
        receiver_trust_in_sender=20,
    )
    return commitments, dispositions, queue


def _record(commitments, dispositions, queue, ledger, **overrides):
    values = dict(
        commitment_ledger=commitments,
        disposition_ledger=dispositions,
        information_queue=queue,
        decision_ledger=ledger,
        request_event_id=EVENT,
        decision_id=DECISION,
        decision=AssistanceRenegotiationDecision.ACCEPT_REOPENING,
        requester_id=MARA,
        semantic_minute=1503,
        rationale_ref="reason:open-to-new-window",
    )
    values.update(overrides)
    return record_assistance_renegotiation_decision(**values)


def test_requester_can_decide_only_after_actual_delivery_and_old_commitment_is_unchanged():
    commitments, dispositions, queue = _state()
    original = commitments.records[COMMITMENT]
    ledger = AssistanceRenegotiationDecisionLedger()

    with pytest.raises(ValueError, match="terminal DELIVERED"):
        _record(commitments, dispositions, queue, ledger)

    queue.process_due(1502)
    record = _record(commitments, dispositions, queue, ledger)
    assert record.decision == AssistanceRenegotiationDecision.ACCEPT_REOPENING.value
    assert record.requester_id == MARA
    assert record.responder_id == TEO
    assert record.commitment_id == COMMITMENT
    assert record.proposal_id == PROPOSAL
    assert record.provenance_root == "decision:teo-renegotiate-pass443"
    assert commitments.records[COMMITMENT] == original


def test_rejecting_reopening_is_a_distinct_durable_choice():
    commitments, dispositions, queue = _state()
    queue.process_due(1502)
    ledger = AssistanceRenegotiationDecisionLedger()
    record = _record(
        commitments,
        dispositions,
        queue,
        ledger,
        decision=AssistanceRenegotiationDecision.REJECT_REOPENING,
        rationale_ref="reason:original-terms-still-required",
    )
    assert record.decision == AssistanceRenegotiationDecision.REJECT_REOPENING.value


def test_wrong_actor_or_tampered_delivered_payload_fails_closed():
    commitments, dispositions, queue = _state()
    queue.process_due(1502)
    ledger = AssistanceRenegotiationDecisionLedger()

    with pytest.raises(ValueError, match="delivered requester"):
        _record(commitments, dispositions, queue, ledger, requester_id=TEO)

    received = queue.ledgers[MARA].claims["claim:mara-renegotiation-pass443"]
    queue.ledgers[MARA].claims[received.claim_id] = replace(received, value='{"commitment_id":"other"}')
    with pytest.raises(ValueError, match="differs from authored request"):
        _record(commitments, dispositions, queue, ledger)


def test_decision_cannot_predate_receipt_even_when_old_window_later_expires():
    commitments, dispositions, queue = _state(latency=5)
    assert queue.process_due(1506) == []
    queue.process_due(1507)
    ledger = AssistanceRenegotiationDecisionLedger()
    with pytest.raises(ValueError, match="cannot predate requester receipt"):
        _record(commitments, dispositions, queue, ledger, semantic_minute=1506)

    record = _record(commitments, dispositions, queue, ledger, semantic_minute=1600)
    assert record.semantic_minute == 1600


def test_exact_replay_is_idempotent_conflicting_reuse_fails_and_snapshot_roundtrips():
    commitments, dispositions, queue = _state()
    queue.process_due(1502)
    ledger = AssistanceRenegotiationDecisionLedger()
    first = _record(commitments, dispositions, queue, ledger)
    assert _record(commitments, dispositions, queue, ledger) == first

    with pytest.raises(ValueError, match="conflicting content"):
        _record(
            commitments,
            dispositions,
            queue,
            ledger,
            decision=AssistanceRenegotiationDecision.REJECT_REOPENING,
        )

    restored = AssistanceRenegotiationDecisionLedger.from_snapshot(ledger.snapshot())
    assert restored.records == ledger.records
