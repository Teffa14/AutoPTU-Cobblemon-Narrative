import json
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
from tools.global_npc_assistance_renegotiation_dispatch import schedule_assistance_renegotiation_request
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, SourceKind

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
COMMITMENT = "commitment:negotiated-help-pass442"
PROPOSAL = "proposal:pass442"
DISPOSITION = "start-disposition:pass442"
EVENT = "event:renegotiation-pass442"


def _commitments():
    ledger = AssistanceCounterproposalCommitmentLedger()
    record = AssistanceCounterproposalCommitmentRecord(
        commitment_id=COMMITMENT,
        proposal_id=PROPOSAL,
        request_action_id="action:request-pass442",
        response_action_id="action:counter-pass442",
        decision_action_id="action:accept-pass442",
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
        provenance_root="action:accept-pass442",
    )
    ledger.add(record)
    return ledger, record


def _dispositions(choice=CommitmentStartDisposition.REQUEST_RENEGOTIATION.value):
    ledger = AssistanceCommitmentDispositionLedger()
    row = AssistanceCommitmentDisposition(
        disposition_id=DISPOSITION,
        commitment_id=COMMITMENT,
        proposal_id=PROPOSAL,
        assessment_id="start-assessment:pass442",
        requester_id=MARA,
        responder_id=TEO,
        actor_id=TEO,
        semantic_minute=1501,
        disposition=choice,
        rationale_ref="reason:route-still-closed",
        provenance_root="decision:teo-renegotiate-pass442",
    )
    ledger.add(row)
    return ledger, row


def _queue(*, available=True, local_ack=False, latency=0):
    return InformationEventQueue(
        channels={
            "channel:field-radio": CommunicationChannel(
                channel_id="channel:field-radio",
                kind="RADIO",
                latency_minutes=latency,
                available=available,
                requires_local_projection=local_ack,
            )
        },
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)},
    )


def _dispatch(commitments, dispositions, queue, **overrides):
    values = dict(
        commitment_ledger=commitments,
        disposition_ledger=dispositions,
        information_queue=queue,
        disposition_id=DISPOSITION,
        event_id=EVENT,
        message_id="message:renegotiation-pass442",
        source_claim_id="claim:teo-renegotiation-pass442",
        receiver_claim_id="claim:mara-renegotiation-pass442",
        channel_id="channel:field-radio",
        created_minute=1502,
        receiver_trust_in_sender=20,
    )
    values.update(overrides)
    return schedule_assistance_renegotiation_request(**values)


def test_request_is_authored_but_requester_knows_only_after_delivery():
    commitments, original = _commitments()
    dispositions, disposition = _dispositions()
    queue = _queue(latency=4)
    envelope = _dispatch(commitments, dispositions, queue)

    source = queue.ledgers[TEO].claims[envelope.source_claim_id]
    assert source.source_kind is SourceKind.AUTHORED_START
    assert source.provenance_root == disposition.provenance_root
    assert source.subject == f"assistance_renegotiation_request:{COMMITMENT}:{DISPOSITION}"
    assert json.loads(source.value) == {
        "commitment_id": COMMITMENT,
        "proposal_id": PROPOSAL,
        "assessment_id": "start-assessment:pass442",
        "disposition_id": DISPOSITION,
        "rationale_ref": "reason:route-still-closed",
        "accepted_start_minute": 1500,
        "accepted_end_minute": 1540,
        "location_ref": "ouros.route.causeway-survey",
        "scope_ref": "survey_only",
        "alternative_ref": "remote_report",
    }
    assert queue.ledgers[MARA].claims == {}
    assert commitments.records[COMMITMENT] == original
    assert queue.process_due(1505) == []
    assert queue.process_due(1506)[0]["status"] == DeliveryStatus.DELIVERED.value
    received = queue.ledgers[MARA].claims[envelope.new_claim_id]
    assert received.source_kind is SourceKind.REPORT
    assert received.parent_claim_id == source.claim_id
    assert received.provenance_root == disposition.provenance_root


def test_failed_or_unacknowledged_request_does_not_create_requester_knowledge():
    commitments, _ = _commitments()
    dispositions, _ = _dispositions()
    failed = _queue(available=False)
    envelope = _dispatch(commitments, dispositions, failed)
    assert failed.process_due(1502)[0]["status"] == DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value
    assert envelope.new_claim_id not in failed.ledgers[MARA].claims

    local = _queue(local_ack=True)
    envelope = _dispatch(commitments, dispositions, local)
    assert local.process_due(1502)[0]["status"] == DeliveryStatus.WAITING_LOCAL_ACK.value
    assert envelope.new_claim_id not in local.ledgers[MARA].claims


def test_only_request_renegotiation_disposition_can_dispatch():
    commitments, _ = _commitments()
    dispositions, _ = _dispositions(CommitmentStartDisposition.WAIT_FOR_CLEARANCE.value)
    with pytest.raises(ValueError, match="requires REQUEST_RENEGOTIATION"):
        _dispatch(commitments, dispositions, _queue())


def test_actor_binding_and_chronology_fail_closed():
    commitments, _ = _commitments()
    dispositions, original = _dispositions()
    dispositions.records[DISPOSITION] = replace(original, actor_id=MARA)
    with pytest.raises(ValueError, match="commitment responder"):
        _dispatch(commitments, dispositions, _queue())

    dispositions.records[DISPOSITION] = original
    with pytest.raises(ValueError, match="before its disposition"):
        _dispatch(commitments, dispositions, _queue(), created_minute=1500, event_id="event:early-pass442")


def test_exact_replay_is_idempotent_and_conflicting_event_reuse_fails_closed():
    commitments, _ = _commitments()
    dispositions, _ = _dispositions()
    queue = _queue()
    first = _dispatch(commitments, dispositions, queue)
    queue.process_due(1502)
    assert _dispatch(commitments, dispositions, queue) == first
    assert len(queue.ledgers[TEO].claims) == 1
    assert len(queue.ledgers[MARA].claims) == 1

    with pytest.raises(ValueError, match="conflicting envelope"):
        _dispatch(
            commitments,
            dispositions,
            queue,
            event_id=EVENT,
            message_id="message:conflict-pass442",
            source_claim_id="claim:conflict-source-pass442",
            receiver_claim_id="claim:conflict-receiver-pass442",
            created_minute=1503,
        )
