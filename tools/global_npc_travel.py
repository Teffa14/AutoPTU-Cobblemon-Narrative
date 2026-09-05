from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
import heapq
import json
import sys
from pathlib import Path
from typing import Iterable, Mapping

from tools.global_npc_ai import AgentMode, Handoff, NpcAgentState


class TravelDecisionKind(str, Enum):
    ALREADY_AT_DESTINATION = "ALREADY_AT_DESTINATION"
    WAIT_BEFORE_DEPARTURE = "WAIT_BEFORE_DEPARTURE"
    DEPART_NOW = "DEPART_NOW"
    TRAVEL_IN_PROGRESS = "TRAVEL_IN_PROGRESS"
    ARRIVED = "ARRIVED"
    REPLAN_REQUIRED = "REPLAN_REQUIRED"
    TRAVEL_BLOCKED = "TRAVEL_BLOCKED"
    PROJECT_LOCAL_TRAVEL = "PROJECT_LOCAL_TRAVEL"
    REQUEST_AUTOPTU = "REQUEST_AUTOPTU"
    HOLD_AUTOPTU = "HOLD_AUTOPTU"
    COMMITMENT_AT_RISK = "COMMITMENT_AT_RISK"


@dataclass(frozen=True)
class RouteEdge:
    edge_id: str
    from_node: str
    to_node: str
    duration_minutes: int
    enabled: bool = True
    requires_local_projection: bool = False
    requires_structured_resolution: bool = False
    required_knowledge: frozenset[str] = frozenset()
    required_permissions: frozenset[str] = frozenset()


@dataclass(frozen=True)
class TravelPlan:
    plan_id: str
    agent_id: str
    origin_node: str
    destination_node: str
    edge_ids: tuple[str, ...]
    departure_minute: int
    expected_arrival_minute: int
    reason_ref: str | None = None
    commitment_start_minute: int | None = None
    arrival_buffer_minutes: int = 0


@dataclass(frozen=True)
class TravelState:
    plan: TravelPlan
    current_node: str
    next_edge_index: int = 0
    edge_started_minute: int | None = None
    semantic_minute: int = 0
    blocked_edge_id: str | None = None


@dataclass(frozen=True)
class TravelDecision:
    kind: TravelDecisionKind
    agent_id: str
    semantic_minute: int
    current_node: str
    destination_node: str
    edge_id: str | None = None
    eta_minute: int | None = None
    handoff: Handoff = Handoff.NONE
    reason_codes: tuple[str, ...] = ()


def _eligible(agent: NpcAgentState, edge: RouteEdge) -> bool:
    return edge.enabled and edge.required_knowledge.issubset(agent.knowledge) and edge.required_permissions.issubset(agent.permissions)


def shortest_route(agent: NpcAgentState, edges: Iterable[RouteEdge], origin: str, destination: str) -> tuple[tuple[str, ...], int] | None:
    """Deterministic semantic world route search.

    This is graph-level travel planning. It is not Minecraft pathfinding and does
    not resolve PTU movement squares, capabilities, interception or forced movement.
    """
    if origin == destination:
        return (), 0

    outgoing: dict[str, list[RouteEdge]] = {}
    for edge in edges:
        if edge.duration_minutes <= 0:
            raise ValueError("route duration must be positive")
        if _eligible(agent, edge):
            outgoing.setdefault(edge.from_node, []).append(edge)
    for values in outgoing.values():
        values.sort(key=lambda e: e.edge_id)

    queue: list[tuple[int, tuple[str, ...], str]] = [(0, (), origin)]
    best: dict[str, tuple[int, tuple[str, ...]]] = {origin: (0, ())}
    while queue:
        cost, path, node = heapq.heappop(queue)
        if best.get(node) != (cost, path):
            continue
        if node == destination:
            return path, cost
        for edge in outgoing.get(node, ()):
            next_cost = cost + edge.duration_minutes
            next_path = path + (edge.edge_id,)
            prior = best.get(edge.to_node)
            candidate = (next_cost, next_path)
            if prior is None or candidate < prior:
                best[edge.to_node] = candidate
                heapq.heappush(queue, (next_cost, next_path, edge.to_node))
    return None


