# Open Ocean, Oceanography & Pelagic Ecology Layer — Pass 87

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU/Caelo mechanic is established by this document.

## Purpose

This layer models persistent open-ocean physical and biological state between the existing Maritime, Fisheries, Reef, Estuary, Meteorology and Ecology systems.

Maritime remains authoritative for sea lanes, vessels, harbors and travel services.

Fisheries remains authoritative for fishing effort, catch observations and stock-management decisions.

Meteorology remains authoritative for atmospheric Weather and forecasts.

This layer owns coarse open-water state such as currents, fronts, water masses, stratification, upwelling, pelagic observation zones and drifting biological material.

It does not define tactical current movement, Swim rules, pressure, drowning, visibility, plankton mechanics, spawn rates or environmental damage.

## Core separation

Keep these separate:

- physical ocean region;
- current regime;
- water-mass identity;
- front position;
- vertical structure;
- upwelling/downwelling episode;
- biological observation;
- productivity interpretation;
- pelagic population/collective state;
- travel consequence;
- fishery consequence;
- tactical PTU state.

A cold front does not automatically create Ice Terrain.

A warm current does not automatically buff Water-types.

A productive front does not automatically increase encounter rolls.

A visible bloom does not automatically inflict Poisoned.

## OPEN_OCEAN_REGION

```yaml
open_ocean_region:
  ocean_region_id: null
  parent_maritime_region_refs: []
  coastal_region_refs: []
  estuary_refs: []
  reef_refs: []
  fishery_refs: []
  named_water_mass_refs: []
  current_regime_refs: []
  persistent_front_refs: []
  observation_network_refs: []
  seasonal_cycle_refs: []
  known_depth_band_refs: []
  current_revision_id: null
  canon_status: proposed
```

An ocean region is a coordination object. It does not imply jurisdiction, ownership or a mechanically homogeneous battlefield.

## OCEAN_STATE_REVISION

Open-ocean physical state changes through versioned revisions.

```yaml
ocean_state_revision:
  revision_id: null
  ocean_region_id: null
  valid_from: null
  valid_to: null
  surface_temperature_class: unknown
  mixed_layer_class: unknown
  stratification_class: unknown
  dominant_current_refs: []
  front_refs: []
  upwelling_refs: []
  bloom_observation_refs: []
  anomaly_refs: []
  source_observation_refs: []
  model_or_interpretation_refs: []
```

Suggested coarse classes should remain descriptive until a science subsystem defines stronger methods.

## CURRENT_REGIME

A current regime is persistent enough to be meaningful but is never treated as a fixed rail.

```yaml
current_regime:
  current_regime_id: null
  ocean_region_id: null
  name: null
  direction_class: unknown
  strength_class: unknown
  vertical_scope: surface|upper_water|deep|mixed|unknown
  seasonality_refs: []
  route_interaction_refs: []
  biological_observation_refs: []
  confidence: null
  observation_refs: []
  history_refs: []
```

Do not convert `strength_class` into forced-movement distance.

## WATER_MASS

```yaml
water_mass:
  water_mass_id: null
  ocean_region_refs: []
  temperature_class: unknown
  salinity_class: unknown
  depth_band_refs: []
  origin_claim_refs: []
  current_extent_revision_id: null
  observation_refs: []
  known_ecology_refs: []
```

Water masses let Ouros represent two nearby marine areas with different histories or biological observations.

This object does not create elemental typing or battle modifiers.

## OCEAN_FRONT

A front is a boundary/transition between water states, not a wall.

```yaml
ocean_front:
  front_id: null
  ocean_region_id: null
  front_type: thermal|salinity|density|current|mixed|unknown
  current_geometry_revision_id: null
  adjacent_water_mass_refs: []
  persistence_class: transient|seasonal|recurrent|persistent|unknown
  observation_refs: []
  biological_concentration_refs: []
  navigation_refs: []
  fishery_refs: []
  tourism_refs: []
```

The front can move, split, weaken or disappear without retconning previous observations.

## FRONT_GEOMETRY_REVISION

```yaml
front_geometry_revision:
  revision_id: null
  front_id: null
  valid_time: null
  coarse_geometry_ref: null
  confidence_band: null
  detection_method_refs: []
  source_refs: []
```

Do not require block-level precision.

A corridor or polyline with uncertainty is usually enough.

## VERTICAL_WATER_PROFILE

