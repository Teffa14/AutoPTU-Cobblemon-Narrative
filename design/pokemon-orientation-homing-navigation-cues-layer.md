# Pokémon Orientation, Homing & Navigation Cues Layer

Status: PROPOSED SYSTEMS DESIGN / NON-CANON
Pass: 177
Date: 2026-08-26

## Purpose

This layer owns evidence-backed biological orientation and homing state for persistent Pokémon, populations and collectives. It records how an observed subject appears to determine direction or return toward a goal under defined conditions.

It does not own route geometry, migration episodes, home ranges, scent fields, astronomical state, signs, tracking, Minecraft pathfinding or PTU movement mechanics.

## Authority boundary

Use this chain:

`goal/context -> available cue environment -> observation or authorized displacement -> orientation response -> route/outcome observation -> cue-use assessment -> revision -> downstream handoff`

Existing authorities remain authoritative:

- Pokémon Agency owns persistent individual identity, agency, custody, partnership and release.
- Wildlife Migration owns migration patterns, annual episodes, corridors and stopovers.
- Pokémon Spatial Ecology owns home ranges, core-use, site fidelity and territoriality.
- Wayfinding owns human-authored guidance, route descriptions, markers, junctions and actor route knowledge.
- Olfactory Landscapes owns odor sources, fields and scent observations.
- Light/Astronomy owns lightscape and celestial observations.
- Geology/Metrology owns physical and measured environmental state relevant to any magnetic-anomaly hypothesis.
- Telemetry owns tags, receivers, fixes and movement segments.
- Field Signs, Photography, Passive Acoustics and Community Science own their evidence records.
- Research Ethics owns authorization for handling, experimental displacement or intrusive tests.
- PTU/AutoPTU owns Capabilities, Abilities, Skills, movement and battle resolution.

This layer consumes references from those systems. It cannot rewrite them.

## Core distinctions

`ORIENTATION != NAVIGATION`

`COMPASS CUE != POSITIONAL MAP`

`HOMING OUTCOME != PROVEN HOMING MECHANISM`

`RETURN != SITE FIDELITY`

`SITE FIDELITY != ABILITY TO RETURN AFTER DISPLACEMENT`

`MIGRATION ROUTE != NAVIGATIONAL CUE`

`LANDMARK USE != HUMAN WAYFINDING KNOWLEDGE`

`SCENT DETECTION != STRAIGHT-LINE PATH TO SOURCE`

`MAGNETIC LORE != MAGNETORECEPTION`

`MAGNET PULL != HOMING`

`MINECRAFT PATHFINDING != BIOLOGICAL ORIENTATION EVIDENCE`

## Primary entities

### ORIENTATION_PROFILE

Persistent analytical container for one subject or authored population under a bounded life/history context.

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
  homing_trial_refs: []
  natural_return_event_refs: []
  cue_conflict_case_refs: []
  orientation_history_refs: []
  canon_status: proposed
```

An orientation profile is not a stat or Capability.

### NAVIGATION_GOAL_CONTEXT

Stores what the observed movement appears directed toward, without assuming motive.

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

Candidate descriptive goal types:

- HOME_OR_CORE_SITE
- NATAL_SITE
- NEST_OR_DEN
- STOPOVER
- MIGRATION_DESTINATION
- COLLECTIVE_LOCATION
- RESOURCE_SITE
- RELEASE_SITE_RETURN
- TRAINER_OR_FORMER_PARTNER_LOCATION
- UNKNOWN

A goal classification does not create attachment, ownership or motive.

### ORIENTATION_OBSERVATION

Stores what the subject actually did.

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
  environmental_context_refs: []
  observation_method_ref: null
  effort_or_coverage_ref: null
  observer_refs: []
  evidence_refs: []
  confidence: null
```

A successful arrival records the outcome only.

### CUE_ENVIRONMENT_SNAPSHOT

References the cue conditions plausibly available during an observation.

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
  magnetic_measurement_or_geology_refs: []
  route_guidance_refs: []
  weather_refs: []
  infrastructure_refs: []
  obscuration_refs: []
  uncertainty_refs: []
```

This object does not claim the Pokémon perceived or used every listed cue.

### CUE_USE_ASSESSMENT

A reviewed claim about which information may have contributed to orientation.

```yaml
cue_use_assessment:
  assessment_id: null
  orientation_profile_id: null
  temporal_scope_ref: null
  goal_context_refs: []
  candidate_cue_types: []
  supporting_observation_refs: []
  contradictory_observation_refs: []
  controlled_test_refs: []
  alternative_hypothesis_refs: []
  current_assessment: UNRESOLVED
  confidence: null
  supersedes_assessment_id: null
