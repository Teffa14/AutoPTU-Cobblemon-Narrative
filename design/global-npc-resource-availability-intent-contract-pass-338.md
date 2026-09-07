# Global NPC resource availability and intent gating contract — Pass 338

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-07

## Purpose

Add a region-neutral world-resource readiness layer to the existing global NPC agenda without moving PTU Item mechanics into the world planner.

The planner already checks knowledge, permissions, agent mode, scheduling and AutoPTU ownership. Pass 338 adds the missing question: does the actor currently have access to the ordinary world resource capability required by the selected work?

Target chain:

`goal / need / commitment / event -> base intent eligibility -> resource requirement assessment -> resource-ready candidate set -> existing deterministic intent scoring -> world action or AutoPTU handoff`

## Core invariants

`RESOURCE_EXISTS != RESOURCE_AVAILABLE`

`RESOURCE_KNOWN != RESOURCE_HELD`

`RESOURCE_HELD != RESOURCE_USABLE`

`RESOURCE_CAPABILITY != RESOURCE_IDENTITY`

`INSTITUTION_OWNS != NPC_CURRENTLY_CONTROLS`

`PERMISSION_TO_USE != PHYSICAL_AVAILABILITY`

`PHYSICAL_AVAILABILITY != PERMISSION_TO_USE`

`RESERVED_FOR_A != AVAILABLE_TO_B`

`RESOURCE_AT_LOCATION_X != RESOURCE_AT_ACTOR_LOCATION`

`MINECRAFT_ITEM_ENTITY != AUTHORITATIVE_RESOURCE_RECORD`

`WORLD_RESOURCE_READY != PTU_ITEM_EFFECT_LEGAL`

## Resource record

Proposed executable primitive:

```yaml
WorldResource:
  resource_id: resource:stable-id
  capability_refs: [FIELD_SAMPLE_KIT]
  quantity: 1
  state: AVAILABLE | RESERVED | IN_USE | UNAVAILABLE | DEPLETED | RETIRED
  location_ref: place:stable-id
  holder_actor_id: null
  reserved_for_actor_id: null
```

A durable resource may move between locations or holders while retaining identity. A consumable supply can instead be represented as a quantified resource lot. Domain-specific provenance or custody systems may attach richer lineage; this layer does not replace them.

## Intent requirement

```yaml
ResourceRequirement:
  capability_ref: FIELD_SAMPLE_KIT
  quantity: 1
  allow_held_by_actor: true
  allow_at_actor_location: true
```

The requirement names capability, not a preferred concrete resource ID. This allows the same task schema to operate across regions and institutions.

Exact named-object requirements remain possible through a higher-level domain contract when object identity matters.

## Availability decision

A requirement is satisfied only when one or more authoritative resource records provide enough matching capability and quantity under allowed access conditions.

For the first executable slice, a resource qualifies when:

- its state is `AVAILABLE`, or it is already `RESERVED` for the same actor;
- its capability set contains the required capability;
- it is held by the actor when held access is allowed, or it is at the actor's current world location when local access is allowed;
- its quantity contributes toward the requirement;
- a reservation for another actor excludes it.

Resource selection is deterministic: matching resource IDs sort lexicographically before allocation.

This is world-resource readiness only. It does not prove a Trainer can legally activate an Item in combat or use a PTU crafting Feature.

## Planner integration

Pass 338 deliberately keeps the base `NpcIntent` schema stable. A separate `ResourceAwareIntent` binds one existing world intent to zero or more resource requirements.

The gate filters candidates before invoking the existing `choose_intent` function. Therefore:

- existing knowledge and permission checks remain authoritative;
- existing scoring remains authoritative;
- an unavailable high-priority task does not suppress a lower-priority task that is actually ready;
- AutoPTU handoff occurs only after world prerequisites are satisfied;
- no resource state is consumed merely by choosing an intent.

Actual reservation, checkout, transfer, consumption, return and repair are separate state transitions and should be added through explicit events rather than hidden planner mutation.

## Reason codes

The executable layer should expose narrow reason codes:

- `RESOURCE_REQUIREMENT_SATISFIED`
- `MISSING_RESOURCE_CAPABILITY`
- `INSUFFICIENT_RESOURCE_QUANTITY`
- `RESOURCE_NOT_LOCALLY_AVAILABLE`
- `RESOURCE_RESERVED_FOR_OTHER_ACTOR`
- `NO_RESOURCE_READY_INTENT`

