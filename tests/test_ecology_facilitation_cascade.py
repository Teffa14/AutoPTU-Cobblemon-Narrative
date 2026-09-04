import json
import unittest
from pathlib import Path


FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-facilitation-cascade-trace-v1.json"


class FacilitationCascadeRegression(unittest.TestCase):
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
        self.assertFalse(self.data["canon_guards"]["population_growth_claimed"])

    def test_cascade_remains_fixture_only(self):
        self.assertFalse(self.data["canon_guards"]["cascade_is_canon"])
        self.assertFalse(self.data["canon_guards"]["species_behavior_is_canon"])

    def test_cooccurrence_does_not_prove_dependency(self):
        step = next(x for x in self.trace if x["event"] == "COOCCURRENCE_EDGE_ATTEMPT")
        self.assertEqual(step["result"], "REMAIN_DEPENDENCY_HYPOTHESIS")

    def test_direct_edges_require_direct_evidence(self):
        accepted = [x for x in self.trace if x["event"] == "DIRECT_DEPENDENCY_EVIDENCE_ACCEPTED"]
        self.assertEqual({x["edge"] for x in accepted}, {"A_TO_B", "B_TO_C"})
        self.assertTrue(all(x["interpretation_state"] == "DIRECT_DEPENDENCY_SUPPORTED" for x in accepted))
        self.assertTrue(all(x["canon_status"] == "FIXTURE_ONLY" for x in accepted))

    def test_transitive_closure_is_forbidden(self):
        step = next(x for x in self.trace if x["event"] == "TRANSITIVE_EDGE_INFERENCE_ATTEMPT")
        self.assertEqual(step["requested_edge"], "A_TO_C")
        self.assertEqual(step["result"], "REJECT_TRANSITIVE_INFERENCE")

    def test_tactical_semantics_fail_closed(self):
        step = next(x for x in self.trace if x["event"] == "TACTICAL_SEMANTICS_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_upstream_closure_does_not_recursively_delete_descendants(self):
        step = next(x for x in self.trace if x["event"] == "AUTHORITATIVE_UPSTREAM_CLOSURE")
        self.assertEqual(step["edge_A_TO_B_validity"], "HISTORICAL")
        self.assertEqual(step["node_b_physical_state"], "PRESENT")
        self.assertFalse(step["descendants_recursively_deleted"])

    def test_restart_preserves_graph_without_synthesizing_edge(self):
        step = next(x for x in self.trace if x["event"] == "RESTART_RESTORE")
        self.assertTrue(step["historical_edge_A_TO_B_preserved"])
        self.assertTrue(step["active_edge_B_TO_C_preserved"])
        self.assertFalse(step["transitive_edge_A_TO_C_present"])
        self.assertEqual(step["demographic_events"], 0)
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)


if __name__ == "__main__":
    unittest.main()
