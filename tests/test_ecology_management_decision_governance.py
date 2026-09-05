import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-ecological-management-decision-trace-v1.json"


class EcologicalManagementDecisionGovernanceRegression(unittest.TestCase):
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
        self.assertFalse(guards["sendero_institution_created_as_canon"])
        self.assertFalse(guards["access_restriction_created_as_canon"])
        for step in self.trace:
            if "population" in step:
                self.assertEqual(step["population"], 12)

    def test_warning_cannot_be_promoted_directly_to_policy(self):
        warning = self.event("WARNING_EVIDENCE_LOADED")
        self.assertFalse(warning["policy_command_created"])
        attempt = self.event("AUTOMATIC_POLICY_PROMOTION_ATTEMPT")
        self.assertEqual(attempt["result"], "REJECT_SIGNAL_AS_POLICY_COMMAND")
        self.assertFalse(attempt["ecological_threshold_equals_decision_threshold"])

    def test_same_evidence_can_support_different_governance_preferences(self):
        step = self.event("OBJECTIVE_PROFILES_DECLARED")
        self.assertTrue(step["same_evidence_consumed"])
        self.assertFalse(step["ecological_truth_duplicated"])
        self.assertEqual(len(step["decision_owners"]), 2)
        self.assertNotEqual(step["decision_owners"][0]["objective"], step["decision_owners"][1]["objective"])
        self.assertNotEqual(step["decision_owners"][0]["risk_posture"], step["decision_owners"][1]["risk_posture"])

    def test_monitoring_must_be_decision_relevant(self):
        high = self.event("HIGH_VALUE_UNCERTAINTY_IDENTIFIED")
        self.assertTrue(high["could_change_owner_b_action"])
        self.assertEqual(high["disposition"], "MONITORING_BEFORE_ACTION")
        low = self.event("LOW_VALUE_MONITORING_ATTEMPT")
        self.assertFalse(low["could_change_selected_action"])
        self.assertEqual(low["result"], "ARCHIVE_WITHOUT_DECISION_GATE")
        self.assertFalse(low["mandatory_progress_created"])

    def test_precautionary_action_requires_reversibility_and_review(self):
        step = self.event("PRECAUTIONARY_ACTION_SELECTED")
        self.assertTrue(step["uncertainty_acknowledged"])
        self.assertEqual(step["reversibility_class"], "EASILY_REVERSIBLE")
        self.assertTrue(step["rollback_condition_present"])
        self.assertFalse(step["ptu_terrain_created"])

    def test_new_evidence_triggers_reassessment_not_automatic_policy_flip(self):
        step = self.event("MATCHED_MONITORING_RESULT")
        self.assertTrue(step["critical_uncertainty_reduced"])
        self.assertFalse(step["automatic_restriction_removal"])
        self.assertEqual(step["disposition"], "REASSESSMENT_REQUIRED")
        rollback = self.event("REASSESSMENT_AND_ROLLBACK")
        self.assertFalse(rollback["ecological_recovery_claimed"])
        self.assertEqual(rollback["disposition"], "ACTION_REVERSED_OR_EXPIRED")

    def test_governance_does_not_create_tactical_semantics(self):
        step = self.event("TACTICAL_SEMANTICS_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_restart_preserves_decision_history_without_advancing_review_time(self):
        step = self.event("RESTART_RESTORE")
        self.assertTrue(step["decision_history_preserved"])
        self.assertTrue(step["objective_profiles_preserved"])
        self.assertTrue(step["risk_profiles_preserved"])
        self.assertTrue(step["monitoring_value_history_preserved"])
        self.assertFalse(step["semantic_review_horizon_advanced_by_restart"])
        self.assertEqual(step["demographic_events"], 0)


if __name__ == "__main__":
    unittest.main()
