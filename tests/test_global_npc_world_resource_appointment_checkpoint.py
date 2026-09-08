import hashlib
import json

import pytest

from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_resource_attempt_checkpoint import snapshot_resource_state_with_attempts
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffAppointmentNotice,
    register_handoff_appointment_notice,
)
from tools.global_npc_resource_handoff_attempts import ResourceHandoffAttemptLedger
from tools.global_npc_resource_handoffs import HandoffMode, ResourceHandoffAuthorization, ResourceHandoffLedger
from tools.global_npc_resource_requests import (
    ResourceRequest,
    ResourceRequestEvent,
    ResourceRequestEventKind,
    ResourceRequestLedger,
)
from tools.global_npc_resource_reservations import ReservationLedger, ResourceReservation
from tools.global_npc_world_checkpoint import build_checkpoint
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator
from tools.global_npc_world_resource_checkpoint import (
    LEGACY_WORLD_RESOURCE_ATTEMPT_CHECKPOINT_SCHEMA,
    WORLD_RESOURCE_CHECKPOINT_SCHEMA,
    build_world_resource_checkpoint,
    restore_world_resource_checkpoint,
)


def _canonical_digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _redigest(checkpoint: dict) -> None:
    payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["sha256"] = _canonical_digest(payload)


def _fixture():
    agents = {
        "teo": NpcAgentState("teo", AgentMode.OFFSCREEN_NAMED, "synthetic", "workshop"),
        "ema": NpcAgentState("ema", AgentMode.OFFSCREEN_NAMED, "synthetic", "repair-row"),
        "nia": NpcAgentState("nia", AgentMode.OFFSCREEN_NAMED, "synthetic", "field-office"),
    }
    ledgers = {actor_id: KnowledgeLedger(actor_id) for actor_id in agents}
    channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 5)}
    queue = InformationEventQueue(channels=channels, ledgers=ledgers)
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents=agents,
    )

    reservations = ReservationLedger(
        (
            ResourceReservation(
                reservation_id="reservation:meter:ema",
                resource_id="meter:field:7",
                actor_id="ema",
                start_tick=30,
                end_tick=70,
                purpose_ref="survey:ridge",
            ),
        )
    )
    requests = ResourceRequestLedger(
        requests=(
            ResourceRequest(
                request_id="request:meter:ema",
                requester_actor_id="ema",
                provider_actor_id="teo",
                resource_id="meter:field:7",
                created_tick=4,
                expires_at_tick=70,
                purpose_ref="survey:ridge",
            ),
        ),
        events=(
            ResourceRequestEvent(
                event_id="request-event:meter:accepted",
                request_id="request:meter:ema",
                actor_id="teo",
                kind=ResourceRequestEventKind.ACCEPTED,
                at_tick=8,
                offered_resource_id="meter:field:7",
                reason_ref="meter-ready",
            ),
        ),
    )
    handoffs = ResourceHandoffLedger(
        authorizations=(
            ResourceHandoffAuthorization(
                authorization_id="handoff-auth:meter:ema",
                request_id="request:meter:ema",
                provider_actor_id="teo",
                accountable_actor_id="nia",
                receiving_actor_id="ema",
                resource_id="meter:field:7",
                mode=HandoffMode.PICKUP,
                handoff_location_ref="workshop",
                valid_from_tick=20,
                valid_until_tick=50,
                authority_ref="request-event:meter:accepted",
            ),
        )
    )
    attempts = ResourceHandoffAttemptLedger()

    record_direct_observation(
        queue.ledgers["teo"],
        claim_id="claim:confirm:meter",
        subject="handoff-auth:meter:ema:appointment-update",
        value="CONFIRM",
        semantic_minute=12,
        confidence=100,
    )
    queue.schedule(
        event_id="delivery:confirm:meter",
        message_id="message:confirm:meter",
        sender_id="teo",
        receiver_id="ema",
        source_claim_id="claim:confirm:meter",
        new_claim_id="received:confirm:meter",
        channel_id="wire",
        created_minute=12,
    )
    notice = ResourceHandoffAppointmentNotice(
        notice_id="notice:confirm:meter",
        authorization_id="handoff-auth:meter:ema",
        sender_actor_id="teo",
        receiver_actor_id="ema",
        kind=HandoffAppointmentNoticeKind.CONFIRM,
        source_claim_id="claim:confirm:meter",
        communication_event_id="delivery:confirm:meter",
        created_tick=12,
        reason_ref="pickup-window-confirmation",
    )
    appointments = register_handoff_appointment_notice(
        ResourceHandoffAppointmentLedger(),
        handoffs,
        notice,
    )
    return coordinator, channels, reservations, requests, handoffs, attempts, appointments


