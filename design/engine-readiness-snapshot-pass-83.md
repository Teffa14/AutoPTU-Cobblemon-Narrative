# Engine Readiness Snapshot — Pass 83

Status: implementation-evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`a5a77bd23cbe9841d896b901522de83e7d4280a8`

Latest visible commit:

`Freeze battle-scoped RNG ownership for lifecycle execution`

Previous Pass 82 head:

`3c82018e8f9f123500688d59cc94eba565593231`

AutoPTU Python oracle inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its current head remains Career-oriented and does not change the permanent tactical capability map.

## New Java evidence since Pass 82

The new Java slice introduces `BattleRandomState`, which owns one Python-compatible mutable RNG stream for a battle.

The RNG accessor is package-private so external adapters cannot request rolls or advance the stream through the public battle boundary.

The new parity contract freezes several Python-oracle facts:

- ordinary move resolution accepts an explicit RNG stream;
- ordinary attack resolution consumes that supplied stream;
- `BattleState` target resolution forwards the battle-owned RNG;
- ordinary target resolution feeds the move resolver;
- matured delayed-hit resolution at round start receives the same battle owner.

This is valuable authority work. Ordinary and covered delayed resolution must consume one battle-owned RNG sequence rather than letting Minecraft, a client or a second subsystem invent rolls.

## What the new RNG evidence does not prove

Pass 83 must not infer:

- all Python RNG call sites are already ported;
- all Moves consume RNG correctly in Java;
- full `BattleSpec -> BattleTranscript` parity;
- complete turn/round lifecycle;
- complete delayed-effect behavior;
- civilian movement or crowd simulation;
- public-space schedules;
- dynamic blockers;
- urban terrain rules;
- civilian HP or panic behavior;
- object/property damage;
- tactical withdrawal;
- tactical escort/protection objectives;
- Minecraft/Cobblemon playback.

The evidence strengthens battle RNG authority. It does not create new world mechanics.

## Java README boundary

The current AutoPTU-Java README still lists unfinished work for:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic event emission and full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the primary anti-overclaim boundary.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

VERIFIED for the implemented geometric surface.

Pass 83 guardrail:

Geometric LoS does not prove crowd visibility, concealment behind moving civilians, glare, smoke, urban lighting, window reflection or dynamic stall occlusion.

A public-space projection may use verified static blockers. It may not turn background NPCs into LoS blockers unless a future authoritative snapshot supports them.

### base movement legality

VERIFIED for the implemented static Shift/Jump and Overland/Swim/Sky surface.

Pass 83 guardrail:

Base legality does not prove movement through crowds, squeezing past civilians, queue behavior, escalators, moving transit, evacuation flow, moving market stalls or public-space right-of-way.

### core calculations

VERIFIED for ported primitives.

Pass 83 guardrail:

There is no generic `crowded plaza penalty`, `park bonus`, `market cover bonus`, `station speed penalty`, `bench cover`, `street-fighting bonus` or `public morale` by implication.

### action economy/initiative

VERIFIED for the implemented surface.

The new RNG ownership work reinforces that battle resolution and action execution must use server-owned deterministic state rather than client/adaptor rolls.

Pass 83 guardrail:

Public event schedules, market hours, commuter waves and evacuation clocks are overworld state. They are not combat-round state by default.

### AI legal-action infrastructure

VERIFIED for deterministic supported legal choices.

It does not establish AI goals such as:

- EXIT_CROWDED_AREA;
- PROTECT_CORRIDOR;
- WITHDRAW_TO_PARK_EDGE;
- AVOID_CIVILIANS;
- ESCORT_NONCOMBATANT;
- CLEAR_FORECOURT;
- HOLD_EXIT_OPEN;
- DISENGAGE_FROM_MARKET;
- PRESERVE_PUBLIC_ASSET.

## PARTIAL

### full turn/round lifecycle

PARTIAL.

Java has typed phases, authoritative initiative, cleanup surfaces, selected status/Ability/Feature hooks, delayed-effect storage/execution slices and now an explicit battle-owned RNG boundary.

Pass 83 adds useful RNG ownership evidence but does not prove every phase effect, duration, switch/send-out flow, reaction, delayed form or transcript event.

### full stateful damage pipeline

PARTIAL.

The covered move paths increasingly derive state authoritatively and consume the battle-owned RNG stream.

The README still declares full damage resolution unfinished.

Pass 83 guardrail:

Attack animation near a bench, stall, lamp, fountain, wall, vehicle or civilian does not create object damage, splash damage or environmental consequences unless an authoritative mechanic emits them.

### status lifecycle

PARTIAL.

Selected statuses have application/phase/expiry evidence. Full status coverage remains incomplete.

Pass 83 guardrail:

Crowding, panic, noise, smoke, litter, heat, rain or public attention cannot generate Slowed, Tripped, Confused, Enraged, Blinded, Poisoned or other battle Status by narrative description.

### move-specific behavior

PARTIAL.

Selected Move contracts and increasingly authoritative delayed-hit paths exist. Full library behavior is not proven.

Pass 83 guardrail:

Moves that appear suited to interacting with public objects or dispersing groups still require exact current implementation evidence. Flavor does not create crowd-control functionality.

### abilities

