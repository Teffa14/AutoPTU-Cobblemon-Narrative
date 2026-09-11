from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_ai import ScheduledCommitment
from tools.global_npc_assistance_acceptance_commitment import (
    AssistanceCommitmentLedger,
    AssistanceCommitmentRecord,
)
from tools.global_npc_assistance_deferral import AssistanceDeferralLedger, AssistanceDeferralRecord
from tools.global_npc_information_network import CommunicationChannel
from tools.global_npc_replanning import ReplanReason
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_checkpoint import RestoredWorldCheckpoint, build_checkpoint, restore_checkpoint
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


SCHEMA_VERSION = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V2"
LEGACY_SCHEMA_VERSION = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V1"


@dataclass(frozen=True)
class RestoredAssistanceWorldCheckpoint:
    world: RestoredWorldCheckpoint
    action_ledger: WorldActionIntentLedger
    commitment_ledger: AssistanceCommitmentLedger
    deferral_ledger: AssistanceDeferralLedger


def _digest(payload: Mapping[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _scheduled_commitment(record: AssistanceCommitmentRecord) -> ScheduledCommitment:
    return ScheduledCommitment(
        commitment_id=record.commitment_id,
        intent_kind=record.intent_kind,
        start_minute=record.start_minute,
        end_minute=record.end_minute,
        priority=record.priority,
        hard=record.hard,
        grace_minutes=record.grace_minutes,
        required_knowledge=frozenset(record.required_knowledge),
        required_permissions=frozenset(record.required_permissions),
        target_ref=record.requester_id,
        requires_local_projection=record.requires_local_projection,
        requires_structured_mechanics=record.requires_structured_mechanics,
    )


def _pending_deferral_trigger(coordinator: GlobalNpcWorldEventCoordinator, record: AssistanceDeferralRecord):
    matches = [entry[3] for entry in coordinator.replan_queue.pending if entry[3].trigger_id == record.trigger_id]
    if len(matches) > 1:
        raise ValueError(f"duplicate assistance deferral trigger in replan queue: {record.deferral_id}")
    return matches[0] if matches else None


def _validate_causal_generation(
    *,
    coordinator: GlobalNpcWorldEventCoordinator,
    action_ledger: WorldActionIntentLedger,
    commitment_ledger: AssistanceCommitmentLedger,
    deferral_ledger: AssistanceDeferralLedger,
    semantic_minute: int,
) -> None:
    for action in action_ledger.records.values():
        if action.semantic_minute > semantic_minute:
            raise ValueError(f"world action intent comes from the future: {action.action_id}")
        if action.agent_id not in coordinator.agents:
            raise ValueError(f"world action intent references missing agent: {action.action_id}")

    for record in commitment_ledger.records.values():
        request = action_ledger.records.get(record.request_action_id)
        response = action_ledger.records.get(record.response_action_id)
        if request is None or response is None:
            raise ValueError(f"assistance commitment references missing action intent: {record.commitment_id}")
        if request.agent_id != record.requester_id or request.target_ref != record.responder_id:
            raise ValueError(f"assistance commitment request binding mismatch: {record.commitment_id}")
        if response.agent_id != record.responder_id or response.target_ref != record.requester_id:
            raise ValueError(f"assistance commitment response binding mismatch: {record.commitment_id}")
        if record.provenance_root != response.action_id:
            raise ValueError(f"assistance commitment provenance mismatch: {record.commitment_id}")
        if response.semantic_minute > semantic_minute:
            raise ValueError(f"assistance commitment response comes from the future: {record.commitment_id}")

        profile = coordinator.agendas.get(record.responder_id, AgentAgendaProfile())
        expected = _scheduled_commitment(record)
        matching = [row for row in profile.commitments if row.commitment_id == record.commitment_id]
        if not matching:
            raise ValueError(f"assistance commitment missing from responder agenda: {record.commitment_id}")
        if matching[0] != expected:
            raise ValueError(f"assistance commitment agenda mismatch: {record.commitment_id}")

    for record in deferral_ledger.records.values():
        request = action_ledger.records.get(record.request_action_id)
        response = action_ledger.records.get(record.response_action_id)
        if request is None or response is None:
            raise ValueError(f"assistance deferral references missing action intent: {record.deferral_id}")
        if request.intent_kind != "REQUEST_ASSISTANCE" or request.agent_id != record.requester_id or request.target_ref != record.responder_id:
            raise ValueError(f"assistance deferral request binding mismatch: {record.deferral_id}")
        if response.intent_kind != "DEFER_ASSISTANCE_REQUEST" or response.agent_id != record.responder_id or response.target_ref != record.requester_id:
            raise ValueError(f"assistance deferral response binding mismatch: {record.deferral_id}")
        if record.provenance_root != response.action_id:
            raise ValueError(f"assistance deferral provenance mismatch: {record.deferral_id}")
        if response.semantic_minute > semantic_minute:
            raise ValueError(f"assistance deferral response comes from the future: {record.deferral_id}")
        if record.reconsider_minute <= response.semantic_minute:
            raise ValueError(f"assistance deferral reconsideration does not follow response: {record.deferral_id}")
        if record.expires_minute is not None and record.expires_minute < record.reconsider_minute:
            raise ValueError(f"assistance deferral expiry precedes reconsideration: {record.deferral_id}")
        if record.trigger_id != f"replan:assistance-deferral:{record.deferral_id}":
            raise ValueError(f"assistance deferral trigger identity mismatch: {record.deferral_id}")
        if record.trigger_id not in coordinator.replan_queue.known_trigger_ids:
            raise ValueError(f"assistance deferral trigger missing from replan queue: {record.deferral_id}")

        pending = _pending_deferral_trigger(coordinator, record)
        completed = record.trigger_id in coordinator.replan_queue.completed_trigger_ids
        if pending is None and not completed:
            raise ValueError(f"assistance deferral trigger has no pending or completed state: {record.deferral_id}")
        if pending is not None:
            if pending.agent_id != record.responder_id:
                raise ValueError(f"assistance deferral trigger agent mismatch: {record.deferral_id}")
            if pending.reason != ReplanReason.SCHEDULE_DUE:
                raise ValueError(f"assistance deferral trigger reason mismatch: {record.deferral_id}")
            if pending.due_minute != record.reconsider_minute:
                raise ValueError(f"assistance deferral trigger time mismatch: {record.deferral_id}")
            if pending.source_ref != record.response_action_id:
                raise ValueError(f"assistance deferral trigger provenance mismatch: {record.deferral_id}")
            if pending.priority != record.priority:
                raise ValueError(f"assistance deferral trigger priority mismatch: {record.deferral_id}")


def build_assistance_world_checkpoint(
    coordinator: GlobalNpcWorldEventCoordinator,
    *,
    semantic_minute: int,
    action_ledger: WorldActionIntentLedger,
    commitment_ledger: AssistanceCommitmentLedger,
    deferral_ledger: AssistanceDeferralLedger | None = None,
) -> dict[str, object]:
    """Snapshot world state and assistance causal state as one logical generation."""
    deferral_ledger = deferral_ledger or AssistanceDeferralLedger()
    _validate_causal_generation(
        coordinator=coordinator,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
        semantic_minute=semantic_minute,
    )
    payload: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "semantic_minute": int(semantic_minute),
        "world_checkpoint": build_checkpoint(coordinator, semantic_minute=semantic_minute),
        "world_action_intents": action_ledger.snapshot(),
        "assistance_commitments": commitment_ledger.snapshot(),
        "assistance_deferrals": deferral_ledger.snapshot(),
    }
    return payload | {"sha256": _digest(payload)}


def restore_assistance_world_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels: Mapping[str, CommunicationChannel],
    agendas: Mapping[str, AgentAgendaProfile] | None = None,
) -> RestoredAssistanceWorldCheckpoint:
    schema_version = snapshot.get("schema_version")
    if schema_version not in {SCHEMA_VERSION, LEGACY_SCHEMA_VERSION}:
        raise ValueError("unsupported assistance world checkpoint schema")
    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("assistance world checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest(payload) != digest:
        raise ValueError("assistance world checkpoint digest mismatch")

    world_snapshot = payload.get("world_checkpoint")
    action_snapshot = payload.get("world_action_intents")
    commitment_snapshot = payload.get("assistance_commitments")
    deferral_snapshot = payload.get("assistance_deferrals")
    if not isinstance(world_snapshot, Mapping):
        raise ValueError("world_checkpoint must be a mapping")
    if not isinstance(action_snapshot, Mapping):
        raise ValueError("world_action_intents must be a mapping")
    if not isinstance(commitment_snapshot, Mapping):
        raise ValueError("assistance_commitments must be a mapping")
    if schema_version == SCHEMA_VERSION and not isinstance(deferral_snapshot, Mapping):
        raise ValueError("assistance_deferrals must be a mapping")

    action_ledger = WorldActionIntentLedger.from_snapshot(action_snapshot)
    commitment_ledger = AssistanceCommitmentLedger.from_snapshot(commitment_snapshot)
    deferral_ledger = (
        AssistanceDeferralLedger.from_snapshot(deferral_snapshot)
        if isinstance(deferral_snapshot, Mapping)
        else AssistanceDeferralLedger()
    )
    world = restore_checkpoint(world_snapshot, channels=channels, agendas=agendas)

    for record in commitment_ledger.records.values():
        expected = _scheduled_commitment(record)
        profile = world.coordinator.agendas.get(record.responder_id, AgentAgendaProfile())
        same_id = [row for row in profile.commitments if row.commitment_id == record.commitment_id]
        if same_id and same_id[0] != expected:
            raise ValueError(f"restored agenda conflicts with assistance commitment: {record.commitment_id}")
        if not same_id:
            world.coordinator.agendas[record.responder_id] = AgentAgendaProfile(
                goals=profile.goals,
                needs=profile.needs,
                commitments=profile.commitments + (expected,),
                situational_intents=profile.situational_intents,
                active_intent_id=profile.active_intent_id,
                continuity_bonus=profile.continuity_bonus,
            )

    checkpoint_minute = int(payload["semantic_minute"])
    if world.semantic_minute != checkpoint_minute:
        raise ValueError("assistance checkpoint generation time does not match world checkpoint")
    _validate_causal_generation(
        coordinator=world.coordinator,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
        semantic_minute=checkpoint_minute,
    )
    return RestoredAssistanceWorldCheckpoint(
        world=world,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
    )
