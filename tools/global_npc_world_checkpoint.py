from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from tools.global_npc_ai import AgentMode, NpcAgentState, agent_from_dict
from tools.global_npc_assessment_decision_dependency import AssessmentDecisionDependencyRegistry
from tools.global_npc_assessment_decision_review import AssessmentDecisionReviewRegistry
from tools.global_npc_deception_runtime import DeceptionInformationEventQueue
from tools.global_npc_decision_consequence_repair import DecisionConsequenceRepairRegistry
from tools.global_npc_evidence_custody import EvidenceCustodyRegistry
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_infrastructure_failure_attribution import InfrastructureAttributionRegistry
from tools.global_npc_memory import KnowledgeLedger, KnowledgeLedgerStore, record_direct_observation
from tools.global_npc_replanning import NpcReplanQueue
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


CHECKPOINT_SCHEMA = "OUROS_NPC_WORLD_CHECKPOINT_V5"
LEGACY_CHECKPOINT_SCHEMAS = {
    "OUROS_NPC_WORLD_CHECKPOINT_V4",
    "OUROS_NPC_WORLD_CHECKPOINT_V3",
    "OUROS_NPC_WORLD_CHECKPOINT_V2",
    "OUROS_NPC_WORLD_CHECKPOINT_V1",
}
STANDARD_QUEUE_KIND = "STANDARD"
DECEPTION_QUEUE_KIND = "DECEPTION"


@dataclass(frozen=True)
class RestoredWorldCheckpoint:
    semantic_minute: int
    coordinator: GlobalNpcWorldEventCoordinator
    ledger_store: KnowledgeLedgerStore
    infrastructure_attribution_registry: InfrastructureAttributionRegistry
    evidence_custody_registry: EvidenceCustodyRegistry
    assessment_decision_dependency_registry: AssessmentDecisionDependencyRegistry
    assessment_decision_review_registry: AssessmentDecisionReviewRegistry
    decision_consequence_repair_registry: DecisionConsequenceRepairRegistry
    publication_runtime_snapshot: Mapping[str, object] | None


def _agent_snapshot(agent: NpcAgentState) -> dict:
    return {
        "agent_id": agent.agent_id,
        "mode": agent.mode.value,
        "region_ref": agent.region_ref,
        "location_ref": agent.location_ref,
        "risk_tolerance": agent.risk_tolerance,
        "energy": agent.energy,
        "knowledge": sorted(agent.knowledge),
        "permissions": sorted(agent.permissions),
        "memory_refs": list(agent.memory_refs),
        "active_autoptu_binding": agent.active_autoptu_binding,
    }


