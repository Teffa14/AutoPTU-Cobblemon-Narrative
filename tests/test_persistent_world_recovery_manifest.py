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
    build_persistent_world_recovery_manifest,
    reconcile_persistent_world_recovery_manifest,
)
from tools.world_resource_catalog_checkpoint import WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA


def signed_checkpoint(schema: str, semantic_minute: int, *, marker: str) -> dict:
    payload = {
        "schema": schema,
        "semantic_minute": semantic_minute,
        "marker": marker,
    }
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
    def _triple(self, minute: int = 41):
        global_checkpoint = signed_checkpoint(
            WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
            minute,
            marker="global-npc-v19",
        )
        evidence_checkpoint = signed_checkpoint(
            PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
            minute,
            marker="persistent-evidence-v2",
        )
        resource_checkpoint = signed_checkpoint(
            WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
            minute,
            marker="resource-catalog-v1",
        )
        return global_checkpoint, evidence_checkpoint, resource_checkpoint

    def test_manifest_round_trip_selects_exact_checkpoint_generation(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint = self._triple()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=resource_checkpoint,
        )
        self.assertEqual(manifest["schema"], PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA)

        restored = reconcile_persistent_world_recovery_manifest(
            manifest,
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=resource_checkpoint,
        )
        self.assertEqual(restored.semantic_minute, 41)
        self.assertEqual(restored.global_npc_checkpoint_sha256, global_checkpoint["sha256"])
        self.assertEqual(restored.persistent_world_evidence_checkpoint_sha256, evidence_checkpoint["sha256"])
        self.assertEqual(restored.world_resource_catalog_checkpoint_sha256, resource_checkpoint["sha256"])

    def test_manifest_rejects_any_owner_from_different_semantic_minute(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint = self._triple()
        resource_checkpoint = signed_checkpoint(
            WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
            42,
            marker="resource-catalog-v1",
        )
        with self.assertRaisesRegex(ValueError, "same semantic minute"):
            build_persistent_world_recovery_manifest(
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=resource_checkpoint,
            )

    def test_reconcile_rejects_valid_but_wrong_checkpoint_generation(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint = self._triple()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=resource_checkpoint,
        )
        other_resource = signed_checkpoint(
            WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA,
            41,
            marker="different-valid-resource-generation",
        )
        with self.assertRaisesRegex(ValueError, "world resource catalog checkpoint digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                manifest,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=other_resource,
            )

    def test_reconcile_rejects_tampered_manifest(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint = self._triple()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=resource_checkpoint,
        )
        tampered = copy.deepcopy(manifest)
        tampered["semantic_minute"] = 42
        with self.assertRaisesRegex(ValueError, "manifest digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                tampered,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=resource_checkpoint,
            )

    def test_reconcile_rejects_redigested_manifest_pointing_at_wrong_resource_digest(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint = self._triple()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=resource_checkpoint,
        )
        tampered = copy.deepcopy(manifest)
        tampered["world_resource_catalog_checkpoint_sha256"] = "0" * 64
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "world resource catalog checkpoint digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                tampered,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=resource_checkpoint,
            )

    def test_reconcile_rejects_candidate_with_invalid_owner_digest_before_manifest_match(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint = self._triple()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=resource_checkpoint,
        )
        broken = copy.deepcopy(resource_checkpoint)
        broken["marker"] = "tampered-without-owner-redigest"
        with self.assertRaisesRegex(ValueError, "world resource catalog checkpoint digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                manifest,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=broken,
            )

    def test_v2_reconcile_requires_resource_catalog_candidate(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint = self._triple()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
            world_resource_catalog_checkpoint=resource_checkpoint,
        )
        with self.assertRaisesRegex(ValueError, "requires world resource catalog checkpoint"):
            reconcile_persistent_world_recovery_manifest(
                manifest,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
            )

    def test_legacy_v1_manifest_remains_readable_without_fabricating_resource_owner(self):
        global_checkpoint, evidence_checkpoint, _ = self._triple()
        payload = {
            "schema": PERSISTENT_WORLD_RECOVERY_MANIFEST_V1_SCHEMA,
            "semantic_minute": 41,
            "global_npc_checkpoint_sha256": global_checkpoint["sha256"],
            "persistent_world_evidence_checkpoint_sha256": evidence_checkpoint["sha256"],
        }
        legacy = payload | {
            "sha256": hashlib.sha256(
                json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
            ).hexdigest()
        }
        restored = reconcile_persistent_world_recovery_manifest(
            legacy,
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
        )
        self.assertIsNone(restored.world_resource_catalog_checkpoint_sha256)

    def test_manifest_requires_current_owner_schemas(self):
        global_checkpoint, evidence_checkpoint, resource_checkpoint = self._triple()
        legacy_resource = signed_checkpoint(
            "OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V0",
            41,
            marker="legacy-resource",
        )
        with self.assertRaisesRegex(ValueError, "requires schema"):
            build_persistent_world_recovery_manifest(
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
                world_resource_catalog_checkpoint=legacy_resource,
            )

        legacy_evidence = signed_checkpoint(
            "OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V1",
            41,
            marker="legacy-evidence",
        )
        with self.assertRaisesRegex(ValueError, "requires schema"):
            build_persistent_world_recovery_manifest(
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=legacy_evidence,
                world_resource_catalog_checkpoint=resource_checkpoint,
            )


if __name__ == "__main__":
    unittest.main()