```

Candidate cue tags are descriptive only:

- VISUAL_LANDMARK
- CELESTIAL
- LIGHT_DIRECTION
- OLFACTORY
- WIND_ASSOCIATED
- ACOUSTIC
- MAGNETIC_COMPASS_HYPOTHESIS
- MAGNETIC_MAP_HYPOTHESIS
- PATH_INTEGRATION_HYPOTHESIS
- SOCIAL_FOLLOWING
- ROUTE_MEMORY
- MULTIMODAL
- UNKNOWN

`MAGNETIC_COMPASS_HYPOTHESIS` and `MAGNETIC_MAP_HYPOTHESIS` must remain separate.

### NATURAL_RETURN_EVENT

Records an unmanipulated return observation.

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

A return can support site fidelity or homing questions but does not identify the mechanism by itself.

### HOMING_TRIAL

Experimental or management-linked displacement evidence. This entity requires Research Ethics and any required Care/Conservation authorization.

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
  release_condition_refs: []
  observation_refs: []
  telemetry_refs: []
  outcome: UNKNOWN
  welfare_stop_condition_refs: []
  followup_refs: []
```

Candidate outcomes:

- GOAL_REACHED
- ORIENTED_GOALWARD_NOT_CONFIRMED_ARRIVAL
- SEARCH_BEHAVIOR_OBSERVED
- ALTERNATIVE_GOAL_REACHED
- RETURNED_TO_RELEASE_SITE
- WITHDREW_FROM_TRIAL
- MONITORING_LOST
- NOT_RESOLVED
- UNKNOWN

Do not create experimental displacement casually for quest content.

### CUE_CONFLICT_CASE

Used when available evidence suggests two or more guidance systems disagree or one expected cue was disrupted.

```yaml
cue_conflict_case:
  case_id: null
  subject_refs: []
  time_window: null
  location_ref: null
  expected_baseline_ref: null
  changed_cue_refs: []
  unchanged_cue_refs: []
  behavior_change_refs: []
  candidate_explanation_refs: []
  current_assessment: UNRESOLVED
  confidence: null
```

Examples may include:

- familiar landmark removed during redevelopment;
- artificial night lighting near a migration corridor;
- odor plume changed by wind or water flow;
- magnetic anomaly hypothesis near geology or infrastructure;
- route obstruction causing search behavior while the cue system remains intact;
- altered visibility after fire, snow or vegetation growth.

No case automatically creates Confused, Accuracy penalties, Fatigue or forced movement.

### ORIENTATION_BASELINE_REVISION

Versioned summary of repeated behavior under comparable conditions.

```yaml
orientation_baseline_revision:
  baseline_revision_id: null
  orientation_profile_id: null
  valid_observation_window: null
  goal_context_refs: []
  typical_initial_heading_band: null
  typical_search_pattern_tags: []
  typical_cue_context_refs: []
  sample_size_band: null
  effort_and_coverage_refs: []
  uncertainty_ref: null
  supersedes_revision_id: null
```

The baseline is descriptive. A deviation is not automatically impairment.

## Multimodal navigation

Ouros should prefer combinations over magical single-cue certainty.

A common research structure can be represented as:

`broad positional cue -> coarse orientation -> local cue encountered -> search/localization -> arrival`

Possible authored examples:

- magnetic hypothesis for broad heading plus familiar odor near a river mouth;
- celestial heading at night plus landmark localization near a roost;
- route memory through a valley plus acoustic contact near a collective;
- visual landmark chain in an urban district plus scent at the final block.

The generator must never assign one of these combinations to a species because it “sounds plausible.” It needs authored species/population evidence or Chronicle observations.

## Learning and life history

Orientation can interact with Social Learning, Cognition, Aging, Migration and Juvenile Dispersal without duplicating them.

Allowed questions:

- did an inexperienced individual improve after repeated trips?
- does a juvenile follow an experienced collective during early travel?
- does an older individual continue to use a landmark removed years later?
- does a released former partner retain a route learned during captivity?
- did a learned route persist after infrastructure changed?

Not allowed as automatic conclusions:

- adult = expert navigator;
- juvenile = poor navigator;
- group movement = teaching;
- repeated path = cultural tradition;
- former partnership = guaranteed homing to Trainer;
- return = memory of a specific route.

## Integration with Migration

Migration owns where and when the regional movement occurred.

Orientation may explain only a reviewed behavioral hypothesis about how movement was guided.

A migration episode can remain fully valid when cue mechanism is unknown.

A detour may result from weather, habitat, infrastructure, disturbance, resource distribution or orientation error. Do not choose among these without evidence.

## Integration with Spatial Ecology

Spatial Ecology owns home range and site fidelity.

Orientation owns the process of directed return or heading selection.

An individual can show high site fidelity because it repeatedly returns, yet the exact mechanism can remain unknown.

An excursion outside a known home range is not a homing trial unless there was a controlled or authorized displacement context.

## Integration with Olfactory Landscapes

Olfactory Landscapes owns source and odor-field state. Orientation can reference detections and field snapshots.

Do not derive a route from a smell source by drawing a straight line. Wind, turbulence, current and intermittent detections matter.

## Integration with Wayfinding

Wayfinding records human guidance and actor route knowledge. A Pokémon may observe a landmark that also appears on a trail map, but the biological navigation assessment does not inherit the human route description.

A sign pointing north is not evidence a Pokémon used the sign.

## Minecraft projection

Minecraft/Cobblemon may render current positions, movements, landmarks, lights, weather, signs and environmental assets. It is not the authority for orientation.

Never infer cue use from:

- pathfinding nodes;
- shortest-path selection;
- entity facing direction unless an authored observation contract explicitly records it;
- chunk load/unload;
- spawn/despawn;
- navigation AI failures;
- client compass direction;
- minimap pins;
- vanilla mob home-position logic.

The direction of authority is:

`authoritative world/ecology state -> presentation/AI intent -> Minecraft playback`

not

`Minecraft movement -> scientific truth`.

## PTU / mechanical guardrails

This layer authors no new battle or overworld mechanics.

Explicit prohibitions:

- `Magnet Pull` does not grant magnetic navigation.
- Rock/Steel/Electric Type does not grant magnetoreception.
- Probopass being the Compass Pokémon does not grant a universal compass mechanic.
- battle LoS does not provide landmark navigation.
- base movement legality does not prove a route is known.
- Tracker does not automatically identify homing mechanisms.
- Telepathy does not automatically share maps.
- Perception does not create perfect orientation.
- Survival does not receive a new navigation DC here.
- a known home range does not grant Accuracy, Initiative, Evasion, Speed or capture bonuses.
- cue conflict does not create Confused, Slowed, Tripped, Suppressed or Fatigue.
- magnetic anomalies do not modify Steel-types, Electric-types or Items without an exact PTU/Caelo rule.

## Battle handoff

Orientation should normally resolve as world state before or after battle.

A FULL mechanically rich encounter may need complete movement when actors must cross, pursue, withdraw, intercept or redirect; `terrain/weather/hazards/zones/reactions` when dynamic environmental cues or barriers have tactical effects; AI tactical policy for non-KO goals such as `HOME`, `SEARCH`, `FOLLOW_CUE`, `WITHDRAW`, `REJOIN_GROUP` or `REACH_LANDMARK`; and Minecraft/Cobblemon/Craftics adapter/playback.

A REDUCED version resolves navigation, search and ecological movement outside the grid, freezes a static legal arena, and lets AutoPTU resolve only a discrete confrontation. The narrative premise remains intact.

## Long-term Chronicle value

The system is most useful when evidence changes over years.

A familiar route can become less reliable after a landmark disappears. A cue hypothesis can be weakened by a displacement observation. A population can begin using a new corridor while keeping the same navigational mechanism. A city can reduce light pollution and later observe a different rate of disorientation without proving causality from a single season.

Old assessments remain historically queryable.

## Canon questions still open

Ouros must eventually define:

- which species or local populations have authored orientation behavior;
- whether any magnetic-sense phenomenon is actually known in-setting;
- what institutions study animal navigation;
- whether displacement experiments are culturally/ethically acceptable and under what restrictions;
- what navigation observations predate the player;
- how much orientation state advances offline;
- how sensitive natal sites, release sites and den locations are handled;
- whether any Caelo-specific rules alter navigation, Survival, Perception, Tracker or magnetic phenomena.

Until those decisions are reviewed, every orientation profile and cue mechanism remains proposed or evidence-backed only, never mechanically inferred.