```yaml
vertical_water_profile:
  profile_id: null
  location_ref: null
  observation_time: null
  depth_bands:
    - band_id: surface
      temperature_class: unknown
      salinity_class: unknown
      oxygen_claim: unknown
      observation_refs: []
    - band_id: mixed_layer
      temperature_class: unknown
      salinity_class: unknown
      oxygen_claim: unknown
      observation_refs: []
    - band_id: thermocline
      depth_claim: unknown
      observation_refs: []
    - band_id: deeper_water
      temperature_class: unknown
      salinity_class: unknown
      oxygen_claim: unknown
      observation_refs: []
  confidence: null
```

The schema can store vertical structure even if battle remains a 2D frozen arena.

Do not infer pressure, visibility, Gilled requirements or damage from a depth label.

## STRATIFICATION_ASSESSMENT

```yaml
stratification_assessment:
  assessment_id: null
  ocean_region_or_station_ref: null
  assessment_time: null
  state: mixed|weakly_stratified|stratified|strongly_stratified|unknown
  evidence_refs: []
  method_ref: null
  interpretation_refs: []
  supersedes_ref: null
```

A stratified water column is not automatically unproductive.

Productivity remains an interpretation supported by biological and chemical observations.

## UPWELLING_EVENT

```yaml
upwelling_event:
  event_id: null
  ocean_region_id: null
  onset_time: null
  end_time: null
  geometry_ref: null
  driver_refs: []
  cold_water_observation_refs: []
  nutrient_observation_refs: []
  plankton_observation_refs: []
  fishery_response_refs: []
  wildlife_response_refs: []
  confidence: null
```

Possible drivers may include Meteorology or current state, but causality must remain evidence-based.

Upwelling does not directly write Cobblemon spawn probabilities.

## DOWNWELLING_EVENT

Use a separate record rather than assuming the inverse of upwelling in every respect.

```yaml
downwelling_event:
  event_id: null
  ocean_region_id: null
  onset_time: null
  end_time: null
  driver_refs: []
  observation_refs: []
  ecological_response_refs: []
```

## PELAGIC_HABITAT_ZONE

```yaml
pelagic_habitat_zone:
  habitat_zone_id: null
  ocean_region_id: null
  zone_type: surface|front|open_water|deep_scattering|nursery|feeding|migration|unknown
  current_geometry_revision_id: null
  observation_refs: []
  population_refs: []
  seasonal_refs: []
  front_or_current_refs: []
  disturbance_refs: []
```

A habitat zone is evidence-backed context. It is not a battle Zone.

## PLANKTON_SAMPLE

```yaml
plankton_sample:
  sample_id: null
  research_program_ref: null
  collection_time: null
  location_ref: null
  depth_band_ref: null
  method_ref: null
  sample_custody_ref: null
  classification_refs: []
  abundance_claims: []
  larval_identity_claims: []
  current_interpretation_refs: []
```

A sample from one tow does not define an ocean population.

## DRIFT_COHORT

This object supports drifting early-life stages or non-swimming biological material without simulating individuals.

```yaml
drift_cohort:
  drift_cohort_id: null
  origin_hypothesis_refs: []
  species_or_group_claim: null
  stage_claim: egg|larva|juvenile_planktonic|plankton|unknown
  first_observation_ref: null
  subsequent_observation_refs: []
  current_regime_refs: []
  destination_or_settlement_claim_refs: []
  confidence: null
```

Do not convert a drift cohort into exact future adult abundance.

## BLOOM_OBSERVATION

```yaml
bloom_observation:
  bloom_observation_id: null
  location_ref: null
  observation_time: null
  visual_claim: null
  sample_refs: []
  classification_ref: null
  extent_claim_ref: null
  transport_hypothesis_refs: []
  health_advisory_refs: []
  fishery_refs: []
  confidence: null
```

A visual discoloration is not automatically a harmful algal bloom.

A confirmed bloom is not automatically toxic.

A toxic bloom does not automatically create PTU Poisoned.

## OCEANOGRAPHIC_STATION

```yaml
oceanographic_station:
  station_id: null
  station_type: buoy|mooring|research_vessel_station|transect_point|remote_platform|shore_station|other
  ocean_region_id: null
  location_history_refs: []
  instrument_refs: []
  operator_refs: []
  service_state: operational|degraded|offline|lost|unknown
  observation_stream_refs: []
  calibration_refs: []
  incident_refs: []
```

A missing station creates uncertainty, not an ocean-state reset.

## TRANSECT

