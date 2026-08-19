# Engine Readiness Snapshot — Pass 41

Status: read-only evidence snapshot for narrative design. No changes are made to AutoPTU-Java or AutoPTU.
Date: 2026-08-19

## Repositories inspected

AutoPTU-Java head: `864761bf75c62976022f245ffd8deeacc61e85e6`

Python AutoPTU head: `e4bb0ca38b7018710af476ce365d515a387de4e7`

Python remains the authoritative oracle while the Java port is incomplete.

## New Java evidence since Pass 40

Commit `864761bf75c62976022f245ffd8deeacc61e85e6` adds authoritative mutable combat-stage state and binds current combat stages into runtime move resolution.

The same slice ports fixed Link Trainer Features through authoritative state:
- Attack Link;
- Defense Link;
- Special Attack Link;
- Special Defense Link;
- Speed Link.

The implementation includes AP spending, END-phase behavior, stage mutation, fail-closed conditions and Python-oracle parity tests for those exact Features.

This is meaningful progress for Trainer Features/perks and stateful combat-stage handling.

## What the new evidence does not prove

Trainer Features/perks remain PARTIAL.

Do not infer:
- complete Trainer Feature catalog coverage;
- social/non-combat Features;
- all Orders;
- interrupts;
- reaction-triggered Features;
- Rider, Athlete, Chef, Medic, Researcher or crafting Feature coverage;
- arbitrary Link-like Features not included in the tested fixed set;
- complete AP semantics for all Features;
- complete interactions among Features, movement, damage, statuses, Abilities and Items.

Mutable combat stages do not prove the full stateful damage pipeline. A parity-tested fixed Link family does not make Trainer Features complete.

## Current Java README boundary

The current README still lists major work as unfinished, including:
- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full semantic battle transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Use this as the conservative boundary when narrative concepts require advanced battle behavior.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

Caveats:
- base movement does not establish push/pull/knockback/interception/forced movement;
- core calculations do not establish the full stateful damage pipeline;
- legal-action enumeration does not establish good tactical choice;
- battle LoS does not establish Minecraft overworld perception.

### PARTIAL

- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

#### Full turn/round lifecycle

PARTIAL.

Typed phases, authoritative actor/phase state, phase families, cleanup, histories, delayed-hit infrastructure and several parity-tested hooks exist. Complete transcript semantics and all triggered families are not finished.

#### Full stateful damage pipeline

PARTIAL.

Java now reads authoritative mutable combat stages during move resolution, strengthening stateful stat handling. The repository still explicitly lists full damage resolution as unfinished.

#### Status lifecycle

PARTIAL.

There is bounded evidence for status application, prevention, metadata, phase processing and selected statuses. Complete status coverage is not present.

#### Move-specific behavior

PARTIAL.

Generic infrastructure plus bounded special cases does not establish full Move coverage.

#### Abilities

PARTIAL.

Concrete and registry-backed slices exist, but the Ability catalog and every interaction are incomplete.

#### Items

PARTIAL.

Representative held-item behavior exists. Full Item coverage is not proven.

#### Trainer Features/perks

PARTIAL, with stronger evidence than Pass 40.

Exact currently evidenced slices include authoritative trainer Feature ownership/AP state, phase registry integration, Defense Mastery, and the fixed Link Features listed above. Other Features remain unverified until implemented and parity-tested individually.

### BLOCKING

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

These remain blocking for FULL encounter versions that depend on them.

## Pass 41 agreement/mediation boundary

Most agreement state is safe to model outside the battle engine:
- disputes;
- negotiation sessions;
- proposal versions;
- explicit acceptance/refusal;
- agreements;
- commitments;
- dependencies;
- performance records;
- breach claims;
- amendments;
- temporary truces;
- repair plans;
- public summaries;
- expiry/termination state.

None of those records should directly alter battle statistics.

Mechanical social resolution remains PTU/Caelo source-gated. The narrative layer must not invent Charm/Command/Guile/Intimidate/Intuition DCs, surrender rules, coercion rules, social clocks or automatic consent.

## Encounter dependency — Relay Station Ceasefire

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:
Resolve the ceasefire as server world state before battle. Keep the two hostile parties physically separated. Run only a conventional static encounter against the external threat. Do not require battle AI to understand truce boundaries.

## Encounter dependency — Waterworks Boundary Agreement

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage — PARTIAL
- statuses — PARTIAL
- terrain/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- tactical AI — BLOCKING
- Minecraft playback/interactables — BLOCKING

REDUCED version:
Negotiate access and emergency responsibilities outside battle. If combat occurs, use a static fight. Update pump schedule and obligation state only after authoritative overworld resolution.

## Encounter dependency — Restitution at the Market Gate

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage — PARTIAL
- statuses — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- tactical AI — BLOCKING
- Minecraft/Cobblemon/Craftics playback — BLOCKING

REDUCED version:
Keep cargo custody and repair commitments outside the grid. Use a conventional battle only to clear the separate threat/chokepoint, then resume the handoff.

## No-inference rule

The new fixed Link Feature parity strengthens one narrow family. It does not change the BLOCKING assessment for forced movement, hazards/reactions, tactical AI or Minecraft playback, and it does not validate any social negotiation Feature.
