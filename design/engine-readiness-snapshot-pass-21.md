# Engine Readiness Snapshot — Pass 21

Status: implementation evidence snapshot for narrative authoring. Not canon. Read-only inspection of AutoPTU-Java and AutoPTU evidence.

Inspected date: 2026-08-19

## Live Java revision inspected

Latest inspected AutoPTU-Java commit:

`62e6bef9e45b2e30febb48b4b6b73927c36328c0` — Bind delayed hits to canonical move execution inputs (#48)

Immediate prior relevant evidence:

- `6111b6c5bcda851a1015ddc3ac4d5b578edc2c10` — authoritative delayed-hit scheduling state and due/future partitioning with Python parity.
- `6c357d59061be2eae7bbbb85f401750acd7cf686` — payload-bearing temporary effect state and round-cleanup parity.
- `6570d95ac874bc26bc6bcc8ffe64d007bba37e34` — authoritative lifecycle hook registry.
- `046cc9f97ed8893e97674222f80789afcdf2cc7f` — pre-damage move hooks, including a parity-backed Mega Launcher slice.
- `1757163fe793335e24a17769ee0fdfb78e87c754` — held-item state and parity-backed Pink Pearl damage hook.
- `7b0fac33d139d8bd72b265aa00bb939e895d5a9a` — ordered damage hook registry with Burn routed through it.
- `63110d03ada723f41a671137a945e8f7b0316198` — authoritative round lifecycle controller with Python parity.

## What the newest delayed-hit commit proves

The current Java runtime can bind an existing delayed-hit entry to:

- the canonical attacker;
- a move in that attacker's canonical moveset;
- a canonical combatant or tile target;
- the move's canonical action type.

The binding fails closed when a forged move or missing target is supplied, and the tests compare the contract with pinned Python-oracle calls.

This is valuable evidence that Minecraft/Cobblemon cannot substitute an arbitrary move or target when a delayed effect resolves.

## What it does not prove

The commit does not by itself establish:

- complete Future Sight or every delayed Move behavior;
- complete delayed-hit execution after binding;
- all status durations and save checks;
- all temporary-effect semantics;
- complete damage calculation;
- hazards, zones or reactions;
- forced movement or interception;
- objective-aware tactical AI;
- Minecraft event playback.

Do not promote a whole family because one representative delayed mechanic has a contract.

## Permanent capability classification

### VERIFIED

#### targeting/footprints/range/LoS

Evidence remains strong from canonical target anchors, direct/tile/Self/Field target handling, footprints, range and LoS tests used by the action-space contract.

#### base movement legality

Verified for the currently ported Shift/Jump legality slice including supported movement modes, terrain cost/blockers and landing-fit rules.

This does not include forced movement, push/pull, knockback or interception.

#### core calculations

Verified for the explicitly ported calculation primitives: Damage Base table, type-effectiveness steps, stages, accuracy, crit probability, supported weather DB calculation, Burn calculation slices and modifier/rounding primitives.

This does not make the end-to-end damage pipeline complete.

#### action economy/initiative

Typed phases, action budgets, deterministic initiative order, Trick Room/League ordering and declared-action ordering have direct tests and parity evidence.

#### AI legal-action infrastructure

The engine exposes deterministic legal choice/action-space infrastructure for movement and supported Move target modes with action-budget filtering.

Legal-action generation is different from tactical policy.

### PARTIAL

#### full turn/round lifecycle

Improved materially through the round lifecycle controller, lifecycle hook registry, temporary-effect cleanup/payload state and delayed-hit scheduling/binding.

Still PARTIAL because full effect execution, all durations, all hooks and full transcript behavior are not established.

#### full stateful damage pipeline

Damage primitives and an ordered hook registry exist, with representative Burn, Mega Launcher and Pink Pearl behavior.

Still PARTIAL because the full end-to-end stateful pipeline and all modifier families are not ported/verified.

#### status lifecycle

Burn has meaningful evidence and lifecycle infrastructure is growing.

Still PARTIAL because the complete PTU status controller, save checks, durations and interactions remain unfinished.

#### move-specific behavior

Canonical move state, selected move hooks and delayed-hit scheduling/binding exist.

Still PARTIAL. A delayed-hit binding contract is not the complete move library.

#### abilities

Mega Launcher is a parity-backed representative slice through an authoritative hook path.

Still PARTIAL. It does not establish the Ability registry/library.

#### items

Held-item state and Pink Pearl provide a real authoritative representative slice.

Still PARTIAL. The item library and all item hook families are not established.

### BLOCKING

#### complete movement including push/pull/knockback/interception/forced movement

The AutoPTU-Java README still groups forced movement and reactions with unfinished work. No current evidence verifies the family.

#### terrain/weather/hazards/zones/reactions

Calculation support for some weather-related math does not establish authoritative battlefield weather state, terrain transitions, hazards, zones and reactions. The family remains blocking for rich encounter authoring.

#### Trainer Features/perks

The Java README still lists perk and Trainer Feature hook registries among incomplete work. Representative damage hook infrastructure does not establish these content families.

#### AI tactical policy

Legal actions exist, but scoring/policy over legal `BattleChoice` lists remains explicitly unfinished.

#### Minecraft/Cobblemon/Craftics adapter/playback support

The Java repository explicitly states it is not a Minecraft mod yet and keeps the adapter after a parity-safe vertical slice. This remains blocking for production in-world battle execution.

## Narrative consequences for Pass 21

Antagonist concepts that depend only on world-state planning, knowledge, faction relations, escalation, defections and off-grid negotiation can advance in narrative design now.

The following tactical concepts remain reduced-only unless newer evidence appears:

- mid-battle surrender selected by AI;
- protect/escort/escape objectives;
- interception/body-blocking rules beyond normal footprint blocking;
- pursuit AI that values a defector over ordinary targets;
- dynamic objective switching;
- reaction-based zone control;
- forced movement around evidence or control points;
- hazard-driven risk evaluation;
- Minecraft playback of objective state.

Delayed-hit concepts may reference the new canonical scheduling/binding evidence, but each specific Move still requires exact PTU/Python/Java validation.

## Source authority boundary

Python `Teffa14/AutoPTU` remains the behavioral oracle while the port is incomplete.

Narrative research may identify desired encounter behavior. It must never implement a substitute PTU rule inside the narrative repository or Minecraft adapter.
