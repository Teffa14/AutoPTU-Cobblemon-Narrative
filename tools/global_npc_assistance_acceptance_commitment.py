from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping

from tools.global_npc_ai import ScheduledCommitment
from tools.global_npc_assistance_response_dispatch import SUPPORTED_RESPONSE_KINDS
from tools.global_npc_information_network import DeliveryStatus
from tools.global_npc_world_action_intent import WorldActionIntentLedger
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


SCHEMA_VERSION = "OUROS_ASSISTANCE_COMMITMENT_LEDGER_V1"
REQUEST_KIND = "REQUEST_ASSISTANCE"
ACCEPT_KIND = "ACCEPT_ASSISTANCE_REQUEST"


@dataclass(frozen=True)
class AssistanceCommitmentRecord:
    commitment_id: str
    request_action_id: str
    response_action_id: str
    response_event_id: str
    responder_id: str
    requester_id: str
    intent_kind: str
    start_minute: int
    end_minute: int
    priority: int
    hard: bool
    grace_minutes: int
    required_knowledge: tuple[str, ...]
    required_permissions: tuple[str, ...]
    requires_local_projection: bool
    requires_structured_mechanics: bool
    provenance_root: str


class AssistanceCommitmentLedger:
    def __init__(self) -> None:
        self.records: dict[str, AssistanceCommitmentRecord] = {}

    def add(self, record: AssistanceCommitmentRecord) -> AssistanceCommitmentRecord:
        existing = self.records.get(record.commitment_id)
        if existing is not None:
            if existing != record:
                raise ValueError("assistance commitment id reused with conflicting content")
            return existing
        self.records[record.commitment_id] = record
        return record

    def snapshot(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "records": [asdict(self.records[key]) for key in sorted(self.records)],
        }

    @classmethod
    def from_snapshot(cls, payload: Mapping[str, object]) -> "AssistanceCommitmentLedger":
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("unsupported assistance commitment ledger schema")
        rows = payload.get("records")
        if not isinstance(rows, list):
            raise ValueError("assistance commitment snapshot records must be a list")
        ledger = cls()
        for raw in rows:
            if not isinstance(raw, Mapping):
                raise ValueError("assistance commitment snapshot row must be an object")
            record = AssistanceCommitmentRecord(
                commitment_id=str(raw["commitment_id"]),
                request_action_id=str(raw["request_action_id"]),
                response_action_id=str(raw["response_action_id"]),
                response_event_id=str(raw["response_event_id"]),
                responder_id=str(raw["responder_id"]),
                requester_id=str(raw["requester_id"]),
                intent_kind=str(raw["intent_kind"]),
                start_minute=int(raw["start_minute"]),
                end_minute=int(raw["end_minute"]),
                priority=int(raw["priority"]),
                hard=bool(raw["hard"]),
                grace_minutes=int(raw["grace_minutes"]),
                required_knowledge=tuple(str(v) for v in raw.get("required_knowledge", [])),
                required_permissions=tuple(str(v) for v in raw.get("required_permissions", [])),
                requires_local_projection=bool(raw["requires_local_projection"]),
                requires_structured_mechanics=bool(raw["requires_structured_mechanics"]),
                provenance_root=str(raw["provenance_root"]),
            )
            if not record.commitment_id or not record.response_action_id:
                raise ValueError("invalid assistance commitment snapshot row")
            ledger.add(record)
        return ledger


@dataclass(frozen=True)
class AssistanceCommitmentOutcome:
    record: AssistanceCommitmentRecord
    commitment: ScheduledCommitment


