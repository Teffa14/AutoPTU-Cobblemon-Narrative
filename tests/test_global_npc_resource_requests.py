import pytest

from tools.global_npc_ai import NpcIntent
from tools.global_npc_resource_recovery import ResourceRecoveryOption
from tools.global_npc_resource_requests import (
    ResourceRequest,
    ResourceRequestEvent,
    ResourceRequestEventKind,
    ResourceRequestLedger,
    ResourceRequestState,
    accepted_request_views,
    provider_respond,
    provider_withdraw_acceptance,
    request_from_recovery_option,
    request_history,
    request_view,
    requester_cancel,
    submit_resource_request,
)
from tools.global_npc_resources import ResourceRequirement


def _request(**overrides) -> ResourceRequest:
    values = dict(
        request_id="request:meter-1",
        requester_actor_id="npc:surveyor",
        provider_actor_id="npc:technician",
        resource_id="resource:field-meter",
        created_tick=100,
        quantity=1,
        expires_at_tick=160,
        purpose_ref="work:water-survey",
    )
    values.update(overrides)
    return ResourceRequest(**values)


def _event(kind: ResourceRequestEventKind, **overrides) -> ResourceRequestEvent:
    values = dict(
        event_id=f"event:{kind.value.lower()}:1",
        request_id="request:meter-1",
        actor_id="npc:technician",
        kind=kind,
        at_tick=120,
    )
    values.update(overrides)
    return ResourceRequestEvent(**values)


def _submitted(request: ResourceRequest | None = None) -> ResourceRequestLedger:
    result = submit_resource_request(ResourceRequestLedger(), request or _request())
    assert result.accepted is True
    return result.ledger


def test_submit_preserves_pending_request_without_transfer() -> None:
    request = _request()
    result = submit_resource_request(ResourceRequestLedger(), request)

    assert result.accepted is True
    assert result.reason_code == "REQUEST_SUBMITTED"
    assert request_view(result.ledger, request.request_id, 100).state == ResourceRequestState.PENDING
    assert result.ledger.events == ()


def test_duplicate_request_id_is_rejected_without_mutation() -> None:
    ledger = _submitted()
    result = submit_resource_request(ledger, _request())

    assert result.accepted is False
    assert result.reason_code == "DUPLICATE_REQUEST_ID"
    assert result.ledger == ledger


def test_provider_acceptance_requires_exact_provider_actor() -> None:
    ledger = _submitted()
    event = _event(ResourceRequestEventKind.ACCEPTED, actor_id="npc:someone-else")
    result = provider_respond(ledger, event)

    assert result.accepted is False
    assert result.reason_code == "PROVIDER_ACTOR_MISMATCH"
    assert request_view(ledger, "request:meter-1", 120).state == ResourceRequestState.PENDING


def test_provider_can_accept_without_transferring_or_reserving_resource() -> None:
    ledger = _submitted()
    event = _event(ResourceRequestEventKind.ACCEPTED)
    result = provider_respond(ledger, event)

    assert result.accepted is True
    view = request_view(result.ledger, "request:meter-1", 120)
    assert view.state == ResourceRequestState.ACCEPTED
    assert view.offered_resource_id is None
    assert request_history(result.ledger, "request:meter-1") == (event,)


def test_provider_can_accept_with_explicit_alternate_offer_without_fabricating_delivery() -> None:
    ledger = _submitted()
    event = _event(
        ResourceRequestEventKind.ACCEPTED,
        offered_resource_id="resource:alternate-meter",
    )
    result = provider_respond(ledger, event)

    assert result.accepted is True
    view = request_view(result.ledger, "request:meter-1", 130)
    assert view.state == ResourceRequestState.ACCEPTED
    assert view.offered_resource_id == "resource:alternate-meter"
    assert view.request.resource_id == "resource:field-meter"


def test_provider_rejection_closes_request() -> None:
    ledger = _submitted()
    rejected = provider_respond(ledger, _event(ResourceRequestEventKind.REJECTED))
    assert rejected.accepted is True

    later = provider_respond(
        rejected.ledger,
        _event(ResourceRequestEventKind.ACCEPTED, event_id="event:accept:late", at_tick=130),
    )
    assert later.accepted is False
    assert later.reason_code == "REQUEST_STATE_MISMATCH"
    assert request_view(rejected.ledger, "request:meter-1", 140).state == ResourceRequestState.REJECTED


