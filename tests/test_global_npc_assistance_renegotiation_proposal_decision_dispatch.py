from dataclasses import replace

import pytest

from tools.global_npc_assistance_renegotiation_proposal import (
    AssistanceRenegotiationProposalLedger,
    AssistanceRenegotiationProposalRecord,
)
from tools.global_npc_assistance_renegotiation_proposal_decision import (
    AssistanceRenegotiationProposalDecisionLedger,
    AssistanceRenegotiationProposalOutcome,
    record_assistance_renegotiation_proposal_decision,
)
from tools.global_npc_assistance_renegotiation_proposal_decision_dispatch import (
    schedule_assistance_renegotiation_proposal_decision_reply,
)
from tools.global_npc_assistance_renegotiation_proposal_dispatch import (
    schedule_assistance_renegotiation_proposal,
)
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, SourceKind

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
OLD_COMMITMENT = "commitment:pass448-original"
OLD_PROPOSAL = "proposal:pass448-original"
NEW_PROPOSAL = "proposal:pass448-replacement"
PROPOSAL_EVENT = "event:pass448-replacement-offer"
DECISION = "decision:pass448-replacement-offer"
REPLY_EVENT = "event:pass448-replacement-offer-decision"


def _state(*, reply_latency=0, reply_available=True, outcome=AssistanceRenegotiationProposalOutcome.ACCEPT):
    proposals = AssistanceRenegotiationProposalLedger()
    original = AssistanceRenegotiationProposalRecord(
        proposal_id=NEW_PROPOSAL,
        supersedes_commitment_id=OLD_COMMITMENT,
        supersedes_proposal_id=OLD_PROPOSAL,
        decision_id="renegotiation-decision:pass448",
        decision_reply_event_id="event:renegotiation-decision-reply-pass448",
        requester_id=MARA,
        responder_id=TEO,
        proposed_start_minute=1620,
        proposed_end_minute=1660,
        location_ref="ouros.route.causeway-survey",
        scope_ref="survey_only",
        alternative_ref="remote_report",
        expires_minute=1600,
        semantic_minute=1510,
        decision_provenance_root="renegotiation-decision:pass448",
        provenance_root=NEW_PROPOSAL,
    )
    proposals.add(original)
    queue = InformationEventQueue(
        channels={
            "channel:offer": CommunicationChannel("channel:offer", "RADIO", 0),
            "channel:reply": CommunicationChannel(
                "channel:reply", "RADIO", reply_latency, available=reply_available
            ),
        },
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)},
    )
    schedule_assistance_renegotiation_proposal(
        proposal_ledger=proposals,
        information_queue=queue,
        proposal_id=NEW_PROPOSAL,
        event_id=PROPOSAL_EVENT,
        message_id="message:pass448-replacement-offer",
        source_claim_id="claim:teo-pass448-replacement-offer",
        receiver_claim_id="claim:mara-pass448-replacement-offer",
        channel_id="channel:offer",
        created_minute=1512,
    )
    queue.process_due(1512)
    decisions = AssistanceRenegotiationProposalDecisionLedger()
    record_assistance_renegotiation_proposal_decision(
        proposal_ledger=proposals,
        information_queue=queue,
        decision_ledger=decisions,
        proposal_event_id=PROPOSAL_EVENT,
        decision_id=DECISION,
        requester_id=MARA,
        outcome=outcome,
        semantic_minute=1513 if outcome is not AssistanceRenegotiationProposalOutcome.EXPIRED else 1601,
        rationale_ref="reason:pass448-answer",
    )
    return proposals, original, decisions, queue


def _dispatch(proposals, decisions, queue, **overrides):
    values = dict(
        proposal_ledger=proposals,
        decision_ledger=decisions,
        information_queue=queue,
        decision_id=DECISION,
        event_id=REPLY_EVENT,
        message_id="message:pass448-replacement-decision",
        source_claim_id="claim:mara-pass448-replacement-decision",
        receiver_claim_id="claim:teo-pass448-replacement-decision",
        channel_id="channel:reply",
        created_minute=1514,
        receiver_trust_in_sender=15,
    )
    values.update(overrides)
    return schedule_assistance_renegotiation_proposal_decision_reply(**values)


