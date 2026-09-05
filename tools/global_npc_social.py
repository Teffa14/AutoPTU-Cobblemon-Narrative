from __future__ import annotations

from dataclasses import dataclass, replace
import json
from pathlib import Path
from typing import FrozenSet, Iterable, Mapping

from tools.global_npc_ai import (
    AgendaDecision,
    DurableGoal,
    NeedState,
    NpcAgentState,
    NpcIntent,
    PlanningContext,
    ScheduledCommitment,
    agent_from_dict,
    choose_agenda_intent,
)


RELATIONSHIP_MIN = -100
RELATIONSHIP_MAX = 100


@dataclass(frozen=True)
class RelationshipState:
    source_agent_id: str
    target_agent_id: str
    affinity: int = 0
    trust: int = 0
    respect: int = 0
    fear: int = 0
    rivalry: int = 0
    debt: int = 0
    last_update_semantic_minute: int = 0
    provenance_refs: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.source_agent_id == self.target_agent_id:
            raise ValueError("relationship must target another agent")
        for name in ("affinity", "trust", "respect", "fear", "rivalry", "debt"):
            value = getattr(self, name)
            if value < RELATIONSHIP_MIN or value > RELATIONSHIP_MAX:
                raise ValueError(f"{name} outside relationship bounds")


@dataclass(frozen=True)
class FactionMembership:
    agent_id: str
    faction_id: str
    role_id: str
    commitment: int = 0
    standing: int = 0
    active: bool = True
    obligation_tags: FrozenSet[str] = frozenset()
    permission_tags: FrozenSet[str] = frozenset()


@dataclass(frozen=True)
class SocialIntentSpec:
    intent_id: str
    kind: str
    base_priority: int = 0
    urgency: int = 0
    risk: int = 0
    travel_cost: int = 0
    target_agent_id: str | None = None
    faction_id: str | None = None
    relationship_motive: str = "NEUTRAL"
    required_faction_obligation: str | None = None
    required_knowledge: FrozenSet[str] = frozenset()
    required_permissions: FrozenSet[str] = frozenset()
    requires_local_projection: bool = False
    requires_structured_mechanics: bool = False


def _clamp_relationship(value: int) -> int:
    return max(RELATIONSHIP_MIN, min(RELATIONSHIP_MAX, value))


def apply_relationship_event(
    relationship: RelationshipState,
    *,
    provenance_ref: str,
    semantic_minute: int,
    affinity_delta: int = 0,
    trust_delta: int = 0,
    respect_delta: int = 0,
    fear_delta: int = 0,
    rivalry_delta: int = 0,
    debt_delta: int = 0,
) -> RelationshipState:
    """Apply one provenance-backed directional social update."""
    if not provenance_ref:
        raise ValueError("relationship mutation requires provenance")
    provenance = relationship.provenance_refs
    if provenance_ref not in provenance:
        provenance = provenance + (provenance_ref,)
    return replace(
        relationship,
        affinity=_clamp_relationship(relationship.affinity + affinity_delta),
        trust=_clamp_relationship(relationship.trust + trust_delta),
        respect=_clamp_relationship(relationship.respect + respect_delta),
        fear=_clamp_relationship(relationship.fear + fear_delta),
        rivalry=_clamp_relationship(relationship.rivalry + rivalry_delta),
        debt=_clamp_relationship(relationship.debt + debt_delta),
        last_update_semantic_minute=semantic_minute,
        provenance_refs=provenance,
    )


def relationship_weight(relationship: RelationshipState | None, motive: str) -> int:
    """Return a bounded world-intent modifier, never tactical policy."""
    if relationship is None:
        return 0
    motive = motive.upper()
    if motive == "ASSIST":
        raw = relationship.affinity // 12 + relationship.trust // 15 + relationship.debt // 12
    elif motive == "SOCIALIZE":
        raw = relationship.affinity // 10 + relationship.trust // 20
    elif motive == "RELY_ON":
        raw = relationship.trust // 8 + relationship.respect // 20
    elif motive == "RIVALRY":
        raw = relationship.rivalry // 9 + relationship.respect // 20
    elif motive == "AVOID":
        raw = relationship.fear // 9 - relationship.affinity // 20
    elif motive == "CONFRONT":
        raw = relationship.rivalry // 12 + max(0, -relationship.affinity) // 15
    else:
        raw = 0
    return max(-10, min(10, raw))


