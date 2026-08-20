# Wildfire, Fire Ecology & Landscape Recovery Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

Pass: 64
Date: 2026-08-20

## Purpose

This layer gives Ouros a persistent model for fire as both a hazard and an ecological process.

The existing crisis system remains responsible for emergency coordination. Conservation remains responsible for stewardship decisions. Meteorology remains responsible for observed/forecast atmospheric state. Freshwater remains responsible for catchments and water movement.

This layer connects them through fire-specific state.

The core rule is simple: a fire is not one boolean and a burned forest is not one endpoint.

Ouros should distinguish ignition, active burning, smoke, burn severity, refugia, suppression, scar state, regrowth, post-fire hydrology and longer-term fire regime.

## 1. Separate the important truths

Keep these states independent:

- actual fire state: where active burning exists;
- ignition observations: what was seen near the beginning;
- cause hypotheses: what actors believe started the fire;
- smoke state: where smoke/haze is observed;
- response state: containment, access and suppression activity;
- burn-severity state: how strongly each patch changed;
- refugia state: unburned/lightly affected areas within or adjacent to the scar;
- ecological response: displacement, regrowth and habitat change;
- watershed response: runoff, ash/sediment and later erosion risk;
- public belief: what residents/media believe happened;
- mechanical state: what AutoPTU actually applies inside battle.

A Fire-type Pokémon near an ignition point is evidence of presence, not evidence of cause.

A smoky town is not necessarily inside the fire perimeter.

A blackened tile is not automatically a PTU hazard.

## 2. Fire event schema

```yaml
fire_event:
  fire_event_id: null
  status: OBSERVED
  first_observation_event_ids: []
  ignition_area_ids: []
  cause_hypothesis_ids: []
  active_front_ids: []
  smoke_footprint_ids: []
  affected_patch_ids: []
  response_operation_ids: []
  access_restriction_ids: []
  displaced_collective_ids: []
  care_signal_ids: []
  infrastructure_impact_ids: []
  fire_scar_id: null
  watershed_followup_ids: []
  recovery_program_ids: []
  public_information_ids: []
  chronicle_refs: []
  canon_status: proposed
```

Possible statuses:

- OBSERVED
- ACTIVE
- ESCALATING
- HOLDING
- CONTAINED
- NO_ACTIVE_FLAME
- RECENT_SCAR
- RECOVERY
- LONG_TERM_MONITORING
- CLOSED_RECORD

These are world-state labels only. They create no PTU rules.

## 3. Ignition evidence and cause hypotheses

```yaml
ignition_observation:
  observation_id: null
  observed_at: null
  location_id: null
  observer_id: null
  observation_type: null
  content: null
  confidence: null
  media_record_ids: []

fire_cause_hypothesis:
  hypothesis_id: null
  fire_event_id: null
  proposed_cause_type: null
  evidence_for_ids: []
  evidence_against_ids: []
  status: OPEN
  author_actor_id: null
  reviewed_at: null
```

Candidate cause types are descriptive:

- LIGHTNING
- VOLCANIC_OR_GEOTHERMAL
- INFRASTRUCTURE_FAILURE
- ACCIDENTAL_HUMAN_ACTIVITY
- DELIBERATE_IGNITION
- POKEMON_ACTIVITY
- UNKNOWN
- MULTIPLE_OR_COMPOUND

The generator must never assign blame because one source is narratively convenient.

## 4. Active fronts

Large fires should use coarse fronts or sectors rather than individual burning blocks.

```yaml
fire_front:
  front_id: null
  fire_event_id: null
  location_patch_ids: []
  observed_at: null
  activity_state: ACTIVE
  direction_claim: null
  severity_claim: null
  response_priority: null
  source_observation_ids: []
```

Front geometry is operational world state.

It is not a tactical grid hazard until projected through an explicit encounter contract.

## 5. Smoke footprint

Smoke should be represented independently from flame.

