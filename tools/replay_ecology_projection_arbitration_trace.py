#!/usr/bin/env python3
"""Replay Pass 249 projection-arbitration trace and enforce authority invariants."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TRACE = ROOT / "implementation" / "marea-sendero-projection-arbitration-trace-v1.json"


class ReplayError(RuntimeError):
    pass


def load_trace(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def replay(trace: dict) -> dict:
    population_total = trace["population"]["initial_total"]
    persistent_actor_id = trace["persistent_actor"]["actor_id"]
    leases: dict[str, dict] = {}
    active_source_leases: dict[str, str] = {}
    materialized: dict[str, dict] = {}
    evidence_roots: set[str] = set()
    observation_claim = None
    observation_confidence = None
    quarantined: set[str] = set()
    demographic_events = 0
    autoptu_battles_opened = 0
    current_uuid = None
    last_seq = 0

    for event in trace["events"]:
        seq = event["seq"]
        if seq <= last_seq:
            raise ReplayError("event sequence must be strictly increasing")
        last_seq = seq
        event_type = event["type"]

        if event_type == "PROJECTION_ENVELOPE_EVALUATED":
            if event.get("population_total") != population_total:
                raise ReplayError("projection envelope cannot rewrite population total")

        elif event_type == "PRESENTATION_ARBITRATED":
            decision = event["decision"]
            if decision == "INDIRECT_SIGN" and event.get("source_id") is not None:
                raise ReplayError("indirect arbitration must not expose a persistent source")
            if decision == "QUARANTINE_UNCORRELATED_ENTITY":
                entity_uuid = event["minecraft_entity_uuid"]
                if event.get("ecology_write_authorized") is not False:
                    raise ReplayError("uncorrelated entity quarantine cannot authorize ecology writes")
                if event.get("autoptu_handoff") not in {None, "BLOCK_UNSUPPORTED", "STAY_OVERWORLD"}:
                    raise ReplayError("uncorrelated entity cannot open AutoPTU")
                quarantined.add(entity_uuid)

        elif event_type == "INDIRECT_SIGN_EMITTED":
            if event.get("minecraft_entity_uuid") is not None:
                raise ReplayError("indirect sign cannot carry a Pokemon entity UUID")
            if event.get("projection_lease_id") is not None:
                raise ReplayError("indirect sign cannot consume a projection lease")
            if event.get("persistent_actor_id") is not None:
                raise ReplayError("indirect sign cannot expose persistent actor identity")
            if event.get("exact_population_total_exposed"):
                raise ReplayError("indirect sign cannot expose hidden population total")
            if event.get("autoptu_handoff") != "STAY_OVERWORLD":
                raise ReplayError("indirect sign cannot independently open AutoPTU")
            evidence_roots.add(event["provenance_root_id"])

        elif event_type == "OBSERVATION_RECORDED":
            if event.get("persistent_actor_id_exposed"):
                raise ReplayError("observation cannot leak persistent actor identity")
            if event.get("exact_population_total_exposed"):
                raise ReplayError("observation cannot leak hidden population total")
            evidence_roots.add(event["provenance_root_id"])
            observation_claim = event["claim"]
            observation_confidence = event["confidence"]

        elif event_type == "SIGN_RELAYED":
            root = event["source_provenance_root_id"]
            if root not in evidence_roots:
                raise ReplayError("relay must reference an existing evidence root")
            if event.get("new_independent_root_created"):
                raise ReplayError("relay cannot manufacture an independent evidence root")
            if event.get("confidence_increase"):
                raise ReplayError("relay alone cannot increase confidence")

        elif event_type == "PROJECTION_LEASE_RESERVED":
            lease_id = event["lease_id"]
            source_id = event["source_id"]
            if lease_id in leases:
                raise ReplayError("projection lease id must be unique")
            if source_id in active_source_leases:
                raise ReplayError("one persistent source cannot hold multiple active direct leases")
            leases[lease_id] = {"source_id": source_id, "state": "RESERVED"}
            active_source_leases[source_id] = lease_id

        elif event_type == "COBBLEMON_ENTITY_MATERIALIZED":
            lease_id = event["lease_id"]
            source_id = event["source_id"]
            lease = leases.get(lease_id)
            if lease is None or lease["state"] != "RESERVED":
                raise ReplayError("direct materialization requires a prior reserved lease")
            if lease["source_id"] != source_id:
                raise ReplayError("materialized source must match reserved lease source")
            entity_uuid = event["minecraft_entity_uuid"]
            if entity_uuid in materialized:
                raise ReplayError("Minecraft entity UUID cannot be correlated twice")
            materialized[entity_uuid] = {"lease_id": lease_id, "source_id": source_id}
            lease["state"] = "MATERIALIZED"
            current_uuid = entity_uuid if source_id == persistent_actor_id else current_uuid

        elif event_type == "UNCORRELATED_NATIVE_ENTITY_SEEN":
            if event.get("lease_id") is not None or event.get("ouros_source_id") is not None:
                raise ReplayError("fixture uncorrelated entity must truly lack authority correlation")

        elif event_type == "COBBLEMON_ENTITY_DESPAWNED":
            entity_uuid = event["minecraft_entity_uuid"]
            correlation = materialized.get(entity_uuid)
            if correlation is None:
                raise ReplayError("despawn must refer to a correlated materialized entity")
            if event.get("demographic_effect") != "NONE":
                raise ReplayError("despawn cannot create demographic change")
            if current_uuid == entity_uuid:
                current_uuid = None

        elif event_type == "PROJECTION_LEASE_RELEASED":
            lease_id = event["lease_id"]
            source_id = event["source_id"]
            lease = leases.get(lease_id)
            if lease is None:
                raise ReplayError("cannot release unknown projection lease")
            if lease["source_id"] != source_id:
                raise ReplayError("lease release source mismatch")
            lease["state"] = "RELEASED"
            if active_source_leases.get(source_id) == lease_id:
                del active_source_leases[source_id]

        elif event_type == "SERVER_RESTART":
            if event.get("population_total") != population_total:
                raise ReplayError("restart cannot change population total")
            if event.get("runtime_uuid_correlations_cleared"):
                current_uuid = None
            if not event.get("persistent_identity_preserved"):
                raise ReplayError("restart must preserve persistent identity")

        elif event_type in {"BIRTH", "DEATH", "IMMIGRATION", "EMIGRATION", "CAPTURE_REMOVAL"}:
            demographic_events += 1
            raise ReplayError("Pass 249 fixture must not contain demographic events")

        elif event_type == "AUTOPTU_BATTLE_OPENED":
            autoptu_battles_opened += 1

        else:
            raise ReplayError(f"unknown event type: {event_type}")

    return {
        "population_total": population_total,
        "persistent_actor_id": persistent_actor_id,
        "runtime_minecraft_uuid": current_uuid,
        "independent_evidence_roots": sorted(evidence_roots),
        "observation_claim": observation_claim,
        "observation_confidence": observation_confidence,
        "quarantined_uncorrelated_entities": sorted(quarantined),
        "demographic_events": demographic_events,
        "autoptu_battles_opened": autoptu_battles_opened,
    }


def validate(trace: dict) -> dict:
    result = replay(trace)
    expected = trace["expected_final"]
    if result != expected:
        raise ReplayError(
            "final replay snapshot differs from fixture expectation:\n"
            + json.dumps({"actual": result, "expected": expected}, indent=2, sort_keys=True)
        )
    if result["population_total"] != trace["population"]["expected_final_total"]:
        raise ReplayError("final population total violates fixture conservation")
    return result


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else DEFAULT_TRACE
    try:
        result = validate(load_trace(path))
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ReplayError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
