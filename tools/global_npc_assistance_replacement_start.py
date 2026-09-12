from __future__ import annotations

from tools.global_npc_assistance_commitment_lineage import resolve_assistance_commitment_lineage
from tools.global_npc_assistance_commitment_start import (
    AssistanceCommitmentStartAssessment,
    AssistanceCommitmentStartLedger,
    AssistanceCommitmentStartWatch,
    CommitmentStartCondition,
)
from tools.global_npc_assistance_commitment_viability import (
    AssistanceCommitmentViabilityLedger,
    CommitmentViability,
)
from tools.global_npc_assistance_counterproposal_commitment import AssistanceCounterproposalCommitmentLedger
from tools.global_npc_assistance_renegotiation_replacement_commitment import (
    AssistanceRenegotiationReplacementCommitmentLedger,
)
from tools.global_npc_replanning import NpcReplanQueue, ReplanReason, ReplanTrigger


def _active_replacement_node(*, initial_ledger, replacement_ledger, commitment_id):
    replacement = replacement_ledger.records.get(commitment_id)
    if replacement is None:
        raise KeyError(f"unknown replacement assistance commitment: {commitment_id}")
    current_id = replacement.supersedes_commitment_id
    seen = {commitment_id}
    while current_id in replacement_ledger.records:
        if current_id in seen:
            raise ValueError(f"assistance replacement lineage cycle at {current_id}")
        seen.add(current_id)
        current_id = replacement_ledger.records[current_id].supersedes_commitment_id
    view = resolve_assistance_commitment_lineage(
        initial_ledger=initial_ledger,
        replacement_ledger=replacement_ledger,
        root_commitment_id=current_id,
    )
    if view.active_commitment_id != commitment_id:
        raise ValueError("start assessment may only target the active replacement commitment")
    return view.nodes[-1]


def arm_active_replacement_start_watch(
    *,
    initial_ledger: AssistanceCounterproposalCommitmentLedger,
    replacement_ledger: AssistanceRenegotiationReplacementCommitmentLedger,
    start_ledger: AssistanceCommitmentStartLedger,
    replan_queue: NpcReplanQueue,
    commitment_id: str,
    watch_id: str,
    armed_minute: int,
    provenance_root: str,
    priority: int = 9,
) -> AssistanceCommitmentStartWatch:
    """Arm the existing start ledger for the currently active replacement generation."""
    if priority < 0:
        raise ValueError("start watch priority must be non-negative")
    if not watch_id or not provenance_root:
        raise ValueError("watch_id and provenance_root are required")
    node = _active_replacement_node(
        initial_ledger=initial_ledger,
        replacement_ledger=replacement_ledger,
        commitment_id=commitment_id,
    )
    trigger_id = f"replan:assistance-replacement-start:{watch_id}"
    watch = AssistanceCommitmentStartWatch(
        watch_id=watch_id,
        commitment_id=node.commitment_id,
        proposal_id=node.proposal_id,
        requester_id=node.requester_id,
        responder_id=node.responder_id,
        start_minute=node.start_minute,
        armed_minute=armed_minute,
        provenance_root=provenance_root,
        trigger_id=trigger_id,
    )
    if armed_minute < 0 or armed_minute >= node.start_minute:
        raise ValueError("replacement start watch must be armed before start")
    existing = start_ledger.watches.get(watch_id)
    if existing is not None:
        if existing != watch:
            raise ValueError("commitment start watch id reused with conflicting content")
        return existing
    stored = start_ledger.add_watch(watch)
    replan_queue.schedule(
        ReplanTrigger(
            trigger_id=trigger_id,
            agent_id=node.responder_id,
            reason=ReplanReason.SCHEDULE_DUE,
            due_minute=node.start_minute,
            source_ref=watch_id,
            priority=priority,
        )
    )
    return stored


def assess_active_replacement_start(
    *,
    initial_ledger: AssistanceCounterproposalCommitmentLedger,
    replacement_ledger: AssistanceRenegotiationReplacementCommitmentLedger,
    viability_ledger: AssistanceCommitmentViabilityLedger,
    start_ledger: AssistanceCommitmentStartLedger,
    commitment_id: str,
    watch_id: str,
    assessment_id: str,
    semantic_minute: int,
) -> AssistanceCommitmentStartAssessment | None:
    """Record an adverse start fact for the active replacement without changing its terms."""
    node = _active_replacement_node(
        initial_ledger=initial_ledger,
        replacement_ledger=replacement_ledger,
        commitment_id=commitment_id,
    )
    watch = start_ledger.watches.get(watch_id)
    if watch is None:
        raise KeyError(f"unknown assistance commitment start watch: {watch_id}")
    if watch.commitment_id != node.commitment_id or watch.proposal_id != node.proposal_id:
        raise ValueError("replacement start watch binding mismatch")
    if semantic_minute != node.start_minute:
        raise ValueError("replacement start assessment must occur at the active start minute")
    existing_for_commitment = start_ledger.assessment_for(commitment_id)
    if existing_for_commitment is not None:
        existing = start_ledger.assessments.get(assessment_id)
        if existing is not None:
            return existing
        raise ValueError("commitment already has a start assessment")

    latest = viability_ledger.latest_for(commitment_id)
    if latest is None or latest.viability == CommitmentViability.RESTORED.value:
        return None
    if latest.semantic_minute >= node.start_minute:
        raise ValueError("replacement start assessment requires a pre-start viability observation")
    if latest.proposal_id != node.proposal_id:
        raise ValueError("replacement viability proposal binding mismatch at start")
    if latest.requester_id != node.requester_id or latest.responder_id != node.responder_id:
        raise ValueError("replacement viability actor binding mismatch at start")

    if latest.viability == CommitmentViability.BLOCKED.value:
        condition = CommitmentStartCondition.BLOCKED_AT_START
    elif latest.viability == CommitmentViability.AT_RISK.value:
        condition = CommitmentStartCondition.AT_RISK_AT_START
    else:
        raise ValueError("unsupported replacement viability state at start")

    assessment = AssistanceCommitmentStartAssessment(
        assessment_id=assessment_id,
        watch_id=watch.watch_id,
        commitment_id=node.commitment_id,
        proposal_id=node.proposal_id,
        requester_id=node.requester_id,
        responder_id=node.responder_id,
        semantic_minute=semantic_minute,
        condition=condition.value,
        viability_observation_id=latest.observation_id,
        constraint_kind=latest.constraint_kind,
        constraint_ref=latest.constraint_ref,
        evidence_ref=latest.evidence_ref,
        provenance_root=latest.provenance_root,
    )
    return start_ledger.add_assessment(assessment)