def _validate_delivered_acceptance(
    *,
    action_ledger: WorldActionIntentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    request_action_id: str,
    response_action_id: str,
    response_event_id: str,
):
    request = action_ledger.records.get(request_action_id)
    if request is None:
        raise KeyError(f"unknown assistance request action: {request_action_id}")
    if request.status != "PLANNED" or request.intent_kind != REQUEST_KIND:
        raise ValueError("referenced action is not a PLANNED assistance request")
    if not request.target_ref or request.target_ref == request.agent_id:
        raise ValueError("assistance request requires another explicit recipient")

    response = action_ledger.records.get(response_action_id)
    if response is None:
        raise KeyError(f"unknown assistance response action: {response_action_id}")
    if response.status != "PLANNED":
        raise ValueError("assistance response must remain PLANNED")
    if response.intent_kind not in SUPPORTED_RESPONSE_KINDS:
        raise ValueError("world action is not an assistance response")
    if response.intent_kind != ACCEPT_KIND:
        raise ValueError("only ACCEPT_ASSISTANCE_REQUEST can create an assistance commitment")
    if response.agent_id != request.target_ref or response.target_ref != request.agent_id:
        raise ValueError("assistance acceptance actor binding mismatch")
    if response.semantic_minute < request.semantic_minute:
        raise ValueError("assistance acceptance cannot predate its request")

    envelope = coordinator.information_queue.envelope_provenance(response_event_id)
    if envelope is None:
        raise KeyError(f"unknown assistance response event: {response_event_id}")
    if envelope.sender_id != response.agent_id or envelope.receiver_id != request.agent_id:
        raise ValueError("assistance acceptance envelope actor binding mismatch")
    if coordinator.information_queue.statuses.get(response_event_id) != DeliveryStatus.DELIVERED:
        raise ValueError("assistance commitment requires a terminal DELIVERED acceptance")

    sender_ledger = coordinator.information_queue.ledgers.get(response.agent_id)
    receiver_ledger = coordinator.information_queue.ledgers.get(request.agent_id)
    if sender_ledger is None or receiver_ledger is None:
        raise KeyError("acceptance participants require knowledge ledgers")
    source_claim = sender_ledger.claims.get(envelope.source_claim_id)
    received_claim = receiver_ledger.claims.get(envelope.new_claim_id)
    if source_claim is None or received_claim is None:
        raise ValueError("delivered acceptance lacks required claim lineage")
    expected_subject = f"assistance_response:{request.action_id}:{response.action_id}"
    if source_claim.subject != expected_subject or source_claim.value != ACCEPT_KIND:
        raise ValueError("assistance acceptance source claim mismatch")
    if source_claim.provenance_root != response.action_id or received_claim.provenance_root != response.action_id:
        raise ValueError("assistance acceptance lost response provenance")
    return request, response


def materialize_assistance_commitment(
    *,
    action_ledger: WorldActionIntentLedger,
    commitment_ledger: AssistanceCommitmentLedger,
    coordinator: GlobalNpcWorldEventCoordinator,
    request_action_id: str,
    response_action_id: str,
    response_event_id: str,
    commitment_id: str,
    intent_kind: str,
    materialized_minute: int,
    start_minute: int,
    end_minute: int,
    priority: int = 5,
    hard: bool = False,
    grace_minutes: int = 0,
    required_knowledge: frozenset[str] = frozenset(),
    required_permissions: frozenset[str] = frozenset(),
    requires_local_projection: bool = False,
    requires_structured_mechanics: bool = False,
) -> AssistanceCommitmentOutcome:
    """Turn a communicated ACCEPT into one explicit responder-owned time window.

    The commitment participates in the ordinary agenda. It does not move the
    responder, reserve a route or resource, complete assistance, or resolve PTU.
    """
    if not commitment_id or not intent_kind:
        raise ValueError("commitment_id and intent_kind are required")
    if min(materialized_minute, start_minute, end_minute, priority, grace_minutes) < 0:
        raise ValueError("commitment time/priority values must be non-negative")
    if end_minute < start_minute:
        raise ValueError("commitment end_minute cannot precede start_minute")
    if start_minute < materialized_minute:
        raise ValueError("assistance commitment cannot reserve a window in the past")

    request, response = _validate_delivered_acceptance(
        action_ledger=action_ledger,
        coordinator=coordinator,
        request_action_id=request_action_id,
        response_action_id=response_action_id,
        response_event_id=response_event_id,
    )
    if materialized_minute < response.semantic_minute:
        raise ValueError("assistance commitment cannot predate the acceptance")

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
        raise ValueError("agenda already contains conflicting assistance commitment")

    record = AssistanceCommitmentRecord(
        commitment_id=commitment_id,
        request_action_id=request.action_id,
        response_action_id=response.action_id,
        response_event_id=response_event_id,
        responder_id=response.agent_id,
        requester_id=request.agent_id,
        intent_kind=intent_kind,
        start_minute=start_minute,
        end_minute=end_minute,
        priority=priority,
        hard=hard,
        grace_minutes=grace_minutes,
        required_knowledge=tuple(sorted(required_knowledge)),
        required_permissions=tuple(sorted(required_permissions)),
        requires_local_projection=requires_local_projection,
        requires_structured_mechanics=requires_structured_mechanics,
        provenance_root=response.action_id,
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
    return AssistanceCommitmentOutcome(record=record, commitment=commitment)
