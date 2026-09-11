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
from tools.global_npc_assistance_counterproposal import (
    AssistanceCounterproposalLedger,
    AssistanceCounterproposalRecord,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)
from tools.global_npc_assistance_deferral import AssistanceDeferralLedger, AssistanceDeferralRecord
from tools.global_npc_information_network import CommunicationChannel
from tools.global_npc_replanning import ReplanReason
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_checkpoint import RestoredWorldCheckpoint, build_checkpoint, restore_checkpoint
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


SCHEMA_VERSION = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V3"
LEGACY_SCHEMA_VERSION_V2 = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V2"
LEGACY_SCHEMA_VERSION_V1 = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V1"


@dataclass(frozen=True)
class RestoredAssistanceWorldCheckpoint:
    world: RestoredWorldCheckpoint
    action_ledger: WorldActionIntentLedger
    commitment_ledger: AssistanceCommitmentLedger
    deferral_ledger: AssistanceDeferralLedger
    counterproposal_ledger: AssistanceCounterproposalLedger
    counterproposal_commitment_ledger: AssistanceCounterproposalCommitmentLedger


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


def _scheduled_counterproposal_commitment(
    record: AssistanceCounterproposalCommitmentRecord,
) -> ScheduledCommitment:
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


def _validate_counterproposal(
    *,
    record: AssistanceCounterproposalRecord,
    action_ledger: WorldActionIntentLedger,
    semantic_minute: int,
) -> None:
    request = action_ledger.records.get(record.request_action_id)
    response = action_ledger.records.get(record.response_action_id)
    if request is None or response is None:
        raise ValueError(f"assistance counterproposal references missing action intent: {record.proposal_id}")
    if request.intent_kind != "REQUEST_ASSISTANCE" or request.agent_id != record.requester_id or request.target_ref != record.responder_id:
        raise ValueError(f"assistance counterproposal request binding mismatch: {record.proposal_id}")
    if response.intent_kind != "COUNTERPROPOSE_ASSISTANCE_REQUEST" or response.agent_id != record.responder_id or response.target_ref != record.requester_id:
        raise ValueError(f"assistance counterproposal response binding mismatch: {record.proposal_id}")
    if record.provenance_root != response.action_id:
        raise ValueError(f"assistance counterproposal provenance mismatch: {record.proposal_id}")
    if response.semantic_minute < request.semantic_minute:
        raise ValueError(f"assistance counterproposal predates its request: {record.proposal_id}")
    if response.semantic_minute > semantic_minute:
        raise ValueError(f"assistance counterproposal response comes from the future: {record.proposal_id}")
    if record.proposed_start_minute is not None and record.proposed_start_minute < response.semantic_minute:
        raise ValueError(f"assistance counterproposal proposes a start before its response: {record.proposal_id}")
    if record.proposed_end_minute is not None:
        if record.proposed_start_minute is None or record.proposed_end_minute < record.proposed_start_minute:
            raise ValueError(f"assistance counterproposal has invalid scheduled terms: {record.proposal_id}")
    if record.expires_minute is not None and record.expires_minute < response.semantic_minute:
        raise ValueError(f"assistance counterproposal expiry predates its response: {record.proposal_id}")


