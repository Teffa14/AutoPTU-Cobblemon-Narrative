from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from tools.global_npc_information_network import DeliveryStatus, InformationEventQueue
from tools.global_npc_resource_handoffs import ResourceHandoffAuthorization, ResourceHandoffLedger


class HandoffAppointmentNoticeKind(str, Enum):
    CONFIRM = "CONFIRM"
    CANCEL = "CANCEL"
    RESCHEDULE_REQUEST = "RESCHEDULE_REQUEST"


class HandoffAppointmentCoordinationState(str, Enum):
    NO_UPDATE = "NO_UPDATE"
    PARTIAL_CONFIRMATION = "PARTIAL_CONFIRMATION"
    MUTUALLY_CONFIRMED = "MUTUALLY_CONFIRMED"
    RESCHEDULE_REQUESTED = "RESCHEDULE_REQUESTED"
    CANCELLATION_AUTHORED = "CANCELLATION_AUTHORED"
    CANCELLATION_DELIVERED = "CANCELLATION_DELIVERED"


@dataclass(frozen=True)
class ResourceHandoffAppointmentNotice:
    notice_id: str
    authorization_id: str
    sender_actor_id: str
    receiver_actor_id: str
    kind: HandoffAppointmentNoticeKind
    source_claim_id: str
    communication_event_id: str
    created_tick: int
    reason_ref: str | None = None

    def __post_init__(self) -> None:
        required = {
            "notice_id": self.notice_id,
            "authorization_id": self.authorization_id,
            "sender_actor_id": self.sender_actor_id,
            "receiver_actor_id": self.receiver_actor_id,
            "source_claim_id": self.source_claim_id,
            "communication_event_id": self.communication_event_id,
        }
        for name, value in required.items():
            if not value.strip():
                raise ValueError(f"{name} is required")
        if self.sender_actor_id == self.receiver_actor_id:
            raise ValueError("handoff appointment notice requires distinct sender and receiver")
        if self.created_tick < 0:
            raise ValueError("created_tick must be non-negative")


@dataclass(frozen=True)
class ResourceHandoffAppointmentLedger:
    notices: tuple[ResourceHandoffAppointmentNotice, ...] = ()


def _authorization_by_id(
    handoff_ledger: ResourceHandoffLedger,
    authorization_id: str,
) -> ResourceHandoffAuthorization | None:
    return next(
        (item for item in handoff_ledger.authorizations if item.authorization_id == authorization_id),
        None,
    )


def _participants(authorization: ResourceHandoffAuthorization) -> frozenset[str]:
    return frozenset(
        {
            authorization.provider_actor_id,
            authorization.receiving_actor_id,
            authorization.accountable_actor_id,
        }
    )


def register_handoff_appointment_notice(
    ledger: ResourceHandoffAppointmentLedger,
    handoff_ledger: ResourceHandoffLedger,
    notice: ResourceHandoffAppointmentNotice,
) -> ResourceHandoffAppointmentLedger:
    if any(item.notice_id == notice.notice_id for item in ledger.notices):
        raise ValueError("duplicate handoff appointment notice id")
    if any(item.communication_event_id == notice.communication_event_id for item in ledger.notices):
        raise ValueError("duplicate handoff appointment communication event id")

    authorization = _authorization_by_id(handoff_ledger, notice.authorization_id)
    if authorization is None:
        raise ValueError("unknown handoff authorization")
    if any(item.authorization_id == notice.authorization_id for item in handoff_ledger.transfers):
        raise ValueError("handoff authorization already completed")

    participants = _participants(authorization)
    if notice.sender_actor_id not in participants or notice.receiver_actor_id not in participants:
        raise ValueError("handoff appointment notice actors must be authorization participants")
    if authorization.valid_until_tick is not None and notice.created_tick >= authorization.valid_until_tick:
        raise ValueError("handoff appointment notice created after authorization expiry")

    return ResourceHandoffAppointmentLedger(
        notices=tuple(
            sorted(
                (*ledger.notices, notice),
                key=lambda item: (item.created_tick, item.notice_id),
            )
        )
    )


def notice_delivery_status(
    queue: InformationEventQueue,
    notice: ResourceHandoffAppointmentNotice,
) -> DeliveryStatus | None:
    return queue.statuses.get(notice.communication_event_id)


def notices_for_authorization(
    ledger: ResourceHandoffAppointmentLedger,
    authorization_id: str,
) -> tuple[ResourceHandoffAppointmentNotice, ...]:
    return tuple(
        item
        for item in ledger.notices
        if item.authorization_id == authorization_id
    )


