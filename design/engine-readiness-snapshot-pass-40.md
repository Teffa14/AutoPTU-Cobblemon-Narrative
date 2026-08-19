# Engine Readiness Snapshot — Pass 40

Status: read-only evidence snapshot for narrative design. No changes are made to AutoPTU-Java or AutoPTU.
Date: 2026-08-19

## Repositories inspected

AutoPTU-Java head: `f0cc35560f7a0de3a9569475b7e08208a8692919`

Python AutoPTU head: `e4bb0ca38b7018710af476ce365d515a387de4e7`

Python remains the authoritative oracle while the Java port is incomplete.

## New Java evidence since Pass 39

Two relevant Java commits landed after the Pass 39 snapshot.

### Canonical trainer-state binding

Commit `cdf40a3e9780a3e0c2dbd470bd4485cdb04f2cf7` binds phase-scoped perk hooks to authoritative trainer state.

The slice adds or strengthens:
- authoritative Trainer Feature state;
- Trainer AP state;
- combatant -> controller binding;
- Feature derivation from canonical trainer state;
- Python-oracle contracts around controller and AP linkage;
- tests that exercise perk lifecycle through canonical trainer state.

This closes the specific Pass 39 caveat that the perk registry was operating from an explicit projected Feature list rather than canonical runtime ownership.

### Defense Mastery

Commit `f0cc35560f7a0de3a9569475b7e08208a8692919` ports a concrete `Defense Mastery` Trainer Feature through the authoritative perk lifecycle.

The slice includes:
- generalized metadata-bearing Trainer Feature events;
- a built-in Defense Mastery END-phase perk effect;
- default-lifecycle wiring;
- temporary-effect state written by the Feature;
- current-turn movement/shift state consulted by the Feature;
- controller identity retained in the emitted event;
- Python-oracle fixtures and Java parity assertions;
- fail-closed behavior when the canonical trainer does not own the Feature.

This is materially stronger Trainer Feature evidence than Pass 39.

## What this evidence does not prove

Trainer Features/perks remain PARTIAL.

Do not infer:
- full Trainer Feature catalog coverage;
- `Stat Mastery` parity;
- Orders;
- interrupts;
- reaction-triggered Features;
- all passive Feature hooks;
- movement Features;
- capture Features;
- social/non-combat Features;
- Chef, Rider, Athlete, Researcher, Medic or crafting Feature coverage;
- complete AP spending semantics across all Features;
- every interaction between Features, Items, Abilities, statuses, damage and movement.

One fully parity-tested Feature does not make the family complete.

## Java README boundary

The current AutoPTU-Java README still lists major work as unfinished, including:
- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The implementation has bounded slices inside some of these families. The README remains a useful conservative boundary against overclaiming completion.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

Caveats:
- base movement does not include complete push/pull/knockback/interception/forced movement;
- core primitives do not establish the complete stateful damage pipeline;
- legal-action enumeration does not establish strong tactical choice;
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

Java has typed phases, authoritative actor/phase state, ordered status/ability/perk phase families, turn/round cleanup, histories, delayed-hit infrastructure and multiple parity-tested effects. Full transcript coverage and every phase-trigger family are not complete.

#### Full stateful damage pipeline

PARTIAL.

Core tables/calculations and bounded runtime damage interactions exist. The repository still explicitly lists full damage resolution as unfinished.

#### Status lifecycle

PARTIAL.

There is direct evidence for bounded Flinch, Confusion/Strange Tempo, status metadata, status application prevention, ordered phase dispatch and round expiry. The complete catalog and all interactions are not implemented.

#### Move-specific behavior

PARTIAL.

Generic move infrastructure plus bounded special cases do not prove complete Move coverage.

#### Abilities

PARTIAL.

Java has concrete and registry-backed Ability slices, including phase behavior and status-prevention interactions. Complete Ability coverage is not present.

#### Items

PARTIAL.

Prior representative held-item slices exist. Complete item coverage is not proven.

#### Trainer Features/perks

PARTIAL, with stronger evidence than Pass 39.

