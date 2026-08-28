# Ouros Manufacturing, Factories & Production Continuity Extension

Status: PROPOSED systems design. Not established canon. No PTU rules are created here.
Date: 2026-08-28
Research provenance: `research/2026-08-28-manufacturing-factories-production-continuity-scan-103.md`.

## Purpose

Ouros already models mechanically validated crafting actions, workshops, commissions, material provenance, procurement, supplier fulfillment, batch traceability, recalls, workplaces, utilities, maintenance, safety, logistics and storefront availability.

This extension adds the missing continuity layer for repeated organized production. It preserves facility identity, production lines/cells, run history, work-in-process, interruptions, release decisions and staged restart without creating a second crafting engine or an economy simulator.

The core rule is simple: production state records what the world has actually done. Mechanical item creation still requires the governing PTU/Caelo/AutoPTU rule path when a real recipe or item effect is involved.

## 1. Production facility

```yaml
production_facility:
  facility_id: null
  location_id: null
  operator_institution_id: null
  facility_class: null
  product_family_tags: []
  production_line_ids: []
  storage_area_ids: []
  quality_area_ids: []
  maintenance_area_ids: []
  public_access_area_ids: []
  restricted_area_ids: []
  utility_dependency_ids: []
  supplier_dependency_ids: []
  outbound_logistics_dependency_ids: []
  staffing_dependency_ids: []
  safety_dependency_ids: []
  environmental_dependency_ids: []
  current_operating_state: null
  history_event_ids: []
```

Candidate classes:
- ARTISAN_CLUSTER
- WORKSHOP_NETWORK
- SMALL_PLANT
- SPECIALIZED_FACTORY
- REFINERY
- FABRICATION_SITE
- PACKAGING_SITE
- PILOT_PLANT
- INSTITUTIONAL_PRODUCTION_SITE

Facility class is descriptive. It grants no unreviewed capability or output.

## 2. Operating state

```yaml
production_operating_state:
  state_id: null
  facility_id: null
  effective_from: null
  state: OPERATIONAL
  scope_line_ids: []
  reason_claim_ids: []
  source_event_ids: []
  verification_ids: []
  supersedes_state_id: null
```

Suggested states:
- OPERATIONAL
- LIMITED
- INPUT_CONSTRAINED
- STAFF_CONSTRAINED
- UTILITY_CONSTRAINED
- QUALITY_HOLD
- MAINTENANCE_STOP
- SAFETY_STOP
- ENVIRONMENTAL_RESTRICTION
- TESTING
- MOTHBALLED
- CLOSED
- RECONFIGURING

A facility may remain OPERATIONAL while one line is stopped.

## 3. Production line or cell

```yaml
production_line:
  line_id: null
  facility_id: null
  line_type: null
  configured_product_family_refs: []
  process_step_refs: []
  tool_or_machine_refs: []
  required_staff_role_ids: []
  input_interface_ids: []
  output_interface_ids: []
  current_configuration_id: null
  current_state: READY
  active_run_id: null
  queued_run_ids: []
  maintenance_dependency_ids: []
  safety_dependency_ids: []
```

Suggested states:
- READY
- SETUP
- RUNNING
- PAUSED
- BLOCKED
- QUALITY_HOLD
- MAINTENANCE
- TESTING
- IDLE
- MOTHBALLED

`READY != RUNNING`.

A conveyor animation or machine sound in Minecraft is not evidence of RUNNING unless Ouros has an active run record.

## 4. Production order

```yaml
production_order:
  production_order_id: null
  requesting_actor_or_institution_id: null
  product_ref: null
  requested_quantity_claim: null
  priority_claim: null
  required_by_claim: null
  procurement_ref_ids: []
  finance_ref_ids: []
  commission_ref_ids: []
  governing_recipe_or_rule_refs: []
  production_run_ids: []
  status: REQUESTED
```

Suggested states:
REQUESTED, ACCEPTED, MATERIAL_PENDING, SCHEDULED, IN_PRODUCTION, PARTIALLY_FULFILLED, FULFILLED, CANCELLED, SUPERSEDED.

