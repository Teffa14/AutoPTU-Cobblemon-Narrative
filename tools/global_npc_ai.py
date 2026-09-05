from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Iterable, Mapping, FrozenSet


class AgentMode(str, Enum):
    OFFSCREEN_NAMED = "OFFSCREEN_NAMED"
    LOCAL_DORMANT = "LOCAL_DORMANT"
    LOCAL_ACTIVE = "LOCAL_ACTIVE"
    CONVERSATION_LOCKED = "CONVERSATION_LOCKED"
    AUTOPTU_BOUND = "AUTOPTU_BOUND"
    SUSPENDED = "SUSPENDED"


class Handoff(str, Enum):
    NONE = "NONE"
    REQUEST_AUTOPTU = "REQUEST_AUTOPTU"
    HOLD_EXISTING_AUTOPTU_BINDING = "HOLD_EXISTING_AUTOPTU_BINDING"


@dataclass(frozen=True)
class NpcIntent:
    intent_id: str
    kind: str
    base_priority: int = 0
    urgency: int = 0
    obligation: int = 0
    risk: int = 0
    travel_cost: int = 0
    relationship_weight: int = 0
    required_knowledge: FrozenSet[str] = frozenset()
    required_permissions: FrozenSet[str] = frozenset()
    requires_local_projection: bool = False
    requires_structured_mechanics: bool = False
    target_ref: str | None = None


@dataclass(frozen=True)
class NpcAgentState:
    agent_id: str
    mode: AgentMode
    region_ref: str
    location_ref: str
    risk_tolerance: int = 50
    energy: int = 100
    knowledge: FrozenSet[str] = frozenset()
    permissions: FrozenSet[str] = frozenset()
    memory_refs: tuple[str, ...] = ()
    active_autoptu_binding: str | None = None


@dataclass(frozen=True)
class Decision:
    agent_id: str
    intent_id: str | None
    kind: str
    score: int | None
    handoff: Handoff
    reason_codes: tuple[str, ...] = ()
    target_ref: str | None = None


@dataclass(frozen=True)
class DurableGoal:
    goal_id: str
    intent_kind: str
    priority: int
    progress: int = 0
    target_progress: int = 100
    required_knowledge: FrozenSet[str] = frozenset()
    required_permissions: FrozenSet[str] = frozenset()
    target_ref: str | None = None
    requires_local_projection: bool = False
    requires_structured_mechanics: bool = False

    @property
    def complete(self) -> bool:
        return self.progress >= self.target_progress


@dataclass(frozen=True)
class NeedState:
    need_id: str
    intent_kind: str
    pressure: int
    activation_threshold: int
    critical_threshold: int = 90
    target_ref: str | None = None


@dataclass(frozen=True)
class ScheduledCommitment:
    commitment_id: str
    intent_kind: str
    start_minute: int
    end_minute: int
    priority: int = 5
    hard: bool = False
    grace_minutes: int = 0
    required_knowledge: FrozenSet[str] = frozenset()
    required_permissions: FrozenSet[str] = frozenset()
    target_ref: str | None = None
    requires_local_projection: bool = False
    requires_structured_mechanics: bool = False


@dataclass(frozen=True)
class PlanningContext:
    semantic_minute: int
    active_intent_id: str | None = None
    continuity_bonus: int = 1


@dataclass(frozen=True)
class AgendaDecision:
    decision: Decision
    source_type: str
    source_ref: str | None
    schedule_state: str | None = None


def _intent_is_eligible(agent: NpcAgentState, intent: NpcIntent) -> tuple[bool, tuple[str, ...]]:
    reasons: list[str] = []

    if not intent.required_knowledge.issubset(agent.knowledge):
        reasons.append("MISSING_KNOWLEDGE")

    if not intent.required_permissions.issubset(agent.permissions):
        reasons.append("MISSING_PERMISSION")

    if intent.requires_local_projection and agent.mode == AgentMode.OFFSCREEN_NAMED:
        reasons.append("LOCAL_PROJECTION_REQUIRED")

    if agent.mode in {AgentMode.CONVERSATION_LOCKED, AgentMode.SUSPENDED}:
        reasons.append("AGENT_MODE_BLOCKS_PLANNING")

    return (not reasons, tuple(reasons))


