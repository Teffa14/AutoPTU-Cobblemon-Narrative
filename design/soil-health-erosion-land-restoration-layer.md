# Ouros Soil Health, Erosion & Land Restoration Layer

Status: proposed systems design. Not established canon.

## Purpose

This layer gives Ouros persistent state for soil, surface condition, erosion, compaction and land restoration.

It bridges existing Agriculture, Freshwater, Wildfire, Cryosphere, Volcanism, Conservation, Geology, Architecture and Travel systems.

It does not define PTU terrain rules, farming yields, environmental damage, Groundshaper behavior, Survival checks or Minecraft physics.

## 1. Core separation

Never collapse these concepts:

```yaml
soil_system_boundary:
  geological_substrate_id: null
  soil_land_unit_id: null
  current_observation_ids: []
  condition_assessment_ids: []
  erosion_event_ids: []
  compaction_event_ids: []
  restoration_project_ids: []
  agricultural_use_ids: []
  habitat_state_ids: []
  battle_projection_id: null
```

Geology answers what material and formation underlie the site.

Soil state answers what has developed or been disturbed near the surface.

Agriculture answers how people use the land.

Freshwater owns water-system state.

AutoPTU owns any actual tactical terrain effects.

## 2. Soil land unit

Use coarse management/ecological units rather than one record per Minecraft block.

```yaml
soil_land_unit:
  soil_unit_id: null
  location_id: null
  geometry_ref: null
  parent_substrate_refs: []
  land_use_refs: []
  habitat_refs: []
  agricultural_site_ids: []
  freshwater_link_ids: []
  infrastructure_overlap_ids: []
  wildfire_patch_ids: []
  cryosphere_link_ids: []
  volcanic_deposit_ids: []
  heritage_context_ids: []
  current_condition_revision_id: null
  observation_ids: []
  restoration_project_ids: []
  public_disclosure_state: normal
```

Recommended unit scales:

- one orchard block;
- one field management zone;
- one trail segment;
- one riverbank reach;
- one construction lot;
- one burn-scar patch;
- one wetland access zone;
- one restoration plot.

A unit can be split later if evidence shows materially different conditions.

## 3. Soil condition revision

Do not represent soil with one quality score.

```yaml
soil_condition_revision:
  revision_id: null
  soil_unit_id: null
  effective_at: null
  physical_state:
    compaction_state: unknown
    infiltration_state: unknown
    structure_state: unknown
    surface_cover_state: unknown
    sealing_state: unknown
    depth_state: unknown
    moisture_context: unknown
  chemical_state:
    nutrient_claim_state: unknown
    salinity_claim_state: unknown
    contamination_ref_ids: []
  biological_state:
    organic_matter_claim_state: unknown
    biological_activity_claim_state: unknown
  erosion_state:
    source_risk_state: unknown
    active_feature_refs: []
  recorder_ids: []
  evidence_ids: []
  supersedes_revision_id: null
```

These are assessment fields, not PTU modifiers.

A site can be fertile but compacted. It can be structurally stable but nutrient-poor. It can have healthy vegetation while an impermeable layer remains below.

## 4. Soil observations

Observations should preserve method and context.

```yaml
soil_observation:
  observation_id: null
  soil_unit_id: null
  observed_at: null
  observer_ids: []
  method: null
  observation_type: null
  measured_value: null
  measurement_unit: null
  moisture_context: null
  weather_context_id: null
  sampling_depth_band: null
  sample_object_ids: []
  image_record_ids: []
  notes: null
  confidence: null
  provenance_refs: []
```

Candidate observation types:

- SURFACE_COVER
- RUTTING
- PONDING
- INFILTRATION
- BULK_DENSITY
- PENETRATION_RESISTANCE
- SOIL_DEPTH
- STRUCTURE
- ORGANIC_MATTER
- ROOTING_PATTERN
- EROSION_RILL
- GULLY
- DEPOSITION
- CRUSTING
- SALINITY_SIGNAL
- CONTAMINATION_SIGNAL
- BIOLOGICAL_ACTIVITY

The exact methods and thresholds need authored/scientific data if they become gameplay requirements.

## 5. Observation is not diagnosis

