import unittest
from dataclasses import replace

from tools.autoptu_world_observation_delivery import schedule_world_observation_delivery
from tools.autoptu_world_observation_owner import WorldObservationRecord
from tools.autoptu_world_observation_replanning import (
    acknowledge_observation_delivery_for_replanning,
    advance_observation_delivery_for_replanning,
)
from tools.global_npc_ai import AgentMode, NpcAgentState, NpcIntent
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


class AutoPTUWorldObservationReplanningTests(unittest.TestCase):
    def observation(self):
        return WorldObservationRecord(
            transaction_id="ouros.world-consequence.pass421",
            session_id="ouros.autoptu.session.pass421",
            result_ref="result:pass421:1",
            objective_ref="objective:pass421:route-inspection",
            outcome="PARTIAL",
            provenance_ref="ingress:pass421:1",
            evidence_ref="evidence:pass421:marker",
        )

    def system(self, *, latency=2, available=True, requires_local_projection=False):
        ledgers = {
            "marea-dispatch": KnowledgeLedger("marea-dispatch"),
            "field-team-b": KnowledgeLedger("field-team-b"),
            "unrelated-member": KnowledgeLedger("unrelated-member"),
        }
        queue = InformationEventQueue(
            channels={
                "radio": CommunicationChannel(
                    channel_id="radio",
                    kind="RADIO",
                    latency_minutes=latency,
                    available=available,
                    requires_local_projection=requires_local_projection,
                )
            },
            ledgers=ledgers,
        )
        agents = {
            "field-team-b": NpcAgentState(
                agent_id="field-team-b",
                mode=AgentMode.OFFSCREEN_NAMED,
                region_ref="marea-interior",
                location_ref="marea-field-office",
            ),
            "unrelated-member": NpcAgentState(
                agent_id="unrelated-member",
                mode=AgentMode.OFFSCREEN_NAMED,
                region_ref="marea-interior",
                location_ref="marea-field-office",
            ),
        }
        response_intent = NpcIntent(
            intent_id="respond-to-field-warning",
            kind="REASSESS_ROUTE",
            base_priority=10,
            urgency=8,
            required_knowledge=frozenset({"claim:pass421:field-team-b"}),
            target_ref="route:alternate-review",
        )
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=queue,
            replan_queue=NpcReplanQueue(),
            agents=agents,
            agendas={
                "field-team-b": AgentAgendaProfile(situational_intents=(response_intent,)),
                "unrelated-member": AgentAgendaProfile(situational_intents=(response_intent,)),
            },
        )
        scheduled, changed = schedule_world_observation_delivery(
            self.observation(),
            queue=queue,
            custodian_id="marea-dispatch",
            recipient_id="field-team-b",
            channel_id="radio",
            created_minute=100,
            source_claim_id="claim:pass421:observation-record",
            event_id="delivery:pass421:field-team-b",
            message_id="message:pass421:field-team-b",
            receiver_claim_id="claim:pass421:field-team-b",
        )
        self.assertTrue(changed)
        return scheduled, coordinator

    def test_only_explicit_recipient_wakes_after_terminal_delivery(self):
        scheduled, coordinator = self.system()
        outcome = advance_observation_delivery_for_replanning(
            scheduled,
            coordinator=coordinator,
            semantic_minute=102,
        )
        self.assertEqual(outcome.delivery_status, "DELIVERED")
        self.assertEqual(outcome.wake_status, "WAKE_SCHEDULED")
        self.assertEqual(outcome.provenance_root, "ouros.world-consequence.pass421")
        self.assertEqual(len(outcome.decisions), 1)
        self.assertEqual(outcome.decisions[0].agent_id, "field-team-b")
        self.assertEqual(outcome.decisions[0].decision.decision.kind, "REASSESS_ROUTE")
        self.assertIn("claim:pass421:field-team-b", coordinator.agents["field-team-b"].knowledge)
        self.assertIn("ouros.world-consequence.pass421", coordinator.agents["field-team-b"].memory_refs)
        self.assertEqual(coordinator.agents["unrelated-member"].knowledge, frozenset())
        self.assertEqual(coordinator.agents["unrelated-member"].memory_refs, ())

    def test_queued_delivery_does_not_wake_recipient(self):
        scheduled, coordinator = self.system(latency=5)
        outcome = advance_observation_delivery_for_replanning(
            scheduled,
            coordinator=coordinator,
            semantic_minute=104,
        )
        self.assertEqual(outcome.delivery_status, "QUEUED")
        self.assertEqual(outcome.wake_status, "NO_DELIVERY_THIS_CYCLE")
        self.assertEqual(outcome.decisions, ())
        self.assertEqual(coordinator.agents["field-team-b"].knowledge, frozenset())

    def test_failed_channel_does_not_wake_recipient(self):
        scheduled, coordinator = self.system(available=False)
        outcome = advance_observation_delivery_for_replanning(
            scheduled,
            coordinator=coordinator,
            semantic_minute=102,
        )
        self.assertEqual(outcome.delivery_status, "FAILED_CHANNEL_UNAVAILABLE")
        self.assertEqual(outcome.wake_status, "NO_WAKE_NON_DELIVERY")
        self.assertEqual(outcome.decisions, ())
        self.assertEqual(coordinator.agents["field-team-b"].knowledge, frozenset())

    def test_waiting_local_ack_does_not_wake_until_accepted(self):
        scheduled, coordinator = self.system(requires_local_projection=True)
        waiting = advance_observation_delivery_for_replanning(
            scheduled,
            coordinator=coordinator,
            semantic_minute=102,
        )
        self.assertEqual(waiting.delivery_status, "WAITING_LOCAL_ACK")
        self.assertEqual(waiting.decisions, ())
        self.assertEqual(coordinator.agents["field-team-b"].knowledge, frozenset())

        accepted = acknowledge_observation_delivery_for_replanning(
            scheduled,
            coordinator=coordinator,
            semantic_minute=103,
            accepted=True,
        )
        self.assertEqual(accepted.delivery_status, "DELIVERED")
        self.assertEqual(accepted.wake_status, "WAKE_SCHEDULED")
        self.assertEqual(accepted.provenance_root, "ouros.world-consequence.pass421")
        self.assertEqual(len(accepted.decisions), 1)
        self.assertEqual(accepted.decisions[0].decision.decision.kind, "REASSESS_ROUTE")

    def test_rejected_local_ack_never_wakes_recipient(self):
        scheduled, coordinator = self.system(requires_local_projection=True)
        advance_observation_delivery_for_replanning(
            scheduled,
            coordinator=coordinator,
            semantic_minute=102,
        )
        rejected = acknowledge_observation_delivery_for_replanning(
            scheduled,
            coordinator=coordinator,
            semantic_minute=103,
            accepted=False,
        )
        self.assertEqual(rejected.delivery_status, "FAILED_CHANNEL_UNAVAILABLE")
        self.assertEqual(rejected.wake_status, "NO_WAKE_NON_DELIVERY")
        self.assertEqual(rejected.decisions, ())
        self.assertEqual(coordinator.agents["field-team-b"].knowledge, frozenset())

    def test_tampered_provenance_binding_fails_before_delivery(self):
        scheduled, coordinator = self.system()
        tampered = replace(scheduled, observation_transaction_id="ouros.world-consequence.other")
        with self.assertRaisesRegex(ValueError, "provenance root mismatch"):
            advance_observation_delivery_for_replanning(
                tampered,
                coordinator=coordinator,
                semantic_minute=102,
            )
        self.assertEqual(coordinator.agents["field-team-b"].knowledge, frozenset())

    def test_delivery_budget_can_defer_target_without_false_wake(self):
        scheduled, coordinator = self.system(latency=0)
        outcome = advance_observation_delivery_for_replanning(
            scheduled,
            coordinator=coordinator,
            semantic_minute=100,
            delivery_budget=0,
        )
        self.assertEqual(outcome.delivery_status, "QUEUED")
        self.assertEqual(outcome.wake_status, "NO_DELIVERY_THIS_CYCLE")
        self.assertEqual(outcome.decisions, ())


if __name__ == "__main__":
    unittest.main()