def score_intent(agent: NpcAgentState, intent: NpcIntent) -> int:
    """Deterministic Ouros world-agent utility score.

    This is world/NPC policy, not PTU arithmetic. It never evaluates tactical
    legality, damage, movement squares, HP, status or move resolution.
    """
    risk_penalty = intent.risk * max(0, 100 - max(0, min(100, agent.risk_tolerance)))
    energy_penalty = max(0, intent.travel_cost - max(0, agent.energy)) * 4

    return (
        intent.base_priority * 100
        + intent.obligation * 80
        + intent.urgency * 60
        + intent.relationship_weight * 20
        - risk_penalty
        - intent.travel_cost * 8
        - energy_penalty
    )


def choose_intent(agent: NpcAgentState, intents: Iterable[NpcIntent]) -> Decision:
    """Choose one global/world intent without executing tactical mechanics."""
    if agent.mode == AgentMode.AUTOPTU_BOUND:
        return Decision(
            agent_id=agent.agent_id,
            intent_id=None,
            kind="HOLD_AUTOPTU",
            score=None,
            handoff=Handoff.HOLD_EXISTING_AUTOPTU_BINDING,
            reason_codes=("AUTOPTU_ALREADY_OWNS_STRUCTURED_RESOLUTION",),
        )

    eligible: list[tuple[int, str, NpcIntent]] = []
    for intent in intents:
        ok, _ = _intent_is_eligible(agent, intent)
        if ok:
            eligible.append((score_intent(agent, intent), intent.intent_id, intent))

    if not eligible:
        return Decision(
            agent_id=agent.agent_id,
            intent_id=None,
            kind="WAIT",
            score=None,
            handoff=Handoff.NONE,
            reason_codes=("NO_ELIGIBLE_INTENT",),
        )

    eligible.sort(key=lambda row: (-row[0], row[1]))
    score, _, chosen = eligible[0]

    if chosen.requires_structured_mechanics:
        return Decision(
            agent_id=agent.agent_id,
            intent_id=chosen.intent_id,
            kind=chosen.kind,
            score=score,
            handoff=Handoff.REQUEST_AUTOPTU,
            reason_codes=("WORLD_INTENT_SELECTED", "STRUCTURED_MECHANICS_REQUIRED"),
            target_ref=chosen.target_ref,
        )

    return Decision(
        agent_id=agent.agent_id,
        intent_id=chosen.intent_id,
        kind=chosen.kind,
        score=score,
        handoff=Handoff.NONE,
        reason_codes=("WORLD_INTENT_SELECTED",),
        target_ref=chosen.target_ref,
    )


def schedule_state(commitment: ScheduledCommitment, semantic_minute: int) -> str:
    if semantic_minute < commitment.start_minute:
        return "UPCOMING"
    if semantic_minute <= commitment.end_minute:
        return "DUE"
    if semantic_minute <= commitment.end_minute + max(0, commitment.grace_minutes):
        return "GRACE"
    return "MISSED"


