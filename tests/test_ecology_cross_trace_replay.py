from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "replay_ecology_cross_trace.py"
SPEC = importlib.util.spec_from_file_location("replay_ecology_cross_trace", MODULE_PATH)
assert SPEC and SPEC.loader
replayer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(replayer)
TRACE_PATH = ROOT / "implementation" / "marea-sendero-persistent-actor-cross-fixture-trace-v1.json"
SNAPSHOT_PATH = ROOT / "implementation" / "marea-sendero-persistent-actor-final-snapshot-v1.json"


class EcologyCrossTraceReplayTest(unittest.TestCase):
    def load_trace(self) -> dict:
        return json.loads(TRACE_PATH.read_text(encoding="utf-8"))

    def expected_snapshot(self) -> dict:
        return json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))["expected_final_state"]

    def test_replay_matches_frozen_final_snapshot(self) -> None:
        state, _ = replayer.replay(self.load_trace())
        self.assertEqual(self.expected_snapshot(), replayer.canonical_snapshot(state))

    def test_replay_is_deterministic(self) -> None:
        trace = self.load_trace()
        first, first_windows = replayer.replay(copy.deepcopy(trace))
        second, second_windows = replayer.replay(copy.deepcopy(trace))
        self.assertEqual(replayer.canonical_snapshot(first), replayer.canonical_snapshot(second))
        self.assertEqual(first_windows, second_windows)

    def test_restart_clears_entity_uuid_but_keeps_actor_and_lease(self) -> None:
        state, _ = replayer.replay(self.load_trace())
        snapshot = replayer.canonical_snapshot(state)
        self.assertEqual("ouros.marea.encounter.sendero_lower_shelf.fletchling.0", snapshot["persistent_actor_ref"])
        self.assertEqual("trace.lease.fletchling.001", snapshot["active_projection_lease"])
        self.assertEqual("SUSPENDED", snapshot["projection_lease_state"])
        self.assertIsNone(snapshot["minecraft_entity_uuid"])

    def test_rejects_semantic_result_for_wrong_battle(self) -> None:
        broken = copy.deepcopy(self.load_trace())
        window = next(item for item in broken["windows"] if item["id"] == "T6_AUTOPTU_SEMANTIC_KO_RETURN")
        window["input_events"][0]["battle_id"] = "trace.battle.wrong"
        with self.assertRaises(replayer.ReplayError):
            replayer.replay(broken)

    def test_rejects_second_projection_lease(self) -> None:
        broken = copy.deepcopy(self.load_trace())
        window = next(item for item in broken["windows"] if item["id"] == "T2_DIRECT_OBSERVATION")
        window["input_events"].insert(0, {
            "event_type": "LEASE_RESERVE",
            "lease_id": "trace.lease.illegal.duplicate",
            "member_id": broken["persistent_actor_ref"]
        })
        with self.assertRaises(replayer.ReplayError):
            replayer.replay(broken)

    def test_rejects_battle_as_direct_ecology_resolution(self) -> None:
        broken = copy.deepcopy(self.load_trace())
        window = next(item for item in broken["windows"] if item["id"] == "T8_SOURCE_EVENT_REEVALUATES")
        window["input_events"][0]["battle_result_is_direct_resolution"] = True
        with self.assertRaises(replayer.ReplayError):
            replayer.replay(broken)


if __name__ == "__main__":
    unittest.main()
