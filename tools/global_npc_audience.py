from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from tools.global_npc_social import FactionMembership, RelationshipState


@dataclass(frozen=True)
class AudienceCandidate:
    agent_id: str
    reachable_channel_ids: tuple[str, ...] = ()
    proximity_band: int = 0
    topic_relevance: int = 0
    explicit_role_relevance: int = 0
    available: bool = True


@dataclass(frozen=True)
class AudiencePolicy:
    max_recipients: int = 3
    min_score: int = 1
    require_reachable_channel: bool = True
    faction_broadcast_allowed: bool = False

    def __post_init__(self) -> None:
        if self.max_recipients < 0:
            raise ValueError("max_recipients must be non-negative")


@dataclass(frozen=True)
class AudienceSelection:
    selected_agent_ids: tuple[str, ...]
    scores: tuple[tuple[str, int], ...]
    rejected: tuple[tuple[str, str], ...]


def _relationship_for(
    sender_id: str,
    receiver_id: str,
    relationships: Iterable[RelationshipState],
) -> RelationshipState | None:
    return next(
        (
            item
            for item in relationships
            if item.source_agent_id == sender_id and item.target_agent_id == receiver_id
        ),
        None,
    )


def _memberships_for(agent_id: str, memberships: Iterable[FactionMembership]) -> tuple[FactionMembership, ...]:
    return tuple(
        item
        for item in memberships
        if item.agent_id == agent_id and item.active
    )


def _shared_factions(
    sender_id: str,
    receiver_id: str,
    memberships: Iterable[FactionMembership],
) -> tuple[str, ...]:
    sender = {item.faction_id for item in _memberships_for(sender_id, memberships)}
    receiver = {item.faction_id for item in _memberships_for(receiver_id, memberships)}
    return tuple(sorted(sender & receiver))


