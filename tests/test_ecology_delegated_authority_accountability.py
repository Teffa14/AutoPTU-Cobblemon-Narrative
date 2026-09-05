import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-delegated-authority-accountability-trace-v1.json"


class EcologicalDelegatedAuthorityRegression(unittest.TestCase):
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
        self.assertFalse(guards["jurisdiction_created_as_canon"])
        self.assertFalse(guards["ownership_created_as_canon"])
        self.assertFalse(guards["player_organization_granted_permanent_authority"])
        for step in self.trace:
            if "population" in step:
                self.assertEqual(step["population"], 12)

    def test_parent_authority_retains_reserved_functions(self):
        step = self.event("PARENT_AUTHORITY_AND_FUNCTION_VERIFIED")
        self.assertIn("RELOCATION_APPROVAL", step["reserved_functions"])
        self.assertIn("ACCESS_CLOSURE_APPROVAL", step["reserved_functions"])
        self.assertEqual(step["disposition"], "PROPOSED")

    def test_repeated_performance_does_not_create_jurisdiction(self):
        step = self.event("PERMANENT_JURISDICTION_INFERENCE_ATTEMPT")
        self.assertGreater(step["completed_prior_assignments"], 1)
        self.assertEqual(step["result"], "REJECT_REPEATED_PERFORMANCE_AS_PERMANENT_MANDATE")
        self.assertFalse(step["jurisdiction_transfer_created"])
        self.assertFalse(step["ownership_created"])

    def test_subdelegation_requires_explicit_permission(self):
        step = self.event("UNAUTHORIZED_SUBDELEGATION_ATTEMPT")
        self.assertFalse(step["parent_permission_present"])
        self.assertEqual(step["result"], "REJECT_UNAUTHORIZED_SUBDELEGATION")
        self.assertFalse(step["subdelegate_authority_created"])

    def test_authorized_function_does_not_create_ecological_or_ptu_truth(self):
        step = self.event("AUTHORIZED_FUNCTION_PERFORMED")
        self.assertTrue(step["within_scope"])
        self.assertFalse(step["ecological_outcome_claimed"])
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_reporting_deficiency_is_separate_from_ecological_failure_or_intent(self):
        step = self.event("REPORTING_DEFICIENCY_DETECTED")
        self.assertFalse(step["bad_faith_inferred"])
        self.assertFalse(step["ecological_failure_inferred"])
        self.assertEqual(step["disposition"], "CORRECTIVE_ACTION_REQUIRED")
        repaired = self.event("CORRECTIVE_EVIDENCE_SUPPLIED")
        self.assertTrue(repaired["missing_record_repaired"])
        self.assertTrue(repaired["provenance_preserved"])

    def test_history_does_not_auto_renew_and_explicit_renewal_stays_narrow(self):
        attempt = self.event("AUTOMATIC_RENEWAL_ATTEMPT")
        self.assertTrue(attempt["successful_review_history"])
        self.assertFalse(attempt["renewal_event_present"])
        self.assertFalse(attempt["term_extended"])
        renewal = self.event("EXPLICIT_NARROW_RENEWAL")
        self.assertTrue(renewal["reserved_functions_unchanged"])
        self.assertFalse(renewal["permanent_authority_created"])

    def test_partial_revocation_is_prospective_and_does_not_reverse_ecology(self):
        step = self.event("PARTIAL_REVOCATION_AFTER_SCOPE_DEFICIENCY")
        self.assertEqual(step["remaining_function"], "OBSERVATION")
        self.assertFalse(step["historical_valid_actions_erased"])
        self.assertFalse(step["ecological_state_reversed"])
        self.assertEqual(step["disposition"], "PARTIALLY_REVOKED")

    def test_delegated_role_does_not_create_tactical_semantics(self):
        step = self.event("TACTICAL_SEMANTICS_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_expiry_ends_future_authority_without_erasing_history(self):
        step = self.event("TERM_EXPIRY_WITHOUT_RENEWAL")
        self.assertTrue(step["semantic_expiry_reached"])
        self.assertFalse(step["automatic_renewal"])
        self.assertFalse(step["future_delegated_actions_authorized"])
        self.assertTrue(step["historical_records_preserved"])

    def test_restart_preserves_records_without_extending_term(self):
        step = self.event("RESTART_RESTORE")
        self.assertTrue(step["delegation_history_preserved"])
        self.assertTrue(step["accountability_history_preserved"])
        self.assertTrue(step["revocation_history_preserved"])
        self.assertFalse(step["semantic_term_extended_by_restart"])
        self.assertEqual(step["demographic_events"], 0)
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)


if __name__ == "__main__":
    unittest.main()
