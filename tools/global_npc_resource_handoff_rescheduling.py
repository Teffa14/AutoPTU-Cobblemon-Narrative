from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from tools.global_npc_information_network import DeliveryStatus, InformationEventQueue
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
)
from tools.global_npc_resource_handoffs import (
    ResourceCustodyTransfer,
    ResourceHandoffAuthorization,
    ResourceHandoffLedger,
    ResourceHandoffResult,
    register_handoff_authorization,
)
from tools.global_npc_resources import WorldResource


class HandoffRescheduleDecisionKind(str, Enum):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"


class HandoffAuthorizationOperationalState(str, Enum):
    CURRENT = "CURRENT"
    SUPERSEDED = "SUPERSEDED"
    COMPLETED = "COMPLETED"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class ResourceHandoffRescheduleProposal:
    proposal_id: str
    authorization_id: str
    source_notice_id: str
    proposer_actor_id: str
    responder_actor_id: str
    proposed_location_ref: str
    proposed_valid_from_tick: int
    proposed_valid_until_tick: int | None
    created_tick: int

    def __post_init__(self) -> None:
        required = {
            "proposal_id": self.proposal_id,
            "authorization_id": self.authorization_id,
            "source_notice_id": self.source_notice_id,
            "proposer_actor_id": self.proposer_actor_id,
            "responder_actor_id": self.responder_actor_id,
            "proposed_location_ref": self.proposed_location_ref,
        }
        for name, value in required.items():
            if not value.strip():
                raise ValueError(f"{name} is required")
        if self.proposer_actor_id == self.responder_actor_id:
            raise ValueError("reschedule proposal requires distinct proposer and responder")
        if self.created_tick < 0 or self.proposed_valid_from_tick < 0:
            raise ValueError("ticks must be non-negative")
        if self.proposed_valid_until_tick is not None and self.proposed_valid_until_tick <= self.proposed_valid_from_tick:
            raise ValueError("proposed_valid_until_tick must be greater than proposed_valid_from_tick")


@dataclass(frozen=True)
class ResourceHandoffRescheduleDecision:
    decision_id: str
    proposal_id: str
    actor_id: str
    kind: HandoffRescheduleDecisionKind
    at_tick: int
    reason_ref: str | None = None

    def __post_init__(self) -> None:
        if not self.decision_id.strip():
            raise ValueError("decision_id is required")
        if not self.proposal_id.strip():
            raise ValueError("proposal_id is required")
        if not self.actor_id.strip():
            raise ValueError("actor_id is required")
        if self.at_tick < 0:
            raise ValueError("at_tick must be non-negative")


@dataclass(frozen=True)
class ResourceHandoffAuthorizationReplacement:
    replacement_id: str
    proposal_id: str
    decision_id: str
    superseded_authorization_id: str
    successor_authorization_id: str
    at_tick: int


@dataclass(frozen=True)
class ResourceHandoffRescheduleLedger:
    proposals: tuple[ResourceHandoffRescheduleProposal, ...] = ()
    decisions: tuple[ResourceHandoffRescheduleDecision, ...] = ()
    replacements: tuple[ResourceHandoffAuthorizationReplacement, ...] = ()


def _authorization_by_id(
    handoff_ledger: ResourceHandoffLedger,
    authorization_id: str,
) -> ResourceHandoffAuthorization | None:
    return next((item for item in handoff_ledger.authorizations if item.authorization_id == authorization_id), None)


def _notice_by_id(
    appointment_ledger: ResourceHandoffAppointmentLedger,
    notice_id: str,
):
    return next((item for item in appointment_ledger.notices if item.notice_id == notice_id), None)


