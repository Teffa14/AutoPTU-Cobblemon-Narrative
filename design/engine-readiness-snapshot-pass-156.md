# Engine Readiness Snapshot — Pass 156

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `d33508f96dc7802d694308ba40bcda64abdb42b8`
Date: 2026-08-30

## Read-only engine heads inspected

AutoPTU-Java:

`ba5d97576b4fe469b2e4064737b1520e8b67a384` — `Resolve Intercept attack line from authoritative battle state (#290)`

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`

No files in either engine repository were modified by Pass 156.

Neither read-only engine head advanced since Pass 155. Pass 156 therefore makes no capability promotion.

## Current interpretation of Java evidence

The current AutoPTU-Java head remains meaningful evidence for server-owned targeting/line geometry and a bounded Intercept path. `GridLineResolution` shares canonical grid-line geometry with targeting/LoS, and Intercept attack-line input is derived from authoritative battle-state positions rather than supplied by Minecraft/Cobblemon.

This evidence remains localized. It does not prove:

- every Push source;
- Pull;
- general Knockback;
- every Intercept form and ordering interaction;
- arbitrary forced movement;
- escort/rescue movement;
- object carrying;
- moving platforms or vehicles;
- structural collapse;
- dynamic water/current displacement;
- electrical hazard timing;
- generalized reaction windows;
- tactical protect, flee, delay or access-denial policy.

The AutoPTU head remains presentation-only evidence and does not change battle rules or outcomes.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted by Pass 156.

## Substation Isolation Perimeter — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL if displacement or Intercept matters near constrained access
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for delayed or phased tactical changes
- full stateful damage pipeline — PARTIAL as selected combat content requires
- status lifecycle — PARTIAL as selected combat content requires
- terrain/weather/hazards/zones/reactions — BLOCKING for live electrical zones, equipment hazard timing or reaction windows
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for access denial, withdrawal, protection or delay objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative hazard/equipment playback

Overall full status: BLOCKED.

Reduced status: READY at narrative-contract level if selected Moves, Abilities, Items and Features are individually audited.

Reduced constraints:

- Ouros establishes any isolation/safe-state fact before initiative;
- technicians, bystanders and semantic equipment remain outside BattleSpec;
- static safe geometry only;
- explicit combatant roster;
- no live electrical hazard semantics;
- no destructible infrastructure objective;
- permitted tactical result: `IMMEDIATE_SUBSTATION_APPROACH_CLEAR`.

Hard safeguards:

`APPROACH_CLEAR != ASSET_ISOLATED`

`BATTLE_WON != POWER_RESTORED`

## Flood Pump Access Corridor — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL if current or forced displacement matters
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for changing water phases
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING for water depth, current, flooded zones or reaction windows
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for hold/clear/withdraw behavior
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative changing-water playback

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- Ouros freezes water level and environmental condition for the tactical slice;
- pump, controls, repair crew and noncombatants remain outside BattleSpec;
- fixed geometry;
- explicit combatants;
- permitted result: `IMMEDIATE_PUMP_ACCESS_CORRIDOR_CLEAR`.

`CORRIDOR_CLEAR != PUMP_WORKING`

`BATTLE_WON != FLOODING_RESOLVED`

## Bridge Inspection Chokepoint — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for ordinary static legal movement only
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL if edge displacement matters
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL if structural changes occur by phase
- full stateful damage pipeline — PARTIAL as selected battle content requires
- status lifecycle — PARTIAL as selected battle content requires
- terrain/weather/hazards/zones/reactions — BLOCKING for collapse, unstable terrain or falling-zone reactions
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING if route denial/withdrawal is semantic
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative structural change

Structural collapse/destructible infrastructure is an additional unverified semantic dependency. Do not infer it from Minecraft block destruction.

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- unsafe bridge span remains non-traversable, non-targetable scenery;
- tactical slice occurs only on static safe staging geometry;
- inspectors and equipment remain outside BattleSpec;
- permitted result: `IMMEDIATE_INSPECTION_STAGING_AREA_CLEAR`.

`STAGING_AREA_CLEAR != BRIDGE_SAFE`

`BATTLE_WON != BRIDGE_REOPENED`

## Repair Convoy Staging Perimeter — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL; escort/carry/vehicle semantics remain unverified
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if moving lanes or dynamic route hazards matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for escort, protect, delay or withdrawal decisions
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for moving vehicles/objects and authoritative tactical playback

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- convoy vehicles are stationary during BattleSpec;
- crew, cargo and repair objectives remain outside BattleSpec;
- no object carrying or escort semantics;
- static geometry;
- explicit combatants;
- permitted result: `IMMEDIATE_REPAIR_CONVOY_APPROACH_CLEAR`.

`APPROACH_CLEAR != CONVOY_ARRIVED`

`BATTLE_WON != MATERIALS_DELIVERED`

## Infrastructure authority boundary

Pass 156 gives Narrative continuity authority only over authored or evidence-supported records such as:

- asset identity and historical function;
- condition observations;
- operational-state records;
- authored service dependencies;
- interruption reports and confirmed scopes;
- condition assessments;
- work-order state;
- stabilization/isolation events;
- repair episodes;
- temporary-service episodes;
- restoration scope;
- decommissioning and repurposing events.

It does not give Narrative authority to manufacture:

- electrical or hydraulic simulation;
- structural-collapse rules;
- infrastructure HP;
- engineering DCs;
- utility ownership law;
- safety codes;
- repair costs or durations;
- technical qualifications;
- contractor licensing;
- service priorities;
- authority to enter, isolate, repair, inspect or reopen a facility;
- Pokémon generation output or construction capability;
- generic effects of Moves/Abilities on infrastructure.

AutoPTU remains authoritative only for tactical facts covered by BattleSpec and verified mechanics.

Minecraft/Cobblemon/Craftics remains presentation/playback only. It may render already-decided damaged/restored states, closures, temporary equipment, lighting or workers. It cannot use block state, redstone, pathfinding, physics, lava, entity AI or Cobblemon battle state to decide service condition, hazard damage, repair success, combatants, PTU HP/status or restoration.

## PTU/Caelo unresolved mechanics and setting assumptions

Keep UNKNOWN until project-approved source evidence and current implementation contracts verify them:

- universal engineering/repair Skill checks;
- electrical grid or water-network rules;
- generic infrastructure damage rules;
- structural collapse and falling infrastructure rules;
- generic electrical hazards;
- generic water-current or flooding combat semantics;
- repair times, costs and material consumption;
- universal inspection procedure;
- utility safety codes;
- building/electrical/plumbing code regimes;
- infrastructure ownership and regulatory structures;
- contractor licensing or certification;
- universal service restoration priorities;
- automatic Move/Ability/Feature interactions with generators, pumps, grids, bridges or machinery;
- universal Pokémon power-generation values;
- generic technical use of Electric-, Water-, Ground-, Steel- or other typed Pokémon based only on flavor;
- automatic repair or service restoration after battle;
- automatic infrastructure damage from Minecraft physics or destructible blocks;
- escort/object-carrying/vehicle tactical semantics;
- dynamic-hazard lifecycle and reaction ordering.

## Canon questions opened by Pass 156

Future canon review must decide explicitly:

- which infrastructure systems exist in each Ouros region;
- which settlements depend on which assets;
- where alternate/backup service exists;
- which institutions own, operate, inspect or authorize work on specific assets;
- what professions or qualifications exist;
- whether formal inspection and reopening procedures exist;
- which old facilities are decommissioned, abandoned in common speech or repurposed;
- which historical outages, bridge closures, floods or rebuilds are canon;
- what technical roles Pokémon may perform under PTU/Caelo authority;
- whether particular Moves, Abilities, Items or Trainer Features can support maintenance or repair outside battle;
- which first infrastructure-service arc should be promoted from proposal to canon.

Until those decisions are approved, Pass 156 remains systems grammar, research provenance and NON-CANON seed material.