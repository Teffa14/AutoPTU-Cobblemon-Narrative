# Ouros Migration, Stopover and Temporal Niche Contract

Status: PROPOSED DESIGN
Date: 2026-09-03
Ecology programme: Pass 235

## Purpose

Represent recurring and condition-driven Pokémon movement through the Ouros world without replacing persistent population truth with seasonal spawn-table swaps.

This contract governs ecology-level movement before structured battle.

## Authority boundary

Migration is an Ouros world-state process.

```text
persistent population truth
-> migration eligibility and timing
-> route/corridor/stopover state
-> local activity and availability
-> native Cobblemon/Minecraft projection
-> observation and intervention
-> explicit Ouros handoff if tactical mechanics begin
-> AutoPTU semantic outcome
-> persistent migration/population state
```

Minecraft/Cobblemon may present actors and native habitat facts. They do not decide whether a population migrated, how many members exist, or whether a seasonal cohort was created/destroyed.

## Migration entity

```yaml
migration_state:
  id: null
  population_id: null
  cohort_id: null
  mode: null
  annual_or_recurrence_key: null
  origin_range_id: null
  destination_range_id: null
  route_id: null
  current_segment_id: null
  phase: PREPARING
  baseline_departure_window: null
  actual_departure_time: null
  expected_arrival_window: null
  actual_arrival_time: null
  diel_activity_window: null
  route_fidelity: null
  progress_fraction: 0.0
  condition_summary: null
  deviation_reason_refs: []
  observation_refs: []
  provenance_refs: []
```

Allowed phases:
- `PREPARING`
- `DEPARTING`
- `TRANSIT`
- `STOPOVER`
- `ARRIVING`
- `SEASONAL_RESIDENCE`
- `RETURN_TRANSIT`
- `COMPLETED`
- `DEVIATED`
- `FAILED`

`FAILED` means the expected movement did not complete. It does not imply death unless separately established by population truth.

## Route graph

```yaml
migration_route:
  id: null
  origin_range_id: null
  destination_range_id: null
  segment_ids: []
  stopover_site_ids: []
  alternate_route_ids: []
  directionality: null
  recurrence: null
  physical_constraints: []
  seasonal_constraints: []
  diel_constraints: []
  provenance_refs: []
```

A route segment must refer to real world geography once the global world is locked. Before that, semantic placeholders are allowed only in proposals and fixtures.

## Stopover contract

A stopover is an ecological resource node, not a save point.

```yaml
stopover_state:
  site_id: null
  time_window: null
  shelter_capacity: null
  food_resource_capacity: null
  water_resource_capacity: null
  disturbance_pressure: null
  predator_pressure: null
  artificial_attraction_pressure: null
  occupancy_pressure: null
  recovery_value: null
  degradation_refs: []
```

Arrival creates local demand. Demand can reduce resources, increase visible density and alter resident behavior. These effects must flow through the normal resource/ecology contracts.

## Departure pressure

Departure is not a fixed timer.

Candidate factors:

```text
baseline timing tendency
+ current condition
+ resource recovery achieved
+ resource trend
+ weather suitability
+ disturbance/threat pressure
+ reproductive/life-stage pressure
+ route congestion
+ group cohesion/leader state
+ daylight/diel window
= departure pressure
```

This is an ecology policy score. It is not initiative, action economy or tactical movement.

## Temporal niche

Temporal niche controls when a population or cohort tends to use habitat or move through it.

Candidate windows:
- dawn
- day
- dusk
- night
- weather-conditioned subwindow
- seasonal window
- breeding window
- resource-triggered window

A temporal niche can alter activity/projection pressure while population truth remains unchanged.

## Cohort integrity

Large moving groups may be represented as cohorts, but aggregation cannot erase persistent named individuals.

Rules:
- named/story-relevant members retain identity references;
- cohort count cannot exceed the source population ledger;
- splitting creates child cohort records referencing the same source population allocation;
- merging reconciles member allocations before deleting temporary cohort records;
- generic Cobblemon actors projected from a cohort cannot become extra population members by existence alone.

## Route fidelity and learning

Populations or individuals may have route memory.

Candidate fields:

```yaml
route_memory:
  owner_id: null
  preferred_route_ids: []
  known_stopover_ids: []
  successful_passages: 0
  failed_passages: 0
  learned_avoidance_refs: []
  confidence: null
```

Route fidelity is allowed to change after disturbance or successful alternates. It must not become omniscient pathfinding.

