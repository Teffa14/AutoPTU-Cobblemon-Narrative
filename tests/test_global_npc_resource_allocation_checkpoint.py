import copy
import unittest

from tools.global_npc_resource_admission_checkpoint import snapshot_resource_state_with_admissions
from tools.global_npc_resource_allocation_checkpoint import (
    RESOURCE_CHECKPOINT_ALLOCATION_SCHEMA,
    restore_resource_state_with_allocations,
    snapshot_resource_state_with_allocations,
    validate_allocation_checkpoint_time,
)
from tools.global_npc_resource_allocation_resolution import (
    AllocationAuthorityEvidence, AllocationAuthorityState, AllocationResolutionKind,
    ResourceAllocationResolutionLedger, record_allocation_resolution,
)
from tools.global_npc_resource_handoff_appointments import HandoffAppointmentNoticeKind, ResourceHandoffAppointmentLedger, ResourceHandoffAppointmentNotice
from tools.global_npc_resource_handoff_attempts import ResourceHandoffAttemptLedger
from tools.global_npc_resource_handoff_reschedule_admission import RescheduleAdmissionAssessment, RescheduleAdmissionState
from tools.global_npc_resource_handoff_reschedule_admission_history import ResourceRescheduleAdmissionLedger, record_reschedule_admission
from tools.global_npc_resource_handoff_rescheduling import HandoffRescheduleDecisionKind, ResourceHandoffAuthorizationReplacement, ResourceHandoffRescheduleDecision, ResourceHandoffRescheduleLedger, ResourceHandoffRescheduleProposal
from tools.global_npc_resource_handoffs import HandoffMode, ResourceHandoffAuthorization, ResourceHandoffLedger
from tools.global_npc_resource_requests import ResourceRequest, ResourceRequestEvent, ResourceRequestEventKind, ResourceRequestLedger
from tools.global_npc_resource_reservations import ReservationLedger, ResourceReservation


class GlobalNpcResourceAllocationCheckpointTests(unittest.TestCase):
    def _state(self):
        reservations = ReservationLedger((ResourceReservation("reservation:other", "meter:field:7", "ori", 95, 110, purpose_ref="survey:marsh"),))
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
        result = record_allocation_resolution(ResourceAllocationResolutionLedger(), assessment, authority, resolution_id="resolution:1", decision_actor_id="scheduler", resolution_kind=AllocationResolutionKind.SELECT_PROPOSED_WINDOW, decided_tick=45, basis_refs=("policy:scarce-equipment",))
        self.assertTrue(result.accepted)
        return (reservations, requests, ResourceHandoffLedger((new, old), ()), ResourceHandoffAttemptLedger(), ResourceHandoffAppointmentLedger((notice,)), reschedules, admissions, (authority,), result.ledger)

    def test_round_trip_preserves_authority_and_decision(self):
        state = self._state()
        snapshot = snapshot_resource_state_with_allocations(*state)
        self.assertEqual(snapshot["schema"], RESOURCE_CHECKPOINT_ALLOCATION_SCHEMA)
        self.assertEqual(restore_resource_state_with_allocations(snapshot), state)

    def test_v6_restore_does_not_infer_allocation_decision(self):
        state = self._state()
        snapshot = snapshot_resource_state_with_admissions(*state[:7])
        restored = restore_resource_state_with_allocations(snapshot)
        self.assertEqual(restored[:7], state[:7])
        self.assertEqual(restored[7], ())
        self.assertEqual(restored[8], ResourceAllocationResolutionLedger())

    def test_resolution_requires_matching_historical_conflict_set(self):
        snapshot = snapshot_resource_state_with_allocations(*self._state())
        snapshot["allocation_resolutions"][0]["conflicting_reservation_ids"] = []
        with self.assertRaisesRegex(ValueError, "matching historical conflict admission"):
            restore_resource_state_with_allocations(snapshot)

    def test_resolution_requires_persisted_authority_evidence(self):
        snapshot = snapshot_resource_state_with_allocations(*self._state())
        snapshot["allocation_authority_evidence"] = []
        with self.assertRaisesRegex(ValueError, "missing authority evidence"):
            restore_resource_state_with_allocations(snapshot)

    def test_authority_scope_cannot_be_rewritten(self):
        snapshot = snapshot_resource_state_with_allocations(*self._state())
        snapshot["allocation_authority_evidence"][0]["target_resource_id"] = "meter:other"
        with self.assertRaisesRegex(ValueError, "authority resource mismatch"):
            restore_resource_state_with_allocations(snapshot)

    def test_future_decision_fails_time_validation(self):
        state = self._state()
        with self.assertRaisesRegex(ValueError, "resolution comes from the future"):
            validate_allocation_checkpoint_time(state[7], state[8], semantic_minute=44)

    def test_duplicate_resolution_id_fails_closed(self):
        snapshot = snapshot_resource_state_with_allocations(*self._state())
        snapshot["allocation_resolutions"].append(copy.deepcopy(snapshot["allocation_resolutions"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate allocation resolution IDs"):
            restore_resource_state_with_allocations(snapshot)


if __name__ == "__main__":
    unittest.main()