The quantity field is a claim unless authoritative implementation data defines the unit and amount.

## 5. Production run

```yaml
production_run:
  production_run_id: null
  production_order_ids: []
  facility_id: null
  line_id: null
  product_ref: null
  governing_recipe_or_rule_refs: []
  planned_input_batch_ids: []
  consumed_input_batch_ids: []
  work_in_process_ids: []
  produced_output_batch_ids: []
  started_at: null
  physically_completed_at: null
  released_at: null
  state: PLANNED
  interruption_ids: []
  quality_review_ids: []
  operator_assignment_ids: []
  source_event_ids: []
```

Lifecycle:
PLANNED → SETUP → READY → RUNNING → PHYSICALLY_COMPLETE → UNDER_REVIEW → RELEASED.

Branches:
PAUSED, BLOCKED, ABORTED, REWORK_REQUIRED, REJECTED, SUPERSEDED.

Hard separation:
`PHYSICALLY_COMPLETE != RELEASED`.

## 6. Work-in-process

```yaml
work_in_process:
  wip_id: null
  production_run_id: null
  source_input_batch_ids: []
  current_process_step_ref: null
  physical_location_id: null
  current_custodian_id: null
  condition_claim_ids: []
  hold_reason_ids: []
  next_allowed_step_ref: null
  status: ACTIVE
```

Suggested states:
ACTIVE, WAITING, HELD, REWORK, SCRAP_CANDIDATE, TRANSFERRED, CONSUMED_IN_OUTPUT.

Work-in-process exists so a stoppage does not erase partially transformed material.

## 7. Process step record

```yaml
process_step_record:
  step_record_id: null
  production_run_id: null
  process_step_ref: null
  input_refs: []
  output_refs: []
  operator_ids: []
  tool_or_machine_refs: []
  started_at: null
  ended_at: null
  governing_rule_refs: []
  validation_state: null
  result: null
  observation_ids: []
```

Narrative can record that a step occurred.

If the step is a PTU crafting action, item transformation or rules-bearing effect, `governing_rule_refs` and mechanical validation remain mandatory.

## 8. Interruption

```yaml
production_interruption:
  interruption_id: null
  facility_id: null
  line_id: null
  production_run_id: null
  detected_at: null
  interruption_class: null
  initial_claim_ids: []
  confirmed_cause_ids: []
  affected_scope_ids: []
  immediate_action_ids: []
  maintenance_ref_ids: []
  safety_ref_ids: []
  utility_ref_ids: []
  supplier_ref_ids: []
  environment_ref_ids: []
  status: OPEN
```

Candidate classes:
- MATERIAL_SHORTAGE
- STAFFING_GAP
- UTILITY_LOSS
- MACHINE_FAULT
- CALIBRATION_ISSUE
- QUALITY_CONCERN
- SAFETY_STOP
- ACCESS_RESTRICTION
- LOGISTICS_BLOCK
- ENVIRONMENTAL_RESTRICTION
- UNKNOWN

`UNKNOWN` is valid. A stoppage does not imply sabotage.

## 9. Quality review

```yaml
production_quality_review:
  review_id: null
  production_run_id: null
  output_batch_ids: []
  reviewer_ids: []
  evidence_ids: []
  governing_spec_refs: []
  scope_claim_ids: []
  decision: PENDING
  decision_time: null
  disposition_ids: []
  supersedes_review_id: null
```

Suggested decisions:
PENDING, RELEASE, PARTIAL_RELEASE, HOLD, REWORK, REJECT, ESCALATE, INCONCLUSIVE.

A visual anomaly is evidence, not an automatic defect.

Quality review cannot invent item mechanics. If an output has a PTU mechanical defect/effect, that behavior requires governing implementation support.

## 10. Rework and disposition