```yaml
oceanographic_transect:
  transect_id: null
  station_or_waypoint_refs: []
  repeat_schedule_ref: null
  research_program_ref: null
  historical_run_refs: []
  current_run_ref: null
  method_version_refs: []
```

Repeat transects are useful because the ocean moves while the sampling plan can remain comparable.

## OCEAN_ANOMALY

```yaml
ocean_anomaly:
  anomaly_id: null
  baseline_ref: null
  observation_refs: []
  anomaly_type: temperature|front_position|stratification|plankton|wildlife|current|mixed|unknown
  interpretation_refs: []
  cause_hypothesis_refs: []
  public_report_refs: []
  status: observed|under_review|explained|unresolved
```

Never jump from `unusual` to Legendary involvement.

## OPEN-OCEAN OBSERVATION PIPELINE

Recommended flow:

world physical state
→ instruments/field observation
→ observation record
→ interpretation/model
→ ecological/fishery/travel consequence
→ public communication
→ later verification

This keeps truth, evidence and public narrative separate.

## PELAGIC POKÉMON OBSERVATIONS

The system may record:

- Wailord sighting routes;
- Mantine/Remoraid associations;
- Mantyke behavior under different regional water conditions;
- Jellicent surface aggregations;
- unidentified large-school observations;
- tagged individual re-sightings;
- predator/prey events.

Do not infer:

- exact migration routes from one observation;
- species-wide behavior from one region;
- friendship/leadership from co-occurrence;
- battle AI from ecology;
- capture eligibility from tourism contact.

## WAILORD-WATCHING EVENT

```yaml
pelagic_tourism_event:
  event_id: null
  target_population_ref: null
  operator_refs: []
  route_ref: null
  observation_window_ref: null
  sighting_records: []
  visitor_pressure_ref: null
  conservation_refs: []
  public_memory_refs: []
```

A tour can be narratively successful even with no sighting if the event was run safely and honestly.

Do not guarantee wildlife contact.

## OPEN OCEAN -> MARITIME

Maritime can consume:

- current regime;
- front geometry;
- drift incident;
- current observation confidence;
- research-vessel station state.

Maritime remains authoritative for whether a service actually operates.

## OPEN OCEAN -> FISHERIES

Fisheries can consume:

- front/productivity observation;
- plankton samples;
- recruitment evidence;
- current regime;
- bloom advisories.

A stock assessment remains its own interpretation.

## OPEN OCEAN -> REEF / ESTUARY

Potential connections:

- larval transport hypothesis;
- water-mass temperature exposure;
- offshore bloom transport;
- nutrient supply;
- connectivity study.

Never declare connectivity from proximity alone.

## OPEN OCEAN -> METEOROLOGY

Meteorology can supply:

- wind event;
- storm mixing context;
- seasonal atmospheric pattern.

Open Ocean derives its own water response.

A windy day does not automatically create upwelling.

## OPEN OCEAN -> ASTRONOMY / SEASONALITY

Astronomy may provide observed lunar timing.

Seasonality may provide recurring windows.

Neither writes species behavior automatically.

## OPEN OCEAN -> HEALTH SURVEILLANCE

A confirmed health-relevant bloom can produce a surveillance signal or advisory.

This layer never creates disease, toxin damage, Poisoned or treatment rules.

## OPEN OCEAN -> COBBLEMON

Projection should be coarse and buffered.

Possible safe outputs:

- habitat presence class;
- broad observation opportunity class;
- migration window availability;
- research visual/event presentation;
- tagged persistent individual presence where canonically justified.

Do not map:

`front -> +30% rare spawn`

or

`upwelling -> spawn Wailord now`.

Anti-exploit principle:

Player-controlled local block placement, short boat movements or repeated chunk reloads must not directly control regional pelagic state.

## Minecraft projection

Minecraft may represent:

- buoy blocks/entities;
- research vessels;
- surface color/haze only when appropriate;
- floating sample equipment;
- observation UI;
- map overlays;
- Wailord-watching routes;
- coarse visual current cues;
- changing station states.

Minecraft is presentation and interaction.

The server-side ocean state remains authoritative.

## Tactical projection gate

Before battle starts, the adapter may request an `ocean_battle_snapshot`.

```yaml
ocean_battle_snapshot:
  source_ocean_revision_id: null
  source_location_ref: null
  frozen_geometry_ref: null
  verified_environment_effect_refs: []
  verified_current_effect_ref: null
  verified_visibility_effect_ref: null
  verified_depth_effect_ref: null
```

