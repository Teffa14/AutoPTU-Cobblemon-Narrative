import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "implementation" / "marea-sendero-cue-quality-divergence-trace-v1.json"


class CueQualityDivergenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.trace = cls.data["trace"]

    def test_population_remains_canon_twelve(self):
        self.assertEqual(self.data["canon_guards"]["authoritative_fletchling_population"], 12)
        self.assertTrue(all(step.get("population", 12) == 12 for step in self.trace))
        self.assertEqual(self.data["assertions"]["population_values_are_always"], [12])

    def test_fixture_does_not_promote_trap_or_cue_to_canon(self):
        guards = self.data["canon_guards"]
        self.assertFalse(guards["cue_is_canon"])
        self.assertFalse(guards["site_quality_is_canon"])
        self.assertFalse(guards["ecological_trap_is_canon"])
        self.assertFalse(guards["new_persistent_actor_created"])

    def test_repeated_use_does_not_prove_quality(self):
        attempt = next(s for s in self.trace if s["action"] == "TRY_INFER_GOOD_HABITAT_FROM_USE")
        self.assertEqual(attempt["result"], "REJECTED_INSUFFICIENT_QUALITY_EVIDENCE")
        self.assertEqual(attempt["quality_evidence_state"], "UNKNOWN")

    def test_ecological_trap_requires_comparative_evidence(self):
        attempt = next(s for s in self.trace if s["action"] == "TRY_DECLARE_ECOLOGICAL_TRAP_FROM_USE_ONLY")
        self.assertEqual(attempt["result"], "REJECTED_COMPARATIVE_OUTCOME_EVIDENCE_MISSING")
        self.assertEqual(attempt["trap_hypothesis_state"], "UNRESOLVED")
        cost = next(s for s in self.trace if s["action"] == "ADD_LOCAL_COST_SIGNAL")
        self.assertEqual(cost["quality_evidence_state"], "OUTCOME_SIGNAL_PRESENT")
        self.assertEqual(cost["trap_hypothesis_state"], "UNRESOLVED")

    def test_only_counted_sources_are_presented(self):
        visible = next(s for s in self.trace if s["action"] == "REPEATED_USE_WINDOW")["visible_counted_sources"]
        self.assertTrue(set(visible).issubset(set(self.data["counted_sources"])))

    def test_minecraft_cannot_author_ptu_aftermath(self):
        step = next(s for s in self.trace if s["action"] == "MINECRAFT_GENERIC_DAMAGE_PRESENTATION")
        self.assertEqual(step["result"], "REJECT_UNAUTHORIZED_PTU_STATE")
        self.assertFalse(step["injury_created"])
        self.assertFalse(step["status_created"])
        self.assertFalse(step["hp_mutated"])

    def test_restart_and_cue_removal_preserve_history_and_uncertainty(self):
        restart = next(s for s in self.trace if s["action"] == "RESTART")
        self.assertEqual(restart["restored_trap_hypothesis_state"], "UNRESOLVED")
        removed = next(s for s in self.trace if s["action"] == "REMOVE_CUE")
        self.assertFalse(removed["history_rewritten"])
        self.assertFalse(removed["recovery_claim_created"])
        self.assertEqual(removed["trap_hypothesis_state"], "UNRESOLVED")

    def test_no_demography_or_autoptu_handoff(self):
        assertions = self.data["assertions"]
        self.assertTrue(assertions["no_demographic_events"])
        self.assertTrue(assertions["no_autoptu_handoff"])


if __name__ == "__main__":
    unittest.main()
