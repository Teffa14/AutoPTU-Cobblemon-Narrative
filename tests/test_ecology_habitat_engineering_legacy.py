import json
import unittest
from pathlib import Path


FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-habitat-engineering-legacy-trace-v1.json"


class HabitatEngineeringLegacyRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.trace = cls.data["trace"]

    def test_population_is_conserved(self):
        self.assertEqual(self.data["canon_guards"]["authoritative_fletchling_population"], 12)
        for step in self.trace:
            if "population" in step:
                self.assertEqual(step["population"], 12)
        self.assertFalse(self.data["canon_guards"]["new_persistent_actor_created"])

    def test_fixture_does_not_promote_structure_or_behavior_to_canon(self):
        guards = self.data["canon_guards"]
        self.assertFalse(guards["structure_is_canon"])
        self.assertFalse(guards["engineering_behavior_is_canon"])
        self.assertFalse(guards["facilitates_edge_is_canon"])
        self.assertFalse(guards["nest_or_territory_created"])

    def test_modification_persists_without_creator_projection(self):
        step = next(x for x in self.trace if x["event"] == "CREATOR_NOT_PRESENT_MODIFICATION_PERSISTS")
        self.assertEqual(step["physical_state"], "PRESENT")
        self.assertFalse(step["creator_currently_projected"])

    def test_recipient_use_does_not_imply_quality_ownership_or_growth(self):
        step = next(x for x in self.trace if x["event"] == "RECIPIENT_USE_OBSERVED")
        self.assertEqual(step["ecological_effect_state"], "RECIPIENT_USE_OBSERVED")
        forbidden = set(step["forbidden_claims"])
        self.assertTrue({"OWNERSHIP", "NESTING", "HABITAT_BENEFIT", "FACILITATES_CANON", "POPULATION_GROWTH"}.issubset(forbidden))

    def test_restart_preserves_legacy_and_history(self):
        step = next(x for x in self.trace if x["event"] == "RESTART_RESTORE")
        self.assertEqual(step["physical_state"], "PRESENT")
        self.assertTrue(step["recipient_use_history_preserved"])
        self.assertFalse(step["creator_currently_projected"])

    def test_unverified_tactical_semantics_fail_closed(self):
        step = next(x for x in self.trace if x["event"] == "TACTICAL_COVER_PROMOTION_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_facilitation_stays_hypothesis_without_comparative_effect(self):
        step = next(x for x in self.trace if x["event"] == "FACILITATION_PROMOTION_ATTEMPT")
        self.assertEqual(step["result"], "REMAIN_HYPOTHESIS")
        self.assertEqual(step["ecological_effect_state"], "FACILITATION_HYPOTHESIS")

    def test_closure_preserves_history_without_demographic_or_ptu_mutation(self):
        step = next(x for x in self.trace if x["event"] == "AUTHORITATIVE_PHYSICAL_CLOSURE")
        self.assertEqual(step["physical_state"], "CLOSED")
        self.assertTrue(step["historical_creator_attribution_preserved"])
        self.assertTrue(step["historical_recipient_use_preserved"])
        self.assertEqual(step["demographic_events"], 0)
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_all_sources_are_already_counted_fixture_or_authoritative_sources(self):
        counted = set(self.data["counted_sources"])
        creator = self.data["modification"]["creator_source_ref"]
        recipient = next(x for x in self.trace if x["event"] == "RECIPIENT_USE_OBSERVED")["recipient_source_ref"]
        self.assertIn(creator, counted)
        self.assertIn(recipient, counted)


if __name__ == "__main__":
    unittest.main()
