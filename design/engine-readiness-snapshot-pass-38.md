# Engine Readiness Snapshot — Pass 38

Status: read-only evidence snapshot for narrative design. No changes are made to AutoPTU-Java or AutoPTU.
Date: 2026-08-19

## Repositories inspected

AutoPTU-Java head: `cd510f3cd812532ae84304b01377c34a285863c5`

Python AutoPTU head: `e4bb0ca38b7018710af476ce365d515a387de4e7`

## New Java evidence since Pass 37

The new Java head integrates the existing combatant phase-effect dispatcher into the default lifecycle.

The commit:
- composes the built-in status phase registry;
- registers the combatant phase dispatcher on PHASE_CHANGE;
- runs STATUS and ABILITY phase families through that default lifecycle path;
- tests that an authoritative Ability phase effect such as Lancer executes when ACTION advances to END.

This is a real architectural improvement. It reduces the gap between isolated hook registries and the actual default turn lifecycle.

It does not prove complete lifecycle, status, Ability or perk coverage.

No-inference rules:
- default dispatcher integration does not prove every phase-triggered rule is registered;
- STATUS + ABILITY integration does not prove the complete Status or Ability families;
- absence of PERK in the currently composed default dispatcher does not alter the permanent Trainer Features/perks classification;
- a generic lifecycle boundary cannot stand in for unported Move, Ability, Item or Trainer Feature semantics;
- no current Java evidence in this pass establishes Sonic keyword handling or Soundproof parity.

The AutoPTU-Java README continues to list full combatant/grid state, full damage resolution, the full status controller, terrain/hazards/forced movement/reactions, complete Move/Ability/Item/perk/Trainer Feature registries, tactical AI and Minecraft/Cobblemon/Craftics integration as unfinished.

## Python evidence relevant to Pass 38

Repository search finds Soundproof in Python AutoPTU's ability implementation/audit surface. Python therefore contains at least an authoritative source path that future Java work can inspect.

This does not establish:
- that Soundproof is fully parity-tested in Java;
- that every Sonic-tagged Move is implemented end-to-end;
- that overworld hearing exists;
- that Soundproof changes mundane hearing outside its explicit governing rule;
- that generic sound propagation exists in the battle engine.

The latest Python head remains Career/API-focused relative to the tactical capability map, so no permanent category changes are justified from Python commits in this pass.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

Caveats:
- battle LoS does not establish acoustic occlusion or overworld hearing;
- verified base movement does not include push/pull/knockback/interception/forced movement;
- core calculation primitives do not equal the full stateful damage pipeline;
- legal action enumeration does not imply tactical decision quality.

### PARTIAL

- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items

Lifecycle evidence is stronger than Pass 37 because STATUS and ABILITY phase dispatch now run through the default lifecycle path rather than existing only as reusable registries/dispatcher infrastructure.

The category remains PARTIAL because full BattleSpec -> BattleTranscript coverage, all phase effects, delayed execution, complete cleanup semantics and all family interactions remain incomplete.

Status remains PARTIAL. Current evidence includes bounded Flinch, Strange Tempo/Confusion, metadata, application prevention, phase registries and lifecycle integration. It does not prove all statuses, Save Checks or cross-status interactions.

Abilities remain PARTIAL. Current evidence includes representative abilities, an ordered Ability phase registry, Lancer parity and lifecycle integration. It does not prove the complete Ability catalog, including Soundproof.

Move-specific behavior remains PARTIAL. Generic Move and targeting infrastructure does not prove every Sonic Move or special-case Move effect.

Items remain PARTIAL based on prior representative held-item slices. No new evidence in this pass promotes the family.

### BLOCKING

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- Trainer Features/perks
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

These remain blocking for any full encounter version that depends on them.

## Pass 38 sound boundary

Narrative soundscape state is not a battle mechanic.

The following concepts can advance as world state today:
- acoustic sources;
- observations;
- recordings;
- call libraries;
- location soundscape baselines;
- anomaly detection;
- quiet-zone policy;
- listening stations;
- acoustic landmarks;
- accessible audio/visual puzzle representations.

The following require explicit mechanics or adapter evidence before they can affect battle or stealth:
- a hearing radius;
- acoustic wall occlusion;
- sound-source localization during tactical movement;
- noise-based enemy detection;
- generic sound damage;
- generic sleep/fear/emotion effects from sound;
- Soundproof outside its exact governing rule;
- Sonic Move interactions;
- sound-triggered Ability effects;
- sound-caused forced movement;
- dynamic acoustic zones;
- sound-reactive tactical AI.

