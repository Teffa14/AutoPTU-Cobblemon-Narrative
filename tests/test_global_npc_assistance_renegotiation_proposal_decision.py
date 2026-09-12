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
from tools.global_npc_assistance_renegotiation_proposal_dispatch import (
    schedule_assistance_renegotiation_proposal,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
OLD_COMMITMENT = "commitment:pass447-original"
OLD_PROPOSAL = "proposal:pass447-original"
NEW_PROPOSAL = "proposal:pass447-replacement"
EVENT = "event:pass447-replacement-offer"
DECISION = "decision:pass447-replacement-offer"


def _state(*, latency=0, expires_minute=1600):
    proposals = AssistanceRenegotiationProposalLedger()
    original = AssistanceRenegotiationProposalRecord(
        proposal_id=NEW_PROPOSAL,
        supersedes_commitment_id=OLD_COMMITMENT,
        supersedes_proposal_id=OLD_PROPOSAL,
        decision_id="renegotiation-decision:pass447",
        decision_reply_event_id="event:renegotiation-decision-reply-pass447",
        requester_id=MARA,
        responder_id=TEO,
        proposed_start_minute=1620,
        proposed_end_minute=1660,
        location_ref="ouros.route.causeway-survey",
        scope_ref="survey_only",
        alternative_ref="remote_report",
        expires_minute=expires_minute,
        semantic_minute=1510,
        decision_provenance_root="renegotiation-decision:pass447",
        provenance_root=NEW_PROPOSAL,
    )
    proposals.add(original)
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
    schedule_assistance_renegotiation_proposal(
        proposal_ledger=proposals,
        information_queue=queue,
        proposal_id=NEW_PROPOSAL,
        event_id=EVENT,
        message_id="message:pass447-replacement-offer",
        source_claim_id="claim:teo-pass447-replacement-offer",
        receiver_claim_id="claim:mara-pass447-replacement-offer",
        channel_id="channel:field-radio",
        created_minute=1512,
        receiver_trust_in_sender=15,
    )
    return proposals, original, queue


def _record(proposals, queue, ledger, **overrides):
    values = dict(
        proposal_ledger=proposals,
        information_queue=queue,
        decision_ledger=ledger,
        proposal_event_id=EVENT,
        decision_id=DECISION,
        requester_id=MARA,
        outcome=AssistanceRenegotiationProposalOutcome.ACCEPT,
        semantic_minute=1513,
        rationale_ref="reason:new-window-works",
    )
    values.update(overrides)
    return record_assistance_renegotiation_proposal_decision(**values)


def test_requester_can_accept_only_after_actual_delivery_and_offer_is_unchanged():
    proposals, original, queue = _state()
    ledger = AssistanceRenegotiationProposalDecisionLedger()

    with pytest.raises(ValueError, match="terminal DELIVERED"):
        _record(proposals, queue, ledger)

    queue.process_due(1512)
    record = _record(proposals, queue, ledger)
    assert record.outcome == AssistanceRenegotiationProposalOutcome.ACCEPT.value
    assert record.proposal_id == NEW_PROPOSAL
    assert record.supersedes_commitment_id == OLD_COMMITMENT
    assert record.requester_id == MARA
    assert record.responder_id == TEO
    assert record.provenance_root == NEW_PROPOSAL
    assert proposals.records[NEW_PROPOSAL] == original


def test_rejecting_exact_terms_is_a_distinct_durable_outcome():
    proposals, _, queue = _state()
    queue.process_due(1512)
    ledger = AssistanceRenegotiationProposalDecisionLedger()
    record = _record(
        proposals,
        queue,
        ledger,
        outcome=AssistanceRenegotiationProposalOutcome.REJECT,
        rationale_ref="reason:new-window-conflicts",
    )
    assert record.outcome == AssistanceRenegotiationProposalOutcome.REJECT.value


def test_expired_offer_cannot_be_accepted_and_expiry_is_recorded_separately():
    proposals, _, queue = _state(latency=20, expires_minute=1520)
    queue.process_due(1532)
    ledger = AssistanceRenegotiationProposalDecisionLedger()

    with pytest.raises(ValueError, match="expired replacement offer"):
        _record(proposals, queue, ledger, semantic_minute=1532)

    record = _record(
        proposals,
        queue,
        ledger,
        outcome=AssistanceRenegotiationProposalOutcome.EXPIRED,
        semantic_minute=1532,
        rationale_ref="reason:offer-window-lapsed",
    )
    assert record.outcome == AssistanceRenegotiationProposalOutcome.EXPIRED.value


def test_expiry_requires_a_real_deadline_and_cannot_be_declared_early():
    proposals, _, queue = _state(expires_minute=1600)
    queue.process_due(1512)
    ledger = AssistanceRenegotiationProposalDecisionLedger()
    with pytest.raises(ValueError, match="cannot expire before"):
        _record(
            proposals,
            queue,
            ledger,
            outcome=AssistanceRenegotiationProposalOutcome.EXPIRED,
        )

    proposals, _, queue = _state(expires_minute=None)
    queue.process_due(1512)
    with pytest.raises(ValueError, match="without expiry"):
        _record(
            proposals,
            queue,
            AssistanceRenegotiationProposalDecisionLedger(),
            outcome=AssistanceRenegotiationProposalOutcome.EXPIRED,
        )


def test_wrong_actor_tampering_and_pre_receipt_decision_fail_closed():
    proposals, _, queue = _state(latency=4)
    queue.process_due(1516)
    ledger = AssistanceRenegotiationProposalDecisionLedger()

    with pytest.raises(ValueError, match="delivered requester"):
        _record(proposals, queue, ledger, requester_id=TEO, semantic_minute=1516)

    with pytest.raises(ValueError, match="cannot predate requester receipt"):
        _record(proposals, queue, ledger, semantic_minute=1515)

    received = queue.ledgers[MARA].claims["claim:mara-pass447-replacement-offer"]
    queue.ledgers[MARA].claims[received.claim_id] = replace(received, value='{"proposal_id":"other"}')
    with pytest.raises(ValueError, match="differs from authored proposal"):
        _record(proposals, queue, ledger, semantic_minute=1516)


def test_exact_replay_is_idempotent_conflicting_reuse_fails_and_snapshot_roundtrips():
    proposals, _, queue = _state()
    queue.process_due(1512)
    ledger = AssistanceRenegotiationProposalDecisionLedger()
    first = _record(proposals, queue, ledger)
    assert _record(proposals, queue, ledger) == first

    with pytest.raises(ValueError, match="conflicting content"):
        _record(
            proposals,
            queue,
            ledger,
            outcome=AssistanceRenegotiationProposalOutcome.REJECT,
        )

    restored = AssistanceRenegotiationProposalDecisionLedger.from_snapshot(ledger.snapshot())
    assert restored.records == ledger.records


def test_decision_owner_has_no_tactical_or_world_execution_surface():
    import inspect
    import tools.global_npc_assistance_renegotiation_proposal_decision as module

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
