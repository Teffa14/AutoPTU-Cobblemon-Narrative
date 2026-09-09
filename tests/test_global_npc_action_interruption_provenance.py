import copy
import unittest

from tools.global_npc_action_interruption_provenance import ActionInterruptionProvenanceLedger
from tools.global_npc_action_start_provenance import ActionStartProvenanceLedger
from tools.global_npc_ai import AgentMode, NpcAgentState, NpcIntent
from tools.global_npc_plan_selection_provenance import PlanSelectionProvenanceLedger
from tools.global_npc_replanning import ReplanBatch
from tools.global_npc_travel import RouteEdge, TravelPlan, TravelState


class GlobalNpcActionInterruptionProvenanceTests(unittest.TestCase):
    def _agent(self):
        return NpcAgentState(
            agent_id="field.lead",
            mode=AgentMode.OFFSCREEN_NAMED,
            region_ref="fixture",
            location_ref="fixture.camp",
        )

    def _started(self):
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
            situational_intents=(NpcIntent("route:survey", "TRAVEL_TO_SURVEY", 8, target_ref="fixture.ridge"),),
        )
        state = TravelState(
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
        original_edges = (RouteEdge("edge.camp-ridge", "fixture.camp", "fixture.ridge", 15),)
        starts = ActionStartProvenanceLedger()
        start, _ = starts.record_travel_start(
            selection,
            self._agent(),
            state,
            original_edges,
            semantic_minute=40,
        )
        return starts, start

    def _blocked_edges(self):
        return (RouteEdge("edge.camp-ridge", "fixture.camp", "fixture.ridge", 15, enabled=False),)

    def test_records_replayable_replan_required_interruption(self):
        starts, start = self._started()
        ledger = ActionInterruptionProvenanceLedger()
        record = ledger.record_travel_replan_required(start, self._blocked_edges(), semantic_minute=44)
        self.assertEqual(record.evidence["decision_kind"], "REPLAN_REQUIRED")
        self.assertEqual(record.evidence["decision_edge_id"], "edge.camp-ridge")
        ledger.validate_against_action_starts(starts, semantic_minute=44)

    def test_snapshot_round_trip_preserves_interruption(self):
        starts, start = self._started()
        ledger = ActionInterruptionProvenanceLedger()
        ledger.record_travel_replan_required(start, self._blocked_edges(), semantic_minute=44)
        restored = ActionInterruptionProvenanceLedger.restore(ledger.snapshot())
        self.assertEqual(restored.snapshot(), ledger.snapshot())
        restored.validate_against_action_starts(starts, semantic_minute=44)

    def test_ordinary_in_progress_travel_is_not_an_interruption(self):
        _, start = self._started()
        ordinary_edges = (RouteEdge("edge.camp-ridge", "fixture.camp", "fixture.ridge", 15),)
        with self.assertRaisesRegex(ValueError, "does not prove a replan-required interruption"):
            ActionInterruptionProvenanceLedger().record_travel_replan_required(start, ordinary_edges, semantic_minute=44)

    def test_missing_action_start_breaks_cross_owner_provenance(self):
        _, start = self._started()
        ledger = ActionInterruptionProvenanceLedger()
        ledger.record_travel_replan_required(start, self._blocked_edges(), semantic_minute=44)
        with self.assertRaisesRegex(ValueError, "missing action start"):
            ledger.validate_against_action_starts(ActionStartProvenanceLedger(), semantic_minute=44)

    def test_future_interruption_is_rejected(self):
        starts, start = self._started()
        ledger = ActionInterruptionProvenanceLedger()
        ledger.record_travel_replan_required(start, self._blocked_edges(), semantic_minute=44)
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            ledger.validate_against_action_starts(starts, semantic_minute=43)

    def test_tampered_route_condition_no_longer_replays(self):
        _, start = self._started()
        ledger = ActionInterruptionProvenanceLedger()
        ledger.record_travel_replan_required(start, self._blocked_edges(), semantic_minute=44)
        snapshot = copy.deepcopy(ledger.snapshot())
        snapshot["interruptions"][0]["evidence"]["edges_at_interruption"][0]["enabled"] = True
        with self.assertRaisesRegex(ValueError, "no longer replays"):
            ActionInterruptionProvenanceLedger.restore(snapshot)

    def test_tampered_source_snapshot_breaks_cross_owner_provenance(self):
        starts, start = self._started()
        ledger = ActionInterruptionProvenanceLedger()
        ledger.record_travel_replan_required(start, self._blocked_edges(), semantic_minute=44)
        snapshot = copy.deepcopy(ledger.snapshot())
        snapshot["interruptions"][0]["evidence"]["agent"]["energy"] = 9
        restored = ActionInterruptionProvenanceLedger.restore(snapshot)
        with self.assertRaisesRegex(ValueError, "diverges from source start"):
            restored.validate_against_action_starts(starts, semantic_minute=44)


if __name__ == "__main__":
    unittest.main()
