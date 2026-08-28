# Ouros Storage, Warehousing & Inventory Operations Continuity Extension

Status: PROPOSED systems design. Not established Ouros canon. No PTU rules are created here.
Date: 2026-08-28
Research provenance: `research/2026-08-28-storage-warehousing-inventory-operations-scan-104.md`.

## Purpose

Ouros already knows how goods are created, ordered, accepted, transported, recalled, sold, issued and consumed. This extension preserves the operational state between those systems when physical goods spend meaningful time in a storage facility.

It owns internal storage location, putaway, picking, staging, inventory observations, reconciliation, capacity/overflow state and handoff readiness. It does not create item mechanics, ownership law, shipment custody rules, procurement acceptance, production output, storefront stock rules or recall authority.

## Authority boundary

This layer owns:

- persistent storage-facility and storage-zone identity;
- addressable bays/shelves/slots only when narratively useful;
- operational accessibility of storage areas;
- authorized intake awaiting putaway;
- internal movement tasks;
- verified physical presence/location observations;
- pick and staging workflow;
- readiness for an external handoff;
- inventory observations and discrepancy reconciliation;
- broad capacity state and overflow episodes;
- facility/zone storage history and reuse.

It references but does not own:

- item instance/material batch identity and rules-bearing effects — Material Culture/PTU/Caelo;
- sourcing, receipt and acceptance — Procurement;
- production runs/WIP/output release — Manufacturing;
- shipment legs and custody transfers — Courier/Port/other transport owner;
- recall/quarantine/correction decision — Batch Traceability;
- customer-facing availability — Storefront;
- issued assets — Shared Equipment;
- money/payment — Finance;
- technical repair — Facility Maintenance;
- safety restrictions — Worksite Safety/Crisis as applicable;
- credentials/permissions — Credentials/Authority;
- Minecraft blocks/entities — presentation only.

## 1. Storage facility

```yaml
storage_facility:
  storage_facility_id: null
  containing_location_or_asset_ref: null
  operator_actor_or_institution_id: null
  facility_class: null
  zone_ids: []
  receiving_interface_ids: []
  dispatch_interface_ids: []
  maintenance_dependency_ids: []
  utility_dependency_ids: []
  safety_dependency_ids: []
  access_dependency_ids: []
  current_operating_state: OPERATIONAL
  capacity_snapshot_id: null
  overflow_episode_ids: []
  history_event_ids: []
  provenance_refs: []
```

Candidate descriptive classes:

- BACK_ROOM
- GENERAL_STOREHOUSE
- DISTRIBUTION_DEPOT
- REFRIGERATED_STORAGE
- INSTITUTIONAL_STORES
- ARCHIVE_OR_SECURE_STORE
- PORT_OR_TRANSIT_STORAGE
- MOBILE_ASSET_STORAGE
- TEMPORARY_OVERFLOW_SITE
- OTHER_AUTHORED

A class grants no mechanical protection, temperature effect, security bonus or item legality.

## 2. Facility operating state

```yaml
storage_operating_state:
  state_id: null
  storage_facility_id: null
  effective_from: null
  state: OPERATIONAL
  affected_zone_ids: []
  reason_refs: []
  verification_refs: []
  supersedes_state_id: null
```

Useful states:

- OPERATIONAL
- CONSTRAINED
- PARTIAL
- INTAKE_PAUSED
- DISPATCH_PAUSED
- ACCESS_RESTRICTED
- MAINTENANCE
- SAFETY_HOLD
- TESTING
- CLOSED
- RELOCATING
- MOTHBALLED

A facility may remain operational while one zone is inaccessible.

## 3. Storage zone

```yaml
storage_zone:
  zone_id: null
  storage_facility_id: null
  zone_kind: null
  parent_zone_id: null
  slot_ids: []
  access_scope_refs: []
  authored_condition_refs: []
  current_state: AVAILABLE
  current_presence_refs: []
  active_task_ids: []
  maintenance_dependency_ids: []
```

Possible descriptive zone kinds include receiving, general storage, secure/restricted, specialized environment, staging, dispatch, returns, quarantine-linked or overflow.

`specialized environment` records world design only. If temperature, humidity, electricity or another condition has a mechanical effect, that effect needs governing rules and implementation evidence.

