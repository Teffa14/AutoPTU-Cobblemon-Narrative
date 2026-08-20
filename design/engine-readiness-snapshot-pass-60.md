# Engine Readiness Snapshot — Pass 60

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.

Date: 2026-08-20

## Repositories inspected

Read-only:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`6678d4563116a4ec8c70d9daafc00d28bb9ab25b`

Latest inspected commit:

`Roll initiative into the next authoritative round (#91)`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/6678d4563116a4ec8c70d9daafc00d28bb9ab25b

The commit adds an initiative-round rebuild contract, preserves lifecycle events when initiative is exhausted, advances the runtime into the next authoritative round and tests round rollover.

This materially strengthens evidence for:

- action economy / initiative;
- full turn / round lifecycle infrastructure;
- authoritative round state;
- integration between exhausted initiative and lifecycle progression.

It does not prove:

- complete lifecycle coverage;
- all end-of-round/start-of-round effects;
- all status timing rules;
- all Ability/Feature phase hooks;
- broad reactions or interrupts;
- full damage sequencing;
- terrain/hazard runtime;
- forced movement;
- tactical AI;
- Minecraft playback.

The Java README continues to state that Python AutoPTU remains authoritative while the port is incomplete and lists broad unfinished work including:

- core battle state expansion;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/Ability/item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

README:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

## Python AutoPTU live evidence

Current inspected Python head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest inspected Python work remains Career-focused (`Career: make roster recovery deterministic`). No new Python tactical commit changes the permanent classification below.

Python remains the behavioral oracle only for slices explicitly frozen and compared by the Java migration process.

## Permanent capability map

One representative mechanic never promotes an entire family.

| Permanent capability family | Pass 60 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Dedicated targeting, areas, footprints, anchors and LoS coverage exist. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers, Wallrunner and fit predicates exist. This is not complete movement. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement and interception/broad movement reactions remain unfinished. |
| core calculations | VERIFIED | Damage Base/type tables, stages, accuracy primitives, crit probability and multiple calculation modifiers exist. |
| action economy / initiative | VERIFIED | Typed turn flow, action budget, deterministic ordering, authoritative initiative progress, combatant-turn advancement and round rollover are directly evidenced. |
| full turn / round lifecycle | PARTIAL | Round rollover is now materially stronger, but complete phase/status/Ability/Feature/reaction/delayed-effect coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Several damage and post-damage slices exist while the README still lists full damage as unfinished. |
| status lifecycle | PARTIAL | Multiple status contracts and lifecycle timing slices exist; full controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Calculation primitives and terrain movement costs do not prove runtime terrain, hazards, zones or broad reactions. |
| move-specific behavior | PARTIAL | Selected contracts exist; complete PTU Move behavior does not. |
| abilities | PARTIAL | Multiple Ability hooks exist; full registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; full catalog behavior remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered/lifecycle infrastructure and selected Features exist; full catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal action generation/filtering is implemented. |
| AI tactical policy | BLOCKING | Scoring/policy remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core, not the Minecraft adapter. |

## Why the newest round-rollover slice does not promote lifecycle to VERIFIED

The latest Java commit closes a real boundary: exhausted initiative can rebuild and enter the next authoritative round while preserving lifecycle events.

The remaining lifecycle surface still includes:

- every START/END round effect;
- every status duration/expiration rule;
- every Ability and Trainer Feature phase trigger;
- reaction and interrupt windows;
- all delayed/queued effect semantics;
- full transcript parity;
- interaction with complete damage, movement, terrain and hazards.

`full turn / round lifecycle` remains PARTIAL.

## Pass 60-specific overworld boundary

Demography and migration belong mainly outside AutoPTU-Java.

Suggested non-battle blockers:

`OVERWORLD_POPULATION_PROFILE = BLOCKING`

The server needs persistent aggregate population profiles by settlement/zone and time.

`OVERWORLD_POPULATION_COHORTS = BLOCKING`

The server needs coarse cohorts for residents, commuters, students, seasonal workers, visitors, evacuees and other authored categories without simulating every person.

