# Pokémon Orientation, Homing & Multimodal Navigation Cues Layer

Status: PROPOSED SYSTEMS DESIGN / NON-CANON
Pass: 177
Date: 2026-08-26

## Authority correction

Pass 81, `geomagnetism-magnetic-navigation-interference-layer.md`, already owns magnetic-field state, magnetic navigation profiles, anomalies, interference and Pokémon magnetic-behavior observations. Pass 177 does not duplicate that authority.

This layer owns the higher-order biological question: how an observed Pokémon appears to orient toward a goal or return to a familiar site while potentially combining visual, olfactory, celestial, acoustic, social, route-memory and Pass 81 magnetic context.

## Purpose

The layer records evidence-backed orientation and homing assessments for persistent Pokémon, populations and collectives. It preserves the difference between an observed heading, a successful return, the goal being pursued and the mechanism hypothesized to have guided that movement.

It does not own route geometry, migration episodes, home ranges, magnetic fields, scent fields, astronomical state, wayfinding signs, tracking, Minecraft pathfinding or PTU movement mechanics.

## Authority boundary

Use this chain:

`goal/context -> cue-state references -> observation or authorized displacement -> orientation response -> route/outcome observation -> multimodal cue-use assessment -> revision -> downstream handoff`

Existing authorities remain authoritative:

- Geomagnetism Pass 81 owns all magnetic field/anomaly/interference state and magnetic-specific navigation profiles/observations.
- Pokémon Agency owns persistent individual identity, agency, custody, partnership and release.
- Wildlife Migration owns migration patterns, episodes, corridors and stopovers.
- Pokémon Spatial Ecology owns home ranges, core-use, site fidelity and territoriality.
- Wayfinding owns human-authored guidance, markers, junctions and actor route knowledge.
- Olfactory Landscapes owns odor sources, fields and scent observations.
- Light/Astronomy owns lightscape and celestial observations.
- Passive Acoustics/Soundscapes owns acoustic detections and sound fields.
- Telemetry owns tags, receivers, fixes and movement segments.
- Research Ethics owns handling, experimental displacement and intrusive testing authorization.
- PTU/AutoPTU owns Skills, Capabilities, Abilities, movement and battle resolution.

Pass 177 may correlate records from these systems. It cannot rewrite them.

## Core distinctions

`ORIENTATION != NAVIGATION`

`COMPASS INFORMATION != POSITIONAL MAP`

`HOMING OUTCOME != PROVEN HOMING MECHANISM`

`RETURN != SITE FIDELITY`

`SITE FIDELITY != HOMING AFTER DISPLACEMENT`

`MIGRATION ROUTE != NAVIGATIONAL CUE`

`LANDMARK USE != HUMAN WAYFINDING KNOWLEDGE`

`SCENT DETECTION != STRAIGHT-LINE PATH`

`PASS_81_MAGNETIC_OBSERVATION != MAGNETIC_HOMING_PROOF`

`MAGNET PULL != MAGNETORECEPTION`

`MINECRAFT PATHFINDING != BIOLOGICAL ORIENTATION EVIDENCE`

## ORIENTATION_PROFILE

```yaml
orientation_profile:
  orientation_profile_id: null
  subject_type: INDIVIDUAL
  pokemon_entity_ids: []
  collective_refs: []
  population_refs: []
  species_refs: []
  life_stage_context_refs: []
  migration_pattern_refs: []
  spatial_use_profile_refs: []
  known_goal_refs: []
  cue_use_assessment_refs: []
  natural_return_event_refs: []
  homing_trial_refs: []
  cue_conflict_case_refs: []
  baseline_revision_refs: []
  canon_status: proposed
```

An orientation profile is an analytical container, never a stat or Capability.

## NAVIGATION_GOAL_CONTEXT

```yaml
navigation_goal_context:
  goal_context_id: null
  subject_ref: null
  goal_type: UNKNOWN
  goal_site_ref: null
  goal_actor_refs: []
  goal_collective_ref: null
  goal_resource_ref: null
  migration_episode_ref: null
  nesting_episode_ref: null
  release_site_ref: null
  evidence_refs: []
  confidence: null
```

Candidate descriptive goal types include HOME_OR_CORE_SITE, NATAL_SITE, NEST_OR_DEN, STOPOVER, MIGRATION_DESTINATION, COLLECTIVE_LOCATION, RESOURCE_SITE, RELEASE_SITE_RETURN and UNKNOWN.

