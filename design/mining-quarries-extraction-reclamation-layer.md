# Mining, Quarries, Extraction & Reclamation Layer

Status: PROPOSED SYSTEM DESIGN. Not established Ouros canon.
Date: 2026-08-24

## Purpose

This layer gives Ouros persistent state for mineral/resource extraction projects across exploration, development, operation, care-and-maintenance, closure, progressive rehabilitation, post-closure monitoring and later reuse.

It fills a missing authority between Geology/Subterranean Systems and Manufacturing/Supply Chains.

It coordinates rather than replaces:

- Geology: resource occurrence, rock/mineral interpretation, structural geology;
- Subterranean Systems: natural caves, mine-natural complexes and underground geometry;
- Seismic/Slope/Crisis: physical hazards and incidents;
- Groundwater/Freshwater: water state;
- Soil/Air Quality/Toxicology/Contaminated Land: environmental observations, contamination and exposure;
- Worker Associations/Workplaces: workers, representation and staffing;
- Working Pokémon/Pokémon Agency: Pokémon participation and agency;
- Material Culture: persistent tools/objects;
- Manufacturing: processing/manufacturing after extraction where applicable;
- Supply Chains: stock, freight and inventory after material handoff;
- Paleontology/Archaeology: fossil or cultural finds;
- Land Tenure/Credentials: access and authority;
- Conservation: habitat outcomes;
- Public Memory/Archives/Museums: historical interpretation and preservation;
- PTU/Caelo/AutoPTU: all battle mechanics.

Mining must never become a shortcut for rules the tactical engine does not possess.

## Core separation

```text
geologic occurrence / hypothesis
        ↓
exploration program + observations
        ↓
resource interpretation / feasibility claim
        ↓
project decision + authorized footprint
        ↓
development / workings / infrastructure
        ↓
extraction events + material batches
        ↓
stockpile / processing / freight handoff
        ↓
care & maintenance OR continuing operation
        ↓
closure / decommissioning
        ↓
progressive/final rehabilitation
        ↓
post-closure monitoring + later reuse
```

None of these stages implies the next one automatically.

Discovery is not approval.

Approval is not production.

Production is not saleable inventory until authoritative material handoff occurs.

Shutdown is not abandonment.

Rehabilitation work is not proof of recovery.

## 1. Persistent extraction site

```yaml
extraction_site:
  extraction_site_id: null
  name: null
  site_type: MINE|QUARRY|PLACER|BORROW_PIT|SAND_GRAVEL|UNDERGROUND_OPERATION|SURFACE_OPERATION|MIXED|UNKNOWN
  location_refs: []
  land_unit_refs: []
  geologic_resource_refs: []
  subterranean_system_refs: []
  project_ids: []
  working_area_ids: []
  infrastructure_refs: []
  water_system_refs: []
  environmental_program_refs: []
  worker_organization_refs: []
  public_information_refs: []
  archive_refs: []
  current_operational_state: null
  current_rehabilitation_state: null
  canon_status: proposed
```

The site persists across names, operators, closures and reuses.

A mine can stop extracting while the place remains a workplace for maintenance, monitoring or reclamation.

## 2. Resource occurrence versus extraction project

Geology owns the resource interpretation.

```yaml
resource_occurrence_link:
  link_id: null
  extraction_site_id: null
  geology_resource_ref: null
  target_material_label: null
  evidence_refs: []
  interpretation_revision_ref: null
  confidence: null
```

Mining owns the human/institutional project around that occurrence.

```yaml
extraction_project:
  project_id: null
  extraction_site_id: null
  project_revision: 1
  project_scope_geometry_ref: null
  target_resource_refs: []
  proposed_method_class: null
  current_phase: EXPLORATION|FEASIBILITY|DEVELOPMENT|OPERATING|CARE_AND_MAINTENANCE|CLOSING|REHABILITATING|POST_CLOSURE_MONITORING|COMPLETE|CANCELLED|DEFERRED
  authorized_activity_refs: []
  planned_working_area_ids: []
  closure_objective_refs: []
  proposed_post_mining_use_refs: []
  starts_at: null
  ends_at: null
  decision_refs: []
  evidence_refs: []
```

A project may be cancelled after exploration without creating a mine.

## 3. Exploration program

```yaml
exploration_program:
  exploration_program_id: null
  site_or_region_ref: null
  objective: null
  method_classes: []
  observation_refs: []
  sample_refs: []
  drill_or_test_location_refs: []
  access_authorization_refs: []
  rehabilitation_commitment_refs: []
  starts_at: null
  ends_at: null
  outcome_state: IN_PROGRESS|INSUFFICIENT_EVIDENCE|RESOURCE_CANDIDATE|DEFERRED|CLOSED
```

