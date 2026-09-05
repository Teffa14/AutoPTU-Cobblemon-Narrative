import inspect
import unittest
from pathlib import Path

from tools.global_npc_ai import AgentMode, DurableGoal, Handoff, NpcAgentState, NpcIntent
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_event_coordinator import (
    AgentAgendaProfile,
    GlobalNpcWorldEventCoordinator,
    replay_fixture,
)


class GlobalNpcWorldEventCoordinatorTests(unittest.TestCase):
    def _runtime(self, *, courier_mode=AgentMode.OFFSCREEN_NAMED, channel_available=True):
        ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in ("witness", "courier", "other")}
        channels = {
            "private": CommunicationChannel("private", "PRIVATE_MESSAGE", 5, available=channel_available)
        }
        information = InformationEventQueue(channels=channels, ledgers=ledgers)
        agents = {
            "witness": NpcAgentState("witness", AgentMode.OFFSCREEN_NAMED, "fixture.a", "fixture.a.1"),
            "courier": NpcAgentState("courier", courier_mode, "fixture.b", "fixture.b.1"),
            "other": NpcAgentState("other", AgentMode.OFFSCREEN_NAMED, "fixture.b", "fixture.b.2"),
        }
        agenda = AgentAgendaProfile(
            goals=(DurableGoal("deliver", "CONTINUE_DELIVERY", 4, target_ref="fixture.destination"),),
            situational_intents=(
                NpcIntent(
                    "detour",
                    "REPLAN_ROUTE",
                    base_priority=9,
                    urgency=9,
                    required_knowledge=frozenset({"claim.courier"}),
                    target_ref="fixture.detour",
                ),
            ),
        )
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=information,
            replan_queue=NpcReplanQueue(),
            agents=agents,
            agendas={"courier": agenda},
        )
        return coordinator, ledgers

    def _schedule_warning(self, coordinator, ledgers):
        record_direct_observation(
            ledgers["witness"],
            claim_id="claim.root",
            subject="route.primary",
            value="closed",
            semantic_minute=10,
            confidence=95,
        )
        coordinator.information_queue.schedule(
            event_id="delivery.warning",
            message_id="message.warning",
            sender_id="witness",
            receiver_id="courier",
            source_claim_id="claim.root",
            new_claim_id="claim.courier",
            channel_id="private",
            created_minute=10,
        )

    def test_delivery_updates_only_receiver_then_replans_that_agent(self):
        coordinator, ledgers = self._runtime()
        self._schedule_warning(coordinator, ledgers)
        before = coordinator.process_cycle(14, delivery_budget=1)
        self.assertEqual(before.decisions, ())
        self.assertNotIn("claim.courier", coordinator.agents["courier"].knowledge)

        cycle = coordinator.process_cycle(15, delivery_budget=1, replan_priority=8)
        self.assertEqual(cycle.delivery_processed_count, 1)
        self.assertEqual(cycle.materialized[0].wake_status, "WAKE_SCHEDULED")
        self.assertEqual([row.agent_id for row in cycle.decisions], ["courier"])
        self.assertEqual(cycle.decisions[0].decision.decision.kind, "REPLAN_ROUTE")
        self.assertEqual(cycle.decisions[0].decision.decision.target_ref, "fixture.detour")
        self.assertIn("claim.courier", coordinator.agents["courier"].knowledge)
        self.assertNotIn("claim.courier", coordinator.agents["other"].knowledge)

    def test_failed_delivery_does_not_change_agent_or_wake_it(self):
        coordinator, ledgers = self._runtime(channel_available=False)
        self._schedule_warning(coordinator, ledgers)
        cycle = coordinator.process_cycle(15, delivery_budget=1)
        self.assertEqual(cycle.materialized[0].wake_status, "NO_WAKE_NON_DELIVERY")
        self.assertEqual(cycle.decisions, ())
        self.assertNotIn("claim.courier", coordinator.agents["courier"].knowledge)

    def test_duplicate_completed_delivery_cannot_create_second_wakeup(self):
        coordinator, ledgers = self._runtime()
        self._schedule_warning(coordinator, ledgers)
        cycle = coordinator.process_cycle(15, delivery_budget=1)
        delivery = cycle.deliveries[0]
        second = coordinator.materialize_delivery(delivery, semantic_minute=15)
        self.assertEqual(second.wake_status, "NO_WAKE_DUPLICATE")
        self.assertEqual(coordinator.replan_queue.process_due(15), [])

    def test_delivery_budget_limits_how_many_agents_can_be_woken_by_messages(self):
        coordinator, ledgers = self._runtime()
        record_direct_observation(
            ledgers["witness"],
            claim_id="claim.root",
            subject="route.primary",
            value="closed",
            semantic_minute=10,
            confidence=95,
        )
        for receiver in ("courier", "other"):
            coordinator.information_queue.schedule(
                event_id=f"delivery.{receiver}",
                message_id=f"message.{receiver}",
                sender_id="witness",
                receiver_id=receiver,
                source_claim_id="claim.root",
                new_claim_id=f"claim.{receiver}",
                channel_id="private",
                created_minute=10,
            )
        first = coordinator.process_cycle(15, delivery_budget=1)
        self.assertEqual(first.delivery_processed_count, 1)
        self.assertEqual(first.delivery_deferred_due_count, 1)
        self.assertEqual(len(first.materialized), 1)
        second = coordinator.process_cycle(15, delivery_budget=1)
        self.assertEqual(second.delivery_processed_count, 1)
        self.assertEqual(second.delivery_deferred_due_count, 0)

    def test_autoptu_bound_receiver_holds_structured_owner_after_wakeup(self):
        coordinator, ledgers = self._runtime(courier_mode=AgentMode.AUTOPTU_BOUND)
        self._schedule_warning(coordinator, ledgers)
        cycle = coordinator.process_cycle(15, delivery_budget=1)
        self.assertEqual(cycle.decisions[0].decision.decision.kind, "HOLD_AUTOPTU")
        self.assertEqual(cycle.decisions[0].decision.decision.handoff, Handoff.HOLD_EXISTING_AUTOPTU_BINDING)

    def test_fixture_replays_integrated_delivery_to_decision_path(self):
        payload = replay_fixture(Path("implementation/global-npc-world-event-coordinator-fixture-v1.json"))
        self.assertEqual(payload["fixture_id"], "GLOBAL_NPC_WORLD_EVENT_COORDINATOR_V1")
        by_id = {row["event_id"]: row for row in payload["results"]}
        self.assertEqual(by_id["cycle.before.delivery"]["processed"], 0)
        self.assertEqual(by_id["cycle.delivery.and.replan"]["materialized"], ["WAKE_SCHEDULED"])
        self.assertEqual(by_id["cycle.delivery.and.replan"]["decisions"][0]["agent_id"], "agent.courier")
        self.assertEqual(by_id["cycle.delivery.and.replan"]["decisions"][0]["kind"], "REPLAN_ROUTE")
        self.assertEqual(by_id["assess.courier"]["status"], "SUPPORTED")
        self.assertTrue(by_id["assess.courier"]["agent_knows_claim"])
        self.assertEqual(by_id["assess.bystander"]["status"], "UNKNOWN")
        self.assertFalse(by_id["assess.bystander"]["agent_knows_claim"])

    def test_core_is_region_neutral_and_does_not_resolve_tactics(self):
        import tools.global_npc_world_event_coordinator as module

        source = inspect.getsource(module)
        for forbidden in ("Marea", "Sendero", "Puerto Bruma", "Loma Clara"):
            self.assertNotIn(forbidden, source)
        for tactical in ("damageDealt", "initiativeOrder", "knockbackDistance", "moveAccuracy"):
            self.assertNotIn(tactical, source)


if __name__ == "__main__":
    unittest.main()
