import copy
import unittest

from tools.global_npc_holder_history_coverage import HolderHistoryCoverageBaseline
from tools.holder_history_coverage_baseline_checkpoint import (
    restore_holder_history_coverage_baselines,
    snapshot_holder_history_coverage_baselines,
)


class HolderHistoryCoverageBaselineCheckpointTests(unittest.TestCase):
    def baseline(self, resource_id: str, holder: str | None, at_tick: int = 20):
        return HolderHistoryCoverageBaseline(
            baseline_id=f"baseline-{resource_id}",
            resource_id=resource_id,
            at_tick=at_tick,
            holder_actor_id=holder,
            source_ref=f"OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1:sha:{resource_id}",
        )

    def test_snapshot_restore_is_deterministic_and_canonical(self):
        baselines = (self.baseline("case-b", None), self.baseline("case-a", "npc-a"))
        first = snapshot_holder_history_coverage_baselines(baselines, semantic_minute=20)
        second = snapshot_holder_history_coverage_baselines(reversed(baselines), semantic_minute=20)
        self.assertEqual(first, second)
        self.assertEqual(
            [item["resource_id"] for item in first["baselines"]],
            ["case-a", "case-b"],
        )

        restored = restore_holder_history_coverage_baselines(first, recovery_semantic_minute=20)
        self.assertEqual(restored.semantic_minute, 20)
        self.assertEqual(restored.baselines, tuple(sorted(baselines, key=lambda item: item.resource_id)))

    def test_rejects_duplicate_resource_or_baseline_identity(self):
        first = self.baseline("case-a", "npc-a")
        second = HolderHistoryCoverageBaseline(
            baseline_id="different-id",
            resource_id="case-a",
            at_tick=20,
            holder_actor_id="npc-a",
            source_ref="checkpoint:other",
        )
        with self.assertRaisesRegex(ValueError, "multiple holder history coverage baselines for resource"):
            snapshot_holder_history_coverage_baselines((first, second), semantic_minute=20)

        duplicate_id = HolderHistoryCoverageBaseline(
            baseline_id=first.baseline_id,
            resource_id="case-b",
            at_tick=20,
            holder_actor_id=None,
            source_ref="checkpoint:other",
        )
        with self.assertRaisesRegex(ValueError, "duplicate holder history coverage baseline id"):
            snapshot_holder_history_coverage_baselines((first, duplicate_id), semantic_minute=20)

    def test_rejects_future_baseline_and_future_checkpoint(self):
        with self.assertRaisesRegex(ValueError, "later than checkpoint"):
            snapshot_holder_history_coverage_baselines(
                (self.baseline("case-a", "npc-a", at_tick=21),),
                semantic_minute=20,
            )

        snapshot = snapshot_holder_history_coverage_baselines(
            (self.baseline("case-a", "npc-a", at_tick=20),),
            semantic_minute=21,
        )
        with self.assertRaisesRegex(ValueError, "checkpoint is from the future"):
            restore_holder_history_coverage_baselines(snapshot, recovery_semantic_minute=20)

    def test_rejects_tampering_even_when_record_shape_remains_valid(self):
        snapshot = snapshot_holder_history_coverage_baselines(
            (self.baseline("case-a", "npc-a"),),
            semantic_minute=20,
        )
        tampered = copy.deepcopy(snapshot)
        tampered["baselines"][0]["holder_actor_id"] = "npc-b"
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            restore_holder_history_coverage_baselines(tampered)

    def test_restore_rejects_noncanonical_record_order(self):
        snapshot = snapshot_holder_history_coverage_baselines(
            (self.baseline("case-a", "npc-a"), self.baseline("case-b", None)),
            semantic_minute=20,
        )
        reversed_snapshot = copy.deepcopy(snapshot)
        reversed_snapshot["baselines"].reverse()

        # Reordering invalidates the signed generation before semantic order is considered.
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            restore_holder_history_coverage_baselines(reversed_snapshot)


if __name__ == "__main__":
    unittest.main()
