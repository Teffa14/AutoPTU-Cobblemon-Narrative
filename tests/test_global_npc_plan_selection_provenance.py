import copy
import unittest

from tools.global_npc_ai import (
    AgentMode,
    DurableGoal,
    NeedState,
    NpcAgentState,
    NpcIntent,
    ScheduledCommitment,
)
from tools.global_npc_delivery_replan_provenance import (
    ConsumedReplanRecord,
    DeliveryReplanProvenanceLedger,
)
from tools.global_npc_plan_selection_provenance import PlanSelectionProvenanceLedger
from tools.global_npc_replanning import ReplanBatch


class GlobalNpcPlanSelectionProvenanceTests(unittest.TestCase):
    def _batch(self):
        return ReplanBatch(
            agent_id="field.lead",
            semantic_minute=40,
            trigger_ids=("trigger.message", "trigger.rescue"),
            reasons=("KNOWLEDGE_DELIVERED", "EXTERNAL_EVENT"),
            source_refs=("delivery.reroute", "incident.bridge"),
            highest_priority=9,
        )

    def _agent(self):
        return NpcAgentState(
            agent_id="field.lead",
            mode=AgentMode.OFFSCREEN_NAMED,
            region_ref="fixture",
            location_ref="fixture.camp",
            knowledge=frozenset({"claim.reroute"}),
            memory_refs=("claim.reroute.root",),
        )

    def _inputs(self):
        return {
            "goals": (
                DurableGoal("survey", "CONTINUE_SURVEY", priority=4, progress=0, target_progress=100),
            ),
            "needs": (
                NeedState("fatigue", "REST", pressure=95, activation_threshold=50),
            ),
            "commitments": (
                ScheduledCommitment(
                    "rescue-window",
                    "ASSIST_STRANDED_TEAM",
                    start_minute=35,
                    end_minute=55,
                    priority=3,
                    hard=True,
                    target_ref="incident.bridge",
                ),
            ),
            "situational_intents": (
                NpcIntent(
                    "reroute:delivery.reroute",
                    "FOLLOW_REROUTE",
                    base_priority=4,
                    urgency=5,
                    obligation=6,
                    target_ref="route.beta",
                ),
            ),
        }

    def _provenance(self):
        ledger = DeliveryReplanProvenanceLedger()
        ledger.consumptions["trigger.message"] = ConsumedReplanRecord(
            consumption_id="consumed-replan:trigger.message",
            trigger_id="trigger.message",
            agent_id="field.lead",
            reason="KNOWLEDGE_DELIVERED",
            source_ref="delivery.reroute",
            due_minute=40,
            priority=5,
            processed_minute=40,
            batch_key="replan-batch:field.lead:40",
        )
        ledger.consumptions["trigger.rescue"] = ConsumedReplanRecord(
            consumption_id="consumed-replan:trigger.rescue",
            trigger_id="trigger.rescue",
            agent_id="field.lead",
            reason="EXTERNAL_EVENT",
            source_ref="incident.bridge",
            due_minute=40,
            priority=9,
            processed_minute=40,
            batch_key="replan-batch:field.lead:40",
        )
        return ledger

    def test_records_inputs_and_replays_selected_agenda_decision(self):
        ledger = PlanSelectionProvenanceLedger()
        record, decision = ledger.record_selection(self._batch(), self._agent(), **self._inputs())

        self.assertEqual(decision.decision.intent_id, "commitment:rescue-window")
        self.assertEqual(decision.source_type, "COMMITMENT")
        self.assertEqual(decision.source_ref, "rescue-window")
        self.assertEqual(record.selected["intent_id"], "commitment:rescue-window")
        self.assertEqual(len(record.goals), 1)
        self.assertEqual(len(record.needs), 1)
        self.assertEqual(len(record.commitments), 1)
        self.assertEqual(len(record.situational_intents), 1)
        ledger.validate_against_replan_provenance(self._provenance(), semantic_minute=40)

    def test_snapshot_round_trip_preserves_replayable_decision_context(self):
        ledger = PlanSelectionProvenanceLedger()
        ledger.record_selection(self._batch(), self._agent(), **self._inputs())
        restored = PlanSelectionProvenanceLedger.restore(ledger.snapshot())
        self.assertEqual(restored.snapshot(), ledger.snapshot())
        restored.validate_against_replan_provenance(self._provenance(), semantic_minute=40)

    def test_selected_decision_tampering_fails_replay_validation(self):
        ledger = PlanSelectionProvenanceLedger()
        ledger.record_selection(self._batch(), self._agent(), **self._inputs())
        snapshot = copy.deepcopy(ledger.snapshot())
        snapshot["selections"][0]["selected"]["intent_id"] = "reroute:delivery.reroute"
        with self.assertRaisesRegex(ValueError, "no longer replays"):
            PlanSelectionProvenanceLedger.restore(snapshot)

    def test_candidate_context_tampering_fails_when_it_changes_the_winner(self):
        ledger = PlanSelectionProvenanceLedger()
        ledger.record_selection(self._batch(), self._agent(), **self._inputs())
        snapshot = copy.deepcopy(ledger.snapshot())
        snapshot["selections"][0]["commitments"][0]["priority"] = 0
        snapshot["selections"][0]["commitments"][0]["hard"] = False
        with self.assertRaisesRegex(ValueError, "no longer replays"):
            PlanSelectionProvenanceLedger.restore(snapshot)

    def test_unconsumed_trigger_breaks_plan_selection_provenance(self):
        ledger = PlanSelectionProvenanceLedger()
        ledger.record_selection(self._batch(), self._agent(), **self._inputs())
        provenance = self._provenance()
        del provenance.consumptions["trigger.rescue"]
        with self.assertRaisesRegex(ValueError, "unconsumed trigger"):
            ledger.validate_against_replan_provenance(provenance, semantic_minute=40)

    def test_trigger_batch_mismatch_breaks_plan_selection_provenance(self):
        ledger = PlanSelectionProvenanceLedger()
        ledger.record_selection(self._batch(), self._agent(), **self._inputs())
        provenance = self._provenance()
        original = provenance.consumptions["trigger.rescue"]
        provenance.consumptions["trigger.rescue"] = ConsumedReplanRecord(
            consumption_id=original.consumption_id,
            trigger_id=original.trigger_id,
            agent_id=original.agent_id,
            reason=original.reason,
            source_ref=original.source_ref,
            due_minute=original.due_minute,
            priority=original.priority,
            processed_minute=original.processed_minute,
            batch_key="replan-batch:field.lead:41",
        )
        with self.assertRaisesRegex(ValueError, "batch provenance mismatch"):
            ledger.validate_against_replan_provenance(provenance, semantic_minute=40)

    def test_future_selection_is_rejected_against_world_time(self):
        ledger = PlanSelectionProvenanceLedger()
        ledger.record_selection(self._batch(), self._agent(), **self._inputs())
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            ledger.validate_against_replan_provenance(self._provenance(), semantic_minute=39)

    def test_duplicate_selection_is_rejected(self):
        ledger = PlanSelectionProvenanceLedger()
        ledger.record_selection(self._batch(), self._agent(), **self._inputs())
        with self.assertRaisesRegex(ValueError, "already recorded"):
            ledger.record_selection(self._batch(), self._agent(), **self._inputs())


if __name__ == "__main__":
    unittest.main()
