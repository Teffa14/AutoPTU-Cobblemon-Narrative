from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping

from tools.global_npc_ai import ScheduledCommitment
from tools.global_npc_assistance_counterproposal import AssistanceCounterproposalLedger
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator

SCHEMA_VERSION = "OUROS_ASSISTANCE_COUNTERPROPOSAL_COMMITMENT_LEDGER_V1"
REQUEST_KIND = "REQUEST_ASSISTANCE"
COUNTERPROPOSE_KIND = "COUNTERPROPOSE_ASSISTANCE_REQUEST"
ACCEPT_KIND = "ACCEPT_ASSISTANCE_COUNTERPROPOSAL"


@dataclass(frozen=True)
class AssistanceCounterproposalCommitmentRecord:
    commitment_id: str
    proposal_id: str
    request_action_id: str
    response_action_id: str
    decision_action_id: str
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


class AssistanceCounterproposalCommitmentLedger:
    """Durable link from one accepted proposal to one responder commitment."""

    def __init__(self) -> None:
        self.records: dict[str, AssistanceCounterproposalCommitmentRecord] = {}

    def add(
        self, record: AssistanceCounterproposalCommitmentRecord
    ) -> AssistanceCounterproposalCommitmentRecord:
        existing = self.records.get(record.commitment_id)
        if existing is not None:
            if existing != record:
                raise ValueError("counterproposal commitment id reused with conflicting content")
            return existing
        self.records[record.commitment_id] = record
        return record

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "records": [asdict(self.records[key]) for key in sorted(self.records)],
        }

    @classmethod
    def from_snapshot(
        cls, payload: Mapping[str, object]
    ) -> "AssistanceCounterproposalCommitmentLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported counterproposal commitment ledger schema")
        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("counterproposal commitment snapshot records must be a list")
        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("counterproposal commitment snapshot row must be an object")
            record = AssistanceCounterproposalCommitmentRecord(
                commitment_id=str(raw["commitment_id"]),
                proposal_id=str(raw["proposal_id"]),
                request_action_id=str(raw["request_action_id"]),
                response_action_id=str(raw["response_action_id"]),
                decision_action_id=str(raw["decision_action_id"]),
                requester_id=str(raw["requester_id"]),
                responder_id=str(raw["responder_id"]),
                intent_kind=str(raw["intent_kind"]),
                start_minute=int(raw["start_minute"]),
                end_minute=int(raw["end_minute"]),
                location_ref=None if raw.get("location_ref") is None else str(raw["location_ref"]),
                scope_ref=None if raw.get("scope_ref") is None else str(raw["scope_ref"]),
                alternative_ref=None if raw.get("alternative_ref") is None else str(raw["alternative_ref"]),
                priority=int(raw["priority"]),
                hard=bool(raw["hard"]),
                grace_minutes=int(raw["grace_minutes"]),
                required_knowledge=tuple(str(v) for v in raw.get("required_knowledge", [])),
                required_permissions=tuple(str(v) for v in raw.get("required_permissions", [])),
                requires_local_projection=bool(raw["requires_local_projection"]),
                requires_structured_mechanics=bool(raw["requires_structured_mechanics"]),
                provenance_root=str(raw["provenance_root"]),
            )
            if (
                not record.commitment_id
                or not record.proposal_id
                or not record.decision_action_id
                or record.provenance_root != record.decision_action_id
            ):
                raise ValueError("invalid counterproposal commitment snapshot row")
            ledger.add(record)
        return ledger


@dataclass(frozen=True)
class AssistanceCounterproposalCommitmentOutcome:
    record: AssistanceCounterproposalCommitmentRecord
    commitment: ScheduledCommitment


def _validated_chain(
    *,
    action_ledger: WorldActionIntentLedger,
    proposal_ledger: AssistanceCounterproposalLedger,
    proposal_id: str,
    decision_action_id: str,
):
    proposal = proposal_ledger.records.get(proposal_id)
    if proposal is None:
        raise KeyError(f"unknown assistance counterproposal: {proposal_id}")
    if proposal.provenance_root != proposal.response_action_id:
        raise ValueError("counterproposal provenance must match response action")

    request = action_ledger.records.get(proposal.request_action_id)
    response = action_ledger.records.get(proposal.response_action_id)
    decision = action_ledger.records.get(decision_action_id)
    if request is None or request.status != "PLANNED" or request.intent_kind != REQUEST_KIND:
        raise ValueError("counterproposal commitment requires its original assistance request")
    if response is None or response.status != "PLANNED" or response.intent_kind != COUNTERPROPOSE_KIND:
        raise ValueError("counterproposal commitment requires its responder counterproposal")
    if decision is None or decision.status != "PLANNED" or decision.intent_kind != ACCEPT_KIND:
        raise ValueError("counterproposal commitment requires requester acceptance")
    if request.agent_id != proposal.requester_id or request.target_ref != proposal.responder_id:
        raise ValueError("counterproposal request actor binding mismatch")
    if response.agent_id != proposal.responder_id or response.target_ref != proposal.requester_id:
        raise ValueError("counterproposal response actor binding mismatch")
    if decision.agent_id != proposal.requester_id or decision.target_ref != proposal.responder_id:
        raise ValueError("counterproposal acceptance actor binding mismatch")
    if decision.source_ref != proposal.proposal_id:
        raise ValueError("counterproposal acceptance must name the exact proposal")
    if decision.semantic_minute < response.semantic_minute:
        raise ValueError("counterproposal acceptance cannot predate its proposal")
    if proposal.expires_minute is not None and decision.semantic_minute > proposal.expires_minute:
        raise ValueError("expired counterproposal cannot create a commitment")
    if proposal.proposed_start_minute is None or proposal.proposed_end_minute is None:
        raise ValueError("accepted counterproposal requires a complete scheduled window")
    return proposal, request, response, decision


