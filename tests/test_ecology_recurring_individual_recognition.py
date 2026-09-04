import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "implementation" / "marea-sendero-recurring-individual-recognition-trace-v1.json"


class EcologyRecurringIndividualRecognitionTest(unittest.TestCase):
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
        self.assertFalse(self.fixture["hidden_truth"]["confounder_is_canon_actor"])

    def test_recognition_never_changes_population_or_opens_autoptu(self):
        for event in self.events:
            if "population_delta" in event:
                self.assertEqual(event["population_delta"], 0)
            if "autoptu_handoff" in event:
                self.assertFalse(event["autoptu_handoff"])
        self.assertEqual(self.fixture["expected_final"]["population_total"], 12)
        self.assertEqual(self.fixture["expected_final"]["demographic_events"], 0)
        self.assertEqual(self.fixture["expected_final"]["autoptu_handoffs"], 0)

    def test_public_evidence_does_not_expose_internal_identity_fields(self):
        forbidden = set(self.fixture["public_payload_forbidden_fields"])
        observations = self.events_of_type("FIELD_OBSERVATION_CAPTURED")
        for observation in observations:
            public_fields = set(observation["public_evidence"].keys())
            self.assertTrue(forbidden.isdisjoint(public_fields))
        for event in self.events:
            if "public_actor_identity_exposed" in event:
                self.assertFalse(event["public_actor_identity_exposed"])
        self.assertFalse(self.fixture["expected_final"]["hidden_actor_identity_exposed"])

    def test_two_independent_compatible_roots_only_promote_to_possible(self):
        update = next(
            event
            for event in self.events_of_type("IDENTITY_HYPOTHESIS_UPDATED")
            if event["to"] == "POSSIBLE_SAME_INDIVIDUAL"
        )
        self.assertEqual(len(set(update["independent_roots"])), 2)
        self.assertEqual(update["from"], "UNRESOLVED")

    def test_relay_does_not_fabricate_corroboration(self):
        relay = self.events_of_type("OBSERVATION_RELAYED")[0]
        evaluation = next(
            event
            for event in self.events_of_type("IDENTITY_HYPOTHESIS_EVALUATED")
            if event.get("reason") == "RELAY_DOES_NOT_CORROBORATE"
        )
        self.assertFalse(relay["counts_as_independent_root"])
        self.assertEqual(evaluation["state_before"], evaluation["state_after"])
        self.assertEqual(evaluation["independent_root_count"], 2)

    def test_confounder_opens_ambiguity_instead_of_silent_merge(self):
        evaluation = next(
            event
            for event in self.events_of_type("IDENTITY_HYPOTHESIS_EVALUATED")
            if event.get("competing_candidate_opened")
        )
        self.assertTrue(evaluation["competing_candidate_opened"])
        self.assertFalse(evaluation["auto_merge_performed"])
        self.assertEqual(evaluation["contradiction_preserved"], "RETREAT_VECTOR_CONFLICT")
        self.assertEqual(evaluation["state_after"], "POSSIBLE_SAME_INDIVIDUAL")

    def test_ordinary_field_evidence_is_capped_at_probable(self):
        final_update = next(
            event
            for event in self.events_of_type("IDENTITY_HYPOTHESIS_UPDATED")
            if event["to"] == "PROBABLE_SAME_INDIVIDUAL"
        )
        self.assertEqual(len(set(final_update["supporting_independent_roots"])), 3)
        self.assertEqual(
            final_update["certainty_cap_reason"],
            "NO_CANON_APPROVED_STABLE_INDIVIDUAL_MARKER",
        )
        self.assertFalse(self.fixture["expected_final"]["confirmed_identity"])

    def test_restart_preserves_epistemic_state_without_entity_continuity(self):
        restart = self.events_of_type("SERVER_RESTART")[0]
        restored = self.events_of_type("OBSERVER_KNOWLEDGE_RESTORED")[0]
        self.assertFalse(restart["minecraft_entity_continuity_required"])
        self.assertEqual(restored["state"], "PROBABLE_SAME_INDIVIDUAL")
        self.assertFalse(restored["hidden_actor_id_in_public_record"])
        self.assertEqual(restart["population_total_after_restart"], 12)


if __name__ == "__main__":
    unittest.main()
