import unittest

from tools.autoptu_engine_authority_report import (
    AutoPTUEngineAuthorityReport,
    AutoPTUEngineAuthorityState,
    reconcile_engine_authority_reports,
)
from tools.autoptu_session_identity import AutoPTUSessionLedger, snapshot_autoptu_sessions
from tools.global_npc_autoptu_session_recovery import reconcile_autoptu_session_checkpoint_with_agents
from tools.global_npc_ai import AgentMode, NpcAgentState


class AutoPTUEngineAuthorityReportTests(unittest.TestCase):
    def _validation(self):
        ledger = AutoPTUSessionLedger()
        binding = ledger.request_session(
            handoff_request_id="handoff:authority:1",
            world_action_ref="world-action:authority:1",
            participant_refs=("npc:a",),
            rules_profile_id="ptu:audit:ordinary",
            requested_at_minute=40,
        )
        ledger.bind_engine_session(binding.session_id, engine_session_ref="engine:battle:9001")
        checkpoint = snapshot_autoptu_sessions(ledger, semantic_minute=60)
        agent = NpcAgentState(
            agent_id="npc:a",
            mode=AgentMode.AUTOPTU_BOUND,
            region_ref="ouros.test",
            location_ref="ouros.test.site",
            risk_tolerance=50,
            energy=100,
            active_autoptu_binding=binding.session_id,
        )
        validation = reconcile_autoptu_session_checkpoint_with_agents(
            checkpoint,
            recovery_semantic_minute=60,
            agents=(agent,),
        )
        return validation, binding.session_id

    def _report(self, session_id, state, **kwargs):
        return AutoPTUEngineAuthorityReport(
            session_id=session_id,
            engine_session_ref=kwargs.pop("engine_session_ref", "engine:battle:9001"),
            authority_ref=kwargs.pop("authority_ref", "autoptu.authority.primary"),
            authority_report_ref=kwargs.pop("authority_report_ref", f"engine-report:{state.value.lower()}:1"),
            observed_at_minute=kwargs.pop("observed_at_minute", 59),
            state=state,
            authoritative_result_ref=kwargs.pop("authoritative_result_ref", None),
            abandonment_authorization_ref=kwargs.pop("abandonment_authorization_ref", None),
        )

    def test_active_report_preserves_unresolved_classification(self):
        validation, session_id = self._validation()
        result = reconcile_engine_authority_reports(
            validation,
            (self._report(session_id, AutoPTUEngineAuthorityState.ACTIVE),),
        )
        self.assertEqual(result.active_session_ids, (session_id,))
        self.assertEqual(result.completed_results, ())
        self.assertEqual(validation.ledger.get(session_id).state.value, "ENGINE_BOUND")

    def test_completed_report_requires_explicit_result_reference(self):
        validation, session_id = self._validation()
        report = self._report(
            session_id,
            AutoPTUEngineAuthorityState.COMPLETED,
            authoritative_result_ref="autoptu.result:9001:sha256:abc",
        )
        result = reconcile_engine_authority_reports(validation, (report,))
        self.assertEqual(
            result.completed_results,
            ((session_id, "autoptu.result:9001:sha256:abc"),),
        )
        self.assertEqual(validation.ledger.get(session_id).state.value, "ENGINE_BOUND")

    def test_completed_without_result_fails_closed(self):
        validation, session_id = self._validation()
        with self.assertRaisesRegex(ValueError, "authoritative_result_ref is required"):
            reconcile_engine_authority_reports(
                validation,
                (self._report(session_id, AutoPTUEngineAuthorityState.COMPLETED),),
            )

    def test_unknown_does_not_become_result_or_abandonment(self):
        validation, session_id = self._validation()
        result = reconcile_engine_authority_reports(
            validation,
            (self._report(session_id, AutoPTUEngineAuthorityState.UNKNOWN),),
        )
        self.assertEqual(result.unknown_session_ids, (session_id,))
        self.assertEqual(result.completed_results, ())
        self.assertEqual(result.explicitly_abandoned, ())

    def test_abandonment_requires_explicit_authorization_reference(self):
        validation, session_id = self._validation()
        with self.assertRaisesRegex(ValueError, "abandonment_authorization_ref is required"):
            reconcile_engine_authority_reports(
                validation,
                (self._report(session_id, AutoPTUEngineAuthorityState.EXPLICITLY_ABANDONED),),
            )
        result = reconcile_engine_authority_reports(
            validation,
            (
                self._report(
                    session_id,
                    AutoPTUEngineAuthorityState.EXPLICITLY_ABANDONED,
                    abandonment_authorization_ref="ouros.authorization:abandon:9001",
                ),
            ),
        )
        self.assertEqual(
            result.explicitly_abandoned,
            ((session_id, "ouros.authorization:abandon:9001"),),
        )

    def test_engine_reference_mismatch_fails_closed(self):
        validation, session_id = self._validation()
        with self.assertRaisesRegex(ValueError, "engine_session_ref mismatch"):
            reconcile_engine_authority_reports(
                validation,
                (
                    self._report(
                        session_id,
                        AutoPTUEngineAuthorityState.ACTIVE,
                        engine_session_ref="engine:battle:different",
                    ),
                ),
            )

    def test_future_report_fails_closed(self):
        validation, session_id = self._validation()
        with self.assertRaisesRegex(ValueError, "newer than recovery cut"):
            reconcile_engine_authority_reports(
                validation,
                (
                    self._report(
                        session_id,
                        AutoPTUEngineAuthorityState.ACTIVE,
                        observed_at_minute=61,
                    ),
                ),
            )

    def test_multiple_reports_for_one_session_fail_closed(self):
        validation, session_id = self._validation()
        with self.assertRaisesRegex(ValueError, "multiple authority reports"):
            reconcile_engine_authority_reports(
                validation,
                (
                    self._report(session_id, AutoPTUEngineAuthorityState.ACTIVE, authority_report_ref="report:1"),
                    self._report(session_id, AutoPTUEngineAuthorityState.UNKNOWN, authority_report_ref="report:2"),
                ),
            )


if __name__ == "__main__":
    unittest.main()
