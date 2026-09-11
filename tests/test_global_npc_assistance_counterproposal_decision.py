from dataclasses import replace

import pytest

from tools.global_npc_ai import AgendaDecision, Decision, Handoff
from tools.global_npc_assistance_counterproposal import (
    AssistanceCounterproposalLedger,
    record_assistance_counterproposal_terms,
)
from tools.global_npc_assistance_counterproposal_decision import (
    record_assistance_counterproposal_decision_from_replan,
)
from tools.global_npc_assistance_counterproposal_dispatch import schedule_assistance_counterproposal_terms
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import CoordinatedDecision

MARA = "ouros.npc.mara_veyra"
TEO = "ouros.npc.teo_lark"
REQUEST = "action:request-teo-pass434"
RESPONSE = "action:counter-teo-pass434"
PROPOSAL = "proposal:teo-pass434"
REQUEST_TRIGGER = "replan:information:event:request-pass434"
TERMS_EVENT = "event:counter-terms-pass434"
TERMS_TRIGGER = f"replan:information:{TERMS_EVENT}"


def _record(ledger, *, action_id, agent_id, intent_id, kind, target_ref, minute, trigger_id, source_ref=None):
    coordinated = CoordinatedDecision(
        agent_id=agent_id,
        trigger_ids=(trigger_id,),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(
                agent_id=agent_id,
                intent_id=intent_id,
                kind=kind,
                score=434,
                handoff=Handoff.NONE,
                target_ref=target_ref,
            ),
            source_type="SITUATIONAL_INTENT",
            source_ref=source_ref if source_ref is not None else intent_id,
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
        intent_id="intent:request-pass434",
        kind="REQUEST_ASSISTANCE",
        target_ref=TEO,
        minute=1200,
        trigger_id="trigger:field-problem-pass434",
    )
    _record(
        ledger,
        action_id=RESPONSE,
        agent_id=TEO,
        intent_id="intent:counter-pass434",
        kind="COUNTERPROPOSE_ASSISTANCE_REQUEST",
        target_ref=MARA,
        minute=1203,
        trigger_id=REQUEST_TRIGGER,
    )
    return ledger


def _proposals(actions: WorldActionIntentLedger, *, expires=1240) -> AssistanceCounterproposalLedger:
    ledger = AssistanceCounterproposalLedger()
    record_assistance_counterproposal_terms(
        action_ledger=actions,
        proposal_ledger=ledger,
        request_action_id=REQUEST,
        response_action_id=RESPONSE,
        proposal_id=PROPOSAL,
        request_delivery_trigger_id=REQUEST_TRIGGER,
        proposed_start_minute=1230,
        proposed_end_minute=1260,
        location_ref="ouros.marea.field_office",
        scope_ref="diagnose_pump_only",
        alternative_ref="remote_parts_list",
        expires_minute=expires,
    )
    return ledger


def _queue() -> InformationEventQueue:
    return InformationEventQueue(
        channels={
            "channel:field-radio": CommunicationChannel(
                channel_id="channel:field-radio",
                kind="RADIO",
                latency_minutes=0,
                available=True,
            )
        },
        ledgers={MARA: KnowledgeLedger(MARA), TEO: KnowledgeLedger(TEO)},
    )


def _deliver(actions, proposals, queue):
    envelope = schedule_assistance_counterproposal_terms(
        action_ledger=actions,
        proposal_ledger=proposals,
        information_queue=queue,
        proposal_id=PROPOSAL,
        event_id=TERMS_EVENT,
        message_id="message:counter-terms-pass434",
        source_claim_id="claim:teo-counter-terms-pass434",
        receiver_claim_id="claim:mara-counter-terms-pass434",
        channel_id="channel:field-radio",
        created_minute=1205,
    )
    assert queue.process_due(1205)[0]["status"] == DeliveryStatus.DELIVERED.value
    return envelope


def _decision(*, kind="ACCEPT_ASSISTANCE_COUNTERPROPOSAL", agent=MARA, target=TEO, source_ref=PROPOSAL, handoff=Handoff.NONE):
    return CoordinatedDecision(
        agent_id=agent,
        trigger_ids=(TERMS_TRIGGER,),
        reasons=("KNOWLEDGE_DELIVERED",),
        decision=AgendaDecision(
            decision=Decision(
                agent_id=agent,
                intent_id=f"intent:{kind.lower()}:pass434",
                kind=kind,
                score=434,
                handoff=handoff,
                target_ref=target,
            ),
            source_type="SITUATIONAL_INTENT",
            source_ref=source_ref,
        ),
    )


def _record_decision(actions, proposals, queue, *, decision=None, minute=1210, action_id="action:mara-proposal-decision-pass434"):
    return record_assistance_counterproposal_decision_from_replan(
        action_ledger=actions,
        proposal_ledger=proposals,
        information_queue=queue,
        proposal_id=PROPOSAL,
        terms_event_id=TERMS_EVENT,
        decision_action_id=action_id,
        coordinated_decision=_decision() if decision is None else decision,
        semantic_minute=minute,
    )