```yaml
smoke_footprint:
  smoke_id: null
  fire_event_id: null
  affected_location_ids: []
  observation_window: null
  intensity_labels: []
  visibility_observation_ids: []
  health_signal_ids: []
  transport_impact_ids: []
  observatory_impact_ids: []
```

Smoke can alter narrative/world operations when those systems have authored policies.

Examples:

- public event rescheduled;
- air observation canceled;
- ferry/aviation-like service reviewed;
- health surveillance notices an unusual cluster;
- astronomy observation quality falls.

Do not apply Accuracy, Evasion, Blindness, Poisoned or suffocation mechanically without exact PTU/Caelo rules plus engine support.

## 6. Burn-severity mosaic

Use patches rather than one scar-wide state.

```yaml
burn_patch:
  patch_id: null
  fire_scar_id: null
  location_geometry_ref: null
  severity_class: UNKNOWN
  severity_evidence_ids: []
  prefire_habitat_state_ref: null
  current_habitat_state_ref: null
  refugia_status: NONE
  regrowth_stage: null
  monitoring_program_ids: []
```

Suggested descriptive severity classes:

- UNBURNED
- VERY_LOW
- LOW
- MODERATE
- HIGH
- UNKNOWN

These labels must not imply tactical damage.

## 7. Fire refugia

Unburned or lightly affected areas can become important after a large event.

```yaml
fire_refugium:
  refugium_id: null
  patch_ids: []
  observed_value_claim_ids: []
  current_collective_ids: []
  access_pressure_ids: []
  protection_review_ids: []
```

A refugium can become:

- temporary wildlife concentration area;
- research priority;
- restricted restoration buffer;
- route-planning constraint;
- source of later recolonization observations.

Do not assume every Pokémon seen there permanently relocated.

## 8. Fire regime

A location should be able to carry an authored long-term relationship with fire.

```yaml
fire_regime_profile:
  regime_id: null
  location_or_ecosystem_ids: []
  authored_expectation: null
  known_history_event_ids: []
  expected_frequency_claim: null
  expected_severity_pattern_claim: null
  seasonal_window_claims: []
  ecological_dependency_claim_ids: []
  fire_sensitivity_claim_ids: []
  uncertainty_notes: []
```

The generator must not invent exact return intervals from real ecosystems.

Possible authored profiles include:

- fire-adapted open woodland;
- infrequent-fire wet forest;
- grassland with recurring low-intensity disturbance;
- alpine zone where fire is unusual;
- urban-wildland edge with strong suppression history.

These are original Ouros ecology decisions when promoted to canon.

## 9. Planned fire and stewardship

Planned landscape fire requires an explicit project and responsible actors.

```yaml
planned_fire_project:
  project_id: null
  stewardship_area_id: null
  objective_ids: []
  responsible_actor_ids: []
  authority_source_ids: []
  weather_window_requirements: []
  preparation_actions: []
  exclusion_or_refugia_areas: []
  monitoring_plan_ids: []
  abort_conditions: []
  result_observation_ids: []
  review_id: null
```

A planned burn can be canceled, modified or produce unexpected outcomes.

This schema is procedural and original. It must not replicate real Indigenous cultural-burning practices.

## 10. Suppression and response

Crisis owns response coordination. This layer stores fire-specific operational facts.

Possible response records:

- road closure;
- defensive line;
- water point;
- temporary wildlife-exit corridor;
- protected facility;
- lookout/observation post;
- evacuated patch;
- contained sector;
- hotspot follow-up.

A successful response action changes the fire-event state only if the authored simulation says it does.

Using a Water-type Move in a battle must not silently reduce the regional fire front.

## 11. Ecological displacement

Wildfire can interact with wild collectives through explicit events.

```yaml
fire_displacement_event:
  event_id: null
  fire_event_id: null
  collective_or_population_id: null
  source_patch_ids: []
  destination_observation_ids: []
  status: OBSERVED
  duration_claim: null
  return_observation_ids: []
```

