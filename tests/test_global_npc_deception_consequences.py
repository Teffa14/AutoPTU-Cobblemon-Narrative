import unittest

from tools.global_npc_deception import SourceAttributionStore, author_deceptive_statement, materialize_deceptive_report
from tools.global_npc_deception_consequences import (
    DeceptionExposureRegistry,
    ExposureStatus,
    apply_deception_trust_consequence,
    assess_false_content_exposure,
)
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind, record_direct_observation
from tools.global_npc_social import RelationshipState


class DeceptionConsequenceTests(unittest.TestCase):
    def setUp(self):
        self.speaker = KnowledgeLedger("speaker")
        self.receiver = KnowledgeLedger("receiver")
        record_direct_observation(
            self.speaker,
            claim_id="basis",
            subject="route:ridge",
            value="CLOSED",
            semantic_minute=10,
            confidence=100,
        )
        self.statement = author_deceptive_statement(
            self.speaker,
            statement_id="lie-1",
            basis_claim_id="basis",
            asserted_value="OPEN",
            semantic_minute=12,
        )
        materialize_deceptive_report(
            self.receiver,
            SourceAttributionStore(),
            statement=self.statement,
            claim_id="heard-lie",
            message_id="msg-1",
            semantic_minute=15,
            confidence=80,
        )
        record_direct_observation(
            self.receiver,
            claim_id="saw-closure",
            subject="route:ridge",
            value="CLOSED",
            semantic_minute=25,
            confidence=95,
        )

    def test_contradiction_alone_does_not_authorize_trust_penalty(self):
        finding = assess_false_content_exposure(
            self.receiver,
            finding_id="finding-1",
            statement=self.statement,
            deceptive_claim_id="heard-lie",
            contradiction_claim_id="saw-closure",
            semantic_minute=26,
        )
        self.assertEqual(ExposureStatus.FALSEHOOD_CORROBORATED, finding.status)
        relationship = RelationshipState("receiver", "speaker", trust=40)
        with self.assertRaises(ValueError):
            apply_deception_trust_consequence(relationship, finding)

    def test_explicit_intent_evidence_allows_directional_trust_consequence_once(self):
        self.receiver.add(Claim(
            claim_id="intent-proof",
            subject="evidence:lie-1:intent",
            value="ESTABLISHED",
            source_kind=SourceKind.INSTITUTIONAL_RECORD,
            source_agent_id=None,
            semantic_minute=30,
            confidence=90,
            provenance_root="record:intent-proof",
        ))
        finding = assess_false_content_exposure(
            self.receiver,
            finding_id="finding-2",
            statement=self.statement,
            deceptive_claim_id="heard-lie",
            contradiction_claim_id="saw-closure",
            intent_evidence_claim_ids=("intent-proof",),
            semantic_minute=31,
        )
        self.assertEqual(ExposureStatus.INTENT_ATTRIBUTED, finding.status)
        relationship = RelationshipState("receiver", "speaker", trust=40)
        changed = apply_deception_trust_consequence(relationship, finding, trust_delta=-15)
        self.assertEqual(25, changed.trust)
        self.assertEqual(("deception-exposure:finding-2",), changed.provenance_refs)
        self.assertEqual(changed, apply_deception_trust_consequence(changed, finding, trust_delta=-15))

    def test_same_root_or_weak_contradiction_fails_closed(self):
        self.receiver.add(Claim(
            claim_id="same-root",
            subject="route:ridge",
            value="CLOSED",
            source_kind=SourceKind.REPORT,
            source_agent_id="relay",
            semantic_minute=20,
            confidence=90,
            provenance_root="deception:lie-1",
        ))
        with self.assertRaises(ValueError):
            assess_false_content_exposure(
                self.receiver,
                finding_id="same-root-finding",
                statement=self.statement,
                deceptive_claim_id="heard-lie",
                contradiction_claim_id="same-root",
                semantic_minute=26,
            )
        self.receiver.add(Claim(
            claim_id="weak",
            subject="route:ridge",
            value="CLOSED",
            source_kind=SourceKind.REPORT,
            source_agent_id="other",
            semantic_minute=21,
            confidence=40,
            provenance_root="other-root",
        ))
        with self.assertRaises(ValueError):
            assess_false_content_exposure(
                self.receiver,
                finding_id="weak-finding",
                statement=self.statement,
                deceptive_claim_id="heard-lie",
                contradiction_claim_id="weak",
                semantic_minute=26,
            )

    def test_registry_snapshot_restore_preserves_finding(self):
        self.receiver.add(Claim(
            claim_id="intent-proof",
            subject="evidence:lie-1:intent",
            value="ESTABLISHED",
            source_kind=SourceKind.INSTITUTIONAL_RECORD,
            source_agent_id=None,
            semantic_minute=30,
            confidence=90,
            provenance_root="record:intent-proof",
        ))
        finding = assess_false_content_exposure(
            self.receiver,
            finding_id="finding-3",
            statement=self.statement,
            deceptive_claim_id="heard-lie",
            contradiction_claim_id="saw-closure",
            intent_evidence_claim_ids=("intent-proof",),
            semantic_minute=31,
        )
        registry = DeceptionExposureRegistry()
        registry.add(finding)
        restored = DeceptionExposureRegistry.restore(registry.snapshot())
        self.assertEqual(finding, restored.findings["finding-3"])


if __name__ == "__main__":
    unittest.main()
