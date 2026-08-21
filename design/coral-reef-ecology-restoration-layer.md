# Ouros Coral Reef Ecology & Restoration Layer

Status: proposed systems design. Not established Ouros canon.

Pass: 82.

## Purpose

This layer gives coral reefs persistent identity and history across Maritime, Conservation, Fisheries, Tourism, Water Quality, Meteorology, Science, Photography, Wild Collectives and Minecraft projection.

`design/maritime-coasts-depths-layer.md` remains authoritative for maritime regions, sea lanes, underwater access, vessels and generic marine habitats. This layer owns reef-specific structure, condition, disturbance and restoration state.

It does not define PTU Swim rules, underwater visibility, reef terrain costs, coral cover, heat damage, bleaching mechanics, currents, drowning, capture rules, spawning bonuses or Minecraft fluid physics.

## 1. Reef identity

A reef must persist independently of its current visual state.

```yaml
reef_system:
  reef_id: null
  maritime_region_id: null
  parent_habitat_id: null
  approved_name: null
  known_aliases: []
  zone_ids: []
  structural_revision_ids: []
  condition_observation_ids: []
  disturbance_event_ids: []
  restoration_project_ids: []
  stewardship_ids: []
  fishery_refs: []
  tourism_refs: []
  water_quality_refs: []
  current_projection_revision_id: null
```

A reef does not stop being the same reef because part of it bleaches, collapses, is restored or becomes covered by rubble.

## 2. Internal reef zones

Useful coarse zones include:

- REEF_FLAT
- CREST
- LAGOON
- CHANNEL
- PATCH_REEF
- OUTER_SLOPE
- DEEP_EDGE
- RUBBLE_FIELD
- NURSERY_AREA
- RESTORATION_PLOT
- SHELTERED_POOL
- CURRENT_EDGE

These are ecological/spatial labels only. They do not imply PTU Terrain.

```yaml
reef_zone:
  reef_zone_id: null
  reef_id: null
  zone_type: null
  geometry_ref: null
  depth_band: null
  exposure_profile_ref: null
  structural_state_ref: null
  observation_station_ids: []
  population_refs: []
  collective_refs: []
  access_refs: []
  current_condition_summary: unknown
```

## 3. Structural revision

Physical complexity changes independently from biological condition.

```yaml
reef_structural_revision:
  revision_id: null
  reef_id: null
  effective_from_event_id: null
  source_observation_ids: []
  zone_structure: {}
  coarse_complexity_by_zone: {}
  rubble_state_by_zone: {}
  known_breakage_ids: []
  known_stable_structure_ids: []
  minecraft_projection_ref: null
  confidence: null
```

Possible coarse complexity states:

- VERY_LOW
- LOW
- MODERATE
- HIGH
- VERY_HIGH
- UNKNOWN

Do not turn complexity directly into cover, Evasion or movement cost.

## 4. Reef-condition observations

Observation and interpretation remain separate.

```yaml
reef_condition_observation:
  observation_id: null
  reef_id: null
  reef_zone_id: null
  observed_at: null
  observer_ids: []
  method_ref: null
  raw_record_refs: []
  condition_type: null
  observed_value: null
  uncertainty: null
  provenance_refs: []
```

Candidate condition types:

- LIVING_COVER
- PALE_COLORATION
- BLEACHING_OBSERVATION
- RECENT_MORTALITY_OBSERVATION
- RECRUITMENT
- RUBBLE_COVER
- MACROALGAE_OBSERVATION
- STRUCTURAL_COMPLEXITY
- SEDIMENT_DEPOSITION
- WATER_CLARITY
- DISEASE_LIKE_SIGNS
- RESTORATION_COHORT_SURVIVAL

A `BLEACHING_OBSERVATION` does not automatically establish cause.

## 5. Stress exposure

Stress belongs to environmental state and observations, not to a universal reef-health meter.

```yaml
reef_stress_exposure:
  exposure_id: null
  reef_id: null
  affected_zone_ids: []
  exposure_type: null
  source_system_refs: []
  start_ref: null
  end_ref: null
  observed_intensity: null
  predicted_intensity: null
  evidence_ids: []
  biological_response_ids: []
```

