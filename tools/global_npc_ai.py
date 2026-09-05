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

    # Highest score wins. intent_id is the stable replay-safe tie-break.
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


def receive_information(
    agent: NpcAgentState,
    *,
    claim_ref: str,
    provenance_ref: str,
) -> NpcAgentState:
    """Add one observed/communicated claim to this NPC's private knowledge.

    Hidden world/ecology truth is never imported automatically. The caller must
    provide an observation, communication or accessible institutional record.
    """
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


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Replay global Ouros NPC world-agent AI fixture")
    parser.add_argument("fixture")
    args = parser.parse_args()

    with open(args.fixture, "r", encoding="utf-8") as handle:
        payload = json.load(handle)

    results = run_fixture(payload)
    print(json.dumps(
        {
            key: {
                "intent_id": value.intent_id,
                "kind": value.kind,
                "score": value.score,
                "handoff": value.handoff.value,
                "reason_codes": list(value.reason_codes),
                "target_ref": value.target_ref,
            }
            for key, value in results.items()
        },
        indent=2,
        sort_keys=True,
    ))
