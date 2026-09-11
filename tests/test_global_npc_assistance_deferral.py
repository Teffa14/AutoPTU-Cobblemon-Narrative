from __future__ import annotations

import pytest

from tools.global_npc_assistance_deferral import (
    AssistanceDeferralLedger,
    deferral_window_state,
    schedule_assistance_deferral,
)
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_action_intent import WorldActionIntentLedger, WorldActionIntentRecord


REQUEST = "action:request"
RESPONSE = "action:defer"
DELIVERY_TRIGGER = "replan:information:event:request"
MARA = "npc:mara"
TEO = "npc:teo"


def _actions(*, response_kind: str = "DEFER_ASSISTANCE_REQUEST", responder: str = TEO, target: str = MARA) -> WorldActionIntentLedger:
    ledger = WorldActionIntentLedger()
    ledger.records[REQUEST] = WorldActionIntentRecord(
        action_id=REQUEST,
        agent_id=MARA,
        intent_id="intent:ask-teo",
        intent_kind="REQUEST_ASSISTANCE",
        target_ref=TEO,
        semantic_minute=100,
        trigger_ids=("replan:information:event:warning",),
        reason_codes=("KNOWLEDGE_DELIVERED",),
        source_type="SITUATIONAL",
        source_ref="warning",
    )
    ledger.records[RESPONSE] = WorldActionIntentRecord(
        action_id=RESPONSE,
        agent_id=responder,
        intent_id="intent:defer-mara",
        intent_kind=response_kind,
        target_ref=target,
        semantic_minute=120,
        trigger_ids=(DELIVERY_TRIGGER,),
        reason_codes=("KNOWLEDGE_DELIVERED",),
        source_type="SITUATIONAL",
        source_ref=REQUEST,
    )
    return ledger


def _schedule(*, actions: WorldActionIntentLedger | None = None, ledger: AssistanceDeferralLedger | None = None, queue: NpcReplanQueue | None = None, **overrides):
    actions = actions or _actions()
    ledger = ledger or AssistanceDeferralLedger()
    queue = queue or NpcReplanQueue()
    values = dict(
        action_ledger=actions,
        deferral_ledger=ledger,
        replan_queue=queue,
        request_action_id=REQUEST,
        response_action_id=RESPONSE,
        deferral_id="deferral:teo:mara:1",
        request_delivery_trigger_id=DELIVERY_TRIGGER,
        reconsider_minute=180,
        expires_minute=240,
        priority=7,
    )
    values.update(overrides)
    return schedule_assistance_deferral(**values), ledger, queue


def test_defer_schedules_only_responder_for_future_reconsideration() -> None:
    record, _, queue = _schedule()
    assert record.responder_id == TEO
    assert record.requester_id == MARA
    assert record.provenance_root == RESPONSE
    assert deferral_window_state(record, 179) == "WAITING"
    assert queue.process_due(179) == []

    batches = queue.process_due(180)
    assert len(batches) == 1
    assert batches[0].agent_id == TEO
    assert batches[0].reasons == ("SCHEDULE_DUE",)
    assert batches[0].source_refs == (RESPONSE,)
    assert batches[0].trigger_ids == ("replan:assistance-deferral:deferral:teo:mara:1",)
    assert deferral_window_state(record, 180) == "OPEN"
    assert deferral_window_state(record, 241) == "EXPIRED"


def test_replay_is_idempotent_and_conflicting_reuse_fails_closed() -> None:
    record, ledger, queue = _schedule()
    replay, _, _ = _schedule(ledger=ledger, queue=queue)
    assert replay == record
    assert len(queue.pending) == 1

    with pytest.raises(ValueError, match="conflicting content"):
        _schedule(ledger=ledger, queue=queue, reconsider_minute=181)


def test_snapshot_restore_preserves_deferral_without_turning_it_into_commitment() -> None:
    record, ledger, _ = _schedule()
    restored = AssistanceDeferralLedger.from_snapshot(ledger.snapshot())
    assert restored.records[record.deferral_id] == record
    assert record.provenance_root == RESPONSE


def test_only_defer_with_original_delivery_trigger_can_schedule_reconsideration() -> None:
    with pytest.raises(ValueError, match="only DEFER_ASSISTANCE_REQUEST"):
        _schedule(actions=_actions(response_kind="ACCEPT_ASSISTANCE_REQUEST"))

    with pytest.raises(ValueError, match="request-delivery replan trigger"):
        _schedule(request_delivery_trigger_id="replan:information:event:other")

    with pytest.raises(ValueError, match="actor binding"):
        _schedule(actions=_actions(responder="npc:oren"))


def test_deferral_requires_future_non_inverted_window() -> None:
    with pytest.raises(ValueError, match="must be in the future"):
        _schedule(reconsider_minute=120)
    with pytest.raises(ValueError, match="cannot precede"):
        _schedule(reconsider_minute=180, expires_minute=179)
