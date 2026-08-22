# Ouros Manufacturing, Production Runs & Quality State Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

This layer models repeatable transformation at workshop-to-industrial scale: process definitions, production runs, work-in-progress, lot genealogy, in-process observations, deviations, quality disposition, rework, scrap, release and recall history.

The goal is persistent industrial world state. It is not a factory minigame, an ERP simulator or a source of new PTU crafting rules.

## 1. Authority boundaries

This layer owns:

- repeatable process definitions and revisions;
- manufacturing/production sites as production contexts;
- production campaigns and individual runs;
- work-in-progress lots;
- genealogy between input, intermediate and output lots;
- process-step execution records;
- in-process observations/checks as records;
- deviations from the intended process;
- nonconformance claims and their evidence;
- quality disposition state;
- rework/scrap history;
- release events;
- production-linked recalls;
- production change history.

It does not own:

- item mechanics, recipes or exact crafting legality -> Material Culture/PTU/Caelo;
- raw-material/item identity and provenance -> Material Culture;
- machine health, maintenance or faults -> Technology/Infrastructure;
- staff roles, shifts or qualifications -> Workplaces/Credentials;
- demand, procurement, inventory, storage, freight and stock availability -> Supply Chains;
- money -> Finance;
- waste streams/environmental pollution -> Waste/Air/Water/etc.;
- listings/sales -> Retail;
- scientific experiments/claims -> Science;
- criminal findings -> Cases/Illicit Networks;
- Minecraft machine blocks as authority -> never;
- battle rules -> AutoPTU-Java/PTU/Caelo.

## 2. Core separation

Never collapse these states:

```text
PROCESS_DEFINED
INPUTS_ALLOCATED
RUN_AUTHORIZED
RUN_STARTED
STEP_EXECUTED
WORK_IN_PROGRESS
OUTPUT_PRODUCED
OUTPUT_INSPECTED
DISPOSITION_DECIDED
RELEASED_FOR_USE
TRANSFERRED_TO_INVENTORY
```

Important no-inferences:

```text
produced != released
released != sold
physical lot != available stock
process deviation != defective output
defect claim != confirmed root cause
nonconformance != sabotage
rework != fraud
scrap != waste-stream completion
recall != criminal wrongdoing
same item type != same specification/revision
machine operational != product conforming
automated line != no human responsibility
factory-made item != different PTU effect
```

## 3. MANUFACTURING_SITE

A production site is a persistent world location or institution where repeatable processes occur.

```yaml
manufacturing_site:
  manufacturing_site_id: null
  workplace_id: null
  location_id: null
  operator_institution_id: null
  production_area_ids: []
  process_definition_ids: []
  technical_asset_ids: []
  storage_node_ids: []
  utility_dependency_ids: []
  waste_stream_ids: []
  access_policy_ids: []
  current_operational_state_ref: null
  history_event_ids: []
  canon_state: PROPOSED
```

A site can manufacture components, refined material, packaging, equipment or finished goods. It does not need to sell anything directly.

## 4. PROCESS_DEFINITION

A process definition is versioned. Old versions remain historically valid for old runs.

```yaml
process_definition:
  process_definition_id: null
  product_or_intermediate_ref: null
  revision_id: null
  effective_from: null
  supersedes_revision_id: null
  required_input_spec_refs: []
  ordered_step_refs: []
  required_asset_refs: []
  authored_staff_role_refs: []
  in_process_observation_refs: []
  output_spec_ref: null
  mechanical_rule_refs: []
  approval_claim_ids: []
  status: DRAFT
```

Suggested states:

- DRAFT
- PILOT
- ACTIVE
- LIMITED
- SUSPENDED
- SUPERSEDED
- RETIRED

A newer revision does not make older production history wrong.

## 5. PROCESS_STEP

```yaml
process_step:
  process_step_id: null
  process_definition_id: null
  sequence_index: null
  operation_type: null
  input_state_refs: []
  output_state_refs: []
  required_asset_ids_or_types: []
  required_staff_role_refs: []
  observation_point_refs: []
  authored_parameter_refs: []
  mechanics_review_required: true
```

Candidate operation labels:

- PREPARE
- SORT
- CLEAN
- REFINE
- FORM
- MIX
- ASSEMBLE
- FILL
- SEAL
- FINISH
- LABEL
- PACKAGE
- INSPECT
- HOLD
- TRANSFER

These labels never create PTU effects by themselves.

## 6. PRODUCTION_RUN

A production run is an execution of one process revision.

```yaml
production_run:
  production_run_id: null
  manufacturing_site_id: null
  process_definition_id: null
  process_revision_id: null
  planned_start: null
  actual_start: null
  actual_end: null
  input_lot_ids: []
  work_in_progress_lot_ids: []
  output_lot_ids: []
  step_execution_ids: []
  deviation_ids: []
  observation_ids: []
  operator_assignment_ids: []
  technical_asset_refs: []
  source_event_id: null
  status: PLANNED
```

