import copy
import unittest

from tools.global_npc_memory import KnowledgeLedger, KnowledgeLedgerStore, SourceKind
from tools.global_npc_site_evidence import ObservationKind, SiteAccessState, SiteEvidenceLedger
from tools.global_npc_site_observation_knowledge import SiteObservationKnowledgeLedger


class GlobalNpcSiteObservationKnowledgeTests(unittest.TestCase):
    def _state(self):
        evidence = SiteEvidenceLedger()
        evidence.record_revision(
            revision_id="site.alpha:r1",
            site_id="site.alpha",
            semantic_minute=10,
            access_state=SiteAccessState.OPEN,
            change_kind="BASELINE_DOCUMENTED",
            source_ref="survey:first",
        )
        evidence.record_observation(
            observation_id="obs.upper-floor",
            site_id="site.alpha",
            revision_id="site.alpha:r1",
            observer_id="researcher.a",
            semantic_minute=12,
            evidence_ref="feature.upper-floor",
            kind=ObservationKind.FIXED_FEATURE,
            content="Visible floor aligns with the upper chamber walls.",
            provenance_root="field-note:upper-floor",
        )
        knowledge = KnowledgeLedgerStore()
        knowledge.add(KnowledgeLedger("researcher.a"))
        knowledge.add(KnowledgeLedger("researcher.b"))
        return evidence, knowledge

    def test_direct_observation_materializes_only_to_observer_with_provenance(self):
        evidence, knowledge = self._state()
        bridge = SiteObservationKnowledgeLedger()
        record = bridge.materialize_observation(
            observation_id="obs.upper-floor",
            site_evidence=evidence,
            knowledge_store=knowledge,
        )

        claim = knowledge.require("researcher.a").claims[record.claim_id]
        self.assertEqual(claim.subject, "site-observation:obs.upper-floor")
        self.assertEqual(claim.value, evidence.observations["obs.upper-floor"].content)
        self.assertEqual(claim.source_kind, SourceKind.DIRECT_OBSERVATION)
        self.assertEqual(claim.source_agent_id, "researcher.a")
        self.assertEqual(claim.semantic_minute, 12)
        self.assertEqual(claim.provenance_root, "field-note:upper-floor")
        self.assertEqual(knowledge.require("researcher.b").claims, {})

    def test_materialization_round_trip_validates_against_both_owners(self):
        evidence, knowledge = self._state()
        bridge = SiteObservationKnowledgeLedger()
        bridge.materialize_observation(
            observation_id="obs.upper-floor",
            site_evidence=evidence,
            knowledge_store=knowledge,
        )
        restored = SiteObservationKnowledgeLedger.restore(
            bridge.snapshot(),
            site_evidence=evidence,
            knowledge_store=knowledge,
            semantic_minute=12,
        )
        self.assertEqual(restored.snapshot(), bridge.snapshot())

    def test_later_site_revision_does_not_rewrite_private_observation_claim(self):
        evidence, knowledge = self._state()
        bridge = SiteObservationKnowledgeLedger()
        record = bridge.materialize_observation(
            observation_id="obs.upper-floor",
            site_evidence=evidence,
            knowledge_store=knowledge,
        )
        original_claim = copy.deepcopy(knowledge.require("researcher.a").claims[record.claim_id])

        evidence.record_revision(
            revision_id="site.alpha:r2",
            site_id="site.alpha",
            previous_revision_id="site.alpha:r1",
            semantic_minute=30,
            access_state=SiteAccessState.RESTRICTED,
            change_kind="LOWER_MASONRY_EXPOSED",
            source_ref="event:floor-exposure",
        )

        bridge.validate(site_evidence=evidence, knowledge_store=knowledge, semantic_minute=30)
        self.assertEqual(knowledge.require("researcher.a").claims[record.claim_id], original_claim)

    def test_restore_rejects_materialization_to_non_observer(self):
        evidence, knowledge = self._state()
        bridge = SiteObservationKnowledgeLedger()
        bridge.materialize_observation(
            observation_id="obs.upper-floor",
            site_evidence=evidence,
            knowledge_store=knowledge,
        )
        snapshot = bridge.snapshot()
        snapshot["records"][0]["agent_id"] = "researcher.b"
        with self.assertRaisesRegex(ValueError, "non-observer"):
            SiteObservationKnowledgeLedger.restore(
                snapshot,
                site_evidence=evidence,
                knowledge_store=knowledge,
            )

    def test_restore_rejects_tampered_private_claim_content(self):
        evidence, knowledge = self._state()
        bridge = SiteObservationKnowledgeLedger()
        record = bridge.materialize_observation(
            observation_id="obs.upper-floor",
            site_evidence=evidence,
            knowledge_store=knowledge,
        )
        original = knowledge.require("researcher.a").claims[record.claim_id]
        knowledge.require("researcher.a").claims[record.claim_id] = original.__class__(
            claim_id=original.claim_id,
            subject=original.subject,
            value="A later interpretation silently replaced the field observation.",
            source_kind=original.source_kind,
            source_agent_id=original.source_agent_id,
            semantic_minute=original.semantic_minute,
            confidence=original.confidence,
            provenance_root=original.provenance_root,
        )
        with self.assertRaisesRegex(ValueError, "diverges from source evidence"):
            bridge.validate(site_evidence=evidence, knowledge_store=knowledge)

    def test_future_materialization_rejected_at_restore_boundary(self):
        evidence, knowledge = self._state()
        bridge = SiteObservationKnowledgeLedger()
        bridge.materialize_observation(
            observation_id="obs.upper-floor",
            site_evidence=evidence,
            knowledge_store=knowledge,
        )
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            SiteObservationKnowledgeLedger.restore(
                bridge.snapshot(),
                site_evidence=evidence,
                knowledge_store=knowledge,
                semantic_minute=11,
            )

    def test_missing_managed_private_ledger_blocks_materialization(self):
        evidence, _ = self._state()
        knowledge = KnowledgeLedgerStore()
        bridge = SiteObservationKnowledgeLedger()
        with self.assertRaisesRegex(ValueError, "no managed private knowledge ledger"):
            bridge.materialize_observation(
                observation_id="obs.upper-floor",
                site_evidence=evidence,
                knowledge_store=knowledge,
            )

    def test_same_observation_is_idempotent_without_duplicate_claim(self):
        evidence, knowledge = self._state()
        bridge = SiteObservationKnowledgeLedger()
        first = bridge.materialize_observation(
            observation_id="obs.upper-floor",
            site_evidence=evidence,
            knowledge_store=knowledge,
        )
        second = bridge.materialize_observation(
            observation_id="obs.upper-floor",
            site_evidence=evidence,
            knowledge_store=knowledge,
        )
        self.assertEqual(first, second)
        self.assertEqual(len(knowledge.require("researcher.a").claims), 1)


if __name__ == "__main__":
    unittest.main()
