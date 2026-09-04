import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "implementation" / "marea-sendero-semantic-result-ingress-trace-v1.json"


def load_fixture():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def events_of_type(data, event_type):
    return [event for event in data["events"] if event["type"] == event_type]


class SemanticResultIngressTests(unittest.TestCase):
    def test_population_is_conserved_and_fixture_does_not_create_canon_injury(self):
        data = load_fixture()
        self.assertEqual(data["population"]["total"], 12)
        self.assertEqual(data["expected_final"]["population_total"], 12)
        self.assertEqual(data["expected_final"]["net_population_delta"], 0)
        self.assertEqual(data["expected_final"]["demographic_events"], 0)
        self.assertEqual(data["expected_final"]["canon_injuries_created"], 0)
        self.assertTrue(all(event.get("population_delta", 0) == 0 for event in data["events"]))

    def test_accepted_fixture_result_has_explicit_authority_lineage_and_capability_provenance(self):
        data = load_fixture()
        accepted = next(
            event for event in events_of_type(data, "AUTOPTU_SEMANTIC_RESULT_INGRESS_ATTEMPT")
            if event.get("result") == "ACCEPTED_COMMITTED"
        )
        envelope = accepted["envelope"]
        self.assertEqual(envelope["schema_version"], "OUROS_AUTOPTU_SEMANTIC_RESULT_V1")
        self.assertEqual(envelope["producer_id"], data["authority_profile"]["producer_id"])
        self.assertEqual(envelope["battle_session_id"], data["battle_handoff"]["battle_session_id"])
        self.assertEqual(envelope["subject_binding"], data["battle_handoff"]["subject_binding"])
        self.assertEqual(envelope["capability_provenance"]["mode"], "FIXTURE_PREVALIDATED_ONLY")
        self.assertFalse(envelope["capability_provenance"]["production_admission_claimed"])
        self.assertFalse(accepted["live_engine_production_capability_admitted"])
        self.assertTrue(accepted["ingress_receipt_created"])
        self.assertFalse(accepted["canon_injury_created"])

    def test_replay_is_idempotent_and_conflicting_replay_is_rejected(self):
        data = load_fixture()
        attempts = events_of_type(data, "AUTOPTU_SEMANTIC_RESULT_INGRESS_ATTEMPT")
        noop = next(event for event in attempts if event.get("result") == "IDEMPOTENT_NO_OP")
        conflict = next(event for event in attempts if event.get("result") == "REJECT_CONFLICTING_REPLAY")
        self.assertEqual(noop["result_id"], conflict["result_id"])
        self.assertTrue(noop["semantic_identity_matches_committed_receipt"])
        self.assertFalse(conflict["semantic_identity_matches_committed_receipt"])
        self.assertEqual(noop["new_persistent_consequences"], 0)
        self.assertEqual(conflict["new_persistent_consequences"], 0)
        self.assertEqual(data["expected_final"]["duplicate_consequences"], 0)

    def test_minecraft_damage_signal_cannot_spoof_autoptu_authority(self):
        data = load_fixture()
        event = events_of_type(data, "MINECRAFT_PRESENTATION_EVENT_OBSERVED")[0]
        self.assertEqual(event["presentation_event"], "GENERIC_ENTITY_DAMAGE_SIGNAL")
        self.assertFalse(event["authoritative_autoptu_envelope_present"])
        self.assertEqual(event["result"], "REJECT_PRODUCER_AUTHORITY")
        self.assertFalse(event["persistent_consequence_created"])
        self.assertTrue(event["observation_record_allowed"])
        self.assertEqual(data["expected_final"]["minecraft_spoof_rejections"], 1)

    def test_subject_lineage_mismatch_is_quarantined_without_aggregate_misattribution(self):
        data = load_fixture()
        event = next(
            event for event in events_of_type(data, "AUTOPTU_SEMANTIC_RESULT_INGRESS_ATTEMPT")
            if event.get("result") == "QUARANTINE_SUBJECT_LINEAGE_UNRESOLVED"
        )
        self.assertNotEqual(event["subject_binding"], event["expected_handoff_subject_binding"])
        self.assertFalse(event["subject_lineage_valid"])
        self.assertFalse(event["persistent_consequence_created"])
        self.assertFalse(event["aggregate_consequence_created"])
        self.assertEqual(data["expected_final"]["aggregate_misattributions"], 0)

    def test_status_result_remains_quarantined_while_status_lifecycle_is_partial(self):
        data = load_fixture()
        event = next(
            event for event in events_of_type(data, "AUTOPTU_SEMANTIC_RESULT_INGRESS_ATTEMPT")
            if event.get("result") == "QUARANTINE_CAPABILITY_PATH_UNVERIFIED"
        )
        self.assertEqual(event["result_type"], "PTU_PERSISTENT_STATUS_APPLIED")
        self.assertIn("status_lifecycle", event["required_capability_families"])
        self.assertEqual(event["status_lifecycle_readiness"], "PARTIAL")
        self.assertFalse(event["persistent_consequence_created"])

    def test_restart_restores_one_receipt_without_duplicate_consequence(self):
        data = load_fixture()
        restart = events_of_type(data, "SERVER_RESTART")[0]
        self.assertEqual(restart["population_total_after_restart"], 12)
        self.assertEqual(restart["accepted_ingress_receipts_restored"], 1)
        self.assertEqual(restart["accepted_fixture_consequences_restored"], 1)
        self.assertEqual(restart["duplicate_consequences_after_restart"], 0)
        self.assertEqual(restart["quarantined_records_restored"], 2)
        self.assertFalse(restart["minecraft_noise_promoted_after_restart"])

    def test_fixture_does_not_claim_crypto_or_live_damage_parity(self):
        data = load_fixture()
        authority = data["authority_profile"]
        self.assertFalse(authority["cryptographic_authentication_claimed"])
        self.assertFalse(authority["live_damage_pipeline_claimed_verified"])
        self.assertFalse(data["scenario_is_canon"])

    def test_public_view_exposes_no_internal_ingress_identifiers(self):
        data = load_fixture()
        public = events_of_type(data, "PUBLIC_KNOWLEDGE_CHECK")[0]
        self.assertFalse(public["fixture_injury_exposed_as_canon_fact"])
        self.assertFalse(public["producer_id_exposed"])
        self.assertFalse(public["result_id_exposed"])
        self.assertFalse(public["battle_session_id_exposed"])
        self.assertFalse(public["internal_source_ref_exposed"])
        self.assertFalse(public["quarantine_state_exposed"])
        self.assertEqual(data["expected_final"]["internal_id_leaks"], 0)

    def test_reduced_fixture_keeps_live_engine_capability_states_conservative(self):
        data = load_fixture()
        deps = data["battle_dependency_categories"]
        self.assertEqual(deps["full_turn_round_lifecycle"], "PARTIAL")
        self.assertEqual(deps["full_stateful_damage_pipeline"], "PARTIAL")
        self.assertEqual(deps["status_lifecycle"], "PARTIAL")
        self.assertEqual(deps["ai_tactical_policy"], "BLOCKING")
        self.assertEqual(deps["minecraft_cobblemon_craftics_adapter_playback"], "PARTIAL_BLOCKING")


if __name__ == "__main__":
    unittest.main()
