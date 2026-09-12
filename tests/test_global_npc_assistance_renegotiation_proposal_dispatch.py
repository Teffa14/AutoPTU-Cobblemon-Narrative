import json

import pytest

from tools.global_npc_assistance_renegotiation_proposal import (
    AssistanceRenegotiationProposalLedger,
    AssistanceRenegotiationProposalRecord,
)
from tools.global_npc_assistance_renegotiation_proposal_dispatch import (
    schedule_assistance_renegotiation_proposal,
)
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, SourceKind

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
OLD_COMMITMENT = "commitment:pass446-original"
OLD_PROPOSAL = "proposal:pass446-original"
NEW_PROPOSAL = "proposal:pass446-replacement"
EVENT = "event:pass446-replacement-offer"


def _proposals(*, expires_minute=1600):
    ledger = AssistanceRenegotiationProposalLedger()
    row = AssistanceRenegotiationProposalRecord(
        proposal_id=NEW_PROPOSAL,
        supersedes_commitment_id=OLD_COMMITMENT,
        supersedes_proposal_id=OLD_PROPOSAL,
        decision_id="renegotiation-decision:pass446",
        decision_reply_event_id="event:renegotiation-decision-reply-pass446",
        requester_id=MARA,
        responder_id=TEO,
        proposed_start_minute=1620,
        proposed_end_minute=1660,
        location_ref="ouros.route.causeway-survey",
        scope_ref="survey_only",
        alternative_ref="remote_report",
        expires_minute=expires_minute,
        semantic_minute=1510,
        decision_provenance_root="renegotiation-decision:pass446",
        provenance_root=NEW_PROPOSAL,
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


def _dispatch(proposals, queue, **overrides):
    values = dict(
        proposal_ledger=proposals,
        information_queue=queue,
        proposal_id=NEW_PROPOSAL,
        event_id=EVENT,
        message_id="message:pass446-replacement-offer",
        source_claim_id="claim:teo-pass446-replacement-offer",
        receiver_claim_id="claim:mara-pass446-replacement-offer",
        channel_id="channel:field-radio",
        created_minute=1512,
        receiver_trust_in_sender=15,
    )
    values.update(overrides)
    return schedule_assistance_renegotiation_proposal(**values)


def test_replacement_offer_is_authored_but_requester_knows_only_after_delivery():
    proposals, original = _proposals()
    queue = _queue(latency=4)
    envelope = _dispatch(proposals, queue)

    source = queue.ledgers[TEO].claims[envelope.source_claim_id]
    assert source.source_kind is SourceKind.AUTHORED_START
    assert source.provenance_root == NEW_PROPOSAL
    assert source.subject == f"assistance_renegotiation_proposal:{OLD_COMMITMENT}:{NEW_PROPOSAL}"
    assert json.loads(source.value) == {
        "proposal_id": NEW_PROPOSAL,
        "supersedes_commitment_id": OLD_COMMITMENT,
        "supersedes_proposal_id": OLD_PROPOSAL,
        "decision_id": "renegotiation-decision:pass446",
        "decision_reply_event_id": "event:renegotiation-decision-reply-pass446",
        "requester_id": MARA,
        "responder_id": TEO,
        "proposed_start_minute": 1620,
        "proposed_end_minute": 1660,
        "location_ref": "ouros.route.causeway-survey",
        "scope_ref": "survey_only",
        "alternative_ref": "remote_report",
        "expires_minute": 1600,
        "proposal_minute": 1510,
        "decision_provenance_root": "renegotiation-decision:pass446",
    }
    assert queue.ledgers[MARA].claims == {}
    assert proposals.records[NEW_PROPOSAL] == original
    assert queue.process_due(1515) == []
    assert queue.process_due(1516)[0]["status"] == DeliveryStatus.DELIVERED.value
    received = queue.ledgers[MARA].claims[envelope.new_claim_id]
    assert received.source_kind is SourceKind.REPORT
    assert received.parent_claim_id == source.claim_id
    assert received.provenance_root == NEW_PROPOSAL


def test_failed_or_unacknowledged_offer_does_not_create_requester_knowledge():
    proposals, _ = _proposals()
    failed = _queue(available=False)
    envelope = _dispatch(proposals, failed)
    assert failed.process_due(1512)[0]["status"] == DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value
    assert envelope.new_claim_id not in failed.ledgers[MARA].claims

    local = _queue(local_ack=True)
    envelope = _dispatch(proposals, local)
    assert local.process_due(1512)[0]["status"] == DeliveryStatus.WAITING_LOCAL_ACK.value
    assert envelope.new_claim_id not in local.ledgers[MARA].claims


def test_chronology_and_expiry_fail_closed():
    proposals, _ = _proposals(expires_minute=1511)
    with pytest.raises(ValueError, match="expired replacement offer"):
        _dispatch(proposals, _queue())

    proposals, _ = _proposals()
    with pytest.raises(ValueError, match="before its proposal"):
        _dispatch(proposals, _queue(), created_minute=1509, event_id="event:early-pass446")


def test_exact_replay_is_idempotent_and_conflicting_event_reuse_fails_closed():
    proposals, _ = _proposals()
    queue = _queue()
    first = _dispatch(proposals, queue)
    queue.process_due(1512)
    assert _dispatch(proposals, queue) == first
    assert len(queue.ledgers[TEO].claims) == 1
    assert len(queue.ledgers[MARA].claims) == 1

    with pytest.raises(ValueError, match="conflicting envelope"):
        _dispatch(
            proposals,
            queue,
            event_id=EVENT,
            message_id="message:conflict-pass446",
            source_claim_id="claim:conflict-source-pass446",
            receiver_claim_id="claim:conflict-receiver-pass446",
            created_minute=1513,
        )


def test_dispatch_has_no_tactical_or_world_execution_surface():
    import inspect
    import tools.global_npc_assistance_renegotiation_proposal_dispatch as module

    source = inspect.getsource(module)
    forbidden = ("REQUEST_AUTOPTU", "reserve_route", "allocate_resource", "move_actor", "relationship_delta")
    assert all(token not in source for token in forbidden)
