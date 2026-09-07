# Global NPC resource reservation lifecycle contract — Pass 339

Status: DESIGN / EXECUTABLE CONTRACT
Date: 2026-09-07
Canon authority: NONE

## Purpose

Extend Pass 338 resource-aware intents with temporal reservation state while preserving one global, region-neutral world-agent architecture.

This contract owns booking lifecycle only. It does not define PTU Item effects, custody evidence, commercial ownership, institutional penalties or tactical equipment use.

## Core boundaries

`RESOURCE_EXISTS != RESOURCE_RESERVED`

`RESOURCE_RESERVED != RESOURCE_HELD`

`RESOURCE_HELD != RESOURCE_USED`

`RESERVATION_ACTIVE != TASK_STARTED`

`RESERVATION_EXPIRED != RESOURCE_RETURNED`

`RESERVATION_RELEASED != RESOURCE_AT_HOME_LOCATION`

`PERMISSION_TO_USE != RESERVATION_CREATED`

`TEMPORARY_CONTROL != OWNERSHIP`

## Stable reservation identity

Every reservation requires:

- stable `reservation_id`;
- stable `resource_id`;
- reserving `actor_id`;
- semantic `start_tick` and exclusive `end_tick`;
- lifecycle state;
- optional purpose reference.

V1 treats one `WorldResource.resource_id` as one indivisible reservable unit. Quantity pools and partial allocation are deliberately deferred rather than inferred from `WorldResource.quantity`.

## Time-window semantics

An ACTIVE reservation has three effective temporal conditions without rewriting history:

- before `start_tick`: `SCHEDULED`;
- `start_tick <= now < end_tick`: `ACTIVE`;
- `now >= end_tick`: `EXPIRED`.

Expiry is derived from semantic time. Historical state can therefore remain queryable as the reservation that was originally created.

Overlapping ACTIVE reservations for the same resource ID are rejected. Adjacent windows are allowed because `end_tick` is exclusive.

## Explicit closure

A reserving actor may explicitly RELEASE or CANCEL an ACTIVE reservation. Both operations produce a new immutable ledger value and preserve the reservation identity.

V1 rejects closure attempts by another actor. Later institutional override/dispatcher authority requires an explicit permission contract and cannot be assumed from faction membership.

## Projection into Pass 338

`project_reservations_onto_resources(...)` derives the current reservation holder at a semantic tick and projects that claim into Pass 338's `WorldResource.reserved_for_actor_id` field.

The projection is read-only. It does not consume, transfer or check out the resource.

A depleted, retired or unavailable resource remains unusable even when a reservation exists.

## Checkout and return seam

Checkout requires one current ACTIVE reservation for the requesting actor and a serviceable resource not held by somebody else.

Checkout changes operational state to `IN_USE` and records `holder_actor_id`.

Return requires the current holder and an explicit destination. Return updates holder/location state. It does not delete the reservation ledger or prove that the resource is undamaged, calibrated, refilled or otherwise ready for every future task.

Future inspection/repair/serviceability events remain separate.

## Planner integration

The intended pipeline is:

world resources + reservation ledger + semantic time
→ reservation projection
→ Pass 338 resource requirement assessment
→ ordinary global NPC intent scorer
→ optional `REQUEST_AUTOPTU` handoff

This ordering means a high-priority task cannot consume an object another actor has legitimately reserved for the active window.

Planning remains non-mutating. Reservation creation/release/cancel, checkout and return are explicit world operations.

## Reduced implementation

The executable V1 supports:

- deterministic stable reservations;
- overlapping-window rejection;
- adjacent-window acceptance;
- explicit release;
- explicit cancellation;
- derived scheduled/active/expired status;
- read-only projection into Pass 338;
- reservation-gated checkout;
- explicit return to a location;
- deterministic ordering by stable IDs.

It does not require battle simulation.

## Deferred extensions

Later passes can add:

- quantity/capacity reservations;
- substitute resource grades;
- reservation requests and approval workflow;
- institutional pools;
- borrowing across organizations;
- delegated booking authority;
- no-show events and policy consequences;
- reservation priority and fairness;
- waitlists;
- checkout due dates;
- transfer/travel state;
- consumable decrement;
- inspection, repair and calibration;
- checkpoint persistence;
- player-facing inventory binding;
- production adapter acknowledgement.

## Combat capability dependencies

Reduced V1 has no battle-mechanics dependency.

A richer encounter involving a reserved or checked-out resource must expose exact dependencies:

- targeting / footprints / range / LoS: ordinary audited contracts are VERIFIED; any targeted device still requires its own verified behavior;
- base movement legality: VERIFIED for ordinary audited movement;
- complete movement: PARTIAL for carrying, dragging, interception, rescue or forced displacement;
- core calculations: VERIFIED for ordinary audited deterministic arithmetic;
- action economy / initiative: VERIFIED for ordinary audited primitives, but any new checkout/use/pass/equip action remains individually gated;
- full turn / round lifecycle: PARTIAL for timed activation, expiry or phase-sensitive equipment effects inside combat;
- full stateful damage pipeline: PARTIAL for equipment damage or effects that alter damage;
- status lifecycle: PARTIAL for resource-caused persistent conditions;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING when equipment changes those systems;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL and individually gated;
- Trainer Features / perks: PARTIAL and individually gated;
- AI legal-action infrastructure: VERIFIED for ordinary audited infrastructure, not for invented tactical resource actions;
- AI tactical policy: BLOCKING for protect/transfer/withdraw-with-resource/non-defeat objectives;
- Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

Minecraft inventory presence never authors reservation, ownership, institutional permission or PTU Item legality.