Possible method classes are descriptive only unless mechanics are separately defined:

- mapping;
- surface sampling;
- trenching;
- drilling;
- geophysical survey;
- underground sampling;
- historical-record review.

Exploration observations flow into Science/Geology. This layer stores operational provenance.

## 4. Working areas and geometry revisions

```yaml
mine_working_area:
  working_area_id: null
  extraction_site_id: null
  area_type: PIT|BENCH|ADIT|SHAFT|LEVEL|STOPE|QUARRY_FACE|PROCESS_PAD|STOCKPILE_PAD|WASTE_ROCK_AREA|TAILINGS_AREA|HAUL_ROAD|WORKSHOP|PORTAL|OTHER
  geometry_revision_refs: []
  operational_state: PLANNED|ACTIVE|IDLE|MAINTENANCE|CLOSED|REHABILITATING|REHABILITATED|RESTRICTED
  access_state_ref: null
  environmental_refs: []
  infrastructure_refs: []
  chronicle_refs: []
```

A mine can contain areas in several states at once.

```yaml
working_geometry_revision:
  revision_id: null
  working_area_id: null
  effective_at: null
  geometry_ref: null
  connected_area_refs: []
  closed_or_blocked_connections: []
  known_uncertain_connections: []
  survey_refs: []
  supersedes: null
```

Old workings are not resurrected by Minecraft chunk reload.

## 5. Extraction event

```yaml
extraction_event:
  extraction_event_id: null
  project_id: null
  working_area_id: null
  occurred_at: null
  activity_class: EXCAVATION|CUTTING|DRILLING|REMOVAL|SORTING|LOADING|OTHER
  source_geometry_ref: null
  resulting_material_batch_ids: []
  waste_or_overburden_batch_ids: []
  equipment_refs: []
  worker_refs: []
  working_pokemon_assignment_refs: []
  observation_refs: []
  incident_refs: []
```

Narrative extraction events do not calculate ore yield. Quantity remains whatever authoritative economy/material system provides.

## 6. Extracted material batch

```yaml
extracted_material_batch:
  extracted_material_batch_id: null
  extraction_event_id: null
  source_working_area_id: null
  source_geology_ref: null
  material_classification: ORE_CANDIDATE|INDUSTRIAL_MINERAL|STONE|AGGREGATE|OVERBURDEN|WASTE_ROCK|TAILINGS_INPUT|UNCLASSIFIED
  measured_quantity_ref: null
  grade_or_quality_claim_refs: []
  custody_ref: null
  current_location_ref: null
  stockpile_ref: null
  downstream_handoff_ref: null
  disposition_state: HELD|STOCKPILED|PROCESSING_HANDOFF|FREIGHT_HANDOFF|WASTE_MANAGEMENT|RESEARCH_HOLD|DISCARDED|UNKNOWN
```

Mining preserves extraction provenance. Manufacturing/Supply Chains take over downstream operational ownership as appropriate.

A batch classified as waste today may later acquire another lawful use, but its provenance remains.

## 7. Stockpiles, waste rock and tailings-related state

Do not collapse everything visible into one resource pile.

```yaml
mine_material_storage_area:
  storage_area_id: null
  site_id: null
  storage_type: ORE_STOCKPILE|PRODUCT_STOCKPILE|WASTE_ROCK|OVERBURDEN|TAILINGS|TOPSOIL_SALVAGE|REHAB_MATERIAL|OTHER
  batch_refs: []
  geometry_ref: null
  containment_or_management_refs: []
  inspection_refs: []
  environmental_handoff_refs: []
```

Contamination, stability, dust and water-quality consequences belong to their governing layers and require evidence.

## 8. Operational state

```yaml
mine_operational_revision:
  revision_id: null
  project_id: null
  effective_at: null
  operating_state: NORMAL|REDUCED|SUSPENDED|CARE_AND_MAINTENANCE|EMERGENCY_SHUTDOWN|RESTARTING|CLOSING
  active_working_area_ids: []
  idle_working_area_ids: []
  maintenance_area_ids: []
  access_restriction_refs: []
  staffing_refs: []
  reason_refs: []
  supersedes: null
```

`CARE_AND_MAINTENANCE` is first-class. It can include pumping, inspections, water management, security, monitoring, ventilation or asset preservation if those systems exist and are authored.

Do not infer abandonment from a lack of production.

