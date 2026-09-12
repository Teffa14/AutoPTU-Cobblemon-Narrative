from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

from tools.global_npc_assistance_commitment_disposition import (
    AssistanceCommitmentDispositionLedger,
)
from tools.global_npc_assistance_commitment_start import (
    AssistanceCommitmentStartLedger,
)
from tools.global_npc_assistance_world_checkpoint import (
    RestoredAssistanceWorldCheckpoint,
    build_assistance_world_checkpoint,
    restore_assistance_world_checkpoint,
)
from tools.global_npc_information_network import CommunicationChannel
from tools.global_npc_replanning import ReplanReason
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_assistance_acceptance_commitment import AssistanceCommitmentLedger
from tools.global_npc_assistance_deferral import AssistanceDeferralLedger
from tools.global_npc_assistance_counterproposal import AssistanceCounterproposalLedger
from tools.global_npc_assistance_counterproposal_commitment import AssistanceCounterproposalCommitmentLedger
from tools.global_npc_assistance_commitment_viability import AssistanceCommitmentViabilityLedger

SCHEMA_VERSION = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V5"
LEGACY_SCHEMA_VERSION_V4 = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V4"


@dataclass(frozen=True)
class RestoredAssistanceWorldCheckpointV5:
    base: RestoredAssistanceWorldCheckpoint
    commitment_start_ledger: AssistanceCommitmentStartLedger
    commitment_disposition_ledger: AssistanceCommitmentDispositionLedger


