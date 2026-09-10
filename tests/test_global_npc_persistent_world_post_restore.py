import unittest

from tools.global_npc_persistent_world_post_restore import (
    validate_persistent_world_post_restore,
)
from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    ResourceReservation,
)
from tools.global_npc_resources import ResourceState, WorldResource
from tools.persistent_world_recovery_manifest import ReconciledPersistentWorldRecoveryManifest
from tools.world_resource_catalog_checkpoint import RestoredWorldResourceCatalog


class PersistentWorldPostRestoreValidationTests(unittest.TestCase):
    def manifest(self, minute=20, resource_digest="resource-digest"):
        return ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=minute,
            global_npc_checkpoint_sha256="global-digest",
            persistent_world_evidence_checkpoint_sha256="evidence-digest",
            world_resource_catalog_checkpoint_sha256=resource_digest,
        )

    def test_matching_restored_owners_are_safe_to_activate(self):
        resource = WorldResource(
            resource_id="kit-1",
            capability_refs=frozenset({"FIELD_KIT"}),
            state=ResourceState.RESERVED,
            reserved_for_actor_id="npc-a",
        )
        reservations = ReservationLedger(
            (
                ResourceReservation(
                    reservation_id="res-1",
                    resource_id="kit-1",
                    actor_id="npc-a",
                    start_tick=10,
                    end_tick=30,
                ),
            )
        )

        result = validate_persistent_world_post_restore(
            self.manifest(),
            RestoredWorldResourceCatalog(20, (resource,)),
            reservation_ledger=reservations,
            handoff_ledger=ResourceHandoffLedger(),
        )

        self.assertTrue(result.safe_to_activate)
        self.assertEqual(result.semantic_minute, 20)
        self.assertEqual(
            result.resource_report.confirmed[0].reason_code,
            "CURRENT_RESERVATION_MATCHES_ACTIVE_HISTORY",
        )

    def test_explicit_cross_owner_conflict_fails_activation(self):
        resource = WorldResource(
            resource_id="kit-1",
            capability_refs=frozenset({"FIELD_KIT"}),
            state=ResourceState.RESERVED,
            reserved_for_actor_id="npc-b",
        )
        reservations = ReservationLedger(
            (
                ResourceReservation(
                    reservation_id="res-1",
                    resource_id="kit-1",
                    actor_id="npc-a",
                    start_tick=10,
                    end_tick=30,
                ),
            )
        )

        with self.assertRaisesRegex(
            ValueError,
            "CURRENT_RESERVATION_ACTOR_CONFLICT",
        ):
            validate_persistent_world_post_restore(
                self.manifest(),
                RestoredWorldResourceCatalog(20, (resource,)),
                reservation_ledger=reservations,
                handoff_ledger=ResourceHandoffLedger(),
            )

    def test_indeterminate_history_remains_activatable_and_visible(self):
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
                    actor_id="npc-a",
                    start_tick=10,
                    end_tick=30,
                ),
            )
        )

        result = validate_persistent_world_post_restore(
            self.manifest(),
            RestoredWorldResourceCatalog(20, (resource,)),
            reservation_ledger=reservations,
            handoff_ledger=ResourceHandoffLedger(),
        )

        self.assertTrue(result.safe_to_activate)
        self.assertEqual(
            result.resource_report.indeterminate[0].reason_code,
            "ACTIVE_RESERVATION_NOT_PROJECTED_IN_CURRENT_CATALOG",
        )

    def test_catalog_from_different_minute_fails_before_reconciliation(self):
        with self.assertRaisesRegex(ValueError, "semantic minute mismatch"):
            validate_persistent_world_post_restore(
                self.manifest(minute=20),
                RestoredWorldResourceCatalog(19, ()),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
            )

    def test_legacy_manifest_without_resource_owner_cannot_use_stage(self):
        with self.assertRaisesRegex(ValueError, "requires a V2 recovery manifest"):
            validate_persistent_world_post_restore(
                self.manifest(resource_digest=None),
                RestoredWorldResourceCatalog(20, ()),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
            )


if __name__ == "__main__":
    unittest.main()
