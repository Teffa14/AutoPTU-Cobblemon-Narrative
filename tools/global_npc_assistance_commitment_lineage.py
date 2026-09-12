from __future__ import annotations

from dataclasses import dataclass

from tools.global_npc_ai import ScheduledCommitment
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
)
from tools.global_npc_assistance_renegotiation_replacement_commitment import (
    AssistanceRenegotiationReplacementCommitmentLedger,
)
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator


@dataclass(frozen=True)
class AssistanceCommitmentLineageNode:
    commitment_id: str
    parent_commitment_id: str | None
    proposal_id: str
    requester_id: str
    responder_id: str
    intent_kind: str
    start_minute: int
    end_minute: int
    location_ref: str | None
    scope_ref: str | None
    alternative_ref: str | None
    priority: int
    hard: bool
    grace_minutes: int
    required_knowledge: tuple[str, ...]
    required_permissions: tuple[str, ...]
    requires_local_projection: bool
    requires_structured_mechanics: bool
    provenance_root: str
    generation: int


@dataclass(frozen=True)
class AssistanceCommitmentLineageView:
    root_commitment_id: str
    active_commitment_id: str
    nodes: tuple[AssistanceCommitmentLineageNode, ...]

    @property
    def replacement_count(self) -> int:
        return len(self.nodes) - 1


def _root_node(record) -> AssistanceCommitmentLineageNode:
    return AssistanceCommitmentLineageNode(
        commitment_id=record.commitment_id,
        parent_commitment_id=None,
        proposal_id=record.proposal_id,
        requester_id=record.requester_id,
        responder_id=record.responder_id,
        intent_kind=record.intent_kind,
        start_minute=record.start_minute,
        end_minute=record.end_minute,
        location_ref=record.location_ref,
        scope_ref=record.scope_ref,
        alternative_ref=record.alternative_ref,
        priority=record.priority,
        hard=record.hard,
        grace_minutes=record.grace_minutes,
        required_knowledge=tuple(record.required_knowledge),
        required_permissions=tuple(record.required_permissions),
        requires_local_projection=record.requires_local_projection,
        requires_structured_mechanics=record.requires_structured_mechanics,
        provenance_root=record.provenance_root,
        generation=0,
    )


def _replacement_node(record, generation: int) -> AssistanceCommitmentLineageNode:
    return AssistanceCommitmentLineageNode(
        commitment_id=record.commitment_id,
        parent_commitment_id=record.supersedes_commitment_id,
        proposal_id=record.replacement_proposal_id,
        requester_id=record.requester_id,
        responder_id=record.responder_id,
        intent_kind=record.intent_kind,
        start_minute=record.start_minute,
        end_minute=record.end_minute,
        location_ref=record.location_ref,
        scope_ref=record.scope_ref,
        alternative_ref=record.alternative_ref,
        priority=record.priority,
        hard=record.hard,
        grace_minutes=record.grace_minutes,
        required_knowledge=tuple(record.required_knowledge),
        required_permissions=tuple(record.required_permissions),
        requires_local_projection=record.requires_local_projection,
        requires_structured_mechanics=record.requires_structured_mechanics,
        provenance_root=record.provenance_root,
        generation=generation,
    )


def _same_execution_identity(parent: AssistanceCommitmentLineageNode, child_record) -> bool:
    return (
        parent.requester_id == child_record.requester_id
        and parent.responder_id == child_record.responder_id
        and parent.intent_kind == child_record.intent_kind
        and parent.priority == child_record.priority
        and parent.hard == child_record.hard
        and parent.grace_minutes == child_record.grace_minutes
        and frozenset(parent.required_knowledge) == frozenset(child_record.required_knowledge)
        and frozenset(parent.required_permissions) == frozenset(child_record.required_permissions)
        and parent.requires_local_projection == child_record.requires_local_projection
        and parent.requires_structured_mechanics == child_record.requires_structured_mechanics
    )


def _children_by_parent(replacement_ledger: AssistanceRenegotiationReplacementCommitmentLedger):
    children: dict[str, list[object]] = {}
    for record in replacement_ledger.records.values():
        children.setdefault(record.supersedes_commitment_id, []).append(record)
    for parent_id, rows in children.items():
        if len(rows) > 1:
            raise ValueError(f"assistance commitment lineage branches at {parent_id}")
    return children


