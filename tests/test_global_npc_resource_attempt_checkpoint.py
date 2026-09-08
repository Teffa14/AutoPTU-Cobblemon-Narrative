import copy
import unittest

from tools.global_npc_resource_attempt_checkpoint import (
    RESOURCE_CHECKPOINT_ATTEMPT_SCHEMA,
    restore_resource_state_with_attempts,
    snapshot_resource_state_with_attempts,
    validate_attempt_checkpoint_time,
)
from tools.global_npc_resource_checkpoint import snapshot_resource_state_with_handoffs
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
from tools.global_npc_resource_reservations import ReservationLedger


class GlobalNpcResourceAttemptCheckpointTests(unittest.TestCase):
    def _state(self, *, with_transfer=False, outcome=HandoffAttemptOutcome.PROVIDER_ABSENT):
        requests = ResourceRequestLedger(
            requests=(
                ResourceRequest(
                    request_id="request:meter:nerea",
                    requester_actor_id="nerea",
                    provider_actor_id="teo",
                    resource_id="meter:field:7",
                    created_tick=12,
                    expires_at_tick=90,
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
            valid_until_tick=60,
            authority_ref="request-event:accepted",
        )
        transfers = ()
        if with_transfer:
            transfers = (
                ResourceCustodyTransfer(
                    transfer_id="handoff-transfer:meter:nerea",
                    authorization_id=authorization.authorization_id,
                    request_id=authorization.request_id,
                    resource_id=authorization.resource_id,
                    from_actor_id="teo",
                    to_actor_id="ema",
                    accountable_actor_id="nerea",
                    location_ref=authorization.handoff_location_ref,
                    at_tick=50,
                    condition_ref="condition:ready",
                ),
            )
        actor_id = "teo" if outcome == HandoffAttemptOutcome.PROVIDER_REFUSED else "ema"
        attempt = ResourceHandoffAttempt(
            attempt_id="handoff-attempt:meter:1",
            authorization_id=authorization.authorization_id,
            actor_id=actor_id,
            location_ref=authorization.handoff_location_ref,
            at_tick=40,
            outcome=outcome,
            observation_ref="observation:desk-empty",
        )
        return (
            ReservationLedger(),
            requests,
            ResourceHandoffLedger((authorization,), transfers),
            ResourceHandoffAttemptLedger((attempt,)),
        )

    def test_round_trip_preserves_failed_attempt_without_inventing_transfer(self):
        reservations, requests, handoffs, attempts = self._state()
        snapshot = snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        self.assertEqual(snapshot["schema"], RESOURCE_CHECKPOINT_ATTEMPT_SCHEMA)

        restored = restore_resource_state_with_attempts(snapshot)
        self.assertEqual(restored, (reservations, requests, handoffs, attempts))
        self.assertEqual(restored[2].transfers, ())
        validate_attempt_checkpoint_time(restored[3], semantic_minute=40)

    def test_v2_restore_has_empty_attempt_history_instead_of_inference(self):
        reservations, requests, handoffs, _ = self._state()
        snapshot = snapshot_resource_state_with_handoffs(reservations, requests, handoffs)
        restored = restore_resource_state_with_attempts(snapshot)
        self.assertEqual(restored[:3], (reservations, requests, handoffs))
        self.assertEqual(restored[3], ResourceHandoffAttemptLedger())

    def test_missing_authorization_fails_closed(self):
        reservations, requests, handoffs, attempts = self._state()
        snapshot = snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        snapshot["handoff_attempts"][0]["authorization_id"] = "handoff-auth:missing"
        with self.assertRaisesRegex(ValueError, "references missing authorization"):
            restore_resource_state_with_attempts(snapshot)

    def test_attempt_must_match_location_window_and_participant(self):
        reservations, requests, handoffs, attempts = self._state()

        snapshot = snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        snapshot["handoff_attempts"][0]["location_ref"] = "place:wrong"
        with self.assertRaisesRegex(ValueError, "location mismatches"):
            restore_resource_state_with_attempts(snapshot)

        snapshot = snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        snapshot["handoff_attempts"][0]["at_tick"] = 60
        with self.assertRaisesRegex(ValueError, "after authorization expiry"):
            restore_resource_state_with_attempts(snapshot)

        snapshot = snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        snapshot["handoff_attempts"][0]["actor_id"] = "npc:bystander"
        with self.assertRaisesRegex(ValueError, "authorized participant"):
            restore_resource_state_with_attempts(snapshot)

    def test_refusal_role_is_preserved_across_restore(self):
        reservations, requests, handoffs, attempts = self._state(outcome=HandoffAttemptOutcome.PROVIDER_REFUSED)
        snapshot = snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        snapshot["handoff_attempts"][0]["actor_id"] = "ema"
        with self.assertRaisesRegex(ValueError, "provider refusal attributed to wrong actor"):
            restore_resource_state_with_attempts(snapshot)

    def test_failed_attempt_can_precede_later_success_but_not_follow_it(self):
        reservations, requests, handoffs, attempts = self._state(with_transfer=True)
        restored = restore_resource_state_with_attempts(
            snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        )
        self.assertEqual(restored[2], handoffs)
        self.assertEqual(restored[3], attempts)

        snapshot = snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        snapshot["handoff_attempts"][0]["at_tick"] = 55
        with self.assertRaisesRegex(ValueError, "after completed transfer"):
            restore_resource_state_with_attempts(snapshot)

    def test_terminal_refusal_cannot_be_followed_by_transfer_under_same_authorization(self):
        reservations, requests, handoffs, attempts = self._state(
            with_transfer=True,
            outcome=HandoffAttemptOutcome.PROVIDER_REFUSED,
        )
        snapshot = snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        with self.assertRaisesRegex(ValueError, "transfer follows terminal refusal"):
            restore_resource_state_with_attempts(snapshot)

    def test_duplicate_attempt_ids_and_future_attempts_fail_closed(self):
        reservations, requests, handoffs, attempts = self._state()
        snapshot = snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        duplicate = copy.deepcopy(snapshot["handoff_attempts"][0])
        snapshot["handoff_attempts"].append(duplicate)
        with self.assertRaisesRegex(ValueError, "duplicate handoff attempt IDs"):
            restore_resource_state_with_attempts(snapshot)

        restored_attempts = restore_resource_state_with_attempts(
            snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        )[3]
        with self.assertRaisesRegex(ValueError, "handoff attempt comes from the future"):
            validate_attempt_checkpoint_time(restored_attempts, semantic_minute=39)

    def test_snapshot_order_is_deterministic(self):
        reservations, requests, handoffs, attempts = self._state()
        later = ResourceHandoffAttempt(
            attempt_id="handoff-attempt:meter:z",
            authorization_id="handoff-auth:meter:nerea",
            actor_id="ema",
            location_ref="puerto-bruma:repair-row",
            at_tick=45,
            outcome=HandoffAttemptOutcome.RESOURCE_ABSENT,
        )
        forward = ResourceHandoffAttemptLedger((*attempts.attempts, later))
        reverse = ResourceHandoffAttemptLedger(tuple(reversed(forward.attempts)))
        self.assertEqual(
            snapshot_resource_state_with_attempts(reservations, requests, handoffs, forward),
            snapshot_resource_state_with_attempts(reservations, requests, handoffs, reverse),
        )


if __name__ == "__main__":
    unittest.main()
