# Groundwater, Aquifers, Wells & Springs Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon. No PTU mechanical effect is created here.

Pass: 109

## Purpose

This layer deepens the groundwater side of `freshwater-watersheds-hydrology-layer.md` without replacing it.

Freshwater owns catchments, surface reaches, reservoirs, wetlands, and the explicit connection graph between surface water and groundwater. Geology owns substrate and aquifer-forming material. This layer owns groundwater storage state, recharge, wells, pumping, drawdown, springs, monitoring, travel-time claims, and groundwater-specific investigations.

Sanitation owns waste systems. Stormwater owns urban runoff networks. Estuaries owns coastal salinity systems. Aridity and Cryosphere can change recharge conditions. Agriculture, settlements, clinics, industry, and conservation may depend on groundwater but do not become the source of truth for it.

## Core separation

Never collapse these into one state:

- aquifer physical identity;
- groundwater level/storage revision;
- recharge event or recharge-area claim;
- well infrastructure;
- pumping/withdrawal event;
- spring discharge observation;
- water-quality sample;
- groundwater-flow interpretation;
- contaminant-source hypothesis;
- public guidance;
- Minecraft water blocks;
- PTU battlefield water/Terrain/Weather/hazard state.

A well is not an aquifer.

A spring is not a proof of the aquifer’s full extent.

A wet Minecraft cave is not automatically a groundwater system.

## 1. Groundwater system

```yaml
groundwater_system:
  groundwater_system_id: null
  name: null
  region_ids: []
  geology_context_ids: []
  freshwater_system_ids: []
  aquifer_unit_ids: []
  recharge_zone_ids: []
  discharge_zone_ids: []
  well_field_ids: []
  spring_ids: []
  monitoring_network_ids: []
  historical_state_refs: []
  canon_status: proposed
```

A groundwater system is a planning/observation identity. Its mapped extent can be revised without creating a new system.

## 2. Aquifer unit

```yaml
aquifer_unit:
  aquifer_unit_id: null
  groundwater_system_id: null
  geometry_revision_ids: []
  confinement_class: unknown
  geology_refs: []
  known_connection_edges: []
  storage_state_revision_ids: []
  water_quality_profile_refs: []
  interpretation_refs: []
```

Candidate confinement labels can remain qualitative until canon requires more detail:
- UNCONFINED
- PARTLY_CONFINED
- CONFINED
- PERCHED
- FRACTURED_ROCK
- KARST
- UNKNOWN

These labels do not create PTU terrain or movement rules.

## 3. Groundwater state revision

```yaml
groundwater_state_revision:
  revision_id: null
  aquifer_unit_id: null
  effective_from: null
  effective_to: null
  level_class: unknown
  storage_trend: unknown
  confidence: null
  observation_refs: []
  model_refs: []
  supersedes_revision_id: null
```

Suggested coarse level/trend states are narrative abstractions, not numeric simulation:
- VERY_HIGH
- HIGH
- TYPICAL
- LOW
- VERY_LOW
- UNKNOWN

Trend:
- RISING
- STABLE
- FALLING
- VARIABLE
- UNKNOWN

Do not calculate every cubic meter. Exact numerical models can exist only where useful and authored.

## 4. Recharge zone and recharge event

```yaml
recharge_zone:
  recharge_zone_id: null
  aquifer_unit_ids: []
  geometry_revision_ids: []
  land_unit_ids: []
  surface_water_connection_ids: []
  soil_unit_ids: []
  recharge_mechanism_claims: []
  sensitivity_notes: []
  source_refs: []
```

```yaml
recharge_event:
  recharge_event_id: null
  aquifer_unit_ids: []
  source_type: rainfall|snowmelt|river_loss|wetland|irrigation_return|managed_recharge|other
  source_event_ref: null
  started_at: null
  ended_at: null
  observed_or_inferred: inferred
  lag_claim_refs: []
  quantity_class: unknown
  quality_refs: []
```

Rainfall over an aquifer does not mean immediate recharge.

A recharge event may be observed indirectly through later level, spring, or chemistry changes.

