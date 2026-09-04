import json
import unittest
from pathlib import Path


FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-resource-pulse-trace-v1.json"


class ResourcePulseWorldEventTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.trace = cls.data["trace"]

    def test_canon_population_is_conserved(self):
        self.assertEqual(self.data["canon_guards"]["authoritative_fletchling_population"], 12)
        populations = {step["population"] for step in self.trace if "population" in step}
        self.assertEqual(populations, {12})
        self.assertEqual(self.data["assertions"]["population_values_are_always"], [12])

    def test_pulse_creates_no_demographic_transaction(self):
        for step in self.trace:
            self.assertEqual(step.get("demographic_events", []), [])
        self.assertTrue(self.data["assertions"]["no_demographic_events"])

    def test_peak_uses_only_already_counted_sources(self):
        counted = set(self.data["counted_sources"])
        peak = next(step for step in self.trace if step["action"] == "PEAK_PROJECTION")
        self.assertTrue(set(peak["visible_counted_sources"]).issubset(counted))
        self.assertFalse(peak["public_population_growth_claim"])

    def test_restart_and_presentation_changes_do_not_expire_pulse(self):
        restart = next(step for step in self.trace if step["action"] == "RESTART")
        presentation = next(step for step in self.trace if step["action"] == "DAY_NIGHT_AND_CHUNK_PRESENTATION_CHANGES")
        self.assertFalse(restart["expired"])
        self.assertFalse(presentation["event_expired"])
        self.assertTrue(self.data["assertions"]["restart_does_not_expire_event"])

    def test_resource_wave_shift_does_not_invent_movement(self):
        shift = next(step for step in self.trace if step["action"] == "SHIFT_RESOURCE_WAVE_SCOPE")
        self.assertFalse(shift["actor_movement_asserted"])
        self.assertFalse(shift["teleport_asserted"])
        self.assertFalse(shift["forced_movement_asserted"])
        self.assertEqual(shift["source_identity_mutations"], [])

    def test_fixture_does_not_mutate_ptu_or_handoff_to_autoptu(self):
        close = next(step for step in self.trace if step["action"] == "CLOSE_BY_SEMANTIC_HORIZON")
        self.assertEqual(close["ptu_state_mutations"], [])
        self.assertEqual(close["autoptu_handoffs"], [])
        self.assertTrue(self.data["assertions"]["no_ptu_state_mutation"])
        self.assertTrue(self.data["assertions"]["no_autoptu_handoff"])

    def test_fixture_resource_and_site_are_not_canon(self):
        guards = self.data["canon_guards"]
        self.assertFalse(guards["resource_is_canon"])
        self.assertFalse(guards["site_variant_is_canon"])
        self.assertFalse(guards["new_persistent_actor_created"])


if __name__ == "__main__":
    unittest.main()
