# Ouros Volcanism, Geothermal Systems & Unrest Layer

Status: proposed systems design. Not established canon.

## Purpose

This layer gives volcanic systems persistent identity and state across quiet periods, unrest, eruptions, geothermal use, scientific monitoring and recovery.

It extends existing systems rather than replacing them:

- Geology owns long-term site identity, formations and subsurface context.
- Meteorology owns atmosphere and weather.
- Freshwater owns catchments and water-regime state.
- Crisis owns emergency response and recovery coordination.
- Wildfire owns landscape fire and succession.
- Science owns measurements, datasets and hypotheses.
- Technology owns monitoring stations, utilities and technical assets.
- Communications owns alerts, notices and information delivery.
- Travel owns route/service closures.
- Tourism owns visitor pressure.
- Conservation owns protected access and habitat response.
- Encounter Implementation Contracts own tactical capability gates.

## Core separation

```text
volcanic system physical state
        ↓
monitoring observations
        ↓
scientific interpretations / hypotheses
        ↓
institutional unrest assessment
        ↓
notifications / access decisions
        ↓
public belief and rumor
```

Tactical battle environment remains downstream and separately validated.

## 1. Volcanic system identity

```yaml
volcanic_system:
  volcanic_system_id: null
  geological_site_ids: []
  region_ids: []
  vent_ids: []
  geothermal_field_ids: []
  monitoring_network_ids: []
  long_term_activity_profile: unknown
  current_activity_revision_id: null
  historical_event_ids: []
  cultural_memory_ids: []
  habitat_overlap_ids: []
  freshwater_link_ids: []
  settlement_dependency_ids: []
```

A volcano keeps the same identity when its appearance changes.

A quiet volcano is still a volcanic system.

## 2. Activity revision

```yaml
volcanic_activity_revision:
  revision_id: null
  volcanic_system_id: null
  valid_from: null
  valid_to: null
  physical_state_tags: []
  vent_state_ids: []
  geothermal_state_ids: []
  gas_observation_ids: []
  deformation_observation_ids: []
  seismic_observation_ids: []
  thermal_observation_ids: []
  ash_or_tephra_event_ids: []
  lava_event_ids: []
  hydrothermal_event_ids: []
  slope_event_ids: []
  uncertainty_notes: []
  source_observation_ids: []
```

Candidate descriptive tags:

- BACKGROUND
- ELEVATED_UNREST
- ESCALATING_UNREST
- ERUPTIVE_EPISODE
- DECLINING_ACTIVITY
- POST_ERUPTIVE

These labels are project-facing abstractions. Canon institutions may use different authored terminology.

## 3. Vent state

```yaml
volcanic_vent:
  vent_id: null
  volcanic_system_id: null
  location_geometry_ref: null
  vent_type_claim: null
  current_state: unknown
  observation_ids: []
  event_history_ids: []
  access_policy_refs: []
```

Do not assume every eruption uses the same vent.

A new vent is a discovery event, not an automatic retcon of the old map.

## 4. Monitoring network

```yaml
volcano_monitoring_network:
  network_id: null
  operator_institution_ids: []
  volcanic_system_ids: []
  station_ids: []
  data_channel_ids: []
  coverage_claims: []
  outage_event_ids: []
  calibration_record_ids: []
  publication_policy_ref: null
```

Possible station observations include:

- seismic signal;
- ground deformation;
- temperature;
- gas chemistry;
- visual observation;
- acoustic signal;
- spring temperature/flow;
- remote imagery.

Narrative generation may use only authored measurement types available in Ouros.

No single measurement automatically predicts eruption.

## 5. Observation and interpretation

```yaml
volcanic_observation:
  observation_id: null
  volcanic_system_id: null
  station_or_observer_id: null
  observed_at: null
  measurement_type: null
  value_or_band: null
  instrument_state_ref: null
  confidence: null
  raw_record_ref: null
```

```yaml
volcanic_interpretation:
  interpretation_id: null
  institution_or_actor_id: null
  based_on_observation_ids: []
  claim: null
  confidence: null
  alternatives: []
  supersedes_id: null
  published_at: null
```

An interpretation can be wrong without the raw observation becoming false.

## 6. Institutional unrest assessment

```yaml
volcanic_unrest_assessment:
  assessment_id: null
  volcanic_system_id: null
  issuing_institution_id: null
  assessment_band: null
  issued_at: null
  based_on_interpretation_ids: []
  access_recommendation_refs: []
  transport_recommendation_refs: []
  next_review_at: null
  supersedes_id: null
```

This is institutional state, not physical truth.

Different institutions may assess the same evidence differently.

## 7. Geothermal field

