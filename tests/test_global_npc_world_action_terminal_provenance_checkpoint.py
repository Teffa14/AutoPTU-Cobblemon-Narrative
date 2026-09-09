import copy
import hashlib
import json

import pytest

from tests.test_global_npc_world_action_start_provenance_checkpoint import _build as _build_v17
from tools.global_npc_action_terminal_provenance import ActionTerminalProvenanceLedger
from tools.global_npc_world_action_terminal_provenance_checkpoint import (
    WORLD_ACTION_TERMINAL_PROVENANCE_CHECKPOINT_SCHEMA,
    build_world_action_terminal_provenance_checkpoint,
    restore_world_action_terminal_provenance_checkpoint,
)


def _digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _build(*, start_minute=55, terminal_minute=65):
    channels, state, runtime, selections, action_start, _ = _build_v17(semantic_minute=start_minute)
    terminal = ActionTerminalProvenanceLedger()
    start = next(iter(action_start.starts.values()))
    terminal.record_travel_arrival(start, semantic_minute=terminal_minute)
    checkpoint = build_world_action_terminal_provenance_checkpoint(
        runtime.coordinator,
        semantic_minute=terminal_minute,
        delivery_replan_provenance=runtime.ledger,
        plan_selection_provenance=selections,
        action_start_provenance=action_start,
        action_terminal_provenance=terminal,
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
    return channels, state, runtime, selections, action_start, terminal, checkpoint


def test_v18_round_trip_preserves_action_terminal_provenance() -> None:
    channels, _, _, _, _, terminal, checkpoint = _build()
    assert checkpoint["schema"] == WORLD_ACTION_TERMINAL_PROVENANCE_CHECKPOINT_SCHEMA
    restored = restore_world_action_terminal_provenance_checkpoint(checkpoint, channels=channels)
    assert restored.action_terminal_provenance.snapshot() == terminal.snapshot()


def test_v18_digest_covers_action_terminal_provenance() -> None:
    channels, _, _, _, _, _, checkpoint = _build()
    checkpoint["action_terminal_provenance"]["terminals"][0]["target_ref"] = "tampered.target"
    with pytest.raises(ValueError, match="digest mismatch"):
        restore_world_action_terminal_provenance_checkpoint(checkpoint, channels=channels)


def test_v18_rejects_terminal_replay_tampering_even_when_resigned() -> None:
    channels, _, _, _, _, _, checkpoint = _build()
    row = checkpoint["action_terminal_provenance"]["terminals"][0]
    row["evidence"]["travel_terminal"]["current_node"] = "tampered.node"
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="no longer replays"):
        restore_world_action_terminal_provenance_checkpoint(checkpoint, channels=channels)


def test_v18_rejects_missing_source_action_start_even_when_resigned() -> None:
    channels, _, _, _, _, _, checkpoint = _build()
    checkpoint["action_start_provenance"]["starts"] = []
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="missing action start"):
        restore_world_action_terminal_provenance_checkpoint(checkpoint, channels=channels)


def test_v18_rejects_future_terminal_even_when_resigned() -> None:
    channels, _, _, _, _, _, checkpoint = _build()
    row = checkpoint["action_terminal_provenance"]["terminals"][0]
    row["terminal_minute"] = 66
    row["evidence"]["travel_terminal"]["semantic_minute"] = 66
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="comes from the future"):
        restore_world_action_terminal_provenance_checkpoint(checkpoint, channels=channels)


def test_v17_migration_keeps_action_terminal_history_empty() -> None:
    channels, _, _, _, _, checkpoint = _build_v17(semantic_minute=55)
    restored = restore_world_action_terminal_provenance_checkpoint(checkpoint, channels=channels)
    assert restored.action_terminal_provenance.terminals == {}


def test_v18_does_not_infer_objective_success_from_arrival() -> None:
    channels, _, _, _, _, terminal, checkpoint = _build()
    restored = restore_world_action_terminal_provenance_checkpoint(copy.deepcopy(checkpoint), channels=channels)
    record = next(iter(restored.action_terminal_provenance.terminals.values()))
    expected = next(iter(terminal.terminals.values()))
    assert record.kind == expected.kind
    assert "mission_success" not in record.evidence
    assert "objective_success" not in record.evidence
    assert "autoptu_resolved" not in record.evidence
    assert "result_ingressed" not in record.evidence
