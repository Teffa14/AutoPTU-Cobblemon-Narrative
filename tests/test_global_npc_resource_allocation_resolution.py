import unittest

from tools.global_npc_resource_allocation_resolution import (
    AllocationAuthorityEvidence,
    AllocationAuthorityState,
    AllocationResolutionKind,
    ResourceAllocationResolutionLedger,
    record_allocation_resolution,
)
from tools.global_npc_resource_handoff_reschedule_admission import (
    RescheduleAdmissionAssessment,
    RescheduleAdmissionState,
)


class GlobalNpcResourceAllocationResolutionTests(unittest.TestCase):
    def _assessment(self):
        return RescheduleAdmissionAssessment(
            state=RescheduleAdmissionState.CONFLICT,
            proposal_id="proposal:later",
            resource_id="meter:1",
            conflicting_reservation_ids=("r:z", "r:a"),
        )

    def _authority(self, **overrides):
        data = dict(
            authority_check_id="authority:1",
            actor_id="allocator",
            action_ref="ALLOCATE_RESOURCE_WINDOW",
            target_resource_id="meter:1",
            state=AllocationAuthorityState.AUTHORIZED,
            checked_tick=20,
            valid_until_tick=60,
        )
        data.update(overrides)
        return AllocationAuthorityEvidence(**data)

    def test_authorized_actor_can_select_proposed_window_without_mutating_reservations(self):
        result = record_allocation_resolution(
            ResourceAllocationResolutionLedger(),
            self._assessment(),
            self._authority(),
            resolution_id="resolution:1",
            decision_actor_id="allocator",
            resolution_kind=AllocationResolutionKind.SELECT_PROPOSED_WINDOW,
            decided_tick=30,
            basis_refs=("policy:field-priority", "evidence:deadline"),
        )
        self.assertTrue(result.accepted)
        self.assertEqual(result.resolution.resource_id, "meter:1")
        self.assertEqual(result.resolution.conflicting_reservation_ids, ("r:a", "r:z"))
        self.assertIsNone(result.resolution.selected_reservation_id)

    def test_authorized_actor_can_select_one_existing_conflicting_reservation(self):
        result = record_allocation_resolution(
            ResourceAllocationResolutionLedger(),
            self._assessment(),
            self._authority(),
            resolution_id="resolution:2",
            decision_actor_id="allocator",
            resolution_kind=AllocationResolutionKind.SELECT_EXISTING_RESERVATION,
            selected_reservation_id="r:z",
            decided_tick=30,
        )
        self.assertTrue(result.accepted)
        self.assertEqual(result.resolution.selected_reservation_id, "r:z")

    def test_non_conflict_cannot_be_arbitrated_by_this_layer(self):
        clear = RescheduleAdmissionAssessment(
            RescheduleAdmissionState.CLEAR, "proposal:clear", resource_id="meter:1"
        )
        result = record_allocation_resolution(
            ResourceAllocationResolutionLedger(), clear, self._authority(),
            resolution_id="resolution:3", decision_actor_id="allocator",
            resolution_kind=AllocationResolutionKind.DEFER, decided_tick=30,
        )
        self.assertFalse(result.accepted)
        self.assertEqual(result.reason_code, "NO_RESOURCE_CONFLICT_TO_RESOLVE")

    def test_authority_must_be_explicit_and_current(self):
        unauthorized = record_allocation_resolution(
            ResourceAllocationResolutionLedger(), self._assessment(),
            self._authority(state=AllocationAuthorityState.NEEDS_VERIFICATION),
            resolution_id="resolution:4", decision_actor_id="allocator",
            resolution_kind=AllocationResolutionKind.DEFER, decided_tick=30,
        )
        self.assertFalse(unauthorized.accepted)
        self.assertEqual(unauthorized.reason_code, "ALLOCATION_AUTHORITY_NOT_ESTABLISHED")

        expired = record_allocation_resolution(
            ResourceAllocationResolutionLedger(), self._assessment(),
            self._authority(valid_until_tick=25),
            resolution_id="resolution:5", decision_actor_id="allocator",
            resolution_kind=AllocationResolutionKind.DEFER, decided_tick=30,
        )
        self.assertFalse(expired.accepted)
        self.assertEqual(expired.reason_code, "ALLOCATION_AUTHORITY_NOT_CURRENT")

    def test_actor_and_resource_scope_must_match(self):
        wrong_actor = record_allocation_resolution(
            ResourceAllocationResolutionLedger(), self._assessment(), self._authority(),
            resolution_id="resolution:6", decision_actor_id="someone-else",
            resolution_kind=AllocationResolutionKind.DEFER, decided_tick=30,
        )
        self.assertEqual(wrong_actor.reason_code, "AUTHORITY_ACTOR_MISMATCH")

        wrong_resource = record_allocation_resolution(
            ResourceAllocationResolutionLedger(), self._assessment(),
            self._authority(target_resource_id="meter:2"),
            resolution_id="resolution:7", decision_actor_id="allocator",
            resolution_kind=AllocationResolutionKind.DEFER, decided_tick=30,
        )
        self.assertEqual(wrong_resource.reason_code, "AUTHORITY_RESOURCE_MISMATCH")

    def test_selected_existing_reservation_must_come_from_current_conflict_set(self):
        result = record_allocation_resolution(
            ResourceAllocationResolutionLedger(), self._assessment(), self._authority(),
            resolution_id="resolution:8", decision_actor_id="allocator",
            resolution_kind=AllocationResolutionKind.SELECT_EXISTING_RESERVATION,
            selected_reservation_id="r:not-present", decided_tick=30,
        )
        self.assertFalse(result.accepted)
        self.assertEqual(result.reason_code, "SELECTED_RESERVATION_NOT_IN_CONFLICT_SET")

    def test_duplicate_ids_fail_closed_and_ledger_order_is_deterministic(self):
        ledger = ResourceAllocationResolutionLedger()
        second = record_allocation_resolution(
            ledger, self._assessment(), self._authority(),
            resolution_id="resolution:z", decision_actor_id="allocator",
            resolution_kind=AllocationResolutionKind.DEFER, decided_tick=30,
        )
        first = record_allocation_resolution(
            second.ledger, self._assessment(), self._authority(),
            resolution_id="resolution:a", decision_actor_id="allocator",
            resolution_kind=AllocationResolutionKind.DEFER, decided_tick=31,
        )
        self.assertEqual(
            tuple(item.resolution_id for item in first.ledger.resolutions),
            ("resolution:a", "resolution:z"),
        )
        duplicate = record_allocation_resolution(
            first.ledger, self._assessment(), self._authority(),
            resolution_id="resolution:a", decision_actor_id="allocator",
            resolution_kind=AllocationResolutionKind.DEFER, decided_tick=32,
        )
        self.assertFalse(duplicate.accepted)
        self.assertEqual(duplicate.reason_code, "DUPLICATE_RESOLUTION_ID")


if __name__ == "__main__":
    unittest.main()
