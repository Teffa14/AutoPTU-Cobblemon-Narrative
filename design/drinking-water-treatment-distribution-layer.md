# Ouros Drinking Water, Treatment & Distribution Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

Pass: 113.

## Purpose

This layer owns the persistent service chain that converts a raw water source into water delivered to a settlement, institution or service point.

It covers:

- raw-water intake state;
- treatment-site identity and process revision;
- finished-water storage;
- distribution zones;
- mains and major service links;
- pump/valve/pressure-management state at narrative resolution;
- service interruptions;
- leak investigations;
- water-quality observations across the chain;
- advisories as information products;
- emergency water service;
- repair/recovery history.

It does not replace:

- Groundwater for aquifers, recharge, wells and drawdown;
- Freshwater for rivers, catchments, reservoirs and water regimes;
- Stormwater for runoff/drainage;
- Waste/Sanitation for wastewater and waste treatment;
- Technology for machine-level assets, controls and faults;
- Supply Chains for consumables/spares/emergency stock;
- Workplaces for staffing;
- Health Surveillance for health signals/outbreaks;
- Communications/Media for delivery of advisories;
- Crisis for region-scale emergency coordination;
- Land Tenure for access/easement claims;
- AutoPTU for battle mechanics.

It does not define drinking requirements, dehydration, contamination damage, treatment chemistry, Water-type utility powers, pipe physics or health thresholds.

## Core principle

Water service is a chain of independently observable states.

`SOURCE -> INTAKE -> TREATMENT -> FINISHED STORAGE -> DISTRIBUTION ZONE -> SERVICE POINT`

A successful upstream state does not prove downstream success.

## 1. Water service system

```yaml
water_service_system:
  system_id: null
  settlement_refs: []
  operator_institution_ref: null
  source_refs: []
  intake_ids: []
  treatment_site_ids: []
  finished_storage_ids: []
  distribution_zone_ids: []
  emergency_supply_plan_ref: null
  service_revision_ids: []
  incident_ids: []
  observation_ids: []
  public_information_refs: []
  provenance_refs: []
  canon_status: proposed
```

The system may serve one settlement, several settlements or a district within a larger city.

## 2. Raw-water source handoff

The source itself belongs to Groundwater or Freshwater.

```yaml
raw_water_source_link:
  link_id: null
  water_service_system_ref: null
  source_authority_ref: null
  source_type: null
  source_entity_ref: null
  source_access_ref: null
  intake_refs: []
  current_availability_claim_ref: null
  current_quality_claim_ref: null
  current_restriction_refs: []
  observed_at: null
```

Candidate source types:

- GROUNDWATER_WELLFIELD
- SPRING
- RIVER
- LAKE
- RESERVOIR
- OTHER_AUTHORED

The link never copies the source state. It references the governing source record.

## 3. Intake identity

```yaml
water_intake:
  intake_id: null
  source_link_ref: null
  location_ref: null
  structure_ref: null
  technology_asset_refs: []
  access_permission_refs: []
  current_operational_state: unknown
  capacity_band: unknown
  obstruction_observation_ids: []
  maintenance_refs: []
  incident_refs: []
  environmental_interaction_refs: []
  current_revision_ref: null
```

Candidate operational states:

- NORMAL
- DEGRADED
- OFFLINE_PLANNED
- OFFLINE_UNPLANNED
- SOURCE_UNAVAILABLE
- ACCESS_BLOCKED
- UNDER_REPAIR
- UNKNOWN

`SOURCE_UNAVAILABLE` is different from `INTAKE_FAULT`.

## 4. Treatment site

```yaml
water_treatment_site:
  treatment_site_id: null
  location_ref: null
  structure_ref: null
  workplace_ref: null
  technology_network_refs: []
  incoming_intake_refs: []
  treatment_process_revision_ref: null
  treatment_train_ids: []
  current_operational_state: unknown
  observation_ids: []
  quality_assessment_refs: []
  supply_dependency_refs: []
  maintenance_refs: []
  incident_refs: []
```

Treatment is represented narratively unless a future canon decision needs greater process detail.

