# Engine Readiness Snapshot — Pass 72

Status: implementation evidence snapshot. Not canon.

## Read-only sources inspected

AutoPTU-Java head: `6beb908f4246eb9f2e94161e3e28e4044be8fa92`

AutoPTU Python head: `e0ac73ba33750e8f214cc7951ee4f4e237070dd0`

Narrative repo pre-pass head: `b0959751dedb5b315c0862e50762ba247c65bd7c`

## New Java evidence since Pass 71

Two new commits materially extend the live StatusController/held-item slice:

- `343ff74d068cf42a7db83ad706cff03117a9fbd5` ports a generic held-item START temporary-effect resolver, freezes the representative effect-family contract and gates it against Python oracle parity.
- `6beb908f4246eb9f2e94161e3e28e4044be8fa92` extends generic held-item START calculation effects, freezes additional families and adds tests for the expanded contract.

This is concrete evidence that more held-item START behavior now participates in the Java parity effort rather than existing only as a future interface.

It strengthens PARTIAL evidence for:

- items;
- status lifecycle;
- full turn/round lifecycle.

It does not prove:

- the full held-item registry;
- every START/END item hook;
- item consumption or all stateful item behavior;
- all statuses;
- full damage resolution;
- move/ability/Trainer Feature hooks;
- reactions;
- tactical AI;
- adapter/playback.

The live Java README still explicitly lists the following as pending:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- semantic battle-event emission and full `BattleSpec -> BattleTranscript` parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Python evidence

AutoPTU Python head `e0ac73ba33750e8f214cc7951ee4f4e237070dd0` contains recent Career work preserving selected Trainer appearance across creation. Adjacent recent work adapts battle rendering quality to raster workload while explicitly preserving combat authority.

This improves persistence/presentation. It is not evidence of a newly completed tactical rule family in Java.

## Permanent capability map

### targeting / footprints / range / LoS

Status: VERIFIED

Java still has explicit range, area, footprint, target-anchor and line-of-sight contracts integrated into the deterministic action-space layer.

### base movement legality

Status: VERIFIED

Shift/Jump legality, Overland/Swim/Sky handling, terrain costs, blockers, Wallrunner, sprint and landing-fit predicates remain implemented.

This category excludes forced movement and interception.

### complete movement including push / pull / knockback / interception / forced movement

Status: BLOCKING

The live Java README continues to list forced movement as pending. No procurement encounter may assume escort/interception/knockback-sensitive cargo behavior is authoritative.

### core calculations

Status: VERIFIED

Damage Base, type-effectiveness, stages, accuracy-stage calculations, weather DB primitive, crit probability, Burn and modifier/rounding primitives remain implemented.

Calculation primitives do not imply full battle-system completion.

### action economy / initiative

Status: VERIFIED

Typed turn flow, phase sequence, action budget, deterministic initiative, Trick Room/League ordering and declared-action ordering remain present.

### full turn / round lifecycle

Status: PARTIAL

The phase-envelope work from Pass 71 is now joined by parity-gated held-item START effect families. This is stronger lifecycle evidence, but full combat state, complete StatusController behavior and semantic transcript parity remain unfinished.

### full stateful damage pipeline

Status: PARTIAL

Core calculations exist, but the README still explicitly marks full damage resolution as pending.

### status lifecycle

Status: PARTIAL

The shared phase envelope is wired live and additional held-item START temporary effects now have parity coverage. The complete StatusController and complete status behavior set remain unfinished.

### terrain / weather / hazards / zones / reactions

Status: BLOCKING

A weather calculation primitive exists. The tactical environment/controller families remain incomplete, with terrain, hazards and reactions explicitly pending.

### move-specific behavior

Status: PARTIAL

Representative infrastructure exists, while the full move hook registry remains pending.

### abilities

Status: PARTIAL

Representative calculations/effects do not establish full Ability coverage. The hook registry remains pending.

### items

Status: PARTIAL

Pass 72 has stronger evidence than Pass 71 because generic held-item START temporary/calculation effect families are now parity-gated. No promotion is justified because the live README still lists the item hook registry as incomplete and representative START families do not prove all item behavior.