## 4. Storage slot or bay

Only create a slot when exact location matters.

```yaml
storage_slot:
  slot_id: null
  zone_id: null
  physical_anchor_ref: null
  slot_label_claims: []
  current_state: AVAILABLE
  reserved_for_ref: null
  observed_presence_refs: []
  last_verified_at: null
  access_dependency_refs: []
```

Suggested states:

- AVAILABLE
- OCCUPIED
- RESERVED
- BLOCKED
- INACCESSIBLE
- MAINTENANCE
- UNKNOWN

`EMPTY != AVAILABLE`.

A visually empty shelf may be reserved, inaccessible or awaiting verification.

## 5. Inventory presence

```yaml
warehouse_inventory_presence:
  presence_id: null
  item_instance_refs: []
  material_batch_refs: []
  aggregate_inventory_ref: null
  storage_facility_id: null
  zone_id: null
  slot_id: null
  observed_quantity_claim: null
  observed_condition_claims: []
  observed_at: null
  observed_by_ids: []
  source_refs: []
  verification_state: OBSERVED
  external_hold_or_allocation_refs: []
```

Presence is an observation, not ownership or availability.

Bulk mundane stock may remain aggregate. Significant items or disputed batches can use exact identity.

## 6. Authorized storage intake

Storage begins only after another owning system authorizes the goods to enter storage workflow.

```yaml
storage_intake:
  storage_intake_id: null
  source_receipt_or_release_ref: null
  item_or_batch_refs: []
  aggregate_inventory_ref: null
  receiving_interface_id: null
  accepted_for_storage_at: null
  intake_observation_refs: []
  putaway_task_ids: []
  status: AWAITING_PUTAWAY
```

Suggested states:

- AWAITING_EXTERNAL_ACCEPTANCE
- ACCEPTED_FOR_STORAGE
- AWAITING_PUTAWAY
- PARTIALLY_PUT_AWAY
- PUT_AWAY_COMPLETE
- HELD_BY_EXTERNAL_AUTHORITY
- REJECTED_OR_REDIRECTED_BY_OWNER
- SUPERSEDED

Procurement or another relevant system owns acceptance. Warehouse state records what happened next.

## 7. Putaway task

```yaml
putaway_task:
  putaway_task_id: null
  storage_intake_id: null
  subject_refs: []
  origin_zone_or_interface_id: null
  intended_zone_id: null
  intended_slot_id: null
  assigned_actor_ids: []
  started_at: null
  completed_at: null
  completion_observation_refs: []
  exception_refs: []
  status: PLANNED
```

Lifecycle:

PLANNED -> READY -> IN_PROGRESS -> PHYSICALLY_PLACED -> VERIFIED_COMPLETE.

Branches: BLOCKED, PARTIAL, REDIRECTED, CANCELLED, SUPERSEDED.

`PHYSICALLY_PLACED != VERIFIED_COMPLETE`.

## 8. Internal move

```yaml
storage_internal_move:
  internal_move_id: null
  subject_refs: []
  from_zone_id: null
  from_slot_id: null
  to_zone_id: null
  to_slot_id: null
  reason_refs: []
  authorization_refs: []
  started_at: null
  completed_at: null
  verification_refs: []
  status: PLANNED
```

An internal move normally changes operational location. It does not automatically transfer ownership or external custody.

## 9. Pick task

The request to pick comes from the system that owns the downstream need.

```yaml
storage_pick_task:
  pick_task_id: null
  request_ref: null
  subject_refs: []
  source_zone_or_slot_refs: []
  destination_staging_zone_id: null
  assigned_actor_ids: []
  requested_at: null
  started_at: null
  completed_at: null
  verification_refs: []
  exception_refs: []
  status: PLANNED
```

Suggested states:

PLANNED, READY, IN_PROGRESS, PICKED, PARTIAL, NOT_FOUND, BLOCKED, CANCELLED, SUPERSEDED.

`PICKED != DISPATCHED`.

## 10. Staging record

```yaml
storage_staging_record:
  staging_id: null
  subject_refs: []
  source_pick_task_ids: []
  staging_zone_id: null
  intended_handoff_ref: null
  staged_at: null
  verification_refs: []
  external_hold_refs: []
  state: STAGED
```

