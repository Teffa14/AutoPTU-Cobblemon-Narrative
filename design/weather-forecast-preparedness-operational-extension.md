# Ouros Weather Forecast & Preparedness Operational Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

The Seasonality, Calendar & Phenology layer already owns climate expectations and observed weather. This extension adds the operational information lifecycle around those observations.

The world should be able to remember that a forecast was issued, revised, distributed, acted on and later checked against actual conditions. Different services can respond differently to the same product. A forecast can be useful even when it is uncertain or later wrong.

This layer does not define Ouros climates. It does not create a meteorological agency. It does not implement PTU tactical Weather.

## 1. Authority boundaries

Use these distinct records:

```text
season/climate expectation
        ↓
weather observations
        ↓
forecast product
        ↓
information dissemination
        ↓
preparedness decisions by owner systems
        ↓
actual observed conditions
        ↓
forecast verification / revision history
```

Each arrow can fail or remain incomplete.

A forecast does not own route closure.

A weather station does not own emergency authority.

An event organizer does not own scientific truth.

A Minecraft visual effect does not own PTU Weather.

## 2. Observation network

Reuse `weather_observation` from the Seasonality layer as the evidence object. This extension adds persistent source nodes and health state.

```yaml
weather_observation_node:
  node_id: null
  location_id: null
  status: PROPOSED
  operator_actor_ids: []
  observation_method_refs: []
  coverage_claim_ids: []
  current_operational_state: UNKNOWN
  last_observation_id: null
  outage_record_ids: []
  maintenance_ref_ids: []
  provenance_refs: []
  canon_status: proposed
```

Candidate operational states:

- OPERATING
- DEGRADED
- OFFLINE
- ACCESS_BLOCKED
- DATA_DELAYED
- STATUS_UNKNOWN

These describe information availability. They do not imply physical damage.

A station can be physically intact and offline.

A damaged site may still transmit partial observations.

## 3. Observation methods

Possible methods are descriptive until canonized:

- staffed observation;
- instrument reading;
- remote sensor;
- visual report;
- ship or ferry report;
- mountain post report;
- research camp observation;
- community report routed through a formal process;
- archival comparison.

Do not assume satellites, radar, radio telemetry, internet-connected sensors or other technologies without regional canon.

## 4. Forecast product

```yaml
forecast_product:
  forecast_id: null
  issuer_actor_or_institution_id: null
  issued_at_world_time: null
  spatial_scope_ids: []
  valid_from_world_time: null
  valid_until_world_time: null
  predicted_condition_bands: []
  confidence_band: null
  source_observation_ids: []
  method_claim_refs: []
  revision_of_forecast_id: null
  superseded_by_forecast_id: null
  dissemination_packet_ids: []
  operational_recommendation_ids: []
  verification_record_id: null
  provenance_refs: []
  canon_status: proposed
```

Forecast condition bands should stay broad unless Ouros canon supports precise measurement.

Examples:

- rain likely during part of the window;
- strong wind possible at exposed elevations;
- visibility expected to deteriorate;
- freezing conditions possible overnight;
- storm timing uncertain;
- conditions expected to improve after a broad window.

A forecast is an authored information object. It is not the future world state.

## 5. Confidence without fake probability

Default candidate confidence values:

- LOW
- MODERATE
- HIGH
- CONFLICTING_INPUTS
- INSUFFICIENT_DATA
- NOT_ASSESSED

Do not invent percentages unless the setting and forecasting method actually support calibrated numerical probabilities.

Confidence should describe forecast uncertainty, not character competence or player difficulty.

## 6. Forecast revision

A forecast can change when new evidence arrives.

```yaml
forecast_revision_event:
  revision_event_id: null
  prior_forecast_id: null
  replacement_forecast_id: null
  changed_dimensions: []
  new_evidence_ids: []
  issued_at: null
  distribution_targets: []
  acknowledged_by_actor_ids: []
```

The old forecast remains historically queryable.