def _membership_for(
    agent_id: str,
    faction_id: str | None,
    memberships: Iterable[FactionMembership],
) -> FactionMembership | None:
    if faction_id is None:
        return None
    matches = [m for m in memberships if m.agent_id == agent_id and m.faction_id == faction_id and m.active]
    if not matches:
        return None
    matches.sort(key=lambda m: (m.faction_id, m.role_id))
    return matches[0]


def agent_with_faction_permissions(
    agent: NpcAgentState,
    memberships: Iterable[FactionMembership],
) -> NpcAgentState:
    permissions = set(agent.permissions)
    for membership in memberships:
        if membership.agent_id == agent.agent_id and membership.active:
            permissions.update(membership.permission_tags)
    return replace(agent, permissions=frozenset(permissions))


def social_intent_to_world_intent(
    agent: NpcAgentState,
    spec: SocialIntentSpec,
    *,
    relationships: Iterable[RelationshipState] = (),
    memberships: Iterable[FactionMembership] = (),
) -> NpcIntent | None:
    relation = None
    if spec.target_agent_id is not None:
        relation = next(
            (
                item
                for item in relationships
                if item.source_agent_id == agent.agent_id
                and item.target_agent_id == spec.target_agent_id
            ),
            None,
        )

    membership = _membership_for(agent.agent_id, spec.faction_id, memberships)
    obligation = 0
    if spec.required_faction_obligation is not None:
        if membership is None or spec.required_faction_obligation not in membership.obligation_tags:
            return None
        obligation = max(0, min(10, membership.commitment // 10))

    return NpcIntent(
        intent_id=spec.intent_id,
        kind=spec.kind,
        base_priority=spec.base_priority,
        urgency=spec.urgency,
        obligation=obligation,
        risk=spec.risk,
        travel_cost=spec.travel_cost,
        relationship_weight=relationship_weight(relation, spec.relationship_motive),
        required_knowledge=spec.required_knowledge,
        required_permissions=spec.required_permissions,
        target_ref=spec.target_agent_id,
        requires_local_projection=spec.requires_local_projection,
        requires_structured_mechanics=spec.requires_structured_mechanics,
    )


def choose_social_agenda_intent(
    agent: NpcAgentState,
    *,
    relationships: Iterable[RelationshipState] = (),
    memberships: Iterable[FactionMembership] = (),
    social_intents: Iterable[SocialIntentSpec] = (),
    goals: Iterable[DurableGoal] = (),
    needs: Iterable[NeedState] = (),
    commitments: Iterable[ScheduledCommitment] = (),
    ordinary_situational_intents: Iterable[NpcIntent] = (),
    context: PlanningContext,
) -> AgendaDecision:
    membership_list = tuple(memberships)
    relationship_list = tuple(relationships)
    effective_agent = agent_with_faction_permissions(agent, membership_list)
    social_candidates: list[NpcIntent] = []
    for spec in social_intents:
        candidate = social_intent_to_world_intent(
            effective_agent,
            spec,
            relationships=relationship_list,
            memberships=membership_list,
        )
        if candidate is not None:
            social_candidates.append(candidate)
    return choose_agenda_intent(
        effective_agent,
        goals=goals,
        needs=needs,
        commitments=commitments,
        situational_intents=tuple(ordinary_situational_intents) + tuple(social_candidates),
        context=context,
    )


def relationship_from_dict(data: Mapping[str, object]) -> RelationshipState:
    return RelationshipState(
        source_agent_id=str(data["source_agent_id"]),
        target_agent_id=str(data["target_agent_id"]),
        affinity=int(data.get("affinity", 0)),
        trust=int(data.get("trust", 0)),
        respect=int(data.get("respect", 0)),
        fear=int(data.get("fear", 0)),
        rivalry=int(data.get("rivalry", 0)),
        debt=int(data.get("debt", 0)),
        last_update_semantic_minute=int(data.get("last_update_semantic_minute", 0)),
        provenance_refs=tuple(str(v) for v in data.get("provenance_refs", [])),
    )


def membership_from_dict(data: Mapping[str, object]) -> FactionMembership:
    return FactionMembership(
        agent_id=str(data["agent_id"]),
        faction_id=str(data["faction_id"]),
        role_id=str(data["role_id"]),
        commitment=int(data.get("commitment", 0)),
        standing=int(data.get("standing", 0)),
        active=bool(data.get("active", True)),
        obligation_tags=frozenset(str(v) for v in data.get("obligation_tags", [])),
        permission_tags=frozenset(str(v) for v in data.get("permission_tags", [])),
    )


def social_spec_from_dict(data: Mapping[str, object]) -> SocialIntentSpec:
    return SocialIntentSpec(
        intent_id=str(data["intent_id"]),
        kind=str(data["kind"]),
        base_priority=int(data.get("base_priority", 0)),
        urgency=int(data.get("urgency", 0)),
        risk=int(data.get("risk", 0)),
        travel_cost=int(data.get("travel_cost", 0)),
        target_agent_id=None if data.get("target_agent_id") is None else str(data["target_agent_id"]),
        faction_id=None if data.get("faction_id") is None else str(data["faction_id"]),
        relationship_motive=str(data.get("relationship_motive", "NEUTRAL")),
        required_faction_obligation=(
            None
            if data.get("required_faction_obligation") is None
            else str(data["required_faction_obligation"])
        ),
        required_knowledge=frozenset(str(v) for v in data.get("required_knowledge", [])),
        required_permissions=frozenset(str(v) for v in data.get("required_permissions", [])),
        requires_local_projection=bool(data.get("requires_local_projection", False)),
        requires_structured_mechanics=bool(data.get("requires_structured_mechanics", False)),
    )


def run_social_fixture(payload: Mapping[str, object]) -> dict[str, AgendaDecision]:
    agents = {
        str(row["agent_id"]): agent_from_dict(row)
        for row in payload.get("agents", [])
    }
    relationships = tuple(relationship_from_dict(row) for row in payload.get("relationships", []))
    memberships = tuple(membership_from_dict(row) for row in payload.get("memberships", []))
    output: dict[str, AgendaDecision] = {}
    for scenario in payload.get("scenarios", []):
        agent = agents[str(scenario["agent_id"])]
        social = tuple(social_spec_from_dict(row) for row in scenario.get("social_intents", []))
        ordinary = tuple(
            NpcIntent(
                intent_id=str(row["intent_id"]),
                kind=str(row["kind"]),
                base_priority=int(row.get("base_priority", 0)),
                urgency=int(row.get("urgency", 0)),
                required_knowledge=frozenset(str(v) for v in row.get("required_knowledge", [])),
            )
            for row in scenario.get("ordinary_intents", [])
        )
        needs = tuple(
            NeedState(
                need_id=str(row["need_id"]),
                intent_kind=str(row["intent_kind"]),
                pressure=int(row["pressure"]),
                activation_threshold=int(row["activation_threshold"]),
                critical_threshold=int(row.get("critical_threshold", 90)),
            )
            for row in scenario.get("needs", [])
        )
        output[str(scenario["scenario_id"])] = choose_social_agenda_intent(
            agent,
            relationships=relationships,
            memberships=memberships,
            social_intents=social,
            needs=needs,
            ordinary_situational_intents=ordinary,
            context=PlanningContext(int(scenario.get("semantic_minute", 0))),
        )
    return output


def main(path: str) -> int:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    decisions = run_social_fixture(payload)
    print(
        json.dumps(
            {
                key: {
                    "kind": value.decision.kind,
                    "intent_id": value.decision.intent_id,
                    "handoff": value.decision.handoff.value,
                }
                for key, value in decisions.items()
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv[1]))