Do not create chemistry formulas or quality thresholds by narrative convenience.

## 5. Treatment process revision

```yaml
water_treatment_process_revision:
  revision_id: null
  treatment_site_ref: null
  effective_from: null
  supersedes_ref: null
  source_categories_supported: []
  process_stage_descriptors: []
  required_asset_refs: []
  required_supply_refs: []
  required_staffing_refs: []
  monitoring_point_refs: []
  operating_constraint_refs: []
  authored_notes: null
```

This record is descriptive and institution-facing. It is not an item recipe.

## 6. Finished-water storage

```yaml
finished_water_storage:
  storage_id: null
  treatment_site_ref: null
  location_ref: null
  structure_ref: null
  storage_type: null
  service_zone_refs: []
  current_fill_band: unknown
  current_operational_state: unknown
  observation_ids: []
  maintenance_refs: []
  quality_assessment_refs: []
  incident_refs: []
```

Candidate storage types:

- GROUND_TANK
- ELEVATED_TANK
- COVERED_RESERVOIR
- SERVICE_RESERVOIR
- OTHER_AUTHORED

The fill band is coarse unless exact volume becomes narratively necessary.

## 7. Distribution zone

```yaml
water_distribution_zone:
  zone_id: null
  water_service_system_ref: null
  settlement_ref: null
  boundary_ref: null
  elevation_context_ref: null
  upstream_storage_refs: []
  pump_refs: []
  valve_refs: []
  major_main_refs: []
  service_point_refs: []
  current_service_state: unknown
  current_pressure_band: unknown
  observation_ids: []
  incident_ids: []
  current_revision_ref: null
```

Candidate service states:

- NORMAL
- DEGRADED
- LOW_PRESSURE
- INTERRUPTED
- ISOLATED_FOR_REPAIR
- EMERGENCY_SUPPLY
- UNKNOWN

Candidate pressure bands:

- NORMAL
- LOW
- HIGH
- UNSTABLE
- NO_PRESSURE
- UNKNOWN

No numeric real-world thresholds are assumed.

## 8. Major network link

Ouros does not need every pipe segment.

```yaml
water_network_link:
  link_id: null
  from_node_ref: null
  to_node_ref: null
  link_type: null
  physical_route_ref: null
  structure_or_utility_corridor_ref: null
  current_condition_band: unknown
  current_operational_state: unknown
  isolation_refs: []
  repair_refs: []
  leak_case_refs: []
  revision_history_refs: []
```

Candidate link types:

- TRUNK_MAIN
- DISTRIBUTION_MAIN
- SERVICE_TRANSFER
- GRAVITY_CONVEYANCE
- PRESSURIZED_CONVEYANCE
- OTHER_AUTHORED

Minor household plumbing stays compressed unless relevant.

## 9. Service point

```yaml
water_service_point:
  service_point_id: null
  location_ref: null
  facility_ref: null
  distribution_zone_ref: null
  service_priority_class: null
  current_service_state: unknown
  last_confirmed_service_at: null
  observation_ids: []
  local_storage_ref: null
  emergency_supply_refs: []
```

Candidate priority classes are authored and descriptive, for example:

- CRITICAL_FACILITY
- PUBLIC_SERVICE
- RESIDENTIAL_CLUSTER
- COMMERCIAL
- INDUSTRIAL
- PUBLIC_TAP
- OTHER_AUTHORED

Priority classification does not itself create legal authority.

## 10. Water-quality observation

Quality observations must be scoped.

```yaml
water_quality_observation:
  observation_id: null
  observed_at: null
  observer_ref: null
  sampling_location_ref: null
  chain_stage: null
  parameter_or_indicator_ref: null
  observed_value_or_band: null
  method_ref: null
  sample_ref: null
  laboratory_ref: null
  quality_flag: null
  interpretation_refs: []
  source_refs: []
```

Candidate chain stages:

- RAW_SOURCE
- POST_INTAKE
- POST_TREATMENT
- FINISHED_STORAGE
- DISTRIBUTION
- SERVICE_POINT

A result is never silently generalized to every stage.

## 11. Water-quality assessment

