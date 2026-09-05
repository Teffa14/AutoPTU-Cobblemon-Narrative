import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-accountability-evidence-contest-trace-v1.json"


class EcologicalAccountabilityEvidenceContestRegression(unittest.TestCase):
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
        self.assertFalse(guards["appeal_right_created_as_canon"])
        self.assertFalse(guards["review_body_created_as_canon"])
        self.assertFalse(guards["ecological_truth_duplicated"])
        for step in self.trace:
            if "population" in step:
                self.assertEqual(step["population"], 12)

    def test_challenge_does_not_reverse_or_suspend_by_itself(self):
        step = self.event("CHALLENGE_AS_AUTOMATIC_REVERSAL_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_CHALLENGE_AS_AUTOMATIC_REVERSAL")
        self.assertFalse(step["delegation_suspended"])
        self.assertFalse(step["original_interpretation_erased"])

    def test_method_mismatch_blocks_false_comparison(self):
        first = self.event("FIRST_LOG_METHOD_PROFILE_LOADED")
        second = self.event("SECOND_LOG_METHOD_MISMATCH_DETECTED")
        self.assertNotEqual(first["method_profile"], second["method_profile"])
        self.assertNotEqual(first["visibility_class"], second["visibility_class"])
        self.assertEqual(second["comparability_assessment"], "METHODS_NOT_COMPARABLE")

    def test_missing_record_does_not_prove_noncompliance_or_bad_faith(self):
        step = self.event("MISSING_LOG_AS_NONCOMPLIANCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_MISSING_EVIDENCE_AS_NONCOMPLIANCE_PROOF")
        self.assertFalse(step["noncompliance_proven"])
        self.assertFalse(step["bad_faith_inferred"])

    def test_reused_source_does_not_count_as_independent_corroboration(self):
        step = self.event("APPARENT_CORROBORATION_INDEPENDENCE_CHECK")
        self.assertTrue(step["same_source_capture_session"])
        self.assertEqual(step["independence_assessment"], "INDEPENDENCE_NOT_ESTABLISHED")

    def test_followup_requires_existing_authority_source(self):
        step = self.event("COMPARABLE_FOLLOWUP_AUTHORIZED_BY_EXISTING_AUTHORITY")
        self.assertTrue(step["authority_source"])
        self.assertEqual(step["review_disposition"], "FOLLOWUP_OBSERVATION_AUTHORIZED")

    def test_stronger_record_supports_only_narrow_process_finding(self):
        step = self.event("STRONGER_RECORD_SUPPORTS_NARROW_PROCESS_FINDING")
        self.assertTrue(step["supports_process_compliance"])
        self.assertFalse(step["supports_ecological_outcome"])
        self.assertEqual(step["review_disposition"], "EVIDENCE_SUFFICIENT_FOR_NARROW_PROCESS_FINDING")

    def test_supersession_preserves_interpretation_history(self):
        step = self.event("INTERPRETATION_SUPERSESSION_RECORDED")
        self.assertTrue(step["historical_interpretation_preserved"])
        self.assertTrue(step["supersedes_interpretation_ref"])
        self.assertEqual(step["review_disposition"], "INTERPRETATION_SUPERSEDED_BY_STRONGER_RECORD")

    def test_process_finding_does_not_create_ecological_truth(self):
        step = self.event("ECOLOGICAL_OUTCOME_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_PROCESS_FINDING_AS_ECOLOGICAL_OUTCOME")
        self.assertFalse(step["population_recovery_claimed"])
        self.assertFalse(step["habitat_quality_claimed"])
        self.assertFalse(step["species_behavior_rule_created"])

    def test_evidence_contest_does_not_imply_formal_appeal_right(self):
        step = self.event("FORMAL_APPEAL_RIGHT_INFERENCE_ATTEMPT")
        self.assertFalse(step["canon_appeal_procedure_exists"])
        self.assertEqual(step["result"], "REJECT_EVIDENCE_CONTEST_AS_IMPLIED_APPEAL_RIGHT")
        self.assertFalse(step["stay_created"])
        self.assertFalse(step["remedy_created"])

    def test_no_tactical_semantics_are_synthesized(self):
        step = self.event("TACTICAL_SEMANTICS_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_restart_preserves_history_without_advancing_semantic_time(self):
        step = self.event("RESTART_RESTORE")
        self.assertTrue(step["contest_history_preserved"])
        self.assertTrue(step["interpretation_lineage_preserved"])
        self.assertTrue(step["provenance_preserved"])
        self.assertFalse(step["semantic_window_advanced_by_restart"])
        self.assertEqual(step["demographic_events"], 0)
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)


if __name__ == "__main__":
    unittest.main()
