# Engine Readiness Snapshot — Pass 42

Status: read-only evidence snapshot for narrative design. No changes are made to AutoPTU-Java or AutoPTU.
Date: 2026-08-19

## Repositories inspected

AutoPTU-Java head: `053c61f949a02bd6baedf769ff74e88ebdfa8ea8`

Python AutoPTU head: `e4bb0ca38b7018710af476ce365d515a387de4e7`

Python remains the authoritative oracle while the Java port is incomplete.

## New Java evidence since Pass 41

Commit `053c61f949a02bd6baedf769ff74e88ebdfa8ea8` adds a parity-safe ordered combat-stage reaction hook registry.

The slice defines:
- a server-owned combat-stage hook context;
- a POST_APPLY hook phase;
- explicit source categories such as Ability, Item, Status and Trainer Feature;
- ordered hook registration;
- semantic events emitted by hooks;
- a concrete `Simple` Ability reaction to already-applied combat-stage changes;
- Python-oracle fixtures and CI parity coverage for the exact contract.

This is meaningful infrastructure for reactions to combat-stage mutation and strengthens the evidence for Ability behavior and lifecycle integration.

## What the new evidence does not prove

Do not promote the combined `terrain/weather/hazards/zones/reactions` family.

The new registry handles one bounded kind of reaction: post-application responses to combat-stage changes. It does not prove:
- attacks of opportunity;
- interception;
- movement reactions;
- damage-triggered interrupts;
- general Trainer Feature interrupts;
- terrain-triggered reactions;
- weather-triggered reactions;
- hazard entry/exit reactions;
- zone control;
- arbitrary Ability reactions;
- Defiant, Competitive, Minus, Plus or other reserved combat-stage hooks until they are actually implemented and parity-tested;
- full ordering among every future Item, Status, Ability and Trainer Feature hook.

`Simple` parity is one Ability slice. It does not make Abilities complete.

## Current Java README boundary

The current README still states that the port has not completed:
- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The README remains the conservative boundary when one narrow implementation appears more advanced than the category as a whole.

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
- legal-action enumeration does not establish good tactical policy;
- battle LoS does not establish Minecraft overworld perception or accessibility.

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

Authoritative phases, actor/phase state, phase dispatch, cleanup, histories, delayed-hit infrastructure, mutable combat stages and multiple parity-safe hook families exist. Complete transcript semantics and every triggered family do not.

#### Full stateful damage pipeline

PARTIAL.

Current combat stages feed move resolution, but Java still explicitly lists full damage resolution as unfinished.

#### Status lifecycle

PARTIAL.

There is bounded coverage for application, prevention, metadata, phase processing and selected statuses. Complete status behavior is not present.

#### Move-specific behavior

PARTIAL.

Special-case infrastructure and representative Moves exist. Full Move library behavior is not established.

#### Abilities

PARTIAL, strengthened in Pass 42.

Evidence now includes phase-scoped Ability infrastructure plus concrete slices such as Lancer, Inner Focus interactions, Strange Tempo-related behavior from earlier passes, and the new `Simple` combat-stage hook. The catalog and cross-family interactions remain incomplete.

#### Items

PARTIAL.

Representative item behavior exists. Full Item coverage is not proven.

#### Trainer Features/perks

PARTIAL.

Authoritative Trainer Feature ownership/AP state, a phase registry, Defense Mastery and fixed Link Features have parity-safe evidence. The new combat-stage hook registry can identify Trainer Feature as a hook source, but that source category does not itself implement new Features.

### BLOCKING

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

These remain blocking for FULL encounter versions that depend on them.

## Pass 42 accessibility boundary

Most accessibility state belongs outside tactical combat:
- player accessibility settings;
- access preferences;
- semantic captions;
- alternate information formats;
- step-free route information;
- public event access plans;
- institution access information;
- UI scaling/contrast preferences;
- communication-channel preferences;
- quiet spaces;
- temporary lift/route outages;
- support arrangements;
- alternate puzzle presentations.

These records must not change PTU stats automatically.

Do not infer:
- Slowed from a mobility aid;
- Blinded from low vision;
- Soundproof from deafness;
- Injury from a request for a rest break;
- Perception bonuses from assistive technology;
- movement capabilities from an alternate route;
- Trainer Features from an accommodation;
- combat advantage from captions or UI scaling.

The Minecraft adapter should use host accessibility features when available. Player-facing settings must remain separate from character/world canon.

## Encounter dependency — Evacuation Route Split

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
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
Resolve evacuation route choice in world state first. Keep civilians outside AutoPTU and run a static battle only against the remaining threat.

## Encounter dependency — Signal Hall Outage

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/forced movement — BLOCKING if moving machinery/interception is required
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage — PARTIAL
- statuses — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if electrical/environmental zones are used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- tactical AI — BLOCKING
- Minecraft playback/interactables — BLOCKING

REDUCED version:
Treat the display/caption outage as infrastructure state. Run a conventional static battle. Restore the system afterward outside AutoPTU.

## Encounter dependency — Quarry Alternate Path

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/forced movement — BLOCKING if collapse, knockback or interception is active
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage — PARTIAL
- statuses — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- tactical AI — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:
Resolve route accessibility and route choice in the overworld, then instantiate a stable static battle map only if an encounter occurs.

## No-inference rule

The `Simple` hook proves one post-combat-stage Ability reaction path. It does not promote general reactions, Abilities, statuses, Items or Trainer Features to complete. Accessibility work in the narrative repository does not create new combat mechanics.