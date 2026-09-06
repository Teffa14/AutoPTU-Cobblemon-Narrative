import unittest

from tools.global_npc_deception_policy import (
    CommunicationOpportunity,
    CommunicationPosture,
    DeceptionMotive,
    DeceptionPolicyProfile,
    choose_communication_posture,
)
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_social import RelationshipState


class GlobalNpcDeceptionPolicyTests(unittest.TestCase):
    def setUp(self):
        self.ledger = KnowledgeLedger("speaker")
        record_direct_observation(
            self.ledger,
            claim_id="route-state",
            subject="route-state",
            value="CLOSED",
            semantic_minute=10,
            confidence=95,
        )

    def opportunity(self, **overrides):
        values = dict(
            opportunity_id="op-1",
            speaker_id="speaker",
            target_agent_id="receiver",
            basis_claim_id="route-state",
            asserted_value="OPEN",
            declared_source_agent_id=None,
            semantic_minute=20,
            motive=DeceptionMotive.STRATEGIC_CONCEALMENT,
            goal_pressure=20,
            utility_gain=10,
            secrecy_value=10,
            truthful_cost=0,
            silence_cost=20,
            exposure_risk=20,
            third_party_harm=10,
            obligation_conflict=0,
        )
        values.update(overrides)
        return CommunicationOpportunity(**values)

    def test_low_stakes_high_aversion_prefers_truth(self):
        decision = choose_communication_posture(
            self.ledger,
            DeceptionPolicyProfile("speaker", deception_aversion=80),
            self.opportunity(),
        )
        self.assertEqual(CommunicationPosture.TRUTHFUL, decision.posture)
        self.assertIn("DISCLOSE_BASIS_VALUE", decision.reason_codes)

    def test_high_secrecy_and_low_deception_value_can_prefer_silence(self):
        decision = choose_communication_posture(
            self.ledger,
            DeceptionPolicyProfile("speaker", deception_aversion=70, silence_preference=40),
            self.opportunity(
                goal_pressure=10,
                utility_gain=0,
                secrecy_value=85,
                truthful_cost=70,
                silence_cost=0,
                exposure_risk=70,
            ),
        )
        self.assertEqual(CommunicationPosture.SILENT, decision.posture)
        self.assertIn("WITHHOLD_INFORMATION", decision.reason_codes)

    def test_goal_pressure_and_gain_can_make_deception_selected(self):
        decision = choose_communication_posture(
            self.ledger,
            DeceptionPolicyProfile(
                "speaker",
                deception_aversion=15,
                harm_aversion=30,
                exposure_sensitivity=25,
                silence_preference=10,
            ),
            self.opportunity(
                goal_pressure=90,
                utility_gain=80,
                secrecy_value=70,
                truthful_cost=80,
                silence_cost=70,
                exposure_risk=15,
                third_party_harm=10,
            ),
        )
        self.assertEqual(CommunicationPosture.DECEPTIVE, decision.posture)
        self.assertIn("MOTIVE:STRATEGIC_CONCEALMENT", decision.reason_codes)
        self.assertIn("HIGH_GOAL_PRESSURE", decision.reason_codes)

    def test_trust_relationship_can_shift_same_opportunity_back_to_truth(self):
        opportunity = self.opportunity(
            goal_pressure=45,
            utility_gain=25,
            secrecy_value=20,
            truthful_cost=20,
            silence_cost=30,
            exposure_risk=20,
        )
        profile = DeceptionPolicyProfile(
            "speaker",
            deception_aversion=35,
            harm_aversion=40,
            exposure_sensitivity=40,
            silence_preference=10,
        )
        without_relation = choose_communication_posture(self.ledger, profile, opportunity)
        with_relation = choose_communication_posture(
            self.ledger,
            profile,
            opportunity,
            relationships=(
                RelationshipState(
                    source_agent_id="speaker",
                    target_agent_id="receiver",
                    affinity=80,
                    trust=100,
                ),
            ),
        )
        self.assertEqual(CommunicationPosture.DECEPTIVE, without_relation.posture)
        self.assertEqual(CommunicationPosture.TRUTHFUL, with_relation.posture)
        self.assertIn("RELATIONSHIP_HONESTY_PRESSURE", with_relation.reason_codes)

    def test_high_harm_and_duty_conflict_gate_deception(self):
        decision = choose_communication_posture(
            self.ledger,
            DeceptionPolicyProfile(
                "speaker",
                deception_aversion=20,
                harm_aversion=100,
                exposure_sensitivity=50,
                silence_preference=20,
            ),
            self.opportunity(
                goal_pressure=80,
                utility_gain=70,
                secrecy_value=50,
                truthful_cost=40,
                silence_cost=20,
                exposure_risk=40,
                third_party_harm=100,
                obligation_conflict=90,
            ),
        )
        self.assertNotEqual(CommunicationPosture.DECEPTIVE, decision.posture)

    def test_truthful_option_cannot_be_misclassified_as_deception(self):
        decision = choose_communication_posture(
            self.ledger,
            DeceptionPolicyProfile("speaker", deception_aversion=0),
            self.opportunity(
                asserted_value="CLOSED",
                declared_source_agent_id=None,
                goal_pressure=100,
                utility_gain=100,
                secrecy_value=100,
                truthful_cost=100,
                silence_cost=100,
            ),
        )
        self.assertNotEqual(CommunicationPosture.DECEPTIVE, decision.posture)
        self.assertLess(decision.deception_score, -5000)

    def test_false_source_only_is_a_real_deceptive_option(self):
        decision = choose_communication_posture(
            self.ledger,
            DeceptionPolicyProfile("speaker", deception_aversion=5),
            self.opportunity(
                asserted_value="CLOSED",
                declared_source_agent_id="inspector",
                goal_pressure=90,
                utility_gain=80,
                secrecy_value=50,
                truthful_cost=80,
                silence_cost=70,
                exposure_risk=5,
                third_party_harm=0,
            ),
        )
        self.assertEqual(CommunicationPosture.DECEPTIVE, decision.posture)

    def test_causal_and_identity_guards(self):
        with self.assertRaises(ValueError):
            choose_communication_posture(
                self.ledger,
                DeceptionPolicyProfile("other"),
                self.opportunity(),
            )
        with self.assertRaises(ValueError):
            choose_communication_posture(
                self.ledger,
                DeceptionPolicyProfile("speaker"),
                self.opportunity(semantic_minute=9),
            )


if __name__ == "__main__":
    unittest.main()