Valid outcomes can include:

- temporary concentration near water;
- use of unburned refugia;
- movement into settlement edges;
- fragmentation of a known collective;
- no detectable displacement;
- delayed return during regrowth.

Never infer that fleeing wild Pokémon are aggressive.

## 12. Post-fire succession

Recovery should be versioned over time.

```yaml
post_fire_recovery_patch:
  patch_id: null
  fire_scar_id: null
  current_stage: RECENT_SCAR
  stage_observation_ids: []
  vegetation_change_ids: []
  habitat_structure_change_ids: []
  wildlife_observation_ids: []
  intervention_ids: []
  next_review_clock_id: null
```

Candidate descriptive stages:

- RECENT_SCAR
- EARLY_REGROWTH
- STRUCTURAL_RECOVERY
- LATE_RECOVERY
- CHANGED_STABLE_STATE
- UNKNOWN

Ouros should not assume the endpoint is identical to the pre-fire landscape.

## 13. Natural recovery versus intervention

Keep spontaneous recovery separate from restoration work.

```yaml
recovery_observation:
  observation_id: null
  patch_id: null
  observed_change: null
  intervention_related: UNKNOWN
  evidence_ids: []
```

A restoration project may help, do nothing measurable, create a tradeoff or require revision.

The world must preserve what was done and why.

## 14. Post-fire watershed coupling

Fire scars can emit state into the freshwater layer.

```yaml
post_fire_watershed_risk:
  risk_id: null
  fire_scar_id: null
  catchment_ids: []
  burn_patch_ids: []
  slope_or_connection_claims: []
  rainfall_trigger_observation_ids: []
  runoff_observation_ids: []
  sediment_or_ash_observation_ids: []
  downstream_asset_ids: []
  current_status: MONITOR
```

Possible downstream consequences:

- turbidity observation;
- treatment-plant load;
- reservoir sediment concern;
- fish/wildlife observation change;
- stream closure review;
- debris-flow warning;
- erosion-control project.

None of these creates PTU damage by itself.

## 15. Fire and buildings

Architecture owns structural versions.

Fire can emit:

- damage observation;
- unsafe-access claim;
- temporary closure;
- demolition/rebuild proposal;
- preserved ruin state;
- adaptive-reuse opportunity after recovery.

The fire layer does not calculate building HP.

## 16. Fire and public memory

Large fires can create durable memory:

- anniversaries;
- memorials;
- changed route names;
- revised building codes or response plans;
- remembered refuge sites;
- archived maps of old fire perimeters;
- disagreements about cause;
- stories of recovery.

Public memory remains separate from cause truth.

## 17. Fire and Pokémon-specific claims

Species lore can inform hypotheses and observation plans.

It cannot automatically create mechanics.

Examples:

- a Fire-type Pokémon may inhabit recently burned terrain;
- a Grass-type species may be observed during regrowth;
- a Water-type species may gather near refuge water;
- a Pokémon may repeatedly appear near response infrastructure.

Each is observation/world ecology until exact PTU state says otherwise.

## 18. Minecraft projection

Minecraft/Cobblemon may present:

- smoke/particle zones;
- charred terrain variants;
- burned structures;
- temporary barriers;
- response camps;
- regrowth stages;
- altered wild-Pokémon presence;
- signage;
- closed/reopened roads.

Server world state remains authoritative.

Loaded fire blocks are presentation/simulation inputs, not automatically the canonical fire perimeter.

## 19. Battle projection contract

Any battle near a fire must freeze a revisioned snapshot.

```yaml
fire_battle_projection:
  projection_id: null
  fire_event_id: null
  source_revision: null
  arena_id: null
  static_geometry_refs: []
  approved_mechanical_effect_ids: []
  visual_only_fire_refs: []
  world_state_writeback_rules: []
```

Narrative fire outside the grid may remain visual only.

A battle must never create new PTU rules because Minecraft has flame blocks nearby.