def validate_assistance_commitment_lineage_graph(
    *,
    initial_ledger: AssistanceCounterproposalCommitmentLedger,
    replacement_ledger: AssistanceRenegotiationReplacementCommitmentLedger,
) -> None:
    """Validate all assistance replacement chains without mutating durable history.

    The current runtime materializes only one replacement generation. This view is
    deliberately generation-neutral so later passes can admit replacement-of-
    replacement records without changing how history is queried.
    """

    duplicate_ids = set(initial_ledger.records).intersection(replacement_ledger.records)
    if duplicate_ids:
        raise ValueError(f"commitment ids exist in both ledgers: {sorted(duplicate_ids)}")

    children = _children_by_parent(replacement_ledger)
    all_ids = set(initial_ledger.records).union(replacement_ledger.records)
    for record in replacement_ledger.records.values():
        if record.supersedes_commitment_id not in all_ids:
            raise ValueError(
                f"replacement commitment {record.commitment_id} has unknown parent "
                f"{record.supersedes_commitment_id}"
            )

    for start_id in replacement_ledger.records:
        seen: set[str] = set()
        current_id = start_id
        while current_id in replacement_ledger.records:
            if current_id in seen:
                raise ValueError(f"assistance commitment lineage cycle at {current_id}")
            seen.add(current_id)
            current_id = replacement_ledger.records[current_id].supersedes_commitment_id

    for root_id, root_record in initial_ledger.records.items():
        parent = _root_node(root_record)
        current_id = root_id
        generation = 0
        while current_id in children:
            child_record = children[current_id][0]
            if child_record.superseded_provenance_root != parent.provenance_root:
                raise ValueError(
                    f"replacement commitment {child_record.commitment_id} parent provenance mismatch"
                )
            if not _same_execution_identity(parent, child_record):
                raise ValueError(
                    f"replacement commitment {child_record.commitment_id} changes execution identity"
                )
            generation += 1
            parent = _replacement_node(child_record, generation)
            current_id = child_record.commitment_id

    rooted_ids: set[str] = set(initial_ledger.records)
    pending = list(initial_ledger.records)
    while pending:
        parent_id = pending.pop()
        for child_record in children.get(parent_id, []):
            if child_record.commitment_id not in rooted_ids:
                rooted_ids.add(child_record.commitment_id)
                pending.append(child_record.commitment_id)
    unrooted = set(replacement_ledger.records).difference(rooted_ids)
    if unrooted:
        raise ValueError(f"replacement commitments lack an original assistance root: {sorted(unrooted)}")


def resolve_assistance_commitment_lineage(
    *,
    initial_ledger: AssistanceCounterproposalCommitmentLedger,
    replacement_ledger: AssistanceRenegotiationReplacementCommitmentLedger,
    root_commitment_id: str,
) -> AssistanceCommitmentLineageView:
    validate_assistance_commitment_lineage_graph(
        initial_ledger=initial_ledger,
        replacement_ledger=replacement_ledger,
    )
    root_record = initial_ledger.records.get(root_commitment_id)
    if root_record is None:
        raise KeyError(f"unknown original assistance commitment: {root_commitment_id}")

    children = _children_by_parent(replacement_ledger)
    nodes = [_root_node(root_record)]
    current_id = root_commitment_id
    while current_id in children:
        record = children[current_id][0]
        nodes.append(_replacement_node(record, len(nodes)))
        current_id = record.commitment_id
    return AssistanceCommitmentLineageView(
        root_commitment_id=root_commitment_id,
        active_commitment_id=current_id,
        nodes=tuple(nodes),
    )


def _scheduled(node: AssistanceCommitmentLineageNode) -> ScheduledCommitment:
    return ScheduledCommitment(
        commitment_id=node.commitment_id,
        intent_kind=node.intent_kind,
        start_minute=node.start_minute,
        end_minute=node.end_minute,
        priority=node.priority,
        hard=node.hard,
        grace_minutes=node.grace_minutes,
        required_knowledge=frozenset(node.required_knowledge),
        required_permissions=frozenset(node.required_permissions),
        target_ref=node.requester_id,
        requires_local_projection=node.requires_local_projection,
        requires_structured_mechanics=node.requires_structured_mechanics,
    )


def assert_assistance_lineage_agenda_consistency(
    *,
    view: AssistanceCommitmentLineageView,
    coordinator: GlobalNpcWorldEventCoordinator,
) -> ScheduledCommitment:
    """Require only the latest generation to remain executable for this lineage."""

    if not view.nodes:
        raise ValueError("assistance lineage view requires at least one node")
    responder_id = view.nodes[0].responder_id
    if any(node.responder_id != responder_id for node in view.nodes):
        raise ValueError("assistance lineage responder changed across generations")
    profile = coordinator.agendas.get(responder_id)
    if profile is None:
        raise ValueError("assistance lineage responder has no agenda")

    expected = _scheduled(view.nodes[-1])
    lineage_ids = {node.commitment_id for node in view.nodes}
    matching = [row for row in profile.commitments if row.commitment_id in lineage_ids]
    if matching != [expected]:
        raise ValueError("assistance lineage agenda must contain only the latest executable commitment")
    return expected
