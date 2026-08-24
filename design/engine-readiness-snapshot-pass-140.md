# Engine Readiness Snapshot — Pass 140

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records live AutoPTU-Java and AutoPTU evidence relevant to the road passenger transit concepts added in Pass 140. Both engine repositories remain read-only for this task.

One representative mechanic never promotes an entire permanent capability family.

## Inspected heads

AutoPTU-Java:

`14662fb67778e71f2d55fc7a74c43dd9a8b06fa1`

Latest inspected commit:

`Freeze multi-target move execution contract (#169)`

The new parity-backed contract freezes how ordinary multi-target Moves spend action/frequency resources once while affected combatants resolve individually through the target loop. This follows Pass 139's authoritative TILE-target expansion work.

This strengthens action economy and move-specific execution boundaries for area attacks. It does not add passenger flow, vehicles, road collision, escort objectives, buses, taxis, route logic or service simulation.

AutoPTU Python:

`cd4668a1b0e7c995bc12f3768f7b04cfa0f1c896`

Latest inspected Python commit:

`Career: keep slim Vercel artifact on thin entrypoint (#78)`

This is deployment/Career packaging work and does not change the tactical capability classification below.

## Java repository boundary

The live AutoPTU-Java README still explicitly leaves unfinished:

- complete combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- complete status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Recent reaction, target-expansion and multi-target execution slices are real progress. They do not override these repository-level blockers.

## Road-transit mechanics boundary

Pass 140 introduces no new PTU mechanic.

The following belong to overworld/service state outside AutoPTU:

- road transit services;
- routes and route revisions;
- stops and temporary stop relocation;
- timetables and headway bands;
- individual trip instances;
- observed arrivals/departures;
- reliability/bunching/crowding state;
- taxis and demand-responsive trip requests;
- transfers and missed connections;
- vehicle assignment/maintenance state;
- working-Pokémon assignments;
- fares/payment handoffs;
- passenger information;
- accessibility references;
- detours and service recovery.

AutoPTU becomes authoritative only if an actual battle opens and combatants need legal actions or mechanical consequences.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

Java has parity-backed range, area, footprint and LoS support, including authoritative TILE-target expansion.

This can support a static battle at a stop, depot or transit hub.

It does not model sightlines for drivers, road traffic, vehicle sensors or passenger service coverage.

### base movement legality — VERIFIED

Ordinary Shift/Jump legality remains verified for the ported scope.

This can move actual combatants inside a frozen arena.

It does not move buses, taxis, passenger queues, escort targets or noncombat vehicles.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

Java has narrow reaction-movement support and Push/Pull instruction contracts, but repository status still leaves forced movement incomplete.

Transit FULL encounters need this family when passengers, technicians, wildlife or service assets must cross threatened space, withdraw or be intercepted.

### core calculations — VERIFIED

Core stat/type/damage-table primitives remain verified for the ported scope.

A driver's experience, a crowded route, a delayed bus or a vehicle model cannot modify combat stats without exact PTU mechanics.

### action economy/initiative — VERIFIED

Action-budget and initiative infrastructure remain verified.

The new multi-target execution contract further protects action/frequency bookkeeping for ordinary area Moves.

Boarding, dispatching, opening a bus door or driving are not combat actions unless an authoritative rule maps them into battle.

### full turn/round lifecycle — PARTIAL

Round flow, delayed effects, selected temporary effects and selected reaction paths have parity-backed slices.

The complete lifecycle remains unfinished.

### full stateful damage pipeline — PARTIAL

Recent pre-damage reaction ordering and target execution slices strengthen the pipeline, but full damage remains listed as incomplete.

Vehicle collision, road debris, a moving shuttle or machinery cannot create custom damage from narrative description.

### status lifecycle — PARTIAL

Selected application, prevention, suppression, stacking and timing behavior exists.

Crowding, missed connections, long waits, motion sickness, panic or road delay do not create Status conditions by narrative declaration.

### terrain/weather/hazards/zones/reactions — BLOCKING

Reaction coverage has concrete slices, but the combined permanent family remains incomplete.

A road, curb, bus lane, wet pavement, stop platform, vehicle or traffic stream does not become tactical Terrain/Hazard/Zone automatically.

### move-specific behavior — PARTIAL

Target resolution and execution coverage continues to grow. The latest Java contract covers ordinary multi-target execution ownership.

