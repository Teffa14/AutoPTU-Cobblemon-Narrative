import unittest
from pathlib import Path

from tools.global_npc_memory import (
    BeliefStatus,
    KnowledgeLedger,
    evaluate_belief,
    record_direct_observation,
    replay_fixture,
    transmit_claim,
)


class GlobalNpcMemoryTests(unittest.TestCase):
    def test_direct_observation_is_local_to_observer(self):
        alpha = KnowledgeLedger("alpha")
        beta = KnowledgeLedger("beta")
        record_direct_observation(alpha, claim_id="a1", subject="gate", value="closed", semantic_minute=1, confidence=90)
        self.assertEqual(evaluate_belief(alpha, "gate").status, BeliefStatus.SUPPORTED)
        self.assertEqual(evaluate_belief(beta, "gate").status, BeliefStatus.UNKNOWN)

    def test_report_keeps_provenance_and_attenuates_confidence(self):
        alpha = KnowledgeLedger("alpha")
        beta = KnowledgeLedger("beta")
        source = record_direct_observation(alpha, claim_id="a1", subject="gate", value="closed", semantic_minute=1, confidence=90)
        report = transmit_claim(alpha, beta, source_claim_id="a1", new_claim_id="b1", message_id="m1", semantic_minute=2, receiver_trust_in_sender=40)
        self.assertEqual(report.provenance_root, source.provenance_root)
        self.assertLessEqual(report.confidence, source.confidence)
        self.assertEqual(report.parent_claim_id, "a1")

    def test_retellings_of_same_root_do_not_fake_independent_corroboration(self):
        alpha = KnowledgeLedger("alpha")
        beta = KnowledgeLedger("beta")
        gamma = KnowledgeLedger("gamma")
        record_direct_observation(alpha, claim_id="a1", subject="gate", value="closed", semantic_minute=1, confidence=90)
        transmit_claim(alpha, beta, source_claim_id="a1", new_claim_id="b1", message_id="m1", semantic_minute=2, receiver_trust_in_sender=40)
        transmit_claim(beta, gamma, source_claim_id="b1", new_claim_id="g1", message_id="m2", semantic_minute=3, receiver_trust_in_sender=20)
        transmit_claim(alpha, gamma, source_claim_id="a1", new_claim_id="g2", message_id="m3", semantic_minute=4, receiver_trust_in_sender=40)
        assessed = evaluate_belief(gamma, "gate")
        self.assertEqual(assessed.independent_roots_by_value["closed"], ("a1",))
        self.assertLessEqual(assessed.support_by_value["closed"], 90)

    def test_independent_observation_can_corroborate(self):
        agent = KnowledgeLedger("agent")
        record_direct_observation(agent, claim_id="a1", subject="gate", value="closed", semantic_minute=1, confidence=40)
        record_direct_observation(agent, claim_id="a2", subject="gate", value="closed", semantic_minute=2, confidence=40)
        assessed = evaluate_belief(agent, "gate")
        self.assertEqual(assessed.status, BeliefStatus.SUPPORTED)
        self.assertEqual(set(assessed.independent_roots_by_value["closed"]), {"a1", "a2"})

    def test_contradiction_is_retained_not_erased(self):
        agent = KnowledgeLedger("agent")
        record_direct_observation(agent, claim_id="a1", subject="gate", value="closed", semantic_minute=1, confidence=90)
        record_direct_observation(agent, claim_id="a2", subject="gate", value="open", semantic_minute=2, confidence=90)
        assessed = evaluate_belief(agent, "gate")
        self.assertEqual(assessed.status, BeliefStatus.CONTESTED)
        self.assertIsNone(assessed.preferred_value)
        self.assertEqual(len(agent.claims), 2)

    def test_fixture_replays_deterministically(self):
        path = Path("implementation/global-npc-memory-belief-communication-fixture-v1.json")
        self.assertEqual(replay_fixture(path), replay_fixture(path))

    def test_core_has_no_authored_region_special_case(self):
        source = Path("tools/global_npc_memory.py").read_text(encoding="utf-8").lower()
        for forbidden in ("marea", "sendero", "puerto bruma", "loma clara"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
