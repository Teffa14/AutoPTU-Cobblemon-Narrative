import hashlib
import json

import pytest

from tests.test_global_npc_resource_allocation_application_checkpoint import GlobalNpcResourceAllocationApplicationCheckpointTests
from tests.test_global_npc_world_resource_reschedule_checkpoint import _fixture
from tools.global_npc_resource_allocation_application import ResourceAllocationApplicationLedger
from tools.global_npc_world_resource_allocation_checkpoint import build_world_resource_allocation_checkpoint
from tools.global_npc_world_resource_allocation_application_checkpoint import (
    WORLD_RESOURCE_ALLOCATION_APPLICATION_CHECKPOINT_SCHEMA,
    build_world_resource_allocation_application_checkpoint,
    restore_world_resource_allocation_application_checkpoint,
)


def _digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _state():
    coordinator, channels, *_ = _fixture(deliver=True)
    resource_state = GlobalNpcResourceAllocationApplicationCheckpointTests()._state()
    return coordinator, channels, resource_state


def _build(semantic_minute: int = 50):
    coordinator, channels, state = _state()
    checkpoint = build_world_resource_allocation_application_checkpoint(
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
        application_ledger=state[9],
    )
    return channels, state, checkpoint


def test_v13_round_trip_binds_application_to_same_world_instant() -> None:
    channels, state, checkpoint = _build()

    assert checkpoint["schema"] == WORLD_RESOURCE_ALLOCATION_APPLICATION_CHECKPOINT_SCHEMA
    assert checkpoint["resource_state"]["schema"] == "OUROS_NPC_RESOURCE_CHECKPOINT_V8"
    restored = restore_world_resource_allocation_application_checkpoint(checkpoint, channels=channels)
    assert restored.application_ledger == state[9]
    assert restored.world_resource_allocation.resolution_ledger == state[8]
    assert restored.world_resource_allocation.authority_evidence == state[7]
    assert restored.world_resource_allocation.world_resource_admission.admission_ledger == state[6]


def test_v13_global_digest_covers_application() -> None:
    channels, _, checkpoint = _build()
    checkpoint["resource_state"]["allocation_applications"][0]["applied_tick"] = 48

    with pytest.raises(ValueError, match="digest mismatch"):
        restore_world_resource_allocation_application_checkpoint(checkpoint, channels=channels)


def test_v13_rejects_application_from_after_restored_world_time() -> None:
    channels, _, checkpoint = _build()
    checkpoint["semantic_minute"] = 46
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)

    with pytest.raises(ValueError, match="application comes from the future"):
        restore_world_resource_allocation_application_checkpoint(checkpoint, channels=channels)


def test_v12_migration_keeps_application_history_empty() -> None:
    coordinator, channels, state = _state()
    checkpoint = build_world_resource_allocation_checkpoint(
        coordinator,
        semantic_minute=50,
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

    restored = restore_world_resource_allocation_application_checkpoint(checkpoint, channels=channels)
    assert restored.world_resource_allocation.resolution_ledger == state[8]
    assert restored.application_ledger == ResourceAllocationApplicationLedger()


def test_v13_rejects_application_if_source_resolution_is_removed_even_when_resigned() -> None:
    channels, _, checkpoint = _build()
    checkpoint["resource_state"]["allocation_resolutions"] = []
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)

    with pytest.raises(ValueError, match="missing resolution"):
        restore_world_resource_allocation_application_checkpoint(checkpoint, channels=channels)