If a requested effect has no verified PTU/Java mechanic, it remains null.

The narrative description may still mention current, temperature or open sea visually.

## Encounter contract — Pelagic Front Survey

### Narrative premise

A research vessel follows a moving front where several Pokémon populations have been observed concentrating. A damaged sampling rig forces the team to stop at a less favorable position.

### FULL version requires

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including forced movement if current drift is tactical;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline as normal combat requires;
- terrain/weather/hazards/zones/reactions if the front/current creates field effects;
- move-specific behavior;
- abilities/items/Trainer Features when used;
- AI legal-action infrastructure;
- AI tactical policy for HOLD_POSITION/WITHDRAW/REACH_RIG objectives;
- Minecraft/Cobblemon/Craftics adapter/playback.

### REDUCED version

- the front and current remain overworld state;
- the research vessel selects a stable sampling position before battle;
- no current-driven movement occurs inside the grid;
- noncombatant crew and sampling gear remain outside tactical state;
- AutoPTU resolves a static legal encounter only if conflict actually occurs;
- research results update the ocean/front record afterward.

## Encounter contract — Drifting Buoy Recovery

### Narrative premise

A mooring breaks loose and begins drifting across a known current boundary. The challenge is first to locate it and determine what data remain trustworthy.

### FULL version requires

- complete movement if the buoy or actors move during combat;
- terrain/weather/hazards/zones/reactions for active current zones;
- AI tactical policy for retrieval/protection/withdrawal;
- adapter/playback;
- full lifecycle if field state changes by round.

### REDUCED version

- drift is resolved by world-state updates between scenes;
- Cartography/Science determines the search region;
- the buoy is stationary at the moment a battle starts;
- AutoPTU receives a static map;
- damaged data are reviewed after recovery rather than treated as automatically valid.

## Encounter contract — Open-Water Wildlife Aggregation

### Narrative premise

Multiple pelagic Pokémon gather near a productivity feature. Visitors and fishers also converge, increasing disturbance risk.

### FULL version requires

- complete movement/interception if groups move through the tactical area;
- terrain/weather/hazards/zones/reactions if current/front effects are mechanical;
- AI tactical policy for WITHDRAW/PROTECT/AVOID objectives;
- adapter/playback.

### REDUCED version

- tourism/fishing vessels are moved out of the combat perimeter first;
- most wildlife remains aggregate world state;
- only the individuals actually involved enter AutoPTU;
- no school-wide combat bonuses are created;
- after battle, population/collective records update from observed outcomes only.

## Permanent capability dependency map for this layer

### VERIFIED-compatible foundation

- targeting/footprints/range/LoS for static encounter geometry;
- base movement legality for already-supported movement modes;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

### PARTIAL dependencies

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

Use only specific implemented slices when required.

### BLOCKING families for FULL ocean encounters

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## Field-state progress does not equal ocean mechanics

AutoPTU-Java now owns duration-bearing terrain/zone/room entries and progresses them during authoritative ROUND_START.

That is useful infrastructure.

It does not prove:

- a `CURRENT` zone exists;
- current-induced forced movement exists;
- a `THERMOCLINE` effect exists;
- an `UPWELLING` field exists;
- water temperature modifies combat;
- ocean visibility exists;
- underwater depth exists;
- pelagic AI exists;
- a Minecraft ocean can initialize battle field state safely.

## PTU/Caelo guardrails

Before promoting mechanics, verify exact rules for:

- Swim;
- Gilled;
- Maelstrom Features;
- water traversal;
- underwater combat;
- drowning/suffocation if present;
- water-based Terrain or Weather;
- forced movement/current interactions if any;
- capture/escape in aquatic encounters;
- movement between depth/elevation states if supported.

No narrative label can substitute for those rules.

## Canon questions intentionally unresolved

- Which named currents exist in Ouros?
- Are current systems global, regional or both?
- Which areas have recurring upwelling?
- What institutions operate research vessels and moorings?
- Which pelagic species have authored migration or aggregation behavior?
- Which populations support tourism or fisheries before player arrival?
- How should depth bands be represented in world state?
- Does Ouros use only coarse 2D battles at sea, or eventually support vertical aquatic states?
- How much ocean state advances offline?
- How does the server prevent local player actions from exploiting pelagic spawn projections?
- Which bloom/toxin systems, if any, exist in canon?
- Which PTU/Caelo aquatic rules are inherited without modification?