```yaml
soil_condition_assessment:
  assessment_id: null
  soil_unit_id: null
  based_on_observation_ids: []
  assessor_ids: []
  physical_condition_claims: []
  chemical_condition_claims: []
  biological_condition_claims: []
  limiting_factor_claims: []
  alternative_explanations: []
  confidence: null
  review_due_at: null
```

Examples:

- ponding may support a compaction hypothesis;
- poor crop growth may support several competing explanations;
- bare ground may be seasonal, disturbed, degraded or intentionally maintained;
- lush vegetation may hide deeper compaction or contamination.

The generator should preserve uncertainty rather than choose the most dramatic explanation.

## 6. Compaction event

```yaml
compaction_event:
  event_id: null
  soil_unit_ids: []
  started_at: null
  ended_at: null
  pressure_source_type: null
  source_actor_or_asset_ids: []
  traffic_intensity_state: null
  wet_condition_overlap: null
  observation_ids: []
  causal_assessment_ids: []
  mitigation_ids: []
  consequence_ids: []
```

Candidate sources:

- CONSTRUCTION_TRAFFIC
- FESTIVAL_FOOT_TRAFFIC
- TOURISM_PRESSURE
- AGRICULTURAL_EQUIPMENT
- TRANSPORT_REROUTE
- WORKPLACE_OPERATIONS
- EMERGENCY_STAGING
- REPEATED_TRAINER_USE
- UNKNOWN

A traffic event does not automatically mean harmful compaction occurred.

## 7. Erosion and sediment transfer

Erosion source and sediment destination are different records.

```yaml
erosion_event:
  erosion_event_id: null
  source_soil_unit_ids: []
  trigger_event_ids: []
  observed_start_at: null
  erosion_form: null
  current_activity_state: null
  material_claim_refs: []
  observation_ids: []
  cause_hypothesis_ids: []
  sediment_transfer_ids: []
  stabilization_project_ids: []
```

```yaml
sediment_transfer_event:
  transfer_id: null
  source_erosion_event_id: null
  transport_path_refs: []
  destination_ids: []
  freshwater_event_ids: []
  deposition_observation_ids: []
  infrastructure_impact_ids: []
  habitat_impact_assessment_ids: []
```

Candidate erosion forms:

- SHEET
- RILL
- GULLY
- BANK
- WIND
- TRAIL
- CONSTRUCTION_EXPOSURE
- POST_FIRE
- UNKNOWN

Minecraft particles or exposed dirt blocks cannot create these records automatically without server-side causal validation.

## 8. Surface stability assessment

This supports Travel and Crisis without inventing tactical hazards.

```yaml
surface_stability_assessment:
  assessment_id: null
  location_or_route_id: null
  soil_unit_ids: []
  evaluated_at: null
  evaluator_ids: []
  intended_use: null
  safe_access_state: unknown
  restrictions: []
  observation_ids: []
  weather_context_ids: []
  expiration_condition: null
```

Suggested access states:

- UNKNOWN
- OPEN
- OPEN_WITH_LIMITS
- TEMPORARILY_CLOSED
- REASSESSMENT_REQUIRED

This is overworld route eligibility. It grants no PTU movement modifier by itself.

## 9. Pokémon–soil interaction

```yaml
soil_pokemon_interaction:
  interaction_id: null
  pokemon_entity_ids: []
  species_refs: []
  soil_unit_ids: []
  observed_at: null
  behavior_type: null
  direct_observation_ids: []
  resulting_change_observation_ids: []
  ecological_interpretation_ids: []
  agricultural_interpretation_ids: []
  infrastructure_interpretation_ids: []
  mechanical_capability_refs: []
  mechanical_validation_state: pending
```

Candidate behavior types:

- BURROWING
- FORAGING
- NEST_BUILDING
- ORGANIC_INPUT
- SEED_DISPERSAL
- ROOT_DISTURBANCE
- SURFACE_TRAMPLING
- UNKNOWN

Species lore may suggest a plausible observation target. It does not prove that every individual is currently performing that role.

## 10. Restoration project

