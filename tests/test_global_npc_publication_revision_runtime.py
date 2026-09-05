import inspect
import unittest
from pathlib import Path

from tools.global_npc_publication_revision_runtime import replay_fixture


class GlobalNpcPublicationRevisionRuntimeTests(unittest.TestCase):
    def test_fixture_preserves_divergent_revision_receipt_histories(self):
        payload = replay_fixture(Path("implementation/global-npc-publication-revision-runtime-fixture-v1.json"))
        self.assertEqual(payload["fixture_id"], "GLOBAL_NPC_PUBLICATION_REVISION_RUNTIME_V1")
        by_id = {row["event_id"]: row for row in payload["results"]}

        self.assertEqual(by_id["publish.original"]["scheduled_agent_ids"], ["agent.amber", "agent.birch"])
        self.assertEqual(by_id["publish.correction"]["scheduled_agent_ids"], ["agent.amber", "agent.cinder"])
        self.assertEqual(by_id["restart.runtime"]["status"], "RESTORED")

        self.assertEqual(
            by_id["lineage.amber"]["received_publication_ids"],
            ["publication.route.v1", "publication.route.v2"],
        )
        self.assertTrue(by_id["lineage.amber"]["current_revision_received"])

        self.assertEqual(by_id["lineage.birch"]["received_publication_ids"], ["publication.route.v1"])
        self.assertEqual(by_id["lineage.birch"]["latest_received_kind"], "ORIGINAL")
        self.assertFalse(by_id["lineage.birch"]["current_revision_received"])

        self.assertEqual(by_id["lineage.cinder"]["received_publication_ids"], ["publication.route.v2"])
        self.assertEqual(by_id["lineage.cinder"]["latest_received_kind"], "CORRECTION")
        self.assertTrue(by_id["lineage.cinder"]["current_revision_received"])

        self.assertEqual(by_id["lineage.delta"]["received_publication_ids"], [])
        self.assertFalse(by_id["lineage.delta"]["current_revision_received"])

    def test_each_revision_wakes_only_actual_receivers(self):
        payload = replay_fixture(Path("implementation/global-npc-publication-revision-runtime-fixture-v1.json"))
        by_id = {row["event_id"]: row for row in payload["results"]}

        self.assertEqual(
            by_id["cycle.original"]["receipts"],
            [["agent.amber", "publication.route.v1"], ["agent.birch", "publication.route.v1"]],
        )
        self.assertEqual(by_id["cycle.original"]["wake_statuses"], ["WAKE_SCHEDULED", "WAKE_SCHEDULED"])

        self.assertEqual(
            by_id["cycle.correction"]["receipts"],
            [["agent.amber", "publication.route.v2"], ["agent.cinder", "publication.route.v2"]],
        )
        self.assertEqual(by_id["cycle.correction"]["wake_statuses"], ["WAKE_SCHEDULED", "WAKE_SCHEDULED"])

    def test_belief_history_is_not_retroactively_overwritten(self):
        payload = replay_fixture(Path("implementation/global-npc-publication-revision-runtime-fixture-v1.json"))
        by_id = {row["event_id"]: row for row in payload["results"]}

        self.assertEqual(by_id["belief.amber"]["status"], "CONTESTED")
        self.assertEqual(by_id["belief.birch"]["status"], "SUPPORTED")
        self.assertEqual(by_id["belief.birch"]["preferred_value"], "CLOSED")
        self.assertEqual(by_id["belief.cinder"]["status"], "SUPPORTED")
        self.assertEqual(by_id["belief.cinder"]["preferred_value"], "OPEN")
        self.assertEqual(by_id["belief.delta"]["status"], "UNKNOWN")

    def test_correction_audience_is_resolved_independently(self):
        payload = replay_fixture(Path("implementation/global-npc-publication-revision-runtime-fixture-v1.json"))
        by_id = {row["event_id"]: row for row in payload["results"]}
        original = set(by_id["publish.original"]["scheduled_agent_ids"])
        correction = set(by_id["publish.correction"]["scheduled_agent_ids"])

        self.assertIn("agent.birch", original)
        self.assertNotIn("agent.birch", correction)
        self.assertNotIn("agent.cinder", original)
        self.assertIn("agent.cinder", correction)

    def test_core_remains_region_neutral_and_outside_tactical_resolution(self):
        import tools.global_npc_publication_revision_runtime as module

        source = inspect.getsource(module)
        for forbidden in ("Marea", "Sendero", "Puerto Bruma", "Loma Clara"):
            self.assertNotIn(forbidden, source)
        for tactical in ("damageDealt", "initiativeOrder", "knockbackDistance", "moveAccuracy"):
            self.assertNotIn(tactical, source)


if __name__ == "__main__":
    unittest.main()
