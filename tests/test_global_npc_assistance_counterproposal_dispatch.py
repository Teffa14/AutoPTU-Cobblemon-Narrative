import json
from dataclasses import replace

import pytest

from tools.global_npc_ai import AgendaDecision, Decision, Handoff
from tools.global_npc_assistance_counterproposal import (
    AssistanceCounterproposalLedger,
    record_assistance_counterproposal_terms,
)
from tools.global_npc_assistance_counterproposal_dispatch import schedule_assistance_counterproposal_terms
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, SourceKind
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import CoordinatedDecision

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
REQUEST = "action:request-teo-pass433"
RESPONSE = "action:counter-teo-pass433"
PROPOSAL = "proposal:teo-pass433"
TRIGGER = "replan:information:event:request-pass433"
EVENT = "event:counter-terms-pass433"


def _record(ledger, *, action_id, agent_id, intent_id, kind, target_ref, minute, trigger_id):
    coordinated = CoordinatedDecision(
        agent_id=agent_id,
        trigger_ids=(trigger_id,),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(
                agent_id=agent_id,
                intent_id=intent_id,
                kind=kind,
                score=433,
                handoff=Handoff.NONE,
                target_ref=target_ref,
            ),
            source_type="SITUATIONAL_INTENT",
            source_ref=intent_id,
        ),
    )
    return ledger.record_from_replan(
        action_id=action_id,
        coordinated_decision=coordinated,
        semantic_minute=minute,
    )


def _actions() -> WorldActionIntentLedger:
    ledger = WorldActionIntentLedger()
    _record(
        ledger,
        action_id=REQUEST,
        agent_id=MARA,
        intent_id="intent:request-pass433",
        kind="REQUEST_ASSISTANCE",
        target_ref=TEO,
        minute=1200,
        trigger_id="trigger:field-problem-pass433",
    )
    _record(
        ledger,
        action_id=RESPONSE,
        agent_id=TEO,
        intent_id="intent:counter-pass433",
        kind="COUNTERPROPOSE_ASSISTANCE_REQUEST",
        target_ref=MARA,
        minute=1203,
        trigger_id=TRIGGER,
    )
    return ledger


def _proposals(actions: WorldActionIntentLedger) -> AssistanceCounterproposalLedger:
    ledger = AssistanceCounterproposalLedger()
    record_assistance_counterproposal_terms(
        action_ledger=actions,
        proposal_ledger=ledger,
        request_action_id=REQUEST,
        response_action_id=RESPONSE,
        proposal_id=PROPOSAL,
        request_delivery_trigger_id=TRIGGER,
        proposed_start_minute=1230,
        proposed_end_minute=1260,
        location_ref="ouros.marea.field_office",
        scope_ref="diagnose_pump_only",
        alternative_ref="remote_parts_list",
        expires_minute=1220,
    )
    return ledger


def _queue(*, available=True, local_ack=False, latency=0) -> InformationEventQueue:
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


def _dispatch(actions, proposals, queue, *, created_minute=1205, event_id=EVENT):
    return schedule_assistance_counterproposal_terms(
        action_ledger=actions,
        proposal_ledger=proposals,
        information_queue=queue,
        proposal_id=PROPOSAL,
        event_id=event_id,
        message_id="message:counter-terms-pass433",
        source_claim_id="claim:teo-counter-terms-pass433",
        receiver_claim_id="claim:mara-counter-terms-pass433",
        channel_id="channel:field-radio",
        created_minute=created_minute,
        receiver_trust_in_sender=20,
    )


