import hashlib
import json
import unittest

from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_evidence_custody import (
    CustodyAction,
    CustodyAssessment,
    CustodyIntegrityStatus,
    CustodyRecord,
    EvidenceCustodyRegistry,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import KnowledgeLedger, record_direct_observation
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_checkpoint import build_checkpoint, restore_checkpoint
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator


class GlobalNpcWorldCheckpointCustodyTests(unittest.TestCase):
    def _world(self):
        agents = {
            "investigator": NpcAgentState(
                "investigator",
                AgentMode.OFFSCREEN_NAMED,
                "synthetic_region",
                "evidence_room",
            )
        }
        ledgers = {"investigator": KnowledgeLedger("investigator")}
        channels = {"local": CommunicationChannel("local", "DIRECT", 0)}
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=InformationEventQueue(channels=channels, ledgers=ledgers),
            replan_queue=NpcReplanQueue(),
            agents=agents,
        )
        return coordinator, channels

    @staticmethod
    def _redigest(checkpoint: dict) -> None:
        payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        checkpoint["sha256"] = hashlib.sha256(canonical).hexdigest()

    def _custody_registry(self, coordinator):
        ledger = coordinator.information_queue.ledgers["investigator"]
        record_direct_observation(
            ledger,
            claim_id="receipt:collection",
            subject="custody:sample-r17",
            value="COLLECTED_BY_TECH_A",
            semantic_minute=5,
            confidence=95,
        )
        record_direct_observation(
            ledger,
            claim_id="receipt:transfer",
            subject="custody:sample-r17",
            value="TRANSFERRED_TO_LAB",
            semantic_minute=8,
            confidence=95,
        )
        registry = EvidenceCustodyRegistry()
        registry.add_record(
            CustodyRecord(
                record_id="custody:1",
                evidence_id="sample:r17",
                action=CustodyAction.COLLECTED,
                holder_id="tech-a",
                semantic_minute=5,
                documentation_claim_id="receipt:collection",
            )
        )
        registry.add_record(
            CustodyRecord(
                record_id="custody:2",
                evidence_id="sample:r17",
                action=CustodyAction.TRANSFERRED,
                holder_id="lab",
                semantic_minute=8,
                documentation_claim_id="receipt:transfer",
                previous_record_id="custody:1",
            )
        )
        registry.add_assessment(
            CustodyAssessment(
                assessment_id="assessment:r17",
                investigator_id="investigator",
                evidence_id="sample:r17",
                semantic_minute=10,
                status=CustodyIntegrityStatus.CONTINUITY_SUPPORTED,
                known_record_ids=("custody:1", "custody:2"),
                support_claim_ids=("receipt:collection", "receipt:transfer"),
            )
        )
        return registry

    def test_custody_registry_survives_atomic_checkpoint_with_evidence_basis(self):
        coordinator, channels = self._world()
        registry = self._custody_registry(coordinator)

        checkpoint = build_checkpoint(
            coordinator,
            semantic_minute=12,
            evidence_custody_registry=registry,
        )
        self.assertEqual(checkpoint["schema"], "OUROS_NPC_WORLD_CHECKPOINT_V5")
        restored = restore_checkpoint(checkpoint, channels=channels)

        self.assertEqual(restored.evidence_custody_registry.records, registry.records)
        self.assertEqual(restored.evidence_custody_registry.assessments, registry.assessments)
        self.assertIn("receipt:transfer", restored.ledger_store.require("investigator").claims)

        restarted = restore_checkpoint(
            build_checkpoint(
                restored.coordinator,
                semantic_minute=14,
                evidence_custody_registry=restored.evidence_custody_registry,
            ),
            channels=channels,
        )
        self.assertEqual(
            restarted.evidence_custody_registry.assessments["assessment:r17"].status,
            CustodyIntegrityStatus.CONTINUITY_SUPPORTED,
        )

    def test_custody_assessment_without_restored_support_claim_fails_closed(self):
        coordinator, channels = self._world()
        registry = EvidenceCustodyRegistry()
        registry.add_record(
            CustodyRecord(
                record_id="custody:orphan",
                evidence_id="sample:r17",
                action=CustodyAction.COLLECTED,
                holder_id="tech-a",
                semantic_minute=5,
                documentation_claim_id="missing-receipt",
            )
        )
        registry.add_assessment(
            CustodyAssessment(
                assessment_id="assessment:orphan",
                investigator_id="investigator",
                evidence_id="sample:r17",
                semantic_minute=6,
                status=CustodyIntegrityStatus.CONTINUITY_SUPPORTED,
                known_record_ids=("custody:orphan",),
                support_claim_ids=("missing-receipt",),
            )
        )
        checkpoint = build_checkpoint(
            coordinator,
            semantic_minute=7,
            evidence_custody_registry=registry,
        )
        with self.assertRaisesRegex(ValueError, "custody support claim is missing"):
            restore_checkpoint(checkpoint, channels=channels)

    def test_custody_assessment_from_future_fails_closed(self):
        coordinator, channels = self._world()
        registry = EvidenceCustodyRegistry()
        registry.add_assessment(
            CustodyAssessment(
                assessment_id="assessment:future",
                investigator_id="investigator",
                evidence_id="sample:r17",
                semantic_minute=11,
                status=CustodyIntegrityStatus.UNASSESSED,
                known_record_ids=(),
                support_claim_ids=(),
            )
        )
        checkpoint = build_checkpoint(
            coordinator,
            semantic_minute=10,
            evidence_custody_registry=registry,
        )
        with self.assertRaisesRegex(ValueError, "custody assessment comes from the future"):
            restore_checkpoint(checkpoint, channels=channels)

    def test_legacy_v3_checkpoint_restores_with_empty_custody_registry(self):
        coordinator, channels = self._world()
        checkpoint = build_checkpoint(coordinator, semantic_minute=4)
        checkpoint["schema"] = "OUROS_NPC_WORLD_CHECKPOINT_V3"
        checkpoint.pop("evidence_custody")
        self._redigest(checkpoint)
        restored = restore_checkpoint(checkpoint, channels=channels)
        self.assertEqual(restored.evidence_custody_registry.records, {})
        self.assertEqual(restored.evidence_custody_registry.assessments, {})

    def test_custody_record_cannot_cross_evidence_identity_after_restart(self):
        coordinator, channels = self._world()
        ledger = coordinator.information_queue.ledgers["investigator"]
        record_direct_observation(
            ledger,
            claim_id="doc:1",
            subject="custody:sample-a",
            value="COLLECTED",
            semantic_minute=2,
            confidence=90,
        )
        record_direct_observation(
            ledger,
            claim_id="doc:2",
            subject="custody:sample-b",
            value="TRANSFERRED",
            semantic_minute=3,
            confidence=90,
        )
        registry = EvidenceCustodyRegistry()
        registry.add_record(CustodyRecord("record:a", "sample:a", CustodyAction.COLLECTED, "tech", 2, "doc:1"))
        registry.add_record(CustodyRecord("record:b", "sample:b", CustodyAction.TRANSFERRED, "lab", 3, "doc:2", "record:a"))
        checkpoint = build_checkpoint(coordinator, semantic_minute=4, evidence_custody_registry=registry)
        with self.assertRaisesRegex(ValueError, "crosses evidence identity"):
            restore_checkpoint(checkpoint, channels=channels)


if __name__ == "__main__":
    unittest.main()
