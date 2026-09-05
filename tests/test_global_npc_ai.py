import inspect
import json
import unittest
from pathlib import Path

from tools.global_npc_ai import (
    AgentMode,
    Handoff,
    NpcAgentState,
    NpcIntent,
    bind_autoptu,
    choose_intent,
    receive_information,
    release_autoptu,
    run_fixture,
)


class GlobalNpcAiTests(unittest.TestCase):
    def test_core_is_region_neutral(self):
        import tools.global_npc_ai as module

        source = inspect.getsource(module).lower()
        for local_name in ("marea", "sendero", "puerto bruma", "loma clara"):
            self.assertNotIn(local_name, source)

    def test_same_planner_works_in_unrelated_fixture_regions(self):
        intents = [
            NpcIntent("work", "WORK", base_priority=5, obligation=3),
            NpcIntent("social", "SOCIALIZE", base_priority=5),
        ]
        north = NpcAgentState(
            "npc:north",
            AgentMode.OFFSCREEN_NAMED,
            "fixture:region:north",
            "fixture:site:n1",
        )
        south = NpcAgentState(
            "npc:south",
            AgentMode.OFFSCREEN_NAMED,
            "fixture:region:south",
            "fixture:site:s1",
        )
        self.assertEqual(choose_intent(north, intents).kind, "WORK")
        self.assertEqual(choose_intent(south, intents).kind, "WORK")

    def test_hidden_fact_does_not_enter_npc_knowledge(self):
        agent = NpcAgentState(
            "npc:1", AgentMode.LOCAL_ACTIVE, "fixture:r", "fixture:s"
        )
        react = NpcIntent(
            "warn",
            "REPORT",
            base_priority=50,
            required_knowledge=frozenset({"claim:ecology-risk"}),
        )
        fallback = NpcIntent("routine", "WORK", base_priority=1)
        self.assertEqual(choose_intent(agent, [react, fallback]).kind, "WORK")

    def test_received_information_can_change_decision(self):
        agent = NpcAgentState(
            "npc:1", AgentMode.LOCAL_ACTIVE, "fixture:r", "fixture:s"
        )
        intents = [
            NpcIntent(
                "warn",
                "REPORT",
                base_priority=50,
                required_knowledge=frozenset({"claim:risk"}),
            ),
            NpcIntent("routine", "WORK", base_priority=1),
        ]
        before = choose_intent(agent, intents)
        informed = receive_information(
            agent, claim_ref="claim:risk", provenance_ref="obs:22"
        )
        after = choose_intent(informed, intents)
        self.assertEqual(before.kind, "WORK")
        self.assertEqual(after.kind, "REPORT")
        self.assertIn("obs:22", informed.memory_refs)

    def test_emergency_can_override_schedule(self):
        agent = NpcAgentState(
            "npc:1", AgentMode.OFFSCREEN_NAMED, "fixture:r", "fixture:s"
        )
        scheduled = NpcIntent(
            "scheduled-shift", "WORK", base_priority=10, obligation=5
        )
        emergency = NpcIntent(
            "emergency", "RESPOND_EMERGENCY", base_priority=10, urgency=10
        )
        self.assertEqual(
            choose_intent(agent, [scheduled, emergency]).kind,
            "RESPOND_EMERGENCY",
        )

    def test_offscreen_agent_does_not_require_minecraft_entity_for_world_work(self):
        agent = NpcAgentState(
            "npc:1", AgentMode.OFFSCREEN_NAMED, "fixture:r", "fixture:s"
        )
        intent = NpcIntent(
            "travel-plan", "TRAVEL", base_priority=10, requires_local_projection=False
        )
        self.assertEqual(choose_intent(agent, [intent]).kind, "TRAVEL")

    def test_offscreen_agent_cannot_choose_local_projection_only_action(self):
        agent = NpcAgentState(
            "npc:1", AgentMode.OFFSCREEN_NAMED, "fixture:r", "fixture:s"
        )
        local = NpcIntent(
            "gesture", "GESTURE", base_priority=100, requires_local_projection=True
        )
        remote = NpcIntent("report", "REPORT", base_priority=1)
        self.assertEqual(choose_intent(agent, [local, remote]).kind, "REPORT")

    def test_structured_conflict_requests_handoff_but_does_not_resolve_tactics(self):
        agent = NpcAgentState(
            "npc:1",
            AgentMode.LOCAL_ACTIVE,
            "fixture:r",
            "fixture:s",
            knowledge=frozenset({"claim:threat"}),
        )
        conflict = NpcIntent(
            "confront",
            "CONFRONT",
            base_priority=20,
            required_knowledge=frozenset({"claim:threat"}),
            requires_structured_mechanics=True,
            target_ref="fixture:actor:threat",
        )
        decision = choose_intent(agent, [conflict])
        self.assertEqual(decision.handoff, Handoff.REQUEST_AUTOPTU)
        self.assertNotIn("damage", repr(decision).lower())
        self.assertNotIn("status", repr(decision).lower())

    def test_risk_tolerance_can_change_choice_without_changing_world_truth(self):
        risky = NpcIntent("cross", "INVESTIGATE", base_priority=20, risk=15)
        safe = NpcIntent("report", "REPORT", base_priority=10)
        cautious = NpcAgentState(
            "npc:cautious",
            AgentMode.LOCAL_ACTIVE,
            "fixture:r",
            "fixture:s",
            risk_tolerance=0,
        )
        bold = NpcAgentState(
            "npc:bold",
            AgentMode.LOCAL_ACTIVE,
            "fixture:r",
            "fixture:s",
            risk_tolerance=100,
        )
        self.assertEqual(choose_intent(cautious, [risky, safe]).kind, "REPORT")
        self.assertEqual(choose_intent(bold, [risky, safe]).kind, "INVESTIGATE")

    def test_replay_is_deterministic(self):
        agent = NpcAgentState(
            "npc:1", AgentMode.LOCAL_ACTIVE, "fixture:r", "fixture:s"
        )
        intents = [
            NpcIntent("b", "B", base_priority=1),
            NpcIntent("a", "A", base_priority=1),
        ]
        self.assertEqual(
            choose_intent(agent, intents),
            choose_intent(agent, list(reversed(intents))),
        )
        self.assertEqual(choose_intent(agent, intents).intent_id, "a")

    def test_machine_readable_fixture_matches_expected_decisions(self):
        fixture_path = (
            Path(__file__).parents[1]
            / "implementation"
            / "global-npc-ai-agent-fixture-v1.json"
        )
        payload = json.loads(fixture_path.read_text(encoding="utf-8"))
        decisions = run_fixture(payload)
        for scenario in payload["scenarios"]:
            actual = decisions[scenario["scenario_id"]]
            self.assertEqual(actual.kind, scenario["expected"]["kind"])
            self.assertEqual(actual.handoff.value, scenario["expected"]["handoff"])

    def test_autoptu_binding_freezes_world_planner_until_release(self):
        agent = NpcAgentState(
            "npc:1", AgentMode.LOCAL_ACTIVE, "fixture:r", "fixture:s"
        )
        bound = bind_autoptu(agent, "battle:1:subject:npc1")
        decision = choose_intent(
            bound, [NpcIntent("work", "WORK", base_priority=99)]
        )
        self.assertEqual(decision.handoff, Handoff.HOLD_EXISTING_AUTOPTU_BINDING)
        released = release_autoptu(bound)
        self.assertEqual(
            choose_intent(
                released, [NpcIntent("work", "WORK", base_priority=99)]
            ).kind,
            "WORK",
        )


if __name__ == "__main__":
    unittest.main()
