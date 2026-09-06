import unittest

from tools.global_npc_deception import (
    AttributionKind,
    DeceptionKind,
    DeceptiveStatement,
    SourceAttributionRecord,
    SourceAttributionStore,
)
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind
from tools.global_npc_social import RelationshipState
from tools.global_npc_source_attribution_exposure import (
    SourceAttributionExposureRegistry,
    SourceExposureStatus,
    SourceVerificationEvidence,
    SourceVerificationKind,
    apply_false_source_trust_consequence,
    assess_false_source_exposure,
)


class SourceAttributionExposureTests(unittest.TestCase):
    def setUp(self):
        self.receiver = KnowledgeLedger("receiver")
        self.statement = DeceptiveStatement(
            statement_id="borrowed-authority",
            speaker_id="dispatcher",
            basis_claim_id="basis",
            subject="route:ridge",
            basis_value="OPEN",
            asserted_value="OPEN",
            basis_source_agent_id="dispatcher",
            declared_source_agent_id="ranger-chief",
            semantic_minute=10,
            kind=DeceptionKind.FALSE_SOURCE,
        )
        self.receiver.add(Claim(
            claim_id="heard",
            subject="route:ridge",
            value="OPEN",
            source_kind=SourceKind.REPORT,
            source_agent_id="dispatcher",
            semantic_minute=12,
            confidence=80,
            provenance_root="deception:borrowed-authority",
            parent_claim_id="basis",
            message_id="msg-1",
        ))
        self.attributions = SourceAttributionStore()
        self.attributions.add(SourceAttributionRecord(
            attribution_id="attr-1",
            agent_id="receiver",
            claim_id="heard",
            actual_source_agent_id="dispatcher",
            perceived_source_agent_id="ranger-chief",
            semantic_minute=12,
            kind=AttributionKind.SPEAKER_DECLARATION,
            statement_id="borrowed-authority",
        ))

    def add_evidence(self, claim_id, *, source, root, confidence=90, minute=20):
        self.receiver.add(Claim(
            claim_id=claim_id,
            subject="evidence:borrowed-authority:source",
            value="ESTABLISHED",
            source_kind=SourceKind.INSTITUTIONAL_RECORD,
            source_agent_id=source,
            semantic_minute=minute,
            confidence=confidence,
            provenance_root=root,
        ))

    def test_named_source_denial_opens_dispute_without_punishing_speaker(self):
        self.add_evidence("denial", source="ranger-chief", root="denial:ranger")
        finding = assess_false_source_exposure(
            self.receiver,
            self.attributions,
            finding_id="f1",
            statement=self.statement,
            deceptive_claim_id="heard",
            evidence=(SourceVerificationEvidence(
                "denial",
                SourceVerificationKind.NAMED_SOURCE_DENIAL,
                "ranger-chief",
            ),),
            semantic_minute=21,
        )
        self.assertEqual(SourceExposureStatus.SOURCE_DISPUTED, finding.status)
        with self.assertRaises(ValueError):
            apply_false_source_trust_consequence(
                RelationshipState("receiver", "dispatcher", trust=40),
                finding,
            )

    def test_authorship_record_corroborates_false_attribution_but_not_intent(self):
        self.add_evidence("record", source=None, root="archive:dispatch")
        finding = assess_false_source_exposure(
            self.receiver,
            self.attributions,
            finding_id="f2",
            statement=self.statement,
            deceptive_claim_id="heard",
            evidence=(SourceVerificationEvidence(
                "record",
                SourceVerificationKind.AUTHORSHIP_RECORD,
                "ranger-chief",
                actual_source_agent_id="dispatcher",
            ),),
            semantic_minute=21,
        )
        self.assertEqual(SourceExposureStatus.FALSE_ATTRIBUTION_CORROBORATED, finding.status)
        self.assertEqual("dispatcher", self.receiver.claims["heard"].source_agent_id)
        self.assertEqual("deception:borrowed-authority", self.receiver.claims["heard"].provenance_root)

    def test_speaker_admission_attributes_intent_and_penalizes_actual_speaker_only_once(self):
        self.add_evidence("admission", source="dispatcher", root="admission:dispatcher")
        finding = assess_false_source_exposure(
            self.receiver,
            self.attributions,
            finding_id="f3",
            statement=self.statement,
            deceptive_claim_id="heard",
            evidence=(SourceVerificationEvidence(
                "admission",
                SourceVerificationKind.SPEAKER_ADMISSION,
                "ranger-chief",
                actual_source_agent_id="dispatcher",
            ),),
            semantic_minute=21,
        )
        self.assertEqual(SourceExposureStatus.INTENT_ATTRIBUTED, finding.status)
        relation = RelationshipState("receiver", "dispatcher", trust=40)
        changed = apply_false_source_trust_consequence(relation, finding, trust_delta=-12)
        self.assertEqual(28, changed.trust)
        self.assertEqual(
            changed,
            apply_false_source_trust_consequence(changed, finding, trust_delta=-12),
        )
        with self.assertRaises(ValueError):
            apply_false_source_trust_consequence(
                RelationshipState("receiver", "ranger-chief", trust=40),
                finding,
            )

    def test_same_root_echo_weak_evidence_and_wrong_denier_fail_closed(self):
        self.add_evidence("echo", source="relay", root="deception:borrowed-authority")
        with self.assertRaises(ValueError):
            assess_false_source_exposure(
                self.receiver,
                self.attributions,
                finding_id="echo",
                statement=self.statement,
                deceptive_claim_id="heard",
                evidence=(SourceVerificationEvidence(
                    "echo",
                    SourceVerificationKind.NAMED_SOURCE_DENIAL,
                    "ranger-chief",
                ),),
                semantic_minute=21,
            )
        self.add_evidence("weak", source="ranger-chief", root="denial:weak", confidence=40)
        with self.assertRaises(ValueError):
            assess_false_source_exposure(
                self.receiver,
                self.attributions,
                finding_id="weak",
                statement=self.statement,
                deceptive_claim_id="heard",
                evidence=(SourceVerificationEvidence(
                    "weak",
                    SourceVerificationKind.NAMED_SOURCE_DENIAL,
                    "ranger-chief",
                ),),
                semantic_minute=21,
            )
        self.add_evidence("wrong", source="other", root="denial:wrong")
        with self.assertRaises(ValueError):
            assess_false_source_exposure(
                self.receiver,
                self.attributions,
                finding_id="wrong",
                statement=self.statement,
                deceptive_claim_id="heard",
                evidence=(SourceVerificationEvidence(
                    "wrong",
                    SourceVerificationKind.NAMED_SOURCE_DENIAL,
                    "ranger-chief",
                ),),
                semantic_minute=21,
            )

    def test_registry_snapshot_round_trip(self):
        self.add_evidence("record", source=None, root="archive:dispatch")
        finding = assess_false_source_exposure(
            self.receiver,
            self.attributions,
            finding_id="f4",
            statement=self.statement,
            deceptive_claim_id="heard",
            evidence=(SourceVerificationEvidence(
                "record",
                SourceVerificationKind.AUTHORSHIP_RECORD,
                "ranger-chief",
                actual_source_agent_id="dispatcher",
            ),),
            semantic_minute=21,
        )
        registry = SourceAttributionExposureRegistry()
        registry.add(finding)
        restored = SourceAttributionExposureRegistry.restore(registry.snapshot())
        self.assertEqual(finding, restored.findings["f4"])


if __name__ == "__main__":
    unittest.main()
