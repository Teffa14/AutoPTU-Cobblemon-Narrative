# Global NPC world travel contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: all persistent/recurring Ouros NPC world agents
Parent: `design/global-npc-world-agent-ai-contract.md`
Consumes: `design/global-npc-goal-need-schedule-contract.md`, `design/global-npc-social-relationship-faction-contract.md`

## Purpose

Give every persistent NPC one region-neutral travel model so goals, work, faction duties, social meetings and scheduled commitments respect distance and travel time.

The world-travel layer works on a semantic route graph. It does not replace Minecraft pathfinding and does not implement PTU tactical movement.

`WORLD_ROUTE != MINECRAFT_PATH != PTU_MOVEMENT`

## Route graph

A world route edge minimally records:

- stable edge ID;
- origin and destination semantic nodes;
- expected semantic duration;
- enabled/disabled state;
- required knowledge where a route is not known to everyone;
- required permission where access is restricted;
- whether local projection is required;
- whether structured resolution is required.

Content owns graph geography. The planner owns generic route semantics. No region may fork travel rules.

Route duration is an Ouros world-simulation estimate. It is not an Overland capability value unless a later adopted PTU integration explicitly derives the duration from verified mechanics.

## Planning around commitments

For a commitment with a known start time:

```text
latest_departure = commitment_start - arrival_buffer - estimated_route_duration
```

When planning before that point, the NPC may reserve travel time and wait until departure.

When planning after that point, the planner starts from current semantic time and exposes a late ETA. It must never relocate the NPC to preserve the schedule.

`LATE_PLAN != TELEPORT`

A missed or endangered commitment is handled by the agenda/social consequence layers. Travel truth is not rewritten to make the appointment succeed.

## Knowledge and permission

An NPC can use only route edges available under its own state.

A hidden shortcut does not enter path search until the agent knows it through an allowed knowledge channel. A restricted corridor remains unavailable without the required permission.

Global map truth does not automatically become NPC route knowledge.

## Off-screen travel

Named NPCs may progress through semantic route edges while off-screen when the edge outcome is fully represented by deterministic world state and does not require unresolved local geometry or structured mechanics.

Progress advances only from Ouros semantic time. Wall clock, Minecraft ticks, chunk load and player proximity do not complete travel.

A route edge completes only after its semantic duration has elapsed.

`CHUNK_UNLOAD != ARRIVAL`

## Dynamic route availability and replanning

If the next planned edge becomes unavailable, travel produces `REPLAN_REQUIRED`.

The planner searches again from the NPC's current semantic node. If an alternate route exists, a new ETA is calculated. If none exists, travel remains blocked. The NPC does not cross the unavailable edge and does not jump to the destination.

World events may disable edges only through explicit state owned by the relevant subsystem. A Minecraft block change is not automatically a world-route closure.

## Local projection boundary

Some edges require local geometry/presentation. Examples can include a short visible walk through a loaded settlement, boarding interaction, door/gate presentation or another adapter-owned sequence.

The world layer emits `PROJECT_LOCAL_TRAVEL` and keeps semantic location unchanged until the adapter returns an accepted semantic result.

Minecraft may choose a path for presentation. It may not silently decide world arrival, permissions or tactical legality.

## AutoPTU boundary

A route edge can lead to a structured encounter or require governed mechanics. In that case the world layer emits `REQUEST_AUTOPTU` and pauses travel.

While the NPC is `AUTOPTU_BOUND`, world travel returns `HOLD_AUTOPTU` and does not progress the edge.

Travel planning does not select battle squares, resolve Overland/Swim/Sky, push/pull/knockback, interception, damage, statuses, reactions, Moves, Abilities, Items, Trainer Features or tactical targets.

## Capability dependency map

Reduced world-only travel requires no AutoPTU tactical capability. It needs only Ouros semantic time, route graph state, NPC knowledge/permissions and persistent agent state.

A full locally projected or mechanically interrupted journey can depend on these permanent capability families:

- targeting/footprints/range/LoS: only if the resulting structured encounter targets entities;
- base movement legality: when AutoPTU must adjudicate ordinary structured movement;
- complete movement: for interception, push/pull, knockback or forced movement;
- core calculations: for adopted deterministic PTU arithmetic;
- action economy/initiative: for structured actions;
- full turn/round lifecycle: for multi-turn resolution;
- full stateful damage pipeline: when damage occurs;
- status lifecycle: when afflictions persist or expire;
- terrain/weather/hazards/zones/reactions: when the route encounter uses them as mechanics;
- move-specific behavior, Abilities, Items and Trainer Features/perks: only where explicitly used;
- AI legal-action infrastructure: for legal structured option generation;
- AI tactical policy: for autonomous tactical choice after handoff;
- Minecraft/Cobblemon/Craftics adapter/playback: for local presentation, adapter acknowledgement and semantic result playback.

A world route never promotes any of these families by existing.

## Determinism and persistence

Identical agent state, graph state and semantic time must yield the same route and ETA. Equal-cost paths use stable edge-ID ordering.

A persisted travel state keeps current semantic node, selected plan, next edge, edge start time and relevant blockage state. Restart must not restart the journey from origin or advance it for free.

## Current executable seam

Pass 281:

- `tools/global_npc_travel.py`;
- `implementation/global-npc-travel-fixture-v1.json`;
- `tests/test_global_npc_travel.py`.

## Canon boundary

This is proposed global implementation architecture. Synthetic route nodes, travel durations, actors and regions in fixtures do not establish Ouros geography, transport networks, travel speeds or NPC canon.
