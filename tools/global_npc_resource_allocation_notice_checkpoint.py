from __future__ import annotations

from typing import Mapping

from tools.global_npc_resource_allocation_application import (
    AllocationApplicationKind,
    ResourceAllocationApplicationLedger,
)
from tools.global_npc_resource_allocation_application_checkpoint import (
    RESOURCE_CHECKPOINT_ALLOCATION_APPLICATION_SCHEMA,
    restore_resource_state_with_allocation_applications,
    snapshot_resource_state_with_allocation_applications,
)
from tools.global_npc_resource_allocation_notices import (
    ResourceAllocationNoticeLedger,
    ResourceAllocationNoticeLink,
    ResourceAllocationNoticeObligation,
)


RESOURCE_CHECKPOINT_ALLOCATION_NOTICE_SCHEMA = "OUROS_NPC_RESOURCE_CHECKPOINT_V9"


def snapshot_resource_state_with_allocation_notices(
    reservation_ledger,
    request_ledger,
    handoff_ledger,
    attempt_ledger,
    appointment_ledger,
    reschedule_ledger,
    admission_ledger,
    authority_evidence,
    resolution_ledger,
    application_ledger: ResourceAllocationApplicationLedger,
    notice_ledger: ResourceAllocationNoticeLedger,
) -> dict:
    """Persist Pass 350 notice ownership without taking over message delivery."""
    snapshot = snapshot_resource_state_with_allocation_applications(
        reservation_ledger,
        request_ledger,
        handoff_ledger,
        attempt_ledger,
        appointment_ledger,
        reschedule_ledger,
        admission_ledger,
        authority_evidence,
        resolution_ledger,
        application_ledger,
    )
    snapshot["schema"] = RESOURCE_CHECKPOINT_ALLOCATION_NOTICE_SCHEMA
    snapshot["allocation_notice_obligations"] = [
        {
            "obligation_id": row.obligation_id,
            "application_id": row.application_id,
            "resource_id": row.resource_id,
            "displaced_reservation_id": row.displaced_reservation_id,
            "affected_actor_id": row.affected_actor_id,
            "created_tick": row.created_tick,
            "basis_refs": list(row.basis_refs),
        }
        for row in sorted(notice_ledger.obligations, key=lambda item: (item.created_tick, item.obligation_id))
    ]
    snapshot["allocation_notice_links"] = [
        {
            "link_id": row.link_id,
            "obligation_id": row.obligation_id,
            "sender_actor_id": row.sender_actor_id,
            "communication_event_id": row.communication_event_id,
            "linked_tick": row.linked_tick,
        }
        for row in sorted(notice_ledger.links, key=lambda item: (item.linked_tick, item.link_id))
    ]
    return snapshot


def restore_resource_state_with_allocation_notices(snapshot: Mapping[str, object]):
    """Restore V9, or migrate V8-and-earlier with deliberately empty notice history."""
    schema = snapshot.get("schema")
    if schema != RESOURCE_CHECKPOINT_ALLOCATION_NOTICE_SCHEMA:
        base = restore_resource_state_with_allocation_applications(snapshot)
        return (*base, ResourceAllocationNoticeLedger())

    base_snapshot = dict(snapshot)
    base_snapshot["schema"] = RESOURCE_CHECKPOINT_ALLOCATION_APPLICATION_SCHEMA
    base_snapshot.pop("allocation_notice_obligations", None)
    base_snapshot.pop("allocation_notice_links", None)
    base = restore_resource_state_with_allocation_applications(base_snapshot)
    reservation_ledger = base[0]
    application_ledger = base[9]

    raw_obligations = snapshot.get("allocation_notice_obligations", [])
    raw_links = snapshot.get("allocation_notice_links", [])
    if not isinstance(raw_obligations, list) or not isinstance(raw_links, list):
        raise ValueError("allocation notice checkpoint collections must be lists")

    obligations = []
    for raw in raw_obligations:
        if not isinstance(raw, Mapping):
            raise ValueError("allocation notice obligation checkpoint row must be a mapping")
        basis = raw.get("basis_refs", [])
        if not isinstance(basis, list):
            raise ValueError("allocation notice obligation basis references must be a list")
        obligations.append(ResourceAllocationNoticeObligation(
            obligation_id=str(raw["obligation_id"]),
            application_id=str(raw["application_id"]),
            resource_id=str(raw["resource_id"]),
            displaced_reservation_id=str(raw["displaced_reservation_id"]),
            affected_actor_id=str(raw["affected_actor_id"]),
            created_tick=int(raw["created_tick"]),
            basis_refs=tuple(str(value) for value in basis),
        ))

    links = []
    for raw in raw_links:
        if not isinstance(raw, Mapping):
            raise ValueError("allocation notice link checkpoint row must be a mapping")
        links.append(ResourceAllocationNoticeLink(
            link_id=str(raw["link_id"]),
            obligation_id=str(raw["obligation_id"]),
            sender_actor_id=str(raw["sender_actor_id"]),
            communication_event_id=str(raw["communication_event_id"]),
            linked_tick=int(raw["linked_tick"]),
        ))

    notice_ledger = ResourceAllocationNoticeLedger(
        obligations=tuple(sorted(obligations, key=lambda item: item.obligation_id)),
        links=tuple(sorted(links, key=lambda item: item.link_id)),
    )
    _validate_allocation_notice_history(
        notice_ledger,
        application_ledger,
        reservation_ledger,
    )
    return (*base, notice_ledger)


