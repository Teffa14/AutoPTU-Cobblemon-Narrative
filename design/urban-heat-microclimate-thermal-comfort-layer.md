# Ouros Urban Heat, Microclimate & Thermal Comfort Layer

Status: PROPOSED SYSTEMS DESIGN. Not established canon.

Pass: 85.

## Purpose

This layer gives settlements fine-scale thermal state without turning descriptive heat into PTU mechanics.

It connects:

- Meteorology for regional weather and heat events;
- Architecture for structure geometry and materials;
- Urban Public Space for time-programmed shared spaces;
- Flora for vegetation identity and canopy;
- Freshwater for water features and supply;
- Energy Infrastructure for cooling demand and service state;
- Air Quality for atmospheric episodes;
- Health Surveillance for aggregate health signals;
- Accessibility for participation needs;
- Light for solar exposure and nighttime lighting;
- Science and Cartography for observations and maps;
- Minecraft for visual projection;
- AutoPTU only after a separate mechanics eligibility check.

## Core separation

Keep these states distinct:

```text
regional weather
-> local built/vegetation/water context
-> microclimate state
-> measurement or observation
-> interpretation
-> operational decision
-> social/ecological consequence
-> optional PTU mechanics eligibility check
-> battle snapshot
```

A hot-looking street does not create battle damage.
A shaded park does not create a buff.
A regional heat event does not make every block equally hot.

## 1. Urban thermal zone

Use coarse persistent areas rather than block-by-block simulation.

```yaml
urban_thermal_zone:
  thermal_zone_id: null
  settlement_id: null
  district_id: null
  geometry_ref: null
  built_structure_refs: []
  public_space_refs: []
  vegetation_unit_refs: []
  water_feature_refs: []
  surface_context_tags: []
  sky_exposure_band: null
  ventilation_context_tags: []
  current_revision_id: null
  observation_ids: []
  mitigation_project_refs: []
  source_refs: []
```

Candidate contexts are descriptive only:

- dense_street_canyon;
- shaded_residential_lane;
- market_square;
- station_forecourt;
- waterfront_edge;
- industrial_yard;
- tree_canopy_corridor;
- courtyard;
- rooftop;
- park_interior;
- exposed_slope;
- transit_platform;
- mixed_use_block.

None are PTU Terrain names.

## 2. Thermal-state revision

```yaml
urban_thermal_revision:
  revision_id: null
  thermal_zone_id: null
  valid_from: null
  valid_until: null
  regional_weather_ref: null
  time_window_ref: null
  surface_heat_band: null
  air_heat_band: null
  humidity_context_band: null
  shade_fraction_band: null
  stored_heat_band: null
  ventilation_band: null
  confidence: null
  observation_basis_ids: []
```

Suggested bands are qualitative until measurement standards are authored:

- LOW
- MODERATE
- HIGH
- VERY_HIGH
- UNKNOWN

Do not expose fake precision.

## 3. Surface and air heat remain separate

A roof, wall or pavement can be much hotter than nearby air.

```yaml
thermal_observation:
  observation_id: null
  thermal_zone_id: null
  observed_at: null
  observation_type: null
  location_ref: null
  height_or_surface_context: null
  measured_values: []
  instrument_ref: null
  observer_ref: null
  shade_state: null
  weather_ref: null
  quality_flags: []
  source_refs: []
```

Candidate observation types:

- AIR_TEMPERATURE
- SURFACE_TEMPERATURE
- HUMIDITY
- SHADE_OBSERVATION
- WIND_EXPOSURE
- OCCUPANT_REPORT
- POKEMON_BEHAVIOR_OBSERVATION
- NIGHT_COOLING_OBSERVATION

A resident report is evidence. It is not automatically less valid, but it has its own provenance.

## 4. Time-of-day thermal memory

The same place can have different problems during the afternoon and after sunset.

```yaml
thermal_daily_cycle_profile:
  profile_id: null
  thermal_zone_id: null
  morning_pattern: null
  afternoon_pattern: null
  evening_pattern: null
  overnight_pattern: null
  evidence_refs: []
  confidence: provisional
```

This profile may strengthen through repeated surveys.

Do not infer it from visual materials alone.

## 5. Shade network

Shade should be represented spatially and temporally.

```yaml
shade_asset:
  shade_asset_id: null
  asset_type: null
  physical_ref: null
  thermal_zone_ids: []
  effective_time_windows: []
  current_state: null
  maintenance_ref: null
  vegetation_ref: null
  provenance_refs: []
```