## 20. Encounter contract A — Firebreak Ridge

Narrative premise:

Responders need to inspect a ridge line while displaced wild Pokémon are using the same corridor.

Full version needs:

- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING if actors must withdraw through lanes;
- core calculations — VERIFIED;
- action economy / initiative — VERIFIED;
- full turn / round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain / weather / hazards / zones / reactions — BLOCKING for moving fire/smoke/heat zones;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features / perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for avoid-fire/withdraw/protect goals;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

Resolve the fire front before battle. Use one static safe corridor as arena geometry. Keep active flame and smoke outside tactical mechanics. If wild Pokémon fight, use a conventional legal encounter and write retreat/displacement back through world state after resolution.

## 21. Encounter contract B — Ash Creek Crossing

Narrative premise:

Rain after a recent fire has changed a creek crossing and responders need to inspect downstream risk while wild Pokémon occupy the area.

Full version may require:

- complete movement — BLOCKING for current/displacement;
- terrain/weather/hazards/zones/reactions — BLOCKING for runoff/debris zones;
- full lifecycle — PARTIAL if hazards evolve by round;
- tactical AI — BLOCKING for reach-exit/withdraw/protect goals;
- Minecraft playback — BLOCKING.

Reduced version:

Hydrology resolves before battle. Freeze the crossing geometry and current water level. Sediment, ash and debris are world-state observations. Use ordinary battle rules only if conflict actually occurs.

## 22. Encounter contract C — Refuge Edge

Narrative premise:

An unburned patch is temporarily holding many displaced Pokémon. Responders need information without turning the refuge into a mass battle.

Preferred current implementation:

This is primarily an observation/conservation scenario.

If a battle starts, project only the actual participants into a static arena. Keep the larger collective outside the grid.

Future full version could require:

- complete movement/interception — BLOCKING;
- zones/reactions — BLOCKING;
- tactical AI for escape/avoidance — BLOCKING;
- adapter/playback — BLOCKING.

## 23. Anti-grind and pacing rule

Do not generate a battle for every burning patch, injured Pokémon or restoration task.

Expand a fire-related scene when it contains a meaningful decision, uncertainty, access problem, ecological consequence, rescue need or validated combat encounter.

Routine monitoring, hotspot checks and repeated measurements should compress when nothing changed.

## 24. Hard guardrails

The generator must not invent:

- tactical wildfire spread;
- per-round fire propagation;
- smoke penalties;
- heat damage;
- environmental Burned;
- firefighting DCs;
- water-volume extinguishing math;
- wildfire immunity by Pokémon type;
- structure HP/fire resistance;
- special capture rules for displaced Pokémon;
- regrowth multipliers;
- post-fire rare-spawn bonuses;
- fuel-load combat stats;
- weather-driven fire damage;
- ash Poisoned effects.

Exact mechanics require PTU/Caelo source validation and Java implementation evidence.

## 25. Canon promotion checklist

Before any fire-regime or wildfire concept enters canon:

1. Confirm the location and ecosystem already exist or approve them together.
2. Define whether fire is expected, rare or historically altered there.
3. Separate ignition truth from actor hypotheses.
4. Define responsible institutions without importing real-world legal authority.
5. Review any culturally specific fire stewardship for originality and sensitivity.
6. Define spatial patch granularity suitable for Minecraft.
7. Validate downstream freshwater and infrastructure dependencies.
8. Validate every proposed tactical effect against PTU/Caelo and current Java contracts.
9. Preserve unburned refugia and uncertainty where appropriate.
10. Record recovery as versioned history rather than restoring an old snapshot.

## Conclusion

The main value of this layer is continuity.

A wildfire can begin as a meteorology/crisis event, become a wildlife-care and route problem, leave a severity mosaic, alter a catchment months later, create a restoration program, change future ecology and remain in public memory years later.

That entire chain can exist without requiring AutoPTU-Java to simulate wildfire until the tactical families are ready.