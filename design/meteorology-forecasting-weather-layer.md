# Ouros Meteorology, Forecasting & Weather Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already tracks seasonality, observed weather, crisis forecasts, transport state, ecology, agriculture, public information and infrastructure. This layer connects those systems through one explicit meteorology model.

Its job is to answer five different questions without collapsing them into one:

- what weather is actually happening;
- what instruments and observers measured;
- what an institution predicts will happen;
- what each actor has heard or believes;
- whether a tactical battle has an authoritative PTU Weather state.

## Relationship to existing layers

This layer extends rather than replaces:

- `seasonality-calendar-phenology-layer.md` for calendar, climate expectation and seasonal baselines;
- `crisis-rescue-recovery-layer.md` for hazardous escalation and emergency response;
- `science-research-discovery-layer.md` for measurements, datasets and hypotheses;
- `media-communications-information-layer.md` for forecast delivery and correction;
- `travel-transport-expedition-layer.md` for route/service decisions;
- `food-agriculture-hospitality-layer.md` for cultivation and service timing;
- `wild-collective-agency-layer.md` and `interspecies-ecological-relations-layer.md` for observed ecological response;
- `technology-energy-infrastructure-layer.md` for stations, sensors and communications dependencies;
- `cartography-survey-wayfinding-layer.md` for spatial forecast products;
- `encounter-implementation-contracts.md` for battle capability gates.

## Core separation

```text
regional climate expectation
        ↓
actual atmospheric/world-weather state
        ↓
observations from instruments/actors
        ↓
analysis/model state
        ↓
forecast issue + confidence
        ↓
delivery to actors/institutions
        ↓
operational decisions
        ↓
observed outcome
        ↓
forecast verification / institutional memory
```

Battle Weather is a separate downstream state.

```text
world weather observation
        ↓
mechanics eligibility check
        ↓
authoritative AutoPTU battlefield Weather
```

Minecraft visuals never create PTU mechanics by themselves.

## 1. Atmospheric world state

```yaml
weather_system:
  weather_system_id: null
  system_type: null
  active_from: null
  projected_end: null
  spatial_footprint_ref: null
  movement_vector: null
  intensity_band: null
  observed_condition_tags: []
  source_observation_ids: []
  causal_claim_ids: []
  confidence: null
  status: OBSERVED
```

Possible system types are authored labels, not automatic mechanics. Examples may include rain band, fog bank, heat event, snow system, coastal wind event or thunderstorm complex.

A weather system may cover several connected locations.

## 2. Weather observation

Reuse the seasonality layer's `weather_observation`, but extend it with provenance.

```yaml
weather_observation:
  observation_id: null
  location_id: null
  observed_at_world_time: null
  observer_type: STATION
  observer_id: null
  instrument_refs: []
  condition_tags: []
  measurements: []
  quality_flags: []
  confidence: null
  raw_record_ref: null
  source_refs: []
```

Candidate observer types:

- STATION
- TRAINED_OBSERVER
- PLAYER_REPORT
- PUBLIC_REPORT
- POKEMON_BEHAVIOR_OBSERVATION
- REMOTE_SENSOR
- VISUAL_RECORD
- INSTITUTIONAL_REPORT

A player report is not less valuable by definition, but it has its own provenance and quality state.

## 3. Observation quality

```yaml
observation_quality:
  observation_id: null
  calibration_state: UNKNOWN
  timestamp_quality: GOOD
  location_quality: GOOD
  sensor_health: UNKNOWN
  obstruction_flags: []
  conflicting_observation_ids: []
  reviewer_ids: []
```

A failed sensor can produce a record. That record must not automatically become weather truth.

## 4. Weather station

```yaml
weather_station:
  station_id: null
  location_id: null
  institution_id: null
  status: OPERATIONAL
  instrument_ids: []
  communications_channel_ids: []
  power_dependency_ids: []
  maintenance_state_id: null
  coverage_profile_ref: null
  archive_refs: []
```

Candidate status values:

- OPERATIONAL
- DEGRADED
- OFFLINE
- CALIBRATION_DUE
- DAMAGED
- TEMPORARY
- RETIRED

Stations connect naturally to infrastructure, workplaces and science systems.

## 5. Microclimate profile

Nearby places do not need identical weather.

```yaml
microclimate_profile:
  profile_id: null
  location_ids: []
  elevation_band: null
  exposure_tags: []
  water_proximity_tags: []
  terrain_context_tags: []
  recurring_condition_patterns: []
  evidence_refs: []
  confidence: provisional
```

