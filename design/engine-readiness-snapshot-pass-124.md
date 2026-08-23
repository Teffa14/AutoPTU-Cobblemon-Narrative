# Engine Readiness Snapshot — Pass 124

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU were inspected read-only.

## Live heads inspected

AutoPTU-Java `main`: `45feae6161c9b92ccb008a60d9b6e16dcbc0c377`

Newest Java slice ports the spatial Ability-based status-prevention family for Aroma Veil, Aroma Veil [Errata], Pastel Veil and Sweet Veil. It uses canonical battle state, battle geometry, Ability suppression, ordered status-application hooks and semantic `status_block` events.

This strengthens evidence for status application, Abilities and geometry-aware hooks. It does not complete the status controller, the Ability catalog, movement objectives, ecological group movement or any migration system.

AutoPTU `main`: `cd2d31ab9438713629ad3fc65939e8cc622b5a1f`

Newest Python change verifies the deployable Career browser artifact and source provenance. It is Career/deployment CI work and does not promote a tactical capability family.

## Java README evidence

The current Java README still lists major incomplete areas including:

- broader canonical combatant/grid state;
- full damage resolution and remaining stateful modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/Perk/Trainer Feature hook registries;
- semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Permanent capability categories

VERIFIED:

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL:

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING:

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 124.

## Why migration remains primarily overworld state

Nothing inspected establishes an authoritative battle or adapter subsystem for:

- migration-pattern identity;
- migration episodes across world time;
- population-scale corridor revisions;
- stopover use;
- movement waves;
- partial migration;
- temporary separation/reunion;
- migration monitoring effort;
- ecological route fidelity;
- response to roads, rail, fences, ports or settlements;
- population-scale CROSS/WITHDRAW behavior;
- unloaded-chunk migration progression;
- persistent migration projection into Cobblemon spawns.

Those belong to world/server persistence. AutoPTU should receive only the combatants and frozen tactical state needed for a real confrontation.

## Important movement boundary

Java base movement legality is VERIFIED for currently supported tactical movement rules.

That does not prove:

- migrating actors can follow a moving corridor objective;
- wildlife understands CROSS, WITHDRAW, REJOIN or AVOID_CONFLICT;
- interception or forced movement is available;
- a herd/flock can move as one entity;
- Sky/Swim/Burrow capability can be inferred narratively;
- road/rail/river crossings have dynamic tactical behavior;
- moving civilians or wildlife can be represented safely in Minecraft playback.

Likewise, battle LoS and spatial Ability radii do not define ecological corridor width.

## Pass 124 encounter dependency map

### Corridor Crossing at Redbank — FULL

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for moving wildlife, crossing lanes and interception
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING when traffic, barriers or environmental state is tactically active
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for CROSS/WITHDRAW/PROTECT/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: the migration group remains outside battle authority while world state resolves the crossing window, workers and civilians. If a confrontation remains, AutoPTU receives a static cleared verge with only actual combatants. After battle, Migration plus Road/Rail state decides whether passage resumes. Battle victory cannot establish corridor success.

### Stopover Disturbance at Reedglass Marsh — FULL

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for retreating groups and changing crowd boundaries
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only when marsh/weather state has an explicitly verified tactical effect
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for WITHDRAW/PROTECT/AVOID_CONFLICT
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: visitor routing and migration-wave movement resolve in overworld state. A small safe perimeter is frozen before combat. AutoPTU handles only the confrontation that remains. The migration episode may progress without any battle.

### Separated Individual at North Pass — FULL

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for pursuit/reunion during an active movement wave
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if mountain/weather effects enter tactical resolution
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for REACH_GROUP/WITHDRAW/ESCORT
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: tracking, route search and reunion are resolved as overworld state. If a separate threat causes combat, the migration group stays outside tactical authority unless its members are actual combatants. Reunion updates participation/history only; it does not create ownership, Loyalty or capture rights.

## New overworld blockers introduced by Pass 124

- `MIGRATION_PATTERN_REGISTRY`
- `MIGRATION_EPISODE_STATE`
- `MIGRATION_CORRIDOR_REVISION_HISTORY`
- `MIGRATION_CORRIDOR_SEGMENT_GRAPH`
- `MIGRATION_STOPOVER_REGISTRY`
- `MIGRATION_WAVE_OBSERVATION_LEDGER`
- `MIGRATION_MONITORING_EFFORT`
- `MIGRATION_PARTICIPATION_STATE`
- `MIGRATION_ROUTE_COMPARISON`
- `MIGRATION_BARRIER_RESPONSE_HISTORY`
- `MIGRATION_TIMING_REVISION`
- `MIGRATION_TO_SEASONALITY_HANDOFF`
- `MIGRATION_TO_WILD_COLLECTIVE_HANDOFF`
- `MIGRATION_TO_ROAD_RAIL_AIRSPACE_MARITIME_HANDOFF`
- `MIGRATION_TO_CONSERVATION_HANDOFF`
- `MIGRATION_TO_COBBLEMON_PROJECTION`
- `MIGRATION_TO_MINECRAFT_PRESENTATION`
- `MIGRATION_TO_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 124

Do not infer:

- Flying type -> migratory behavior;
- flock/herd/school -> active migration;
- seasonal encounter-table change -> confirmed migration;
- one route observation -> permanent corridor;
- one successful crossing -> corridor restored;
- stopover not observed -> stopover abandoned;
- missing annual migration -> extinction;
- late/early movement -> climate causation;
- wind/rain -> forced movement;
- visible subgroup size -> population size;
- temporary separation -> abandonment;
- migrating Pokémon -> capture availability;
- migrating former partner -> renewed Trainer authority;
- migration group -> Pack Mon, swarm or morale mechanics;
- base movement legality -> migration objective support;
- AI legal-action infrastructure -> CROSS/WITHDRAW tactical policy;
- Minecraft entity movement -> canonical corridor;
- chunk despawn -> migration departure;
- battle withdrawal -> permanent migration reroute;
- battle victory -> corridor reopened or stopover restored.

## PTU/Caelo validation state

The accessible runtime did not expose Super PTU Online Helper as an invocable capability. The complete primary Caelo Player’s Guide/rulebook/errata corpus was not reliably available through the tools used in this run.

No generic PTU/Caelo migration mechanic, migration Skill DC, tracking bonus, travel speed, group-movement modifier, migration capture modifier or swarm rule is claimed.

The project’s existing PTU/Python evidence contains specific movement capabilities and tactical effects, but Pass 124 does not generalize Sky, Swim, Burrow, Naturewalk, Run Away, Pack Mon or any similar rule into migration behavior.

## Current engine conclusion

Java’s status path remains stronger than earlier passes because the current head includes spatial Ability-based status prevention through canonical state and geometry. Status lifecycle and Abilities remain PARTIAL because this is representative coverage, not family-complete implementation.

Migration stories can advance safely today when corridor history, stopovers, observations, timing, route changes and persistent Pokémon identity remain overworld state. Mechanically rich versions with active crossing, withdrawal, escort or pursuit should wait for complete movement, tactical AI and Minecraft playback. Reduced static-battle versions preserve the same narrative premise without reimplementing missing PTU rules in the adapter.