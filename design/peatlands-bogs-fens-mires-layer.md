# Ouros Peatlands, Bogs, Fens & Mires Layer — Pass 88

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

This layer models persistent peat-forming wetlands across Freshwater, Soil, Conservation, Road Ecology, Wildfire, Flora, Science, Archaeology, Travel, Infrastructure and Minecraft projection.

It does not define PTU marsh terrain, bog movement, sinking, mud penalties, water damage, smoke, fire damage, poison, drowning, Naturewalk, Survival DCs or Cobblemon spawn bonuses.

## Purpose

Peatlands preserve long environmental histories. Drainage, water-table change, decomposition, subsidence, fire, rewetting and vegetation response can unfold over years.

The existing Freshwater layer remains authoritative for catchments, surface-water reaches and groundwater connections. Soil remains authoritative for general soil condition and erosion. Wildfire owns active fire events. Conservation owns stewardship and protected-area decisions. This layer owns peatland-specific identity, hydrologic interpretation, peat condition and restoration history.

## Core separations

Keep these concepts independent:

- visible wetland surface;
- verified peat presence;
- peatland type assessment;
- source of water;
- water-table state;
- drainage infrastructure;
- peat condition;
- vegetation observations;
- subsidence observations;
- fire involvement;
- restoration intervention;
- restoration outcome;
- public belief;
- tactical PTU state.

Mud does not prove peat.

Dark water does not prove pollution.

A site labeled “bog” on a tourist map does not establish hydrologic classification.

Rewetting does not automatically mean restoration succeeded.

## 1. PEATLAND_SYSTEM

```yaml
peatland_system:
  peatland_id: null
  approved_name: null
  known_aliases: []
  parent_freshwater_system_refs: []
  groundwater_refs: []
  soil_land_unit_refs: []
  conservation_refs: []
  road_infrastructure_refs: []
  vegetation_unit_refs: []
  wildfire_refs: []
  archaeology_refs: []
  current_type_assessment_id: null
  current_hydrology_revision_id: null
  current_condition_revision_id: null
  restoration_project_ids: []
  observation_ids: []
  access_refs: []
  minecraft_projection_ref: null
  canon_status: proposed
```

The same peatland keeps its identity after drainage, fire, ditch blocking, boardwalk construction or vegetation change.

## 2. PEATLAND_TYPE_ASSESSMENT

The classification is an assessment with evidence, not a visual tag.

```yaml
peatland_type_assessment:
  assessment_id: null
  peatland_id: null
  assessed_at: null
  proposed_type: unknown
  water_source_interpretation: unknown
  nutrient_source_interpretation: unknown
  evidence_refs: []
  method_refs: []
  confidence: null
  assessor_ids: []
  supersedes_ref: null
```

Candidate descriptive types:

- BOG
- FEN
- FORESTED_PEATLAND
- SHRUB_PEATLAND
- SEDGE_PEATLAND
- PEAT_POOL_COMPLEX
- MODIFIED_PEATLAND
- UNKNOWN

These labels are narrative/scientific. They do not create PTU terrain.

A fen may be groundwater-supported. A bog may depend primarily on precipitation. Ouros should not infer either solely from vegetation or water color.

## 3. PEAT_EXTENT_REVISION

Peat distribution can be uncertain and can be exposed or lost over time.

```yaml
peat_extent_revision:
  revision_id: null
  peatland_id: null
  valid_from: null
  mapped_extent_ref: null
  depth_class_by_zone: {}
  confidence_by_zone: {}
  observation_refs: []
  excavation_or_core_refs: []
  supersedes_ref: null
```

Depth classes should remain coarse unless a scientific project specifically needs measurements.

Possible classes:

- TRACE_OR_UNCERTAIN
- SHALLOW
- MODERATE
- DEEP
- UNKNOWN

Peat depth does not become fall depth or movement cost.

## 4. PEAT_HYDROLOGY_REVISION

