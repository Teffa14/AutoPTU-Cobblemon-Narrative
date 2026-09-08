from __future__ import annotations

from typing import Mapping

from tools.global_npc_resource_appointment_checkpoint import (
    RESOURCE_CHECKPOINT_APPOINTMENT_SCHEMA,
    restore_resource_state_with_appointment_notices,
    snapshot_resource_state_with_appointment_notices,
)
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
)
from tools.global_npc_resource_handoff_attempts import ResourceHandoffAttemptLedger
from tools.global_npc_resource_handoff_rescheduling import (
    HandoffRescheduleDecisionKind,
    ResourceHandoffAuthorizationReplacement,
    ResourceHandoffRescheduleDecision,
    ResourceHandoffRescheduleLedger,
    ResourceHandoffRescheduleProposal,
    current_authorization_id,
)
from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_requests import ResourceRequestLedger
from tools.global_npc_resource_reservations import ReservationLedger


RESOURCE_CHECKPOINT_RESCHEDULE_SCHEMA = "OUROS_NPC_RESOURCE_CHECKPOINT_V5"


def snapshot_resource_state_with_reschedules(
    reservation_ledger: ReservationLedger,
    request_ledger: ResourceRequestLedger,
    handoff_ledger: ResourceHandoffLedger,
    attempt_ledger: ResourceHandoffAttemptLedger,
    appointment_ledger: ResourceHandoffAppointmentLedger,
    reschedule_ledger: ResourceHandoffRescheduleLedger,
) -> dict:
    """Serialize Pass 339/342/343/344/345 state plus Pass 346 reschedule history."""
    snapshot = snapshot_resource_state_with_appointment_notices(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
    )
    snapshot["schema"] = RESOURCE_CHECKPOINT_RESCHEDULE_SCHEMA
    snapshot["handoff_reschedule_proposals"] = [
        {
            "proposal_id": row.proposal_id,
            "authorization_id": row.authorization_id,
            "source_notice_id": row.source_notice_id,
            "proposer_actor_id": row.proposer_actor_id,
            "responder_actor_id": row.responder_actor_id,
            "proposed_location_ref": row.proposed_location_ref,
            "proposed_valid_from_tick": row.proposed_valid_from_tick,
            "proposed_valid_until_tick": row.proposed_valid_until_tick,
            "created_tick": row.created_tick,
        }
        for row in sorted(reschedule_ledger.proposals, key=lambda item: (item.created_tick, item.proposal_id))
    ]
    snapshot["handoff_reschedule_decisions"] = [
        {
            "decision_id": row.decision_id,
            "proposal_id": row.proposal_id,
            "actor_id": row.actor_id,
            "kind": row.kind.value,
            "at_tick": row.at_tick,
            "reason_ref": row.reason_ref,
        }
        for row in sorted(reschedule_ledger.decisions, key=lambda item: (item.at_tick, item.decision_id))
    ]
    snapshot["handoff_authorization_replacements"] = [
        {
            "replacement_id": row.replacement_id,
            "proposal_id": row.proposal_id,
            "decision_id": row.decision_id,
            "superseded_authorization_id": row.superseded_authorization_id,
            "successor_authorization_id": row.successor_authorization_id,
            "at_tick": row.at_tick,
        }
        for row in sorted(reschedule_ledger.replacements, key=lambda item: (item.at_tick, item.replacement_id))
    ]
    return snapshot


