import inspect
import json
import unittest
from pathlib import Path

from tools.global_npc_ai import (
    AgentMode,
    DurableGoal,
    Handoff,
    NeedState,
    NpcAgentState,
    NpcIntent,
    PlanningContext,
    ScheduledCommitment,
    bind_autoptu,
    choose_agenda_intent,
    run_agenda_fixture,
    schedule_state,
)


class GlobalNpcAgendaTests(unittest.TestCase):
    def setUp(self):
        self.agent = NpcAgentState(
            "fixture:npc:one",
            AgentMode.OFFSCREEN_NAMED,
            "fixture:region:any",
            "fixture:site:any",
            permissions=frozenset({"TRAVEL", "WORK"}),
        )

    def test_core_remains_free_of_authored_place_special_cases(self):
        import tools.global_npc_ai as module

        source = inspect.getsource(module).lower()
        for local_name in ("marea", "sendero", "puerto bruma", "loma clara"):
            self.assertNotIn(local_name, source)

    def test_complete_goal_generates_no_work(self):
        result = choose_agenda_intent(
            self.agent,
            goals=[DurableGoal("done", "WORK", 10, progress=100, target_progress=100)],
            context=PlanningContext(10),
        )
        self.assertEqual(result.decision.kind, "WAIT")

    def test_upcoming_commitment_does_not_preempt_current_goal(self):
        result = choose_agenda_intent(
            self.agent,
            goals=[DurableGoal("work", "WORK", 4, progress=20, target_progress=100)],
            commitments=[
                ScheduledCommitment(
                    "meeting", "TRAVEL", 200, 240, priority=10, hard=True
                )
            ],
            context=PlanningContext(100),
        )
        self.assertEqual(result.source_type, "GOAL")
        self.assertEqual(result.decision.kind, "WORK")

    def test_due_hard_commitment_preempts_ordinary_goal(self):
        result = choose_agenda_intent(
            self.agent,
            goals=[DurableGoal("work", "WORK", 7, progress=40, target_progress=100)],
            commitments=[
                ScheduledCommitment(
                    "meeting", "TRAVEL", 100, 140, priority=6, hard=True
                )
            ],
            context=PlanningContext(110),
        )
        self.assertEqual(result.source_type, "COMMITMENT")
        self.assertEqual(result.schedule_state, "DUE")
        self.assertEqual(result.decision.kind, "TRAVEL")

    def test_schedule_uses_explicit_semantic_time(self):
        commitment = ScheduledCommitment("meeting", "TRAVEL", 100, 140, grace_minutes=20)
        self.assertEqual(schedule_state(commitment, 99), "UPCOMING")
        self.assertEqual(schedule_state(commitment, 120), "DUE")
        self.assertEqual(schedule_state(commitment, 150), "GRACE")
        self.assertEqual(schedule_state(commitment, 161), "MISSED")

    def test_missed_commitment_creates_followup_without_location_mutation(self):
        before = self.agent.location_ref
        result = choose_agenda_intent(
            self.agent,
            commitments=[ScheduledCommitment("meeting", "TRAVEL", 10, 20, hard=True)],
            context=PlanningContext(100),
        )
        self.assertEqual(result.schedule_state, "MISSED")
        self.assertEqual(result.decision.kind, "RESCHEDULE_OR_REPORT_MISSED_COMMITMENT")
        self.assertEqual(self.agent.location_ref, before)

    def test_need_below_threshold_does_not_create_intent(self):
        result = choose_agenda_intent(
            self.agent,
            needs=[NeedState("rest", "REST", pressure=40, activation_threshold=50)],
            context=PlanningContext(10),
        )
        self.assertEqual(result.decision.kind, "WAIT")

    def test_critical_need_can_preempt_low_priority_goal(self):
        result = choose_agenda_intent(
            self.agent,
            goals=[DurableGoal("tidy", "WORK", 2, progress=80, target_progress=100)],
            needs=[NeedState("rest", "REST", pressure=95, activation_threshold=50)],
            context=PlanningContext(10),
        )
        self.assertEqual(result.source_type, "NEED")
        self.assertEqual(result.decision.kind, "REST")

    def test_continuity_bonus_breaks_near_tie_without_locking_agent_forever(self):
        current = DurableGoal("current", "WORK", 5, progress=90, target_progress=100)
        other = NpcIntent("other", "SOCIALIZE", base_priority=5, urgency=1)
        result = choose_agenda_intent(
            self.agent,
            goals=[current],
            situational_intents=[other],
            context=PlanningContext(10, active_intent_id="goal:current", continuity_bonus=2),
        )
        self.assertEqual(result.decision.intent_id, "goal:current")
        emergency = NpcIntent("emergency", "RESPOND_EMERGENCY", base_priority=20, urgency=10)
        interrupted = choose_agenda_intent(
            self.agent,
            goals=[current],
            situational_intents=[emergency],
            context=PlanningContext(11, active_intent_id="goal:current", continuity_bonus=2),
        )
        self.assertEqual(interrupted.decision.kind, "RESPOND_EMERGENCY")

    def test_unknown_emergency_does_not_become_omniscient_interrupt(self):
        emergency = NpcIntent(
            "emergency",
            "RESPOND_EMERGENCY",
            base_priority=50,
            required_knowledge=frozenset({"claim:unknown-emergency"}),
        )
        result = choose_agenda_intent(
            self.agent,
            goals=[DurableGoal("work", "WORK", 2)],
            situational_intents=[emergency],
            context=PlanningContext(10),
        )
        self.assertEqual(result.decision.kind, "WORK")

    def test_structured_agenda_action_requests_autoptu(self):
        local = NpcAgentState(
            "fixture:npc:local", AgentMode.LOCAL_ACTIVE, "fixture:r", "fixture:s"
        )
        result = choose_agenda_intent(
            local,
            situational_intents=[
                NpcIntent(
                    "training",
                    "TRAIN",
                    base_priority=10,
                    requires_structured_mechanics=True,
                    target_ref="fixture:actor:partner",
                )
            ],
            context=PlanningContext(10),
        )
        self.assertEqual(result.decision.handoff, Handoff.REQUEST_AUTOPTU)

    def test_autoptu_bound_agent_does_not_replan_world_agenda(self):
        local = NpcAgentState(
            "fixture:npc:local", AgentMode.LOCAL_ACTIVE, "fixture:r", "fixture:s"
        )
        bound = bind_autoptu(local, "fixture:battle:1")
        result = choose_agenda_intent(
            bound,
            goals=[DurableGoal("work", "WORK", 99)],
            context=PlanningContext(10),
        )
        self.assertEqual(result.decision.handoff, Handoff.HOLD_EXISTING_AUTOPTU_BINDING)

    def test_fixture_expected_outcomes(self):
        path = (
            Path(__file__).parents[1]
            / "implementation"
            / "global-npc-goal-need-schedule-fixture-v1.json"
        )
        payload = json.loads(path.read_text(encoding="utf-8"))
        decisions = run_agenda_fixture(payload)
        for scenario in payload["scenarios"]:
            actual = decisions[scenario["scenario_id"]]
            expected = scenario["expected"]
            self.assertEqual(actual.decision.kind, expected["kind"])
            self.assertEqual(actual.decision.handoff.value, expected["handoff"])
            self.assertEqual(actual.source_type, expected["source_type"])
            if "schedule_state" in expected:
                self.assertEqual(actual.schedule_state, expected["schedule_state"])


if __name__ == "__main__":
    unittest.main()