A goal classification does not create motive, attachment, ownership or partnership.

## ORIENTATION_OBSERVATION

```yaml
orientation_observation:
  observation_id: null
  subject_ref: null
  observed_at: null
  start_location_ref: null
  goal_context_ref: null
  initial_heading_ref: null
  heading_change_refs: []
  movement_segment_refs: []
  pause_or_search_behavior_refs: []
  arrival_or_nonarrival_ref: null
  cue_environment_snapshot_ref: null
  observation_method_ref: null
  effort_or_coverage_ref: null
  observer_refs: []
  evidence_refs: []
  confidence: null
```

Arrival proves arrival only.

## CUE_ENVIRONMENT_SNAPSHOT

This object is a bundle of references to existing authorities, not a second environmental model.

```yaml
cue_environment_snapshot:
  snapshot_id: null
  occurred_at: null
  spatial_scope_ref: null
  visual_landmark_refs: []
  lightscape_refs: []
  celestial_observation_refs: []
  olfactory_field_refs: []
  wind_context_refs: []
  acoustic_context_refs: []
  pass81_magnetic_field_or_anomaly_refs: []
  wayfinding_asset_refs: []
  weather_refs: []
  infrastructure_refs: []
  obscuration_refs: []
  uncertainty_refs: []
```

Presence in the snapshot does not prove perception or use by the Pokémon.

## MULTIMODAL_CUE_USE_ASSESSMENT

```yaml
multimodal_cue_use_assessment:
  assessment_id: null
  orientation_profile_id: null
  temporal_scope_ref: null
  goal_context_refs: []
  candidate_cue_refs: []
  pass81_magnetic_assessment_refs: []
  supporting_observation_refs: []
  contradictory_observation_refs: []
  controlled_test_refs: []
  alternative_hypothesis_refs: []
  current_assessment: UNRESOLVED
  confidence: null
  supersedes_assessment_id: null
```

Candidate non-authoritative cue tags may include VISUAL_LANDMARK, CELESTIAL, LIGHT_DIRECTION, OLFACTORY, WIND_ASSOCIATED, ACOUSTIC, ROUTE_MEMORY, SOCIAL_FOLLOWING, PATH_INTEGRATION_HYPOTHESIS, PASS81_MAGNETIC_CONTEXT and MULTIMODAL.

Any detailed magnetic claim must point to Pass 81 rather than being authored here.

## NATURAL_RETURN_EVENT

```yaml
natural_return_event:
  return_event_id: null
  subject_ref: null
  origin_observation_ref: null
  destination_site_ref: null
  departure_or_last_seen_window: null
  return_window: null
  intervening_observation_refs: []
  monitoring_coverage_refs: []
  migration_context_ref: null
  release_context_ref: null
  outcome: RETURN_OBSERVED
  mechanism_assessment_ref: null
```

A natural return may support Spatial Ecology or Rehabilitation handoffs. It does not establish the route or cue mechanism.

## HOMING_TRIAL

Experimental displacement evidence is allowed only after Research Ethics and any required Care/Conservation authorization.

```yaml
homing_trial:
  homing_trial_id: null
  subject_refs: []
  authorization_refs: []
  handling_event_refs: []
  transport_provenance_refs: []
  release_location_ref: null
  familiar_goal_ref: null
  displacement_band: null
  cue_manipulation_refs: []
  pass81_magnetic_context_refs: []
  release_condition_refs: []
  observation_refs: []
  telemetry_refs: []
  outcome: UNKNOWN
  welfare_stop_condition_refs: []
  followup_refs: []
```

Candidate outcomes include GOAL_REACHED, ORIENTED_GOALWARD_NOT_CONFIRMED_ARRIVAL, SEARCH_BEHAVIOR_OBSERVED, ALTERNATIVE_GOAL_REACHED, RETURNED_TO_RELEASE_SITE, WITHDREW_FROM_TRIAL, MONITORING_LOST, NOT_RESOLVED and UNKNOWN.

Do not generate displacement experiments merely to create quest content.

## CUE_CONFLICT_CASE

```yaml
cue_conflict_case:
  case_id: null
  subject_refs: []
  time_window: null
  location_ref: null
  expected_baseline_ref: null
  changed_cue_refs: []
  unchanged_cue_refs: []
  pass81_magnetic_context_refs: []
  behavior_change_refs: []
  candidate_explanation_refs: []
  current_assessment: UNRESOLVED
  confidence: null
```