## 5. Groundwater well

```yaml
groundwater_well:
  well_id: null
  location_id: null
  aquifer_unit_claim_ids: []
  operator_actor_ids: []
  purpose: monitoring|settlement_supply|agriculture|industry|research|emergency|other
  physical_state: operational|degraded|offline|abandoned|unknown
  permission_refs: []
  pump_asset_id: null
  screen_or_intake_context_ref: null
  historical_name_refs: []
  observation_ids: []
  withdrawal_event_ids: []
  sample_ids: []
```

A well being operational means only that the physical access point can function. It does not prove water quality, sustainable yield, authority to pump, or availability to all users.

## 6. Withdrawal / pumping event

```yaml
groundwater_withdrawal_event:
  withdrawal_event_id: null
  well_id: null
  started_at: null
  ended_at: null
  use_ref: null
  rate_or_class: null
  meter_or_observation_refs: []
  linked_drawdown_assessment_ids: []
```

Routine pumping can be aggregated by day/week/season rather than emitted as thousands of events.

## 7. Drawdown and well interference

```yaml
drawdown_assessment:
  assessment_id: null
  aquifer_unit_id: null
  pumping_event_refs: []
  observation_refs: []
  affected_well_or_spring_ids: []
  spatial_claim_ref: null
  confidence: null
  alternative_hypothesis_ids: []
```

Possible observed symptoms:
- declining water level;
- slower well recovery;
- spring discharge decrease;
- intermittent well failure;
- changed connection to a wetland or stream;
- increased pumping time.

None establishes pumping as cause without evidence.

Two users can affect one another without either actor acting maliciously.

## 8. Spring / seep

```yaml
groundwater_spring:
  spring_id: null
  location_id: null
  groundwater_system_claim_ids: []
  freshwater_system_ids: []
  discharge_observation_ids: []
  chemistry_observation_ids: []
  seasonal_profile_ref: null
  capture_or_infrastructure_ids: []
  ecological_dependency_ids: []
  cultural_use_refs: []
  current_access_state: unknown
```

A spring can be:
- perennial;
- seasonal;
- intermittent;
- newly observed;
- historically known but currently dry;
- redirected/captured by infrastructure;
- geothermal only when Volcanism/Geology support that claim.

No spring is automatically healing water.

## 9. Monitoring network

```yaml
groundwater_monitoring_network:
  network_id: null
  operator_actor_ids: []
  observation_point_ids: []
  active_periods: []
  data_gap_records: []
  calibration_refs: []
  coverage_assessment_refs: []
```

Sparse network coverage must remain visible in the uncertainty model.

`NOT_DETECTED` at one monitoring well does not mean `ABSENT_FROM_AQUIFER`.

## 10. Groundwater observation

```yaml
groundwater_observation:
  observation_id: null
  observed_at: null
  observation_point_id: null
  observer_or_sensor_id: null
  observation_type: water_level|spring_discharge|temperature|conductivity|chemistry|visual|pump_response|other
  raw_value_ref: null
  quality_flag: null
  method_ref: null
  source_refs: []
```

Water-quality observations remain observations. Health Surveillance or Sanitation may consume them but does not rewrite them.

## 11. Groundwater flow / travel-time claim

```yaml
groundwater_flow_claim:
  claim_id: null
  aquifer_unit_id: null
  source_zone_id: null
  destination_zone_or_well_id: null
  direction_claim: null
  travel_time_range_claim: null
  evidence_refs: []
  model_refs: []
  confidence: null
  superseded_by: null
```

A travel-time claim is a model/interpretation, not a scheduled courier route.

Use it to support delayed causal possibilities without pretending subsurface movement is perfectly known.

## 12. Groundwater quality case

Groundwater quality investigations should use Science/Case patterns rather than `contaminated=true` shortcuts.

```yaml
groundwater_quality_case:
  case_id: null
  groundwater_system_id: null
  initial_signal_refs: []
  monitoring_well_ids: []
  affected_use_refs: []
  source_hypothesis_ids: []
  plume_revision_ids: []
  sample_ids: []
  current_assessment_ref: null
  health_surveillance_refs: []
  sanitation_refs: []
  public_guidance_refs: []
```

