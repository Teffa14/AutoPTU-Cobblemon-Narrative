import hashlib
import json

import pytest

from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_resource_appointment_checkpoint import snapshot_resource_state_with_appointment_notices
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffAppointmentNotice,
)
from tools.global_npc_resource_handoff_attempts import ResourceHandoffAttemptLedger
from tools.global_npc_resource_handoff_rescheduling import (
    HandoffRescheduleDecisionKind,
    ResourceHandoffAuthorizationReplacement,
    ResourceHandoffRescheduleDecision,
    ResourceHandoffRescheduleLedger,
    ResourceHandoffRescheduleProposal,
)
from tools.global_npc_resource_handoffs import HandoffMode, ResourceHandoffAuthorization, ResourceHandoffLedger
from tools.global_npc_resource_requests import (
    ResourceRequest,
    ResourceRequestEvent,
    ResourceRequestEventKind,
    ResourceRequestLedger,
)
from tools.global_npc_resource_reservations import ReservationLedger
from tools.global_npc_world_checkpoint import build_checkpoint
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator
from tools.global_npc_world_resource_checkpoint import (
    LEGACY_WORLD_RESOURCE_APPOINTMENT_CHECKPOINT_SCHEMA,
    WORLD_RESOURCE_CHECKPOINT_SCHEMA,
    build_world_resource_checkpoint,
    restore_world_resource_checkpoint,
)


def _digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _fixture(*, deliver: bool):
    agents = {
        "teo": NpcAgentState("teo", AgentMode.OFFSCREEN_NAMED, "synthetic", "repair-row"),
        "ema": NpcAgentState("ema", AgentMode.OFFSCREEN_NAMED, "synthetic", "field-office"),
        "nerea": NpcAgentState("nerea", AgentMode.OFFSCREEN_NAMED, "synthetic", "ridge"),
    }
    ledgers = {actor_id: KnowledgeLedger(actor_id) for actor_id in agents}
    channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 5)}
    queue = InformationEventQueue(channels=channels, ledgers=ledgers)
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=NpcReplanQueue(),
        agents=agents,
    )

    requests = ResourceRequestLedger(
        requests=(ResourceRequest(
            request_id="request:meter:nerea", requester_actor_id="nerea", provider_actor_id="teo",
            resource_id="meter:field:7", created_tick=4, expires_at_tick=150, purpose_ref="survey:ridge",
        ),),
        events=(ResourceRequestEvent(
            event_id="request-event:accepted", request_id="request:meter:nerea", actor_id="teo",
            kind=ResourceRequestEventKind.ACCEPTED, at_tick=8, offered_resource_id="meter:field:7",
        ),),
    )
    old = ResourceHandoffAuthorization(
        authorization_id="auth:old", request_id="request:meter:nerea", provider_actor_id="teo",
        accountable_actor_id="nerea", receiving_actor_id="ema", resource_id="meter:field:7",
        mode=HandoffMode.PICKUP, handoff_location_ref="place:repair-row", valid_from_tick=30,
        valid_until_tick=70, authority_ref="request-event:accepted",
    )
    new = ResourceHandoffAuthorization(
        authorization_id="auth:new", request_id=old.request_id, provider_actor_id=old.provider_actor_id,
        accountable_actor_id=old.accountable_actor_id, receiving_actor_id=old.receiving_actor_id,
        resource_id=old.resource_id, mode=old.mode, handoff_location_ref="place:field-office",
        valid_from_tick=90, valid_until_tick=120, authority_ref="decision:accept",
    )
    handoffs = ResourceHandoffLedger((new, old), ())

    record_direct_observation(
        queue.ledgers["ema"], claim_id="claim:reschedule", subject="auth:old:appointment-update",
        value="RESCHEDULE_REQUEST", semantic_minute=40, confidence=100,
    )
    queue.schedule(
        event_id="delivery:reschedule", message_id="message:reschedule", sender_id="ema", receiver_id="teo",
        source_claim_id="claim:reschedule", new_claim_id="received:reschedule", channel_id="wire",
        created_minute=40,
    )
    if deliver:
        queue.process_due(45)

    notice = ResourceHandoffAppointmentNotice(
        notice_id="notice:reschedule", authorization_id="auth:old", sender_actor_id="ema",
        receiver_actor_id="teo", kind=HandoffAppointmentNoticeKind.RESCHEDULE_REQUEST,
        source_claim_id="claim:reschedule", communication_event_id="delivery:reschedule", created_tick=40,
    )
    proposal = ResourceHandoffRescheduleProposal(
        proposal_id="proposal:later", authorization_id="auth:old", source_notice_id="notice:reschedule",
        proposer_actor_id="ema", responder_actor_id="teo", proposed_location_ref="place:field-office",
        proposed_valid_from_tick=90, proposed_valid_until_tick=120, created_tick=45,
    )
    decision = ResourceHandoffRescheduleDecision(
        decision_id="decision:accept", proposal_id="proposal:later", actor_id="teo",
        kind=HandoffRescheduleDecisionKind.ACCEPT, at_tick=46,
    )
    replacement = ResourceHandoffAuthorizationReplacement(
        replacement_id="replacement:1", proposal_id="proposal:later", decision_id="decision:accept",
        superseded_authorization_id="auth:old", successor_authorization_id="auth:new", at_tick=46,
    )
    return (
        coordinator,
        channels,
        ReservationLedger(),
        requests,
        handoffs,
        ResourceHandoffAttemptLedger(),
        ResourceHandoffAppointmentLedger((notice,)),
        ResourceHandoffRescheduleLedger((proposal,), (decision,), (replacement,)),
    )


