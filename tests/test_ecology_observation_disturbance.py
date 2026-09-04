import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE_PATH = ROOT / "implementation" / "marea-sendero-observation-disturbance-trace-v1.json"


class EcologyObservationDisturbanceTest(unittest.TestCase):
    def setUp(self):
        self.trace = json.loads(TRACE_PATH.read_text(encoding="utf-8"))
        self.events = self.trace["events"]

    def test_fixture_is_noncanon_and_preserves_population(self):
        self.assertFalse(self.trace["scenario_is_canon"])
        self.assertFalse(self.trace["fixture_policy"]["thresholds_are_canon"])
        self.assertEqual(12, self.trace["population"]["total"])
        self.assertEqual(12, self.trace["expected_final"]["population_total"])
        self.assertEqual(0, self.trace["expected_final"]["demographic_events"])

    def test_evidence_quality_and_disturbance_are_independent(self):
        observations = {event["observation_id"]: event for event in self.events if event["type"] == "FIELD_OBSERVATION_CAPTURED"}
        impacts = {event["observation_id"]: event for event in self.events if event["type"] == "OBSERVATION_IMPACT_APPLIED"}
        self.assertEqual("MEDIUM", observations["obs.255.passive.001"]["evidence_quality"])
        self.assertEqual(0.00, impacts["obs.255.passive.001"]["disturbance_pressure_delta"])
        self.assertEqual("LOW", observations["obs.255.close.002"]["evidence_quality"])
        self.assertEqual(0.20, impacts["obs.255.close.002"]["disturbance_pressure_delta"])

    def test_impact_transactions_are_unique_and_relays_do_not_repeat_them(self):
        impacts = [event for event in self.events if event["type"] == "OBSERVATION_IMPACT_APPLIED"]
        transaction_ids = [event["impact_transaction_id"] for event in impacts]
        self.assertEqual(len(transaction_ids), len(set(transaction_ids)))
        relays = [event for event in self.events if event["type"] == "OBSERVATION_RELAYED"]
        self.assertEqual(1, len(relays))
        self.assertFalse(relays[0]["new_impact_transaction_created"])
        self.assertEqual(0.00, relays[0]["disturbance_pressure_delta"])

    def test_accumulated_pressure_changes_projection_not_abundance(self):
        projection_events = [event for event in self.events if event["type"] == "PROJECTION_POLICY_EVALUATED"]
        self.assertEqual("REDUCED", projection_events[0]["visibility_band"])
        self.assertEqual(0.50, projection_events[0]["disturbance_pressure"])
        self.assertEqual("NORMAL", projection_events[-1]["visibility_band"])
        self.assertEqual(0.10, projection_events[-1]["disturbance_pressure"])
        self.assertTrue(all(event.get("population_delta", 0) == 0 for event in projection_events))

    def test_unauthorized_physical_handling_fails_closed(self):
        handling = [event for event in self.events if event["type"] == "PHYSICAL_HANDLING_REQUESTED"]
        self.assertEqual(1, len(handling))
        event = handling[0]
        self.assertFalse(event["canon_authority_present"])
        self.assertEqual("DENIED_FAIL_CLOSED", event["result"])
        self.assertFalse(event["marker_applied"])
        self.assertEqual(0, event["population_delta"])
        self.assertFalse(event["autoptu_handoff"])

    def test_recovery_is_explicit_and_history_survives_restart(self):
        recovery = [event for event in self.events if event["type"] == "ECOLOGY_DISTURBANCE_RECOVERY_APPLIED"]
        self.assertEqual(1, len(recovery))
        self.assertTrue(recovery[0]["quiet_condition_verified"])
        restart = [event for event in self.events if event["type"] == "SERVER_RESTART"][0]
        self.assertEqual(12, restart["population_total_after_restart"])
        self.assertEqual(0.10, restart["disturbance_pressure_after_restart"])
        self.assertTrue(restart["observation_history_preserved"])

    def test_no_observation_opens_autoptu_or_demographic_event(self):
        forbidden = {
            "LOCAL_RECRUITMENT", "IMMIGRATION", "EMIGRATION", "ECOLOGICAL_MORTALITY",
            "CAPTURE_REMOVAL", "RELOCATION_IN", "RELOCATION_OUT"
        }
        self.assertTrue(forbidden.isdisjoint({event["type"] for event in self.events}))
        self.assertTrue(all(not event.get("autoptu_handoff", False) for event in self.events))


if __name__ == "__main__":
    unittest.main()
