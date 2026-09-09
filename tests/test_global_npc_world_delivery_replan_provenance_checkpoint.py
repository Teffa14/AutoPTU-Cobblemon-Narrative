import copy
import hashlib
import json

import pytest

from tests.test_global_npc_world_resource_allocation_notice_checkpoint import _state
from tools.global_npc_delivery_replan_provenance import ProvenanceAwareWorldEventRuntime
from tools.global_npc_world_delivery_replan_provenance_checkpoint import (
    WORLD_DELIVERY_REPLAN_PROVENANCE_CHECKPOINT_SCHEMA,
    build_world_delivery_replan_provenance_checkpoint,
    restore_world_delivery_replan_provenance_checkpoint,
)
from tools.global_npc_world_resource_allocation_notice_checkpoint import build_world_resource_allocation_notice_checkpoint


def _digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _build(*, semantic_minute=55):
    coordinator, channels, state = _state(deliver=False)
    runtime = ProvenanceAwareWorldEventRuntime(coordinator)
    runtime.process_cycle(54, delivery_budget=1, replan_priority=8)
    checkpoint = build_world_delivery_replan_provenance_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        delivery_replan_provenance=runtime.ledger,
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
    return channels, state, runtime, checkpoint


def test_v15_round_trip_preserves_delivery_materialization_and_consumed_replan() -> None:
    channels, _, runtime, checkpoint = _build()
    assert checkpoint["schema"] == WORLD_DELIVERY_REPLAN_PROVENANCE_CHECKPOINT_SCHEMA
    restored = restore_world_delivery_replan_provenance_checkpoint(checkpoint, channels=channels)
    assert restored.delivery_replan_provenance.materializations == runtime.ledger.materializations
    assert restored.delivery_replan_provenance.consumptions == runtime.ledger.consumptions


def test_v15_digest_covers_delivery_replan_provenance() -> None:
    channels, _, _, checkpoint = _build()
    checkpoint["delivery_replan_provenance"]["consumptions"][0]["priority"] = 99
    with pytest.raises(ValueError, match="digest mismatch"):
        restore_world_delivery_replan_provenance_checkpoint(checkpoint, channels=channels)


def test_v15_rejects_receiver_tampering_even_when_resigned() -> None:
    channels, _, _, checkpoint = _build()
    checkpoint["delivery_replan_provenance"]["materializations"][0]["receiver_id"] = "teo"
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="receiver mismatch"):
        restore_world_delivery_replan_provenance_checkpoint(checkpoint, channels=channels)


def test_v15_rejects_consumed_trigger_source_tampering_even_when_resigned() -> None:
    channels, _, _, checkpoint = _build()
    checkpoint["delivery_replan_provenance"]["consumptions"][0]["source_ref"] = "delivery:other"
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="lacks materialization receipt"):
        restore_world_delivery_replan_provenance_checkpoint(checkpoint, channels=channels)


def test_v15_rejects_future_materialization_even_when_resigned() -> None:
    channels, _, _, checkpoint = _build(semantic_minute=54)
    checkpoint["delivery_replan_provenance"]["materializations"][0]["materialized_minute"] = 55
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="comes from the future"):
        restore_world_delivery_replan_provenance_checkpoint(checkpoint, channels=channels)


def test_v14_migration_keeps_delivery_replan_provenance_empty() -> None:
    coordinator, channels, state = _state(deliver=False)
    checkpoint = build_world_resource_allocation_notice_checkpoint(
        coordinator,
        semantic_minute=55,
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
    restored = restore_world_delivery_replan_provenance_checkpoint(checkpoint, channels=channels)
    assert restored.delivery_replan_provenance.materializations == {}
    assert restored.delivery_replan_provenance.consumptions == {}


def test_v15_rejects_missing_completed_trigger_history_even_when_resigned() -> None:
    channels, _, _, checkpoint = _build()
    replan = copy.deepcopy(checkpoint["replan_queue"])
    replan["completed_trigger_ids"] = []
    checkpoint["replan_queue"] = replan
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)
    with pytest.raises(ValueError, match="incomplete trigger"):
        restore_world_delivery_replan_provenance_checkpoint(checkpoint, channels=channels)
