import copy
import unittest
from pathlib import Path

from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_checkpoint import build_checkpoint, replay_fixture, restore_checkpoint
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator


class GlobalNpcWorldCheckpointTests(unittest.TestCase):
    def _world(self):
        agents = {
            "sender": NpcAgentState("sender", AgentMode.OFFSCREEN_NAMED, "synthetic_a", "relay"),
            "receiver": NpcAgentState("receiver", AgentMode.OFFSCREEN_NAMED, "synthetic_a", "road"),
        }
        ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
        channels = {
            "wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 0),
        }
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=InformationEventQueue(channels=channels, ledgers=ledgers),
            replan_queue=NpcReplanQueue(),
            agents=agents,
        )
        return coordinator, channels

    def test_pending_delivery_survives_checkpoint_and_delivers_once(self):
        coordinator, channels = self._world()
        record_direct_observation(
            coordinator.information_queue.ledgers["sender"],
            claim_id="source",
            subject="route:test",
            value="CLOSED",
            semantic_minute=1,
            confidence=90,
        )
        coordinator.information_queue.schedule(
            event_id="delivery-1",
            message_id="message-1",
            sender_id="sender",
            receiver_id="receiver",
            source_claim_id="source",
            new_claim_id="received",
            channel_id="wire",
            created_minute=2,
        )
        restored = restore_checkpoint(build_checkpoint(coordinator, semantic_minute=2), channels=channels)
        cycle = restored.coordinator.process_cycle(2, delivery_budget=2)
        self.assertEqual(cycle.delivery_processed_count, 1)
        self.assertEqual(cycle.materialized[0].wake_status, "WAKE_SCHEDULED")
        self.assertIn("received", restored.ledger_store.require("receiver").claims)
        self.assertIn("received", restored.coordinator.agents["receiver"].knowledge)
        second = restored.coordinator.process_cycle(2, delivery_budget=2)
        self.assertEqual(second.delivery_processed_count, 0)
        self.assertEqual(len(second.decisions), 0)

    def test_materialization_guard_survives_checkpoint(self):
        coordinator, channels = self._world()
        record_direct_observation(
            coordinator.information_queue.ledgers["sender"],
            claim_id="source",
            subject="route:test",
            value="CLOSED",
            semantic_minute=1,
            confidence=90,
        )
        coordinator.information_queue.schedule(
            event_id="delivery-1",
            message_id="message-1",
            sender_id="sender",
            receiver_id="receiver",
            source_claim_id="source",
            new_claim_id="received",
            channel_id="wire",
            created_minute=2,
        )
        first = coordinator.process_cycle(2, delivery_budget=1)
        delivery = first.deliveries[0]
        restored = restore_checkpoint(build_checkpoint(coordinator, semantic_minute=2), channels=channels)
        duplicate = restored.coordinator.materialize_delivery(delivery, semantic_minute=2)
        self.assertEqual(duplicate.wake_status, "NO_WAKE_DUPLICATE")

    def test_digest_rejects_partial_or_mutated_checkpoint(self):
        coordinator, channels = self._world()
        checkpoint = build_checkpoint(coordinator, semantic_minute=4)
        corrupted = copy.deepcopy(checkpoint)
        corrupted["semantic_minute"] = 5
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            restore_checkpoint(corrupted, channels=channels)

    def test_materialized_guard_must_reference_delivered_event(self):
        coordinator, channels = self._world()
        coordinator.materialized_delivery_event_ids.add("ghost-delivery")
        checkpoint = build_checkpoint(coordinator, semantic_minute=4)
        with self.assertRaisesRegex(ValueError, "non-delivered"):
            restore_checkpoint(checkpoint, channels=channels)

    def test_fixture_replays_deterministically(self):
        path = Path("implementation/global-npc-world-checkpoint-fixture-v1.json")
        first = replay_fixture(path)
        second = replay_fixture(path)
        self.assertEqual(first, second)
        courier = next(row for row in first["results"] if row["event_id"] == "inspect-courier")
        bystander = next(row for row in first["results"] if row["event_id"] == "inspect-bystander")
        self.assertIn("courier-route-warning", courier["claim_ids"])
        self.assertIn("courier-route-warning", courier["knowledge"])
        self.assertEqual(bystander["claim_ids"], [])

    def test_core_has_no_authored_region_or_tactical_special_case(self):
        source = Path("tools/global_npc_world_checkpoint.py").read_text(encoding="utf-8").lower()
        for forbidden in (
            "marea",
            "sendero",
            "puerto bruma",
            "loma clara",
            "knockback",
            "initiative",
            "damage roll",
            "move accuracy",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
