from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from tools.global_npc_resource_recovery import ResourceRecoveryOption


class ResourceRequestEventKind(str, Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"
    WITHDRAWN = "WITHDRAWN"


class ResourceRequestState(str, Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"
    WITHDRAWN = "WITHDRAWN"
    EXPIRED = "EXPIRED"


@dataclass(frozen=True)
class ResourceRequest:
    request_id: str
    requester_actor_id: str
    provider_actor_id: str
    resource_id: str
    created_tick: int
    quantity: int = 1
    expires_at_tick: int | None = None
    purpose_ref: str | None = None

    def __post_init__(self) -> None:
        if not self.request_id.strip():
            raise ValueError("request_id is required")
        if not self.requester_actor_id.strip():
            raise ValueError("requester_actor_id is required")
        if not self.provider_actor_id.strip():
            raise ValueError("provider_actor_id is required")
        if not self.resource_id.strip():
            raise ValueError("resource_id is required")
        if self.requester_actor_id == self.provider_actor_id:
            raise ValueError("requester and provider must be different actors")
        if self.created_tick < 0:
            raise ValueError("created_tick must be non-negative")
        if self.quantity <= 0:
            raise ValueError("quantity must be positive")
        if self.expires_at_tick is not None and self.expires_at_tick <= self.created_tick:
            raise ValueError("expires_at_tick must be greater than created_tick")


@dataclass(frozen=True)
class ResourceRequestEvent:
    event_id: str
    request_id: str
    actor_id: str
    kind: ResourceRequestEventKind
    at_tick: int
    offered_resource_id: str | None = None
    reason_ref: str | None = None

    def __post_init__(self) -> None:
        if not self.event_id.strip():
            raise ValueError("event_id is required")
        if not self.request_id.strip():
            raise ValueError("request_id is required")
        if not self.actor_id.strip():
            raise ValueError("actor_id is required")
        if self.at_tick < 0:
            raise ValueError("at_tick must be non-negative")
        if self.offered_resource_id is not None and not self.offered_resource_id.strip():
            raise ValueError("offered_resource_id cannot be blank")


@dataclass(frozen=True)
class ResourceRequestLedger:
    requests: tuple[ResourceRequest, ...] = ()
    events: tuple[ResourceRequestEvent, ...] = ()


@dataclass(frozen=True)
class ResourceRequestTransitionResult:
    accepted: bool
    ledger: ResourceRequestLedger
    request: ResourceRequest | None = None
    event: ResourceRequestEvent | None = None
    reason_code: str = "REQUEST_TRANSITION_ACCEPTED"


@dataclass(frozen=True)
class ResourceRequestView:
    request: ResourceRequest
    state: ResourceRequestState
    terminal_event: ResourceRequestEvent | None = None
    offered_resource_id: str | None = None


def _request_by_id(ledger: ResourceRequestLedger, request_id: str) -> ResourceRequest | None:
    return next((item for item in ledger.requests if item.request_id == request_id), None)


def _events_for_request(
    ledger: ResourceRequestLedger,
    request_id: str,
) -> tuple[ResourceRequestEvent, ...]:
    return tuple(
        sorted(
            (event for event in ledger.events if event.request_id == request_id),
            key=lambda event: (event.at_tick, event.event_id),
        )
    )


def request_view(
    ledger: ResourceRequestLedger,
    request_id: str,
    at_tick: int,
) -> ResourceRequestView | None:
    request = _request_by_id(ledger, request_id)
    if request is None:
        return None
    if at_tick < 0:
        raise ValueError("at_tick must be non-negative")

    applicable_events = [
        event for event in _events_for_request(ledger, request_id) if event.at_tick <= at_tick
    ]
    if applicable_events:
        event = applicable_events[-1]
        return ResourceRequestView(
            request=request,
            state=ResourceRequestState(event.kind.value),
            terminal_event=event,
            offered_resource_id=event.offered_resource_id,
        )

    if request.expires_at_tick is not None and at_tick >= request.expires_at_tick:
        return ResourceRequestView(request, ResourceRequestState.EXPIRED)
    return ResourceRequestView(request, ResourceRequestState.PENDING)


def submit_resource_request(
    ledger: ResourceRequestLedger,
    request: ResourceRequest,
) -> ResourceRequestTransitionResult:
    if _request_by_id(ledger, request.request_id) is not None:
        return ResourceRequestTransitionResult(
            False,
            ledger,
            reason_code="DUPLICATE_REQUEST_ID",
        )
    updated = ResourceRequestLedger(
        requests=tuple(sorted((*ledger.requests, request), key=lambda item: item.request_id)),
        events=ledger.events,
    )
    return ResourceRequestTransitionResult(
        True,
        updated,
        request=request,
        reason_code="REQUEST_SUBMITTED",
    )


def request_from_recovery_option(
    option: ResourceRecoveryOption,
    *,
    request_id: str,
    requester_actor_id: str,
    created_tick: int,
    expires_at_tick: int | None = None,
    purpose_ref: str | None = None,
) -> ResourceRequest:
    if option.intent.kind != "REQUEST_RESOURCE":
        raise ValueError("recovery option is not a resource request")
    if not option.request_target_actor_id:
        raise ValueError("resource request recovery option lacks provider actor")
    return ResourceRequest(
        request_id=request_id,
        requester_actor_id=requester_actor_id,
        provider_actor_id=option.request_target_actor_id,
        resource_id=option.resource_id,
        quantity=option.requirement.quantity,
        created_tick=created_tick,
        expires_at_tick=expires_at_tick,
        purpose_ref=purpose_ref or option.intent.intent_id,
    )


def provider_respond(
    ledger: ResourceRequestLedger,
    event: ResourceRequestEvent,
) -> ResourceRequestTransitionResult:
    if event.kind not in {ResourceRequestEventKind.ACCEPTED, ResourceRequestEventKind.REJECTED}:
        return ResourceRequestTransitionResult(
            False,
            ledger,
            reason_code="INVALID_PROVIDER_RESPONSE_KIND",
        )
    request = _request_by_id(ledger, event.request_id)
    if request is None:
        return ResourceRequestTransitionResult(False, ledger, reason_code="UNKNOWN_REQUEST")
    if event.actor_id != request.provider_actor_id:
        return ResourceRequestTransitionResult(
            False,
            ledger,
            request=request,
            reason_code="PROVIDER_ACTOR_MISMATCH",
        )
    return _append_transition_if_allowed(ledger, request, event, require_state=ResourceRequestState.PENDING)


def requester_cancel(
    ledger: ResourceRequestLedger,
    event: ResourceRequestEvent,
) -> ResourceRequestTransitionResult:
    if event.kind != ResourceRequestEventKind.CANCELLED:
        return ResourceRequestTransitionResult(
            False,
            ledger,
            reason_code="INVALID_REQUESTER_CANCEL_KIND",
        )
    request = _request_by_id(ledger, event.request_id)
    if request is None:
        return ResourceRequestTransitionResult(False, ledger, reason_code="UNKNOWN_REQUEST")
    if event.actor_id != request.requester_actor_id:
        return ResourceRequestTransitionResult(
            False,
            ledger,
            request=request,
            reason_code="REQUESTER_ACTOR_MISMATCH",
        )
    return _append_transition_if_allowed(ledger, request, event, require_state=ResourceRequestState.PENDING)


def provider_withdraw_acceptance(
    ledger: ResourceRequestLedger,
    event: ResourceRequestEvent,
) -> ResourceRequestTransitionResult:
    if event.kind != ResourceRequestEventKind.WITHDRAWN:
        return ResourceRequestTransitionResult(
            False,
            ledger,
            reason_code="INVALID_WITHDRAWAL_KIND",
        )
    request = _request_by_id(ledger, event.request_id)
    if request is None:
        return ResourceRequestTransitionResult(False, ledger, reason_code="UNKNOWN_REQUEST")
    if event.actor_id != request.provider_actor_id:
        return ResourceRequestTransitionResult(
            False,
            ledger,
            request=request,
            reason_code="PROVIDER_ACTOR_MISMATCH",
        )
    return _append_transition_if_allowed(ledger, request, event, require_state=ResourceRequestState.ACCEPTED)


def _append_transition_if_allowed(
    ledger: ResourceRequestLedger,
    request: ResourceRequest,
    event: ResourceRequestEvent,
    *,
    require_state: ResourceRequestState,
) -> ResourceRequestTransitionResult:
    if any(existing.event_id == event.event_id for existing in ledger.events):
        return ResourceRequestTransitionResult(
            False,
            ledger,
            request=request,
            reason_code="DUPLICATE_REQUEST_EVENT_ID",
        )
    if event.at_tick < request.created_tick:
        return ResourceRequestTransitionResult(
            False,
            ledger,
            request=request,
            reason_code="REQUEST_EVENT_BEFORE_CREATION",
        )

    before = request_view(ledger, request.request_id, event.at_tick)
    assert before is not None
    if before.state == ResourceRequestState.EXPIRED:
        return ResourceRequestTransitionResult(
            False,
            ledger,
            request=request,
            reason_code="REQUEST_EXPIRED",
        )
    if before.state != require_state:
        return ResourceRequestTransitionResult(
            False,
            ledger,
            request=request,
            reason_code="REQUEST_STATE_MISMATCH",
        )

    updated = ResourceRequestLedger(
        requests=ledger.requests,
        events=tuple(
            sorted(
                (*ledger.events, event),
                key=lambda item: (item.request_id, item.at_tick, item.event_id),
            )
        ),
    )
    return ResourceRequestTransitionResult(
        True,
        updated,
        request=request,
        event=event,
        reason_code=f"REQUEST_{event.kind.value}",
    )


def accepted_request_views(
    ledger: ResourceRequestLedger,
    at_tick: int,
) -> tuple[ResourceRequestView, ...]:
    views = [
        request_view(ledger, request.request_id, at_tick)
        for request in sorted(ledger.requests, key=lambda item: item.request_id)
    ]
    return tuple(
        view
        for view in views
        if view is not None and view.state == ResourceRequestState.ACCEPTED
    )


def request_history(
    ledger: ResourceRequestLedger,
    request_id: str,
) -> tuple[ResourceRequestEvent, ...]:
    return _events_for_request(ledger, request_id)
