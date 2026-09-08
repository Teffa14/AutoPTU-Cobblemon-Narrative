import pytest

from tools.global_npc_resource_handoffs import (
    HandoffMode,
    ResourceCustodyTransfer,
    ResourceHandoffLedger,
    active_authorizations_for_actor,
    authorization_from_accepted_request,
    custody_history,
    execute_authorized_handoff,
    register_handoff_authorization,
)
from tools.global_npc_resource_requests import (
    ResourceRequest,
    ResourceRequestEvent,
    ResourceRequestEventKind,
    ResourceRequestLedger,
    provider_respond,
    submit_resource_request,
)
from tools.global_npc_resources import ResourceState, WorldResource


def _accepted_request(*, offered_resource_id: str | None = None) -> ResourceRequestLedger:
    request = ResourceRequest(
        request_id="request:meter",
        requester_actor_id="npc:surveyor",
        provider_actor_id="npc:technician",
        resource_id="resource:meter-a",
        created_tick=10,
        expires_at_tick=100,
        purpose_ref="work:survey",
    )
    ledger = submit_resource_request(ResourceRequestLedger(), request).ledger
    event = ResourceRequestEvent(
        event_id="request-event:accept",
        request_id=request.request_id,
        actor_id=request.provider_actor_id,
        kind=ResourceRequestEventKind.ACCEPTED,
        at_tick=20,
        offered_resource_id=offered_resource_id,
    )
    return provider_respond(ledger, event).ledger


def _authorization(request_ledger: ResourceRequestLedger, **overrides):
    values = dict(
        request_id="request:meter",
        authorization_id="handoff-auth:meter",
        receiving_actor_id="npc:surveyor",
        mode=HandoffMode.PICKUP,
        handoff_location_ref="place:field-office",
        valid_from_tick=30,
        valid_until_tick=60,
        authority_ref="request-event:accept",
    )
    values.update(overrides)
    return authorization_from_accepted_request(request_ledger, **values)


def _resource(**overrides) -> WorldResource:
    values = dict(
        resource_id="resource:meter-a",
        capability_refs=frozenset({"FIELD_METER"}),
        state=ResourceState.IN_USE,
        location_ref="place:field-office",
        holder_actor_id="npc:technician",
    )
    values.update(overrides)
    return WorldResource(**values)


def _transfer(**overrides) -> ResourceCustodyTransfer:
    values = dict(
        transfer_id="custody-transfer:1",
        authorization_id="handoff-auth:meter",
        request_id="request:meter",
        resource_id="resource:meter-a",
        from_actor_id="npc:technician",
        to_actor_id="npc:surveyor",
        accountable_actor_id="npc:surveyor",
        location_ref="place:field-office",
        at_tick=40,
        condition_ref="condition:checked-at-handoff",
    )
    values.update(overrides)
    return ResourceCustodyTransfer(**values)


def test_accepted_request_can_authorize_future_pickup_without_moving_resource() -> None:
    request_ledger = _accepted_request()
    authorization = _authorization(request_ledger)

    assert authorization.resource_id == "resource:meter-a"
    assert authorization.provider_actor_id == "npc:technician"
    assert authorization.accountable_actor_id == "npc:surveyor"
    assert authorization.receiving_actor_id == "npc:surveyor"


def test_unaccepted_request_cannot_create_handoff_authorization() -> None:
    request = ResourceRequest(
        request_id="request:pending",
        requester_actor_id="npc:a",
        provider_actor_id="npc:b",
        resource_id="resource:x",
        created_tick=10,
    )
    ledger = submit_resource_request(ResourceRequestLedger(), request).ledger

    with pytest.raises(ValueError, match="not accepted"):
        authorization_from_accepted_request(
            ledger,
            request_id=request.request_id,
            authorization_id="handoff-auth:x",
            receiving_actor_id="npc:a",
            mode=HandoffMode.PICKUP,
            handoff_location_ref="place:x",
            valid_from_tick=20,
        )


def test_alternate_offer_becomes_handoff_resource_without_rewriting_request() -> None:
    ledger = _accepted_request(offered_resource_id="resource:meter-b")
    authorization = _authorization(ledger)

    assert authorization.resource_id == "resource:meter-b"


def test_authorized_handoff_changes_only_current_custody_and_records_history() -> None:
    authorization = _authorization(_accepted_request())
    handoff_ledger = register_handoff_authorization(ResourceHandoffLedger(), authorization)
    original = _resource()
    transfer = _transfer()

    result = execute_authorized_handoff(handoff_ledger, original, transfer)

    assert result.accepted is True
    assert result.reason_code == "CUSTODY_TRANSFER_RECORDED"
    assert original.holder_actor_id == "npc:technician"
    assert result.resource.holder_actor_id == "npc:surveyor"
    assert result.resource.location_ref == "place:field-office"
    assert custody_history(result.ledger, original.resource_id) == (transfer,)


