import copy
import hashlib
import json
import unittest

from tools.global_npc_world_action_interruption_provenance_checkpoint import (
    WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
)
from tools.persistent_world_evidence_checkpoint import PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA
from tools.persistent_world_recovery_manifest import (
    PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA,
    PERSISTENT_WORLD_RECOVERY_MANIFEST_V1_SCHEMA,
    PERSISTENT_WORLD_RECOVERY_MANIFEST_V2_SCHEMA,
    build_persistent_world_recovery_manifest,
    reconcile_persistent_world_recovery_manifest,
)
from tools.resource_holder_transition_checkpoint import RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA
from tools.world_resource_catalog_checkpoint import WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA


def signed_checkpoint(schema: str, semantic_minute: int, *, marker: str) -> dict:
    payload = {"schema": schema, "semantic_minute": semantic_minute, "marker": marker}
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return payload | {"sha256": digest}


def redigest(snapshot: dict) -> dict:
    payload = {key: value for key, value in snapshot.items() if key != "sha256"}
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return payload | {"sha256": digest}


class PersistentWorldRecoveryManifestTests(unittest.TestCase):
    def _owners(self, minute: int = 41):
        return (
            signed_checkpoint(WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA, minute, marker="global-npc-v19"),
            signed_checkpoint(PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA, minute, marker="persistent-evidence-v2"),
            signed_checkpoint(WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA, minute, marker="resource-catalog-v1"),
            signed_checkpoint(RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA, minute, marker="holder-transitions-v1"),
        )

    def _build(self, minute: int = 41):
        global_checkpoint, evidence_checkpoint, resource_checkpoint, holder_checkpoint = self._owners(minute)
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=resource_checkpoint,
            resource_holder_transition_checkpoint=holder_checkpoint,
        )
        return manifest, global_checkpoint, evidence_checkpoint, resource_checkpoint, holder_checkpoint

    def test_v3_round_trip_selects_exact_four_owner_generation(self):
        manifest, global_checkpoint, evidence_checkpoint, resource_checkpoint, holder_checkpoint = self._build()
        self.assertEqual(manifest["schema"], PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA)
        restored = reconcile_persistent_world_recovery_manifest(
            manifest,
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=resource_checkpoint,
            resource_holder_transition_checkpoint=holder_checkpoint,
        )
        self.assertEqual(restored.semantic_minute, 41)
        self.assertEqual(restored.global_npc_checkpoint_sha256, global_checkpoint["sha256"])
        self.assertEqual(restored.persistent_world_evidence_checkpoint_sha256, evidence_checkpoint["sha256"])
        self.assertEqual(restored.world_resource_catalog_checkpoint_sha256, resource_checkpoint["sha256"])
        self.assertEqual(restored.resource_holder_transition_checkpoint_sha256, holder_checkpoint["sha256"])

    def test_build_rejects_any_owner_from_different_semantic_minute(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint, _ = self._owners()
        holder_checkpoint = signed_checkpoint(
            RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA, 42, marker="holder-transitions-v1"
        )
        with self.assertRaisesRegex(ValueError, "same semantic minute"):
            build_persistent_world_recovery_manifest(
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=resource_checkpoint,
                resource_holder_transition_checkpoint=holder_checkpoint,
            )

    def test_reconcile_rejects_valid_but_wrong_holder_generation(self):
        manifest, global_checkpoint, evidence_checkpoint, resource_checkpoint, _ = self._build()
        other_holder = signed_checkpoint(
            RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA, 41, marker="different-valid-holder-generation"
        )
        with self.assertRaisesRegex(ValueError, "resource holder transition checkpoint digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                manifest,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=resource_checkpoint,
                resource_holder_transition_checkpoint=other_holder,
            )

    def test_reconcile_rejects_tampered_manifest(self):
        manifest, global_checkpoint, evidence_checkpoint, resource_checkpoint, holder_checkpoint = self._build()
        tampered = copy.deepcopy(manifest)
        tampered["semantic_minute"] = 42
        with self.assertRaisesRegex(ValueError, "manifest digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                tampered,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=resource_checkpoint,
                resource_holder_transition_checkpoint=holder_checkpoint,
            )

    def test_reconcile_rejects_redigested_manifest_pointing_at_wrong_holder_digest(self):
        manifest, global_checkpoint, evidence_checkpoint, resource_checkpoint, holder_checkpoint = self._build()
        tampered = copy.deepcopy(manifest)
        tampered["resource_holder_transition_checkpoint_sha256"] = "0" * 64
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "resource holder transition checkpoint digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                tampered,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=resource_checkpoint,
                resource_holder_transition_checkpoint=holder_checkpoint,
            )

    def test_v3_reconcile_requires_holder_checkpoint_candidate(self):
        manifest, global_checkpoint, evidence_checkpoint, resource_checkpoint, _ = self._build()
        with self.assertRaisesRegex(ValueError, "requires resource holder transition checkpoint"):
            reconcile_persistent_world_recovery_manifest(
                manifest,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=resource_checkpoint,
            )

    def test_legacy_v2_remains_readable_without_fabricating_holder_journal(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint, _ = self._owners()
        payload = {
            "schema": PERSISTENT_WORLD_RECOVERY_MANIFEST_V2_SCHEMA,
            "semantic_minute": 41,
            "global_npc_checkpoint_sha256": global_checkpoint["sha256"],
            "persistent_world_evidence_checkpoint_sha256": evidence_checkpoint["sha256"],
            "world_resource_catalog_checkpoint_sha256": resource_checkpoint["sha256"],
        }
        legacy = redigest(payload)
        restored = reconcile_persistent_world_recovery_manifest(
            legacy,
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=resource_checkpoint,
        )
        self.assertEqual(restored.world_resource_catalog_checkpoint_sha256, resource_checkpoint["sha256"])
        self.assertIsNone(restored.resource_holder_transition_checkpoint_sha256)

    def test_legacy_v1_remains_readable_without_fabricating_newer_owners(self):
        global_checkpoint, evidence_checkpoint, _, _ = self._owners()
        payload = {
            "schema": PERSISTENT_WORLD_RECOVERY_MANIFEST_V1_SCHEMA,
            "semantic_minute": 41,
            "global_npc_checkpoint_sha256": global_checkpoint["sha256"],
            "persistent_world_evidence_checkpoint_sha256": evidence_checkpoint["sha256"],
        }
        legacy = redigest(payload)
        restored = reconcile_persistent_world_recovery_manifest(
            legacy,
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
        )
        self.assertIsNone(restored.world_resource_catalog_checkpoint_sha256)
        self.assertIsNone(restored.resource_holder_transition_checkpoint_sha256)

    def test_manifest_requires_current_holder_checkpoint_schema(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint, _ = self._owners()
        legacy_holder = signed_checkpoint(
            "OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V0", 41, marker="legacy-holder"
        )
        with self.assertRaisesRegex(ValueError, "requires schema"):
            build_persistent_world_recovery_manifest(
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=resource_checkpoint,
                resource_holder_transition_checkpoint=legacy_holder,
            )


if __name__ == "__main__":
    unittest.main()
