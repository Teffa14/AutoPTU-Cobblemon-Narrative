# Global NPC resource recovery intent contract — Pass 341

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-07

## Purpose

Bridge a resource-blocked world task into safe follow-up intents without inventing possession, permission, delivery or tactical effects.

Pass 338 answers whether a task has the required resource capability. Pass 339 projects temporal reservations. Pass 340 projects technical readiness. Pass 341 answers the next world-planning question: when the task is blocked, what action is currently justified by the known resource state?

Target chain:

`agenda work intent -> Pass 339 reservation projection -> Pass 340 readiness projection -> Pass 338 resource assessment -> Pass 341 recovery options -> existing planner / travel / communication owners`

## Core invariants

`RESOURCE_BLOCKED != NPC_PARALYZED`

`RESOURCE_NEEDED != RESOURCE_REQUESTED`

`REQUEST_RESOURCE != TRANSFER_RESOURCE`

`REQUEST_SENT != REQUEST_RECEIVED`

`REQUEST_RECEIVED != REQUEST_ACCEPTED`

`REQUEST_ACCEPTED != CHECKOUT`

`RESOURCE_REMOTE != ACCESS_AUTHORIZED`

`RESOURCE_RESERVED_FOR_ACTOR != RESOURCE_HELD_BY_ACTOR`

`TRAVEL_INTENT != TRAVEL_COMPLETE`

`WAIT_FOR_RESOURCE != RESERVATION_RELEASED`

`RECOVERY_OPTION != EXECUTED_WORLD_EVENT`

`WORLD_RESOURCE_ACQUIRED != PTU_ITEM_EFFECT_LEGAL`

## Executable primitive

`tools/global_npc_resource_recovery.py` introduces:

```yaml
ResourceRecoveryOption:
  intent: NpcIntent
  requirement: ResourceRequirement
  resource_id: resource:stable-id
  reason_code: RESOURCE_HELD_BY_OTHER_ACTOR | RESOURCE_RESERVED_FOR_OTHER_ACTOR | RESERVED_RESOURCE_AT_REMOTE_LOCATION
  destination_location_ref: place:stable-id | null
  request_target_actor_id: npc:stable-id | null
```

and:

```yaml
ResourceRecoveryResult:
  blocked_intent_id: intent:stable-id
  blocked: true | false
  options: [...]
  reason_codes: [...]
```

The result is advisory world-agent state. It does not mutate any authoritative resource record.

## Safe derivation rules

### Known holder

When a viable matching resource is currently held by another known actor, Pass 341 may derive:

`REQUEST_RESOURCE`

The request target is the holder actor.

This does not mean the holder agrees, the communication is delivered, the resource is transferable, institutional policy permits the transfer or the item later becomes available.

The existing audience/communication systems remain responsible for message delivery. A later authority layer remains responsible for consent and transfer.

### Reservation already belonging to the blocked actor

When a matching resource is reserved for the blocked actor but located elsewhere and not held by another actor, Pass 341 may derive:

`TRAVEL_TO_RESERVED_RESOURCE`

Only the existing world travel graph may establish whether a route exists. The recovery layer does not teleport the actor or calculate Minecraft paths.

The generated intent carries the semantic travel cost returned by the existing route planner.

### Another actor owns the reservation claim

When another actor currently holds the reservation claim, Pass 341 may derive:

`WAIT_FOR_RESOURCE`

This is deliberately narrow. V1 does not cancel the other reservation, force a release, create a waitlist or assume urgency overrides fairness.

### Unreserved remote resource

A known matching resource at another location is not enough to derive travel-to-acquire.

`REMOTE_RESOURCE_EXISTS != ACCESS_AUTHORIZED`

Until institutional ownership/borrowing authority is represented explicitly, Pass 341 fails closed with:

`REMOTE_RESOURCE_ACCESS_NOT_ESTABLISHED`

### No viable candidate

If no known candidate has the capability and required quantity while remaining outside unavailable/depleted/retired states, the layer reports:

`NO_KNOWN_RESOURCE_CANDIDATE`

It does not synthesize a substitute.

## Determinism

Candidate resources sort by stable `resource_id`.

Generated recovery options sort by stable `intent_id`.

The same world snapshot therefore yields the same option set and order.

## Planner boundary

Pass 341 does not replace `choose_intent` or `choose_agenda_intent`.

