import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "implementation" / "marea-sendero-diegetic-marker-recognition-trace-v1.json"


class EcologyDiegeticMarkerRecognitionTest(unittest.TestCase):
    def setUp(self):
        with FIXTURE_PATH.open("r", encoding="utf-8") as handle:
            self.fixture = json.load(handle)
        self.events = self.fixture["events"]

    def events_of_type(self, event_type):
        return [event for event in self.events if event["type"] == event_type]

    def test_fixture_is_non_canon_and_reuses_existing_population(self):
        self.assertFalse(self.fixture["scenario_is_canon"])
        self.assertEqual(self.fixture["population"]["species_id"], "cobblemon:fletchling")
        self.assertEqual(self.fixture["population"]["total"], 12)
        self.assertTrue(self.fixture["hidden_truth"]["marker_binding_is_fixture_only"])
        self.assertFalse(self.fixture["marker_registry"][0]["canon_authorized"])

    def test_recognition_and_marker_lifecycle_never_change_population_or_open_autoptu(self):
        for event in self.events:
            if "population_delta" in event:
                self.assertEqual(event["population_delta"], 0)
            if "autoptu_handoff" in event:
                self.assertFalse(event["autoptu_handoff"])
        self.assertEqual(self.fixture["expected_final"]["population_total"], 12)
        self.assertEqual(self.fixture["expected_final"]["demographic_events"], 0)
        self.assertEqual(self.fixture["expected_final"]["autoptu_handoffs"], 0)

    def test_public_observation_never_exposes_hidden_identity_fields(self):
        forbidden = set(self.fixture["public_payload_forbidden_fields"])
        for observation in self.events_of_type("FIELD_OBSERVATION_CAPTURED"):
            self.assertTrue(forbidden.isdisjoint(observation["public_evidence"].keys()))
        lookup = self.events_of_type("MARKER_REGISTRY_LOOKUP")[0]
        self.assertFalse(lookup["hidden_actor_id_exposed"])
        updates = self.events_of_type("IDENTITY_HYPOTHESIS_UPDATED")
        for update in updates:
            if "public_actor_identity_exposed" in update:
                self.assertFalse(update["public_actor_identity_exposed"])
        self.assertFalse(self.fixture["expected_final"]["hidden_actor_identity_exposed"])

    def test_active_unique_marker_with_high_quality_observation_can_confirm(self):
        registry = self.fixture["marker_registry"][0]
        observation = self.events_of_type("FIELD_OBSERVATION_CAPTURED")[0]
        lookup = self.events_of_type("MARKER_REGISTRY_LOOKUP")[0]
        confirm = next(
            event
            for event in self.events_of_type("IDENTITY_HYPOTHESIS_UPDATED")
            if event["to"] == "CONFIRMED_BY_DIEGETIC_MARKER"
        )
        self.assertEqual(registry["validity_state"], "ACTIVE")
        self.assertEqual(observation["public_evidence"]["marker_read_quality"], "HIGH")
        self.assertEqual(lookup["active_candidate_count"], 1)
        self.assertEqual(confirm["supporting_root"], observation["provenance_root"])
        self.assertEqual(confirm["marker_record_id"], lookup["public_marker_record_id"])

    def test_poor_resighting_cannot_create_new_confirmation(self):
        observation = self.events_of_type("FIELD_OBSERVATION_CAPTURED")[1]
        evaluation = next(
            event
            for event in self.events_of_type("IDENTITY_HYPOTHESIS_EVALUATED")
            if event["reason"] == "POOR_RESIGHT_DOES_NOT_OVERRIDE_EXISTING_VALID_CONFIRMATION"
        )
        self.assertEqual(observation["public_evidence"]["marker_read_quality"], "LOW")
        self.assertIsNone(observation["public_evidence"]["observable_marker_code"])
        self.assertFalse(evaluation["new_confirmation_created"])

    def test_lost_marker_downgrades_current_certainty_but_preserves_history(self):
        validity_change = self.events_of_type("MARKER_VALIDITY_CHANGED")[0]
        downgrade = next(
            event
            for event in self.events_of_type("IDENTITY_HYPOTHESIS_UPDATED")
            if event["reason"] == "MARKER_NO_LONGER_ACTIVE"
        )
        self.assertEqual(validity_change["from"], "ACTIVE")
        self.assertEqual(validity_change["to"], "REPORTED_LOST")
        self.assertEqual(downgrade["from"], "CONFIRMED_BY_DIEGETIC_MARKER")
        self.assertEqual(downgrade["to"], "PROBABLE_SAME_INDIVIDUAL")
        self.assertTrue(downgrade["historical_confirmation_preserved"])
        self.assertTrue(self.fixture["expected_final"]["historical_marker_confirmation_preserved"])

    def test_unverified_trainer_feature_modifier_is_not_applied(self):
        modifier = self.events_of_type("TRAINER_OBSERVATION_MODIFIER_PROPOSED")[0]
        self.assertEqual(modifier["engine_support_state"], "UNVERIFIED_FOR_THIS_USE")
        self.assertFalse(modifier["effect_applied"])
        self.assertFalse(self.fixture["expected_final"]["trainer_feature_modifier_applied"])

    def test_restart_preserves_marker_validity_and_epistemic_state(self):
        restart = self.events_of_type("SERVER_RESTART")[0]
        self.assertEqual(restart["population_total_after_restart"], 12)
        self.assertEqual(restart["marker_registry_state_after_restart"], "REPORTED_LOST")
        self.assertEqual(restart["hypothesis_state_after_restart"], "PROBABLE_SAME_INDIVIDUAL")
        self.assertEqual(self.fixture["expected_final"]["marker_validity_state"], "REPORTED_LOST")
        self.assertEqual(
            self.fixture["expected_final"]["current_hypothesis_state"],
            "PROBABLE_SAME_INDIVIDUAL",
        )


if __name__ == "__main__":
    unittest.main()
