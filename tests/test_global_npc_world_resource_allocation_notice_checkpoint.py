import hashlib
import json

import pytest

from tests.test_global_npc_resource_allocation_notice_checkpoint import GlobalNpcResourceAllocationNoticeCheckpointTests
from tests.test_global_npc_world_resource_reschedule_checkpoint import _fixture
from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_resource_allocation_notices import (
    ResourceAllocationNoticeLedger,
    ResourceAllocationNoticeLink,
    derive_displacement_notice_obligations,
    link_notice_communication,
)
from tools.global_npc_world_resource_allocation_application_checkpoint import build_world_resource_allocation_application_checkpoint
from tools.global_npc_world_resource_allocation_notice_checkpoint import (
    WORLD_RESOURCE_ALLOCATION_NOTICE_CHECKPOINT_SCHEMA,
    build_world_resource_allocation_notice_checkpoint,
    restore_world_resource_allocation_notice_checkpoint,
)


def _digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _state(*, deliver=True, available=True):
    coordinator, channels, *_ = _fixture(deliver=True)
    state = GlobalNpcResourceAllocationNoticeCheckpointTests()._state(with_link=False)

    coordinator.agents["ori"] = NpcAgentState(
        "ori", AgentMode.OFFSCREEN_NAMED, "synthetic", "marsh-camp"
    )
    coordinator.information_queue.ledgers["ori"] = KnowledgeLedger("ori")

    channel = CommunicationChannel("wire", "REMOTE_MESSAGE", 5, available=available)
    channels["wire"] = channel
    coordinator.information_queue.channels["wire"] = channel

    notice_ledger = derive_displacement_notice_obligations(
        ResourceAllocationNoticeLedger(),
        state[9].applications[0],
        state[0],
        obligation_id_prefix="notice-obligation:allocation-1",
        created_tick=48,
        basis_refs=("application:1", "reservation:other"),
    )

    record_direct_observation(
        coordinator.information_queue.ledgers["teo"],
        claim_id="claim:allocation-change",
        subject="reservation:other:status",
        value="displaced",
        semantic_minute=49,
        confidence=100,
    )
    coordinator.information_queue.schedule(
        event_id="delivery:allocation-change",
        message_id="message:allocation-change",
        sender_id="teo",
        receiver_id="ori",
        source_claim_id="claim:allocation-change",
        new_claim_id="received:allocation-change",
        channel_id="wire",
        created_minute=49,
    )
    if deliver:
        coordinator.information_queue.process_due(54)

    notice_ledger = link_notice_communication(
        notice_ledger,
        coordinator.information_queue,
        ResourceAllocationNoticeLink(
            "notice-link:allocation-1",
            notice_ledger.obligations[0].obligation_id,
            "teo",
            "delivery:allocation-change",
            55 if deliver else 50,
        ),
    )
    return coordinator, channels, (*state[:10], notice_ledger)


def _build(*, deliver=True, available=True, semantic_minute=55):
    coordinator, channels, state = _state(deliver=deliver, available=available)
    checkpoint = build_world_resource_allocation_notice_checkpoint(
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
        notice_ledger=state[10],
    )
    return channels, state, checkpoint


def test_v14_round_trip_binds_notice_link_to_real_terminal_delivery() -> None:
    channels, state, checkpoint = _build()

    assert checkpoint["schema"] == WORLD_RESOURCE_ALLOCATION_NOTICE_CHECKPOINT_SCHEMA
    assert checkpoint["resource_state"]["schema"] == "OUROS_NPC_RESOURCE_CHECKPOINT_V9"
    restored = restore_world_resource_allocation_notice_checkpoint(checkpoint, channels=channels)
    assert restored.notice_ledger == state[10]
    queue = (
        restored.world_resource_allocation_application
        .world_resource_allocation
        .world_resource_admission
        .world_resource
        .world
        .coordinator
        .information_queue
    )
    assert queue.statuses["delivery:allocation-change"] == DeliveryStatus.DELIVERED
    assert queue.envelope_provenance("delivery:allocation-change").receiver_id == "ori"


def test_v14_terminal_failed_delivery_preserves_binding_without_faking_notification() -> None:
    channels, state, checkpoint = _build(available=False)
    restored = restore_world_resource_allocation_notice_checkpoint(checkpoint, channels=channels)
    assert restored.notice_ledger == state[10]
    queue = (
        restored.world_resource_allocation_application
        .world_resource_allocation
        .world_resource_admission
        .world_resource
        .world
        .coordinator
        .information_queue
    )
    assert queue.statuses["delivery:allocation-change"] == DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE
    assert "received:allocation-change" not in queue.ledgers["ori"].claims


def test_v14_rejects_sender_tampering_even_when_snapshot_is_resigned() -> None:
    channels, _, checkpoint = _build()
    checkpoint["resource_state"]["allocation_notice_links"][0]["sender_actor_id"] = "ema"
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)

    with pytest.raises(ValueError, match="communication sender mismatch"):
        restore_world_resource_allocation_notice_checkpoint(checkpoint, channels=channels)


def test_v14_rejects_missing_transport_provenance_even_when_snapshot_is_resigned() -> None:
    channels, _, checkpoint = _build()
    queue_snapshot = checkpoint["information_queue"]
    queue_snapshot["archived_envelopes"] = []
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _digest(payload)

    with pytest.raises(ValueError, match="communication provenance unavailable"):
        restore_world_resource_allocation_notice_checkpoint(checkpoint, channels=channels)


def test_v13_migration_keeps_notice_history_empty() -> None:
    coordinator, channels, state = _state()
    checkpoint = build_world_resource_allocation_application_checkpoint(
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
    )

    restored = restore_world_resource_allocation_notice_checkpoint(checkpoint, channels=channels)
    assert restored.notice_ledger == ResourceAllocationNoticeLedger()


def test_v14_rejects_notice_link_from_after_restored_world_time() -> None:
    channels, _, checkpoint = _build(semantic_minute=54)
    with pytest.raises(ValueError, match="link comes from the future"):
        restore_world_resource_allocation_notice_checkpoint(checkpoint, channels=channels)
