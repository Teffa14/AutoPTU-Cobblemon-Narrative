import hashlib
import json
import unittest

from tools.autoptu_session_identity import AutoPTUSessionLedger, snapshot_autoptu_sessions
from tools.global_npc_world_action_interruption_provenance_checkpoint import (
    WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
)
from tools.holder_history_coverage_baseline_checkpoint import (
    HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_SCHEMA,
)
from tools.persistent_world_evidence_checkpoint import PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA
from tools.persistent_world_recovery_manifest import (
    build_persistent_world_recovery_manifest,
    build_persistent_world_recovery_manifest_v5,
)
from tools.persistent_world_v5_autoptu_session_recovery import (
    reconcile_v5_autoptu_session_recovery_boundary,
)
from tools.resource_holder_transition_checkpoint import RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA
from tools.world_resource_catalog_checkpoint import WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA


def signed(payload: dict) -> dict:
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return payload | {"sha256": digest}


def owner(schema: str, minute: int, marker: str) -> dict:
    return signed({"schema": schema, "semantic_minute": minute, "marker": marker})


def agent_row(agent_id: str, session_id: str | None) -> dict:
    return {
        "agent_id": agent_id,
        "mode": "AUTOPTU_BOUND" if session_id is not None else "OFFSCREEN_NAMED",
        "region_ref": "ouros.test",
        "location_ref": "ouros.test.site",
        "risk_tolerance": 50,
        "energy": 100,
        "knowledge": [],
        "permissions": [],
        "memory_refs": [],
        "active_autoptu_binding": session_id,
    }