```yaml
water_quality_assessment:
  assessment_id: null
  water_service_system_ref: null
  scope_refs: []
  observation_refs: []
  assessed_at: null
  assessor_refs: []
  assessment_state: null
  confidence_band: null
  alternative_explanations: []
  recommended_action_refs: []
  supersedes_ref: null
```

Candidate states:

- ACCEPTABLE_FOR_AUTHORED_USE
- INVESTIGATING
- CONDITIONALLY_RESTRICTED
- NOT_ACCEPTED_FOR_AUTHORED_USE
- INSUFFICIENT_EVIDENCE
- SUPERSEDED

These labels are Ouros institutional states, not imported health standards.

## 12. Service interruption incident

```yaml
water_service_incident:
  incident_id: null
  water_service_system_ref: null
  started_at: null
  detected_at: null
  affected_zone_refs: []
  affected_service_point_refs: []
  initial_observation_refs: []
  cause_hypothesis_ids: []
  confirmed_cause_refs: []
  technical_action_refs: []
  emergency_supply_refs: []
  public_information_refs: []
  restored_at: null
  recovery_review_ref: null
```

Candidate incident families:

- SOURCE_SHORTFALL
- INTAKE_OBSTRUCTION
- TREATMENT_OUTAGE
- STORAGE_FAILURE
- PUMP_FAILURE
- POWER_DEPENDENCY_FAILURE
- MAIN_BREAK
- LEAK
- PRESSURE_LOSS
- VALVE_CONFIGURATION
- QUALITY_INVESTIGATION
- ACCESS_CONSTRAINT
- UNKNOWN

Do not infer sabotage from any of these states.

## 13. Leak investigation

```yaml
water_leak_case:
  leak_case_id: null
  suspected_zone_ref: null
  first_signal_ref: null
  field_observation_refs: []
  meter_or_sensor_refs: []
  suspected_link_refs: []
  isolation_test_refs: []
  confirmed_location_ref: null
  confirmed_at: null
  repair_ref: null
  post_repair_observation_refs: []
  status: open
```

A leak may remain localized only approximately for some time.

## 14. Isolation and valve state

```yaml
network_isolation_action:
  action_id: null
  incident_ref: null
  authorized_by_ref: null
  valve_or_link_refs: []
  requested_at: null
  applied_at: null
  expected_affected_zone_refs: []
  observed_affected_zone_refs: []
  rollback_or_reopen_ref: null
```

Physical valve state and authorization remain separate.

## 15. Advisory as information product

An advisory belongs partly to Communications/Public Information.

```yaml
water_service_advisory:
  advisory_id: null
  issuing_institution_ref: null
  issued_at: null
  scope_refs: []
  advisory_type: null
  evidence_snapshot_ref: null
  instruction_text_ref: null
  delivery_channel_refs: []
  supersedes_ref: null
  lifted_at: null
```

Candidate advisory types:

- SERVICE_INTERRUPTION
- LOW_PRESSURE
- QUALITY_INVESTIGATION
- RESTRICTED_USE
- EMERGENCY_DISTRIBUTION
- RESTORATION_NOTICE
- OTHER_AUTHORED

An advisory is not proof that the underlying hypothesis is true. It records an institutional action under uncertainty.

## 16. Emergency water service

```yaml
emergency_water_distribution_event:
  event_id: null
  incident_ref: null
  started_at: null
  distribution_site_refs: []
  supply_batch_refs: []
  transport_refs: []
  staffing_refs: []
  recipient_scope_ref: null
  priority_refs: []
  current_state: active
  ended_at: null
```

This connects to Supply Chains, Logistics and Public Space.

Emergency service does not equal permanent restoration.

## 17. Recovery review

```yaml
water_service_recovery_review:
  review_id: null
  incident_ref: null
  restored_service_at: null
  stabilization_observation_refs: []
  confirmed_cause_refs: []
  contributing_factor_refs: []
  repair_refs: []
  temporary_measure_refs: []
  resilience_project_refs: []
  unresolved_questions: []
  reviewed_at: null
```

This preserves institutional learning and prevents the system from forgetting repeated failures.