Potential source hypotheses may include:
- surface infiltration;
- leaking infrastructure;
- historic industrial source;
- agricultural input;
- saline intrusion;
- natural geology/mineral source;
- sampling/analytical issue;
- unknown.

Do not infer criminal action from contamination.

## 13. Groundwater plume revision

```yaml
groundwater_plume_revision:
  plume_revision_id: null
  case_id: null
  mapped_or_modeled_extent_ref: null
  effective_at: null
  evidence_refs: []
  uncertainty_notes: []
  supersedes: null
```

The plume map can change because the plume moved, because new monitoring wells were added, or because the model improved. Chronicle should preserve which explanation is known.

## 14. Managed recharge / underground storage

```yaml
managed_recharge_project:
  project_id: null
  aquifer_unit_id: null
  source_water_refs: []
  recharge_asset_ids: []
  operating_window_refs: []
  monitoring_plan_refs: []
  recharge_event_ids: []
  recovery_well_ids: []
  quality_review_ids: []
  current_status: proposed|pilot|active|paused|completed|review
```

A successful injection/infiltration event does not prove successful long-term storage or safe later use.

## 15. Surface-water handoff

Freshwater remains authoritative for surface reaches.

Example chain:

```text
winter snowpack
→ spring snowmelt
→ infiltration/recharge event
→ aquifer level rises after lag
→ spring discharge increases
→ freshwater reach gains baseflow
→ wetland remains connected later into dry season
→ ecological observations change
```

Each arrow needs a validated connection or hypothesis. Do not skip directly from snow to Pokémon spawn changes.

## 16. Coastal handoff

Estuaries owns salinity fronts and coastal wetland state.

Groundwater can provide:
- fresh groundwater discharge;
- well drawdown observations;
- saline groundwater observations;
- seawater-intrusion hypotheses.

Estuaries/coastal systems consume those outputs. This layer does not simulate tides.

## 17. Geology / cave / volcanism handoff

Geology owns aquifer material and fractures.

Cave Ecology owns mapped cave space.

Volcanism owns geothermal system state.

A cave stream may intersect an aquifer but is not identical to it. A warm spring becomes geothermal only when the evidence supports that link.

## 18. Minecraft projection

Minecraft is a renderer/projection client for groundwater state.

Possible presentation:
- wells and pumps;
- spring outlets;
- dry or wet basins;
- monitoring huts;
- sampling equipment;
- recharge basins;
- cave seep visuals;
- changed vegetation near springs;
- public advisory boards.

Hard rules:
- loaded water blocks do not set aquifer storage;
- filling a hole with water does not recharge an aquifer automatically;
- breaking a block does not create a new spring unless world-state logic validates a pathway;
- an unloaded chunk does not freeze aquifer time;
- players cannot manufacture rare ecology by repeatedly placing/removing water.

## 19. Encounter implementation contracts

### Wellfield Access After Storm — FULL

Premise:
A storm damages access near monitoring wells while a groundwater-quality investigation is already underway. The objective is to reach designated sampling points without turning samples or technicians into generic HP objectives.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED for normal battle targeting
- base movement legality: VERIFIED for static movement
- complete movement/interception/forced movement: BLOCKING for true moving technicians, route protection or forced displacement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if floodwater, unstable ground or protected sampling zones become tactical mechanics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `REACH_SAMPLE_POINT`, `WITHDRAW`, `PROTECT_TECHNICIAN`
- Minecraft/Cobblemon/Craftics playback: BLOCKING

Reduced version:
Resolve access, stormwater, technician movement and sampling in overworld state. Freeze one safe/static arena if combat remains. Battle outcome does not determine groundwater-quality findings.

### Dry Spring Survey — FULL

Premise:
A historically reliable spring stops flowing. Several wild Pokémon still use the surrounding habitat, while the investigation compares drought, pumping, geology and infrastructure hypotheses.

