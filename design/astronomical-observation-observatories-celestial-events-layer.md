# Ouros Astronomical Observation, Observatories & Celestial Events Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon.
Date: 2026-08-25

## Purpose

Ouros needs a persistent authority for observations of the sky without turning astronomy into prophecy, a Legendary scheduler, a Remote Sensing duplicate or a source of invented PTU mechanics.

The central chain is:

`physical sky event/object -> observing opportunity -> observing session -> raw observation -> reduction/measurement -> candidate linkage -> solution or event revision -> follow-up -> scientific interpretation -> optional public/cultural response`

Astronomy produces evidence and predictions. It does not write the future directly.

## 1. Authority boundaries

This layer owns:

- astronomical observing programs;
- observatory/site identity when narratively important;
- observing sessions and sky coverage;
- astronomical target and event records;
- candidate transient detections;
- follow-up requests and observations;
- ephemeris/orbit/event-solution revisions at narrative scale;
- visibility predictions and observing windows;
- corroboration and disagreement between sites;
- astronomical observing archives and long-baseline series;
- public observing notices tied to scientific revisions;
- links between a luminous atmospheric/celestial observation and a later terrestrial recovery candidate.

This layer does not own:

- clock/time-standard truth -> Timekeeping;
- calibration, traceability or measurement uncertainty standards -> Metrology;
- cloud/weather truth -> Meteorology;
- night-sky brightness and artificial-light state -> Lightscapes;
- Earth/region surface observation from elevated or orbital platforms -> Remote Sensing;
- scientific hypotheses/publications -> Science;
- cultural stories, sacred meanings or beliefs -> Sacred Sites, Mythology, Public Memory;
- airspace/platform permission -> Airspace;
- recovered physical meteorites or specimens -> Geology, Material Culture, Museums;
- Pokémon identity or species determination -> Pokémon Agency, Identity, Taxonomy;
- PTU/Caelo rules -> authoritative rules/AutoPTU;
- Minecraft sky/render state as astronomical truth -> never.

## 2. Core separation

Keep these states separate:

```text
PREDICTED VISIBLE != ACTUALLY OBSERVED
CANDIDATE DETECTION != CONFIRMED OBJECT
SAME SKY POSITION != SAME OBJECT
NO DETECTION != EVENT DID NOT OCCUR
CLEAR WEATHER != INSTRUMENT WORKING
INSTRUMENT WORKING != DATA VALIDATED
PUBLIC NOTICE != SCIENTIFIC CERTAINTY
METEOR OBSERVED != METEORITE RECOVERED
CELESTIAL TRADITION != COSMOLOGICAL TRUTH
POKEMON PRESENT != CAUSE OF CELESTIAL EVENT
```

## 3. ASTRONOMICAL_OBSERVING_PROGRAM

```yaml
astronomical_observing_program:
  program_id: null
  institution_ids: []
  purpose_refs: []
  target_class_refs: []
  observing_site_ids: []
  method_revision_ids: []
  schedule_or_trigger_policy_ref: null
  archive_ref: null
  public_participation_policy_ref: null
  started_at: null
  ended_at: null
  status: ACTIVE
```

Candidate purposes:

- LONG_BASELINE_MONITORING
- TRANSIENT_SEARCH
- FOLLOW_UP
- VARIABLE_OBJECT_MONITORING
- METEOR_SHOWER_MONITORING
- LUNAR_OR_PLANETARY_OBSERVATION
- SMALL_BODY_TRACKING
- PUBLIC_EDUCATION
- HISTORICAL_CHART_COMPARISON
- OTHER_AUTHORED

No candidate purpose implies Earth-equivalent technology.

## 4. OBSERVING_SITE

```yaml
observing_site:
  site_id: null
  location_ref: null
  institution_ids: []
  site_type: null
  horizon_profile_ref: null
  lightscape_ref: null
  meteorology_ref: null
  timekeeping_ref: null
  instrument_ids: []
  access_policy_ref: null
  current_operational_state: UNKNOWN
  history_event_ids: []
```

Candidate types include fixed observatory, community observing field, rooftop station, mountain station, mobile setup, radio/other authored station and educational facility. Their actual technology is canon-dependent.

A site can be physically intact but scientifically unusable for a session because of cloud, light pollution, equipment state, time-reference failure or target geometry.

