import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE_PATH = ROOT / "implementation" / "marea-sendero-projection-arbitration-trace-v1.json"
MODULE_PATH = ROOT / "tools" / "replay_ecology_projection_arbitration_trace.py"

spec = importlib.util.spec_from_file_location("projection_arbitration_replay", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class ProjectionArbitrationReplayTest(unittest.TestCase):
    def setUp(self):
        with TRACE_PATH.open("r", encoding="utf-8") as handle:
            self.trace = json.load(handle)

    def test_fixture_replays_to_expected_snapshot(self):
        self.assertEqual(module.validate(copy.deepcopy(self.trace)), self.trace["expected_final"])

    def test_replay_is_deterministic(self):
        first = module.validate(copy.deepcopy(self.trace))
        second = module.validate(copy.deepcopy(self.trace))
        self.assertEqual(first, second)

    def test_population_and_identity_survive_restart(self):
        result = module.validate(copy.deepcopy(self.trace))
        self.assertEqual(result["population_total"], 12)
        self.assertEqual(
            result["persistent_actor_id"],
            "ouros.marea.encounter.sendero_lower_shelf.fletchling.0",
        )
        self.assertIsNone(result["runtime_minecraft_uuid"])
        self.assertEqual(result["demographic_events"], 0)

    def test_indirect_sign_cannot_leak_persistent_actor_identity(self):
        broken = copy.deepcopy(self.trace)
        sign = next(event for event in broken["events"] if event["type"] == "INDIRECT_SIGN_EMITTED")
        sign["persistent_actor_id"] = self.trace["persistent_actor"]["actor_id"]
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_indirect_sign_cannot_open_autoptu(self):
        broken = copy.deepcopy(self.trace)
        sign = next(event for event in broken["events"] if event["type"] == "INDIRECT_SIGN_EMITTED")
        sign["autoptu_handoff"] = "OPEN_AUTOPTU"
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_direct_materialization_requires_prior_lease(self):
        broken = copy.deepcopy(self.trace)
        broken["events"] = [
            event for event in broken["events"] if event.get("lease_id") != "lease.249.direct.001" or event["type"] != "PROJECTION_LEASE_RESERVED"
        ]
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_one_source_cannot_hold_two_active_direct_leases(self):
        broken = copy.deepcopy(self.trace)
        second_reservation = next(
            event for event in broken["events"] if event.get("lease_id") == "lease.249.direct.002"
        )
        second_reservation["seq"] = 10.5
        insert_at = next(i for i, event in enumerate(broken["events"]) if event["seq"] == 11)
        broken["events"].insert(insert_at, broken["events"].pop(broken["events"].index(second_reservation)))
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_uncorrelated_native_entity_cannot_authorize_ecology_write(self):
        broken = copy.deepcopy(self.trace)
        quarantine = next(
            event
            for event in broken["events"]
            if event.get("decision") == "QUARANTINE_UNCORRELATED_ENTITY"
        )
        quarantine["ecology_write_authorized"] = True
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_relay_cannot_manufacture_independent_corroboration(self):
        broken = copy.deepcopy(self.trace)
        relay = next(event for event in broken["events"] if event["type"] == "SIGN_RELAYED")
        relay["new_independent_root_created"] = True
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_despawn_cannot_be_demographic_event(self):
        broken = copy.deepcopy(self.trace)
        despawn = next(event for event in broken["events"] if event["type"] == "COBBLEMON_ENTITY_DESPAWNED")
        despawn["demographic_effect"] = "DEATH"
        with self.assertRaises(module.ReplayError):
            module.validate(broken)


if __name__ == "__main__":
    unittest.main()