```yaml
peat_hydrology_revision:
  revision_id: null
  peatland_id: null
  valid_from: null
  water_table_class_by_zone: {}
  surface_saturation_class_by_zone: {}
  groundwater_support_claim_refs: []
  precipitation_dependency_claim_refs: []
  surface_flow_refs: []
  drainage_feature_refs: []
  control_structure_refs: []
  observation_refs: []
  interpretation_refs: []
```

Candidate coarse water-table classes:

- ABOVE_SURFACE
- NEAR_SURFACE
- SHALLOW_BELOW_SURFACE
- LOW
- VERY_LOW
- UNKNOWN

These classes are world-state descriptors only.

No PTU status, movement penalty or damage follows automatically.

## 5. PEATLAND_OBSERVATION

```yaml
peatland_observation:
  observation_id: null
  peatland_id: null
  zone_ref: null
  observed_at: null
  observer_ids: []
  observation_type: null
  observed_value: null
  units_or_class: null
  method_ref: null
  equipment_ref: null
  raw_record_refs: []
  uncertainty: null
  provenance_refs: []
```

Candidate observation types:

- WATER_LEVEL
- PEAT_DEPTH
- SURFACE_ELEVATION
- VEGETATION_COVER
- MOSS_COVER
- SEDGE_COVER
- SHRUB_COVER
- OPEN_WATER_EXTENT
- SURFACE_CRACKING
- SUBSIDENCE_MARKER
- FIRE_SCAR
- CHARRED_PEAT_OBSERVATION
- DITCH_FLOW
- BOARDWALK_CONDITION
- POKEMON_USE
- NESTING_OR_FORAGING_USE
- WATER_CHEMISTRY
- TEMPERATURE

Observation and interpretation remain separate.

## 6. DRAINAGE_FEATURE

Drainage can be historical, active, accidental or partially disconnected.

```yaml
peat_drainage_feature:
  drainage_feature_id: null
  peatland_id: null
  feature_type: null
  infrastructure_ref: null
  construction_or_origin_ref: null
  current_physical_state: unknown
  current_flow_state: unknown
  current_management_state: unknown
  connected_zone_refs: []
  road_refs: []
  hydrology_effect_claim_refs: []
  observation_refs: []
  intervention_history_refs: []
```

Candidate types:

- DITCH
- CUT
- CANAL
- SPOIL_BANK
- ROAD_DRAIN
- CULVERT
- OLD_EXTRACTION_TRENCH
- WATER_CONTROL_CHANNEL
- UNKNOWN

Do not label every ditch harmful by default.

Some may be legacy infrastructure, current flood management, habitat features or partially inactive.

## 7. WATER_CONTROL_STRUCTURE

Infrastructure layer owns the physical asset. This layer records peatland-specific hydrologic role.

```yaml
peat_water_control_link:
  link_id: null
  peatland_id: null
  infrastructure_asset_ref: null
  target_zone_refs: []
  intended_function: null
  operation_state_ref: null
  expected_hydrology_claim_refs: []
  monitoring_refs: []
  observed_response_refs: []
```

Candidate functions:

- RAISE_WATER_LEVEL
- REDUCE_DRAINAGE
- REDISTRIBUTE_FLOW
- PROTECT_INFRASTRUCTURE
- MAINTAIN_ACCESS
- RESTORE_SHEET_FLOW
- EXPERIMENTAL
- UNKNOWN

A gate being closed does not prove the water table rose as intended.

## 8. PEAT_CONDITION_REVISION

Avoid a single universal “peatland health” number.

```yaml
peat_condition_revision:
  revision_id: null
  peatland_id: null
  valid_from: null
  surface_integrity_by_zone: {}
  decomposition_claims: []
  subsidence_claims: []
  vegetation_state_refs: []
  fire_susceptibility_claims: []
  hydrology_refs: []
  observation_refs: []
  scientific_interpretation_refs: []
```

A site can have improved water level and still show legacy subsidence.

A site can support wetland vegetation while a drainage channel remains active.

## 9. SUBSIDENCE_OBSERVATION

