# Ouros Timekeeping, Clocks & Synchronization Layer

Status: PROPOSED SYSTEMS DESIGN. Not established canon.
Pass: 132
Date: 2026-08-23

## Purpose

Ouros already has calendars, schedules, daily activity, narrative escalation clocks and exceptional time anomalies. It still needs a shared authority for ordinary clock time.

This layer answers questions such as:

- What time standard did this record use?
- Was this clock synchronized when it produced the timestamp?
- How far was it believed to be offset?
- Is a station timetable using the same reference as the traveler’s device?
- If an old timestamp is later corrected, how do we preserve the original record?
- Which time source should Minecraft display?

The layer does not define time zones, daylight-saving rules, atomic-clock technology or any other regional convention as canon. It provides a schema that can support whichever conventions Ouros later adopts.

## Authority boundaries

### This layer owns

- time standards and their revisions;
- local clock instances;
- synchronization events;
- raw timestamp provenance;
- corrected timestamp estimates;
- clock offsets and drift observations;
- schedule time references;
- ordinary clock outages;
- temporal discrepancy investigations;
- presentation profiles for time display.

### Other layers continue to own

- Calendar/Seasonality: dates, annual cycles and phenology.
- Observation/Settlement/Time: narrative escalation clocks and action windows.
- Diel Activity: biological daily activity patterns.
- Rail/Postal/Festivals/etc.: their own schedules and operations.
- Metrology: general calibration and measurement traceability.
- Digital Systems: software logs and data stores.
- Temporal Continuity: time travel, loops, divergent contexts and genuine temporal anomalies.
- AutoPTU: turn order, initiative, duration, delayed effects and battle time.

## Core rule

Never collapse these into one field:

`world chronology -> standard/reference -> local clock -> raw timestamp -> corrected estimate -> displayed time`

Each may be different while referring to the same underlying event.

## 1. Time standard

```yaml
time_standard:
  time_standard_id: null
  name: null
  authority_institution_id: null
  status: proposed
  valid_from_event_id: null
  valid_to_event_id: null
  parent_standard_id: null
  offset_rule: null
  reference_method: null
  source_refs: []
```

Possible uses:

- a town’s historical civic time convention;
- a railway operating standard;
- a regional scientific reference;
- a future interregional shared standard.

Do not author a universal standard until canon review establishes one.

## 2. Standard revisions

```yaml
time_standard_revision:
  revision_id: null
  time_standard_id: null
  effective_from: null
  effective_to: null
  definition_notes: null
  supersedes_revision_id: null
  reason: null
  publication_event_id: null
```

Old revisions remain queryable.

A timestamp made under an old revision remains valid evidence for that historical context.

## 3. Local time rules

```yaml
local_time_ruleset:
  ruleset_id: null
  spatial_scope_ids: []
  valid_from: null
  valid_to: null
  reference_standard_id: null
  display_offset_rule: null
  date_rollover_rule: null
  labels: []
  status: proposed
```

This schema can support future local-time differences without assuming that Ouros uses modern Earth-style time zones.

## 4. Clock sources

```yaml
clock_source:
  clock_source_id: null
  source_type: null
  authority_id: null
  reference_standard_id: null
  operational_state: active
  confidence_band: null
  distribution_channels: []
  last_verified_event_id: null
```

Candidate source types:

- observatory reference;
- civic clock service;
- railway master clock;
- radio time signal;
- network time service;
- portable expedition reference;
- manually maintained local standard.

These are design categories, not canon technology commitments.

## 5. Clock instance

A displayed or logging clock is a persistent object.

```yaml
clock_instance:
  clock_id: null
  asset_id: null
  owner_or_operator_id: null
  location_id: null
  device_type: null
  configured_source_id: null
  local_ruleset_id: null
  operational_state: active
  last_sync_event_id: null
  estimated_offset: null
  offset_uncertainty: null
  drift_assessment: unknown
  power_dependency_ids: []
  communications_dependency_ids: []
```

A clock can remain operational while unsynchronized.

