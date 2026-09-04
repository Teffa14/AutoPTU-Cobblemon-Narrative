#!/usr/bin/env python3
"""Replay the Pass 244 cross-fixture trace into a deterministic Ouros ecology snapshot.

This reducer owns only narrative/ecology state. It never simulates PTU rules. AutoPTU
results enter as semantic events and Minecraft UUIDs remain presentation correlation.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


class ReplayError(Exception):
    pass


@dataclass
class EcologyReplayState:
    persistent_actor_ref: str
    population_id: str
    population_total: int
    known_member_exists: bool
    active_projection_lease: str | None
    projection_lease_state: str | None
    minecraft_entity_uuid: str | None
    active_battle_id: str | None
    battle_open: bool
    encounter_history_count: int
    avoidance_pressure: float
    ecological_mortality_events: int
    emigration_events: int
    source_event_state: str
    last_semantic_result: str | None
    restart_count: int


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ReplayError(message)


def load_trace(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReplayError(f"cannot load {path}: {exc}") from exc
    require(isinstance(data, dict), "trace root must be an object")
    return data


def initial_state(trace: dict[str, Any]) -> EcologyReplayState:
    start = trace["starting_state"]
    return EcologyReplayState(
        persistent_actor_ref=str(trace["persistent_actor_ref"]),
        population_id=str(trace["population_id"]),
        population_total=int(start["population_total"]),
        known_member_exists=bool(start["known_member_exists"]),
        active_projection_lease=start.get("active_projection_lease"),
        projection_lease_state=None,
        minecraft_entity_uuid=start.get("minecraft_entity_uuid"),
        active_battle_id=start.get("battle_id"),
        battle_open=False,
        encounter_history_count=int(start["encounter_history_count"]),
        avoidance_pressure=float(start["avoidance_pressure"]),
        ecological_mortality_events=int(start["ecological_mortality_events"]),
        emigration_events=int(start["emigration_events"]),
        source_event_state=str(start["source_event_state"]),
        last_semantic_result=None,
        restart_count=0,
    )


def apply_event(state: EcologyReplayState, event: dict[str, Any], frozen_manifests: set[str]) -> None:
    kind = event.get("event_type")
    actor = state.persistent_actor_ref
    event_actor = event.get("member_id") or event.get("actor_ref")
    if event_actor and not str(event_actor).startswith("FIXTURE_PLAYER"):
        require(event_actor == actor, f"actor identity drift: {event_actor}")

    if kind == "LEASE_RESERVE":
        require(state.active_projection_lease is None, "cannot reserve a second active lease")
        state.active_projection_lease = str(event["lease_id"])
        state.projection_lease_state = "RESERVED"
    elif kind in {"LEASE_MATERIALIZE", "LEASE_REMATERIALIZE"}:
        require(state.active_projection_lease == event.get("lease_id"), "materialization uses wrong lease")
        state.minecraft_entity_uuid = str(event["minecraft_entity_uuid"])
        state.projection_lease_state = "MATERIALIZED"
    elif kind == "OBSERVATION_RECORDED":
        require(event.get("internal_id_exposed_to_player") is False, "observation leaked internal actor id")
    elif kind == "ECOLOGY_EVENT_EVALUATION":
        state.source_event_state = str(event["result_state"])
    elif kind == "OVERWORLD_INTERACTION":
        require(event.get("decision") == "STAY_OVERWORLD", "unsupported overworld decision in reduced trace")
    elif kind == "BATTLE_MANIFEST_FREEZE":
        battle_id = str(event["battle_id"])
        participants = event.get("participants", [])
        require(sum(1 for p in participants if p.get("persistent_actor_ref") == actor) == 1,
                "manifest must contain persistent actor exactly once")
        frozen_manifests.add(battle_id)
    elif kind == "STRUCTURED_BATTLE_HANDOFF":
        battle_id = str(event["battle_id"])
        require(battle_id in frozen_manifests, "battle handoff before manifest freeze")
        require(not state.battle_open, "nested battle handoff")
        require(state.active_projection_lease == event.get("lease_id"), "handoff uses wrong projection lease")
        state.active_battle_id = battle_id
        state.battle_open = True
        state.projection_lease_state = "ENGAGED"
    elif kind == "AUTOPTU_SEMANTIC_RESULT":
        require(state.battle_open, "semantic result without active battle")
        require(event.get("battle_id") == state.active_battle_id, "semantic result battle mismatch")
        require(event.get("actor_ref") == actor, "semantic result actor mismatch")
        require(event.get("capture_confirmed") is False, "reduced trace cannot capture actor")
        require(event.get("removal_confirmed") is False, "reduced trace cannot remove actor")
        results = event.get("objective_results", [])
        state.last_semantic_result = str(results[0]) if results else None
        state.active_battle_id = None
        state.battle_open = False
    elif kind == "ENCOUNTER_HISTORY_APPEND":
        require(event.get("actor_ref") == actor, "history append actor mismatch")
        state.encounter_history_count += 1
    elif kind == "ECOLOGY_PRESSURE_DELTA":
        require(event.get("actor_ref") == actor, "pressure delta actor mismatch")
        state.avoidance_pressure += float(event.get("avoidance_pressure_delta", 0.0))
    elif kind == "LEASE_SUSPEND":
        require(state.active_projection_lease == event.get("lease_id"), "suspend uses wrong lease")
        state.projection_lease_state = "SUSPENDED"
        state.minecraft_entity_uuid = None
    elif kind == "ECOLOGY_EVENT_REEVALUATION":
        require(event.get("battle_result_is_direct_resolution") is False,
                "battle result cannot directly resolve ecology event")
        state.source_event_state = str(event["result_state"])
    elif kind == "SERVER_RESTART":
        state.restart_count += 1
        state.minecraft_entity_uuid = None
        if state.projection_lease_state == "MATERIALIZED":
            state.projection_lease_state = "SUSPENDED"
    elif kind == "LEASE_INDEX_RECONCILE":
        require(state.known_member_exists, "cannot reconcile lease index for missing persistent member")
    else:
        raise ReplayError(f"unsupported event type: {kind!r}")


def replay(trace: dict[str, Any]) -> tuple[EcologyReplayState, list[dict[str, Any]]]:
    state = initial_state(trace)
    frozen_manifests: set[str] = set()
    snapshots: list[dict[str, Any]] = []
    for window in trace.get("windows", []):
        for event in window.get("input_events", []):
            apply_event(state, event, frozen_manifests)
        snapshot = asdict(state)
        snapshot["window_id"] = window.get("id")
        snapshots.append(snapshot)

    require(not state.battle_open, "replay ended with battle open")
    require(state.known_member_exists, "persistent actor disappeared during replay")
    return state, snapshots


def canonical_snapshot(state: EcologyReplayState) -> dict[str, Any]:
    value = asdict(state)
    value["avoidance_pressure"] = round(float(value["avoidance_pressure"]), 6)
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--emit-snapshots", action="store_true")
    args = parser.parse_args(argv)
    path = args.root / "implementation" / "marea-sendero-persistent-actor-cross-fixture-trace-v1.json"
    try:
        trace = load_trace(path)
        state, snapshots = replay(trace)
    except ReplayError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1

    if args.emit_snapshots:
        print(json.dumps(snapshots, indent=2, sort_keys=True))
    else:
        print(json.dumps(canonical_snapshot(state), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
