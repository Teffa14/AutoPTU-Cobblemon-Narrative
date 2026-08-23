# Ouros Wildlife Migration, Stopovers & Corridors Layer

Status: Proposed systems design. Not established Ouros canon.

## Purpose

Ouros already models calendar/phenology, wild collectives, travel networks, airspace, road ecology, island biogeography, field signs and habitat state. This layer owns the missing longitudinal process: repeated seasonal or condition-linked movement by a population or persistent collective across multiple locations.

The core goal is to preserve migration history without turning Minecraft pathfinding into ecological truth or inventing PTU movement rules.

## Authority boundary

Use this chain:

`season/calendar expectation -> habitat/resource context -> migration episode -> observed movement -> corridor/stopover revision -> consequences -> optional tactical snapshot`

Seasonality owns expected windows and phenology.
Wild Collectives owns persistent group identity.
Habitat layers own local ecological state.
Road/Airspace/Maritime/Island layers own infrastructure or medium-specific constraints.
Migration owns the repeated movement process tying those locations together.

## 1. Migration pattern

A long-term pattern is separate from one year’s event.

```yaml
migration_pattern:
  migration_pattern_id: null
  subject_population_refs: []
  persistent_collective_refs: []
  species_refs: []
  movement_medium_tags: []
  origin_region_refs: []
  destination_region_refs: []
  expected_window_ref: null
  recurring_driver_claim_refs: []
  corridor_revision_refs: []
  stopover_site_refs: []
  historical_episode_refs: []
  confidence: provisional
  source_refs: []
```

Candidate medium tags:

- TERRESTRIAL
- AERIAL
- FRESHWATER
- COASTAL
- OPEN_OCEAN
- SUBTERRANEAN
- MIXED
- UNKNOWN

A medium tag does not grant PTU movement capability.

## 2. Migration episode

```yaml
migration_episode:
  migration_episode_id: null
  migration_pattern_id: null
  world_year_or_cycle_ref: null
  expected_start_window: null
  observed_departure_window: null
  observed_arrival_window: null
  state: PREPARING
  estimated_participant_band: unknown
  exact_known_pokemon_entity_ids: []
  observed_subgroup_refs: []
  route_revision_ref: null
  stopover_use_refs: []
  disturbance_refs: []
  weather_context_refs: []
  phenology_context_refs: []
  final_outcome: null
  confidence: null
```

Suggested states:

- EXPECTED
- PREPARING
- DEPARTURE_OBSERVED
- IN_PROGRESS
- PAUSED_OR_STOPOVER
- DETOURED
- PARTIALLY_COMPLETED
- ARRIVAL_OBSERVED
- COMPLETED
- ABORTED_OR_RETURNED
- NOT_CONFIRMED
- UNKNOWN

Do not force every migration into a clean departure-arrival sequence.

## 3. Corridor revisions

A migration corridor is an ecological footprint, not a single path.

```yaml
migration_corridor_revision:
  corridor_revision_id: null
  migration_pattern_id: null
  valid_from_event_id: null
  valid_to_event_id: null
  corridor_segment_refs: []
  high_use_segment_refs: []
  low_use_segment_refs: []
  alternative_segment_refs: []
  evidence_refs: []
  confidence: null
  supersedes_revision_id: null
```

Old revisions remain historically valid.

## 4. Corridor segment

```yaml
migration_corridor_segment:
  segment_id: null
  geometry_ref: null
  medium_tag: null
  connected_segment_refs: []
  adjacent_habitat_refs: []
  infrastructure_intersection_refs: []
  known_barrier_refs: []
  known_crossing_refs: []
  observation_station_refs: []
  current_access_for_monitoring_ref: null
```

The server should store coarse segments. It should not record every Minecraft coordinate traversed by every Pokémon.

## 5. Stopovers

Stopovers are first-class locations because time spent there may matter more than transit speed.

