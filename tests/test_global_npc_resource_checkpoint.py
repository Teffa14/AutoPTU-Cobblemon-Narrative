import copy
import unittest

from tools.global_npc_resource_checkpoint import (
    RESOURCE_CHECKPOINT_SCHEMA,
    restore_resource_state,
    snapshot_resource_state,
    validate_resource_checkpoint_time,
)
from tools.global_npc_resource_requests import (
    ResourceRequest,
    ResourceRequestEvent,
    ResourceRequestEventKind,
    ResourceRequestLedger,
)
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    ReservationState,
    ResourceReservation,
)


class GlobalNpcResourceCheckpointTests(unittest.TestCase):
    def _state(self):
        reservations = ReservationLedger(
            (
                ResourceReservation(
                    reservation_id="reservation:meter:ema",
                    resource_id="meter:field:7",
                    actor_id="ema",
                    start_tick=40,
                    end_tick=90,
                    state=ReservationState.ACTIVE,
                    purpose_ref="survey:ridge",
                ),
            )
        )
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
                    event_id="request-event:meter:accepted",
                    request_id="request:meter:nerea",
                    actor_id="teo",
                    kind=ResourceRequestEventKind.ACCEPTED,
                    at_tick=18,
                    offered_resource_id="meter:field:7",
                    reason_ref="meter-ready",
                ),
            ),
        )
        return reservations, requests

    def test_round_trip_preserves_reservation_and_request_history(self):
        reservations, requests = self._state()
        snapshot = snapshot_resource_state(reservations, requests)
        self.assertEqual(snapshot["schema"], RESOURCE_CHECKPOINT_SCHEMA)

        restored_reservations, restored_requests = restore_resource_state(snapshot)
        self.assertEqual(restored_reservations, reservations)
        self.assertEqual(restored_requests, requests)
        validate_resource_checkpoint_time(restored_requests, semantic_minute=20)

    def test_snapshot_is_deterministic_even_if_input_order_differs(self):
        reservations, requests = self._state()
        second_reservation = ResourceReservation(
            reservation_id="reservation:meter:later",
            resource_id="meter:field:8",
            actor_id="teo",
            start_tick=100,
            end_tick=120,
        )
        forward = ReservationLedger((*reservations.reservations, second_reservation))
        reverse = ReservationLedger(tuple(reversed(forward.reservations)))
        self.assertEqual(
            snapshot_resource_state(forward, requests),
            snapshot_resource_state(reverse, requests),
        )

    def test_orphan_request_event_fails_closed(self):
        reservations, requests = self._state()
        snapshot = snapshot_resource_state(reservations, requests)
        snapshot["request_events"][0]["request_id"] = "request:missing"
        with self.assertRaisesRegex(ValueError, "references missing request"):
            restore_resource_state(snapshot)

    def test_nonparticipant_request_event_fails_closed(self):
        reservations, requests = self._state()
        snapshot = snapshot_resource_state(reservations, requests)
        snapshot["request_events"][0]["actor_id"] = "bystander"
        with self.assertRaisesRegex(ValueError, "not a participant"):
            restore_resource_state(snapshot)

    def test_future_request_or_event_fails_closed_against_checkpoint_time(self):
        reservations, requests = self._state()
        restored_reservations, restored_requests = restore_resource_state(
            snapshot_resource_state(reservations, requests)
        )
        self.assertEqual(restored_reservations, reservations)
        with self.assertRaisesRegex(ValueError, "event comes from the future"):
            validate_resource_checkpoint_time(restored_requests, semantic_minute=17)

    def test_duplicate_identity_fails_closed(self):
        reservations, requests = self._state()
        snapshot = snapshot_resource_state(reservations, requests)
        snapshot["reservations"].append(copy.deepcopy(snapshot["reservations"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate reservation IDs"):
            restore_resource_state(snapshot)

    def test_unknown_schema_fails_closed(self):
        reservations, requests = self._state()
        snapshot = snapshot_resource_state(reservations, requests)
        snapshot["schema"] = "UNKNOWN"
        with self.assertRaisesRegex(ValueError, "unsupported resource checkpoint schema"):
            restore_resource_state(snapshot)


if __name__ == "__main__":
    unittest.main()
