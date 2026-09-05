import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).resolve().parents[1] / "implementation" / "marea-sendero-joint-jurisdiction-coordination-trace-v1.json"


class EcologicalJointJurisdictionRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.trace = cls.data["trace"]

    def event(self, name):
        return next(x for x in self.trace if x["event"] == name)

    def test_population_and_canon_guards_are_conserved(self):
        guards = self.data["canon_guards"]
        self.assertEqual(guards["authoritative_fletchling_population"], 12)
        self.assertFalse(guards["new_persistent_actor_created"])
        self.assertFalse(guards["population_change_claimed"])
        self.assertFalse(guards["sendero_institution_created_as_canon"])
        self.assertFalse(guards["jurisdiction_created_as_canon"])
        self.assertFalse(guards["ownership_created_as_canon"])
        self.assertFalse(guards["player_organization_granted_authority"])
        for step in self.trace:
            if "population" in step:
                self.assertEqual(step["population"], 12)

    def test_shared_ecological_evidence_does_not_create_governance_command(self):
        step = self.event("SHARED_ECOLOGICAL_EVIDENCE_LOADED")
        self.assertEqual(step["ecological_truth_records"], 1)
        self.assertEqual(step["governance_commands_created"], 0)
        self.assertEqual(step["disposition"], "AUTHORITY_MAPPING_PENDING")

    def test_overlapping_scope_does_not_imply_supersession(self):
        scopes = self.event("OVERLAPPING_SCOPES_IDENTIFIED")
        self.assertTrue(scopes["ecological_process_crosses_admin_boundary"])
        self.assertFalse(scopes["one_scope_supersedes_other"])
        attempt = self.event("OVERLAP_SUPERSESSION_ATTEMPT")
        self.assertEqual(attempt["result"], "REJECT_OVERLAP_AS_SUPERSESSION")
        self.assertFalse(attempt["authority_transfer_created"])

    def test_participation_and_silence_do_not_create_approval(self):
        step = self.event("PARTICIPATION_AS_APPROVAL_ATTEMPT")
        self.assertGreater(step["participants_present"], step["explicit_approvals"])
        self.assertEqual(step["result"], "REJECT_PARTICIPATION_AS_APPROVAL")
        self.assertFalse(step["silence_treated_as_consent"])

    def test_action_class_maps_distinct_authority_roles(self):
        step = self.event("ACTION_CLASS_AUTHORITY_MAPPED")
        self.assertIn("APPROVE_ACCESS_CHANGE", step["required_roles"])
        self.assertIn("IMPLEMENT", step["required_roles"])
        self.assertTrue(step["consultation_required"])
        self.assertFalse(step["joint_consensus_required"])
        self.assertEqual(step["disposition"], "JOINT_APPROVAL_REQUIRED")

    def test_coordinated_action_is_temporary_and_does_not_claim_recovery(self):
        step = self.event("COORDINATED_ACTION_AUTHORIZED")
        self.assertTrue(step["temporary"])
        self.assertFalse(step["ecological_recovery_claimed"])
        self.assertEqual(step["disposition"], "COORDINATED_ACTION_AUTHORIZED")

    def test_veto_cannot_expand_beyond_its_authored_scope(self):
        step = self.event("UNRELATED_VETO_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_VETO_SCOPE_EXPANSION")
        self.assertFalse(step["universal_veto_created"])

    def test_capacity_constraint_is_separate_from_authority_and_intent(self):
        step = self.event("CAPACITY_CONSTRAINT_RECORDED")
        self.assertTrue(step["authorized_to_implement"])
        self.assertFalse(step["implementation_capacity_available"])
        self.assertFalse(step["bad_faith_claim_created"])
        self.assertFalse(step["authority_revoked"])
        self.assertEqual(step["disposition"], "CAPACITY_CONSTRAINED")

    def test_emergency_action_is_bounded_and_requires_review(self):
        step = self.event("EMERGENCY_TRIGGER_AND_BOUNDED_ACTION")
        self.assertTrue(step["trigger_within_mandate"])
        self.assertTrue(step["scope_bounded"])
        self.assertTrue(step["affected_authorities_recorded"])
        self.assertFalse(step["permanent_authority_expansion"])
        self.assertTrue(step["review_required"])
        review = self.event("POST_EMERGENCY_REVIEW")
        self.assertTrue(review["ordinary_mandates_preserved"])
        self.assertFalse(review["ecological_outcome_inferred_from_governance"])

    def test_governance_does_not_create_tactical_semantics(self):
        step = self.event("TACTICAL_SEMANTICS_INFERENCE_ATTEMPT")
        self.assertEqual(step["result"], "REJECT_UNVERIFIED_TACTICAL_SEMANTICS")
        self.assertEqual(step["ptu_state_mutations"], 0)
        self.assertEqual(step["autoptu_handoffs"], 0)

    def test_restart_preserves_history_without_advancing_review_time(self):
        step = self.event("RESTART_RESTORE")
        self.assertTrue(step["authority_map_preserved"])
        self.assertTrue(step["approval_history_preserved"])
        self.assertTrue(step["capacity_history_preserved"])
        self.assertTrue(step["emergency_action_history_preserved"])
        self.assertFalse(step["semantic_review_horizon_advanced_by_restart"])
        self.assertEqual(step["demographic_events"], 0)


if __name__ == "__main__":
    unittest.main()
