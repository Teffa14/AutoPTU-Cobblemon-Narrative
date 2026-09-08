import pytest

from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_resource_handoff_attempts import (
    HandoffAttemptOutcome,
    HandoffAuthorizationState,
    ResourceHandoffAttempt,
    ResourceHandoffAttemptLedger,
    attempts_for_authorization,
    authorization_state,
    record_handoff_attempt,
    schedule_handoff_attempt_replans,
)
from tools.global_npc_resource_handoffs import (
    HandoffMode,
    ResourceCustodyTransfer,
    ResourceHandoffAuthorization,
    ResourceHandoffLedger,
    execute_authorized_handoff,
    register_handoff_authorization,
)
from tools.global_npc_resources import ResourceState, WorldResource


def _authorization(**overrides):
    values = dict(
        authorization_id="handoff-auth:meter",
        request_id="request:meter",
        provider_actor_id="npc:technician",
        accountable_actor_id="npc:surveyor",
        receiving_actor_id="npc:assistant",
        resource_id="resource:meter-a",
        mode=HandoffMode.PICKUP,
        handoff_location_ref="place:field-office",
        valid_from_tick=30,
        valid_until_tick=60,
        authority_ref="request-event:accept",
    )
    values.update(overrides)
    return ResourceHandoffAuthorization(**values)


def _handoff_ledger(**overrides):
    authorization = _authorization(**overrides)
    return register_handoff_authorization(ResourceHandoffLedger(), authorization)


def _attempt(**overrides):
    values = dict(
        attempt_id="handoff-attempt:1",
        authorization_id="handoff-auth:meter",
        actor_id="npc:assistant",
        location_ref="place:field-office",
        at_tick=40,
        outcome=HandoffAttemptOutcome.PROVIDER_ABSENT,
        observation_ref="observation:empty-desk",
    )
    values.update(overrides)
    return ResourceHandoffAttempt(**values)


def test_no_show_is_recorded_without_consuming_authorization() -> None:
    handoff_ledger = _handoff_ledger()
    attempt = _attempt()
    ledger = record_handoff_attempt(ResourceHandoffAttemptLedger(), handoff_ledger, attempt)

    assert attempts_for_authorization(ledger, attempt.authorization_id) == (attempt,)
    assert authorization_state(handoff_ledger, ledger, attempt.authorization_id, 41) == HandoffAuthorizationState.ACTIVE


def test_refusal_closes_authorization_without_fabricating_transfer() -> None:
    handoff_ledger = _handoff_ledger(receiving_actor_id="npc:surveyor")
    attempt = _attempt(
        actor_id="npc:technician",
        outcome=HandoffAttemptOutcome.PROVIDER_REFUSED,
    )
    ledger = record_handoff_attempt(ResourceHandoffAttemptLedger(), handoff_ledger, attempt)

    assert authorization_state(handoff_ledger, ledger, attempt.authorization_id, 41) == HandoffAuthorizationState.REFUSED
    assert handoff_ledger.transfers == ()


def test_refusal_must_be_recorded_by_the_refusing_role() -> None:
    handoff_ledger = _handoff_ledger()
    with pytest.raises(ValueError, match="provider refusal"):
        record_handoff_attempt(
            ResourceHandoffAttemptLedger(),
            handoff_ledger,
            _attempt(outcome=HandoffAttemptOutcome.PROVIDER_REFUSED),
        )


def test_attempt_requires_authorized_participant_place_and_window() -> None:
    handoff_ledger = _handoff_ledger()
    with pytest.raises(ValueError, match="authorized participant"):
        record_handoff_attempt(ResourceHandoffAttemptLedger(), handoff_ledger, _attempt(actor_id="npc:bystander"))
    with pytest.raises(ValueError, match="location mismatch"):
        record_handoff_attempt(ResourceHandoffAttemptLedger(), handoff_ledger, _attempt(location_ref="place:wrong"))
    with pytest.raises(ValueError, match="too early"):
        record_handoff_attempt(ResourceHandoffAttemptLedger(), handoff_ledger, _attempt(at_tick=29))
    with pytest.raises(ValueError, match="expired"):
        record_handoff_attempt(ResourceHandoffAttemptLedger(), handoff_ledger, _attempt(at_tick=60))


def test_completed_handoff_rejects_later_failed_attempt() -> None:
    handoff_ledger = _handoff_ledger()
    resource = WorldResource(
        resource_id="resource:meter-a",
        capability_refs=frozenset({"FIELD_METER"}),
        state=ResourceState.IN_USE,
        location_ref="place:field-office",
        holder_actor_id="npc:technician",
    )
    transfer = ResourceCustodyTransfer(
        transfer_id="custody-transfer:1",
        authorization_id="handoff-auth:meter",
        request_id="request:meter",
        resource_id="resource:meter-a",
        from_actor_id="npc:technician",
        to_actor_id="npc:assistant",
        accountable_actor_id="npc:surveyor",
        location_ref="place:field-office",
        at_tick=35,
    )
    completed = execute_authorized_handoff(handoff_ledger, resource, transfer)
    assert completed.accepted is True

    with pytest.raises(ValueError, match="already completed"):
        record_handoff_attempt(ResourceHandoffAttemptLedger(), completed.ledger, _attempt(at_tick=40))


def test_authorization_state_distinguishes_scheduled_active_expired_and_completed() -> None:
    handoff_ledger = _handoff_ledger()
    attempts = ResourceHandoffAttemptLedger()
    assert authorization_state(handoff_ledger, attempts, "handoff-auth:meter", 20) == HandoffAuthorizationState.SCHEDULED
    assert authorization_state(handoff_ledger, attempts, "handoff-auth:meter", 40) == HandoffAuthorizationState.ACTIVE
    assert authorization_state(handoff_ledger, attempts, "handoff-auth:meter", 60) == HandoffAuthorizationState.EXPIRED
    assert authorization_state(handoff_ledger, attempts, "missing", 40) is None


def test_failed_attempt_schedules_selective_replans_for_participants() -> None:
    handoff_ledger = _handoff_ledger()
    attempt = _attempt()
    queue = NpcReplanQueue()

    triggers = schedule_handoff_attempt_replans(queue, handoff_ledger, attempt)
    assert [trigger.agent_id for trigger in triggers] == ["npc:assistant", "npc:surveyor", "npc:technician"]
    batches = queue.process_due(40)
    assert [batch.agent_id for batch in batches] == ["npc:assistant", "npc:surveyor", "npc:technician"]
    assert all(batch.reasons == ("EXTERNAL_EVENT",) for batch in batches)
    assert all(batch.source_refs == ("handoff-attempt:1",) for batch in batches)


def test_attempt_history_is_append_only_and_deterministic() -> None:
    handoff_ledger = _handoff_ledger()
    later = _attempt(attempt_id="handoff-attempt:z", at_tick=45, outcome=HandoffAttemptOutcome.RESOURCE_ABSENT)
    earlier = _attempt(attempt_id="handoff-attempt:a", at_tick=40)
    ledger = record_handoff_attempt(ResourceHandoffAttemptLedger(), handoff_ledger, later)
    ledger = record_handoff_attempt(ledger, handoff_ledger, earlier)

    assert [item.attempt_id for item in attempts_for_authorization(ledger, "handoff-auth:meter")] == [
        "handoff-attempt:a",
        "handoff-attempt:z",
    ]
    with pytest.raises(ValueError, match="duplicate"):
        record_handoff_attempt(ledger, handoff_ledger, earlier)
