import copy
import hashlib
import json

import pytest

from tests.test_global_npc_world_plan_selection_provenance_checkpoint import _build as _build_v16
from tools.global_npc_action_start_provenance import ActionStartProvenanceLedger
from tools.global_npc_travel import RouteEdge, TravelPlan, TravelState
from tools.global_npc_world_action_start_provenance_checkpoint import (
    WORLD_ACTION_START_PROVENANCE_CHECKPOINT_SCHEMA,
    build_world_action_start_provenance_checkpoint,
    restore_world_action_start_provenance_checkpoint,
)


def _digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _action_start(runtime, selections, *, semantic_minute: int):
    selection = next(iter(selections.selections.values()))
    agent = runtime.coordinator.agents[selection.agent_id]
    target_ref = str(selection.selected["target_ref"])
    edge = RouteEdge(
        edge_id="edge.action-start-fixture",
        from_node=agent.location_ref,
        to_node=target_ref,
        duration_minutes=10,
    )
    plan = TravelPlan(
        plan_id="travel.action-start-fixture",
        agent_id=agent.agent_id,
        origin_node=agent.location_ref,
        destination_node=target_ref,
        edge_ids=(edge.edge_id,),
        departure_minute=semantic_minute,
        expected_arrival_minute=semantic_minute + edge.duration_minutes,
        reason_ref=selection.selection_id,
    )
    state = TravelState(
        plan=plan,
        current_node=agent.location_ref,
        semantic_minute=semantic_minute,
    )
    ledger = ActionStartProvenanceLedger()
    ledger.record_travel_start(
        selection,
        agent,
        state,
        (edge,),
        semantic_minute=semantic_minute,
    )
    return ledger


def _build(*, semantic_minute=55):
    channels, state, runtime, selections, _ = _build_v16(semantic_minute=semantic_minute)
    action_start = _action_start(runtime, selections, semantic_minute=semantic_minute)
    checkpoint = build_world_action_start_provenance_checkpoint(
        runtime.coordinator,
        semantic_minute=semantic_minute,
        delivery_replan_provenance=runtime.ledger,
        plan_selection_provenance=selections,
        action_start_provenance=action_start,
        reservation_ledger=state[0],
        request_ledger=state[1],
        handoff_ledger=state[2],
        attempt_ledger=state[3],
        appointment_ledger=state[4],
        reschedule_ledger=state[5],
        admission_ledger=state[6],
        authority_evidence=state[7],
        resolution_ledger=state[8],
        application_ledger=state[9],
        notice_ledger=state[10],
    )
    return channels, state, runtime, selections, action_start, checkpoint


def test_v17_round_trip_preserves_action_start_provenance() -> None:
    channels, _, _, _, action_start, checkpoint = _build()
    assert checkpoint["schema"] == WORLD_ACTION_START_PROVENANCE_CHECKPOINT_SCHEMA
    restored = restore_world_action_start_provenance_checkpoint(checkpoint, channels=channels)
    assert restored.action_start_provenance.snapshot() == action_start.snapshot()


def test_v17_digest_covers_action_start_provenance() -> None:
    channels, _, _, _, _, checkpoint = _build()
    checkpoint["action_start_provenance"]["starts"][0]["target_ref"] = "tampered.target"
    with pytest.raises(ValueError, match="digest mismatch"):
        restore_world_action_start_provenance_checkpoint(checkpoint, channels=channels)


def test_v17_rejects_replay_tampering_even_when_resigned() -> None:
    channels, _, _, _, _, checkpoint = _build()
    row = checkpoint["action_start_provenance"]["starts"][0]
    row["evidence"]["travel_after"]["current_node"] = "tampered.node"
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="no longer replays"):
        restore_world_action_start_provenance_checkpoint(checkpoint, channels=channels)


def test_v17_rejects_missing_plan_selection_even_when_resigned() -> None:
    channels, _, _, _, _, checkpoint = _build()
    checkpoint["plan_selection_provenance"]["selections"] = []
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="missing plan selection"):
        restore_world_action_start_provenance_checkpoint(checkpoint, channels=channels)


def test_v17_rejects_future_action_start_even_when_resigned() -> None:
    channels, _, _, _, _, checkpoint = _build(semantic_minute=55)
    row = checkpoint["action_start_provenance"]["starts"][0]
    row["started_minute"] = 56
    row["evidence"]["travel_after"]["edge_started_minute"] = 56
    row["evidence"]["travel_after"]["semantic_minute"] = 56
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="comes from the future"):
        restore_world_action_start_provenance_checkpoint(checkpoint, channels=channels)


def test_v16_migration_keeps_action_start_history_empty() -> None:
    channels, _, _, _, checkpoint = _build_v16()
    restored = restore_world_action_start_provenance_checkpoint(checkpoint, channels=channels)
    assert restored.action_start_provenance.starts == {}


def test_v17_does_not_infer_completion_from_action_start() -> None:
    channels, _, _, _, action_start, checkpoint = _build()
    restored = restore_world_action_start_provenance_checkpoint(copy.deepcopy(checkpoint), channels=channels)
    record = next(iter(restored.action_start_provenance.starts.values()))
    expected = next(iter(action_start.starts.values()))
    assert record.kind == expected.kind
    assert "completed" not in record.evidence
    assert "succeeded" not in record.evidence
    assert "result" not in record.evidence