def restore_resource_state_with_reschedules(
    snapshot: Mapping[str, object],
) -> tuple[
    ReservationLedger,
    ResourceRequestLedger,
    ResourceHandoffLedger,
    ResourceHandoffAttemptLedger,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffRescheduleLedger,
]:
    """Restore V5 reschedule history; V1-V4 return an explicit empty reschedule ledger."""
    schema = snapshot.get("schema")
    if schema != RESOURCE_CHECKPOINT_RESCHEDULE_SCHEMA:
        reservations, requests, handoffs, attempts, appointments = restore_resource_state_with_appointment_notices(snapshot)
        return reservations, requests, handoffs, attempts, appointments, ResourceHandoffRescheduleLedger()

    base_snapshot = dict(snapshot)
    base_snapshot["schema"] = RESOURCE_CHECKPOINT_APPOINTMENT_SCHEMA
    base_snapshot.pop("handoff_reschedule_proposals", None)
    base_snapshot.pop("handoff_reschedule_decisions", None)
    base_snapshot.pop("handoff_authorization_replacements", None)
    reservations, requests, handoffs, attempts, appointments = restore_resource_state_with_appointment_notices(base_snapshot)

    raw_proposals = snapshot.get("handoff_reschedule_proposals", [])
    raw_decisions = snapshot.get("handoff_reschedule_decisions", [])
    raw_replacements = snapshot.get("handoff_authorization_replacements", [])
    for collection, label in (
        (raw_proposals, "handoff reschedule proposal"),
        (raw_decisions, "handoff reschedule decision"),
        (raw_replacements, "handoff authorization replacement"),
    ):
        if not isinstance(collection, list):
            raise ValueError(f"{label} checkpoint collection must be a list")

    proposals = tuple(
        ResourceHandoffRescheduleProposal(
            proposal_id=str(raw["proposal_id"]),
            authorization_id=str(raw["authorization_id"]),
            source_notice_id=str(raw["source_notice_id"]),
            proposer_actor_id=str(raw["proposer_actor_id"]),
            responder_actor_id=str(raw["responder_actor_id"]),
            proposed_location_ref=str(raw["proposed_location_ref"]),
            proposed_valid_from_tick=int(raw["proposed_valid_from_tick"]),
            proposed_valid_until_tick=None if raw.get("proposed_valid_until_tick") is None else int(raw["proposed_valid_until_tick"]),
            created_tick=int(raw["created_tick"]),
        )
        for raw in _mapping_rows(raw_proposals, "handoff reschedule proposal")
    )
    decisions = tuple(
        ResourceHandoffRescheduleDecision(
            decision_id=str(raw["decision_id"]),
            proposal_id=str(raw["proposal_id"]),
            actor_id=str(raw["actor_id"]),
            kind=HandoffRescheduleDecisionKind(str(raw["kind"])),
            at_tick=int(raw["at_tick"]),
            reason_ref=None if raw.get("reason_ref") is None else str(raw["reason_ref"]),
        )
        for raw in _mapping_rows(raw_decisions, "handoff reschedule decision")
    )
    replacements = tuple(
        ResourceHandoffAuthorizationReplacement(
            replacement_id=str(raw["replacement_id"]),
            proposal_id=str(raw["proposal_id"]),
            decision_id=str(raw["decision_id"]),
            superseded_authorization_id=str(raw["superseded_authorization_id"]),
            successor_authorization_id=str(raw["successor_authorization_id"]),
            at_tick=int(raw["at_tick"]),
        )
        for raw in _mapping_rows(raw_replacements, "handoff authorization replacement")
    )

    ledger = ResourceHandoffRescheduleLedger(
        proposals=tuple(sorted(proposals, key=lambda item: (item.created_tick, item.proposal_id))),
        decisions=tuple(sorted(decisions, key=lambda item: (item.at_tick, item.decision_id))),
        replacements=tuple(sorted(replacements, key=lambda item: (item.at_tick, item.replacement_id))),
    )
    _validate_reschedule_history(ledger, handoffs, appointments)
    return reservations, requests, handoffs, attempts, appointments, ledger


def _mapping_rows(raw_rows: list, label: str) -> list[Mapping[str, object]]:
    rows: list[Mapping[str, object]] = []
    for raw in raw_rows:
        if not isinstance(raw, Mapping):
            raise ValueError(f"{label} checkpoint row must be a mapping")
        rows.append(raw)
    return rows


