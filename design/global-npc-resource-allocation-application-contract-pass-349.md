# Global NPC resource allocation application contract — Pass 349

Status: IMPLEMENTED GLOBAL CONTRACT
Date: 2026-09-08

## Purpose

Apply a Pass 348 resource-allocation decision to the operational reservation view without deleting or rewriting the reservation history that existed before the institutional decision.

Pass 349 is deliberately narrow. It does not decide priority. It does not derive authority. It does not communicate the result. It does not transfer custody.

## Existing owners retained

- Pass 201 owns authority and delegation semantics.
- Pass 339 owns source reservation lifecycle.
- Pass 343 owns physical handoff/custody.
- Pass 345 owns appointment communication state.
- Pass 346 owns successor handoff authorization.
- Pass 347 owns conflict detection/admission.
- Pass 348 owns the authorized allocation decision and its evidence.
- Procurement owns acquisition after a documented need.

Pass 349 owns only the append-only application record plus a deterministic operational projection over the Pass 339 reservation ledger.

## Executable records

`ResourceAllocationApplication` records:
- stable application ID;
- source Pass 348 resolution ID;
- exact resource ID;
- application kind;
- semantic application tick;
- exact displaced reservation IDs, when any;
- exact retained reservation ID, when any;
- optional basis/provenance references.

`ResourceAllocationApplicationLedger` stores application records in stable order.

## Supported V1 applications

### DISPLACE_CONFLICTING_RESERVATIONS

Produced only from `SELECT_PROPOSED_WINDOW`.

Every reservation that Pass 348 recorded in the conflict set is retained in the source ledger. The application records that those claims are displaced operationally by the institutional decision.

The derived planning view represents those still-ACTIVE source reservations as `CANCELLED` only for consumers that need current availability. This projection is not historical truth and must not replace the source ledger in persistence/provenance views.

### PRESERVE_SELECTED_RESERVATION

Produced from `SELECT_EXISTING_RESERVATION`.

The selected existing reservation remains operative. No conflicting reservation is silently changed by Pass 349. The proposed successor window remains a downstream negotiation/rejection problem.

### DEFER_NO_CHANGE

Produced from `DEFER`.

No reservation state changes in the derived operational view.

## Hard boundaries

`RESERVATION_DISPLACED != RESERVATION_NEVER_EXISTED`

`INSTITUTIONAL_DISPLACEMENT != RESERVATION_HOLDER_CANCELLED`

`ALLOCATION_DECISION != ALLOCATION_APPLICATION`

`ALLOCATION_APPLICATION != HOLDER_NOTIFICATION`

`ALLOCATION_APPLICATION != SUCCESSOR_RESERVATION_CREATED`

`ALLOCATION_APPLICATION != RESOURCE_CHECKED_OUT`

`ALLOCATION_APPLICATION != RESOURCE_TRANSFERRED`

`ALLOCATION_APPLICATION != RESOURCE_OPERATIONALLY_READY`

`WORLD_RESOURCE != PTU_ITEM`

## Validation

Application fails closed when:
- the application ID already exists;
- the same Pass 348 resolution was already applied;
- application time precedes the institutional decision;
- a conflict reservation recorded by Pass 348 no longer exists in the supplied source ledger;
- a conflict reservation references another resource;
- a conflict reservation is no longer ACTIVE at application time;
- a `SELECT_EXISTING_RESERVATION` result points outside the recorded conflict set.

The `CONFLICT_RESERVATION_NOT_ACTIVE` failure is deliberate. If the world changed between decision and application, the decision must be re-evaluated or applied through an explicit later rule. Pass 349 does not silently reinterpret stale decisions.

## Projection semantics

`project_allocation_onto_reservations()` returns a new `ReservationLedger`.

The source Pass 339 ledger is immutable.

Only ACTIVE reservations named by an application displacement are projected as CANCELLED. Closed historical states are never rewritten. Application provenance remains available in the separate ledger.

Downstream planners may use the projected ledger for availability checks. Historical UI, audit, memory and investigation systems should retain access to both ledgers.

## Why this matters for world simulation

An earlier booking can have been valid, visible and acted upon. A later authorized choice can still displace it.

That produces ordinary world consequences:
- somebody may have planned travel around a booking that is no longer operative;
- a colleague may remember the old schedule correctly;
- a later complaint can cite the original booking and the allocation decision;
- repeated displacement may contribute evidence to an existing Procurement need or institutional policy review;
- none of those outcomes require hidden reputation scores or retroactive history edits.

## Communication boundary

Pass 349 does not notify affected actors.

A later coordinator must create explicit communication events through the existing communication runtime. Until those events are delivered, an affected NPC may continue to act from older knowledge without being irrational.

## Procurement boundary

Repeated applications may become evidence for `procurement_need.source_event_ids` or equivalent authored evidence under the existing Procurement owner.

Pass 349 does not create a procurement need automatically. Frequency alone cannot prove that buying another unit is the correct remedy.

## Encounter dependency contract

The reduced implementation uses world-state systems only:
- semantic time;
- Pass 339 reservations;
- Pass 347 conflict assessment;
- Pass 348 allocation decision;
- Pass 349 application projection;
- communications, memory/belief and replanning when a scenario uses notification consequences.

No AutoPTU capability is required for the reduced version.

A mechanically rich variant may occur after a selected resource is physically collected and transported. Its dependencies remain explicit:
- targeting/footprints/range/LoS: VERIFIED within previously audited ordinary contracts;
- base movement legality: VERIFIED within previously audited ordinary contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within previously audited ordinary deterministic arithmetic;
- action economy/initiative: VERIFIED for audited primitives; pickup/drop/handoff/guard actions remain individually gated;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within ordinary audited action-generation scope;
- AI tactical policy: BLOCKING for escort, protect-carrier, preserve-resource, delivery-first and disengage-after-objective policies;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

No representative mechanic promotes an entire capability category.
