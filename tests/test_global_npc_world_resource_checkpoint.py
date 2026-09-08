import copy
import hashlib
import json
import unittest

from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_resource_requests import (
    ResourceRequest,
    ResourceRequestEvent,
    ResourceRequestEventKind,
    ResourceRequestLedger,
)
from tools.global_npc_resource_reservations import ReservationLedger, ResourceReservation
from tools.global_npc_world_checkpoint import build_checkpoint
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator
from tools.global_npc_world_resource_checkpoint import (
    WORLD_RESOURCE_CHECKPOINT_SCHEMA,
    build_world_resource_checkpoint,
    restore_world_resource_checkpoint,
)


class GlobalNpcWorldResourceCheckpointTests(unittest.TestCase):
    def _world(self):
        agents = {
            "ema": NpcAgentState("ema", AgentMode.OFFSCREEN_NAMED, "synthetic", "repair-row"),
            "teo": NpcAgentState("teo", AgentMode.OFFSCREEN_NAMED, "synthetic", "workshop"),
        }
        ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
        channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 0)}
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=InformationEventQueue(channels=channels, ledgers=ledgers),
            replan_queue=NpcReplanQueue(),
            agents=agents,
        )
        return coordinator, channels

    def _resource_state(self):
        reservations = ReservationLedger(
            (
                ResourceReservation(
                    reservation_id="reservation:meter:ema",
                    resource_id="meter:field:7",
                    actor_id="ema",
                    start_tick=40,
                    end_tick=90,
                    purpose_ref="survey:ridge",
                ),
            )
        )
        requests = ResourceRequestLedger(
            requests=(
                ResourceRequest(
                    request_id="request:meter:ema",
                    requester_actor_id="ema",
                    provider_actor_id="teo",
                    resource_id="meter:field:7",
                    created_tick=12,
                    expires_at_tick=80,
                    purpose_ref="survey:ridge",
                ),
            ),
            events=(
                ResourceRequestEvent(
                    event_id="request-event:meter:accepted",
                    request_id="request:meter:ema",
                    actor_id="teo",
                    kind=ResourceRequestEventKind.ACCEPTED,
                    at_tick=18,
                    offered_resource_id="meter:field:7",
                    reason_ref="meter-ready",
                ),
            ),
        )
        return reservations, requests

    @staticmethod
    def _redigest(checkpoint: dict) -> None:
        payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        checkpoint["sha256"] = hashlib.sha256(canonical).hexdigest()

    def test_v6_round_trip_preserves_world_and_resource_history(self):
        coordinator, channels = self._world()
        reservations, requests = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
        )
        self.assertEqual(checkpoint["schema"], WORLD_RESOURCE_CHECKPOINT_SCHEMA)
        restored = restore_world_resource_checkpoint(checkpoint, channels=channels)
        self.assertEqual(restored.world.semantic_minute, 20)
        self.assertEqual(restored.reservation_ledger, reservations)
        self.assertEqual(restored.request_ledger, requests)
        self.assertEqual(set(restored.world.coordinator.agents), {"ema", "teo"})

    def test_v5_checkpoint_restores_empty_resource_ledgers_without_inference(self):
        coordinator, channels = self._world()
        legacy = build_checkpoint(coordinator, semantic_minute=20)
        restored = restore_world_resource_checkpoint(legacy, channels=channels)
        self.assertEqual(restored.reservation_ledger, ReservationLedger())
        self.assertEqual(restored.request_ledger, ResourceRequestLedger())
        self.assertEqual(restored.world.semantic_minute, 20)

    def test_resource_tampering_is_covered_by_global_digest(self):
        coordinator, channels = self._world()
        reservations, requests = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
        )
        checkpoint["resource_state"]["requests"][0]["provider_actor_id"] = "intruder"
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            restore_world_resource_checkpoint(checkpoint, channels=channels)

    def test_future_resource_event_fails_closed_after_valid_redigest(self):
        coordinator, channels = self._world()
        reservations, requests = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
        )
        checkpoint["resource_state"]["request_events"][0]["at_tick"] = 21
        self._redigest(checkpoint)
        with self.assertRaisesRegex(ValueError, "event comes from the future"):
            restore_world_resource_checkpoint(checkpoint, channels=channels)

    def test_unknown_nested_resource_schema_fails_closed(self):
        coordinator, channels = self._world()
        reservations, requests = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
        )
        checkpoint["resource_state"]["schema"] = "UNKNOWN"
        self._redigest(checkpoint)
        with self.assertRaisesRegex(ValueError, "unsupported resource checkpoint schema"):
            restore_world_resource_checkpoint(checkpoint, channels=channels)

    def test_missing_v6_resource_state_fails_closed(self):
        coordinator, channels = self._world()
        reservations, requests = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
        )
        checkpoint.pop("resource_state")
        self._redigest(checkpoint)
        with self.assertRaisesRegex(ValueError, "resource_state checkpoint is required"):
            restore_world_resource_checkpoint(checkpoint, channels=channels)


if __name__ == "__main__":
    unittest.main()
