import copy
import unittest

from tools.autoptu_session_identity import (
    AutoPTUSessionLedger,
    AutoPTUSessionState,
    restore_autoptu_sessions,
    snapshot_autoptu_sessions,
)
from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_autoptu_session_recovery import (
    reconcile_autoptu_session_checkpoint_with_agents,
    unresolved_engine_bound_sessions,
)


class AutoPTUSessionIdentityTests(unittest.TestCase):
    def request(self, ledger: AutoPTUSessionLedger, *, minute: int = 41):
        return ledger.request_session(
            handoff_request_id="handoff:sendero:incident:1",
            world_action_ref="world-action:sendero:incident:1",
            participant_refs=("ouros.npc.mara_veyra", "player:1"),
            rules_profile_id="ptu-ouros-authoritative",
            requested_at_minute=minute,
        )

    def mara(self, *, session_id: str | None, mode: AgentMode = AgentMode.AUTOPTU_BOUND):
        return NpcAgentState(
            agent_id="ouros.npc.mara_veyra",
            mode=mode,
            region_ref="ouros.marea",
            location_ref="ouros.marea.sendero_vidrio",
            active_autoptu_binding=session_id,
        )

    def test_replayed_handoff_request_keeps_exact_session_identity(self):
        ledger = AutoPTUSessionLedger()
        first = self.request(ledger)
        repeated = self.request(ledger)

        self.assertEqual(first, repeated)
        self.assertTrue(first.session_id.startswith("autoptu.session."))
        self.assertEqual(first.state, AutoPTUSessionState.REQUESTED)
        self.assertEqual(len(ledger.bindings()), 1)

    def test_same_request_id_with_changed_immutable_inputs_fails_closed(self):
        ledger = AutoPTUSessionLedger()
        self.request(ledger)

        with self.assertRaisesRegex(ValueError, "different AutoPTU session identity"):
            ledger.request_session(
                handoff_request_id="handoff:sendero:incident:1",
                world_action_ref="world-action:sendero:incident:DIFFERENT",
                participant_refs=("ouros.npc.mara_veyra", "player:1"),
                rules_profile_id="ptu-ouros-authoritative",
                requested_at_minute=41,
            )

    def test_restart_preserves_unresolved_engine_bound_session_without_inventing_result(self):
        ledger = AutoPTUSessionLedger()
        requested = self.request(ledger)
        ledger.bind_engine_session(requested.session_id, engine_session_ref="engine:battle:77")

        snapshot = snapshot_autoptu_sessions(ledger, semantic_minute=50)
        restored = restore_autoptu_sessions(snapshot, recovery_semantic_minute=50)
        binding = restored.get(requested.session_id)

        self.assertEqual(binding.state, AutoPTUSessionState.ENGINE_BOUND)
        self.assertEqual(binding.engine_session_ref, "engine:battle:77")
        self.assertIsNone(binding.authoritative_result_ref)
        with self.assertRaisesRegex(ValueError, "cannot retire before"):
            restored.retire(binding.session_id)

    def test_authoritative_result_is_idempotent_and_conflicting_result_is_rejected(self):
        ledger = AutoPTUSessionLedger()
        requested = self.request(ledger)
        ledger.bind_engine_session(requested.session_id, engine_session_ref="engine:battle:77")

        first = ledger.record_authoritative_result(requested.session_id, result_ref="result:77:final")
        repeated = ledger.record_authoritative_result(requested.session_id, result_ref="result:77:final")
        self.assertEqual(first, repeated)

        with self.assertRaisesRegex(ValueError, "different authoritative result"):
            ledger.record_authoritative_result(requested.session_id, result_ref="result:77:other")

        retired = ledger.retire(requested.session_id)
        self.assertEqual(retired.state, AutoPTUSessionState.RETIRED)

    def test_checkpoint_tamper_and_future_generation_fail_closed(self):
        ledger = AutoPTUSessionLedger()
        self.request(ledger)
        snapshot = snapshot_autoptu_sessions(ledger, semantic_minute=50)

        tampered = copy.deepcopy(snapshot)
        tampered["sessions"][0]["world_action_ref"] = "world-action:tampered"
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            restore_autoptu_sessions(tampered, recovery_semantic_minute=50)

        with self.assertRaisesRegex(ValueError, "newer than recovery cut"):
            restore_autoptu_sessions(snapshot, recovery_semantic_minute=49)

    def test_engine_binding_conflict_does_not_guess_after_restart(self):
        ledger = AutoPTUSessionLedger()
        requested = self.request(ledger)
        ledger.bind_engine_session(requested.session_id, engine_session_ref="engine:battle:77")
        restored = restore_autoptu_sessions(
            snapshot_autoptu_sessions(ledger, semantic_minute=50),
            recovery_semantic_minute=50,
        )

        with self.assertRaisesRegex(ValueError, "different engine session"):
            restored.bind_engine_session(requested.session_id, engine_session_ref="engine:battle:88")

    def test_world_agent_recovery_keeps_engine_bound_session_unresolved(self):
        ledger = AutoPTUSessionLedger()
        requested = self.request(ledger)
        ledger.bind_engine_session(requested.session_id, engine_session_ref="engine:battle:77")
        snapshot = snapshot_autoptu_sessions(ledger, semantic_minute=50)

        validation = reconcile_autoptu_session_checkpoint_with_agents(
            snapshot,
            recovery_semantic_minute=50,
            agents=(self.mara(session_id=requested.session_id),),
        )

        self.assertEqual(
            validation.active_agent_session_ids,
            (("ouros.npc.mara_veyra", requested.session_id),),
        )
        unresolved = unresolved_engine_bound_sessions(validation)
        self.assertEqual(tuple(item.session_id for item in unresolved), (requested.session_id,))
        self.assertIsNone(unresolved[0].authoritative_result_ref)

    def test_world_agent_recovery_rejects_missing_or_retired_session_reference(self):
        ledger = AutoPTUSessionLedger()
        requested = self.request(ledger)
        snapshot = snapshot_autoptu_sessions(ledger, semantic_minute=50)

        with self.assertRaisesRegex(ValueError, "unknown AutoPTU session_id"):
            reconcile_autoptu_session_checkpoint_with_agents(
                snapshot,
                recovery_semantic_minute=50,
                agents=(self.mara(session_id="autoptu.session.missing"),),
            )

        ledger.bind_engine_session(requested.session_id, engine_session_ref="engine:battle:77")
        ledger.record_authoritative_result(requested.session_id, result_ref="result:77:final")
        ledger.retire(requested.session_id)
        retired_snapshot = snapshot_autoptu_sessions(ledger, semantic_minute=51)
        with self.assertRaisesRegex(ValueError, "references retired AutoPTU session"):
            reconcile_autoptu_session_checkpoint_with_agents(
                retired_snapshot,
                recovery_semantic_minute=51,
                agents=(self.mara(session_id=requested.session_id),),
            )

    def test_world_agent_mode_and_binding_must_agree(self):
        ledger = AutoPTUSessionLedger()
        requested = self.request(ledger)
        snapshot = snapshot_autoptu_sessions(ledger, semantic_minute=50)

        with self.assertRaisesRegex(ValueError, "AUTOPTU_BOUND agent lacks session identity"):
            reconcile_autoptu_session_checkpoint_with_agents(
                snapshot,
                recovery_semantic_minute=50,
                agents=(self.mara(session_id=None),),
            )

        with self.assertRaisesRegex(ValueError, "non-AUTOPTU_BOUND agent carries session identity"):
            reconcile_autoptu_session_checkpoint_with_agents(
                snapshot,
                recovery_semantic_minute=50,
                agents=(self.mara(session_id=requested.session_id, mode=AgentMode.LOCAL_ACTIVE),),
            )

    def test_world_agent_must_be_participant_in_referenced_session(self):
        ledger = AutoPTUSessionLedger()
        other = ledger.request_session(
            handoff_request_id="handoff:other:1",
            world_action_ref="world-action:other:1",
            participant_refs=("ouros.npc.sela_orrin", "player:1"),
            rules_profile_id="ptu-ouros-authoritative",
            requested_at_minute=41,
        )
        snapshot = snapshot_autoptu_sessions(ledger, semantic_minute=50)

        with self.assertRaisesRegex(ValueError, "not a participant"):
            reconcile_autoptu_session_checkpoint_with_agents(
                snapshot,
                recovery_semantic_minute=50,
                agents=(self.mara(session_id=other.session_id),),
            )


if __name__ == "__main__":
    unittest.main()
