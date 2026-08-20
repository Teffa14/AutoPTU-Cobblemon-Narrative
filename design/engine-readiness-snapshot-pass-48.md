# Engine Readiness Snapshot — Pass 48

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only Python oracle
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live heads

### AutoPTU-Java

Inspected head:

`11748b3c77f86ea96f78a357aaa92370e3478a58`

Latest inspected change:

`Add move keyword parity gate to CI`

The newest sequence adds a canonical move-keyword contract, a Python oracle exporter, Java parity testing, Gradle wiring and CI enforcement for the resulting fixtures.

This is useful implementation evidence because move metadata now has another explicit cross-language contract.

Do not infer from it:

- complete Move behavior;
- full Move hook coverage;
- full damage resolution;
- complete status behavior;
- complete Ability or item behavior;
- terrain/weather/hazard execution;
- forced movement or broad reactions;
- tactical objective AI;
- Minecraft/Cobblemon/Craftics playback.

The current Java README still explicitly lists as unfinished:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- semantic battle-event emission and full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

### Python AutoPTU

Inspected head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest visible Python commits are Career/roster-recovery work. They do not justify promotion of any Java tactical family.

Python remains the behavioral oracle while the Java port is incomplete.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Battle targeting, areas, anchors, footprints, range and line-of-sight have strong deterministic evidence.

This does not verify digital-network topology, terminal visibility, camera coverage or access graphs.

#### base movement legality

Overland/Swim/Sky Shift legality, represented terrain costs, blockers, Wallrunner, sprint, jump and landing-fit boundaries have strong evidence.

This does not verify cyberspace traversal, virtual movement rules, network routing or Porygon digital travel.

#### core calculations

Damage Base tables, type-effectiveness steps, combat stages, accuracy stages and several calculation primitives remain verified.

#### action economy / initiative

Typed phases, action budgets and deterministic initiative/League ordering remain verified.

#### AI legal-action infrastructure

The core can produce and filter deterministic legal battle choices.

It does not yet prove tactical or objective-aware policy.

### PARTIAL

#### full turn / round lifecycle

Typed phases, actor/phase state, end-turn cleanup, round histories, delayed-hit infrastructure and selected status/Ability/perk dispatch provide substantial slices.

The complete lifecycle remains unproven.

#### full stateful damage pipeline

Multiple calculation and hook slices are authoritative, but the Java README still lists full damage resolution as unfinished.

#### status lifecycle

Selected status applications, metadata and phase behavior exist. The full controller is incomplete.

#### move-specific behavior

The new move-keyword parity contract improves data/metadata parity and CI coverage.

It does not prove executable behavior for the complete Move catalogue. The category remains PARTIAL.

#### abilities

Several Ability hooks, combat-stage interactions and spatial aura slices are parity-tested.

Representative Abilities do not prove the complete catalogue.

#### items

Held-item state and selected item hooks exist. The complete item family remains partial.

#### Trainer Features / perks

Ordered perk infrastructure and selected concrete Trainer Features exist with parity evidence.

The complete Feature/perk catalogue remains partial.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

The Java README still groups forced movement with unfinished combat systems. Any encounter that depends on tactical displacement, escort interception or dynamic route denial remains blocked on this family.

#### terrain / weather / hazards / zones / reactions

Broad battlefield state remains unfinished. Narrow reaction hooks and aura queries do not prove general zones, weather phases, attacks of opportunity, hazard lifecycles or interactable battlefield regions.

#### AI tactical policy

Legal choices exist; strategy, retreat, escort, protection, objective prioritization and scenario-aware planning remain blocking.

#### Minecraft / Cobblemon / Craftics adapter and playback

AutoPTU-Java remains a Java core library, not a Minecraft mod. The README explicitly defers the adapter until a parity-safe vertical slice exists.

## Pass 48 digital-system implications

Most of the new layer can advance as world state without new battle rules:

- digital systems and services;
- record/version histories;
- backups and restores;
- access grants;
- account/identity claims;
- software releases;
- event logs;
- data reconciliation;
- digital incidents;
- virtual-space persistence descriptions;
- privacy rules;
- Porygon/Rotom observed digital interactions;
- terminal and server-room presentation state.

None of those objects creates a PTU modifier by itself.

## Source gate: Porygon cyberspace

Official Pokémon material supports Porygon moving through cyberspace at a setting level.

This snapshot does not treat that sentence as an AutoPTU movement implementation.

Before tactical use, the project still needs exact PTU/Caelo source extraction for relevant Pokémon capabilities, Moves, Abilities, Technology Education interactions or other rules.

Therefore:

- ordinary Java base movement legality remains VERIFIED;
- Porygon-specific cyberspace traversal remains an unresolved rules/source gate;
- Minecraft virtual-space traversal remains adapter-blocked.

## Encounter dependency — Server Room Failover

Reduced version:

World-state operators switch to fallback service before/after a conventional static battle. This can preserve the narrative premise with current verified tactical fundamentals.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if unsafe technical zones become tactical;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for PROTECT/ACTIVATE/REACH objectives;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## Encounter dependency — Porygon Diagnostic Dive

Reduced version:

Resolve cyberspace diagnosis through world-state investigation. If combat occurs, instantiate a separate static legal battle. Do not grant invented cyberspace movement or access permissions.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED for battle geometry;
- base movement legality — VERIFIED only for ordinary represented battle movement;
- full turn/round lifecycle — PARTIAL;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- AI tactical policy — BLOCKING for diagnostic/objective behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- exact PTU/Caelo Porygon digital interaction — UNRESOLVED SOURCE GATE.

## Encounter dependency — Archive Restore Conflict

Reduced version:

Choose backup/version and perform reconciliation outside battle. If the room is physically contested, use a conventional static AutoPTU encounter. Restore changes present data state while post-snapshot Chronicle history remains intact.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- action economy/initiative — VERIFIED;
- terrain/weather/hazards/zones/reactions — BLOCKING if restoration nodes become tactical zones;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## Digital-system non-inferences

Current Java evidence does not establish:

- hacking or intrusion mechanics;
- digital access-control checks;
- Porygon traversal rules;
- Rotom network control;
- virtual-space injury/damage transfer;
- Pokémon digital storage;
- battle effects from software;
- network latency as Initiative;
- software corruption as a PTU status;
- data objects as battle targets;
- terminal interaction as a Standard/Shift action.

These require explicit governing rules and implementation contracts.

## Promotion rule

A permanent capability family moves upward only when runtime wiring, representative deterministic contracts, tests and Python-oracle parity establish that family. Data-schema parity, a keyword fixture or one representative mechanic never promotes an entire behavior category.
