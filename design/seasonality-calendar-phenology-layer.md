# Ouros Seasonality, Calendar & Phenology Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already has regional clocks, event schedules, agriculture, wild collectives, travel state, crises, observation and public memory. Those systems reference time, but they do not yet share one explicit seasonal substrate.

This layer defines that substrate.

The goal is to make familiar places change coherently over recurring world time while keeping calendar state, ecology, actual weather, visual presentation and PTU tactical weather separate.

## 1. Temporal authority

A multiplayer persistent world needs one authoritative fictional date source.

```yaml
world_calendar:
  calendar_id: null
  current_world_date: null
  current_world_time: null
  time_scale_policy: null
  pause_policy: null
  offline_advance_policy: null
  calendar_version: 1
  source_of_truth: server
  last_advanced_event_id: null
```

The player's local PC clock must not independently decide canon world state.

Possible `time_scale_policy` values may later include:
- REALTIME_LINKED
- ACCELERATED_CONTINUOUS
- SESSION_ADVANCED
- EVENT_ADVANCED
- HYBRID

No policy becomes canon until multiplayer and persistence requirements are reviewed.

## 2. World date and local temporal context

Separate global date from local daylight and regional cycles.

```yaml
local_temporal_context:
  location_id: null
  world_date: null
  local_time_band: DAY
  daylight_profile_id: null
  regional_cycle_id: null
  season_phase_id: null
  special_calendar_tags: []
```

Candidate `local_time_band` values:
- DAWN
- MORNING
- DAY
- EVENING
- NIGHT
- DEEP_NIGHT

Caelo already distinguishes Morning/Day/Night for wild encounters. Ouros may use finer presentation bands, but mechanical encounter rules must still reference the adopted authoritative definitions.

## 3. Region-specific seasonal profiles

Do not force every part of Ouros into the same four-season model.

```yaml
regional_cycle:
  cycle_id: null
  region_ids: []
  public_name: null
  phase_ids: []
  expected_duration_policy: null
  transition_rules: []
  daylight_profile_refs: []
  climate_expectation_refs: []
  ecology_expectation_refs: []
  cultural_event_refs: []
  source_refs: []
```

Examples of authorable cycle structures:
- spring / summer / autumn / winter;
- wet / transition / dry;
- thaw / bloom / high summer / storm / frost;
- migration season / nesting season / quiet season;
- urban service cycle that follows an external natural season.

Cycle names and durations are worldbuilding decisions, not automatically Earth defaults.

## 4. Season phase

```yaml
season_phase:
  phase_id: null
  cycle_id: null
  label: null
  ordinal: null
  expected_start_window: null
  expected_end_window: null
  current_state: EXPECTED
  previous_phase_id: null
  next_phase_id: null
  overworld_variant_refs: []
  expected_phenology_refs: []
  recurring_event_refs: []
```

A phase describes broad recurring context. It does not itself grant combat modifiers.

## 5. Calendar, climate and weather are separate

Use this causal chain when relevant:

```text
world calendar
    ↓
regional season phase
    ↓
regional climate expectation
    ↓
actual observed weather
    ↓
overworld presentation / route state / ecology
    ↓
optional validated AutoPTU battlefield weather
```

The chain may branch. A winter phase can exist without snow. An unusual storm can occur outside the expected season. A warm day does not change the season.

## 6. Climate expectation

```yaml
climate_expectation:
  expectation_id: null
  region_id: null
  season_phase_id: null
  temperature_band: null
  precipitation_band: null
  wind_band: null
  visibility_band: null
  notable_expected_conditions: []
  evidence_source_ids: []
  confidence: null
```

These are world/ecology expectations, not PTU battle effects.

Avoid fake scientific precision unless Ouros canon has actual measurement data.

## 7. Actual weather observation

```yaml
weather_observation:
  observation_id: null
  location_id: null
  observed_at_world_time: null
  condition_tags: []
  measurement_ids: []
  observer_or_station_ids: []
  confidence: null
  source_refs: []
```

The narrative system can state that rain, snow, heat, fog or wind was observed.

It cannot infer mechanical battlefield Weather unless the battle engine receives and validates a separate authoritative weather state.

## 8. Phenology object

Phenology tracks the timing of recurring biological/environmental events.

```yaml
phenology_pattern:
  pattern_id: null
  subject_refs: []
  location_ids: []
  phenomenon_type: null
  expected_window: null
  trigger_hypothesis_ids: []
  historical_observation_ids: []
  confidence: provisional
  current_status: UNKNOWN
  current_observation_ids: []
```