def test_acceptance_is_not_known_by_responder_until_reply_is_delivered_and_offer_is_preserved():
    proposals, original, decisions, queue = _state(reply_latency=3)
    envelope = _dispatch(proposals, decisions, queue)
    assert envelope.sender_id == MARA
    assert envelope.receiver_id == TEO
    assert queue.statuses[REPLY_EVENT] == DeliveryStatus.QUEUED
    assert "claim:teo-pass448-replacement-decision" not in queue.ledgers[TEO].claims

    assert queue.process_due(1516) == []
    result = queue.process_due(1517)
    assert result[0]["status"] == DeliveryStatus.DELIVERED.value
    received = queue.ledgers[TEO].claims["claim:teo-pass448-replacement-decision"]
    assert received.source_kind is SourceKind.REPORT
    assert received.parent_claim_id == "claim:mara-pass448-replacement-decision"
    assert received.provenance_root == DECISION
    assert proposals.records[NEW_PROPOSAL] == original


def test_reply_payload_carries_exact_decision_and_lineage_without_creating_commitment():
    proposals, _, decisions, queue = _state()
    _dispatch(proposals, decisions, queue)
    queue.process_due(1514)
    source = queue.ledgers[MARA].claims["claim:mara-pass448-replacement-decision"]
    assert '"outcome":"ACCEPT_REPLACEMENT_TERMS"' in source.value
    assert f'"proposal_id":"{NEW_PROPOSAL}"' in source.value
    assert f'"supersedes_commitment_id":"{OLD_COMMITMENT}"' in source.value
    assert '"proposed_start_minute":1620' in source.value
    assert source.provenance_root == DECISION


def test_rejection_can_travel_but_expiry_is_not_misrepresented_as_a_requester_reply():
    proposals, _, decisions, queue = _state(outcome=AssistanceRenegotiationProposalOutcome.REJECT)
    _dispatch(proposals, decisions, queue)
    queue.process_due(1514)
    source = queue.ledgers[MARA].claims["claim:mara-pass448-replacement-decision"]
    assert '"outcome":"REJECT_REPLACEMENT_TERMS"' in source.value

    proposals, _, decisions, queue = _state(outcome=AssistanceRenegotiationProposalOutcome.EXPIRED)
    with pytest.raises(ValueError, match="observed timeout"):
        _dispatch(proposals, decisions, queue, created_minute=1602)


def test_unavailable_reply_channel_does_not_create_responder_knowledge():
    proposals, _, decisions, queue = _state(reply_available=False)
    _dispatch(proposals, decisions, queue)
    result = queue.process_due(1514)
    assert result[0]["status"] == DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value
    assert "claim:teo-pass448-replacement-decision" not in queue.ledgers[TEO].claims


def test_tampered_actor_or_provenance_fails_closed():
    proposals, _, decisions, queue = _state()
    original = decisions.records[DECISION]
    decisions.records[DECISION] = replace(original, requester_id=TEO)
    with pytest.raises(ValueError, match="actor binding"):
        _dispatch(proposals, decisions, queue)

    decisions.records[DECISION] = replace(original, proposal_provenance_root="other-root")
    with pytest.raises(ValueError, match="proposal provenance"):
        _dispatch(proposals, decisions, queue)


def test_reply_cannot_predate_decision_and_exact_replay_is_idempotent():
    proposals, _, decisions, queue = _state()
    with pytest.raises(ValueError, match="before requester decision"):
        _dispatch(proposals, decisions, queue, created_minute=1512)

    first = _dispatch(proposals, decisions, queue)
    assert _dispatch(proposals, decisions, queue) == first
    with pytest.raises(ValueError, match="conflicting envelope"):
        _dispatch(proposals, decisions, queue, message_id="message:other")


def test_dispatch_owner_has_no_commitment_or_tactical_execution_surface():
    import inspect
    import tools.global_npc_assistance_renegotiation_proposal_decision_dispatch as module

    source = inspect.getsource(module)
    forbidden = (
        "REQUEST_AUTOPTU",
        "reserve_route",
        "allocate_resource",
        "move_actor",
        "relationship_delta",
        "ScheduledCommitment(",
    )
    assert all(token not in source for token in forbidden)
