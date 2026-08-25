# Ouros Rangeland, Grazing & Managed Seasonal Movement Layer

Status: PROPOSED SYSTEMS DESIGN. NON-CANON.

## Purpose

This layer owns managed use of grasslands and other forage landscapes across time: planned or customary grazing episodes, forage-use observations, rest periods, waterpoint use, seasonal managed movements and follow-up reviews.

It exists because Ouros already knows whether land may be used, what plants/soil/water are present and how wild populations migrate, but did not have an authority for the managed use process tying those states together.

## Authority boundaries

Land Tenure owns ownership, stewardship, commons, passage permissions and resource-use grants.
Food/Agriculture owns farms, crops and cultivated production.
Flora owns vegetation state. Soil owns soil state. Freshwater, Groundwater and Irrigation own water truth.
Wildlife Migration owns wild migration patterns and episodes.
Wild Collectives owns wild group identity.
Pokémon Agency owns individual identity, custody, partnership and observed cooperation/refusal.
Working Pokémon owns institutional work assignments.
Breeding/Nursery owns directed breeding and Eggs in custody.
Conservation owns ecological restrictions and conservation decisions.
Road Ecology owns road/crossing effects.

Rangeland owns the managed-use episode and its longitudinal monitoring. It must reference, never overwrite, those authorities.

## Core chain

`valid use/access -> current forage/water/soil context -> management plan -> grazing or managed-movement episode -> observed distribution/use -> rest/recovery interval -> follow-up monitoring -> review/revision`

No transition proves the next one occurred.

## Persistent entities

### RANGELAND_UNIT

A stable managed-land identity referencing Land Tenure geometry rather than replacing it.

```yaml
rangeland_unit:
  rangeland_unit_id: null
  land_unit_refs: []
  vegetation_unit_refs: []
  soil_unit_refs: []
  waterpoint_refs: []
  route_refs: []
  management_program_refs: []
  historical_use_refs: []
  current_status: ACTIVE
  provenance_refs: []
```

Candidate statuses: ACTIVE, RESTING, SEASONALLY_UNUSED, RESTRICTED, UNDER_REVIEW, HISTORIC, UNKNOWN.

RESTING is a management state. It is not biological healing.

### GRAZING_MANAGEMENT_PROGRAM

```yaml
grazing_management_program:
  program_id: null
  rangeland_unit_refs: []
  authority_refs: []
  use_permission_refs: []
  subject_group_refs: []
  stated_objectives: []
  monitoring_protocol_refs: []
  schedule_revision_refs: []
  waterpoint_strategy_refs: []
  contingency_refs: []
  status: PROPOSED
```

Objectives remain explicit and may differ: forage availability, vegetation composition, soil protection, wildlife coexistence, route continuity, cultural practice or operational reliability.

### FORAGE_CONDITION_OBSERVATION

```yaml
forage_condition_observation:
  observation_id: null
  rangeland_unit_id: null
  observed_at: null
  location_scope_ref: null
  method_ref: null
  effort_ref: null
  vegetation_state_ref: null
  qualitative_availability: UNKNOWN
  use_evidence_tags: []
  photo_or_sample_refs: []
  observer_ref: null
  confidence: null
```

A short or sparse patch is an observation. Cause remains separate.

### GRAZING_EPISODE

```yaml
grazing_episode:
  episode_id: null
  program_id: null
  planned_window: null
  observed_start: null
  observed_end: null
  subject_group_refs: []
  exact_known_pokemon_entity_ids: []
  rangeland_unit_refs: []
  waterpoint_use_refs: []
  distribution_observation_refs: []
  interruption_refs: []
  deviation_refs: []
  outcome_review_ref: null
  state: PLANNED
```

Candidate states: PLANNED, STARTED, PAUSED, REDIRECTED, SPLIT, COMPLETED, ENDED_EARLY, NOT_CONFIRMED, CANCELLED.

A group split can be operational, ecological or voluntary. Do not infer cause without evidence.

### USE_DISTRIBUTION_OBSERVATION

Records where use was observed or not detected within a surveyed scope. Minecraft path traces are not authoritative evidence.

```yaml
use_distribution_observation:
  observation_id: null
  episode_id: null
  observed_at: null
  zone_ref: null
  observation_method_ref: null
  effort_ref: null
  use_state: UNKNOWN
  estimated_group_band: null
  exact_entity_ids: []
  evidence_refs: []
  confidence: null
```

Use states: OBSERVED_HIGH, OBSERVED_MODERATE, OBSERVED_LOW, NOT_DETECTED, NOT_SURVEYED, UNKNOWN.

NOT_DETECTED is not ABSENT.

### WATERPOINT_USE_RECORD

Water truth stays with the water authority. This record stores managed-use observations only.

