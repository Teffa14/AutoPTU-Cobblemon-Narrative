import copy
import unittest

from tools.global_npc_evidence_custody import (
    CustodyAction,
    CustodyAssessment,
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

    def test_late_documentation_creates_new_assessment_without_erasing_old_one(self) -> None:
        ledger = KnowledgeLedger("investigator")
        add_claim(ledger, "doc-collect", root="record:collect", minute=101)
        add_claim(ledger, "doc-transfer", root="record:transfer", minute=120)
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r1", "doc-collect", 101, None, "collector"))
        registry.add_record(record("r2", "doc-transfer", 102, "r1", "lab"))

        earlier = assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="assessment:early", known_record_ids=("r2",), semantic_minute=121,
        )
        later = assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="assessment:reopened", known_record_ids=("r1", "r2"),
            supersedes_assessment_id=earlier.assessment_id, semantic_minute=125,
        )

        self.assertIs(earlier.status, CustodyIntegrityStatus.DOCUMENTATION_GAP)
        self.assertIs(later.status, CustodyIntegrityStatus.CONTINUITY_SUPPORTED)
        self.assertEqual(registry.assessments[earlier.assessment_id], earlier)
        self.assertEqual(
            [row.assessment_id for row in registry.assessment_lineage(later.assessment_id)],
            ["assessment:early", "assessment:reopened"],
        )

    def test_lineage_must_stay_with_same_investigator_and_evidence(self) -> None:
        registry = EvidenceCustodyRegistry()
        base = CustodyAssessment(
            assessment_id="base", investigator_id="investigator", evidence_id="relay-brace-17",
            semantic_minute=110, status=CustodyIntegrityStatus.UNASSESSED,
            known_record_ids=(), support_claim_ids=(),
        )
        registry.add_assessment(base)
        with self.assertRaisesRegex(ValueError, "investigators"):
            registry.add_assessment(CustodyAssessment(
                assessment_id="other-investigator", investigator_id="other", evidence_id="relay-brace-17",
                semantic_minute=111, status=CustodyIntegrityStatus.UNASSESSED,
                known_record_ids=(), support_claim_ids=(), supersedes_assessment_id="base",
            ))
        with self.assertRaisesRegex(ValueError, "evidence identity"):
            registry.add_assessment(CustodyAssessment(
                assessment_id="other-evidence", investigator_id="investigator", evidence_id="another-artifact",
                semantic_minute=111, status=CustodyIntegrityStatus.UNASSESSED,
                known_record_ids=(), support_claim_ids=(), supersedes_assessment_id="base",
            ))

    def test_lineage_rejects_unknown_predecessor_and_time_regression(self) -> None:
        registry = EvidenceCustodyRegistry()
        with self.assertRaisesRegex(ValueError, "missing assessment"):
            registry.add_assessment(CustodyAssessment(
                assessment_id="orphan", investigator_id="investigator", evidence_id="relay-brace-17",
                semantic_minute=110, status=CustodyIntegrityStatus.UNASSESSED,
                known_record_ids=(), support_claim_ids=(), supersedes_assessment_id="missing",
            ))
        registry.add_assessment(CustodyAssessment(
            assessment_id="later", investigator_id="investigator", evidence_id="relay-brace-17",
            semantic_minute=120, status=CustodyIntegrityStatus.UNASSESSED,
            known_record_ids=(), support_claim_ids=(),
        ))
        with self.assertRaisesRegex(ValueError, "predates superseded"):
            registry.add_assessment(CustodyAssessment(
                assessment_id="earlier", investigator_id="investigator", evidence_id="relay-brace-17",
                semantic_minute=119, status=CustodyIntegrityStatus.UNASSESSED,
                known_record_ids=(), support_claim_ids=(), supersedes_assessment_id="later",
            ))

    def test_restore_detects_lineage_cycle_even_when_snapshot_rows_are_out_of_order(self) -> None:
        registry = EvidenceCustodyRegistry()
        snapshot = {
            "schema": "OUROS_NPC_EVIDENCE_CUSTODY_V2",
            "records": [],
            "assessments": [
                {
                    "assessment_id": "b", "investigator_id": "investigator", "evidence_id": "relay-brace-17",
                    "semantic_minute": 111, "status": "UNASSESSED", "known_record_ids": [],
                    "support_claim_ids": [], "compromise_claim_ids": [], "supersedes_assessment_id": "a",
                },
                {
                    "assessment_id": "a", "investigator_id": "investigator", "evidence_id": "relay-brace-17",
                    "semantic_minute": 111, "status": "UNASSESSED", "known_record_ids": [],
                    "support_claim_ids": [], "compromise_claim_ids": [], "supersedes_assessment_id": "b",
                },
            ],
        }
        with self.assertRaisesRegex(ValueError, "cycle"):
            registry.restore(snapshot)

    def test_registry_snapshot_round_trip_preserves_records_assessments_and_lineage(self) -> None:
        ledger = KnowledgeLedger("investigator")
        add_claim(ledger, "doc-collect", root="record:collect", minute=101)
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r1", "doc-collect", 101, None, "collector"))
        first = assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="z-first", known_record_ids=("r1",), semantic_minute=110,
        )
        assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="a-second", known_record_ids=("r1",), semantic_minute=115,
            supersedes_assessment_id=first.assessment_id,
        )
        restored = EvidenceCustodyRegistry.restore(registry.snapshot())
        self.assertEqual(restored.records, registry.records)
        self.assertEqual(restored.assessments, registry.assessments)
        self.assertEqual(
            [row.assessment_id for row in restored.assessment_lineage("a-second")],
            ["z-first", "a-second"],
        )

    def test_v1_snapshot_restores_without_inventing_lineage(self) -> None:
        ledger = KnowledgeLedger("investigator")
        add_claim(ledger, "doc-collect", root="record:collect", minute=101)
        registry = EvidenceCustodyRegistry()
        registry.add_record(record("r1", "doc-collect", 101, None, "collector"))
        assess_evidence_custody(
            ledger, artifact(), registry,
            assessment_id="legacy", known_record_ids=("r1",), semantic_minute=110,
        )
        snapshot = copy.deepcopy(registry.snapshot())
        snapshot["schema"] = "OUROS_NPC_EVIDENCE_CUSTODY_V1"
        for row in snapshot["assessments"]:
            row.pop("supersedes_assessment_id", None)
        restored = EvidenceCustodyRegistry.restore(snapshot)
        self.assertIsNone(restored.assessments["legacy"].supersedes_assessment_id)


if __name__ == "__main__":
    unittest.main()
