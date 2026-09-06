import unittest

from tools.global_npc_deception_policy import (
    CommunicationOpportunity,
    CommunicationPolicyDecision,
    CommunicationPosture,
    DeceptionMotive,
)
from tools.global_npc_disclosure_expectation import (
    DisclosureAssessmentStatus,
    DisclosureBasis,
    DisclosureBreachRegistry,
    DisclosureExpectation,
    apply_disclosure_breach_trust,
    assess_observable_silence,
    bind_disclosure_expectation,
)
from tools.global_npc_social import RelationshipState


class GlobalNpcDisclosureExpectationTests(unittest.TestCase):
    def opportunity(self, **overrides):
        values = dict(
            opportunity_id="op-1",
            speaker_id="dispatcher",
            target_agent_id="traveler",
            basis_claim_id="route-state",
            asserted_value="OPEN",
            declared_source_agent_id=None,
            semantic_minute=20,
            motive=DeceptionMotive.STRATEGIC_CONCEALMENT,
            silence_cost=5,
            obligation_conflict=0,
        )
        values.update(overrides)
        return CommunicationOpportunity(**values)

    def expectation(self, **overrides):
        values = dict(
            expectation_id="expect-1",
            speaker_id="dispatcher",
            recipient_id="traveler",
            basis_claim_id="route-state",
            basis=DisclosureBasis.EMERGENCY_WARNING,
            created_semantic_minute=10,
            strength=80,
            provenance_ref="role:route-safety-dispatch",
        )
        values.update(overrides)
        return DisclosureExpectation(**values)

    def decision(self, posture):
        return CommunicationPolicyDecision(
            opportunity_id="op-1",
            posture=posture,
            truthful_score=0,
            silence_score=0,
            deception_score=0,
            reason_codes=(),
        )

    def test_duty_expectation_derives_silence_and_obligation_pressure(self):
        bound = bind_disclosure_expectation(self.opportunity(), self.expectation())
        self.assertEqual(80, bound.silence_cost)
        self.assertEqual(80, bound.obligation_conflict)

    def test_explicit_request_adds_silence_cost_without_inventing_role_duty(self):
        bound = bind_disclosure_expectation(
            self.opportunity(),
            self.expectation(basis=DisclosureBasis.EXPLICIT_REQUEST, strength=70),
        )
        self.assertEqual(70, bound.silence_cost)
        self.assertEqual(0, bound.obligation_conflict)

    def test_observable_silence_breaches_strong_active_expectation(self):
        finding = assess_observable_silence(
            self.decision(CommunicationPosture.SILENT),
            self.opportunity(),
            self.expectation(),
            observed_semantic_minute=21,
        )
        self.assertEqual(DisclosureAssessmentStatus.EXPECTATION_BREACHED, finding.status)
        self.assertEqual(("role:route-safety-dispatch", "decision:op-1"), finding.provenance_refs)

    def test_truth_or_deception_is_not_classified_as_silence_breach(self):
        for posture in (CommunicationPosture.TRUTHFUL, CommunicationPosture.DECEPTIVE):
            finding = assess_observable_silence(
                self.decision(posture),
                self.opportunity(),
                self.expectation(),
                observed_semantic_minute=21,
            )
            self.assertEqual(DisclosureAssessmentStatus.DISCLOSED_OR_DECEIVED, finding.status)

    def test_expired_or_weak_expectation_does_not_create_breach(self):
        expired = assess_observable_silence(
            self.decision(CommunicationPosture.SILENT),
            self.opportunity(),
            self.expectation(expires_semantic_minute=15),
            observed_semantic_minute=21,
        )
        weak = assess_observable_silence(
            self.decision(CommunicationPosture.SILENT),
            self.opportunity(),
            self.expectation(strength=30),
            observed_semantic_minute=21,
        )
        self.assertEqual(DisclosureAssessmentStatus.NOT_APPLICABLE, expired.status)
        self.assertEqual(DisclosureAssessmentStatus.EXPECTATION_TOO_WEAK, weak.status)

    def test_trust_consequence_is_directional_and_idempotent(self):
        finding = assess_observable_silence(
            self.decision(CommunicationPosture.SILENT),
            self.opportunity(),
            self.expectation(),
            observed_semantic_minute=21,
        )
        relationship = RelationshipState(
            source_agent_id="traveler",
            target_agent_id="dispatcher",
            trust=40,
        )
        registry = DisclosureBreachRegistry()
        updated, applied = apply_disclosure_breach_trust(relationship, finding, registry)
        duplicate, applied_again = apply_disclosure_breach_trust(updated, finding, registry)
        self.assertTrue(applied)
        self.assertFalse(applied_again)
        self.assertEqual(32, updated.trust)
        self.assertEqual(updated, duplicate)
        self.assertIn(f"disclosure-breach:{finding.finding_id}", updated.provenance_refs)

    def test_registry_round_trip_preserves_idempotency(self):
        finding = assess_observable_silence(
            self.decision(CommunicationPosture.SILENT),
            self.opportunity(),
            self.expectation(),
            observed_semantic_minute=21,
        )
        relationship = RelationshipState(
            source_agent_id="traveler",
            target_agent_id="dispatcher",
            trust=40,
        )
        registry = DisclosureBreachRegistry()
        updated, _ = apply_disclosure_breach_trust(relationship, finding, registry)
        restored = DisclosureBreachRegistry.restore(registry.snapshot())
        duplicate, applied = apply_disclosure_breach_trust(updated, finding, restored)
        self.assertFalse(applied)
        self.assertEqual(updated, duplicate)

    def test_identity_and_causality_guards(self):
        with self.assertRaises(ValueError):
            bind_disclosure_expectation(
                self.opportunity(),
                self.expectation(recipient_id="someone-else"),
            )
        with self.assertRaises(ValueError):
            assess_observable_silence(
                self.decision(CommunicationPosture.SILENT),
                self.opportunity(),
                self.expectation(),
                observed_semantic_minute=19,
            )


if __name__ == "__main__":
    unittest.main()
