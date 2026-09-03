from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "validate_ecology_fixtures.py"
SPEC = importlib.util.spec_from_file_location("validate_ecology_fixtures", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class EcologyFixtureValidatorTest(unittest.TestCase):
    def test_all_repository_fixtures_validate(self) -> None:
        paths = sorted((ROOT / "implementation").glob("*fixture-v1.json"))
        self.assertTrue(paths, "expected at least one implementation fixture")
        for path in paths:
            with self.subTest(path=path.name):
                validator.validate_file(path)

    def test_demography_validator_rejects_population_creation_from_spawn(self) -> None:
        path = ROOT / "implementation" / "marea-sendero-population-demography-fixture-v1.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        broken = copy.deepcopy(data)
        window = next(item for item in broken["windows"] if item["id"] == "G_GENERIC_PRESENTATION_NO_WRITE")
        window["expected"]["target_total_count"] += 5
        with self.assertRaises(validator.ValidationError):
            validator.validate_demography(path, broken)

    def test_spawn_validator_rejects_duplicate_persistent_lease(self) -> None:
        path = ROOT / "implementation" / "marea-sendero-spawn-reconciliation-fixture-v1.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        broken = copy.deepcopy(data)
        capture_window = next(item for item in broken["windows"] if item["id"] == "K_CAPTURE_REQUIRES_SEMANTIC_CONFIRMATION")
        capture_window["input_events"] = [
            event for event in capture_window["input_events"]
            if not (event.get("event_type") == "LEASE_RELEASE" and event.get("lease_id") == "lease.pool.002")
        ]
        with self.assertRaises(validator.ValidationError):
            validator.validate_spawn_reconciliation(path, broken)

    def test_handoff_validator_keeps_unopposed_flee_overworld(self) -> None:
        path = ROOT / "implementation" / "marea-sendero-autoptu-handoff-fixture-v1.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        broken = copy.deepcopy(data)
        flee = next(item for item in broken["windows"] if item["id"] == "W2_UNOPPOSED_FLEE")
        flee["expect"]["decision"] = "OPEN_AUTOPTU"
        with self.assertRaises(validator.ValidationError):
            validator.validate_handoff(path, broken)


if __name__ == "__main__":
    unittest.main()