## 5. CELESTIAL_TARGET_OR_EVENT

```yaml
celestial_target_or_event:
  celestial_id: null
  identity_state: CANDIDATE
  target_or_event_type: null
  canonical_name: null
  historical_name_refs: []
  first_observation_ref: null
  accepted_observation_refs: []
  solution_revision_ids: []
  scientific_status: UNRESOLVED
  cultural_reference_ids: []
```

Candidate states:

- CANDIDATE
- CORROBORATED
- ACCEPTED_FOR_SCOPE
- MERGED_WITH_EXISTING
- SPLIT_INTO_MULTIPLE
- REJECTED_AS_ARTIFACT
- UNRESOLVED

Do not infer metaphysical importance from rarity.

## 6. OBSERVING_SESSION

```yaml
observing_session:
  session_id: null
  program_id: null
  site_id: null
  observer_actor_ids: []
  planned_window_ref: null
  actual_start_time_ref: null
  actual_end_time_ref: null
  target_refs: []
  instrument_refs: []
  method_revision_ref: null
  meteorology_context_ref: null
  lightscape_context_ref: null
  timekeeping_quality_ref: null
  planned_coverage_ref: null
  achieved_coverage_ref: null
  interruption_refs: []
  raw_observation_ids: []
  completion_state: null
```

A session can be scientifically useful even if interrupted or if nothing unusual was detected.

## 7. ASTRONOMICAL_OBSERVATION

```yaml
astronomical_observation:
  observation_id: null
  session_id: null
  observer_or_device_ref: null
  raw_record_ref: null
  timestamp_ref: null
  sky_position_or_field_ref: null
  filter_or_method_ref: null
  signal_or_measurement_ref: null
  quality_flags: []
  metrology_refs: []
  candidate_celestial_refs: []
  review_state: UNREVIEWED
  created_at: null
```

Raw observation and interpretation stay separate. A later clock correction or calibration review attaches a derived/corrected record; it never silently edits the raw source.

## 8. CANDIDATE_DETECTION_AND_LINKAGE

```yaml
candidate_detection:
  candidate_id: null
  source_observation_ids: []
  candidate_type: null
  preliminary_position_or_signature_ref: null
  automatic_or_manual: null
  duplicate_or_source_dependency_refs: []
  follow_up_priority: null
  review_state: OPEN
  linked_celestial_id: null
```

Possible outcomes include artifact, already-known object, unresolved candidate, new accepted target, or multiple observations incorrectly merged at first.

A detector or observer can be wrong without misconduct.

## 9. FOLLOW_UP_REQUEST

```yaml
astronomy_follow_up_request:
  request_id: null
  celestial_or_candidate_ref: null
  requested_observation_window_ref: null
  requested_method_or_precision_ref: null
  participating_site_ids: []
  reason_ref: null
  response_observation_ids: []
  result_state: OPEN
```

This supports distributed campaigns and keeps one observatory from becoming omniscient.

## 10. SOLUTION_REVISION

```yaml
astronomical_solution_revision:
  solution_revision_id: null
  celestial_id: null
  predecessor_revision_ref: null
  included_observation_ids: []
  excluded_observation_ids: []
  method_revision_ref: null
  epoch_or_reference_time_ref: null
  parameter_or_ephemeris_ref: null
  uncertainty_summary_ref: null
  valid_scope_ref: null
  supersedes_for_current_use: []
  created_at: null
```

The exact numerical model can remain coarse. What matters for Chronicle is that predictions have provenance and can change as evidence improves.

`superseded` does not mean `fraudulent` or `never used`.

## 11. VISIBILITY_PREDICTION

```yaml
visibility_prediction:
  prediction_id: null
  solution_revision_ref: null
  site_or_region_ref: null
  predicted_window_ref: null
  expected_visibility_band: null
  geometry_assumption_refs: []
  weather_dependency_ref: null
  lightscape_dependency_ref: null
  uncertainty_or_confidence_ref: null
  publication_ref: null
```

Observation outcome is stored separately:

- OBSERVED_AS_PREDICTED
- OBSERVED_WITH_DIFFERENCE
- NOT_OBSERVED_COVERAGE_GOOD
- NOT_OBSERVED_COVERAGE_INCOMPLETE
- WEATHER_BLOCKED
- LIGHTSCAPE_LIMITED
- EQUIPMENT_FAILURE
- TIME_REFERENCE_PROBLEM
- NOT_ATTEMPTED

