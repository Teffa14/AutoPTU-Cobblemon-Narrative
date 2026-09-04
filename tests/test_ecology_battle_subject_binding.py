import json
import unittest
from pathlib import Path


TRACE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-battle-subject-binding-trace-v1.json"


class BattleSubjectBindingRegression(unittest.TestCase):
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

    def test_minecraft_uuid_cannot_bind_ecological_subject(self):
        first = self.event(1)
        self.assertEqual("MINECRAFT_ENTITY_UUID", first["candidate_key_type"])
        self.assertEqual("REJECT_NONAUTHORITATIVE_SUBJECT_KEY", first["result"])

    def test_private_binding_does_not_leak_player_facing_identity(self):
        binding = self.event(2)
        self.assertEqual("ACTIVE", binding["binding_state"])
        self.assertFalse(binding["player_facing_private_id_exposure"])

    def test_integration_receipt_cannot_mutate_ptu_or_population_state(self):
        receipt = self.event(3)
        self.assertEqual("ACCEPTED_RECEIPT_ONLY", receipt["result"])
        self.assertTrue(all(value is False for value in receipt["mutations"].values()))

    def test_exact_replay_is_idempotent(self):
        replay = self.event(4)
        self.assertTrue(replay["same_result_identity"])
        self.assertTrue(replay["same_semantic_content"])
        self.assertEqual("IDEMPOTENT_NO_OP", replay["result"])

    def test_subject_ref_is_session_scoped(self):
        wrong_session = self.event(5)
        self.assertEqual("REJECT_SUBJECT_SESSION_MISMATCH", wrong_session["result"])

    def test_unverified_injury_and_status_are_quarantined(self):
        injury = self.event(6)
        status = self.event(7)
        self.assertEqual("QUARANTINE_UNVERIFIED_CAPABILITY_PATH", injury["result"])
        self.assertFalse(injury["canon_injury_created"])
        self.assertEqual("QUARANTINE_UNVERIFIED_CAPABILITY_PATH", status["result"])
        self.assertFalse(status["canon_status_created"])

    def test_unresolved_counted_source_cannot_receive_durable_aftermath(self):
        unresolved = self.event(8)
        self.assertTrue(unresolved["source_already_counted_in_population"])
        self.assertFalse(unresolved["lineage_proof_present"])
        self.assertEqual("STABLE_SUBJECT_REQUIRED_FOR_DURABLE_AFTERMATH", unresolved["result"])
        self.assertFalse(unresolved["promotion_committed"])
        self.assertEqual(0, unresolved["population_delta"])

    def test_restart_restores_active_binding_and_receipts(self):
        restart = self.event(9)
        self.assertIn("active_battle_binding", restart["restored"])
        self.assertIn("accepted_receipt", restart["restored"])
        self.assertIn("quarantine_receipts", restart["restored"])
        self.assertEqual(12, restart["population"])

    def test_finalized_binding_rejects_late_results(self):
        self.assertEqual("RETIRED", self.event(10)["binding_state"])
        self.assertEqual("REJECT_RETIRED_BATTLE_SUBJECT", self.event(11)["result"])

    def test_fixture_does_not_claim_engine_or_transport_completion(self):
        self.assertFalse(self.trace["autoptu_rule_execution_claimed"])
        self.assertFalse(self.trace["production_transport_claimed"])
        self.assertFalse(self.trace["canon_new_state_created"])


if __name__ == "__main__":
    unittest.main()