def test_proxy_pickup_records_proxy_as_physical_holder_but_requester_as_accountable_actor() -> None:
    request_ledger = _accepted_request()
    authorization = _authorization(
        request_ledger,
        receiving_actor_id="npc:assistant",
        authorization_id="handoff-auth:proxy",
    )
    ledger = register_handoff_authorization(ResourceHandoffLedger(), authorization)
    transfer = _transfer(
        authorization_id="handoff-auth:proxy",
        to_actor_id="npc:assistant",
    )

    result = execute_authorized_handoff(ledger, _resource(), transfer)

    assert result.accepted is True
    assert result.resource.holder_actor_id == "npc:assistant"
    assert result.transfer.accountable_actor_id == "npc:surveyor"


def test_provider_must_still_be_current_holder_at_handoff() -> None:
    authorization = _authorization(_accepted_request())
    ledger = register_handoff_authorization(ResourceHandoffLedger(), authorization)

    result = execute_authorized_handoff(
        ledger,
        _resource(holder_actor_id="npc:someone-else"),
        _transfer(),
    )

    assert result.accepted is False
    assert result.reason_code == "PROVIDER_NOT_CURRENT_HOLDER"


def test_resource_must_be_at_authored_handoff_location() -> None:
    authorization = _authorization(_accepted_request())
    ledger = register_handoff_authorization(ResourceHandoffLedger(), authorization)

    result = execute_authorized_handoff(
        ledger,
        _resource(location_ref="place:remote-site"),
        _transfer(),
    )

    assert result.accepted is False
    assert result.reason_code == "RESOURCE_NOT_AT_HANDOFF_LOCATION"


def test_handoff_window_is_enforced_without_erasing_authorization() -> None:
    authorization = _authorization(_accepted_request())
    ledger = register_handoff_authorization(ResourceHandoffLedger(), authorization)

    early = execute_authorized_handoff(ledger, _resource(), _transfer(at_tick=29))
    late = execute_authorized_handoff(ledger, _resource(), _transfer(at_tick=60))

    assert early.accepted is False
    assert early.reason_code == "HANDOFF_TOO_EARLY"
    assert late.accepted is False
    assert late.reason_code == "HANDOFF_AUTHORIZATION_EXPIRED"
    assert ledger.authorizations == (authorization,)


def test_authorization_is_single_use_and_duplicate_transfer_ids_fail_closed() -> None:
    authorization = _authorization(_accepted_request())
    ledger = register_handoff_authorization(ResourceHandoffLedger(), authorization)
    first = execute_authorized_handoff(ledger, _resource(), _transfer())
    assert first.accepted is True

    reused = execute_authorized_handoff(first.ledger, _resource(), _transfer(transfer_id="custody-transfer:2"))
    duplicate = execute_authorized_handoff(first.ledger, _resource(), _transfer())

    assert reused.accepted is False
    assert reused.reason_code == "HANDOFF_AUTHORIZATION_ALREADY_USED"
    assert duplicate.accepted is False
    assert duplicate.reason_code == "DUPLICATE_CUSTODY_TRANSFER_ID"


def test_active_authorizations_are_deterministic_and_exclude_used_or_expired_entries() -> None:
    request_ledger = _accepted_request()
    a = _authorization(request_ledger, authorization_id="handoff-auth:z")
    b = _authorization(request_ledger, authorization_id="handoff-auth:a")
    ledger = register_handoff_authorization(ResourceHandoffLedger(), a)
    ledger = register_handoff_authorization(ledger, b)

    assert [item.authorization_id for item in active_authorizations_for_actor(ledger, "npc:surveyor", 40)] == [
        "handoff-auth:a",
        "handoff-auth:z",
    ]

    used = execute_authorized_handoff(
        ledger,
        _resource(),
        _transfer(authorization_id="handoff-auth:a"),
    )
    assert used.accepted is True
    assert [item.authorization_id for item in active_authorizations_for_actor(used.ledger, "npc:surveyor", 40)] == [
        "handoff-auth:z"
    ]
    assert active_authorizations_for_actor(used.ledger, "npc:surveyor", 60) == ()


def test_handoff_does_not_claim_delivery_when_recipient_identity_mismatches() -> None:
    authorization = _authorization(_accepted_request())
    ledger = register_handoff_authorization(ResourceHandoffLedger(), authorization)

    result = execute_authorized_handoff(
        ledger,
        _resource(),
        _transfer(to_actor_id="npc:unauthorized-proxy"),
    )

    assert result.accepted is False
    assert result.reason_code == "HANDOFF_FACT_MISMATCH"