Candidate states:

- STAGED
- HANDOFF_READY
- HELD
- RESTAGE_REQUIRED
- RETURN_TO_STORAGE_REQUIRED
- HANDED_OFF_EXTERNAL
- CANCELLED

`HANDOFF_READY` is a warehouse fact. Courier, Port, Shared Equipment or another owning system records the actual custody/issue handoff.

## 11. Inventory observation

```yaml
inventory_observation:
  observation_id: null
  storage_facility_id: null
  scope_zone_ids: []
  scope_slot_ids: []
  subject_refs: []
  observed_at: null
  observed_by_ids: []
  method_claim: null
  observed_presence_claims: []
  comparison_record_refs: []
  provenance_refs: []
```

A count or scan is evidence at a time and scope. It is not omniscient truth.

## 12. Reconciliation case

```yaml
storage_reconciliation:
  reconciliation_id: null
  storage_facility_id: null
  discrepancy_claim_refs: []
  relevant_presence_ids: []
  relevant_task_ids: []
  relevant_external_refs: []
  hypotheses: []
  verified_findings: []
  corrected_location_refs: []
  correction_event_refs: []
  unresolved_refs: []
  status: OPEN
```

Candidate causes may be proposed only as hypotheses:

- observation timing mismatch;
- stale slot label;
- legitimate internal move;
- staged but not handed off;
- returned but not put away;
- duplicate record;
- wrong scope;
- external hold;
- unknown.

Do not jump from discrepancy to theft, fraud, loss or sabotage.

## 13. Capacity snapshot

```yaml
storage_capacity_snapshot:
  snapshot_id: null
  storage_facility_id: null
  observed_at: null
  overall_band: UNKNOWN
  zone_bands: []
  receiving_pressure_band: null
  staging_pressure_band: null
  overflow_active: false
  basis_refs: []
```

Suggested broad bands:

- AVAILABLE
- CONSTRAINED
- SATURATED
- UNAVAILABLE
- UNKNOWN

These bands support narrative continuity. They do not define cubic volume, pallet counts, throughput or productivity formulas.

## 14. Overflow storage episode

```yaml
overflow_storage_episode:
  overflow_episode_id: null
  source_facility_id: null
  overflow_location_id: null
  trigger_refs: []
  authorized_scope_refs: []
  subject_refs: []
  began_at: null
  expected_review_at: null
  ended_at: null
  access_refs: []
  maintenance_or_safety_refs: []
  downstream_effect_refs: []
  state: ACTIVE
```

Temporary overflow may become socially important without silently becoming a permanent warehouse.

## 15. External holds and quarantine

Batch Traceability or another owning system decides whether a batch is held, quarantined, recalled, cleared or corrected.

Warehouse may enforce the physical consequence:

```yaml
storage_external_hold_binding:
  binding_id: null
  external_hold_ref: null
  subject_refs: []
  enforced_zone_or_slot_refs: []
  enforcement_started_at: null
  enforcement_verified_at: null
  released_by_external_ref: null
  enforcement_state: ACTIVE
```

Moving tape, signs or Minecraft barriers does not cancel the underlying hold.

## 16. Downstream availability

A warehouse can possess stock while a store remains unavailable, a production line remains stopped, or a shipment remains unscheduled.

Warehouse should expose references such as:

- physically present;
- verified location;
- held/not held according to linked authority;
- picked/not picked;
- staged/not staged;
- handoff-ready/not ready.

The consuming system decides what those facts mean for its own availability.

## 17. Facility history and reuse

```yaml
storage_history_event:
  event_id: null
  storage_facility_id: null
  event_type: null
  effective_at: null
  changed_zone_refs: []
  changed_use_refs: []
  source_refs: []
  successor_location_refs: []
  public_memory_refs: []
```

Useful event types include OPENED, EXPANDED, SPECIALIZED, PARTIALLY_CLOSED, RELOCATED, MOTHBALLED, DEMOLISHED, REPURPOSED and OVERFLOW_ACTIVATED.

Old worker routes, labels, names or neighborhood habits may survive after operational use changes.

## 18. Pokémon work assignments

A Pokémon can participate only through an individual authored assignment with evidence appropriate to the task.