def _validate_counterproposal_commitment(
    *,
    record: AssistanceCounterproposalCommitmentRecord,
    action_ledger: WorldActionIntentLedger,
    counterproposal_ledger: AssistanceCounterproposalLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    semantic_minute: int,
) -> None:
    proposal = counterproposal_ledger.records.get(record.proposal_id)
    request = action_ledger.records.get(record.request_action_id)
    response = action_ledger.records.get(record.response_action_id)
    decision = action_ledger.records.get(record.decision_action_id)
    if proposal is None or request is None or response is None or decision is None:
        raise ValueError(f"counterproposal commitment references missing causal state: {record.commitment_id}")
    if proposal.request_action_id != record.request_action_id or proposal.response_action_id != record.response_action_id:
        raise ValueError(f"counterproposal commitment proposal chain mismatch: {record.commitment_id}")
    if proposal.requester_id != record.requester_id or proposal.responder_id != record.responder_id:
        raise ValueError(f"counterproposal commitment actor binding mismatch: {record.commitment_id}")
    if request.intent_kind != "REQUEST_ASSISTANCE" or request.agent_id != record.requester_id or request.target_ref != record.responder_id:
        raise ValueError(f"counterproposal commitment request binding mismatch: {record.commitment_id}")
    if response.intent_kind != "COUNTERPROPOSE_ASSISTANCE_REQUEST" or response.agent_id != record.responder_id or response.target_ref != record.requester_id:
        raise ValueError(f"counterproposal commitment response binding mismatch: {record.commitment_id}")
    if decision.intent_kind != "ACCEPT_ASSISTANCE_COUNTERPROPOSAL" or decision.agent_id != record.requester_id or decision.target_ref != record.responder_id:
        raise ValueError(f"counterproposal commitment acceptance binding mismatch: {record.commitment_id}")
    if decision.source_ref != record.proposal_id:
        raise ValueError(f"counterproposal commitment acceptance names another proposal: {record.commitment_id}")
    if record.provenance_root != decision.action_id:
        raise ValueError(f"counterproposal commitment provenance mismatch: {record.commitment_id}")
    if response.semantic_minute < request.semantic_minute or decision.semantic_minute < response.semantic_minute:
        raise ValueError(f"counterproposal commitment chronology mismatch: {record.commitment_id}")
    if decision.semantic_minute > semantic_minute:
        raise ValueError(f"counterproposal commitment acceptance comes from the future: {record.commitment_id}")
    if proposal.expires_minute is not None and decision.semantic_minute > proposal.expires_minute:
        raise ValueError(f"counterproposal commitment derives from expired proposal: {record.commitment_id}")
    if proposal.proposed_start_minute != record.start_minute or proposal.proposed_end_minute != record.end_minute:
        raise ValueError(f"counterproposal commitment changed accepted time terms: {record.commitment_id}")
    if proposal.location_ref != record.location_ref or proposal.scope_ref != record.scope_ref or proposal.alternative_ref != record.alternative_ref:
        raise ValueError(f"counterproposal commitment changed accepted non-time terms: {record.commitment_id}")

    profile = coordinator.agendas.get(record.responder_id, AgentAgendaProfile())
    expected = _scheduled_counterproposal_commitment(record)
    matching = [row for row in profile.commitments if row.commitment_id == record.commitment_id]
    if not matching:
        raise ValueError(f"counterproposal commitment missing from responder agenda: {record.commitment_id}")
    if matching[0] != expected:
        raise ValueError(f"counterproposal commitment agenda mismatch: {record.commitment_id}")


def _validate_causal_generation(
    *,
    coordinator: GlobalNpcWorldEventCoordinator,
    action_ledger: WorldActionIntentLedger,
    commitment_ledger: AssistanceCommitmentLedger,
    deferral_ledger: AssistanceDeferralLedger,
    counterproposal_ledger: AssistanceCounterproposalLedger,
    counterproposal_commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    semantic_minute: int,
) -> None:
    for action in action_ledger.records.values():
        if action.semantic_minute > semantic_minute:
            raise ValueError(f"world action intent comes from the future: {action.action_id}")
        if action.agent_id not in coordinator.agents:
            raise ValueError(f"world action intent references missing agent: {action.action_id}")

    ordinary_ids = set(commitment_ledger.records)
    negotiated_ids = set(counterproposal_commitment_ledger.records)
    overlap = ordinary_ids & negotiated_ids
    if overlap:
        raise ValueError(f"assistance commitment id belongs to multiple owners: {sorted(overlap)[0]}")

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

    for record in counterproposal_ledger.records.values():
        _validate_counterproposal(record=record, action_ledger=action_ledger, semantic_minute=semantic_minute)

    for record in counterproposal_commitment_ledger.records.values():
        _validate_counterproposal_commitment(
            record=record,
            action_ledger=action_ledger,
            counterproposal_ledger=counterproposal_ledger,
            coordinator=coordinator,
            semantic_minute=semantic_minute,
        )


def build_assistance_world_checkpoint(
    coordinator: GlobalNpcWorldEventCoordinator,
    *,
    semantic_minute: int,
    action_ledger: WorldActionIntentLedger,
    commitment_ledger: AssistanceCommitmentLedger,
    deferral_ledger: AssistanceDeferralLedger | None = None,
    counterproposal_ledger: AssistanceCounterproposalLedger | None = None,
    counterproposal_commitment_ledger: AssistanceCounterproposalCommitmentLedger | None = None,
) -> dict[str, object]:
    """Snapshot world state and assistance causal state as one logical generation."""
    deferral_ledger = deferral_ledger or AssistanceDeferralLedger()
    counterproposal_ledger = counterproposal_ledger or AssistanceCounterproposalLedger()
    counterproposal_commitment_ledger = counterproposal_commitment_ledger or AssistanceCounterproposalCommitmentLedger()
    _validate_causal_generation(
        coordinator=coordinator,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
        counterproposal_ledger=counterproposal_ledger,
        counterproposal_commitment_ledger=counterproposal_commitment_ledger,
        semantic_minute=semantic_minute,
    )
    payload: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "semantic_minute": int(semantic_minute),
        "world_checkpoint": build_checkpoint(coordinator, semantic_minute=semantic_minute),
        "world_action_intents": action_ledger.snapshot(),
        "assistance_commitments": commitment_ledger.snapshot(),
        "assistance_deferrals": deferral_ledger.snapshot(),
        "assistance_counterproposals": counterproposal_ledger.snapshot(),
        "assistance_counterproposal_commitments": counterproposal_commitment_ledger.snapshot(),
    }
    return payload | {"sha256": _digest(payload)}


