import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-controlled-comparison-trace-v1.json"

class ControlledComparisonCausalAttributionRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.trace = cls.data["trace"]

    def event(self, name):
        return next(x for x in self.trace if x["event"] == name)

    def test_population_is_conserved(self):
        self.assertEqual(self.data["canon_guards"]["authoritative_fletchling_population"], 12)
        for step in self.trace:
            if "population" in step:
                self.assertEqual(step["population"], 12)
        self.assertFalse(self.data["canon_guards"]["new_persistent_actor_created"])
        self.assertFalse(self.data["canon_guards"]["population_change_claimed"])

    def test_fixture_comparison_does_not_create_canon(self):
        guards = self.data["canon_guards"]
        self.assertFalse(guards["disturbance_is_canon"])
        self.assertFalse(guards["comparator_site_is_canon"])
        self.assertFalse(guards["schedule_response_is_canon"])
        self.assertFalse(guards["causal_relation_is_canon"])

    def test_before_after_change_is_not_causal_proof(self):
        self.assertEqual(self.event("FOCAL_AFTER_CHANGE")["causal_disposition"], "DESCRIPTIVE_ONLY")
        self.assertEqual(self.event("CAUSAL_INFERENCE_WITHOUT_COMPARATOR_ATTEMPT")["result"], "REJECT_BEFORE_AFTER_AS_CAUSAL_PROOF")

    def test_detection_mismatch_invalidates_strong_comparison(self):
        step = self.event("COMPARATOR_SURVEY_WITH_DETECTION_MISMATCH")
        self.assertEqual(step["comparator_validity"], "MATERIAL_MISMATCH")
        self.assertEqual(step["causal_disposition"], "COMPARATOR_INSUFFICIENT")

    def test_same_observer_redetection_is_not_independent_corroboration(self):
        step = self.event("REPEATED_REDETECTION_SAME_OBSERVER")
        self.assertTrue(step["observer_prior_detection_known"])
        self.assertEqual(step["raw_detection_count_added"], 1)
        self.assertEqual(step["independent_corroboration_added"], 0)

    def test_matched_comparison_can_support_narrow_review(self):
        step = self.event("MATCHED_COMPARATOR_WINDOW")
        self.assertTrue(step["methods_matched"])
        self.assertTrue(step["effort_matched"])
        self.assertEqual(step["comparator_validity"], "PLAUSIBLE")
        self.assertEqual(step["causal_disposition"], "CONTROLLED_COMPARISON_SUPPORTED")
        review = self.event("NARROW_CAUSAL_REVIEW")
        self.assertEqual(review["causal_disposition"], "CAUSAL_ATTRIBUTION_SUPPORTED_NARROWLY")
        self.assertFalse(review["population_effect_claimed"])
        self.assertFalse(review["species_global_rule_claimed"])

    def test_nondetection_does_not_create_absence_or_decline(self):
        step = self.event("NONDETECTION_AFTER_DISTURBANCE")
        self.assertFalse(step["source_visible"])
        self.assertFalse(step["absence_claimed"])
        self.assertFalse(step["population_decline_claimed"])

    def test_observation_does_not_create_tactical_semantics(self):
        step = self.event("TACTICAL_SEMANTICS_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_restart_preserves_scope_and_lineage(self):
        step = self.event("RESTART_RESTORE")
        self.assertTrue(step["comparison_history_preserved"])
        self.assertTrue(step["source_lineage_preserved"])
        self.assertEqual(step["causal_scope"], "LOCAL_TESTED_WINDOW_ONLY")
        self.assertEqual(step["demographic_events"], 0)

if __name__ == "__main__":
    unittest.main()
