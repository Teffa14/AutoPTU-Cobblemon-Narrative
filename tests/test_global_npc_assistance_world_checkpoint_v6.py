import copy
import hashlib
import json
import unittest

from tools.global_npc_ai import AgentMode, NpcAgentState, ScheduledCommitment
from tools.global_npc_assistance_acceptance_commitment import AssistanceCommitmentLedger
from tools.global_npc_assistance_commitment_disposition import (
    AssistanceCommitmentDisposition,
    AssistanceCommitmentDispositionLedger,
    CommitmentStartDisposition,
)
from tools.global_npc_assistance_commitment_start import (
    AssistanceCommitmentStartAssessment,
    AssistanceCommitmentStartLedger,
    AssistanceCommitmentStartWatch,
    CommitmentStartCondition,
)
from tools.global_npc_assistance_commitment_viability import (
    AssistanceCommitmentViabilityLedger,
    AssistanceCommitmentViabilityObservation,
)
from tools.global_npc_assistance_counterproposal import AssistanceCounterproposalLedger, AssistanceCounterproposalRecord
from tools.global_npc_assistance_counterproposal_commitment import (
    AssistanceCounterproposalCommitmentLedger,
    AssistanceCounterproposalCommitmentRecord,
)
from tools.global_npc_assistance_renegotiation_decision import (
    AssistanceRenegotiationDecision,
    AssistanceRenegotiationDecisionLedger,
    AssistanceRenegotiationDecisionRecord,
)
from tools.global_npc_assistance_renegotiation_proposal import (
    AssistanceRenegotiationProposalLedger,
    AssistanceRenegotiationProposalRecord,
)
from tools.global_npc_assistance_renegotiation_proposal_decision import (
    AssistanceRenegotiationProposalDecisionLedger,
    AssistanceRenegotiationProposalDecisionRecord,
    AssistanceRenegotiationProposalOutcome,
)
from tools.global_npc_assistance_renegotiation_replacement_commitment import (
    AssistanceRenegotiationReplacementCommitmentLedger,
    AssistanceRenegotiationReplacementCommitmentRecord,
)
from tools.global_npc_assistance_world_checkpoint_v5 import build_assistance_world_checkpoint_v5
from tools.global_npc_assistance_world_checkpoint_v6 import (
    build_assistance_world_checkpoint_v6,
    restore_assistance_world_checkpoint_v6,
)
from tools.global_npc_information_network import CommunicationChannel, InformationEventQueue
from tools.global_npc_memory import Claim, KnowledgeLedger, SourceKind
from tools.global_npc_replanning import NpcReplanQueue, ReplanReason, ReplanTrigger
from tools.global_npc_world_action_intent import WorldActionIntentLedger, WorldActionIntentRecord
from tools.global_npc_world_event_coordinator import AgentAgendaProfile, GlobalNpcWorldEventCoordinator