def _restore_commitment_into_agenda(
    *,
    world: RestoredWorldCheckpoint,
    responder_id: str,
    expected: ScheduledCommitment,
    conflict_label: str,
) -> None:
    profile = world.coordinator.agendas.get(responder_id, AgentAgendaProfile())
    same_id = [row for row in profile.commitments if row.commitment_id == expected.commitment_id]
    if same_id and same_id[0] != expected:
        raise ValueError(f"restored agenda conflicts with {conflict_label}: {expected.commitment_id}")
    if not same_id:
        world.coordinator.agendas[responder_id] = AgentAgendaProfile(
            goals=profile.goals,
            needs=profile.needs,
            commitments=profile.commitments + (expected,),
            situational_intents=profile.situational_intents,
            active_intent_id=profile.active_intent_id,
            continuity_bonus=profile.continuity_bonus,
        )


def restore_assistance_world_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels: Mapping[str, CommunicationChannel],
    agendas: Mapping[str, AgentAgendaProfile] | None = None,
) -> RestoredAssistanceWorldCheckpoint:
    schema_version = snapshot.get("schema_version")
    supported = {SCHEMA_VERSION, LEGACY_SCHEMA_VERSION_V2, LEGACY_SCHEMA_VERSION_V1}
    if schema_version not in supported:
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
    counterproposal_snapshot = payload.get("assistance_counterproposals")
    counterproposal_commitment_snapshot = payload.get("assistance_counterproposal_commitments")
    if not isinstance(world_snapshot, Mapping):
        raise ValueError("world_checkpoint must be a mapping")
    if not isinstance(action_snapshot, Mapping):
        raise ValueError("world_action_intents must be a mapping")
    if not isinstance(commitment_snapshot, Mapping):
        raise ValueError("assistance_commitments must be a mapping")
    if schema_version in {SCHEMA_VERSION, LEGACY_SCHEMA_VERSION_V2} and not isinstance(deferral_snapshot, Mapping):
        raise ValueError("assistance_deferrals must be a mapping")
    if schema_version == SCHEMA_VERSION and not isinstance(counterproposal_snapshot, Mapping):
        raise ValueError("assistance_counterproposals must be a mapping")
    if schema_version == SCHEMA_VERSION and not isinstance(counterproposal_commitment_snapshot, Mapping):
        raise ValueError("assistance_counterproposal_commitments must be a mapping")

    action_ledger = WorldActionIntentLedger.from_snapshot(action_snapshot)
    commitment_ledger = AssistanceCommitmentLedger.from_snapshot(commitment_snapshot)
    deferral_ledger = (
        AssistanceDeferralLedger.from_snapshot(deferral_snapshot)
        if isinstance(deferral_snapshot, Mapping)
        else AssistanceDeferralLedger()
    )
    counterproposal_ledger = (
        AssistanceCounterproposalLedger.from_snapshot(counterproposal_snapshot)
        if isinstance(counterproposal_snapshot, Mapping)
        else AssistanceCounterproposalLedger()
    )
    counterproposal_commitment_ledger = (
        AssistanceCounterproposalCommitmentLedger.from_snapshot(counterproposal_commitment_snapshot)
        if isinstance(counterproposal_commitment_snapshot, Mapping)
        else AssistanceCounterproposalCommitmentLedger()
    )
    world = restore_checkpoint(world_snapshot, channels=channels, agendas=agendas)

    for record in commitment_ledger.records.values():
        _restore_commitment_into_agenda(
            world=world,
            responder_id=record.responder_id,
            expected=_scheduled_commitment(record),
            conflict_label="assistance commitment",
        )
    for record in counterproposal_commitment_ledger.records.values():
        _restore_commitment_into_agenda(
            world=world,
            responder_id=record.responder_id,
            expected=_scheduled_counterproposal_commitment(record),
            conflict_label="counterproposal commitment",
        )

    checkpoint_minute = int(payload["semantic_minute"])
    if world.semantic_minute != checkpoint_minute:
        raise ValueError("assistance checkpoint generation time does not match world checkpoint")
    _validate_causal_generation(
        coordinator=world.coordinator,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
        counterproposal_ledger=counterproposal_ledger,
        counterproposal_commitment_ledger=counterproposal_commitment_ledger,
        semantic_minute=checkpoint_minute,
    )
    return RestoredAssistanceWorldCheckpoint(
        world=world,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
        counterproposal_ledger=counterproposal_ledger,
        counterproposal_commitment_ledger=counterproposal_commitment_ledger,
    )