## 18. Demand and capacity

Demand should stay coarse unless a specific story needs detail.

```yaml
water_demand_revision:
  revision_id: null
  distribution_zone_ref: null
  effective_at: null
  demand_band: null
  driver_refs: []
  observation_refs: []
  forecast_refs: []
```

Candidate drivers:

- POPULATION_CHANGE
- FESTIVAL_OR_EVENT
- TOURISM_SURGE
- INDUSTRIAL_OPERATION
- WILDFIRE_RESPONSE
- HEAT_EVENT
- SEASONAL_WORKFORCE
- SERVICE_EXPANSION
- UNKNOWN

No universal liters-per-person model is assumed.

## 19. Reliability and redundancy

```yaml
water_service_resilience_measure:
  measure_id: null
  water_service_system_ref: null
  measure_type: null
  dependency_reduced_ref: null
  implementation_project_ref: null
  operational_test_refs: []
  current_state: null
```

Candidate types:

- BACKUP_POWER
- SECOND_SOURCE
- INTERZONE_CONNECTION
- EXTRA_STORAGE
- REPLACEMENT_MAIN
- LEAK_PROGRAM
- MONITORING_EXPANSION
- EMERGENCY_DISTRIBUTION_PLAN
- OTHER_AUTHORED

A resilience measure is not successful until tested/observed.

## 20. Pokémon interactions

Pokémon can interact with the system only through authored species behavior, observed events or validated mechanics.

Candidate world-state events:

- a wild group repeatedly uses a reservoir edge;
- a persistent individual blocks an intake area;
- burrowing activity is observed near a major main;
- a Pokémon-built structure alters source flow upstream;
- a utility Pokémon voluntarily participates in inspection/maintenance under an established institutional relationship.

Do not infer:

- Water-type -> potable water;
- Water Gun -> safe drinking water;
- Rain Dance -> supply restoration;
- Water Absorb -> treatment;
- Hydration -> purification;
- Poison-type -> contamination;
- Ground-type -> pipe damage;
- Electric-type -> pump failure.

## 21. Minecraft projection

Minecraft may render:

- treatment buildings;
- tanks/towers;
- major mains where visible;
- valves and hydrant-like markers;
- pump stations;
- public taps;
- emergency distribution sites;
- maintenance work;
- dry fountains or closed fixtures;
- visible leaks where appropriate;
- advisories/signage.

Minecraft must not decide:

- water safety;
- system pressure;
- treatment success;
- confirmed leak location;
- contamination cause;
- authorization;
- distribution-zone truth;
- health effect;
- PTU status.

The server projects authoritative world state into the visible environment.

## 22. World-state to battle boundary

A water-service incident may create an encounter, but the battle receives a frozen validated snapshot.

Example:

`main break -> flooded excavation in world state -> technicians isolate zone -> safe combat perimeter selected -> AutoPTU battle`

The adapter must not invent:

- current knockback;
- electrocution;
- drowning;
- Poisoned water;
- slippery terrain;
- Water Terrain;
- pressure damage;
- moving valve objectives;
- pump HP;
- civilian escort rules.

## 23. Encounter contract — Treatment Plant Intake Interruption

Narrative premise:
An intake has stopped providing expected flow. Technicians need access while the cause remains uncertain.

FULL version:

- technicians move toward inspection points;
- wild Pokémon may withdraw through alternate routes;
- intake machinery may define protected/interactable zones;
- the objective can be `REACH_CONTROL`, `PROTECT_TECHNICIAN`, `CLEAR_ROUTE` or `WITHDRAW` rather than pure KO.

Required families:

- targeting/footprints/range/LoS
- base movement legality
- complete movement including interception/forced movement
- core calculations
- action economy/initiative
- full lifecycle
- full stateful damage
- statuses where invoked
- terrain/weather/hazards/zones/reactions if the intake environment gains mechanics
- move-specific behavior
- abilities
- items
- Trainer Features/perks where used
- AI legal-action infrastructure
- AI tactical policy
- Minecraft/Cobblemon/Craftics playback

REDUCED version:

Technicians withdraw first. The intake is isolated in world state. Freeze one dry, safe arena adjacent to the asset. AutoPTU resolves only the combatants actually involved. Inspection and service restoration occur afterward.

## 24. Encounter contract — Main Break Street Closure

Narrative premise:
A major distribution main fails beneath a busy street. The service incident and the urban incident overlap.

FULL version:

- civilians/workers evacuate;
- a work zone changes access;
- background water may alter routes only if validated mechanics exist;
- actors may need to protect a work perimeter rather than defeat everything.

REDUCED version:

Close the street in world state. Move civilians and workers out. Isolate the main. Freeze a dry adjacent battle area if a confrontation remains. Battle outcome never determines repair success.

## 25. Encounter contract — Emergency Tank Transfer

Narrative premise:
A district has lost normal service and emergency water is being transferred to a temporary distribution site.

FULL version:

- cargo/vehicle movement;
- protected route;
- potentially time-sensitive delivery;
- tactical objectives such as `PROTECT_ROUTE`, `REACH_EXIT` or `WITHDRAW`.

REDUCED version:

Keep tankers/cargo outside the grid. Clear one static chokepoint if needed. Resolve logistics afterward through Supply Chains and Water Service state.

## 26. Integration contracts

### Groundwater -> Drinking Water

Groundwater provides source availability and well state. Drinking Water records abstraction/intake and treatment/service consequences.

### Freshwater -> Drinking Water

Freshwater provides reservoir/river/lake source state. Drinking Water records utility intake and downstream service.

### Technology -> Drinking Water

Technology owns pumps, controls, backup power and asset faults. Drinking Water owns service consequence.

### Supply Chains -> Drinking Water

Supply Chains owns treatment consumables, spare parts and emergency water batches.

### Health Surveillance -> Drinking Water

Health consumes service-point observations and exposure hypotheses. Drinking Water does not diagnose illness.

### Communications -> Drinking Water

Communications delivers advisories. Delivery does not guarantee receipt/belief.

### Crisis -> Drinking Water

Crisis coordinates large outages. Drinking Water preserves the technical/service record afterward.

## 27. Hard non-inferences

Do not infer:

- full reservoir -> adequate service;
- working intake -> working treatment;
- working treatment -> working network;
- network pressure -> water quality;
- clear water -> accepted quality;
- unusual smell/taste -> toxic;
- advisory -> confirmed contamination;
- no advisory -> safe;
- low pressure -> contamination;
- one sample -> whole-network truth;
- source contamination -> every endpoint contaminated;
- endpoint issue -> source cause;
- Water-type presence -> treatment capability;
- battle near a utility -> outage cause;
- leak -> sabotage;
- vandalized appearance -> deliberate interference;
- emergency supply -> normal service restored;
- pipe visible in Minecraft -> current authoritative route;
- open valve model -> authorized valve state;
- shut faucet -> upstream outage;
- Hydration/Rain Dish/Water Absorb -> potable-water mechanics;
- Rain Dance -> municipal water production;
- Poisoned status -> drinking-water contamination;
- successful battle -> successful repair.

## 28. Canon boundary

Nothing in this document establishes:

- which settlements have piped water;
- treatment technology level;
- drinking-water standards;
- utility ownership/governance;
- universal public-water institutions;
- rates/prices;
- water rights;
- household plumbing norms;
- Water-type employment;
- purification powers;
- health thresholds;
- legal penalties for interference.

Those require later canon review.

## 29. Open implementation questions

- Which settlements use centralized systems versus wells/springs/local storage?
- What scale of network topology should persist server-side?
- How many pressure/service zones are useful before the model becomes too granular?
- Which facilities count as critical service points?
- How should service state advance while chunks are unloaded?
- How should a major main route survive Minecraft rebuilding without becoming block-authoritative?
- How should water-quality samples integrate with Science and Health Surveillance?
- How should emergency distribution consume real Supply Chain batches?
- What PTU/Caelo rules, if any, govern drinking, dehydration, environmental contamination or purification?
- Which validated Java mechanics could ever justify water-related tactical terrain rather than a static dry snapshot?