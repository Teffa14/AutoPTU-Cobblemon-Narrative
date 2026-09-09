import copy
import unittest

from tools.global_npc_action_start_provenance import ActionStartProvenanceLedger
from tools.global_npc_action_terminal_provenance import ActionTerminalProvenanceLedger
from tools.global_npc_ai import AgentMode, NpcAgentState, NpcIntent
from tools.global_npc_plan_selection_provenance import PlanSelectionProvenanceLedger
from tools.global_npc_replanning import ReplanBatch
from tools.global_npc_travel import RouteEdge, TravelPlan, TravelState


class GlobalNpcActionTerminalProvenanceTests(unittest.TestCase):
    def _agent(self):
        return NpcAgentState(
            agent_id="field.lead",
            mode=AgentMode.OFFSCREEN_NAMED,
            region_ref="fixture",
            location_ref="fixture.camp",
        )

    def _selection(self):
        selections = PlanSelectionProvenanceLedger()
        batch = ReplanBatch(
            agent_id="field.lead",
            semantic_minute=40,
            trigger_ids=("trigger.route",),
            reasons=("EXTERNAL_EVENT",),
            source_refs=("route.order",),
            highest_priority=7,
        )
        selection, _ = selections.record_selection(
            batch,
            self._agent(),
            situational_intents=(
                NpcIntent(
                    "route:survey",
                    "TRAVEL_TO_SURVEY",
                    base_priority=8,
                    target_ref="fixture.ridge",
                ),
            ),
        )
        return selections, selection

    def _edges(self):
        return (
            RouteEdge(
                edge_id="edge.camp-ridge",
                from_node="fixture.camp",
                to_node="fixture.ridge",
                duration_minutes=15,
            ),
        )

    def _travel_state(self):
        return TravelState(
            plan=TravelPlan(
                plan_id="travel.survey",
                agent_id="field.lead",
                origin_node="fixture.camp",
                destination_node="fixture.ridge",
                edge_ids=("edge.camp-ridge",),
                departure_minute=40,
                expected_arrival_minute=55,
                reason_ref="plan-selection",
            ),
            current_node="fixture.camp",
            semantic_minute=40,
        )

    def _started(self):
        selections, selection = self._selection()
        starts = ActionStartProvenanceLedger()
        start, _ = starts.record_travel_start(
            selection,
            self._agent(),
            self._travel_state(),
            self._edges(),
            semantic_minute=40,
        )
        return selections, starts, start

    def test_records_replayable_destination_arrival(self):
        _, starts, start = self._started()
        ledger = ActionTerminalProvenanceLedger()
        record = ledger.record_travel_arrival(start, semantic_minute=55)

        self.assertEqual(record.terminal_minute, 55)
        self.assertEqual(record.target_ref, "fixture.ridge")
        self.assertEqual(record.evidence["decision_kind"], "ARRIVED")
        ledger.validate_against_action_starts(starts, semantic_minute=55)

    def test_snapshot_round_trip_preserves_arrival_evidence(self):
        _, starts, start = self._started()
        ledger = ActionTerminalProvenanceLedger()
        ledger.record_travel_arrival(start, semantic_minute=55)
        restored = ActionTerminalProvenanceLedger.restore(ledger.snapshot())
        self.assertEqual(restored.snapshot(), ledger.snapshot())
        restored.validate_against_action_starts(starts, semantic_minute=55)

    def test_in_progress_travel_does_not_count_as_terminal(self):
        _, _, start = self._started()
        with self.assertRaisesRegex(ValueError, "does not prove destination arrival"):
            ActionTerminalProvenanceLedger().record_travel_arrival(start, semantic_minute=54)

    def test_missing_action_start_breaks_cross_owner_provenance(self):
        _, _, start = self._started()
        ledger = ActionTerminalProvenanceLedger()
        ledger.record_travel_arrival(start, semantic_minute=55)
        with self.assertRaisesRegex(ValueError, "missing action start"):
            ledger.validate_against_action_starts(ActionStartProvenanceLedger(), semantic_minute=55)

    def test_future_terminal_is_rejected(self):
        _, starts, start = self._started()
        ledger = ActionTerminalProvenanceLedger()
        ledger.record_travel_arrival(start, semantic_minute=55)
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            ledger.validate_against_action_starts(starts, semantic_minute=54)

    def test_tampered_terminal_state_fails_closed(self):
        _, _, start = self._started()
        ledger = ActionTerminalProvenanceLedger()
        ledger.record_travel_arrival(start, semantic_minute=55)
        snapshot = copy.deepcopy(ledger.snapshot())
        snapshot["terminals"][0]["evidence"]["travel_terminal"]["current_node"] = "fixture.wrong"
        with self.assertRaisesRegex(ValueError, "no longer replays"):
            ActionTerminalProvenanceLedger.restore(snapshot)

    def test_tampered_source_snapshot_breaks_cross_owner_provenance(self):
        _, starts, start = self._started()
        ledger = ActionTerminalProvenanceLedger()
        ledger.record_travel_arrival(start, semantic_minute=55)
        snapshot = copy.deepcopy(ledger.snapshot())
        snapshot["terminals"][0]["evidence"]["agent"]["energy"] = 9
        restored = ActionTerminalProvenanceLedger.restore(snapshot)
        with self.assertRaisesRegex(ValueError, "diverges from source start"):
            restored.validate_against_action_starts(starts, semantic_minute=55)


if __name__ == "__main__":
    unittest.main()
