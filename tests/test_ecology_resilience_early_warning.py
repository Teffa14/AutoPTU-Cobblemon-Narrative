import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-resilience-early-warning-trace-v1.json"


class EcologicalResilienceEarlyWarningRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.trace = cls.data["trace"]

    def event(self, name):
        return next(x for x in self.trace if x["event"] == name)

    def test_population_and_canon_guards_are_conserved(self):
        guards = self.data["canon_guards"]
        self.assertEqual(guards["authoritative_fletchling_population"], 12)
        self.assertFalse(guards["new_persistent_actor_created"])
        self.assertFalse(guards["population_change_claimed"])
        self.assertFalse(guards["resilience_loss_is_canon"])
        self.assertFalse(guards["collapse_predicted"])
        for step in self.trace:
            if "population" in step:
                self.assertEqual(step["population"], 12)

    def test_single_warning_metric_cannot_predict_collapse(self):
        step = self.event("SINGLE_METRIC_COLLAPSE_PROMOTION_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_WARNING_AS_COLLAPSE_PREDICTION")
        self.assertFalse(step["collapse_predicted"])
        self.assertFalse(step["critical_threshold_supported"])

    def test_false_positive_controls_are_required(self):
        review = self.event("NOISE_AND_DETECTABILITY_REVIEW")
        self.assertEqual(review["disposition"], "FALSE_POSITIVE_RISK_HIGH")
        self.assertFalse(review["false_positive_check_complete"])
        matched = self.event("MATCHED_COMPARISON_WINDOWS")
        self.assertTrue(matched["false_positive_check_complete"])
        self.assertEqual(matched["disposition"], "RESILIENCE_LOSS_SIGNAL_SUPPORTED_NARROWLY")
        self.assertFalse(matched["collapse_predicted"])
        self.assertFalse(matched["species_global_rule_created"])

    def test_second_site_can_demonstrate_false_positive_risk(self):
        step = self.event("SECOND_SITE_FALSE_POSITIVE_CONTROL")
        self.assertTrue(step["candidate_variance_increase"])
        self.assertFalse(step["resilience_loss_supported"])
        self.assertEqual(step["disposition"], "SIGNAL_NOT_SUPPORTED")

    def test_warning_does_not_create_tactical_semantics(self):
        step = self.event("TACTICAL_SEMANTICS_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_restart_preserves_history_without_advancing_ecology(self):
        step = self.event("RESTART_RESTORE")
        self.assertTrue(step["semantic_windows_preserved"])
        self.assertTrue(step["warning_history_preserved"])
        self.assertTrue(step["false_positive_history_preserved"])
        self.assertFalse(step["semantic_time_advanced_by_restart"])
        self.assertEqual(step["demographic_events"], 0)


if __name__ == "__main__":
    unittest.main()