## 9. Incidents and observations

Mining records operational context. Crisis/environmental layers determine incident consequences.

```yaml
mine_incident_link:
  link_id: null
  project_id: null
  working_area_id: null
  incident_ref: null
  observed_at: null
  operational_effect: null
  shutdown_or_restriction_ref: null
  worker_report_refs: []
  investigation_refs: []
```

Examples:

- unexpected water inflow;
- ground movement;
- damaged access;
- equipment failure;
- wildlife presence;
- unusual Pokémon behavior;
- lost communications;
- archaeological/fossil discovery;
- material discrepancy.

The observation does not establish causation.

## 10. Scientific/cultural find handoff

```yaml
mine_find_event:
  find_event_id: null
  extraction_site_id: null
  working_area_id: null
  discovered_at: null
  discovery_kind: FOSSIL|ARCHAEOLOGICAL|GEOLOGIC|BIOLOGICAL|UNKNOWN
  finder_refs: []
  initial_context_record_ref: null
  work_stop_scope_ref: null
  custody_handoff_ref: null
  destination_authority: PALEONTOLOGY|ARCHAEOLOGY|GEOLOGY|CONSERVATION|SCIENCE|OTHER
```

A fossil found in a mine is not automatically owned by the mine, worker, Trainer or museum.

A battle must never decide custody.

## 11. Working Pokémon boundary

Mining references the Working Pokémon layer.

```yaml
mine_working_pokemon_link:
  assignment_ref: null
  project_id: null
  working_area_id: null
  role_label: null
  observed_task_refs: []
  availability_state_ref: null
  welfare_or_care_refs: []
```

Never infer role qualification from species alone.

Rolycoly, Machoke, Excadrill, Diglett, Carbink or any other species may inspire authored occupational history; individual use still requires agency, capability/rule support and world-state evidence.

## 12. Closure plan and objective revisions

```yaml
mine_closure_plan_revision:
  closure_plan_revision_id: null
  project_id: null
  effective_at: null
  closure_area_ids: []
  infrastructure_disposition_refs: []
  working_closure_refs: []
  waste_storage_management_refs: []
  water_management_refs: []
  landform_objective_refs: []
  vegetation_or_habitat_objective_refs: []
  post_mining_use_refs: []
  monitoring_program_refs: []
  uncertainty_notes: []
  supersedes: null
```

Closure objectives can change over decades. Old revisions remain part of institutional history.

## 13. Progressive rehabilitation

```yaml
rehabilitation_area_revision:
  rehab_area_revision_id: null
  working_area_id: null
  rehabilitation_project_ref: null
  action_classes: []
  starts_at: null
  completed_at: null
  physical_completion_state: NOT_STARTED|IN_PROGRESS|EARTHWORK_COMPLETE|STABILIZED|VEGETATED|MONITORING|OBJECTIVE_MET|REOPENED_FOR_WORK
  follow_up_observation_refs: []
  objective_assessment_refs: []
```

Different portions of a mine can be rehabilitated while extraction continues elsewhere.

Possible action classes are narrative descriptors only:

- grading/recontouring;
- securing/closing workings;
- infrastructure removal;
- topsoil replacement;
- revegetation;
- drainage/water-management work;
- habitat creation;
- access conversion;
- contamination remediation handoff.

These actions do not create Minecraft/PTU effects automatically.

## 14. Post-closure monitoring

```yaml
mine_post_closure_monitoring_program:
  monitoring_program_id: null
  extraction_site_id: null
  objective_refs: []
  monitoring_location_refs: []
  discipline_refs: []
  observation_refs: []
  issue_refs: []
  current_assessment: STABLE|IMPROVING|MIXED|ISSUE_DETECTED|INSUFFICIENT_DATA|COMPLETE
  review_dates: []
```

A short period without detected issues does not prove permanent stability.

Environmental response may lag behind physical works.

## 15. Post-mining use

```yaml
post_mining_use_revision:
  post_mining_use_revision_id: null
  extraction_site_id: null
  effective_at: null
  use_class: HABITAT|PUBLIC_OPEN_SPACE|RESEARCH|INDUSTRIAL|STORAGE|TRANSPORT|HERITAGE|MUSEUM|TRAINING|RESTRICTED|MIXED|OTHER
  active_area_refs: []
  residual_restriction_refs: []
  steward_refs: []
  monitoring_refs: []
  public_access_refs: []
```

Reuse does not erase industrial history.

A former quarry can become habitat and still retain restricted walls, water-quality monitoring or inaccessible workings.

