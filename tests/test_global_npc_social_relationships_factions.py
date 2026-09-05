import inspect
import json
import unittest
from pathlib import Path

from tools.global_npc_ai import AgentMode, Handoff, NpcAgentState, PlanningContext
from tools.global_npc_social import (
    FactionMembership,
    RelationshipState,
    SocialIntentSpec,
    apply_relationship_event,
    choose_social_agenda_intent,
    relationship_weight,
    run_social_fixture,
)


class GlobalNpcSocialRelationshipTests(unittest.TestCase):
    def setUp(self):
        self.agent = NpcAgentState(
            "fixture:npc:a",
            AgentMode.OFFSCREEN_NAMED,
            "fixture:region:any",
            "fixture:site:any",
            knowledge=frozenset({"claim:known"}),
        )
        self.relationship = RelationshipState(
            "fixture:npc:a",
            "fixture:npc:b",
            affinity=70,
            trust=50,
            respect=65,
            rivalry=60,
            provenance_refs=("fixture:event:history",),
        )

    def test_core_social_module_has_no_authored_place_special_cases(self):
        import tools.global_npc_social as module

        source = inspect.getsource(module).lower()
        for local_name in ("marea", "sendero", "puerto bruma", "loma clara"):
            self.assertNotIn(local_name, source)

    def test_relationship_is_directional(self):
        reverse = RelationshipState("fixture:npc:b", "fixture:npc:a", affinity=-20)
        self.assertNotEqual(self.relationship.affinity, reverse.affinity)
        self.assertEqual(self.relationship.source_agent_id, "fixture:npc:a")
        self.assertEqual(reverse.source_agent_id, "fixture:npc:b")

    def test_relationship_mutation_requires_provenance(self):
        with self.assertRaises(ValueError):
            apply_relationship_event(
                self.relationship,
                provenance_ref="",
                semantic_minute=10,
                trust_delta=5,
            )

    def test_relationship_event_changes_only_requested_dimensions(self):
        updated = apply_relationship_event(
            self.relationship,
            provenance_ref="fixture:event:kept-promise",
            semantic_minute=50,
            trust_delta=15,
        )
        self.assertEqual(updated.trust, 65)
        self.assertEqual(updated.affinity, self.relationship.affinity)
        self.assertEqual(updated.rivalry, self.relationship.rivalry)
        self.assertIn("fixture:event:kept-promise", updated.provenance_refs)

    def test_relationship_weight_is_bounded(self):
        extreme = RelationshipState(
            "fixture:npc:a",
            "fixture:npc:b",
            affinity=100,
            trust=100,
            debt=100,
        )
        self.assertLessEqual(relationship_weight(extreme, "ASSIST"), 10)
        self.assertGreaterEqual(relationship_weight(extreme, "ASSIST"), -10)

    def test_same_faction_does_not_grant_private_knowledge(self):
        membership = FactionMembership(
            "fixture:npc:a",
            "fixture:faction:x",
            "member",
            commitment=80,
            obligation_tags=frozenset({"REPORT"}),
        )
        result = choose_social_agenda_intent(
            self.agent,
            memberships=[membership],
            social_intents=[
                SocialIntentSpec(
                    "secret-report",
                    "REPORT",
                    base_priority=50,
                    faction_id="fixture:faction:x",
                    required_faction_obligation="REPORT",
                    required_knowledge=frozenset({"claim:private-other-member"}),
                )
            ],
            context=PlanningContext(10),
        )
        self.assertEqual(result.decision.kind, "WAIT")

    def test_rivalry_does_not_force_structured_resolution(self):
        result = choose_social_agenda_intent(
            self.agent,
            relationships=[self.relationship],
            social_intents=[
                SocialIntentSpec(
                    "challenge",
                    "ARRANGE_CHALLENGE",
                    base_priority=5,
                    target_agent_id="fixture:npc:b",
                    relationship_motive="RIVALRY",
                )
            ],
            context=PlanningContext(10),
        )
        self.assertEqual(result.decision.kind, "ARRANGE_CHALLENGE")
        self.assertEqual(result.decision.handoff, Handoff.NONE)

    def test_actual_structured_spar_requests_autoptu(self):
        local = NpcAgentState(
            "fixture:npc:a",
            AgentMode.LOCAL_ACTIVE,
            "fixture:r",
            "fixture:s",
        )
        result = choose_social_agenda_intent(
            local,
            relationships=[self.relationship],
            social_intents=[
                SocialIntentSpec(
                    "spar",
                    "SPAR",
                    base_priority=5,
                    target_agent_id="fixture:npc:b",
                    relationship_motive="RIVALRY",
                    requires_structured_mechanics=True,
                )
            ],
            context=PlanningContext(10),
        )
        self.assertEqual(result.decision.handoff, Handoff.REQUEST_AUTOPTU)

    def test_fixture_expected_outcomes(self):
        path = (
            Path(__file__).parents[1]
            / "implementation"
            / "global-npc-social-relationship-faction-fixture-v1.json"
        )
        payload = json.loads(path.read_text(encoding="utf-8"))
        decisions = run_social_fixture(payload)
        for scenario in payload["scenarios"]:
            actual = decisions[scenario["scenario_id"]]
            expected = scenario["expected"]
            self.assertEqual(actual.decision.kind, expected["kind"])
            self.assertEqual(actual.decision.handoff.value, expected["handoff"])


if __name__ == "__main__":
    unittest.main()