Dependencies:
The environmental investigation itself needs no special battle mechanic. A rich combat version would require tactical withdrawal AI and potentially terrain/zones if spring geometry changes during combat; those are BLOCKING.

Reduced version:
Survey the spring and nearby wells in world state. If a conflict occurs, use one static arena and keep all hydrological conclusions outside battle.

### Recharge Basin Night Watch — FULL

Premise:
A pilot recharge project attracts wildlife during a scheduled operating window. The goal is operational safety and observation, not defeating everything present.

Dependencies:
- complete movement/interception/forced movement: BLOCKING for moving wildlife corridors
- terrain/weather/hazards/zones/reactions: BLOCKING if water level changes dynamically or the basin creates tactical zones
- AI tactical policy: BLOCKING for `WITHDRAW`, `AVOID_ZONE`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics playback: BLOCKING
- ordinary static combat primitives remain usable at current VERIFIED/PARTIAL scope

Reduced version:
Pause the recharge operation, resolve wildlife movement in world state, freeze the basin state, and open a static battle only if a distinct confrontation remains.

## 20. Hard non-inferences

Do not infer:
- well water -> safe drinking water;
- well water -> healing;
- spring -> healing spring;
- visible water -> aquifer;
- cave pool -> regional groundwater storage;
- rainfall -> immediate recharge;
- drought -> every well fails;
- low well -> aquifer exhausted;
- contaminated well -> known contaminant source;
- contamination -> Poisoned;
- groundwater flow -> underground current hazard;
- Water-type Pokémon -> groundwater detector;
- Ground-type Pokémon -> aquifer access;
- Groundshaper -> permission to create wells or springs;
- pump -> infinite water;
- aquifer recharge -> instant ecological recovery;
- Minecraft water placement -> aquifer mutation;
- battle victory -> water-rights or scientific conclusion.

## 21. New overworld blockers

These belong outside AutoPTU-Java:

- `GROUNDWATER_SYSTEM_IDENTITY`
- `AQUIFER_UNIT_GEOMETRY_HISTORY`
- `GROUNDWATER_STORAGE_STATE`
- `RECHARGE_ZONE_AND_EVENT_STATE`
- `GROUNDWATER_WELL_STATE`
- `WITHDRAWAL_AND_DRAWDOWN_HISTORY`
- `SPRING_DISCHARGE_HISTORY`
- `GROUNDWATER_MONITORING_NETWORK`
- `GROUNDWATER_OBSERVATION_PROVENANCE`
- `GROUNDWATER_FLOW_TRAVEL_TIME_CLAIMS`
- `GROUNDWATER_QUALITY_CASE_GRAPH`
- `GROUNDWATER_PLUME_REVISION_HISTORY`
- `MANAGED_RECHARGE_PROJECT_STATE`
- `GROUNDWATER_TO_FRESHWATER_HANDOFF`
- `GROUNDWATER_TO_ESTUARY_HANDOFF`
- `GROUNDWATER_TO_SANITATION_HEALTH_HANDOFF`
- `GROUNDWATER_TO_MINECRAFT_PROJECTION`
- `GROUNDWATER_TO_FROZEN_BATTLE_SNAPSHOT`

## Mechanical/canon questions

- Which Ouros regions depend materially on groundwater?
- Which aquifers, springs, and well fields exist before campaign start?
- Which wells are public, institutional, household, agricultural, industrial, or research infrastructure?
- Who operates monitoring networks?
- Which springs have cultural meaning, and which claims about them are fact versus tradition?
- How coarse should groundwater storage be for offline simulation?
- Which surface-water/groundwater links are authored versus discovered through play?
- Can player construction materially alter recharge, or only through reviewed projects?
- How should coastal aquifers interact with the existing salinity layer?
- What exact PTU/Caelo rules govern Groundshaper, Survival, Water/ground sensing, environmental exposure, Swim, and underground water hazards?

The full primary Caelo corpus was not reliably accessible in this run. Super PTU Online Helper was not exposed as an invokable capability. No mechanics were invented from either source.