Its output consists of ordinary `NpcIntent` values that can be passed into the existing global planning path. Their scores remain governed by the base planner.

A resource request is a world communication intent. A travel recovery is a world travel intent. A wait intent is a world scheduling state. None are tactical battle actions.

## Communication boundary

`REQUEST_RESOURCE` only identifies the intended actor and requested resource context.

Actual delivery must use the existing communication stack:

`audience/recipient selection -> channel scheduling -> delivery -> receiver knowledge -> selective replanning`

A failed, deferred or unheard request cannot transfer anything.

## Travel boundary

`TRAVEL_TO_RESERVED_RESOURCE` uses `build_travel_plan` only to verify that an eligible semantic route exists and to derive world travel cost.

Actual departure, progress, interruption, arrival and any AutoPTU route interruption remain in `tools/global_npc_travel.py`.

## Reservation/readiness boundary

Pass 341 consumes already projected resource state. It cannot:

- create or close Pass 339 reservations;
- overrule another actor's reservation;
- create Pass 340 readiness records;
- convert `LIMITED` or `MAINTENANCE` into ready state;
- repair, calibrate or inspect equipment.

## Reduced narrative version

A blocked NPC can now respond to a missing tool by asking the known holder, traveling to a tool already reserved for them, or waiting behind another valid reservation.

All transitions can occur through semantic world events without local projection.

This is enough to create ordinary logistics consequences in schedules, obligations and relationships.

## Rich narrative version

A later layer can add:

- explicit provider acceptance/rejection;
- institutional resource pools;
- delegated borrowing authority;
- transfer events and courier travel;
- alternate capable resources;
- waitlists and fairness;
- capacity/quantity reservation;
- consumable replenishment;
- emergency prioritization;
- player-mediated pickup/delivery;
- persistent request state across checkpoints.

These must remain explicit systems rather than hidden consequences of `REQUEST_RESOURCE`.

## AutoPTU capability classification

The reduced Pass 341 layer requires no AutoPTU combat capability.

When a resource-recovery story enters structured play, the exact dependency families must be recorded:

- targeting / footprints / range / LoS: if a tool or tactical objective requires exact targets or visibility;
- base movement legality: ordinary tactical movement to a pickup, delivery or work point;
- complete movement: carrying, dragging, interception, rescue, push/pull, knockback or forced movement involving the resource;
- core calculations: any exact PTU arithmetic invoked by the structured action;
- action economy / initiative: handoff, equip, activate, guard or abandon actions during structured play;
- full turn / round lifecycle: timed delivery windows, delayed activation or phase-bound effects;
- full stateful damage pipeline: damage to actors or equipment when mechanically represented;
- status lifecycle: persistent tactical conditions caused or removed by the exact content;
- terrain / weather / hazards / zones / reactions: routes or work areas whose tactical state changes during the encounter;
- move-specific behavior: every exact Move individually;
- abilities: every exact Ability individually;
- items: every exact PTU Item effect individually;
- Trainer Features/perks: every exact Feature individually;
- AI legal-action infrastructure: generation of legal tactical pickup/use/transfer actions when implemented;
- AI tactical policy: decisions to protect, deliver, abandon, share or retreat with resources;
- Minecraft/Cobblemon/Craftics adapter/playback: presentation and acknowledgement only.

A world resource passing Pass 341 never proves its PTU Item implementation.

## Acceptance cases

1. Resource-ready work generates no recovery options.
2. A matching resource held by another actor generates `REQUEST_RESOURCE` without mutation.
3. A matching resource reserved for another actor generates `WAIT_FOR_RESOURCE`.
4. A remote resource reserved for this actor generates travel only when the existing travel graph has an eligible route.
5. No route fails closed.
6. An unreserved remote resource does not grant access or travel-to-acquire authority.
7. Depleted/unavailable/retired candidates do not generate false recovery.
8. Recovery option ordering is deterministic.
9. Recovery options never request AutoPTU by themselves.
10. No local region or place appears in the global executable module.

## Deferred work

- provider consent and request-state lifecycle;
- institutional pools and delegated borrowing authority;
- explicit resource-transfer world events;
- travel/communication coordinator for accepted transfers;
- quantity/capacity reservations;
- waitlists and fairness;
- consumable use/replenishment;
- checkpoint persistence;
- player inventory binding;
- Minecraft acknowledgement;
- exact PTU/Caelo Item/crafting validation when mechanics are invoked.
