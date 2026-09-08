import hashlib
import json

import pytest

from tests.test_global_npc_resource_allocation_checkpoint import GlobalNpcResourceAllocationCheckpointTests
from tests.test_global_npc_world_resource_reschedule_checkpoint import _fixture
from tools.global_npc_resource_allocation_resolution import ResourceAllocationResolutionLedger
from tools.global_npc_world_resource_admission_checkpoint import build_world_resource_admission_checkpoint
from tools.global_npc_world_resource_allocation_checkpoint import (
    WORLD_RESOURCE_ALLOCATION_CHECKPOINT_SCHEMA,
    build_world_resource_allocation_checkpoint,
    restore_world_resource_allocation_checkpoint,
)


def _digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _state():
    coordinator, channels, *_ = _fixture(deliver=True)
    resource_state = GlobalNpcResourceAllocationCheckpointTests()._state()
    return coordinator, channels, resource_state


def _build(semantic_minute: int = 50):
    coordinator, channels, state = _state()
    checkpoint = build_world_resource_allocation_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        reservation_ledger=state[0],
        request_ledger=state[1],
        handoff_ledger=state[2],
        attempt_ledger=state[3],
        appointment_ledger=state[4],
        reschedule_ledger=state[5],
        admission_ledger=state[6],
        authority_evidence=state[7],
        resolution_ledger=state[8],
    )
    return channels, state, checkpoint


def test_v12_round_trip_binds_allocation_decision_to_same_world_instant() -> None:
    channels, state, checkpoint = _build()

    assert checkpoint["schema"] == WORLD_RESOURCE_ALLOCATION_CHECKPOINT_SCHEMA
    assert checkpoint["resource_state"]["schema"] == "OUROS_NPC_RESOURCE_CHECKPOINT_V7"
    restored = restore_world_resource_allocation_checkpoint(checkpoint, channels=channels)
    assert restored.authority_evidence == state[7]
    assert restored.resolution_ledger == state[8]
    assert restored.world_resource_admission.admission_ledger == state[6]
    assert restored.world_resource_admission.world_resource.reservation_ledger == state[0]
    assert (
        restored.world_resource_admission.world_resource.world.coordinator.information_queue.envelope_provenance(
            "delivery:reschedule"
        )
        is not None
    )


def test_v12_global_digest_covers_allocation_decision() -> None:
    channels, _, checkpoint = _build()
    checkpoint["resource_state"]["allocation_resolutions"][0]["resolution_kind"] = "DEFER"

    with pytest.raises(ValueError, match="digest mismatch"):
        restore_world_resource_allocation_checkpoint(checkpoint, channels=channels)


def test_v12_rejects_allocation_decision_from_after_restored_world_time() -> None:
    channels, _, checkpoint = _build()
    checkpoint["semantic_minute"] = 44
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)

    with pytest.raises(ValueError, match="resolution comes from the future"):
        restore_world_resource_allocation_checkpoint(checkpoint, channels=channels)


def test_v11_migration_keeps_allocation_history_empty() -> None:
    coordinator, channels, state = _state()
    checkpoint = build_world_resource_admission_checkpoint(
        coordinator,
        semantic_minute=50,
        reservation_ledger=state[0],
        request_ledger=state[1],
        handoff_ledger=state[2],
        attempt_ledger=state[3],
        appointment_ledger=state[4],
        reschedule_ledger=state[5],
        admission_ledger=state[6],
    )

    restored = restore_world_resource_allocation_checkpoint(checkpoint, channels=channels)
    assert restored.world_resource_admission.admission_ledger == state[6]
    assert restored.authority_evidence == ()
    assert restored.resolution_ledger == ResourceAllocationResolutionLedger()


def test_v12_rejects_allocation_if_historical_conflict_is_removed_even_when_resigned() -> None:
    channels, _, checkpoint = _build()
    checkpoint["resource_state"]["reschedule_admission_records"] = []
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)

    with pytest.raises(ValueError, match="matching historical conflict admission"):
        restore_world_resource_allocation_checkpoint(checkpoint, channels=channels)


def test_v12_rejects_authority_retargeted_to_another_resource_even_when_resigned() -> None:
    channels, _, checkpoint = _build()
    checkpoint["resource_state"]["allocation_authority_evidence"][0]["target_resource_id"] = "meter:other"
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)

    with pytest.raises(ValueError, match="authority resource mismatch"):
        restore_world_resource_allocation_checkpoint(checkpoint, channels=channels)