def test_delivered_exact_terms_can_produce_requester_owned_acceptance() -> None:
    actions = _actions()
    proposals = _proposals(actions)
    queue = _queue()
    _deliver(actions, proposals, queue)

    outcome = _record_decision(actions, proposals, queue)
    assert outcome.proposal_id == PROPOSAL
    assert outcome.requester_id == MARA
    assert outcome.responder_id == TEO
    assert outcome.decision_kind == "ACCEPT_ASSISTANCE_COUNTERPROPOSAL"
    assert outcome.record.source_ref == PROPOSAL
    assert outcome.record.target_ref == TEO
    assert len(proposals.records) == 1


def test_rejection_is_a_distinct_requester_decision_and_does_not_mutate_proposal() -> None:
    actions = _actions()
    proposals = _proposals(actions)
    queue = _queue()
    _deliver(actions, proposals, queue)

    outcome = _record_decision(
        actions,
        proposals,
        queue,
        decision=_decision(kind="REJECT_ASSISTANCE_COUNTERPROPOSAL"),
    )
    assert outcome.decision_kind == "REJECT_ASSISTANCE_COUNTERPROPOSAL"
    assert proposals.records[PROPOSAL].proposed_start_minute == 1230
    assert all(record.intent_kind != "ACCEPT_ASSISTANCE_REQUEST" for record in actions.records.values())


def test_undelivered_terms_cannot_authorize_a_requester_decision() -> None:
    actions = _actions()
    proposals = _proposals(actions)
    queue = _queue()
    schedule_assistance_counterproposal_terms(
        action_ledger=actions,
        proposal_ledger=proposals,
        information_queue=queue,
        proposal_id=PROPOSAL,
        event_id=TERMS_EVENT,
        message_id="message:counter-terms-pass434",
        source_claim_id="claim:teo-counter-terms-pass434",
        receiver_claim_id="claim:mara-counter-terms-pass434",
        channel_id="channel:field-radio",
        created_minute=1205,
    )
    with pytest.raises(ValueError, match="DELIVERED"):
        _record_decision(actions, proposals, queue)


def test_requester_actor_exact_proposal_and_delivery_trigger_are_required() -> None:
    actions = _actions()
    proposals = _proposals(actions)
    queue = _queue()
    _deliver(actions, proposals, queue)

    with pytest.raises(ValueError, match="original requester"):
        _record_decision(actions, proposals, queue, decision=_decision(agent=TEO, target=MARA))
    with pytest.raises(ValueError, match="exact proposal"):
        _record_decision(actions, proposals, queue, decision=_decision(source_ref="proposal:wrong"))

    missing_trigger = replace(_decision(), trigger_ids=("replan:information:event:other",))
    with pytest.raises(ValueError, match="terms-delivery"):
        _record_decision(actions, proposals, queue, decision=missing_trigger)


def test_tampered_provenance_or_payload_fails_closed() -> None:
    actions = _actions()
    proposals = _proposals(actions)
    queue = _queue()
    envelope = _deliver(actions, proposals, queue)

    original = proposals.records[PROPOSAL]
    proposals.records[PROPOSAL] = replace(original, provenance_root="action:wrong")
    with pytest.raises(ValueError, match="provenance"):
        _record_decision(actions, proposals, queue)

    proposals.records[PROPOSAL] = original
    received = queue.ledgers[MARA].claims[envelope.new_claim_id]
    queue.ledgers[MARA].claims[envelope.new_claim_id] = replace(received, value='{"proposal_id":"wrong"}')
    with pytest.raises(ValueError, match="differ from authored|match durable"):
        _record_decision(actions, proposals, queue)


def test_expired_proposal_cannot_be_accepted_but_can_be_rejected_as_stale_offer() -> None:
    actions = _actions()
    proposals = _proposals(actions, expires=1208)
    queue = _queue()
    _deliver(actions, proposals, queue)

    with pytest.raises(ValueError, match="expired"):
        _record_decision(actions, proposals, queue, minute=1210)

    outcome = _record_decision(
        actions,
        proposals,
        queue,
        decision=_decision(kind="REJECT_ASSISTANCE_COUNTERPROPOSAL"),
        minute=1210,
        action_id="action:mara-reject-stale-pass434",
    )
    assert outcome.decision_kind == "REJECT_ASSISTANCE_COUNTERPROPOSAL"


def test_decision_is_not_an_autoptu_handoff_and_exact_replay_is_idempotent() -> None:
    actions = _actions()
    proposals = _proposals(actions)
    queue = _queue()
    _deliver(actions, proposals, queue)

    with pytest.raises(ValueError, match="AutoPTU"):
        _record_decision(actions, proposals, queue, decision=_decision(handoff=Handoff.REQUEST_AUTOPTU))

    first = _record_decision(actions, proposals, queue)
    replay = _record_decision(actions, proposals, queue)
    assert replay.record == first.record

    with pytest.raises(ValueError, match="conflicting content"):
        _record_decision(
            actions,
            proposals,
            queue,
            decision=_decision(kind="REJECT_ASSISTANCE_COUNTERPROPOSAL"),
        )