def _validate_reschedule_history(
    ledger: ResourceHandoffRescheduleLedger,
    handoffs: ResourceHandoffLedger,
    appointments: ResourceHandoffAppointmentLedger,
) -> None:
    proposal_ids = [row.proposal_id for row in ledger.proposals]
    decision_ids = [row.decision_id for row in ledger.decisions]
    replacement_ids = [row.replacement_id for row in ledger.replacements]
    successor_ids = [row.successor_authorization_id for row in ledger.replacements]
    superseded_ids = [row.superseded_authorization_id for row in ledger.replacements]
    for values, label in (
        (proposal_ids, "handoff reschedule proposal"),
        (decision_ids, "handoff reschedule decision"),
        (replacement_ids, "handoff authorization replacement"),
        (successor_ids, "successor handoff authorization"),
        (superseded_ids, "superseded handoff authorization"),
    ):
        if len(set(values)) != len(values):
            raise ValueError(f"resource checkpoint contains duplicate {label} IDs")

    authorizations = {row.authorization_id: row for row in handoffs.authorizations}
    notices = {row.notice_id: row for row in appointments.notices}
    transfers = {row.authorization_id: row for row in handoffs.transfers}
    proposals = {row.proposal_id: row for row in ledger.proposals}
    decisions_by_proposal: dict[str, ResourceHandoffRescheduleDecision] = {}

    for proposal in ledger.proposals:
        authorization = authorizations.get(proposal.authorization_id)
        notice = notices.get(proposal.source_notice_id)
        if authorization is None:
            raise ValueError(f"reschedule proposal references missing authorization: {proposal.proposal_id}")
        if notice is None:
            raise ValueError(f"reschedule proposal references missing source notice: {proposal.proposal_id}")
        if notice.authorization_id != proposal.authorization_id or notice.kind != HandoffAppointmentNoticeKind.RESCHEDULE_REQUEST:
            raise ValueError(f"reschedule proposal source notice mismatch: {proposal.proposal_id}")
        if notice.sender_actor_id != proposal.proposer_actor_id or notice.receiver_actor_id != proposal.responder_actor_id:
            raise ValueError(f"reschedule proposal actor mismatch: {proposal.proposal_id}")
        if proposal.created_tick < notice.created_tick:
            raise ValueError(f"reschedule proposal predates source notice: {proposal.proposal_id}")
        transfer = transfers.get(proposal.authorization_id)
        if transfer is not None and proposal.created_tick >= transfer.at_tick:
            raise ValueError(f"reschedule proposal occurs after completed transfer: {proposal.proposal_id}")

    for decision in ledger.decisions:
        proposal = proposals.get(decision.proposal_id)
        if proposal is None:
            raise ValueError(f"reschedule decision references missing proposal: {decision.decision_id}")
        if decision.proposal_id in decisions_by_proposal:
            raise ValueError(f"reschedule proposal has multiple decisions: {decision.proposal_id}")
        if decision.actor_id != proposal.responder_actor_id:
            raise ValueError(f"reschedule decision actor mismatch: {decision.decision_id}")
        if decision.at_tick < proposal.created_tick:
            raise ValueError(f"reschedule decision predates proposal: {decision.decision_id}")
        decisions_by_proposal[decision.proposal_id] = decision

    for replacement in ledger.replacements:
        proposal = proposals.get(replacement.proposal_id)
        decision = decisions_by_proposal.get(replacement.proposal_id)
        original = authorizations.get(replacement.superseded_authorization_id)
        successor = authorizations.get(replacement.successor_authorization_id)
        if proposal is None or decision is None:
            raise ValueError(f"authorization replacement references incomplete reschedule history: {replacement.replacement_id}")
        if decision.kind != HandoffRescheduleDecisionKind.ACCEPT or replacement.decision_id != decision.decision_id:
            raise ValueError(f"authorization replacement lacks matching acceptance: {replacement.replacement_id}")
        if replacement.superseded_authorization_id != proposal.authorization_id:
            raise ValueError(f"authorization replacement superseded ID mismatch: {replacement.replacement_id}")
        if replacement.at_tick != decision.at_tick:
            raise ValueError(f"authorization replacement timestamp mismatch: {replacement.replacement_id}")
        if original is None or successor is None:
            raise ValueError(f"authorization replacement references missing authorization: {replacement.replacement_id}")
        if transfers.get(original.authorization_id) is not None:
            raise ValueError(f"completed authorization cannot be superseded: {replacement.replacement_id}")
        expected = (
            original.request_id,
            original.provider_actor_id,
            original.accountable_actor_id,
            original.receiving_actor_id,
            original.resource_id,
            original.mode,
            proposal.proposed_location_ref,
            proposal.proposed_valid_from_tick,
            proposal.proposed_valid_until_tick,
            decision.decision_id,
        )
        actual = (
            successor.request_id,
            successor.provider_actor_id,
            successor.accountable_actor_id,
            successor.receiving_actor_id,
            successor.resource_id,
            successor.mode,
            successor.handoff_location_ref,
            successor.valid_from_tick,
            successor.valid_until_tick,
            successor.authority_ref,
        )
        if actual != expected:
            raise ValueError(f"successor authorization does not match accepted reschedule: {replacement.replacement_id}")

    for replacement in ledger.replacements:
        current_authorization_id(ledger, replacement.superseded_authorization_id)


def validate_reschedule_checkpoint_time(
    ledger: ResourceHandoffRescheduleLedger,
    *,
    semantic_minute: int,
) -> None:
    """Completed proposal/decision/replacement records cannot originate after the restored world time."""
    for proposal in ledger.proposals:
        if proposal.created_tick > semantic_minute:
            raise ValueError(f"handoff reschedule proposal comes from the future: {proposal.proposal_id}")
    for decision in ledger.decisions:
        if decision.at_tick > semantic_minute:
            raise ValueError(f"handoff reschedule decision comes from the future: {decision.decision_id}")
    for replacement in ledger.replacements:
        if replacement.at_tick > semantic_minute:
            raise ValueError(f"handoff authorization replacement comes from the future: {replacement.replacement_id}")
