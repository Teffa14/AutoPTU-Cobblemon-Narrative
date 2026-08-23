# Ouros Climate Baselines, Long-Term Change & Adaptation Layer

Status: PROPOSED SYSTEMS DESIGN. Not established canon.
Date: 2026-08-23

## Purpose

Ouros already has authorities for calendar, seasonality, observed weather, forecasts, measurement quality and many climate-sensitive environmental systems. This layer owns the longer temporal question: how a region understands persistent change across years or decades.

Its job is to preserve dated baselines, anomaly comparisons, trend assessments, attribution claims, vulnerability assessments, scenario sets and adaptation decisions without rewriting the original observations or creating battle rules.

## Relationship to existing layers

This layer extends rather than replaces:

- `seasonality-calendar-phenology-layer.md` for recurring annual cycles and phenological windows;
- `meteorology-forecasting-weather-layer.md` for actual weather and forecasts;
- `metrology-calibration-measurement-standards-layer.md` for instrument traceability and comparability;
- `science-research-discovery-layer.md` for datasets, hypotheses, analysis and publications;
- `cryosphere-snowpack-glacier-freeze-thaw-layer.md` for snow/glacier state;
- `freshwater-watersheds-hydrology-layer.md` and `groundwater-aquifers-wells-springs-layer.md` for water state;
- `wildfire-fire-ecology-landscape-recovery-layer.md` for fire history;
- `aridity-drought-desert-ecology-layer.md` for drought/arid state;
- `coastal-geomorphology-shoreline-dunes-layer.md`, `estuaries-tidal-wetlands-salinity-layer.md`, `coral-reef-ecology-restoration-layer.md` and `open-ocean-oceanography-pelagic-ecology-layer.md` for marine/coastal responses;
- `alpine-mountain-elevation-zonation-layer.md` and `forest-canopy-vertical-ecology-layer.md` for elevation/vegetation structure;
- `flora-pollination-seed-dispersal-layer.md`, `diel-activity-circadian-rhythms-layer.md` and `wildlife-migration-stopovers-corridors-layer.md` for biological timing/behavior;
- `urban-heat-microclimate-thermal-comfort-layer.md` for local urban thermal state;
- `travel-transport-expedition-layer.md`, `technology-energy-infrastructure-layer.md`, `civic-governance-public-works-layer.md`, `demography-migration-population-change-layer.md` and `tourism-visitors-destination-pressure-layer.md` for human responses.

The climate layer references authoritative outputs from those systems. It does not duplicate them.

## Core authority separation

```text
raw observations in owning systems
        ↓
measurement / method / coverage validation
        ↓
indicator series
        ↓
versioned climate baseline
        ↓
anomaly comparisons
        ↓
trend assessment
        ↓
attribution claims / competing explanations
        ↓
vulnerability assessment
        ↓
scenario set
        ↓
adaptation decision
        ↓
domain-specific implementation
        ↓
long-term review
```

Battle state is downstream and separate:

```text
long-term climate assessment
        X
        └── does NOT create battle Weather/Terrain/Status

current authoritative world condition
        ↓
PTU/Caelo mechanics eligibility
        ↓
AutoPTU battle state
```

## 1. Climate region

```yaml
climate_region:
  climate_region_id: null
  spatial_scope_ref: null
  public_name: null
  nested_region_ids: []
  indicator_series_ids: []
  baseline_ids: []
  assessment_ids: []
  active_scenario_set_ids: []
  adaptation_plan_ids: []
  source_refs: []
```

A climate region is an analytical scope. It does not need to match a political region, biome, settlement or battle map.

## 2. Climate indicator series

The climate layer should normally link to observations owned elsewhere rather than copy them.

```yaml
climate_indicator_series:
  series_id: null
  climate_region_id: null
  indicator_type: null
  source_authority_layer: null
  source_series_ref: null
  temporal_resolution: null
  spatial_resolution: null
  method_revision_ids: []
  coverage_summary: null
  quality_flags: []
  comparable_from: null
  comparable_until: null
  notes: []
```

Candidate indicator types may include:

