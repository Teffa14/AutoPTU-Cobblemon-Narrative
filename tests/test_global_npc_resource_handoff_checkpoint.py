import copy
import unittest

from tools.global_npc_resource_checkpoint import (
    RESOURCE_CHECKPOINT_HANDOFF_SCHEMA,
    restore_resource_state_with_handoffs,
    snapshot_resource_state,
    snapshot_resource_state_with_handoffs,
    validate_handoff_checkpoint_time,
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
from tools.global_npc_resource_reservations import ReservationLedger


class GlobalNpcResourceHandoffCheckpointTests(unittest.TestCase):
    def _state(self):
        requests = ResourceRequestLedger(
            requests=(
                ResourceRequest(
                    request_id="request:meter:nerea",
                    requester_actor_id="nerea",
                    provider_actor_id="teo",
                    resource_id="meter:field:7",
                    created_tick=12,
                    expires_at_tick=80,
                    purpose_ref="survey:ridge",
                ),
            ),
            events=(
                ResourceRequestEvent(
                    event_id="request-event:accepted",
                    request_id="request:meter:nerea",
                    actor_id="teo",
                    kind=ResourceRequestEventKind.ACCEPTED,
                    at_tick=18,
                    offered_resource_id="meter:field:7",
                    reason_ref="meter-ready",
                ),
            ),
        )
        authorization = ResourceHandoffAuthorization(
            authorization_id="handoff-auth:meter:nerea",
            request_id="request:meter:nerea",
            provider_actor_id="teo",
            accountable_actor_id="nerea",
            receiving_actor_id="ema",
            resource_id="meter:field:7",
            mode=HandoffMode.PICKUP,
            handoff_location_ref="puerto-bruma:repair-row",
            valid_from_tick=30,
            valid_until_tick=50,
            authority_ref="request-event:accepted",
        )
        transfer = ResourceCustodyTransfer(
            transfer_id="handoff-transfer:meter:nerea",
            authorization_id=authorization.authorization_id,
            request_id=authorization.request_id,
            resource_id=authorization.resource_id,
            from_actor_id="teo",
            to_actor_id="ema",
            accountable_actor_id="nerea",
            location_ref=authorization.handoff_location_ref,
            at_tick=35,
            condition_ref="condition:ready",
        )
        return ReservationLedger(), requests, ResourceHandoffLedger((authorization,), (transfer,))

    def test_round_trip_preserves_authorization_and_transfer_without_reexecution(self):
        reservations, requests, handoffs = self._state()
        snapshot = snapshot_resource_state_with_handoffs(reservations, requests, handoffs)
        self.assertEqual(snapshot["schema"], RESOURCE_CHECKPOINT_HANDOFF_SCHEMA)

        restored_reservations, restored_requests, restored_handoffs = restore_resource_state_with_handoffs(snapshot)
        self.assertEqual(restored_reservations, reservations)
        self.assertEqual(restored_requests, requests)
        self.assertEqual(restored_handoffs, handoffs)
        validate_handoff_checkpoint_time(restored_handoffs, semantic_minute=35)

    def test_v1_restore_produces_empty_handoff_history_instead_of_inference(self):
        reservations, requests, _ = self._state()
        snapshot = snapshot_resource_state(reservations, requests)
        restored_reservations, restored_requests, restored_handoffs = restore_resource_state_with_handoffs(snapshot)
        self.assertEqual(restored_reservations, reservations)
        self.assertEqual(restored_requests, requests)
        self.assertEqual(restored_handoffs, ResourceHandoffLedger())

    def test_orphan_authorization_fails_closed(self):
        reservations, requests, handoffs = self._state()
        snapshot = snapshot_resource_state_with_handoffs(reservations, requests, handoffs)
        snapshot["handoff_authorizations"][0]["request_id"] = "request:missing"
        with self.assertRaisesRegex(ValueError, "references missing request"):
            restore_resource_state_with_handoffs(snapshot)

    def test_provider_and_resource_must_match_accepted_request(self):
        reservations, requests, handoffs = self._state()
        snapshot = snapshot_resource_state_with_handoffs(reservations, requests, handoffs)
        snapshot["handoff_authorizations"][0]["provider_actor_id"] = "someone-else"
        with self.assertRaisesRegex(ValueError, "provider mismatches request"):
            restore_resource_state_with_handoffs(snapshot)

        snapshot = snapshot_resource_state_with_handoffs(reservations, requests, handoffs)
        snapshot["handoff_authorizations"][0]["resource_id"] = "meter:field:other"
        with self.assertRaisesRegex(ValueError, "resource mismatches accepted request"):
            restore_resource_state_with_handoffs(snapshot)

    def test_transfer_must_match_authorization_and_use_it_once(self):
        reservations, requests, handoffs = self._state()
        snapshot = snapshot_resource_state_with_handoffs(reservations, requests, handoffs)
        snapshot["custody_transfers"][0]["to_actor_id"] = "wrong-receiver"
        with self.assertRaisesRegex(ValueError, "mismatches authorization"):
            restore_resource_state_with_handoffs(snapshot)

        snapshot = snapshot_resource_state_with_handoffs(reservations, requests, handoffs)
        duplicate = copy.deepcopy(snapshot["custody_transfers"][0])
        duplicate["transfer_id"] = "handoff-transfer:second"
        snapshot["custody_transfers"].append(duplicate)
        with self.assertRaisesRegex(ValueError, "multiple custody transfers use one authorization"):
            restore_resource_state_with_handoffs(snapshot)

    def test_transfer_outside_authorized_window_fails_closed(self):
        reservations, requests, handoffs = self._state()
        snapshot = snapshot_resource_state_with_handoffs(reservations, requests, handoffs)
        snapshot["custody_transfers"][0]["at_tick"] = 50
        with self.assertRaisesRegex(ValueError, "after authorization expiry"):
            restore_resource_state_with_handoffs(snapshot)

    def test_completed_transfer_cannot_come_from_future(self):
        reservations, requests, handoffs = self._state()
        restored = restore_resource_state_with_handoffs(
            snapshot_resource_state_with_handoffs(reservations, requests, handoffs)
        )[2]
        with self.assertRaisesRegex(ValueError, "custody transfer comes from the future"):
            validate_handoff_checkpoint_time(restored, semantic_minute=34)

    def test_snapshot_order_is_deterministic(self):
        reservations, requests, handoffs = self._state()
        second = ResourceHandoffAuthorization(
            authorization_id="handoff-auth:future",
            request_id="request:meter:nerea",
            provider_actor_id="teo",
            accountable_actor_id="nerea",
            receiving_actor_id="ema",
            resource_id="meter:field:7",
            mode=HandoffMode.PICKUP,
            handoff_location_ref="puerto-bruma:repair-row",
            valid_from_tick=60,
            valid_until_tick=70,
        )
        forward = ResourceHandoffLedger((*handoffs.authorizations, second), handoffs.transfers)
        reverse = ResourceHandoffLedger(tuple(reversed(forward.authorizations)), handoffs.transfers)
        self.assertEqual(
            snapshot_resource_state_with_handoffs(reservations, requests, forward),
            snapshot_resource_state_with_handoffs(reservations, requests, reverse),
        )


if __name__ == "__main__":
    unittest.main()
