import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-recovery-trajectory-trace-v1.json"

class EcologicalRecoveryTrajectoryRegression(unittest.TestCase):
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

    def test_fixture_only_recovery_does_not_create_canon(self):
        guards = self.data["canon_guards"]
        self.assertFalse(guards["disturbance_is_canon"])
        self.assertFalse(guards["secondary_pressure_is_canon"])
        self.assertFalse(guards["reference_state_is_canon"])
        self.assertFalse(guards["recovery_outcome_is_canon"])
        self.assertFalse(guards["hysteresis_is_canon"])

    def test_cessation_does_not_assert_recovery(self):
        step = self.event("DISTURBANCE_CESSATION_CONFIRMED")
        self.assertEqual(step["recovery_disposition"], "CESSATION_CONFIRMED")
        self.assertFalse(step["recovery_claimed"])
        post = self.event("IMMEDIATE_POST_CESSATION_ASSESSMENT")
        self.assertEqual(post["activity_disposition"], "RECOVERY_LAG_OBSERVED")
        self.assertFalse(post["system_recovered"])

    def test_single_normal_sighting_is_not_recovery(self):
        self.assertEqual(
            self.event("SINGLE_NORMAL_SIGHTING")["result"],
            "REJECT_SINGLE_OBSERVATION_AS_RECOVERY"
        )

    def test_recovery_is_dimension_specific(self):
        step = self.event("LATER_DIMENSION_SPECIFIC_ASSESSMENT")
        self.assertEqual(step["site_use_disposition"], "RECOVERED_WITHIN_REFERENCE_BAND")
        self.assertEqual(step["activity_disposition"], "PERSISTENT_SHIFT_HYPOTHESIS")
        self.assertFalse(step["system_recovered"])

    def test_persistence_alone_does_not_confirm_hysteresis(self):
        step = self.event("HYSTERESIS_PROMOTION_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_INSUFFICIENT_HYSTERESIS_EVIDENCE")

    def test_secondary_pressure_remains_an_alternative_explanation(self):
        step = self.event("SECONDARY_PRESSURE_DOCUMENTED")
        self.assertEqual(step["recovery_disposition"], "SECONDARY_PRESSURE_SUSPECTED")
        self.assertFalse(step["original_cause_reinterpreted"])
        cessation = self.event("SECONDARY_PRESSURE_CESSATION_CONFIRMED")
        self.assertFalse(cessation["recovery_claimed"])

    def test_later_recovery_does_not_claim_population_recovery_or_hysteresis(self):
        step = self.event("MATCHED_FOLLOWUP_ASSESSMENT")
        self.assertEqual(step["activity_disposition"], "RECOVERED_WITHIN_REFERENCE_BAND")
        self.assertEqual(step["site_use_disposition"], "RECOVERED_WITHIN_REFERENCE_BAND")
        self.assertFalse(step["hysteresis_confirmed"])
        self.assertFalse(step["population_recovery_claimed"])

    def test_observation_does_not_create_tactical_semantics(self):
        step = self.event("TACTICAL_SEMANTICS_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_restart_preserves_trajectory(self):
        step = self.event("RESTART_RESTORE")
        self.assertTrue(step["trajectory_history_preserved"])
        self.assertTrue(step["dimension_history_preserved"])
        self.assertTrue(step["cessation_epochs_preserved"])
        self.assertEqual(step["demographic_events"], 0)

if __name__ == "__main__":
    unittest.main()