Current evidence now includes:
- canonical trainer Feature ownership in runtime state;
- controller binding;
- AP state infrastructure;
- a phase-scoped perk registry;
- default lifecycle integration;
- a concrete Defense Mastery implementation;
- Python-oracle parity around that Feature.

Narrative rule:
A concept requiring `Defense Mastery` may cite that exact implemented slice when its full semantics match the encounter need. A concept requiring any other Trainer Feature remains mechanically unverified until that exact Feature is implemented and parity-tested.

### BLOCKING

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

These remain blocking for FULL versions that depend on them.

## Pass 40 finance/sponsorship boundary

Most finance world state does not require the battle engine.

Safe to model narratively now:
- funding sources;
- grants;
- sponsorship agreements;
- donations;
- payment commitments;
- payment receipts/provenance;
- restricted-purpose support;
- scholarship records;
- prize-pool provenance;
- public sponsor visibility;
- funding reviews;
- coarse financial exposure;
- relief-fund state;
- unresolved claims;
- qualitative institutional budget pressure;
- economic consequences of route closures, discoveries, events and service changes.

These records must not directly alter battle statistics.

Mechanics still requiring authored PTU/Caelo/Ouros validation:
- exact prices;
- exact Job rewards;
- event prize values;
- Trainer battle payments;
- salary values;
- grant amounts;
- discounts;
- insurance premiums;
- interest;
- debt enforcement;
- taxes;
- resale values;
- sponsor combat effects;
- item or Feature benefits purchased through a funding relationship.

## Encounter dependency — Grant Shipment Chokepoint

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL as used
- terrain/weather/hazards/zones/reactions — BLOCKING when route hazards are tactical
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL; exact required Feature must have direct parity evidence
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:
Keep the shipment outside the grid. Use a static legal battle to clear the chokepoint. Resolve delivery, receipt, custody and grant accounting in world state afterward.

## Encounter dependency — Sponsored Exhibition Interruption

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception — BLOCKING for crowd protection
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage pipeline — PARTIAL
- status lifecycle — PARTIAL as used
- terrain/hazards/zones/reactions — BLOCKING for dynamic venue safety state
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL; no sponsor-linked Feature is inferred
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protection/evacuation objectives
- adapter/playback — BLOCKING

REDUCED version:
Pause the show and evacuate through overworld logic. Run a conventional static legal encounter in a cleared area. Resume/cancel the event according to world state.

## Encounter dependency — Claims Survey at the Warehouse

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement — BLOCKING where moving rubble/interception is required
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage/status/moves/abilities/items — PARTIAL as used
- terrain/weather/hazards/zones/reactions — BLOCKING for unstable floor, machinery or protected zones
- Trainer Features/perks — PARTIAL; an exact technical/support Feature still needs direct evidence
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protected-work-zone objectives
- adapter/playback — BLOCKING

REDUCED version:
Complete the financial/evidence survey before combat. Move people and records to safety. Resolve any subsequent encounter as a normal static battle. Claim outcome remains an agreement/evidence decision rather than a combat reward.

## No-inference rules for finance encounters

- Sponsor funding does not grant combat bonuses.
- An expensive item is not mechanically stronger because it cost more.
- An insurer, grant provider or donor does not gain battle authority from funding.
- Losing a battle cannot automatically void a contract unless that exact condition was authored and valid.
- Winning a battle cannot automatically force payment.
- Financial stakes do not justify inventing escort/interception/hazard rules in Minecraft.
- A Trainer Feature is available only when the authoritative battle state proves the actor owns the exact implemented Feature.

## Python state

Python AutoPTU remains at `e4bb0ca38b7018710af476ce365d515a387de4e7` for this snapshot. Its recent changes remain Career/API-oriented and do not justify tactical family promotions.

## Pass 40 conclusion

The only material capability change since Pass 39 is stronger evidence inside Trainer Features/perks: canonical runtime ownership is now wired and Defense Mastery is a concrete parity-tested Feature.

The family remains PARTIAL.

No other permanent category is promoted.