def test_terms_are_authored_but_requester_learns_them_only_after_delivery() -> None:
    actions = _actions()
    proposals = _proposals(actions)
    queue = _queue(latency=4)
    envelope = _dispatch(actions, proposals, queue)

    source = queue.ledgers[TEO].claims[envelope.source_claim_id]
    assert source.source_kind is SourceKind.AUTHORED_START
    assert source.provenance_root == RESPONSE
    assert source.subject == f"assistance_counterproposal_terms:{REQUEST}:{RESPONSE}:{PROPOSAL}"
    assert json.loads(source.value) == {
        "proposal_id": PROPOSAL,
        "request_action_id": REQUEST,
        "response_action_id": RESPONSE,
        "proposed_start_minute": 1230,
        "proposed_end_minute": 1260,
        "location_ref": "ouros.marea.field_office",
        "scope_ref": "diagnose_pump_only",
        "alternative_ref": "remote_parts_list",
        "expires_minute": 1220,
    }
    assert queue.ledgers[MARA].claims == {}
    assert queue.process_due(1208) == []

    result = queue.process_due(1209)
    assert result[0]["status"] == DeliveryStatus.DELIVERED.value
    received = queue.ledgers[MARA].claims[envelope.new_claim_id]
    assert received.source_kind is SourceKind.REPORT
    assert received.value == source.value
    assert received.parent_claim_id == source.claim_id
    assert received.provenance_root == RESPONSE


def test_failed_or_unacknowledged_terms_do_not_create_requester_knowledge() -> None:
    actions = _actions()
    proposals = _proposals(actions)

    failed = _queue(available=False)
    envelope = _dispatch(actions, proposals, failed)
    assert failed.process_due(1205)[0]["status"] == DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value
    assert envelope.new_claim_id not in failed.ledgers[MARA].claims

    local = _queue(local_ack=True)
    envelope = _dispatch(actions, proposals, local)
    assert local.process_due(1205)[0]["status"] == DeliveryStatus.WAITING_LOCAL_ACK.value
    assert envelope.new_claim_id not in local.ledgers[MARA].claims


def test_expired_terms_can_arrive_as_stale_information_without_becoming_acceptance() -> None:
    actions = _actions()
    proposals = _proposals(actions)
    queue = _queue()
    envelope = _dispatch(actions, proposals, queue, created_minute=1225)
    queue.process_due(1225)

    received = queue.ledgers[MARA].claims[envelope.new_claim_id]
    assert json.loads(received.value)["expires_minute"] == 1220
    assert len(proposals.records) == 1
    assert all(record.intent_kind != "ACCEPT_ASSISTANCE_REQUEST" for record in actions.records.values())


def test_exact_replay_is_idempotent_and_conflicting_event_reuse_fails_closed() -> None:
    actions = _actions()
    proposals = _proposals(actions)
    queue = _queue()
    first = _dispatch(actions, proposals, queue)
    queue.process_due(1205)
    replay = _dispatch(actions, proposals, queue)
    assert replay == first
    assert len(queue.ledgers[TEO].claims) == 1
    assert len(queue.ledgers[MARA].claims) == 1

    with pytest.raises(ValueError, match="conflicting envelope"):
        schedule_assistance_counterproposal_terms(
            action_ledger=actions,
            proposal_ledger=proposals,
            information_queue=queue,
            proposal_id=PROPOSAL,
            event_id=EVENT,
            message_id="message:conflict-pass433",
            source_claim_id="claim:conflict-source-pass433",
            receiver_claim_id="claim:conflict-receiver-pass433",
            channel_id="channel:field-radio",
            created_minute=1206,
        )


def test_actor_binding_provenance_and_chronology_fail_closed() -> None:
    actions = _actions()
    proposals = _proposals(actions)
    original = proposals.records[PROPOSAL]

    proposals.records[PROPOSAL] = replace(original, provenance_root="action:wrong")
    with pytest.raises(ValueError, match="provenance"):
        _dispatch(actions, proposals, _queue())

    proposals.records[PROPOSAL] = replace(original, requester_id="ouros.npc.someone_else")
    with pytest.raises(ValueError, match="actor binding"):
        _dispatch(actions, proposals, _queue())

    proposals.records[PROPOSAL] = original
    with pytest.raises(ValueError, match="before the response"):
        _dispatch(actions, proposals, _queue(), created_minute=1202, event_id="event:early-pass433")
