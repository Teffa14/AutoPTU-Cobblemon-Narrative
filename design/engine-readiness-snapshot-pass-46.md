# Engine Readiness Snapshot — Pass 46

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only Python oracle
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live heads

### AutoPTU-Java

Inspected head:

`9e68bde8391b057c982900d038cc9ec3a3d348f9`

Latest change inspected:

`Apply post-damage hooks in authoritative move runtime`

The commit connects the existing post-damage hook family to authoritative move resolution. Flat post-damage bonuses are applied after ordinary damage/type arithmetic, before HP mutation and damage-history recording. The integration includes a runtime test for the adjacent Aqua Boost behavior.

Important non-inference:

- this does not complete the full damage pipeline;
- this does not complete Abilities;
- this does not complete broad reactions;
- this does not implement terrain, weather or hazards;
- this does not prove all post-damage effects;
- this does not implement tactical AI;
- this does not implement Minecraft/Cobblemon/Craftics playback.

The Java README still explicitly lists as unfinished:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete move/ability/item/perk/Trainer Feature registries;
- full semantic battle transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

### Python AutoPTU oracle

Inspected head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The newest Python commits inspected are Career-side changes and do not provide evidence for promotion of the Java tactical capability families.

Python runtime evidence remains useful as an oracle. It includes Chronicler-oriented Trainer actions and a broader Trainer Feature catalogue. The generated trainer runtime coverage report still contains many entries without runtime mappings, so individual Trainer Features must be verified by name before use.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Evidence remains strong for target anchors, areas, footprints, range and line-of-sight contracts.

Do not infer overworld camera vision, patrol sight, photographic field of view or Minecraft visibility from battle LoS.

#### base movement legality

Evidence remains strong for Shift movement, Overland/Swim/Sky basics, terrain costs already represented by the movement grid, blockers, Wallrunner, sprint, jump and landing-fit predicates.

Do not infer forced movement, interception, currents, evacuation traffic or arbitrary overworld traversal.

#### core calculations

Damage Base tables, type-effectiveness step chart, stages, accuracy stages and several modifier primitives remain verified at the core-calculation level.

#### action economy / initiative

Typed turn phases, action budget, initiative ordering and League ordering remain verified.

#### AI legal-action infrastructure

The deterministic action-space contract can enumerate/filter legal battle choices.

This does not mean the AI chooses strategically good actions.

### PARTIAL

#### full turn / round lifecycle

Lifecycle evidence has expanded substantially across recent passes: typed phases, actor/phase state, phase transitions, end-turn cleanup, round histories, delayed-hit infrastructure, status-phase registries, ability/perk phase dispatch and several concrete hooks.

The full family remains partial because the complete battle transcript and every rule-trigger interaction are not yet proven.

#### full stateful damage pipeline

The current head improves this category materially by applying authoritative post-damage hooks before HP mutation and damage-history recording.

The category remains partial because the Java README still lists full damage resolution and remaining stateful modifiers as unfinished, and one integrated aura family does not prove all damage effects.

#### status lifecycle

Flinch, Confusion-related behavior, status metadata, application boundaries, status-phase registries and selected Ability interactions provide real coverage.

The complete controller remains unfinished.

#### move-specific behavior

Selected Move/rider behavior exists, but the complete PTU Move library and all unusual effects are not proven.

#### abilities

Coverage now includes several concrete Ability families and hooks, including stage reactions, spatial interactions and adjacent post-damage aura effects.

`Aqua Boost`, `Ignition Boost`, `Thunder Boost`, `Plus`, `Minus`, `Defiant`, `Competitive`, `Simple`, `Inner Focus`, `Lancer`, `Mega Launcher` and other representative slices do not prove the full Ability catalogue.

#### items

Held-item state and selected item hooks exist from earlier slices.

The full item catalogue remains incomplete.

#### Trainer Features / perks

The Java runtime now has an ordered perk registry, authoritative Trainer state binding and selected implemented Features such as Defense Mastery and fixed Link Features.

The family remains partial. The Python trainer runtime coverage report still shows a large majority of entries without runtime mapping. Chronicler-related functionality visible in Python must not be assumed in Java until its exact contract is ported and parity-tested.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

The movement baseline does not prove these effects.

Any encounter whose premise requires forced displacement, body interception, escort blocking or movement reactions must retain this dependency explicitly.

#### terrain / weather / hazards / zones / reactions

Some existing calculations know about terrain costs or weather-related arithmetic, and selected hook reactions exist.

The broad battlefield-state family remains blocking because the README still lists terrain, hazards, forced movement and reactions as unfinished.

Do not treat a combat-stage reaction registry as proof of attacks of opportunity, hazard triggers, moving zones, weather phases or battlefield-control reactions.

#### AI tactical policy

Legal choice generation exists.

Strategic scoring, objective awareness, retreat planning, protection behavior and scenario-specific tactical policy remain blocking.

#### Minecraft / Cobblemon / Craftics adapter and playback

Java remains a core library, not a Minecraft mod. Minecraft/Cobblemon/Craftics integration remains future work.

This blocks assumptions about:

- physical battle playback;
- camera blocks or camera entities;
- battle replay capture;
- screenshot-to-world-record ingestion;
- per-player image privacy;
- camera-trap ticking in unloaded chunks;
- spatial audio/visual evidence synchronization;
- visible tactical objectives implemented by the world adapter.

## Pass 46 visual-evidence implications

### Visual records can advance without battle support

The following can be implemented as narrative/world-state data before tactical expansion:

- visual record provenance;
- camera station metadata;
- image classification history;
- derivative/crop/redaction chains;
- public/private access rules;
- historical photo comparisons;
- media captions and publication links;
- archive/museum catalog integration;
- identity-match hypotheses;
- camera-network maintenance state;
- scientific dataset references.

### Battle records should derive from engine events

The authoritative source for battle truth should remain AutoPTU semantic state/events.

A visual replay or screenshot is a representation of that result, not the authority for damage, status, legality or outcome.

### Chronicler remains feature-specific

Python evidence shows Chronicler-oriented runtime actions. Java Trainer Features are only partially ported.

Therefore photography and visual evidence must not grant:

- Chronicler archive records;
- Cinematic Analysis effects;
- Targeted Profiling;
- Accuracy bonuses;
- scouting bonuses;
- Move knowledge;
- social bonuses;

unless the exact Feature implementation and preconditions are authoritative in the runtime being used.

## New encounter dependency summary

### Camera Trap Recovery

Current reduced version: feasible as overworld investigation plus static legal battle when required.

Full-version blockers:

- complete movement/interception if wildlife or enemies dynamically block escape/recovery routes;
- terrain/weather/hazards/zones/reactions if the corridor changes during battle;
- AI tactical policy for objective-aware movement;
- Minecraft/Cobblemon/Craftics adapter/playback for physical station interaction and world synchronization.

### Press Gallery Incident

Current reduced version: feasible as standard battle plus post-resolution visual/public-memory records.

Full-version blockers:

- complete movement/interception for evacuation lanes;
- broad terrain/hazards/reactions for venue changes;
- AI tactical policy for civilians/objective-aware actors;
- adapter/playback for camera placement and deterministic visual reconstruction.

### Historic Photograph Survey

Preferred current implementation is mostly noncombat.

If a static battle occurs, use only exact implemented Moves/Abilities/Items/Features. No photography-specific tactical mechanic is required.

## Promotion rule

A capability moves upward only when representative contracts, runtime wiring, deterministic tests and Python parity establish the relevant family. One working representative effect never promotes the whole family.
