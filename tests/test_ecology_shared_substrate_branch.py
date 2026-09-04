import json
import unittest
from pathlib import Path


FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-shared-substrate-branch-trace-v1.json"


class SharedSubstrateBranchRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.trace = cls.data["trace"]

    def test_population_is_conserved(self):
        self.assertEqual(self.data["canon_guards"]["authoritative_fletchling_population"], 12)
        for step in self.trace:
            if "population" in step:
                self.assertEqual(step["population"], 12)
        self.assertFalse(self.data["canon_guards"]["new_persistent_actor_created"])
        self.assertFalse(self.data["canon_guards"]["population_growth_claimed"])

    def test_fixture_content_is_not_canon(self):
        guards = self.data["canon_guards"]
        self.assertFalse(guards["branch_actors_are_canon"])
        self.assertFalse(guards["shared_substrate_is_canon"])
        self.assertFalse(guards["species_behavior_is_canon"])

    def test_overlap_does_not_prove_competition(self):
        step = next(x for x in self.trace if x["event"] == "SHARED_SITE_OBSERVED")
        self.assertEqual(step["interpretation"], "OBSERVED_OVERLAP")
        self.assertFalse(step["competition_claimed"])

    def test_priority_requires_mechanism(self):
        step = next(x for x in self.trace if x["event"] == "ARRIVAL_ORDER_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_PRIORITY_WITHOUT_MECHANISM")

    def test_direct_limitation_is_local_and_fixture_only(self):
        step = next(x for x in self.trace if x["event"] == "DIRECT_LIMITATION_EVIDENCE_ACCEPTED")
        self.assertEqual(step["mechanism"], "ACCESS_OBSTRUCTION")
        self.assertEqual(step["interpretation"], "DIRECT_LIMITATION_SUPPORTED")
        self.assertEqual(step["canon_status"], "FIXTURE_ONLY")

    def test_local_result_does_not_become_global_species_rule(self):
        step = next(x for x in self.trace if x["event"] == "GLOBAL_SPECIES_RELATION_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_CONTEXT_COLLAPSE")

    def test_visual_crowding_does_not_create_ptu_displacement(self):
        step = next(x for x in self.trace if x["event"] == "TACTICAL_DISPLACEMENT_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_branch_closure_only_triggers_reevaluation(self):
        step = next(x for x in self.trace if x["event"] == "AUTHORITATIVE_BRANCH_A_CLOSURE")
        self.assertEqual(step["branch_b_state"], "ACTIVE_REEVALUATION_REQUIRED")
        self.assertEqual(step["substrate_state"], "PRESENT_UNREASSESSED")
        self.assertFalse(step["population_recovery_claimed"])
        self.assertFalse(step["habitat_recovery_claimed"])
        self.assertFalse(step["ownership_transferred"])

    def test_restart_preserves_history_without_mutation(self):
        step = next(x for x in self.trace if x["event"] == "RESTART_RESTORE")
        self.assertTrue(step["historical_limitation_edge_preserved"])
        self.assertEqual(step["population"], 12)
        self.assertEqual(step["demographic_events"], 0)
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)


if __name__ == "__main__":
    unittest.main()
