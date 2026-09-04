#!/usr/bin/env python3
"""Replay Pass 246 shared-resource ecology trace.

This reducer validates scoped ecological writes across multiple population/resource
ledgers. It does not execute PTU mechanics or promote proposed fixture content to canon.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any


class ReplayError(Exception):
    pass


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


def initial_state(trace: dict[str, Any]) -> dict[str, Any]:
    state = copy.deepcopy(trace["starting_state"])
    state["resource_transactions"] = []
    state["observations"] = []
    state["restart_count"] = 0
    return state


def population(state: dict[str, Any], population_id: str) -> dict[str, Any]:
    require(population_id in state["populations"], f"unknown population: {population_id}")
    return state["populations"][population_id]


def actor(state: dict[str, Any], actor_ref: str) -> dict[str, Any]:
    require(actor_ref in state["actors"], f"unknown actor: {actor_ref}")
    return state["actors"][actor_ref]


def resource(state: dict[str, Any], resource_id: str) -> dict[str, Any]:
    require(resource_id in state["resources"], f"unknown resource: {resource_id}")
    return state["resources"][resource_id]


def apply_event(state: dict[str, Any], event: dict[str, Any]) -> None:
    kind = event.get("event_type")

    if kind == "RESOURCE_USE_OBSERVED":
        resource(state, str(event["resource_id"]))
        population(state, str(event["population_id"]))
        require(event.get("consumption_confirmed") is False,
                "observation cannot masquerade as confirmed consumption")
        state["observations"].append({
            "resource_id": event["resource_id"],
            "population_id": event["population_id"],
            "observed_units": int(event["observed_units"]),
        })
        return

    if kind == "RESOURCE_CONSUMPTION_CONFIRMED":
        tx_id = str(event["transaction_id"])
        require(tx_id not in state["resource_transactions"], f"duplicate resource transaction: {tx_id}")
        consumer_id = str(event["consumer_population_id"])
        population(state, consumer_id)
        node = resource(state, str(event["resource_id"]))
        units = int(event["units"])
        require(units > 0, "resource consumption must be positive")
        require(node["available_units"] >= units, "resource transaction exceeds available units")
        node["available_units"] -= units
        node["depleted"] = node["available_units"] == 0
        state["resource_transactions"].append(tx_id)
        return

    if kind == "ACTOR_PRESSURE_DELTA":
        target = actor(state, str(event["actor_ref"]))
        target["avoidance_pressure"] = round(
            float(target["avoidance_pressure"]) + float(event.get("avoidance_pressure_delta", 0.0)), 6
        )
        return

    if kind == "POPULATION_RESOURCE_PRESSURE_DELTA":
        target = population(state, str(event["population_id"]))
        target["resource_pressure"] = round(
            float(target["resource_pressure"]) + float(event.get("resource_pressure_delta", 0.0)), 6
        )
        return

    if kind == "ENCOUNTER_HISTORY_APPEND":
        target = actor(state, str(event["actor_ref"]))
        target["encounter_history_count"] = int(target["encounter_history_count"]) + 1
        return

    if kind == "SERVER_RESTART":
        state["restart_count"] += 1
        return

    raise ReplayError(f"unsupported event type: {kind!r}")


def replay(trace: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    state = initial_state(trace)
    baseline_totals = {key: int(value["total"]) for key, value in state["populations"].items()}
    snapshots: list[dict[str, Any]] = []

    for window in trace.get("windows", []):
        for event in window.get("input_events", []):
            apply_event(state, event)

        for population_id, total in baseline_totals.items():
            require(int(state["populations"][population_id]["total"]) == total,
                    f"resource-only trace illegally changed population total: {population_id}")
        snapshot = copy.deepcopy(state)
        snapshot["window_id"] = window.get("id")
        snapshots.append(snapshot)

    return state, snapshots


def canonical_snapshot(state: dict[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(state)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--emit-snapshots", action="store_true")
    args = parser.parse_args(argv)
    path = args.root / "implementation" / "marea-sendero-shared-resource-multi-species-trace-v1.json"
    try:
        trace = load_trace(path)
        state, snapshots = replay(trace)
    except ReplayError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1

    payload = snapshots if args.emit_snapshots else canonical_snapshot(state)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
