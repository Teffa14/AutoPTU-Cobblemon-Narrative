from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffAppointmentNotice,
    register_handoff_appointment_notice,
)
from tools.global_npc_resource_handoff_rescheduling import (
    HandoffAuthorizationOperationalState,
    HandoffRescheduleDecisionKind,
    ResourceHandoffRescheduleDecision,
    ResourceHandoffRescheduleLedger,
    ResourceHandoffRescheduleProposal,
    create_successor_authorization,
    current_authorization_id,
    execute_current_authorized_handoff,
    operational_authorization_state,
    record_reschedule_decision,
    register_reschedule_proposal,
)
from tools.global_npc_resource_handoffs import (
    HandoffMode,
    ResourceCustodyTransfer,
    ResourceHandoffAuthorization,
    ResourceHandoffLedger,
    register_handoff_authorization,
)
from tools.global_npc_resources import ResourceState, WorldResource


def _foundation(deliver: bool = True):
    auth = ResourceHandoffAuthorization(
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
    handoffs = register_handoff_authorization(ResourceHandoffLedger(), auth)
    queue = InformationEventQueue(
        channels={"channel:phone": CommunicationChannel("channel:phone", "PHONE", 5)},
        ledgers={actor: KnowledgeLedger(actor) for actor in ("npc:teo", "npc:nerea", "npc:ema")},
    )
    record_direct_observation(
        queue.ledgers["npc:ema"],
        claim_id="claim:reschedule",
        subject="auth:old:appointment",
        value="RESCHEDULE_REQUEST",
        semantic_minute=40,
        confidence=100,
    )
    queue.schedule(
        event_id="delivery:reschedule",
        message_id="message:reschedule",
        sender_id="npc:ema",
        receiver_id="npc:teo",
        source_claim_id="claim:reschedule",
        new_claim_id="received:reschedule",
        channel_id="channel:phone",
        created_minute=40,
    )
    notice = ResourceHandoffAppointmentNotice(
        notice_id="notice:reschedule",
        authorization_id="auth:old",
        sender_actor_id="npc:ema",
        receiver_actor_id="npc:teo",
        kind=HandoffAppointmentNoticeKind.RESCHEDULE_REQUEST,
        source_claim_id="claim:reschedule",
        communication_event_id="delivery:reschedule",
        created_tick=40,
    )
    appointments = register_handoff_appointment_notice(ResourceHandoffAppointmentLedger(), handoffs, notice)
    if deliver:
        queue.process_due(45)
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
    reschedules = register_reschedule_proposal(
        ResourceHandoffRescheduleLedger(), handoffs, appointments, proposal
    )
    return handoffs, appointments, queue, reschedules


def _decision(kind: HandoffRescheduleDecisionKind = HandoffRescheduleDecisionKind.ACCEPT):
    return ResourceHandoffRescheduleDecision(
        decision_id=f"decision:{kind.value.lower()}",
        proposal_id="proposal:later",
        actor_id="npc:teo",
        kind=kind,
        at_tick=46,
    )


def test_undelivered_reschedule_request_cannot_be_decided() -> None:
    handoffs, appointments, queue, reschedules = _foundation(deliver=False)
    try:
        record_reschedule_decision(reschedules, appointments, queue, _decision())
        assert False, "expected delivery validation"
    except ValueError as exc:
        assert "not delivered" in str(exc)


def test_only_named_responder_can_decide_proposal() -> None:
    handoffs, appointments, queue, reschedules = _foundation()
    wrong_actor = ResourceHandoffRescheduleDecision(
        decision_id="decision:wrong",
        proposal_id="proposal:later",
        actor_id="npc:nerea",
        kind=HandoffRescheduleDecisionKind.ACCEPT,
        at_tick=46,
    )
    try:
        record_reschedule_decision(reschedules, appointments, queue, wrong_actor)
        assert False, "expected responder validation"
    except ValueError as exc:
        assert "responder" in str(exc)


def test_rejected_reschedule_does_not_create_successor_authorization() -> None:
    handoffs, appointments, queue, reschedules = _foundation()
    reschedules = record_reschedule_decision(reschedules, appointments, queue, _decision(HandoffRescheduleDecisionKind.REJECT))
    try:
        create_successor_authorization(
            reschedules,
            handoffs,
            proposal_id="proposal:later",
            successor_authorization_id="auth:new",
            replacement_id="replacement:1",
        )
        assert False, "expected accepted proposal requirement"
    except ValueError as exc:
        assert "not accepted" in str(exc)
    assert operational_authorization_state(reschedules, handoffs, "auth:old") == HandoffAuthorizationOperationalState.CURRENT


def test_accepted_reschedule_preserves_old_record_and_creates_successor() -> None:
    handoffs, appointments, queue, reschedules = _foundation()
    reschedules = record_reschedule_decision(reschedules, appointments, queue, _decision())
    reschedules, handoffs, successor = create_successor_authorization(
        reschedules,
        handoffs,
        proposal_id="proposal:later",
        successor_authorization_id="auth:new",
        replacement_id="replacement:1",
    )

    assert [item.authorization_id for item in handoffs.authorizations] == ["auth:new", "auth:old"]
    assert successor.handoff_location_ref == "place:field-office"
    assert successor.valid_from_tick == 90
    assert successor.valid_until_tick == 120
    assert successor.authority_ref == "decision:accept"
    assert operational_authorization_state(reschedules, handoffs, "auth:old") == HandoffAuthorizationOperationalState.SUPERSEDED
    assert operational_authorization_state(reschedules, handoffs, "auth:new") == HandoffAuthorizationOperationalState.CURRENT
    assert current_authorization_id(reschedules, "auth:old") == "auth:new"


def test_superseded_authorization_cannot_execute_through_operational_wrapper() -> None:
    handoffs, appointments, queue, reschedules = _foundation()
    reschedules = record_reschedule_decision(reschedules, appointments, queue, _decision())
    reschedules, handoffs, _ = create_successor_authorization(
        reschedules,
        handoffs,
        proposal_id="proposal:later",
        successor_authorization_id="auth:new",
        replacement_id="replacement:1",
    )
    resource = WorldResource(
        resource_id="resource:meter",
        capability_tags=frozenset({"FIELD_METER"}),
        quantity=1,
        state=ResourceState.AVAILABLE,
        location_ref="place:repair-row",
        holder_actor_id="npc:teo",
    )
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
    result = execute_current_authorized_handoff(reschedules, handoffs, resource, transfer)
    assert not result.accepted
    assert result.reason_code == "HANDOFF_AUTHORIZATION_SUPERSEDED"
    assert result.resource == resource


def test_successor_authorization_executes_only_in_new_window_and_location() -> None:
    handoffs, appointments, queue, reschedules = _foundation()
    reschedules = record_reschedule_decision(reschedules, appointments, queue, _decision())
    reschedules, handoffs, _ = create_successor_authorization(
        reschedules,
        handoffs,
        proposal_id="proposal:later",
        successor_authorization_id="auth:new",
        replacement_id="replacement:1",
    )
    resource = WorldResource(
        resource_id="resource:meter",
        capability_tags=frozenset({"FIELD_METER"}),
        quantity=1,
        state=ResourceState.AVAILABLE,
        location_ref="place:field-office",
        holder_actor_id="npc:teo",
    )
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
    result = execute_current_authorized_handoff(reschedules, handoffs, resource, transfer)
    assert result.accepted
    assert result.resource.holder_actor_id == "npc:ema"
