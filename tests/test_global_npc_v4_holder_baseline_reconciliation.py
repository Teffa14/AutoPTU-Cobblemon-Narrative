import unittest

from tools.global_npc_holder_history_coverage import HolderHistoryCoverageBaseline
from tools.global_npc_persistent_world_post_restore import validate_persistent_world_post_restore
from tools.global_npc_resource_handoffs import ResourceHandoffLedger
from tools.global_npc_resource_holder_transitions import (
    HolderTransitionKind,
    ResourceHolderTransition,
    ResourceHolderTransitionLedger,
)
from tools.global_npc_resource_reservations import ReservationLedger
from tools.global_npc_resources import ResourceState, WorldResource
from tools.holder_history_coverage_baseline_checkpoint import (
    snapshot_holder_history_coverage_baselines,
)
from tools.persistent_world_recovery_manifest import ReconciledPersistentWorldRecoveryManifest
from tools.resource_holder_transition_checkpoint import RestoredResourceHolderTransitions
from tools.world_resource_catalog_checkpoint import RestoredWorldResourceCatalog


class PersistentWorldV4HolderBaselineReconciliationTests(unittest.TestCase):
    def manifest(self, baseline_digest: str, minute: int = 20):
        return ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=minute,
            global_npc_checkpoint_sha256="global-digest",
            persistent_world_evidence_checkpoint_sha256="evidence-digest",
            world_resource_catalog_checkpoint_sha256="catalog-digest",
            resource_holder_transition_checkpoint_sha256="holder-digest",
            holder_history_coverage_baseline_checkpoint_sha256=baseline_digest,
        )

    def baseline_snapshot(self, *, at_tick=10, holder="npc-a", minute=20):
        return snapshot_holder_history_coverage_baselines(
            (
                HolderHistoryCoverageBaseline(
                    baseline_id=f"baseline-meter-1-{at_tick}",
                    resource_id="meter-1",
                    at_tick=at_tick,
                    holder_actor_id=holder,
                    source_ref=f"catalog-generation-{at_tick}",
                ),
            ),
            semantic_minute=minute,
        )

    def holder_transitions(self):
        return RestoredResourceHolderTransitions(
            20,
            ResourceHolderTransitionLedger(
                (
                    ResourceHolderTransition(
                        transition_id="handoff-15",
                        resource_id="meter-1",
                        kind=HolderTransitionKind.HANDOFF,
                        from_actor_id="npc-a",
                        to_actor_id="npc-b",
                        at_tick=15,
                        source_ref="custody-transfer-15",
                    ),
                )
            ),
        )

    def test_v4_replays_selected_older_baseline_through_holder_journal(self):
        snapshot = self.baseline_snapshot()
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id="npc-b",
        )

        result = validate_persistent_world_post_restore(
            self.manifest(snapshot["sha256"]),
            RestoredWorldResourceCatalog(20, (resource,)),
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            holder_transitions=self.holder_transitions(),
            holder_history_coverage_baseline_checkpoint_snapshot=snapshot,
        )

        self.assertTrue(result.safe_to_activate)
        matches = [
            finding
            for finding in result.resource_report.confirmed
            if finding.reason_code == "CURRENT_HOLDER_MATCHES_BOUNDED_HOLDER_HISTORY"
        ]
        self.assertEqual(len(matches), 1)
        self.assertIn("baseline-meter-1-10", matches[0].evidence_refs)
        self.assertIn("handoff-15", matches[0].evidence_refs)

    def test_v4_selected_baseline_detects_holder_conflict(self):
        snapshot = self.baseline_snapshot()
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id="npc-c",
        )

        with self.assertRaisesRegex(
            ValueError,
            "CURRENT_HOLDER_CONFLICTS_BOUNDED_HOLDER_HISTORY",
        ):
            validate_persistent_world_post_restore(
                self.manifest(snapshot["sha256"]),
                RestoredWorldResourceCatalog(20, (resource,)),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
                holder_transitions=self.holder_transitions(),
                holder_history_coverage_baseline_checkpoint_snapshot=snapshot,
            )

    def test_v4_requires_exact_selected_baseline_generation(self):
        selected = self.baseline_snapshot(holder="npc-a")
        different = self.baseline_snapshot(holder="npc-z")

        with self.assertRaisesRegex(ValueError, "digest does not match recovery manifest"):
            validate_persistent_world_post_restore(
                self.manifest(selected["sha256"]),
                RestoredWorldResourceCatalog(20, ()),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
                holder_transitions=RestoredResourceHolderTransitions(
                    20,
                    ResourceHolderTransitionLedger(),
                ),
                holder_history_coverage_baseline_checkpoint_snapshot=different,
            )

    def test_same_cut_baseline_cannot_certify_the_catalog_that_produced_it(self):
        snapshot = self.baseline_snapshot(at_tick=20, holder="npc-z")
        resource = WorldResource(
            resource_id="meter-1",
            capability_refs=frozenset({"SURVEY_METER"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id="npc-b",
        )

        result = validate_persistent_world_post_restore(
            self.manifest(snapshot["sha256"]),
            RestoredWorldResourceCatalog(20, (resource,)),
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            holder_transitions=RestoredResourceHolderTransitions(
                20,
                ResourceHolderTransitionLedger(),
            ),
            holder_history_coverage_baseline_checkpoint_snapshot=snapshot,
        )

        self.assertTrue(result.safe_to_activate)
        bounded_findings = [
            finding
            for finding in result.resource_report.findings
            if "BOUNDED_HOLDER_HISTORY" in finding.reason_code
        ]
        self.assertEqual(bounded_findings, [])

    def test_v4_requires_selected_baseline_checkpoint(self):
        snapshot = self.baseline_snapshot()
        with self.assertRaisesRegex(ValueError, "requires holder history coverage baseline checkpoint"):
            validate_persistent_world_post_restore(
                self.manifest(snapshot["sha256"]),
                RestoredWorldResourceCatalog(20, ()),
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
                holder_transitions=RestoredResourceHolderTransitions(
                    20,
                    ResourceHolderTransitionLedger(),
                ),
            )


if __name__ == "__main__":
    unittest.main()
