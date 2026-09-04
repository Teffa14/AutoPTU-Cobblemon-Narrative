from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "replay_ecology_shared_resource_trace.py"
SPEC = importlib.util.spec_from_file_location("replay_ecology_shared_resource_trace", MODULE_PATH)
assert SPEC and SPEC.loader
replayer = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = replayer
SPEC.loader.exec_module(replayer)
TRACE_PATH = ROOT / "implementation" / "marea-sendero-shared-resource-multi-species-trace-v1.json"
SNAPSHOT_PATH = ROOT / "implementation" / "marea-sendero-shared-resource-final-snapshot-v1.json"


class SharedResourceReplayTest(unittest.TestCase):
    def load_trace(self) -> dict:
        return json.loads(TRACE_PATH.read_text(encoding="utf-8"))

    def expected_snapshot(self) -> dict:
        return json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))["expected_final_state"]

    def test_replay_matches_frozen_snapshot(self) -> None:
        state, _ = replayer.replay(self.load_trace())
        self.assertEqual(self.expected_snapshot(), replayer.canonical_snapshot(state))

    def test_replay_is_deterministic(self) -> None:
        trace = self.load_trace()
        first, first_windows = replayer.replay(copy.deepcopy(trace))
        second, second_windows = replayer.replay(copy.deepcopy(trace))
        self.assertEqual(first, second)
        self.assertEqual(first_windows, second_windows)

    def test_population_totals_are_isolated_from_resource_use(self) -> None:
        state, _ = replayer.replay(self.load_trace())
        self.assertEqual(12, state["populations"]["ouros.marea.wild.sendero_lower_shelf.fletchling.v1"]["total"])
        self.assertEqual(5, state["populations"]["fixture.marea.sendero.squawkabilly.v1"]["total"])
        self.assertEqual(3, state["resources"]["fixture.marea.sendero.lower_shelf.forage_patch.246"]["available_units"])

    def test_actor_history_does_not_leak_to_population_or_other_species(self) -> None:
        state, _ = replayer.replay(self.load_trace())
        actor = state["actors"]["ouros.marea.encounter.sendero_lower_shelf.fletchling.0"]
        self.assertEqual(1, actor["encounter_history_count"])
        self.assertNotIn("encounter_history_count", state["populations"]["fixture.marea.sendero.squawkabilly.v1"])
        self.assertEqual(0.22, state["populations"]["fixture.marea.sendero.squawkabilly.v1"]["resource_pressure"])

    def test_observation_without_confirmation_does_not_consume_resource(self) -> None:
        trace = self.load_trace()
        trace["windows"] = trace["windows"][:2]
        state, _ = replayer.replay(trace)
        self.assertEqual(8, state["resources"]["fixture.marea.sendero.lower_shelf.forage_patch.246"]["available_units"])

    def test_rejects_duplicate_resource_transaction(self) -> None:
        broken = copy.deepcopy(self.load_trace())
        duplicate = copy.deepcopy(broken["windows"][2]["input_events"][0])
        broken["windows"][3]["input_events"].insert(0, duplicate)
        with self.assertRaises(replayer.ReplayError):
            replayer.replay(broken)

    def test_overdraw_rejects_without_partial_resource_mutation(self) -> None:
        trace = self.load_trace()
        state = replayer.initial_state(trace)
        event = {
            "event_type": "RESOURCE_CONSUMPTION_CONFIRMED",
            "transaction_id": "tx.overdraw",
            "resource_id": "fixture.marea.sendero.lower_shelf.forage_patch.246",
            "consumer_population_id": "fixture.marea.sendero.squawkabilly.v1",
            "units": 9,
        }
        with self.assertRaises(replayer.ReplayError):
            replayer.apply_event(state, event)
        self.assertEqual(8, state["resources"]["fixture.marea.sendero.lower_shelf.forage_patch.246"]["available_units"])
        self.assertEqual([], state["resource_transactions"])

    def test_restart_preserves_scoped_ecology_state(self) -> None:
        state, _ = replayer.replay(self.load_trace())
        self.assertEqual(1, state["restart_count"])
        self.assertEqual(0.28, state["actors"]["ouros.marea.encounter.sendero_lower_shelf.fletchling.0"]["avoidance_pressure"])
        self.assertEqual(3, state["resources"]["fixture.marea.sendero.lower_shelf.forage_patch.246"]["available_units"])


if __name__ == "__main__":
    unittest.main()