class PersistentWorldV5AutoPTUSessionRecoveryTests(unittest.TestCase):
    def _generation(self, minute: int = 90):
        ledger = AutoPTUSessionLedger()
        binding = ledger.request_session(
            handoff_request_id="handoff:survey-yard:1",
            world_action_ref="world-action:survey-yard:1",
            participant_refs=("npc:a",),
            rules_profile_id="ptu:audit:ordinary",
            requested_at_minute=84,
        )
        ledger.bind_engine_session(binding.session_id, engine_session_ref="engine:battle:771")
        session_cp = snapshot_autoptu_sessions(ledger, semantic_minute=minute)
        global_cp = signed(
            {
                "schema": WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
                "semantic_minute": minute,
                "agents": [agent_row("npc:a", binding.session_id), agent_row("npc:b", None)],
            }
        )
        evidence_cp = owner(PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_SCHEMA, minute, "evidence")
        resource_cp = owner(WORLD_RESOURCE_CATALOG_CHECKPOINT_SCHEMA, minute, "resources")
        holder_cp = owner(RESOURCE_HOLDER_TRANSITION_CHECKPOINT_SCHEMA, minute, "holders")
        baseline_cp = owner(HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_SCHEMA, minute, "baselines")
        manifest = build_persistent_world_recovery_manifest_v5(
            global_npc_checkpoint=global_cp,
            persistent_world_evidence_checkpoint=evidence_cp,
            world_resource_catalog_checkpoint=resource_cp,
            resource_holder_transition_checkpoint=holder_cp,
            holder_history_coverage_baseline_checkpoint=baseline_cp,
            autoptu_session_checkpoint=session_cp,
        )
        return manifest, global_cp, evidence_cp, resource_cp, holder_cp, baseline_cp, session_cp, binding.session_id

    def _reconcile(self, generation):
        manifest, global_cp, evidence_cp, resource_cp, holder_cp, baseline_cp, session_cp, _ = generation
        return reconcile_v5_autoptu_session_recovery_boundary(
            manifest,
            global_npc_checkpoint=global_cp,
            persistent_world_evidence_checkpoint=evidence_cp,
            world_resource_catalog_checkpoint=resource_cp,
            resource_holder_transition_checkpoint=holder_cp,
            holder_history_coverage_baseline_checkpoint=baseline_cp,
            autoptu_session_checkpoint=session_cp,
        )

    def test_exact_v5_generation_binds_selected_agent_state_to_selected_session_owner(self):
        generation = self._generation()
        result = self._reconcile(generation)
        session_id = generation[-1]
        self.assertEqual(result.manifest.semantic_minute, 90)
        self.assertEqual(result.session_validation.active_agent_session_ids, (("npc:a", session_id),))
        self.assertEqual(result.unresolved_engine_bound_session_ids, (session_id,))

    def test_valid_same_minute_session_checkpoint_from_other_generation_fails_before_binding(self):
        generation = self._generation()
        manifest, global_cp, evidence_cp, resource_cp, holder_cp, baseline_cp, _, _ = generation
        other = AutoPTUSessionLedger()
        other_binding = other.request_session(
            handoff_request_id="handoff:other:1",
            world_action_ref="world-action:other:1",
            participant_refs=("npc:a",),
            rules_profile_id="ptu:audit:ordinary",
            requested_at_minute=84,
        )
        other.bind_engine_session(other_binding.session_id, engine_session_ref="engine:battle:other")
        other_cp = snapshot_autoptu_sessions(other, semantic_minute=90)
        with self.assertRaisesRegex(ValueError, "AutoPTU session checkpoint digest mismatch"):
            reconcile_v5_autoptu_session_recovery_boundary(
                manifest,
                global_npc_checkpoint=global_cp,
                persistent_world_evidence_checkpoint=evidence_cp,
                world_resource_catalog_checkpoint=resource_cp,
                resource_holder_transition_checkpoint=holder_cp,
                holder_history_coverage_baseline_checkpoint=baseline_cp,
                autoptu_session_checkpoint=other_cp,
            )

    def test_valid_same_minute_global_checkpoint_from_other_generation_fails_before_agent_parse(self):
        generation = self._generation()
        manifest, _, evidence_cp, resource_cp, holder_cp, baseline_cp, session_cp, _ = generation
        wrong_global = signed(
            {
                "schema": WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
                "semantic_minute": 90,
                "agents": "malformed-but-in-another-valid-generation",
            }
        )
        with self.assertRaisesRegex(ValueError, "global NPC checkpoint digest mismatch"):
            reconcile_v5_autoptu_session_recovery_boundary(
                manifest,
                global_npc_checkpoint=wrong_global,
                persistent_world_evidence_checkpoint=evidence_cp,
                world_resource_catalog_checkpoint=resource_cp,
                resource_holder_transition_checkpoint=holder_cp,
                holder_history_coverage_baseline_checkpoint=baseline_cp,
                autoptu_session_checkpoint=session_cp,
            )

    def test_selected_generation_fails_closed_when_agent_references_unknown_session(self):
        _, _, evidence_cp, resource_cp, holder_cp, baseline_cp, session_cp, _ = self._generation()
        inconsistent_global = signed(
            {
                "schema": WORLD_ACTION_INTERRUPTION_PROVENANCE_CHECKPOINT_SCHEMA,
                "semantic_minute": 90,
                "agents": [agent_row("npc:a", "autoptu.session.unknown")],
            }
        )
        manifest = build_persistent_world_recovery_manifest_v5(
            global_npc_checkpoint=inconsistent_global,
            persistent_world_evidence_checkpoint=evidence_cp,
            world_resource_catalog_checkpoint=resource_cp,
            resource_holder_transition_checkpoint=holder_cp,
            holder_history_coverage_baseline_checkpoint=baseline_cp,
            autoptu_session_checkpoint=session_cp,
        )
        with self.assertRaisesRegex(ValueError, "unknown AutoPTU session_id"):
            reconcile_v5_autoptu_session_recovery_boundary(
                manifest,
                global_npc_checkpoint=inconsistent_global,
                persistent_world_evidence_checkpoint=evidence_cp,
                world_resource_catalog_checkpoint=resource_cp,
                resource_holder_transition_checkpoint=holder_cp,
                holder_history_coverage_baseline_checkpoint=baseline_cp,
                autoptu_session_checkpoint=session_cp,
            )

    def test_v4_cannot_enter_exact_session_recovery_boundary(self):
        generation = self._generation()
        _, global_cp, evidence_cp, resource_cp, holder_cp, baseline_cp, session_cp, _ = generation
        v4 = build_persistent_world_recovery_manifest(
            global_npc_checkpoint=global_cp,
            persistent_world_evidence_checkpoint=evidence_cp,
            world_resource_catalog_checkpoint=resource_cp,
            resource_holder_transition_checkpoint=holder_cp,
            holder_history_coverage_baseline_checkpoint=baseline_cp,
        )
        with self.assertRaisesRegex(ValueError, "requires V5 manifest"):
            reconcile_v5_autoptu_session_recovery_boundary(
                v4,
                global_npc_checkpoint=global_cp,
                persistent_world_evidence_checkpoint=evidence_cp,
                world_resource_catalog_checkpoint=resource_cp,
                resource_holder_transition_checkpoint=holder_cp,
                holder_history_coverage_baseline_checkpoint=baseline_cp,
                autoptu_session_checkpoint=session_cp,
            )


if __name__ == "__main__":
    unittest.main()