class AssistanceWorldCheckpointV6Tests(unittest.TestCase):
    @staticmethod
    def _redigest(checkpoint: dict) -> None:
        payload = {key: value for key, value in checkpoint.items() if key != "sha256"}
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        checkpoint["sha256"] = hashlib.sha256(raw).hexdigest()

    @staticmethod
    def _deliver(queue, ledgers, *, event_id, sender, receiver, minute, root):
        source_id = f"claim:{event_id}:source"
        ledgers[sender].add(
            Claim(
                claim_id=source_id,
                subject=f"subject:{event_id}",
                value=f"payload:{event_id}",
                source_kind=SourceKind.AUTHORED_START,
                source_agent_id=sender,
                semantic_minute=minute,
                confidence=100,
                provenance_root=root,
            )
        )
        queue.schedule(
            event_id=event_id,
            message_id=f"message:{event_id}",
            sender_id=sender,
            receiver_id=receiver,
            source_claim_id=source_id,
            new_claim_id=f"claim:{event_id}:received",
            channel_id="wire",
            created_minute=minute,
        )
        queue.process_due(minute)

    def _state(self):
        requester = "requester"
        responder = "responder"
        agents = {
            requester: NpcAgentState(requester, AgentMode.OFFSCREEN_NAMED, "synthetic", "station"),
            responder: NpcAgentState(responder, AgentMode.OFFSCREEN_NAMED, "synthetic", "workshop"),
        }
        channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 0)}
        ledgers = {agent_id: KnowledgeLedger(agent_id) for agent_id in agents}
        information = InformationEventQueue(channels=channels, ledgers=ledgers)
        replan = NpcReplanQueue()

        old = ScheduledCommitment(
            commitment_id="commit:old", intent_kind="ASSIST_SURVEY", start_minute=80, end_minute=110,
            priority=8, hard=False, grace_minutes=5, required_knowledge=frozenset(),
            required_permissions=frozenset(), target_ref=requester, requires_local_projection=True,
            requires_structured_mechanics=False,
        )
        replacement = ScheduledCommitment(
            commitment_id="commit:new", intent_kind="ASSIST_SURVEY", start_minute=120, end_minute=150,
            priority=8, hard=False, grace_minutes=5, required_knowledge=frozenset(),
            required_permissions=frozenset(), target_ref=requester, requires_local_projection=True,
            requires_structured_mechanics=False,
        )
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=information,
            replan_queue=replan,
            agents=agents,
            agendas={responder: AgentAgendaProfile(commitments=(replacement,))},
        )

        actions = WorldActionIntentLedger()
        actions.records["request:1"] = WorldActionIntentRecord(
            action_id="request:1", agent_id=requester, intent_id="intent:req", intent_kind="REQUEST_ASSISTANCE",
            target_ref=responder, semantic_minute=10, trigger_ids=("t:req",), reason_codes=("NEEDS_SUPPORT",),
            source_type="SITUATIONAL", source_ref="site:crossing",
        )
        actions.records["response:1"] = WorldActionIntentRecord(
            action_id="response:1", agent_id=responder, intent_id="intent:counter",
            intent_kind="COUNTERPROPOSE_ASSISTANCE_REQUEST", target_ref=requester, semantic_minute=20,
            trigger_ids=("t:counter",), reason_codes=("CAN_HELP_LATER",), source_type="SITUATIONAL",
            source_ref="request:1",
        )
        actions.records["decision:1"] = WorldActionIntentRecord(
            action_id="decision:1", agent_id=requester, intent_id="intent:accept",
            intent_kind="ACCEPT_ASSISTANCE_COUNTERPROPOSAL", target_ref=responder, semantic_minute=30,
            trigger_ids=("t:accept",), reason_codes=("TERMS_ACCEPTED",), source_type="SITUATIONAL",
            source_ref="proposal:old",
        )

        proposals = AssistanceCounterproposalLedger()
        proposals.add(AssistanceCounterproposalRecord(
            proposal_id="proposal:old", request_action_id="request:1", response_action_id="response:1",
            requester_id=requester, responder_id=responder, proposed_start_minute=80, proposed_end_minute=110,
            location_ref="site:old", scope_ref="scope:survey", alternative_ref="alternative:report",
            expires_minute=50, provenance_root="response:1",
        ))
        negotiated = AssistanceCounterproposalCommitmentLedger()
        negotiated.add(AssistanceCounterproposalCommitmentRecord(
            commitment_id="commit:old", proposal_id="proposal:old", request_action_id="request:1",
            response_action_id="response:1", decision_action_id="decision:1", requester_id=requester,
            responder_id=responder, intent_kind="ASSIST_SURVEY", start_minute=80, end_minute=110,
            location_ref="site:old", scope_ref="scope:survey", alternative_ref="alternative:report",
            priority=8, hard=False, grace_minutes=5, required_knowledge=(), required_permissions=(),
            requires_local_projection=True, requires_structured_mechanics=False, provenance_root="decision:1",
        ))

        viability = AssistanceCommitmentViabilityLedger()
        viability.add(AssistanceCommitmentViabilityObservation(
            observation_id="viability:1", commitment_id="commit:old", proposal_id="proposal:old",
            requester_id=requester, responder_id=responder, observer_id=responder, semantic_minute=40,
            viability="BLOCKED", constraint_kind="ROUTE_UNAVAILABLE", constraint_ref="route:crossing",
            evidence_ref="claim:closure", provenance_root="claim:closure",
        ))
        replan.schedule(ReplanTrigger(
            trigger_id="replan:assistance-viability:viability:1", agent_id=responder,
            reason=ReplanReason.EXTERNAL_EVENT, due_minute=40, source_ref="viability:1", priority=8,
        ))
        start = AssistanceCommitmentStartLedger()
        start.add_watch(AssistanceCommitmentStartWatch(
            watch_id="watch:1", commitment_id="commit:old", proposal_id="proposal:old", requester_id=requester,
            responder_id=responder, start_minute=80, armed_minute=45, provenance_root="viability:1",
            trigger_id="replan:assistance-start:watch:1",
        ))
        replan.schedule(ReplanTrigger(
            trigger_id="replan:assistance-start:watch:1", agent_id=responder,
            reason=ReplanReason.SCHEDULE_DUE, due_minute=80, source_ref="watch:1", priority=9,
        ))
        replan.process_due(80)
        start.add_assessment(AssistanceCommitmentStartAssessment(
            assessment_id="assessment:1", watch_id="watch:1", commitment_id="commit:old",
            proposal_id="proposal:old", requester_id=requester, responder_id=responder, semantic_minute=80,
            condition=CommitmentStartCondition.BLOCKED_AT_START.value, viability_observation_id="viability:1",
            constraint_kind="ROUTE_UNAVAILABLE", constraint_ref="route:crossing", evidence_ref="claim:closure",
            provenance_root="claim:closure",
        ))
        dispositions = AssistanceCommitmentDispositionLedger()
        dispositions.add(AssistanceCommitmentDisposition(
            disposition_id="disposition:1", commitment_id="commit:old", proposal_id="proposal:old",
            assessment_id="assessment:1", requester_id=requester, responder_id=responder, actor_id=responder,
            semantic_minute=80, disposition=CommitmentStartDisposition.REQUEST_RENEGOTIATION.value,
            rationale_ref="reason:blocked", provenance_root="assessment:1",
        ))

        self._deliver(information, ledgers, event_id="event:request", sender=responder, receiver=requester, minute=81, root="assessment:1")
        reopen_decisions = AssistanceRenegotiationDecisionLedger()
        reopen_decisions.add(AssistanceRenegotiationDecisionRecord(
            decision_id="decision:reopen", commitment_id="commit:old", proposal_id="proposal:old",
            disposition_id="disposition:1", request_event_id="event:request", requester_id=requester,
            responder_id=responder, decision=AssistanceRenegotiationDecision.ACCEPT_REOPENING.value,
            semantic_minute=82, rationale_ref="reason:okay", provenance_root="assessment:1",
        ))

        self._deliver(information, ledgers, event_id="event:reopen-reply", sender=requester, receiver=responder, minute=83, root="decision:reopen")
        replacement_proposals = AssistanceRenegotiationProposalLedger()
        replacement_proposals.add(AssistanceRenegotiationProposalRecord(
            proposal_id="proposal:new", supersedes_commitment_id="commit:old",
            supersedes_proposal_id="proposal:old", decision_id="decision:reopen",
            decision_reply_event_id="event:reopen-reply", requester_id=requester, responder_id=responder,
            proposed_start_minute=120, proposed_end_minute=150, location_ref="site:new",
            scope_ref="scope:survey", alternative_ref="alternative:remote", expires_minute=100,
            semantic_minute=84, decision_provenance_root="assessment:1", provenance_root="proposal:new",
        ))

        self._deliver(information, ledgers, event_id="event:offer", sender=responder, receiver=requester, minute=85, root="proposal:new")
        offer_decisions = AssistanceRenegotiationProposalDecisionLedger()
        offer_decisions.add(AssistanceRenegotiationProposalDecisionRecord(
            decision_id="decision:offer", proposal_id="proposal:new", supersedes_commitment_id="commit:old",
            supersedes_proposal_id="proposal:old", proposal_event_id="event:offer", requester_id=requester,
            responder_id=responder, outcome=AssistanceRenegotiationProposalOutcome.ACCEPT.value,
            semantic_minute=86, rationale_ref="reason:accepted", proposal_provenance_root="proposal:new",
            provenance_root="proposal:new",
        ))

        self._deliver(information, ledgers, event_id="event:offer-reply", sender=requester, receiver=responder, minute=87, root="decision:offer")
        replacements = AssistanceRenegotiationReplacementCommitmentLedger()
        replacements.add(AssistanceRenegotiationReplacementCommitmentRecord(
            commitment_id="commit:new", supersedes_commitment_id="commit:old",
            replacement_proposal_id="proposal:new", proposal_decision_id="decision:offer",
            decision_reply_event_id="event:offer-reply", requester_id=requester, responder_id=responder,
            intent_kind="ASSIST_SURVEY", start_minute=120, end_minute=150, location_ref="site:new",
            scope_ref="scope:survey", alternative_ref="alternative:remote", priority=8, hard=False,
            grace_minutes=5, required_knowledge=(), required_permissions=(), requires_local_projection=True,
            requires_structured_mechanics=False, superseded_provenance_root="decision:1",
            proposal_provenance_root="proposal:new", provenance_root="decision:offer",
        ))
        return {
            "coordinator": coordinator,
            "channels": channels,
            "actions": actions,
            "proposals": proposals,
            "negotiated": negotiated,
            "viability": viability,
            "start": start,
            "dispositions": dispositions,
            "reopen_decisions": reopen_decisions,
            "replacement_proposals": replacement_proposals,
            "offer_decisions": offer_decisions,
            "replacements": replacements,
        }

    def _build(self, state):
        return build_assistance_world_checkpoint_v6(
            state["coordinator"], semantic_minute=90, action_ledger=state["actions"],
            commitment_ledger=AssistanceCommitmentLedger(), counterproposal_ledger=state["proposals"],
            counterproposal_commitment_ledger=state["negotiated"], commitment_viability_ledger=state["viability"],
            commitment_start_ledger=state["start"], commitment_disposition_ledger=state["dispositions"],
            renegotiation_decision_ledger=state["reopen_decisions"],
            renegotiation_proposal_ledger=state["replacement_proposals"],
            renegotiation_proposal_decision_ledger=state["offer_decisions"],
            replacement_commitment_ledger=state["replacements"],
        )

    def test_restart_preserves_history_but_restores_only_replacement_schedule(self):
        state = self._state()
        checkpoint = self._build(state)
        restored = restore_assistance_world_checkpoint_v6(checkpoint, channels=state["channels"])
        self.assertIn("commit:old", restored.counterproposal_commitment_ledger.records)
        self.assertIn("commit:new", restored.replacement_commitment_ledger.records)
        agenda_ids = [row.commitment_id for row in restored.world.coordinator.agendas["responder"].commitments]
        self.assertEqual(agenda_ids, ["commit:new"])
        self.assertEqual(restored.renegotiation_proposal_ledger.records["proposal:new"].supersedes_commitment_id, "commit:old")
        second = restore_assistance_world_checkpoint_v6(checkpoint, channels=state["channels"])
        self.assertEqual(
            second.replacement_commitment_ledger.records["commit:new"],
            restored.replacement_commitment_ledger.records["commit:new"],
        )

    def test_redigested_snapshot_cannot_detach_replacement_from_old_commitment(self):
        state = self._state()
        checkpoint = self._build(state)
        corrupted = copy.deepcopy(checkpoint)
        corrupted["assistance_renegotiation_replacement_commitments"]["records"][0]["supersedes_commitment_id"] = "commit:missing"
        self._redigest(corrupted)
        with self.assertRaisesRegex(ValueError, "missing causal state"):
            restore_assistance_world_checkpoint_v6(corrupted, channels=state["channels"])

    def test_v5_restore_defaults_post_v5_renegotiation_ledgers_to_empty(self):
        agents = {"npc": NpcAgentState("npc", AgentMode.OFFSCREEN_NAMED, "synthetic", "home")}
        channels = {"wire": CommunicationChannel("wire", "REMOTE_MESSAGE", 0)}
        coordinator = GlobalNpcWorldEventCoordinator(
            information_queue=InformationEventQueue(channels=channels, ledgers={"npc": KnowledgeLedger("npc")}),
            replan_queue=NpcReplanQueue(), agents=agents,
        )
        legacy = build_assistance_world_checkpoint_v5(
            coordinator, semantic_minute=0, action_ledger=WorldActionIntentLedger(),
            commitment_ledger=AssistanceCommitmentLedger(),
        )
        restored = restore_assistance_world_checkpoint_v6(legacy, channels=channels)
        self.assertEqual(restored.renegotiation_decision_ledger.records, {})
        self.assertEqual(restored.renegotiation_proposal_ledger.records, {})
        self.assertEqual(restored.renegotiation_proposal_decision_ledger.records, {})
        self.assertEqual(restored.replacement_commitment_ledger.records, {})

    def test_checkpoint_v6_has_no_tactical_or_social_execution_surface(self):
        source = open("tools/global_npc_assistance_world_checkpoint_v6.py", encoding="utf-8").read().lower()
        for forbidden in (
            "request_autoptu", "reserve_route", "consume_item", "apply_damage", "roll_accuracy",
            "knockback", "relationship_delta", "adjudicate_blame", "grant_permission",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