Candidate exposure types:

- MARINE_HEAT
- EXTREME_COLD
- SEDIMENT_PULSE
- FRESHWATER_PULSE
- WATER_QUALITY_CHANGE
- STORM_WAVE_ENERGY
- VESSEL_GROUNDING
- ANCHOR_DAMAGE
- CONSTRUCTION_DISTURBANCE
- VISITOR_PRESSURE
- DISEASE_EVENT
- UNKNOWN

Do not convert an exposure into PTU damage or Status.

## 6. Disturbance events

```yaml
reef_disturbance_event:
  disturbance_id: null
  reef_id: null
  event_type: null
  start_event_id: null
  end_event_id: null
  affected_zone_ids: []
  source_claim_ids: []
  verified_cause_refs: []
  structural_delta_refs: []
  biological_observation_refs: []
  access_change_refs: []
  recovery_project_refs: []
```

A vessel grounding can have a known physical cause while biological consequences remain under observation.

## 7. Recruitment and recovery

Recovery needs history.

```yaml
reef_recruitment_observation:
  recruitment_id: null
  reef_id: null
  zone_id: null
  observation_date: null
  taxon_or_species_ref: null
  count_or_index: null
  method_ref: null
  substrate_context_ref: null
  source_ids: []
```

Recruitment may rise, fall or remain uncertain independently of visible adult cover.

Do not create Pokémon Eggs, breeding state or PTU nursery mechanics from coral recruitment terminology.

## 8. Restoration project

```yaml
reef_restoration_project:
  project_id: null
  reef_id: null
  institution_ids: []
  approved_goal: null
  baseline_refs: []
  target_zone_ids: []
  intervention_ids: []
  cohort_ids: []
  maintenance_schedule_refs: []
  monitoring_plan_refs: []
  funding_refs: []
  permit_refs: []
  incident_ids: []
  current_state: PLANNED
  outcome_assessment_ids: []
```

Candidate states:

- PROPOSED
- PLANNED
- ACTIVE
- PAUSED
- MONITORING
- REVISED
- COMPLETED
- DISCONTINUED

`COMPLETED` means project work ended. It does not mean ecological recovery succeeded.

## 9. Restoration intervention

```yaml
reef_restoration_intervention:
  intervention_id: null
  project_id: null
  intervention_type: null
  performed_at: null
  zone_id: null
  material_or_cohort_refs: []
  operator_ids: []
  provenance_refs: []
  immediate_result_refs: []
  followup_observation_ids: []
```

Possible design categories:

- STRUCTURE_STABILIZATION
- DEBRIS_REMOVAL
- SUBSTRATE_PREPARATION
- CORAL_OUTPLANT
- NURSERY_TRANSFER
- ALGAL_MANAGEMENT
- ACCESS_RESTRICTION
- VISITOR_REDIRECTION
- WATER_QUALITY_UPSTREAM_ACTION
- MONITORING_ONLY

These are project categories. They do not grant PTU effects.

## 10. Coral/restoration cohorts

If Ouros authors coral propagation or analogous reef-organism restoration, provenance should persist.

```yaml
restoration_cohort:
  cohort_id: null
  source_site_refs: []
  source_record_ids: []
  nursery_site_id: null
  preparation_history_ids: []
  transfer_history_ids: []
  outplant_location_refs: []
  followup_observation_ids: []
  current_status: unknown
```

Never use lineage/provenance as a purity or value score.

## 11. Reef complexity and habitat use

Structural state can affect where wild collectives are observed without forcing a deterministic spawn table.

Example causal chain:

storm damage → reduced shelter complexity in one zone → survey detects different habitat use → ecology review → controlled Cobblemon projection after validation.

Loaded entity count must never become the reef-population truth.

## 12. Species relationships

Species interactions should be stored as observations or evidence-backed ecological relations.

Example:

```yaml
reef_species_interaction:
  interaction_id: null
  reef_id: null
  zone_id: null
  actor_population_refs: []
  observed_behavior: null
  condition_refs: []
  observation_ids: []
  interpretation_ids: []
  confidence: null
```