def _institutional_duty_score(
    sender_id: str,
    receiver_id: str,
    memberships: Iterable[FactionMembership],
    required_obligation_tag: str | None,
) -> int:
    if required_obligation_tag is None:
        return 0
    shared = set(_shared_factions(sender_id, receiver_id, memberships))
    if not shared:
        return 0
    score = 0
    for membership in _memberships_for(receiver_id, memberships):
        if membership.faction_id in shared and required_obligation_tag in membership.obligation_tags:
            score = max(score, 8 + max(0, min(4, membership.commitment // 25)))
    return score


def score_recipient(
    *,
    sender_id: str,
    candidate: AudienceCandidate,
    relationships: Iterable[RelationshipState] = (),
    memberships: Iterable[FactionMembership] = (),
    required_obligation_tag: str | None = None,
) -> int:
    relation = _relationship_for(sender_id, candidate.agent_id, relationships)
    social = 0
    if relation is not None:
        social += relation.trust // 12
        social += relation.affinity // 20
        social += relation.respect // 25
        social -= relation.fear // 25
    institutional = _institutional_duty_score(
        sender_id,
        candidate.agent_id,
        memberships,
        required_obligation_tag,
    )
    proximity = max(-4, min(4, candidate.proximity_band))
    relevance = max(-10, min(10, candidate.topic_relevance))
    role = max(-10, min(10, candidate.explicit_role_relevance))
    return social + institutional + proximity + relevance + role


def resolve_audience(
    *,
    sender_id: str,
    candidates: Iterable[AudienceCandidate],
    relationships: Iterable[RelationshipState] = (),
    memberships: Iterable[FactionMembership] = (),
    required_obligation_tag: str | None = None,
    policy: AudiencePolicy = AudiencePolicy(),
) -> AudienceSelection:
    relationship_list = tuple(relationships)
    membership_list = tuple(memberships)
    rejected: list[tuple[str, str]] = []
    scored: list[tuple[str, int]] = []

    for candidate in candidates:
        if candidate.agent_id == sender_id:
            rejected.append((candidate.agent_id, "SELF"))
            continue
        if not candidate.available:
            rejected.append((candidate.agent_id, "UNAVAILABLE"))
            continue
        if policy.require_reachable_channel and not candidate.reachable_channel_ids:
            rejected.append((candidate.agent_id, "NO_REACHABLE_CHANNEL"))
            continue

        shared = _shared_factions(sender_id, candidate.agent_id, membership_list)
        if shared and not policy.faction_broadcast_allowed and required_obligation_tag is None:
            # Shared membership alone is deliberately worth zero. It does not reject the candidate;
            # other relationship/relevance factors may still justify contact.
            pass

        score = score_recipient(
            sender_id=sender_id,
            candidate=candidate,
            relationships=relationship_list,
            memberships=membership_list,
            required_obligation_tag=required_obligation_tag,
        )
        if score < policy.min_score:
            rejected.append((candidate.agent_id, "BELOW_THRESHOLD"))
            continue
        scored.append((candidate.agent_id, score))

    scored.sort(key=lambda item: (-item[1], item[0]))
    selected = tuple(agent_id for agent_id, _ in scored[: policy.max_recipients])
    overflow = scored[policy.max_recipients :]
    rejected.extend((agent_id, "AUDIENCE_BUDGET") for agent_id, _ in overflow)
    rejected.sort(key=lambda item: (item[0], item[1]))
    return AudienceSelection(
        selected_agent_ids=selected,
        scores=tuple(scored),
        rejected=tuple(rejected),
    )


def candidate_from_dict(data: Mapping[str, object]) -> AudienceCandidate:
    return AudienceCandidate(
        agent_id=str(data["agent_id"]),
        reachable_channel_ids=tuple(str(v) for v in data.get("reachable_channel_ids", [])),
        proximity_band=int(data.get("proximity_band", 0)),
        topic_relevance=int(data.get("topic_relevance", 0)),
        explicit_role_relevance=int(data.get("explicit_role_relevance", 0)),
        available=bool(data.get("available", True)),
    )


def _relationship_from_dict(data: Mapping[str, object]) -> RelationshipState:
    return RelationshipState(
        source_agent_id=str(data["source_agent_id"]),
        target_agent_id=str(data["target_agent_id"]),
        affinity=int(data.get("affinity", 0)),
        trust=int(data.get("trust", 0)),
        respect=int(data.get("respect", 0)),
        fear=int(data.get("fear", 0)),
        rivalry=int(data.get("rivalry", 0)),
        debt=int(data.get("debt", 0)),
    )


def _membership_from_dict(data: Mapping[str, object]) -> FactionMembership:
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


def replay_fixture(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    relationships = tuple(_relationship_from_dict(v) for v in data.get("relationships", []))
    memberships = tuple(_membership_from_dict(v) for v in data.get("memberships", []))
    results: list[dict] = []
    for scenario in data["scenarios"]:
        policy_data = scenario.get("policy", {})
        selection = resolve_audience(
            sender_id=str(scenario["sender_id"]),
            candidates=tuple(candidate_from_dict(v) for v in scenario.get("candidates", [])),
            relationships=relationships,
            memberships=memberships,
            required_obligation_tag=(
                None if scenario.get("required_obligation_tag") is None
                else str(scenario["required_obligation_tag"])
            ),
            policy=AudiencePolicy(
                max_recipients=int(policy_data.get("max_recipients", 3)),
                min_score=int(policy_data.get("min_score", 1)),
                require_reachable_channel=bool(policy_data.get("require_reachable_channel", True)),
                faction_broadcast_allowed=bool(policy_data.get("faction_broadcast_allowed", False)),
            ),
        )
        results.append({
            "scenario_id": scenario["scenario_id"],
            "selected_agent_ids": list(selection.selected_agent_ids),
            "scores": [[agent_id, score] for agent_id, score in selection.scores],
            "rejected": [[agent_id, reason] for agent_id, reason in selection.rejected],
        })
    return {"fixture_id": data["fixture_id"], "results": results}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m tools.global_npc_audience <fixture.json>", file=sys.stderr)
        return 2
    print(json.dumps(replay_fixture(argv[1]), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