### Trainer Features / perks

Status: PARTIAL

Focused Training/Chronicler Accuracy slices remain concrete evidence. The complete perk/Trainer Feature registry is still pending.

### AI legal-action infrastructure

Status: VERIFIED

Deterministic legal-choice generation remains implemented for Shift, direct targets, SELF/FIELD, tile-AoE, footprints, LoS and action-budget filtering.

### AI tactical policy

Status: BLOCKING

AI scoring/policy remains explicitly pending.

### Minecraft / Cobblemon / Craftics adapter and playback

Status: BLOCKING

AutoPTU-Java still explicitly identifies itself as a Java rules library rather than a Minecraft mod. The adapter remains future work after a parity-safe vertical slice.

## Pass 72 encounter consequences

### Supplier Yard Transfer Under Pressure

The intended full encounter requires:

- BLOCKING complete movement/interception/forced movement if cargo or workers move tactically;
- BLOCKING terrain/hazards/zones/reactions if unsafe yard lanes change during combat;
- BLOCKING AI tactical policy for protect/withdraw/territorial objectives;
- BLOCKING Minecraft/Cobblemon/Craftics adapter/playback to persist which cargo physically moved;
- PARTIAL lifecycle/damage/status/moves/abilities/items/Trainer Features for the normal battle-rule families.

Reduced version:

Workers secure cargo and leave the tactical area before battle. AutoPTU receives a static conventional arena. Procurement/Courier resumes the transfer after the authoritative battle result. Battle victory does not create receipt, acceptance, payment or ownership transfer.

### Installation Window Interrupted

The intended full encounter requires:

- BLOCKING complete movement for technician withdrawal/interception-sensitive routing;
- BLOCKING environment/hazard/zone/reaction support for active site conditions;
- BLOCKING tactical AI for CLEAR_ROUTE/PROTECT/WITHDRAW goals;
- BLOCKING adapter/playback to preserve installation-stage state through a battle.

Reduced version:

Technicians evacuate and work pauses in world state before battle. Dynamic machinery, installation progress and protected assets remain outside AutoPTU. A static conventional battle resolves the threat, after which the owning technical/Maintenance system determines whether work can resume.

## Procurement-system mechanical boundary

The Pass 72 procurement layer normally requires no AutoPTU mechanics.

Procurement may reference:

- a mechanical item requested by an institution;
- an item or material batch with provenance;
- a workshop commission;
- a repair/install project;
- an accepted delivery;
- an authoritative battle result when a threat interrupted fulfillment.

Procurement state must never itself grant or modify:

- item battle effects;
- held-item timing;
- Move legality;
- Ability effects;
- Trainer Features;
- accuracy;
- damage;
- initiative;
- action budget;
- movement;
- statuses;
- terrain/weather effects;
- AI priorities.

The new Java held-item START work is especially important as a guardrail: it proves some item families, not the whole category. A supplier delivering a mechanically defined item does not make that item's complete battle behavior adapter-ready. Exact item support still requires direct verification of the relevant Java contracts/tests.

## Promotion decision

No permanent capability category is promoted in Pass 72.

Qualitative evidence changed in one place: Items, status lifecycle and full turn/round lifecycle have stronger PARTIAL evidence because additional held-item START effect families now have explicit Java implementation and Python parity gates.

## Open mechanical questions

- Which held-item START families are still missing after `6beb908f`?
- When will held-item END, consumption and other stateful item paths be parity-complete?
- When will the full StatusController be considered complete rather than representative/live slices?
- Which Move/Ability/Item/Trainer Feature registries will be ported next?
- When will forced movement/interception become authoritative?
- What objective semantics will exist for PROTECT, ESCAPE, WITHDRAW, CLEAR_ROUTE or moving cargo?
- What is the first parity-safe Minecraft/Cobblemon/Craftics adapter slice?
- Which physical world-state events will BattleTranscript/playback own versus leave to overworld systems?

Until live tests/contracts answer these, Pass 72 rich encounters must retain their reduced versions.