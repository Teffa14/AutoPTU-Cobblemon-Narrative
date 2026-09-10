import hashlib
import json
import unittest

from tools.global_npc_holder_history_coverage import HolderHistoryCoverageBaseline
from tools.global_npc_holder_history_generation_rollover import (
    carry_forward_issued_holder_history_baselines,
)
from tools.global_npc_holder_history_v4_generation import (
    validate_exact_v4_holder_history_generation,
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
from tools.global_npc_world_action_interruption_provenance_checkpoint import (
    WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
)
from tools.holder_history_coverage_baseline_checkpoint import (
    snapshot_holder_history_coverage_baselines,
)
from tools.persistent_world_evidence_checkpoint import PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA
from tools.persistent_world_recovery_manifest import (
    ReconciledPersistentWorldRecoveryManifest,
    build_persistent_world_recovery_manifest,
)
from tools.resource_holder_transition_checkpoint import snapshot_resource_holder_transitions
from tools.world_resource_catalog_checkpoint import (
    restore_world_resource_catalog,
    snapshot_world_resource_catalog,
)


def signed_checkpoint(schema: str, semantic_minute: int, marker: str) -> dict:
    payload = {"schema": schema, "semantic_minute": semantic_minute, "marker": marker}
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return payload | {"sha256": digest}


class HolderHistoryFullV4RolloverTests(unittest.TestCase):
    def resource(self, holder: str) -> WorldResource:
        return WorldResource(
            resource_id="survey-case-1",
            capability_refs=frozenset({"FIELD_SURVEY_CASE"}),
            state=ResourceState.AVAILABLE,
            holder_actor_id=holder,
        )

    def transition(self, transition_id: str, from_actor: str, to_actor: str, at_tick: int):
        return ResourceHolderTransition(
            transition_id=transition_id,
            resource_id="survey-case-1",
            kind=HolderTransitionKind.HANDOFF,
            from_actor_id=from_actor,
            to_actor_id=to_actor,
            at_tick=at_tick,
            source_ref=f"custody-{transition_id}",
        )

    def bootstrap_validation(self):
        baseline_10 = HolderHistoryCoverageBaseline(
            baseline_id="baseline-10",
            resource_id="survey-case-1",
            at_tick=10,
            holder_actor_id="npc-a",
            source_ref="catalog-10",
        )
        baseline_snapshot = snapshot_holder_history_coverage_baselines(
            (baseline_10,), semantic_minute=20
        )
        handoff_15 = self.transition("handoff-15", "npc-a", "npc-b", 15)
        catalog_snapshot = snapshot_world_resource_catalog(
            (self.resource("npc-b"),), semantic_minute=20
        )
        manifest = ReconciledPersistentWorldRecoveryManifest(
            semantic_minute=20,
            global_npc_checkpoint_sha256="bootstrap-global",
            persistent_world_evidence_checkpoint_sha256="bootstrap-evidence",
            world_resource_catalog_checkpoint_sha256=catalog_snapshot["sha256"],
            resource_holder_transition_checkpoint_sha256="bootstrap-holder",
            holder_history_coverage_baseline_checkpoint_sha256=baseline_snapshot["sha256"],
        )
        restored_holder = type("Restored", (), {
            "semantic_minute": 20,
            "ledger": ResourceHolderTransitionLedger((handoff_15,)),
        })()
        validation = validate_persistent_world_post_restore(
            manifest,
            restore_world_resource_catalog(catalog_snapshot),
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
            holder_transitions=restored_holder,
            resource_catalog_checkpoint_snapshot=catalog_snapshot,
            holder_history_coverage_baseline_checkpoint_snapshot=baseline_snapshot,
        )
        self.assertTrue(validation.safe_to_activate)
        return validation, handoff_15

    def full_v4_validation(self, *, minute, holder, baseline_snapshot, transitions):
        global_checkpoint = signed_checkpoint(
            WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
            minute,
            f"global-{minute}",
        )
        evidence_checkpoint = signed_checkpoint(
            PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
            minute,
            f"evidence-{minute}",
        )
        catalog_checkpoint = snapshot_world_resource_catalog(
            (self.resource(holder),), semantic_minute=minute
        )
        holder_checkpoint = snapshot_resource_holder_transitions(
            ResourceHolderTransitionLedger(tuple(transitions)),
            semantic_minute=minute,
        )
        manifest_snapshot = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=catalog_checkpoint,
            resource_holder_transition_checkpoint=holder_checkpoint,
            holder_history_coverage_baseline_checkpoint=baseline_snapshot,
        )
        validation = validate_exact_v4_holder_history_generation(
            manifest_snapshot,
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=catalog_checkpoint,
            resource_holder_transition_checkpoint=holder_checkpoint,
            holder_history_coverage_baseline_checkpoint=baseline_snapshot,
            reservation_ledger=ReservationLedger(),
            handoff_ledger=ResourceHandoffLedger(),
        )
        return validation, manifest_snapshot, catalog_checkpoint, holder_checkpoint

    def test_rollover_survives_two_complete_v4_generations(self):
        validated_20, handoff_15 = self.bootstrap_validation()
        selected_40 = carry_forward_issued_holder_history_baselines(
            validated_20, checkpoint_semantic_minute=40
        )
        handoff_30 = self.transition("handoff-30", "npc-b", "npc-c", 30)

        validated_40, manifest_40, catalog_40, holder_40 = self.full_v4_validation(
            minute=40,
            holder="npc-c",
            baseline_snapshot=selected_40,
            transitions=(handoff_15, handoff_30),
        )
        self.assertTrue(validated_40.safe_to_activate)
        self.assertEqual(validated_40.issued_holder_history_coverage_baselines[0].at_tick, 40)
        self.assertEqual(validated_40.issued_holder_history_coverage_baselines[0].holder_actor_id, "npc-c")
        self.assertEqual(manifest_40["world_resource_catalog_checkpoint_sha256"], catalog_40["sha256"])
        self.assertEqual(manifest_40["resource_holder_transition_checkpoint_sha256"], holder_40["sha256"])
        self.assertEqual(
            manifest_40["holder_history_coverage_baseline_checkpoint_sha256"],
            selected_40["sha256"],
        )

        selected_60 = carry_forward_issued_holder_history_baselines(
            validated_40, checkpoint_semantic_minute=60
        )
        handoff_50 = self.transition("handoff-50", "npc-c", "npc-d", 50)
        validated_60, manifest_60, catalog_60, holder_60 = self.full_v4_validation(
            minute=60,
            holder="npc-d",
            baseline_snapshot=selected_60,
            transitions=(handoff_15, handoff_30, handoff_50),
        )
        self.assertTrue(validated_60.safe_to_activate)
        self.assertEqual(validated_60.issued_holder_history_coverage_baselines[0].at_tick, 60)
        self.assertEqual(validated_60.issued_holder_history_coverage_baselines[0].holder_actor_id, "npc-d")
        self.assertEqual(manifest_60["world_resource_catalog_checkpoint_sha256"], catalog_60["sha256"])
        self.assertEqual(manifest_60["resource_holder_transition_checkpoint_sha256"], holder_60["sha256"])
        self.assertEqual(
            manifest_60["holder_history_coverage_baseline_checkpoint_sha256"],
            selected_60["sha256"],
        )

    def test_full_v4_generation_rejects_valid_wrong_baseline_owner(self):
        validated_20, handoff_15 = self.bootstrap_validation()
        selected_40 = carry_forward_issued_holder_history_baselines(
            validated_20, checkpoint_semantic_minute=40
        )
        handoff_30 = self.transition("handoff-30", "npc-b", "npc-c", 30)
        global_checkpoint = signed_checkpoint(
            WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA, 40, "global-40"
        )
        evidence_checkpoint = signed_checkpoint(
            PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA, 40, "evidence-40"
        )
        catalog_checkpoint = snapshot_world_resource_catalog(
            (self.resource("npc-c"),), semantic_minute=40
        )
        holder_checkpoint = snapshot_resource_holder_transitions(
            ResourceHolderTransitionLedger((handoff_15, handoff_30)), semantic_minute=40
        )
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=catalog_checkpoint,
            resource_holder_transition_checkpoint=holder_checkpoint,
            holder_history_coverage_baseline_checkpoint=selected_40,
        )
        wrong_baseline = snapshot_holder_history_coverage_baselines(
            (HolderHistoryCoverageBaseline(
                baseline_id="other-baseline",
                resource_id="survey-case-1",
                at_tick=20,
                holder_actor_id="npc-z",
                source_ref="other-catalog-20",
            ),),
            semantic_minute=40,
        )
        with self.assertRaisesRegex(ValueError, "holder history coverage baseline checkpoint digest mismatch"):
            validate_exact_v4_holder_history_generation(
                manifest,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=catalog_checkpoint,
                resource_holder_transition_checkpoint=holder_checkpoint,
                holder_history_coverage_baseline_checkpoint=wrong_baseline,
                reservation_ledger=ReservationLedger(),
                handoff_ledger=ResourceHandoffLedger(),
            )


if __name__ == "__main__":
    unittest.main()