```yaml
land_restoration_project:
  project_id: null
  soil_unit_ids: []
  sponsor_ids: []
  steward_ids: []
  scientific_partner_ids: []
  current_phase: proposed
  target_condition_claims: []
  intervention_refs: []
  access_management_refs: []
  monitoring_plan_ids: []
  baseline_observation_ids: []
  followup_observation_ids: []
  ecological_project_ids: []
  freshwater_project_ids: []
  public_works_ids: []
  completion_claim_ids: []
```

Suggested phases:

- PROPOSED
- BASELINING
- ACTIVE
- STABILIZING
- MONITORING
- ADAPTIVE_REVIEW
- COMPLETED
- SUSPENDED

Completion should mean the project's authored objectives were met, not that every soil property returned to an imaginary pristine state.

## 11. Restoration is a trajectory

A project may improve one indicator while another lags.

Examples:

- surface cover returns before infiltration improves;
- erosion slows but sediment already deposited downstream remains;
- a trail closure reduces pressure but changes visitor flow elsewhere;
- a burn scar stabilizes but vegetation composition changes;
- a former field becomes habitat rather than returning to agriculture.

Chronicle should preserve baseline and follow-up versions.

## 12. Agriculture integration

Agriculture may query soil state for narrative planning.

It may ask:

- is the field currently accessible?
- is there evidence of compaction?
- is a restoration project active?
- is an irrigation problem actually a soil-infiltration problem?
- does a research plot have a known baseline?

Agriculture may not turn those answers into invented Berry yields, growth rates or Food Buffs.

## 13. Freshwater integration

Use explicit causal edges:

```text
soil cover change
-> erosion observation
-> sediment transfer
-> freshwater observation
-> ecological/infrastructure assessment
```

Do not infer downstream damage merely because erosion occurred upstream.

## 14. Wildfire integration

Wildfire owns burn severity and fire history.

Soil may receive references to:

- loss of cover;
- ash/debris deposition;
- post-fire erosion observations;
- stabilization projects;
- later rainfall responses.

A burn patch does not automatically become degraded soil.

## 15. Cryosphere integration

Cryosphere owns snow, ice, freeze/thaw and glacier state.

Soil records resulting observations such as:

- surface heave;
- thaw-related rutting;
- seasonal infiltration change;
- exposed former ground;
- new erosion features.

No ice or mud mechanic follows automatically.

## 16. Volcanism integration

Volcanism owns ash/tephra and geothermal events.

Soil can version:

- new deposits;
- developing organic layer;
- altered drainage observations;
- restoration or agricultural trials.

Fresh volcanic material is not automatically fertile.

## 17. Architecture, public works and travel

Construction projects should optionally preserve:

- topsoil removal/stockpile state;
- sealed surface extent;
- machinery traffic area;
- restoration requirement;
- post-construction monitoring.

Travel/tourism can consume route-surface assessments rather than infer safety from block type.

## 18. Archaeology and context preservation

Soil can be part of provenance.

```yaml
soil_context_link:
  context_link_id: null
  soil_unit_id: null
  horizon_or_depth_label: null
  archaeological_context_id: null
  fossil_context_id: null
  disturbance_state: null
  observation_ids: []
```

Removing an object can destroy context even when the object remains intact.

## 19. Minecraft projection

Minecraft may render validated state with coarse visual cues:

- ruts;
- exposed soil;
- recovery vegetation;
- erosion scars;
- stabilized paths;
- stockpiles;
- fencing/closures;
- sampling markers.

Loaded blocks are presentation state.

They must not independently decide:

- soil condition;
- erosion cause;
- fertility;
- route safety;
- agricultural yield;
- PTU terrain.

## 20. Battle projection boundary

```yaml
soil_to_battle_projection:
  projection_id: null
  source_soil_revision_ids: []
  battle_location_id: null
  authored_mechanical_terrain_refs: []
  rules_validation_refs: []
  engine_capability_requirements: []
  frozen_at_battle_start: true
```

If no exact validated PTU terrain/effect exists, the battle receives ordinary static geometry.

Narrative labels such as `muddy`, `eroded`, `compacted`, `loose`, `ash-rich` or `fertile` remain presentation only.

## 21. PTU / AutoPTU guardrails

Project evidence contains narrow terrain rules and capability behavior.