```yaml
migration_stopover:
  stopover_id: null
  location_ref: null
  migration_pattern_refs: []
  current_habitat_state_refs: []
  recurring_resource_refs: []
  shelter_refs: []
  observation_history_refs: []
  use_history_refs: []
  disturbance_refs: []
  stewardship_refs: []
  current_assessment: UNKNOWN
```

Candidate assessments:

- HIGH_USE
- MODERATE_USE
- LOW_USE
- HISTORIC_USE
- DECLINING_USE
- RECENTLY_RESTORED
- NOT_OBSERVED_THIS_EPISODE
- UNKNOWN

`NOT_OBSERVED_THIS_EPISODE` is not abandonment.

## 6. Movement-wave observations

```yaml
migration_wave_observation:
  observation_id: null
  migration_episode_id: null
  observed_at: null
  location_ref: null
  direction_or_route_claim: null
  estimated_count_band: null
  exact_entity_ids: []
  species_composition_claims: []
  behavior_tags: []
  observation_method_ref: null
  effort_ref: null
  evidence_refs: []
  confidence: null
```

Multiple waves can belong to the same episode.

A migration may be staggered by age, life stage, sex, condition, local weather or unknown causes. Do not invent those explanations unless sourced or observed.

## 7. Partial migration and residency

Some members of a population may remain resident.

```yaml
migration_participation_assessment:
  subject_ref: null
  migration_episode_id: null
  participation_state: UNKNOWN
  evidence_refs: []
  confidence: null
```

States:

- CONFIRMED_PARTICIPANT
- CONFIRMED_RESIDENT_DURING_EPISODE
- TEMPORARILY_SEPARATED
- REJOINED
- POSSIBLE_PARTICIPANT
- UNKNOWN

This avoids assuming that every individual of a species migrates.

## 8. Persistent Pokémon identity

A known Pokémon keeps the same `pokemon_entity_id` through movement.

Migration can update:

- current coarse location;
- collective association;
- observation history;
- route knowledge available to actors;
- public sightings;
- research records.

Migration does not automatically update:

- ownership;
- custody;
- Loyalty;
- command authority;
- mechanical movement capability;
- capture eligibility.

A released former partner may later be observed migrating. That does not restore the old Trainer relationship.

## 9. Route fidelity and revision

```yaml
migration_route_comparison:
  comparison_id: null
  migration_pattern_id: null
  baseline_episode_refs: []
  comparison_episode_ref: null
  reused_segment_refs: []
  new_segment_refs: []
  bypassed_segment_refs: []
  stopover_changes: []
  timing_difference_ref: null
  explanatory_hypothesis_refs: []
  confidence: null
```

One detour does not create a permanent route revision.

A new corridor revision should require repeated evidence, a persistent landscape change, or explicit authored state.

## 10. Barriers and crossings

Migration can intersect:

- roads;
- railways;
- canals;
- dams;
- fences;
- cities;
- ports;
- air routes;
- lighting;
- wind farms or other technology only if Ouros canon later includes them;
- protected areas;
- wildfire scars;
- drought refuges;
- newly created wetlands;
- player construction.

The intersecting layer owns the physical object. Migration owns observed response.

Possible responses:

- unchanged use;
- route compression;
- slower passage;
- faster passage;
- detour;
- increased stopover use;
- reduced stopover use;
- temporary hold;
- partial return;
- unknown response.

No response should be generated as a guaranteed formula from one infrastructure tag.

## 11. Migration timing

Seasonality owns expected timing.

Migration records actual timing.

```yaml
migration_timing_revision:
  migration_episode_id: null
  expected_window_ref: null
  first_confirmed_departure_at: null
  peak_movement_window: null
  last_confirmed_passage_at: null
  first_confirmed_arrival_at: null
  evidence_refs: []
```

A late or early event becomes a causal investigation only if a baseline exists.

## 12. Observation effort

Absence needs effort context.

