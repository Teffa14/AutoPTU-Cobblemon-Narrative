from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Iterable

from tools.global_npc_resource_requests import (
    ResourceRequestLedger,
    ResourceRequestState,
    request_view,
)
from tools.global_npc_resources import WorldResource


class HandoffMode(str, Enum):
    PICKUP = "PICKUP"
    DELIVERY = "DELIVERY"


@dataclass(frozen=True)
class ResourceHandoffAuthorization:
    authorization_id: str
    request_id: str
    provider_actor_id: str
    accountable_actor_id: str
    receiving_actor_id: str
    resource_id: str
    mode: HandoffMode
    handoff_location_ref: str
    valid_from_tick: int
    valid_until_tick: int | None = None
    authority_ref: str | None = None

    def __post_init__(self) -> None:
        required = {
            "authorization_id": self.authorization_id,
            "request_id": self.request_id,
            "provider_actor_id": self.provider_actor_id,
            "accountable_actor_id": self.accountable_actor_id,
            "receiving_actor_id": self.receiving_actor_id,
            "resource_id": self.resource_id,
            "handoff_location_ref": self.handoff_location_ref,
        }
        for name, value in required.items():
            if not value.strip():
                raise ValueError(f"{name} is required")
        if self.valid_from_tick < 0:
            raise ValueError("valid_from_tick must be non-negative")
        if self.valid_until_tick is not None and self.valid_until_tick <= self.valid_from_tick:
            raise ValueError("valid_until_tick must be greater than valid_from_tick")


@dataclass(frozen=True)
class ResourceCustodyTransfer:
    transfer_id: str
    authorization_id: str
    request_id: str
    resource_id: str
    from_actor_id: str
    to_actor_id: str
    accountable_actor_id: str
    location_ref: str
    at_tick: int
    condition_ref: str | None = None

    def __post_init__(self) -> None:
        if not self.transfer_id.strip():
            raise ValueError("transfer_id is required")
        if self.at_tick < 0:
            raise ValueError("at_tick must be non-negative")
        if self.from_actor_id == self.to_actor_id:
            raise ValueError("custody transfer requires distinct actors")


@dataclass(frozen=True)
class ResourceHandoffLedger:
    authorizations: tuple[ResourceHandoffAuthorization, ...] = ()
    transfers: tuple[ResourceCustodyTransfer, ...] = ()


@dataclass(frozen=True)
class ResourceHandoffResult:
    accepted: bool
    ledger: ResourceHandoffLedger
    resource: WorldResource
    authorization: ResourceHandoffAuthorization | None = None
    transfer: ResourceCustodyTransfer | None = None
    reason_code: str = "HANDOFF_ACCEPTED"


def authorization_from_accepted_request(
    request_ledger: ResourceRequestLedger,
    *,
    request_id: str,
    authorization_id: str,
    receiving_actor_id: str,
    mode: HandoffMode,
    handoff_location_ref: str,
    valid_from_tick: int,
    valid_until_tick: int | None = None,
    authority_ref: str | None = None,
) -> ResourceHandoffAuthorization:
    view = request_view(request_ledger, request_id, valid_from_tick)
    if view is None:
        raise ValueError("unknown resource request")
    if view.state != ResourceRequestState.ACCEPTED:
        raise ValueError("resource request is not accepted")

    resource_id = view.offered_resource_id or view.request.resource_id
    return ResourceHandoffAuthorization(
        authorization_id=authorization_id,
        request_id=request_id,
        provider_actor_id=view.request.provider_actor_id,
        accountable_actor_id=view.request.requester_actor_id,
        receiving_actor_id=receiving_actor_id,
        resource_id=resource_id,
        mode=mode,
        handoff_location_ref=handoff_location_ref,
        valid_from_tick=valid_from_tick,
        valid_until_tick=valid_until_tick,
        authority_ref=authority_ref,
    )


def register_handoff_authorization(
    ledger: ResourceHandoffLedger,
    authorization: ResourceHandoffAuthorization,
) -> ResourceHandoffLedger:
    if any(item.authorization_id == authorization.authorization_id for item in ledger.authorizations):
        raise ValueError("duplicate handoff authorization id")
    return ResourceHandoffLedger(
        authorizations=tuple(sorted((*ledger.authorizations, authorization), key=lambda item: item.authorization_id)),
        transfers=ledger.transfers,
    )


