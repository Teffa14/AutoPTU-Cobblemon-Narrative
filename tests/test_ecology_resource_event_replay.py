import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "resource_event_replay", ROOT / "tools" / "replay_ecology_resource_event_trace.py"
)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)


class ResourceScarcityWorldEventReplayTest(unittest.TestCase):
    def setUp(self):
        self.trace = module.load_trace(
            ROOT / "implementation" / "marea-sendero-resource-scarcity-world-event-trace-v1.json"
        )

    def test_replay_is_deterministic_and_conserves_population(self):
        first, _ = module.replay(copy.deepcopy(self.trace))
        second, _ = module.replay(copy.deepcopy(self.trace))
        self.assertEqual(first, second)
        population = first["populations"]["ouros.marea.wild.sendero_lower_shelf.fletchling.v1"]
        self.assertEqual(12, population["total"])
        self.assertEqual(0.20, population["resource_pressure"])
        resource = first["resources"]["fixture.marea.sendero.lower_shelf.forage_patch.247"]
        self.assertEqual(5, resource["available_units"])

    def test_event_opens_from_world_state_and_clears_with_hysteresis(self):
        _, snapshots = module.replay(copy.deepcopy(self.trace))
        phases = {snapshot["window_id"]: snapshot["events"]["fixture.event.sendero.resource_scarcity.247"]["phase"] for snapshot in snapshots}
        self.assertEqual("ACTIVE", phases["R2_EVENT_OPENS_FROM_WORLD_STATE"])
        self.assertEqual("STABILIZING", phases["R7_FIRST_CLEAR_EVALUATION"])
        self.assertEqual("RESOLVED", phases["R8_SECOND_CLEAR_EVALUATION"])

    def test_knowledge_can_lag_resolved_world_truth(self):
        state, _ = module.replay(copy.deepcopy(self.trace))
        event = state["events"]["fixture.event.sendero.resource_scarcity.247"]
        claim = state["knowledge_holders"]["fixture.marea.field_observer.247"]["claims"]["claim.247.resource_scarcity"]
        self.assertEqual("RESOLVED", event["phase"])
        self.assertEqual("SUSPECTED", claim["state"])
        self.assertEqual("LOW", claim["confidence_band"])
        self.assertEqual(2, claim["relay_count"])
        self.assertEqual(["obs.247.001"], claim["source_roots"])

    def test_observation_cannot_leak_hidden_resource_units(self):
        trace = copy.deepcopy(self.trace)
        trace["windows"][3]["input_events"][0]["exposes_hidden_resource_units"] = True
        with self.assertRaises(module.ReplayError):
            module.replay(trace)

    def test_duplicate_resource_transaction_is_rejected(self):
        trace = copy.deepcopy(self.trace)
        duplicate = copy.deepcopy(trace["windows"][1]["input_events"][0])
        trace["windows"][2]["input_events"].insert(0, duplicate)
        with self.assertRaises(module.ReplayError):
            module.replay(trace)

    def test_one_clear_evaluation_cannot_resolve_event(self):
        trace = copy.deepcopy(self.trace)
        trace["windows"] = [window for window in trace["windows"] if window["id"] != "R8_SECOND_CLEAR_EVALUATION"]
        state, _ = module.replay(trace)
        self.assertEqual("STABILIZING", state["events"]["fixture.event.sendero.resource_scarcity.247"]["phase"])

    def test_relay_does_not_upgrade_confidence(self):
        state, _ = module.replay(copy.deepcopy(self.trace))
        claim = state["knowledge_holders"]["fixture.marea.field_observer.247"]["claims"]["claim.247.resource_scarcity"]
        self.assertEqual("LOW", claim["confidence_band"])
        self.assertEqual("SUSPECTED", claim["state"])


if __name__ == "__main__":
    unittest.main()