def register_reschedule_proposal(
    ledger: ResourceHandoffRescheduleLedger,
    handoff_ledger: ResourceHandoffLedger,
    appointment_ledger: ResourceHandoffAppointmentLedger,
    proposal: ResourceHandoffRescheduleProposal,
) -> ResourceHandoffRescheduleLedger:
    if any(item.proposal_id == proposal.proposal_id for item in ledger.proposals):
        raise ValueError("duplicate handoff reschedule proposal id")
    authorization = _authorization_by_id(handoff_ledger, proposal.authorization_id)
    if authorization is None:
        raise ValueError("unknown handoff authorization")
    if any(item.authorization_id == proposal.authorization_id for item in handoff_ledger.transfers):
        raise ValueError("completed handoff authorization cannot be rescheduled")
    if any(item.superseded_authorization_id == proposal.authorization_id for item in ledger.replacements):
        raise ValueError("superseded handoff authorization cannot be rescheduled again")

    notice = _notice_by_id(appointment_ledger, proposal.source_notice_id)
    if notice is None:
        raise ValueError("unknown reschedule source notice")
    if notice.authorization_id != proposal.authorization_id:
        raise ValueError("reschedule source notice authorization mismatch")
    if notice.kind != HandoffAppointmentNoticeKind.RESCHEDULE_REQUEST:
        raise ValueError("reschedule proposal requires RESCHEDULE_REQUEST source notice")
    if notice.sender_actor_id != proposal.proposer_actor_id or notice.receiver_actor_id != proposal.responder_actor_id:
        raise ValueError("reschedule proposal actors must match source notice")
    if proposal.created_tick < notice.created_tick:
        raise ValueError("reschedule proposal cannot predate source notice")

    return ResourceHandoffRescheduleLedger(
        proposals=tuple(sorted((*ledger.proposals, proposal), key=lambda item: (item.created_tick, item.proposal_id))),
        decisions=ledger.decisions,
        replacements=ledger.replacements,
    )


def record_reschedule_decision(
    ledger: ResourceHandoffRescheduleLedger,
    appointment_ledger: ResourceHandoffAppointmentLedger,
    queue: InformationEventQueue,
    decision: ResourceHandoffRescheduleDecision,
) -> ResourceHandoffRescheduleLedger:
    if any(item.decision_id == decision.decision_id for item in ledger.decisions):
        raise ValueError("duplicate handoff reschedule decision id")
    proposal = next((item for item in ledger.proposals if item.proposal_id == decision.proposal_id), None)
    if proposal is None:
        raise ValueError("unknown handoff reschedule proposal")
    if any(item.proposal_id == proposal.proposal_id for item in ledger.decisions):
        raise ValueError("handoff reschedule proposal already decided")
    if decision.actor_id != proposal.responder_actor_id:
        raise ValueError("only proposal responder can decide reschedule")
    if decision.at_tick < proposal.created_tick:
        raise ValueError("reschedule decision cannot predate proposal")

    notice = _notice_by_id(appointment_ledger, proposal.source_notice_id)
    if notice is None:
        raise ValueError("unknown reschedule source notice")
    if queue.statuses.get(notice.communication_event_id) != DeliveryStatus.DELIVERED:
        raise ValueError("reschedule request was not delivered to responder")

    return ResourceHandoffRescheduleLedger(
        proposals=ledger.proposals,
        decisions=tuple(sorted((*ledger.decisions, decision), key=lambda item: (item.at_tick, item.decision_id))),
        replacements=ledger.replacements,
    )