```yaml
production_disposition:
  disposition_id: null
  output_or_wip_ids: []
  decision: null
  authorized_by_ids: []
  destination_ref: null
  rework_run_id: null
  batch_traceability_ref_ids: []
  waste_ref_ids: []
  status: PLANNED
```

Candidate decisions:
RELEASE, REWORK, RETURN_TO_INPUT, DOWNGRADE_NARRATIVE_ONLY, HOLD, SCRAP, QUARANTINE, TRANSFER_FOR_REVIEW.

`DOWNGRADE_NARRATIVE_ONLY` cannot alter mechanical item statistics.

## 11. Restart lifecycle

A stopped line should not jump directly to full production.

Suggested sequence:
1. interruption isolated;
2. Maintenance/Safety/Utility owner performs its work;
3. physical repair or dependency restoration completes;
4. line enters TESTING;
5. test evidence is reviewed;
6. line becomes READY;
7. a new or resumed run starts;
8. output receives normal review/release.

Hard separation:
`REPAIR_COMPLETE != READY`.
`READY != RUNNING`.
`RUNNING != RELEASED_OUTPUT_AVAILABLE_DOWNSTREAM`.

## 12. Capacity without fake industrial arithmetic

```yaml
production_capacity_snapshot:
  snapshot_id: null
  facility_id: null
  line_id: null
  observed_at: null
  capacity_band: NORMAL
  limiting_reason_ids: []
  source_ids: []
  expires_or_review_at: null
```

Suggested bands:
NORMAL, CONSTRAINED, SEVERELY_CONSTRAINED, UNAVAILABLE, UNKNOWN.

Exact units-per-hour, utilization, yield and OEE-like metrics are used only if canon/implementation data explicitly defines them.

## 13. Public tours and restricted production

A facility can expose selected areas to visitors while keeping production truth and access separate.

```yaml
production_visit_program:
  program_id: null
  facility_id: null
  accessible_area_ids: []
  restricted_area_ids: []
  schedule_ref_ids: []
  guide_role_ids: []
  safety_requirement_ids: []
  operational_dependency_ids: []
  status: ACTIVE
```

A tour closing does not imply production stopped. Production stopping does not necessarily close the whole property.

## 14. Facility historical continuity

```yaml
production_facility_history_event:
  event_id: null
  facility_id: null
  event_type: null
  effective_at: null
  prior_use_claim_ids: []
  new_use_claim_ids: []
  affected_line_ids: []
  source_ids: []
  public_memory_ref_ids: []
```

Candidate types:
OPENED, EXPANDED, RECONFIGURED, LINE_ADDED, LINE_REMOVED, MOTHBALLED, RESTARTED, CLOSED, REPURPOSED, PARTIALLY_REUSED.

Repurposing preserves place identity and history.

## 15. Integration ownership

Material Culture/Crafting owns:
- actual recipe knowledge;
- mechanically validated crafting/production actions;
- item-instance significance and provenance.

Procurement owns:
- sourcing obligations;
- supplier fulfillment;
- purchase/commission inputs.

Batch Traceability owns:
- batch ancestry;
- recall/quarantine scope;
- downstream trace.

Workplaces owns:
- employment/staff roles and staffing relationships.

Maintenance owns:
- diagnosis, repair, inspection and verification of equipment/facilities.

Worksite Safety owns:
- hazard reporting, near misses, incidents and safety decisions.

Infrastructure/Utilities owns:
- service availability and restoration.

Waste/Sanitation/Conservation/Science own:
- pollution, waste, ecological and scientific interpretation.

Courier/Ports/Rail/Road/Aviation own:
- movement after custody/dispatch handoff.

Commercial Services owns:
- downstream public availability.

Manufacturing owns:
- facility/line/run/WIP operational history;
- staged interruption and restart state;
- production-release continuity.

## 16. Pokémon work-role boundary

No species or Type is inherently a factory worker.

A Pokémon production role requires:
- a persistent individual `pokemon_id`;
- explicit assignment/relationship state;
- governing PTU/Caelo capability, Move, Ability, Item or Feature evidence if the role depends on mechanics;
- safety/cultural authorization if canon later defines it.

