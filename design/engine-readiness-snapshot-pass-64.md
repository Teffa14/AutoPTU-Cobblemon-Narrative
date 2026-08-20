# Engine Readiness Snapshot — Pass 64

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

`3e26f9d856da02a23403164f49bb46ea296ecd99`

Latest inspected commit:

`Port trainer initiative speed resolution (#97)`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/3e26f9d856da02a23403164f49bb46ea296ecd99

This follows the Pass 63 inspected head:

`44f7d67afe7573593e996ebc39c99cd188c88f1d` — `Port initiative additional bonus family (#96)`.

New bounded evidence since Pass 63:

- a dedicated trainer-initiative Speed resolution contract;
- explicit Trainer Speed wins when present;
- otherwise the fastest active, non-fainted controlled Pokémon supplies the Speed;
- when no eligible active Pokémon exists, the fastest Pokémon in that Trainer's battle roster is used;
- an empty roster resolves to zero;
- pinned Python-oracle fixtures;
- Java parity tests;
- Gradle and CI wiring for that exact slice.

This strengthens the already-VERIFIED action economy / initiative family.

It does not prove:

- full lifecycle coverage;
- complete Trainer Feature behavior;
- tactical AI policy;
- terrain or wildfire state;
- hazards or moving zones;
- forced movement or interception;
- Minecraft/Cobblemon projection.

No permanent capability family is promoted by Pass 64.

## Java README boundary

The current AutoPTU-Java README still states that Python AutoPTU remains authoritative while the port is incomplete.

It still lists unfinished broad work including:

- core combatant/grid battle state expansion;
- full damage resolution pipeline;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/item/perk/Trainer Feature hook registries;
- semantic battle-event and full BattleSpec -> BattleTranscript parity;
- tactical AI scoring/policy;
- Craftics/Cobblemon adapter.

That boundary is decisive for Pass 64 because a dynamic wildfire encounter would depend heavily on several of those unfinished families.

## Python AutoPTU live evidence

Current inspected Python main head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible main work remains Career-focused (`Career: make roster recovery deterministic`).

Available project evidence shows specific Python behavior for Burned, Fire-type interactions, terrain-dependent Features and selected environment logic.

That evidence must remain narrow.

For example, a Python rule that makes Fire-type Pokémon immune to the Burned status does not establish immunity to wildfire, smoke, heat or an environmental hazard that has not been defined by PTU/Caelo and implemented in Java.

Likewise, terrain-aware Feature code does not prove a general fire-spread or wildfire-zone subsystem.

## Permanent capability map

| Permanent capability family | Pass 64 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Dedicated geometry, targeting, footprint, anchor and LoS coverage exists. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers and fit predicates exist. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement/interception and broad movement reactions remain unfinished. |
| core calculations | VERIFIED | PTU tables, combat stages, accuracy primitives, crit probability and selected modifiers exist. |
| action economy / initiative | VERIFIED | Typed turn flow, deterministic ordering, round rebuilds and multiple Python-parity initiative slices now include trainer initiative Speed resolution. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure is substantial, but complete status/Ability/Feature/reaction/delayed-effect coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Multiple damage and post-damage slices exist while the README still lists full damage as unfinished. |
| status lifecycle | PARTIAL | Multiple status contracts/timing slices exist; complete controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Semantic terrain/weather consumers and selected Python terrain logic do not prove runtime battlefield wildfire, smoke, zones or broad reactions. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; complete PTU Move behavior does not. |
| abilities | PARTIAL | Multiple Ability hooks exist; full registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog behavior remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered/lifecycle infrastructure plus selected Features exist; complete catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-action generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware scoring/policy such as retreating from fire or protecting an exit remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core and does not yet own Minecraft projection/playback. |

## Pass 64-specific overworld blockers

Wildfire is mostly persistent world-state infrastructure until tactical fire mechanics exist.

`OVERWORLD_FIRE_EVENT_GRAPH = BLOCKING`

The server needs persistent fire-event identity, revision history and lifecycle from first observation through recovery and long-term monitoring.

`OVERWORLD_IGNITION_CAUSE_EVIDENCE = BLOCKING`

Ignition observations, competing hypotheses, evidence and public belief need separate records. A nearby Fire-type Pokémon, damaged power line or lightning report must remain evidence rather than automatic cause truth.

`OVERWORLD_FIRE_FRONT_AND_SMOKE_FOOTPRINT = BLOCKING`

Active fronts and smoke-affected areas need separate spatial state. Smoke may affect a place that is nowhere near active flame.

`OVERWORLD_BURN_SEVERITY_MOSAIC = BLOCKING`

A fire scar needs coarse spatial patches for unburned, low-, moderate-, high- and unknown-severity state. The system must not depend on every Minecraft block.

`OVERWORLD_FIRE_REFUGIA_AND_SUCCESSION = BLOCKING`

Unburned refugia, early regrowth, structural recovery and later changed habitat need persistent ecological versions.

`OVERWORLD_PLANNED_FIRE_PROJECT_STATE = BLOCKING`

