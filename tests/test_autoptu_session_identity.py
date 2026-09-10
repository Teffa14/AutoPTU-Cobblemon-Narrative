import copy
import unittest

from tools.autoptu_session_identity import (
    AutoPTUSessionLedger,
    AutoPTUSessionState,
    restore_autoptu_sessions,
    snapshot_autoptu_sessions,
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


if __name__ == "__main__":
    unittest.main()