def _goal_intent(goal: DurableGoal) -> NpcIntent | None:
    if goal.complete:
        return None
    remaining = max(0, goal.target_progress - goal.progress)
    urgency = min(10, max(0, remaining // 10))
    return NpcIntent(
        intent_id=f"goal:{goal.goal_id}",
        kind=goal.intent_kind,
        base_priority=goal.priority,
        urgency=urgency,
        required_knowledge=goal.required_knowledge,
        required_permissions=goal.required_permissions,
        target_ref=goal.target_ref,
        requires_local_projection=goal.requires_local_projection,
        requires_structured_mechanics=goal.requires_structured_mechanics,
    )


def _need_intent(need: NeedState) -> NpcIntent | None:
    if need.pressure < need.activation_threshold:
        return None
    critical = need.pressure >= need.critical_threshold
    return NpcIntent(
        intent_id=f"need:{need.need_id}",
        kind=need.intent_kind,
        base_priority=8 if critical else 3,
        urgency=min(10, max(1, need.pressure // 10)),
        target_ref=need.target_ref,
    )


def _commitment_intent(
    commitment: ScheduledCommitment,
    semantic_minute: int,
) -> tuple[NpcIntent | None, str]:
    state = schedule_state(commitment, semantic_minute)
    if state == "UPCOMING":
        return None, state
    if state == "MISSED":
        return (
            NpcIntent(
                intent_id=f"missed:{commitment.commitment_id}",
                kind="RESCHEDULE_OR_REPORT_MISSED_COMMITMENT",
                base_priority=commitment.priority,
                urgency=8 if commitment.hard else 4,
                obligation=8 if commitment.hard else 4,
                required_knowledge=commitment.required_knowledge,
                required_permissions=commitment.required_permissions,
                target_ref=commitment.target_ref,
            ),
            state,
        )
    urgency = 10 if commitment.hard else (6 if state == "DUE" else 8)
    obligation = 10 if commitment.hard else 6
    return (
        NpcIntent(
            intent_id=f"commitment:{commitment.commitment_id}",
            kind=commitment.intent_kind,
            base_priority=commitment.priority,
            urgency=urgency,
            obligation=obligation,
            required_knowledge=commitment.required_knowledge,
            required_permissions=commitment.required_permissions,
            target_ref=commitment.target_ref,
            requires_local_projection=commitment.requires_local_projection,
            requires_structured_mechanics=commitment.requires_structured_mechanics,
        ),
        state,
    )


def choose_agenda_intent(
    agent: NpcAgentState,
    *,
    goals: Iterable[DurableGoal] = (),
    needs: Iterable[NeedState] = (),
    commitments: Iterable[ScheduledCommitment] = (),
    situational_intents: Iterable[NpcIntent] = (),
    context: PlanningContext,
) -> AgendaDecision:
    """Select world action from durable goals, needs, commitments and events.

    Time is supplied explicitly as Ouros semantic time. No wall-clock,
    Minecraft tick, chunk-load or entity-presence inference is performed here.
    """
    if agent.mode == AgentMode.AUTOPTU_BOUND:
        return AgendaDecision(choose_intent(agent, ()), "SYSTEM", None)

    candidates: list[tuple[NpcIntent, str, str | None, str | None]] = []

    for goal in goals:
        intent = _goal_intent(goal)
        if intent is not None:
            candidates.append((intent, "GOAL", goal.goal_id, None))

    for need in needs:
        intent = _need_intent(need)
        if intent is not None:
            candidates.append((intent, "NEED", need.need_id, None))

    for commitment in commitments:
        intent, state = _commitment_intent(commitment, context.semantic_minute)
        if intent is not None:
            candidates.append((intent, "COMMITMENT", commitment.commitment_id, state))

    for intent in situational_intents:
        candidates.append((intent, "SITUATIONAL", intent.intent_id, None))

    if not candidates:
        return AgendaDecision(choose_intent(agent, ()), "SYSTEM", None)

    scored: list[tuple[int, str, NpcIntent, str, str | None, str | None]] = []
    for intent, source_type, source_ref, state in candidates:
        ok, _ = _intent_is_eligible(agent, intent)
        if not ok:
            continue
        score = score_intent(agent, intent)
        if context.active_intent_id == intent.intent_id:
            score += max(0, context.continuity_bonus) * 100
        scored.append((score, intent.intent_id, intent, source_type, source_ref, state))

    if not scored:
        return AgendaDecision(choose_intent(agent, ()), "SYSTEM", None)

    scored.sort(key=lambda row: (-row[0], row[1]))
    score, _, chosen, source_type, source_ref, state = scored[0]
    handoff = Handoff.REQUEST_AUTOPTU if chosen.requires_structured_mechanics else Handoff.NONE
    reasons = ["AGENDA_INTENT_SELECTED", f"SOURCE_{source_type}"]
    if context.active_intent_id == chosen.intent_id and context.continuity_bonus > 0:
        reasons.append("CONTINUITY_PRESERVED")
    if state == "MISSED":
        reasons.append("MISSED_COMMITMENT_REQUIRES_FOLLOWUP")
    if handoff == Handoff.REQUEST_AUTOPTU:
        reasons.append("STRUCTURED_MECHANICS_REQUIRED")
    return AgendaDecision(
        Decision(
            agent_id=agent.agent_id,
            intent_id=chosen.intent_id,
            kind=chosen.kind,
            score=score,
            handoff=handoff,
            reason_codes=tuple(reasons),
            target_ref=chosen.target_ref,
        ),
        source_type,
        source_ref,
        state,
    )


def receive_information(
    agent: NpcAgentState,
    *,
    claim_ref: str,
    provenance_ref: str,
) -> NpcAgentState:
    """Add one observed/communicated claim to this NPC's private knowledge."""
    memory = agent.memory_refs
    if provenance_ref not in memory:
        memory = memory + (provenance_ref,)
    return replace(
        agent,
        knowledge=frozenset(set(agent.knowledge) | {claim_ref}),
        memory_refs=memory,
    )


def bind_autoptu(agent: NpcAgentState, binding_ref: str) -> NpcAgentState:
    if agent.active_autoptu_binding is not None:
        raise ValueError("agent already has an AutoPTU binding")
    return replace(
        agent,
        mode=AgentMode.AUTOPTU_BOUND,
        active_autoptu_binding=binding_ref,
    )


def release_autoptu(
    agent: NpcAgentState,
    *,
    local_after_release: bool = True,
) -> NpcAgentState:
    if agent.active_autoptu_binding is None:
        raise ValueError("agent has no AutoPTU binding")
    return replace(
        agent,
        mode=AgentMode.LOCAL_ACTIVE if local_after_release else AgentMode.OFFSCREEN_NAMED,
        active_autoptu_binding=None,
    )


def agent_from_dict(data: Mapping[str, object]) -> NpcAgentState:
    return NpcAgentState(
        agent_id=str(data["agent_id"]),
        mode=AgentMode(str(data["mode"])),
        region_ref=str(data["region_ref"]),
        location_ref=str(data["location_ref"]),
        risk_tolerance=int(data.get("risk_tolerance", 50)),
        energy=int(data.get("energy", 100)),
        knowledge=frozenset(str(v) for v in data.get("knowledge", [])),
        permissions=frozenset(str(v) for v in data.get("permissions", [])),
        memory_refs=tuple(str(v) for v in data.get("memory_refs", [])),
        active_autoptu_binding=(
            None
            if data.get("active_autoptu_binding") is None
            else str(data["active_autoptu_binding"])
        ),
    )


def intent_from_dict(data: Mapping[str, object]) -> NpcIntent:
    return NpcIntent(
        intent_id=str(data["intent_id"]),
        kind=str(data["kind"]),
        base_priority=int(data.get("base_priority", 0)),
        urgency=int(data.get("urgency", 0)),
        obligation=int(data.get("obligation", 0)),
        risk=int(data.get("risk", 0)),
        travel_cost=int(data.get("travel_cost", 0)),
        relationship_weight=int(data.get("relationship_weight", 0)),
        required_knowledge=frozenset(str(v) for v in data.get("required_knowledge", [])),
        required_permissions=frozenset(str(v) for v in data.get("required_permissions", [])),
        requires_local_projection=bool(data.get("requires_local_projection", False)),
        requires_structured_mechanics=bool(data.get("requires_structured_mechanics", False)),
        target_ref=None if data.get("target_ref") is None else str(data["target_ref"]),
    )


def goal_from_dict(data: Mapping[str, object]) -> DurableGoal:
    return DurableGoal(
        goal_id=str(data["goal_id"]),
        intent_kind=str(data["intent_kind"]),
        priority=int(data.get("priority", 0)),
        progress=int(data.get("progress", 0)),
        target_progress=int(data.get("target_progress", 100)),
        required_knowledge=frozenset(str(v) for v in data.get("required_knowledge", [])),
        required_permissions=frozenset(str(v) for v in data.get("required_permissions", [])),
        target_ref=None if data.get("target_ref") is None else str(data["target_ref"]),
        requires_local_projection=bool(data.get("requires_local_projection", False)),
        requires_structured_mechanics=bool(data.get("requires_structured_mechanics", False)),
    )


def need_from_dict(data: Mapping[str, object]) -> NeedState:
    return NeedState(
        need_id=str(data["need_id"]),
        intent_kind=str(data["intent_kind"]),
        pressure=int(data["pressure"]),
        activation_threshold=int(data.get("activation_threshold", 50)),
        critical_threshold=int(data.get("critical_threshold", 90)),
        target_ref=None if data.get("target_ref") is None else str(data["target_ref"]),
    )


def commitment_from_dict(data: Mapping[str, object]) -> ScheduledCommitment:
    return ScheduledCommitment(
        commitment_id=str(data["commitment_id"]),
        intent_kind=str(data["intent_kind"]),
        start_minute=int(data["start_minute"]),
        end_minute=int(data["end_minute"]),
        priority=int(data.get("priority", 5)),
        hard=bool(data.get("hard", False)),
        grace_minutes=int(data.get("grace_minutes", 0)),
        required_knowledge=frozenset(str(v) for v in data.get("required_knowledge", [])),
        required_permissions=frozenset(str(v) for v in data.get("required_permissions", [])),
        target_ref=None if data.get("target_ref") is None else str(data["target_ref"]),
        requires_local_projection=bool(data.get("requires_local_projection", False)),
        requires_structured_mechanics=bool(data.get("requires_structured_mechanics", False)),
    )


def run_fixture(data: Mapping[str, object]) -> dict[str, Decision]:
    """Execute region-neutral scenarios from a machine-readable fixture."""
    agents = {
        str(raw["agent_id"]): agent_from_dict(raw)
        for raw in data.get("agents", [])
    }
    decisions: dict[str, Decision] = {}

    for scenario in data.get("scenarios", []):
        scenario_id = str(scenario["scenario_id"])
        agent = agents[str(scenario["agent_id"])]

        for info in scenario.get("information_before_decision", []):
            agent = receive_information(
                agent,
                claim_ref=str(info["claim_ref"]),
                provenance_ref=str(info["provenance_ref"]),
            )

        intents = [intent_from_dict(raw) for raw in scenario.get("intents", [])]
        decisions[scenario_id] = choose_intent(agent, intents)

    return decisions


def run_agenda_fixture(data: Mapping[str, object]) -> dict[str, AgendaDecision]:
    """Execute global goal/need/schedule scenarios without local special cases."""
    agents = {
        str(raw["agent_id"]): agent_from_dict(raw)
        for raw in data.get("agents", [])
    }
    decisions: dict[str, AgendaDecision] = {}

    for scenario in data.get("scenarios", []):
        scenario_id = str(scenario["scenario_id"])
        agent = agents[str(scenario["agent_id"])]

        for info in scenario.get("information_before_decision", []):
            agent = receive_information(
                agent,
                claim_ref=str(info["claim_ref"]),
                provenance_ref=str(info["provenance_ref"]),
            )

        context_raw = scenario.get("context", {})
        context = PlanningContext(
            semantic_minute=int(context_raw.get("semantic_minute", 0)),
            active_intent_id=(
                None if context_raw.get("active_intent_id") is None
                else str(context_raw["active_intent_id"])
            ),
            continuity_bonus=int(context_raw.get("continuity_bonus", 1)),
        )
        decisions[scenario_id] = choose_agenda_intent(
            agent,
            goals=[goal_from_dict(raw) for raw in scenario.get("goals", [])],
            needs=[need_from_dict(raw) for raw in scenario.get("needs", [])],
            commitments=[
                commitment_from_dict(raw) for raw in scenario.get("commitments", [])
            ],
            situational_intents=[
                intent_from_dict(raw) for raw in scenario.get("situational_intents", [])
            ],
            context=context,
        )

    return decisions


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Replay global Ouros NPC world-agent AI fixture")
    parser.add_argument("fixture")
    args = parser.parse_args()

    with open(args.fixture, "r", encoding="utf-8") as handle:
        payload = json.load(handle)

    if payload.get("fixture_type") == "GOAL_NEED_SCHEDULE":
        agenda_results = run_agenda_fixture(payload)
        rendered = {
            key: {
                "intent_id": value.decision.intent_id,
                "kind": value.decision.kind,
                "score": value.decision.score,
                "handoff": value.decision.handoff.value,
                "reason_codes": list(value.decision.reason_codes),
                "target_ref": value.decision.target_ref,
                "source_type": value.source_type,
                "source_ref": value.source_ref,
                "schedule_state": value.schedule_state,
            }
            for key, value in agenda_results.items()
        }
    else:
        results = run_fixture(payload)
        rendered = {
            key: {
                "intent_id": value.intent_id,
                "kind": value.kind,
                "score": value.score,
                "handoff": value.handoff.value,
                "reason_codes": list(value.reason_codes),
                "target_ref": value.target_ref,
            }
            for key, value in results.items()
        }

    print(json.dumps(rendered, indent=2, sort_keys=True))
