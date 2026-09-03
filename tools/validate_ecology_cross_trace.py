#!/usr/bin/env python3
"""Validate Pass 244 persistent-actor continuity without simulating PTU rules."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


class ValidationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"{path}: cannot load JSON: {exc}") from exc
    require(isinstance(value, dict), f"{path}: top-level JSON must be an object")
    return value


def validate_source_anchors(root: Path, trace: dict[str, Any]) -> None:
    sources = trace.get("source_fixtures")
    require(isinstance(sources, list) and sources, "trace must declare source_fixtures")
    for source in sources:
        source_path = root / source["path"]
        require(source_path.is_file(), f"missing source fixture: {source_path}")
        data = load_json(source_path)
        window_ids = {window.get("id") for window in data.get("windows", [])}
        for required_window in source.get("required_windows", []):
            require(required_window in window_ids, f"{source_path}: missing anchor window {required_window}")


def validate_trace(path: Path, data: dict[str, Any], root: Path | None = None) -> None:
    require(data.get("pass") == 244, f"{path}: expected pass 244")
    actor = data.get("persistent_actor_ref")
    population_id = data.get("population_id")
    require(isinstance(actor, str) and actor, f"{path}: missing persistent_actor_ref")
    require(isinstance(population_id, str) and population_id, f"{path}: missing population_id")
    validate_source_anchors(root or path.resolve().parents[1], data)

    start = data["starting_state"]
    population_total = int(start["population_total"])
    known_member_exists = bool(start["known_member_exists"])
    active_lease: str | None = start.get("active_projection_lease")
    lease_state: str | None = None
    minecraft_uuid: str | None = start.get("minecraft_entity_uuid")
    first_materialized_uuid: str | None = None
    manifest_frozen_for: set[str] = set()
    battle_open = False
    active_battle_id: str | None = None
    encounter_history_count = int(start["encounter_history_count"])
    avoidance_pressure = float(start["avoidance_pressure"])
    ecological_mortality_events = int(start["ecological_mortality_events"])
    emigration_events = int(start["emigration_events"])
    source_event_state = str(start["source_event_state"])

    windows = data.get("windows", [])
    require(windows, f"{path}: trace has no windows")
    ids = [window.get("id") for window in windows]
    require(len(ids) == len(set(ids)), f"{path}: duplicate trace window ids")

    for window in windows:
        window_id = window["id"]
        for event in window.get("input_events", []):
            kind = event.get("event_type")
            event_actor = event.get("member_id") or event.get("actor_ref")
            if event_actor and not str(event_actor).startswith("FIXTURE_PLAYER"):
                require(event_actor == actor, f"{path}: {window_id} actor identity drift: {event_actor}")

            if kind == "LEASE_RESERVE":
                require(active_lease is None, f"{path}: {window_id} reserves while actor already leased")
                active_lease = event["lease_id"]
                lease_state = "RESERVED"
            elif kind in {"LEASE_MATERIALIZE", "LEASE_REMATERIALIZE"}:
                require(active_lease == event.get("lease_id"), f"{path}: {window_id} materializes wrong lease")
                new_uuid = event["minecraft_entity_uuid"]
                if kind == "LEASE_REMATERIALIZE":
                    require(first_materialized_uuid is not None, f"{path}: rematerialize before initial materialization")
                    require(new_uuid != first_materialized_uuid, f"{path}: rematerialization must demonstrate UUID correlation change")
                else:
                    first_materialized_uuid = new_uuid
                minecraft_uuid = new_uuid
                lease_state = "MATERIALIZED"
            elif kind == "OBSERVATION_RECORDED":
                require(event.get("internal_id_exposed_to_player") is False, f"{path}: {window_id} leaks persistent id")
            elif kind == "ECOLOGY_EVENT_EVALUATION":
                source_event_state = event["result_state"]
            elif kind == "OVERWORLD_INTERACTION":
                require(event.get("decision") == "STAY_OVERWORLD", f"{path}: {window_id} warning interaction incorrectly opens battle")
            elif kind == "BATTLE_MANIFEST_FREEZE":
                battle_id = event["battle_id"]
                participants = event.get("participants", [])
                actor_entries = [entry for entry in participants if entry.get("persistent_actor_ref") == actor]
                require(len(actor_entries) == 1, f"{path}: {window_id} manifest must contain actor exactly once")
                manifest_frozen_for.add(battle_id)
            elif kind == "STRUCTURED_BATTLE_HANDOFF":
                battle_id = event["battle_id"]
                require(battle_id in manifest_frozen_for, f"{path}: {window_id} handoff occurred before manifest freeze")
                require(active_lease == event.get("lease_id"), f"{path}: {window_id} handoff uses wrong lease")
                require(not battle_open, f"{path}: nested battle handoff")
                battle_open = True
                active_battle_id = battle_id
                lease_state = "ENGAGED"
            elif kind == "AUTOPTU_SEMANTIC_RESULT":
                require(battle_open, f"{path}: {window_id} semantic result without active battle")
                require(event.get("battle_id") == active_battle_id, f"{path}: {window_id} semantic result battle mismatch")
                require(event.get("actor_ref") == actor, f"{path}: {window_id} semantic result actor mismatch")
                require(event.get("capture_confirmed") is False, f"{path}: reduced trace must not capture actor")
                require(event.get("removal_confirmed") is False, f"{path}: reduced trace must not remove actor")
                battle_open = False
                active_battle_id = None
            elif kind == "ENCOUNTER_HISTORY_APPEND":
                encounter_history_count += 1
            elif kind == "ECOLOGY_PRESSURE_DELTA":
                avoidance_pressure += float(event.get("avoidance_pressure_delta", 0.0))
            elif kind == "LEASE_SUSPEND":
                require(active_lease == event.get("lease_id"), f"{path}: {window_id} suspends wrong lease")
                lease_state = "SUSPENDED"
                minecraft_uuid = None
            elif kind == "ECOLOGY_EVENT_REEVALUATION":
                require(event.get("battle_result_is_direct_resolution") is False, f"{path}: {window_id} battle directly resolves ecology event")
                source_event_state = event["result_state"]
            elif kind in {"SERVER_RESTART", "LEASE_INDEX_RECONCILE"}:
                pass
            else:
                raise ValidationError(f"{path}: {window_id} unsupported trace event {kind!r}")

        expected = window.get("expected", {})
        if "persistent_actor_ref" in expected:
            require(expected["persistent_actor_ref"] == actor, f"{path}: {window_id} expected actor drift")
        if "population_total" in expected:
            require(population_total == int(expected["population_total"]), f"{path}: {window_id} population changed without demographic event")
        if "known_member_exists" in expected:
            require(known_member_exists == bool(expected["known_member_exists"]), f"{path}: {window_id} member existence mismatch")
        if "active_projection_lease" in expected:
            require(active_lease == expected["active_projection_lease"], f"{path}: {window_id} active lease mismatch")
        if "active_projection_lease_state" in expected:
            require(lease_state == expected["active_projection_lease_state"], f"{path}: {window_id} lease state mismatch")
        if "minecraft_entity_uuid" in expected:
            require(minecraft_uuid == expected["minecraft_entity_uuid"], f"{path}: {window_id} UUID mismatch")
        if "battle_open" in expected:
            require(battle_open == bool(expected["battle_open"]), f"{path}: {window_id} battle-open mismatch")
        if "source_event_state" in expected:
            require(source_event_state == expected["source_event_state"], f"{path}: {window_id} source event state mismatch")
        if "encounter_history_count" in expected:
            require(encounter_history_count == int(expected["encounter_history_count"]), f"{path}: {window_id} encounter history mismatch")
        if "avoidance_pressure" in expected:
            require(abs(avoidance_pressure - float(expected["avoidance_pressure"])) < 1e-9, f"{path}: {window_id} avoidance pressure mismatch")
        if "ecological_mortality_events" in expected:
            require(ecological_mortality_events == int(expected["ecological_mortality_events"]), f"{path}: {window_id} ecological mortality mismatch")
        if "emigration_events" in expected:
            require(emigration_events == int(expected["emigration_events"]), f"{path}: {window_id} emigration mismatch")
        if expected.get("minecraft_uuid_changed"):
            require(minecraft_uuid is not None and minecraft_uuid != first_materialized_uuid, f"{path}: {window_id} did not change UUID")
        if "event_resolved_directly_by_battle" in expected:
            require(expected["event_resolved_directly_by_battle"] is False, f"{path}: {window_id} illegal direct event resolution")
        if "ecological_death" in expected:
            require(expected["ecological_death"] is False, f"{path}: {window_id} KO promoted to death")
        if "automatic_emigration" in expected:
            require(expected["automatic_emigration"] is False, f"{path}: {window_id} KO promoted to emigration")

    require(not battle_open, f"{path}: trace ends with battle still active")
    require(known_member_exists, f"{path}: persistent actor disappeared")
    require(population_total == int(start["population_total"]), f"{path}: trace changed population without demographic authority")
    require(encounter_history_count == 1, f"{path}: expected exactly one persistent encounter-history entry")
    require(ecological_mortality_events == 0, f"{path}: unexpected ecological mortality")
    require(emigration_events == 0, f"{path}: unexpected emigration")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    path = args.root / "implementation" / "marea-sendero-persistent-actor-cross-fixture-trace-v1.json"
    try:
        data = load_json(path)
        validate_trace(path, data, args.root)
    except ValidationError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    print(f"PASS {path.relative_to(args.root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
