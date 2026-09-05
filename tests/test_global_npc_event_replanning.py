import inspect
import unittest

from tools.global_npc_ai import (
    AgentMode,
    DurableGoal,
    NpcAgentState,
    NpcIntent,
)
from tools.global_npc_replanning import (
    NpcReplanQueue,
    ReplanReason,
    ReplanTrigger,
    apply_information_delivery,
    replan_from_batch,
    schedule_information_replan,
)


class GlobalNpcEventReplanningTests(unittest.TestCase):
    def test_due_only_processing_wakes_only_affected_agent(self):
        queue = NpcReplanQueue()
        queue.schedule(ReplanTrigger("t.a", "agent.a", ReplanReason.EXTERNAL_EVENT, 10, "event.a", 3))
        queue.schedule(ReplanTrigger("t.b", "agent.b", ReplanReason.EXTERNAL_EVENT, 20, "event.b", 3))
        self.assertEqual([], queue.process_due(9))
        batches = queue.process_due(10)
        self.assertEqual(["agent.a"], [batch.agent_id for batch in batches])
        self.assertEqual([], queue.process_due(19))
        self.assertEqual(["agent.b"], [batch.agent_id for batch in queue.process_due(20)])

    def test_same_agent_same_wakeup_window_is_coalesced(self):
        queue = NpcReplanQueue()
        queue.schedule(ReplanTrigger("t.knowledge", "agent.a", ReplanReason.KNOWLEDGE_DELIVERED, 10, "message.1", 6))
        queue.schedule(ReplanTrigger("t.social", "agent.a", ReplanReason.SOCIAL_CHANGE, 10, "relationship.1", 2))
        batches = queue.process_due(10)
        self.assertEqual(1, len(batches))
        self.assertEqual(("t.knowledge", "t.social"), batches[0].trigger_ids)
        self.assertEqual(6, batches[0].highest_priority)

    def test_restart_preserves_pending_trigger_and_no_duplicate_completion(self):
        queue = NpcReplanQueue()
        queue.schedule(ReplanTrigger("t.future", "agent.a", ReplanReason.SCHEDULE_DUE, 50, "commitment.1", 4))
        restored = NpcReplanQueue.from_snapshot(queue.to_snapshot())
        self.assertEqual([], restored.process_due(49))
        self.assertEqual(1, len(restored.process_due(50)))
        snapshot_after = restored.to_snapshot()
        restored_again = NpcReplanQueue.from_snapshot(snapshot_after)
        self.assertEqual([], restored_again.process_due(100))

    def test_information_delivery_wakes_receiver_only(self):
        queue = NpcReplanQueue()
        delivery = {
            "event_id": "message.event.1",
            "receiver_id": "agent.b",
            "status": "DELIVERED",
            "claim_id": "claim.route.closed",
            "provenance_root": "observation.route.closed",
        }
        schedule_information_replan(queue, delivery=delivery, semantic_minute=15)
        batches = queue.process_due(15)
        self.assertEqual(["agent.b"], [batch.agent_id for batch in batches])

    def test_failed_delivery_does_not_wake_agent(self):
        queue = NpcReplanQueue()
        delivery = {
            "event_id": "message.event.failed",
            "receiver_id": "agent.b",
            "status": "FAILED_CHANNEL_UNAVAILABLE",
        }
        self.assertIsNone(schedule_information_replan(queue, delivery=delivery, semantic_minute=15))
        self.assertEqual([], queue.process_due(15))

    def test_delivered_claim_can_change_replanned_agenda_without_global_poll(self):
        agent = NpcAgentState(
            agent_id="agent.b",
            mode=AgentMode.OFFSCREEN_NAMED,
            region_ref="fixture.region.beta",
            location_ref="fixture.stop.old",
        )
        goal = DurableGoal("deliver", "CONTINUE_DELIVERY", priority=4, target_ref="fixture.stop.destination")
        detour = NpcIntent(
            intent_id="situational:detour",
            kind="REPLAN_ROUTE",
            base_priority=9,
            urgency=9,
            required_knowledge=frozenset({"claim.route.closed"}),
            target_ref="fixture.stop.detour",
        )
        queue = NpcReplanQueue()
        queue.schedule(ReplanTrigger("t.before", "agent.b", ReplanReason.EXTERNAL_EVENT, 1, "initial", 1))
        before = replan_from_batch(agent, queue.process_due(1)[0], goals=(goal,), situational_intents=(detour,))
        self.assertEqual("CONTINUE_DELIVERY", before.decision.kind)

        delivery = {
            "event_id": "message.route.closed",
            "receiver_id": "agent.b",
            "status": "DELIVERED",
            "claim_id": "claim.route.closed",
            "provenance_root": "observation.route.closed",
        }
        agent = apply_information_delivery(agent, delivery)
        schedule_information_replan(queue, delivery=delivery, semantic_minute=10, priority=8)
        after = replan_from_batch(agent, queue.process_due(10)[0], goals=(goal,), situational_intents=(detour,))
        self.assertEqual("REPLAN_ROUTE", after.decision.kind)
        self.assertEqual("fixture.stop.detour", after.decision.target_ref)

    def test_duplicate_trigger_id_is_rejected(self):
        queue = NpcReplanQueue()
        trigger = ReplanTrigger("t.same", "agent.a", ReplanReason.EXTERNAL_EVENT, 1, "event", 1)
        queue.schedule(trigger)
        with self.assertRaises(ValueError):
            queue.schedule(trigger)

    def test_core_is_region_neutral_and_does_not_resolve_tactics(self):
        import tools.global_npc_replanning as module

        source = inspect.getsource(module)
        for forbidden in ("Marea", "Sendero", "Puerto Bruma", "Loma Clara"):
            self.assertNotIn(forbidden, source)
        for tactical in ("damageDealt", "initiativeOrder", "knockbackDistance", "moveAccuracy"):
            self.assertNotIn(tactical, source)


if __name__ == "__main__":
    unittest.main()
