import unittest

from tools.global_npc_persistent_world_post_restore import (
    validate_persistent_world_post_restore,
)
from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_holder_transitions import (
    HolderTransitionKind,
    ResourceHolderTransition,
    ResourceHolderTransitionLedger,
)
from tools.global_npc_resource_reservations import (
    ReservationLedger,
    ResourceReservation,
)
from tools.global_npc_resources import ResourceState, WorldResource
from tools.persistent_world_recovery_manifest import ReconciledPersistentWorldRecoveryManifest
from tools.resource_holder_transition_checkpoint import RestoredResourceHolderTransitions
from tools.world_resource_catalog_checkpoint import RestoredWorldResourceCatalog


class PersistentWorldPostRestoreValidationTests(unittest.TestCase):
    def manifest(
        self,
        minute=20,
        resource_digest="resource-digest",
        holder_digest=None,
    ):
        return ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=minute,
            global_npc_checkpoint_sha256="global-digest",
            persistent_world_evidence_checkpoint_sha256="evidence-digest",
            world_resource_catalog_checkpoint_sha256=resource_digest,
            resource_holder_transition_checkpoint_sha256=holder_digest,
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

    def test_v3_requires_restored_holder_owner_from_same_semantic_minute(self):
        manifest = self.manifest(holder_digest="holder-digest")
        catalog = RestoredWorldResourceCatalog(20, ())

        with self.assertRaisesRegex(ValueError, "requires restored holder transitions"):
            validate_persistent_world_post_restore(
                manifest,
                catalog,
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
            )

        with self.assertRaisesRegex(ValueError, "holder transition semantic minute mismatch"):
            validate_persistent_world_post_restore(
                manifest,
                catalog,
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
                holder_transitions=RestoredResourceHolderTransitions(
                    19,
                    ResourceHolderTransitionLedger(),
                ),
            )

    def test_v3_complete_holder_history_conflict_blocks_activation(self):
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id=None,
        )
        holder_ledger = ResourceHolderTransitionLedger(
            (
                ResourceHolderTransition(
                    transition_id="meter-checkout",
                    resource_id="meter-1",
                    kind=HolderTransitionKind.CHECKOUT,
                    from_actor_id=None,
                    to_actor_id="npc-a",
                    at_tick=10,
                ),
            )
        )

        with self.assertRaisesRegex(
            ValueError,
            "CURRENT_HOLDER_CONFLICTS_COMPLETE_HOLDER_JOURNAL",
        ):
            validate_persistent_world_post_restore(
                self.manifest(holder_digest="holder-digest"),
                RestoredWorldResourceCatalog(20, (resource,)),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
                holder_transitions=RestoredResourceHolderTransitions(20, holder_ledger),
                complete_holder_history_resource_ids=frozenset({"meter-1"}),
            )

    def test_v3_unaudited_holder_history_stays_visible_and_activatable(self):
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id=None,
        )
        holder_ledger = ResourceHolderTransitionLedger(
            (
                ResourceHolderTransition(
                    transition_id="meter-checkout",
                    resource_id="meter-1",
                    kind=HolderTransitionKind.CHECKOUT,
                    from_actor_id=None,
                    to_actor_id="npc-a",
                    at_tick=10,
                ),
            )
        )

        result = validate_persistent_world_post_restore(
            self.manifest(holder_digest="holder-digest"),
            RestoredWorldResourceCatalog(20, (resource,)),
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            holder_transitions=RestoredResourceHolderTransitions(20, holder_ledger),
        )

        self.assertTrue(result.safe_to_activate)
        self.assertEqual(
            result.resource_report.indeterminate[0].reason_code,
            "HOLDER_JOURNAL_COVERAGE_NOT_AUDITED_COMPLETE",
        )

    def test_legacy_manifest_rejects_unselected_holder_owner(self):
        with self.assertRaisesRegex(ValueError, "did not select holder transitions"):
            validate_persistent_world_post_restore(
                self.manifest(),
                RestoredWorldResourceCatalog(20, ()),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
                holder_transitions=RestoredResourceHolderTransitions(
                    20,
                    ResourceHolderTransitionLedger(),
                ),
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
