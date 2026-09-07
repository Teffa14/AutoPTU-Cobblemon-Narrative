from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Mapping

from tools.global_npc_ai import Decision, NpcAgentState, NpcIntent, choose_intent


class ResourceState(str, Enum):
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    IN_USE = "IN_USE"
    UNAVAILABLE = "UNAVAILABLE"
    DEPLETED = "DEPLETED"
    RETIRED = "RETIRED"


@dataclass(frozen=True)
class WorldResource:
    resource_id: str
    capability_refs: frozenset[str]
    quantity: int = 1
    state: ResourceState = ResourceState.AVAILABLE
    location_ref: str | None = None
    holder_actor_id: str | None = None
    reserved_for_actor_id: str | None = None


@dataclass(frozen=True)
class ResourceRequirement:
    capability_ref: str
    quantity: int = 1
    allow_held_by_actor: bool = True
    allow_at_actor_location: bool = True


@dataclass(frozen=True)
class ResourceAwareIntent:
    intent: NpcIntent
    requirements: tuple[ResourceRequirement, ...] = ()


@dataclass(frozen=True)
class RequirementAssessment:
    requirement: ResourceRequirement
    satisfied: bool
    resource_ids: tuple[str, ...] = ()
    reason_code: str = "RESOURCE_REQUIREMENT_SATISFIED"


@dataclass(frozen=True)
class ResourceGateResult:
    decision: Decision
    ready_intent_ids: tuple[str, ...]
    blocked_intent_ids: tuple[str, ...]
    assessments_by_intent: Mapping[str, tuple[RequirementAssessment, ...]]


def _resource_accessible(
    agent: NpcAgentState,
    resource: WorldResource,
    requirement: ResourceRequirement,
) -> bool:
    if resource.state in {
        ResourceState.UNAVAILABLE,
        ResourceState.DEPLETED,
        ResourceState.RETIRED,
    }:
        return False

    if resource.reserved_for_actor_id not in {None, agent.agent_id}:
        return False

    if resource.state == ResourceState.RESERVED and resource.reserved_for_actor_id != agent.agent_id:
        return False

    held = requirement.allow_held_by_actor and resource.holder_actor_id == agent.agent_id
    local = (
        requirement.allow_at_actor_location
        and resource.location_ref is not None
        and resource.location_ref == agent.location_ref
        and resource.holder_actor_id in {None, agent.agent_id}
    )
    return held or local


def assess_requirement(
    agent: NpcAgentState,
    requirement: ResourceRequirement,
    resources: Iterable[WorldResource],
) -> RequirementAssessment:
    if requirement.quantity <= 0:
        raise ValueError("resource requirement quantity must be positive")

    all_resources = sorted(resources, key=lambda resource: resource.resource_id)
    capability_matches = [
        resource
        for resource in all_resources
        if requirement.capability_ref in resource.capability_refs
    ]
    if not capability_matches:
        return RequirementAssessment(
            requirement,
            False,
            reason_code="MISSING_RESOURCE_CAPABILITY",
        )

    unreserved_matches = [
        resource
        for resource in capability_matches
        if resource.reserved_for_actor_id in {None, agent.agent_id}
        and not (
            resource.state == ResourceState.RESERVED
            and resource.reserved_for_actor_id != agent.agent_id
        )
    ]
    if not unreserved_matches:
        return RequirementAssessment(
            requirement,
            False,
            reason_code="RESOURCE_RESERVED_FOR_OTHER_ACTOR",
        )

    accessible = [
        resource
        for resource in unreserved_matches
        if _resource_accessible(agent, resource, requirement)
    ]
    if not accessible:
        return RequirementAssessment(
            requirement,
            False,
            reason_code="RESOURCE_NOT_LOCALLY_AVAILABLE",
        )

    selected: list[str] = []
    total = 0
    for resource in accessible:
        if resource.state in {
            ResourceState.UNAVAILABLE,
            ResourceState.DEPLETED,
            ResourceState.RETIRED,
        }:
            continue
        if resource.quantity <= 0:
            continue
        selected.append(resource.resource_id)
        total += resource.quantity
        if total >= requirement.quantity:
            return RequirementAssessment(
                requirement,
                True,
                tuple(selected),
                "RESOURCE_REQUIREMENT_SATISFIED",
            )

    return RequirementAssessment(
        requirement,
        False,
        tuple(selected),
        "INSUFFICIENT_RESOURCE_QUANTITY",
    )


def assess_resource_aware_intent(
    agent: NpcAgentState,
    resource_intent: ResourceAwareIntent,
    resources: Iterable[WorldResource],
) -> tuple[bool, tuple[RequirementAssessment, ...]]:
    resource_list = tuple(resources)
    assessments = tuple(
        assess_requirement(agent, requirement, resource_list)
        for requirement in resource_intent.requirements
    )
    return all(assessment.satisfied for assessment in assessments), assessments


def choose_resource_aware_intent(
    agent: NpcAgentState,
    resource_intents: Iterable[ResourceAwareIntent],
    resources: Iterable[WorldResource],
) -> ResourceGateResult:
    """Filter world intents by resource readiness, then reuse the base planner.

    This function does not reserve, consume, transfer or mutate resources.
    Tactical item legality and effects remain outside this world-agent layer.
    """
    resource_list = tuple(resources)
    ready: list[NpcIntent] = []
    ready_ids: list[str] = []
    blocked_ids: list[str] = []
    assessments: dict[str, tuple[RequirementAssessment, ...]] = {}

    for wrapped in resource_intents:
        is_ready, intent_assessments = assess_resource_aware_intent(
            agent, wrapped, resource_list
        )
        assessments[wrapped.intent.intent_id] = intent_assessments
        if is_ready:
            ready.append(wrapped.intent)
            ready_ids.append(wrapped.intent.intent_id)
        else:
            blocked_ids.append(wrapped.intent.intent_id)

    decision = choose_intent(agent, ready)
    if decision.kind == "WAIT" and blocked_ids:
        decision = Decision(
            agent_id=decision.agent_id,
            intent_id=None,
            kind="WAIT_RESOURCE",
            score=None,
            handoff=decision.handoff,
            reason_codes=("NO_RESOURCE_READY_INTENT",),
            target_ref=None,
        )

    return ResourceGateResult(
        decision=decision,
        ready_intent_ids=tuple(sorted(ready_ids)),
        blocked_intent_ids=tuple(sorted(blocked_ids)),
        assessments_by_intent=assessments,
    )
