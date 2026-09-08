import copy
import unittest

from tools.global_npc_resource_appointment_checkpoint import (
    RESOURCE_CHECKPOINT_APPOINTMENT_SCHEMA,
    restore_resource_state_with_appointment_notices,
    snapshot_resource_state_with_appointment_notices,
    validate_appointment_checkpoint_time,
)
from tools.global_npc_resource_attempt_checkpoint import snapshot_resource_state_with_attempts
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffAppointmentNotice,
)
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


class GlobalNpcResourceAppointmentCheckpointTests(unittest.TestCase):
    def _state(self, *, with_transfer=False):
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
            valid_until_tick=70,
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
        attempt = ResourceHandoffAttempt(
            attempt_id="handoff-attempt:meter:1",
            authorization_id=authorization.authorization_id,
            actor_id="ema",
            location_ref=authorization.handoff_location_ref,
            at_tick=40,
            outcome=HandoffAttemptOutcome.PROVIDER_ABSENT,
            observation_ref="observation:desk-empty",
        )
        notice = ResourceHandoffAppointmentNotice(
            notice_id="appointment-notice:meter:confirm",
            authorization_id=authorization.authorization_id,
            sender_actor_id="teo",
            receiver_actor_id="ema",
            kind=HandoffAppointmentNoticeKind.CONFIRM,
            source_claim_id="claim:meter:confirm",
            communication_event_id="delivery:meter:confirm",
            created_tick=25,
            reason_ref="schedule:pickup-window",
        )
        return (
            ReservationLedger(),
            requests,
            ResourceHandoffLedger((authorization,), transfers),
            ResourceHandoffAttemptLedger((attempt,)),
            ResourceHandoffAppointmentLedger((notice,)),
        )

    def test_round_trip_preserves_authored_notice_without_inventing_delivery(self):
        state = self._state()
        snapshot = snapshot_resource_state_with_appointment_notices(*state)
        self.assertEqual(snapshot["schema"], RESOURCE_CHECKPOINT_APPOINTMENT_SCHEMA)

        restored = restore_resource_state_with_appointment_notices(snapshot)
        self.assertEqual(restored, state)
        self.assertNotIn("delivery_status", snapshot["handoff_appointment_notices"][0])
        validate_appointment_checkpoint_time(restored[4], semantic_minute=25)

    def test_v3_restore_has_empty_appointment_history_instead_of_inference(self):
        reservations, requests, handoffs, attempts, _ = self._state()
        snapshot = snapshot_resource_state_with_attempts(reservations, requests, handoffs, attempts)
        restored = restore_resource_state_with_appointment_notices(snapshot)
        self.assertEqual(restored[:4], (reservations, requests, handoffs, attempts))
        self.assertEqual(restored[4], ResourceHandoffAppointmentLedger())

    def test_missing_authorization_fails_closed(self):
        snapshot = snapshot_resource_state_with_appointment_notices(*self._state())
        snapshot["handoff_appointment_notices"][0]["authorization_id"] = "handoff-auth:missing"
        with self.assertRaisesRegex(ValueError, "references missing authorization"):
            restore_resource_state_with_appointment_notices(snapshot)

    def test_notice_actors_must_be_authorization_participants(self):
        snapshot = snapshot_resource_state_with_appointment_notices(*self._state())
        snapshot["handoff_appointment_notices"][0]["receiver_actor_id"] = "npc:bystander"
        with self.assertRaisesRegex(ValueError, "authorization participants"):
            restore_resource_state_with_appointment_notices(snapshot)

    def test_notice_may_confirm_a_future_window_but_not_outlive_authorization(self):
        restored = restore_resource_state_with_appointment_notices(
            snapshot_resource_state_with_appointment_notices(*self._state())
        )
        self.assertEqual(restored[4].notices[0].created_tick, 25)
        self.assertEqual(restored[2].authorizations[0].valid_from_tick, 30)

        snapshot = snapshot_resource_state_with_appointment_notices(*self._state())
        snapshot["handoff_appointment_notices"][0]["created_tick"] = 70
        with self.assertRaisesRegex(ValueError, "after authorization expiry"):
            restore_resource_state_with_appointment_notices(snapshot)

    def test_historical_notice_can_precede_transfer_but_not_follow_it(self):
        restored = restore_resource_state_with_appointment_notices(
            snapshot_resource_state_with_appointment_notices(*self._state(with_transfer=True))
        )
        self.assertEqual(restored[2].transfers[0].at_tick, 50)
        self.assertEqual(restored[4].notices[0].created_tick, 25)

        snapshot = snapshot_resource_state_with_appointment_notices(*self._state(with_transfer=True))
        snapshot["handoff_appointment_notices"][0]["created_tick"] = 50
        with self.assertRaisesRegex(ValueError, "after completed transfer"):
            restore_resource_state_with_appointment_notices(snapshot)

    def test_duplicate_notice_and_communication_event_ids_fail_closed(self):
        snapshot = snapshot_resource_state_with_appointment_notices(*self._state())
        duplicate = copy.deepcopy(snapshot["handoff_appointment_notices"][0])
        snapshot["handoff_appointment_notices"].append(duplicate)
        with self.assertRaisesRegex(ValueError, "duplicate handoff appointment notice IDs"):
            restore_resource_state_with_appointment_notices(snapshot)

        snapshot = snapshot_resource_state_with_appointment_notices(*self._state())
        duplicate = copy.deepcopy(snapshot["handoff_appointment_notices"][0])
        duplicate["notice_id"] = "appointment-notice:meter:second"
        snapshot["handoff_appointment_notices"].append(duplicate)
        with self.assertRaisesRegex(ValueError, "duplicate handoff appointment communication event IDs"):
            restore_resource_state_with_appointment_notices(snapshot)

    def test_authored_notice_cannot_come_from_future(self):
        restored = restore_resource_state_with_appointment_notices(
            snapshot_resource_state_with_appointment_notices(*self._state())
        )[4]
        with self.assertRaisesRegex(ValueError, "handoff appointment notice comes from the future"):
            validate_appointment_checkpoint_time(restored, semantic_minute=24)

    def test_snapshot_order_is_deterministic(self):
        reservations, requests, handoffs, attempts, appointments = self._state()
        later = ResourceHandoffAppointmentNotice(
            notice_id="appointment-notice:meter:z",
            authorization_id="handoff-auth:meter:nerea",
            sender_actor_id="ema",
            receiver_actor_id="teo",
            kind=HandoffAppointmentNoticeKind.CONFIRM,
            source_claim_id="claim:meter:z",
            communication_event_id="delivery:meter:z",
            created_tick=26,
        )
        forward = ResourceHandoffAppointmentLedger((*appointments.notices, later))
        reverse = ResourceHandoffAppointmentLedger(tuple(reversed(forward.notices)))
        self.assertEqual(
            snapshot_resource_state_with_appointment_notices(reservations, requests, handoffs, attempts, forward),
            snapshot_resource_state_with_appointment_notices(reservations, requests, handoffs, attempts, reverse),
        )


if __name__ == "__main__":
    unittest.main()
