import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "implementation" / "marea-sendero-site-use-identity-trace-v1.json"


def load_fixture():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_site_use_fixture_preserves_population_and_has_no_battle_handoff():
    data = load_fixture()
    assert data["population"]["total"] == 12
    assert data["expected_final"]["population_total"] == 12
    assert data["expected_final"]["demographic_events"] == 0
    assert data["expected_final"]["autoptu_handoffs"] == 0
    assert all(event.get("population_delta", 0) == 0 for event in data["events"])


def test_same_site_can_be_used_by_two_already_counted_sources_without_auto_alias():
    data = load_fixture()
    uses = [event for event in data["events"] if event["type"] == "SITE_USE_RECORDED"]
    source_refs = {event["internal_source_ref"] for event in uses}
    assert len(uses) == 3
    assert len(source_refs) == 2
    assert all(event["source_already_counted"] for event in uses)
    assert data["expected_final"]["distinct_counted_sources_using_site"] == 2
    assert data["expected_final"]["same_site_auto_aliases"] == 0


def test_nondetection_is_not_absence_or_demography():
    data = load_fixture()
    nondetection = next(event for event in data["events"] if event["type"] == "SITE_NONDETECTION_RECORDED")
    assert nondetection["absence_inferred"] is False
    assert nondetection["death_inferred"] is False
    assert nondetection["emigration_inferred"] is False
    assert nondetection["population_delta"] == 0


def test_same_site_only_identity_alias_attempt_is_rejected():
    data = load_fixture()
    attempt = next(event for event in data["events"] if event["type"] == "IDENTITY_ALIAS_ATTEMPT")
    assert attempt["basis"] == "SAME_SITE_RECURRENCE_ONLY"
    assert attempt["result"] == "REJECTED_INSUFFICIENT_DISCRIMINATIVE_EVIDENCE"
    assert attempt["auto_merge_performed"] is False
    assert attempt["autoptu_handoff"] is False


def test_public_observations_do_not_expose_internal_source_refs():
    data = load_fixture()
    observations = [event for event in data["events"] if event["type"] == "PUBLIC_OBSERVATION_RECORDED"]
    assert observations
    assert all(event["internal_source_exposed"] is False for event in observations)
    assert all("internal_source_ref" not in event for event in observations)
    assert data["expected_final"]["internal_source_leaks"] == 0


def test_restart_preserves_history_without_aliasing_sources():
    data = load_fixture()
    restart = next(event for event in data["events"] if event["type"] == "SERVER_RESTART")
    assert restart["population_total_after_restart"] == 12
    assert restart["site_use_history_preserved"] is True
    assert restart["distinct_internal_sources_preserved"] == 2
    assert restart["auto_aliases_after_restart"] == 0


def test_fixture_does_not_canonize_site_ownership_or_nesting():
    data = load_fixture()
    assert data["scenario_is_canon"] is False
    assert data["site"]["canon_site"] is False
    assert data["site"]["territory_implied"] is False
    assert data["site"]["nest_implied"] is False
    assert data["site"]["ownership_implied"] is False