Any authored management fire needs objectives, responsible actors, authority source, preparation, monitoring, abort conditions and review. This is world-state governance and stewardship, not a battle-core feature.

`OVERWORLD_POST_FIRE_WATERSHED_COUPLING = BLOCKING`

Fire scar state needs a safe causal bridge into freshwater catchments so later rainfall, sediment/ash observations and downstream infrastructure effects can be recorded without inventing combat effects.

`OVERWORLD_FIRE_TO_COBBLEMON_ECOLOGY = BLOCKING`

The server needs a non-exploitable projection from fire-scar/recovery state into coarse wild-Pokémon presence. Loaded Cobblemon entities cannot become the ecological source of truth.

`OVERWORLD_FIRE_TO_BATTLE_PROJECTION = BLOCKING`

A revisioned adapter contract is required before any regional fire state can become a battlefield hazard, smoke zone, Weather interaction or other PTU mechanic. Only effects validated by exact PTU/Caelo rules and Java contracts may cross this boundary.

`OVERWORLD_FIRE_TO_MINECRAFT_PLAYBACK = BLOCKING`

Minecraft needs safe visual hooks for smoke, flame, charred terrain, barriers, recovery works and regrowth. Client-visible fire blocks or particles cannot become authoritative battle or regional state by themselves.

## Encounter dependency review

### Firebreak Ridge

Full version requires:

- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement incl. push/pull/knockback/interception/forced movement — BLOCKING if retreat lanes can be intercepted or an environmental effect forces movement;
- core calculations — VERIFIED;
- action economy / initiative — VERIFIED;
- full turn / round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain / weather / hazards / zones / reactions — BLOCKING for active flame, smoke, heat or changing safe zones;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features / perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for avoid-fire, withdraw, protect-corridor or escape goals;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- fire-event and ecological writeback — BLOCKING outside battle core.

Reduced version:

Resolve fire-front movement and safe-lane selection before battle. Freeze one static ridge arena. Keep active wildfire and smoke outside tactical mechanics or visual-only. If a legal fight occurs, run a conventional encounter using current verified/partial engine boundaries and apply displacement/route consequences afterward through world state.

### Ash Creek Crossing

Full version may require:

- targeting / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for current, debris displacement or forced retreat;
- core calculations — VERIFIED;
- action economy / initiative — VERIFIED;
- full lifecycle — PARTIAL if environmental state changes by round;
- full damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain / weather / hazards / zones / reactions — BLOCKING for changing runoff, unstable banks or debris zones;
- tactical AI — BLOCKING for reach-exit, survey, protect or withdraw objectives;
- adapter/playback — BLOCKING.

Reduced version:

Resolve hydrology and post-fire runoff before battle. Freeze one safe crossing revision and water level. Treat ash, sediment and erosion as overworld observations. Start a standard static battle only if a real confrontation occurs.

### Refuge Edge

This concept should normally remain an observation, conservation and route-management scenario rather than a mass battle.

If a battle occurs now:

- project only actual participants;
- use static geometry;
- keep the larger refuge population outside the grid;
- do not infer a new collective merely because many displaced Pokémon are co-located;
- do not assign special capture rules.

A future full version with movement-based avoidance or escape would require:

- complete movement/interception/forced movement — BLOCKING;
- terrain/zones/reactions — BLOCKING;
- AI tactical policy — BLOCKING;
- Minecraft playback — BLOCKING.

## PTU / Caelo caution

Pass 64 creates no wildfire mechanic.

Do not infer or invent:

- fire spread per round;
- ignition probability from Fire Moves;
- wildfire damage;
- smoke damage;
- smoke Accuracy/Evasion penalties;
- oxygen or suffocation rules;
- environmental Burned merely from entering a burned or flaming area;
- structure HP or fire resistance;
- water-volume extinguishing math;
- Rain Dance extinguishing a regional wildfire;
- Firestarter ignition/suppression beyond exact governing text;
- automatic wildfire immunity for Fire-type Pokémon;
- heat-exhaustion mechanics;
- firefighting Skill DCs;
- ash Poisoned effects;
- post-fire rare-spawn bonuses;
- special capture modifiers for displaced Pokémon.

Available Python evidence for Burned immunity and terrain-linked effects is narrow and cannot be generalized to these concepts.

The project-supplied full Caelo corpus was not reliably retrievable during this run. No new exact Caelo wildfire, smoke, environmental-Burned, firefighting or fire-regime rule is asserted.

## Snapshot conclusion

Pass 64 does not justify a permanent capability promotion.

Java head `3e26f9d856da02a23403164f49bb46ea296ecd99` strengthens the already-VERIFIED action economy / initiative family with a parity-tested trainer initiative Speed resolver.

It does not materially reduce the main blockers for dynamic wildfire encounters.

Wildfire worldbuilding can advance safely as persistent ignition evidence, fronts, smoke, severity mosaics, refugia, ecological succession, recovery and post-fire watershed state. Mechanically rich fire encounters should continue to use reduced static versions until terrain/weather/hazards/zones/reactions, complete movement, tactical AI and the Minecraft adapter are actually verified.