def build_travel_plan(
    agent: NpcAgentState,
    edges: Iterable[RouteEdge],
    *,
    destination_node: str,
    semantic_minute: int,
    plan_id: str,
    reason_ref: str | None = None,
    commitment_start_minute: int | None = None,
    arrival_buffer_minutes: int = 0,
) -> TravelPlan | None:
    route = shortest_route(agent, edges, agent.location_ref, destination_node)
    if route is None:
        return None
    edge_ids, duration = route
    buffer_minutes = max(0, arrival_buffer_minutes)
    if commitment_start_minute is None:
        departure = semantic_minute
    else:
        departure = max(semantic_minute, commitment_start_minute - buffer_minutes - duration)
    return TravelPlan(
        plan_id=plan_id,
        agent_id=agent.agent_id,
        origin_node=agent.location_ref,
        destination_node=destination_node,
        edge_ids=edge_ids,
        departure_minute=departure,
        expected_arrival_minute=departure + duration,
        reason_ref=reason_ref,
        commitment_start_minute=commitment_start_minute,
        arrival_buffer_minutes=buffer_minutes,
    )


def commitment_at_risk(plan: TravelPlan) -> bool:
    if plan.commitment_start_minute is None:
        return False
    return plan.expected_arrival_minute > plan.commitment_start_minute - plan.arrival_buffer_minutes


def _edge_map(edges: Iterable[RouteEdge]) -> dict[str, RouteEdge]:
    return {edge.edge_id: edge for edge in edges}


def advance_travel(
    agent: NpcAgentState,
    state: TravelState,
    edges: Iterable[RouteEdge],
    *,
    semantic_minute: int,
) -> tuple[TravelState, TravelDecision]:
    if agent.mode == AgentMode.AUTOPTU_BOUND:
        return state, TravelDecision(
            TravelDecisionKind.HOLD_AUTOPTU,
            agent.agent_id,
            semantic_minute,
            state.current_node,
            state.plan.destination_node,
            handoff=Handoff.HOLD_EXISTING_AUTOPTU_BINDING,
            reason_codes=("AUTOPTU_ALREADY_OWNS_STRUCTURED_RESOLUTION",),
        )

    if state.current_node == state.plan.destination_node:
        return state, TravelDecision(
            TravelDecisionKind.ARRIVED,
            agent.agent_id,
            semantic_minute,
            state.current_node,
            state.plan.destination_node,
            eta_minute=semantic_minute,
            reason_codes=("DESTINATION_REACHED",),
        )

    if semantic_minute < state.plan.departure_minute and state.next_edge_index == 0:
        return replace(state, semantic_minute=semantic_minute), TravelDecision(
            TravelDecisionKind.WAIT_BEFORE_DEPARTURE,
            agent.agent_id,
            semantic_minute,
            state.current_node,
            state.plan.destination_node,
            eta_minute=state.plan.expected_arrival_minute,
            reason_codes=("TRAVEL_TIME_RESERVED",),
        )

    edge_by_id = _edge_map(edges)
    if state.next_edge_index >= len(state.plan.edge_ids):
        return state, TravelDecision(
            TravelDecisionKind.TRAVEL_BLOCKED,
            agent.agent_id,
            semantic_minute,
            state.current_node,
            state.plan.destination_node,
            reason_codes=("ROUTE_STATE_INCOMPLETE",),
        )

    edge_id = state.plan.edge_ids[state.next_edge_index]
    edge = edge_by_id.get(edge_id)
    if edge is None or not _eligible(agent, edge) or edge.from_node != state.current_node:
        return replace(state, semantic_minute=semantic_minute, blocked_edge_id=edge_id), TravelDecision(
            TravelDecisionKind.REPLAN_REQUIRED,
            agent.agent_id,
            semantic_minute,
            state.current_node,
            state.plan.destination_node,
            edge_id=edge_id,
            reason_codes=("PLANNED_EDGE_UNAVAILABLE",),
        )

    if edge.requires_structured_resolution:
        return replace(state, semantic_minute=semantic_minute), TravelDecision(
            TravelDecisionKind.REQUEST_AUTOPTU,
            agent.agent_id,
            semantic_minute,
            state.current_node,
            state.plan.destination_node,
            edge_id=edge.edge_id,
            handoff=Handoff.REQUEST_AUTOPTU,
            reason_codes=("STRUCTURED_RESOLUTION_REQUIRED", "WORLD_TRAVEL_PAUSED"),
        )

    if edge.requires_local_projection:
        return replace(state, semantic_minute=semantic_minute), TravelDecision(
            TravelDecisionKind.PROJECT_LOCAL_TRAVEL,
            agent.agent_id,
            semantic_minute,
            state.current_node,
            state.plan.destination_node,
            edge_id=edge.edge_id,
            reason_codes=("LOCAL_GEOMETRY_OR_PRESENTATION_REQUIRED",),
        )

    start = state.edge_started_minute
    if start is None:
        start = max(semantic_minute, state.plan.departure_minute)
        new_state = replace(state, edge_started_minute=start, semantic_minute=semantic_minute)
        return new_state, TravelDecision(
            TravelDecisionKind.DEPART_NOW,
            agent.agent_id,
            semantic_minute,
            state.current_node,
            state.plan.destination_node,
            edge_id=edge.edge_id,
            eta_minute=state.plan.expected_arrival_minute,
            reason_codes=("SEMANTIC_EDGE_TRAVEL_STARTED",),
        )

    finish = start + edge.duration_minutes
    if semantic_minute < finish:
        return replace(state, semantic_minute=semantic_minute), TravelDecision(
            TravelDecisionKind.TRAVEL_IN_PROGRESS,
            agent.agent_id,
            semantic_minute,
            state.current_node,
            state.plan.destination_node,
            edge_id=edge.edge_id,
            eta_minute=state.plan.expected_arrival_minute,
            reason_codes=("OFFSCREEN_SEMANTIC_TRAVEL",),
        )

    next_index = state.next_edge_index + 1
    arrived = edge.to_node == state.plan.destination_node and next_index == len(state.plan.edge_ids)
    new_state = replace(
        state,
        current_node=edge.to_node,
        next_edge_index=next_index,
        edge_started_minute=None,
        semantic_minute=semantic_minute,
        blocked_edge_id=None,
    )
    kind = TravelDecisionKind.ARRIVED if arrived else TravelDecisionKind.TRAVEL_IN_PROGRESS
    return new_state, TravelDecision(
        kind,
        agent.agent_id,
        semantic_minute,
        edge.to_node,
        state.plan.destination_node,
        edge_id=edge.edge_id,
        eta_minute=semantic_minute if arrived else state.plan.expected_arrival_minute,
        reason_codes=("SEMANTIC_EDGE_COMPLETED", "DESTINATION_REACHED") if arrived else ("SEMANTIC_EDGE_COMPLETED",),
    )


