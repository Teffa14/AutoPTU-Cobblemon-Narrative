from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Mapping

from tools.global_npc_ai import ScheduledCommitment
from tools.global_npc_assistance_acceptance_commitment import AssistanceCommitmentLedger
from tools.global_npc_assistance_commitment_disposition import (
    AssistanceCommitmentDispositionLedger,
    CommitmentStartDisposition,
)
from tools.global_npc_assistance_commitment_start import AssistanceCommitmentStartLedger
from tools.global_npc_assistance_commitment_viability import AssistanceCommitmentViabilityLedger
from tools.global_npc_assistance_counterproposal import AssistanceCounterproposalLedger
from tools.global_npc_assistance_counterproposal_commitment import AssistanceCounterproposalCommitmentLedger
from tools.global_npc_assistance_deferral import AssistanceDeferralLedger
from tools.global_npc_assistance_renegotiation_decision import (
    AssistanceRenegotiationDecision,
    AssistanceRenegotiationDecisionLedger,
)
from tools.global_npc_assistance_renegotiation_proposal import AssistanceRenegotiationProposalLedger
from tools.global_npc_assistance_renegotiation_proposal_decision import (
    AssistanceRenegotiationProposalDecisionLedger,
    AssistanceRenegotiationProposalOutcome,
)
from tools.global_npc_assistance_renegotiation_replacement_commitment import (
    AssistanceRenegotiationReplacementCommitmentLedger,
)
from tools.global_npc_assistance_world_checkpoint import (
    _restore_commitment_into_agenda,
    _scheduled_commitment,
    _scheduled_counterproposal_commitment,
    _validate_causal_generation,
)
from tools.global_npc_assistance_world_checkpoint_v5 import (
    _validate_start_and_disposition,
    restore_assistance_world_checkpoint_v5,
)
from tools.global_npc_information_network import CommunicationChannel, DeliveryStatus
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_checkpoint import RestoredWorldCheckpoint, build_checkpoint, restore_checkpoint
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator

SCHEMA_VERSION = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V6"
LEGACY_SCHEMA_VERSION_V5 = "OUROS_ASSISTANCE_WORLD_CHECKPOINT_V5"


@dataclass(frozen=True)
class RestoredAssistanceWorldCheckpointV6:
    world: RestoredWorldCheckpoint
    action_ledger: WorldActionIntentLedger
    commitment_ledger: AssistanceCommitmentLedger
    deferral_ledger: AssistanceDeferralLedger
    counterproposal_ledger: AssistanceCounterproposalLedger
    counterproposal_commitment_ledger: AssistanceCounterproposalCommitmentLedger
    commitment_viability_ledger: AssistanceCommitmentViabilityLedger
    commitment_start_ledger: AssistanceCommitmentStartLedger
    commitment_disposition_ledger: AssistanceCommitmentDispositionLedger
    renegotiation_decision_ledger: AssistanceRenegotiationDecisionLedger
    renegotiation_proposal_ledger: AssistanceRenegotiationProposalLedger
    renegotiation_proposal_decision_ledger: AssistanceRenegotiationProposalDecisionLedger
    replacement_commitment_ledger: AssistanceRenegotiationReplacementCommitmentLedger


