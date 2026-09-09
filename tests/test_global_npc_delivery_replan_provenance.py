import copy
import unittest

from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_delivery_replan_provenance import (
    DeliveryReplanProvenanceLedger,
    ProvenanceAwareWorldEventRuntime,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_replanning import NpcReplanQueue, ReplanReason, ReplanTrigger
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator


class GlobalNpcDeliveryReplanProvenanceTests(unittest.TestCase):
    def _runtime(self, *, channel_available=True):
        ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in ("sender", "receiver")}
        queue = InformationEventQueue(
            channels={"radio": CommunicationChannel("radio", "PRIVATE_RADIO", 5, available=channel_available)},
            ledgers=ledgers,
        )
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=queue,
            replan_queue=NpcReplanQueue(),
            agents={
                "sender": NpcAgentState("sender", AgentMode.OFFSCREEN_NAMED, "fixture", "fixture.office"),
                "receiver": NpcAgentState("receiver", AgentMode.OFFSCREEN_NAMED, "fixture", "fixture.field"),
            },
        )
        runtime = ProvenanceAwareWorldEventRuntime(coordinator)
        return runtime, ledgers

    def _schedule(self, runtime, ledgers):
        record_direct_observation(
            ledgers["sender"],
            claim_id="claim.root",
            subject="route.alpha",
            value="closed",
            semantic_minute=10,
            confidence=95,
        )
        runtime.coordinator.information_queue.schedule(
            event_id="delivery.route",
            message_id="message.route",
            sender_id="sender",
            receiver_id="receiver",
            source_claim_id="claim.root",
            new_claim_id="claim.receiver",
            channel_id="radio",
            created_minute=10,
        )

    def test_delivered_materialization_and_consumed_trigger_keep_structured_provenance(self):
        runtime, ledgers = self._runtime()
        self._schedule(runtime, ledgers)
        cycle = runtime.process_cycle(15, delivery_budget=1, replan_priority=8)

        self.assertEqual(cycle.materialized[0].wake_status, "WAKE_SCHEDULED")
        receipt = runtime.ledger.materializations["delivery.route"]
        self.assertEqual(receipt.receiver_id, "receiver")
        self.assertEqual(receipt.claim_ref, "claim.receiver")
        self.assertEqual(receipt.provenance_root, "claim.root")
        self.assertEqual(receipt.replan_trigger_id, "replan:information:delivery.route")

        consumed = runtime.ledger.consumptions[receipt.replan_trigger_id]
        self.assertEqual(consumed.agent_id, "receiver")
        self.assertEqual(consumed.reason, ReplanReason.KNOWLEDGE_DELIVERED.value)
        self.assertEqual(consumed.source_ref, "delivery.route")
        self.assertEqual(consumed.due_minute, 15)
        self.assertEqual(consumed.processed_minute, 15)
        runtime.ledger.validate_against(runtime.coordinator, semantic_minute=15)

    def test_snapshot_round_trip_preserves_receipt_and_consumption(self):
        runtime, ledgers = self._runtime()
        self._schedule(runtime, ledgers)
        runtime.process_cycle(15, delivery_budget=1)

        restored = DeliveryReplanProvenanceLedger.restore(runtime.ledger.snapshot())
        self.assertEqual(restored.materializations, runtime.ledger.materializations)
        self.assertEqual(restored.consumptions, runtime.ledger.consumptions)
        restored.validate_against(runtime.coordinator, semantic_minute=15)

    def test_failed_delivery_cannot_create_successful_materialization_receipt(self):
        runtime, ledgers = self._runtime(channel_available=False)
        self._schedule(runtime, ledgers)
        cycle = runtime.process_cycle(15, delivery_budget=1)
        self.assertEqual(cycle.materialized[0].wake_status, "NO_WAKE_NON_DELIVERY")
        self.assertEqual(runtime.ledger.materializations, {})
        self.assertEqual(runtime.ledger.consumptions, {})

    def test_receiver_tampering_fails_validation_even_if_ledger_shape_is_valid(self):
        runtime, ledgers = self._runtime()
        self._schedule(runtime, ledgers)
        runtime.process_cycle(15, delivery_budget=1)
        snapshot = runtime.ledger.snapshot()
        snapshot["materializations"][0]["receiver_id"] = "sender"
        tampered = DeliveryReplanProvenanceLedger.restore(snapshot)
        with self.assertRaisesRegex(ValueError, "receiver mismatch"):
            tampered.validate_against(runtime.coordinator, semantic_minute=15)

    def test_consumed_trigger_source_tampering_fails_against_materialization(self):
        runtime, ledgers = self._runtime()
        self._schedule(runtime, ledgers)
        runtime.process_cycle(15, delivery_budget=1)
        snapshot = copy.deepcopy(runtime.ledger.snapshot())
        snapshot["consumptions"][0]["source_ref"] = "delivery.other"
        tampered = DeliveryReplanProvenanceLedger.restore(snapshot)
        with self.assertRaisesRegex(ValueError, "lacks materialization receipt"):
            tampered.validate_against(runtime.coordinator, semantic_minute=15)

    def test_future_materialization_fails_validation(self):
        runtime, ledgers = self._runtime()
        self._schedule(runtime, ledgers)
        runtime.process_cycle(15, delivery_budget=1)
        snapshot = copy.deepcopy(runtime.ledger.snapshot())
        snapshot["materializations"][0]["materialized_minute"] = 16
        future = DeliveryReplanProvenanceLedger.restore(snapshot)
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            future.validate_against(runtime.coordinator, semantic_minute=15)

    def test_non_delivery_trigger_consumption_keeps_full_trigger_provenance(self):
        runtime, _ = self._runtime()
        trigger = ReplanTrigger(
            "trigger.schedule",
            "receiver",
            ReplanReason.SCHEDULE_DUE,
            20,
            "commitment.field-shift",
            4,
        )
        runtime.coordinator.replan_queue.schedule(trigger)
        runtime.process_cycle(20, delivery_budget=0)
        consumed = runtime.ledger.consumptions["trigger.schedule"]
        self.assertEqual(consumed.reason, ReplanReason.SCHEDULE_DUE.value)
        self.assertEqual(consumed.source_ref, "commitment.field-shift")
        self.assertEqual(consumed.priority, 4)
        self.assertEqual(consumed.batch_key, "replan-batch:receiver:20")

    def test_duplicate_successful_materialization_is_rejected_by_ledger(self):
        runtime, ledgers = self._runtime()
        self._schedule(runtime, ledgers)
        cycle = runtime.process_cycle(15, delivery_budget=1)
        delivery = cycle.deliveries[0]
        materialized = cycle.materialized[0]
        with self.assertRaisesRegex(ValueError, "already materialized"):
            runtime.ledger.record_materialization(delivery, materialized, semantic_minute=15)


if __name__ == "__main__":
    unittest.main()
