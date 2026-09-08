import unittest

from tools.global_npc_resource_handoff_reschedule_admission import (
    RescheduleAdmissionState,
    assess_reschedule_resource_window,
)
from tools.global_npc_resource_handoff_rescheduling import (
    ResourceHandoffRescheduleLedger,
    ResourceHandoffRescheduleProposal,
)
from tools.global_npc_resource_handoffs import (
    HandoffMode,
    ResourceHandoffAuthorization,
    ResourceHandoffLedger,
)
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    ReservationState,
    ResourceReservation,
)


class GlobalNpcResourceHandoffRescheduleAdmissionTests(unittest.TestCase):
    def _handoffs(self):
        authorization = ResourceHandoffAuthorization(
            authorization_id="handoff:original",
            request_id="request:meter",
            provider_actor_id="provider",
            accountable_actor_id="requester",
            receiving_actor_id="courier",
            resource_id="meter:1",
            mode=HandoffMode.PICKUP,
            handoff_location_ref="repair-row",
            valid_from_tick=20,
            valid_until_tick=30,
            authority_ref="decision:accept",
        )
        return ResourceHandoffLedger(authorizations=(authorization,))

    def _reschedules(self, end_tick=50):
        proposal = ResourceHandoffRescheduleProposal(
            proposal_id="proposal:later",
            authorization_id="handoff:original",
            source_notice_id="notice:reschedule",
            proposer_actor_id="courier",
            responder_actor_id="provider",
            proposed_location_ref="south-counter",
            proposed_valid_from_tick=40,
            proposed_valid_until_tick=end_tick,
            created_tick=15,
        )
        return ResourceHandoffRescheduleLedger(proposals=(proposal,))

    def test_clear_when_no_reservation_overlaps(self):
        reservations = ReservationLedger((
            ResourceReservation("r:early", "meter:1", "other", 5, 10),
        ))
        assessment = assess_reschedule_resource_window(
            self._reschedules(), self._handoffs(), reservations, proposal_id="proposal:later"
        )
        self.assertTrue(assessment.admissible)
        self.assertEqual(assessment.state, RescheduleAdmissionState.CLEAR)

    def test_overlapping_unrelated_reservation_blocks_admission(self):
        reservations = ReservationLedger((
            ResourceReservation("r:conflict", "meter:1", "other", 45, 55, purpose_ref="survey:other"),
        ))
        assessment = assess_reschedule_resource_window(
            self._reschedules(), self._handoffs(), reservations, proposal_id="proposal:later"
        )
        self.assertFalse(assessment.admissible)
        self.assertEqual(assessment.state, RescheduleAdmissionState.CONFLICT)
        self.assertEqual(assessment.conflicting_reservation_ids, ("r:conflict",))

    def test_same_request_reservation_is_evidence_for_same_work_not_conflict(self):
        reservations = ReservationLedger((
            ResourceReservation("r:same", "meter:1", "requester", 40, 50, purpose_ref="request:meter"),
        ))
        assessment = assess_reschedule_resource_window(
            self._reschedules(), self._handoffs(), reservations, proposal_id="proposal:later"
        )
        self.assertTrue(assessment.admissible)
        self.assertEqual(assessment.matched_same_purpose_reservation_ids, ("r:same",))

    def test_cancelled_reservation_does_not_block(self):
        reservations = ReservationLedger((
            ResourceReservation(
                "r:cancelled", "meter:1", "other", 45, 55,
                state=ReservationState.CANCELLED, purpose_ref="survey:other"
            ),
        ))
        assessment = assess_reschedule_resource_window(
            self._reschedules(), self._handoffs(), reservations, proposal_id="proposal:later"
        )
        self.assertTrue(assessment.admissible)

    def test_other_resource_does_not_block(self):
        reservations = ReservationLedger((
            ResourceReservation("r:other", "meter:2", "other", 40, 50, purpose_ref="survey:other"),
        ))
        assessment = assess_reschedule_resource_window(
            self._reschedules(), self._handoffs(), reservations, proposal_id="proposal:later"
        )
        self.assertTrue(assessment.admissible)

    def test_unbounded_successor_window_fails_closed_for_conflict_screening(self):
        assessment = assess_reschedule_resource_window(
            self._reschedules(end_tick=None), self._handoffs(), ReservationLedger(), proposal_id="proposal:later"
        )
        self.assertFalse(assessment.admissible)
        self.assertEqual(assessment.state, RescheduleAdmissionState.UNBOUNDED_WINDOW)

    def test_conflict_ids_are_deterministic(self):
        reservations = ReservationLedger((
            ResourceReservation("r:z", "meter:1", "z", 42, 49, purpose_ref="z"),
            ResourceReservation("r:a", "meter:1", "a", 41, 48, purpose_ref="a"),
        ))
        assessment = assess_reschedule_resource_window(
            self._reschedules(), self._handoffs(), reservations, proposal_id="proposal:later"
        )
        self.assertEqual(assessment.conflicting_reservation_ids, ("r:a", "r:z"))


if __name__ == "__main__":
    unittest.main()