```yaml
peat_subsidence_observation:
  subsidence_observation_id: null
  peatland_id: null
  benchmark_ref: null
  measured_at: null
  elevation_or_change: null
  method_ref: null
  prior_comparison_ref: null
  cause_hypothesis_refs: []
  confidence: null
```

Slow surface lowering can affect:

- boardwalk elevation;
- drainage gradients;
- road approaches;
- archaeology exposure;
- vegetation patterns;
- flood susceptibility.

It does not create tactical sinking automatically.

## 10. PEAT_FIRE_INVOLVEMENT

Wildfire owns the fire event itself.

This layer stores verified peat-specific involvement.

```yaml
peat_fire_involvement:
  involvement_id: null
  wildfire_event_ref: null
  peatland_id: null
  verified_peat_combustion: unknown
  affected_zone_refs: []
  depth_or_severity_claim_refs: []
  observation_refs: []
  smoke_refs: []
  hydrology_after_refs: []
  surface_change_refs: []
  recovery_refs: []
```

Smoke is not proof of below-surface peat combustion.

A peat-fire observation does not apply Burned, smoke damage or hidden hazard tiles in battle.

## 11. REWETTING_PROJECT

```yaml
peat_rewetting_project:
  project_id: null
  peatland_id: null
  governance_or_stewardship_refs: []
  baseline_revision_refs: []
  objective_refs: []
  intervention_refs: []
  infrastructure_refs: []
  expected_mechanism_claims: []
  monitoring_plan_refs: []
  implementation_event_ids: []
  followup_observation_ids: []
  review_ids: []
  current_state: proposed
```

Possible states:

- PROPOSED
- UNDER_REVIEW
- PILOT
- ACTIVE
- PARTIALLY_IMPLEMENTED
- MONITORING
- ADJUSTED
- COMPLETE_WITH_MONITORING
- SUSPENDED
- ABANDONED

“Complete” means the physical intervention ended. It does not prove ecological recovery.

## 12. RESTORATION_REVIEW

```yaml
peat_restoration_review:
  review_id: null
  project_id: null
  reviewed_at: null
  baseline_comparison_refs: []
  water_table_response: unknown
  vegetation_response: unknown
  subsidence_response: unknown
  fire_risk_interpretation: unknown
  infrastructure_side_effect_refs: []
  ecological_side_effect_refs: []
  unresolved_questions: []
  recommendation_refs: []
```

Mixed outcomes are valid.

One zone can recover faster than another.

## 13. PEAT EXTRACTION / HISTORIC CUTTING

Material Culture, Workplaces and Governance own economic/legal context.

This layer records physical peat removal history.

```yaml
peat_extraction_history:
  extraction_history_id: null
  peatland_id: null
  zone_refs: []
  activity_period_refs: []
  extraction_type: unknown
  operator_or_claim_refs: []
  remaining_cut_geometry_refs: []
  drainage_refs: []
  archaeology_refs: []
  current_use_refs: []
```

Historic extraction can leave pools, cuts, tracks or drainage patterns long after the industry ends.

Do not invent modern extraction as a default regional practice.

## 14. ARCHAEOLOGY AND PRESERVATION

Peat can preserve long histories, but discoveries must stay evidence-driven.

```yaml
peat_archaeology_context:
  context_id: null
  peatland_id: null
  discovery_ref: null
  stratigraphic_or_depth_context_ref: null
  water_table_context_ref: null
  custody_refs: []
  preservation_observation_refs: []
  interpretation_refs: []
```

The Archaeology layer remains authoritative for excavation, interpretation and stewardship.

A peatland must not procedurally generate intact ancient artifacts merely because “peat preserves things.”

## 15. BOARDWALK / ACCESS STATE

Travel, Accessibility and Infrastructure own route/service status.

```yaml
peat_access_profile:
  access_profile_id: null
  peatland_id: null
  route_refs: []
  current_public_access: unknown
  research_access: unknown
  seasonal_constraints: []
  maintenance_refs: []
  water_level_dependency_refs: []
  conservation_dependency_refs: []
  verified_at: null
```

