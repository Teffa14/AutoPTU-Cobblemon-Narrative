import inspect
import unittest

from tools.global_npc_information_network import (
    CommunicationChannel,
    DeliveryStatus,
    InformationEventQueue,
)
from tools.global_npc_memory import (
    BeliefStatus,
    KnowledgeLedger,
    evaluate_belief,
    record_direct_observation,
)


class GlobalNpcInformationNetworkTests(unittest.TestCase):
    def setUp(self):
        self.ledgers = {
            agent_id: KnowledgeLedger(agent_id)
            for agent_id in ("agent.a", "agent.b", "agent.c", "agent.d")
        }
        self.channels = {
            "direct": CommunicationChannel("direct", "DIRECT_MESSAGE", 10),
            "relay": CommunicationChannel("relay", "PERSONAL_RELAY", 5),
            "local": CommunicationChannel("local", "FACE_TO_FACE", 0, requires_local_projection=True),
            "down": CommunicationChannel("down", "REMOTE_LINK", 2, available=False),
        }
        self.queue = InformationEventQueue(self.channels, self.ledgers)
        record_direct_observation(
            self.ledgers["agent.a"],
            claim_id="root.a",
            subject="fact.x",
            value="YES",
            semantic_minute=0,
            confidence=90,
        )

    def schedule(self, **overrides):
        values = dict(
            event_id="event.a.b",
            message_id="message.a.b",
            sender_id="agent.a",
            receiver_id="agent.b",
            source_claim_id="root.a",
            new_claim_id="claim.b",
            channel_id="direct",
            created_minute=0,
            receiver_trust_in_sender=20,
        )
        values.update(overrides)
        return self.queue.schedule(**values)

    def test_message_has_latency_and_due_only_processing(self):
        envelope = self.schedule()
        self.assertEqual(10, envelope.delivery_minute)
        self.assertEqual([], self.queue.process_due(9))
        self.assertEqual(BeliefStatus.UNKNOWN, evaluate_belief(self.ledgers["agent.b"], "fact.x").status)
        deliveries = self.queue.process_due(10)
        self.assertEqual(DeliveryStatus.DELIVERED.value, deliveries[0]["status"])
        self.assertIn("claim.b", self.ledgers["agent.b"].claims)

    def test_same_faction_or_world_existence_does_not_broadcast(self):
        self.queue.process_due(100)
        self.assertEqual(BeliefStatus.UNKNOWN, evaluate_belief(self.ledgers["agent.c"], "fact.x").status)
        self.assertEqual(BeliefStatus.UNKNOWN, evaluate_belief(self.ledgers["agent.d"], "fact.x").status)

    def test_forwarding_preserves_provenance_root(self):
        self.schedule()
        self.queue.process_due(10)
        self.queue.schedule(
            event_id="event.b.c",
            message_id="message.b.c",
            sender_id="agent.b",
            receiver_id="agent.c",
            source_claim_id="claim.b",
            new_claim_id="claim.c.relay",
            channel_id="relay",
            created_minute=10,
        )
        self.queue.process_due(15)
        self.assertEqual("root.a", self.ledgers["agent.c"].claims["claim.c.relay"].provenance_root)

    def test_two_paths_from_same_root_are_one_independent_source(self):
        self.schedule()
        self.queue.process_due(10)
        self.queue.schedule(
            event_id="event.b.c",
            message_id="message.b.c",
            sender_id="agent.b",
            receiver_id="agent.c",
            source_claim_id="claim.b",
            new_claim_id="claim.c.relay",
            channel_id="relay",
            created_minute=10,
        )
        self.queue.schedule(
            event_id="event.a.c",
            message_id="message.a.c",
            sender_id="agent.a",
            receiver_id="agent.c",
            source_claim_id="root.a",
            new_claim_id="claim.c.direct",
            channel_id="relay",
            created_minute=10,
        )
        self.queue.process_due(15)
        assessment = evaluate_belief(self.ledgers["agent.c"], "fact.x")
        self.assertEqual(("root.a",), assessment.independent_roots_by_value["YES"])

    def test_independent_observer_adds_independent_root(self):
        self.schedule()
        self.queue.process_due(10)
        record_direct_observation(
            self.ledgers["agent.d"],
            claim_id="root.d",
            subject="fact.x",
            value="YES",
            semantic_minute=11,
            confidence=80,
        )
        self.queue.schedule(
            event_id="event.a.c",
            message_id="message.a.c",
            sender_id="agent.a",
            receiver_id="agent.c",
            source_claim_id="root.a",
            new_claim_id="claim.c.a",
            channel_id="relay",
            created_minute=11,
        )
        self.queue.schedule(
            event_id="event.d.c",
            message_id="message.d.c",
            sender_id="agent.d",
            receiver_id="agent.c",
            source_claim_id="root.d",
            new_claim_id="claim.c.d",
            channel_id="relay",
            created_minute=11,
        )
        self.queue.process_due(16)
        assessment = evaluate_belief(self.ledgers["agent.c"], "fact.x")
        self.assertEqual(("root.a", "root.d"), assessment.independent_roots_by_value["YES"])

    def test_unavailable_channel_fails_without_knowledge_transfer(self):
        self.schedule(channel_id="down")
        results = self.queue.process_due(2)
        self.assertEqual(DeliveryStatus.FAILED_CHANNEL_UNAVAILABLE.value, results[0]["status"])
        self.assertNotIn("claim.b", self.ledgers["agent.b"].claims)

    def test_local_projection_requires_ack_before_ledger_mutation(self):
        self.schedule(channel_id="local")
        results = self.queue.process_due(0)
        self.assertEqual(DeliveryStatus.WAITING_LOCAL_ACK.value, results[0]["status"])
        self.assertNotIn("claim.b", self.ledgers["agent.b"].claims)
        ack = self.queue.acknowledge_local_delivery("event.a.b", 1, accepted=True)
        self.assertEqual(DeliveryStatus.DELIVERED.value, ack["status"])
        self.assertIn("claim.b", self.ledgers["agent.b"].claims)

    def test_replay_delivery_is_idempotent(self):
        self.schedule()
        first = self.queue.process_due(10)
        second = self.queue.process_due(10)
        self.assertEqual(1, len(first))
        self.assertEqual([], second)
        self.assertEqual(1, len(self.ledgers["agent.b"].claims))

    def test_deterministic_order_for_same_minute(self):
        self.schedule(event_id="event.z", new_claim_id="claim.b.z")
        self.queue.schedule(
            event_id="event.a",
            message_id="message.a.c",
            sender_id="agent.a",
            receiver_id="agent.c",
            source_claim_id="root.a",
            new_claim_id="claim.c.a",
            channel_id="direct",
            created_minute=0,
        )
        results = self.queue.process_due(10)
        self.assertEqual(["event.a", "event.z"], [entry["event_id"] for entry in results])

    def test_core_is_region_neutral_and_has_no_tactical_resolution(self):
        import tools.global_npc_information_network as module

        source = inspect.getsource(module)
        for forbidden in ("Marea", "Sendero", "Puerto Bruma", "Loma Clara"):
            self.assertNotIn(forbidden, source)
        for tactical in ("damageDealt", "initiativeOrder", "knockbackDistance", "moveAccuracy"):
            self.assertNotIn(tactical, source)


if __name__ == "__main__":
    unittest.main()
