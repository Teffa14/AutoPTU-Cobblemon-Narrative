import unittest

from tools.autoptu_engine_authority_report import AutoPTUEngineAuthorityReconciliation
from tools.autoptu_engine_authority_transition_plan import (
    AutoPTUAuthorityTransitionKind,
    plan_engine_authority_followup,
)


class AutoPTUEngineAuthorityTransitionPlanTests(unittest.TestCase):
    def _reconciliation(self):
        return AutoPTUEngineAuthorityReconciliation(
            active_session_ids=("session:active",),
            completed_results=(("session:completed", "result:verified-later"),),
            unknown_session_ids=("session:unknown",),
            explicitly_abandoned=(("session:abandoned", "authorization:abandon:1"),),
            reported_session_ids=(
                "session:abandoned",
                "session:active",
                "session:completed",
                "session:unknown",
            ),
        )

    def test_completed_report_waits_until_exact_result_ref_is_admitted(self):
        plan = plan_engine_authority_followup(self._reconciliation())
        intent = plan.for_session("session:completed")
        self.assertEqual(intent.kind, AutoPTUAuthorityTransitionKind.HOLD_PENDING_RESULT_ADMISSION)
        self.assertEqual(intent.evidence_ref, "result:verified-later")

    def test_exact_admitted_result_can_be_planned_for_recording(self):
        plan = plan_engine_authority_followup(
            self._reconciliation(),
            admitted_result_refs=("result:verified-later",),
        )
        intent = plan.for_session("session:completed")
        self.assertEqual(intent.kind, AutoPTUAuthorityTransitionKind.RECORD_ADMITTED_RESULT)
        self.assertEqual(intent.evidence_ref, "result:verified-later")

    def test_unrelated_admitted_result_does_not_unlock_completion(self):
        plan = plan_engine_authority_followup(
            self._reconciliation(),
            admitted_result_refs=("result:other-session",),
        )
        self.assertEqual(
            plan.for_session("session:completed").kind,
            AutoPTUAuthorityTransitionKind.HOLD_PENDING_RESULT_ADMISSION,
        )

    def test_active_session_stays_engine_bound(self):
        plan = plan_engine_authority_followup(self._reconciliation())
        self.assertEqual(
            plan.for_session("session:active").kind,
            AutoPTUAuthorityTransitionKind.HOLD_ENGINE_BOUND,
        )

    def test_unknown_session_is_quarantined_for_review_without_result(self):
        plan = plan_engine_authority_followup(self._reconciliation())
        intent = plan.for_session("session:unknown")
        self.assertEqual(intent.kind, AutoPTUAuthorityTransitionKind.QUARANTINE_FOR_ENGINE_UNKNOWN)
        self.assertIsNone(intent.evidence_ref)

    def test_explicit_abandonment_does_not_become_result_or_retirement(self):
        plan = plan_engine_authority_followup(self._reconciliation())
        intent = plan.for_session("session:abandoned")
        self.assertEqual(intent.kind, AutoPTUAuthorityTransitionKind.HOLD_PENDING_ABANDONMENT_POLICY)
        self.assertEqual(intent.evidence_ref, "authorization:abandon:1")

    def test_plan_requires_exact_reconciliation_coverage(self):
        malformed = AutoPTUEngineAuthorityReconciliation(
            active_session_ids=("session:active",),
            completed_results=(),
            unknown_session_ids=(),
            explicitly_abandoned=(),
            reported_session_ids=("session:active", "session:missing"),
        )
        with self.assertRaisesRegex(ValueError, "does not cover reconciliation exactly"):
            plan_engine_authority_followup(malformed)

    def test_blank_admitted_result_ref_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "cannot be blank"):
            plan_engine_authority_followup(self._reconciliation(), admitted_result_refs=(" ",))


if __name__ == "__main__":
    unittest.main()