A wet boardwalk is not automatically PTU slippery terrain.

## 16. POKÉMON USE OBSERVATIONS

Species-specific observations can accumulate without becoming mechanics.

```yaml
peat_pokemon_use_observation:
  observation_id: null
  peatland_id: null
  species_or_entity_ref: null
  collective_ref: null
  observed_behavior: null
  zone_ref: null
  observed_at: null
  environmental_context_refs: []
  evidence_refs: []
  interpretation_refs: []
```

Examples may include:

- repeated Wooper movement through a wetland corridor;
- Ducklett foraging around a bog-moss patch;
- a persistent individual using the same pool;
- absence from a previously regular survey route.

Do not infer motivation, ownership, preferred Trainer, capture desire or tactical behavior.

## 17. PEATLAND KNOWLEDGE MODEL

The Chronicle should preserve:

- what the peatland actually did;
- what was measured;
- how people classified it at the time;
- what restoration was attempted;
- what later evidence changed the interpretation.

A historical map can say “bog” while a later groundwater survey reclassifies the site as a fen. Both records remain valid historical artifacts.

## 18. MINECRAFT PROJECTION

Minecraft is presentation and interaction, not authority.

A peatland projection can include:

- coarse wet/dry visual variants;
- pools;
- boardwalks;
- ditches;
- weirs;
- moss/sedge/shrub palettes;
- charred patches;
- survey wells;
- monitoring stations;
- restricted-access signs;
- restoration works.

Minecraft block state must not determine:

- peat depth;
- bog/fen classification;
- water-table truth;
- environmental hazards;
- PTU Terrain;
- Pokémon spawn probability;
- restoration success.

## 19. OFFLINE ADVANCEMENT

Peatland state should advance coarsely.

Candidate slow clocks:

- seasonal water-table revision;
- drought response;
- ditch/control-structure operation;
- restoration monitoring windows;
- vegetation observations;
- subsidence checkpoints;
- fire-recovery follow-up.

Do not simulate every hour of groundwater movement.

Major changes should be event-driven or observation-driven.

## 20. ANTI-EXPLOIT RULES

Players must not be able to manipulate rare spawns by placing/removing water or moss blocks.

A proposed flow:

world intervention
→ server-valid hydrology change
→ coarse peatland revision
→ ecological observation/assessment
→ reviewed population response
→ controlled Cobblemon projection

Loaded entities never define population truth.

## 21. CONNECTIONS TO EXISTING OUROS LAYERS

### Freshwater

Owns catchments, groundwater/surface-water networks and regional hydrology.

Peatlands reference those systems rather than duplicating them.

### Soil

Owns general soil condition, erosion and sediment transfer.

Peatland layer owns organic-soil accumulation/decomposition history specific to the peat-forming wetland.

### Wildfire

Owns ignition, fire fronts, smoke and crisis lifecycle.

Peatland layer owns verified peat combustion involvement and post-fire peat condition.

### Road Ecology

Roads, culverts and spoil banks can alter hydrology or wildlife routes. Road Ecology owns the linear infrastructure/ecological connectivity relationship.

### Conservation

Owns stewardship, protected-area status, management plans and access policy.

### Flora

Owns vegetation units, flowering, recruitment and succession.

### Archaeology

Owns excavation, claims and interpretation of preserved cultural material.

### Science

Owns hypotheses, methods, datasets, replication and publication.

### Crisis

Owns emergency response to peat fire, sudden access failure or flooding.

## 22. ENCOUNTER CONTRACT — REWETTING WEIR INSPECTION

Narrative premise:

A restoration project reports that one peatland sector is responding differently from the others. Players inspect a water-control structure, recent field records and Pokémon use around the site.

FULL version may include:

- water-level zones changing during the encounter;
- interactable weir/gate objective;
- protected technician/researcher;
- route closure/opening based on field state;
- environmental reactions;
- tactical AI that understands PROTECT_OBJECT / REACH_CONTROL / WITHDRAW.