def _authorization_by_id(
    ledger: ResourceHandoffLedger,
    authorization_id: str,
) -> ResourceHandoffAuthorization | None:
    return next(
        (item for item in ledger.authorizations if item.authorization_id == authorization_id),
        None,
    )


def execute_authorized_handoff(
    ledger: ResourceHandoffLedger,
    resource: WorldResource,
    transfer: ResourceCustodyTransfer,
) -> ResourceHandoffResult:
    authorization = _authorization_by_id(ledger, transfer.authorization_id)
    if authorization is None:
        return ResourceHandoffResult(False, ledger, resource, reason_code="UNKNOWN_HANDOFF_AUTHORIZATION")
    if any(item.transfer_id == transfer.transfer_id for item in ledger.transfers):
        return ResourceHandoffResult(False, ledger, resource, authorization, reason_code="DUPLICATE_CUSTODY_TRANSFER_ID")
    if any(item.authorization_id == authorization.authorization_id for item in ledger.transfers):
        return ResourceHandoffResult(False, ledger, resource, authorization, reason_code="HANDOFF_AUTHORIZATION_ALREADY_USED")

    expected = (
        transfer.request_id == authorization.request_id
        and transfer.resource_id == authorization.resource_id
        and transfer.from_actor_id == authorization.provider_actor_id
        and transfer.to_actor_id == authorization.receiving_actor_id
        and transfer.accountable_actor_id == authorization.accountable_actor_id
        and transfer.location_ref == authorization.handoff_location_ref
    )
    if not expected:
        return ResourceHandoffResult(False, ledger, resource, authorization, reason_code="HANDOFF_FACT_MISMATCH")
    if transfer.at_tick < authorization.valid_from_tick:
        return ResourceHandoffResult(False, ledger, resource, authorization, reason_code="HANDOFF_TOO_EARLY")
    if authorization.valid_until_tick is not None and transfer.at_tick >= authorization.valid_until_tick:
        return ResourceHandoffResult(False, ledger, resource, authorization, reason_code="HANDOFF_AUTHORIZATION_EXPIRED")
    if resource.resource_id != authorization.resource_id:
        return ResourceHandoffResult(False, ledger, resource, authorization, reason_code="RESOURCE_ID_MISMATCH")
    if resource.holder_actor_id != authorization.provider_actor_id:
        return ResourceHandoffResult(False, ledger, resource, authorization, reason_code="PROVIDER_NOT_CURRENT_HOLDER")
    if resource.location_ref != authorization.handoff_location_ref:
        return ResourceHandoffResult(False, ledger, resource, authorization, reason_code="RESOURCE_NOT_AT_HANDOFF_LOCATION")

    updated_resource = replace(
        resource,
        holder_actor_id=authorization.receiving_actor_id,
        location_ref=authorization.handoff_location_ref,
    )
    updated_ledger = ResourceHandoffLedger(
        authorizations=ledger.authorizations,
        transfers=tuple(
            sorted(
                (*ledger.transfers, transfer),
                key=lambda item: (item.at_tick, item.transfer_id),
            )
        ),
    )
    return ResourceHandoffResult(
        True,
        updated_ledger,
        updated_resource,
        authorization,
        transfer,
        "CUSTODY_TRANSFER_RECORDED",
    )


def custody_history(
    ledger: ResourceHandoffLedger,
    resource_id: str,
) -> tuple[ResourceCustodyTransfer, ...]:
    return tuple(
        sorted(
            (item for item in ledger.transfers if item.resource_id == resource_id),
            key=lambda item: (item.at_tick, item.transfer_id),
        )
    )


def active_authorizations_for_actor(
    ledger: ResourceHandoffLedger,
    actor_id: str,
    at_tick: int,
) -> tuple[ResourceHandoffAuthorization, ...]:
    used_ids = {item.authorization_id for item in ledger.transfers}
    matches: list[ResourceHandoffAuthorization] = []
    for item in ledger.authorizations:
        if item.authorization_id in used_ids:
            continue
        if item.receiving_actor_id != actor_id:
            continue
        if at_tick < item.valid_from_tick:
            continue
        if item.valid_until_tick is not None and at_tick >= item.valid_until_tick:
            continue
        matches.append(item)
    return tuple(sorted(matches, key=lambda item: item.authorization_id))