Do not silently mutate `valid_until`, predicted conditions or confidence after issue.

This enables fair questions later:

- what did the ferry operator know when it departed?
- did the event team receive the later revision?
- was a trail closed before or after the forecast changed?
- did a researcher rely on an outdated bulletin?

## 7. Weather notice

A forecast can produce a public or operational notice.

```yaml
weather_notice:
  notice_id: null
  issuer_id: null
  forecast_ref_ids: []
  observation_ref_ids: []
  scope_ids: []
  notice_type: null
  effective_from: null
  expires_at: null
  recommendation_text_ref: null
  distribution_channel_ids: []
  acknowledgement_refs: []
  authority_claim_ref: null
  status: ACTIVE
```

Candidate descriptive types:

- INFORMATION
- PREPARE
- TRAVEL_CAUTION
- SERVICE_ADVISORY
- FIELDWORK_CAUTION
- EVENT_CAUTION
- LOCAL_HAZARD_NOTICE

These labels have no automatic legal force.

If Ouros later canonizes formal warning tiers, their powers and thresholds need separate approval.

## 8. Preparedness response

Owner systems record their own responses.

```yaml
weather_preparedness_response:
  response_id: null
  subject_type: null
  subject_id: null
  trigger_forecast_ids: []
  trigger_notice_ids: []
  decision_actor_ids: []
  selected_action_refs: []
  rejected_action_refs: []
  effective_window: null
  rollback_or_review_conditions: []
  outcome_refs: []
  status: PLANNED
```

Potential subjects:

- travel service;
- route;
- public event edition;
- facility;
- storefront;
- courier dispatch;
- research expedition;
- protected area;
- agricultural site;
- residential service;
- temporary worksite.

The response should link back to the actual owner system rather than duplicate its state.

## 9. Response examples

Travel may:

- delay departure;
- reduce service;
- use an already-canon alternative route;
- suspend one segment;
- stage a later inspection.

Temporary events may:

- activate a rain layout;
- move activities indoors;
- close one temporary structure;
- shorten operating hours;
- postpone teardown.

Facility Maintenance may:

- secure exposed equipment;
- schedule a condition check;
- create a post-weather inspection;
- maintain a temporary closure after conditions improve.

Courier may:

- hold a dispatch;
- split a batch;
- redirect to an approved pickup point;
- preserve custody while delivery is delayed.

Conservation may:

- restrict visitors from one vulnerable sector;
- change monitoring plans;
- prepare to observe a known ecological response.

None of these consequences arise directly from the forecast object.

## 10. Actual conditions

Actual conditions continue to use Seasonality’s `weather_observation` records.

Operational systems can aggregate observations into a time-window summary without creating new truth.

```yaml
observed_weather_window:
  window_id: null
  location_scope_ids: []
  start_time: null
  end_time: null
  observation_ids: []
  summary_condition_tags: []
  data_gap_intervals: []
  confidence: null
```

A data gap must remain visible.

“No observation” is not “clear weather”.

## 11. Forecast verification

```yaml
forecast_verification:
  verification_id: null
  forecast_id: null
  relevant_observation_ids: []
  scope_match_state: null
  timing_match_state: null
  condition_match_notes: []
  unverified_dimensions: []
  known_data_gaps: []
  explanatory_claim_ids: []
  review_actor_ids: []
  verification_state: OPEN
```

Candidate states:

- OPEN
- BROADLY_SUPPORTED
- PARTIALLY_SUPPORTED
- NOT_SUPPORTED_BY_AVAILABLE_OBSERVATIONS
- INSUFFICIENT_OBSERVATION
- OUT_OF_SCOPE
- SUPERSEDED_BEFORE_WINDOW

Avoid a single hidden “forecast accuracy” score.

A historical institution may eventually calculate its own metrics, but those require an authored methodology.

## 12. Forecast miss investigation

A miss is a research question, not a misconduct verdict.

Possible claims include:

