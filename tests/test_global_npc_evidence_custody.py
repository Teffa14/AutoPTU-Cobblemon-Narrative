import unittest

from tools.global_npc_evidence_custody import (
    CustodyAction,
    CustodyIntegrityStatus,
    CustodyRecord,
    EvidenceCustodyRegistry,
    PhysicalEvidenceArtifact,
    assess_evidence_custody,
)
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind


def add_claim(ledger: KnowledgeLedger, claim_id: str, *, root: str, minute: int, confidence: int = 90) -> None:
    ledger.add(Claim(
        claim_id=claim_id,
        subject="evidence:relay-brace:custody",
        value=claim_id,
        source_kind=SourceKind.INSTITUTIONAL_RECORD,
        source_agent_id="evidence-office",
        semantic_minute=minute,
        confidence=confidence,
        provenance_root=root,
    ))


def artifact() -> PhysicalEvidenceArtifact:
    return PhysicalEvidenceArtifact(
        evidence_id="relay-brace-17",
        subject_ref="incident:relay-r17-outage",
        created_semantic_minute=100,
        provenance_ref="scene:relay-r17:brace",
    )


def record(record_id: str, claim_id: str, minute: int, previous: str | None, holder: str) -> CustodyRecord:
    return CustodyRecord(
        record_id=record_id,
        evidence_id="relay-brace-17",
        action=CustodyAction.COLLECTED if previous is None else CustodyAction.TRANSFERRED,
        holder_id=holder,
        semantic_minute=minute,
        documentation_claim_id=claim_id,
        previous_record_id=previous,
    )


class EvidenceCustodyTests(unittest.TestCase):
    def test_complete_known_chain_supports_continuity(self) -> None:
        ledger = KnowledgeLedger("investigator")
        add_claim(ledger, "doc-collect", root="record:collect", minute=101)
        add_claim(ledger, "doc-transfer", root="record:transfer", minute=102)
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r1", "doc-collect", 101, None, "collector"))
        registry.add_record(record("r2", "doc-transfer", 102, "r1", "lab"))
        result = assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="a1", known_record_ids=("r1", "r2"), semantic_minute=110,
        )
        self.assertIs(result.status, CustodyIntegrityStatus.CONTINUITY_SUPPORTED)

    def test_missing_handoff_is_documentation_gap_not_tampering(self) -> None:
        ledger = KnowledgeLedger("investigator")
        add_claim(ledger, "doc-transfer", root="record:transfer", minute=102)
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r2", "doc-transfer", 102, "r1", "lab"))
        result = assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="a-gap", known_record_ids=("r2",), semantic_minute=110,
        )
        self.assertIs(result.status, CustodyIntegrityStatus.DOCUMENTATION_GAP)

    def test_two_independent_records_claiming_same_predecessor_are_conflict(self) -> None:
        ledger = KnowledgeLedger("investigator")
        for claim_id, root, minute in (("doc-collect", "record:collect", 101), ("doc-a", "record:a", 102), ("doc-b", "record:b", 103)):
            add_claim(ledger, claim_id, root=root, minute=minute)
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r1", "doc-collect", 101, None, "collector"))
        registry.add_record(record("r2a", "doc-a", 102, "r1", "lab-a"))
        registry.add_record(record("r2b", "doc-b", 103, "r1", "lab-b"))
        result = assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="a-conflict", known_record_ids=("r1", "r2a", "r2b"), semantic_minute=110,
        )
        self.assertIs(result.status, CustodyIntegrityStatus.RECORD_CONFLICT)

    def test_gap_alone_never_bootstraps_compromise(self) -> None:
        ledger = KnowledgeLedger("investigator")
        add_claim(ledger, "doc-transfer", root="record:transfer", minute=102)
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r2", "doc-transfer", 102, "missing", "lab"))
        result = assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="a-no-compromise", known_record_ids=("r2",), semantic_minute=110,
        )
        self.assertNotEqual(result.status, CustodyIntegrityStatus.COMPROMISE_CORROBORATED)

    def test_independent_compromise_evidence_can_corrobate_compromise(self) -> None:
        ledger = KnowledgeLedger("investigator")
        add_claim(ledger, "doc-collect", root="record:collect", minute=101)
        add_claim(ledger, "seal-broken", root="observation:broken-seal", minute=104)
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r1", "doc-collect", 101, None, "collector"))
        result = assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="a-compromise", known_record_ids=("r1",),
            compromise_claim_ids=("seal-broken",), semantic_minute=110,
        )
        self.assertIs(result.status, CustodyIntegrityStatus.COMPROMISE_CORROBORATED)

    def test_same_provenance_root_cannot_create_independent_compromise(self) -> None:
        ledger = KnowledgeLedger("investigator")
        add_claim(ledger, "doc-collect", root="single-report", minute=101)
        add_claim(ledger, "alleged-break", root="single-report", minute=104)
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r1", "doc-collect", 101, None, "collector"))
        result = assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="a-same-root", known_record_ids=("r1",),
            compromise_claim_ids=("alleged-break",), semantic_minute=110,
        )
        self.assertIs(result.status, CustodyIntegrityStatus.CONTINUITY_SUPPORTED)

    def test_unknown_or_future_documentation_fails_closed(self) -> None:
        ledger = KnowledgeLedger("investigator")
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r1", "unknown-doc", 101, None, "collector"))
        with self.assertRaises(KeyError):
            assess_evidence_custody(
                ledger, artifact(), registry,
                assessment_id="a-unknown", known_record_ids=("r1",), semantic_minute=110,
            )

        future = KnowledgeLedger("investigator")
        add_claim(future, "future-doc", root="record:future", minute=120)
        registry2 = EvidenceCustodyRegistry()
        registry2.add_record(record("r1", "future-doc", 120, None, "collector"))
        with self.assertRaisesRegex(ValueError, "future"):
            assess_evidence_custody(
                future, artifact(), registry2,
                assessment_id="a-future", known_record_ids=("r1",), semantic_minute=110,
            )

    def test_registry_snapshot_round_trip_preserves_records_and_assessments(self) -> None:
        ledger = KnowledgeLedger("investigator")
        add_claim(ledger, "doc-collect", root="record:collect", minute=101)
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r1", "doc-collect", 101, None, "collector"))
        assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="a-persist", known_record_ids=("r1",), semantic_minute=110,
        )
        restored = EvidenceCustodyRegistry.restore(registry.snapshot())
        self.assertEqual(restored.records, registry.records)
        self.assertEqual(restored.assessments, registry.assessments)


if __name__ == "__main__":
    unittest.main()
