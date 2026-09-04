import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "implementation" / "marea-sendero-provisional-source-state-trace-v1.json"


def load_fixture():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def events_of_type(data, event_type):
    return [event for event in data["events"] if event["type"] == event_type]


def event_of_type(data, event_type):
    return events_of_type(data, event_type)[0]


def test_provisional_lifecycle_never_changes_population_or_opens_battle():
    data = load_fixture()
    assert data["population"]["total"] == 12
    assert data["expected_final"]["population_total"] == 12
    assert data["expected_final"]["net_population_delta"] == 0
    assert data["expected_final"]["demographic_events"] == 0
    assert data["expected_final"]["autoptu_handoffs"] == 0
    assert all(event.get("population_delta", 0) == 0 for event in data["events"])


def test_only_already_counted_sources_can_open_provisional_episodes():
    data = load_fixture()
    opens = events_of_type(data, "PROVISIONAL_EPISODE_OPENED")
    assert len(opens) == 2
    assert all(event["source_was_already_counted"] is True for event in opens)
    source_refs = {source["internal_source_ref"] for source in data["sources"] if source["already_counted"]}
    assert all(event["source_ref"] in source_refs for event in opens)


def test_ephemeral_episode_expires_without_erasing_public_history():
    data = load_fixture()
    expired = event_of_type(data, "PROVISIONAL_EPISODE_EXPIRED")
    assert expired["new_state"] == "EXPIRED_TO_AGGREGATE"
    assert expired["public_observation_history_preserved"] is True
    assert expired["source_count_contribution_preserved"] is True
    assert expired["private_linkage_closed"] is True
    assert expired["demographic_event"] is False


def test_repeated_sightings_and_same_site_cannot_force_promotion():
    data = load_fixture()
    evaluations = events_of_type(data, "PROMOTION_EVALUATION")
    rejected = next(event for event in evaluations if event["result"].startswith("REJECTED_"))
    assert rejected["basis"] == "REPEATED_SIGHTINGS_AND_SAME_SITE_ONLY"
    assert rejected["admissible_internal_continuity_present"] is False
    assert rejected["promotion_committed"] is False


def test_durable_history_plus_internal_continuity_requires_resolution():
    data = load_fixture()
    evaluations = events_of_type(data, "PROMOTION_EVALUATION")
    required = next(event for event in evaluations if event["result"] == "PROMOTION_REQUIRED")
    assert required["durable_consequence_present"] is True
    assert required["admissible_internal_continuity_present"] is True
    assert data["expected_final"]["promotion_required_evaluations"] == 1


def test_promotion_delegates_to_pass258_and_preserves_count():
    data = load_fixture()
    committed = event_of_type(data, "COUNTED_SOURCE_RESOLUTION_COMMITTED")
    assert committed["delegated_contract"] == "design/counted-source-resolution-contract.md"
    assert committed["source_was_already_counted"] is True
    assert committed["source_lineage_locked"] is True
    assert committed["anonymous_source_delta"] == -1
    assert committed["persistent_source_delta"] == 1
    assert committed["population_delta"] == 0
    assert committed["demographic_event"] is False
    assert committed["public_identity_promoted"] is False


def test_expired_private_linkage_cannot_be_resurrected_without_fresh_basis():
    data = load_fixture()
    reopen = event_of_type(data, "PROVISIONAL_REOPEN_ATTEMPT")
    assert reopen["fresh_continuity_basis_present"] is False
    assert reopen["result"] == "REJECTED_EXPIRED_LINKAGE_CANNOT_RESURRECT"
    assert reopen["episode_opened"] is False
    assert data["expected_final"]["expired_episode_resurrections"] == 0


def test_public_knowledge_never_exposes_private_source_or_episode_identity():
    data = load_fixture()
    public_events = [event for event in data["events"] if event["type"] in {"PUBLIC_OBSERVATION_RECORDED", "PUBLIC_KNOWLEDGE_CHECK"}]
    assert public_events
    for event in public_events:
        assert "source_ref" not in event
        assert "episode_id" not in event
        assert "persistent_actor_id" not in event
        assert "minecraft_entity_uuid" not in event
    check = event_of_type(data, "PUBLIC_KNOWLEDGE_CHECK")
    assert check["internal_resolution_exposed"] is False
    assert check["internal_episode_ids_exposed"] is False
    assert check["automatic_confirmation"] is False


def test_restart_preserves_closed_and_resolved_guards_without_creating_population():
    data = load_fixture()
    restart = event_of_type(data, "SERVER_RESTART")
    assert restart["population_total_after_restart"] == 12
    assert restart["expired_episode_state_preserved"] is True
    assert restart["resolved_source_retirement_preserved"] is True
    assert restart["resolution_transaction_preserved"] is True
    assert restart["durable_history_preserved_on_persistent_actor"] is True
    assert restart["public_observation_history_preserved"] is True
    assert restart["autoptu_handoffs_after_restart"] == 0


def test_fixture_does_not_canonize_more_fletchling_actors():
    data = load_fixture()
    assert data["scenario_is_canon"] is False
    assert all(source["canon_actor"] is False for source in data["sources"])
    committed = event_of_type(data, "COUNTED_SOURCE_RESOLUTION_COMMITTED")
    assert committed["target_persistent_ref"].startswith("fixture-only:")
