from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from tools.global_npc_ai import NpcAgentState, NpcIntent
from tools.global_npc_resources import (
    ResourceAwareIntent,
    ResourceRequirement,
    ResourceState,
    WorldResource,
    assess_resource_aware_intent,
)
from tools.global_npc_travel import RouteEdge, build_travel_plan


@dataclass(frozen=True)
class ResourceRecoveryOption:
    intent: NpcIntent
    requirement: ResourceRequirement
    resource_id: str
    reason_code: str
    destination_location_ref: str | None = None
    request_target_actor_id: str | None = None


@dataclass(frozen=True)
class ResourceRecoveryResult:
    blocked_intent_id: str
    blocked: bool
    options: tuple[ResourceRecoveryOption, ...]
    reason_codes: tuple[str, ...]


def _usable_candidate(resource: WorldResource, requirement: ResourceRequirement) -> bool:
    return (
        requirement.capability_ref in resource.capability_refs
        and resource.quantity >= requirement.quantity
        and resource.state
        not in {
            ResourceState.UNAVAILABLE,
            ResourceState.DEPLETED,
            ResourceState.RETIRED,
        }
    )


def derive_resource_recovery_options(
    agent: NpcAgentState,
    blocked_intent: ResourceAwareIntent,
    resources: Iterable[WorldResource],
    *,
    route_edges: Iterable[RouteEdge] = (),
    semantic_minute: int = 0,
) -> ResourceRecoveryResult:
    """Derive world-level recovery intents for resource-blocked work.

    The result proposes communication, travel or waiting. It never transfers,
    reserves, checks out, consumes or grants permission to use a resource.
    Structured PTU resolution remains outside this layer.
    """
    resource_list = tuple(sorted(resources, key=lambda item: item.resource_id))
    is_ready, assessments = assess_resource_aware_intent(
        agent, blocked_intent, resource_list
    )
    if is_ready:
        return ResourceRecoveryResult(
            blocked_intent.intent.intent_id,
            False,
            (),
            ("RESOURCE_REQUIREMENTS_ALREADY_SATISFIED",),
        )

    edges = tuple(route_edges)
    options: list[ResourceRecoveryOption] = []
    unresolved_reason_codes: set[str] = set()

    for assessment in assessments:
        if assessment.satisfied:
            continue
        requirement = assessment.requirement
        candidates = [
            resource
            for resource in resource_list
            if _usable_candidate(resource, requirement)
        ]
        if not candidates:
            unresolved_reason_codes.add("NO_KNOWN_RESOURCE_CANDIDATE")
            continue

        produced_for_requirement = False
        for resource in candidates:
            if resource.holder_actor_id not in {None, agent.agent_id}:
                target_actor = resource.holder_actor_id
                options.append(
                    ResourceRecoveryOption(
                        intent=NpcIntent(
                            intent_id=(
                                f"resource-request:{blocked_intent.intent.intent_id}:"
                                f"{resource.resource_id}:{target_actor}"
                            ),
                            kind="REQUEST_RESOURCE",
                            base_priority=max(1, blocked_intent.intent.base_priority),
                            urgency=blocked_intent.intent.urgency,
                            obligation=blocked_intent.intent.obligation,
                            relationship_weight=blocked_intent.intent.relationship_weight,
                            target_ref=target_actor,
                        ),
                        requirement=requirement,
                        resource_id=resource.resource_id,
                        reason_code="RESOURCE_HELD_BY_OTHER_ACTOR",
                        request_target_actor_id=target_actor,
                    )
                )
                produced_for_requirement = True
                continue

            if resource.reserved_for_actor_id not in {None, agent.agent_id}:
                options.append(
                    ResourceRecoveryOption(
                        intent=NpcIntent(
                            intent_id=(
                                f"resource-wait:{blocked_intent.intent.intent_id}:"
                                f"{resource.resource_id}"
                            ),
                            kind="WAIT_FOR_RESOURCE",
                            base_priority=1,
                            urgency=blocked_intent.intent.urgency,
                            obligation=blocked_intent.intent.obligation,
                            target_ref=resource.resource_id,
                        ),
                        requirement=requirement,
                        resource_id=resource.resource_id,
                        reason_code="RESOURCE_RESERVED_FOR_OTHER_ACTOR",
                    )
                )
                produced_for_requirement = True
                continue

            if (
                resource.reserved_for_actor_id == agent.agent_id
                and resource.location_ref
                and resource.location_ref != agent.location_ref
                and resource.holder_actor_id is None
            ):
                plan = build_travel_plan(
                    agent,
                    edges,
                    destination_node=resource.location_ref,
                    semantic_minute=semantic_minute,
                    plan_id=(
                        f"resource-travel:{blocked_intent.intent.intent_id}:"
                        f"{resource.resource_id}"
                    ),
                    reason_ref=blocked_intent.intent.intent_id,
                )
                if plan is None:
                    unresolved_reason_codes.add("RESERVED_RESOURCE_ROUTE_UNAVAILABLE")
                    continue
                options.append(
                    ResourceRecoveryOption(
                        intent=NpcIntent(
                            intent_id=plan.plan_id,
                            kind="TRAVEL_TO_RESERVED_RESOURCE",
                            base_priority=max(1, blocked_intent.intent.base_priority),
                            urgency=blocked_intent.intent.urgency,
                            obligation=blocked_intent.intent.obligation,
                            travel_cost=max(0, plan.expected_arrival_minute - plan.departure_minute),
                            target_ref=resource.location_ref,
                        ),
                        requirement=requirement,
                        resource_id=resource.resource_id,
                        reason_code="RESERVED_RESOURCE_AT_REMOTE_LOCATION",
                        destination_location_ref=resource.location_ref,
                    )
                )
                produced_for_requirement = True
                continue

            if resource.location_ref and resource.location_ref != agent.location_ref:
                unresolved_reason_codes.add("REMOTE_RESOURCE_ACCESS_NOT_ESTABLISHED")

        if not produced_for_requirement and not unresolved_reason_codes:
            unresolved_reason_codes.add("NO_SAFE_RESOURCE_RECOVERY_OPTION")

    options.sort(key=lambda option: option.intent.intent_id)
    reasons = tuple(sorted(unresolved_reason_codes)) or (
        "RESOURCE_RECOVERY_OPTIONS_DERIVED",
    )
    return ResourceRecoveryResult(
        blocked_intent.intent.intent_id,
        True,
        tuple(options),
        reasons,
    )
