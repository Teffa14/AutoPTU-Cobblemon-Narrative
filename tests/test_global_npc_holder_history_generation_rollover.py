import unittest

from tools.global_npc_holder_history_coverage import HolderHistoryCoverageBaseline
from tools.global_npc_holder_history_generation_rollover import (
    carry_forward_issued_holder_history_baselines,
)
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
    restore_holder_history_coverage_baselines,
    snapshot_holder_history_coverage_baselines,
)
from tools.persistent_world_recovery_manifest import ReconciledPersistentWorldRecoveryManifest
from tools.resource_holder_transition_checkpoint import RestoredResourceHolderTransitions
from tools.world_resource_catalog_checkpoint import (
    restore_world_resource_catalog,
    snapshot_world_resource_catalog,
)


class HolderHistoryGenerationRolloverTests(unittest.TestCase):
    def resource(self, holder: str) -> WorldResource:
        return WorldResource(
            resource_id="field-kit-1",
            capability_refs=frozenset({"FIELD_KIT"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id=holder,
        )

    def manifest(self, *, minute: int, catalog_digest: str, baseline_digest: str):
        return ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=minute,
            global_npc_checkpoint_sha256=f"global-{minute}",
            persistent_world_evidence_checkpoint_sha256=f"evidence-{minute}",
            world_resource_catalog_checkpoint_sha256=catalog_digest,
            resource_holder_transition_checkpoint_sha256=f"holder-{minute}",
            holder_history_coverage_baseline_checkpoint_sha256=baseline_digest,
        )

    def transition(
        self,
        *,
        transition_id: str,
        from_actor: str,
        to_actor: str,
        at_tick: int,
    ) -> ResourceHolderTransition:
        return ResourceHolderTransition(
            transition_id=transition_id,
            resource_id="field-kit-1",
            kind=HolderTransitionKind.HANDOFF,
            from_actor_id=from_actor,
            to_actor_id=to_actor,
            at_tick=at_tick,
            source_ref=f"custody-{transition_id}",
        )

    def validate_cut(
        self,
        *,
        minute: int,
        holder: str,
        baseline_snapshot,
        transitions,
    ):
        catalog_snapshot = snapshot_world_resource_catalog(
            (self.resource(holder),),
            semantic_minute=minute,
        )
        restored_catalog = restore_world_resource_catalog(catalog_snapshot)
        return validate_persistent_world_post_restore(
            self.manifest(
                minute=minute,
                catalog_digest=catalog_snapshot["sha256"],
                baseline_digest=baseline_snapshot["sha256"],
            ),
            restored_catalog,
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            holder_transitions=RestoredResourceHolderTransitions(
                minute,
                ResourceHolderTransitionLedger(tuple(transitions)),
            ),
            resource_catalog_checkpoint_snapshot=catalog_snapshot,
            holder_history_coverage_baseline_checkpoint_snapshot=baseline_snapshot,
        )

    def test_safe_baseline_rolls_across_two_later_generations(self):
        baseline_10 = HolderHistoryCoverageBaseline(
            baseline_id="baseline-10",
            resource_id="field-kit-1",
            at_tick=10,
            holder_actor_id="npc-a",
            source_ref="catalog-10",
        )
        selected_at_20 = snapshot_holder_history_coverage_baselines(
            (baseline_10,),
            semantic_minute=20,
        )
        handoff_15 = self.transition(
            transition_id="handoff-15",
            from_actor="npc-a",
            to_actor="npc-b",
            at_tick=15,
        )

        validated_20 = self.validate_cut(
            minute=20,
            holder="npc-b",
            baseline_snapshot=selected_at_20,
            transitions=(handoff_15,),
        )
        self.assertTrue(validated_20.safe_to_activate)
        self.assertEqual(len(validated_20.issued_holder_history_coverage_baselines), 1)
        self.assertEqual(validated_20.issued_holder_history_coverage_baselines[0].at_tick, 20)
        self.assertEqual(validated_20.issued_holder_history_coverage_baselines[0].holder_actor_id, "npc-b")

        selected_at_40 = carry_forward_issued_holder_history_baselines(
            validated_20,
            checkpoint_semantic_minute=40,
        )
        restored_at_40 = restore_holder_history_coverage_baselines(selected_at_40)
        self.assertEqual(restored_at_40.semantic_minute, 40)
        self.assertEqual(restored_at_40.baselines[0].at_tick, 20)
        self.assertEqual(restored_at_40.baselines[0].holder_actor_id, "npc-b")

        handoff_30 = self.transition(
            transition_id="handoff-30",
            from_actor="npc-b",
            to_actor="npc-c",
            at_tick=30,
        )
        validated_40 = self.validate_cut(
            minute=40,
            holder="npc-c",
            baseline_snapshot=selected_at_40,
            transitions=(handoff_15, handoff_30),
        )
        self.assertTrue(validated_40.safe_to_activate)
        self.assertEqual(validated_40.issued_holder_history_coverage_baselines[0].at_tick, 40)
        self.assertEqual(validated_40.issued_holder_history_coverage_baselines[0].holder_actor_id, "npc-c")

        selected_at_60 = carry_forward_issued_holder_history_baselines(
            validated_40,
            checkpoint_semantic_minute=60,
        )
        restored_at_60 = restore_holder_history_coverage_baselines(selected_at_60)
        self.assertEqual(restored_at_60.baselines[0].at_tick, 40)
        self.assertEqual(restored_at_60.baselines[0].holder_actor_id, "npc-c")

    def test_rollover_keeps_original_certification_cut(self):
        baseline_10 = HolderHistoryCoverageBaseline(
            baseline_id="baseline-10",
            resource_id="field-kit-1",
            at_tick=10,
            holder_actor_id="npc-a",
            source_ref="catalog-10",
        )
        selected_at_20 = snapshot_holder_history_coverage_baselines(
            (baseline_10,),
            semantic_minute=20,
        )
        validated_20 = self.validate_cut(
            minute=20,
            holder="npc-b",
            baseline_snapshot=selected_at_20,
            transitions=(
                self.transition(
                    transition_id="handoff-15",
                    from_actor="npc-a",
                    to_actor="npc-b",
                    at_tick=15,
                ),
            ),
        )

        rolled = carry_forward_issued_holder_history_baselines(
            validated_20,
            checkpoint_semantic_minute=100,
        )
        restored = restore_holder_history_coverage_baselines(rolled)
        self.assertEqual(restored.semantic_minute, 100)
        self.assertEqual(restored.baselines[0].at_tick, 20)
        self.assertNotEqual(restored.baselines[0].at_tick, restored.semantic_minute)

    def test_rollover_rejects_checkpoint_before_validated_cut(self):
        baseline_10 = HolderHistoryCoverageBaseline(
            baseline_id="baseline-10",
            resource_id="field-kit-1",
            at_tick=10,
            holder_actor_id="npc-a",
            source_ref="catalog-10",
        )
        selected_at_20 = snapshot_holder_history_coverage_baselines(
            (baseline_10,),
            semantic_minute=20,
        )
        validated_20 = self.validate_cut(
            minute=20,
            holder="npc-b",
            baseline_snapshot=selected_at_20,
            transitions=(
                self.transition(
                    transition_id="handoff-15",
                    from_actor="npc-a",
                    to_actor="npc-b",
                    at_tick=15,
                ),
            ),
        )

        with self.assertRaisesRegex(ValueError, "at or after the validated recovery cut"):
            carry_forward_issued_holder_history_baselines(
                validated_20,
                checkpoint_semantic_minute=19,
            )

    def test_next_generation_fails_closed_on_journal_discontinuity(self):
        baseline_10 = HolderHistoryCoverageBaseline(
            baseline_id="baseline-10",
            resource_id="field-kit-1",
            at_tick=10,
            holder_actor_id="npc-a",
            source_ref="catalog-10",
        )
        selected_at_20 = snapshot_holder_history_coverage_baselines(
            (baseline_10,),
            semantic_minute=20,
        )
        validated_20 = self.validate_cut(
            minute=20,
            holder="npc-b",
            baseline_snapshot=selected_at_20,
            transitions=(
                self.transition(
                    transition_id="handoff-15",
                    from_actor="npc-a",
                    to_actor="npc-b",
                    at_tick=15,
                ),
            ),
        )
        selected_at_40 = carry_forward_issued_holder_history_baselines(
            validated_20,
            checkpoint_semantic_minute=40,
        )

        with self.assertRaisesRegex(ValueError, "baseline conflicts with journal continuity"):
            self.validate_cut(
                minute=40,
                holder="npc-c",
                baseline_snapshot=selected_at_40,
                transitions=(
                    self.transition(
                        transition_id="handoff-30",
                        from_actor="npc-z",
                        to_actor="npc-c",
                        at_tick=30,
                    ),
                ),
            )


if __name__ == "__main__":
    unittest.main()
