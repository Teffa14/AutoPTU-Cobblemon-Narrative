import copy
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE_PATH = ROOT / "implementation" / "marea-sendero-resource-pressure-projection-trace-v1.json"


class EcologyProjectionFixtureTest(unittest.TestCase):
    def setUp(self):
        self.trace = json.loads(TRACE_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_noncanon_and_uses_existing_population(self):
        self.assertFalse(self.trace["scenario_is_canon"])
        self.assertFalse(self.trace["canon_scope"]["creates_new_canon"])
        self.assertEqual(
            ["ouros.marea.wild.sendero_lower_shelf.fletchling.v1"],
            self.trace["canon_scope"]["canon_population_refs"],
        )
        self.assertEqual(12, self.trace["starting_state"]["populations"]["ouros.marea.wild.sendero_lower_shelf.fletchling.v1"]["total"])

    def test_pressure_rules_change_projection_not_abundance(self):
        population = copy.deepcopy(self.trace["starting_state"]["populations"]["ouros.marea.wild.sendero_lower_shelf.fletchling.v1"])
        total = population["total"]
        population["resource_pressure"] += 0.20
        scarcity = self.trace["projection_rules"]["scarcity_search"]
        self.assertEqual("EXPANDED", scarcity["search_radius_band"])
        self.assertIn("sendero_margin", scarcity["eligible_microhabitats"])
        self.assertEqual(total, population["total"])
        population["disturbance_pressure"] += 0.40
        avoidance = self.trace["projection_rules"]["disturbance_avoidance"]
        self.assertEqual("REDUCED", avoidance["visibility_band"])
        self.assertNotIn("sendero_margin", avoidance["eligible_microhabitats"])
        self.assertEqual(total, population["total"])

    def test_every_reserved_candidate_uses_already_counted_source_class(self):
        reserves = []
        for window in self.trace["windows"]:
            for event in window.get("input_events", []):
                if event["event_type"] == "PROJECTION_CANDIDATE_RESERVE":
                    reserves.append(event)
        self.assertGreaterEqual(len(reserves), 2)
        for event in reserves:
            self.assertIn(event["source_class"], {"PERSISTENT_MEMBER", "UNRESOLVED_POOL_SLOT"})
            if event["source_class"] == "PERSISTENT_MEMBER":
                self.assertIn(event["member_id"], self.trace["canon_scope"]["canon_member_refs"])
            else:
                self.assertTrue(event["unresolved_slot_token"])

    def test_disturbance_rejection_is_explicit(self):
        rejected = [
            event
            for window in self.trace["windows"]
            for event in window.get("input_events", [])
            if event["event_type"] == "PROJECTION_CANDIDATE_REJECT_EXPECTED"
        ]
        self.assertEqual(1, len(rejected))
        self.assertEqual("CURRENT_POLICY_INELIGIBLE", rejected[0]["reason"])
        self.assertEqual("sendero_margin", rejected[0]["microhabitat"])

    def test_fixture_contains_no_demographic_event(self):
        forbidden = {
            "LOCAL_RECRUITMENT", "IMMIGRATION", "EMIGRATION", "ECOLOGICAL_MORTALITY",
            "CAPTURE_REMOVAL", "RELOCATION_IN", "RELOCATION_OUT"
        }
        kinds = {
            event["event_type"]
            for window in self.trace["windows"]
            for event in window.get("input_events", [])
        }
        self.assertTrue(forbidden.isdisjoint(kinds))


if __name__ == "__main__":
    unittest.main()
