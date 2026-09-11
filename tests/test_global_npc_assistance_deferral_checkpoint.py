from __future__ import annotations

import copy
import hashlib
import json

import pytest

from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_assistance_acceptance_commitment import AssistanceCommitmentLedger
from tools.global_npc_assistance_deferral import AssistanceDeferralLedger, schedule_assistance_deferral
from tools.global_npc_assistance_world_checkpoint import (
    build_assistance_world_checkpoint,
    restore_assistance_world_checkpoint,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_action_intent import WorldActionIntentLedger, WorldActionIntentRecord
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator


REQUEST = "action:request"
RESPONSE = "action:defer"
DELIVERY_TRIGGER = "replan:information:event:request"
REQUESTER = "npc:requester"
RESPONDER = "npc:responder"
DEFERRAL_ID = "deferral:responder:requester:1"


def _redigest(checkpoint: dict) -> None:
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    checkpoint["sha256"] = hashlib.sha256(raw).hexdigest()


def _state():
    agents = {
        REQUESTER: NpcAgentState(REQUESTER, AgentMode.OFFSCREEN_NAMED, "synthetic", "office"),
        RESPONDER: NpcAgentState(RESPONDER, AgentMode.OFFSCREEN_NAMED, "synthetic", "workshop"),
    }
    ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
    channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 0)}
    queue = NpcReplanQueue()
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=InformationEventQueue(channels=channels, ledgers=ledgers),
        replan_queue=queue,
        agents=agents,
    )

    actions = WorldActionIntentLedger()
    actions.records[REQUEST] = WorldActionIntentRecord(
        action_id=REQUEST,
        agent_id=REQUESTER,
        intent_id="intent:request",
        intent_kind="REQUEST_ASSISTANCE",
        target_ref=RESPONDER,
        semantic_minute=100,
        trigger_ids=("replan:information:event:warning",),
        reason_codes=("KNOWLEDGE_DELIVERED",),
        source_type="SITUATIONAL",
        source_ref="warning",
    )
    actions.records[RESPONSE] = WorldActionIntentRecord(
        action_id=RESPONSE,
        agent_id=RESPONDER,
        intent_id="intent:defer",
        intent_kind="DEFER_ASSISTANCE_REQUEST",
        target_ref=REQUESTER,
        semantic_minute=120,
        trigger_ids=(DELIVERY_TRIGGER,),
        reason_codes=("KNOWLEDGE_DELIVERED",),
        source_type="SITUATIONAL",
        source_ref=REQUEST,
    )

    deferrals = AssistanceDeferralLedger()
    schedule_assistance_deferral(
        action_ledger=actions,
        deferral_ledger=deferrals,
        replan_queue=queue,
        request_action_id=REQUEST,
        response_action_id=RESPONSE,
        deferral_id=DEFERRAL_ID,
        request_delivery_trigger_id=DELIVERY_TRIGGER,
        reconsider_minute=180,
        expires_minute=240,
        priority=7,
    )
    return coordinator, channels, actions, AssistanceCommitmentLedger(), deferrals


def test_deferral_and_future_wake_restore_as_one_generation() -> None:
    coordinator, channels, actions, commitments, deferrals = _state()
    checkpoint = build_assistance_world_checkpoint(
        coordinator,
        semantic_minute=150,
        action_ledger=actions,
        commitment_ledger=commitments,
        deferral_ledger=deferrals,
    )

    restored = restore_assistance_world_checkpoint(checkpoint, channels=channels)
    record = restored.deferral_ledger.records[DEFERRAL_ID]
    assert record.response_action_id == RESPONSE
    assert record.reconsider_minute == 180
    assert record.expires_minute == 240
    assert restored.world.coordinator.replan_queue.process_due(179) == []

    batches = restored.world.coordinator.replan_queue.process_due(180)
    assert len(batches) == 1
    assert batches[0].agent_id == RESPONDER
    assert batches[0].source_refs == (RESPONSE,)


def test_completed_deferral_wake_and_history_restore_together() -> None:
    coordinator, channels, actions, commitments, deferrals = _state()
    batches = coordinator.replan_queue.process_due(180)
    assert len(batches) == 1

    checkpoint = build_assistance_world_checkpoint(
        coordinator,
        semantic_minute=181,
        action_ledger=actions,
        commitment_ledger=commitments,
        deferral_ledger=deferrals,
    )
    restored = restore_assistance_world_checkpoint(checkpoint, channels=channels)
    trigger_id = deferrals.records[DEFERRAL_ID].trigger_id
    assert trigger_id in restored.world.coordinator.replan_queue.completed_trigger_ids
    assert restored.world.coordinator.replan_queue.process_due(999) == []
    assert DEFERRAL_ID in restored.deferral_ledger.records


def test_checkpoint_rejects_deferral_trigger_time_drift() -> None:
    coordinator, channels, actions, commitments, deferrals = _state()
    checkpoint = build_assistance_world_checkpoint(
        coordinator,
        semantic_minute=150,
        action_ledger=actions,
        commitment_ledger=commitments,
        deferral_ledger=deferrals,
    )
    corrupted = copy.deepcopy(checkpoint)
    pending = corrupted["world_checkpoint"]["replan_queue"]["pending"]
    assert pending
    pending[0]["due_minute"] = 181
    world_payload = {key: value for key, value in corrupted["world_checkpoint"].items() if key != "sha256"}
    world_raw = json.dumps(world_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    corrupted["world_checkpoint"]["sha256"] = hashlib.sha256(world_raw).hexdigest()
    _redigest(corrupted)

    with pytest.raises(ValueError, match="trigger time mismatch"):
        restore_assistance_world_checkpoint(corrupted, channels=channels)


def test_checkpoint_rejects_deferral_provenance_drift() -> None:
    coordinator, channels, actions, commitments, deferrals = _state()
    checkpoint = build_assistance_world_checkpoint(
        coordinator,
        semantic_minute=150,
        action_ledger=actions,
        commitment_ledger=commitments,
        deferral_ledger=deferrals,
    )
    corrupted = copy.deepcopy(checkpoint)
    corrupted["assistance_deferrals"]["records"][0]["provenance_root"] = "action:other"
    _redigest(corrupted)

    with pytest.raises(ValueError, match="deferral provenance mismatch"):
        restore_assistance_world_checkpoint(corrupted, channels=channels)


def test_legacy_v1_checkpoint_restores_without_inventing_deferrals() -> None:
    coordinator, channels, actions, commitments, _ = _state()
    legacy = build_assistance_world_checkpoint(
        coordinator,
        semantic_minute=150,
        action_ledger=actions,
        commitment_ledger=commitments,
    )
    legacy["schema_version"] = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V1"
    legacy.pop("assistance_deferrals")
    _redigest(legacy)

    restored = restore_assistance_world_checkpoint(legacy, channels=channels)
    assert restored.deferral_ledger.records == {}
