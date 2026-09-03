#!/usr/bin/env python3
"""Validate Ouros ecology implementation fixtures with only the Python stdlib.

The validator intentionally checks authority and conservation invariants rather than
simulating PTU mechanics. AutoPTU remains the owner of structured battle rules.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

PERMANENT_CAPABILITIES = {
    "targeting_footprints_range_los",
    "base_movement_legality",
    "complete_movement",
    "core_calculations",
    "action_economy_initiative",
    "full_turn_round_lifecycle",
    "full_stateful_damage_pipeline",
    "status_lifecycle",
    "terrain_weather_hazards_zones_reactions",
    "move_specific_behavior",
    "abilities",
    "items",
    "trainer_features_perks",
    "ai_legal_action_infrastructure",
    "ai_tactical_policy",
    "minecraft_cobblemon_craftics_adapter_playback",
}
ALLOWED_CAPABILITY_STATES = {
    "VERIFIED",
    "PARTIAL",
    "BLOCKING",
    "MIXED_PARTIAL_BLOCKING",
    "PARTIAL_BLOCKING",
}
PRESENTATION_ONLY_EVENTS = {
    "MINECRAFT_GENERIC_ENTITY_SPAWN",
    "MINECRAFT_ENTITY_DESPAWN",
    "MINECRAFT_VANILLA_DEATH",
    "AUTOPTU_KO_PRESENTATION_ONLY",
}


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


def validate_common(path: Path, data: dict[str, Any]) -> None:
    require(bool(data.get("fixture_id")), f"{path}: missing fixture_id")
    require(bool(data.get("status")), f"{path}: missing status")
    windows = data.get("windows")
    require(isinstance(windows, list) and windows, f"{path}: windows must be a non-empty list")
    ids: list[str] = []
    for index, window in enumerate(windows):
        require(isinstance(window, dict), f"{path}: window {index} must be an object")
        window_id = window.get("id")
        require(isinstance(window_id, str) and window_id, f"{path}: window {index} missing id")
        ids.append(window_id)
    require(len(ids) == len(set(ids)), f"{path}: duplicate window ids")

    deps = data.get("battle_dependency_categories")
    if deps is not None:
        require(isinstance(deps, dict), f"{path}: battle_dependency_categories must be an object")
        missing = PERMANENT_CAPABILITIES - set(deps)
        extra = set(deps) - PERMANENT_CAPABILITIES
        require(not missing, f"{path}: missing capability categories: {sorted(missing)}")
        require(not extra, f"{path}: unknown capability categories: {sorted(extra)}")
        bad = {key: value for key, value in deps.items() if value not in ALLOWED_CAPABILITY_STATES}
        require(not bad, f"{path}: invalid capability states: {bad}")


def population_for(event: dict[str, Any], target_id: str) -> str:
    return str(event.get("population_id", target_id))


def validate_demography(path: Path, data: dict[str, Any]) -> None:
    if "population_demography" not in str(data.get("fixture_id", "")):
        return
    start = data["starting_state"]
    target_id = data["population_id"]
    source = data["test_source_population"]
    source_id = source["population_id"]
    target_total = int(start["total_count"])
    source_total = int(source["starting_total_count"])
    stages = {key: int(value) for key, value in start["stage_counts"].items()}
    known = len(start["known_persistent_member_ids"])
    unresolved = int(start["unresolved_member_pool_count"])
    require(sum(stages.values()) == target_total, f"{path}: starting stage counts do not sum to total")
    require(known + unresolved == target_total, f"{path}: known + unresolved does not equal starting total")
    seen_event_ids: set[str] = set()

    for window in data["windows"]:
        for event in window.get("input_events", []):
            event_id = event.get("demographic_event_id")
            if event_id:
                require(event_id not in seen_event_ids, f"{path}: duplicate demographic event id {event_id}")
                seen_event_ids.add(event_id)
            kind = event.get("event_type")
            count = int(event.get("count", 0))
            population_id = population_for(event, target_id)

            if kind in PRESENTATION_ONLY_EVENTS or kind == "ECOLOGY_CONTEXT_UPDATE":
                continue
            if kind == "STAGE_TRANSITION":
                require(population_id == target_id, f"{path}: fixture runner tracks target stages only")
                from_stage = event["from_stage"]
                to_stage = event["to_stage"]
                require(stages.get(from_stage, 0) >= count, f"{path}: stage transition underflow in {window['id']}")
                stages[from_stage] -= count
                stages[to_stage] = stages.get(to_stage, 0) + count
                continue

            delta = 0
            if kind in {"LOCAL_RECRUITMENT", "IMMIGRATION", "RELEASE_RETURN", "RELOCATION_IN", "MIGRATION_SETTLEMENT"}:
                delta = count
            elif kind in {"ECOLOGICAL_MORTALITY", "EMIGRATION", "CAPTURE_REMOVAL", "RELOCATION_OUT", "MIGRATION_DEPARTURE"}:
                delta = -count
            elif kind is not None:
                raise ValidationError(f"{path}: unsupported demographic event type {kind!r} in {window['id']}")

            if population_id == target_id:
                target_total += delta
                require(target_total >= 0, f"{path}: target population underflow in {window['id']}")
            elif population_id == source_id:
                source_total += delta
                require(source_total >= 0, f"{path}: source population underflow in {window['id']}")
            else:
                raise ValidationError(f"{path}: unknown population {population_id!r} in {window['id']}")

        expected = window.get("expected", {})
        if "target_total_count" in expected:
            require(target_total == expected["target_total_count"], f"{path}: {window['id']} target total {target_total} != {expected['target_total_count']}")
        if "source_total_count" in expected:
            require(source_total == expected["source_total_count"], f"{path}: {window['id']} source total {source_total} != {expected['source_total_count']}")
        if "regional_total_count" in expected:
            regional = target_total + source_total
            require(regional == expected["regional_total_count"], f"{path}: {window['id']} regional total {regional} != {expected['regional_total_count']}")
        if "stage_counts" in expected:
            require(stages == expected["stage_counts"], f"{path}: {window['id']} stage ledger mismatch")


def validate_spawn_reconciliation(path: Path, data: dict[str, Any]) -> None:
    if "spawn_reconciliation" not in str(data.get("fixture_id", "")):
        return
    start = data["starting_state"]
    total = int(start["population_total"])
    known = set(start["known_persistent_member_ids"])
    unresolved = int(start["unresolved_member_pool_count"])
    leases: dict[str, dict[str, Any]] = {}
    source_locks: dict[str, str] = {}
    uuids: dict[str, str] = {}
    semantic_captures: set[str] = set()

    def source_key(event: dict[str, Any]) -> str | None:
        if event.get("member_id"):
            return f"member:{event['member_id']}"
        if event.get("unresolved_slot_token"):
            return f"slot:{event['unresolved_slot_token']}"
        return None

    for window in data["windows"]:
        for event in window.get("input_events", []):
            kind = event.get("event_type")
            lease_id = event.get("lease_id")
            if kind == "LEASE_RESERVE":
                key = source_key(event)
                require(key is not None, f"{path}: {window['id']} reserve missing source")
                require(key not in source_locks, f"{path}: {window['id']} duplicate active lease for {key}")
                leases[lease_id] = {"source": key, "state": "RESERVED", "uuid": None}
                source_locks[key] = lease_id
            elif kind == "LEASE_RESERVE_ATTEMPT":
                key = source_key(event)
                if event.get("lease_class") == "EXTERNAL_ASSOCIATED_LEASE":
                    continue
                require(key in source_locks, f"{path}: {window['id']} expected duplicate-source rejection but source is not locked")
            elif kind in {"LEASE_MATERIALIZE", "LEASE_REMATERIALIZE"}:
                require(lease_id in leases, f"{path}: {window['id']} materializes unknown lease {lease_id}")
                uuid = event["minecraft_entity_uuid"]
                require(uuid not in uuids, f"{path}: {window['id']} reuses active Minecraft UUID {uuid}")
                old_uuid = leases[lease_id].get("uuid")
                if old_uuid:
                    uuids.pop(old_uuid, None)
                leases[lease_id]["uuid"] = uuid
                leases[lease_id]["state"] = "MATERIALIZED"
                uuids[uuid] = lease_id
            elif kind == "IDENTITY_PROMOTION":
                require(lease_id in leases, f"{path}: {window['id']} promotes unknown lease")
                lease = leases[lease_id]
                old_key = lease["source"]
                require(old_key.startswith("slot:"), f"{path}: {window['id']} promotion source is not unresolved")
                new_member = event["new_member_id"]
                new_key = f"member:{new_member}"
                require(new_key not in source_locks, f"{path}: {window['id']} promoted member already locked")
                source_locks.pop(old_key, None)
                source_locks[new_key] = lease_id
                lease["source"] = new_key
                known.add(new_member)
                unresolved -= 1
                require(unresolved >= 0, f"{path}: unresolved pool underflow")
            elif kind == "CHUNK_UNLOAD":
                require(lease_id in leases, f"{path}: {window['id']} unloads unknown lease")
                old_uuid = leases[lease_id].get("uuid")
                if old_uuid:
                    uuids.pop(old_uuid, None)
                leases[lease_id]["uuid"] = None
                leases[lease_id]["state"] = "SUSPENDED"
            elif kind == "STRUCTURED_BATTLE_HANDOFF":
                require(lease_id in leases, f"{path}: {window['id']} hands off unknown lease")
                leases[lease_id]["state"] = "ENGAGED"
            elif kind == "AUTOPTU_SEMANTIC_RESULT" and event.get("capture_confirmed") and event.get("removal_confirmed"):
                semantic_captures.add(event["battle_id"])
            elif kind == "CAPTURE_REMOVAL":
                battle_id = event.get("related_battle_id")
                require(battle_id in semantic_captures, f"{path}: {window['id']} capture removal lacks verified semantic result")
                count = int(event.get("count", 0))
                total -= count
                for member in event.get("member_ids_if_resolved", []):
                    known.discard(member)
                    key = f"member:{member}"
                    active = source_locks.pop(key, None)
                    if active:
                        lease = leases.pop(active, None)
                        if lease and lease.get("uuid"):
                            uuids.pop(lease["uuid"], None)
            elif kind == "LEASE_RELEASE":
                require(lease_id in leases, f"{path}: {window['id']} releases unknown lease")
                lease = leases.pop(lease_id)
                source_locks.pop(lease["source"], None)
                if lease.get("uuid"):
                    uuids.pop(lease["uuid"], None)
            elif kind == "ENTITY_CORRELATION_MISMATCH":
                require(lease_id in leases, f"{path}: {window['id']} invalidates unknown lease")
                old_uuid = leases[lease_id].get("uuid")
                if old_uuid:
                    uuids.pop(old_uuid, None)
                leases[lease_id]["uuid"] = None
                leases[lease_id]["state"] = "INVALIDATED_WITH_AUDIT"
            elif kind in {"MINECRAFT_ENTITY_DESPAWN", "SERVER_RESTART", "LEASE_INDEX_RECONCILE"}:
                continue

        require(total == len(known) + unresolved, f"{path}: {window['id']} population total != known + unresolved")
        expected = window.get("expected", {})
        if "population_total" in expected:
            require(total == expected["population_total"], f"{path}: {window['id']} population total mismatch")
        if "known_persistent_count" in expected:
            require(len(known) == expected["known_persistent_count"], f"{path}: {window['id']} known-member count mismatch")
        if "unresolved_pool_count" in expected:
            require(unresolved == expected["unresolved_pool_count"], f"{path}: {window['id']} unresolved count mismatch")
        if "active_lease_count" in expected:
            require(len(leases) == expected["active_lease_count"], f"{path}: {window['id']} active lease count mismatch")


def validate_observation(path: Path, data: dict[str, Any]) -> None:
    if data.get("pass") != 240:
        return
    for window in data["windows"]:
        expected = window.get("expect", {})
        if window["id"] == "W9_NO_SIGHTING_IS_NOT_ABSENCE":
            require(expected.get("absence_claim_automatically_created") is False, f"{path}: no-detection must not prove absence")
        if window["id"] == "W12_AUTOPTU_KO_RESULT":
            require(expected.get("death_claim") is False and expected.get("ecological_mortality_event") is False, f"{path}: KO must not imply death")


def validate_world_event(path: Path, data: dict[str, Any]) -> None:
    if data.get("pass") != 241:
        return
    params = data["test_parameters"]
    clear_count = 0
    active = False
    for window in data["windows"]:
        inp = window.get("input", {})
        exp = window.get("expect", {})
        if all(key in inp for key in ("resource_window_remaining", "activity_pressure", "human_overlap_pressure")):
            should_open = (
                inp["resource_window_remaining"] <= params["open_resource_window_remaining_max"]
                and inp["activity_pressure"] >= params["open_activity_pressure_min"]
                and inp["human_overlap_pressure"] >= params["open_human_overlap_pressure_min"]
            )
            if not active and should_open:
                active = True
            if "event_open" in exp:
                require(exp["event_open"] == active, f"{path}: {window['id']} event-open expectation disagrees with thresholds")
        if active and "disturbance_pressure" in inp:
            if inp["disturbance_pressure"] <= params["clear_disturbance_pressure_max"]:
                clear_count += 1
            else:
                clear_count = 0
            if exp.get("clear_counter_reset"):
                require(clear_count == 0, f"{path}: {window['id']} expected hysteresis reset")
            if "clear_counter" in exp:
                require(clear_count == exp["clear_counter"], f"{path}: {window['id']} clear counter mismatch")


def validate_handoff(path: Path, data: dict[str, Any]) -> None:
    if data.get("pass") != 242:
        return
    by_id = {window["id"]: window for window in data["windows"]}
    for window_id in ("W0_VISIBLE_NOT_BATTLE", "W1_WARNING_NOT_BATTLE", "W2_UNOPPOSED_FLEE", "W3_PLAYER_BACKS_AWAY"):
        require(by_id[window_id]["expect"].get("decision") == "STAY_OVERWORLD", f"{path}: {window_id} must remain overworld")
    require(by_id["W4_DIRECT_STRUCTURED_ENGAGEMENT"]["expect"].get("decision") == "OPEN_AUTOPTU", f"{path}: structured engagement must open AutoPTU")
    reduced = by_id["W7_UNSUPPORTED_TACTICAL_PURSUIT"]["expect"]
    require(reduced.get("decision") == "USE_REDUCED_VERSION", f"{path}: unsupported pursuit must use reduced version")
    require(by_id["W10_TACTICAL_KO_RETURN"]["expect"].get("ecological_death") is False, f"{path}: tactical KO must not imply ecological death")
    require(by_id["W14_CAPTURE_WRITEBACK_GATED"]["expect"].get("population_reduced") is False, f"{path}: unverified capture cannot reduce population")


def validate_file(path: Path) -> None:
    data = load_json(path)
    validate_common(path, data)
    validate_demography(path, data)
    validate_spawn_reconciliation(path, data)
    validate_observation(path, data)
    validate_world_event(path, data)
    validate_handoff(path, data)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    paths = sorted((args.root / "implementation").glob("*fixture-v1.json"))
    if not paths:
        print("No ecology fixture JSON files found", file=sys.stderr)
        return 2
    failures: list[str] = []
    for path in paths:
        try:
            validate_file(path)
            print(f"PASS {path.relative_to(args.root)}")
        except ValidationError as exc:
            failures.append(str(exc))
            print(f"FAIL {exc}", file=sys.stderr)
    if failures:
        print(f"{len(failures)} fixture(s) failed validation", file=sys.stderr)
        return 1
    print(f"Validated {len(paths)} ecology fixture(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