Possible assets:

- mature_tree_canopy;
- arcade;
- awning;
- transit_canopy;
- courtyard_colonnade;
- shade_sail;
- bridge_shadow;
- cliff_or_structure_shadow;
- other authored element.

Shade is not a battle bonus unless an exact mechanic later says so.

## 6. Water and evaporative context

Water can affect local thermal conditions, but the system must not create free cooling from any water block.

```yaml
urban_water_thermal_link:
  link_id: null
  water_feature_ref: null
  thermal_zone_id: null
  operating_state_ref: null
  water_availability_ref: null
  observed_effect_ids: []
  confidence: null
```

Possible world assets include fountains, canals, ponds, irrigated gardens and misting systems where canon/technology supports them.

Their operation must connect to Freshwater and Infrastructure state.

## 7. Vegetation and canopy

Reuse Flora identities rather than create anonymous green tiles.

```yaml
urban_canopy_thermal_link:
  link_id: null
  vegetation_unit_ref: null
  thermal_zone_id: null
  canopy_state_ref: null
  flowering_or_ecology_refs: []
  irrigation_dependency_refs: []
  observed_thermal_effect_ids: []
```

A canopy project can change habitat, shade, pollen, maintenance and stormwater at the same time.

Those outcomes are separate.

## 8. Anthropogenic heat sources

Buildings and machines can emit waste heat.

```yaml
urban_heat_source:
  heat_source_id: null
  source_type: null
  physical_asset_ref: null
  operating_schedule_ref: null
  activity_state_ref: null
  thermal_zone_ids: []
  observation_refs: []
  source_claim_refs: []
```

Possible source types:

- industrial_process;
- transit_hub;
- cooling_exhaust;
- generator;
- dense_commercial_activity;
- event_equipment;
- other authored source.

A nearby machine does not prove it caused the local thermal pattern.

## 9. Thermal exposure event

Exposure is actor- and time-specific.

```yaml
thermal_exposure_event:
  exposure_id: null
  actor_or_cohort_ref: null
  thermal_zone_id: null
  start_time: null
  end_time: null
  observed_conditions_ref: null
  activity_context: null
  shelter_or_cooling_access_refs: []
  reported_effect_refs: []
  mechanical_effect_ref: null
  privacy_scope: null
```

The world-state layer can record presence and reports.

It cannot invent Injury, Status, HP loss or diagnosis.

## 10. Operational adaptations

The useful gameplay comes from decisions.

Possible operational responses:

- reschedule a market;
- open a shaded waiting room;
- move a queue;
- change a festival setup;
- reroute a walking tour;
- adjust maintenance hours;
- increase water-service availability;
- inspect cooling equipment;
- add temporary shade;
- prioritize a long-term retrofit.

These are world actions, not buffs.

## 11. Cooling and retrofit project

```yaml
thermal_mitigation_project:
  project_id: null
  target_zone_ids: []
  intervention_type: null
  baseline_observation_ids: []
  proposal_ref: null
  funding_ref: null
  construction_or_planting_refs: []
  maintenance_refs: []
  expected_effect_claims: []
  followup_observation_ids: []
  status: PROPOSED
```

Possible interventions include:

- canopy planting;
- shade infrastructure;
- green roof;
- roof material retrofit;
- pavement retrofit;
- water-feature restoration;
- ventilation corridor protection;
- reduction/relocation of heat-emitting equipment;
- adaptive reuse that changes exposure.

No project is automatically successful.

## 12. Thermal survey mission grammar

A typical noncombat investigation can be:

```text
REPORT
-> choose transects / sites
-> morning survey
-> afternoon survey
-> evening survey
-> compare land use / shade / vegetation
-> inspect anomalous point
-> publish or retain results
-> propose response
-> follow-up after intervention
```

Failure-forward options:

- sensor calibration issue;
- missing time window;
- route blocked;
- heat event ended before survey completion;
- one site changed during construction;
- volunteer observations conflict;
- data show no clear problem.

A null result remains useful world knowledge.

## 13. Pokémon observations

Pokémon can be part of the evidence without becoming thermometers by flavor.

Possible observation records:

- a species changes time of use of a plaza;
- a known individual shifts to a shaded resting site;
- a wild collective stops using a rooftop during afternoon hours;
- a watering feature draws more activity during a hot period;
- an urban habitat remains occupied despite hotter readings.

Do not infer cause from correlation.

Do not grant heat immunity/resistance from Type without PTU authority.

## 14. Minecraft projection

Minecraft can safely present:

- shade structures;
- canopy changes;
- open/closed cooling spaces;
- altered NPC schedules;
- fountains operating or offline;
- public notices;
- sensor stations;
- retrofit construction;
- visual heat shimmer where presentation supports it;
- different crowd use by time of day.

Minecraft must not decide:

- actor heat damage;
- PTU Weather;
- terrain cost;
- status application;
- Pokémon immunity;
- encounter rarity changes;
- medical diagnosis.

## 15. Cobblemon projection

Any ecological projection must pass through an authored ecological rule.

Bad path:

`hot block -> spawn Fire type`

Allowed path:

`multi-season thermal observations -> authored species-response hypothesis -> validated regional ecology rule -> coarse spawn-weight adjustment with anti-exploit limits`

Loaded entity counts never become ecology truth.

## 16. Battle projection

Before AutoPTU opens a battle, create a frozen thermal context.

```yaml
battle_thermal_projection:
  source_world_revision_ids: []
  battle_map_revision_id: null
  visual_context_tags: []
  validated_ptu_weather_ref: null
  validated_terrain_refs: []
  validated_hazard_refs: []
  rules_evidence_refs: []
```

If no validated mechanic exists, the battle remains visually hot/shaded without mechanical effect.

## 17. PTU / Caelo guardrails

This layer does not invent:

- heat damage;
- dehydration;
- fatigue;
- Burned;
- Sunny Day;
- harsh sunlight;
- shade bonuses;
- water bonuses;
- Fire-type immunity;
- Ice-type vulnerability;
- Accuracy penalties;
- Slowed;
- movement costs;
- equipment bonuses;
- cooling-center healing;
- heat-based capture modifiers.

Exact mechanics must come from authoritative PTU/Caelo text and verified engine coverage.

## 18. Encounter contracts

### Heat-Survey Station Interruption

Narrative premise:

A temporary sensor route through a dense district is interrupted while multiple institutions are trying to complete the same afternoon survey window.

FULL version dependencies:

- complete movement including interception/forced movement if moving crowds or competing actors exist inside the grid;
- terrain/weather/hazards/zones/reactions if thermal zones have tactical effects;
- AI tactical policy for PROTECT_SENSOR / REACH_SAMPLE_POINT / WITHDRAW;
- Minecraft/Cobblemon/Craftics adapter/playback.

REDUCED version:

Resolve civilian flow and sensor placement in overworld state. If conflict becomes a battle, freeze one static plaza/alley map. Heat remains descriptive only.

### Cooling-Courtyard Access

Narrative premise:

A shaded courtyard becomes operationally important during a hot period, but access is complicated by maintenance and an unrelated wild-Pokémon disturbance.

FULL version dependencies:

- objective-aware AI;
- complete movement/interception for evacuation or protected access;
- terrain/zones only if a validated mechanic exists;
- adapter/playback.

REDUCED version:

Move civilians and maintenance staff before battle. Keep the cooling function in world state. Run only a conventional legal encounter with actual combatants.

### Night-Heat Relay Failure

Narrative premise:

A district remains unexpectedly warm after sunset while a cooling/energy relay reports inconsistent status and Pokémon activity shifts around nearby roofs.

FULL version dependencies:

- field/environment state if a verified tactical heat/weather effect is ever used;
- interactable-object objectives;
- tactical AI;
- Minecraft playback.

REDUCED version:

Treat investigation, roof access and relay diagnosis as overworld actions. If battle occurs, use a frozen rooftop arena with no invented thermal penalties.

## 19. Long-term consequences

This layer can feed:

- Public Works: shade/cooling proposals;
- Architecture: retrofit versions;
- Flora: canopy projects;
- Energy: cooling demand and outages;
- Health Surveillance: aggregate heat-related signals when supported;
- Public Space: time-program changes;
- Tourism: route/schedule changes;
- Workplaces: shift changes;
- Accessibility: alternative participation routes/times;
- Air Quality: compound episodes;
- Freshwater: water demand;
- Public Memory: famous hot summers or successful interventions.

## 20. Promotion gates

Before promoting any thermal mechanic to canon or executable battle behavior, confirm:

1. Ouros canon defines the local technology/institution involved.
2. The world state has a measured/authored basis rather than a visual guess.
3. PTU/Caelo actually defines the mechanical effect, if any.
4. Python oracle behavior is understood where relevant.
5. Java has specific parity evidence for the mechanic.
6. Minecraft only renders or submits validated input.
7. The mechanic cannot be exploited by trivial block placement or removal.
