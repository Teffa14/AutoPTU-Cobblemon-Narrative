import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE_PATH = ROOT / "implementation" / "marea-sendero-individual-disturbance-response-trace-v1.json"


class EcologyIndividualDisturbanceResponseTest(unittest.TestCase):
    def setUp(self):
        self.trace = json.loads(TRACE_PATH.read_text(encoding="utf-8"))
        self.events = self.trace["events"]

    def test_fixture_is_noncanon_and_preserves_population(self):
        self.assertFalse(self.trace["scenario_is_canon"])
        self.assertFalse(self.trace["fixture_policy"]["values_are_canon"])
        self.assertEqual(12, self.trace["population"]["total"])
        self.assertEqual(12, self.trace["expected_final"]["population_total"])
        self.assertEqual(0, self.trace["expected_final"]["demographic_events"])

    def test_same_shared_pressure_can_produce_distinct_individual_responses(self):
        evaluations = [e for e in self.events if e["type"] == "INDIVIDUAL_RESPONSE_EVALUATED"]
        self.assertEqual(2, len(evaluations))
        self.assertEqual({"CONTEXT_TOLERANCE", "EARLY_WITHDRAWAL"}, {e["result"] for e in evaluations})
        self.assertEqual({"HABITUATING", "SENSITIZING"}, {e["prior_response_trend"] for e in evaluations})

    def test_response_transactions_are_unique_and_do_not_touch_ptu_state(self):
        evaluations = [e for e in self.events if e["type"] == "INDIVIDUAL_RESPONSE_EVALUATED"]
        transaction_ids = [e["response_transaction_id"] for e in evaluations]
        self.assertEqual(len(transaction_ids), len(set(transaction_ids)))
        self.assertTrue(all(e["population_delta"] == 0 for e in evaluations))
        self.assertTrue(all(e["ptu_state_delta"] == 0 for e in evaluations))
        self.assertTrue(all(not e["autoptu_handoff"] for e in evaluations))

    def test_projection_contributions_do_not_change_abundance(self):
        projection = [e for e in self.events if e["type"] == "PROJECTION_RESPONSE_CONTRIBUTION"]
        self.assertEqual(2, len(projection))
        self.assertEqual({"ELIGIBLE_QUIET_EDGE_WINDOW", "REDUCED_EXPOSURE"}, {e["projection_result"] for e in projection})
        self.assertTrue(all(e["population_delta"] == 0 for e in projection))

    def test_tolerance_does_not_generalize_across_stimulus_classes(self):
        query = [e for e in self.events if e["type"] == "STIMULUS_CLASS_QUERY"][0]
        self.assertEqual("PHYSICAL_HANDLING", query["queried_stimulus_class"])
        self.assertFalse(query["inherited_close_approach_tolerance"])
        self.assertEqual("UNKNOWN_FAIL_CLOSED", query["result"])

    def test_fixture_uses_only_already_counted_source_classes(self):
        source_classes = {actor["source_class"] for actor in self.trace["actors"]}
        self.assertEqual({"PERSISTENT_MEMBER", "UNRESOLVED_POOL_SLOT"}, source_classes)
        fixture_actor = [a for a in self.trace["actors"] if a["source_class"] == "UNRESOLVED_POOL_SLOT"][0]
        self.assertTrue(fixture_actor["fixture_source_id"].startswith("fixture-only:"))

    def test_restart_preserves_history_without_demography_or_battle(self):
        restart = [e for e in self.events if e["type"] == "SERVER_RESTART"][0]
        self.assertEqual(12, restart["population_total_after_restart"])
        self.assertTrue(restart["response_history_preserved"])
        self.assertEqual("fixture.fletchling.response.v1", restart["policy_revision_preserved"])
        self.assertEqual(0, self.trace["expected_final"]["autoptu_handoffs"])
        self.assertEqual(0, self.trace["expected_final"]["ptu_state_mutations"])


if __name__ == "__main__":
    unittest.main()