def _canonical_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _digest_payload(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _validated_payload(snapshot: Mapping[str, object]) -> dict:
    if snapshot.get("schema") not in {CHECKPOINT_SCHEMA, *LEGACY_CHECKPOINT_SCHEMAS}:
        raise ValueError("unsupported global NPC world checkpoint schema")
    digest = snapshot.get("sha256")
    if not isinstance(digest, str) or not digest:
        raise ValueError("checkpoint sha256 is required")
    payload = {str(key): value for key, value in snapshot.items() if key != "sha256"}
    if _digest_payload(payload) != digest:
        raise ValueError("global NPC world checkpoint digest mismatch")
    return payload


def _queue_kind(queue: InformationEventQueue) -> str:
    if isinstance(queue, DeceptionInformationEventQueue):
        return DECEPTION_QUEUE_KIND
    return STANDARD_QUEUE_KIND


def build_checkpoint(
    coordinator: GlobalNpcWorldEventCoordinator,
    *,
    semantic_minute: int,
    infrastructure_attribution_registry: InfrastructureAttributionRegistry | None = None,
    evidence_custody_registry: EvidenceCustodyRegistry | None = None,
    assessment_decision_dependency_registry: AssessmentDecisionDependencyRegistry | None = None,
    assessment_decision_review_registry: AssessmentDecisionReviewRegistry | None = None,
    decision_consequence_repair_registry: DecisionConsequenceRepairRegistry | None = None,
    publication_runtime_snapshot: Mapping[str, object] | None = None,
) -> dict:
    """Create one deterministic logical snapshot of coupled global-NPC state.

    The returned object is a logical atomic unit only. Durable crash-safe commit
    to disk/database belongs to the persistence adapter and is intentionally not
    claimed by this module.
    """
    ledger_store = KnowledgeLedgerStore(dict(coordinator.information_queue.ledgers))
    attribution_registry = infrastructure_attribution_registry or InfrastructureAttributionRegistry()
    custody_registry = evidence_custody_registry or EvidenceCustodyRegistry()
    dependency_registry = assessment_decision_dependency_registry or AssessmentDecisionDependencyRegistry()
    review_registry = assessment_decision_review_registry or AssessmentDecisionReviewRegistry()
    consequence_registry = decision_consequence_repair_registry or DecisionConsequenceRepairRegistry()
    payload = {
        "schema": CHECKPOINT_SCHEMA,
        "semantic_minute": int(semantic_minute),
        "agents": [_agent_snapshot(coordinator.agents[agent_id]) for agent_id in sorted(coordinator.agents)],
        "knowledge_ledgers": ledger_store.snapshot(),
        "information_queue_kind": _queue_kind(coordinator.information_queue),
        "information_queue": coordinator.information_queue.snapshot(),
        "replan_queue": coordinator.replan_queue.to_snapshot(),
        "materialized_delivery_event_ids": sorted(coordinator.materialized_delivery_event_ids),
        "infrastructure_attribution": attribution_registry.snapshot(),
        "evidence_custody": custody_registry.snapshot(),
        "assessment_decision_dependencies": dependency_registry.snapshot(),
        "assessment_decision_reviews": review_registry.snapshot(),
        "decision_consequence_repairs": consequence_registry.snapshot(),
        "publication_runtime": None if publication_runtime_snapshot is None else dict(publication_runtime_snapshot),
    }
    return payload | {"sha256": _digest_payload(payload)}


def _validate_references(*, queue: InformationEventQueue, coordinator: GlobalNpcWorldEventCoordinator) -> None:
    ledgers = queue.ledgers
    envelopes = [entry[2] for entry in queue.pending] + list(queue.awaiting_local_ack.values())
    for envelope in envelopes:
        if envelope.sender_id not in ledgers or envelope.receiver_id not in ledgers:
            raise ValueError(f"checkpoint envelope references missing ledger: {envelope.event_id}")
        if envelope.source_claim_id not in ledgers[envelope.sender_id].claims:
            raise ValueError(f"checkpoint envelope source claim is missing: {envelope.event_id}")
    missing_materialized = coordinator.materialized_delivery_event_ids - queue.delivered_event_ids
    if missing_materialized:
        raise ValueError(
            "checkpoint materialized delivery guard references non-delivered events: "
            + ",".join(sorted(missing_materialized))
        )


def _restore_information_queue(
    payload: Mapping[str, object],
    *,
    channels: Mapping[str, CommunicationChannel],
    ledgers: dict[str, KnowledgeLedger],
) -> InformationEventQueue:
    kind = str(payload.get("information_queue_kind", STANDARD_QUEUE_KIND))
    queue_snapshot = payload["information_queue"]
    if not isinstance(queue_snapshot, Mapping):
        raise ValueError("information_queue checkpoint must be a mapping")
    if kind == STANDARD_QUEUE_KIND:
        return InformationEventQueue.restore(queue_snapshot, channels=dict(channels), ledgers=ledgers)
    if kind == DECEPTION_QUEUE_KIND:
        return DeceptionInformationEventQueue.restore(queue_snapshot, channels=dict(channels), ledgers=ledgers)
    raise ValueError(f"unsupported information queue kind: {kind}")


def _restore_registry(payload: Mapping[str, object], key: str, factory, restore):
    raw = payload.get(key)
    if raw is None:
        if payload.get("schema") in LEGACY_CHECKPOINT_SCHEMAS:
            return factory()
        raise ValueError(f"{key} checkpoint is required")
    if not isinstance(raw, Mapping):
        raise ValueError(f"{key} checkpoint must be a mapping")
    return restore(raw)


def _restore_infrastructure_attribution(payload: Mapping[str, object]) -> InfrastructureAttributionRegistry:
    return _restore_registry(payload, "infrastructure_attribution", InfrastructureAttributionRegistry, InfrastructureAttributionRegistry.restore)


def _restore_evidence_custody(payload: Mapping[str, object]) -> EvidenceCustodyRegistry:
    return _restore_registry(payload, "evidence_custody", EvidenceCustodyRegistry, EvidenceCustodyRegistry.restore)


def _validate_infrastructure_attribution(
    registry: InfrastructureAttributionRegistry,
    ledger_store: KnowledgeLedgerStore,
    *,
    semantic_minute: int,
) -> None:
    for finding in registry.findings.values():
        if finding.semantic_minute > semantic_minute:
            raise ValueError(f"infrastructure finding comes from the future: {finding.finding_id}")
        ledger = ledger_store.ledgers.get(finding.discoverer_id)
        if ledger is None:
            raise ValueError(f"infrastructure finding references missing discoverer ledger: {finding.finding_id}")
        for claim_id in finding.evidence_claim_ids:
            claim = ledger.claims.get(claim_id)
            if claim is None:
                raise ValueError(f"infrastructure finding evidence claim is missing: {finding.finding_id}:{claim_id}")
            if claim.semantic_minute > finding.semantic_minute:
                raise ValueError(f"infrastructure finding predates its evidence: {finding.finding_id}:{claim_id}")


def _validate_evidence_custody(
    registry: EvidenceCustodyRegistry,
    ledger_store: KnowledgeLedgerStore,
    *,
    semantic_minute: int,
) -> None:
    for record in registry.records.values():
        if record.semantic_minute > semantic_minute:
            raise ValueError(f"custody record comes from the future: {record.record_id}")
        if record.previous_record_id is not None:
            previous = registry.records.get(record.previous_record_id)
            if previous is None:
                continue
            if previous.evidence_id != record.evidence_id:
                raise ValueError(f"custody record crosses evidence identity: {record.record_id}")
            if previous.semantic_minute > record.semantic_minute:
                raise ValueError(f"custody record predates its predecessor: {record.record_id}")

    for assessment in registry.assessments.values():
        if assessment.semantic_minute > semantic_minute:
            raise ValueError(f"custody assessment comes from the future: {assessment.assessment_id}")
        ledger = ledger_store.ledgers.get(assessment.investigator_id)
        if ledger is None:
            raise ValueError(f"custody assessment references missing investigator ledger: {assessment.assessment_id}")
        known_documentation_claim_ids: set[str] = set()
        for record_id in assessment.known_record_ids:
            record = registry.records.get(record_id)
            if record is None:
                raise ValueError(f"custody assessment references missing record: {assessment.assessment_id}:{record_id}")
            if record.evidence_id != assessment.evidence_id:
                raise ValueError(f"custody assessment mixes evidence identities: {assessment.assessment_id}:{record_id}")
            if record.semantic_minute > assessment.semantic_minute:
                raise ValueError(f"custody assessment predates known record: {assessment.assessment_id}:{record_id}")
            known_documentation_claim_ids.add(record.documentation_claim_id)
        for claim_id in assessment.support_claim_ids:
            claim = ledger.claims.get(claim_id)
            if claim is None:
                raise ValueError(f"custody support claim is missing: {assessment.assessment_id}:{claim_id}")
            if claim.semantic_minute > assessment.semantic_minute:
                raise ValueError(f"custody assessment predates support claim: {assessment.assessment_id}:{claim_id}")
            if claim_id not in known_documentation_claim_ids:
                raise ValueError(f"custody support claim has no known record: {assessment.assessment_id}:{claim_id}")
        for claim_id in assessment.compromise_claim_ids:
            claim = ledger.claims.get(claim_id)
            if claim is None:
                raise ValueError(f"custody compromise claim is missing: {assessment.assessment_id}:{claim_id}")
            if claim.semantic_minute > assessment.semantic_minute:
                raise ValueError(f"custody assessment predates compromise claim: {assessment.assessment_id}:{claim_id}")


def _validate_decision_chain(
    dependencies: AssessmentDecisionDependencyRegistry,
    reviews: AssessmentDecisionReviewRegistry,
    consequences: DecisionConsequenceRepairRegistry,
    custody: EvidenceCustodyRegistry,
    ledger_store: KnowledgeLedgerStore,
    *,
    semantic_minute: int,
) -> None:
    for decision in dependencies.decisions.values():
        if decision.semantic_minute > semantic_minute:
            raise ValueError(f"assessment-dependent decision comes from the future: {decision.decision_id}")
        assessment = custody.assessments.get(decision.basis_assessment_id)
        if assessment is None:
            raise ValueError(f"decision references missing basis assessment: {decision.decision_id}")
        if assessment.semantic_minute > decision.semantic_minute:
            raise ValueError(f"decision predates basis assessment: {decision.decision_id}")
        ledger = ledger_store.ledgers.get(decision.actor_id)
        if ledger is None:
            raise ValueError(f"decision references missing actor ledger: {decision.decision_id}")
        claim = ledger.claims.get(decision.basis_claim_id)
        if claim is None:
            raise ValueError(f"decision basis claim is missing: {decision.decision_id}")
        if claim.semantic_minute > decision.semantic_minute:
            raise ValueError(f"decision predates basis claim: {decision.decision_id}")
        if claim.provenance_root != f"custody-assessment:{assessment.assessment_id}":
            raise ValueError(f"decision basis provenance mismatch: {decision.decision_id}")
        if claim.subject != f"custody:{assessment.evidence_id}" or claim.value != assessment.status.value:
            raise ValueError(f"decision basis conclusion mismatch: {decision.decision_id}")

    for review in reviews.reviews.values():
        if review.semantic_minute > semantic_minute:
            raise ValueError(f"assessment decision review comes from the future: {review.review_id}")
        decision = dependencies.decisions.get(review.decision_id)
        if decision is None:
            raise ValueError(f"review references missing decision: {review.review_id}")
        if review.actor_id != decision.actor_id:
            raise ValueError(f"review actor mismatch: {review.review_id}")
        assessment = custody.assessments.get(review.superseding_assessment_id)
        if assessment is None:
            raise ValueError(f"review references missing superseding assessment: {review.review_id}")
        lineage_ids = tuple(row.assessment_id for row in custody.assessment_lineage(assessment.assessment_id))
        if decision.basis_assessment_id not in lineage_ids[:-1]:
            raise ValueError(f"review assessment does not supersede decision basis: {review.review_id}")
        ledger = ledger_store.ledgers.get(review.actor_id)
        if ledger is None:
            raise ValueError(f"review references missing actor ledger: {review.review_id}")
        claim = ledger.claims.get(review.superseding_claim_id)
        if claim is None:
            raise ValueError(f"review basis claim is missing: {review.review_id}")
        if claim.semantic_minute > review.semantic_minute:
            raise ValueError(f"review predates basis claim: {review.review_id}")
        if claim.provenance_root != f"custody-assessment:{assessment.assessment_id}":
            raise ValueError(f"review basis provenance mismatch: {review.review_id}")

    for consequence in consequences.consequences.values():
        decision = dependencies.decisions.get(consequence.decision_id)
        if decision is None:
            raise ValueError(f"consequence references missing decision: {consequence.consequence_id}")
        if consequence.applied_semantic_minute > semantic_minute:
            raise ValueError(f"decision consequence comes from the future: {consequence.consequence_id}")
        if consequence.applied_semantic_minute < decision.semantic_minute:
            raise ValueError(f"decision consequence predates decision: {consequence.consequence_id}")

    for repair in consequences.repairs.values():
        consequence = consequences.consequences.get(repair.consequence_id)
        review = reviews.reviews.get(repair.review_id)
        if consequence is None or review is None:
            raise ValueError(f"repair references missing consequence or review: {repair.repair_id}")
        if repair.semantic_minute > semantic_minute:
            raise ValueError(f"consequence repair comes from the future: {repair.repair_id}")
        if review.decision_id != consequence.decision_id:
            raise ValueError(f"repair review does not match consequence decision: {repair.repair_id}")
        if repair.actor_id != review.actor_id:
            raise ValueError(f"repair actor mismatch: {repair.repair_id}")
        if repair.semantic_minute < max(consequence.applied_semantic_minute, review.semantic_minute):
            raise ValueError(f"repair predates consequence or review: {repair.repair_id}")


def restore_checkpoint(
    snapshot: Mapping[str, object],
    *,
    channels: Mapping[str, CommunicationChannel],
    agendas: Mapping[str, AgentAgendaProfile] | None = None,
) -> RestoredWorldCheckpoint:
    """Validate the complete checkpoint before returning restored live objects."""
    payload = _validated_payload(snapshot)
    ledger_store = KnowledgeLedgerStore.restore(payload["knowledge_ledgers"])
    queue = _restore_information_queue(payload, channels=channels, ledgers=ledger_store.ledgers)
    replan_queue = NpcReplanQueue.from_snapshot(payload["replan_queue"])
    agents = {str(row["agent_id"]): agent_from_dict(row) for row in payload.get("agents", [])}
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=queue,
        replan_queue=replan_queue,
        agents=agents,
        agendas=agendas,
    )
    coordinator.materialized_delivery_event_ids = {str(value) for value in payload.get("materialized_delivery_event_ids", [])}
    attribution_registry = _restore_infrastructure_attribution(payload)
    custody_registry = _restore_evidence_custody(payload)
    dependency_registry = _restore_registry(
        payload,
        "assessment_decision_dependencies",
        AssessmentDecisionDependencyRegistry,
        AssessmentDecisionDependencyRegistry.restore,
    )
    review_registry = _restore_registry(
        payload,
        "assessment_decision_reviews",
        AssessmentDecisionReviewRegistry,
        AssessmentDecisionReviewRegistry.restore,
    )
    consequence_registry = _restore_registry(
        payload,
        "decision_consequence_repairs",
        DecisionConsequenceRepairRegistry,
        DecisionConsequenceRepairRegistry.restore,
    )
    _validate_references(queue=queue, coordinator=coordinator)
    _validate_infrastructure_attribution(attribution_registry, ledger_store, semantic_minute=int(payload["semantic_minute"]))
    _validate_evidence_custody(custody_registry, ledger_store, semantic_minute=int(payload["semantic_minute"]))
    _validate_decision_chain(
        dependency_registry,
        review_registry,
        consequence_registry,
        custody_registry,
        ledger_store,
        semantic_minute=int(payload["semantic_minute"]),
    )
    runtime = payload.get("publication_runtime")
    if runtime is not None and not isinstance(runtime, Mapping):
        raise ValueError("publication_runtime checkpoint must be a mapping or null")
    return RestoredWorldCheckpoint(
        semantic_minute=int(payload["semantic_minute"]),
        coordinator=coordinator,
        ledger_store=ledger_store,
        infrastructure_attribution_registry=attribution_registry,
        evidence_custody_registry=custody_registry,
        assessment_decision_dependency_registry=dependency_registry,
        assessment_decision_review_registry=review_registry,
        decision_consequence_repair_registry=consequence_registry,
        publication_runtime_snapshot=runtime,
    )