PARTIAL.

Multiple representative Ability hooks have parity evidence. The family remains incomplete.

Pass 83 guardrail:

Intimidating, soothing, sound-related, light-related or movement-related Ability flavor cannot become public crowd behavior without exact rules and implementation.

### items

PARTIAL.

Representative item state/effects exist. Complete coverage does not.

Pass 83 guardrail:

Barricades, market goods, benches, cameras, signs, transit tickets, vendor equipment and event assets remain world-state objects unless validated as PTU Items.

### Trainer Features/perks

PARTIAL.

Representative Features and hook infrastructure exist. The complete class/Feature/Edge/Order catalog remains incomplete.

Pass 83 guardrail:

Charm, Command, Guile, Intimidate, Acrobatics, Athletics or other Skill/Feature concepts cannot produce custom crowd DCs or public-space bonuses without exact PTU/Caelo validation.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

BLOCKING as a family.

Pass 83 FULL encounters need this for:

- intercepting actors before they enter a crowd;
- keeping evacuation corridors open;
- moving through chokepoints with competing flows;
- forced displacement away from civilians;
- moving obstacles or noncombatants;
- escort-style movement;
- controlled withdrawal routes.

Reduced versions must resolve civilian/crowd movement before battle and freeze a static tactical boundary.

### terrain/weather/hazards/zones/reactions

BLOCKING as a family.

Pass 83 would need this for:

- protected exit lanes as tactical zones;
- dynamic crowd boundaries;
- temporary market/stall zones;
- reactions to crossing restricted areas;
- public-space hazards;
- weather-driven changing conditions;
- interactive public objects;
- dynamic event barriers.

Until verified, public-space conditions remain overworld state/presentation.

### AI tactical policy

BLOCKING.

Legal actions do not establish AI understanding of:

- withdrawal instead of KO;
- protecting civilians;
- clearing a corridor;
- avoiding a crowd;
- escaping through a route;
- separating fighting groups;
- avoiding property;
- choosing a safer battle area;
- disengaging after an objective is met.

### Minecraft/Cobblemon/Craftics adapter/playback support

BLOCKING.

The adapter has no parity-safe contract yet for projecting a public-space revision, crowd state and static battle perimeter into AutoPTU-Java and rendering the semantic results back into Minecraft.

Minecraft must not calculate:

- PTU crowd penalties;
- public-space Terrain;
- civilian combat state;
- object HP;
- knockback consequences;
- panic movement;
- retreat legality;
- battle RNG.

The latest Java RNG ownership work makes the last boundary especially explicit: the adapter must never own or advance battle rolls.

# Encounter dependency summary

## Station Forecourt Rush — FULL

Needs:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement family — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full damage — PARTIAL;
- status lifecycle — PARTIAL if used;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED:

Resolve crowd diversion before battle. Use a static forecourt with fixed blockers and combatants only.

## Park Edge Wildlife Conflict — FULL

Critical blockers:

- complete movement;
- zones/reactions;
- tactical AI;
- adapter/playback.

REDUCED:

Clear spectators first, freeze one static park-edge arena and preserve crossing/withdrawal as world-state outcomes after ordinary legal combat.

## Night Market Chokepoint — FULL

Critical blockers:

- complete movement;
- dynamic/interactable zones or object contracts;
- tactical AI;
- adapter/playback.

REDUCED:

Close the affected market lane and secure visitors/goods before battle. Stalls may project as ordinary static blockers only.

# Public-space-specific non-battle blockers

These are not AutoPTU-Java responsibilities:

- `PUBLIC_SPACE_IDENTITY_AND_BOUNDARY` — BLOCKING;
- `PUBLIC_SPACE_TIME_PROGRAM` — BLOCKING;
- `PUBLIC_SPACE_USE_OBSERVATION` — BLOCKING;
- `PUBLIC_SPACE_FRONTAGE_GRAPH` — BLOCKING;
- `INFORMAL_PATH_HISTORY` — BLOCKING;
- `PUBLIC_SPACE_EVENT_OCCUPATION` — BLOCKING;
- `PUBLIC_SPACE_PRESSURE_REVISION` — BLOCKING;
- `URBAN_POKEMON_USE_OBSERVATION` — BLOCKING;
- `PUBLIC_SPACE_COHORT_PROJECTION` — BLOCKING;
- `PUBLIC_SPACE_TO_MINECRAFT_PROJECTION` — BLOCKING;
- `PUBLIC_SPACE_TO_BATTLE_SNAPSHOT` — BLOCKING.

# Current conclusion

The public-space layer can advance now as persistent world state because its core value comes from schedules, repeated use, co-presence, edges, callbacks, Pokémon observations and physical/social change across time.

Mechanically rich public-space battles should remain conservative. Before AutoPTU-Java can support crowds, escorts, safe corridors, dynamic stalls or withdrawal-aware wild actors, the reduced pattern should be:

world state resolves civilian movement and current place use
→ server chooses a safe bounded snapshot
→ AutoPTU-Java resolves only the real combatants and verified mechanics
→ authoritative result writes back to Chronicle/public-space/ecology/case state
→ Minecraft renders the new state.

The new battle-owned RNG evidence strengthens this authority boundary without changing the permanent category classifications.