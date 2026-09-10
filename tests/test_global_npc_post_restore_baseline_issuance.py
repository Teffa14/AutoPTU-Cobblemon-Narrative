import unittest

from tools.global_npc_persistent_world_post_restore import validate_persistent_world_post_restore
from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_holder_transitions import (
    HolderTransitionKind,
    ResourceHolderTransition,
    ResourceHolderTransitionLedger,
)
from tools.global_npc_resource_reservations import ReservationLedger
from tools.global_npc_resources import ResourceState, WorldResource
from tools.persistent_world_recovery_manifest import ReconciledPersistentWorldRecoveryManifest
from tools.resource_holder_transition_checkpoint import RestoredResourceHolderTransitions
from tools.world_resource_catalog_checkpoint import (
    RestoredWorldResourceCatalog,
    snapshot_world_resource_catalog,
)


class PostRestoreBaselineIssuanceTests(unittest.TestCase):
    def manifest(self, snapshot):
        return ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=20,
            global_npc_checkpoint_sha256="global-digest",
            persistent_world_evidence_checkpoint_sha256="evidence-digest",
            world_resource_catalog_checkpoint_sha256=snapshot["sha256"],
            resource_holder_transition_checkpoint_sha256="holder-digest",
        )

    def validate(self, resource, snapshot, ledger=None):
        return validate_persistent_world_post_restore(
            self.manifest(snapshot),
            RestoredWorldResourceCatalog(20, (resource,)),
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            holder_transitions=RestoredResourceHolderTransitions(
                20,
                ledger or ResourceHolderTransitionLedger(),
            ),
            resource_catalog_checkpoint_snapshot=snapshot,
        )

    def test_successful_v3_validation_issues_baseline_from_exact_selected_catalog(self):
        resource = WorldResource(
            resource_id="case-1",
            capability_refs=frozenset({"FIELD_CASE"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id="npc-a",
        )
        snapshot = snapshot_world_resource_catalog((resource,), semantic_minute=20)

        result = self.validate(resource, snapshot)

        self.assertTrue(result.safe_to_activate)
        self.assertEqual(len(result.issued_holder_history_coverage_baselines), 1)
        baseline = result.issued_holder_history_coverage_baselines[0]
        self.assertEqual(baseline.resource_id, "case-1")
        self.assertEqual(baseline.at_tick, 20)
        self.assertEqual(baseline.holder_actor_id, "npc-a")
        self.assertIn(snapshot["sha256"], baseline.source_ref)

    def test_same_minute_different_catalog_generation_is_rejected(self):
        restored_resource = WorldResource(
            resource_id="case-1",
            capability_refs=frozenset({"FIELD_CASE"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id="npc-a",
        )
        selected_resource = WorldResource(
            resource_id="case-1",
            capability_refs=frozenset({"FIELD_CASE"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id="npc-b",
        )
        snapshot = snapshot_world_resource_catalog((selected_resource,), semantic_minute=20)

        with self.assertRaisesRegex(ValueError, "does not match selected checkpoint generation"):
            self.validate(restored_resource, snapshot)

    def test_checkpoint_digest_must_match_outer_recovery_manifest(self):
        resource = WorldResource(
            resource_id="case-1",
            capability_refs=frozenset({"FIELD_CASE"}),
            state=ResourceState.AVAILABLE,
        )
        snapshot = snapshot_world_resource_catalog((resource,), semantic_minute=20)
        manifest = ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=20,
            global_npc_checkpoint_sha256="global-digest",
            persistent_world_evidence_checkpoint_sha256="evidence-digest",
            world_resource_catalog_checkpoint_sha256="different-generation",
            resource_holder_transition_checkpoint_sha256="holder-digest",
        )

        with self.assertRaisesRegex(ValueError, "digest does not match recovery manifest"):
            validate_persistent_world_post_restore(
                manifest,
                RestoredWorldResourceCatalog(20, (resource,)),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
                holder_transitions=RestoredResourceHolderTransitions(
                    20,
                    ResourceHolderTransitionLedger(),
                ),
                resource_catalog_checkpoint_snapshot=snapshot,
            )

    def test_new_baseline_does_not_retroactively_certify_pre_checkpoint_journal(self):
        resource = WorldResource(
            resource_id="case-1",
            capability_refs=frozenset({"FIELD_CASE"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id=None,
        )
        snapshot = snapshot_world_resource_catalog((resource,), semantic_minute=20)
        ledger = ResourceHolderTransitionLedger(
            (
                ResourceHolderTransition(
                    transition_id="checkout-1",
                    resource_id="case-1",
                    kind=HolderTransitionKind.CHECKOUT,
                    from_actor_id=None,
                    to_actor_id="npc-a",
                    at_tick=10,
                ),
            )
        )

        result = self.validate(resource, snapshot, ledger)

        self.assertTrue(result.safe_to_activate)
        self.assertEqual(
            result.resource_report.indeterminate[0].reason_code,
            "HOLDER_JOURNAL_COVERAGE_NOT_AUDITED_COMPLETE",
        )
        self.assertEqual(
            result.issued_holder_history_coverage_baselines[0].holder_actor_id,
            None,
        )
        self.assertEqual(result.issued_holder_history_coverage_baselines[0].at_tick, 20)

    def test_v3_without_raw_selected_checkpoint_remains_conservative_and_issues_no_baseline(self):
        resource = WorldResource(
            resource_id="case-1",
            capability_refs=frozenset({"FIELD_CASE"}),
            state=ResourceState.AVAILABLE,
        )
        snapshot = snapshot_world_resource_catalog((resource,), semantic_minute=20)

        result = validate_persistent_world_post_restore(
            self.manifest(snapshot),
            RestoredWorldResourceCatalog(20, (resource,)),
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            holder_transitions=RestoredResourceHolderTransitions(
                20,
                ResourceHolderTransitionLedger(),
            ),
        )

        self.assertTrue(result.safe_to_activate)
        self.assertEqual(result.issued_holder_history_coverage_baselines, ())


if __name__ == "__main__":
    unittest.main()
