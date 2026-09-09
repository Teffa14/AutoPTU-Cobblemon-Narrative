import copy
import hashlib
import json
import unittest

from tools.global_npc_memory import KnowledgeLedger, KnowledgeLedgerStore
from tools.global_npc_site_evidence import ObservationKind, SiteAccessState, SiteEvidenceLedger
from tools.global_npc_site_interpretation_knowledge import SiteInterpretationKnowledgeLedger
from tools.global_npc_site_observation_knowledge import SiteObservationKnowledgeLedger
from tools.persistent_world_evidence_checkpoint import (
    PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
    build_persistent_world_evidence_checkpoint,
    restore_persistent_world_evidence_checkpoint,
)


def redigest(snapshot: dict) -> dict:
    payload = {key: value for key, value in snapshot.items() if key != "sha256"}
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return payload | {"sha256": digest}


class PersistentWorldEvidenceCheckpointTests(unittest.TestCase):
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
        observations.materialize_observation(
            observation_id="obs.wall-a", site_evidence=evidence, knowledge_store=knowledge
        )
        observations.materialize_observation(
            observation_id="obs.floor-cut", site_evidence=evidence, knowledge_store=knowledge
        )
        interpretations = SiteInterpretationKnowledgeLedger()
        interpretations.materialize_interpretation(
            interpretation_id="interp.phase-one", site_evidence=evidence, knowledge_store=knowledge
        )
        return evidence, knowledge, observations, interpretations

    def test_round_trip_binds_world_evidence_to_matching_private_knowledge(self):
        evidence, knowledge, observations, interpretations = self._state()
        snapshot = build_persistent_world_evidence_checkpoint(
            semantic_minute=15,
            site_evidence=evidence,
            observation_knowledge=observations,
            interpretation_knowledge=interpretations,
            knowledge_store=knowledge,
        )
        self.assertEqual(snapshot["schema"], PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA)
        restored = restore_persistent_world_evidence_checkpoint(snapshot, knowledge_store=knowledge)
        self.assertEqual(restored.semantic_minute, 15)
        self.assertEqual(restored.site_evidence.snapshot(), evidence.snapshot())
        self.assertEqual(restored.observation_knowledge.snapshot(), observations.snapshot())
        self.assertEqual(restored.interpretation_knowledge.snapshot(), interpretations.snapshot())

    def test_digest_tampering_fails_closed(self):
        evidence, knowledge, observations, interpretations = self._state()
        snapshot = build_persistent_world_evidence_checkpoint(
            semantic_minute=15,
            site_evidence=evidence,
            observation_knowledge=observations,
            interpretation_knowledge=interpretations,
            knowledge_store=knowledge,
        )
        tampered = copy.deepcopy(snapshot)
        tampered["site_evidence"]["observations"][0]["content"] = "Different content"
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            restore_persistent_world_evidence_checkpoint(tampered, knowledge_store=knowledge)

    def test_redigested_world_tampering_still_fails_bridge_validation(self):
        evidence, knowledge, observations, interpretations = self._state()
        snapshot = build_persistent_world_evidence_checkpoint(
            semantic_minute=15,
            site_evidence=evidence,
            observation_knowledge=observations,
            interpretation_knowledge=interpretations,
            knowledge_store=knowledge,
        )
        tampered = copy.deepcopy(snapshot)
        tampered["site_evidence"]["observations"][0]["content"] = "Different content"
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "diverges from source evidence"):
            restore_persistent_world_evidence_checkpoint(tampered, knowledge_store=knowledge)

    def test_private_knowledge_from_another_recovery_unit_is_rejected(self):
        evidence, knowledge, observations, interpretations = self._state()
        snapshot = build_persistent_world_evidence_checkpoint(
            semantic_minute=15,
            site_evidence=evidence,
            observation_knowledge=observations,
            interpretation_knowledge=interpretations,
            knowledge_store=knowledge,
        )
        other = KnowledgeLedgerStore.restore(knowledge.snapshot())
        other.require("researcher.b").add(
            next(iter(other.require("researcher.a").claims.values())).__class__(
                claim_id="unrelated:later",
                subject="unrelated",
                value="Later state",
                source_kind=next(iter(other.require("researcher.a").claims.values())).source_kind,
                source_agent_id="researcher.b",
                semantic_minute=16,
                confidence=100,
                provenance_root="unrelated:later",
            )
        )
        with self.assertRaisesRegex(ValueError, "does not match private knowledge state"):
            restore_persistent_world_evidence_checkpoint(snapshot, knowledge_store=other)

    def test_future_site_evidence_cannot_enter_checkpoint(self):
        evidence, knowledge, observations, interpretations = self._state()
        with self.assertRaisesRegex(ValueError, "comes from the future"):
            build_persistent_world_evidence_checkpoint(
                semantic_minute=14,
                site_evidence=evidence,
                observation_knowledge=observations,
                interpretation_knowledge=interpretations,
                knowledge_store=knowledge,
            )

    def test_redigested_bridge_tampering_fails_closed(self):
        evidence, knowledge, observations, interpretations = self._state()
        snapshot = build_persistent_world_evidence_checkpoint(
            semantic_minute=15,
            site_evidence=evidence,
            observation_knowledge=observations,
            interpretation_knowledge=interpretations,
            knowledge_store=knowledge,
        )
        tampered = copy.deepcopy(snapshot)
        tampered["interpretation_knowledge"]["records"][0]["observation_ids"] = ["obs.wall-a"]
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "diverges from supporting interpretation"):
            restore_persistent_world_evidence_checkpoint(tampered, knowledge_store=knowledge)


if __name__ == "__main__":
    unittest.main()