## 6. Synchronization event

```yaml
clock_sync_event:
  sync_event_id: null
  clock_id: null
  timestamp_recorded: null
  reference_source_id: null
  observed_offset_before: null
  adjustment_applied: null
  observed_offset_after: null
  method: null
  technician_or_system_id: null
  evidence_ids: []
```

A synchronization event does not rewrite older records made by the clock.

## 7. Clock offset observation

```yaml
clock_offset_observation:
  observation_id: null
  clock_id: null
  reference_source_id: null
  observed_at_event_id: null
  estimated_offset: null
  uncertainty: null
  method_id: null
  confidence: provisional
```

A single offset observation does not prove a constant offset across all earlier records.

## 8. Raw timestamp

Every important event record should preserve its original time statement.

```yaml
raw_timestamp:
  timestamp_id: null
  source_record_id: null
  clock_id: null
  raw_value: null
  referenced_standard_id: null
  local_ruleset_id: null
  capture_method: automatic
  author_or_system_id: null
  provenance_ids: []
```

Never replace `raw_value` after correction.

## 9. Corrected timestamp estimate

```yaml
corrected_timestamp_estimate:
  estimate_id: null
  raw_timestamp_id: null
  estimated_world_instant: null
  correction_method: null
  offset_evidence_ids: []
  uncertainty_window: null
  confidence: null
  supersedes_estimate_id: null
```

This is an interpretation layer.

The world can later produce a better estimate while preserving the earlier one.

## 10. Schedule time reference

Schedules must say what their times mean.

```yaml
schedule_time_reference:
  schedule_id: null
  owning_system_id: null
  reference_standard_id: null
  local_ruleset_id: null
  publication_revision_id: null
  effective_from: null
  effective_to: null
```

Examples:

- railway departure;
- ferry sailing;
- clinic appointment;
- tournament registration deadline;
- observatory reservation;
- festival procession;
- field survey window.

## 11. Time correction event

```yaml
time_correction_event:
  correction_id: null
  affected_record_ids: []
  correction_basis: null
  old_estimate_ids: []
  new_estimate_ids: []
  approved_by_id: null
  published_event_id: null
```

Corrections are append-only history.

## 12. Temporal discrepancy case

A discrepancy should be investigated before it becomes a plot claim.

```yaml
temporal_discrepancy_case:
  case_id: null
  compared_record_ids: []
  discrepancy_type: null
  observed_difference: null
  hypotheses: []
  evidence_ids: []
  current_assessment: unresolved
  resolved_cause_ids: []
```

Candidate causes:

- unsynchronized clock;
- manual clock setting;
- clock drift;
- power interruption;
- stale schedule;
- communications outage;
- transcription error;
- different local rulesets;
- different historical standard revisions;
- record generated before/after a correction;
- actual unknown cause.

A true temporal anomaly is never the default explanation.

## 13. Clock outage

```yaml
clock_outage:
  outage_id: null
  clock_ids: []
  start_event_id: null
  end_event_id: null
  cause_claim_ids: []
  fallback_reference_ids: []
  downstream_system_ids: []
  recovery_event_ids: []
```

Time continues during an outage.

Systems can continue operating with degraded synchronization, local fallback or manual procedures if their own rules allow it.

## 14. Time display profile

Player-facing formatting is presentation state.

```yaml
time_display_profile:
  profile_id: null
  actor_or_client_id: null
  format: twenty_four_hour
  show_seconds: false
  show_reference_label: false
  countdown_preference: relative
  accessibility_notes: []
```

Changing this profile does not mutate world time.

## 15. Server-authoritative chronology

For persistent multiplayer, world time should originate from server state.

Minecraft client local clocks must not decide:

- day/night world state;
- expiration of permissions;
- train departures;
- migration windows;
- festival dates;
- research timestamps;
- market sessions;
- battle start ordering;
- Chronicle event ordering.

Clients may format and display the server time.

## 16. Time compression

Routine time may be compressed while preserving ordering.

