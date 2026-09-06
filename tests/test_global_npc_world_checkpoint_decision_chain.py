import hashlib
import json
import unittest

from tools.global_npc_ai import AgentMode, NpcAgentState
from tools.global_npc_assessment_decision_dependency import (
    AssessmentDecisionDependencyRegistry,
    record_assessment_dependent_decision,
)
from tools.global_npc_assessment_decision_review import (
    AssessmentDecisionReviewRegistry,
    DecisionReviewOutcome,
    record_assessment_decision_review,
)
from tools.global_npc_decision_consequence_repair import (
    ConsequenceRepairAction,
    DecisionConsequenceRepairRegistry,
    record_consequence_repair,
    record_decision_consequence,
)
from tools.global_npc_evidence_custody import CustodyAssessment, CustodyIntegrityStatus, EvidenceCustodyRegistry
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_checkpoint import build_checkpoint, restore_checkpoint
from tools.global_npc_world_event_coordinator import GlobalNpcWorldEventCoordinator


class WorldCheckpointDecisionChainTests(unittest.TestCase):
    def _world(self):
        agents = {
            "investigator": NpcAgentState("investigator", AgentMode.OFFSCREEN_NAMED, "synthetic", "archive"),
            "authority": NpcAgentState("authority", AgentMode.OFFSCREEN_NAMED, "synthetic", "gate"),
        }
        ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
        channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 0)}
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

    def _chain(self):
        coordinator, channels = self._world()
        custody = EvidenceCustodyRegistry()
        custody.add_assessment(CustodyAssessment(
            assessment_id="old", investigator_id="investigator", evidence_id="sample",
            semantic_minute=10, status=CustodyIntegrityStatus.DOCUMENTATION_GAP,
            known_record_ids=(), support_claim_ids=(),
        ))
        custody.add_assessment(CustodyAssessment(
            assessment_id="new", investigator_id="investigator", evidence_id="sample",
            semantic_minute=30, status=CustodyIntegrityStatus.CONTINUITY_SUPPORTED,
            known_record_ids=(), support_claim_ids=(), supersedes_assessment_id="old",
        ))
        authority = coordinator.information_queue.ledgers["authority"]
        authority.add(Claim(
            claim_id="old-claim", subject="custody:sample", value=CustodyIntegrityStatus.DOCUMENTATION_GAP.value,
            source_kind=SourceKind.REPORT, source_agent_id="investigator", semantic_minute=15,
            confidence=80, provenance_root="custody-assessment:old",
        ))
        authority.add(Claim(
            claim_id="new-claim", subject="custody:sample", value=CustodyIntegrityStatus.CONTINUITY_SUPPORTED.value,
            source_kind=SourceKind.REPORT, source_agent_id="investigator", semantic_minute=35,
            confidence=90, provenance_root="custody-assessment:new",
        ))
        dependencies = AssessmentDecisionDependencyRegistry()
        record_assessment_dependent_decision(
            dependencies, custody, authority,
            decision_id="closure", basis_assessment_id="old", basis_claim_id="old-claim",
            decision_kind="ROUTE_RESTRICTION", subject_ref="relay-road", semantic_minute=20,
        )
        reviews = AssessmentDecisionReviewRegistry()
        record_assessment_decision_review(
            reviews, dependencies, custody, authority,
            review_id="review", decision_id="closure", superseding_assessment_id="new",
            superseding_claim_id="new-claim", outcome=DecisionReviewOutcome.RESCIND,
            rationale_ref="corrected-custody", semantic_minute=40,
        )
        consequences = DecisionConsequenceRepairRegistry()
        record_decision_consequence(
            consequences, dependencies,
            consequence_id="gate", decision_id="closure", consequence_kind="ACCESS_STATE",
            subject_ref="relay-road-gate", applied_semantic_minute=21, value_ref="CLOSED",
        )
        record_consequence_repair(
            consequences, reviews,
            repair_id="open-gate", consequence_id="gate", review_id="review",
            action=ConsequenceRepairAction.CEASE, rationale_ref="order-rescinded", semantic_minute=41,
        )
        return coordinator, channels, custody, dependencies, reviews, consequences

    def test_complete_decision_review_repair_chain_survives_restart(self):
        coordinator, channels, custody, dependencies, reviews, consequences = self._chain()
        checkpoint = build_checkpoint(
            coordinator,
            semantic_minute=45,
            evidence_custody_registry=custody,
            assessment_decision_dependency_registry=dependencies,
            assessment_decision_review_registry=reviews,
            decision_consequence_repair_registry=consequences,
        )
        restored = restore_checkpoint(checkpoint, channels=channels)
        self.assertEqual(restored.assessment_decision_dependency_registry.decisions, dependencies.decisions)
        self.assertEqual(restored.assessment_decision_review_registry.reviews, reviews.reviews)
        self.assertEqual(restored.decision_consequence_repair_registry.consequences, consequences.consequences)
        self.assertEqual(restored.decision_consequence_repair_registry.repairs, consequences.repairs)

    def test_missing_decision_basis_assessment_fails_closed(self):
        coordinator, channels, custody, dependencies, reviews, consequences = self._chain()
        checkpoint = build_checkpoint(
            coordinator,
            semantic_minute=45,
            evidence_custody_registry=custody,
            assessment_decision_dependency_registry=dependencies,
            assessment_decision_review_registry=reviews,
            decision_consequence_repair_registry=consequences,
        )
        checkpoint["evidence_custody"]["assessments"] = [
            row for row in checkpoint["evidence_custody"]["assessments"] if row["assessment_id"] != "old"
        ]
        checkpoint["evidence_custody"]["assessments"][0]["supersedes_assessment_id"] = None
        self._redigest(checkpoint)
        with self.assertRaisesRegex(ValueError, "missing basis assessment"):
            restore_checkpoint(checkpoint, channels=channels)

    def test_legacy_v4_restores_with_empty_decision_chain_registries(self):
        coordinator, channels = self._world()
        checkpoint = build_checkpoint(coordinator, semantic_minute=5)
        checkpoint["schema"] = "OUROS_NPC_WORLD_CHECKPOINT_V4"
        checkpoint.pop("assessment_decision_dependencies")
        checkpoint.pop("assessment_decision_reviews")
        checkpoint.pop("decision_consequence_repairs")
        self._redigest(checkpoint)
        restored = restore_checkpoint(checkpoint, channels=channels)
        self.assertEqual(restored.assessment_decision_dependency_registry.decisions, {})
        self.assertEqual(restored.assessment_decision_review_registry.reviews, {})
        self.assertEqual(restored.decision_consequence_repair_registry.consequences, {})
        self.assertEqual(restored.decision_consequence_repair_registry.repairs, {})


if __name__ == "__main__":
    unittest.main()
