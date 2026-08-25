# Rangeland Managed Seasonal Movement & Monitoring Protocol

Status: PROPOSED EXTENSION. NON-CANON.

Authority: this protocol extends `grasslands-grazing-rangeland-ecology-layer.md` from Pass 79. It does not create a second grassland/rangeland authority.

## Scope

Pass 79 already owns grassland systems, grazing units, managed herds, range-use plans, forage observations, grazing-pressure revisions, congregation hotspots, herd-route revisions and range-condition assessments.

Pass 163 adds a narrower longitudinal protocol for two gaps inside that authority: adaptive monitoring of timing/frequency/duration/distribution, and managed seasonal movements between range-use areas.

Land Tenure still owns use/access/passage authority. Water layers own water truth. Flora and Soil own vegetation/soil truth. Wildlife Migration owns wild migration. Pokémon Agency owns individual identity/custody/agency. Working Pokémon owns institutional assignments.

## Adaptive use monitoring

Do not reduce grazing management to presence or absence. Link a `RANGE_USE_PLAN` to an ordered series of episodes and reviews.

```yaml
managed_use_episode:
  episode_id: null
  range_use_plan_id: null
  managed_herd_ref: null
  grazing_unit_refs: []
  planned_window: null
  observed_start: null
  observed_end: null
  frequency_context_ref: null
  distribution_observation_refs: []
  waterpoint_use_refs: []
  forage_observation_refs: []
  deviations: []
  state: planned
```

Suggested states: planned, active, paused, redirected, ended_early, completed, not_confirmed, cancelled.

The episode records what happened. It does not itself decide ecological consequence.

### USE_DISTRIBUTION_OBSERVATION

```yaml
use_distribution_observation:
  observation_id: null
  episode_id: null
  grazing_unit_id: null
  observed_at: null
  method_ref: null
  effort_ref: null
  use_class: unknown
  estimated_group_band: null
  exact_pokemon_entity_ids: []
  evidence_refs: []
  confidence: null
```

Suggested classes: observed_high, observed_moderate, observed_low, not_detected, not_surveyed, unknown.

`not_detected` never means `absent` without stronger evidence.

### WATERPOINT_USE_OBSERVATION

```yaml
waterpoint_use_observation:
  observation_id: null
  episode_id: null
  waterpoint_ref: null
  water_state_ref: null
  access_permission_ref: null
  observed_use_band: null
  surrounding_condition_refs: []
  source_refs: []
```

A congregation around water is evidence of use, not automatic evidence of degradation, distress or overgrazing.

### ADAPTIVE_RANGE_REVIEW

```yaml
adaptive_range_review:
  review_id: null
  range_use_plan_id: null
  episode_refs: []
  forage_observation_refs: []
  grazing_pressure_revision_refs: []
  soil_state_refs: []
  water_state_refs: []
  wildlife_overlap_refs: []
  care_or_agency_refs: []
  findings: []
  unresolved_questions: []
  proposed_plan_change_refs: []
  confidence: null
```

Timing, frequency, duration and distribution remain separately reviewable. A management change can improve one objective while leaving another uncertain.

## Managed seasonal movement

Pass 79 already has `HERD_ROUTE_REVISION`. Pass 163 adds an event record for an actual seasonal movement using such a route.

```yaml
seasonal_managed_move:
  move_id: null
  managed_herd_ref: null
  range_use_plan_ref: null
  herd_route_revision_ref: null
  origin_grazing_unit_refs: []
  destination_grazing_unit_refs: []
  expected_window: null
  observed_departure: null
  observed_arrival: null
  staging_site_refs: []
  waterpoint_refs: []
  passage_permission_refs: []
  exact_pokemon_entity_ids: []
  wildlife_migration_overlap_refs: []
  deviation_refs: []
  state: expected
```

Suggested states: expected, preparing, departed, in_transit, staged, detoured, split, partially_arrived, arrived, returned, cancelled, unknown.

Managed seasonal movement is not Wild Migration. A managed herd is not a tactical hive mind. A split does not prove disobedience. A known individual retains its `pokemon_entity_id` throughout.

## Rest and recovery of land use

Pass 79 already supports `rest_status`. This protocol can attach a versioned review window to that state.

```yaml
range_rest_review:
  rest_review_id: null
  grazing_unit_id: null
  rest_started_at: null
  intended_review_at: null
  objective_refs: []
  followup_forage_refs: []
  followup_soil_refs: []
  followup_wildlife_refs: []
  decision: continue|resume_use|modify_plan|unknown
```

This is land-management language. It has no relationship to PTU healing, HP, Injuries, Fatigue or Status.

## Chronicle behavior

Routine seasons may be compressed. Expand the record when movement timing changes, a route is blocked, a waterpoint changes distribution, wild migration overlaps, an individual stops or separates, a monitoring method contradicts prior assumptions, or a plan revision creates a durable consequence.

Institutional competence may make future seasons quieter. Successful management should sometimes remove quests.

## Minecraft boundary

Minecraft can project managed groups, shelters, fences, troughs, route markers and vegetation presentation. Loaded entities cannot determine herd size or grazing pressure. Block state cannot determine permissions, water quality, forage condition, range recovery or tactical terrain.

## PTU guardrails

Do not map herd membership to Pack Mon/shared initiative; Gogoat/Skiddo lore to Mountable or willingness; Wooloo presence to authorized fleece collection; trampling to Rough Terrain/Slowed/Tripped; fences to forced movement; dung to Poisoned; drought/forage shortage to Fatigue or stat loss; rest status to healing; waterpoints to Water Terrain; rotational use to spawn/XP/stat bonuses.

Any exact Move, Ability, Item, Trainer Feature or environmental mechanic requires independent PTU/AutoPTU/Caelo verification.