A documented Toxapex/Bruxish conflict at a warm-current edge may become local knowledge.

Do not infer:

- universal hostility;
- automatic battle pairing;
- territorial bonuses;
- species-wide social structures;
- predator/prey status where the evidence only shows competition.

## 13. Corsola boundary

Corsola can support reef stories as a Pokémon species, individual or population.

Possible state:

- repeated observation at one reef;
- absence from a historically documented station;
- juvenile recruitment observations;
- partnership with a Trainer;
- persistent individual identity;
- rehabilitation/release history;
- public symbolic importance.

Do not infer reef health from Corsola alone.

Do not create Galarian Corsola, extinction, Ghost typing or a historical catastrophe unless explicitly authored in Ouros canon.

## 14. Heat stress and bleaching

Marine heat should come from a physical/environmental source system.

Proposed flow:

Meteorology/ocean condition → heat-stress observation/forecast → reef monitoring → bleaching observations → review → public communication → management action.

A heat-stress warning can exist before bleaching is observed.

Bleaching can be patchy.

Bleaching does not equal death.

Recovery after bleaching is not guaranteed.

No stage creates tactical Burned, damage or Weather by narrative implication.

## 15. Water quality and sediment

Water Quality and Freshwater/Coastal layers remain authoritative for pollutant/sediment source state.

This layer records reef exposure and response.

Possible chain:

upstream construction → sediment event → plume reaches reef → observation stations record deposition → recruitment changes later → investigation.

Do not assign guilt from spatial coincidence alone.

## 16. Fisheries relationship

Fisheries manages fishing effort, catch ledgers, stock assessment and management.

Reef ecology may provide:

- habitat-use evidence;
- spawning/recruitment observations;
- structural context;
- restoration zones;
- access/stewardship overlaps.

A healthier-looking reef does not automatically raise fishery yield.

## 17. Tourism and recreation

Tourism manages visitor flows and destination pressure.

Reef-specific visitor state may include:

- dive/snorkel site usage;
- anchoring pressure;
- guide routes;
- temporary closures;
- education programs;
- photography hotspots;
- restoration volunteer access.

Visitor popularity does not establish ecological damage by itself.

## 18. Photography and visual evidence

Photomosaics and repeated visual surveys can become `VISUAL_RECORD` derivatives linked to reef stations.

Image appearance does not replace structural or biological assessment.

A beautiful screenshot can be genuine while its caption is wrong.

## 19. Science integration

A reef program can support:

- permanent transects;
- repeated photo stations;
- temperature loggers;
- recruitment panels where canon supports them;
- water-quality observations;
- restoration cohort monitoring;
- species behavior surveys;
- null results.

Science remains allowed to conclude that a suspected trend is unsupported.

## 20. Public memory

A reef can accumulate public history:

- old navigation charts;
- famous dive photographs;
- storm scars;
- restoration anniversaries;
- fishing closures;
- disputed development decisions;
- memorials after maritime incidents;
- recovered wreck history.

Public reputation can lag behind ecological state.

## 21. Minecraft projection

The server-owned reef revision should drive Minecraft presentation.

Possible visual projection:

- coarse coral/rock geometry;
- rubble patches;
- restored frames/markers;
- survey stakes/buoys;
- selected reef Pokémon entities;
- boats and dive stations;
- temporary closure markers;
- pale/healthy visual variants when assets support them;
- restoration plots.

The adapter must not derive PTU effects from block palette.

A chunk reload must never restore an obsolete reef revision.

## 22. Performance policy

Do not simulate every coral colony.

Use coarse persistent state for:

- reef zones;
- structural revisions;
- condition observations;
- restoration cohorts;
- wild populations/collectives;
- disturbance history.

Materialize only interaction-relevant entities and geometry.

## 23. Anti-exploit policy

Players must not be able to farm rare spawns by repeatedly placing/removing coral-like blocks, lighting the area, moving rubble or toggling restoration decorations.

Required pipeline:

player action → validated world-state change → ecological review/state update → bounded population projection → Cobblemon materialization.

