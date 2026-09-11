import unittest

from tools.autoptu_world_consequence_transaction import WorldConsequenceTransaction
from tools.autoptu_world_observation_owner import WorldObservationLedger


class AutoPTUWorldObservationOwnerTests(unittest.TestCase):
    def _transaction(self, **overrides):
        values = {
            "transaction_id": "ouros.world-consequence.pass419",
            "session_id": "ouros.autoptu.session.pass419",
            "result_ref": "result:pass419:1",
            "mapper_id": "mapper:field-outcome:v1",
            "consequence_kind": "FIELD_OBSERVATION",
            "provenance_ref": "ingress:pass419:1",
            "projected_payload": (
                ("evidence_ref", "evidence:pass419:sample"),
                ("objective_ref", "objective:pass419:return"),
                ("outcome", "PARTIAL"),
            ),
        }
        values.update(overrides)
        return WorldConsequenceTransaction(**values)

    def test_exact_transaction_becomes_persistent_observation(self):
        ledger = WorldObservationLedger()
        record, changed = ledger.apply(self._transaction())
        self.assertTrue(changed)
        self.assertEqual(record.transaction_id, "ouros.world-consequence.pass419")
        self.assertEqual(record.session_id, "ouros.autoptu.session.pass419")
        self.assertEqual(record.result_ref, "result:pass419:1")
        self.assertEqual(record.objective_ref, "objective:pass419:return")
        self.assertEqual(record.outcome, "PARTIAL")
        self.assertEqual(record.evidence_ref, "evidence:pass419:sample")
        self.assertEqual(record.provenance_ref, "ingress:pass419:1")

    def test_replay_is_idempotent(self):
        ledger = WorldObservationLedger()
        first, first_changed = ledger.apply(self._transaction())
        second, second_changed = ledger.apply(self._transaction())
        self.assertTrue(first_changed)
        self.assertFalse(second_changed)
        self.assertEqual(first, second)
        self.assertEqual(len(ledger.all()), 1)

    def test_wrong_consequence_kind_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "FIELD_OBSERVATION only"):
            WorldObservationLedger().apply(self._transaction(consequence_kind="RELATIONSHIP_CHANGE"))

    def test_owner_rejects_extra_fields_even_after_mapping(self):
        transaction = self._transaction(
            projected_payload=(
                ("objective_ref", "objective:pass419:return"),
                ("outcome", "PARTIAL"),
                ("hp_after", 17),
            )
        )
        with self.assertRaisesRegex(ValueError, "unsupported fields"):
            WorldObservationLedger().apply(transaction)

    def test_required_semantic_fields_are_not_inferred(self):
        transaction = self._transaction(projected_payload=(("evidence_ref", "evidence:pass419:sample"),))
        with self.assertRaisesRegex(ValueError, "requires objective_ref and outcome"):
            WorldObservationLedger().apply(transaction)

    def test_blank_optional_evidence_ref_fails_closed(self):
        transaction = self._transaction(
            projected_payload=(
                ("objective_ref", "objective:pass419:return"),
                ("outcome", "PARTIAL"),
                ("evidence_ref", "   "),
            )
        )
        with self.assertRaisesRegex(ValueError, "evidence_ref must be non-empty"):
            WorldObservationLedger().apply(transaction)

    def test_conflicting_same_transaction_identity_fails(self):
        ledger = WorldObservationLedger()
        ledger.apply(self._transaction())
        conflicting = self._transaction(
            projected_payload=(
                ("objective_ref", "objective:pass419:return"),
                ("outcome", "COMPLETE"),
                ("evidence_ref", "evidence:pass419:sample"),
            )
        )
        with self.assertRaisesRegex(ValueError, "conflicting replay"):
            ledger.apply(conflicting)


if __name__ == "__main__":
    unittest.main()
