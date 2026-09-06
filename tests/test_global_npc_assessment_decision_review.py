import unittest

from tools.global_npc_assessment_decision_dependency import (
    AssessmentDecisionDependencyRegistry,
    record_assessment_dependent_decision,
)
from tools.global_npc_assessment_decision_review import (
    AssessmentDecisionReviewRegistry,
    DecisionReviewOutcome,
    record_assessment_decision_review,
)
from tools.global_npc_evidence_custody import CustodyAssessment, CustodyIntegrityStatus, EvidenceCustodyRegistry
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind


class AssessmentDecisionReviewTests(unittest.TestCase):
    def setUp(self):
        self.custody = EvidenceCustodyRegistry()
        self.old = CustodyAssessment(
            assessment_id="old", investigator_id="investigator", evidence_id="sample",
            semantic_minute=10, status=CustodyIntegrityStatus.DOCUMENTATION_GAP,
            known_record_ids=(), support_claim_ids=(),
        )
        self.new = CustodyAssessment(
            assessment_id="new", investigator_id="investigator", evidence_id="sample",
            semantic_minute=30, status=CustodyIntegrityStatus.CONTINUITY_SUPPORTED,
            known_record_ids=(), support_claim_ids=(), supersedes_assessment_id="old",
        )
        self.custody.add_assessment(self.old)
        self.custody.add_assessment(self.new)
        self.actor = KnowledgeLedger("authority")
        self.actor.add(self._claim("old-claim", self.old, 15))
        self.dependencies = AssessmentDecisionDependencyRegistry()
        record_assessment_dependent_decision(
            self.dependencies, self.custody, self.actor,
            decision_id="closure", basis_assessment_id="old", basis_claim_id="old-claim",
            decision_kind="ROUTE_RESTRICTION", subject_ref="relay-road", semantic_minute=20,
        )
        self.reviews = AssessmentDecisionReviewRegistry()

    @staticmethod
    def _claim(claim_id, assessment, minute):
        return Claim(
            claim_id=claim_id,
            subject=f"custody:{assessment.evidence_id}",
            value=assessment.status.value,
            source_kind=SourceKind.REPORT,
            source_agent_id=assessment.investigator_id,
            semantic_minute=minute,
            confidence=80,
            provenance_root=f"custody-assessment:{assessment.assessment_id}",
        )

    def test_records_explicit_review_after_correction_receipt(self):
        self.actor.add(self._claim("new-claim", self.new, 35))
        review = record_assessment_decision_review(
            self.reviews, self.dependencies, self.custody, self.actor,
            review_id="review-1", decision_id="closure", superseding_assessment_id="new",
            superseding_claim_id="new-claim", outcome=DecisionReviewOutcome.RESCIND,
            rationale_ref="custody-correction", semantic_minute=40,
        )
        self.assertEqual(review.outcome, DecisionReviewOutcome.RESCIND)
        self.assertIn("closure", self.dependencies.decisions)

    def test_rejects_review_before_actor_receives_correction(self):
        with self.assertRaises(ValueError):
            record_assessment_decision_review(
                self.reviews, self.dependencies, self.custody, self.actor,
                review_id="review-1", decision_id="closure", superseding_assessment_id="new",
                superseding_claim_id="missing", outcome=DecisionReviewOutcome.DEFER,
                rationale_ref="awaiting", semantic_minute=40,
            )

    def test_rejects_wrong_actor(self):
        outsider = KnowledgeLedger("outsider")
        outsider.add(self._claim("new-claim", self.new, 35))
        with self.assertRaises(ValueError):
            record_assessment_decision_review(
                self.reviews, self.dependencies, self.custody, outsider,
                review_id="review-1", decision_id="closure", superseding_assessment_id="new",
                superseding_claim_id="new-claim", outcome=DecisionReviewOutcome.MAINTAIN,
                rationale_ref="independent-risk", semantic_minute=40,
            )

    def test_rejects_unrelated_assessment(self):
        other = CustodyAssessment(
            assessment_id="other", investigator_id="investigator", evidence_id="other-sample",
            semantic_minute=32, status=CustodyIntegrityStatus.CONTINUITY_SUPPORTED,
            known_record_ids=(), support_claim_ids=(),
        )
        self.custody.add_assessment(other)
        self.actor.add(self._claim("new-claim", self.new, 35))
        self.actor.add(self._claim("other-claim", other, 35))
        with self.assertRaises(ValueError):
            record_assessment_decision_review(
                self.reviews, self.dependencies, self.custody, self.actor,
                review_id="review-1", decision_id="closure", superseding_assessment_id="other",
                superseding_claim_id="other-claim", outcome=DecisionReviewOutcome.AMEND,
                rationale_ref="wrong-lineage", semantic_minute=40,
            )

    def test_rejects_future_review_basis(self):
        self.actor.add(self._claim("future", self.new, 50))
        with self.assertRaises(ValueError):
            record_assessment_decision_review(
                self.reviews, self.dependencies, self.custody, self.actor,
                review_id="review-1", decision_id="closure", superseding_assessment_id="new",
                superseding_claim_id="future", outcome=DecisionReviewOutcome.AMEND,
                rationale_ref="future", semantic_minute=40,
            )

    def test_preserves_multiple_historical_reviews(self):
        self.actor.add(self._claim("new-claim", self.new, 35))
        for review_id, minute, outcome in (("r1", 40, DecisionReviewOutcome.DEFER), ("r2", 50, DecisionReviewOutcome.MAINTAIN)):
            record_assessment_decision_review(
                self.reviews, self.dependencies, self.custody, self.actor,
                review_id=review_id, decision_id="closure", superseding_assessment_id="new",
                superseding_claim_id="new-claim", outcome=outcome,
                rationale_ref=f"reason-{review_id}", semantic_minute=minute,
            )
        self.assertEqual([r.review_id for r in self.reviews.reviews_for_decision("closure")], ["r1", "r2"])

    def test_registry_snapshot_round_trip(self):
        self.actor.add(self._claim("new-claim", self.new, 35))
        review = record_assessment_decision_review(
            self.reviews, self.dependencies, self.custody, self.actor,
            review_id="review-1", decision_id="closure", superseding_assessment_id="new",
            superseding_claim_id="new-claim", outcome=DecisionReviewOutcome.AMEND,
            rationale_ref="revised-order", semantic_minute=40,
        )
        restored = AssessmentDecisionReviewRegistry.restore(self.reviews.snapshot())
        self.assertEqual(restored.reviews[review.review_id], review)


if __name__ == "__main__":
    unittest.main()
