import unittest

from tools.autoptu_session_identity import AutoPTUSessionLedger
from tools.autoptu_world_consequence_transaction import (
    AdmittedSemanticResult,
    WorldConsequenceMapper,
    WorldConsequenceTransactionLedger,
)


class AutoPTUWorldConsequenceTransactionTests(unittest.TestCase):
    def _recorded(self):
        sessions = AutoPTUSessionLedger()
        session = sessions.request_session(
            handoff_request_id="handoff:pass418:1",
            world_action_ref="world-action:pass418:1",
            participant_refs=("npc:mara", "player:1"),
            rules_profile_id="ptu:standard",
            requested_at_minute=70,
        )
        sessions.bind_engine_session(session.session_id, engine_session_ref="engine:pass418:1")
        sessions.record_authoritative_result(session.session_id, result_ref="result:pass418:1")
        return sessions, session.session_id

    def _mapper(self):
        return WorldConsequenceMapper(
            mapper_id="mapper:field-outcome:v1",
            result_type="FIELD_OBJECTIVE_OUTCOME",
            consequence_kind="FIELD_OBSERVATION",
            required_payload_fields=("objective_ref", "outcome"),
            allowed_payload_fields=("objective_ref", "outcome", "evidence_ref"),
        )

    def _result(self, **payload):
        base = {"objective_ref": "objective:sample-return", "outcome": "PARTIAL"}
        base.update(payload)
        return AdmittedSemanticResult(
            result_ref="result:pass418:1",
            result_type="FIELD_OBJECTIVE_OUTCOME",
            provenance_ref="ingress:pass418:1",
            semantic_payload=base,
        )

    def test_exact_mapper_commits_only_explicit_payload(self):
        sessions, session_id = self._recorded()
        ledger = WorldConsequenceTransactionLedger()
        tx, changed = ledger.commit(
            session_ledger=sessions,
            session_id=session_id,
            result=self._result(evidence_ref="evidence:sample-a"),
            mapper=self._mapper(),
        )
        self.assertTrue(changed)
        self.assertEqual(tx.consequence_kind, "FIELD_OBSERVATION")
        self.assertEqual(dict(tx.projected_payload)["outcome"], "PARTIAL")
        self.assertEqual(len(ledger.all()), 1)

    def test_replay_is_idempotent(self):
        sessions, session_id = self._recorded()
        ledger = WorldConsequenceTransactionLedger()
        first, first_changed = ledger.commit(
            session_ledger=sessions,
            session_id=session_id,
            result=self._result(),
            mapper=self._mapper(),
        )
        second, second_changed = ledger.commit(
            session_ledger=sessions,
            session_id=session_id,
            result=self._result(),
            mapper=self._mapper(),
        )
        self.assertTrue(first_changed)
        self.assertFalse(second_changed)
        self.assertEqual(first, second)

    def test_unmapped_tactical_fields_fail_closed(self):
        sessions, session_id = self._recorded()
        ledger = WorldConsequenceTransactionLedger()
        with self.assertRaisesRegex(ValueError, "unmapped fields"):
            ledger.commit(
                session_ledger=sessions,
                session_id=session_id,
                result=self._result(hp_after=17, initiative_index=3),
                mapper=self._mapper(),
            )

    def test_missing_required_field_fails_closed(self):
        sessions, session_id = self._recorded()
        ledger = WorldConsequenceTransactionLedger()
        result = AdmittedSemanticResult(
            result_ref="result:pass418:1",
            result_type="FIELD_OBJECTIVE_OUTCOME",
            provenance_ref="ingress:pass418:missing",
            semantic_payload={"objective_ref": "objective:sample-return"},
        )
        with self.assertRaisesRegex(ValueError, "missing required fields"):
            ledger.commit(
                session_ledger=sessions,
                session_id=session_id,
                result=result,
                mapper=self._mapper(),
            )

    def test_wrong_result_ref_or_type_fails_closed(self):
        sessions, session_id = self._recorded()
        ledger = WorldConsequenceTransactionLedger()
        wrong_ref = AdmittedSemanticResult(
            result_ref="result:other",
            result_type="FIELD_OBJECTIVE_OUTCOME",
            provenance_ref="ingress:other",
            semantic_payload={"objective_ref": "objective:x", "outcome": "COMPLETE"},
        )
        with self.assertRaisesRegex(ValueError, "does not match"):
            ledger.commit(session_ledger=sessions, session_id=session_id, result=wrong_ref, mapper=self._mapper())

        wrong_type = AdmittedSemanticResult(
            result_ref="result:pass418:1",
            result_type="BATTLE_RAW_STATE",
            provenance_ref="ingress:wrong-type",
            semantic_payload={"objective_ref": "objective:x", "outcome": "COMPLETE"},
        )
        with self.assertRaisesRegex(ValueError, "not admitted"):
            ledger.commit(session_ledger=sessions, session_id=session_id, result=wrong_type, mapper=self._mapper())

    def test_engine_bound_session_cannot_emit_world_consequence(self):
        sessions = AutoPTUSessionLedger()
        session = sessions.request_session(
            handoff_request_id="handoff:pass418:pending",
            world_action_ref="world-action:pass418:pending",
            participant_refs=("npc:teo", "player:1"),
            rules_profile_id="ptu:standard",
            requested_at_minute=71,
        )
        sessions.bind_engine_session(session.session_id, engine_session_ref="engine:pass418:pending")
        with self.assertRaisesRegex(ValueError, "RESULT_RECORDED or RETIRED"):
            WorldConsequenceTransactionLedger().commit(
                session_ledger=sessions,
                session_id=session.session_id,
                result=self._result(),
                mapper=self._mapper(),
            )

    def test_conflicting_replay_same_identity_fails(self):
        sessions, session_id = self._recorded()
        ledger = WorldConsequenceTransactionLedger()
        ledger.commit(
            session_ledger=sessions,
            session_id=session_id,
            result=self._result(),
            mapper=self._mapper(),
        )
        changed = AdmittedSemanticResult(
            result_ref="result:pass418:1",
            result_type="FIELD_OBJECTIVE_OUTCOME",
            provenance_ref="ingress:pass418:1",
            semantic_payload={"objective_ref": "objective:sample-return", "outcome": "COMPLETE"},
        )
        with self.assertRaisesRegex(ValueError, "conflicting replay"):
            ledger.commit(
                session_ledger=sessions,
                session_id=session_id,
                result=changed,
                mapper=self._mapper(),
            )


if __name__ == "__main__":
    unittest.main()