Required permanent capability families:

- targeting/footprints/range/LoS: VERIFIED for static geometry;
- base movement legality: VERIFIED for implemented surface movement;
- complete movement including interception/forced movement: BLOCKING if water/route changes displace or intercept;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:

The server resolves inspection and gate operation before combat. If a battle occurs, a single stable boardwalk/dry-platform geometry is frozen for the encounter. Water level does not change during battle. Technicians remain outside the grid. The narrative premise remains restoration inspection.

## 23. ENCOUNTER CONTRACT — SMOLDERING PEAT EDGE

Narrative premise:

Smoke remains near a previously burned peatland. The question is whether active peat combustion persists, whether smoke has another source, and whether a safe survey can continue.

FULL version may require:

- hidden or revealed unsafe zones;
- changing smoke/visibility;
- dynamic fire/hazard progression;
- rescue or withdrawal objective;
- AI capable of avoiding unsafe areas;
- verified environmental status/damage if PTU rules support them.

Dependencies:

VERIFIED:

- targeting/footprints/range/LoS for static geometry only;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- lifecycle;
- damage;
- statuses;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- complete movement if evacuation/interception matters;
- terrain/weather/hazards/zones/reactions;
- tactical AI;
- Minecraft adapter/playback.

REDUCED version:

Wildfire/Crisis resolves the fire perimeter and marks unsafe zones before battle. The party fights only on a verified safe patch if a conflict occurs. Smoke never applies Accuracy, status or damage. Investigation and sampling remain outside the tactical grid.

## 24. ENCOUNTER CONTRACT — FLOATING MAT SURVEY

Narrative premise:

A research route crosses a peatland surface whose apparent stable patches have changed since the last survey. Players must verify access while documenting wildlife use.

FULL version may require:

- unstable surface zones;
- changing safe routes;
- collapse/fall or displacement rules if PTU defines them;
- withdrawal goals;
- wildlife AI that prefers known safe substrate;
- multi-stage pathfinding.

REDUCED version:

The route-finding problem is resolved in exploration/world state using verified Skill/capability rules when available. Any battle begins only after the server chooses a stable tactical patch. The encounter uses static blockers and ordinary movement.

FULL dependencies remain BLOCKING on complete movement, environmental zones/reactions, tactical AI and Minecraft playback.

## 25. RULES SAFETY

This layer must never create by prose alone:

- Rough Terrain;
- Slow Terrain;
- Stuck;
- Tripped;
- Poisoned;
- Burned;
- smoke Accuracy modifiers;
- drowning;
- sinking damage;
- water-current displacement;
- Naturewalk;
- Swim;
- Burrow;
- healing from moss;
- rare encounter bonuses;
- automatic wild aggression.

Those require PTU/Caelo authority and implementation evidence.

## 26. CANON PROMOTION GATE

Before any peatland becomes canon, a human review should establish:

- region and location;
- pre-player physical history;
- authored water sources;
- known drainage/infrastructure history;
- known restoration or extraction history;
- important species/collectives that truly belong there;
- stewardship/institutional relationships;
- whether the “bog/fen” label is confirmed or merely local usage;
- exact mechanics used by encounters;
- Minecraft projection scope.

## Open questions

- Which Ouros regions contain true peat-forming wetlands?
- Which are groundwater-fed fens versus precipitation-dominated bogs or other peatlands?
- Which drainage structures predate the campaign?
- Are any old peat-cutting/extraction areas part of authored history?
- Which Pokémon have regional behavior explicitly tied to these sites?
- How slowly should peatland revisions advance offline?
- What is the exact PTU/Caelo treatment of Wetland, marsh, mud, Naturewalk and Survival?
- Will Java eventually support verified environmental terrain/hazard behavior for these encounters, or will peatland battles always use frozen safe snapshots?

Until those questions are answered, the layer remains proposed systems architecture only.