Possible contexts include landmark removal, artificial night lighting, altered odor plumes, changed acoustic conditions, a Pass 81 magnetic anomaly/interference incident, route obstruction, snow, fire or vegetation growth.

None automatically creates Confused, Accuracy penalties, Fatigue, Slowed or forced movement.

## ORIENTATION_BASELINE_REVISION

```yaml
orientation_baseline_revision:
  baseline_revision_id: null
  orientation_profile_id: null
  valid_observation_window: null
  goal_context_refs: []
  typical_heading_band: null
  typical_search_pattern_tags: []
  typical_cue_context_refs: []
  sample_size_band: null
  effort_and_coverage_refs: []
  uncertainty_ref: null
  supersedes_revision_id: null
```

A deviation from baseline is evidence, not a diagnosis.

## Multimodal pattern

A useful abstract sequence is:

`coarse positional/orientation information -> approach -> local cue encounter -> search/localization -> arrival`

One population might use a Pass 81 magnetic context during broad travel and an olfactory or visual context near its goal. Another may rely on route memory and landmarks. Another may remain completely unresolved.

The generator must never assign these mechanisms from Type, Pokédex category or narrative convenience.

## Integration rules

Wildlife Migration remains valid even when mechanism is unknown. A detour does not prove orientation failure.

Spatial Ecology owns repeated use of places. Repeated return can support site fidelity while homing mechanism remains unknown.

Olfactory Landscapes owns the odor field. Pass 177 cannot draw a direct route from odor source to animal.

Wayfinding owns signs and human guidance. A Pokémon using a physical landmark does not inherit the written route instructions associated with it.

Pass 81 owns magnetic observations, local anomalies, corrections and magnetic-specific navigation profiles. Pass 177 only uses those records as one possible component of a wider cue assessment.

Social Learning owns transmission. Following an experienced Pokémon once does not prove teaching or cultural navigation.

## Minecraft boundary

Minecraft/Cobblemon may render movement and environmental state but cannot decide what cue a Pokémon used.

Do not infer orientation from shortest-path choice, entity facing direction, pathfinding nodes, chunk loading, spawn/despawn, vanilla home-position logic, client compass direction or minimap pins.

Authority remains:

`world/ecology evidence -> reviewed orientation intent/assessment -> presentation`

never the reverse.

## PTU / AutoPTU guardrails

Pass 177 authors no new battle or overworld mechanics.

- `Magnet Pull` does not grant navigation.
- Rock/Steel/Electric Type does not grant magnetoreception.
- Probopass flavor does not create compass accuracy.
- Pass 81 magnetic anomalies do not modify Pokémon mechanically without an exact PTU/Caelo contract.
- battle LoS does not provide landmark navigation.
- base movement legality does not prove a route is known.
- Tracker does not reveal a homing mechanism automatically.
- Telepathy does not share maps automatically.
- Perception does not create perfect orientation.
- Survival receives no new navigation DC here.
- familiar territory grants no Accuracy, Evasion, Initiative, Speed or capture modifier.
- cue conflict creates no Status.

## Battle handoff and capability dependencies

Orientation normally resolves outside combat.

A FULL encounter with moving wildlife, escorts, crossing, withdrawal, pursuit or interception needs complete movement. If environmental cues/barriers change tactical legality it also needs `terrain/weather/hazards/zones/reactions`. Non-KO behaviors such as `HOME`, `SEARCH`, `FOLLOW_CUE`, `WITHDRAW`, `REJOIN_GROUP` or `REACH_LANDMARK` need AI tactical policy. Minecraft/Cobblemon/Craftics adapter/playback remains required for faithful overworld handoff.

A REDUCED version resolves orientation and ecological movement in world state, freezes a static legal arena, and gives AutoPTU only the discrete confrontation.

## Canon questions

Ouros must eventually decide which species/populations have authored orientation behaviors, whether any Pass 81 magnetic phenomena are behaviorally relevant, which institutions study navigation, whether displacement research is acceptable, which natal/release/den locations remain private, how much state advances offline and whether Caelo changes any relevant Survival, Perception, Tracker or movement rules.

Until reviewed, all cue mechanisms remain proposed or evidence-backed hypotheses, not mechanics or canon facts.