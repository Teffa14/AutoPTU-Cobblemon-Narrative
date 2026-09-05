import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-regime-transition-evidence-trace-v1.json"


class EcologicalRegimeTransitionEvidenceRegression(unittest.TestCase):
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
        self.assertFalse(guards["regime_transition_is_canon"])
        self.assertFalse(guards["hysteresis_is_canon"])
        self.assertFalse(guards["feedback_is_canon"])
        for step in self.trace:
            if "population" in step:
                self.assertEqual(step["population"], 12)

    def test_persistence_alone_cannot_promote_regime_transition(self):
        step = self.event("PERSISTENCE_ONLY_PROMOTION_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_PERSISTENCE_AS_REGIME_PROOF")
        self.assertFalse(step["regime_transition_supported"])
        self.assertFalse(step["hysteresis_supported"])

    def test_abrupt_visible_change_cannot_prove_threshold(self):
        step = self.event("ABRUPT_CHANGE_THRESHOLD_PROMOTION_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_ABRUPT_CHANGE_AS_THRESHOLD_PROOF")
        self.assertFalse(step["critical_threshold_supported"])

    def test_feedback_requires_comparison_before_narrow_support(self):
        candidate = self.event("FIXTURE_FEEDBACK_CANDIDATE_DOCUMENTED")
        self.assertEqual(candidate["feedback_support"], "OBSERVATION_CONSISTENT")
        self.assertFalse(candidate["regime_transition_supported"])
        matched = self.event("MATCHED_FEEDBACK_COMPARISON")
        self.assertEqual(matched["feedback_support"], "SUPPORTED_NARROWLY")
        self.assertEqual(matched["regime_disposition"], "FEEDBACK_MECHANISM_SUPPORTED")

    def test_regime_support_is_narrow_and_non_demographic(self):
        step = self.event("REGIME_TRANSITION_GATE_REVIEW")
        self.assertEqual(step["regime_disposition"], "REGIME_TRANSITION_SUPPORTED_NARROWLY")
        self.assertFalse(step["species_global_rule_created"])
        self.assertEqual(step["population"], 12)

    def test_hysteresis_requires_return_path_evidence(self):
        rejected = self.event("HYSTERESIS_WITHOUT_RETURN_ASYMMETRY_ATTEMPT")
        self.assertEqual(rejected["result"], "REJECT_HYSTERESIS_WITHOUT_RETURN_PATH_EVIDENCE")
        self.assertFalse(rejected["hysteresis_supported"])
        single = self.event("ORIGINAL_DRIVER_REVERSAL_TEST")
        self.assertEqual(single["return_path_asymmetry_support"], "INSUFFICIENT_SINGLE_TEST")
        self.assertFalse(single["hysteresis_supported"])

    def test_matched_return_path_can_support_fixture_only_hysteresis(self):
        step = self.event("MATCHED_RETURN_PATH_ASSESSMENT")
        self.assertEqual(step["feedback_support"], "SUPPORTED_NARROWLY")
        self.assertEqual(step["return_path_asymmetry"], "SUPPORTED")
        self.assertEqual(step["regime_disposition"], "HYSTERESIS_SUPPORTED_NARROWLY")
        self.assertFalse(step["species_global_rule_created"])
        self.assertFalse(step["population_recovery_claimed"])

    def test_ecological_state_does_not_create_tactical_semantics(self):
        step = self.event("TACTICAL_SEMANTICS_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_restart_preserves_evidence_without_demography(self):
        step = self.event("RESTART_RESTORE")
        self.assertTrue(step["transition_history_preserved"])
        self.assertTrue(step["feedback_evidence_preserved"])
        self.assertTrue(step["return_path_evidence_preserved"])
        self.assertTrue(step["semantic_windows_preserved"])
        self.assertEqual(step["population"], 12)
        self.assertEqual(step["demographic_events"], 0)


if __name__ == "__main__":
    unittest.main()
