import json
import unittest
from pathlib import Path


TRACE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-quarantined-aftermath-reconciliation-trace-v1.json"


class QuarantinedAftermathReconciliationRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trace = json.loads(TRACE.read_text(encoding="utf-8"))
        cls.events = cls.trace["events"]

    def event(self, step):
        return next(item for item in self.events if item["step"] == step)

    def test_population_is_conserved(self):
        self.assertEqual(12, self.trace["population_before"])
        self.assertEqual(12, self.trace["population_after"])
        self.assertEqual([], self.trace["demographic_events"])
        self.assertFalse(self.trace["canon_new_actor_created"])

    def test_initial_injury_result_is_quarantined_without_mutation(self):
        event = self.event(1)
        self.assertEqual("QUARANTINED_OPEN", event["quarantine_state"])
        self.assertEqual("UNVERIFIED_EXACT_CAPABILITY_PATH", event["reason"])
        self.assertFalse(event["canon_injury_created"])
        self.assertEqual(0, event["population_delta"])

    def test_transport_retry_cannot_change_semantic_disposition(self):
        event = self.event(2)
        self.assertTrue(event["same_result_identity"])
        self.assertTrue(event["same_semantic_content"])
        self.assertFalse(event["admission_generation_changed"])
        self.assertFalse(event["lineage_generation_changed"])
        self.assertEqual("REVIEW_BLOCKED_NO_CHANGE", event["result"])

    def test_field_observation_is_knowledge_only(self):
        event = self.event(3)
        self.assertEqual("OBSERVATION_RECORDED", event["knowledge_effect"])
        self.assertFalse(event["mechanical_truth_created"])
        self.assertFalse(event["quarantine_released"])
        self.assertFalse(event["private_result_id_exposed"])

    def test_broad_family_change_is_not_exact_admission(self):
        event = self.event(4)
        self.assertEqual("BROAD_FAMILY_LABEL_ONLY", event["evidence_change"])
        self.assertFalse(event["exact_admission_record_present"])
        self.assertEqual("REVIEW_BLOCKED_NO_EXACT_PATH_EVIDENCE", event["result"])
        self.assertFalse(event["canon_injury_created"])

    def test_fixture_only_exact_evidence_can_enter_reconciliation_without_production_claim(self):
        event = self.event(5)
        self.assertEqual("FIXTURE_ONLY", event["admission_scope"])
        self.assertTrue(event["exact_result_type_match"])
        self.assertTrue(event["exact_producer_revision_match"])
        self.assertTrue(event["exact_rules_profile_match"])
        self.assertTrue(event["exact_path_match"])
        self.assertFalse(event["production_admission_claimed"])
        self.assertEqual("RECONCILIATION_ELIGIBLE", event["quarantine_state"])

    def test_reconciliation_is_atomic_and_does_not_rewrite_envelope(self):
        event = self.event(6)
        self.assertFalse(event["original_envelope_mutated"])
        self.assertEqual("ADMITTED_COMMITTED_FIXTURE_ONLY", event["result"])
        self.assertEqual(1, event["mapper_invocations"])
        self.assertTrue(event["fixture_injury_record_created"])
        self.assertFalse(event["canon_injury_created"])
        self.assertEqual(0, event["population_delta"])

    def test_replay_after_reconciliation_is_idempotent(self):
        event = self.event(7)
        self.assertTrue(event["same_result_identity"])
        self.assertEqual("IDEMPOTENT_NO_OP", event["result"])
        self.assertEqual(0, event["mapper_invocations_added"])

    def test_unverified_status_remains_quarantined(self):
        event = self.event(8)
        self.assertEqual("PERSISTENT_STATUS", event["result_type"])
        self.assertEqual(["PARTIAL"], event["live_readiness"])
        self.assertEqual("QUARANTINED_OPEN", event["quarantine_state"])
        self.assertFalse(event["canon_status_created"])

    def test_restart_restores_reconciliation_and_open_quarantine_once(self):
        event = self.event(9)
        self.assertIn("reconciled_receipt", event["restored"])
        self.assertIn("reconciliation_provenance", event["restored"])
        self.assertIn("unresolved_status_quarantine", event["restored"])
        self.assertIn("field_observation_history", event["restored"])
        self.assertEqual(1, event["reconciled_mapper_invocations"])
        self.assertEqual(12, event["population"])

    def test_fixture_does_not_claim_live_engine_or_canon_completion(self):
        self.assertFalse(self.trace["autoptu_rule_execution_claimed"])
        self.assertFalse(self.trace["production_semantic_export_claimed"])
        self.assertFalse(self.trace["production_transport_claimed"])
        self.assertFalse(self.trace["production_admission_claimed"])
        self.assertFalse(self.trace["canon_new_state_created"])


if __name__ == "__main__":
    unittest.main()
