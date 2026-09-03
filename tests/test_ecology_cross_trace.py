from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "validate_ecology_cross_trace.py"
SPEC = importlib.util.spec_from_file_location("validate_ecology_cross_trace", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)
TRACE_PATH = ROOT / "implementation" / "marea-sendero-persistent-actor-cross-fixture-trace-v1.json"


class EcologyCrossTraceTest(unittest.TestCase):
    def load_trace(self) -> dict:
        return json.loads(TRACE_PATH.read_text(encoding="utf-8"))

    def test_repository_cross_trace_validates(self) -> None:
        validator.validate_trace(TRACE_PATH, self.load_trace(), ROOT)

    def test_rejects_identity_drift_at_battle_return(self) -> None:
        broken = copy.deepcopy(self.load_trace())
        window = next(item for item in broken["windows"] if item["id"] == "T6_AUTOPTU_SEMANTIC_KO_RETURN")
        window["input_events"][0]["actor_ref"] = "fixture.different.pokemon"
        with self.assertRaises(validator.ValidationError):
            validator.validate_trace(TRACE_PATH, broken, ROOT)

    def test_rejects_handoff_before_manifest_freeze(self) -> None:
        broken = copy.deepcopy(self.load_trace())
        window = next(item for item in broken["windows"] if item["id"] == "T5_MANIFEST_FREEZE_THEN_HANDOFF")
        window["input_events"] = list(reversed(window["input_events"]))
        with self.assertRaises(validator.ValidationError):
            validator.validate_trace(TRACE_PATH, broken, ROOT)

    def test_rejects_uuid_as_persistent_identity(self) -> None:
        broken = copy.deepcopy(self.load_trace())
        window = next(item for item in broken["windows"] if item["id"] == "T10_REPEAT_SIGHTING")
        window["input_events"][0]["internal_id_exposed_to_player"] = True
        with self.assertRaises(validator.ValidationError):
            validator.validate_trace(TRACE_PATH, broken, ROOT)

    def test_rejects_population_creation_without_demography(self) -> None:
        broken = copy.deepcopy(self.load_trace())
        window = next(item for item in broken["windows"] if item["id"] == "T8_SOURCE_EVENT_REEVALUATES")
        window["expected"]["population_total"] = 13
        with self.assertRaises(validator.ValidationError):
            validator.validate_trace(TRACE_PATH, broken, ROOT)

    def test_rejects_direct_battle_resolution_of_ecology_event(self) -> None:
        broken = copy.deepcopy(self.load_trace())
        window = next(item for item in broken["windows"] if item["id"] == "T8_SOURCE_EVENT_REEVALUATES")
        window["input_events"][0]["battle_result_is_direct_resolution"] = True
        with self.assertRaises(validator.ValidationError):
            validator.validate_trace(TRACE_PATH, broken, ROOT)


if __name__ == "__main__":
    unittest.main()