## Disturbance and ecological traps

A site can be attractive and harmful simultaneously.

Therefore:

```text
high local presence != high habitat quality
```

Artificial light, concentrated food, human structures or other attractors can increase arrival/occupancy while lowering recovery or increasing risk.

## Observation boundary

Players and NPCs receive evidence, not migration truth directly.

Possible observations:
- unusual directional flight/movement;
- repeated arrival at similar times;
- marked individuals seen at multiple sites;
- temporary resource depletion;
- tracks/droppings/feeding signs;
- abrupt silence after departure;
- institutional counts or ranger reports;
- missing expected arrivals.

Knowledge confidence depends on observation quality and information channels.

## Cobblemon projection

Migration can influence which native-compatible actors become visible locally.

Projection eligibility still requires:

```text
real world coordinate/biome facts
+ Cobblemon native spawn envelope
+ Ouros population/cohort presence
+ current activity/exposure state
+ temporal/weather conditions
= candidate visible projection
```

Migration never authorizes projection into an incompatible native habitat without an explicit authored exception reviewed under the source authority policy.

## Encounter handoff

### World-state only

Examples:
- observe a passing cohort;
- protect a stopover from traffic;
- document delayed arrival;
- restore a resource;
- reroute NPC travel;
- compare counts between stations.

AutoPTU dependency: none.

### Reduced supported battle variant

Narrative premise:
- the migration/stopover remains the reason the encounter exists;
- Ouros freezes or abstracts cohort transit while a local subset enters structured battle;
- only explicit combatants enter AutoPTU;
- after battle, semantic outcome updates disturbance, route confidence, condition or departure pressure.

Use only currently verified foundations plus explicitly supported slices.

### Full rich variant

Possible features and exact dependency categories:

- moving escort objective: complete movement including interception/forced movement — PARTIAL;
- multi-wave or timed crossing: full turn/round lifecycle — PARTIAL;
- injury/attrition effects: full stateful damage pipeline — PARTIAL;
- fatigue/status interactions: status lifecycle — PARTIAL;
- wind, rain, hazardous crossing tiles or defended corridors: terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING;
- species-specific travel Moves: move-specific behavior — PARTIAL;
- travel-relevant Abilities: abilities — PARTIAL;
- consumable rescue/support gear: items — PARTIAL;
- Trainer interrupts/commands: Trainer Features/perks — PARTIAL;
- autonomous flee/escort/protect-route objectives: AI tactical policy — BLOCKING;
- faithful visible movement and semantic writeback: Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL/BLOCKING.

Targeting/footprints/range/LoS, base movement legality, core calculations, action economy/initiative and AI legal-action infrastructure remain the currently verified broad foundations from the project readiness snapshots.

## Required persistence effects

A completed migration may update:
- seasonal range occupancy;
- stopover resource pressure;
- local resident activity;
- route memory/fidelity;
- disturbance history;
- observation records;
- NPC institutional knowledge;
- breeding/nesting eligibility at destination;
- later return-route timing.

A battle result cannot directly rewrite these without semantic translation through Ouros.

## Validation invariants

1. No population duplication during origin-to-destination transfer.
2. Named individuals retain identity through cohort aggregation.
3. A local projection cannot outlive cohort/population presence without an explicit persistence reason.
4. Stopover use consumes/affects real ecology state, not cosmetic counters only.
5. Route deviation has a cause or is explicitly stochastic within species/population policy.
6. Weather affecting migration does not automatically instantiate tactical weather.
7. Observation does not grant omniscient route knowledge.
8. Generic Minecraft/Cobblemon spawning cannot fabricate migration truth.

## Implementation sequence after world lock

1. bind semantic ranges and corridors to real coordinates and biome tags;
2. verify native spawn compatibility for candidate migratory species;
3. create one population/cohort ledger fixture;
4. simulate one departure, one stopover and one arrival without tactical battle;
5. verify no duplication across projection boundaries;
6. add observation packets and institutional reports;
7. add one reduced AutoPTU handoff;
8. add richer mechanics only when capability families are verified.

## Unresolved design questions

- Maximum cohort aggregation size before spatial approximation becomes misleading.
- Whether condition is tracked per member, distribution bucket or cohort summary for generic individuals.
- How multiple migrating populations compete for the same stopover resource.
- How route-memory inheritance works for juveniles.
- How far NPC institutions can infer route continuity from sparse observations.
- How world border/pregeneration limits interact with long-distance routes.
