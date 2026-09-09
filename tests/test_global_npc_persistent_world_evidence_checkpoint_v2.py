import copy
import hashlib
import json
import unittest

from tools.global_npc_memory import KnowledgeLedger, KnowledgeLedgerStore
from tools.global_npc_portable_find_resource_binding import PortableFindResourceBindingLedger
from tools.global_npc_resources import ResourceState, WorldResource
from tools.global_npc_site_evidence import ObservationKind, SiteAccessState, SiteEvidenceLedger
from tools.global_npc_site_interpretation_knowledge import SiteInterpretationKnowledgeLedger
from tools.global_npc_site_observation_knowledge import SiteObservationKnowledgeLedger
from tools.persistent_world_evidence_checkpoint import (
    LEGACY_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
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


class PersistentWorldEvidenceCheckpointV2Tests(unittest.TestCase):
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
            observation_id="obs.find.alpha",
            site_id="site.alpha",
            revision_id="site.alpha:r1",
            observer_id="researcher.a",
            semantic_minute=12,
            evidence_ref="find.field-number.17",
            kind=ObservationKind.PORTABLE_FIND,
            content="A tagged fragment is documented before removal.",
            provenance_root="field-note:alpha:17",
        )

        knowledge = KnowledgeLedgerStore()
        knowledge.add(KnowledgeLedger("researcher.a"))
        observations = SiteObservationKnowledgeLedger()
        observations.materialize_observation(
            observation_id="obs.find.alpha",
            site_evidence=evidence,
            knowledge_store=knowledge,
        )
        interpretations = SiteInterpretationKnowledgeLedger()

        resources = {
            "resource.find.alpha": WorldResource(
                resource_id="resource.find.alpha",
                capability_refs=frozenset({"portable_find"}),
                quantity=1,
                state=ResourceState.AVAILABLE,
                location_ref="site.alpha",
            )
        }
        bindings = PortableFindResourceBindingLedger()
        bindings.bind(
            binding_id="binding.find.alpha",
            observation_id="obs.find.alpha",
            resource_id="resource.find.alpha",
            bound_at_semantic_minute=13,
            bound_by_actor_id="researcher.a",
            authority_ref="field-register:alpha",
            site_evidence=evidence,
            declared_resources=resources,
        )
        return evidence, knowledge, observations, interpretations, resources, bindings

    def test_v2_round_trip_restores_portable_find_binding(self):
        evidence, knowledge, observations, interpretations, resources, bindings = self._state()
        snapshot = build_persistent_world_evidence_checkpoint(
            semantic_minute=15,
            site_evidence=evidence,
            observation_knowledge=observations,
            interpretation_knowledge=interpretations,
            knowledge_store=knowledge,
            portable_find_bindings=bindings,
            declared_resources=resources,
        )
        self.assertEqual(snapshot["schema"], PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA)
        restored = restore_persistent_world_evidence_checkpoint(
            snapshot,
            knowledge_store=knowledge,
            declared_resources=resources,
        )
        self.assertEqual(
            restored.portable_find_bindings.binding_for_resource("resource.find.alpha").observation_id,
            "obs.find.alpha",
        )
        self.assertIsNotNone(restored.resource_identity_catalog_sha256)

    def test_v2_rejects_different_declared_resource_identity_catalog(self):
        evidence, knowledge, observations, interpretations, resources, bindings = self._state()
        snapshot = build_persistent_world_evidence_checkpoint(
            semantic_minute=15,
            site_evidence=evidence,
            observation_knowledge=observations,
            interpretation_knowledge=interpretations,
            knowledge_store=knowledge,
            portable_find_bindings=bindings,
            declared_resources=resources,
        )
        wrong_resources = {
            "resource.other": WorldResource(
                resource_id="resource.other",
                capability_refs=frozenset({"portable_find"}),
            )
        }
        with self.assertRaisesRegex(ValueError, "does not match declared resource identities"):
            restore_persistent_world_evidence_checkpoint(
                snapshot,
                knowledge_store=knowledge,
                declared_resources=wrong_resources,
            )

    def test_v2_allows_mutable_resource_state_to_change_when_identity_is_stable(self):
        evidence, knowledge, observations, interpretations, resources, bindings = self._state()
        snapshot = build_persistent_world_evidence_checkpoint(
            semantic_minute=15,
            site_evidence=evidence,
            observation_knowledge=observations,
            interpretation_knowledge=interpretations,
            knowledge_store=knowledge,
            portable_find_bindings=bindings,
            declared_resources=resources,
        )
        moved_resources = {
            "resource.find.alpha": WorldResource(
                resource_id="resource.find.alpha",
                capability_refs=frozenset({"portable_find"}),
                quantity=1,
                state=ResourceState.IN_USE,
                location_ref="archive.receiving",
                holder_actor_id="curator.b",
            )
        }
        restored = restore_persistent_world_evidence_checkpoint(
            snapshot,
            knowledge_store=knowledge,
            declared_resources=moved_resources,
        )
        self.assertEqual(
            restored.portable_find_bindings.binding_for_resource("resource.find.alpha").observation_id,
            "obs.find.alpha",
        )

    def test_redigested_binding_tampering_still_fails_closed(self):
        evidence, knowledge, observations, interpretations, resources, bindings = self._state()
        snapshot = build_persistent_world_evidence_checkpoint(
            semantic_minute=15,
            site_evidence=evidence,
            observation_knowledge=observations,
            interpretation_knowledge=interpretations,
            knowledge_store=knowledge,
            portable_find_bindings=bindings,
            declared_resources=resources,
        )
        tampered = copy.deepcopy(snapshot)
        tampered["portable_find_bindings"]["bindings"][0]["observation_sha256"] = "0" * 64
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "observation provenance mismatch"):
            restore_persistent_world_evidence_checkpoint(
                tampered,
                knowledge_store=knowledge,
                declared_resources=resources,
            )

    def test_v1_restore_migrates_with_empty_portable_find_binding_ledger(self):
        evidence, knowledge, observations, interpretations, _, _ = self._state()
        current = build_persistent_world_evidence_checkpoint(
            semantic_minute=15,
            site_evidence=evidence,
            observation_knowledge=observations,
            interpretation_knowledge=interpretations,
            knowledge_store=knowledge,
        )
        legacy = copy.deepcopy(current)
        legacy["schema"] = LEGACY_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA
        legacy.pop("resource_identity_catalog_sha256")
        legacy.pop("portable_find_bindings")
        legacy = redigest(legacy)
        restored = restore_persistent_world_evidence_checkpoint(
            legacy,
            knowledge_store=knowledge,
        )
        self.assertEqual(restored.portable_find_bindings.bindings, {})
        self.assertIsNone(restored.resource_identity_catalog_sha256)


if __name__ == "__main__":
    unittest.main()
