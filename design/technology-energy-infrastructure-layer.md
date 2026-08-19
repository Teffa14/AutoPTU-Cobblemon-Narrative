# Ouros Technology, Energy & Infrastructure Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models public works, crafting, crisis response, communications, travel, settlements, science and conservation. This layer covers the operational life of technical systems after they exist: energy, machinery, utility networks, maintenance, degraded service, technical operators, failure diagnosis and Pokémon-machine interaction.

This layer does not define a universal technology level for Ouros. Regional technology remains authored canon.

## 1. Technical asset

A technical asset is a persistent machine, device or engineered system that matters to world state.

```yaml
technical_asset:
  asset_id: null
  asset_type: null
  location_id: null
  operator_institution_id: null
  operator_actor_ids: []
  manufacturer_or_builder_ids: []
  installed_event_id: null
  service_role_ids: []
  upstream_dependency_ids: []
  downstream_dependency_ids: []
  current_operational_state: unknown
  maintenance_record_ids: []
  fault_record_ids: []
  control_interface_ids: []
  pokemon_interaction_ids: []
  mechanical_rule_refs: []
  canon_reference_ids: []
```

Candidate asset types:
- generator;
- transformer;
- pump;
- relay;
- lift;
- gate controller;
- refrigeration system;
- workshop machine;
- environmental control unit;
- research instrument;
- transport machinery;
- factory line;
- security system;
- habitat-support system;
- personal device;
- legacy machine.

Narrative classification never creates a PTU mechanical effect by itself.

## 2. Infrastructure network

A network connects assets to services.

```yaml
infrastructure_network:
  network_id: null
  network_type: null
  geographic_scope_ids: []
  asset_ids: []
  source_node_ids: []
  distribution_node_ids: []
  service_sink_ids: []
  operator_ids: []
  normal_capacity_state: null
  current_capacity_state: null
  redundancy_paths: []
  isolation_points: []
  monitoring_ids: []
  current_incident_ids: []
```

Potential network types:
- POWER
- WATER
- WASTE
- HEAT
- REFRIGERATION
- COMMUNICATIONS_BACKHAUL
- INDUSTRIAL_PROCESS
- HABITAT_SUPPORT
- TRANSPORT_CONTROL

The Media/Communications layer still owns message delivery. This layer owns the physical/technical systems that may support it.

## 3. Service dependency

A settlement service can depend on several technical systems.

```yaml
service_dependency:
  dependency_id: null
  service_id: null
  required_network_ids: []
  required_asset_ids: []
  required_staff_role_ids: []
  minimum_operating_conditions: []
  fallback_modes: []
  degraded_outputs: []
  failure_outputs: []
```

Example: a clinic may depend on power, refrigeration, staff and communications. Loss of one dependency may reduce capacity instead of closing the clinic entirely.

## 4. Operational state

Use explicit readable states rather than one boolean.

```yaml
operational_state:
  subject_id: null
  state: NORMAL
  capacity_band: normal
  active_fault_ids: []
  workaround_ids: []
  restricted_functions: []
  effective_from: null
  expected_review_at: null
  source_evidence_ids: []
```

Suggested states:
- NORMAL
- DEGRADED
- INTERMITTENT
- EMERGENCY_ONLY
- OFFLINE_PLANNED
- OFFLINE_FAILURE
- BYPASSED
- ISOLATED
- UNDER_REPAIR
- TESTING
- DECOMMISSIONED

A machine may be powered but still unsafe, miscalibrated or unable to provide its normal service.

## 5. Fault record

A fault is observed technical state, not an accusation.

```yaml
fault_record:
  fault_id: null
  asset_id: null
  first_observed_at: null
  observed_symptoms: []
  diagnostic_claim_ids: []
  confirmed_cause_ids: []
  affected_function_ids: []
  downstream_effect_ids: []
  severity: unknown
  intermittent: false
  safety_state: unknown
  evidence_ids: []
  case_id: null
  resolved_by_maintenance_id: null
```

Possible causes should remain unresolved until evidence supports them.

Candidate cause families:
- wear;
- overload;
- environmental damage;
- supply interruption;
- incorrect configuration;
- operator error;
- Pokémon interaction;
- deliberate interference;
- component defect;
- unknown.

Sabotage belongs in the Case/Antagonist systems only when evidence supports it.

## 6. Maintenance record

Maintenance creates persistent history.

```yaml
maintenance_record:
  maintenance_id: null
  asset_id: null
  maintenance_type: null
  performed_by_ids: []
  supporting_pokemon_ids: []
  started_at: null
  completed_at: null
  parts_or_material_refs: []
  tool_refs: []
  procedures_claimed: []
  inspection_findings: []
  output_state: null
  next_review_at: null
  evidence_ids: []
  mechanical_validation_required: true
```

Candidate types:
- INSPECTION
- CLEANING
- CALIBRATION
- PREVENTIVE_SERVICE
- COMPONENT_REPLACEMENT
- EMERGENCY_REPAIR
- SOFTWARE_OR_CONTROL_UPDATE
- SAFETY_TEST
- CAPACITY_TEST
- DECOMMISSIONING

