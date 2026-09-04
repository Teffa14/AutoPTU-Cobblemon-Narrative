import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "implementation" / "marea-sendero-semantic-horizon-clock-trace-v1.json"


def load_fixture():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def events_of_type(data, event_type):
    return [event for event in data["events"] if event["type"] == event_type]


class SemanticHorizonClockTests(unittest.TestCase):
    def test_population_and_battle_authority_are_unchanged(self):
        data = load_fixture()
        self.assertEqual(data["population"]["total"], 12)
        self.assertEqual(data["expected_final"]["population_total"], 12)
        self.assertEqual(data["expected_final"]["net_population_delta"], 0)
        self.assertEqual(data["expected_final"]["demographic_events"], 0)
        self.assertEqual(data["expected_final"]["autoptu_handoffs"], 0)
        self.assertTrue(all(event.get("population_delta", 0) == 0 for event in data["events"]))

    def test_time_of_day_is_not_the_monotonic_clock(self):
        data = load_fixture()
        self.assertFalse(data["clock"]["time_of_day_is_monotonic_basis"])
        event = events_of_type(data, "MINECRAFT_TIME_OF_DAY_CHANGED")[0]
        self.assertNotEqual(event["time_of_day_before"], event["time_of_day_after"])
        self.assertEqual(event["monotonic_value_before"], event["monotonic_value_after"])
        self.assertFalse(event["retained_state_expired"])
        self.assertEqual(data["expected_final"]["time_of_day_false_expiries"], 0)

    def test_duration_horizon_closes_only_at_declared_policy_boundary(self):
        data = load_fixture()
        site = next(
            event for event in events_of_type(data, "SEMANTIC_HORIZON_EVALUATED")
            if event["retained_state_id"] == "retained.261.site"
        )
        self.assertEqual(site["horizon_type"], "DURATION_SINCE_AUTHORITY_EVENT")
        self.assertTrue(site["horizon_reached"])
        self.assertEqual(site["result"], "DROP_PRIVATE_KEEP_PUBLIC_HISTORY")
        self.assertTrue(site["public_observation_history_preserved"])

    def test_restart_does_not_expire_active_condition_horizon(self):
        data = load_fixture()
        restart = events_of_type(data, "SERVER_RESTART")[0]
        disturbance = next(
            event for event in events_of_type(data, "SEMANTIC_HORIZON_EVALUATED")
            if event["retained_state_id"] == "retained.261.disturbance"
        )
        self.assertTrue(restart["disturbance_state_restored"])
        self.assertFalse(restart["restart_implied_expiry"])
        self.assertEqual(restart["clock_epoch_after_restart"], 4)
        self.assertLess(disturbance["stable_ticks_elapsed"], disturbance["required_fixture_stable_ticks"])
        self.assertFalse(disturbance["horizon_reached"])
        self.assertEqual(disturbance["result"], "RETAIN_ACTIVE")

    def test_validity_record_can_close_without_elapsed_duration(self):
        data = load_fixture()
        validity = events_of_type(data, "MARKER_VALIDITY_RECORD_CHANGED")[0]
        marker = next(
            event for event in events_of_type(data, "SEMANTIC_HORIZON_EVALUATED")
            if event["retained_state_id"] == "retained.261.marker"
        )
        self.assertFalse(validity["elapsed_ticks_required"])
        self.assertEqual(validity["marker_status_after"], "REPORTED_LOST")
        self.assertEqual(marker["horizon_type"], "VALIDITY_RECORD_BOUND")
        self.assertTrue(marker["horizon_reached"])
        self.assertEqual(marker["result"], "DOWNGRADE_MARKER_LINK")

    def test_clock_rollback_fails_closed_and_requires_epoch_reconciliation(self):
        data = load_fixture()
        rollback = events_of_type(data, "CLOCK_ROLLBACK_DETECTED")[0]
        reconcile = events_of_type(data, "CLOCK_EPOCH_RECONCILED")[0]
        self.assertLess(rollback["observed_raw_world_tick"], rollback["previous_committed_raw_world_tick"])
        self.assertTrue(rollback["rollback_detected"])
        self.assertTrue(rollback["automatic_horizon_expiry_suspended"])
        self.assertEqual(rollback["states_expired_due_to_rollback"], 0)
        self.assertEqual(reconcile["previous_epoch"], 4)
        self.assertEqual(reconcile["new_epoch"], 5)
        self.assertFalse(reconcile["history_rewritten"])
        self.assertEqual(data["expected_final"]["rollback_false_expiries"], 0)

    def test_fixture_durations_are_explicitly_noncanon(self):
        data = load_fixture()
        self.assertFalse(data["scenario_is_canon"])
        self.assertTrue(all(policy["canon_duration"] is False for policy in data["registry"]))
        self.assertEqual(data["clock"]["source_adapter"], "FIXTURE_ONLY_SYNTHETIC_CLOCK")

    def test_public_payload_does_not_expose_internal_clock_or_retention_state(self):
        data = load_fixture()
        public = events_of_type(data, "PUBLIC_KNOWLEDGE_CHECK")[0]
        self.assertFalse(public["clock_epoch_exposed"])
        self.assertFalse(public["registry_policy_exposed"])
        self.assertFalse(public["internal_retained_state_exposed"])
        self.assertFalse(public["public_identity_promoted"])
        self.assertEqual(data["expected_final"]["internal_clock_leaks"], 0)

    def test_reduced_fixture_keeps_tactical_categories_unpromoted(self):
        data = load_fixture()
        deps = data["battle_dependency_categories"]
        self.assertEqual(deps["complete_movement"], "PARTIAL")
        self.assertEqual(deps["full_stateful_damage_pipeline"], "PARTIAL")
        self.assertEqual(deps["ai_tactical_policy"], "BLOCKING")
        self.assertEqual(deps["minecraft_cobblemon_craftics_adapter_playback"], "PARTIAL_BLOCKING")


if __name__ == "__main__":
    unittest.main()
