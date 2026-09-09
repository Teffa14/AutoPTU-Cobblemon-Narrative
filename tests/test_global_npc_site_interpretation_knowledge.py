import copy
import unittest

from tools.global_npc_memory import KnowledgeLedger, KnowledgeLedgerStore, SourceKind
from tools.global_npc_site_evidence import ObservationKind, SiteAccessState, SiteEvidenceLedger
from tools.global_npc_site_interpretation_knowledge import SiteInterpretationKnowledgeLedger
from tools.global_npc_site_observation_knowledge import SiteObservationKnowledgeLedger


class GlobalNpcSiteInterpretationKnowledgeTests(unittest.TestCase):
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
            observation_id="obs.wall-a",
            site_id="site.alpha",
            revision_id="site.alpha:r1",
            observer_id="researcher.a",
            semantic_minute=12,
            evidence_ref="feature.wall-a",
            kind=ObservationKind.FIXED_FEATURE,
            content="Lower stones use a different alignment from the visible upper wall.",
            provenance_root="field-note:wall-a",
        )
        evidence.record_observation(
            observation_id="obs.floor-cut",
            site_id="site.alpha",
            revision_id="site.alpha:r1",
            observer_id="researcher.a",
            semantic_minute=13,
            evidence_ref="feature.floor-cut",
            kind=ObservationKind.SPATIAL_RELATIONSHIP,
            content="The floor cut crosses the upper wall line and continues beneath it.",
            provenance_root="field-note:floor-cut",
        )
        evidence.record_interpretation(
            interpretation_id="interp.phase-one",
            site_id="site.alpha",
            actor_id="researcher.a",
            semantic_minute=15,
            observation_ids=("obs.wall-a", "obs.floor-cut"),
            claim="The lower masonry may belong to an earlier construction phase.",
            confidence=0.72,
        )
        knowledge = KnowledgeLedgerStore()
        knowledge.add(KnowledgeLedger("researcher.a"))
        knowledge.add(KnowledgeLedger("researcher.b"))
        observations = SiteObservationKnowledgeLedger()
        observations.materialize_observation(observation_id="obs.wall-a", site_evidence=evidence, knowledge_store=knowledge)
        observations.materialize_observation(observation_id="obs.floor-cut", site_evidence=evidence, knowledge_store=knowledge)
        return evidence, knowledge

    def test_interpretation_materializes_as_private_inference_with_all_source_refs(self):
        evidence, knowledge = self._state()
        bridge = SiteInterpretationKnowledgeLedger()
        record = bridge.materialize_interpretation(
            interpretation_id="interp.phase-one", site_evidence=evidence, knowledge_store=knowledge
        )
        claim = knowledge.require("researcher.a").claims[record.claim_id]
        self.assertEqual(claim.subject, "site-interpretation:site.alpha")
        self.assertEqual(claim.source_kind, SourceKind.INFERENCE)
        self.assertEqual(claim.source_agent_id, "researcher.a")
        self.assertEqual(claim.confidence, 72)
        self.assertEqual(record.observation_ids, ("obs.wall-a", "obs.floor-cut"))
        self.assertEqual(record.source_provenance_roots, ("field-note:floor-cut", "field-note:wall-a"))
        self.assertEqual(knowledge.require("researcher.b").claims, {})

    def test_interpreter_must_privately_know_every_supporting_observation(self):
        evidence, knowledge = self._state()
        knowledge.require("researcher.a").claims.pop("site-observation-claim:obs.floor-cut")
        with self.assertRaisesRegex(ValueError, "lacks explicit private knowledge"):
            SiteInterpretationKnowledgeLedger().materialize_interpretation(
                interpretation_id="interp.phase-one", site_evidence=evidence, knowledge_store=knowledge
            )

    def test_round_trip_revalidates_site_evidence_and_private_claim(self):
        evidence, knowledge = self._state()
        bridge = SiteInterpretationKnowledgeLedger()
        bridge.materialize_interpretation(
            interpretation_id="interp.phase-one", site_evidence=evidence, knowledge_store=knowledge
        )
        restored = SiteInterpretationKnowledgeLedger.restore(
            bridge.snapshot(), site_evidence=evidence, knowledge_store=knowledge, semantic_minute=15
        )
        self.assertEqual(restored.snapshot(), bridge.snapshot())

    def test_superseding_interpretation_preserves_old_claim_and_links_parent(self):
        evidence, knowledge = self._state()
        bridge = SiteInterpretationKnowledgeLedger()
        first = bridge.materialize_interpretation(
            interpretation_id="interp.phase-one", site_evidence=evidence, knowledge_store=knowledge
        )
        original = copy.deepcopy(knowledge.require("researcher.a").claims[first.claim_id])
        evidence.record_interpretation(
            interpretation_id="interp.phase-two",
            site_id="site.alpha",
            actor_id="researcher.a",
            semantic_minute=20,
            observation_ids=("obs.wall-a", "obs.floor-cut"),
            claim="An earlier construction phase is now the preferred explanation.",
            confidence=0.88,
            supersedes_id="interp.phase-one",
        )
        second = bridge.materialize_interpretation(
            interpretation_id="interp.phase-two", site_evidence=evidence, knowledge_store=knowledge
        )
        newer = knowledge.require("researcher.a").claims[second.claim_id]
        self.assertEqual(knowledge.require("researcher.a").claims[first.claim_id], original)
        self.assertEqual(newer.parent_claim_id, first.claim_id)
        self.assertEqual(newer.provenance_root, original.provenance_root)

    def test_supersession_requires_prior_private_inference_materialization(self):
        evidence, knowledge = self._state()
        evidence.record_interpretation(
            interpretation_id="interp.phase-two",
            site_id="site.alpha",
            actor_id="researcher.a",
            semantic_minute=20,
            observation_ids=("obs.wall-a", "obs.floor-cut"),
            claim="An earlier construction phase is now the preferred explanation.",
            confidence=0.88,
            supersedes_id="interp.phase-one",
        )
        with self.assertRaisesRegex(ValueError, "requires prior private inference"):
            SiteInterpretationKnowledgeLedger().materialize_interpretation(
                interpretation_id="interp.phase-two", site_evidence=evidence, knowledge_store=knowledge
            )

    def test_future_inference_rejected_at_restore_boundary(self):
        evidence, knowledge = self._state()
        bridge = SiteInterpretationKnowledgeLedger()
        bridge.materialize_interpretation(
            interpretation_id="interp.phase-one", site_evidence=evidence, knowledge_store=knowledge
        )
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            SiteInterpretationKnowledgeLedger.restore(
                bridge.snapshot(), site_evidence=evidence, knowledge_store=knowledge, semantic_minute=14
            )

    def test_tampered_private_inference_is_rejected(self):
        evidence, knowledge = self._state()
        bridge = SiteInterpretationKnowledgeLedger()
        record = bridge.materialize_interpretation(
            interpretation_id="interp.phase-one", site_evidence=evidence, knowledge_store=knowledge
        )
        claim = knowledge.require("researcher.a").claims[record.claim_id]
        knowledge.require("researcher.a").claims[record.claim_id] = claim.__class__(
            claim_id=claim.claim_id,
            subject=claim.subject,
            value="The site definitely proves a specific lost civilization existed.",
            source_kind=claim.source_kind,
            source_agent_id=claim.source_agent_id,
            semantic_minute=claim.semantic_minute,
            confidence=claim.confidence,
            provenance_root=claim.provenance_root,
            parent_claim_id=claim.parent_claim_id,
        )
        with self.assertRaisesRegex(ValueError, "diverges from source interpretation"):
            bridge.validate(site_evidence=evidence, knowledge_store=knowledge)

    def test_same_interpretation_is_idempotent(self):
        evidence, knowledge = self._state()
        bridge = SiteInterpretationKnowledgeLedger()
        first = bridge.materialize_interpretation(
            interpretation_id="interp.phase-one", site_evidence=evidence, knowledge_store=knowledge
        )
        second = bridge.materialize_interpretation(
            interpretation_id="interp.phase-one", site_evidence=evidence, knowledge_store=knowledge
        )
        self.assertEqual(first, second)
        self.assertEqual(len([c for c in knowledge.require("researcher.a").claims.values() if c.source_kind is SourceKind.INFERENCE]), 1)


if __name__ == "__main__":
    unittest.main()
