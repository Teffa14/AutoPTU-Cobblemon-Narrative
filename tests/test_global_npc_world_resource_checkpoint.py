import copy
import hashlib
import json
import unittest

from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_resource_checkpoint import snapshot_resource_state, snapshot_resource_state_with_handoffs
from tools.global_npc_resource_handoff_attempts import (
    HandoffAttemptOutcome,
    ResourceHandoffAttempt,
    ResourceHandoffAttemptLedger,
)
from tools.global_npc_resource_handoffs import (
    HandoffMode,
    ResourceCustodyTransfer,
    ResourceHandoffAuthorization,
    ResourceHandoffLedger,
)
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
    LEGACY_WORLD_RESOURCE_CHECKPOINT_SCHEMA,
    LEGACY_WORLD_RESOURCE_HANDOFF_CHECKPOINT_SCHEMA,
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
        handoffs = ResourceHandoffLedger(
            authorizations=(
                ResourceHandoffAuthorization(
                    authorization_id="handoff-auth:meter:ema",
                    request_id="request:meter:ema",
                    provider_actor_id="teo",
                    accountable_actor_id="teo",
                    receiving_actor_id="ema",
                    resource_id="meter:field:7",
                    mode=HandoffMode.PICKUP,
                    handoff_location_ref="workshop",
                    valid_from_tick=19,
                    valid_until_tick=30,
                    authority_ref="workshop:instrument-custody",
                ),
            ),
            transfers=(
                ResourceCustodyTransfer(
                    transfer_id="handoff-transfer:meter:ema",
                    authorization_id="handoff-auth:meter:ema",
                    request_id="request:meter:ema",
                    resource_id="meter:field:7",
                    from_actor_id="teo",
                    to_actor_id="ema",
                    accountable_actor_id="teo",
                    location_ref="workshop",
                    at_tick=20,
                    condition_ref="inspection:ready",
                ),
            ),
        )
        attempts = ResourceHandoffAttemptLedger(
            attempts=(
                ResourceHandoffAttempt(
                    attempt_id="handoff-attempt:meter:first",
                    authorization_id="handoff-auth:meter:ema",
                    actor_id="ema",
                    location_ref="workshop",
                    at_tick=19,
                    outcome=HandoffAttemptOutcome.PROVIDER_ABSENT,
                    observation_ref="observation:closed-counter",
                ),
            )
        )
        return reservations, requests, handoffs, attempts

    @staticmethod
    def _redigest(checkpoint: dict) -> None:
        payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        checkpoint["sha256"] = hashlib.sha256(canonical).hexdigest()

    def _legacy_v6(self, coordinator, reservations, requests, *, semantic_minute=20):
        checkpoint = build_checkpoint(coordinator, semantic_minute=semantic_minute)
        checkpoint = {key: value for key, value in checkpoint.items() if key != "sha256"}
        checkpoint["schema"] = LEGACY_WORLD_RESOURCE_CHECKPOINT_SCHEMA
        checkpoint["resource_state"] = snapshot_resource_state(reservations, requests)
        self._redigest(checkpoint)
        return checkpoint

    def _legacy_v7(self, coordinator, reservations, requests, handoffs, *, semantic_minute=20):
        checkpoint = build_checkpoint(coordinator, semantic_minute=semantic_minute)
        checkpoint = {key: value for key, value in checkpoint.items() if key != "sha256"}
        checkpoint["schema"] = LEGACY_WORLD_RESOURCE_HANDOFF_CHECKPOINT_SCHEMA
        checkpoint["resource_state"] = snapshot_resource_state_with_handoffs(reservations, requests, handoffs)
        self._redigest(checkpoint)
        return checkpoint

    def test_v8_round_trip_preserves_world_handoff_and_failed_attempt_history(self):
        coordinator, channels = self._world()
        reservations, requests, handoffs, attempts = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
            handoff_ledger=handoffs,
            attempt_ledger=attempts,
        )
        self.assertEqual(checkpoint["schema"], WORLD_RESOURCE_CHECKPOINT_SCHEMA)
        self.assertEqual(checkpoint["resource_state"]["schema"], "OUROS_NPC_RESOURCE_CHECKPOINT_V3")
        restored = restore_world_resource_checkpoint(checkpoint, channels=channels)
        self.assertEqual(restored.world.semantic_minute, 20)
        self.assertEqual(restored.reservation_ledger, reservations)
        self.assertEqual(restored.request_ledger, requests)
        self.assertEqual(restored.handoff_ledger, handoffs)
        self.assertEqual(restored.attempt_ledger, attempts)
        self.assertEqual(set(restored.world.coordinator.agents), {"ema", "teo"})

    def test_v8_default_empty_attempt_ledger_is_explicit(self):
        coordinator, channels = self._world()
        reservations, requests, handoffs, _ = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
            handoff_ledger=handoffs,
        )
        restored = restore_world_resource_checkpoint(checkpoint, channels=channels)
        self.assertEqual(restored.attempt_ledger, ResourceHandoffAttemptLedger())

    def test_v7_checkpoint_restores_handoff_history_and_empty_attempts(self):
        coordinator, channels = self._world()
        reservations, requests, handoffs, _ = self._resource_state()
        legacy = self._legacy_v7(coordinator, reservations, requests, handoffs)
        restored = restore_world_resource_checkpoint(legacy, channels=channels)
        self.assertEqual(restored.reservation_ledger, reservations)
        self.assertEqual(restored.request_ledger, requests)
        self.assertEqual(restored.handoff_ledger, handoffs)
        self.assertEqual(restored.attempt_ledger, ResourceHandoffAttemptLedger())

    def test_v6_checkpoint_restores_resource_history_and_empty_handoffs_and_attempts(self):
        coordinator, channels = self._world()
        reservations, requests, _, _ = self._resource_state()
        legacy = self._legacy_v6(coordinator, reservations, requests)
        restored = restore_world_resource_checkpoint(legacy, channels=channels)
        self.assertEqual(restored.reservation_ledger, reservations)
        self.assertEqual(restored.request_ledger, requests)
        self.assertEqual(restored.handoff_ledger, ResourceHandoffLedger())
        self.assertEqual(restored.attempt_ledger, ResourceHandoffAttemptLedger())

    def test_v5_checkpoint_restores_empty_resource_ledgers_without_inference(self):
        coordinator, channels = self._world()
        legacy = build_checkpoint(coordinator, semantic_minute=20)
        restored = restore_world_resource_checkpoint(legacy, channels=channels)
        self.assertEqual(restored.reservation_ledger, ReservationLedger())
        self.assertEqual(restored.request_ledger, ResourceRequestLedger())
        self.assertEqual(restored.handoff_ledger, ResourceHandoffLedger())
        self.assertEqual(restored.attempt_ledger, ResourceHandoffAttemptLedger())

    def test_attempt_tampering_is_covered_by_global_digest(self):
        coordinator, channels = self._world()
        reservations, requests, handoffs, attempts = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
            handoff_ledger=handoffs,
            attempt_ledger=attempts,
        )
        checkpoint["resource_state"]["handoff_attempts"][0]["actor_id"] = "intruder"
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            restore_world_resource_checkpoint(checkpoint, channels=channels)

    def test_future_resource_event_fails_closed_after_valid_redigest(self):
        coordinator, channels = self._world()
        reservations, requests, handoffs, attempts = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
            handoff_ledger=handoffs,
            attempt_ledger=attempts,
        )
        checkpoint["resource_state"]["request_events"][0]["at_tick"] = 21
        self._redigest(checkpoint)
        with self.assertRaisesRegex(ValueError, "event comes from the future"):
            restore_world_resource_checkpoint(checkpoint, channels=channels)

    def test_future_handoff_attempt_fails_closed_after_valid_redigest(self):
        coordinator, channels = self._world()
        reservations, requests, handoffs, attempts = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
            handoff_ledger=handoffs,
            attempt_ledger=attempts,
        )
        checkpoint["resource_state"]["handoff_attempts"][0]["at_tick"] = 21
        self._redigest(checkpoint)
        with self.assertRaisesRegex(ValueError, "handoff attempt comes from the future"):
            restore_world_resource_checkpoint(checkpoint, channels=channels)

    def test_unknown_nested_resource_schema_fails_closed(self):
        coordinator, channels = self._world()
        reservations, requests, handoffs, attempts = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
            handoff_ledger=handoffs,
            attempt_ledger=attempts,
        )
        checkpoint["resource_state"]["schema"] = "UNKNOWN"
        self._redigest(checkpoint)
        with self.assertRaisesRegex(ValueError, "unsupported resource attempt checkpoint schema"):
            restore_world_resource_checkpoint(checkpoint, channels=channels)

    def test_missing_v8_resource_state_fails_closed(self):
        coordinator, channels = self._world()
        reservations, requests, handoffs, attempts = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
            handoff_ledger=handoffs,
            attempt_ledger=attempts,
        )
        checkpoint.pop("resource_state")
        self._redigest(checkpoint)
        with self.assertRaisesRegex(ValueError, "resource_state checkpoint is required"):
            restore_world_resource_checkpoint(checkpoint, channels=channels)

    def test_v8_restore_does_not_execute_attempt_or_handoff_again(self):
        coordinator, channels = self._world()
        reservations, requests, handoffs, attempts = self._resource_state()
        checkpoint = build_world_resource_checkpoint(
            coordinator,
            semantic_minute=20,
            reservation_ledger=reservations,
            request_ledger=requests,
            handoff_ledger=handoffs,
            attempt_ledger=attempts,
        )
        first = restore_world_resource_checkpoint(checkpoint, channels=channels)
        second = restore_world_resource_checkpoint(copy.deepcopy(checkpoint), channels=channels)
        self.assertEqual(first.handoff_ledger, handoffs)
        self.assertEqual(first.attempt_ledger, attempts)
        self.assertEqual(second.handoff_ledger, handoffs)
        self.assertEqual(second.attempt_ledger, attempts)
        self.assertEqual(len(second.handoff_ledger.transfers), 1)
        self.assertEqual(len(second.attempt_ledger.attempts), 1)


if __name__ == "__main__":
    unittest.main()