def _digest(payload: Mapping[str, object]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _replacement_schedule(record) -> ScheduledCommitment:
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


def _shadow_with_superseded_commitments(
    coordinator: GlobalNpcWorldEventCoordinator,
    counterproposal_commitments: AssistanceCounterproposalCommitmentLedger,
    replacements: AssistanceRenegotiationReplacementCommitmentLedger,
) -> GlobalNpcWorldEventCoordinator:
    """Return a validation-only shallow copy with historical commitments reinserted.

    Older assistance validators correctly require every negotiated commitment to
    be represented in the agenda. V6 preserves that invariant for unsuperseded
    commitments while allowing a replacement to own future execution. The
    historical commitment is reinserted only into this private validation view;
    it is never returned as live executable schedule state.
    """
    shadow = copy.copy(coordinator)
    shadow.agendas = dict(coordinator.agendas)
    superseded_ids = {row.supersedes_commitment_id for row in replacements.records.values()}
    for commitment_id in sorted(superseded_ids):
        record = counterproposal_commitments.records.get(commitment_id)
        if record is None:
            continue
        profile = shadow.agendas.get(record.responder_id, AgentAgendaProfile())
        if any(row.commitment_id == commitment_id for row in profile.commitments):
            continue
        shadow.agendas[record.responder_id] = AgentAgendaProfile(
            goals=profile.goals,
            needs=profile.needs,
            commitments=profile.commitments + (_scheduled_counterproposal_commitment(record),),
            situational_intents=profile.situational_intents,
            active_intent_id=profile.active_intent_id,
            continuity_bonus=profile.continuity_bonus,
        )
    return shadow


def _require_delivered_event(queue, event_id: str, *, sender_id: str, receiver_id: str, label: str) -> None:
    envelope = queue.envelope_provenance(event_id)
    if envelope is None:
        raise ValueError(f"{label} references missing information event: {event_id}")
    if queue.statuses.get(event_id) != DeliveryStatus.DELIVERED:
        raise ValueError(f"{label} requires delivered information event: {event_id}")
    if envelope.sender_id != sender_id or envelope.receiver_id != receiver_id:
        raise ValueError(f"{label} information-event actor binding mismatch: {event_id}")


def _validate_late_assistance_chain(
    *,
    coordinator: GlobalNpcWorldEventCoordinator,
    counterproposal_commitments: AssistanceCounterproposalCommitmentLedger,
    disposition_ledger: AssistanceCommitmentDispositionLedger,
    renegotiation_decisions: AssistanceRenegotiationDecisionLedger,
    renegotiation_proposals: AssistanceRenegotiationProposalLedger,
    proposal_decisions: AssistanceRenegotiationProposalDecisionLedger,
    replacements: AssistanceRenegotiationReplacementCommitmentLedger,
    semantic_minute: int,
) -> None:
    queue = coordinator.information_queue

    for decision in renegotiation_decisions.records.values():
        commitment = counterproposal_commitments.records.get(decision.commitment_id)
        disposition = disposition_ledger.records.get(decision.disposition_id)
        if commitment is None or disposition is None:
            raise ValueError(f"renegotiation decision references missing causal state: {decision.decision_id}")
        if disposition.disposition != CommitmentStartDisposition.REQUEST_RENEGOTIATION.value:
            raise ValueError(f"renegotiation decision lacks REQUEST_RENEGOTIATION disposition: {decision.decision_id}")
        if decision.proposal_id != commitment.proposal_id or disposition.proposal_id != commitment.proposal_id:
            raise ValueError(f"renegotiation decision proposal lineage mismatch: {decision.decision_id}")
        if disposition.commitment_id != commitment.commitment_id:
            raise ValueError(f"renegotiation decision commitment lineage mismatch: {decision.decision_id}")
        if decision.requester_id != commitment.requester_id or decision.responder_id != commitment.responder_id:
            raise ValueError(f"renegotiation decision actor binding mismatch: {decision.decision_id}")
        if decision.semantic_minute < disposition.semantic_minute or decision.semantic_minute > semantic_minute:
            raise ValueError(f"renegotiation decision chronology mismatch: {decision.decision_id}")
        _require_delivered_event(
            queue,
            decision.request_event_id,
            sender_id=commitment.responder_id,
            receiver_id=commitment.requester_id,
            label="renegotiation decision",
        )

    for proposal in renegotiation_proposals.records.values():
        commitment = counterproposal_commitments.records.get(proposal.supersedes_commitment_id)
        decision = renegotiation_decisions.records.get(proposal.decision_id)
        if commitment is None or decision is None:
            raise ValueError(f"renegotiation proposal references missing causal state: {proposal.proposal_id}")
        if decision.decision != AssistanceRenegotiationDecision.ACCEPT_REOPENING.value:
            raise ValueError(f"renegotiation proposal lacks accepted reopening: {proposal.proposal_id}")
        if proposal.supersedes_proposal_id != commitment.proposal_id or decision.proposal_id != commitment.proposal_id:
            raise ValueError(f"renegotiation proposal old-proposal lineage mismatch: {proposal.proposal_id}")
        if decision.commitment_id != commitment.commitment_id:
            raise ValueError(f"renegotiation proposal old-commitment lineage mismatch: {proposal.proposal_id}")
        if proposal.requester_id != commitment.requester_id or proposal.responder_id != commitment.responder_id:
            raise ValueError(f"renegotiation proposal actor binding mismatch: {proposal.proposal_id}")
        if proposal.decision_provenance_root != decision.provenance_root:
            raise ValueError(f"renegotiation proposal decision provenance mismatch: {proposal.proposal_id}")
        if proposal.semantic_minute < decision.semantic_minute or proposal.semantic_minute > semantic_minute:
            raise ValueError(f"renegotiation proposal chronology mismatch: {proposal.proposal_id}")
        _require_delivered_event(
            queue,
            proposal.decision_reply_event_id,
            sender_id=commitment.requester_id,
            receiver_id=commitment.responder_id,
            label="renegotiation proposal",
        )

    for decision in proposal_decisions.records.values():
        proposal = renegotiation_proposals.records.get(decision.proposal_id)
        if proposal is None:
            raise ValueError(f"replacement-offer decision references missing proposal: {decision.decision_id}")
        if decision.supersedes_commitment_id != proposal.supersedes_commitment_id:
            raise ValueError(f"replacement-offer decision old-commitment lineage mismatch: {decision.decision_id}")
        if decision.supersedes_proposal_id != proposal.supersedes_proposal_id:
            raise ValueError(f"replacement-offer decision old-proposal lineage mismatch: {decision.decision_id}")
        if decision.requester_id != proposal.requester_id or decision.responder_id != proposal.responder_id:
            raise ValueError(f"replacement-offer decision actor binding mismatch: {decision.decision_id}")
        if decision.proposal_provenance_root != proposal.provenance_root:
            raise ValueError(f"replacement-offer decision proposal provenance mismatch: {decision.decision_id}")
        if decision.semantic_minute < proposal.semantic_minute or decision.semantic_minute > semantic_minute:
            raise ValueError(f"replacement-offer decision chronology mismatch: {decision.decision_id}")
        expired = proposal.expires_minute is not None and decision.semantic_minute > proposal.expires_minute
        if decision.outcome == AssistanceRenegotiationProposalOutcome.EXPIRED.value:
            if proposal.expires_minute is None or not expired:
                raise ValueError(f"replacement-offer expiry chronology mismatch: {decision.decision_id}")
        elif expired:
            raise ValueError(f"replacement-offer decision accepted or rejected after expiry: {decision.decision_id}")
        _require_delivered_event(
            queue,
            decision.proposal_event_id,
            sender_id=proposal.responder_id,
            receiver_id=proposal.requester_id,
            label="replacement-offer decision",
        )

    superseded_seen: set[str] = set()
    for record in replacements.records.values():
        old = counterproposal_commitments.records.get(record.supersedes_commitment_id)
        proposal = renegotiation_proposals.records.get(record.replacement_proposal_id)
        decision = proposal_decisions.records.get(record.proposal_decision_id)
        if old is None or proposal is None or decision is None:
            raise ValueError(f"replacement commitment references missing causal state: {record.commitment_id}")
        if record.supersedes_commitment_id in superseded_seen:
            raise ValueError(f"multiple replacement commitments supersede one obligation: {record.supersedes_commitment_id}")
        superseded_seen.add(record.supersedes_commitment_id)
        if decision.outcome != AssistanceRenegotiationProposalOutcome.ACCEPT.value:
            raise ValueError(f"replacement commitment lacks accepted replacement terms: {record.commitment_id}")
        if proposal.supersedes_commitment_id != old.commitment_id or proposal.supersedes_proposal_id != old.proposal_id:
            raise ValueError(f"replacement commitment old-lineage mismatch: {record.commitment_id}")
        if decision.proposal_id != proposal.proposal_id or record.replacement_proposal_id != proposal.proposal_id:
            raise ValueError(f"replacement commitment proposal lineage mismatch: {record.commitment_id}")
        if record.requester_id != old.requester_id or record.responder_id != old.responder_id:
            raise ValueError(f"replacement commitment actor binding mismatch: {record.commitment_id}")
        if record.proposal_provenance_root != proposal.provenance_root:
            raise ValueError(f"replacement commitment proposal provenance mismatch: {record.commitment_id}")
        _require_delivered_event(
            queue,
            record.decision_reply_event_id,
            sender_id=old.requester_id,
            receiver_id=old.responder_id,
            label="replacement commitment",
        )

        profile = coordinator.agendas.get(record.responder_id, AgentAgendaProfile())
        old_rows = [row for row in profile.commitments if row.commitment_id == record.supersedes_commitment_id]
        replacement_rows = [row for row in profile.commitments if row.commitment_id == record.commitment_id]
        if old_rows:
            raise ValueError(f"superseded assistance commitment remains executable: {record.supersedes_commitment_id}")
        if len(replacement_rows) != 1 or replacement_rows[0] != _replacement_schedule(record):
            raise ValueError(f"replacement assistance commitment agenda mismatch: {record.commitment_id}")


def _validate_generation(
    *,
    coordinator: GlobalNpcWorldEventCoordinator,
    semantic_minute: int,
    action_ledger: WorldActionIntentLedger,
    commitment_ledger: AssistanceCommitmentLedger,
    deferral_ledger: AssistanceDeferralLedger,
    counterproposal_ledger: AssistanceCounterproposalLedger,
    counterproposal_commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    commitment_viability_ledger: AssistanceCommitmentViabilityLedger,
    commitment_start_ledger: AssistanceCommitmentStartLedger,
    commitment_disposition_ledger: AssistanceCommitmentDispositionLedger,
    renegotiation_decision_ledger: AssistanceRenegotiationDecisionLedger,
    renegotiation_proposal_ledger: AssistanceRenegotiationProposalLedger,
    renegotiation_proposal_decision_ledger: AssistanceRenegotiationProposalDecisionLedger,
    replacement_commitment_ledger: AssistanceRenegotiationReplacementCommitmentLedger,
) -> None:
    shadow = _shadow_with_superseded_commitments(
        coordinator,
        counterproposal_commitment_ledger,
        replacement_commitment_ledger,
    )
    _validate_causal_generation(
        coordinator=shadow,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
        counterproposal_ledger=counterproposal_ledger,
        counterproposal_commitment_ledger=counterproposal_commitment_ledger,
        commitment_viability_ledger=commitment_viability_ledger,
        semantic_minute=semantic_minute,
    )
    compatibility_base = SimpleNamespace(
        world=SimpleNamespace(coordinator=shadow),
        counterproposal_commitment_ledger=counterproposal_commitment_ledger,
        commitment_viability_ledger=commitment_viability_ledger,
    )
    _validate_start_and_disposition(
        base=compatibility_base,
        start_ledger=commitment_start_ledger,
        disposition_ledger=commitment_disposition_ledger,
        semantic_minute=semantic_minute,
    )
    _validate_late_assistance_chain(
        coordinator=coordinator,
        counterproposal_commitments=counterproposal_commitment_ledger,
        disposition_ledger=commitment_disposition_ledger,
        renegotiation_decisions=renegotiation_decision_ledger,
        renegotiation_proposals=renegotiation_proposal_ledger,
        proposal_decisions=renegotiation_proposal_decision_ledger,
        replacements=replacement_commitment_ledger,
        semantic_minute=semantic_minute,
    )


def build_assistance_world_checkpoint_v6(
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
    renegotiation_decision_ledger: AssistanceRenegotiationDecisionLedger | None = None,
    renegotiation_proposal_ledger: AssistanceRenegotiationProposalLedger | None = None,
    renegotiation_proposal_decision_ledger: AssistanceRenegotiationProposalDecisionLedger | None = None,
    replacement_commitment_ledger: AssistanceRenegotiationReplacementCommitmentLedger | None = None,
) -> dict[str, object]:
    """Snapshot assistance state through accepted renegotiated replacement commitments."""
    deferral_ledger = deferral_ledger or AssistanceDeferralLedger()
    counterproposal_ledger = counterproposal_ledger or AssistanceCounterproposalLedger()
    counterproposal_commitment_ledger = counterproposal_commitment_ledger or AssistanceCounterproposalCommitmentLedger()
    commitment_viability_ledger = commitment_viability_ledger or AssistanceCommitmentViabilityLedger()
    commitment_start_ledger = commitment_start_ledger or AssistanceCommitmentStartLedger()
    commitment_disposition_ledger = commitment_disposition_ledger or AssistanceCommitmentDispositionLedger()
    renegotiation_decision_ledger = renegotiation_decision_ledger or AssistanceRenegotiationDecisionLedger()
    renegotiation_proposal_ledger = renegotiation_proposal_ledger or AssistanceRenegotiationProposalLedger()
    renegotiation_proposal_decision_ledger = (
        renegotiation_proposal_decision_ledger or AssistanceRenegotiationProposalDecisionLedger()
    )
    replacement_commitment_ledger = (
        replacement_commitment_ledger or AssistanceRenegotiationReplacementCommitmentLedger()
    )
    _validate_generation(
        coordinator=coordinator,
        semantic_minute=semantic_minute,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
        counterproposal_ledger=counterproposal_ledger,
        counterproposal_commitment_ledger=counterproposal_commitment_ledger,
        commitment_viability_ledger=commitment_viability_ledger,
        commitment_start_ledger=commitment_start_ledger,
        commitment_disposition_ledger=commitment_disposition_ledger,
        renegotiation_decision_ledger=renegotiation_decision_ledger,
        renegotiation_proposal_ledger=renegotiation_proposal_ledger,
        renegotiation_proposal_decision_ledger=renegotiation_proposal_decision_ledger,
        replacement_commitment_ledger=replacement_commitment_ledger,
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
        "assistance_commitment_viability": commitment_viability_ledger.snapshot(),
        "assistance_commitment_start": commitment_start_ledger.snapshot(),
        "assistance_commitment_disposition": commitment_disposition_ledger.snapshot(),
        "assistance_renegotiation_decisions": renegotiation_decision_ledger.snapshot(),
        "assistance_renegotiation_proposals": renegotiation_proposal_ledger.snapshot(),
        "assistance_renegotiation_proposal_decisions": renegotiation_proposal_decision_ledger.snapshot(),
        "assistance_renegotiation_replacement_commitments": replacement_commitment_ledger.snapshot(),
    }
    return payload | {"sha256": _digest(payload)}


def _restore_schedules(
    *,
    world: RestoredWorldCheckpoint,
    commitment_ledger: AssistanceCommitmentLedger,
    counterproposal_commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    replacement_commitment_ledger: AssistanceRenegotiationReplacementCommitmentLedger,
) -> None:
    superseded = {row.supersedes_commitment_id for row in replacement_commitment_ledger.records.values()}
    for record in commitment_ledger.records.values():
        _restore_commitment_into_agenda(
            world=world,
            responder_id=record.responder_id,
            expected=_scheduled_commitment(record),
            conflict_label="assistance commitment",
        )
    for record in counterproposal_commitment_ledger.records.values():
        if record.commitment_id in superseded:
            continue
        _restore_commitment_into_agenda(
            world=world,
            responder_id=record.responder_id,
            expected=_scheduled_counterproposal_commitment(record),
            conflict_label="counterproposal commitment",
        )
    for record in replacement_commitment_ledger.records.values():
        _restore_commitment_into_agenda(
            world=world,
            responder_id=record.responder_id,
            expected=_replacement_schedule(record),
            conflict_label="replacement assistance commitment",
        )


def restore_assistance_world_checkpoint_v6(
    snapshot: Mapping[str, object],
    *,
    channels: Mapping[str, CommunicationChannel],
    agendas: Mapping[str, AgentAgendaProfile] | None = None,
) -> RestoredAssistanceWorldCheckpointV6:
    if snapshot.get("schema_version") == LEGACY_SCHEMA_VERSION_V5:
        legacy = restore_assistance_world_checkpoint_v5(snapshot, channels=channels, agendas=agendas)
        return RestoredAssistanceWorldCheckpointV6(
            world=legacy.base.world,
            action_ledger=legacy.base.action_ledger,
            commitment_ledger=legacy.base.commitment_ledger,
            deferral_ledger=legacy.base.deferral_ledger,
            counterproposal_ledger=legacy.base.counterproposal_ledger,
            counterproposal_commitment_ledger=legacy.base.counterproposal_commitment_ledger,
            commitment_viability_ledger=legacy.base.commitment_viability_ledger,
            commitment_start_ledger=legacy.commitment_start_ledger,
            commitment_disposition_ledger=legacy.commitment_disposition_ledger,
            renegotiation_decision_ledger=AssistanceRenegotiationDecisionLedger(),
            renegotiation_proposal_ledger=AssistanceRenegotiationProposalLedger(),
            renegotiation_proposal_decision_ledger=AssistanceRenegotiationProposalDecisionLedger(),
            replacement_commitment_ledger=AssistanceRenegotiationReplacementCommitmentLedger(),
        )
    if snapshot.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unsupported assistance world checkpoint v6 schema")
    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("assistance world checkpoint v6 sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest(payload) != digest:
        raise ValueError("assistance world checkpoint v6 digest mismatch")

    component_names = (
        "world_checkpoint",
        "world_action_intents",
        "assistance_commitments",
        "assistance_deferrals",
        "assistance_counterproposals",
        "assistance_counterproposal_commitments",
        "assistance_commitment_viability",
        "assistance_commitment_start",
        "assistance_commitment_disposition",
        "assistance_renegotiation_decisions",
        "assistance_renegotiation_proposals",
        "assistance_renegotiation_proposal_decisions",
        "assistance_renegotiation_replacement_commitments",
    )
    for name in component_names:
        if not isinstance(payload.get(name), Mapping):
            raise ValueError(f"assistance world checkpoint v6 component must be a mapping: {name}")

    action_ledger = WorldActionIntentLedger.from_snapshot(payload["world_action_intents"])
    commitment_ledger = AssistanceCommitmentLedger.from_snapshot(payload["assistance_commitments"])
    deferral_ledger = AssistanceDeferralLedger.from_snapshot(payload["assistance_deferrals"])
    counterproposal_ledger = AssistanceCounterproposalLedger.from_snapshot(payload["assistance_counterproposals"])
    counterproposal_commitment_ledger = AssistanceCounterproposalCommitmentLedger.from_snapshot(
        payload["assistance_counterproposal_commitments"]
    )
    commitment_viability_ledger = AssistanceCommitmentViabilityLedger.from_snapshot(
        payload["assistance_commitment_viability"]
    )
    commitment_start_ledger = AssistanceCommitmentStartLedger.from_snapshot(payload["assistance_commitment_start"])
    commitment_disposition_ledger = AssistanceCommitmentDispositionLedger.from_snapshot(
        payload["assistance_commitment_disposition"]
    )
    renegotiation_decision_ledger = AssistanceRenegotiationDecisionLedger.from_snapshot(
        payload["assistance_renegotiation_decisions"]
    )
    renegotiation_proposal_ledger = AssistanceRenegotiationProposalLedger.from_snapshot(
        payload["assistance_renegotiation_proposals"]
    )
    renegotiation_proposal_decision_ledger = AssistanceRenegotiationProposalDecisionLedger.from_snapshot(
        payload["assistance_renegotiation_proposal_decisions"]
    )
    replacement_commitment_ledger = AssistanceRenegotiationReplacementCommitmentLedger.from_snapshot(
        payload["assistance_renegotiation_replacement_commitments"]
    )
    world = restore_checkpoint(payload["world_checkpoint"], channels=channels, agendas=agendas)
    checkpoint_minute = int(payload["semantic_minute"])
    if world.semantic_minute != checkpoint_minute:
        raise ValueError("assistance world checkpoint v6 generation time mismatch")
    _restore_schedules(
        world=world,
        commitment_ledger=commitment_ledger,
        counterproposal_commitment_ledger=counterproposal_commitment_ledger,
        replacement_commitment_ledger=replacement_commitment_ledger,
    )
    _validate_generation(
        coordinator=world.coordinator,
        semantic_minute=checkpoint_minute,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
        counterproposal_ledger=counterproposal_ledger,
        counterproposal_commitment_ledger=counterproposal_commitment_ledger,
        commitment_viability_ledger=commitment_viability_ledger,
        commitment_start_ledger=commitment_start_ledger,
        commitment_disposition_ledger=commitment_disposition_ledger,
        renegotiation_decision_ledger=renegotiation_decision_ledger,
        renegotiation_proposal_ledger=renegotiation_proposal_ledger,
        renegotiation_proposal_decision_ledger=renegotiation_proposal_decision_ledger,
        replacement_commitment_ledger=replacement_commitment_ledger,
    )
    return RestoredAssistanceWorldCheckpointV6(
        world=world,
        action_ledger=action_ledger,
        commitment_ledger=commitment_ledger,
        deferral_ledger=deferral_ledger,
        counterproposal_ledger=counterproposal_ledger,
        counterproposal_commitment_ledger=counterproposal_commitment_ledger,
        commitment_viability_ledger=commitment_viability_ledger,
        commitment_start_ledger=commitment_start_ledger,
        commitment_disposition_ledger=commitment_disposition_ledger,
        renegotiation_decision_ledger=renegotiation_decision_ledger,
        renegotiation_proposal_ledger=renegotiation_proposal_ledger,
        renegotiation_proposal_decision_ledger=renegotiation_proposal_decision_ledger,
        replacement_commitment_ledger=replacement_commitment_ledger,
    )
