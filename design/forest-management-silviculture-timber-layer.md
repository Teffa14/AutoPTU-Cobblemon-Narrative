# Forest Management, Silviculture & Timber Provenance Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanical effect is established here.

Pass: 92

## Purpose

This layer gives Ouros persistent state for managed forests, forestry projects, access routes, timber provenance and regeneration. It coordinates existing Forest Canopy, Flora, Decomposition, Soil, Freshwater, Wildfire, Workplaces, Material Culture, Road Ecology and Conservation layers without replacing them.

## Core separation

Keep separate:

- forest identity;
- current forest structure;
- management intent;
- approved plan;
- treatment zones;
- work actually completed;
- material removed;
- retained trees/deadwood;
- road and landing state;
- post-work observations;
- regeneration trajectory;
- timber provenance;
- public interpretation;
- tactical PTU state.

A project can finish operationally while ecological monitoring remains open.

## Persistent objects

### MANAGED_FOREST_UNIT

```yaml
managed_forest_id: null
name: null
forest_canopy_unit_ids: []
flora_unit_ids: []
catchment_ids: []
road_segment_ids: []
settlement_ids: []
management_institution_ids: []
history_refs: []
canon_status: proposed
```

### FOREST_MANAGEMENT_PLAN

```yaml
plan_id: null
managed_forest_id: null
valid_from: null
valid_to: null
objectives: []
retention_area_refs: []
production_area_refs: []
monitoring_requirements: []
source_refs: []
status: draft|reviewed|approved|superseded|withdrawn
```

### FORESTRY_PROJECT

```yaml
project_id: null
managed_forest_id: null
plan_id: null
project_type: inventory|thinning|selective_harvest|regeneration_harvest|road_work|restoration|planting|monitoring|other
status: proposed|authorized|scheduled|active|paused|completed_operationally|under_assessment|closed
start_time: null
end_time: null
authority_refs: []
workplace_refs: []
finance_refs: []
```

### FORESTRY_TREATMENT_ZONE

```yaml
treatment_zone_id: null
project_id: null
spatial_ref: null
treatment_intent: retain|thin|harvest|plant|monitor_only|road|landing|buffer|restoration|other
valid_from: null
valid_to: null
```

A treatment intent never creates PTU Terrain by itself.

### TREE_RETENTION_RECORD

Use this only for trees important enough to remain persistent entities.

```yaml
retention_record_id: null
project_id: null
tree_entity_id: null
reason_refs: []
status: retained|damaged|fallen|removed_later|unknown
history_refs: []
```

### HARVEST_OPERATION_RECORD

```yaml
operation_id: null
project_id: null
observed_start: null
observed_end: null
crew_refs: []
equipment_refs: []
planned_zone_refs: []
actual_zone_refs: []
material_batch_ids: []
incident_refs: []
observation_refs: []
```

### TIMBER_BATCH

```yaml
timber_batch_id: null
source_project_id: null
source_forest_id: null
source_zone_ref: null
harvested_at: null
landing_ref: null
custody_history_refs: []
transport_refs: []
processing_refs: []
current_location_ref: null
material_class: null
```

Do not simulate every log. Preserve individual identity only when provenance matters.

### FOREST_ACCESS_FEATURE

```yaml
access_feature_id: null
managed_forest_id: null
feature_type: road|skid_trail|landing|temporary_bridge|worker_camp|gate|other
spatial_ref: null
created_by_project_id: null
status: active|temporary|closing|closed|rehabilitating|repurposed|unknown
history_refs: []
```

### POST_HARVEST_ASSESSMENT

```yaml
assessment_id: null
project_id: null
assessed_at: null
reviewer_ids: []
plan_compliance: null
residual_structure_notes: []
soil_observation_refs: []
water_observation_refs: []
road_observation_refs: []
regeneration_observation_refs: []
wildlife_observation_refs: []
followup_actions: []
confidence: null
```

### FOREST_REGENERATION_TRAJECTORY

```yaml
regeneration_id: null
managed_forest_id: null
project_id: null
baseline_ref: null
pathway: natural|assisted|planted|mixed|unknown
state: adequate|patchy|delayed|failed_or_uncertain|mixed|not_yet_assessed
observation_refs: []
followup_due: null
```

## Lifecycle

Recommended coarse sequence:

1. demand or management need appears;
2. inventory and survey;
3. proposal/review;
4. treatment zones designated;
5. access plan;
6. operation;
7. timber or other material enters provenance chain;
8. temporary access is closed, retained or repurposed;
9. post-harvest assessment;
10. regeneration and habitat monitoring;
11. later plan revision when evidence supports it.

Demand should come from Public Works, Housing, Industry, Disaster Recovery, Material Culture or another system. Forest Management does not create demand merely to generate content.

## Handoffs

To Forest Canopy: canopy gaps, retained-tree state and tree removals.

To Flora: regeneration observations, planting cohorts and seed-source provenance.

To Decomposition: retained slash, snags and downed wood.

To Soil: disturbed landings, compacted access and erosion observations.

To Freshwater: riparian geometry, road drainage and sediment observations.

To Wildfire: fuels-treatment proposals, fire-access routes and post-fire project state.

To Material Culture: timber-batch provenance.

To Workplaces: crews, staffing, shifts and qualifications.

To Road Ecology: road creation, closure, repurpose and crossing implications.

## Player-facing loops

Useful activities include survey, mapping, marking, wildlife observation, worker support, provenance investigation, road rehabilitation, post-work review and multi-year regeneration monitoring.

Routine operations should compress. Expand a scene when a decision, anomaly, dependency, conflict or milestone matters.

## Pokémon guardrails

A Pokémon may use, avoid or investigate a work site. It may occupy retained trees or return to an old route. Those observations do not prove ownership, hostility, consent, employment, leadership or ecological causality.

Trevenant lore can support species-specific observation hooks. It does not establish forest-wide control or an anti-forestry rule.

## Minecraft projection

Minecraft may show treatment markers, machinery, roads, landings, stacked timber, retained-tree tags, closed trails, worker camps and regeneration plots.

The server-side graph remains authoritative for project phase, provenance and ecological interpretation. Chunk reload must not restore a superseded forest revision.

## Battle boundary

Forestry world state may explain why an encounter occurs. It never creates battle effects by itself.

### Timber Landing Interruption

Premise: wild Pokémon enter an active landing and work stops.

Full version needs moving-site hazards, evacuation lanes, objective-aware AI and semantic playback.

Reduced version:

- workers evacuate before combat;
- machinery is shut down;
- the arena is fixed;
- only real combatants enter AutoPTU;
- work delay and provenance update afterward.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including forced movement/interception: BLOCKING for full version;
- terrain/weather/hazards/zones/reactions: BLOCKING for full version;
- AI tactical policy: BLOCKING for full version;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

### Riparian Buffer Survey

Premise: field observations no longer match the current work map near a stream.

Reduced version keeps survey, buffer and water state in overworld and uses a normal static encounter only if conflict occurs.

Full version additionally needs objective movement, environment mechanics, tactical AI and adapter/playback.

### Regeneration Plot Night Watch

Premise: repeated disturbance at a young plot needs observation before managers decide what it means.

Reduced version handles observations outside combat and uses a standard battle only if a confrontation actually begins.

Full version needs multiple moving actors, protect/observe objectives, non-KO withdrawal behavior and supported environmental zones.

## Permanent capability map

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
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## Forest-specific blockers

`OVERWORLD_MANAGED_FOREST_STATE`

`OVERWORLD_FORESTRY_PROJECT_GRAPH`

`OVERWORLD_TIMBER_PROVENANCE`

`OVERWORLD_FOREST_ACCESS_HISTORY`

`OVERWORLD_POST_HARVEST_ASSESSMENT`

`OVERWORLD_REGENERATION_TRAJECTORY`

`FORESTRY_TO_SOIL_HANDOFF`

`FORESTRY_TO_FRESHWATER_HANDOFF`

`FORESTRY_TO_COBBLEMON_PROJECTION`

`FORESTRY_TO_BATTLE_SNAPSHOT`

## Canon questions

- Which Ouros regions contain working forests before players arrive?
- Who owns, manages or stewards them?
- Which institutions authorize projects?
- Which timber types and material traditions exist?
- Which forests are production, mixed-use, protected or unmanaged?
- Which roads and mills predate the campaign?
- Which Pokémon have authored relationships with managed forests?
- How much state advances offline?
- How can player construction consume timber provenance?
- Which PTU/Caelo Skills, Features and Capabilities govern forestry-related actions?

Until those questions are authored or mechanically verified, this layer remains world-state architecture only.