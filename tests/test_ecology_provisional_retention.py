import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "implementation" / "marea-sendero-provisional-retention-trace-v1.json"


def load_fixture():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def events_of_type(data, event_type):
    return [event for event in data["events"] if event["type"] == event_type]


def event_of_type(data, event_type):
    return events_of_type(data, event_type)[0]


def test_retention_policy_never_changes_population_or_opens_battle():
    data = load_fixture()
    assert data["population"]["total"] == 12
    assert data["expected_final"]["population_total"] == 12
    assert data["expected_final"]["net_population_delta"] == 0
    assert data["expected_final"]["demographic_events"] == 0
    assert data["expected_final"]["autoptu_handoffs"] == 0
    assert all(event.get("population_delta", 0) == 0 for event in data["events"])


def test_recent_site_use_can_expire_without_erasing_observation_history():
    data = load_fixture()
    horizon_events = events_of_type(data, "SEMANTIC_HORIZON_EVALUATED")
    site = next(event for event in horizon_events if event["state_class"] == "RECENT_SITE_USE")
    assert site["horizon_reached"] is True
    assert site["result"] == "DROP_PRIVATE_KEEP_PUBLIC_HISTORY"
    assert site["public_observation_history_preserved"] is True
    assert site["private_linkage_closed"] is True
    assert site["source_count_contribution_preserved"] is True
    assert data["expected_final"]["site_use_private_linkages_expired"] == 1


def test_active_individual_disturbance_response_survives_restart_without_identity_promotion():
    data = load_fixture()
    restart = event_of_type(data, "SERVER_RESTART")
    assert restart["population_total_after_restart"] == 12
    assert restart["disturbance_response_restored"] is True
    assert restart["semantic_horizon_still_active"] is True
    assert restart["expired_site_linkage_restored"] is False
    assert restart["public_identity_promoted"] is False
    assert data["expected_final"]["restart_safe_retained_states"] == 1


def test_minecraft_damage_signal_cannot_author_persistent_injury():
    data = load_fixture()
    observed = event_of_type(data, "MINECRAFT_PRESENTATION_EVENT_OBSERVED")
    attempt = event_of_type(data, "RETAINED_STATE_AUTHORING_ATTEMPT")
    assert observed["presentation_event"] == "GENERIC_ENTITY_DAMAGE_SIGNAL"
    assert observed["authoritative_ptu_result_present"] is False
    assert attempt["requested_state_class"] == "PERSISTENT_INJURY"
    assert attempt["authority_source"] == "MINECRAFT_PRESENTATION_ONLY"
    assert attempt["authoritative_autoptu_semantic_result_present"] is False
    assert attempt["result"] == "REJECT_UNAUTHORIZED_STATE"
    assert attempt["retained_state_created"] is False
    assert attempt["ptu_state_mutated"] is False
    assert data["expected_final"]["persistent_injuries_created_from_minecraft_noise"] == 0


def test_unresolved_durable_consequence_is_quarantined_instead_of_smeared_across_population():
    data = load_fixture()
    horizon_events = events_of_type(data, "SEMANTIC_HORIZON_EVALUATED")
    response = next(event for event in horizon_events if event["state_class"] == "INDIVIDUAL_DISTURBANCE_RESPONSE")
    assert response["horizon_reached"] is False
    assert response["aggregation_would_misattribute_active_consequence"] is True
    assert response["admissible_internal_continuity_present"] is False
    assert response["result"] == "PROMOTE_OR_QUARANTINE"
    assert response["promotion_committed"] is False
    assert response["quarantined_from_aggregate_application"] is True
    assert data["expected_final"]["aggregate_misattributions"] == 0


def test_public_knowledge_does_not_expose_retention_or_source_identity():
    data = load_fixture()
    public = event_of_type(data, "PUBLIC_KNOWLEDGE_CHECK")
    assert public["public_identity_state"] == "UNRESOLVED"
    assert public["internal_retention_state_exposed"] is False
    assert public["internal_source_exposed"] is False
    assert public["minecraft_damage_promoted_to_injury"] is False
    assert data["expected_final"]["public_identity_promotions"] == 0
    assert data["expected_final"]["internal_source_leaks"] == 0


def test_fixture_uses_only_already_counted_noncanon_sources():
    data = load_fixture()
    assert data["scenario_is_canon"] is False
    assert len(data["sources"]) == 3
    assert all(source["already_counted"] is True for source in data["sources"])
    assert all(source["contribution_to_population_total"] == 1 for source in data["sources"])
    assert all(source["canon_actor"] is False for source in data["sources"])
    known_refs = {source["internal_source_ref"] for source in data["sources"]}
    private_events = [event for event in data["events"] if "source_ref" in event]
    assert all(event["source_ref"] in known_refs for event in private_events)


def test_reduced_fixture_declares_adapter_as_only_end_to_end_blocking_family():
    data = load_fixture()
    deps = data["battle_dependency_categories"]
    assert deps["minecraft_cobblemon_craftics_adapter_playback"] == "PARTIAL_BLOCKING"
    assert deps["ai_tactical_policy"] == "BLOCKING"
    assert deps["full_stateful_damage_pipeline"] == "PARTIAL"
    attempt = event_of_type(data, "RETAINED_STATE_AUTHORING_ATTEMPT")
    assert attempt["ptu_state_mutated"] is False
