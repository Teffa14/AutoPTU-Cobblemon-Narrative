# Wildfire, Fire Regimes & Post-Fire Recovery Layer

Status: PROPOSED SYSTEMS ARCHITECTURE. Not established Ouros canon.
Pass: 178
Date: 2026-08-26

## Authority boundary

This layer owns long-term fire ecology and fire-history state.

It does not replace:
- Crisis / Emergency Services for active incident response, evacuation, suppression operations, shelters or responder coordination;
- Meteorology / Climate for weather, forecasts, drought and long-term climate state;
- Air Quality for smoke and aerosol exposure;
- Flora for vegetation condition, recruitment and succession;
- Soil for soil condition, erosion and soil observations;
- Freshwater / Stormwater / Groundwater for runoff, water quality and hydrologic response;
- Wildlife / Migration / Spatial Ecology for animal movement and habitat use;
- Remote Sensing for imagery acquisitions and derived spatial products;
- Conservation for protected-area policy and management authorization;
- Toxicology for exposure to hazardous agents;
- Minecraft/Cobblemon for presentation only.

The layer exists so those systems can refer to the same durable fire history without collapsing their conclusions into one boolean.

## Core principle

A fire event is a physical disturbance with a spatial history. Its ecological effects are heterogeneous and interpreted through later observations.

The authoritative chain is:

`ignition/event identity -> evolving fire footprint -> observed fire effects -> spatial burn-effect zones -> downstream ecological observations -> recovery assessments -> repeated-fire history -> revisable fire-regime assessment`

Each arrow requires evidence or an authored world-state transition.

## Core entities

### FIRE_EVENT

```yaml
fire_event:
  fire_event_id: null
  event_name: null
  ignition_time_interval:
    earliest: null
    latest: null
  end_time_interval:
    earliest: null
    latest: null
  ignition_cause_status: UNKNOWN
  ignition_cause_claim_refs: []
  crisis_id: null
  affected_location_ids: []
  fire_footprint_revision_ids: []
  monitoring_refs: []
  source_refs: []
  canon_state: PROPOSED
```

`ignition_cause_status` may remain `UNKNOWN` permanently. A battle, presence of a Fire-type Pokémon, lightning report, campfire, infrastructure fault or public rumor never establishes cause without supporting evidence.

### FIRE_FOOTPRINT_REVISION

Represents best-known extent during or after an event.

```yaml
fire_footprint_revision:
  revision_id: null
  fire_event_id: null
  valid_time: null
  geometry_ref: null
  source_method: null
  coverage_state: PARTIAL
  confidence: null
  supersedes_revision_id: null
  remote_sensing_product_refs: []
  field_observation_refs: []
```

The footprint can grow during an active event and be revised later after better mapping.

### BURN_EFFECT_ZONE

Stores observed or assessed effects inside the footprint.

```yaml
burn_effect_zone:
  zone_id: null
  fire_event_id: null
  geometry_ref: null
  effect_domain: VEGETATION
  severity_class: null
  assessment_method: null
  observed_at: null
  evidence_refs: []
  interpretation_confidence: null
```

Possible effect domains include vegetation, surface fuels, soil surface and other authored categories. Do not create a universal cross-domain severity number.

### FIRE_HISTORY_UNIT

A stable analysis area such as a watershed, management unit, forest block, grassland or valley.

```yaml
fire_history_unit:
  unit_id: null
  geometry_ref: null
  fire_event_refs: []
  treatment_refs: []
  monitoring_series_refs: []
  regime_assessment_refs: []
```

### FIRE_REGIME_ASSESSMENT

A revisable interpretation of long-term patterns.

```yaml
fire_regime_assessment:
  assessment_id: null
  unit_id: null
  valid_as_of: null
  evidence_window: null
  frequency_assessment: null
  seasonality_assessment: null
  size_pattern_assessment: null
  severity_pattern_assessment: null
  spatial_pattern_assessment: null
  uncertainty_notes: []
  evidence_refs: []
  supersedes_assessment_id: null
```

This is an interpretation, not an immutable property of the map.

### PRESCRIBED_FIRE_PROJECT

```yaml
prescribed_fire_project:
  project_id: null
  authority_id: null
  objective_refs: []
  planned_area_ref: null
  planned_window: null
  prerequisites: []
  approval_state: PROPOSED
  actual_fire_event_id: null
  monitoring_plan_ref: null
  outcome_assessment_refs: []
```

A prescribed fire can be cancelled, partially implemented or completed without meeting every objective.

### FIRE_EFFECT_MONITORING_SERIES

```yaml
fire_effect_monitoring_series:
  series_id: null
  unit_id: null
  plot_or_site_ids: []
  baseline_observation_refs: []
  postfire_observation_refs: []
  treatment_refs: []
  method_revision_refs: []
  continuity_notes: []
```

A method change may reduce comparability without invalidating all earlier observations.

### POSTFIRE_RECOVERY_ASSESSMENT

```yaml
postfire_recovery_assessment:
  assessment_id: null
  fire_event_id: null
  area_ref: null
  domain: VEGETATION
  valid_as_of: null
  observed_trajectory: null
  baseline_ref: null
  uncertainty_notes: []
  evidence_refs: []
```

Use domain-specific downstream observations. This layer must not fabricate recovery metrics owned by Flora, Soil, Water or Wildlife.

## Fire lifecycle handoff

During an active fire:

`Fire Ecology -> creates/updates fire_event and spatial history`

`Crisis -> owns emergency phase and operational jobs`

`Meteorology -> owns weather context`

`Air Quality -> owns smoke exposure`

After stabilization:

