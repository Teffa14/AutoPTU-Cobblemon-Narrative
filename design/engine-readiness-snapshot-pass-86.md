# Engine Readiness Snapshot — Pass 86

Status: implementation-evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`f4a5232b406fe0c80137e4d1d2f8408771ab4ba0`

Latest visible commit:

`Run canonical field progression during ROUND_START`

Previous Pass 85 head:

`c78ebef5203b2ab67b59ae58b3729fb2ab282cef`

AutoPTU Python `main` inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest visible Python changes remain Career-oriented and do not justify changing the tactical capability map.

## New Java evidence since Pass 85

The current Java head moves the field-state lifecycle slice one step closer to the live battle runtime:

- canonical terrain/zone/room entries remain owned by `BattleEnvironmentState`;
- ROUND_START field progression is registered in the default lifecycle hook registry;
- field progression now executes through the authoritative ROUND_START lifecycle;
- parity coverage includes lifecycle-level field progression against Python-oracle fixtures;
- Minecraft/controller code still does not own field expiry.

This is stronger evidence than a standalone field-state utility.

It still does not demonstrate the full permanent category `terrain/weather/hazards/zones/reactions`.

## Why the environment family remains BLOCKING

Current evidence still does not prove:

- application/creation of the full library of terrain/weather/hazard/zone effects;
- semantic behavior of all named PTU field states;
- hazard damage/status application;
- zone entry/exit effects;
- reactions triggered by movement through zones;
- terrain movement-cost changes across the full ruleset;
- weather lifecycle and interactions across the full library;
- field-effect stacking/conflict rules;
- dynamic geometry or interactables;
- forced movement produced by field effects;
- initialization from Minecraft world state;
- complete semantic playback into Minecraft/Cobblemon/Craftics.

Pass 86 therefore treats the new Java work as real lifecycle/state infrastructure inside a still-blocking environment family.

## AutoPTU-Java README boundary

The current README continues to list unfinished work for:

- core combatant/grid battle state expansion;
- full damage resolution pipeline;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic battle-event emission and full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the anti-overclaim boundary.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

VERIFIED for implemented static geometric targeting.

Pass 86 guardrail:

Geometric LoS does not prove visibility through traffic, fencing, culverts, vegetation screens, underpasses, tunnels or atmospheric conditions beyond implemented blockers.

### base movement legality

VERIFIED for the implemented Shift/Jump and Overland/Swim/Sky surface.

Pass 86 guardrail:

A road, ditch, culvert, fence, bridge shoulder or wildlife crossing does not receive a movement cost or traversal rule merely from its world label.

### core calculations

VERIFIED for ported calculation primitives.

Pass 86 guardrail:

There is no generic road-collision, vehicle-impact, fence, culvert, traffic, crossing or fragmentation modifier.

### action economy/initiative

VERIFIED for the implemented initiative/action surface.

Pass 86 guardrail:

Traffic windows, road closures, migrations and route schedules are overworld clocks unless an exact battle mechanic is authored and implemented.

### AI legal-action infrastructure

VERIFIED for supported legal choices.

It does not provide tactical policy goals such as:

- CROSS_ROAD;
- REACH_UNDERPASS;
- WITHDRAW_FROM_TRAFFIC;
- PROTECT_SURVEYOR;
- GUIDE_TO_CROSSING;
- CLEAR_CULVERT;
- HOLD_SAFE_SIDE;
- ESCORT_NONCOMBATANT.

## PARTIAL

### full turn/round lifecycle

PARTIAL.

Java now executes canonical field progression through the default ROUND_START lifecycle, in addition to its existing turn/round, RNG, delayed-hit, phase and cleanup infrastructure.

It still does not prove every phase effect, switch/send-out path, duration, cleanup, delayed form, reaction, field interaction or transcript event.

### full stateful damage pipeline

PARTIAL.

Normal and delayed-hit paths increasingly derive and mutate authoritative state.

Pass 86 guardrail:

Road collisions, moving vehicles, debris, falling from bridges or being trapped against a fence cannot deal HP damage unless a verified rule path produces it.

### status lifecycle

PARTIAL.

Selected status application/phase/expiry slices exist.

Pass 86 guardrail:

A traffic incident or road surface cannot create Tripped, Slowed, Stuck, Injured, Confused or any other Status by narrative description.

### move-specific behavior

PARTIAL.

Representative Move contracts and delayed-hit execution exist.

Pass 86 guardrail:

A Move that pushes, blocks, creates terrain or interacts with structures must be individually verified before a road-crossing encounter depends on it.

### abilities

PARTIAL.

Representative Ability hooks have parity evidence.

Pass 86 guardrail:

Run Away, Pack Mon, Arena Trap, Magnet Pull, species flavor or migration lore cannot be converted into generic road-crossing AI.

### items

PARTIAL.

Representative held-item behavior exists.

Pass 86 guardrail:

Reflective signs, fencing, survey cameras, barriers, cones, road tools and monitoring equipment remain world-state assets unless they correspond to verified PTU Items.

### Trainer Features/perks

PARTIAL.

Representative Features and hook infrastructure exist.

Pass 86 guardrail:

Survival, Ranger-like work, engineering, transportation, ecology or civic roles do not grant road-control or crossing bonuses without exact validated rules.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

BLOCKING as a family.

Pass 86 FULL encounters may need:

- interception before a Pokémon reaches a dangerous lane;
- displacement around fencing or bridge edges;
- pushing/pulling actors from hazardous positions;
- moving objectives through chokepoints;
- reactions to attempted crossings;
- routing around dynamic obstacles.

### terrain/weather/hazards/zones/reactions

BLOCKING as a family despite the stronger canonical ROUND_START field progression.

Pass 86 FULL concepts may eventually need:

- hazardous traffic lanes;
- road/rail boundary zones;
- culvert water/debris state;
- temporary barriers;
- zone entry/exit effects;
- reactions around protected crossing lanes;
- environmental field duration.

The current Java head proves canonical storage/progression/expiry wiring for field entries. It does not authorize those behaviors.

### AI tactical policy

BLOCKING.

Legal actions exist, but there is no verified scoring/policy for migration, escape, crossing, withdrawal, escort, survey protection or infrastructure interaction.

### Minecraft/Cobblemon/Craftics adapter/playback

BLOCKING.

There is no verified end-to-end contract that converts persistent route/crossing state into AutoPTU battlefield state and then replays movement, traffic, barriers or ecological consequences in Minecraft without duplicating PTU rules.

# Pass 86 encounter dependency summary

## Crossing Retrofit Survey

REDUCED version can rely on:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL when a normal battle uses them:
- full lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING for the FULL version:
- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions if the road/crossing becomes mechanically active;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## Culvert After the Storm

REDUCED version resolves hydraulic state, debris and passage in Freshwater/world state before battle.

FULL version additionally depends on:
- complete movement if actors can be displaced or must reach specific exits;
- terrain/weather/hazards/zones/reactions for active current/debris;
- full lifecycle for changing field state;
- AI tactical policy for reach-exit/withdraw/protect goals;
- adapter/playback.

## Fence-End Bottleneck

REDUCED version halts/reroutes service and keeps moving non-hostile groups out of the battle grid.

FULL version additionally depends on:
- complete movement/interception;
- terrain/zones/reactions if fence lanes are mechanically meaningful;
- AI tactical policy;
- adapter/playback.

# Pass 86 overworld blockers

These are outside the battle-core permanent categories but are required for the intended world system:

- `LINEAR_INFRASTRUCTURE_SEGMENT_STATE` — authoritative segment identity/condition/use band;
- `ECOLOGICAL_CONNECTIVITY_ASSESSMENT` — target-population-specific connectivity evidence;
- `WILDLIFE_CROSSING_ASSET_STATE` — overpass/underpass/culvert/bridge passage history;
- `CROSSING_ADOPTION_HISTORY` — longitudinal observed use without collapsing observation into success;
- `FENCE_GUIDANCE_STATE` — condition, gaps, endpoints and linked crossings;
- `LINEAR_CONFLICT_INCIDENT_GRAPH` — near-miss/obstruction/collision evidence without inventing mechanical outcomes;
- `ROAD_STREAM_CROSSING_LINK` — separate hydraulic and biological-passage state;
- `LINEAR_MITIGATION_PROJECT_STATE` — proposal -> implementation -> monitoring -> review;
- `ROAD_ECOLOGY_TO_COBBLEMON_PROJECTION` — coarse, anti-exploit population/corridor projection;
- `ROAD_ECOLOGY_TO_BATTLE_SNAPSHOT` — validated frozen tactical state where needed;
- `ROAD_ECOLOGY_TO_MINECRAFT_PROJECTION` — physical rendering without making loaded blocks/entities authoritative.

# No-inference rules for Pass 86

The following statements remain invalid unless later evidence explicitly proves them:

- `road = Rough Terrain`;
- `road = vehicle hazard`;
- `fence = forced movement`;
- `culvert = current hazard`;
- `bridge = falling risk`;
- `crossing structure used once = connectivity restored`;
- `no collisions = healthy corridor`;
- `many collisions = population decline`;
- `Run Away = wildlife-crossing AI`;
- `Pack Mon = herd road behavior`;
- `Ground type = can tunnel under road`;
- `Flying type = unaffected by linear infrastructure`;
- `road closure = ecological recovery`;
- `loaded Cobblemon count = crossing success`.

# Capability conclusion

The new Java commit is meaningful evidence that field entries are increasingly owned and progressed by the authoritative battle core. It does not change the permanent capability classifications used by narrative planning.

Pass 86 should therefore ship Road Ecology as world-state architecture now and keep mechanically rich road-crossing encounters behind FULL/REDUCED implementation contracts.