- AIR_TEMPERATURE
- PRECIPITATION
- EXTREME_HEAT_FREQUENCY
- FROST_WINDOW
- SNOW_COVER_DURATION
- GLACIER_TERMINUS_POSITION
- STREAMFLOW_TIMING
- GROUNDWATER_LEVEL
- LAKE_TURNOVER_TIMING
- BLOOM_DATE
- TREELINE_POSITION
- MIGRATION_ARRIVAL_WINDOW
- FIRE_SEASON_LENGTH
- SHORELINE_POSITION
- REEF_HEAT_STRESS_EXPOSURE
- URBAN_NIGHT_HEAT

These labels are observational categories, not mechanics.

## 3. Versioned climate baseline

```yaml
climate_baseline:
  baseline_id: null
  climate_region_id: null
  indicator_series_id: null
  reference_period_start: null
  reference_period_end: null
  baseline_method_ref: null
  issued_at: null
  issuer_id: null
  quality_state: null
  coverage_state: null
  baseline_values_ref: null
  supersedes_baseline_id: null
  source_refs: []
```

Rules:

1. A baseline is a dated analytical product.
2. Publishing a new baseline does not delete the old one.
3. Old reports retain their original baseline references.
4. The same observation can have several anomaly values against different baselines.
5. No fixed 30-year duration is assumed for Ouros until canon defines institutional practice.

## 4. Anomaly record

```yaml
climate_anomaly_record:
  anomaly_id: null
  observation_or_period_ref: null
  baseline_id: null
  indicator_type: null
  anomaly_value_or_band: null
  calculation_method_ref: null
  interpretation_state: DESCRIPTIVE
  created_at: null
  source_refs: []
```

An anomaly is a comparison. It is not automatically evidence of a trend and does not mean the observed condition was hazardous.

## 5. Trend assessment

```yaml
climate_trend_assessment:
  assessment_id: null
  climate_region_id: null
  indicator_series_ids: []
  assessed_period_start: null
  assessed_period_end: null
  method_ref: null
  trend_direction: null
  magnitude_band: null
  confidence: null
  limitations: []
  competing_assessment_ids: []
  issued_at: null
  issuer_id: null
  source_refs: []
```

Possible descriptive directions:

- INCREASING
- DECREASING
- SHIFTING_EARLIER
- SHIFTING_LATER
- MORE_VARIABLE
- LESS_VARIABLE
- NO_CLEAR_TREND
- INSUFFICIENT_DATA

Do not fabricate numerical significance thresholds unless an Ouros institution defines them.

## 6. Attribution claims remain claims

```yaml
climate_attribution_claim:
  claim_id: null
  observed_change_ref: null
  proposed_driver_refs: []
  evidence_refs: []
  counterevidence_refs: []
  confidence: null
  claimant_id: null
  published_at: null
  review_state: OPEN
  supersedes_claim_id: null
```

Possible drivers can coexist:

- wider climate change;
- local land-use change;
- urbanization;
- altered monitoring method;
- station relocation;
- hydrological engineering;
- vegetation change;
- natural variability;
- wildfire legacy;
- volcanic aerosol episode;
- unknown.

Never infer cause from temporal coincidence alone.

## 7. Regime-shift case

Some systems can move into a persistently different state. That deserves an explicit case rather than a silent flag flip.

```yaml
climate_regime_shift_case:
  shift_case_id: null
  subject_system_refs: []
  previous_state_summary: null
  candidate_new_state_summary: null
  first_signal_date: null
  evidence_series_ids: []
  threshold_claim_ids: []
  persistence_requirement: null
  current_assessment: SUSPECTED
  review_history: []
```

Suggested assessment states:

- SUSPECTED
- UNDER_REVIEW
- SUPPORTED
- DISPUTED
- NOT_SUPPORTED
- REVERSED_OR_TRANSIENT

Examples that could eventually qualify only after evidence:

- a snow-dependent route ceases to form in most winters;
- a lake’s turnover timing persistently shifts;
- a marsh changes hydroperiod regime;
- an established migration stopover loses its historical timing window.

The owning domain still controls the physical state.

## 8. Historical climate knowledge

Chronicle should preserve what institutions believed at each time.