Do not infer warehouse competence from:

- species;
- Type;
- size;
- Strength-like visual presentation;
- an anime precedent;
- a Minecraft carrying/riding animation;
- proximity to goods.

If a task requires a PTU Capability, Move, Ability, Item or Trainer Feature, the exact rule path must be verified before mechanical execution.

## 19. Encounter boundary

Storage is usually noncombat content. When violence occurs, world operations pause before tactical resolution whenever possible.

Ouros remains authoritative for:

- which actors and Pokémon are combatants;
- which warehouse areas are inside the arena;
- which goods are tactical scenery versus excluded world objects;
- which workers/nonparticipants have already evacuated;
- the post-battle operational consequence.

AutoPTU remains authoritative for tactical battle state and results.

Minecraft/Cobblemon presents geometry, entities, animation, UI and playback but never decides inventory truth, custody, damage, forced movement or combatant membership.

## 20. Encounter concepts

### Receiving Dock Withdrawal — full

Premise: an operational disruption requires staff and noncombatants to withdraw through more than one reviewed route while hostile participants threaten the perimeter.

Required capability families:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including Intercept/forced movement;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle as required by exact combatants;
- terrain/weather/hazards/zones/reactions if active loading equipment, moving vehicles or dock hazards matter;
- move-specific behavior, abilities, items and Trainer Features/perks as used;
- AI legal-action infrastructure;
- AI tactical policy for withdrawal/protection objectives;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced form:

Freeze intake and dispatch first. Evacuate workers, cargo, vehicles/equipment and nonparticipant Pokémon. Ouros creates a reviewed static yard or dock-apron BattleSpec with explicit combatants. Victory secures immediate access only. Procurement, Courier and Storage resume their own workflows afterward.

### Staging Aisle Perimeter — full

Premise: a conflict near outbound staging threatens access to a prepared handoff without making the goods themselves combat rewards.

Full form may require narrow-route protection, Intercept/forced movement, generalized reactions, tactical AI and semantic playback. Any falling-rack, conveyor or moving-equipment mechanic additionally requires terrain/hazards/zones support and an exact governing rule.

Reduced form:

Staged goods remain off-grid or inert untargetable world objects. The handoff is frozen at its last verified state. Combat occurs in a static aisle/perimeter. Victory changes only immediate access/safety state; it does not dispatch goods, change custody or reveal container contents.

### Overflow Yard Conflict — full

Premise: a temporary outdoor storage area becomes contested while the original facility remains capacity-constrained.

Full form may require reviewed terrain, weather/hazard zones, route protection, reactions, objective-aware AI and playback.

Reduced form:

Overflow stock and workers remain outside the BattleSpec. Weather is presentation-only unless an exact PTU Weather contract is intentionally active. Combat uses a static perimeter. Victory does not change ownership, count, quarantine status or storage disposition.

## 21. Minecraft/Cobblemon boundary

Safe reuse includes:

- warehouse/building geometry;
- shelves, racks, bays, crates and containers as presentation;
- doors, lights, signs and barriers;
- sounds and particles;
- forklifts/conveyors/vehicles as nonauthoritative visual assets when available;
- Pokémon models/forms/poses/animations/cries;
- NPCs;
- UI, networking, entity tracking and persistence hooks.

Adapter responsibilities include:

- stable binding for facility/zone/slot IDs;
- mapping world objects to narrative inventory references without making every block authoritative;
- projecting access and operational state;
- reviewed conversion of geometry to AutoPTU arena cells;
- preserving world identity through unload/reload;
- semantic battle playback.

Minecraft/Cobblemon must never decide that:

- an item is stored because an entity entered a chest;
- a putaway task completed because a hopper moved an item;
- a slot is available because it looks empty;
- a count is correct because entities are visible;
- custody transferred because two entities crossed a line;
- a quarantine ended because a barrier moved;
- a worker is assigned because a Pokémon stands nearby;
- native collision/falling blocks/fire/ice apply PTU effects;
- every entity inside the warehouse is a combatant.

## Canon status

Everything in this extension is PROPOSED unless a referenced established source already owns the underlying fact.

The layer introduces no warehouses, technologies, institutions, labor systems or storage standards into canon by itself.
