from __future__ import annotations

import unittest

from tools.global_npc_publication import PublicPublication
from tools.global_npc_publication_revision import (
    PublicationRevision,
    PublicationRevisionRegistry,
    RevisionKind,
)


def publication(publication_id: str, minute: int, *, supersedes: str | None = None) -> PublicPublication:
    return PublicPublication(
        publication_id=publication_id,
        publisher_id="publisher-alpha",
        source_claim_id=f"claim-{publication_id}",
        service_id="service-public",
        channel_id="channel-public",
        published_minute=minute,
        scope_ids=frozenset({"scope-a"}),
        topic_id="route-status",
        supersedes_publication_id=supersedes,
    )


class PublicationRevisionRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = PublicationRevisionRegistry()
        self.registry.register(PublicationRevision(publication("bulletin-1", 10), RevisionKind.ORIGINAL))
        self.registry.register(PublicationRevision(publication("bulletin-2", 20, supersedes="bulletin-1"), RevisionKind.CORRECTION))
        self.registry.register(PublicationRevision(publication("bulletin-3", 30, supersedes="bulletin-2"), RevisionKind.UPDATE))

    def test_lineage_is_stable_and_current_revision_is_deterministic(self) -> None:
        self.assertEqual(self.registry.lineage("bulletin-3"), ("bulletin-1", "bulletin-2", "bulletin-3"))
        self.assertEqual(self.registry.root_publication_id("bulletin-2"), "bulletin-1")
        self.assertEqual(self.registry.current_publication_id("bulletin-1"), "bulletin-3")

    def test_partial_receipt_preserves_information_divergence(self) -> None:
        stale = self.registry.received_state("bulletin-1", {"bulletin-1"})
        corrected = self.registry.received_state("bulletin-1", {"bulletin-1", "bulletin-2"})
        current = self.registry.received_state("bulletin-1", {"bulletin-2", "bulletin-3"})
        unaware = self.registry.received_state("bulletin-1", set())

        self.assertEqual(stale.latest_received_publication_id, "bulletin-1")
        self.assertFalse(stale.current_revision_received)
        self.assertEqual(corrected.latest_received_kind, RevisionKind.CORRECTION)
        self.assertFalse(corrected.current_revision_received)
        self.assertEqual(current.latest_received_publication_id, "bulletin-3")
        self.assertTrue(current.current_revision_received)
        self.assertIsNone(unaware.latest_received_publication_id)

    def test_missing_predecessor_and_revision_forks_are_rejected(self) -> None:
        registry = PublicationRevisionRegistry()
        with self.assertRaises(KeyError):
            registry.register(PublicationRevision(publication("orphan", 20, supersedes="missing"), RevisionKind.CORRECTION))

        registry.register(PublicationRevision(publication("root", 10), RevisionKind.ORIGINAL))
        registry.register(PublicationRevision(publication("child-a", 20, supersedes="root"), RevisionKind.CORRECTION))
        with self.assertRaises(ValueError):
            registry.register(PublicationRevision(publication("child-b", 21, supersedes="root"), RevisionKind.UPDATE))

    def test_revision_identity_and_time_cannot_silently_change(self) -> None:
        registry = PublicationRevisionRegistry()
        registry.register(PublicationRevision(publication("root", 10), RevisionKind.ORIGINAL))
        with self.assertRaises(ValueError):
            registry.register(PublicationRevision(publication("early", 9, supersedes="root"), RevisionKind.CORRECTION))

        wrong_publisher = PublicPublication(
            publication_id="wrong-publisher",
            publisher_id="publisher-beta",
            source_claim_id="claim-x",
            service_id="service-public",
            channel_id="channel-public",
            published_minute=20,
            topic_id="route-status",
            supersedes_publication_id="root",
        )
        with self.assertRaises(ValueError):
            registry.register(PublicationRevision(wrong_publisher, RevisionKind.CORRECTION))

    def test_snapshot_restore_preserves_lineage(self) -> None:
        restored = PublicationRevisionRegistry.restore(self.registry.snapshot())
        self.assertEqual(restored.lineage("bulletin-3"), self.registry.lineage("bulletin-3"))
        self.assertEqual(restored.current_publication_id("bulletin-1"), "bulletin-3")

    def test_original_and_revision_shape_are_enforced(self) -> None:
        with self.assertRaises(ValueError):
            PublicationRevision(publication("bad-original", 20, supersedes="bulletin-1"), RevisionKind.ORIGINAL)
        with self.assertRaises(ValueError):
            PublicationRevision(publication("bad-correction", 20), RevisionKind.CORRECTION)

    def test_core_is_region_neutral_and_contains_no_tactical_resolution(self) -> None:
        import inspect
        import tools.global_npc_publication_revision as module

        source = inspect.getsource(module).lower()
        for forbidden in ("marea", "sendero", "puerto bruma", "loma clara", "knockback", "initiative", "damage pipeline"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