```yaml
climate_knowledge_revision:
  revision_id: null
  climate_region_id: null
  valid_from: null
  public_summary_ref: null
  baseline_ids: []
  trend_assessment_ids: []
  attribution_claim_ids: []
  uncertainty_notes: []
  superseded_at: null
```

A guidebook published twenty years ago can be internally consistent with the data available then and later become obsolete without becoming fraudulent.

## 9. Vulnerability profile

```yaml
climate_vulnerability_profile:
  vulnerability_id: null
  subject_refs: []
  climate_exposure_refs: []
  sensitivity_refs: []
  adaptive_capacity_refs: []
  dependency_refs: []
  confidence: null
  current_priority_band: null
  assessed_at: null
  assessor_ids: []
  source_refs: []
```

The profile should link to domain facts instead of generating them.

Examples:

- a ferry route exposed to more frequent low-water closures;
- a settlement dependent on one spring;
- a festival tied to a phenological event;
- a research station dependent on seasonal ice access;
- a reef-restoration project exposed to repeated heat-stress windows.

No single vulnerability score is required.

## 10. Scenario sets are planning tools

```yaml
climate_scenario_set:
  scenario_set_id: null
  climate_region_id: null
  created_at: null
  time_horizon: null
  scenario_ids: []
  assumptions_ref: null
  uncertainty_summary: null
  intended_use: PLANNING
  source_refs: []
```

```yaml
climate_scenario:
  scenario_id: null
  scenario_set_id: null
  label: null
  parameter_bands: []
  downstream_assumption_refs: []
  probability_claim: null
  status: PLAUSIBLE
```

Rules:

- a scenario is not prophecy;
- several scenarios can be retained simultaneously;
- a player cannot “discover the future” merely because a planning document exists;
- scenario assumptions cannot write future Chronicle events directly.

## 11. Adaptation plans

```yaml
climate_adaptation_plan:
  adaptation_plan_id: null
  subject_refs: []
  vulnerability_id: null
  scenario_set_id: null
  goal_refs: []
  action_ids: []
  decision_authority_ids: []
  adopted_at: null
  review_window: null
  status: PROPOSED
```

```yaml
climate_adaptation_action:
  adaptation_action_id: null
  plan_id: null
  action_type: null
  implementation_layer: null
  implementation_ref: null
  intended_function: null
  trigger_conditions: []
  tradeoff_claim_ids: []
  monitoring_ref: null
  status: PLANNED
```

Possible actions belong to their real system:

- move a trail → Travel/Public Works;
- raise or replace infrastructure → Architecture/Public Works;
- change seasonal staffing → Workplaces/Emergency Services;
- alter restoration target → Conservation/relevant ecology layer;
- add shade → Urban Heat/Public Space;
- diversify water source → Drinking Water/Groundwater/Freshwater;
- revise festival timing → Festivals/Seasonality;
- change crop schedule → Food/Phenology.

The climate layer records why the action was selected and reviews the long-term outcome.

## 12. Adaptation review

```yaml
climate_adaptation_review:
  review_id: null
  adaptation_action_id: null
  reviewed_at: null
  observed_outcome_refs: []
  expected_outcome_refs: []
  unintended_effect_refs: []
  still_fit_for_purpose: null
  recommendation: null
  source_refs: []
```

Successful adaptation may mean maintaining a function while the physical state changes. It does not require restoring a historical snapshot.

## 13. Quiet progression is mandatory

Long-term change must not become a quest generator that constantly interrupts players.

Routine progression may produce:

- annual monitoring updates;
- a revised baseline;
- a route schedule shifting by a few days;
- a species observation moving slightly in elevation;
- an infrastructure maintenance standard changing;
- a festival planner selecting an earlier contingency date;
- no actionable player content at all.

Create playable content only when a decision, conflict, investigation, relationship, expedition or meaningful tradeoff exists.

## 14. Climate and Pokémon

A Pokémon can participate in climate evidence through:

- repeated observations;
- distribution history;
- phenology;
- migration timing;
- habitat use;
- historical photographs;
- museum specimens;
- field-sign records.

Protections:

- climate trend does not create a regional form;
- climate trend does not change Types, Abilities, stats or Moves;
- climate trend does not trigger evolution;
- climate trend does not prove extinction or local extirpation;
- climate trend does not force migration;
- a species known to respond to climate elsewhere does not prove the same response in Ouros;
- a Legendary or weather-linked Pokémon does not become the default explanation for long-term change.

## 15. Minecraft projection

Minecraft should visualize only selected consequences already authored by the owning systems.

Potential projections:

- changed snowline after Cryosphere updates;
- changed vegetation after Flora/Forest updates;
- a raised walkway after Public Works construction;
- changed signage or public displays after institutional updates;
- monitoring stations and historical markers;
- a revised seasonal route or service schedule.

Loaded blocks, biome temperature values, particle systems or entity counts are not the climate authority.

## 16. Cobblemon projection

Climate assessments may trigger an ecological review. They do not write spawn tables directly.

Safe chain:

```text
climate evidence
  → ecological hypothesis
  → observations in authoritative ecology layer
  → population/distribution revision if supported
  → controlled Cobblemon projection
```

This prevents players from farming rare species by manipulating local blocks, clocks or weather visuals.

## 17. Battle-engine boundary

Long-term climate state has no direct PTU battle effect.

If an encounter occurs during a current heatwave, storm, flood or wildfire, the current condition must be resolved by Meteorology/Urban Heat/Fire/Freshwater and then validated against PTU/Caelo/AutoPTU mechanics.

Do not create:

- `CLIMATE_CHANGE` Weather;
- climate damage;
- climate Accuracy modifiers;
- climate Status;
- climate Combat Stages;
- climate initiative modifiers;
- climate forced movement;
- climate immunity by Pokémon Type;
- climate-based capture modifiers.

## 18. Encounter contract — High Pass Sensor Retrofit

Narrative premise:

A long-running alpine monitoring series is becoming hard to compare because the original station site is no longer representative and the replacement site sits beyond a seasonally difficult pass.

FULL version:

Technicians, equipment and Pokémon must reach the replacement location while an active current-weather event alters tactical routes. The objective is `PROTECT_EQUIPMENT` plus `REACH_SITE`, not simple defeat.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if escort/interception or displacement matters
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL only for real PTU statuses
- terrain/weather/hazards/zones/reactions — BLOCKING if the current alpine weather has tactical effects
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:

Travel and current weather resolve in overworld state. Technicians remain outside the battle grid. If a confrontation is unavoidable, AutoPTU receives one static legal battle at a validated route segment. Installation and time-series reconciliation occur afterward.

## 19. Encounter contract — Early Fire-Season Relay

Narrative premise:

A district has moved seasonal emergency staffing earlier after several years of fire-season observations. During deployment, an unrelated wild disturbance blocks access to a relay site.

FULL version:

Responders and equipment need a clear route while wildfire/smoke state may exist nearby. The climate layer only explains why the deployment was scheduled earlier; Wildfire/Air Quality/Meteorology own current conditions.

Dependencies:

- complete movement — BLOCKING for route clearing/escort/interception
- terrain/weather/hazards/zones/reactions — BLOCKING if smoke/fire/wind becomes tactical
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING
- ordinary targeting/base movement/core/action foundations — VERIFIED
- lifecycle/damage/status/moves/abilities/items/Features — PARTIAL as used

REDUCED version:

The active fire perimeter and responders stay outside the grid. Resolve one static confrontation on a safe access segment. Relay deployment advances only through a separate overworld transition.

## 20. Encounter contract — Heat-Night Monitoring Walk

Narrative premise:

A city is investigating a multi-year increase in unusually warm nights. A survey team repeats the same historical walking transect when urban wildlife blocks one station approach.

FULL version:

Surveyors must complete an objective route while wildlife has believable withdrawal behavior and civilians remain protected. Any current heat effect belongs to Urban Heat and requires validated mechanics before entering battle.

Dependencies:

