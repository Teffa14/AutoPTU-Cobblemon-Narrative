from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from tools.global_npc_information_network import DeliveryStatus, InformationEventQueue
from tools.global_npc_resource_allocation_application import (
    AllocationApplicationKind,
    ResourceAllocationApplication,
)
from tools.global_npc_resource_reservations import ReservationLedger


class AllocationNoticeState(str, Enum):
    REQUIRED = "REQUIRED"
    QUEUED = "QUEUED"
    WAITING_LOCAL_ACK = "WAITING_LOCAL_ACK"
    DELIVERED = "DELIVERED"
    DELIVERY_FAILED = "DELIVERY_FAILED"


@dataclass(frozen=True)
class ResourceAllocationNoticeObligation:
    obligation_id: str
    application_id: str
    resource_id: str
    displaced_reservation_id: str
    affected_actor_id: str
    created_tick: int
    basis_refs: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for name, value in {
            "obligation_id": self.obligation_id,
            "application_id": self.application_id,
            "resource_id": self.resource_id,
            "displaced_reservation_id": self.displaced_reservation_id,
            "affected_actor_id": self.affected_actor_id,
        }.items():
            if not value.strip():
                raise ValueError(f"{name} is required")
        if self.created_tick < 0:
            raise ValueError("created_tick must be non-negative")


@dataclass(frozen=True)
class ResourceAllocationNoticeLink:
    link_id: str
    obligation_id: str
    sender_actor_id: str
    communication_event_id: str
    linked_tick: int

    def __post_init__(self) -> None:
        for name, value in {
            "link_id": self.link_id,
            "obligation_id": self.obligation_id,
            "sender_actor_id": self.sender_actor_id,
            "communication_event_id": self.communication_event_id,
        }.items():
            if not value.strip():
                raise ValueError(f"{name} is required")
        if self.linked_tick < 0:
            raise ValueError("linked_tick must be non-negative")


@dataclass(frozen=True)
class ResourceAllocationNoticeLedger:
    obligations: tuple[ResourceAllocationNoticeObligation, ...] = ()
    links: tuple[ResourceAllocationNoticeLink, ...] = ()


def derive_displacement_notice_obligations(
    ledger: ResourceAllocationNoticeLedger,
    application: ResourceAllocationApplication,
    reservations: ReservationLedger,
    *,
    obligation_id_prefix: str,
    created_tick: int,
    basis_refs: tuple[str, ...] = (),
) -> ResourceAllocationNoticeLedger:
    """Create one auditable notice obligation per displaced reservation.

    This records who is affected by Pass 349. It does not author, send, deliver,
    interpret, or acknowledge a message.
    """
    if application.application_kind != AllocationApplicationKind.DISPLACE_CONFLICTING_RESERVATIONS:
        raise ValueError("allocation application does not displace reservations")
    if created_tick < application.applied_tick:
        raise ValueError("notice obligation cannot precede allocation application")
    if not obligation_id_prefix.strip():
        raise ValueError("obligation_id_prefix is required")

    reservation_map = {item.reservation_id: item for item in reservations.reservations}
    existing_keys = {
        (item.application_id, item.displaced_reservation_id)
        for item in ledger.obligations
    }
    additions: list[ResourceAllocationNoticeObligation] = []
    for reservation_id in sorted(application.displaced_reservation_ids):
        reservation = reservation_map.get(reservation_id)
        if reservation is None:
            raise ValueError("displaced reservation is missing from source ledger")
        if reservation.resource_id != application.resource_id:
            raise ValueError("displaced reservation resource mismatch")
        key = (application.application_id, reservation_id)
        if key in existing_keys:
            raise ValueError("notice obligation already exists for displaced reservation")
        additions.append(
            ResourceAllocationNoticeObligation(
                obligation_id=f"{obligation_id_prefix}:{reservation_id}",
                application_id=application.application_id,
                resource_id=application.resource_id,
                displaced_reservation_id=reservation_id,
                affected_actor_id=reservation.actor_id,
                created_tick=created_tick,
                basis_refs=tuple(basis_refs),
            )
        )

    all_obligations = (*ledger.obligations, *additions)
    ids = [item.obligation_id for item in all_obligations]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate allocation notice obligation id")
    return ResourceAllocationNoticeLedger(
        obligations=tuple(sorted(all_obligations, key=lambda item: item.obligation_id)),
        links=ledger.links,
    )


def link_notice_communication(
    ledger: ResourceAllocationNoticeLedger,
    queue: InformationEventQueue,
    link: ResourceAllocationNoticeLink,
) -> ResourceAllocationNoticeLedger:
    obligation = next((item for item in ledger.obligations if item.obligation_id == link.obligation_id), None)
    if obligation is None:
        raise ValueError("unknown allocation notice obligation")
    if link.linked_tick < obligation.created_tick:
        raise ValueError("communication link cannot precede notice obligation")
    if link.communication_event_id not in queue.statuses:
        raise ValueError("unknown communication event")
    if any(item.link_id == link.link_id for item in ledger.links):
        raise ValueError("duplicate allocation notice link id")
    if any(item.obligation_id == link.obligation_id for item in ledger.links):
        raise ValueError("notice obligation already has a communication link")
    if any(item.communication_event_id == link.communication_event_id for item in ledger.links):
        raise ValueError("communication event already linked to an allocation notice")

    envelope = queue.envelope_provenance(link.communication_event_id)
    if envelope is None:
        raise ValueError("communication envelope provenance unavailable for notice binding")
    if link.linked_tick < envelope.created_minute:
        raise ValueError("communication link cannot precede authored communication")
    if envelope.sender_id != link.sender_actor_id:
        raise ValueError("notice sender does not match communication sender")
    if envelope.receiver_id != obligation.affected_actor_id:
        raise ValueError("notice receiver does not match affected reservation holder")

    return ResourceAllocationNoticeLedger(
        obligations=ledger.obligations,
        links=tuple(sorted((*ledger.links, link), key=lambda item: item.link_id)),
    )


def notice_state(
    ledger: ResourceAllocationNoticeLedger,
    queue: InformationEventQueue,
    obligation_id: str,
) -> AllocationNoticeState | None:
    obligation = next((item for item in ledger.obligations if item.obligation_id == obligation_id), None)
    if obligation is None:
        return None
    link = next((item for item in ledger.links if item.obligation_id == obligation_id), None)
    if link is None:
        return AllocationNoticeState.REQUIRED
    status = queue.statuses.get(link.communication_event_id)
    if status == DeliveryStatus.DELIVERED:
        return AllocationNoticeState.DELIVERED
    if status == DeliveryStatus.WAITING_LOCAL_ACK:
        return AllocationNoticeState.WAITING_LOCAL_ACK
    if status == DeliveryStatus.QUEUED:
        return AllocationNoticeState.QUEUED
    return AllocationNoticeState.DELIVERY_FAILED


def outstanding_notice_obligations(
    ledger: ResourceAllocationNoticeLedger,
    queue: InformationEventQueue,
) -> tuple[ResourceAllocationNoticeObligation, ...]:
    return tuple(
        item
        for item in sorted(ledger.obligations, key=lambda value: value.obligation_id)
        if notice_state(ledger, queue, item.obligation_id) != AllocationNoticeState.DELIVERED
    )
