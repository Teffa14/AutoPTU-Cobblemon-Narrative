from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from tools.global_npc_resource_handoffs import (
    ResourceCustodyTransfer,
    ResourceHandoffLedger,
    ResourceHandoffResult,
    execute_authorized_handoff,
)
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    active_reservations_for_resource,
    checkout_reserved_resource,
    return_resource,
)
from tools.global_npc_resources import WorldResource


class HolderTransitionKind(str, Enum):
    CHECKOUT = "CHECKOUT"
    RETURN = "RETURN"
    HANDOFF = "HANDOFF"


@dataclass(frozen=True)
class ResourceHolderTransition:
    transition_id: str
    resource_id: str
    kind: HolderTransitionKind
    from_actor_id: str | None
    to_actor_id: str | None
    at_tick: int
    location_ref: str | None = None
    source_ref: str | None = None

    def __post_init__(self) -> None:
        if not self.transition_id.strip():
            raise ValueError("transition_id is required")
        if not self.resource_id.strip():
            raise ValueError("resource_id is required")
        if isinstance(self.at_tick, bool) or not isinstance(self.at_tick, int):
            raise ValueError("at_tick must be an integer")
        if self.at_tick < 0:
            raise ValueError("at_tick must be non-negative")
        if self.location_ref is not None and not self.location_ref.strip():
            raise ValueError("location_ref cannot be blank")
        if self.source_ref is not None and not self.source_ref.strip():
            raise ValueError("source_ref cannot be blank")

        if self.kind == HolderTransitionKind.CHECKOUT:
            if self.from_actor_id is not None or self.to_actor_id is None:
                raise ValueError("checkout must transition from no holder to one actor")
        elif self.kind == HolderTransitionKind.RETURN:
            if self.from_actor_id is None or self.to_actor_id is not None:
                raise ValueError("return must transition from one actor to no holder")
        elif self.kind == HolderTransitionKind.HANDOFF:
            if self.from_actor_id is None or self.to_actor_id is None:
                raise ValueError("handoff requires from_actor_id and to_actor_id")
            if self.from_actor_id == self.to_actor_id:
                raise ValueError("handoff requires distinct actors")


@dataclass(frozen=True)
class ResourceHolderTransitionLedger:
    transitions: tuple[ResourceHolderTransition, ...] = ()


def holder_history(
    ledger: ResourceHolderTransitionLedger,
    resource_id: str,
    *,
    through_tick: int | None = None,
) -> tuple[ResourceHolderTransition, ...]:
    items = (
        transition
        for transition in ledger.transitions
        if transition.resource_id == resource_id
        and (through_tick is None or transition.at_tick <= through_tick)
    )
    return tuple(sorted(items, key=lambda item: (item.at_tick, item.transition_id)))


def record_holder_transition(
    ledger: ResourceHolderTransitionLedger,
    transition: ResourceHolderTransition,
) -> ResourceHolderTransitionLedger:
    if any(
        existing.transition_id == transition.transition_id
        for existing in ledger.transitions
    ):
        raise ValueError("duplicate holder transition id")

    history = holder_history(ledger, transition.resource_id)
    if history:
        latest = history[-1]
        if transition.at_tick <= latest.at_tick:
            raise ValueError("holder transitions require strictly increasing semantic order")
        if transition.from_actor_id != latest.to_actor_id:
            raise ValueError("holder transition breaks resource holder continuity")

    return ResourceHolderTransitionLedger(
        transitions=tuple(
            sorted(
                (*ledger.transitions, transition),
                key=lambda item: (item.at_tick, item.transition_id),
            )
        )
    )


def checkout_with_holder_transition(
    resource: WorldResource,
    reservation_ledger: ReservationLedger,
    holder_ledger: ResourceHolderTransitionLedger,
    *,
    actor_id: str,
    at_tick: int,
    transition_id: str,
) -> tuple[WorldResource, ResourceHolderTransitionLedger, ResourceHolderTransition]:
    if resource.holder_actor_id is not None:
        raise ValueError("journaled checkout requires an unheld resource")

    active = active_reservations_for_resource(
        reservation_ledger,
        resource.resource_id,
        at_tick,
    )
    if len(active) != 1 or active[0].actor_id != actor_id:
        raise ValueError("actor lacks an active reservation for this resource")

    updated_resource = checkout_reserved_resource(
        resource,
        reservation_ledger,
        actor_id,
        at_tick,
    )
    transition = ResourceHolderTransition(
        transition_id=transition_id,
        resource_id=resource.resource_id,
        kind=HolderTransitionKind.CHECKOUT,
        from_actor_id=None,
        to_actor_id=actor_id,
        at_tick=at_tick,
        location_ref=updated_resource.location_ref,
        source_ref=active[0].reservation_id,
    )
    updated_ledger = record_holder_transition(holder_ledger, transition)
    return updated_resource, updated_ledger, transition


def return_with_holder_transition(
    resource: WorldResource,
    holder_ledger: ResourceHolderTransitionLedger,
    *,
    actor_id: str,
    return_location_ref: str,
    at_tick: int,
    transition_id: str,
    source_ref: str | None = None,
) -> tuple[WorldResource, ResourceHolderTransitionLedger, ResourceHolderTransition]:
    updated_resource = return_resource(resource, actor_id, return_location_ref)
    transition = ResourceHolderTransition(
        transition_id=transition_id,
        resource_id=resource.resource_id,
        kind=HolderTransitionKind.RETURN,
        from_actor_id=actor_id,
        to_actor_id=None,
        at_tick=at_tick,
        location_ref=return_location_ref,
        source_ref=source_ref,
    )
    updated_ledger = record_holder_transition(holder_ledger, transition)
    return updated_resource, updated_ledger, transition


@dataclass(frozen=True)
class HolderAwareHandoffResult:
    handoff: ResourceHandoffResult
    holder_ledger: ResourceHolderTransitionLedger
    holder_transition: ResourceHolderTransition | None = None


def execute_handoff_with_holder_transition(
    handoff_ledger: ResourceHandoffLedger,
    holder_ledger: ResourceHolderTransitionLedger,
    resource: WorldResource,
    transfer: ResourceCustodyTransfer,
    *,
    transition_id: str,
) -> HolderAwareHandoffResult:
    result = execute_authorized_handoff(handoff_ledger, resource, transfer)
    if not result.accepted or result.transfer is None:
        return HolderAwareHandoffResult(result, holder_ledger)

    transition = ResourceHolderTransition(
        transition_id=transition_id,
        resource_id=transfer.resource_id,
        kind=HolderTransitionKind.HANDOFF,
        from_actor_id=transfer.from_actor_id,
        to_actor_id=transfer.to_actor_id,
        at_tick=transfer.at_tick,
        location_ref=transfer.location_ref,
        source_ref=transfer.transfer_id,
    )
    updated_ledger = record_holder_transition(holder_ledger, transition)
    return HolderAwareHandoffResult(result, updated_ledger, transition)