- station was offline;
- observations arrived late;
- forecast scope was too broad;
- local conditions diverged;
- timing shifted;
- the forecast was superseded;
- an expected weather front weakened;
- an unusual event occurred;
- the available evidence cannot explain the difference.

Each explanation needs evidence and provenance.

## 13. Microclimate profile

Ouros can preserve recurring local divergence without pretending to model full atmospheric physics.

```yaml
microclimate_claim:
  claim_id: null
  location_scope_ids: []
  claimed_pattern: null
  condition_context: []
  supporting_observation_ids: []
  contradictory_observation_ids: []
  confidence: provisional
  source_actor_ids: []
  review_state: OPEN
```

Examples:

- one pass becomes foggy earlier than nearby lowlands;
- a sheltered valley remains calmer than a ridge;
- a coast receives earlier wind shifts;
- a built-up district drains or heats differently.

These are claims until supported.

## 14. Local knowledge integration

A ferry crew, farmer, ranger, resident or shopkeeper may notice recurring signs before a formal bulletin reaches them.

Their observations can become evidence.

Their experience does not automatically establish meteorological authority.

Use Rumor/Testimony lineage when the report is informal. Convert it into a formal observation only when the relevant process records what was actually observed.

## 15. Science integration

Weather can be part of a long-term dataset.

Candidate research questions:

- does a migration repeatedly coincide with one observed weather window?
- does a high pass receive conditions different from the regional forecast?
- did a storm arrive earlier than the local historical window?
- did an observation-node outage create a blind spot?
- are two recurring reports really independent sources?

Science owns causal interpretation.

This layer owns forecast provenance and operational use.

## 16. Crisis integration

Crisis owns emergency activation, rescue, stabilization and recovery.

This extension can supply:

- prior forecast history;
- warning distribution history;
- preparedness actions;
- actual weather observations;
- post-event forecast verification.

Do not retroactively make a forecast “obviously correct” because a crisis occurred.

## 17. Facility and route reopening

Hard rule:

weather ended != infrastructure safe.

After severe conditions, Travel, Facility Maintenance, Public Works, Conservation or another owner may require inspection.

This avoids a common game-state shortcut where rain stopping instantly repairs bridges, clears debris or reopens dangerous trails.

## 18. Minecraft representation

Potential eventual surfaces:

- station instruments or props appropriate to canon technology;
- public forecast board;
- route advisory sign;
- changed NPC routine after an advisory;
- temporary barriers activated by an owner system;
- event rain-plan overlay;
- ferry departure board changes;
- field-team packing state;
- visible station outage or maintenance state;
- a forecast history UI;
- localized rain/fog/snow visuals when adapter support exists.

Minecraft visuals must consume world state. They must not generate tactical PTU effects independently.

## 19. Battlefield weather handoff

A separate bridge is required if observed overworld conditions should become PTU battlefield Weather.

```yaml
battle_weather_handoff:
  battle_id: null
  source_observed_weather_ids: []
  candidate_ptu_weather_state: null
  mapping_rule_ref: null
  mapping_source_ref: null
  mechanics_verified: false
  adapter_verified: false
  applied_battle_weather_state: null
```

No mapping should happen merely because the words “rain”, “sun”, “snow”, “fog” or “wind” appear in world state.

Required questions:

- Does PTU/Caelo define the candidate Weather state?
- Does the exact environmental condition map to it?
- Does AutoPTU implement its lifecycle and effects?
- Are affected Moves, Abilities, Items and Features implemented?
- Can Minecraft/Cobblemon faithfully display the authoritative events?

If any required answer is no, keep the condition as overworld context only.

## 20. Ability and Pokémon guardrail

A Pokémon associated with weather does not automatically forecast it.

A Pokémon used by a weather institution does not automatically gain a job capability.

Type does not prove forecasting, sensing, wind resistance, lightning safety or rescue competence.

Any mechanically relevant behavior must come from validated species lore, Capabilities, Moves, Abilities, Skills, relationship state or explicit world evidence.

## 21. Encounter contract A — Ridgeline Evacuation Window

