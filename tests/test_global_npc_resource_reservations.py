import unittest

from tools.global_npc_resource_reservations import (
    ReservationLedger,
    ReservationState,
    ResourceReservation,
    cancel_reservation,
    checkout_reserved_resource,
    effective_state,
    project_reservations_onto_resources,
    release_reservation,
    reserve_resource,
    return_resource,
)
from tools.global_npc_resources import ResourceState, WorldResource


class GlobalNpcResourceReservationTests(unittest.TestCase):
    def reservation(self, reservation_id: str, actor_id: str, start: int, end: int):
        return ResourceReservation(
            reservation_id=reservation_id,
            resource_id="kit-1",
            actor_id=actor_id,
            start_tick=start,
            end_tick=end,
            purpose_ref="sample-run",
        )

    def resource(self):
        return WorldResource(
            resource_id="kit-1",
            capability_refs=frozenset({"FIELD_SAMPLE_KIT"}),
            location_ref="field-office",
        )

    def test_non_overlapping_reservations_are_allowed(self):
        first = reserve_resource(ReservationLedger(), self.reservation("r1", "nerea", 10, 20))
        second = reserve_resource(first.ledger, self.reservation("r2", "mara", 20, 30))
        self.assertTrue(first.accepted)
        self.assertTrue(second.accepted)
        self.assertEqual(tuple(r.reservation_id for r in second.ledger.reservations), ("r1", "r2"))

    def test_overlapping_reservation_is_rejected_without_mutating_ledger(self):
        first = reserve_resource(ReservationLedger(), self.reservation("r1", "nerea", 10, 20))
        second = reserve_resource(first.ledger, self.reservation("r2", "mara", 19, 30))
        self.assertFalse(second.accepted)
        self.assertEqual(second.reason_code, "RESOURCE_WINDOW_CONFLICT")
        self.assertEqual(second.conflicting_reservation_ids, ("r1",))
        self.assertEqual(second.ledger, first.ledger)

    def test_release_makes_window_bookable_again(self):
        first = reserve_resource(ReservationLedger(), self.reservation("r1", "nerea", 10, 20))
        released = release_reservation(first.ledger, "r1", "nerea")
        replacement = reserve_resource(released.ledger, self.reservation("r2", "mara", 12, 18))
        self.assertTrue(released.accepted)
        self.assertEqual(released.reservation.state, ReservationState.RELEASED)
        self.assertTrue(replacement.accepted)

    def test_only_reserving_actor_can_release_or_cancel(self):
        first = reserve_resource(ReservationLedger(), self.reservation("r1", "nerea", 10, 20))
        bad_release = release_reservation(first.ledger, "r1", "mara")
        self.assertFalse(bad_release.accepted)
        self.assertEqual(bad_release.reason_code, "RESERVATION_ACTOR_MISMATCH")
        cancelled = cancel_reservation(first.ledger, "r1", "nerea")
        self.assertTrue(cancelled.accepted)
        self.assertEqual(cancelled.reservation.state, ReservationState.CANCELLED)

    def test_expiry_is_derived_without_rewriting_history(self):
        reservation = self.reservation("r1", "nerea", 10, 20)
        self.assertEqual(effective_state(reservation, 9), "SCHEDULED")
        self.assertEqual(effective_state(reservation, 10), "ACTIVE")
        self.assertEqual(effective_state(reservation, 20), "EXPIRED")
        self.assertEqual(reservation.state, ReservationState.ACTIVE)

    def test_projection_marks_resource_reserved_only_inside_window(self):
        result = reserve_resource(ReservationLedger(), self.reservation("r1", "nerea", 10, 20))
        before = project_reservations_onto_resources((self.resource(),), result.ledger, 9)[0]
        during = project_reservations_onto_resources((self.resource(),), result.ledger, 12)[0]
        after = project_reservations_onto_resources((self.resource(),), result.ledger, 20)[0]
        self.assertEqual(before.state, ResourceState.AVAILABLE)
        self.assertIsNone(before.reserved_for_actor_id)
        self.assertEqual(during.state, ResourceState.RESERVED)
        self.assertEqual(during.reserved_for_actor_id, "nerea")
        self.assertEqual(after.state, ResourceState.AVAILABLE)

    def test_reservation_does_not_imply_checkout(self):
        result = reserve_resource(ReservationLedger(), self.reservation("r1", "nerea", 10, 20))
        projected = project_reservations_onto_resources((self.resource(),), result.ledger, 12)[0]
        self.assertIsNone(projected.holder_actor_id)
        checked_out = checkout_reserved_resource(self.resource(), result.ledger, "nerea", 12)
        self.assertEqual(checked_out.state, ResourceState.IN_USE)
        self.assertEqual(checked_out.holder_actor_id, "nerea")

    def test_checkout_fails_without_current_reservation(self):
        result = reserve_resource(ReservationLedger(), self.reservation("r1", "nerea", 10, 20))
        with self.assertRaises(ValueError):
            checkout_reserved_resource(self.resource(), result.ledger, "mara", 12)
        with self.assertRaises(ValueError):
            checkout_reserved_resource(self.resource(), result.ledger, "nerea", 20)

    def test_return_changes_holder_and_location_but_not_reservation_history(self):
        result = reserve_resource(ReservationLedger(), self.reservation("r1", "nerea", 10, 20))
        checked_out = checkout_reserved_resource(self.resource(), result.ledger, "nerea", 12)
        returned = return_resource(checked_out, "nerea", "field-office-locker")
        self.assertEqual(returned.state, ResourceState.AVAILABLE)
        self.assertIsNone(returned.holder_actor_id)
        self.assertEqual(returned.location_ref, "field-office-locker")
        self.assertEqual(result.ledger.reservations[0].state, ReservationState.ACTIVE)

    def test_duplicate_reservation_id_fails_closed(self):
        first = reserve_resource(ReservationLedger(), self.reservation("r1", "nerea", 10, 20))
        duplicate = reserve_resource(first.ledger, self.reservation("r1", "nerea", 30, 40))
        self.assertFalse(duplicate.accepted)
        self.assertEqual(duplicate.reason_code, "DUPLICATE_RESERVATION_ID")


if __name__ == "__main__":
    unittest.main()