def create_successor_authorization(
    ledger: ResourceHandoffRescheduleLedger,
    handoff_ledger: ResourceHandoffLedger,
    *,
    proposal_id: str,
    successor_authorization_id: str,
    replacement_id: str,
) -> tuple[ResourceHandoffRescheduleLedger, ResourceHandoffLedger, ResourceHandoffAuthorization]:
    if any(item.replacement_id == replacement_id for item in ledger.replacements):
        raise ValueError("duplicate handoff authorization replacement id")
    if any(item.successor_authorization_id == successor_authorization_id for item in ledger.replacements):
        raise ValueError("duplicate successor handoff authorization id")

    proposal = next((item for item in ledger.proposals if item.proposal_id == proposal_id), None)
    if proposal is None:
        raise ValueError("unknown handoff reschedule proposal")
    decision = next((item for item in ledger.decisions if item.proposal_id == proposal_id), None)
    if decision is None or decision.kind != HandoffRescheduleDecisionKind.ACCEPT:
        raise ValueError("reschedule proposal is not accepted")
    if any(item.proposal_id == proposal_id for item in ledger.replacements):
        raise ValueError("accepted reschedule already materialized")

    original = _authorization_by_id(handoff_ledger, proposal.authorization_id)
    if original is None:
        raise ValueError("unknown superseded handoff authorization")
    if any(item.authorization_id == original.authorization_id for item in handoff_ledger.transfers):
        raise ValueError("completed handoff authorization cannot be superseded")

    successor = ResourceHandoffAuthorization(
        authorization_id=successor_authorization_id,
        request_id=original.request_id,
        provider_actor_id=original.provider_actor_id,
        accountable_actor_id=original.accountable_actor_id,
        receiving_actor_id=original.receiving_actor_id,
        resource_id=original.resource_id,
        mode=original.mode,
        handoff_location_ref=proposal.proposed_location_ref,
        valid_from_tick=proposal.proposed_valid_from_tick,
        valid_until_tick=proposal.proposed_valid_until_tick,
        authority_ref=decision.decision_id,
    )
    updated_handoffs = register_handoff_authorization(handoff_ledger, successor)
    replacement = ResourceHandoffAuthorizationReplacement(
        replacement_id=replacement_id,
        proposal_id=proposal_id,
        decision_id=decision.decision_id,
        superseded_authorization_id=original.authorization_id,
        successor_authorization_id=successor.authorization_id,
        at_tick=decision.at_tick,
    )
    updated_reschedules = ResourceHandoffRescheduleLedger(
        proposals=ledger.proposals,
        decisions=ledger.decisions,
        replacements=tuple(sorted((*ledger.replacements, replacement), key=lambda item: (item.at_tick, item.replacement_id))),
    )
    return updated_reschedules, updated_handoffs, successor


def operational_authorization_state(
    ledger: ResourceHandoffRescheduleLedger,
    handoff_ledger: ResourceHandoffLedger,
    authorization_id: str,
) -> HandoffAuthorizationOperationalState:
    if _authorization_by_id(handoff_ledger, authorization_id) is None:
        return HandoffAuthorizationOperationalState.UNKNOWN
    if any(item.authorization_id == authorization_id for item in handoff_ledger.transfers):
        return HandoffAuthorizationOperationalState.COMPLETED
    if any(item.superseded_authorization_id == authorization_id for item in ledger.replacements):
        return HandoffAuthorizationOperationalState.SUPERSEDED
    return HandoffAuthorizationOperationalState.CURRENT


def current_authorization_id(
    ledger: ResourceHandoffRescheduleLedger,
    authorization_id: str,
) -> str:
    current = authorization_id
    seen: set[str] = set()
    while True:
        if current in seen:
            raise ValueError("handoff authorization replacement cycle")
        seen.add(current)
        replacement = next(
            (item for item in ledger.replacements if item.superseded_authorization_id == current),
            None,
        )
        if replacement is None:
            return current
        current = replacement.successor_authorization_id


def execute_current_authorized_handoff(
    reschedule_ledger: ResourceHandoffRescheduleLedger,
    handoff_ledger: ResourceHandoffLedger,
    resource: WorldResource,
    transfer: ResourceCustodyTransfer,
) -> ResourceHandoffResult:
    """Compatibility guard for the former unjournaled reschedule executor.

    A superseded authorization is still rejected with its historical reason code.
    A current authorization must use the holder-aware executor in
    global_npc_resource_handoff_rescheduling_holder so every successful holder
    mutation receives a ResourceHolderTransition.
    """
    current_id = current_authorization_id(reschedule_ledger, transfer.authorization_id)
    authorization = _authorization_by_id(handoff_ledger, transfer.authorization_id)
    if current_id != transfer.authorization_id:
        return ResourceHandoffResult(
            False,
            handoff_ledger,
            resource,
            authorization,
            reason_code="HANDOFF_AUTHORIZATION_SUPERSEDED",
        )
    return ResourceHandoffResult(
        False,
        handoff_ledger,
        resource,
        authorization,
        reason_code="HOLDER_TRANSITION_LEDGER_REQUIRED",
    )