def test_requester_can_cancel_only_while_pending() -> None:
    ledger = _submitted()
    event = _event(
        ResourceRequestEventKind.CANCELLED,
        actor_id="npc:surveyor",
        event_id="event:cancel:1",
    )
    result = requester_cancel(ledger, event)

    assert result.accepted is True
    assert request_view(result.ledger, "request:meter-1", 130).state == ResourceRequestState.CANCELLED


def test_expiry_is_derived_without_rewriting_request_history() -> None:
    ledger = _submitted()

    assert request_view(ledger, "request:meter-1", 159).state == ResourceRequestState.PENDING
    assert request_view(ledger, "request:meter-1", 160).state == ResourceRequestState.EXPIRED
    assert request_history(ledger, "request:meter-1") == ()

    late = provider_respond(
        ledger,
        _event(ResourceRequestEventKind.ACCEPTED, at_tick=160),
    )
    assert late.accepted is False
    assert late.reason_code == "REQUEST_EXPIRED"


def test_provider_can_withdraw_only_after_acceptance() -> None:
    ledger = _submitted()
    premature = provider_withdraw_acceptance(
        ledger,
        _event(ResourceRequestEventKind.WITHDRAWN, event_id="event:withdraw:early"),
    )
    assert premature.accepted is False
    assert premature.reason_code == "REQUEST_STATE_MISMATCH"

    accepted = provider_respond(ledger, _event(ResourceRequestEventKind.ACCEPTED))
    withdrawn = provider_withdraw_acceptance(
        accepted.ledger,
        _event(ResourceRequestEventKind.WITHDRAWN, event_id="event:withdraw:1", at_tick=130),
    )
    assert withdrawn.accepted is True
    assert request_view(withdrawn.ledger, "request:meter-1", 140).state == ResourceRequestState.WITHDRAWN
    assert [event.kind for event in request_history(withdrawn.ledger, "request:meter-1")] == [
        ResourceRequestEventKind.ACCEPTED,
        ResourceRequestEventKind.WITHDRAWN,
    ]


def test_accepted_request_views_are_deterministic_and_exclude_terminal_nonaccepted_states() -> None:
    first = _request(request_id="request:z", resource_id="resource:z")
    second = _request(request_id="request:a", resource_id="resource:a")
    ledger = ResourceRequestLedger()
    ledger = submit_resource_request(ledger, first).ledger
    ledger = submit_resource_request(ledger, second).ledger
    ledger = provider_respond(
        ledger,
        ResourceRequestEvent(
            "event:z", "request:z", "npc:technician", ResourceRequestEventKind.ACCEPTED, 110
        ),
    ).ledger
    ledger = provider_respond(
        ledger,
        ResourceRequestEvent(
            "event:a", "request:a", "npc:technician", ResourceRequestEventKind.ACCEPTED, 111
        ),
    ).ledger

    assert [view.request.request_id for view in accepted_request_views(ledger, 120)] == [
        "request:a",
        "request:z",
    ]


def test_recovery_request_option_can_be_materialized_without_executing_it() -> None:
    option = ResourceRecoveryOption(
        intent=NpcIntent(
            intent_id="resource-request:work:survey:resource:meter:npc:technician",
            kind="REQUEST_RESOURCE",
            base_priority=4,
            target_ref="npc:technician",
        ),
        requirement=ResourceRequirement("FIELD_METER", 1),
        resource_id="resource:meter",
        reason_code="RESOURCE_HELD_BY_OTHER_ACTOR",
        request_target_actor_id="npc:technician",
    )

    request = request_from_recovery_option(
        option,
        request_id="request:from-recovery",
        requester_actor_id="npc:surveyor",
        created_tick=200,
        expires_at_tick=230,
    )

    assert request.provider_actor_id == "npc:technician"
    assert request.resource_id == "resource:meter"
    assert request.quantity == 1
    assert request.purpose_ref == option.intent.intent_id


def test_nonrequest_recovery_option_cannot_be_materialized_as_request() -> None:
    option = ResourceRecoveryOption(
        intent=NpcIntent(intent_id="wait:1", kind="WAIT_FOR_RESOURCE", base_priority=1),
        requirement=ResourceRequirement("FIELD_METER", 1),
        resource_id="resource:meter",
        reason_code="RESOURCE_RESERVED_FOR_OTHER_ACTOR",
    )

    with pytest.raises(ValueError, match="not a resource request"):
        request_from_recovery_option(
            option,
            request_id="request:invalid",
            requester_actor_id="npc:surveyor",
            created_tick=200,
        )