```yaml
migration_monitoring_effort:
  effort_id: null
  station_or_route_ref: null
  migration_episode_id: null
  method_refs: []
  active_window: null
  coverage_band: null
  equipment_health_refs: []
  weather_constraints: []
  observer_refs: []
```

No detections during low coverage must not become `migration failed`.

## 13. Institutions and community practices

Ouros may later author:

- migration observatories;
- seasonal crossing stewards;
- village protection traditions;
- ferry/rail/road seasonal operating windows;
- research stations;
- volunteer count networks;
- temporary quiet/light restrictions;
- conservation closures;
- festivals synchronized to migration.

These practices belong to institutions/culture. The migration layer records their relationship to migration state.

## 14. Knowledge boundary

Different actors may know different route editions.

A farmer may know a reliable local crossing.
A regional atlas may contain a corridor that is five years out of date.
A researcher may know a stopover is declining.
A tourist guide may still advertise the old viewpoint.

Do not expose global migration state omnisciently.

## 15. Minecraft projection

Minecraft should visualize the current migration episode without becoming its source of truth.

Safe projection examples:

- temporary observation stations;
- signage and seasonal route closures;
- coarse groups moving through loaded regions;
- temporary camps;
- crowds at viewpoints;
- habitat state at stopovers.

Loaded entity count must never equal canonical population size.

Chunk unload/reload must not restart a migration wave or duplicate persistent Pokémon.

## 16. Cobblemon projection

A future adapter may use migration state to modify encounter availability or presence bands, but only through a controlled server projection.

Required anti-exploit rules:

- block placement cannot directly create a rare migration;
- repeated chunk reload cannot respawn the same canonical wave;
- player clock manipulation cannot trigger a new episode;
- capture of visible subgroup members cannot instantly rewrite population abundance;
- one sighting cannot promote a rare species into permanent local spawn tables.

## 17. Battle authority

Migration explains why combatants are present and what they may be trying to do.

AutoPTU remains authoritative for combat legality.

Migration does not create:

- free Shift;
- Sky/Swim/Burrow speed;
- Run Away effects;
- Pack Mon;
- swarm bonuses;
- interception;
- forced movement;
- terrain;
- weather;
- panic;
- morale;
- capture bonuses;
- initiative bonuses.

## 18. Encounter design rule

Every migration encounter should state:

1. migration episode and route context;
2. what world state changes if no battle occurs;
3. tactical participants only;
4. full implementation dependencies;
5. reduced version using currently safer capabilities;
6. post-battle world-state update that does not treat victory as ecological resolution.

## 19. Suggested migration story grammar

`baseline -> expected window -> observation effort -> first movement -> route/stopover choice -> disturbance or normal passage -> arrival/return -> institutional/public consequence -> post-season review`

Possible outcomes include:

- normal passage;
- route shift;
- temporary detour;
- stopover decline;
- new stopover use;
- partial migration;
- delayed movement;
- failed observation rather than failed migration;
- separation and reunion of a persistent individual;
- conservation or infrastructure response.

## 20. Hard non-inferences

Never infer:

- species appearance -> migratory behavior;
- migration -> aggression;
- migration -> swarm mechanics;
- flock -> Pack Mon;
- migration corridor -> ownership or protected status;
- road closure -> migration success;
- one crossing -> corridor health;
- missing annual observation -> extinction;
- late timing -> climate cause;
- north wind -> universal trigger;
- Pokémon alone -> abandoned;
- migrating former partner -> returning to old Trainer;
- Legendary sighting -> migration leader;
- Minecraft despawn -> departure;
- battle Fainted -> ecological death;
- battle withdrawal -> permanent route change.

## 21. Canon promotion gate

Before any specific migration becomes canon, review:

- species or population source support;
- regional geography;
- baseline/history;
- seasonality relationship;
- corridor and stopover evidence;
- interaction with existing settlements/infrastructure;
- conservation implications;
- persistent Pokémon identity implications;
- Cobblemon projection feasibility;
- PTU/Caelo movement/capture rules if tactical use is planned.