import unittest
from dataclasses import replace
from pathlib import Path

from tools.global_npc_ai import AgentMode, Handoff, NpcAgentState
from tools.global_npc_travel import (
    RouteEdge,
    TravelDecisionKind,
    TravelState,
    advance_travel,
    build_travel_plan,
    commitment_at_risk,
    replan_from_state,
    shortest_route,
)


class GlobalNpcTravelTests(unittest.TestCase):
    def agent(self, *, location="a", mode=AgentMode.OFFSCREEN_NAMED, knowledge=(), permissions=()):
        return NpcAgentState(
            agent_id="fixture.agent",
            mode=mode,
            region_ref="fixture.region",
            location_ref=location,
            knowledge=frozenset(knowledge),
            permissions=frozenset(permissions),
        )

    def test_shortest_route_is_deterministic(self):
        edges = [
            RouteEdge("b-path", "a", "c", 10),
            RouteEdge("a-path", "a", "b", 5),
            RouteEdge("b-finish", "b", "c", 5),
        ]
        first = shortest_route(self.agent(), edges, "a", "c")
        second = shortest_route(self.agent(), reversed(edges), "a", "c")
        self.assertEqual(first, second)
        self.assertEqual(("a-path", "b-finish"), first[0])

    def test_commitment_reserves_departure_time(self):
        plan = build_travel_plan(
            self.agent(),
            [RouteEdge("road", "a", "b", 45)],
            destination_node="b",
            semantic_minute=500,
            plan_id="meeting",
            commitment_start_minute=600,
            arrival_buffer_minutes=10,
        )
        self.assertEqual(545, plan.departure_minute)
        self.assertEqual(590, plan.expected_arrival_minute)
        self.assertFalse(commitment_at_risk(plan))

    def test_late_planning_does_not_teleport_to_commitment(self):
        plan = build_travel_plan(
            self.agent(),
            [RouteEdge("road", "a", "b", 45)],
            destination_node="b",
            semantic_minute=580,
            plan_id="late-meeting",
            commitment_start_minute=600,
            arrival_buffer_minutes=10,
        )
        self.assertEqual(580, plan.departure_minute)
        self.assertEqual(625, plan.expected_arrival_minute)
        self.assertTrue(commitment_at_risk(plan))
        self.assertEqual("a", self.agent().location_ref)

    def test_unknown_shortcut_cannot_be_used(self):
        edges = [
            RouteEdge("secret", "a", "b", 2, required_knowledge=frozenset({"secret.route"})),
            RouteEdge("public", "a", "b", 10),
        ]
        self.assertEqual(("public",), shortest_route(self.agent(), edges, "a", "b")[0])
        self.assertEqual(("secret",), shortest_route(self.agent(knowledge={"secret.route"}), edges, "a", "b")[0])

    def test_offscreen_travel_progresses_only_after_semantic_duration(self):
        agent = self.agent()
        edge = RouteEdge("road", "a", "b", 20)
        plan = build_travel_plan(agent, [edge], destination_node="b", semantic_minute=100, plan_id="p")
        state = TravelState(plan, "a", semantic_minute=100)
        state, decision = advance_travel(agent, state, [edge], semantic_minute=100)
        self.assertEqual(TravelDecisionKind.DEPART_NOW, decision.kind)
        state, decision = advance_travel(agent, state, [edge], semantic_minute=119)
        self.assertEqual(TravelDecisionKind.TRAVEL_IN_PROGRESS, decision.kind)
        self.assertEqual("a", state.current_node)
        state, decision = advance_travel(agent, state, [edge], semantic_minute=120)
        self.assertEqual(TravelDecisionKind.ARRIVED, decision.kind)
        self.assertEqual("b", state.current_node)

    def test_closed_edge_requires_replan_and_alternate_route_updates_eta(self):
        agent = self.agent()
        initial_edges = [RouteEdge("fast", "a", "b", 10)]
        plan = build_travel_plan(agent, initial_edges, destination_node="b", semantic_minute=100, plan_id="p")
        state = TravelState(plan, "a", semantic_minute=100)
        closed = [
            RouteEdge("fast", "a", "b", 10, enabled=False),
            RouteEdge("detour-1", "a", "c", 12),
            RouteEdge("detour-2", "c", "b", 13),
        ]
        state, decision = advance_travel(agent, state, closed, semantic_minute=100)
        self.assertEqual(TravelDecisionKind.REPLAN_REQUIRED, decision.kind)
        replanned = replan_from_state(agent, state, closed, semantic_minute=100)
        self.assertEqual(("detour-1", "detour-2"), replanned.plan.edge_ids)
        self.assertEqual(125, replanned.plan.expected_arrival_minute)

    def test_no_alternative_route_is_blocked_not_teleport(self):
        agent = self.agent()
        plan = build_travel_plan(agent, [RouteEdge("road", "a", "b", 10)], destination_node="b", semantic_minute=1, plan_id="p")
        state = TravelState(plan, "a")
        unavailable = [RouteEdge("road", "a", "b", 10, enabled=False)]
        state, decision = advance_travel(agent, state, unavailable, semantic_minute=1)
        self.assertEqual(TravelDecisionKind.REPLAN_REQUIRED, decision.kind)
        self.assertIsNone(replan_from_state(agent, state, unavailable, semantic_minute=1))
        self.assertEqual("a", state.current_node)

    def test_local_projection_edge_is_not_resolved_offscreen(self):
        agent = self.agent()
        edge = RouteEdge("local-crossing", "a", "b", 5, requires_local_projection=True)
        plan = build_travel_plan(agent, [edge], destination_node="b", semantic_minute=10, plan_id="p")
        state, decision = advance_travel(agent, TravelState(plan, "a"), [edge], semantic_minute=10)
        self.assertEqual(TravelDecisionKind.PROJECT_LOCAL_TRAVEL, decision.kind)
        self.assertEqual("a", state.current_node)

    def test_structured_edge_requests_autoptu_and_freezes_world_travel(self):
        agent = self.agent()
        edge = RouteEdge("structured-crossing", "a", "b", 5, requires_structured_resolution=True)
        plan = build_travel_plan(agent, [edge], destination_node="b", semantic_minute=10, plan_id="p")
        state, decision = advance_travel(agent, TravelState(plan, "a"), [edge], semantic_minute=10)
        self.assertEqual(TravelDecisionKind.REQUEST_AUTOPTU, decision.kind)
        self.assertEqual(Handoff.REQUEST_AUTOPTU, decision.handoff)
        self.assertEqual("a", state.current_node)

    def test_existing_autoptu_binding_holds_travel(self):
        agent = replace(self.agent(), mode=AgentMode.AUTOPTU_BOUND, active_autoptu_binding="battle:1")
        edge = RouteEdge("road", "a", "b", 5)
        plan = build_travel_plan(replace(agent, mode=AgentMode.OFFSCREEN_NAMED, active_autoptu_binding=None), [edge], destination_node="b", semantic_minute=10, plan_id="p")
        state, decision = advance_travel(agent, TravelState(plan, "a"), [edge], semantic_minute=20)
        self.assertEqual(TravelDecisionKind.HOLD_AUTOPTU, decision.kind)
        self.assertEqual(Handoff.HOLD_EXISTING_AUTOPTU_BINDING, decision.handoff)
        self.assertEqual("a", state.current_node)

    def test_core_travel_module_has_no_authored_region_special_case(self):
        text = Path("tools/global_npc_travel.py").read_text(encoding="utf-8").lower()
        for forbidden in ("marea", "sendero", "puerto bruma", "loma clara"):
            self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