## Soundproof no-inference rule

Even if Python contains Soundproof logic, do not infer any of the following for Java or Minecraft:
- the Ability family is complete;
- every Sonic Move is correctly tagged;
- Soundproof blocks all world audio;
- Soundproof creates hearing impairment;
- Soundproof blocks public alarms or speech;
- Soundproof changes stealth perception.

Only the exact PTU/Caelo rule and parity-backed Java implementation may define those effects.

## Sonic Move no-inference rule

A narrative event described as loud does not become a Sonic Move.

A Pokémon species known for powerful cries does not automatically know a sound-based Move.

A Move with sound flavor does not receive Sonic behavior unless authoritative move data says so.

A Sonic Move that applies a status or movement effect depends on:
- move-specific behavior — PARTIAL;
- status lifecycle — PARTIAL when a status is involved;
- abilities — PARTIAL when Soundproof or other Ability interactions matter;
- complete movement — BLOCKING when push/pull/knockback/forced movement occurs;
- full lifecycle — PARTIAL for phase-timed consequences;
- AI tactical policy — BLOCKING if AI must reason about the sonic interaction.

## Pass 38 encounter dependencies

### Echo Cavern Search

FULL version:
- targeting/footprints/range/LoS — VERIFIED for battle targeting only
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING if the encounter uses those mechanics
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL if legal Sonic Moves apply statuses
- terrain/weather/hazards/zones/reactions — BLOCKING for mechanical cave zones/acoustic effects
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — BLOCKING if used
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version: resolve acoustic observations and directional clues in overworld state with visual/text accessibility equivalents. AutoPTU receives a fixed legal arena only after contact occurs. Echo/reflection does not alter PTU range, LoS or Accuracy.

### Silent Relay Station

FULL version may require:
- ACTIVATE_OBJECT / HOLD_ZONE style objective support;
- terrain/hazards if damaged electrical/mechanical areas are tactical;
- objective-aware AI;
- Minecraft signal playback and world-state synchronization;
- authoritative item/Trainer Feature actions if repairs are mechanical.

Those dependencies remain PARTIAL or BLOCKING.

REDUCED version: investigate and restore the relay in overworld logic. A conventional static battle can occur before or after the repair. The restored signal becomes a world sound event rather than a combat buff.

### Roost Quiet Corridor

FULL version depends on an overworld auditory perception/noise model, collective reaction logic, possibly withdrawal/protection objectives and Minecraft playback.

The permanent categories most affected are:
- complete movement/interception — BLOCKING if tactical escape/protection is required;
- move-specific behavior — PARTIAL for actual Sonic Moves;
- abilities — PARTIAL;
- AI tactical policy — BLOCKING;
- Minecraft adapter/playback — BLOCKING.

REDUCED version: use explicit overworld choices and observations, no hidden numeric noise meter. Any battle occurs in a fixed arena separate from protected roost state.

### Fog Beacon

FULL version depends on:
- terrain/weather/hazards/zones/reactions — BLOCKING for mechanical fog/visibility changes;
- Minecraft adapter/playback — BLOCKING for spatial beacon presentation;
- AI tactical policy — BLOCKING if route/objective behavior matters;
- move-specific/Ability families only if actual combatants use relevant rules.

REDUCED version: fog and beacon timing remain overworld state. Any battle uses the verified normal battle LoS/range rules rather than custom fog or hearing modifiers.

## Accessibility boundary

Minecraft audio presentation cannot be the only route to mandatory information.

Until an accessibility contract exists, every required acoustic clue must have an equivalent observable representation. This is a narrative/UI design requirement and does not change PTU mechanics.

## Conclusion

Pass 38 can safely add persistent soundscape state, species-call observations, recordings, acoustic baselines, quiet/noise conflicts, listening stations, acoustic landmarks and accessible sound-led puzzles.

The new Java head strengthens default lifecycle integration but does not change the permanent capability classification. Sonic combat mechanics remain gated behind exact PTU/Caelo extraction plus parity-safe move/Ability/status implementation. Acoustic stealth, propagation, dynamic sound zones and spatial playback remain outside current verified tactical capabilities and should stay in reduced overworld forms until explicit contracts exist.