```yaml
geothermal_field:
  geothermal_field_id: null
  volcanic_system_id: null
  spring_ids: []
  vent_or_fumarole_ids: []
  groundwater_link_ids: []
  temperature_observation_ids: []
  chemistry_observation_ids: []
  service_dependency_ids: []
  habitat_overlap_ids: []
  tourism_site_ids: []
  energy_asset_ids: []
  current_state: unknown
```

Geothermal output can matter during long quiet periods.

A hot spring may support:

- bathing or hospitality;
- care or rehabilitation locations;
- research;
- local heating;
- agriculture;
- tourism;
- specialized habitats;
- energy infrastructure.

No health benefit or healing effect is mechanical unless explicitly validated.

## 8. Hydrothermal event

```yaml
hydrothermal_event:
  event_id: null
  volcanic_system_id: null
  geothermal_field_id: null
  event_type: null
  observed_at: null
  footprint_ref: null
  precursor_observation_ids: []
  consequence_ids: []
  causal_hypothesis_ids: []
```

Candidate descriptive types:

- SPRING_FLOW_CHANGE
- SPRING_TEMPERATURE_CHANGE
- STEAM_RELEASE
- NEW_VENT
- FUMAROLE_CHANGE
- PHREATIC_EVENT

These are world-state labels. They do not define PTU damage.

## 9. Eruptive event

```yaml
volcanic_event:
  event_id: null
  volcanic_system_id: null
  event_class: null
  started_at: null
  ended_at: null
  active_vent_ids: []
  observation_ids: []
  lava_footprint_refs: []
  ash_tephra_event_ids: []
  gas_event_ids: []
  slope_event_ids: []
  lahar_event_ids: []
  infrastructure_impact_ids: []
  habitat_change_ids: []
  route_change_ids: []
  public_memory_ids: []
```

An event may have several phases.

Do not collapse every event into `eruption=true`.

## 10. Ash and tephra footprint

```yaml
ash_tephra_event:
  ash_event_id: null
  volcanic_event_id: null
  emitted_at: null
  airborne_footprint_ref: null
  deposition_footprint_ref: null
  observation_ids: []
  meteorology_state_refs: []
  resuspension_event_ids: []
  cleanup_project_ids: []
  freshwater_effect_claim_ids: []
  agriculture_effect_claim_ids: []
  health_signal_ids: []
```

Ash movement depends on atmosphere and later surface processes.

A historic deposit may create a future resuspension event without a new eruption.

Minecraft particles are presentation only.

## 11. Lava footprint

```yaml
lava_flow_event:
  lava_event_id: null
  volcanic_event_id: null
  active_from: null
  active_to: null
  footprint_versions: []
  infrastructure_intersection_ids: []
  route_intersection_ids: []
  habitat_intersection_ids: []
  cooling_state: unknown
  later_landform_id: null
```

Lava can become geology after the event.

Do not infer damage or movement legality from a rendered lava block.

## 12. Lahar and volcanic watershed coupling

Volcanic material can interact with later rain or snowmelt.

```text
volcanic deposit
  -> catchment material state
  -> weather / melt event
  -> hydrology assessment
  -> lahar/debris-flow world event
```

Freshwater owns the water-flow side of this chain.

Volcanism records the volcanic material provenance.

No rainfall directly triggers tactical damage without a validated bridge.

## 13. Long quiet periods

A volcano should generate content when nothing is erupting.

Examples:

- instrument maintenance;
- geothermal service changes;
- trail surveys;
- habitat monitoring;
- historical research;
- hot-spring tourism;
- old lava-field mapping;
- school field trips;
- infrastructure inspection;
- observatory staffing;
- disputes about access;
- archival comparison of old vent maps.

This prevents the layer from becoming a crisis generator.

## 14. Ecological integration

Wild Pokémon presence should respond only through validated ecological state.

Possible authored relationships:

- warm tunnels used as habitat;
- newly cooled ground colonized over time;
- ash-covered areas changing forage availability;
- springs supporting specialized local activity;
- evacuation/displacement during active events.

Do not infer species behavior only from type.

A Fire-type is not automatically attracted to every volcano.

## 15. Settlement and infrastructure integration

Volcanic systems can support or disrupt:

- cable cars;
- roads and passes;
- hot-spring facilities;
- utilities;
- geothermal energy;
- scientific observatories;
- tourism;
- water supply;
- hospitals/clinics;
- farms;
- ports or aviation routes through ash impacts.

Dependencies should remain explicit.

## 16. Public belief and myth

Volcanoes naturally accumulate stories.

Keep separate:

- geological observation;
- scientific interpretation;
- institutional alert;
- historical record;
- public rumor;
- cultural tradition;
- Legendary claim;
- canonical supernatural fact.