## 16. Minecraft projection rules

Minecraft represents current physical state; it does not own Mining truth.

Allowed projection examples:

- visible portals/shafts/pits/benches;
- haul roads;
- stockpile silhouettes;
- workshops and conveyors as scenery;
- fences/signs reflecting authoritative restrictions;
- reclaimed slopes/vegetation;
- museum or heritage interpretation;
- closed or backfilled access;
- environmental monitoring equipment.

Forbidden authority inversions:

- block drops -> ore production truth;
- player mining blocks -> legal extraction event without world-state authorization;
- item stacks -> measured deposit reserves;
- minecart movement -> vehicle collision rules;
- placed TNT -> validated blasting mechanics;
- lava/water blocks -> automatic PTU hazard;
- darkness -> automatic Accuracy penalty;
- gravel fall -> automatic damage;
- mobs loaded -> workforce/population count;
- grass/tree placement -> reclamation complete.

## 17. Chronicle compression

Routine extraction does not need event-by-event narration.

Compress normal operation into production/inspection revisions unless one of these changes:

- geometry;
- worker/Pokémon role state;
- material provenance;
- access;
- water/environmental state;
- incident state;
- research/fossil/cultural discovery;
- closure/rehabilitation status;
- institutional ownership/stewardship;
- public consequences.

A normal year is useful baseline state.

## 18. Original Ouros hooks enabled by the layer

- a mine where only one level is still producing while upper levels are already being reclaimed;
- an old haul road that becomes the safest wildlife crossing after closure;
- a fossil discovery that pauses one working face but not the whole operation;
- a closure plan whose planned lake never fills because groundwater behavior differs from the model;
- a former quarry converted to public recreation while one wall remains restricted;
- an abandoned adit rediscovered during unrelated road work;
- a mine in care-and-maintenance that still employs a small multigenerational crew;
- a stockpile whose old material classification becomes valuable after technology changes;
- a closed site that becomes habitat before its formal reuse plan is complete;
- an extraction town whose institutional identity persists after the mine closes.

## 19. Battle handoff contract

Mining world state must resolve as much as possible before AutoPTU starts.

A battle snapshot may include only validated static geometry, combatants, authoritative positions and mechanics the engine already supports.

Potential FULL-version dependencies:

- complete movement for mine carts, retreats, rescues, escorts, crossing objectives or forced displacement;
- terrain/weather/hazards/zones/reactions for unstable ground, dust, gas, water, dynamic machinery, collapse or protected work zones;
- AI tactical policy for `WITHDRAW`, `REACH_EXIT`, `PROTECT_WORKER`, `CLEAR_ROUTE`, `REACH_CONTROL`, `PROTECT_FIND`;
- adapter/playback for equipment, workers, objectives, evacuations and changing geometry;
- items/Features/Abilities only when an encounter explicitly uses a validated mechanic from those families.

Reduced versions should shut down machinery, evacuate workers, freeze water/geometry, remove fragile finds and use a stable arena before combat.

## 20. Explicit non-inferences

This layer never infers:

- Rock/Ground/Steel type -> mining skill;
- Burrow -> excavation production;
- Groundshaper -> mine-development authority;
- Strength-like fiction -> carrying capacity;
- Rolycoly -> fuel rate;
- Carbink -> ore grade;
- Sableye -> gemstone reserve;
- Excadrill -> tunnel stability;
- mining uniform -> credential;
- worker testimony -> geologic truth;
- closed mine -> abandoned mine;
- reclaimed land -> safe for every use;
- mine water -> contamination;
- contamination -> mine causation;
- mine collapse -> operator fault;
- resource discovery -> economic viability;
- economic viability -> authorization;
- extraction -> player inventory;
- block destruction -> production;
- Pokémon KO/capture -> operational resolution.

## 21. PTU/Caelo and engine boundary

No excavation, mining, blasting, carrying, darkness, gas, dust, cave-in, minecart, occupational or industrial mechanics are invented here.

The project PTU/Caelo source set remains authority when available. Full primary Caelo material was not reliably exposed during this run. Super PTU Online Helper was not available as an invocable capability.

AutoPTU-Java and AutoPTU remain read-only evidence sources for this task.

## 22. Canon status

Everything in this layer is architecture only. It does not establish:

- an Ouros mining region;
- specific minerals;
- companies;
- worker guilds/unions;
- extraction technology;
- legal authority;
- closure standards;
- pollution history;
- worker Pokémon roles;
- mine ownership;
- post-mining land uses.

Those remain proposal/canon-review decisions.