def replay_fixture(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    agents = {
        str(row["agent_id"]): NpcAgentState(
            agent_id=str(row["agent_id"]),
            mode=AgentMode(str(row.get("mode", "OFFSCREEN_NAMED"))),
            region_ref=str(row["region_ref"]),
            location_ref=str(row["location_ref"]),
        )
        for row in data["agents"]
    }
    ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
    channels = {
        str(row["channel_id"]): CommunicationChannel(
            channel_id=str(row["channel_id"]),
            kind=str(row["kind"]),
            latency_minutes=int(row["latency_minutes"]),
            available=bool(row.get("available", True)),
            requires_local_projection=bool(row.get("requires_local_projection", False)),
        )
        for row in data["channels"]
    }
    coordinator = GlobalNpcWorldEventCoordinator(
        information_queue=InformationEventQueue(channels=channels, ledgers=ledgers),
        replan_queue=NpcReplanQueue(),
        agents=agents,
    )
    results: list[dict] = []

    for event in data["events"]:
        kind = str(event["kind"])
        if kind == "observe":
            claim = record_direct_observation(
                coordinator.information_queue.ledgers[str(event["agent_id"])],
                claim_id=str(event["claim_id"]),
                subject=str(event["subject"]),
                value=str(event["value"]),
                semantic_minute=int(event["semantic_minute"]),
                confidence=int(event["confidence"]),
            )
            results.append({"event_id": event["event_id"], "claim_id": claim.claim_id})
        elif kind == "schedule":
            envelope = coordinator.information_queue.schedule(
                event_id=str(event["delivery_event_id"]),
                message_id=str(event["message_id"]),
                sender_id=str(event["sender_id"]),
                receiver_id=str(event["receiver_id"]),
                source_claim_id=str(event["source_claim_id"]),
                new_claim_id=str(event["new_claim_id"]),
                channel_id=str(event["channel_id"]),
                created_minute=int(event["semantic_minute"]),
            )
            results.append({"event_id": event["event_id"], "delivery_minute": envelope.delivery_minute})
        elif kind == "checkpoint_restart":
            checkpoint = build_checkpoint(coordinator, semantic_minute=int(event["semantic_minute"]))
            restored = restore_checkpoint(checkpoint, channels=channels)
            coordinator = restored.coordinator
            results.append({
                "event_id": event["event_id"],
                "status": "RESTORED",
                "semantic_minute": restored.semantic_minute,
                "digest": checkpoint["sha256"],
            })
        elif kind == "cycle":
            cycle = coordinator.process_cycle(int(event["semantic_minute"]), delivery_budget=int(event["delivery_budget"]))
            results.append({
                "event_id": event["event_id"],
                "processed": cycle.delivery_processed_count,
                "deferred": cycle.delivery_deferred_due_count,
                "wake_statuses": [row.wake_status for row in cycle.materialized],
                "decision_agent_ids": [row.agent_id for row in cycle.decisions],
            })
        elif kind == "inspect":
            agent_id = str(event["agent_id"])
            results.append({
                "event_id": event["event_id"],
                "claim_ids": sorted(coordinator.information_queue.ledgers[agent_id].claims),
                "knowledge": sorted(coordinator.agents[agent_id].knowledge),
                "delivered_event_ids": sorted(coordinator.information_queue.delivered_event_ids),
                "materialized_event_ids": sorted(coordinator.materialized_delivery_event_ids),
            })
        else:
            raise ValueError(f"unsupported fixture event kind: {kind}")

    return {"fixture_id": data["fixture_id"], "results": results}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m tools.global_npc_world_checkpoint <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))