## 24. Encounter contract — Broken Crest Survey

Narrative premise:

After a storm, researchers need to document a damaged reef crest while wild Pokémon continue using the surviving channels.

FULL version:

- mixed Swim/static-platform movement;
- reef channels as meaningful geometry;
- current/wave zones if authoritative;
- objective `SURVEY_POINTS` / `REACH_EXIT`;
- wild AI that may defend, avoid or withdraw based on actual state;
- fragile zones that players should avoid damaging if a verified mechanic exists;
- semantic writeback to reef observations.

Capability dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED for current static Swim/Shift surface
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if current/displacement matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version:

The server freezes a safe reef revision before combat. Survey interaction occurs before/after the battle. Reef walls are static blockers. No current, wave, fragile-coral penalty, objective AI or dynamic terrain exists inside the grid. AutoPTU handles only a conventional battle among actual combatants.

## 25. Encounter contract — Nursery Transfer Interruption

Narrative premise:

A restoration team is moving a documented reef-restoration cohort between facilities when an unrelated wild disturbance blocks the route.

FULL version:

- protected cargo/cohort objective;
- route-clear or withdrawal goals;
- mobile noncombatant team;
- interception/forced movement where rules support it;
- environmental zones only if authoritative;
- AI aware of objective and retreat.

Dependency emphasis:

- complete movement/forced movement/interception: BLOCKING
- terrain/weather/hazards/zones/reactions: BLOCKING
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- items: PARTIAL only if a real PTU item is used; restoration containers themselves are world-state assets, not battle items.

REDUCED version:

The restoration cohort and staff remain off-grid. The players clear one static chokepoint using normal battle rules. After the result, the world-state system resumes or aborts the transfer and preserves cohort provenance.

## 26. Encounter contract — Warm-Current Boundary

Narrative premise:

Repeated Toxapex/Bruxish conflict at one reef edge has increased after a local current pattern shifted. Players are asked to observe first and intervene only if a real safety problem develops.

FULL version:

- current boundary represented as an authoritative battlefield zone;
- multi-faction wild AI with territorial/withdrawal goals derived from observed local state;
- current-dependent movement only if rules exist;
- non-KO outcomes such as separation or withdrawal;
- behavior writeback to the reef ecology graph.

REDUCED version:

The current boundary remains world state only. Observation determines whether a conventional battle occurs. If it does, the arena is static; no species receives territorial, current or reef bonuses. The result is recorded separately from the ecological interpretation.

## 27. Mechanical boundary

Before any FULL reef encounter is executable, validate exact PTU/Caelo behavior for:

- Swim and underwater movement;
- breathing/Gilled if applicable;
- underwater visibility and LoS;
- water/depth terrain costs;
- currents and forced movement if any;
- cover or obstruction from reef geometry;
- environmental damage;
- Weather at sea;
- hazards/zones;
- capture while swimming;
- retreat/escape;
- relevant Moves/Abilities/Features;
- item/equipment use underwater.

Python AutoPTU has specific `ocean`/`wetlands` feature behavior and movement capability checks. Those exact implementations do not establish a generic reef mechanic or Java parity.

## 28. Canon promotion checklist

Before a reef proposal becomes canon:

1. Reef location and region geography are approved.
2. Species populations are approved.
3. Historical disturbances are approved.
4. Restoration/stewardship institutions are approved.
5. Fishing/tourism overlaps are reviewed.
6. Water-quality and heat-stress dependencies are explicit.
7. PTU/Caelo mechanics required by executable encounters are validated.
8. AutoPTU-Java capability evidence is current.
9. Cobblemon projection cannot be exploited for spawn manipulation.
10. No external reef community, project or culture has been copied into Ouros.

## 29. Current implementation posture

World-state work can advance immediately:

reef identity, zones, observations, structural versions, disturbance history, restoration projects, cohorts, science records, tourism/fishery overlaps and Minecraft visual revision planning.

Mechanically rich underwater encounters must continue using FULL/REDUCED contracts until the blocking engine families are implemented and parity-tested.
