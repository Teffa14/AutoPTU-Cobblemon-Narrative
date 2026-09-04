import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE_PATH = ROOT / "implementation" / "marea-sendero-cobblemon-spawn-admission-fixture-v1.json"


class ReplayError(RuntimeError):
    pass


def validate(trace):
    population_total = trace["population"]["total"]
    expected_actor = trace["persistent_actor"]["actor_id"]
    active_leases = {}
    tokens = {}
    admitted = 0
    cancelled_uncontrolled = 0
    passthrough = 0
    unknown_with_authority = 0
    demographic_events = 0
    autoptu_handoffs = 0

    if not trace["verified_adapter_primitives"].get("entity_spawn_cancelable"):
        raise ReplayError("fixture requires a verified cancellable entity-spawn primitive")

    for event in sorted(trace["events"], key=lambda item: item["seq"]):
        kind = event["type"]

        if event.get("population_delta", 0) != 0:
            raise ReplayError(f"adapter presentation event cannot change population: {kind}")

        if kind == "PROJECTION_LEASE_RESERVED":
            source_id = event["source_id"]
            if source_id != expected_actor:
                raise ReplayError("fixture may only lease the existing persistent actor")
            if any(lease["source_id"] == source_id for lease in active_leases.values()):
                raise ReplayError("persistent actor already has an active direct lease")
            active_leases[event["lease_id"]] = {"source_id": source_id}

        elif kind == "ADMISSION_TOKEN_ISSUED":
            lease_id = event["lease_id"]
            if lease_id not in active_leases:
                raise ReplayError("admission token requires a prior active lease")
            if event["source_id"] != active_leases[lease_id]["source_id"]:
                raise ReplayError("admission token source must match lease source")
            tokens[event["token_id"]] = {"lease_id": lease_id, "consumed": False}

        elif kind == "COBBLEMON_MATERIALIZATION_REQUESTED":
            token_id = event["token_id"]
            if token_id not in tokens or tokens[token_id]["consumed"]:
                raise ReplayError("materialization request requires live unused token")

        elif kind == "POKEMON_ENTITY_SPAWN_CALLBACK":
            admission_class = event["admission_class"]
            if admission_class == "OUROS_MANAGED_DIRECT":
                token_id = event.get("token_id")
                if token_id not in tokens or tokens[token_id]["consumed"]:
                    raise ReplayError("managed direct entity requires live unused token")
                if event["decision"] != "ADMIT" or event.get("cancel_event"):
                    raise ReplayError("valid managed direct entity should be admitted")
                if event.get("ecology_write_authorized"):
                    raise ReplayError("entity admission cannot authorize ecology writes")
                admitted += 1
            elif admission_class == "UNCONTROLLED_NATURAL":
                if not event.get("cancel_event"):
                    raise ReplayError("uncontrolled natural entity must hit cancellation backstop")
                if event.get("ecology_write_authorized") or event.get("persistent_actor_created"):
                    raise ReplayError("uncontrolled natural entity cannot author ecology")
                if event.get("autoptu_eligible"):
                    raise ReplayError("uncontrolled natural entity cannot enter AutoPTU")
                cancelled_uncontrolled += 1
            elif admission_class == "EXEMPT_OWNED_OR_SYSTEM_PRESENTATION":
                if event.get("cancel_event"):
                    raise ReplayError("fixture must not blanket-cancel exempt owned/system presentation")
                if event.get("wild_population_membership_created"):
                    raise ReplayError("owned/system presentation cannot become wild population membership")
                passthrough += 1
            elif admission_class == "UNKNOWN_OR_UNCLASSIFIED":
                if event.get("ecology_write_authorized") or event.get("persistent_actor_created"):
                    unknown_with_authority += 1
                if event.get("autoptu_eligible"):
                    raise ReplayError("unknown entity cannot enter AutoPTU")
            else:
                raise ReplayError(f"unknown admission class: {admission_class}")

        elif kind == "ADMISSION_TOKEN_CONSUMED":
            token_id = event["token_id"]
            if token_id not in tokens or tokens[token_id]["consumed"]:
                raise ReplayError("token may be consumed exactly once")
            tokens[token_id]["consumed"] = True

        elif kind == "UUID_CORRELATED_TO_LEASE":
            if event["lease_id"] not in active_leases:
                raise ReplayError("UUID correlation requires active lease")
            if not any(token["lease_id"] == event["lease_id"] and token["consumed"] for token in tokens.values()):
                raise ReplayError("UUID correlation must follow token consumption/admission")

        elif kind == "COBBLEMON_ENTITY_DESPAWNED":
            if event.get("demographic_effect") != "NONE":
                demographic_events += 1
                raise ReplayError("despawn cannot create demographic truth")

        elif kind == "PROJECTION_LEASE_RELEASED":
            if event["lease_id"] not in active_leases:
                raise ReplayError("cannot release missing lease")
            del active_leases[event["lease_id"]]

        elif kind == "SERVER_RESTART":
            tokens.clear()
            if event["population_total_after_restart"] != population_total:
                raise ReplayError("restart cannot change population total")
            if not event.get("persistent_actor_survives"):
                raise ReplayError("persistent actor must survive restart")

        if event.get("autoptu_handoff") == "OPEN_AUTOPTU":
            autoptu_handoffs += 1

    result = {
        "population_total": population_total,
        "persistent_actor_id": expected_actor,
        "active_direct_leases": len(active_leases),
        "live_admission_tokens": len(tokens),
        "admitted_managed_entities": admitted,
        "cancelled_uncontrolled_entities": cancelled_uncontrolled,
        "owned_or_system_passthrough_entities": passthrough,
        "unknown_entities_with_ecology_authority": unknown_with_authority,
        "demographic_events": demographic_events,
        "autoptu_handoffs": autoptu_handoffs,
    }

    if result != trace["expected_final"]:
        raise ReplayError(f"final snapshot mismatch: {result!r}")
    return result


def main():
    with TRACE_PATH.open("r", encoding="utf-8") as handle:
        trace = json.load(handle)
    print(json.dumps(validate(trace), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
