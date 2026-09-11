import unittest

from tools.autoptu_admitted_result_executor import execute_admitted_result_recording
from tools.autoptu_engine_authority_transition_plan import (
    AutoPTUAuthorityTransitionIntent,
    AutoPTUAuthorityTransitionKind,
)
from tools.autoptu_session_identity import AutoPTUSessionLedger, AutoPTUSessionState


class AutoPTUAdmittedResultExecutorTests(unittest.TestCase):
    def _engine_bound(self):
        ledger = AutoPTUSessionLedger()
        binding = ledger.request_session(
            handoff_request_id="handoff:pass416:1",
            world_action_ref="world-action:pass416:1",
            participant_refs=("npc:mara", "player:1"),
            rules_profile_id="ptu:standard",
            requested_at_minute=40,
        )
        ledger.bind_engine_session(binding.session_id, engine_session_ref="engine:pass416:1")
        return ledger, binding.session_id

    def _intent(self, session_id, result_ref="result:admitted:1"):
        return AutoPTUAuthorityTransitionIntent(
            session_id=session_id,
            kind=AutoPTUAuthorityTransitionKind.RECORD_ADMITTED_RESULT,
            evidence_ref=result_ref,
        )

    def test_exact_admitted_result_records_on_exact_engine_bound_session(self):
        ledger, session_id = self._engine_bound()
        execution = execute_admitted_result_recording(ledger, self._intent(session_id))
        restored = ledger.get(session_id)
        self.assertTrue(execution.changed)
        self.assertEqual(execution.state, AutoPTUSessionState.RESULT_RECORDED)
        self.assertEqual(restored.authoritative_result_ref, "result:admitted:1")
        self.assertEqual(restored.engine_session_ref, "engine:pass416:1")

    def test_same_exact_result_is_idempotent(self):
        ledger, session_id = self._engine_bound()
        intent = self._intent(session_id)
        first = execute_admitted_result_recording(ledger, intent)
        second = execute_admitted_result_recording(ledger, intent)
        self.assertTrue(first.changed)
        self.assertFalse(second.changed)
        self.assertEqual(ledger.get(session_id).authoritative_result_ref, "result:admitted:1")

    def test_conflicting_result_cannot_replace_recorded_result(self):
        ledger, session_id = self._engine_bound()
        execute_admitted_result_recording(ledger, self._intent(session_id))
        with self.assertRaisesRegex(ValueError, "different authoritative result"):
            execute_admitted_result_recording(ledger, self._intent(session_id, "result:other"))

    def test_non_record_intent_cannot_mutate_ledger(self):
        ledger, session_id = self._engine_bound()
        hold = AutoPTUAuthorityTransitionIntent(
            session_id=session_id,
            kind=AutoPTUAuthorityTransitionKind.HOLD_ENGINE_BOUND,
        )
        with self.assertRaisesRegex(ValueError, "accepts only RECORD_ADMITTED_RESULT"):
            execute_admitted_result_recording(ledger, hold)
        self.assertEqual(ledger.get(session_id).state, AutoPTUSessionState.ENGINE_BOUND)

    def test_blank_result_reference_fails_closed(self):
        ledger, session_id = self._engine_bound()
        with self.assertRaisesRegex(ValueError, "exact result reference"):
            execute_admitted_result_recording(ledger, self._intent(session_id, " "))
        self.assertEqual(ledger.get(session_id).state, AutoPTUSessionState.ENGINE_BOUND)

    def test_unknown_session_fails_closed(self):
        ledger, _ = self._engine_bound()
        with self.assertRaisesRegex(ValueError, "unknown AutoPTU session_id"):
            execute_admitted_result_recording(ledger, self._intent("session:missing"))

    def test_requested_session_cannot_skip_engine_binding(self):
        ledger = AutoPTUSessionLedger()
        binding = ledger.request_session(
            handoff_request_id="handoff:pass416:requested",
            world_action_ref="world-action:pass416:requested",
            participant_refs=("npc:teo", "player:1"),
            rules_profile_id="ptu:standard",
            requested_at_minute=41,
        )
        with self.assertRaisesRegex(ValueError, "ENGINE_BOUND"):
            execute_admitted_result_recording(ledger, self._intent(binding.session_id))
        self.assertEqual(ledger.get(binding.session_id).state, AutoPTUSessionState.REQUESTED)

    def test_executor_does_not_retire_session(self):
        ledger, session_id = self._engine_bound()
        execute_admitted_result_recording(ledger, self._intent(session_id))
        self.assertEqual(ledger.get(session_id).state, AutoPTUSessionState.RESULT_RECORDED)
        self.assertNotEqual(ledger.get(session_id).state, AutoPTUSessionState.RETIRED)


if __name__ == "__main__":
    unittest.main()