Candidate `phenomenon_type` values:
- BLOOMING
- FRUITING
- LEAF_FALL
- THAW
- FREEZE
- MIGRATION_ARRIVAL
- MIGRATION_DEPARTURE
- NESTING
- ROOST_GATHERING
- HIBERNATION_ENTRY
- HIBERNATION_EMERGENCE
- SPAWNING
- MOLTING_OR_FORM_CHANGE only when source-supported
- POLLINATOR_ACTIVITY
- PREDATOR_ACTIVITY
- RESOURCE_PULSE
- OTHER_OBSERVED_CYCLE

Phenology records what the world expects and what has been observed. It does not invent species mechanics.

## 9. Phenological observation

```yaml
phenology_observation:
  observation_id: null
  pattern_id: null
  observed_at: null
  location_id: null
  observer_ids: []
  evidence_ids: []
  observed_stage: null
  disturbance_context_id: null
  confidence: null
```

A first observation cannot establish a long-term cycle by itself.

Repeated observations, historical records and research can strengthen confidence.

## 10. Seasonal anomaly

An anomaly compares observation against an established expectation.

```yaml
seasonal_anomaly:
  anomaly_id: null
  expectation_ref: null
  observation_refs: []
  anomaly_type: null
  magnitude_band: null
  confidence: null
  suspected_cause_ids: []
  confirmed_cause_ids: []
  affected_system_refs: []
```

Candidate anomaly types:
- EARLY
- LATE
- ABSENT
- PROLONGED
- OUT_OF_RANGE
- UNUSUAL_LOCATION
- UNUSUAL_ABUNDANCE
- UNEXPECTED_WEATHER

Hard rule:

No expected baseline means no anomaly claim. The first year of data is observation, not proof that something is wrong.

## 11. Seasonal overworld variants

A known location can have variant state without becoming a duplicate map identity.

```yaml
seasonal_location_variant:
  location_id: null
  phase_id: null
  visual_tags: []
  traversal_state_changes: []
  service_state_changes: []
  encounter_ecology_changes: []
  npc_schedule_changes: []
  accessible_subareas: []
  inaccessible_subareas: []
  mechanics_review_required: true
```

Examples:
- a shallow channel freezes and becomes visually crossable;
- leaf accumulation exposes a route;
- a high pass closes;
- a ferry changes schedule;
- a market moves indoors;
- a seasonal research station opens;
- nesting temporarily restricts one path;
- an old dungeon entrance becomes accessible after thaw.

Any movement, hazard or battle effect requires separate validation.

## 12. Seasonal ecology integration

Wild encounter ecology can read the seasonal layer.

```yaml
seasonal_ecology_rule:
  ecology_rule_id: null
  location_id: null
  species_or_collective_refs: []
  phase_requirements: []
  time_band_requirements: []
  phenology_requirements: []
  abundance_effect: null
  behavior_context: null
  provenance_refs: []
  confidence: null
```

Do not use generic rules such as `Ice types increase in winter` unless authored encounter ecology supports that location/species relationship.

## 13. Wild collective integration

A collective may have seasonal movement without being teleported by the calendar.

```yaml
collective_season_transition:
  collective_id: null
  expected_departure_window: null
  expected_arrival_window: null
  route_refs: []
  prerequisite_world_states: []
  observed_transition_ids: []
  current_confidence: null
```

If a corridor is blocked, the expected migration may fail, reroute or become an anomaly. The calendar does not override current route state.

## 14. Agriculture integration

Agricultural cycles should reference seasonal expectations rather than inventing fixed growth math.

```yaml
seasonal_cultivation_context:
  site_id: null
  cycle_id: null
  suitable_phase_ids: []
  expected_activity_windows: []
  observed_condition_ids: []
  disruption_ids: []
  mechanical_yield_ref: null
```

Season state can determine when work is narratively relevant. Exact Berry growth, yields and food mechanics remain PTU/Caelo/implementation data.

## 15. Recurring event rule

Public events can be bound to calendar or ecological signs.

```yaml
recurring_event_rule:
  recurring_event_id: null
  recurrence_type: null
  calendar_window: null
  phenology_trigger_refs: []
  institution_trigger_refs: []
  minimum_world_state: []
  suppression_conditions: []
  prior_edition_refs: []
  next_candidate_window: null
```

