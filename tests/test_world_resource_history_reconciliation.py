import unittest

from tools.global_npc_resource_handoffs import (
    ResourceCustodyTransfer,
    ResourceHandoffLedger,
)
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    ResourceReservation,
)
from tools.global_npc_resources import ResourceState, WorldResource
from tools.world_resource_history_reconciliation import (
    ReconciliationStatus,
    reconcile_world_resource_history,
)


class WorldResourceHistoryReconciliationTests(unittest.TestCase):
    def test_matching_current_reservation_and_latest_handoff_are_confirmed(self):
        resource = WorldResource(
            resource_id="kit-1",
            capability_refs=frozenset({"FIELD_KIT"}),
            state=ResourceState.IN_USE,
            location_ref="station-a",
            holder_actor_id="npc-b",
            reserved_for_actor_id="npc-b",
        )
        reservations = ReservationLedger(
            (
                ResourceReservation(
                    reservation_id="res-1",
                    resource_id="kit-1",
                    actor_id="npc-b",
                    start_tick=10,
                    end_tick=40,
                ),
            )
        )
        handoffs = ResourceHandoffLedger(
            transfers=(
                ResourceCustodyTransfer(
                    transfer_id="transfer-1",
                    authorization_id="auth-1",
                    request_id="req-1",
                    resource_id="kit-1",
                    from_actor_id="npc-a",
                    to_actor_id="npc-b",
                    accountable_actor_id="npc-b",
                    location_ref="station-a",
                    at_tick=12,
                ),
            )
        )

        report = reconcile_world_resource_history(
            (resource,),
            reservation_ledger=reservations,
            handoff_ledger=handoffs,
            semantic_minute=20,
        )

        self.assertTrue(report.safe_to_restore)
        self.assertEqual(len(report.confirmed), 2)
        self.assertFalse(report.conflicts)
        self.assertFalse(report.indeterminate)

    def test_explicit_current_reservation_for_different_actor_is_conflict(self):
        resource = WorldResource(
            resource_id="kit-1",
            capability_refs=frozenset({"FIELD_KIT"}),
            state=ResourceState.RESERVED,
            reserved_for_actor_id="npc-c",
        )
        reservations = ReservationLedger(
            (
                ResourceReservation(
                    reservation_id="res-1",
                    resource_id="kit-1",
                    actor_id="npc-b",
                    start_tick=10,
                    end_tick=40,
                ),
            )
        )

        report = reconcile_world_resource_history(
            (resource,),
            reservation_ledger=reservations,
            handoff_ledger=ResourceHandoffLedger(),
            semantic_minute=20,
        )

        self.assertFalse(report.safe_to_restore)
        self.assertEqual(report.conflicts[0].reason_code, "CURRENT_RESERVATION_ACTOR_CONFLICT")
        self.assertEqual(report.conflicts[0].evidence_refs, ("res-1",))

    def test_unprojected_active_reservation_is_indeterminate_not_corruption(self):
        resource = WorldResource(
            resource_id="kit-1",
            capability_refs=frozenset({"FIELD_KIT"}),
            state=ResourceState.AVAILABLE,
        )
        reservations = ReservationLedger(
            (
                ResourceReservation(
                    reservation_id="res-1",
                    resource_id="kit-1",
                    actor_id="npc-b",
                    start_tick=10,
                    end_tick=40,
                ),
            )
        )

        report = reconcile_world_resource_history(
            (resource,),
            reservation_ledger=reservations,
            handoff_ledger=ResourceHandoffLedger(),
            semantic_minute=20,
        )

        self.assertTrue(report.safe_to_restore)
        self.assertEqual(
            report.indeterminate[0].reason_code,
            "ACTIVE_RESERVATION_NOT_PROJECTED_IN_CURRENT_CATALOG",
        )

    def test_latest_handoff_does_not_authorize_deriving_current_holder(self):
        resource = WorldResource(
            resource_id="kit-1",
            capability_refs=frozenset({"FIELD_KIT"}),
            state=ResourceState.AVAILABLE,
            location_ref="depot",
            holder_actor_id=None,
        )
        handoffs = ResourceHandoffLedger(
            transfers=(
                ResourceCustodyTransfer(
                    transfer_id="transfer-1",
                    authorization_id="auth-1",
                    request_id="req-1",
                    resource_id="kit-1",
                    from_actor_id="npc-a",
                    to_actor_id="npc-b",
                    accountable_actor_id="npc-b",
                    location_ref="station-a",
                    at_tick=12,
                ),
            )
        )

        report = reconcile_world_resource_history(
            (resource,),
            reservation_ledger=ReservationLedger(),
            handoff_ledger=handoffs,
            semantic_minute=20,
        )

        self.assertTrue(report.safe_to_restore)
        self.assertEqual(
            report.indeterminate[0].reason_code,
            "CURRENT_HOLDER_NOT_DERIVABLE_FROM_HANDOFF_HISTORY",
        )

    def test_reserved_state_without_actor_is_a_catalog_conflict(self):
        resource = WorldResource(
            resource_id="kit-1",
            capability_refs=frozenset({"FIELD_KIT"}),
            state=ResourceState.RESERVED,
        )

        report = reconcile_world_resource_history(
            (resource,),
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            semantic_minute=20,
        )

        self.assertFalse(report.safe_to_restore)
        self.assertEqual(
            report.conflicts[0].reason_code,
            "RESERVED_STATE_WITHOUT_RESERVED_ACTOR",
        )

    def test_historical_resource_missing_from_current_catalog_stays_indeterminate(self):
        reservations = ReservationLedger(
            (
                ResourceReservation(
                    reservation_id="old-res",
                    resource_id="retired-kit",
                    actor_id="npc-a",
                    start_tick=1,
                    end_tick=2,
                ),
            )
        )

        report = reconcile_world_resource_history(
            (),
            reservation_ledger=reservations,
            handoff_ledger=ResourceHandoffLedger(),
            semantic_minute=20,
        )

        self.assertTrue(report.safe_to_restore)
        self.assertEqual(
            report.indeterminate[0].reason_code,
            "HISTORY_REFERENCES_RESOURCE_ABSENT_FROM_CURRENT_CATALOG",
        )
        self.assertEqual(report.indeterminate[0].evidence_refs, ("old-res",))

    def test_duplicate_catalog_identity_fails_closed(self):
        resource = WorldResource(
            resource_id="kit-1",
            capability_refs=frozenset({"FIELD_KIT"}),
        )
        with self.assertRaisesRegex(ValueError, "duplicate world resource id"):
            reconcile_world_resource_history(
                (resource, resource),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
                semantic_minute=20,
            )

    def test_invalid_semantic_minute_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "semantic_minute"):
            reconcile_world_resource_history(
                (),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
                semantic_minute=-1,
            )

    def test_status_values_are_stable_for_machine_consumers(self):
        self.assertEqual(ReconciliationStatus.CONFIRMED.value, "CONFIRMED")
        self.assertEqual(ReconciliationStatus.INDETERMINATE.value, "INDETERMINATE")
        self.assertEqual(ReconciliationStatus.CONFLICT.value, "CONFLICT")


if __name__ == "__main__":
    unittest.main()