An old story can be culturally important without being geologically correct.

## 17. Minecraft projection

Minecraft may render:

- active/inactive vents;
- fumaroles;
- hot springs;
- ash deposits;
- cooled lava fields;
- access barriers;
- monitoring stations;
- cable-car or route closures;
- evacuation signs;
- damaged infrastructure;
- recovery construction.

Minecraft must not decide:

- whether unrest escalates;
- eruption timing;
- lava propagation;
- gas toxicity;
- ash mechanical effects;
- PTU Weather;
- battle hazard damage;
- Pokémon ecological truth.

Those remain server-owned states.

## 18. Battle projection contract

A volcanic world-state revision may be projected into an encounter only after validation.

```yaml
volcanic_battle_projection:
  projection_id: null
  source_activity_revision_id: null
  source_event_ids: []
  battle_map_revision_id: null
  validated_static_geometry_refs: []
  validated_ptu_environment_refs: []
  visual_only_effects: []
  excluded_world_hazards: []
  capability_review_id: null
```

When the engine lacks a family, keep the feature outside battle.

## 19. Encounter contracts

### Observatory Evacuation

Narrative premise:

Monitoring data rises while a summit station is staffed. The objective is to withdraw people and preserve the latest records before access closes.

Full version depends on:

- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement incl. interception/forced movement — BLOCKING if evacuees move through the grid;
- core calculations — VERIFIED;
- action economy / initiative — VERIFIED;
- full turn / round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain / weather / hazards / zones / reactions — BLOCKING for ash, heat or falling material;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features / perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for withdraw/protect goals;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

Resolve evacuation and access closure in world state. Freeze a safe static platform as the battle map. Keep ash, heat, gas and civilians outside tactical mechanics. Run a conventional battle only if a real confrontation occurs.

### Geothermal Intake Failure

Narrative premise:

A town's hot-water service drops unexpectedly. Investigation reaches an intake chamber where Pokémon activity and infrastructure damage must be distinguished from the underlying geothermal change.

Full version depends on dynamic terrain/hazards/interactables, tactical objectives and adapter playback.

Reduced version:

Investigate spring flow, machinery and Pokémon behavior in overworld state. If combat occurs, use a fixed dry arena. Service restoration occurs after the authoritative world-state investigation, not because a combatant hits a pipe.

### Ashfall Pass Reopening

Narrative premise:

After an eruptive episode ends, a mountain pass remains closed. The task is to survey the route, identify stable sections and resolve any genuine Pokémon confrontation without treating ash as automatic PTU terrain.

Full version depends on terrain/zones/reactions, movement objectives, tactical AI and Minecraft projection.

Reduced version:

Survey ash/deposit state before battle. Select a validated stable section as static geometry. Keep ash mechanical effects disabled unless an exact PTU/Caelo effect is validated.

## 20. Permanent capability map used by this layer

Current planning state from live Java evidence:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter & playback — BLOCKING

## 21. Overworld implementation blockers

`OVERWORLD_VOLCANIC_SYSTEM_STATE = BLOCKING`

`OVERWORLD_VOLCANO_MONITORING_NETWORK = BLOCKING`

`OVERWORLD_GEOTHERMAL_FIELD_STATE = BLOCKING`

`OVERWORLD_VOLCANIC_UNREST_ASSESSMENT = BLOCKING`

`OVERWORLD_VOLCANIC_EVENT_FOOTPRINTS = BLOCKING`

`OVERWORLD_ASH_TEPHRA_STATE = BLOCKING`

`OVERWORLD_VOLCANISM_TO_FRESHWATER = BLOCKING`

`OVERWORLD_VOLCANISM_TO_TRAVEL = BLOCKING`

`OVERWORLD_VOLCANISM_TO_COBBLEMON = BLOCKING`

`OVERWORLD_VOLCANISM_TO_BATTLE = BLOCKING`

`OVERWORLD_VOLCANISM_TO_MINECRAFT = BLOCKING`

## 22. Rules guardrails

Do not generate any of the following without authoritative PTU/Caelo text and implementation evidence:

- lava damage;
- magma movement legality;
- ambient heat damage;
- volcanic-gas Status effects;
- ash Accuracy penalties;
- automatic Rough/Slow Terrain from ash;
- eruption dice;
- random volcanic strikes;
- lahar displacement;
- steam-blast damage;
- hot-spring healing;
- Fire-type environmental immunity;
- Water-type penalties from geothermal heat;
- automatic weather from volcanic activity;
- Ground/Rock/Fire bonuses because of location flavor;
- Legendary-triggered eruption mechanics.

Volcanic state can enrich the world now. Tactical volcano mechanics remain gated.