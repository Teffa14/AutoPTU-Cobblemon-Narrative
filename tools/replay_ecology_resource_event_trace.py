#!/usr/bin/env python3
"""Replay Pass 247 scarcity -> observation -> world-event integration trace."""
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
    state["observations"] = {}
    state["relays"] = []
    state["restart_count"] = 0
    return state


def apply_event(state: dict[str, Any], trace: dict[str, Any], event: dict[str, Any]) -> None:
    kind = event.get("event_type")

    if kind in {"RESOURCE_CONSUMPTION_CONFIRMED", "RESOURCE_RENEWAL_CONFIRMED"}:
        tx_id = str(event["transaction_id"])
        require(tx_id not in state["resource_transactions"], f"duplicate resource transaction: {tx_id}")
        node = state["resources"][str(event["resource_id"])]
        units = int(event["units"])
        require(units > 0, "resource transaction units must be positive")
        if kind == "RESOURCE_CONSUMPTION_CONFIRMED":
            require(str(event["consumer_population_id"]) in state["populations"], "unknown consumer population")
            require(node["available_units"] >= units, "resource transaction exceeds available units")
            node["available_units"] -= units
        else:
            node["available_units"] += units
        node["depleted"] = node["available_units"] == 0
        state["resource_transactions"].append(tx_id)
        return

    if kind == "POPULATION_RESOURCE_PRESSURE_DELTA":
        population = state["populations"][str(event["population_id"])]
        population["resource_pressure"] = round(
            float(population["resource_pressure"]) + float(event["resource_pressure_delta"]), 6
        )
        return

    if kind == "ECOLOGY_EVENT_EVALUATE":
        rule = trace["event_rule"]
        require(str(event["event_id"]) == rule["event_id"], "event evaluation rule mismatch")
        instance = state["events"][rule["event_id"]]
        resource = state["resources"][rule["resource_id"]]
        population = state["populations"][rule["population_id"]]
        open_rule = rule["open_when"]
        clear_rule = rule["clear_when"]
        opens = (
            resource["available_units"] <= int(open_rule["available_units_lte"])
            and float(population["resource_pressure"]) >= float(open_rule["resource_pressure_gte"])
        )
        clears = (
            resource["available_units"] >= int(clear_rule["available_units_gte"])
            and float(population["resource_pressure"]) <= float(clear_rule["resource_pressure_lte"])
        )
        if instance["phase"] == "INACTIVE" and opens:
            instance["phase"] = "ACTIVE"
            instance["open_count"] += 1
            instance["clear_streak"] = 0
        elif instance["phase"] in {"ACTIVE", "STABILIZING"}:
            if clears:
                instance["clear_streak"] += 1
                if instance["clear_streak"] >= int(clear_rule["consecutive_evaluations"]):
                    instance["phase"] = "RESOLVED"
                else:
                    instance["phase"] = "STABILIZING"
            else:
                instance["clear_streak"] = 0
                instance["phase"] = "ACTIVE"
        return

    if kind == "OBSERVATION_CAPTURED":
        require(event.get("exposes_hidden_resource_units") is False, "observation leaked hidden resource quantity")
        observation_id = str(event["observation_id"])
        require(observation_id not in state["observations"], "duplicate observation")
        state["observations"][observation_id] = {
            "holder_id": event["holder_id"],
            "claimable_symptom": event["claimable_symptom"],
            "visible_count": int(event["visible_count"]),
        }
        return

    if kind == "CLAIM_UPSERT":
        holder = state["knowledge_holders"][str(event["holder_id"])]
        for evidence_ref in event["evidence_refs"]:
            require(evidence_ref in state["observations"], f"unknown evidence: {evidence_ref}")
        holder["claims"][str(event["claim_id"])] = {
            "claim_type": event["claim_type"],
            "state": event["state"],
            "confidence_band": event["confidence_band"],
            "evidence_refs": list(event["evidence_refs"]),
            "source_roots": [event["source_root"]],
            "relay_count": 0,
        }
        return

    if kind == "CLAIM_RELAY":
        holder = state["knowledge_holders"][str(event["holder_id"])]
        claim = holder["claims"][str(event["claim_id"])]
        require(str(event["source_root"]) in claim["source_roots"], "relay source root is not in claim provenance")
        relay_id = str(event["relay_id"])
        require(relay_id not in state["relays"], "duplicate relay")
        state["relays"].append(relay_id)
        claim["relay_count"] += 1
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
            apply_event(state, trace, event)
        for population_id, total in baseline_totals.items():
            require(int(state["populations"][population_id]["total"]) == total,
                    f"non-demographic trace changed population total: {population_id}")
        snapshot = copy.deepcopy(state)
        snapshot["window_id"] = window.get("id")
        snapshots.append(snapshot)
    return state, snapshots


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--emit-snapshots", action="store_true")
    args = parser.parse_args(argv)
    path = args.root / "implementation" / "marea-sendero-resource-scarcity-world-event-trace-v1.json"
    try:
        trace = load_trace(path)
        state, snapshots = replay(trace)
    except (ReplayError, KeyError, TypeError, ValueError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    print(json.dumps(snapshots if args.emit_snapshots else state, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