Python AutoPTU has a specific `Mold the Earth` path requiring the Trainer Feature plus Groundshaper. It can alter ground and place Spikes under that exact implementation.

This layer cannot call that mechanic because a site was excavated, eroded or farmed.

Naturewalk also remains authoritative individual capability state.

Never generate from soil state alone:

- Rough Terrain;
- Slow Terrain;
- Spikes;
- Accuracy modifiers;
- fall/slip checks;
- damage;
- Tripped;
- Ground-type bonuses;
- Groundshaper;
- Naturewalk;
- movement penalties;
- crop bonuses;
- healing;
- status conditions.

## 22. Encounter contract — Hillside Survey After Rain

Narrative premise:

A hillside route develops new rills after heavy rain. Surveyors need to establish whether the public path can reopen while wild Pokémon continue using the slope.

Full version dependencies:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. forced movement/interception — BLOCKING if gullies or sliding alter position
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL if exact effects exist
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for withdraw/avoid-zone behavior
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:

Survey erosion outside battle. Resolve route access in world state. Freeze one mapped stable platform if combat occurs. Rills and mud have no tactical effect. Run a conventional static encounter only with real combatants.

## 23. Encounter contract — Orchard Compaction Study

Narrative premise:

An orchard's outer rows show ponding after a season of transport and festival traffic. Researchers and growers disagree about whether traffic, drainage or another cause dominates.

Full version dependencies:

- static targeting/base movement/core/initiative — VERIFIED
- dynamic muddy/compacted zones — BLOCKING under terrain/weather/hazards/zones/reactions
- movement around protected sample plots — BLOCKING if objective zones/reactions matter
- lifecycle/damage/status/Abilities/items/Features — PARTIAL as applicable
- tactical AI — BLOCKING for protect/avoid/interact goals
- adapter/playback — BLOCKING

Reduced version:

Sampling, traffic closure and drainage investigation remain overworld state. If battle occurs, fields and instruments remain outside the grid and the fight uses a static service lane.

## 24. Encounter contract — Sediment Fan Reopening

Narrative premise:

A storm moves material from an eroding slope onto a route near a stream. Teams must determine which corridor is stable enough to reopen.

Full version dependencies:

- targeting/base movement/core/initiative — VERIFIED
- sediment/debris zones — BLOCKING under terrain/hazards/zones
- displacement or collapse-driven movement — BLOCKING under complete movement
- lifecycle — PARTIAL if conditions evolve by round
- tactical AI — BLOCKING for route/withdraw objectives
- adapter/playback — BLOCKING

Reduced version:

Freshwater + Soil assessment selects a safe corridor before battle. One static arena is frozen. No automatic Slow/Rough Terrain, displacement or damage comes from the sediment label.

## 25. Implementation blockers outside battle core

- `OVERWORLD_SOIL_LAND_UNIT_STATE`
- `OVERWORLD_SOIL_CONDITION_VERSIONING`
- `OVERWORLD_SOIL_OBSERVATION_PROVENANCE`
- `OVERWORLD_EROSION_SEDIMENT_GRAPH`
- `OVERWORLD_COMPACTION_HISTORY`
- `OVERWORLD_LAND_RESTORATION_PROJECTS`
- `OVERWORLD_SOIL_TO_AGRICULTURE`
- `OVERWORLD_SOIL_TO_FRESHWATER`
- `OVERWORLD_SOIL_TO_COBBLEMON`
- `OVERWORLD_SOIL_TO_BATTLE`
- `OVERWORLD_SOIL_TO_MINECRAFT`

These belong to server-owned world state, not AutoPTU-Java combat internals.

## 26. Canon questions

Before promotion, Ouros still needs authored answers for:

- which regions have intensive agriculture, fragile slopes or heavily used trails;
- which sites already carry historic land degradation or restoration;
- what institutions conduct soil surveys;
- which restoration practices exist locally;
- how land stewardship and access decisions work;
- which Pokémon–soil relationships are canonical by region;
- how much soil information players can publish or keep private;
- what exact PTU/Caelo Skills, Features or capabilities govern field assessment;
- which battlefield terrain effects are actually legal and implemented.

Until those questions are resolved, soil state enriches causal worldbuilding without becoming a second rules engine.