def test_v9_round_trip_preserves_notice_and_queued_envelope_binding() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments = _fixture()
    checkpoint = build_world_resource_checkpoint(
        coordinator,
        semantic_minute=12,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
    )

    assert checkpoint["schema"] == WORLD_RESOURCE_CHECKPOINT_SCHEMA
    assert checkpoint["resource_state"]["schema"] == "OUROS_NPC_RESOURCE_CHECKPOINT_V4"
    restored = restore_world_resource_checkpoint(checkpoint, channels=channels)
    assert restored.appointment_ledger == appointments
    envelope = restored.world.coordinator.information_queue.envelope_provenance("delivery:confirm:meter")
    assert envelope is not None
    assert envelope.sender_id == "teo"
    assert envelope.receiver_id == "ema"


def test_v9_delivered_notice_binding_survives_restart() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments = _fixture()
    coordinator.information_queue.process_due(17)
    checkpoint = build_world_resource_checkpoint(
        coordinator,
        semantic_minute=17,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
    )

    restored = restore_world_resource_checkpoint(checkpoint, channels=channels)
    envelope = restored.world.coordinator.information_queue.envelope_provenance("delivery:confirm:meter")
    assert envelope is not None
    assert envelope.message_id == "message:confirm:meter"
    assert restored.appointment_ledger == appointments


def test_v9_notice_receiver_must_match_restored_communication_envelope() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments = _fixture()
    checkpoint = build_world_resource_checkpoint(
        coordinator,
        semantic_minute=12,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
    )
    checkpoint["resource_state"]["handoff_appointment_notices"][0]["receiver_actor_id"] = "nia"
    _redigest(checkpoint)

    with pytest.raises(ValueError, match="receiver mismatch"):
        restore_world_resource_checkpoint(checkpoint, channels=channels)


def test_v9_notice_requires_restored_communication_provenance() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments = _fixture()
    checkpoint = build_world_resource_checkpoint(
        coordinator,
        semantic_minute=12,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
    )
    checkpoint["resource_state"]["handoff_appointment_notices"][0]["communication_event_id"] = "delivery:missing"
    _redigest(checkpoint)

    with pytest.raises(ValueError, match="communication provenance unavailable"):
        restore_world_resource_checkpoint(checkpoint, channels=channels)


def test_v9_notice_source_claim_must_match_restored_envelope() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments = _fixture()
    checkpoint = build_world_resource_checkpoint(
        coordinator,
        semantic_minute=12,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
    )
    checkpoint["resource_state"]["handoff_appointment_notices"][0]["source_claim_id"] = "claim:other"
    _redigest(checkpoint)

    with pytest.raises(ValueError, match="source claim mismatch"):
        restore_world_resource_checkpoint(checkpoint, channels=channels)


def test_v8_restores_attempt_history_and_explicit_empty_appointment_history() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, _ = _fixture()
    checkpoint = build_checkpoint(coordinator, semantic_minute=12)
    checkpoint = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["schema"] = LEGACY_WORLD_RESOURCE_ATTEMPT_CHECKPOINT_SCHEMA
    checkpoint["resource_state"] = snapshot_resource_state_with_attempts(
        reservations,
        requests,
        handoffs,
        attempts,
    )
    checkpoint["sha256"] = _canonical_digest(checkpoint)

    restored = restore_world_resource_checkpoint(checkpoint, channels=channels)
    assert restored.reservation_ledger == reservations
    assert restored.request_ledger == requests
    assert restored.handoff_ledger == handoffs
    assert restored.attempt_ledger == attempts
    assert restored.appointment_ledger == ResourceHandoffAppointmentLedger()
