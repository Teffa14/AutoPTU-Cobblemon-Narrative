import copy
import unittest

from tools.global_npc_holder_history_baseline_issuance import (
    issue_holder_history_coverage_baselines_from_catalog_checkpoint,
)
from tools.global_npc_resources import ResourceState, WorldResource
from tools.world_resource_catalog_checkpoint import snapshot_world_resource_catalog


class GlobalNpcHolderHistoryBaselineIssuanceTests(unittest.TestCase):
    def setUp(self):
        self.resources = (
            WorldResource(
                resource_id="meter-b",
                capability_refs=frozenset({"SURVEY_METER"}),
                state=ResourceState.IN_USE,
                holder_actor_id="npc-b",
            ),
            WorldResource(
                resource_id="meter-a",
                capability_refs=frozenset({"SURVEY_METER"}),
                state=ResourceState.AVAILABLE,
                holder_actor_id=None,
            ),
        )
        self.snapshot = snapshot_world_resource_catalog(self.resources, semantic_minute=40)

    def test_issuance_is_deterministic_and_bound_to_exact_catalog_generation(self):
        first = issue_holder_history_coverage_baselines_from_catalog_checkpoint(self.snapshot)
        second = issue_holder_history_coverage_baselines_from_catalog_checkpoint(self.snapshot)

        self.assertEqual(first, second)
        self.assertEqual(tuple(item.resource_id for item in first), ("meter-a", "meter-b"))
        self.assertEqual(tuple(item.at_tick for item in first), (40, 40))
        self.assertEqual(first[0].holder_actor_id, None)
        self.assertEqual(first[1].holder_actor_id, "npc-b")
        for baseline in first:
            self.assertIn(self.snapshot["sha256"], baseline.source_ref)
            self.assertTrue(baseline.baseline_id.startswith("holder-baseline-"))

    def test_expected_generation_digest_mismatch_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "does not match expected generation"):
            issue_holder_history_coverage_baselines_from_catalog_checkpoint(
                self.snapshot,
                expected_catalog_sha256="0" * 64,
            )

    def test_tampered_catalog_fails_before_baseline_issuance(self):
        tampered = copy.deepcopy(self.snapshot)
        tampered["resources"][0]["holder_actor_id"] = "npc-x"
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            issue_holder_history_coverage_baselines_from_catalog_checkpoint(tampered)

    def test_future_catalog_fails_closed_for_recovery_cut(self):
        with self.assertRaisesRegex(ValueError, "from the future"):
            issue_holder_history_coverage_baselines_from_catalog_checkpoint(
                self.snapshot,
                recovery_semantic_minute=39,
            )


if __name__ == "__main__":
    unittest.main()
