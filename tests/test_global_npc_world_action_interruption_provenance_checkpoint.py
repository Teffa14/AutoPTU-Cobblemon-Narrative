import copy
import hashlib
import json

import pytest

from tests.test_global_npc_world_action_start_provenance_checkpoint import _build as _build_v17
from tools.global_npc_action_interruption_provenance import ActionInterruptionProvenanceLedger
from tools.global_npc_action_terminal_provenance import ActionTerminalProvenanceLedger
from tools.global_npc_travel import RouteEdge
from tools.global_npc_world_action_interruption_provenance_checkpoint import (
    WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
    build_world_action_interruption_provenance_checkpoint,
    restore_world_action_interruption_provenance_checkpoint,
)
from tools.global_npc_world_action_terminal_provenance_checkpoint import (
    build_world_action_terminal_provenance_checkpoint,
)


def _digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _blocked_edge_for(start):
    edge_id = start.evidence["travel_after"]["plan"]["edge_ids"][0]
    origin = start.evidence["travel_after"]["plan"]["origin_node"]
    destination = start.evidence["travel_after"]["plan"]["destination_node"]
    return RouteEdge(edge_id, origin, destination, 10, enabled=False)


def _build(*, start_minute=55, interruption_minute=59):
    channels, state, runtime, selections, action_start, _ = _build_v17(semantic_minute=start_minute)
    terminal = ActionTerminalProvenanceLedger()
    interruption = ActionInterruptionProvenanceLedger()
    start = next(iter(action_start.starts.values()))
    interruption.record_travel_replan_required(
        start,
        (_blocked_edge_for(start),),
        semantic_minute=interruption_minute,
    )
    checkpoint = build_world_action_interruption_provenance_checkpoint(
        runtime.coordinator,
        semantic_minute=interruption_minute,
        delivery_replan_provenance=runtime.ledger,
        plan_selection_provenance=selections,
        action_start_provenance=action_start,
        action_terminal_provenance=terminal,
        action_interruption_provenance=interruption,
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
    return channels, state, runtime, selections, action_start, terminal, interruption, checkpoint


def test_v19_round_trip_preserves_action_interruption_provenance() -> None:
    channels, _, _, _, _, _, interruption, checkpoint = _build()
    assert checkpoint["schema"] == WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA
    restored = restore_world_action_interruption_provenance_checkpoint(checkpoint, channels=channels)
    assert restored.action_interruption_provenance.snapshot() == interruption.snapshot()


def test_v19_digest_covers_action_interruption_provenance() -> None:
    channels, _, _, _, _, _, _, checkpoint = _build()
    checkpoint["action_interruption_provenance"]["interruptions"][0]["target_ref"] = "tampered.target"
    with pytest.raises(ValueError, match="digest mismatch"):
        restore_world_action_interruption_provenance_checkpoint(checkpoint, channels=channels)


def test_v19_rejects_interruption_replay_tampering_even_when_resigned() -> None:
    channels, _, _, _, _, _, _, checkpoint = _build()
    row = checkpoint["action_interruption_provenance"]["interruptions"][0]
    row["evidence"]["edges_at_interruption"][0]["enabled"] = True
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="no longer replays"):
        restore_world_action_interruption_provenance_checkpoint(checkpoint, channels=channels)


def test_v19_rejects_missing_source_action_start_even_when_resigned() -> None:
    channels, _, _, _, _, _, _, checkpoint = _build()
    checkpoint["action_start_provenance"]["starts"] = []
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="missing action start"):
        restore_world_action_interruption_provenance_checkpoint(checkpoint, channels=channels)


def test_v19_rejects_future_interruption_even_when_resigned() -> None:
    channels, _, _, _, _, _, _, checkpoint = _build()
    row = checkpoint["action_interruption_provenance"]["interruptions"][0]
    row["interrupted_minute"] = 60
    row["evidence"]["travel_interrupted"]["semantic_minute"] = 60
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="comes from the future"):
        restore_world_action_interruption_provenance_checkpoint(checkpoint, channels=channels)


def test_v18_migration_keeps_action_interruption_history_empty() -> None:
    channels, state, runtime, selections, action_start, _ = _build_v17(semantic_minute=55)
    terminal = ActionTerminalProvenanceLedger()
    checkpoint = build_world_action_terminal_provenance_checkpoint(
        runtime.coordinator,
        semantic_minute=55,
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
    restored = restore_world_action_interruption_provenance_checkpoint(checkpoint, channels=channels)
    assert restored.action_interruption_provenance.interruptions == {}


def test_v19_rejects_arrival_and_interruption_for_same_action_start() -> None:
    channels, state, runtime, selections, action_start, _, interruption, _ = _build()
    terminal = ActionTerminalProvenanceLedger()
    start = next(iter(action_start.starts.values()))
    terminal.record_travel_arrival(start, semantic_minute=65)
    with pytest.raises(ValueError, match="conflicting terminal and interruption outcomes"):
        build_world_action_interruption_provenance_checkpoint(
            runtime.coordinator,
            semantic_minute=65,
            delivery_replan_provenance=runtime.ledger,
            plan_selection_provenance=selections,
            action_start_provenance=action_start,
            action_terminal_provenance=terminal,
            action_interruption_provenance=interruption,
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


def test_v19_does_not_infer_failure_or_cancellation_from_interruption() -> None:
    channels, _, _, _, _, _, interruption, checkpoint = _build()
    restored = restore_world_action_interruption_provenance_checkpoint(copy.deepcopy(checkpoint), channels=channels)
    record = next(iter(restored.action_interruption_provenance.interruptions.values()))
    expected = next(iter(interruption.interruptions.values()))
    assert record.kind == expected.kind
    assert "action_failed" not in record.evidence
    assert "action_canceled" not in record.evidence
    assert "objective_failed" not in record.evidence
