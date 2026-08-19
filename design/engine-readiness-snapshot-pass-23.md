# Engine Readiness Snapshot — Pass 23

Status: implementation evidence snapshot for narrative authoring. Not canon. AutoPTU-Java and AutoPTU are read-only inputs for this task.

Inspected date: 2026-08-19

## Live revisions inspected

Latest inspected AutoPTU-Java commit:

`28d49949b63f2e675680356e650ac5b04e0c5c6b` — Port authoritative round injury history rotation.

New Java evidence since Pass 22:

- `53d9a7b521fb398e28984334e9aa2a9a33d98db0` — authoritative round damage-history rotation, exposed through lifecycle hooks and checked against the Python lifecycle oracle.
- `28d49949b63f2e675680356e650ac5b04e0c5c6b` — authoritative current/last/previous-round injury history, lifecycle-hook exposure and round-start rotation with Python parity.

Earlier relevant evidence remains:

- `62e6bef9e45b2e30febb48b4b6b73927c36328c0` — delayed hits bound to canonical attacker/move/target execution inputs.
- `6111b6c5bcda851a1015ddc3ac4d5b578edc2c10` — authoritative delayed-hit scheduling and due/future partitioning.
- `6c357d59061be2eae7bbbb85f401750acd7cf686` — payload-bearing temporary effect state.
- `6570d95ac874bc26bc6bcc8ffe64d007bba37e34` — authoritative lifecycle hook registry.
- `046cc9f97ed8893e97674222f80789afcdf2cc7f` — pre-damage move hooks and a parity-backed Mega Launcher slice.
- `1757163fe793335e24a17769ee0fdfb78e87c754` — held-item state and parity-backed Pink Pearl hook.
- `7b0fac33d139d8bd72b265aa00bb939e895d5a9a` — ordered damage-hook registry with representative Burn behavior.
- `63110d03ada723f41a671137a945e8f7b0316198` — authoritative round lifecycle controller with Python parity.

Latest inspected Python AutoPTU commit:

`8238201919f176c8c3923340dd9e887ca3be44f6` — Career: persist trainer appearance and validate creation flow.

The recent Python commits are Career-mode work. They do not by themselves alter battle-family readiness.

## Permanent capability classification

### VERIFIED

#### targeting/footprints/range/LoS

Canonical target anchors, target modes, footprints, range and LoS have explicit action-space/test evidence.

#### base movement legality

Verified for the ported Shift/Jump legality slice, supported movement modes, terrain costs/blockers and landing-fit behavior.

This excludes push/pull, knockback, interception and forced movement.

#### core calculations

Verified for explicitly ported primitives including Damage Base tables, type-effectiveness steps, stages, selected accuracy/crit/weather calculations, Burn calculation slices, modifiers and rounding points.

This is not the full end-to-end damage pipeline.

#### action economy/initiative

Typed phases, action budget and deterministic initiative/League/Trick Room/declaration ordering have direct evidence.

#### AI legal-action infrastructure

The engine can enumerate deterministic legal choices for supported movement and target modes with action-budget filtering.

This proves legality infrastructure only.

### PARTIAL

#### full turn/round lifecycle

This category is stronger than in Pass 22.

Verified slices now include:
- authoritative round controller;
- lifecycle hooks;
- temporary-effect cleanup and payload state;
- delayed-hit scheduling and canonical binding;
- round damage-history rotation;
- round injury-history rotation.

It remains PARTIAL because full effect execution, all duration semantics, all hook families, complete move/status interaction and full BattleSpec -> BattleTranscript parity are not established.

#### full stateful damage pipeline

Calculation primitives, ordered hook infrastructure and round damage-history state exist.

Representative Burn, Mega Launcher and Pink Pearl paths are meaningful evidence.

Still PARTIAL because every stateful modifier source and full end-to-end resolution are not verified.

#### status lifecycle

Burn and lifecycle/injury state provide real supporting infrastructure.

Still PARTIAL because the complete status controller, save checks, durations and cross-status interactions are not ported.

#### move-specific behavior

Canonical move state, selected move hooks and delayed-hit scheduling/binding exist.

Still PARTIAL. Representative behavior does not establish the full Move library.

#### abilities

Mega Launcher is parity-backed through an authoritative hook path.

Still PARTIAL because the complete Ability registry and behavior set are not established.

#### items

Held-item state and Pink Pearl provide one authoritative representative item path.

Still PARTIAL because the complete item library and item hook families remain unverified.

### BLOCKING

#### complete movement including push/pull/knockback/interception/forced movement

Current Java README still lists forced movement/reactions among unfinished work. No live evidence verifies this family.

#### terrain/weather/hazards/zones/reactions

Calculation support mentioning weather does not establish authoritative battlefield weather state, terrain transitions, hazards, zones or reactions.

#### Trainer Features/perks

Current Java README still lists perk/Trainer Feature registries among unfinished work.

General lifecycle/damage hooks do not prove Trainer Features.

#### AI tactical policy

Legal action generation exists. Tactical scoring/policy over legal choices remains unfinished.

#### Minecraft/Cobblemon/Craftics adapter/playback support

AutoPTU-Java explicitly remains a standalone Java rules core. Minecraft/Cobblemon/Craftics are intended to consume it later and remain blocking for production battle playback.

## Pass 23 housing implications

The housing system itself can advance almost entirely as world-state data:
- residence identity;
- household membership;
- access policy;
- resident routines;
- home Chronicle;
- move history;
- former residences;
- neighborhood graph;
- visitor state;
- public/private address state;
- physical repair state;
- provenance-bearing displays/storage references.

These do not need tactical battle support.

Mechanically rich home encounters must remain reduced where they depend on:
- escort/protect objectives;
- breakable/mutable structures;
- smoke/fire/hazard zones;
- forced movement through doorways/windows;
- interception/body blocking;
- tactical AI that protects or attacks objectives;
- Minecraft playback of mutable home state.

## Pass 23 encounter dependency table

| Encounter | Full-version key dependencies | Readiness | Reduced version |
|---|---|---|---|
| Courtyard Disturbance | tactical AI for territorial/withdrawal behavior; adapter playback; optional terrain state; ordinary battle families | BLOCKING overall | static reviewed arena; observation/retreat/occupancy remain overworld state |
| Moving Day Chokepoint | BREAK_THROUGH/PROTECT objective; complete movement/interception; tactical AI; adapter playback; ordinary battle families | BLOCKING overall | residents/cargo outside grid; normal legal battle at chokepoint |
| Damaged Rowhouse Evacuation | PROTECT/ESCAPE; hazards/zones/reactions; optional forced movement/interception; tactical AI; mutable Minecraft structure; ordinary battle families | BLOCKING overall | evacuation outside battle; hazards visual/world-state only; static legal battle if needed |

## New lifecycle evidence and non-inference

Round damage and injury history are useful future inputs for:
- abilities that inspect recent damage;
- Trainer Features that inspect injuries;
- tactical policy;
- phase/lifecycle rules.

They do not prove any of those downstream systems by themselves.

Do not infer:
- full injury mechanics from injury-history rotation;
- full damage resolution from damage-history rotation;
- tactical AI from state becoming available to future AI;
- Trainer Features from lifecycle hooks exposing injury state;
- reactions from hook infrastructure;
- Minecraft support from server-owned runtime state.

## Current source-of-truth boundary

Python `Teffa14/AutoPTU` remains the behavioral oracle while Java parity is incomplete.

The narrative repository may describe desired housing encounters and reduced implementations. It must not recreate missing PTU mechanics in Minecraft scripts or narrative code.
