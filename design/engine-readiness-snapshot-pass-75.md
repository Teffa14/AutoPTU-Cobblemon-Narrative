# Engine readiness snapshot — pass 75

Status: implementation evidence only. This document does not expand canon or mechanically authorize narrative content.

## Repositories inspected

Narrative writable destination:
- `Teffa14/AutoPTU-Cobblemon-Narrative`
- working branch: `agent/pass-53-evolution-life-stage`

Read-only engine evidence:
- `Teffa14/AutoPTU-Java` main at `4bab1de9abcc28dc1257af8ad7aa4b803dfaa9c3`
- `Teffa14/AutoPTU` main at `e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest Java head message:
`Execute canonical Trainer initiative slots`

The latest Java slice allows canonical initiative order to contain server-owned Trainer turns as well as Pokémon turns, validates actor identities fail-closed and freezes the relevant contract against Python.

This strengthens the already-VERIFIED action-economy/initiative family. It does not add cave visibility, 3D navigation, dynamic water, cave-ins, sinkhole behavior, subterranean ecology, airflow or underground mapping.

Java README still states that these broad areas remain incomplete:
- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Permanent capability classification

### VERIFIED

Targeting / footprints / range / LoS

Evidence: Java README marks range, areas, footprints, target anchors and line of sight complete for the documented contracts.

Pass-75 non-inference: geometric LoS does not prove cave darkness, visibility distance, fog/mist, glare, echo localization, concealment or line tracing across vertical cave levels.

Base movement legality

Evidence: Java README marks Shift movement and Jump slices complete for their documented contracts, including Overland/Swim/Sky and fit predicates.

Pass-75 non-inference: this does not prove squeezing through cave passages, climbing shafts, unstable ledges, rope use, currents, diving, underwater tunnels, falling, rubble traversal or multi-level cave adjacency.

Core calculations

Evidence: PTU tables, calculation primitives, accuracy and combat-stat resolution are marked complete for their documented contracts.

Action economy / initiative

Evidence: typed turn flow, deterministic ordering and current canonical Trainer/Pokémon initiative-slot work are parity-backed.

AI legal-action infrastructure

Evidence: deterministic legal `BattleChoice` generation exists for currently represented action types and geometry.

### PARTIAL

Full turn / round lifecycle

Many lifecycle slices exist, including canonical initiative slots, phase infrastructure, effect dispatch and rollover work, but the README does not claim complete BattleSpec -> BattleTranscript lifecycle parity.

Full stateful damage pipeline

Representative damage/Ability hooks exist; the README still lists the full pipeline as incomplete.

Status lifecycle

Specific statuses and phase infrastructure exist, but the controller is incomplete.

Move-specific behavior

Metadata and representative move behaviors exist; catalog-wide behavior remains incomplete.

Abilities

Multiple parity-tested Ability slices exist; the complete registry remains incomplete.

Items

Representative held-item behavior exists; catalog-wide item support is incomplete.

Trainer Features / perks

Representative Features and lifecycle infrastructure exist; catalog-wide support is incomplete.

### BLOCKING

Complete movement including push / pull / knockback / interception / forced movement

No current evidence promotes this family. For pass 75 it also covers lack of verified current movement, falling, multi-elevation traversal and route-interception behavior.

Terrain / weather / hazards / zones / broad reactions

Java owns some semantic environment state for specific calculations, but terrain/hazards/reactions remain explicitly incomplete.

A cave floor, flood pulse, loose rock, low ceiling, darkness, gas pocket or sinkhole must not become PTU terrain/hazard/reaction state merely because Minecraft renders it.

AI tactical policy

Legal-action enumeration exists. Objective-aware choice for withdraw, reach-exit, protect-roost, escape-flood, use-high-ground or avoid-unstable-route goals is not verified.

Minecraft / Cobblemon / Craftics adapter and playback

Still future work per Java README.

## Python-oracle evidence relevant to pass 75

Available project `battle_state.py` evidence shows:
- `cave`, `cavern` and `underground` as recognized environment-context labels for specific named mechanics;
- cave context in narrow Nature Power / Secret Power style mappings;
- explicit movement/capability checks for Overland, Swim, Sky/Levitate and other movement modes;
- habitat matching through Naturewalk labels for specific effects.

This proves narrow Python mechanics only.

It does not establish:
- a generic cave-terrain engine;
- darkness or visibility mechanics for every cave;
- 3D or multi-height cave movement;
- cave-in hazards;
- dynamic water levels or currents;
- gas/suffocation rules;
- squeezing/crawling rules;
- echo-based targeting;
- universal cave encounter modifiers;
- cave ecology or population persistence.

The primary Caelo corpus was not reliably retrievable during this pass. No new Caelo-specific cave, darkness, climbing, falling, Burrow, underground-water or environmental rule is claimed.

## Pass-75 encounter dependency matrix

### Sinking Passage Survey

Full version requires:
- targeting/footprints/range/LoS: VERIFIED baseline;
- base movement legality: VERIFIED baseline;
- complete movement / forced movement / interception: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full lifecycle: PARTIAL;
- full stateful damage: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal actions: VERIFIED;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

Reduced version is viable earlier because hydrology and route eligibility remain world state. The server chooses one validated chamber state before battle and does not change water levels during combat.

### Roost Entrance Disturbance

Full version additionally needs:
- a visibility context distinct from LoS if darkness matters;
- wild withdrawal goals;
- noncombatant/protected-zone handling;
- objective-aware AI;
- complete movement/interception if exits can be contested.

Reduced version keeps visitor evacuation and roost state outside battle. Only actual defenders/attackers enter a static entrance chamber.

### Sinkhole Dye-Tracer Follow-Up

This is primarily research/exploration and can exist with no battle.

If combat occurs, the reduced version requires only a static validated chamber and current verified geometry/movement.

The full version would need dynamic water/access state, interactable monitoring points and multi-stage world-to-battle transitions, all currently unverified.

### Collapsed Mine-Natural Junction

Full version requires:
- unstable-route or collapse hazards: BLOCKING;
- rescue/protect objectives: tactical AI BLOCKING;
- workers/noncombatants in tactical space: adapter/objective contracts unverified;
- complete movement if falling or blocked-edge displacement is possible: BLOCKING.

Reduced version resolves stability and rescue corridors before battle. Combat occurs on one safe frozen geometry version with no invented rockfall damage.

### Deep Pool Crossing

Full version would require validated underwater/deep-water movement, possible exit objectives and any current/drowning rules.

Reduced version handles the pool as an overworld access gate. If combat occurs, use a fixed dry ledge or shallow-water arena compatible with existing base movement legality.

## Pass-75 blockers outside permanent battle categories

BLOCKING: `SUBTERRANEAN_SYSTEM_STATE`
No runtime service yet owns durable cave-system identity independent of Minecraft chunks.

BLOCKING: `SUBTERRANEAN_GEOMETRY_VERSIONING`
No server-owned graph currently versions discovered passages, collapses, newly opened entrances and uncertain edges.

BLOCKING: `CAVE_ENTRANCE_STATE`
Surface/subsurface access, condition, wildlife use and institutional restrictions are not yet unified persistent state.

BLOCKING: `CAVE_MICROCLIMATE_STATE`
No coarse server model owns cave temperature/humidity/airflow revisions.

BLOCKING: `SUBTERRANEAN_HYDROLOGY_LINKS`
Freshwater/groundwater state is not yet connected to cave passages, sinkholes, springs or flood pulses through a persistent graph.

BLOCKING: `CAVE_NUTRIENT_INPUT_STATE`
No service tracks coarse external organic inputs or their ecological relevance.

BLOCKING: `CAVE_OCCUPANCY_EVIDENCE`
Calls, marks, guano, tracks and camera records are not yet standardized evidence objects linked to cave features.

BLOCKING: `ROOST_COLONY_SITE_STATE`
Repeated cave aggregation sites do not yet have durable identity and disturbance history.

BLOCKING: `CAVE_TO_CARTOGRAPHY_PROJECTION`
No contract publishes cave geometry revisions and uncertainty into actor-specific map editions.

BLOCKING: `CAVE_TO_COBBLEMON_PROJECTION`
No safe anti-exploit contract maps cave ecological state to loaded Pokémon presentation/spawns.

BLOCKING: `CAVE_TO_BATTLE_PROJECTION`
No validated adapter converts cave world state into an immutable legal battle environment with visibility/hazard semantics.

## Explicit non-inferences

- `cave` in a Python environment label does not prove a complete cave subsystem.
- A dark Minecraft chamber does not automatically apply Blinded or Accuracy penalties.
- Zubat or Woobat cave ecology does not grant other species generic echolocation.
- Wall marks or guano do not prove exact current abundance.
- A visible group at a roost is not automatically the whole population.
- A sinkhole does not prove a connection to the nearest known cave.
- Water underground does not prove Swim legality, current mechanics or drowning rules.
- A cave collapse in world state does not create battle damage or forced movement automatically.
- A mined chamber does not create loot nodes, Carbink, fossils or rare spawns by default.
- A maintained cave gate does not automatically create or remove ecological impact.
- Current Trainer initiative parity does not affect any cave/environment capability category.

## Next mechanical checks

1. Extract exact PTU/Caelo text for darkness, Darkvision, Blindsense, Glow and visibility.
2. Extract exact PTU/Caelo rules for climbing, falling, Burrow, Wallrunner and narrow/vertical traversal.
3. Confirm how deep water, underwater travel and drowning/suffocation are represented in PTU/Caelo.
4. Inspect whether Java plans a separate visibility context from geometric LoS.
5. Keep cave hydrology in world state until an explicit `world environment -> BattleEnvironmentState` contract exists.
6. Keep cave geometry versioning separate from battle-map geometry.
7. Keep reduced cave encounters on one frozen tactical chamber until dynamic terrain/hazards/objectives are authoritative.
