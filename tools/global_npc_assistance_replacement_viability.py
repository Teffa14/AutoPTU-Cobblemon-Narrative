from __future__ import annotations

from tools.global_npc_assistance_commitment_lineage import (
    AssistanceCommitmentLineageView,
    resolve_assistance_commitment_lineage,
)
from tools.global_npc_assistance_commitment_viability import (
    AssistanceCommitmentViabilityLedger,
    AssistanceCommitmentViabilityObservation,
    CommitmentConstraintKind,
    CommitmentViability,
)
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
)
from tools.global_npc_assistance_renegotiation_replacement_commitment import (
    AssistanceRenegotiationReplacementCommitmentLedger,
)
from tools.global_npc_replanning import NpcReplanQueue, ReplanReason, ReplanTrigger


def _lineage_for_replacement(
    *,
    initial_ledger: AssistanceCounterproposalCommitmentLedger,
    replacement_ledger: AssistanceRenegotiationReplacementCommitmentLedger,
    commitment_id: str,
) -> AssistanceCommitmentLineageView:
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

    if current_id not in initial_ledger.records:
        raise ValueError(f"replacement commitment {commitment_id} lacks an original assistance root")

    view = resolve_assistance_commitment_lineage(
        initial_ledger=initial_ledger,
        replacement_ledger=replacement_ledger,
        root_commitment_id=current_id,
    )
    if view.active_commitment_id != commitment_id:
        raise ValueError("viability evidence may only target the active replacement commitment")
    return view


def record_active_replacement_prestart_viability(
    *,
    initial_ledger: AssistanceCounterproposalCommitmentLedger,
    replacement_ledger: AssistanceRenegotiationReplacementCommitmentLedger,
    viability_ledger: AssistanceCommitmentViabilityLedger,
    replan_queue: NpcReplanQueue,
    commitment_id: str,
    observation_id: str,
    observer_id: str,
    semantic_minute: int,
    viability: CommitmentViability,
    constraint_kind: CommitmentConstraintKind,
    constraint_ref: str,
    evidence_ref: str,
    provenance_root: str,
    replan_priority: int = 8,
) -> AssistanceCommitmentViabilityObservation:
    """Attach pre-start evidence to the current replacement generation.

    Pass 437 remains the owner for original commitments. This bridge admits the
    same evidence semantics after a valid replacement exists, while preserving
    the full lineage and refusing observations on superseded generations.

    It does not cancel or reschedule work, create another replacement, reserve
    travel/resources, grant access, move an actor, change relationships, decide
    blame, complete assistance, or invoke AutoPTU.
    """

    if replan_priority < 0:
        raise ValueError("replan_priority must be non-negative")
    if not all((commitment_id, observation_id, observer_id, constraint_ref, evidence_ref, provenance_root)):
        raise ValueError("replacement viability requires non-empty references")

    view = _lineage_for_replacement(
        initial_ledger=initial_ledger,
        replacement_ledger=replacement_ledger,
        commitment_id=commitment_id,
    )
    node = view.nodes[-1]
    if observer_id != node.responder_id:
        raise ValueError("only the responder owning the active replacement can record execution viability")
    if semantic_minute < 0 or semantic_minute >= node.start_minute:
        raise ValueError("replacement viability observation must occur before the active start minute")

    if viability is CommitmentViability.RESTORED:
        if constraint_kind is not CommitmentConstraintKind.CLEARED:
            raise ValueError("restored replacement viability requires CLEARED constraint kind")
    elif constraint_kind is CommitmentConstraintKind.CLEARED:
        raise ValueError("CLEARED constraint kind is reserved for restored replacement viability")

    observation = AssistanceCommitmentViabilityObservation(
        observation_id=observation_id,
        commitment_id=node.commitment_id,
        proposal_id=node.proposal_id,
        requester_id=node.requester_id,
        responder_id=node.responder_id,
        observer_id=observer_id,
        semantic_minute=semantic_minute,
        viability=viability.value,
        constraint_kind=constraint_kind.value,
        constraint_ref=constraint_ref,
        evidence_ref=evidence_ref,
        provenance_root=provenance_root,
    )

    existing = viability_ledger.records.get(observation_id)
    if existing is not None:
        if existing != observation:
            raise ValueError("viability observation id reused with conflicting content")
        return existing

    previous = viability_ledger.latest_for(commitment_id)
    if previous is not None and semantic_minute < previous.semantic_minute:
        raise ValueError("viability history cannot move backward in semantic time")
    if viability is CommitmentViability.RESTORED:
        if previous is None or previous.viability == CommitmentViability.RESTORED.value:
            raise ValueError("restored viability requires a prior at-risk or blocked observation")

    stored = viability_ledger.add(observation)
    replan_queue.schedule(
        ReplanTrigger(
            trigger_id=f"replan:assistance-replacement-viability:{observation_id}",
            agent_id=node.responder_id,
            reason=ReplanReason.EXTERNAL_EVENT,
            due_minute=semantic_minute,
            source_ref=observation_id,
            priority=replan_priority,
        )
    )
    return stored