Narrative premise:

A field team is working beyond an exposed ridge. A revised forecast narrows the safe return window. Wild Pokémon are also moving through the approach, but the cause of that movement is not yet established.

Full intended version:

- weather changes during the encounter;
- visibility or environmental zones matter;
- wind may cause authoritative forced displacement if PTU/Caelo supports it;
- civilians or field staff withdraw across the map;
- protected equipment may matter;
- AI understands retreat/protect/clear-route objectives;
- Minecraft renders the same authoritative weather and movement events.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when gusts, interception or forced displacement matter;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if any exact status is used;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

The forecast and evacuation decision occur entirely in world state. Field staff leave the tactical area before combat. The exposed section closes before the encounter begins. If hostile contact remains, AutoPTU receives one static reviewed arena with no weather modifiers, no gust displacement and no live escort objective. The battle result does not determine whether the ridge is safe afterward; route inspection does.

## 22. Encounter contract B — Weather Station Blackout

Narrative premise:

A remote observation node stops reporting as conditions deteriorate. The players go to determine whether the problem is access, equipment, communications, staffing or another cause. Wild Pokémon near the site may complicate entry without being responsible for the outage.

Full intended version:

- active rain/wind/lightning or another canon condition may create tactical zones;
- equipment can be protected without becoming an ordinary combat target;
- safe cover may change;
- actors can withdraw;
- forced movement/reactions may matter;
- AI can prioritize escape, territorial defense or protection according to validated goals;
- adapter persists node state and battle playback.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/forced movement/interception — BLOCKING when used;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

The current weather remains visual/narrative world state. Any staff evacuate before battle. Investigation establishes the node’s condition through explicit interaction. If a fight occurs, it happens in a sheltered static area using individually verified mechanics. Equipment repair or communications restoration is resolved afterward by the proper owner system.

## 23. Noncombat encounter — Forecast Dispute Review

Premise:

Two services made different decisions from forecasts that appear contradictory. The players reconstruct issue times, geographic scope, revisions, observations and receipt history.

Playable now as narrative/world-state content:

- compare forecast products;
- inspect source observations;
- identify whether the products covered the same place and time;
- check whether one was superseded;
- verify who received each revision;
- compare actual observations afterward;
- record an unresolved explanation when evidence is insufficient.

No battle support is required.

The resolution must not automatically label an actor incompetent, dishonest or negligent.

## 24. Long-term world loop

A weather-information network can become better known over time without becoming omniscient.

Repeated play can accumulate:

- new observation nodes;
- repaired nodes;
- known blind spots;
- local microclimate claims;
- revised distribution practices;
- prior service decisions;
- remembered false alarms;
- remembered successful preparation;
- post-event inspection habits;
- seasonal datasets.

This gives weather institutional memory rather than random environmental decoration.

## 25. Design guardrails

- Forecasts are claims, not future truth.
- Observations require time and place.
- Missing data stays missing.
- Confidence is not a hidden mechanical bonus.
- Forecast misses do not prove wrongdoing.
- Strange weather does not prove a Legendary, supernatural cause or sabotage.
- Weather expertise does not prove closure authority.
- Weather ending does not prove a route or facility safe.
- A warning does not alter PTU stats.
- A Pokémon’s type does not establish occupational competence.
- A weather DB helper in AutoPTU-Java does not establish the complete weather family.
- Minecraft does not invent PTU weather modifiers.
- Do not import weather mechanics from main-series or Mystery Dungeon systems into PTU.
- Preserve revisions and verification history.
- Keep forecast science separate from public rumor.

## 26. Canon promotion gate

Before any weather-network element becomes canon, confirm:

- region and location;
- technology available there;
- institution or actor operating it;
- observation methods;
- forecast terminology;
- dissemination channels;
- authority boundaries;
- expected climate baseline;
- relationship to existing routes/services;
- whether tactical PTU Weather mapping exists;
- whether adapter representation is feasible.

Until then, all schemas and examples in this file remain proposed.