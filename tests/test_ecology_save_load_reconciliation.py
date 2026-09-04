import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "implementation" / "marea-sendero-cobblemon-save-load-reconciliation-fixture-v1.json"


class EcologySaveLoadReconciliationTest(unittest.TestCase):
    def setUp(self):
        with FIXTURE_PATH.open("r", encoding="utf-8") as handle:
            self.fixture = json.load(handle)
        self.events = self.fixture["events"]

    def events_of_type(self, event_type):
        return [event for event in self.events if event["type"] == event_type]

    def test_fixture_is_non_canon_and_population_is_existing_fletchling(self):
        self.assertFalse(self.fixture["scenario_is_canon"])
        self.assertEqual(self.fixture["population"]["species_id"], "cobblemon:fletchling")
        self.assertEqual(self.fixture["population"]["total"], 12)

    def test_source_verified_load_surface_is_cancelable_but_runtime_receipt_is_not_claimed_verified(self):
        primitives = self.fixture["verified_adapter_primitives"]
        self.assertEqual(primitives["pokemon_entity_load_event"], "CobblemonEvents.POKEMON_ENTITY_LOAD")
        self.assertTrue(primitives["load_event_cancelable"])
        self.assertFalse(primitives["runtime_dependency_pin_verified"])
        self.assertFalse(primitives["custom_receipt_roundtrip_runtime_verified"])

    def test_save_and_restore_do_not_change_population(self):
        for event in self.events:
            if "population_delta" in event:
                self.assertEqual(event["population_delta"], 0)
        self.assertEqual(self.fixture["expected_final"]["population_total"], 12)
        self.assertEqual(self.fixture["expected_final"]["demographic_events"], 0)

    def test_valid_load_reconciles_same_actor_without_autoptu_handoff(self):
        loads = self.events_of_type("POKEMON_ENTITY_LOAD_CALLBACK")
        valid = next(event for event in loads if event["decision"] == "RECONCILE_EXISTING_PROJECTION")
        self.assertEqual(valid["receipt_actor_id"], self.fixture["persistent_actor"]["actor_id"])
        self.assertFalse(valid["cancel_event"])
        self.assertFalse(valid["autoptu_eligible"])
        self.assertEqual(self.fixture["expected_final"]["autoptu_handoffs"], 0)

    def test_stale_epoch_fails_closed(self):
        loads = self.events_of_type("POKEMON_ENTITY_LOAD_CALLBACK")
        stale = next(event for event in loads if event["decision"] == "REJECT_STALE_OR_CONFLICTING_RECEIPT")
        valid = next(event for event in loads if event["decision"] == "RECONCILE_EXISTING_PROJECTION")
        self.assertLess(stale["receipt_projection_epoch"], valid["receipt_projection_epoch"])
        self.assertTrue(stale["cancel_event"])
        self.assertFalse(stale["persistent_actor_created"])

    def test_unclaimed_managed_load_fails_closed(self):
        loads = self.events_of_type("POKEMON_ENTITY_LOAD_CALLBACK")
        unclaimed = next(event for event in loads if event["decision"] == "UNCLAIMED_LOAD_FAIL_CLOSED")
        self.assertFalse(unclaimed["receipt_present"])
        self.assertTrue(unclaimed["managed_scope"])
        self.assertTrue(unclaimed["cancel_event"])
        self.assertFalse(unclaimed["persistent_actor_created"])

    def test_new_uuid_does_not_create_new_actor(self):
        correlations = self.events_of_type("UUID_CORRELATED_TO_LEASE")
        self.assertNotEqual(correlations[0]["minecraft_uuid"], correlations[1]["minecraft_uuid"])
        self.assertEqual(
            self.fixture["expected_final"]["persistent_actor_id"],
            self.fixture["persistent_actor"]["actor_id"],
        )

    def test_released_lease_is_not_reused_for_fresh_projection(self):
        releases = self.events_of_type("PROJECTION_LEASE_RELEASED")
        reserves = self.events_of_type("PROJECTION_LEASE_RESERVED")
        released = releases[0]["lease_id"]
        later = reserves[-1]
        self.assertNotEqual(released, later["lease_id"])
        self.assertEqual(later["source_id"], self.fixture["persistent_actor"]["actor_id"])
        self.assertEqual(later["projection_epoch"], 8)


if __name__ == "__main__":
    unittest.main()