```yaml
waterpoint_use_record:
  record_id: null
  waterpoint_ref: null
  episode_id: null
  observed_window: null
  availability_state_ref: null
  access_permission_ref: null
  observed_use_band: null
  queue_or_concentration_note: null
  surrounding_condition_refs: []
  evidence_refs: []
```

A concentration near water does not by itself prove degradation or distress.

### REST_RECOVERY_PERIOD

```yaml
rest_recovery_period:
  rest_id: null
  rangeland_unit_id: null
  starts_at: null
  intended_review_at: null
  objective_refs: []
  access_or_use_restriction_refs: []
  followup_observation_refs: []
  final_review: null
```

The name describes management of land use. It does not alter Pokémon HP, Injuries, Fatigue or Status.

## Managed seasonal movement

### SEASONAL_MANAGED_MOVE

This is deliberately separate from Wild Migration.

```yaml
seasonal_managed_move:
  move_id: null
  management_program_ref: null
  subject_group_refs: []
  exact_entity_ids: []
  expected_window: null
  origin_use_area_ref: null
  destination_use_area_ref: null
  route_revision_ref: null
  staging_site_refs: []
  waterpoint_refs: []
  passage_permission_refs: []
  travel_service_refs: []
  wildlife_migration_overlap_refs: []
  observed_departure: null
  observed_arrival: null
  state: EXPECTED
  deviation_refs: []
```

Candidate states: EXPECTED, PREPARING, DEPARTED, IN_TRANSIT, STAGED, DETOURED, PARTIALLY_ARRIVED, ARRIVED, RETURNED, CANCELLED, UNKNOWN.

If a managed group later becomes wild, feral or otherwise changes status, another authority must establish that transition. This layer does not decide it from location alone.

## Group and individual agency

A managed group is an operational grouping, not a biological hive mind.

Individual Pokémon may have persistent identity, different route histories and different observed responses. A refusal, early stop or separation is recorded as behavior and handed to Pokémon Agency/Care/Working Pokémon as appropriate. It does not reduce Loyalty or create disobedience mechanics.

Species lore may motivate authored roles, but species never substitutes for an individual assessment or PTU rules capability.

## Monitoring and review

### GRAZING_OUTCOME_REVIEW

```yaml
grazing_outcome_review:
  review_id: null
  episode_or_program_ref: null
  forage_observation_refs: []
  soil_state_refs: []
  water_state_refs: []
  wildlife_observation_refs: []
  agency_or_welfare_refs: []
  comparison_baseline_refs: []
  findings: []
  unresolved_questions: []
  management_change_refs: []
  confidence: null
```

Do not collapse several resource objectives into one health number. A program can improve one outcome and worsen or leave uncertain another.

## Multiplayer and Chronicle

Routine episodes can be compressed. Chronicle should expand a season when a route changes, access is disputed, water becomes unavailable, a known individual responds differently, wild migration overlaps, monitoring contradicts expectations or a management revision produces a durable consequence.

Player-founded institutions may propose programs only through the relevant permissions and Pokémon-agency authorities. A player cannot manufacture population truth by loading more entities or placing fences/water blocks.

Offline progression should advance schedules and known institutional actions conservatively. Irreversible ecological conclusions require observations or authored transitions.

## Minecraft projection contract

Allowed direction: authoritative world state -> coarse visual presentation.

Minecraft may show fencing, gates, troughs, shelters, marked routes, grass-height variants or a visible managed group. It must not infer permission, forage condition, group size, overgrazing, welfare, water quality or mechanical terrain from those blocks/entities.

Block break/place actions are observations or requests until the owning world system validates their meaning.

## PTU/mechanical guardrails

Never infer:

- herd -> Pack Mon, shared initiative or coordinated tactical AI;
- Gogoat/Skiddo -> Mountable, carrying capacity or willingness;
- Wooloo -> authorized fleece collection;
- trampling -> Rough Terrain, Slowed or Tripped;
- fence -> forced movement or interception;
- dung -> Poisoned or toxic hazard;
- drought/forage shortage -> Fatigue, Injury or stat loss;
- rest pasture -> healing;
- waterpoint -> Water Terrain;
- short vegetation -> confirmed degradation;
- rotational use -> spawn bonus, XP or stat bonus;
- managed seasonal movement -> Wild Migration.

Any exact Move, Ability, Item, Feature or environmental effect used in a battle must be verified independently against AutoPTU/PTU/Caelo evidence.

## Canon questions left open

Which Ouros regions practice managed grazing or seasonal pastoral movement? Which species/individuals participate voluntarily? Are there historic commons or seasonal-use routes? Which institutions monitor forage and water? Are any material products such as fleece actually part of canon? How are welfare, custody and work roles governed? Which routes predate modern roads or settlements? How much of this state may advance offline?