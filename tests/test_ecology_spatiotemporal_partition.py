import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-spatiotemporal-partition-trace-v1.json"

class SpatiotemporalPartitionRegression(unittest.TestCase):
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

    def test_fixture_partition_is_not_canon(self):
        guards = self.data["canon_guards"]
        self.assertFalse(guards["partition_behavior_is_canon"])
        self.assertFalse(guards["resource_is_canon"])
        self.assertFalse(guards["avoidance_is_canon"])
        self.assertFalse(guards["competition_is_canon"])

    def test_axes_remain_independent(self):
        step = self.event("MULTIWINDOW_OBSERVATION")
        self.assertEqual(step["spatial_state"], "SPATIAL_OVERLAP")
        self.assertEqual(step["temporal_state"], "TEMPORAL_SEPARATION")
        self.assertEqual(step["resource_fraction_state"], "RESOURCE_FRACTION_OVERLAP")
        self.assertFalse(step["avoidance_claimed"])
        self.assertFalse(step["competition_claimed"])

    def test_non_cooccurrence_does_not_prove_avoidance(self):
        self.assertEqual(self.event("NON_COOCCURRENCE_INFERENCE_ATTEMPT")["result"], "REJECT_PATTERN_WITHOUT_MECHANISM")

    def test_temporal_separation_does_not_prove_competition(self):
        self.assertEqual(self.event("COMPETITION_INFERENCE_ATTEMPT")["result"], "REJECT_CAUSAL_OVERREACH")

    def test_disturbance_shift_remains_hypothesis_without_causal_support(self):
        step = self.event("DISTURBANCE_CONTEXT_ADDED")
        self.assertEqual(step["interpretation"], "DISTURBANCE_MEDIATED_SHIFT_HYPOTHESIS")
        self.assertEqual(step["causal_support"], "INSUFFICIENT_FOR_SUPPORTED")

    def test_axis_change_does_not_mutate_population(self):
        step = self.event("AXIS_CHANGE_WITHOUT_POPULATION_CHANGE")
        self.assertFalse(step["population_decline_claimed"])
        self.assertFalse(step["population_growth_claimed"])
        self.assertEqual(step["population"], 12)

    def test_visual_partition_does_not_create_tactical_semantics(self):
        step = self.event("TACTICAL_SEMANTICS_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_restart_preserves_evidence_without_promoting_cause(self):
        step = self.event("RESTART_RESTORE")
        self.assertTrue(step["axis_history_preserved"])
        self.assertEqual(step["causal_interpretation"], "UNCERTAIN")
        self.assertEqual(step["demographic_events"], 0)

if __name__ == "__main__":
    unittest.main()