Do not fabricate precise meteorology from terrain tags alone. A profile strengthens only through authored data and observations.

## 6. Forecast issue

```yaml
forecast_issue:
  forecast_id: null
  issuing_institution_id: null
  issued_at: null
  valid_from: null
  valid_to: null
  spatial_scope_refs: []
  predicted_conditions: []
  uncertainty_band: null
  confidence: null
  model_or_method_ref: null
  source_observation_ids: []
  supersedes_forecast_id: null
  publication_packet_ids: []
  status: ACTIVE
```

Candidate status values:

- ACTIVE
- SUPERSEDED
- EXPIRED
- CORRECTED
- WITHDRAWN

A superseded forecast remains in history.

## 7. Forecast uncertainty

Forecasts should not expose fake precision.

Useful uncertainty forms:

- broad confidence bands;
- spatial uncertainty;
- timing windows;
- competing scenarios;
- explicit unknowns.

Example:

```yaml
forecast_uncertainty:
  forecast_id: null
  timing_window: null
  spatial_margin: null
  alternate_scenarios: []
  low_confidence_factors: []
```

Do not present probability numbers unless the underlying system actually produces them.

## 8. Forecast revision

Weather knowledge changes over time.

A later forecast may:

- shift arrival time;
- change expected route;
- increase or reduce confidence;
- downgrade severity;
- split one system into two;
- acknowledge sensor failure;
- retract an earlier interpretation.

Revision is not retcon.

## 9. Forecast delivery

The Communications layer remains authoritative for who receives information.

```yaml
forecast_delivery:
  forecast_id: null
  packet_id: null
  channel_id: null
  recipient_scope_refs: []
  sent_at: null
  delivery_state: null
```

An issued forecast can fail to reach a remote route.

## 10. Operational decision record

Institutions can act on forecasts before the outcome is known.

```yaml
weather_decision:
  decision_id: null
  actor_or_institution_id: null
  forecast_refs: []
  observation_refs: []
  decision_type: null
  action_refs: []
  issued_at: null
  rationale_summary: null
  reversible: true
```

Examples:

- delay ferry;
- move outdoor event;
- stage line crew;
- close exposed trail;
- move livestock/Pokémon care operation;
- alter field-survey window;
- deploy temporary sensor;
- prepare drainage equipment.

A forecast that later proves wrong does not make the earlier decision irrational if it was reasonable from the information available then.

## 11. Forecast verification

```yaml
forecast_verification:
  verification_id: null
  forecast_id: null
  verifying_observation_ids: []
  evaluated_at: null
  timing_result: null
  spatial_result: null
  condition_result: null
  evaluator_ids: []
  notes: null
```

Use qualitative assessment first.

Possible values:

- CONSISTENT
- PARTIALLY_CONSISTENT
- MISSED
- INCONCLUSIVE
- NOT_EVALUABLE

Do not reduce institutional credibility to one universal score.

## 12. Institutional forecast memory

A weather institution can maintain:

- forecast archive;
- calibration history;
- missed-event reviews;
- station outages;
- known blind spots;
- retired models;
- regional knowledge;
- public corrections.

This can produce later quests without inventing a villain.

## 13. Pokémon as meteorological participants

Pokémon may participate in weather research only through source-supported behavior or validated mechanics.

Examples of safe narrative roles:

- repeated observation of weather-sensitive behavior;
- station companion;
- field-team partner;
- source of a biological observation;
- subject of research into weather-linked form/activity.

Hard rules:

- Castform does not provide perfect forecasts by species identity.
- Forecast Ability does not automatically grant overworld prediction powers.
- Drizzle, Drought, Sand Stream, Snow Warning or weather Moves cannot be used narratively unless the individual Pokémon and authoritative rules support them.
- A Pokémon causing battlefield Weather does not prove it caused the regional storm outside battle.

## 14. Natural versus Pokémon-caused weather

Store causal claims explicitly.

```yaml
weather_causal_claim:
  claim_id: null
  weather_system_id: null
  proposed_cause_ref: null
  evidence_ids: []
  confidence: null
  state: HYPOTHESIS
```

Possible causes can remain competing hypotheses.

A Legendary rumor, unusual Ability or ancient device never becomes the cause because the story needs escalation.

## 15. Weather anomalies

Seasonality already defines anomalies against climate expectations.

Meteorology adds short-horizon anomalies such as:

- unexpected intensification;
- stalled system;
- unusual direction;
- unexplained local gap;
- station disagreement;
- rapid dissipation;
- repeated microclimate mismatch.

