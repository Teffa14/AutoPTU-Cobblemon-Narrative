import unittest
from pathlib import Path

from tools.global_npc_audience import AudienceCandidate, AudiencePolicy
from tools.global_npc_communication_runtime import dispatch_to_audience, replay_fixture
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, evaluate_belief, record_direct_observation
from tools.global_npc_social import FactionMembership, RelationshipState


class GlobalNpcCommunicationRuntimeTests(unittest.TestCase):
    def _queue(self):
        ledgers = {agent: KnowledgeLedger(agent) for agent in ("a", "b", "c")}
        channels = {
            "slow": CommunicationChannel("slow", "MESSAGE", 5),
            "fast": CommunicationChannel("fast", "MESSAGE", 1),
        }
        return InformationEventQueue(channels=channels, ledgers=ledgers)

    def test_dispatch_schedules_only_selected_recipients(self):
        queue = self._queue()
        record_direct_observation(queue.ledgers["a"], claim_id="root", subject="route", value="closed", semantic_minute=10, confidence=90)
        result = dispatch_to_audience(
            dispatch_id="d",
            sender_id="a",
            source_claim_id="root",
            semantic_minute=10,
            queue=queue,
            candidates=(
                AudienceCandidate("b", ("slow", "fast"), topic_relevance=5),
                AudienceCandidate("c", ("fast",), topic_relevance=1),
            ),
            relationships=(RelationshipState("a", "b", trust=60),),
            policy=AudiencePolicy(max_recipients=1),
        )
        self.assertEqual(result.selection.selected_agent_ids, ("b",))
        self.assertEqual([row["receiver_id"] for row in result.scheduled], ["b"])
        self.assertEqual(result.scheduled[0]["channel_id"], "fast")
        self.assertEqual(len(queue.pending), 1)

    def test_shared_faction_does_not_create_envelope(self):
        queue = self._queue()
        record_direct_observation(queue.ledgers["a"], claim_id="root", subject="route", value="closed", semantic_minute=10, confidence=90)
        result = dispatch_to_audience(
            dispatch_id="d",
            sender_id="a",
            source_claim_id="root",
            semantic_minute=10,
            queue=queue,
            candidates=(AudienceCandidate("b", ("fast",)),),
            memberships=(
                FactionMembership("a", "f", "member"),
                FactionMembership("b", "f", "member"),
            ),
        )
        self.assertEqual(result.selection.selected_agent_ids, ())
        self.assertEqual(queue.pending, [])

    def test_budget_defers_due_messages_without_loss(self):
        queue = self._queue()
        record_direct_observation(queue.ledgers["a"], claim_id="root", subject="route", value="closed", semantic_minute=10, confidence=90)
        for receiver in ("b", "c"):
            queue.schedule(
                event_id=f"e.{receiver}",
                message_id=f"m.{receiver}",
                sender_id="a",
                receiver_id=receiver,
                source_claim_id="root",
                new_claim_id=f"claim.{receiver}",
                channel_id="fast",
                created_minute=10,
            )
        first = queue.process_due_budgeted(20, max_events=1)
        self.assertEqual(first["processed_count"], 1)
        self.assertEqual(first["deferred_due_count"], 1)
        second = queue.process_due_budgeted(20, max_events=1)
        self.assertEqual(second["processed_count"], 1)
        self.assertEqual(second["deferred_due_count"], 0)
        self.assertEqual(len(queue.delivered_event_ids), 2)

    def test_snapshot_restore_preserves_pending_and_delivered_idempotence(self):
        queue = self._queue()
        record_direct_observation(queue.ledgers["a"], claim_id="root", subject="route", value="closed", semantic_minute=10, confidence=90)
        queue.schedule(event_id="e.b", message_id="m.b", sender_id="a", receiver_id="b", source_claim_id="root", new_claim_id="claim.b", channel_id="fast", created_minute=10)
        restored = InformationEventQueue.restore(queue.snapshot(), channels=queue.channels, ledgers=queue.ledgers)
        self.assertEqual(len(restored.pending), 1)
        restored.process_due(20)
        second_restore = InformationEventQueue.restore(restored.snapshot(), channels=queue.channels, ledgers=queue.ledgers)
        self.assertEqual(second_restore.process_due(20), [])
        self.assertEqual(evaluate_belief(queue.ledgers["b"], "route").preferred_value, "closed")

    def test_fixture_replays_integrated_path(self):
        payload = replay_fixture(Path("implementation/global-npc-communication-runtime-fixture-v1.json"))
        self.assertEqual(payload["fixture_id"], "GLOBAL_NPC_COMMUNICATION_RUNTIME_V1")
        by_id = {row["event_id"]: row for row in payload["results"]}
        self.assertEqual(by_id["dispatch.route"]["selected_agent_ids"], ["agent.friend", "agent.officer"])
        self.assertEqual(by_id["advance.first.budget"]["processed_count"], 1)
        self.assertEqual(by_id["advance.first.budget"]["deferred_due_count"], 1)
        self.assertEqual(by_id["assess.friend"]["status"], "SUPPORTED")
        self.assertEqual(by_id["assess.officer"]["status"], "SUPPORTED")
        self.assertEqual(by_id["assess.coworker"]["status"], "UNKNOWN")

    def test_core_is_region_neutral_and_not_tactical(self):
        for filename in ("tools/global_npc_communication_runtime.py", "tools/global_npc_information_network.py"):
            source = Path(filename).read_text(encoding="utf-8")
            for forbidden in ("Marea", "Sendero", "Puerto Bruma", "Loma Clara"):
                self.assertNotIn(forbidden, source)
            for forbidden in ("knockback", "initiative", "status_affliction", "move_id"):
                self.assertNotIn(forbidden, source.lower())


if __name__ == "__main__":
    unittest.main()