A Fire-type near a furnace does not prove heat-work capability. An Electric-type near machinery does not prove power-generation or repair competence. A Machoke model beside a crate does not prove lifting capacity beyond governing rules.

## 17. Minecraft/Cobblemon boundary

Safe reuse includes:
- factory/workshop buildings;
- conveyors and decorative machinery;
- doors, lights, sounds, particles and status boards;
- storage racks and containers as presentation;
- Pokémon models/forms/poses/animations/cries;
- NPCs;
- UI, networking, entity tracking and persistence hooks.

Adapter-required work includes:
- stable facility/line/run/WIP bindings;
- authoritative state projection;
- revised arena conversion;
- semantic event playback;
- persistence across chunk unload/reload.

Minecraft/Cobblemon never decides that:
- a recipe completed because redstone fired;
- an item entity crossing a conveyor became a produced item;
- a batch passed quality because it reached a chest;
- a machine repaired because a block was replaced;
- a Pokémon is a worker because it is nearby;
- a factory accident applies PTU damage from native block damage;
- everyone inside the facility is a combatant;
- Cobblemon BattleState/controller logic owns combatant selection, legality or battle truth.

## 18. Encounter implementation profiles

### Line Shutdown Withdrawal

Narrative premise:
An operational incident or hostile intrusion requires explicit withdrawal from a production hall while preserving a safe route.

Full intended version depends on:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- action economy/initiative;
- full turn/round lifecycle;
- terrain/weather/hazards/zones/reactions for active machinery or process hazards;
- AI legal-action infrastructure;
- AI tactical policy for withdrawal/protection;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:
Ouros stops the line first. Workers, WIP, machinery, moving conveyors and nonparticipant Pokémon leave the BattleSpec. The fight occurs in a reviewed static aisle/yard. Victory secures only the immediate area. Restart requires separate Maintenance/Safety/Manufacturing review.

### Loading Bay Production Hold

Narrative premise:
A dispute or threat at the boundary between released production and outbound logistics interrupts handoff.

Full intended version depends on:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement for protected withdrawal/interception;
- action economy/initiative;
- full turn/round lifecycle;
- terrain/hazards/zones/reactions if vehicles, moving loads or active dock machinery matter;
- AI legal-action infrastructure;
- AI tactical policy;
- adapter/playback support.

Reduced version:
Manufacturing freezes the batch at the last verified custody state. Cargo, vehicles, operators and forklifts remain outside the grid. AutoPTU receives only explicit combatants in a static perimeter. Victory does not transfer custody or dispatch goods.

### Reconfiguration Cell Perimeter

Narrative premise:
A line being reconfigured or tested becomes the setting for a conflict whose story depends on access to the area, not on simulating machinery.

Full intended version may depend on:
- reviewed terrain;
- generalized reactions;
- forced movement;
- zones/hazards if energized equipment is mechanically active;
- tactical AI;
- playback.

Reduced version:
The cell is de-energized before battle. Tools, test equipment and staff are excluded from the BattleSpec. The tactical result secures access only. Testing and readiness decisions occur afterward in world state.

## 19. Immediate noncombat value

This extension is usable now for:
- persistent factory/workshop identity;
- production line/cell history;
- orders and scheduled runs;
- WIP continuity;
- staged stoppages;
- quality holds and releases;
- rework history;
- dependency-driven shortages;
- staged restart;
- public tour versus production access;
- recurring workers/operators;
- downstream service pressure without invented economics;
- facility repurposing and industrial memory.

## 20. Canon questions left open

- Which regions of Ouros have organized factories, refineries or fabrication sites?
- Which products are locally produced versus imported?
- What production technologies exist at each development level?
- Which institutions own or operate major facilities?
- Which labor and safety norms exist?
- Which plants permit public tours?
- Which industrial sites have historical, civic or ecological significance?
- Which individual Pokémon, if any, hold production roles and under what governing evidence?

No answer becomes canon through this extension.