Suggested states:

- PLANNED
- READY
- RUNNING
- PAUSED
- STOPPED
- COMPLETED
- ABORTED
- SUPERSEDED_RECORD

`COMPLETED` means the process finished. It does not mean the output is accepted for use.

## 7. LOT and WORK_IN_PROGRESS

Use a production lot when output or intermediate material must remain traceable.

```yaml
production_lot:
  lot_id: null
  item_or_material_ref: null
  specification_ref: null
  lot_role: INPUT|INTERMEDIATE|OUTPUT|REWORK
  parent_lot_ids: []
  child_lot_ids: []
  production_run_id: null
  quantity_ref_or_band: null
  condition_claim_ids: []
  current_disposition: HOLD
  material_batch_refs: []
  inventory_pool_ref: null
  history_event_ids: []
```

Work-in-progress can persist across pauses, shifts or maintenance events. Do not regenerate it as a new lot simply because the server unloaded the factory chunk.

## 8. LOT_GENEALOGY

```yaml
lot_genealogy_edge:
  genealogy_edge_id: null
  source_lot_id: null
  destination_lot_id: null
  transformation_type: null
  production_run_id: null
  process_step_execution_id: null
  quantity_relation_ref: null
  timestamp: null
  evidence_refs: []
```

Candidate transformations:

- CONSUMED_INTO
- SPLIT_INTO
- MERGED_INTO
- REFINED_INTO
- ASSEMBLED_INTO
- PACKAGED_AS
- REWORKED_INTO
- SCRAPPED_FROM

A downstream investigation can traverse genealogy without assuming the root cause lies in the earliest shared parent.

## 9. STEP_EXECUTION

```yaml
process_step_execution:
  execution_id: null
  production_run_id: null
  process_step_id: null
  process_revision_id: null
  started_at: null
  completed_at: null
  operator_assignment_refs: []
  asset_refs: []
  input_lot_refs: []
  output_lot_refs: []
  observed_parameter_refs: []
  deviation_ids: []
  status: COMPLETED
```

A missing record is an information problem. It is not automatic proof the step was skipped.

## 10. IN_PROCESS_OBSERVATION

An observation records what was measured or noticed during production.

```yaml
in_process_observation:
  observation_id: null
  production_run_id: null
  process_step_execution_id: null
  subject_lot_id: null
  observation_type: null
  observed_value_or_state: null
  expected_range_or_claim_ref: null
  observed_by_ids: []
  instrument_or_method_ref: null
  timestamp: null
  evidence_refs: []
  assessment_state: UNREVIEWED
```

Possible assessment states:

- UNREVIEWED
- WITHIN_EXPECTATION
- OUTSIDE_EXPECTATION
- INCONCLUSIVE
- INVALIDATED_MEASUREMENT
- SUPERSEDED

An out-of-range observation can be real while the final output remains acceptable after investigation. The reverse is also possible.

## 11. DEVIATION_RECORD

```yaml
deviation_record:
  deviation_id: null
  production_run_id: null
  process_step_execution_id: null
  expected_process_claim_ref: null
  observed_difference: null
  first_observed_at: null
  reported_by_ids: []
  affected_lot_ids: []
  immediate_action_ids: []
  cause_hypothesis_ids: []
  confirmed_cause_ids: []
  impact_assessment_ids: []
  case_id: null
  status: OPEN
```

Suggested states:

- OPEN
- UNDER_REVIEW
- IMPACT_UNCLEAR
- NO_PRODUCT_IMPACT_FOUND
- PRODUCT_IMPACT_FOUND
- CLOSED
- SUPERSEDED

Deviation is a process fact, not a moral judgment.

## 12. NONCONFORMANCE_CLAIM

```yaml
nonconformance_claim:
  nonconformance_id: null
  subject_lot_or_item_id: null
  specification_ref: null
  observed_difference_refs: []
  evidence_refs: []
  confidence: unresolved
  current_status: CLAIMED
  disposition_ref: null
```

Do not use one universal `quality_score`. A lot may be suitable for one authorized use and unsuitable for another if specifications differ.

## 13. QUALITY_DISPOSITION

Disposition answers what may happen next to a lot. It is not an intrinsic mechanical property.

```yaml
quality_disposition:
  disposition_id: null
  lot_id: null
  decision: HOLD
  decision_actor_or_scope_ref: null
  evidence_reviewed_ids: []
  restriction_refs: []
  effective_at: null
  supersedes_disposition_id: null
  rationale_claim_ids: []
```

Suggested decisions:

- HOLD
- RELEASE
- RELEASE_RESTRICTED
- REWORK
- SORT
- RETURN_TO_SOURCE
- SCRAP
- FURTHER_REVIEW