def _validate_allocation_notice_history(notice_ledger, application_ledger, reservation_ledger) -> None:
    obligation_ids = [row.obligation_id for row in notice_ledger.obligations]
    if len(obligation_ids) != len(set(obligation_ids)):
        raise ValueError("resource checkpoint contains duplicate allocation notice obligation IDs")

    obligation_keys = [(row.application_id, row.displaced_reservation_id) for row in notice_ledger.obligations]
    if len(obligation_keys) != len(set(obligation_keys)):
        raise ValueError("resource checkpoint contains duplicate allocation notice application/reservation obligations")

    application_by_id = {row.application_id: row for row in application_ledger.applications}
    reservation_by_id = {row.reservation_id: row for row in reservation_ledger.reservations}

    for row in notice_ledger.obligations:
        application = application_by_id.get(row.application_id)
        if application is None:
            raise ValueError(f"allocation notice references missing application: {row.obligation_id}")
        if application.application_kind != AllocationApplicationKind.DISPLACE_CONFLICTING_RESERVATIONS:
            raise ValueError(f"allocation notice source application does not displace reservations: {row.obligation_id}")
        if row.resource_id != application.resource_id:
            raise ValueError(f"allocation notice resource mismatch: {row.obligation_id}")
        if row.displaced_reservation_id not in application.displaced_reservation_ids:
            raise ValueError(f"allocation notice reservation was not displaced by source application: {row.obligation_id}")
        reservation = reservation_by_id.get(row.displaced_reservation_id)
        if reservation is None:
            raise ValueError(f"allocation notice displaced reservation missing: {row.obligation_id}")
        if reservation.resource_id != row.resource_id:
            raise ValueError(f"allocation notice displaced reservation resource mismatch: {row.obligation_id}")
        if reservation.actor_id != row.affected_actor_id:
            raise ValueError(f"allocation notice affected actor mismatch: {row.obligation_id}")
        if row.created_tick < application.applied_tick:
            raise ValueError(f"allocation notice precedes source application: {row.obligation_id}")

    obligation_by_id = {row.obligation_id: row for row in notice_ledger.obligations}
    link_ids = [row.link_id for row in notice_ledger.links]
    if len(link_ids) != len(set(link_ids)):
        raise ValueError("resource checkpoint contains duplicate allocation notice link IDs")
    linked_obligation_ids = [row.obligation_id for row in notice_ledger.links]
    if len(linked_obligation_ids) != len(set(linked_obligation_ids)):
        raise ValueError("resource checkpoint links one allocation notice obligation more than once")
    communication_event_ids = [row.communication_event_id for row in notice_ledger.links]
    if len(communication_event_ids) != len(set(communication_event_ids)):
        raise ValueError("resource checkpoint reuses a communication event across allocation notices")

    for row in notice_ledger.links:
        obligation = obligation_by_id.get(row.obligation_id)
        if obligation is None:
            raise ValueError(f"allocation notice link references missing obligation: {row.link_id}")
        if row.linked_tick < obligation.created_tick:
            raise ValueError(f"allocation notice link precedes obligation: {row.link_id}")


def validate_allocation_notice_checkpoint_time(
    ledger: ResourceAllocationNoticeLedger,
    *,
    semantic_minute: int,
) -> None:
    for row in ledger.obligations:
        if row.created_tick > semantic_minute:
            raise ValueError(f"allocation notice obligation comes from the future: {row.obligation_id}")
    for row in ledger.links:
        if row.linked_tick > semantic_minute:
            raise ValueError(f"allocation notice link comes from the future: {row.link_id}")