Exact repair legality, Skill checks, time, items and Feature effects come from PTU/Caelo and implementation data.

## 7. Maintenance debt

Systems can accumulate risk without forcing a crisis.

```yaml
maintenance_debt:
  subject_id: null
  overdue_task_ids: []
  known_risk_claim_ids: []
  deferred_reason_ids: []
  responsible_operator_ids: []
  current_public_visibility: internal
  escalation_thresholds: []
```

Maintenance debt is a narrative and operational state. It does not automatically roll for random failure.

If a future failure is generated, it must be causally supported by the actual asset state, not by a hidden "drama meter".

## 8. Technical operator

Technical systems depend on people and Pokémon with real roles.

```yaml
technical_operator_role:
  role_id: null
  institution_id: null
  actor_id: null
  specialty_tags: []
  authorized_asset_ids: []
  shift_or_availability_state: null
  certification_claim_ids: []
  mentor_ids: []
  apprentice_ids: []
  governing_rule_refs: []
```

Do not infer PTU Skill Ranks from job titles.

A character described as an engineer still needs authoritative Technology Education or other required mechanical state when a check is called for.

## 9. Control interface

A machine should expose authored controls, not arbitrary interaction verbs.

```yaml
control_interface:
  interface_id: null
  asset_id: null
  physical_location_id: null
  authorized_actor_ids: []
  credential_requirement_ids: []
  available_command_ids: []
  lockout_state: null
  manual_override_id: null
  logging_state: null
```

Examples of commands:
- START
- STOP
- ISOLATE
- RESET
- SWITCH_SOURCE
- OPEN
- CLOSE
- RUN_TEST
- ENTER_SAFE_MODE

Only commands explicitly authored for the asset may be offered.

## 10. Technical puzzle recovery contract

Persistent-machine puzzles must be recoverable.

```yaml
machine_puzzle:
  puzzle_id: null
  asset_ids: []
  initial_state_ref: null
  legal_transition_ids: []
  success_state_ids: []
  nonterminal_failure_states: []
  reset_methods: []
  manual_bypass_methods: []
  technician_recovery_methods: []
  irreversible_transition_ids: []
```

Default policy:
- irreversible actions require explicit authored intent;
- failure should create a new solvable state where possible;
- a puzzle must not softlock a persistent location because a player logged out or moved one object incorrectly;
- Minecraft block state may present the puzzle, but the authoritative puzzle state should be stored explicitly.

## 11. Redundancy and fallback

Infrastructure can survive partial failure.

```yaml
fallback_plan:
  fallback_id: null
  network_id: null
  trigger_conditions: []
  alternate_source_ids: []
  priority_service_ids: []
  shed_service_ids: []
  manual_operation_ids: []
  consumable_resource_refs: []
  duration_limits: []
```

This can produce meaningful choices during crises without inventing arbitrary timers.

Example questions:
- Does the clinic or the public transit depot receive backup power first?
- Can a pump be operated manually?
- Is refrigeration kept while decorative lighting is shut down?
- Can communications continue at reduced capacity?

The civic layer decides who has authority when canon requires a formal decision. This layer records what the system can physically do.

## 12. Pokémon-machine interaction

Pokémon interactions with devices are explicit per individual and per asset.

```yaml
pokemon_machine_interaction:
  interaction_id: null
  pokemon_id: null
  asset_id: null
  interaction_type: null
  observed_effect_ids: []
  voluntary_state: unknown
  operator_interpretation_ids: []
  governing_capability_refs: []
  governing_move_refs: []
  governing_feature_refs: []
  evidence_ids: []
  mechanical_validation_state: unresolved
```

Candidate interaction types:
- POWERS
- DRAWS_POWER
- OCCUPIES
- OPERATES
- INTERFERES
- SENSES
- MAINTAINS
- STABILIZES
- DAMAGING_INTERACTION
- UNKNOWN

No type grants a mechanical effect automatically.

Rotom is the clearest canonical Pokémon precedent for device-specific interaction, but even Rotom cannot be treated as universal admin access to every machine.

## 13. Infrastructure and ecology

Technical systems can alter habitats.

```yaml
tech_ecology_link:
  link_id: null
  asset_or_network_id: null
  location_id: null
  observed_ecological_effect_ids: []
  hypothesized_effect_ids: []
  mitigation_project_ids: []
  conservation_management_ids: []
  monitoring_program_ids: []
```

Possible observations:
- heat discharge;
- noise;
- light;
- electromagnetic activity;
- water-flow changes;
- pollution;
- habitat creation;
- food availability;
- shelter creation;
- altered human traffic.

The system must keep observation separate from causal interpretation.

## 14. Technical institutions

Technology should be socially situated.

Institution types may include:
- utility operator;
- repair cooperative;
- research laboratory;
- manufacturer;
- municipal works team;
- transit engineering unit;
- independent workshop;
- specialist contractor;
- apprenticeship school;
- historical preservation team.

Each institution may have different priorities and competence without being morally classified by default.

## 15. Lifecycle of a technical asset

Suggested lifecycle:

PROPOSED → BUILT → COMMISSIONING → ACTIVE → MAINTAINED / DEGRADED → REPAIRED / MODIFIED → DECOMMISSIONED / REPURPOSED

Old assets should remain part of history.

A decommissioned power station may become:
- a museum;
- a workshop;
- housing;
- a Pokémon habitat;
- a dungeon-like exploration site;
- an archaeological/industrial-heritage site;
- a source of contamination requiring cleanup.

No outcome is automatic.

## 16. Infrastructure incident propagation

An incident produces explicit downstream events.

```yaml
infrastructure_incident:
  incident_id: null
  origin_asset_id: null
  initial_fault_id: null
  affected_network_ids: []
  affected_service_ids: []
  route_impacts: []
  communications_impacts: []
  care_impacts: []
  economic_impacts: []
  ecological_impacts: []
  crisis_id: null
  case_id: null
  current_state: active
```

Do not jump directly from "generator failed" to "whole region blacked out" unless the dependency graph supports it.

## 17. Minecraft representation boundary

Minecraft may render:
- machines;
- cables/pipes as visual or logical connections;
- status lights;
- active/inactive animation;
- maintenance scaffolding;
- NPC technicians;
- locked access panels;
- backup equipment;
- damaged components;
- facility zones;
- Rotom or other persistent Pokémon nearby when canon permits.

The adapter must not become a second PTU rules engine.

Minecraft may request an operation and display a result. PTU/Caelo/AutoPTU remains authoritative for combat, Skills and Pokémon mechanics.

## 18. Routine compression

Most maintenance should happen in the background.

Surface maintenance as playable content when one of these is true:
- the player chose the profession/project;
- a finding changes world state;
- resources are constrained;
- there is uncertainty worth investigating;
- multiple services compete for capacity;
- ecology or public access is affected;
- a known relationship/NPC is involved;
- a past player action created the current system;
- failure or success will create a meaningful callback.

Do not generate daily "replace fuse" chores for every settlement.

## 19. Mechanical boundary

The generator must not invent:
- Technology Education DCs;
- machine repair bonuses;
- electricity damage;
- shock status;
- hazard zones;
- Move-powered generators;
- Rotom possession legality;
- Porygon network access;
- item crafting/repair rules;
- Trainer Feature effects;
- Skill Stunts;
- device stat bonuses;
- hacking rules;
- forced movement from machinery;
- reaction windows around machinery;
- custom interactable-object HP.

These require governing PTU/Caelo rules plus implementation evidence.

## 20. Encounter implementation contracts

### Substation Cascade

Narrative premise: a distribution substation has entered degraded operation. Players arrive while technicians isolate circuits and a territorial Pokémon encounter begins near the facility.

FULL version:
- changing powered/unpowered zones;
- interactable isolation controls;
- electrical hazard state;
- protect/hold technician objective;
- objective-aware enemy movement;
- possible reaction windows around machinery.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if machinery can move/intercept actors
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING if used for technical interventions
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version: technicians isolate the equipment before combat. AutoPTU receives a static legal arena. The operational consequence is resolved after battle through world-state checks rather than electrical battle hazards.

### Pump Hall Emergency

Narrative premise: a pumping station is losing capacity while wild Pokémon displaced by the disturbance occupy the access route.

FULL version:
- interactable pump controls;
- timed capacity loss;
- rising/falling environmental zones;
- REACH_OBJECT / ACTIVATE_OBJECT objective;
- objective-aware pathing.

Required blocking families:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback;
- complete movement if changing water or machinery forces displacement.

REDUCED version: pump state changes outside the battle grid. Players resolve a conventional encounter to secure access, then authorized operators perform the technical action.

### Factory Safe Shutdown

Narrative premise: a production line must be shut down safely after an abnormal condition while a separate encounter obstructs the control route.

FULL version:
- ordered interactable objectives;
- machine-state transitions during combat;
- fail-forward states rather than instant catastrophic loss;
- tactical AI that can contest objectives.

REDUCED version: machine shutdown is an overworld puzzle with reset/recovery states. Any combat is a separate static battle, preserving the same narrative premise without embedding unfinished object rules inside AutoPTU.

## 21. Promotion gates

A technical encounter may move from REDUCED to FULL only when:
1. exact PTU/Caelo mechanical effects are identified;
2. the required Java capability families have current parity evidence;
3. interactable-object semantics are defined if used;
4. tactical AI understands the objective when necessary;
5. Minecraft/Cobblemon/Craftics can faithfully display and send the required state;
6. failure/recovery states are tested so a persistent facility cannot softlock.

## 22. Canon questions left open

- What is the technological baseline of each Ouros region?
- Which cities operate centralized utilities versus local systems?
- Which services are public, private, guild-run or mixed?
- Which Pokémon are canonically used in infrastructure roles?
- What are the actual mechanical limits of Technology Education?
- Which PTU/Caelo repair/crafting Features carry into Ouros?
- Are Rotom devices common, rare or institution-specific?
- How advanced are automation and computer networks?
- How is technical training certified, if at all?
- Which historical industrial sites already exist before player arrival?