Any specific Move used in a transit encounter still depends on parity for that Move and its side effects.

### abilities — PARTIAL

Selected Ability families have parity-backed behavior.

Pokémon taxi/shuttle lore does not create a carrying Ability, traffic immunity or work bonus.

### items — PARTIAL

Item coverage remains incomplete.

Tickets, fare cards, radios, vehicle keys, uniforms, stop signs and ordinary tools remain narrative objects unless mapped to validated PTU Items.

### Trainer Features/perks — PARTIAL

Generic Trainer Feature infrastructure and selected effects exist, but catalog coverage remains incomplete.

Driver, dispatcher, conductor, mechanic or route supervisor are occupational roles and grant no Feature by title alone.

### AI legal-action infrastructure — VERIFIED

Battle-choice legality remains verified. Authoritative TILE expansion and multi-target execution ownership strengthen this boundary.

This does not provide objective-aware passenger or transport AI.

### AI tactical policy — BLOCKING

No complete policy exists for transit objectives such as:

- `EVACUATE`;
- `CLEAR_ROUTE`;
- `PROTECT_PASSENGER`;
- `REACH_EXIT`;
- `REACH_DESTINATION`;
- `PROTECT_ROUTE`;
- `WITHDRAW`;
- `PROTECT_WILDLIFE`.

A legal-action list is not route, escort or service-objective reasoning.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

No parity-safe adapter exists.

Minecraft must not infer authoritative transit state from:

- a vehicle model or minecart;
- a Gogoat or other Pokémon standing near a stop;
- a route sign;
- a named NPC labelled driver;
- passenger entities gathered near a curb;
- a redstone timetable;
- road blocks or lane markings;
- visible vehicle movement.

The adapter must not invent passenger capacity, fare settlement, collision rules, vehicle movement mechanics, Mountable legality or service availability.

## Pass 140 encounter dependencies

### Transit Hub Evacuation — FULL

Requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL if exact supported effects are invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING if the disruption itself creates a tactical hazard;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED:

Stop boarding and evacuate every passenger/noncombat worker in world state. Freeze vehicles outside the arena. Open a static AutoPTU encounter with actual combatants only. Transit service recovery happens afterward.

### Last Shuttle Through the Detour — FULL

Primary blockers:

- complete movement for a moving service asset and interception;
- AI tactical policy for `REACH_DESTINATION`, `PROTECT_ROUTE`, `WITHDRAW`;
- adapter/playback;
- terrain/weather/hazards/zones/reactions only if a validated environmental effect becomes tactical.

REDUCED:

Stop the shuttle at a safe location, disembark passengers through world state and resolve alternate travel separately. Any battle occurs in a static arena. Victory does not move the vehicle or reopen the road.

### Taxi Rank Wildlife Spillover — FULL

Primary blockers:

- complete movement for live wildlife withdrawal and passenger flow;
- AI tactical policy for `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_WILDLIFE`;
- adapter/playback;
- environmental family only when a validated road/weather mechanic is required.

REDUCED:

Urban Wildlife resolves population movement first. Transit relocates pickups. A static battle opens only for remaining combatants. Service resumption does not prove the ecological issue is solved.

## Explicit non-inferences

Pass 140 does not authorize:

- vehicle collision damage;
- vehicle initiative;
- driving Skill checks;
- traffic hazards;
- road Terrain effects;
- passenger HP;
- crowd panic mechanics;
- Mountable/carrying rules;
- bus/taxi speed values;
- boarding action costs;
- pursuit bonuses;
- service-worker Features;
- automatic battle encounters for unpaid fares;
- road-service bonuses from species lore.

## Open engine/rules questions

- Does the final PTU/Caelo source set contain vehicle or passenger-carrying rules relevant to road transit?
- Which exact Mountable/carrying rules govern Pokémon-assisted passenger services?
- Can any future vehicle exist as an interactable tactical object without duplicating PTU rules in Minecraft?
- Will complete movement support moving protected actors/objects or only combatants?
- What objective vocabulary will tactical AI eventually support for evacuation/escort/route-clearing encounters?
- Should road-transit incidents always freeze vehicles before battle until those contracts exist?

The full Caelo corpus and Super PTU Online Helper were not available as reliable invocable sources during this run. No missing mechanics were invented.