def test_v10_round_trip_binds_decision_to_delivered_reschedule_request() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments, reschedules = _fixture(deliver=True)
    checkpoint = build_world_resource_checkpoint(
        coordinator,
        semantic_minute=46,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
        reschedule_ledger=reschedules,
    )

    assert checkpoint["schema"] == WORLD_RESOURCE_CHECKPOINT_SCHEMA
    assert checkpoint["resource_state"]["schema"] == "OUROS_NPC_RESOURCE_CHECKPOINT_V5"
    restored = restore_world_resource_checkpoint(checkpoint, channels=channels)
    assert restored.reschedule_ledger == reschedules
    assert restored.appointment_ledger == appointments
    assert restored.world.coordinator.information_queue.envelope_provenance("delivery:reschedule") is not None


def test_v10_rejects_decision_when_source_request_was_not_delivered() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments, reschedules = _fixture(deliver=False)
    checkpoint = build_world_resource_checkpoint(
        coordinator,
        semantic_minute=46,
        reservation_ledger=reservations,
        request_ledger=requests,
        handoff_ledger=handoffs,
        attempt_ledger=attempts,
        appointment_ledger=appointments,
        reschedule_ledger=reschedules,
    )

    with pytest.raises(ValueError, match="source request was not delivered"):
        restore_world_resource_checkpoint(checkpoint, channels=channels)


def test_v10_requires_appointment_history_when_reschedule_history_is_supplied() -> None:
    coordinator, _, reservations, requests, handoffs, attempts, _, reschedules = _fixture(deliver=True)
    with pytest.raises(ValueError, match="reschedule history requires appointment history"):
        build_world_resource_checkpoint(
            coordinator,
            semantic_minute=46,
            reservation_ledger=reservations,
            request_ledger=requests,
            handoff_ledger=handoffs,
            attempt_ledger=attempts,
            reschedule_ledger=reschedules,
        )


def test_v9_migration_preserves_appointment_history_and_leaves_reschedules_empty() -> None:
    coordinator, channels, reservations, requests, handoffs, attempts, appointments, _ = _fixture(deliver=True)
    checkpoint = build_checkpoint(coordinator, semantic_minute=46)
    checkpoint = {key: value for key, value in checkpoint.items() if key != "sha256"}
    checkpoint["schema"] = LEGACY_WORLD_RESOURCE_APPOINTMENT_CHECKPOINT_SCHEMA
    checkpoint["resource_state"] = snapshot_resource_state_with_appointment_notices(
        reservations, requests, handoffs, attempts, appointments
    )
    checkpoint["sha256"] = _digest(checkpoint)

    restored = restore_world_resource_checkpoint(checkpoint, channels=channels)
    assert restored.appointment_ledger == appointments
    assert restored.reschedule_ledger == ResourceHandoffRescheduleLedger()