def replan_from_state(
    agent: NpcAgentState,
    state: TravelState,
    edges: Iterable[RouteEdge],
    *,
    semantic_minute: int,
) -> TravelState | None:
    local_agent = replace(agent, location_ref=state.current_node)
    plan = build_travel_plan(
        local_agent,
        edges,
        destination_node=state.plan.destination_node,
        semantic_minute=semantic_minute,
        plan_id=state.plan.plan_id,
        reason_ref=state.plan.reason_ref,
        commitment_start_minute=state.plan.commitment_start_minute,
        arrival_buffer_minutes=state.plan.arrival_buffer_minutes,
    )
    if plan is None:
        return None
    return TravelState(plan=plan, current_node=state.current_node, semantic_minute=semantic_minute)


def edge_from_dict(data: Mapping[str, object]) -> RouteEdge:
    return RouteEdge(
        edge_id=str(data["edge_id"]),
        from_node=str(data["from_node"]),
        to_node=str(data["to_node"]),
        duration_minutes=int(data["duration_minutes"]),
        enabled=bool(data.get("enabled", True)),
        requires_local_projection=bool(data.get("requires_local_projection", False)),
        requires_structured_resolution=bool(data.get("requires_structured_resolution", False)),
        required_knowledge=frozenset(str(v) for v in data.get("required_knowledge", [])),
        required_permissions=frozenset(str(v) for v in data.get("required_permissions", [])),
    )


def _run_fixture(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    for case in payload.get("route_cases", []):
        agent = NpcAgentState(
            agent_id=case["agent_id"],
            mode=AgentMode(case.get("mode", "OFFSCREEN_NAMED")),
            region_ref=case["region_ref"],
            location_ref=case["origin_node"],
            knowledge=frozenset(case.get("knowledge", [])),
            permissions=frozenset(case.get("permissions", [])),
        )
        edges = [edge_from_dict(row) for row in case["edges"]]
        plan = build_travel_plan(
            agent,
            edges,
            destination_node=case["destination_node"],
            semantic_minute=int(case["semantic_minute"]),
            plan_id=case["case_id"],
            commitment_start_minute=case.get("commitment_start_minute"),
            arrival_buffer_minutes=int(case.get("arrival_buffer_minutes", 0)),
        )
        expected = case.get("expected_edge_ids")
        if expected is None:
            assert plan is None, case["case_id"]
        else:
            assert plan is not None, case["case_id"]
            assert list(plan.edge_ids) == expected, case["case_id"]
            if "expected_departure_minute" in case:
                assert plan.departure_minute == case["expected_departure_minute"], case["case_id"]
            if "expected_arrival_minute" in case:
                assert plan.expected_arrival_minute == case["expected_arrival_minute"], case["case_id"]
    print(f"global NPC travel fixture OK: {path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python -m tools.global_npc_travel <fixture.json>")
    _run_fixture(Path(sys.argv[1]))
