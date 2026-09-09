import copy
import unittest

from tests.test_global_npc_resource_allocation_application_checkpoint import GlobalNpcResourceAllocationApplicationCheckpointTests
from tools.global_npc_resource_allocation_application_checkpoint import snapshot_resource_state_with_allocation_applications
from tools.global_npc_resource_allocation_notice_checkpoint import (
    RESOURCE_CHECKPOINT_ALLOCATION_NOTICE_SCHEMA,
    restore_resource_state_with_allocation_notices,
    snapshot_resource_state_with_allocation_notices,
    validate_allocation_notice_checkpoint_time,
)
from tools.global_npc_resource_allocation_notices import (
    ResourceAllocationNoticeLedger,
    ResourceAllocationNoticeLink,
    derive_displacement_notice_obligations,
)


class GlobalNpcResourceAllocationNoticeCheckpointTests(unittest.TestCase):
    def _state(self, *, with_link=False):
        base = GlobalNpcResourceAllocationApplicationCheckpointTests()._state()
        notice_ledger = derive_displacement_notice_obligations(
            ResourceAllocationNoticeLedger(),
            base[9].applications[0],
            base[0],
            obligation_id_prefix="notice-obligation:allocation-1",
            created_tick=48,
            basis_refs=("application:1", "reservation:other"),
        )
        if with_link:
            obligation = notice_ledger.obligations[0]
            notice_ledger = ResourceAllocationNoticeLedger(
                obligations=notice_ledger.obligations,
                links=(ResourceAllocationNoticeLink(
                    "notice-link:1",
                    obligation.obligation_id,
                    "scheduler",
                    "delivery:allocation-change",
                    49,
                ),),
            )
        return (*base, notice_ledger)

    def test_round_trip_preserves_notice_obligation_and_link(self):
        state = self._state(with_link=True)
        snapshot = snapshot_resource_state_with_allocation_notices(*state)
        self.assertEqual(snapshot["schema"], RESOURCE_CHECKPOINT_ALLOCATION_NOTICE_SCHEMA)
        self.assertEqual(restore_resource_state_with_allocation_notices(snapshot), state)

    def test_v8_restore_does_not_infer_notice_history(self):
        state = self._state()
        snapshot = snapshot_resource_state_with_allocation_applications(*state[:10])
        restored = restore_resource_state_with_allocation_notices(snapshot)
        self.assertEqual(restored[:10], state[:10])
        self.assertEqual(restored[10], ResourceAllocationNoticeLedger())

    def test_notice_requires_persisted_application(self):
        snapshot = snapshot_resource_state_with_allocation_notices(*self._state())
        snapshot["allocation_applications"] = []
        with self.assertRaisesRegex(ValueError, "missing application"):
            restore_resource_state_with_allocation_notices(snapshot)

    def test_notice_holder_must_match_displaced_reservation(self):
        snapshot = snapshot_resource_state_with_allocation_notices(*self._state())
        snapshot["allocation_notice_obligations"][0]["affected_actor_id"] = "someone-else"
        with self.assertRaisesRegex(ValueError, "affected actor mismatch"):
            restore_resource_state_with_allocation_notices(snapshot)

    def test_notice_reservation_must_be_in_application_displacement_set(self):
        snapshot = snapshot_resource_state_with_allocation_notices(*self._state())
        snapshot["allocation_notice_obligations"][0]["displaced_reservation_id"] = "reservation:not-displaced"
        with self.assertRaisesRegex(ValueError, "was not displaced"):
            restore_resource_state_with_allocation_notices(snapshot)

    def test_same_application_reservation_pair_cannot_have_two_obligations(self):
        snapshot = snapshot_resource_state_with_allocation_notices(*self._state())
        duplicate = copy.deepcopy(snapshot["allocation_notice_obligations"][0])
        duplicate["obligation_id"] = "notice-obligation:duplicate"
        snapshot["allocation_notice_obligations"].append(duplicate)
        with self.assertRaisesRegex(ValueError, "application/reservation obligations"):
            restore_resource_state_with_allocation_notices(snapshot)

    def test_link_requires_persisted_obligation(self):
        snapshot = snapshot_resource_state_with_allocation_notices(*self._state(with_link=True))
        snapshot["allocation_notice_links"][0]["obligation_id"] = "notice-obligation:missing"
        with self.assertRaisesRegex(ValueError, "missing obligation"):
            restore_resource_state_with_allocation_notices(snapshot)

    def test_future_notice_fails_time_validation(self):
        state = self._state(with_link=True)
        with self.assertRaisesRegex(ValueError, "obligation comes from the future"):
            validate_allocation_notice_checkpoint_time(state[10], semantic_minute=47)
        with self.assertRaisesRegex(ValueError, "link comes from the future"):
            validate_allocation_notice_checkpoint_time(state[10], semantic_minute=48)


if __name__ == "__main__":
    unittest.main()