These should usually generate investigation before crisis.

## 16. Non-crisis weather content

Weather should create ordinary world texture.

Examples:

- photographers seek a brief fog window;
- cafés prepare sheltered seating;
- harbor crews alter loading order;
- farmers postpone work;
- schools move field practice indoors;
- Rangers reschedule surveys;
- a festival activates its rain plan;
- climbers wait for visibility;
- researchers compare local rainfall reports;
- residents argue about a famously unreliable forecast without anyone being malicious.

## 17. Crisis promotion gate

A weather system becomes a Crisis object only when it crosses authored impact thresholds.

Possible triggers:

- route closure;
- infrastructure risk;
- shelter activation;
- medical/public-safety response;
- large ecological displacement;
- evacuation;
- major service interruption.

Ordinary rain should not become a crisis because the generator needs drama.

## 18. Minecraft presentation contract

Minecraft may present:

- rain/snow/fog/cloud visuals when available;
- wind ambience;
- wet/dry variants;
- station blocks or structures;
- forecast boards;
- warning signage;
- player-facing forecast UI;
- sensor status;
- route closures.

Minecraft must not independently decide:

- PTU battlefield Weather;
- weather damage;
- accuracy/evasion modifiers;
- wind displacement;
- status effects;
- Move legality;
- Ability activation;
- Trainer Feature effects.

## 19. Battle Weather handoff

When an encounter begins, the adapter may request a battlefield-weather initialization from authoritative battle logic.

Proposed request shape:

```yaml
battle_weather_request:
  battle_id: null
  world_weather_observation_refs: []
  location_id: null
  authored_encounter_weather_ref: null
  requested_weather_tag: null
```

The battle core must accept, normalize or reject that request according to the rules contract.

The narrative system does not translate `heavy_rain_visual` directly into a PTU effect.

## 20. Capability dependency policy

Any encounter that uses weather only as backdrop can run without tactical Weather support.

Any encounter where Weather changes damage, Accuracy, types, abilities, movement, visibility, hazards, zones or action legality depends on `terrain/weather/hazards/zones/reactions`.

Weather-dependent Moves and Abilities also depend on their own permanent categories:

- `move-specific behavior`;
- `abilities`;
- `items` when relevant;
- `Trainer Features/perks` when relevant;
- `full turn/round lifecycle` when duration/tick timing matters;
- `full stateful damage pipeline` when Weather changes damage;
- `status lifecycle` when Weather causes or removes statuses.

## 21. Reduced-version rule

A reduced encounter may preserve:

- storm visuals;
- forecast pressure;
- route closure;
- station failure;
- evacuation preparation;
- ecological behavior;
- NPC decisions;
- timing consequences;

while freezing the tactical grid into one legal static state.

Reduced versions must never simulate missing PTU Weather rules through Minecraft commands.

## 22. Data persistence

Weather-system state should be coarse.

Do not simulate every cloud.

Persist only data that affects:

- future observations;
- forecasts;
- route/service decisions;
- ecology;
- agriculture;
- crisis state;
- public information;
- meaningful player planning;
- battle initialization.

## 23. Offline advancement

Weather may advance while no player is present if the world-time policy permits it.

Offline simulation should operate at system/state-transition level rather than tick-level physics.

If a player returns after a weather event, world state can preserve:

- changed route condition;
- missed forecast issue;
- station damage;
- delayed service;
- ecological observations;
- public reports;
- cleanup/recovery work.

Do not punish offline players by silently applying unresolved mechanical damage to their Pokémon.

## 24. Accessibility

Critical weather warnings cannot rely only on color, sound or particle intensity.

Warnings should support equivalent presentation through:

- text;
- iconography;
- map overlays;
- captions;
- clear route/service state;
- optional audio.

## 25. Canon boundary

Human review must decide:

- which meteorological institutions exist;
- regional climate identities;
- technology level of forecasting;
- whether weather-control technology exists;
- which Pokémon have authored institutional roles;
- what weather phenomena can have supernatural causes;
- whether players can alter regional weather outside PTU combat;
- how reliable long-range forecasts are.

## 26. Mechanical boundary

This layer never invents:

- Weather duration;
- Rain/Sun/Sand/Hail/Snow battle effects;
- Weather Ball behavior;
- Forecast behavior;
- weather damage;
- immunity;
- wind movement;
- visibility penalties;
- Lightning damage;
- Survival or Education DCs;
- Ability activation;
- Move legality;
- Trainer Feature interactions.

Those remain PTU/Caelo + AutoPTU responsibilities.