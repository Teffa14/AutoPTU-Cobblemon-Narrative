import hashlib
import json
import unittest

from tools.autoptu_session_identity import AUTOPTU_SESSION_CHECKPOINT_SCHEMA
from tools.global_npc_world_action_interruption_provenance_checkpoint import (
    WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
)
from tools.holder_history_coverage_baseline_checkpoint import (
    HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_SCHEMA,
)
from tools.persistent_world_evidence_checkpoint import PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA
from tools.persistent_world_recovery_manifest import (
    PERSISTENT_WORLD_RECOVERY_MANIFEST_V4_SCHEMA,
    PERSISTENT_WORLD_RECOVERY_MANIFEST_V5_SCHEMA,
    build_persistent_world_recovery_manifest,
    build_persistent_world_recovery_manifest_v5,
    reconcile_persistent_world_recovery_manifest,
)
from tools.resource_holder_transition_checkpoint import RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA
from tools.world_resource_catalog_checkpoint import WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA


def signed_checkpoint(schema: str, semantic_minute: int, marker: str) -> dict:
    payload = {"schema": schema, "semantic_minute": semantic_minute, "marker": marker}
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return payload | {"sha256": digest}


class PersistentWorldRecoveryManifestV5Tests(unittest.TestCase):
    def _owners(self, minute: int = 73):
        return (
            signed_checkpoint(WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA, minute, "global"),
            signed_checkpoint(PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA, minute, "evidence"),
            signed_checkpoint(WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA, minute, "resources"),
            signed_checkpoint(RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA, minute, "holders"),
            signed_checkpoint(HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_SCHEMA, minute, "baselines"),
            signed_checkpoint(AUTOPTU_SESSION_CHECKPOINT_SCHEMA, minute, "autoptu-sessions"),
        )

    def test_v5_round_trip_selects_exact_six_owner_generation(self):
        global_cp, evidence_cp, resource_cp, holder_cp, baseline_cp, session_cp = self._owners()
        manifest = build_persistent_world_recovery_manifest_v5(
            global_npc_checkpoint=global_cp,
            persistent_world_evidence_checkpoint=evidence_cp,
            world_resource_catalog_checkpoint=resource_cp,
            resource_holder_transition_checkpoint=holder_cp,
            holder_history_coverage_baseline_checkpoint=baseline_cp,
            autoptu_session_checkpoint=session_cp,
        )
        self.assertEqual(manifest["schema"], PERSISTENT_WORLD_RECOVERY_MANIFEST_V5_SCHEMA)
        restored = reconcile_persistent_world_recovery_manifest(
            manifest,
            global_npc_checkpoint=global_cp,
            persistent_world_evidence_checkpoint=evidence_cp,
            world_resource_catalog_checkpoint=resource_cp,
            resource_holder_transition_checkpoint=holder_cp,
            holder_history_coverage_baseline_checkpoint=baseline_cp,
            autoptu_session_checkpoint=session_cp,
        )
        self.assertEqual(restored.semantic_minute, 73)
        self.assertEqual(restored.autoptu_session_checkpoint_sha256, session_cp["sha256"])

    def test_v5_requires_session_checkpoint_from_same_semantic_minute(self):
        global_cp, evidence_cp, resource_cp, holder_cp, baseline_cp, _ = self._owners()
        session_cp = signed_checkpoint(AUTOPTU_SESSION_CHECKPOINT_SCHEMA, 74, "autoptu-sessions")
        with self.assertRaisesRegex(ValueError, "same semantic minute"):
            build_persistent_world_recovery_manifest_v5(
                global_npc_checkpoint=global_cp,
                persistent_world_evidence_checkpoint=evidence_cp,
                world_resource_catalog_checkpoint=resource_cp,
                resource_holder_transition_checkpoint=holder_cp,
                holder_history_coverage_baseline_checkpoint=baseline_cp,
                autoptu_session_checkpoint=session_cp,
            )

    def test_v5_rejects_valid_session_checkpoint_from_wrong_generation(self):
        global_cp, evidence_cp, resource_cp, holder_cp, baseline_cp, session_cp = self._owners()
        manifest = build_persistent_world_recovery_manifest_v5(
            global_npc_checkpoint=global_cp,
            persistent_world_evidence_checkpoint=evidence_cp,
            world_resource_catalog_checkpoint=resource_cp,
            resource_holder_transition_checkpoint=holder_cp,
            holder_history_coverage_baseline_checkpoint=baseline_cp,
            autoptu_session_checkpoint=session_cp,
        )
        wrong_session_cp = signed_checkpoint(AUTOPTU_SESSION_CHECKPOINT_SCHEMA, 73, "other-autoptu-generation")
        with self.assertRaisesRegex(ValueError, "AutoPTU session checkpoint digest mismatch"):
            reconcile_persistent_world_recovery_manifest(
                manifest,
                global_npc_checkpoint=global_cp,
                persistent_world_evidence_checkpoint=evidence_cp,
                world_resource_catalog_checkpoint=resource_cp,
                resource_holder_transition_checkpoint=holder_cp,
                holder_history_coverage_baseline_checkpoint=baseline_cp,
                autoptu_session_checkpoint=wrong_session_cp,
            )

    def test_v5_reconcile_requires_session_checkpoint(self):
        global_cp, evidence_cp, resource_cp, holder_cp, baseline_cp, session_cp = self._owners()
        manifest = build_persistent_world_recovery_manifest_v5(
            global_npc_checkpoint=global_cp,
            persistent_world_evidence_checkpoint=evidence_cp,
            world_resource_catalog_checkpoint=resource_cp,
            resource_holder_transition_checkpoint=holder_cp,
            holder_history_coverage_baseline_checkpoint=baseline_cp,
            autoptu_session_checkpoint=session_cp,
        )
        with self.assertRaisesRegex(ValueError, "requires AutoPTU session checkpoint"):
            reconcile_persistent_world_recovery_manifest(
                manifest,
                global_npc_checkpoint=global_cp,
                persistent_world_evidence_checkpoint=evidence_cp,
                world_resource_catalog_checkpoint=resource_cp,
                resource_holder_transition_checkpoint=holder_cp,
                holder_history_coverage_baseline_checkpoint=baseline_cp,
            )

    def test_v4_generation_remains_five_owner_and_rejects_session_injection(self):
        global_cp, evidence_cp, resource_cp, holder_cp, baseline_cp, session_cp = self._owners()
        manifest = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_cp,
            persistent_world_evidence_checkpoint=evidence_cp,
            world_resource_catalog_checkpoint=resource_cp,
            resource_holder_transition_checkpoint=holder_cp,
            holder_history_coverage_baseline_checkpoint=baseline_cp,
        )
        self.assertEqual(manifest["schema"], PERSISTENT_WORLD_RECOVERY_MANIFEST_V4_SCHEMA)
        with self.assertRaisesRegex(ValueError, "V4 recovery manifest did not select AutoPTU session checkpoint"):
            reconcile_persistent_world_recovery_manifest(
                manifest,
                global_npc_checkpoint=global_cp,
                persistent_world_evidence_checkpoint=evidence_cp,
                world_resource_catalog_checkpoint=resource_cp,
                resource_holder_transition_checkpoint=holder_cp,
                holder_history_coverage_baseline_checkpoint=baseline_cp,
                autoptu_session_checkpoint=session_cp,
            )


if __name__ == "__main__":
    unittest.main()
