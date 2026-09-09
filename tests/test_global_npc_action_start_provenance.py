import copy
import unittest

from tools.global_npc_action_start_provenance import ActionStartProvenanceLedger
from tools.global_npc_ai import AgentMode, NpcAgentState, NpcIntent
from tools.global_npc_plan_selection_provenance import PlanSelectionProvenanceLedger
from tools.global_npc_replanning import ReplanBatch
from tools.global_npc_travel import RouteEdge, TravelPlan, TravelState


class GlobalNpcActionStartProvenanceTests(unittest.TestCase):
    def _batch(self, minute=40):
        return ReplanBatch(
            agent_id="field.lead",
            semantic_minute=minute,
            trigger_ids=("trigger.route",),
            reasons=("EXTERNAL_EVENT",),
            source_refs=("route.order",),
            highest_priority=7,
        )

    def _agent(self):
        return NpcAgentState(
            agent_id="field.lead",
            mode=AgentMode.OFFSCREEN_NAMED,
            region_ref="fixture",
            location_ref="fixture.camp",
        )

    def _travel_selection(self):
        selections = PlanSelectionProvenanceLedger()
        record, _ = selections.record_selection(
            self._batch(),
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
        return selections, record

    def _autoptu_selection(self):
        selections = PlanSelectionProvenanceLedger()
        record, _ = selections.record_selection(
            self._batch(),
            self._agent(),
            situational_intents=(
                NpcIntent(
                    "encounter:blocked-pass",
                    "CLEAR_BLOCKED_PASS",
                    base_priority=8,
                    target_ref="fixture.pass",
                    requires_structured_mechanics=True,
                ),
            ),
        )
        return selections, record

    def _travel_state(self):
        plan = TravelPlan(
            plan_id="travel.survey",
            agent_id="field.lead",
            origin_node="fixture.camp",
            destination_node="fixture.ridge",
            edge_ids=("edge.camp-ridge",),
            departure_minute=40,
            expected_arrival_minute=55,
            reason_ref="plan-selection",
        )
        return TravelState(plan=plan, current_node="fixture.camp", semantic_minute=40)

    def _edges(self):
        return (
            RouteEdge(
                edge_id="edge.camp-ridge",
                from_node="fixture.camp",
                to_node="fixture.ridge",
                duration_minutes=15,
            ),
        )

    def test_records_replayable_travel_departure_after_selection(self):
        selections, selection = self._travel_selection()
        ledger = ActionStartProvenanceLedger()
        record, state_after = ledger.record_travel_start(
            selection,
            self._agent(),
            self._travel_state(),
            self._edges(),
            semantic_minute=40,
        )

        self.assertEqual(record.intent_id, "route:survey")
        self.assertEqual(record.started_minute, 40)
        self.assertEqual(state_after.edge_started_minute, 40)
        ledger.validate_against_plan_selections(selections, semantic_minute=40)

    def test_records_replayable_autoptu_binding_acceptance(self):
        selections, selection = self._autoptu_selection()
        ledger = ActionStartProvenanceLedger()
        record, agent_after = ledger.record_autoptu_binding_start(
            selection,
            self._agent(),
            binding_ref="autoptu.session.77",
            semantic_minute=41,
        )

        self.assertEqual(agent_after.mode, AgentMode.AUTOPTU_BOUND)
        self.assertEqual(agent_after.active_autoptu_binding, "autoptu.session.77")
        self.assertEqual(record.started_minute, 41)
        ledger.validate_against_plan_selections(selections, semantic_minute=41)

    def test_snapshot_round_trip_preserves_start_evidence(self):
        selections, selection = self._travel_selection()
        ledger = ActionStartProvenanceLedger()
        ledger.record_travel_start(
            selection,
            self._agent(),
            self._travel_state(),
            self._edges(),
            semantic_minute=40,
        )
        restored = ActionStartProvenanceLedger.restore(ledger.snapshot())
        self.assertEqual(restored.snapshot(), ledger.snapshot())
        restored.validate_against_plan_selections(selections, semantic_minute=40)

    def test_tampered_travel_start_state_fails_closed(self):
        _, selection = self._travel_selection()
        ledger = ActionStartProvenanceLedger()
        ledger.record_travel_start(
            selection,
            self._agent(),
            self._travel_state(),
            self._edges(),
            semantic_minute=40,
        )
        snapshot = copy.deepcopy(ledger.snapshot())
        snapshot["starts"][0]["evidence"]["travel_after"]["edge_started_minute"] = 41
        with self.assertRaisesRegex(ValueError, "no longer replays"):
            ActionStartProvenanceLedger.restore(snapshot)

    def test_missing_selection_breaks_cross_owner_provenance(self):
        _, selection = self._travel_selection()
        ledger = ActionStartProvenanceLedger()
        ledger.record_travel_start(
            selection,
            self._agent(),
            self._travel_state(),
            self._edges(),
            semantic_minute=40,
        )
        with self.assertRaisesRegex(ValueError, "missing plan selection"):
            ledger.validate_against_plan_selections(PlanSelectionProvenanceLedger(), semantic_minute=40)

    def test_future_action_start_is_rejected(self):
        selections, selection = self._autoptu_selection()
        ledger = ActionStartProvenanceLedger()
        ledger.record_autoptu_binding_start(
            selection,
            self._agent(),
            binding_ref="autoptu.session.77",
            semantic_minute=41,
        )
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            ledger.validate_against_plan_selections(selections, semantic_minute=40)

    def test_waiting_travel_state_does_not_count_as_action_started(self):
        _, selection = self._travel_selection()
        waiting = self._travel_state()
        waiting = TravelState(
            plan=TravelPlan(
                plan_id=waiting.plan.plan_id,
                agent_id=waiting.plan.agent_id,
                origin_node=waiting.plan.origin_node,
                destination_node=waiting.plan.destination_node,
                edge_ids=waiting.plan.edge_ids,
                departure_minute=50,
                expected_arrival_minute=65,
                reason_ref=waiting.plan.reason_ref,
            ),
            current_node=waiting.current_node,
            semantic_minute=40,
        )
        with self.assertRaisesRegex(ValueError, "does not prove a departure"):
            ActionStartProvenanceLedger().record_travel_start(
                selection,
                self._agent(),
                waiting,
                self._edges(),
                semantic_minute=40,
            )

    def test_autoptu_binding_requires_selected_handoff(self):
        _, selection = self._travel_selection()
        with self.assertRaisesRegex(ValueError, "did not request AutoPTU"):
            ActionStartProvenanceLedger().record_autoptu_binding_start(
                selection,
                self._agent(),
                binding_ref="autoptu.session.77",
                semantic_minute=41,
            )


if __name__ == "__main__":
    unittest.main()