def _digest(payload: Mapping[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _pending_trigger(coordinator: GlobalNpcWorldEventCoordinator, trigger_id: str):
    rows = [entry[3] for entry in coordinator.replan_queue.pending if entry[3].trigger_id == trigger_id]
    if len(rows) > 1:
        raise ValueError(f"duplicate assistance start trigger in replan queue: {trigger_id}")
    return rows[0] if rows else None


def _validate_start_and_disposition(
    *,
    base: RestoredAssistanceWorldCheckpoint,
    start_ledger: AssistanceCommitmentStartLedger,
    disposition_ledger: AssistanceCommitmentDispositionLedger,
    semantic_minute: int,
) -> None:
    coordinator = base.world.coordinator
    commitments = base.counterproposal_commitment_ledger
    viability = base.commitment_viability_ledger

    for watch in start_ledger.watches.values():
        commitment = commitments.records.get(watch.commitment_id)
        if commitment is None:
            raise ValueError(f"assistance start watch references missing negotiated commitment: {watch.watch_id}")
        if watch.proposal_id != commitment.proposal_id:
            raise ValueError(f"assistance start watch proposal binding mismatch: {watch.watch_id}")
        if watch.requester_id != commitment.requester_id or watch.responder_id != commitment.responder_id:
            raise ValueError(f"assistance start watch actor binding mismatch: {watch.watch_id}")
        if watch.start_minute != commitment.start_minute:
            raise ValueError(f"assistance start watch changed accepted start minute: {watch.watch_id}")
        if watch.armed_minute >= watch.start_minute or watch.armed_minute > semantic_minute:
            raise ValueError(f"assistance start watch chronology mismatch: {watch.watch_id}")
        expected_trigger_id = f"replan:assistance-start:{watch.watch_id}"
        if watch.trigger_id != expected_trigger_id:
            raise ValueError(f"assistance start watch trigger identity mismatch: {watch.watch_id}")
        if watch.trigger_id not in coordinator.replan_queue.known_trigger_ids:
            raise ValueError(f"assistance start watch trigger missing from replan queue: {watch.watch_id}")
        pending = _pending_trigger(coordinator, watch.trigger_id)
        completed = watch.trigger_id in coordinator.replan_queue.completed_trigger_ids
        if pending is None and not completed:
            raise ValueError(f"assistance start watch trigger has no pending or completed state: {watch.watch_id}")
        if pending is not None:
            if pending.agent_id != commitment.responder_id:
                raise ValueError(f"assistance start watch trigger agent mismatch: {watch.watch_id}")
            if pending.reason != ReplanReason.SCHEDULE_DUE:
                raise ValueError(f"assistance start watch trigger reason mismatch: {watch.watch_id}")
            if pending.due_minute != commitment.start_minute:
                raise ValueError(f"assistance start watch trigger time mismatch: {watch.watch_id}")
            if pending.source_ref != watch.watch_id:
                raise ValueError(f"assistance start watch trigger provenance mismatch: {watch.watch_id}")

    for assessment in start_ledger.assessments.values():
        watch = start_ledger.watches.get(assessment.watch_id)
        commitment = commitments.records.get(assessment.commitment_id)
        observation = viability.records.get(assessment.viability_observation_id)
        if watch is None or commitment is None or observation is None:
            raise ValueError(f"assistance start assessment references missing causal state: {assessment.assessment_id}")
        if watch.commitment_id != assessment.commitment_id or watch.proposal_id != assessment.proposal_id:
            raise ValueError(f"assistance start assessment watch binding mismatch: {assessment.assessment_id}")
        if assessment.proposal_id != commitment.proposal_id:
            raise ValueError(f"assistance start assessment proposal binding mismatch: {assessment.assessment_id}")
        if assessment.requester_id != commitment.requester_id or assessment.responder_id != commitment.responder_id:
            raise ValueError(f"assistance start assessment actor binding mismatch: {assessment.assessment_id}")
        if assessment.semantic_minute != commitment.start_minute or assessment.semantic_minute > semantic_minute:
            raise ValueError(f"assistance start assessment chronology mismatch: {assessment.assessment_id}")
        if observation.commitment_id != commitment.commitment_id or observation.proposal_id != commitment.proposal_id:
            raise ValueError(f"assistance start assessment viability binding mismatch: {assessment.assessment_id}")
        expected = (
            observation.constraint_kind,
            observation.constraint_ref,
            observation.evidence_ref,
            observation.provenance_root,
        )
        actual = (
            assessment.constraint_kind,
            assessment.constraint_ref,
            assessment.evidence_ref,
            assessment.provenance_root,
        )
        if actual != expected:
            raise ValueError(f"assistance start assessment changed viability evidence: {assessment.assessment_id}")

    for record in disposition_ledger.records.values():
        commitment = commitments.records.get(record.commitment_id)
        assessment = start_ledger.assessments.get(record.assessment_id)
        if commitment is None or assessment is None:
            raise ValueError(f"assistance disposition references missing causal state: {record.disposition_id}")
        if record.proposal_id != commitment.proposal_id or assessment.proposal_id != commitment.proposal_id:
            raise ValueError(f"assistance disposition proposal binding mismatch: {record.disposition_id}")
        if assessment.commitment_id != record.commitment_id:
            raise ValueError(f"assistance disposition assessment binding mismatch: {record.disposition_id}")
        if record.requester_id != commitment.requester_id or record.responder_id != commitment.responder_id:
            raise ValueError(f"assistance disposition actor binding mismatch: {record.disposition_id}")
        if record.actor_id != commitment.responder_id:
            raise ValueError(f"assistance disposition actor does not own commitment: {record.disposition_id}")
        if record.semantic_minute < assessment.semantic_minute or record.semantic_minute > commitment.end_minute:
            raise ValueError(f"assistance disposition chronology mismatch: {record.disposition_id}")
        if record.semantic_minute > semantic_minute:
            raise ValueError(f"assistance disposition comes from the future: {record.disposition_id}")


def build_assistance_world_checkpoint_v5(
    coordinator: GlobalNpcWorldEventCoordinator,
    *,
    semantic_minute: int,
    action_ledger: WorldActionIntentLedger,
    commitment_ledger: AssistanceCommitmentLedger,
    deferral_ledger: AssistanceDeferralLedger | None = None,
    counterproposal_ledger: AssistanceCounterproposalLedger | None = None,
    counterproposal_commitment_ledger: AssistanceCounterproposalCommitmentLedger | None = None,
    commitment_viability_ledger: AssistanceCommitmentViabilityLedger | None = None,
    commitment_start_ledger: AssistanceCommitmentStartLedger | None = None,
    commitment_disposition_ledger: AssistanceCommitmentDispositionLedger | None = None,
) -> dict[str, object]:
    """Atomically snapshot V4 assistance state plus adverse-start fact and responder choice."""
    start_ledger = commitment_start_ledger or AssistanceCommitmentStartLedger()
    disposition_ledger = commitment_disposition_ledger or AssistanceCommitmentDispositionLedger()
    base_checkpoint = build_assistance_world_checkpoint(
        coordinator,
        semantic_minute=semantic_minute,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
        counterproposal_ledger=counterproposal_ledger,
        counterproposal_commitment_ledger=counterproposal_commitment_ledger,
        commitment_viability_ledger=commitment_viability_ledger,
    )
    base = restore_assistance_world_checkpoint(
        base_checkpoint,
        channels=coordinator.information_queue.channels,
    )
    _validate_start_and_disposition(
        base=base,
        start_ledger=start_ledger,
        disposition_ledger=disposition_ledger,
        semantic_minute=semantic_minute,
    )
    payload: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "semantic_minute": int(semantic_minute),
        "base_assistance_checkpoint": base_checkpoint,
        "assistance_commitment_start": start_ledger.snapshot(),
        "assistance_commitment_disposition": disposition_ledger.snapshot(),
    }
    return payload | {"sha256": _digest(payload)}


def restore_assistance_world_checkpoint_v5(
    snapshot: Mapping[str, object],
    *,
    channels: Mapping[str, CommunicationChannel],
    agendas: Mapping[str, AgentAgendaProfile] | None = None,
) -> RestoredAssistanceWorldCheckpointV5:
    if snapshot.get("schema_version") == LEGACY_SCHEMA_VERSION_V4:
        base = restore_assistance_world_checkpoint(snapshot, channels=channels, agendas=agendas)
        return RestoredAssistanceWorldCheckpointV5(
            base=base,
            commitment_start_ledger=AssistanceCommitmentStartLedger(),
            commitment_disposition_ledger=AssistanceCommitmentDispositionLedger(),
        )
    if snapshot.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unsupported assistance world checkpoint v5 schema")
    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("assistance world checkpoint v5 sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest(payload) != digest:
        raise ValueError("assistance world checkpoint v5 digest mismatch")

    base_snapshot = payload.get("base_assistance_checkpoint")
    start_snapshot = payload.get("assistance_commitment_start")
    disposition_snapshot = payload.get("assistance_commitment_disposition")
    if not isinstance(base_snapshot, Mapping) or not isinstance(start_snapshot, Mapping) or not isinstance(disposition_snapshot, Mapping):
        raise ValueError("assistance world checkpoint v5 components must be mappings")
    base = restore_assistance_world_checkpoint(base_snapshot, channels=channels, agendas=agendas)
    checkpoint_minute = int(payload["semantic_minute"])
    if base.world.semantic_minute != checkpoint_minute:
        raise ValueError("assistance world checkpoint v5 generation time mismatch")
    start_ledger = AssistanceCommitmentStartLedger.from_snapshot(start_snapshot)
    disposition_ledger = AssistanceCommitmentDispositionLedger.from_snapshot(disposition_snapshot)
    _validate_start_and_disposition(
        base=base,
        start_ledger=start_ledger,
        disposition_ledger=disposition_ledger,
        semantic_minute=checkpoint_minute,
    )
    return RestoredAssistanceWorldCheckpointV5(
        base=base,
        commitment_start_ledger=start_ledger,
        commitment_disposition_ledger=disposition_ledger,
    )