```yaml
time_advance_event:
  event_id: null
  from_world_instant: null
  to_world_instant: null
  reason: travel_compression
  affected_system_ids: []
  advancement_policy_ids: []
```

Each downstream system remains responsible for how it advances across the interval.

This layer never assumes that every system progresses continuously while chunks are unloaded.

## 17. Timestamp comparison rule

Before comparing two records temporally, verify:

1. source clocks are known;
2. reference standards are known or estimated;
3. local rulesets are accounted for;
4. synchronization/offset evidence exists when precision matters;
5. uncertainty windows overlap or do not overlap;
6. any corrections are versioned rather than destructive.

## 18. Schedule conflict rule

When actors miss a connection, distinguish:

- actor arrived late;
- service departed early;
- published schedule was stale;
- clocks disagreed;
- local display used another convention;
- service itself was delayed;
- route/handoff time exceeded the plan.

Do not automatically blame one actor.

## 19. Cross-layer handoffs

### Timekeeping -> Railways

Supplies the reference for timetable publication and event logs.

### Timekeeping -> Postal

Supplies comparable intake, handoff and delivery timestamps.

### Timekeeping -> Emergency Dispatch

Supplies report, dispatch, arrival and handoff chronology.

### Timekeeping -> Astronomy / Meteorology / Science

Supplies timestamp provenance for observations.

### Timekeeping -> Migration / Diel Activity

Supplies event timestamps. Those layers still own biological interpretation.

### Timekeeping -> Digital Systems

Digital logs keep their original device timestamp and reference link.

### Timekeeping -> Archives / Museums / Libraries

Historical time conventions and corrections remain discoverable.

### Timekeeping -> Temporal Continuity

Only hands off when evidence cannot be explained through ordinary clock/synchronization state and a true temporal-context investigation is justified.

## 20. Minecraft projection

Minecraft may render:

- station clocks;
- clock towers;
- wall clocks;
- observatory timing displays;
- relay status indicators;
- schedule boards;
- portable clock interfaces;
- daylight/sky presentation.

Minecraft blocks or client system time never become authoritative chronology.

If a clock block is broken, the `clock_instance` can persist as damaged or absent. Chronicle retains prior timestamps.

## 21. Player-created clocks and shared servers

A player may build a visible clock or timetable if Minecraft permits it.

That does not make it an official time source.

Institutional recognition requires an authored relationship to the governing time standard and clock source.

## 22. No inferred time anomaly

The generator must never escalate ordinary discrepancy directly into:

- time travel;
- a loop;
- Dialga involvement;
- Celebi involvement;
- future knowledge;
- duplicated entities;
- rewound world state.

Use mundane synchronization hypotheses first.

## 23. Battle boundary

This layer is overworld/institutional state.

It does not alter:

- initiative;
- action economy;
- turn phases;
- Round count;
- Move frequency;
- delayed-hit maturity;
- Status durations;
- Weather/Terrain duration;
- Trick Room ordering;
- reaction timing.

Those are owned by AutoPTU.

A battle transcript may reference world timestamps at its start/end, but battle events remain ordered by the battle engine.

## 24. Encounter implementation contracts

### Clocktower Relay Access

Narrative premise:

A regional clock relay loses synchronization after a communications outage. A technician must reach the relay while a separate wildlife disturbance blocks the route.

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED family;
- base movement legality: VERIFIED family;
- complete movement including interception/forced movement: BLOCKING family for a moving technician or route-protection objective;
- core calculations: VERIFIED family;
- action economy/initiative: VERIFIED family;
- full turn/round lifecycle: PARTIAL family;
- full stateful damage pipeline: PARTIAL family;
- status lifecycle: PARTIAL family if any status interaction occurs;
- terrain/weather/hazards/zones/reactions: BLOCKING family if weather or live reaction movement is part of the tactical scene;
- move-specific behavior: PARTIAL family;
- abilities: PARTIAL family;
- items: PARTIAL family;
- Trainer Features/perks: PARTIAL family;
- AI legal-action infrastructure: VERIFIED family;
- AI tactical policy: BLOCKING family for `PROTECT_TECHNICIAN` / `CLEAR_ROUTE`;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:

Resolve technician movement and relay access in world state. Freeze a legal static arena when the wildlife confrontation occurs. After AutoPTU resolves the battle, the technician can perform a synchronization check outside the grid. Winning the battle does not automatically repair or synchronize the clock.

### Station Platform Time Dispute

Narrative premise:

Two platform displays disagree after a local clock fallback. Crowds begin moving toward the wrong platform while an unrelated Pokémon incident creates a safety problem.

FULL version dependencies:

- complete movement/interception: BLOCKING for dynamic crowd clearing;
- AI tactical policy: BLOCKING for `CLEAR_ROUTE`, `WITHDRAW`, `PROTECT`;
- Minecraft/Cobblemon/Craftics playback: BLOCKING for crowd/platform semantics;
- terrain/weather/hazards/zones/reactions: only if a separately validated tactical hazard exists.

REDUCED version:

Railway state stops boarding, staff redirect passengers outside the grid, and the platform is cleared before battle. AutoPTU receives only actual combatants on a static arena. The later investigation compares schedule revision, clock logs and sync state.

### Observatory Timestamp Reconciliation

Narrative premise:

Three instruments recorded the same celestial event under clock references that do not agree.

This is primarily a non-combat investigation.

No battle capability is required unless an independent encounter occurs. The resolution uses Metrology, Astronomy, Science and Timekeeping evidence. A successful investigation can conclude that the records remain uncertain.

## 25. Live engine evidence — Pass 132

AutoPTU-Java inspected head: `aefc058328a9217d634477835a4851d521aaeccb`.

The newest slice applies a narrow reaction escape movement authoritatively. It derives legal reachable tiles from canonical movement state, chooses a safe destination under the frozen contract, moves the combatant and emits a `ShiftResolvedEvent` without consuming a normal Shift action.

This is meaningful progress for reaction movement.

It does not prove:

- generic reaction dispatch;
- interception;
- Push/Pull execution;
- knockback;
- collision resolution;
- movement-triggered hazards;
- moving objectives;
- all reaction permissions/bookkeeping;
- complete forced movement.

The Java README still explicitly lists status controller, terrain, hazards, forced movement and reactions as incomplete, along with full damage, registries, AI policy and Minecraft/Cobblemon integration.

AutoPTU Python inspected head: `29a8e62e24c3e58233ca2c8154a30d796099f90a`.

Its latest visible changes are Career persistence/resilience work and do not change the tactical capability classification.

## 26. Permanent capability classification for this pass

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## 27. PTU/Caelo boundary

The complete project Caelo source corpus was not available as a reliable invocable source in this runtime. Super PTU Online Helper was not exposed as a callable capability.

Do not invent:

- timekeeping Skill checks;
- stopwatch bonuses;
- initiative bonuses from clocks;
- extra actions for precise timing;
- day/night accuracy changes;
- time-based capture modifiers;
- Trick Room extensions;
- temporal Move behavior;
- Legendary time powers.

## 28. Open canon questions

- Does Ouros use one regional standard or multiple local conventions?
- Are there formal time zones, offsets or another system entirely?
- Which institutions maintain trusted time references?
- How advanced are ordinary clocks and network synchronization?
- Which historical settlements used local solar/civic time before transport standardization?
- How quickly does server world time advance relative to real time?
- What happens to shared schedules when no players are online?
- Which clocks are public landmarks before the players arrive?
- How are old timestamps presented when their original time convention is obsolete?
- Which systems require high precision and which only need coarse morning/afternoon/night bands?

## 29. Implementation priority

Recommended order:

1. authoritative server world instant;
2. raw timestamp provenance;
3. schedule time references;
4. clock instances and sync state;
5. corrected timestamp estimates;
6. temporal discrepancy cases;
7. Minecraft clock/display projection;
8. historical/local standard revisions.
