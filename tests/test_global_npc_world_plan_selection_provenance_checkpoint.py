import copy
import hashlib
import json

import pytest

from tests.test_global_npc_world_delivery_replan_provenance_checkpoint import _build as _build_v15
from tools.global_npc_ai import NpcIntent
from tools.global_npc_plan_selection_provenance import PlanSelectionProvenanceLedger
from tools.global_npc_replanning import ReplanBatch
from tools.global_npc_world_plan_selection_provenance_checkpoint import (
    WORLD_PLAN_SELECTION_PROVENANCE_CHECKPOINT_SCHEMA,
    build_world_plan_selection_provenance_checkpoint,
    restore_world_plan_selection_provenance_checkpoint,
)


def _digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _selection(runtime):
    consumed = next(iter(runtime.ledger.consumptions.values()))
    batch = ReplanBatch(
        agent_id=consumed.agent_id,
        semantic_minute=consumed.processed_minute,
        trigger_ids=(consumed.trigger_id,),
        reasons=(consumed.reason,),
        source_refs=(consumed.source_ref,),
        highest_priority=consumed.priority,
    )
    agent = runtime.coordinator.agents[consumed.agent_id]
    ledger = PlanSelectionProvenanceLedger()
    ledger.record_selection(
        batch,
        agent,
        situational_intents=(
            NpcIntent(
                intent_id="respond-to-delivered-update",
                kind="RESPOND_TO_DELIVERED_UPDATE",
                base_priority=5,
                urgency=3,
                obligation=2,
                target_ref=consumed.source_ref,
            ),
        ),
    )
    return ledger


def _build(*, semantic_minute=55):
    channels, state, runtime, _ = _build_v15(semantic_minute=semantic_minute)
    selection = _selection(runtime)
    checkpoint = build_world_plan_selection_provenance_checkpoint(
        runtime.coordinator,
        semantic_minute=semantic_minute,
        delivery_replan_provenance=runtime.ledger,
        plan_selection_provenance=selection,
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
    return channels, state, runtime, selection, checkpoint


def test_v16_round_trip_preserves_plan_selection_context() -> None:
    channels, _, _, selection, checkpoint = _build()
    assert checkpoint["schema"] == WORLD_PLAN_SELECTION_PROVENANCE_CHECKPOINT_SCHEMA
    restored = restore_world_plan_selection_provenance_checkpoint(checkpoint, channels=channels)
    assert restored.plan_selection_provenance.snapshot() == selection.snapshot()


def test_v16_digest_covers_plan_selection_provenance() -> None:
    channels, _, _, _, checkpoint = _build()
    checkpoint["plan_selection_provenance"]["selections"][0]["continuity_bonus"] = 9
    with pytest.raises(ValueError, match="digest mismatch"):
        restore_world_plan_selection_provenance_checkpoint(checkpoint, channels=channels)


def test_v16_rejects_selected_winner_tampering_even_when_resigned() -> None:
    channels, _, _, _, checkpoint = _build()
    checkpoint["plan_selection_provenance"]["selections"][0]["selected"]["intent_id"] = "tampered-intent"
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="no longer replays"):
        restore_world_plan_selection_provenance_checkpoint(checkpoint, channels=channels)


def test_v16_rejects_consumption_history_removal_even_when_resigned() -> None:
    channels, _, _, _, checkpoint = _build()
    checkpoint["delivery_replan_provenance"]["consumptions"] = []
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="unconsumed trigger"):
        restore_world_plan_selection_provenance_checkpoint(checkpoint, channels=channels)


def test_v16_rejects_batch_provenance_tampering_even_when_resigned() -> None:
    channels, _, _, _, checkpoint = _build()
    checkpoint["plan_selection_provenance"]["selections"][0]["batch_key"] = "replan-batch:other:55"
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="batch provenance mismatch"):
        restore_world_plan_selection_provenance_checkpoint(checkpoint, channels=channels)


def test_v16_rejects_future_selection_even_when_resigned() -> None:
    channels, _, _, _, checkpoint = _build()
    row = checkpoint["plan_selection_provenance"]["selections"][0]
    row["semantic_minute"] = 56
    row["batch_key"] = f"replan-batch:{row['agent_id']}:56"
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="no longer replays|comes from the future|minute mismatch"):
        restore_world_plan_selection_provenance_checkpoint(checkpoint, channels=channels)


def test_v15_migration_keeps_plan_selection_history_empty() -> None:
    channels, _, _, _, checkpoint = _build_v15()
    restored = restore_world_plan_selection_provenance_checkpoint(checkpoint, channels=channels)
    assert restored.plan_selection_provenance.selections == {}


def test_v16_keeps_plan_selection_separate_from_later_action_state() -> None:
    channels, _, _, selection, checkpoint = _build()
    altered = copy.deepcopy(checkpoint)
    restored = restore_world_plan_selection_provenance_checkpoint(altered, channels=channels)
    record = next(iter(restored.plan_selection_provenance.selections.values()))
    expected = next(iter(selection.selections.values()))
    assert record.selected == expected.selected
    assert "action_started" not in record.selected
    assert "action_succeeded" not in record.selected
