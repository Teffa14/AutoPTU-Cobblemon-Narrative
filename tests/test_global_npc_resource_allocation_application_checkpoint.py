import copy
import unittest

from tools.global_npc_resource_allocation_application import (
    ResourceAllocationApplicationLedger,
    apply_allocation_resolution,
)
from tools.global_npc_resource_allocation_application_checkpoint import (
    RESOURCE_CHECKPOINT_ALLOCATION_APPLICATION_SCHEMA,
    restore_resource_state_with_allocation_applications,
    snapshot_resource_state_with_allocation_applications,
    validate_allocation_application_checkpoint_time,
)
from tools.global_npc_resource_allocation_checkpoint import snapshot_resource_state_with_allocations
from tools.global_npc_resource_allocation_resolution import (
    AllocationAuthorityEvidence,
    AllocationAuthorityState,
    AllocationResolutionKind,
    ResourceAllocationResolutionLedger,
    record_allocation_resolution,
)
from tools.global_npc_resource_handoff_appointments import (
    HandoffAppointmentNoticeKind,
    ResourceHandoffAppointmentLedger,
    ResourceHandoffAppointmentNotice,
)
from tools.global_npc_resource_handoff_attempts import ResourceHandoffAttemptLedger
from tools.global_npc_resource_handoff_reschedule_admission import (
    RescheduleAdmissionAssessment,
    RescheduleAdmissionState,
)
from tools.global_npc_resource_handoff_reschedule_admission_history import (
    ResourceRescheduleAdmissionLedger,
    record_reschedule_admission,
)
from tools.global_npc_resource_handoff_rescheduling import (
    HandoffRescheduleDecisionKind,
    ResourceHandoffAuthorizationReplacement,
    ResourceHandoffRescheduleDecision,
    ResourceHandoffRescheduleLedger,
    ResourceHandoffRescheduleProposal,
)
from tools.global_npc_resource_handoffs import (
    HandoffMode,
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


class GlobalNpcResourceAllocationApplicationCheckpointTests(unittest.TestCase):
    def _state(self):
        reservations = ReservationLedger((
            ResourceReservation("reservation:other", "meter:field:7", "ori", 95, 110, purpose_ref="survey:marsh"),
        ))
        requests = ResourceRequestLedger(
            requests=(ResourceRequest("request:meter:nerea", "nerea", "teo", "meter:field:7", 12, 150, purpose_ref="survey:ridge"),),
            events=(ResourceRequestEvent("request-event:accepted", "request:meter:nerea", "teo", ResourceRequestEventKind.ACCEPTED, 18, offered_resource_id="meter:field:7"),),
        )
        old = ResourceHandoffAuthorization("auth:old", "request:meter:nerea", "teo", "nerea", "ema", "meter:field:7", HandoffMode.PICKUP, "place:repair-row", 30, 70, "request-event:accepted")
        new = ResourceHandoffAuthorization("auth:new", old.request_id, old.provider_actor_id, old.accountable_actor_id, old.receiving_actor_id, old.resource_id, old.mode, "place:field-office", 90, 120, "decision:accept")
        notice = ResourceHandoffAppointmentNotice("notice:reschedule", "auth:old", "ema", "teo", HandoffAppointmentNoticeKind.RESCHEDULE_REQUEST, "claim:reschedule", "delivery:reschedule", 40)
        proposal = ResourceHandoffRescheduleProposal("proposal:later", "auth:old", "notice:reschedule", "ema", "teo", "place:field-office", 90, 120, 40)
        decision = ResourceHandoffRescheduleDecision("decision:accept", "proposal:later", "teo", HandoffRescheduleDecisionKind.ACCEPT, 46)
        replacement = ResourceHandoffAuthorizationReplacement("replacement:1", "proposal:later", "decision:accept", "auth:old", "auth:new", 46)
        reschedules = ResourceHandoffRescheduleLedger((proposal,), (decision,), (replacement,))
        assessment = RescheduleAdmissionAssessment(RescheduleAdmissionState.CONFLICT, "proposal:later", resource_id="meter:field:7", conflicting_reservation_ids=("reservation:other",))
        admissions = record_reschedule_admission(ResourceRescheduleAdmissionLedger(), assessment, record_id="admission:1", assessed_tick=44)
        authority = AllocationAuthorityEvidence("authority:allocator", "scheduler", "ALLOCATE_RESOURCE_WINDOW", "meter:field:7", AllocationAuthorityState.AUTHORIZED, 43, 80)
        resolved = record_allocation_resolution(
            ResourceAllocationResolutionLedger(),
            assessment,
            authority,
            resolution_id="resolution:1",
            decision_actor_id="scheduler",
            resolution_kind=AllocationResolutionKind.SELECT_PROPOSED_WINDOW,
            decided_tick=45,
            basis_refs=("policy:scarce-equipment",),
        )
        self.assertTrue(resolved.accepted)
        applied = apply_allocation_resolution(
            ResourceAllocationApplicationLedger(),
            reservations,
            resolved.resolution,
            application_id="application:1",
            applied_tick=47,
            basis_refs=("work-order:allocation",),
        )
        self.assertTrue(applied.accepted)
        return (
            reservations,
            requests,
            ResourceHandoffLedger((new, old), ()),
            ResourceHandoffAttemptLedger(),
            ResourceHandoffAppointmentLedger((notice,)),
            reschedules,
            admissions,
            (authority,),
            resolved.ledger,
            applied.ledger,
        )

    def test_round_trip_preserves_allocation_application(self):
        state = self._state()
        snapshot = snapshot_resource_state_with_allocation_applications(*state)
        self.assertEqual(snapshot["schema"], RESOURCE_CHECKPOINT_ALLOCATION_APPLICATION_SCHEMA)
        self.assertEqual(restore_resource_state_with_allocation_applications(snapshot), state)

    def test_v7_restore_does_not_infer_application(self):
        state = self._state()
        snapshot = snapshot_resource_state_with_allocations(*state[:9])
        restored = restore_resource_state_with_allocation_applications(snapshot)
        self.assertEqual(restored[:9], state[:9])
        self.assertEqual(restored[9], ResourceAllocationApplicationLedger())

    def test_application_requires_persisted_resolution(self):
        snapshot = snapshot_resource_state_with_allocation_applications(*self._state())
        snapshot["allocation_resolutions"] = []
        with self.assertRaisesRegex(ValueError, "missing resolution"):
            restore_resource_state_with_allocation_applications(snapshot)

    def test_application_kind_must_match_resolution(self):
        snapshot = snapshot_resource_state_with_allocation_applications(*self._state())
        snapshot["allocation_applications"][0]["application_kind"] = "DEFER_NO_CHANGE"
        snapshot["allocation_applications"][0]["displaced_reservation_ids"] = []
        with self.assertRaisesRegex(ValueError, "kind contradicts resolution"):
            restore_resource_state_with_allocation_applications(snapshot)

    def test_displacement_set_must_match_decision_conflicts(self):
        snapshot = snapshot_resource_state_with_allocation_applications(*self._state())
        snapshot["allocation_applications"][0]["displaced_reservation_ids"] = []
        with self.assertRaisesRegex(ValueError, "displacement set contradicts resolution"):
            restore_resource_state_with_allocation_applications(snapshot)

    def test_same_resolution_cannot_have_two_persisted_applications(self):
        snapshot = snapshot_resource_state_with_allocation_applications(*self._state())
        duplicate = copy.deepcopy(snapshot["allocation_applications"][0])
        duplicate["application_id"] = "application:2"
        snapshot["allocation_applications"].append(duplicate)
        with self.assertRaisesRegex(ValueError, "resolution more than once"):
            restore_resource_state_with_allocation_applications(snapshot)

    def test_future_application_fails_time_validation(self):
        state = self._state()
        with self.assertRaisesRegex(ValueError, "application comes from the future"):
            validate_allocation_application_checkpoint_time(state[9], semantic_minute=46)

    def test_closed_current_reservation_does_not_erase_historical_application(self):
        state = self._state()
        closed = ResourceReservation(
            "reservation:other",
            "meter:field:7",
            "ori",
            95,
            110,
            state=__import__("tools.global_npc_resource_reservations", fromlist=["ReservationState"]).ReservationState.CANCELLED,
            purpose_ref="survey:marsh",
        )
        modified = (ReservationLedger((closed,)), *state[1:])
        snapshot = snapshot_resource_state_with_allocation_applications(*modified)
        restored = restore_resource_state_with_allocation_applications(snapshot)
        self.assertEqual(restored[9], state[9])


if __name__ == "__main__":
    unittest.main()