No universal Ouros law or regulatory authority is implied by these labels. Each institution needs an authored mandate if formal disposition authority matters.

## 14. RELEASE_EVENT

```yaml
release_event:
  release_event_id: null
  lot_id: null
  disposition_id: null
  released_by_scope_ref: null
  released_at: null
  destination_inventory_pool_id: null
  restriction_refs: []
  provenance_event_ref: null
```

After release, Supply Chains becomes the main authority for available stock. Manufacturing history remains linked.

## 15. REWORK_RECORD

```yaml
rework_record:
  rework_id: null
  source_lot_id: null
  approved_process_ref: null
  production_run_id: null
  output_lot_ids: []
  reason_ref: null
  verification_observation_ids: []
  disposition_id: null
  history_event_ids: []
```

Rework preserves genealogy. It never silently edits the original lot into a perfect version.

## 16. SCRAP_EVENT

Scrap exits manufacturing disposition but may enter Waste/Material Culture as another stream.

```yaml
scrap_event:
  scrap_event_id: null
  source_lot_id: null
  quantity_ref_or_band: null
  reason_ref: null
  destination_waste_or_recovery_ref: null
  timestamp: null
```

Scrap can later become salvage/recycled input only through the appropriate provenance and waste/recovery systems.

## 17. RECALL_EVENT

A recall is a world-state response to a credible concern about distributed output.

```yaml
recall_event:
  recall_event_id: null
  affected_lot_ids: []
  affected_item_instance_ids: []
  initiating_institution_or_actor_id: null
  initiating_signal_ids: []
  scope_claim: null
  started_at: null
  status: ACTIVE
  recovered_or_accounted_refs: []
  downstream_inventory_refs: []
  public_information_ids: []
  case_id: null
```

Suggested states:

- ACTIVE
- EXPANDING_SCOPE
- NARROWED_SCOPE
- COMPLETED
- SUPERSEDED

A recall does not prove negligence, fraud, sabotage or criminality.

## 18. CHANGE_CONTROL_RECORD

Process changes should have history even when informal or institution-specific.

```yaml
production_change_record:
  change_id: null
  process_definition_id: null
  old_revision_id: null
  new_revision_id: null
  change_reason_ids: []
  evidence_or_trial_ids: []
  affected_site_ids: []
  effective_at: null
  transition_run_ids: []
```

This is version history, not imported real-world regulation.

## 19. PILOT and SCALE-UP

A workshop or new process can scale gradually.

```text
CRAFTED_PROTOTYPE
→ PILOT_PROCESS
→ LIMITED_RUN
→ REPEATABLE_RUN
→ MULTI_SITE_OR_HIGH_VOLUME_PRODUCTION
```

Each transition can create stories around:

- tooling;
- staffing;
- supply compatibility;
- utility capacity;
- waste handling;
- storage;
- transport;
- quality evidence;
- public expectations;
- loss or preservation of craft identity.

Scale is not an automatic improvement or decline.

## 20. Pokémon participation

Pokémon may participate in authored production roles, but every relationship remains explicit.

Store:

- Pokémon identity;
- institution/partner relationship;
- observed task;
- voluntary/authorized participation state where canon defines it;
- relevant mechanical capability refs only when verified;
- current availability.

Do not infer:

- ownership from workplace participation;
- unlimited labor;
- consent from species lore;
- free energy/material generation;
- PTU bonuses;
- automation privileges;
- replacement of required staff qualifications.

If a Pokémon stops participating, first record the operational fact. Do not procedurally invent abuse, illness, disloyalty or sabotage as the explanation.

## 21. World handoffs

### Material Culture

Receives or supplies:

- persistent item/material identities;
- material batches;
- provenance events;
- mechanically validated item refs.

### Technology/Infrastructure

Owns:

- line/machine state;
- utilities;
- faults;
- maintenance;
- calibration state where it is a machine concern.

Manufacturing records which asset/revision was used.

### Workplaces

Owns staffing, roles, shifts, handoffs and training. Manufacturing references actual assignments.

### Supply Chains

Owns input allocation before production and output inventory/distribution after release.

### Waste

Receives scrap, rejected material and process waste only through explicit handoff.

### Cases/Illicit Networks

Receive deviation/diversion evidence only when facts justify an investigation. Manufacturing does not label misconduct.

### Science

Owns experimental claims. Pilot production can generate observations but does not become scientific truth automatically.

## 22. Minecraft projection

Minecraft may present:

- machines and line geometry;
- containers representing server-authoritative lots;
- process status signage;
- WIP locations;
- safe/closed production zones;
- workers and supporting Pokémon;
- visual output accumulation;
- maintenance/rework areas.

Minecraft must not decide:

- which process revision ran;
- what a lot contains;
- whether a check passed;
- whether a lot is released;
- whether an item is defective;
- recall scope;
- mechanical item effect;
- PTU damage/hazards from industrial scenery.

Chunk unload/reload must never reset production or recreate released/scrapped lots.

## 23. Offline advancement

Routine healthy production can be compressed into coarse progress if:

- an authored process is active;
- inputs were already allocated;
- staffing/technical dependencies are satisfied;
- no player-facing decision is pending;
- no unresolved mechanical action is being invented.

Stop coarse advancement when:

- a deviation requires review;
- an input specification changes;
- a machine fault blocks a step;
- a player-owned/significant batch is affected;
- a Pokémon participant changes availability;
- a recall/quality hold begins;
- an irreversible authored decision is needed.

Do not roll hidden random defects merely because time passed.

## 24. Encounter contracts

### Assembly Line Emergency Stop — FULL

Premise: an operational anomaly and unexpected Pokémon presence force a line stop while technicians isolate the process and clear people from a production area.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for moving workers, carriers, protected lanes or conveyor-like displacement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if hot surfaces, steam, machinery, conveyors or exclusion zones become tactical mechanics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `EVACUATE`, `REACH_SHUTOFF`, `PROTECT_TECHNICIAN`, `WITHDRAW`
- Minecraft/Cobblemon/Craftics playback: BLOCKING

Reduced version:

Stop machinery and evacuate workers in world state first. Freeze a safe factory-floor arena. Battle only the actors who remain. Resume diagnosis and production disposition afterward.

### Quality Hold Warehouse Transfer — FULL

Premise: a held production lot needs to be isolated or transferred while a separate confrontation threatens the route.

Dependencies:

- ordinary targeting/calculations/action economy: usable at VERIFIED scopes
- complete movement/interception: BLOCKING for moving cargo escort/intercept
- lifecycle/damage/status/move/ability/item/Feature families: current PARTIAL scope when invoked
- AI tactical policy: BLOCKING for `PROTECT_CARGO`, `INTERCEPT`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics playback: BLOCKING
- environmental family: BLOCKING only if warehouse machinery/conditions gain tactical mechanics

Reduced version:

Secure the lot outside the grid under explicit custody/hold state. Run a static chokepoint encounter. Determine quality disposition later from production records and observations; battle victory cannot release the lot.

### Rework Cell Disturbance — FULL

Premise: an output lot already assigned to rework is interrupted by a machine problem or wildlife incursion while its genealogy must remain intact.

Dependencies:

- base combat categories: current VERIFIED/PARTIAL scopes
- complete movement: BLOCKING for moving workers/WIP and interception
- terrain/hazards/zones/reactions: BLOCKING if active machinery or process zones affect combat
- AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_WORKER`, `REACH_EXIT`
- adapter/playback: BLOCKING

Reduced version:

Pause rework and move workers/WIP to a safe state outside the grid. Use a conventional static battle if conflict remains. Resume the same rework record afterward; never generate a fresh perfect lot because combat ended.

## 25. Hard non-inferences

Do not infer:

- factory floor -> Hazard Terrain;
- conveyor -> forced movement;
- furnace -> automatic Fire damage;
- chemical-looking tank -> Poisoned;
- loud machine -> Sonic effect;
- automated line -> perfect quality;
- machine fault -> defective lot;
- lot hold -> defect;
- deviation -> defect;
- defect -> sabotage;
- recall -> crime;
- rework -> counterfeit item;
- scrap -> destroyed provenance;
- same item model -> interchangeable revision;
- more production -> better settlement outcome;
- fewer workers -> exploitation;
- Pokémon labor -> ownership or unlimited consent;
- factory-made Poké Ball -> different capture rate from the same canonical mechanical item;
- successful battle -> production restart, quality release or root-cause conclusion.

## 26. Unresolved mechanical/canon questions

- Which products are manufactured at repeatable/industrial scale in each Ouros region?
- Which sites and companies/institutions exist before players arrive?
- Which products remain primarily artisan-made?
- How much lot-level detail should ordinary consumer goods retain?
- Who has authority to place/release institutional quality holds?
- Which recalls are public and how does public information propagate?
- How do player-owned workshops transition into repeatable production, if at all?
- Can clubs/businesses operate shared production sites in multiplayer?
- Which Pokémon participate in manufacturing roles, and under what explicit relationship?
- What exact PTU/Caelo rules govern Technology Education, crafting, repair, tools, recipes, extended actions and relevant Features?
- Which mechanically distinct item revisions actually exist, rather than merely narrative production revisions?
- How should production output enter authoritative Minecraft inventories without block/container duplication exploits?

Until PTU/Caelo and implementation contracts answer a mechanical question, manufacturing state remains narrative/world authority only.