These describe planning state. They do not imply theft, negligence, equipment failure or PTU illegality.

## Reduced implementation

The reduced version treats resources as stable world records and requires exact same-location or held-by-actor availability. It does not perform route planning, institutional borrowing, capacity optimization or automatic checkout.

When work is blocked, the ordinary agenda can select another ready intent. A later slice may derive `ACQUIRE_RESOURCE`, `REQUEST_RESOURCE`, `WAIT_FOR_RESOURCE` or `RESCHEDULE_RESOURCE_DEPENDENT_WORK` intents using the existing travel, communication and relationship systems.

This is sufficient to prevent impossible actions now.

## Rich implementation

A richer version can add:

- temporal reservations and release windows;
- institutional pools and role-scoped borrowing permissions;
- transfer requests through the existing communication runtime;
- travel to a resource location through the existing world-route planner;
- consumable decrement and replenishment events;
- durable checkout/return/repair lifecycle;
- resource contention arbitration;
- substitutes with capability grades;
- joint tasks requiring resources and multiple actors;
- checkpoint persistence for reservations and resource movement.

None of these should be inferred from Minecraft chest contents or entity presence.

## Relationship to custody and inventory owners

Existing evidence custody, found-property, cold-chain and other domain systems retain authority over their richer state.

This contract only answers whether a resource capability is ready for an NPC world intent. It must not flatten evidence custody into generic inventory or allow generic availability to bypass legal, ethical or institutional restrictions.

## AutoPTU boundary

World resources can gate whether an NPC begins a task or reaches the point where structured mechanics are requested.

Once an action depends on tactical PTU resolution, AutoPTU owns it.

Examples:

A field kit may be required before an NPC travels to collect samples. The world planner can confirm the kit is present. If the later scene includes combat, the kit's presence does not create an attack, reaction, Item effect or Trainer Feature.

A recovery tool may be required before a rescue attempt begins. If the rescue uses forced movement, statuses or hazards during combat, those exact engine families remain independently gated.

## Mechanical dependency classification

The reduced resource gate itself requires no AutoPTU combat category.

A rich encounter using resource-dependent actions may additionally require:

- targeting / footprints / range / LoS when a device acts on a target or visibility matters;
- base movement legality to reach a resource or work point during structured play;
- complete movement for carrying, dragging, push/pull, rescue, interception or forced displacement;
- core calculations if the exact PTU action uses deterministic combat arithmetic;
- action economy / initiative if equipping, using, transferring or protecting a resource costs tactical actions;
- full turn / round lifecycle for timed equipment, delayed activation or phase-dependent work;
- full stateful damage pipeline when equipment interaction causes or prevents damage;
- status lifecycle when an exact resource applies/removes persistent tactical conditions;
- terrain / weather / hazards / zones / reactions when the equipment modifies or responds to those systems;
- move-specific behavior, abilities, items and Trainer Features/perks when exact PTU content is invoked;
- AI legal-action infrastructure for resource-related tactical action generation;
- AI tactical policy for deciding when to fetch, protect, share, abandon or use equipment;
- Minecraft/Cobblemon/Craftics adapter/playback for presentation, inventory UI and resource animation.

No category is promoted by this world-system contract.

## First executable acceptance cases

1. An NPC has permission and knowledge but the required kit is elsewhere: the work intent is blocked.
2. A kit at the same location satisfies the requirement.
3. A resource reserved for another actor is unavailable.
4. A resource already reserved for the same actor remains usable for planning.
5. Insufficient consumable quantity blocks the intent.
6. Two ready intents compete; the existing deterministic score chooses between them.
7. A higher-scoring blocked intent does not suppress a lower-scoring ready intent.
8. A structured-mechanics intent requests AutoPTU only after its world-resource requirement is met.
9. No local authored place name appears in the global executable module.

## Unresolved next slices

- reservation mutation and expiry;
- resource acquisition intents;
- institutional pool permissions;
- resource travel/transfer integration;
- checkpoint persistence;
- consumable use and durable return events;
- substitution/capability grades;
- player inventory bindings;
- Minecraft acknowledgement without inventory authority;
- reconciliation with exact PTU/Caelo Item and crafting rules when mechanical effects are needed.