def delivered_notices_for_actor(
    ledger: ResourceHandoffAppointmentLedger,
    queue: InformationEventQueue,
    authorization_id: str,
    actor_id: str,
) -> tuple[ResourceHandoffAppointmentNotice, ...]:
    return tuple(
        item
        for item in notices_for_authorization(ledger, authorization_id)
        if item.receiver_actor_id == actor_id
        and notice_delivery_status(queue, item) == DeliveryStatus.DELIVERED
    )


def known_notices_for_actor(
    ledger: ResourceHandoffAppointmentLedger,
    queue: InformationEventQueue,
    authorization_id: str,
    actor_id: str,
) -> tuple[ResourceHandoffAppointmentNotice, ...]:
    """Return authored notices plus notices actually delivered to this actor.

    Sending a notice is knowledge of one's own authored act. A notice addressed to an
    actor becomes available to that actor only after the existing information runtime
    reports DELIVERED. QUEUED, failed and local-ack-waiting events do not count.
    """
    matches = []
    for item in notices_for_authorization(ledger, authorization_id):
        if item.sender_actor_id == actor_id:
            matches.append(item)
        elif item.receiver_actor_id == actor_id and notice_delivery_status(queue, item) == DeliveryStatus.DELIVERED:
            matches.append(item)
    return tuple(sorted(matches, key=lambda item: (item.created_tick, item.notice_id)))


def coordination_state(
    ledger: ResourceHandoffAppointmentLedger,
    queue: InformationEventQueue,
    handoff_ledger: ResourceHandoffLedger,
    authorization_id: str,
) -> HandoffAppointmentCoordinationState | None:
    authorization = _authorization_by_id(handoff_ledger, authorization_id)
    if authorization is None:
        return None

    notices = notices_for_authorization(ledger, authorization_id)
    cancellations = [item for item in notices if item.kind == HandoffAppointmentNoticeKind.CANCEL]
    if cancellations:
        if any(notice_delivery_status(queue, item) == DeliveryStatus.DELIVERED for item in cancellations):
            return HandoffAppointmentCoordinationState.CANCELLATION_DELIVERED
        return HandoffAppointmentCoordinationState.CANCELLATION_AUTHORED

    reschedules = [item for item in notices if item.kind == HandoffAppointmentNoticeKind.RESCHEDULE_REQUEST]
    if reschedules:
        return HandoffAppointmentCoordinationState.RESCHEDULE_REQUESTED

    provider = authorization.provider_actor_id
    recipient = authorization.receiving_actor_id
    provider_confirmed_to_recipient = any(
        item.kind == HandoffAppointmentNoticeKind.CONFIRM
        and item.sender_actor_id == provider
        and item.receiver_actor_id == recipient
        and notice_delivery_status(queue, item) == DeliveryStatus.DELIVERED
        for item in notices
    )
    recipient_confirmed_to_provider = any(
        item.kind == HandoffAppointmentNoticeKind.CONFIRM
        and item.sender_actor_id == recipient
        and item.receiver_actor_id == provider
        and notice_delivery_status(queue, item) == DeliveryStatus.DELIVERED
        for item in notices
    )
    if provider_confirmed_to_recipient and recipient_confirmed_to_provider:
        return HandoffAppointmentCoordinationState.MUTUALLY_CONFIRMED
    if provider_confirmed_to_recipient or recipient_confirmed_to_provider:
        return HandoffAppointmentCoordinationState.PARTIAL_CONFIRMATION
    return HandoffAppointmentCoordinationState.NO_UPDATE


def actors_unaware_of_authored_cancellation(
    ledger: ResourceHandoffAppointmentLedger,
    queue: InformationEventQueue,
    handoff_ledger: ResourceHandoffLedger,
    authorization_id: str,
) -> tuple[str, ...]:
    """Find participants who have not authored or received any current cancellation notice."""
    authorization = _authorization_by_id(handoff_ledger, authorization_id)
    if authorization is None:
        return ()
    cancellations = tuple(
        item
        for item in notices_for_authorization(ledger, authorization_id)
        if item.kind == HandoffAppointmentNoticeKind.CANCEL
    )
    if not cancellations:
        return ()

    unaware: list[str] = []
    for actor_id in sorted(_participants(authorization)):
        actor_knows = any(
            item.sender_actor_id == actor_id
            or (
                item.receiver_actor_id == actor_id
                and notice_delivery_status(queue, item) == DeliveryStatus.DELIVERED
            )
            for item in cancellations
        )
        if not actor_knows:
            unaware.append(actor_id)
    return tuple(unaware)