## 12. METEOR / METEORITE HANDOFF

A luminous event in the atmosphere and a physical object recovered on the ground are not the same record.

```text
luminous observation
 -> trajectory / fall-area hypothesis
 -> search area
 -> candidate terrestrial object
 -> Geology / Material Culture identification
 -> optional linkage assessment
```

A recovered rock is not a meteorite because a player found it inside the predicted area. Likewise, a meteor can be well observed with no recovered material.

If Minior is involved, Pokémon Agency owns the living individual. A fallen Minior is never converted into a mineral specimen by analogy.

## 13. Cultural and public handoffs

Astronomical events can generate:

- festivals;
- public observing nights;
- newspaper/media attention;
- folklore revisions;
- sacred-site activity;
- tourism;
- school programs;
- public-memory artifacts.

Those systems own the social/cultural consequences. Astronomy owns only the evidence and scientific prediction/revision.

A festival date can remain fixed even if the astronomical event drifts or the scientific model changes. A successful ritual cannot guarantee an observation or encounter.

## 14. Pokémon-specific guardrails

Minior may have authored high-altitude/fall behavior because official species lore supports it. Do not infer:

- every meteor is Minior;
- Minior fall = collision damage;
- Minior abundance = meteor-shower intensity;
- astronomy observation = capture eligibility.

Lunatone may have authored full-moon behavior only where canon chooses to use that species lore. Do not infer:

- global lunar stat modifiers;
- automatic full-moon spawns;
- Sleep effects from observation;
- Moonlight/Gravity execution from world phase.

Solrock or other celestial-themed species receive the same protection.

## 15. Minecraft projection contract

Allowed direction:

`authoritative astronomical/time/weather/lightscape state -> presentation hints in Minecraft`

Forbidden direction:

`Minecraft sky texture / moon phase / shader / particle / entity count -> authoritative astronomy`

Minecraft may render a sky event after world state schedules it. The adapter must not use a vanilla moon texture, tick counter or client shader as PTU/canon evidence unless a future integration contract explicitly maps it.

## 16. Long-term Chronicle behavior

Astronomy should generate history through revision, not constant spectacle.

Useful persistent records include:

- a hundred-year observing archive;
- a quiet baseline series;
- a target whose solution improves over five observing seasons;
- a public notice later revised;
- an observatory rebuilt while its archive survives;
- a community observer whose measurements remain useful after retirement;
- a meteorite recovery decades after the original event record is reprocessed;
- an old chart whose coordinate convention is reconstructed by Languages/Timekeeping/Metrology.

## 17. Mechanical boundary

Astronomical world state does not automatically create:

- Weather;
- Terrain;
- zones;
- Gravity;
- Moonlight healing;
- Accuracy or Initiative changes;
- surprise;
- stat changes;
- evolution triggers;
- Legendary appearances;
- capture modifiers;
- meteor damage;
- radiation/status effects;
- Psychic/Occult bonuses.

Any battle that actually uses a particular Move, Ability, Item or Trainer Feature still depends on the corresponding current engine capability and exact mechanic coverage.

## 18. Proposed implementation records

Minimum useful persistence:

```text
astronomical_observing_program
observing_site
celestial_target_or_event
observing_session
astronomical_observation
candidate_detection
astronomy_follow_up_request
astronomical_solution_revision
visibility_prediction
meteorite_linkage_assessment
```

These records remain PROPOSED until the world-state architecture chooses concrete storage and canon institutions.

## 19. Open canon questions

- Does Ouros have formal observatories at campaign start?
- What observing technologies exist: naked-eye, optical instruments, photography, spectroscopy, radio, high-altitude platforms, orbital systems?
- Does Ouros possess artificial satellites at all?
- Which regions have dark-sky observing sites?
- Which celestial cycles/events are authored before players arrive?
- Which cultural observances refer to the sky, and which claims are scientifically confirmed versus traditional?
- Which Pokémon populations have authored celestial-phase behavior?
- Who maintains long-term astronomical archives?
- Can players/communities submit observations into accepted programs?
- What location or technical data should remain restricted?

Until answered, candidates in this file remain system design rather than canon.