from tools.global_npc_resource_handoff_rescheduling import (
    HandoffRescheduleDecisionKind,
    ResourceHandoffAuthorizationReplacement,
    ResourceHandoffRescheduleDecision,
    ResourceHandoffRescheduleLedger,
    ResourceHandoffRescheduleProposal,
)
from tools.global_npc_resource_handoff_rescheduling_holder import (
    execute_current_authorized_handoff_with_holder_transition,
)
from tools.global_npc_resource_handoffs import (
    HandoffMode,
    ResourceCustodyTransfer,
    ResourceHandoffAuthorization,
    ResourceHandoffLedger,
)
from tools.global_npc_resource_holder_transitions import (
    HolderTransitionKind,
    ResourceHolderTransitionLedger,
)
from tools.global_npc_resources import ResourceState, WorldResource


def _handoff_ledger() -> ResourceHandoffLedger:
    old = ResourceHandoffAuthorization(
        authorization_id="auth:old",
        request_id="request:meter",
        provider_actor_id="npc:teo",
        accountable_actor_id="npc:nerea",
        receiving_actor_id="npc:ema",
        resource_id="resource:meter",
        mode=HandoffMode.PICKUP,
        handoff_location_ref="place:repair-row",
        valid_from_tick=30,
        valid_until_tick=60,
    )
    new = ResourceHandoffAuthorization(
        authorization_id="auth:new",
        request_id="request:meter",
        provider_actor_id="npc:teo",
        accountable_actor_id="npc:nerea",
        receiving_actor_id="npc:ema",
        resource_id="resource:meter",
        mode=HandoffMode.PICKUP,
        handoff_location_ref="place:field-office",
        valid_from_tick=90,
        valid_until_tick=120,
        authority_ref="decision:accept",
    )
    return ResourceHandoffLedger(authorizations=(new, old))


def _reschedule_ledger() -> ResourceHandoffRescheduleLedger:
    proposal = ResourceHandoffRescheduleProposal(
        proposal_id="proposal:later",
        authorization_id="auth:old",
        source_notice_id="notice:reschedule",
        proposer_actor_id="npc:ema",
        responder_actor_id="npc:teo",
        proposed_location_ref="place:field-office",
        proposed_valid_from_tick=90,
        proposed_valid_until_tick=120,
        created_tick=40,
    )
    decision = ResourceHandoffRescheduleDecision(
        decision_id="decision:accept",
        proposal_id="proposal:later",
        actor_id="npc:teo",
        kind=HandoffRescheduleDecisionKind.ACCEPT,
        at_tick=46,
    )
    replacement = ResourceHandoffAuthorizationReplacement(
        replacement_id="replacement:1",
        proposal_id="proposal:later",
        decision_id="decision:accept",
        superseded_authorization_id="auth:old",
        successor_authorization_id="auth:new",
        at_tick=46,
    )
    return ResourceHandoffRescheduleLedger(
        proposals=(proposal,), decisions=(decision,), replacements=(replacement,)
    )


def _resource(location: str) -> WorldResource:
    return WorldResource(
        resource_id="resource:meter",
        capability_refs=frozenset({"FIELD_METER"}),
        quantity=1,
        state=ResourceState.AVAILABLE,
        location_ref=location,
        holder_actor_id="npc:teo",
    )


def test_current_successor_records_exact_holder_transition() -> None:
    handoffs = _handoff_ledger()
    reschedules = _reschedule_ledger()
    holders = ResourceHolderTransitionLedger()
    transfer = ResourceCustodyTransfer(
        transfer_id="transfer:new",
        authorization_id="auth:new",
        request_id="request:meter",
        resource_id="resource:meter",
        from_actor_id="npc:teo",
        to_actor_id="npc:ema",
        accountable_actor_id="npc:nerea",
        location_ref="place:field-office",
        at_tick=95,
    )

    result = execute_current_authorized_handoff_with_holder_transition(
        reschedules,
        handoffs,
        holders,
        _resource("place:field-office"),
        transfer,
        transition_id="holder:transfer:new",
    )

    assert result.handoff.accepted
    assert result.handoff.resource.holder_actor_id == "npc:ema"
    assert result.holder_transition is not None
    assert result.holder_transition.kind == HolderTransitionKind.HANDOFF
    assert result.holder_transition.from_actor_id == "npc:teo"
    assert result.holder_transition.to_actor_id == "npc:ema"
    assert result.holder_transition.source_ref == "transfer:new"
    assert result.holder_ledger.transitions == (result.holder_transition,)


def test_superseded_authorization_cannot_create_transfer_or_holder_history() -> None:
    handoffs = _handoff_ledger()
    reschedules = _reschedule_ledger()
    holders = ResourceHolderTransitionLedger()
    resource = _resource("place:repair-row")
    transfer = ResourceCustodyTransfer(
        transfer_id="transfer:stale",
        authorization_id="auth:old",
        request_id="request:meter",
        resource_id="resource:meter",
        from_actor_id="npc:teo",
        to_actor_id="npc:ema",
        accountable_actor_id="npc:nerea",
        location_ref="place:repair-row",
        at_tick=50,
    )

    result = execute_current_authorized_handoff_with_holder_transition(
        reschedules,
        handoffs,
        holders,
        resource,
        transfer,
        transition_id="holder:transfer:stale",
    )

    assert not result.handoff.accepted
    assert result.handoff.reason_code == "HANDOFF_AUTHORIZATION_SUPERSEDED"
    assert result.handoff.resource == resource
    assert result.handoff.ledger.transfers == ()
    assert result.holder_transition is None
    assert result.holder_ledger == holders


def test_failed_current_handoff_cannot_create_holder_history() -> None:
    handoffs = _handoff_ledger()
    reschedules = _reschedule_ledger()
    holders = ResourceHolderTransitionLedger()
    resource = _resource("place:wrong-location")
    transfer = ResourceCustodyTransfer(
        transfer_id="transfer:new",
        authorization_id="auth:new",
        request_id="request:meter",
        resource_id="resource:meter",
        from_actor_id="npc:teo",
        to_actor_id="npc:ema",
        accountable_actor_id="npc:nerea",
        location_ref="place:field-office",
        at_tick=95,
    )

    result = execute_current_authorized_handoff_with_holder_transition(
        reschedules,
        handoffs,
        holders,
        resource,
        transfer,
        transition_id="holder:transfer:new",
    )

    assert not result.handoff.accepted
    assert result.handoff.reason_code == "RESOURCE_NOT_AT_HANDOFF_LOCATION"
    assert result.holder_transition is None
    assert result.holder_ledger == holders
