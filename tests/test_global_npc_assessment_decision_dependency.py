import unittest

from tools.global_npc_assessment_decision_dependency import (
    AssessmentDecisionDependencyRegistry,
    DecisionReviewStatus,
    affected_decisions,
    evaluate_decision_review_status,
    record_assessment_dependent_decision,
)
from tools.global_npc_evidence_custody import (
    CustodyAssessment,
    CustodyIntegrityStatus,
    EvidenceCustodyRegistry,
)
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind


class AssessmentDecisionDependencyTests(unittest.TestCase):
    def setUp(self):
        self.custody = EvidenceCustodyRegistry()
        self.old = CustodyAssessment(
            assessment_id="assessment-old",
            investigator_id="investigator",
            evidence_id="relay-sample",
            semantic_minute=10,
            status=CustodyIntegrityStatus.DOCUMENTATION_GAP,
            known_record_ids=(),
            support_claim_ids=(),
        )
        self.new = CustodyAssessment(
            assessment_id="assessment-new",
            investigator_id="investigator",
            evidence_id="relay-sample",
            semantic_minute=30,
            status=CustodyIntegrityStatus.CONTINUITY_SUPPORTED,
            known_record_ids=(),
            support_claim_ids=(),
            supersedes_assessment_id="assessment-old",
        )
        self.custody.add_assessment(self.old)
        self.custody.add_assessment(self.new)
        self.actor = KnowledgeLedger("route-authority")
        self.actor.add(self._assessment_claim("known-old", self.old, 15))
        self.registry = AssessmentDecisionDependencyRegistry()

    @staticmethod
    def _assessment_claim(claim_id, assessment, semantic_minute):
        return Claim(
            claim_id=claim_id,
            subject=f"custody:{assessment.evidence_id}",
            value=assessment.status.value,
            source_kind=SourceKind.REPORT,
            source_agent_id=assessment.investigator_id,
            semantic_minute=semantic_minute,
            confidence=80,
            provenance_root=f"custody-assessment:{assessment.assessment_id}",
        )

    def _record(self, decision_id="closure-order", minute=20):
        return record_assessment_dependent_decision(
            self.registry,
            self.custody,
            self.actor,
            decision_id=decision_id,
            basis_assessment_id="assessment-old",
            basis_claim_id="known-old",
            decision_kind="ROUTE_RESTRICTION",
            subject_ref="relay-road",
            semantic_minute=minute,
        )

    def test_records_exact_assessment_known_when_decision_was_made(self):
        decision = self._record()
        self.assertEqual(decision.actor_id, "route-authority")
        self.assertEqual(decision.basis_assessment_id, "assessment-old")
        self.assertEqual(decision.basis_claim_id, "known-old")

    def test_rejects_decision_basis_actor_does_not_have(self):
        outsider = KnowledgeLedger("outsider")
        with self.assertRaises(KeyError):
            record_assessment_dependent_decision(
                self.registry,
                self.custody,
                outsider,
                decision_id="bad",
                basis_assessment_id="assessment-old",
                basis_claim_id="known-old",
                decision_kind="ROUTE_RESTRICTION",
                subject_ref="relay-road",
                semantic_minute=20,
            )

    def test_rejects_future_basis_claim(self):
        self.actor.add(self._assessment_claim("future-old", self.old, 25))
        with self.assertRaises(ValueError):
            record_assessment_dependent_decision(
                self.registry,
                self.custody,
                self.actor,
                decision_id="bad-future",
                basis_assessment_id="assessment-old",
                basis_claim_id="future-old",
                decision_kind="ROUTE_RESTRICTION",
                subject_ref="relay-road",
                semantic_minute=20,
            )

    def test_new_assessment_marks_old_decision_affected(self):
        decision = self._record()
        affected = affected_decisions(
            self.registry,
            self.custody,
            superseding_assessment_id="assessment-new",
        )
        self.assertEqual(affected, (decision,))

    def test_actor_without_correction_remains_outdated(self):
        self._record()
        status = evaluate_decision_review_status(
            self.registry,
            self.custody,
            self.actor,
            decision_id="closure-order",
            as_of_minute=35,
        )
        self.assertEqual(status, DecisionReviewStatus.SUPERSEDED_NOT_RECEIVED)

    def test_received_correction_makes_review_eligible_without_auto_reversal(self):
        decision = self._record()
        self.actor.add(self._assessment_claim("known-new", self.new, 35))
        status = evaluate_decision_review_status(
            self.registry,
            self.custody,
            self.actor,
            decision_id="closure-order",
            as_of_minute=35,
        )
        self.assertEqual(status, DecisionReviewStatus.REVIEW_ELIGIBLE)
        self.assertEqual(self.registry.decisions[decision.decision_id], decision)
        self.assertEqual(decision.decision_kind, "ROUTE_RESTRICTION")

    def test_basis_is_current_before_superseding_assessment_exists(self):
        self._record()
        status = evaluate_decision_review_status(
            self.registry,
            self.custody,
            self.actor,
            decision_id="closure-order",
            as_of_minute=25,
        )
        self.assertEqual(status, DecisionReviewStatus.BASIS_CURRENT)

    def test_unrelated_assessment_does_not_affect_decision(self):
        unrelated = CustodyAssessment(
            assessment_id="assessment-other",
            investigator_id="other-investigator",
            evidence_id="other-sample",
            semantic_minute=32,
            status=CustodyIntegrityStatus.CONTINUITY_SUPPORTED,
            known_record_ids=(),
            support_claim_ids=(),
        )
        self.custody.add_assessment(unrelated)
        self._record()
        self.actor.add(self._assessment_claim("known-other", unrelated, 34))
        status = evaluate_decision_review_status(
            self.registry,
            self.custody,
            self.actor,
            decision_id="closure-order",
            as_of_minute=35,
        )
        self.assertEqual(status, DecisionReviewStatus.SUPERSEDED_NOT_RECEIVED)

    def test_registry_snapshot_round_trip(self):
        decision = self._record()
        restored = AssessmentDecisionDependencyRegistry.restore(self.registry.snapshot())
        self.assertEqual(restored.decisions[decision.decision_id], decision)


if __name__ == "__main__":
    unittest.main()
