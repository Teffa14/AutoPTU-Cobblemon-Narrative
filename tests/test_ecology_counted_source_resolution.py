import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "implementation" / "marea-sendero-counted-source-resolution-trace-v1.json"


def load_fixture():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def event_of_type(data, event_type):
    return next(event for event in data["events"] if event["type"] == event_type)


def test_resolution_preserves_population_and_never_opens_battle():
    data = load_fixture()
    committed = event_of_type(data, "COUNTED_SOURCE_RESOLUTION_COMMITTED")
    assert data["population"]["total"] == 12
    assert data["expected_final"]["population_total"] == 12
    assert committed["anonymous_source_delta"] == -1
    assert committed["persistent_source_delta"] == 1
    assert committed["population_delta"] == 0
    assert committed["demographic_event"] is False
    assert committed["autoptu_handoff"] is False
    assert data["expected_final"]["demographic_events"] == 0
    assert data["expected_final"]["autoptu_handoffs"] == 0


def test_only_an_already_counted_source_is_resolved():
    data = load_fixture()
    committed = event_of_type(data, "COUNTED_SOURCE_RESOLUTION_COMMITTED")
    assert committed["source_was_already_counted"] is True
    assert committed["source_lineage_locked"] is True
    assert data["resolution_target"]["created_from_existing_count"] is True
    assert data["expected_final"]["net_population_delta"] == 0


def test_same_site_recurrence_cannot_resolve_identity():
    data = load_fixture()
    attempt = event_of_type(data, "COUNTED_SOURCE_RESOLUTION_ATTEMPT")
    assert attempt["basis"] == "SAME_SITE_RECURRENCE_ONLY"
    assert attempt["result"] == "REJECTED_INSUFFICIENT_DISCRIMINATIVE_EVIDENCE"
    assert attempt["transaction_committed"] is False
    assert attempt["population_delta"] == 0


def test_resolution_replay_is_idempotent():
    data = load_fixture()
    committed = event_of_type(data, "COUNTED_SOURCE_RESOLUTION_COMMITTED")
    replay = event_of_type(data, "COUNTED_SOURCE_RESOLUTION_REPLAY")
    assert committed["transaction_id"] == replay["transaction_id"]
    assert replay["same_payload"] is True
    assert replay["result"] == "IDEMPOTENT_NO_OP"
    assert replay["additional_persistent_sources_created"] == 0
    assert data["expected_final"]["resolution_commits"] == 1


def test_retired_unresolved_source_cannot_lease_again():
    data = load_fixture()
    lease = event_of_type(data, "PROJECTION_LEASE_ATTEMPT")
    assert lease["source_state"] == "RETIRED_RESOLVED"
    assert lease["result"] == "REJECTED_RETIRED_SOURCE"
    assert lease["lease_created"] is False
    assert data["expected_final"]["retired_source_leases"] == 0


def test_internal_resolution_does_not_promote_character_knowledge():
    data = load_fixture()
    committed = event_of_type(data, "COUNTED_SOURCE_RESOLUTION_COMMITTED")
    public = event_of_type(data, "PUBLIC_KNOWLEDGE_CHECK")
    assert committed["public_identity_promoted"] is False
    assert public["public_identity_state"] == "POSSIBLE_SAME_INDIVIDUAL"
    assert public["internal_resolution_exposed"] is False
    assert public["automatic_confirmation"] is False
    assert data["expected_final"]["internal_source_leaks"] == 0


def test_public_observation_never_contains_internal_source_identity():
    data = load_fixture()
    observations = [event for event in data["events"] if event["type"] == "PUBLIC_OBSERVATION_RECORDED"]
    assert observations
    assert all(event["internal_source_exposed"] is False for event in observations)
    assert all("internal_source_ref" not in event for event in observations)
    assert all("persistent_actor_id" not in event for event in observations)


def test_restart_preserves_lineage_retirement_and_epistemic_state():
    data = load_fixture()
    restart = event_of_type(data, "SERVER_RESTART")
    assert restart["population_total_after_restart"] == 12
    assert restart["source_lineage_mapping_preserved"] is True
    assert restart["retired_source_state_preserved"] is True
    assert restart["transaction_id_preserved"] is True
    assert restart["history_refs_preserved"] is True
    assert restart["public_identity_state_after_restart"] == "POSSIBLE_SAME_INDIVIDUAL"
    assert data["expected_final"]["lineage_preserved_after_restart"] is True


def test_fixture_does_not_create_second_canon_fletchling():
    data = load_fixture()
    assert data["scenario_is_canon"] is False
    assert data["resolution_target"]["canon_actor"] is False
    assert data["resolution_target"]["persistent_ref"].startswith("fixture-only:")
