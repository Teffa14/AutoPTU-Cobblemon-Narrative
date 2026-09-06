import unittest

from tools.global_npc_assessment_decision_dependency import (
    AssessmentDecisionDependencyRegistry,
    record_assessment_dependent_decision,
)
from tools.global_npc_assessment_decision_review import (
    AssessmentDecisionReview,
    AssessmentDecisionReviewRegistry,
    DecisionReviewOutcome,
)
from tools.global_npc_decision_consequence_repair import (
    ConsequenceRepairAction,
    ConsequenceState,
    DecisionConsequenceRepairRegistry,
    record_consequence_repair,
    record_decision_consequence,
)
from tools.global_npc_evidence_custody import CustodyAssessment, CustodyIntegrityStatus, EvidenceCustodyRegistry
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind


class DecisionConsequenceRepairTests(unittest.TestCase):
    def setUp(self):
        self.custody = EvidenceCustodyRegistry()
        old = CustodyAssessment(
            assessment_id="old", investigator_id="investigator", evidence_id="sample",
            semantic_minute=10, status=CustodyIntegrityStatus.DOCUMENTATION_GAP,
            known_record_ids=(), support_claim_ids=(),
        )
        self.custody.add_assessment(old)
        actor = KnowledgeLedger("authority")
        actor.add(Claim(
            claim_id="old-claim", subject="custody:sample", value=CustodyIntegrityStatus.DOCUMENTATION_GAP.value,
            source_kind=SourceKind.REPORT, source_agent_id="investigator", semantic_minute=15,
            confidence=80, provenance_root="custody-assessment:old",
        ))
        self.dependencies = AssessmentDecisionDependencyRegistry()
        record_assessment_dependent_decision(
            self.dependencies, self.custody, actor,
            decision_id="closure", basis_assessment_id="old", basis_claim_id="old-claim",
            decision_kind="ROUTE_RESTRICTION", subject_ref="relay-road", semantic_minute=20,
        )
        self.reviews = AssessmentDecisionReviewRegistry()
        self.registry = DecisionConsequenceRepairRegistry()
        record_decision_consequence(
            self.registry, self.dependencies,
            consequence_id="gate", decision_id="closure", consequence_kind="ACCESS_STATE",
            subject_ref="relay-road-gate", applied_semantic_minute=21, value_ref="CLOSED",
        )

    def _review(self, outcome, review_id="review"):
        review = AssessmentDecisionReview(
            review_id=review_id, decision_id="closure", actor_id="authority",
            superseding_assessment_id="new", superseding_claim_id="new-claim",
            outcome=outcome, rationale_ref="review-rationale", semantic_minute=40,
        )
        self.reviews.add(review)
        return review

    def test_rescission_ceases_only_targeted_consequence(self):
        self._review(DecisionReviewOutcome.RESCIND)
        record_decision_consequence(
            self.registry, self.dependencies,
            consequence_id="notice", decision_id="closure", consequence_kind="PUBLIC_NOTICE",
            subject_ref="relay-board", applied_semantic_minute=22, value_ref="POSTED",
        )
        record_consequence_repair(
            self.registry, self.reviews,
            repair_id="repair-gate", consequence_id="gate", review_id="review",
            action=ConsequenceRepairAction.CEASE, rationale_ref="order-rescinded", semantic_minute=41,
        )
        self.assertEqual(self.registry.effective_consequence("gate").state, ConsequenceState.CEASED)
        self.assertEqual(self.registry.effective_consequence("notice").state, ConsequenceState.ACTIVE)

    def test_amended_decision_changes_only_selected_value(self):
        self._review(DecisionReviewOutcome.AMEND)
        record_consequence_repair(
            self.registry, self.reviews,
            repair_id="repair-gate", consequence_id="gate", review_id="review",
            action=ConsequenceRepairAction.AMEND, rationale_ref="partial-reopening", semantic_minute=41,
            amended_value_ref="LIMITED_ACCESS",
        )
        effective = self.registry.effective_consequence("gate")
        self.assertEqual(effective.state, ConsequenceState.AMENDED)
        self.assertEqual(effective.value_ref, "LIMITED_ACCESS")

    def test_maintained_decision_cannot_cease_consequence(self):
        self._review(DecisionReviewOutcome.MAINTAIN)
        with self.assertRaises(ValueError):
            record_consequence_repair(
                self.registry, self.reviews,
                repair_id="bad", consequence_id="gate", review_id="review",
                action=ConsequenceRepairAction.CEASE, rationale_ref="bad", semantic_minute=41,
            )

    def test_deferred_review_cannot_change_consequence(self):
        self._review(DecisionReviewOutcome.DEFER)
        with self.assertRaises(ValueError):
            record_consequence_repair(
                self.registry, self.reviews,
                repair_id="bad", consequence_id="gate", review_id="review",
                action=ConsequenceRepairAction.RETAIN, rationale_ref="wait", semantic_minute=41,
            )

    def test_rescinded_decision_can_retain_consequence_only_with_independent_basis(self):
        self._review(DecisionReviewOutcome.RESCIND)
        with self.assertRaises(ValueError):
            record_consequence_repair(
                self.registry, self.reviews,
                repair_id="bad", consequence_id="gate", review_id="review",
                action=ConsequenceRepairAction.RETAIN, rationale_ref="still-risky", semantic_minute=41,
            )
        repair = record_consequence_repair(
            self.registry, self.reviews,
            repair_id="keep", consequence_id="gate", review_id="review",
            action=ConsequenceRepairAction.RETAIN, rationale_ref="structural-risk", semantic_minute=42,
            independent_basis_ref="inspection:bridge-instability",
        )
        self.assertEqual(repair.independent_basis_ref, "inspection:bridge-instability")
        self.assertEqual(self.registry.effective_consequence("gate").state, ConsequenceState.ACTIVE)

    def test_rejects_review_for_other_decision(self):
        other = AssessmentDecisionReview(
            review_id="other-review", decision_id="different", actor_id="authority",
            superseding_assessment_id="new", superseding_claim_id="new-claim",
            outcome=DecisionReviewOutcome.RESCIND, rationale_ref="other", semantic_minute=40,
        )
        self.reviews.add(other)
        with self.assertRaises(ValueError):
            record_consequence_repair(
                self.registry, self.reviews,
                repair_id="bad", consequence_id="gate", review_id="other-review",
                action=ConsequenceRepairAction.CEASE, rationale_ref="wrong-decision", semantic_minute=41,
            )

    def test_rejects_repair_before_review(self):
        self._review(DecisionReviewOutcome.RESCIND)
        with self.assertRaises(ValueError):
            record_consequence_repair(
                self.registry, self.reviews,
                repair_id="bad", consequence_id="gate", review_id="review",
                action=ConsequenceRepairAction.CEASE, rationale_ref="too-early", semantic_minute=39,
            )

    def test_ceased_consequence_cannot_be_repaired_again(self):
        self._review(DecisionReviewOutcome.RESCIND)
        record_consequence_repair(
            self.registry, self.reviews,
            repair_id="stop", consequence_id="gate", review_id="review",
            action=ConsequenceRepairAction.CEASE, rationale_ref="rescinded", semantic_minute=41,
        )
        with self.assertRaises(ValueError):
            record_consequence_repair(
                self.registry, self.reviews,
                repair_id="again", consequence_id="gate", review_id="review",
                action=ConsequenceRepairAction.RETAIN, rationale_ref="again", semantic_minute=42,
                independent_basis_ref="new-risk",
            )

    def test_registry_snapshot_round_trip(self):
        self._review(DecisionReviewOutcome.AMEND)
        record_consequence_repair(
            self.registry, self.reviews,
            repair_id="repair-gate", consequence_id="gate", review_id="review",
            action=ConsequenceRepairAction.AMEND, rationale_ref="partial-reopening", semantic_minute=41,
            amended_value_ref="LIMITED_ACCESS",
        )
        restored = DecisionConsequenceRepairRegistry.restore(self.registry.snapshot())
        self.assertEqual(restored.consequences, self.registry.consequences)
        self.assertEqual(restored.repairs, self.registry.repairs)
        self.assertEqual(restored.effective_consequence("gate"), self.registry.effective_consequence("gate"))


if __name__ == "__main__":
    unittest.main()