Candidate recurrence types:
- FIXED_CALENDAR
- SEASON_WINDOW
- PHENOLOGY_TRIGGERED
- INSTITUTION_SCHEDULED
- CONDITIONAL_RECURRING

An event can be delayed or canceled by world state. Recurrence is not guaranteed magic.

## 16. Edition continuity

Recurring festivals, migrations and competitions should query prior editions.

Potential carryover:
- previous winners;
- safety changes;
- route modifications;
- remembered incidents;
- ecological timing history;
- former organizers;
- sponsorship changes;
- player traditions;
- public controversies;
- records and commemorations.

This connects directly to the Public Memory, Event & Legacy layer.

## 17. Anti-FOMO policy

Ouros is a persistent RPG, not a live-service calendar treadmill.

Rules:

1. Core character progression should not depend on logging in during a narrow real-world date.
2. A missed seasonal event may advance world state, but important consequences should remain discoverable through records, NPC memory and follow-up content.
3. Recurring opportunities should return when fiction supports recurrence.
4. Personal arcs may use delayed alternatives when missing a window would otherwise erase the player's authored trajectory.
5. Rare seasonal content can exist, but scarcity should serve world coherence rather than engagement pressure.
6. Offline players should not lose Pokémon, homes, relationships or irreversible personal assets solely because a seasonal timer elapsed unless an explicitly accepted system governs that risk.

## 18. Offline advancement

World time advancement needs a central policy.

```yaml
offline_time_resolution:
  elapsed_real_time: null
  elapsed_world_time: null
  policy_ref: null
  clocks_advanced: []
  recurring_events_processed: []
  ecological_transitions_processed: []
  protected_player_state_ids: []
  summarized_outputs: []
```

Do not individually simulate every NPC and wild Pokémon while no chunks are loaded.

Use coarse state transitions and materialize detail when a relevant location becomes active again.

## 19. Multiplayer temporal consistency

All players in one world should read the same canonical world date.

Player-specific differences may exist in:
- knowledge of the date/event;
- whether the player witnessed a transition;
- personal invitations;
- unlocked access;
- private research results.

They should not receive contradictory canonical seasons for the same loaded region unless an explicit supernatural/world-state effect exists.

## 20. Daylight and schedules

NPC, service and encounter availability can use time bands.

```yaml
temporal_availability:
  subject_id: null
  location_id: null
  valid_phase_ids: []
  valid_time_bands: []
  exceptions: []
  current_availability: null
  source_refs: []
```

Routine unavailable periods should not automatically become quests.

Schedules become playable when they intersect a decision, deadline, investigation, transport dependency or character goal.

## 21. Seasonal information surfaces

Players should learn seasonal state through the world, not only a HUD.

Possible surfaces:
- vegetation and snow cover;
- daylight changes;
- Pokémon behavior;
- local sayings;
- weather stations;
- migration reports;
- route notices;
- market inventories;
- research bulletins;
- event preparation;
- transport schedules;
- soundscape changes;
- NPC clothing and routines when authored.

A UI calendar may summarize information already knowable in-world.

## 22. Science integration

Researchers can maintain long-term timing datasets.

Useful research questions:
- Did this migration arrive earlier than prior years?
- Is flowering now mismatched with pollinator activity?
- Does thaw timing correlate with route instability?
- Is a seasonal form appearing outside its historical window?
- Are winter storms increasing in duration?

Generated hypotheses must remain separate from world truth until evidence supports them.

## 23. Crisis integration

A seasonal baseline makes crises more legible.

Examples:
- a storm inside the normal storm season may be severe but expected;
- an early freeze may create preparedness problems;
- a late thaw may delay a route opening;
- drought persisting beyond its expected phase can become a regional problem.

The crisis layer owns emergency lifecycle. This layer only supplies temporal context and expectations.

## 24. Travel integration

Routes and transport can expose seasonal service variants.

```yaml
seasonal_service_variant:
  service_id: null
  phase_id: null
  schedule_variant_ref: null
  route_variant_ref: null
  capacity_state: null
  suspension_conditions: []
```

No travel speed, carrying capacity, Surf/Fly rule or Mountable eligibility is invented here.

## 25. Dungeon integration

Seasonality can create return-value in persistent dungeons.

Examples:
- thaw reveals an entrance;
- flood season fills a lower chamber;
- nesting season makes one wing ecologically sensitive;
- winter exposes tracks or frozen access;
- vegetation opens/closes routes;
- a recurring ritual changes public access without changing supernatural truth.

Tactical hazards remain separate.