`Fire Ecology -> preserves footprint/effects/history`

`Flora/Soil/Water/Wildlife -> record downstream responses`

`Remote Sensing/Photography/Community Science -> provide observations`

`Conservation/Public Works -> decide interventions under their authority`

## Reburns and overlapping events

Never replace an older footprint with a new one.

```yaml
reburn_relation:
  earlier_fire_event_id: null
  later_fire_event_id: null
  overlap_geometry_ref: null
  interval: null
  evidence_refs: []
```

The later event can affect previously burned, recovered, treated or unburned patches differently. Any ecological conclusion requires downstream evidence.

## Prescribed fire workflow

```text
management question
-> objective definition
-> authority / approvals
-> baseline monitoring
-> planned area and window
-> operational execution through Crisis/Emergency if needed
-> actual footprint and effects
-> post-burn monitoring
-> objective assessment
-> management revision
```

A successful operational burn can still miss an ecological objective. A burn that differs from its intended footprint can still produce mixed outcomes rather than binary failure.

## Fire effects versus recovery

Keep these separate:

- area burned;
- observed burn effect or severity;
- mortality/survival;
- vegetation recruitment;
- soil response;
- runoff/erosion;
- wildlife use;
- public access;
- infrastructure state;
- long-term recovery assessment.

One system cannot infer another’s result.

## Observation and uncertainty

Valid observation states include:

- `OBSERVED_DIRECTLY`
- `REMOTE_SENSING_DERIVED`
- `FIELD_VALIDATED`
- `ESTIMATED`
- `INFERRED`
- `NOT_SURVEYED`
- `NOT_DETECTED_WITH_EFFORT`
- `UNRESOLVED`

A blackened patch is not automatically high severity. Green vegetation is not automatically full recovery. A satellite product does not replace field truth where field validation is necessary.

## Public memory and narrative simplification

Public Memory may preserve statements like “the whole valley burned.” Fire Ecology may simultaneously preserve a mosaic of burned, lightly affected and unburned patches.

Both records can be historically meaningful if their provenance remains clear.

## Pokémon ecology guardrails

Species behavior must be authored or supported by observations.

Never infer:

- Fire-type -> fire adapted;
- Grass/Bug-type -> fire vulnerable;
- Water-type -> firefighter;
- Flying-type -> automatic evacuation success;
- Flash Fire -> wildfire immunity;
- Flame Body -> ignition source;
- Heatproof -> smoke/heat immunity;
- Rain Dance -> fire suppression system;
- Sunny Weather -> wildfire state;
- Burned status -> ecological burn injury;
- wild Pokémon presence after fire -> habitat fully recovered.

A surviving Pokémon may be resident, displaced, returning, opportunistically using the site or simply passing through.

## Minecraft projection contract

Minecraft/Cobblemon can render:

- burned vegetation variants;
- charred structures where authored;
- cleared firelines;
- closed roads;
- regrowth stages;
- monitoring plots;
- signage;
- temporary access controls.

Minecraft must not author:

- fire-event cause;
- ecological burn severity;
- recovery state;
- soil sterility;
- wildlife population loss;
- prescribed-fire success;
- smoke exposure;
- PTU Burned status;
- fire spread history from vanilla block ticks;
- fire-regime interpretation.

If Minecraft fire simulation is used for presentation, its spread must be downstream of authoritative world-state instructions or sandboxed so it cannot write ecological truth back into Chronicle.

## Battle handoff

The preferred handoff for most wildfire scenes is:

1. world state resolves the active fire perimeter, evacuations, smoke, civilians and ecological movement;
2. if a combat confrontation remains, choose a tactically stable location;
3. pass only validated combatants and validated tactical environment to AutoPTU;
4. return the battle transcript to world state;
5. continue Crisis/Fire Ecology resolution outside the battle engine.

Do not implement wildfire by creating ad hoc fire tiles in the Minecraft adapter.

## Capability-family rules

If a full encounter requires any of the following, it must declare them explicitly:

- moving flame fronts, dynamic blocked routes, current-like displacement or knockback: `complete movement including push/pull/knockback/interception/forced movement`;
- burning zones, smoke zones, changing visibility, weather phases, environmental reactions or delayed fire spread: `terrain/weather/hazards/zones/reactions`;
- Burned, Poisoned or other PTU conditions: `status lifecycle` plus the exact validated source mechanic;
- Fire Move interactions, secondary effects or special timing: `move-specific behavior`;
- Flash Fire, Flame Body, Heatproof or similar: `abilities`;
- protective gear or consumables: `items`;
- Fire Ace, Weather specialist or Feature interrupts: `Trainer Features/perks`;
- wildlife fleeing, responders escorting, route-clearing or non-hostile objectives: `AI tactical policy`;
- any world-to-battle representation: `Minecraft/Cobblemon/Craftics adapter/playback support`.

Reduced versions should move these processes outside battle whenever the narrative premise survives intact.

## Candidate canon questions

Unresolved until authored:

- Which regions have fire-dependent, fire-sensitive or infrequent-fire ecosystems?
- Which historic fires predate the player campaign?
- Which institutions maintain fire-history records?
- Does Ouros use prescribed fire, and under whose authority?
- Are there community or Indigenous-equivalent authored fire traditions? If so, they must be original Ouros cultures, not renamed real-world traditions.
- Which Pokémon populations have documented fire-related behaviors?
- How much fire-state progression occurs while chunks are unloaded?
- Which post-fire restrictions are public and which protect sensitive habitats?
- Which PTU/Caelo environmental fire rules exist in the final ruleset?

Until answered, all examples remain proposed.