`OVERWORLD_MIGRATION_EVENT_GRAPH = BLOCKING`

The server needs causal relocation/temporary-movement events linked to housing, transport, workplaces, crisis and institutions.

`OVERWORLD_PRESENCE_PROJECTION = BLOCKING`

Minecraft needs a projection strategy that converts population context into representative NPCs, crowd density, occupied buildings, queues and event presence without making loaded entity count the source of truth.

`OVERWORLD_DEMOGRAPHIC_PRIVACY = BLOCKING`

The server needs access control separating public aggregates from private residence, household and movement records.

These blockers do not lower battle-core categories. They identify world-state work outside the Java tactical core.

## Encounter dependency review

### Station Rush

Full version needs:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement if civilians and wildlife share tactical lanes — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions if lanes dynamically open/close — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy for `CLEAR_ROUTE`/`REACH_EXIT`-style goals — BLOCKING;
- Minecraft/Cobblemon/Craftics playback — BLOCKING;
- overworld population/presence projection — BLOCKING outside battle core.

Reduced version:

Resolve crowd routing before battle. Remove commuters from the tactical projection. Freeze station geometry and run a conventional legal battle only with actual combatants. After battle, update commuter-flow and transport state.

### Temporary Camp Perimeter

Full version needs:

- complete movement — BLOCKING if residents/wildlife move in tactical space;
- terrain/zones/reactions — BLOCKING for protected corridors or dynamic perimeter state;
- tactical AI — BLOCKING for wildlife withdrawal/protection goals;
- playback — BLOCKING;
- basic targeting/calculations/initiative — VERIFIED where applicable.

Reduced version:

Keep camp residents outside the battle grid. Determine the active wildlife corridor in overworld state. If conflict occurs, use one static legal arena. Apply no invented panic, crowd, morale or escort mechanics.

### Boomtown Survey

Full version needs:

- targeting/LoS — VERIFIED;
- base movement — VERIFIED;
- complete movement/interception — BLOCKING for dynamic crossings;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL;
- terrain/zones/reactions — BLOCKING if construction changes battlefield state;
- tactical AI — BLOCKING;
- playback — BLOCKING;
- move/Ability/item/Feature families — PARTIAL unless the exact mechanic is specifically verified.

Reduced version:

Resolve survey progress and wildlife crossings in world state. Freeze construction state before battle. Use conventional combat only when a real encounter occurs.

## PTU / Caelo caution

Pass 60 creates no demographic combat mechanics.

Do not infer or invent:

- crowd initiative;
- crowd cover;
- panic conditions;
- stampede damage;
- morale modifiers;
- migration Skill checks;
- settlement population bonuses;
- social modifiers based on origin;
- civilian escort actions;
- encounter scaling based on population density;
- legal residence/citizenship mechanics.

The project-supplied primary Caelo corpus was not reliably available in this automation runtime, so no new Caelo-specific large-group, settlement or social rule is asserted.

## Evidence required for richer population-driven encounters

Battle-side:

- verified objective contracts such as CLEAR_ROUTE / REACH_EXIT / PROTECT or equivalents;
- complete interception/forced movement;
- broad zone/reaction support;
- tactical AI that understands movement objectives;
- authoritative Minecraft playback.

Overworld-side:

- population profiles and cohorts;
- migration events;
- residence/presence distinction;
- commuter flows;
- aggregate service pressure;
- crisis-displacement links;
- privacy controls;
- settlement/housing capacity integration;
- representative-NPC projection;
- offline advancement for population state.

## Snapshot conclusion

Pass 60 does not justify relaxing the permanent capability map.

Java's newest round-rollover work materially strengthens initiative and lifecycle evidence, but full lifecycle remains PARTIAL.

Demographic worldbuilding can advance now because population context, cohorts, migration events, commuters, displacement and settlement pressure are overworld concepts. Mechanically rich crowd or evacuation encounters remain blocked by complete movement, dynamic zones/reactions, tactical AI and Minecraft playback. Reduced versions can keep population movement outside the grid and use static legal battles.