## 26. Encounter implementation boundary

Seasonal narrative state may change why an encounter happens, who is present and what the overworld looks like.

It may not automatically change:
- damage;
- Accuracy;
- Move frequency;
- movement cost;
- status conditions;
- Weather effects;
- terrain effects;
- Ability behavior;
- item behavior;
- Trainer Feature triggers.

Those belong to PTU/Caelo and AutoPTU.

## 27. Encounter contract A — Frostline Crossing

Narrative premise:
A normally wet crossing has frozen during a cold phase. The players need to investigate unusual tracks beyond it while local wildlife uses the same route.

Full version:
- validated frozen/winter battlefield state if PTU/Caelo provides one;
- terrain-dependent movement where authoritative;
- possible breaking/unstable zones only if explicitly supported;
- tactical AI aware of safe/unsafe ground if such policy exists.

Reduced version:
- overworld visually shows frozen conditions;
- route geometry uses a reviewed static arena with ordinary blockers/costs already legal in Java;
- investigation happens before/after a standard encounter;
- no scripted slipping, cold damage or ice breakage.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED for ported slice
- complete movement including push/pull/knockback/interception/forced movement: not required in reduced; BLOCKING for any full version that uses sliding/forced displacement
- core calculations: VERIFIED primitives
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL if cold/status interaction is ever used
- terrain/weather/hazards/zones/reactions: BLOCKING for the intended rich version
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING if used
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

## 28. Encounter contract B — Migration Corridor Bottleneck

Narrative premise:
A recurring wild collective migration reaches a corridor that has narrowed since the previous year because of construction and erosion.

Full version:
- tactical objective based on CLEAR_ROUTE / WITHDRAW / PROTECT rather than simple defeat;
- several groups entering/leaving the tactical space;
- objective-aware AI that prefers movement or escape over fighting;
- interception/forced movement only where legal;
- world writeback to collective route state.

Reduced version:
- players investigate and modify the corridor in overworld state;
- a standard legal encounter represents one stressed subgroup;
- retreat/migration outcome is resolved narratively from authoritative battle result plus overworld choices, not fake battle AI.

Key blockers:
- complete movement including interception/forced movement;
- AI tactical policy;
- objective-state support;
- Minecraft adapter/playback.

## 29. Encounter contract C — Storm-Season Relay

Narrative premise:
A communications relay on a high ridge must be inspected during the region's expected storm period after its reports become inconsistent.

Full version:
- battlefield weather/hazard zones if supported;
- lifecycle-timed weather effects;
- ACTIVATE_OBJECT or PROTECT objective;
- tactical AI and adapter events for the relay/weather state.

Reduced version:
- storm exists as overworld/visual context only;
- relay interaction occurs outside AutoPTU;
- any battle uses static geometry and legal ordinary rules;
- no lightning damage, wind displacement or weather bonuses are scripted outside the engine.

Key blockers:
- terrain/weather/hazards/zones/reactions;
- objective interaction;
- AI tactical policy;
- adapter/playback.

## 30. Promotion gates

A seasonal encounter may move from reduced to full only when:

- the exact PTU/Caelo environmental rule is identified;
- Python oracle behavior is pinned where applicable;
- Java supports the exact family through authoritative runtime state;
- tests cover timing/order/interaction required by the encounter;
- adapter events can render the state without owning the rule;
- content review confirms the seasonal mechanic fits the location and ecology.

A weather calculation helper or one terrain-cost test is not sufficient evidence for the whole environmental family.

## 31. Implementation order

Recommended order for narrative/world-state implementation:

1. authoritative world calendar object;
2. region cycle definitions;
3. time-band projection;
4. seasonal location variants;
5. phenology patterns and observations;
6. recurring-event binding;
7. ecology/agriculture/travel readers;
8. offline coarse advancement;
9. anomaly detection after enough history exists;
10. adapter visualization hooks;
11. tactical seasonal effects only after AutoPTU readiness permits them.

## 32. Canon boundary

Before this layer becomes canon, Ouros must decide:

- how fast fictional time passes;
- whether time advances while nobody is online;
- how many regional cycle models exist;
- whether one global calendar is used;
- what counts as a year/season in-world;
- which annual festivals and institutions actually exist;
- whether climate trends are part of authored regional history;
- which seasonal forms/behaviors from Pokémon canon are represented by Cobblemon and PTU data;
- how missed seasonal opportunities are handled.

Until those decisions are made, this file is architecture only.