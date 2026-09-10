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
    build_persistent_world_recovery_manifest,
    reconcile_persistent_world_recovery_manifest,
)


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
    def _pair(self, minute: int = 41):
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
        return global_checkpoint, evidence_checkpoint

    def test_manifest_round_trip_selects_exact_checkpoint_pair(self):
        global_checkpoint, evidence_checkpoint = self._pair()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
        )
        self.assertEqual(manifest["schema"], PERSISTENT_WORLD_RECOVERY_MANIFEST_SCHEMA)

        restored = reconcile_persistent_world_recovery_manifest(
            manifest,
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
        )
        self.assertEqual(restored.semantic_minute, 41)
        self.assertEqual(restored.global_npc_checkpoint_sha256, global_checkpoint["sha256"])
        self.assertEqual(restored.persistent_world_evidence_checkpoint_sha256, evidence_checkpoint["sha256"])

    def test_manifest_rejects_checkpoint_pair_from_different_semantic_minutes(self):
        global_checkpoint, evidence_checkpoint = self._pair()
        evidence_checkpoint = signed_checkpoint(
            PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA,
            42,
            marker="persistent-evidence-v2",
        )
        with self.assertRaisesRegex(ValueError, "same semantic minute"):
            build_persistent_world_recovery_manifest(
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
            )

    def test_reconcile_rejects_valid_but_wrong_checkpoint_generation(self):
        global_checkpoint, evidence_checkpoint = self._pair()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
        )
        other_global = signed_checkpoint(
            WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
            41,
            marker="different-valid-global-checkpoint",
        )
        with self.assertRaisesRegex(ValueError, "global NPC checkpoint digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                manifest,
                global_npc_checkpoint=other_global,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
            )

    def test_reconcile_rejects_tampered_manifest(self):
        global_checkpoint, evidence_checkpoint = self._pair()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
        )
        tampered = copy.deepcopy(manifest)
        tampered["semantic_minute"] = 42
        with self.assertRaisesRegex(ValueError, "manifest digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                tampered,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
            )

    def test_reconcile_rejects_redigested_manifest_pointing_at_wrong_owner_digest(self):
        global_checkpoint, evidence_checkpoint = self._pair()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
        )
        tampered = copy.deepcopy(manifest)
        tampered["persistent_world_evidence_checkpoint_sha256"] = "0" * 64
        tampered = redigest(tampered)
        with self.assertRaisesRegex(ValueError, "persistent world evidence checkpoint digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                tampered,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
            )

    def test_reconcile_rejects_candidate_with_invalid_owner_digest_before_manifest_match(self):
        global_checkpoint, evidence_checkpoint = self._pair()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_checkpoint,
            persistent_world_evidence_checkpoint=evidence_checkpoint,
        )
        broken = copy.deepcopy(evidence_checkpoint)
        broken["marker"] = "tampered-without-owner-redigest"
        with self.assertRaisesRegex(ValueError, "persistent world evidence checkpoint digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                manifest,
                global_npc_checkpoint=global_checkpoint,
                persistent_world_evidence_checkpoint=broken,
            )

    def test_manifest_requires_current_owner_schemas(self):
        global_checkpoint, evidence_checkpoint = self._pair()
        legacy = signed_checkpoint(
            "OUROS_NPC_WORLD_CHECKPOINT_V18",
            41,
            marker="legacy-global",
        )
        with self.assertRaisesRegex(ValueError, "requires schema"):
            build_persistent_world_recovery_manifest(
                global_npc_checkpoint=legacy,
                persistent_world_evidence_checkpoint=evidence_checkpoint,
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
            )


if __name__ == "__main__":
    unittest.main()