def materialize_counterproposal_assistance_commitment(
    *,
    action_ledger: WorldActionIntentLedger,
    proposal_ledger: AssistanceCounterproposalLedger,
    commitment_ledger: AssistanceCounterproposalCommitmentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    proposal_id: str,
    decision_action_id: str,
    commitment_id: str,
    intent_kind: str,
    materialized_minute: int,
    priority: int = 5,
    hard: bool = False,
    grace_minutes: int = 0,
    required_knowledge: frozenset[str] = frozenset(),
    required_permissions: frozenset[str] = frozenset(),
    requires_local_projection: bool = False,
    requires_structured_mechanics: bool = False,
) -> AssistanceCounterproposalCommitmentOutcome:
    """Materialize exact accepted time terms as responder-owned agenda work.

    Location, scope and alternative terms remain provenance metadata here. This
    function does not move the responder, reserve a route/resource, grant a
    tactical verb, complete assistance or execute AutoPTU.
    """
    if not commitment_id or not intent_kind:
        raise ValueError("commitment_id and intent_kind are required")
    if min(materialized_minute, priority, grace_minutes) < 0:
        raise ValueError("commitment materialization values must be non-negative")

    proposal, request, response, decision = _validated_chain(
        action_ledger=action_ledger,
        proposal_ledger=proposal_ledger,
        proposal_id=proposal_id,
        decision_action_id=decision_action_id,
    )
    start_minute = proposal.proposed_start_minute
    end_minute = proposal.proposed_end_minute
    assert start_minute is not None and end_minute is not None
    if materialized_minute < decision.semantic_minute:
        raise ValueError("counterproposal commitment cannot predate requester acceptance")
    if start_minute < materialized_minute:
        raise ValueError("accepted counterproposal window is already in the past")

    commitment = ScheduledCommitment(
        commitment_id=commitment_id,
        intent_kind=intent_kind,
        start_minute=start_minute,
        end_minute=end_minute,
        priority=priority,
        hard=hard,
        grace_minutes=grace_minutes,
        required_knowledge=required_knowledge,
        required_permissions=required_permissions,
        target_ref=request.agent_id,
        requires_local_projection=requires_local_projection,
        requires_structured_mechanics=requires_structured_mechanics,
    )
    profile = coordinator.agendas.get(response.agent_id, AgentAgendaProfile())
    same_id = [row for row in profile.commitments if row.commitment_id == commitment_id]
    if same_id and same_id[0] != commitment:
        raise ValueError("agenda already contains conflicting counterproposal commitment")

    record = AssistanceCounterproposalCommitmentRecord(
        commitment_id=commitment_id,
        proposal_id=proposal.proposal_id,
        request_action_id=request.action_id,
        response_action_id=response.action_id,
        decision_action_id=decision.action_id,
        requester_id=proposal.requester_id,
        responder_id=proposal.responder_id,
        intent_kind=intent_kind,
        start_minute=start_minute,
        end_minute=end_minute,
        location_ref=proposal.location_ref,
        scope_ref=proposal.scope_ref,
        alternative_ref=proposal.alternative_ref,
        priority=priority,
        hard=hard,
        grace_minutes=grace_minutes,
        required_knowledge=tuple(sorted(required_knowledge)),
        required_permissions=tuple(sorted(required_permissions)),
        requires_local_projection=requires_local_projection,
        requires_structured_mechanics=requires_structured_mechanics,
        provenance_root=decision.action_id,
    )
    record = commitment_ledger.add(record)

    if not same_id:
        coordinator.agendas[response.agent_id] = AgentAgendaProfile(
            goals=profile.goals,
            needs=profile.needs,
            commitments=profile.commitments + (commitment,),
            situational_intents=profile.situational_intents,
            active_intent_id=profile.active_intent_id,
            continuity_bonus=profile.continuity_bonus,
        )
    return AssistanceCounterproposalCommitmentOutcome(record=record, commitment=commitment)
