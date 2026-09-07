from tools.global_npc_ai import AgentMode, NpcAgentState, NpcIntent
from tools.global_npc_resource_recovery import derive_resource_recovery_options
from tools.global_npc_resources import (
    ResourceAwareIntent,
    ResourceRequirement,
    ResourceState,
    WorldResource,
)
from tools.global_npc_travel import RouteEdge


def _agent() -> NpcAgentState:
    return NpcAgentState(
        agent_id="npc:worker",
        mode=AgentMode.OFFSCREEN_NAMED,
        region_ref="region:test",
        location_ref="place:field-office",
    )


def _blocked_intent() -> ResourceAwareIntent:
    return ResourceAwareIntent(
        NpcIntent(
            intent_id="work:survey",
            kind="FIELD_SURVEY",
            base_priority=5,
            urgency=6,
            obligation=4,
        ),
        (ResourceRequirement("FIELD_METER", 1),),
    )


def test_ready_work_does_not_generate_recovery_options() -> None:
    result = derive_resource_recovery_options(
        _agent(),
        _blocked_intent(),
        (
            WorldResource(
                "resource:meter-local",
                frozenset({"FIELD_METER"}),
                location_ref="place:field-office",
            ),
        ),
    )

    assert result.blocked is False
    assert result.options == ()
    assert result.reason_codes == ("RESOURCE_REQUIREMENTS_ALREADY_SATISFIED",)


def test_known_holder_generates_request_without_transfer() -> None:
    resource = WorldResource(
        "resource:meter-held",
        frozenset({"FIELD_METER"}),
        state=ResourceState.IN_USE,
        location_ref="place:workshop",
        holder_actor_id="npc:technician",
    )
    result = derive_resource_recovery_options(_agent(), _blocked_intent(), (resource,))

    assert result.blocked is True
    assert len(result.options) == 1
    option = result.options[0]
    assert option.intent.kind == "REQUEST_RESOURCE"
    assert option.intent.target_ref == "npc:technician"
    assert option.resource_id == "resource:meter-held"
    assert option.request_target_actor_id == "npc:technician"
    assert resource.holder_actor_id == "npc:technician"


def test_other_actor_reservation_generates_wait_not_checkout() -> None:
    resource = WorldResource(
        "resource:meter-booked",
        frozenset({"FIELD_METER"}),
        state=ResourceState.RESERVED,
        location_ref="place:field-office",
        reserved_for_actor_id="npc:other",
    )
    result = derive_resource_recovery_options(_agent(), _blocked_intent(), (resource,))

    assert len(result.options) == 1
    assert result.options[0].intent.kind == "WAIT_FOR_RESOURCE"
    assert result.options[0].reason_code == "RESOURCE_RESERVED_FOR_OTHER_ACTOR"
    assert resource.reserved_for_actor_id == "npc:other"


def test_remote_resource_reserved_for_actor_uses_existing_travel_graph() -> None:
    resource = WorldResource(
        "resource:meter-reserved",
        frozenset({"FIELD_METER"}),
        state=ResourceState.RESERVED,
        location_ref="place:warehouse",
        reserved_for_actor_id="npc:worker",
    )
    edge = RouteEdge(
        edge_id="route:office-warehouse",
        from_node="place:field-office",
        to_node="place:warehouse",
        duration_minutes=18,
    )

    result = derive_resource_recovery_options(
        _agent(),
        _blocked_intent(),
        (resource,),
        route_edges=(edge,),
        semantic_minute=100,
    )

    assert len(result.options) == 1
    option = result.options[0]
    assert option.intent.kind == "TRAVEL_TO_RESERVED_RESOURCE"
    assert option.intent.target_ref == "place:warehouse"
    assert option.intent.travel_cost == 18
    assert option.destination_location_ref == "place:warehouse"


def test_reserved_remote_resource_without_route_fails_closed() -> None:
    resource = WorldResource(
        "resource:meter-reserved",
        frozenset({"FIELD_METER"}),
        state=ResourceState.RESERVED,
        location_ref="place:warehouse",
        reserved_for_actor_id="npc:worker",
    )
    result = derive_resource_recovery_options(_agent(), _blocked_intent(), (resource,))

    assert result.options == ()
    assert "RESERVED_RESOURCE_ROUTE_UNAVAILABLE" in result.reason_codes


def test_unreserved_remote_resource_does_not_imply_access_permission() -> None:
    resource = WorldResource(
        "resource:meter-remote",
        frozenset({"FIELD_METER"}),
        location_ref="place:warehouse",
    )
    edge = RouteEdge(
        edge_id="route:office-warehouse",
        from_node="place:field-office",
        to_node="place:warehouse",
        duration_minutes=10,
    )
    result = derive_resource_recovery_options(
        _agent(), _blocked_intent(), (resource,), route_edges=(edge,)
    )

    assert result.options == ()
    assert "REMOTE_RESOURCE_ACCESS_NOT_ESTABLISHED" in result.reason_codes


def test_depleted_resource_does_not_generate_false_recovery() -> None:
    resource = WorldResource(
        "resource:meter-depleted",
        frozenset({"FIELD_METER"}),
        state=ResourceState.DEPLETED,
        location_ref="place:field-office",
    )
    result = derive_resource_recovery_options(_agent(), _blocked_intent(), (resource,))

    assert result.options == ()
    assert result.reason_codes == ("NO_KNOWN_RESOURCE_CANDIDATE",)


def test_recovery_option_order_is_stable_by_intent_id() -> None:
    resources = (
        WorldResource(
            "resource:z-meter",
            frozenset({"FIELD_METER"}),
            state=ResourceState.IN_USE,
            holder_actor_id="npc:z-holder",
        ),
        WorldResource(
            "resource:a-meter",
            frozenset({"FIELD_METER"}),
            state=ResourceState.IN_USE,
            holder_actor_id="npc:a-holder",
        ),
    )
    result = derive_resource_recovery_options(_agent(), _blocked_intent(), resources)

    assert [option.resource_id for option in result.options] == [
        "resource:a-meter",
        "resource:z-meter",
    ]


def test_recovery_never_requests_autoptu() -> None:
    resource = WorldResource(
        "resource:meter-held",
        frozenset({"FIELD_METER"}),
        state=ResourceState.IN_USE,
        holder_actor_id="npc:technician",
    )
    result = derive_resource_recovery_options(_agent(), _blocked_intent(), (resource,))

    assert all(option.intent.requires_structured_mechanics is False for option in result.options)
