import unittest
from pathlib import Path

from tools.global_npc_memory import (
    BeliefStatus,
    KnowledgeLedger,
    KnowledgeLedgerStore,
    evaluate_belief,
    record_direct_observation,
    replay_fixture,
    transmit_claim,
)


class GlobalNpcMemoryPersistenceTests(unittest.TestCase):
    def test_ledger_round_trip_preserves_claim_identity_and_provenance(self):
        alpha = KnowledgeLedger("alpha")
        beta = KnowledgeLedger("beta")
        record_direct_observation(
            alpha,
            claim_id="a1",
            subject="route:north",
            value="closed",
            semantic_minute=10,
            confidence=90,
        )
        transmit_claim(
            alpha,
            beta,
            source_claim_id="a1",
            new_claim_id="b1",
            message_id="m1",
            semantic_minute=15,
            receiver_trust_in_sender=40,
        )

        restored = KnowledgeLedger.restore(beta.snapshot())
        self.assertEqual(restored, beta)
        self.assertEqual(restored.claims["b1"].provenance_root, "a1")
        self.assertEqual(restored.claims["b1"].parent_claim_id, "a1")
        self.assertEqual(restored.claims["b1"].message_id, "m1")

    def test_store_round_trip_keeps_private_knowledge_isolated(self):
        alpha = KnowledgeLedger("alpha")
        beta = KnowledgeLedger("beta")
        gamma = KnowledgeLedger("gamma")
        record_direct_observation(
            alpha,
            claim_id="a1",
            subject="route:north",
            value="closed",
            semantic_minute=10,
            confidence=90,
        )
        transmit_claim(
            alpha,
            beta,
            source_claim_id="a1",
            new_claim_id="b1",
            message_id="m1",
            semantic_minute=15,
            receiver_trust_in_sender=40,
        )

        store = KnowledgeLedgerStore({"alpha": alpha, "beta": beta, "gamma": gamma})
        restored = KnowledgeLedgerStore.restore(store.snapshot())

        self.assertEqual(evaluate_belief(restored.require("beta"), "route:north").status, BeliefStatus.SUPPORTED)
        self.assertEqual(evaluate_belief(restored.require("gamma"), "route:north").status, BeliefStatus.UNKNOWN)

    def test_store_snapshot_is_deterministic_across_insertion_order(self):
        first = KnowledgeLedger("first")
        second = KnowledgeLedger("second")
        record_direct_observation(first, claim_id="z", subject="s", value="v", semantic_minute=2, confidence=70)
        record_direct_observation(first, claim_id="a", subject="s2", value="v2", semantic_minute=1, confidence=80)

        left = KnowledgeLedgerStore({"second": second, "first": first})
        right = KnowledgeLedgerStore({"first": first, "second": second})
        self.assertEqual(left.snapshot(), right.snapshot())

    def test_restore_rejects_unknown_schema(self):
        with self.assertRaises(ValueError):
            KnowledgeLedger.restore({"schema": "OUROS_UNKNOWN", "agent_id": "a", "claims": []})
        with self.assertRaises(ValueError):
            KnowledgeLedgerStore.restore({"schema": "OUROS_UNKNOWN", "ledgers": []})

    def test_restore_rejects_duplicate_agent_with_conflicting_state(self):
        one = KnowledgeLedger("a")
        two = KnowledgeLedger("a")
        record_direct_observation(one, claim_id="c1", subject="s", value="one", semantic_minute=1, confidence=80)
        record_direct_observation(two, claim_id="c2", subject="s", value="two", semantic_minute=2, confidence=80)
        snapshot = {
            "schema": "OUROS_NPC_KNOWLEDGE_LEDGER_STORE_V1",
            "ledgers": [one.snapshot(), two.snapshot()],
        }
        with self.assertRaises(ValueError):
            KnowledgeLedgerStore.restore(snapshot)

    def test_restart_fixture_preserves_belief_and_is_deterministic(self):
        path = Path("implementation/global-npc-memory-persistence-fixture-v1.json")
        first = replay_fixture(path)
        second = replay_fixture(path)
        self.assertEqual(first, second)
        restart = next(row for row in first["results"] if row["event_id"] == "restart-1")
        after = next(row for row in first["results"] if row["event_id"] == "assess-after")
        self.assertEqual(restart["status"], "RESTORED")
        self.assertEqual(restart["claim_count"], 2)
        self.assertEqual(after["status"], "SUPPORTED")
        self.assertEqual(after["preferred_value"], "closed")

    def test_core_has_no_authored_region_special_case(self):
        source = Path("tools/global_npc_memory.py").read_text(encoding="utf-8").lower()
        for forbidden in ("marea", "sendero", "puerto bruma", "loma clara"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