- complete movement — BLOCKING for mobile objective actors
- AI tactical policy — BLOCKING for WITHDRAW/REACH_SITE/AVOID_CIVILIANS
- adapter/playback — BLOCKING
- terrain/weather/hazards/zones/reactions — BLOCKING only if current heat/urban environment becomes tactical
- ordinary static battle foundations — usable under existing VERIFIED/PARTIAL boundaries

REDUCED version:

The walking transect proceeds in world state. Civilians/surveyors leave the area before combat. A static battle occurs only if one confrontation remains. The climate series is updated from observation data afterward.

## 21. Encounter contract — The Baseline Dispute

Narrative premise:

Two research institutions publish apparently conflicting claims about whether a valley’s summers have become unusually dry. Both used valid observations but different baseline periods and spatial coverage.

Battle dependency: NONE.

This should remain an investigation, archive, metrology and science scenario. Combat cannot resolve a statistical disagreement.

## 22. Permanent capability classification

Live snapshot details are recorded in `design/engine-readiness-snapshot-pass-131.md`.

```yaml
VERIFIED:
  - targeting/footprints/range/LoS
  - base movement legality
  - core calculations
  - action economy/initiative
  - AI legal-action infrastructure

PARTIAL:
  - full turn/round lifecycle
  - full stateful damage pipeline
  - status lifecycle
  - move-specific behavior
  - abilities
  - items
  - Trainer Features/perks

BLOCKING:
  - complete movement including push/pull/knockback/interception/forced movement
  - terrain/weather/hazards/zones/reactions
  - AI tactical policy
  - Minecraft/Cobblemon/Craftics adapter/playback
```

Java now has a narrow parity-backed contract that chooses an escape destination for specific Perception/Telepathy area-attack reaction patterns. This is meaningful progress inside reaction movement, but it consumes externally supplied legal reachable tiles and does not prove the complete movement/reaction family.

## 23. Overworld blockers

Future implementation needs explicit ownership for:

- `CLIMATE_REGION_STATE`
- `CLIMATE_INDICATOR_SERIES`
- `CLIMATE_BASELINE_VERSIONING`
- `CLIMATE_ANOMALY_RECORDS`
- `CLIMATE_TREND_ASSESSMENTS`
- `CLIMATE_ATTRIBUTION_CLAIMS`
- `CLIMATE_REGIME_SHIFT_CASES`
- `CLIMATE_VULNERABILITY_PROFILES`
- `CLIMATE_SCENARIO_SETS`
- `CLIMATE_ADAPTATION_PLANS`
- `CLIMATE_ADAPTATION_REVIEWS`
- `CLIMATE_TO_DOMAIN_HANDOFF`
- `CLIMATE_TO_MINECRAFT_PROJECTION`
- `CLIMATE_TO_COBBLEMON_REVIEW_HANDOFF`

None belongs inside AutoPTU-Java.

## 24. Anti-invention rules

Do not infer or invent:

- one weather event = climate trend;
- one trend = confirmed cause;
- new baseline = old data invalid;
- historical normal = mandatory restoration target;
- future scenario = future fact;
- climate trend = PTU Weather;
- climate trend = Status/damage/Accuracy/Combat Stage/initiative;
- climate trend = regional form/evolution/type/stat/Ability change;
- climate trend = spawn-table change;
- climate trend = extinction or migration without ecological evidence;
- current Minecraft biome/block/particle state = climate truth;
- current Cobblemon entity count = population trend;
- weather-linked Pokémon presence = cause of multi-year climate change;
- Legendary involvement without authored evidence.

## 25. Open canon/mechanics questions

- Which Ouros institutions maintain long-term climate records?
- What baseline periods and methods do they use, if any?
- Which regions have sufficiently long historical records at campaign start?
- Which changes are already known before the players arrive?
- Which climate-sensitive systems should have authored historical shifts rather than procedural ones?
- How much long-term state advances while no players are present?
- How are scenario sets exposed without presenting them as prophecy?
- How does multiplayer governance decide adaptation projects that alter shared infrastructure?
- Which PTU/Caelo rules, if any, govern long-term environmental exposure separately from battlefield Weather?

The full named Caelo corpus was not recoverable as a reliable invocable source in this runtime. Super PTU Online Helper was not exposed as a callable capability. No rule output is fabricated.