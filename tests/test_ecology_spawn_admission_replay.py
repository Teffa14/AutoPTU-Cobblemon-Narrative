import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE_PATH = ROOT / "implementation" / "marea-sendero-cobblemon-spawn-admission-fixture-v1.json"
MODULE_PATH = ROOT / "tools" / "replay_ecology_spawn_admission_trace.py"

spec = importlib.util.spec_from_file_location("spawn_admission_replay", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class SpawnAdmissionReplayTest(unittest.TestCase):
    def setUp(self):
        with TRACE_PATH.open("r", encoding="utf-8") as handle:
            self.trace = json.load(handle)

    def test_fixture_replays_to_expected_snapshot(self):
        self.assertEqual(module.validate(copy.deepcopy(self.trace)), self.trace["expected_final"])

    def test_managed_direct_requires_prior_lease(self):
        broken = copy.deepcopy(self.trace)
        broken["events"] = [event for event in broken["events"] if event["type"] != "PROJECTION_LEASE_RESERVED"]
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_managed_direct_requires_token(self):
        broken = copy.deepcopy(self.trace)
        callback = next(event for event in broken["events"] if event.get("admission_class") == "OUROS_MANAGED_DIRECT")
        callback["token_id"] = "missing.token"
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_uncontrolled_natural_must_be_cancelled(self):
        broken = copy.deepcopy(self.trace)
        callback = next(event for event in broken["events"] if event.get("admission_class") == "UNCONTROLLED_NATURAL")
        callback["cancel_event"] = False
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_uncontrolled_natural_cannot_create_persistent_actor(self):
        broken = copy.deepcopy(self.trace)
        callback = next(event for event in broken["events"] if event.get("admission_class") == "UNCONTROLLED_NATURAL")
        callback["persistent_actor_created"] = True
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_owned_or_system_presentation_must_not_be_blanket_cancelled(self):
        broken = copy.deepcopy(self.trace)
        callback = next(
            event
            for event in broken["events"]
            if event.get("admission_class") == "EXEMPT_OWNED_OR_SYSTEM_PRESENTATION"
        )
        callback["cancel_event"] = True
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_owned_presentation_cannot_join_wild_population(self):
        broken = copy.deepcopy(self.trace)
        callback = next(
            event
            for event in broken["events"]
            if event.get("admission_class") == "EXEMPT_OWNED_OR_SYSTEM_PRESENTATION"
        )
        callback["wild_population_membership_created"] = True
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_token_cannot_be_reused_for_second_entity(self):
        broken = copy.deepcopy(self.trace)
        callback = next(event for event in broken["events"] if event.get("admission_class") == "OUROS_MANAGED_DIRECT")
        duplicate = copy.deepcopy(callback)
        duplicate["seq"] = 7.5
        duplicate["minecraft_uuid"] = "00000000-0000-0000-0000-000000250002"
        broken["events"].append(duplicate)
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_despawn_cannot_be_demographic_event(self):
        broken = copy.deepcopy(self.trace)
        despawn = next(event for event in broken["events"] if event["type"] == "COBBLEMON_ENTITY_DESPAWNED")
        despawn["demographic_effect"] = "EMIGRATION"
        with self.assertRaises(module.ReplayError):
            module.validate(broken)

    def test_adapter_event_cancellation_must_be_verified(self):
        broken = copy.deepcopy(self.trace)
        broken["verified_adapter_primitives"]["entity_spawn_cancelable"] = False
        with self.assertRaises(module.ReplayError):
            module.validate(broken)


if __name__ == "__main__":
    unittest.main()
