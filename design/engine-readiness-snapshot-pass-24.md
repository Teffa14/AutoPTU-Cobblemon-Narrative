# Engine Readiness Snapshot — Pass 24

Status: implementation evidence snapshot for narrative authoring. Not canon. AutoPTU-Java and AutoPTU are read-only inputs for this task.

Inspected date: 2026-08-19

## Live revisions inspected

Latest inspected AutoPTU-Java commit:

`a735d66c8bf19c5fdda712b4fce4773e6f0ee3d4` — Record authoritative move damage history (#51).

New Java evidence since Pass 23:

- `a735d66c8bf19c5fdda712b4fce4773e6f0ee3d4` connects ordinary resolved Move outcomes to server-owned round damage history, records actual HP loss rather than nominal overflow damage, preserves zero-damage hit history, shares the same history object with the round controller, and adds Python-oracle parity fixtures/tests.

Relevant immediately prior evidence remains:

- `28d49949b63f2e675680356e650ac5b04e0c5c6b` — round injury-history rotation with lifecycle hooks and Python parity.
- `53d9a7b521fb398e28984334e9aa2a9a33d98db0` — round damage-history rotation with lifecycle hooks and Python parity.
- `62e6bef9e45b2e30febb48b4b6b73927c36328c0` — delayed hits bound to canonical attacker/move/target inputs.
- `6111b6c5bcda851a1015ddc3ac4d5b578edc2c10` — authoritative delayed-hit scheduling and due/future partitioning.
- `6c357d59061be2eae7bbbb85f401750acd7cf686` — payload-bearing temporary-effect state.
- `6570d95ac874bc26bc6bcc8ffe64d007bba37e34` — authoritative lifecycle hook registry.
- `046cc9f97ed8893e97674222f80789afcdf2cc7f` — pre-damage Move hooks with parity-backed Mega Launcher slice.
- `1757163fe793335e24a17769ee0fdfb78e87c754` — authoritative held-item state and parity-backed Pink Pearl damage hook.
- `7b0fac33d139d8bd72b265aa00bb939e895d5a9a` — ordered damage-hook registry with representative Burn behavior.
- `63110d03ada723f41a671137a945e8f7b0316198` — authoritative round lifecycle controller with Python parity.

Latest inspected Python AutoPTU commit:

`01e5c98b2825b433631ff8e913e56b0eadb251e2` — merge of Career browser-local unranked persistence work.

Recent Python commits inspected are Career/runtime persistence changes. They do not establish additional battle-family readiness for this pass.

## Permanent capability classification

### VERIFIED

#### targeting/footprints/range/LoS

Canonical target anchors, target modes, footprints, range and LoS have explicit action-space/test evidence.

#### base movement legality

Verified for the ported Shift/Jump legality slice, supported movement modes, terrain costs/blockers and landing-fit behavior.

This excludes push/pull, knockback, interception and forced movement.

#### core calculations

Verified for explicitly ported primitives including Damage Base tables, type-effectiveness steps, stages, selected accuracy/crit/weather calculations, Burn calculation slices, modifiers and rounding points.

Weather calculation primitives do not establish battlefield Weather state.

#### action economy/initiative

Typed phases, action budget and deterministic initiative/League/Trick Room/declaration ordering have direct evidence.

#### AI legal-action infrastructure

The engine can enumerate deterministic legal choices for supported movement and target modes with action-budget filtering.

This proves legality infrastructure only.

### PARTIAL

#### full turn/round lifecycle

This category gains another useful integration point in Pass 24.

Verified slices include:
- authoritative round controller;
- lifecycle hook registry;
- temporary-effect cleanup and payload state;
- delayed-hit scheduling and canonical binding;
- round damage-history rotation;
- round injury-history rotation;
- ordinary Move resolution writing into the same authoritative damage history consumed by lifecycle state.

It remains PARTIAL because complete effect execution, duration semantics, every trigger family and full BattleSpec -> BattleTranscript parity are not established.

#### full stateful damage pipeline

This category is stronger than Pass 23 because the ordinary Move-application path now records actual HP loss into authoritative history and Python parity verifies that history contract.

Existing evidence also includes calculation primitives, ordered hooks and representative Burn/Mega Launcher/Pink Pearl paths.

It remains PARTIAL because full end-to-end resolution and all modifier/trigger sources are not verified.

#### status lifecycle

Burn and lifecycle/injury infrastructure provide real slices.

Still PARTIAL because the complete status controller, saves, durations and cross-status interactions are not ported.

#### move-specific behavior

Canonical Move state, selected hooks, delayed-hit scheduling/binding and damage-history integration exist.

Still PARTIAL. Representative Move behavior does not establish the complete Move library.

#### abilities

Mega Launcher has parity-backed authoritative hook evidence.

Still PARTIAL because the complete Ability registry and behavior set are not established.

#### items

Held-item state and Pink Pearl provide an authoritative representative item path.

Still PARTIAL because the complete item library and item hook families remain unverified.

### BLOCKING

#### complete movement including push/pull/knockback/interception/forced movement

The current Java README still lists forced movement/reactions among unfinished work. No inspected live evidence verifies this family.

#### terrain/weather/hazards/zones/reactions

This family is the principal blocker for Pass 24's rich seasonal encounters.

Current evidence includes calculation primitives that can mention weather and movement legality that can consume static terrain costs. That does not establish:
- authoritative battlefield Weather state;
- Weather creation/removal/duration;
- terrain transitions;
- hazard lifecycle;
- moving or timed zones;
- reactions;
- environmental Ability/Move interactions;
- adapter presentation of those states.

Remain BLOCKING.

#### Trainer Features/perks

The Java README still lists perk/Trainer Feature registries among unfinished work.

Lifecycle hooks do not prove Trainer Feature behavior.

#### AI tactical policy

Legal action generation exists. Tactical scoring/policy over legal choices remains unfinished.

This blocks encounters where wild groups should prefer escape, migration, zone control, protection or another objective over ordinary defeat-oriented behavior.

#### Minecraft/Cobblemon/Craftics adapter/playback support

AutoPTU-Java remains a standalone Java rules core. The current README explicitly says Minecraft/Cobblemon/Craftics should consume it later and lists the adapter as unfinished.

## Pass 24 seasonality implications

The seasonality system itself can advance as world-state data without tactical environmental support:

- world calendar;
- region-specific seasonal cycle;
- daylight/time-band projection;
- phenology patterns;
- observations and anomaly claims;
- seasonal route variants;
- NPC/service schedules;
- recurring-event windows;
- agriculture windows;
- wild-collective expected migration windows;
- public information and research datasets;
- offline coarse transitions;
- Minecraft visual-variant requirements as future adapter contracts.

The following must not be promoted to tactical mechanics yet:

- cold/heat damage;
- snowfall or rain as PTU Weather;
- ice/sliding movement;
- weather-driven Accuracy or Damage changes;
- wind displacement;
- seasonal hazard zones;
- dynamic flooding/freezing grids;
- seasonal Ability triggers unless independently implemented;
- environment-aware AI policy.

## Pass 24 encounter dependency table

| Encounter | Full-version key dependencies | Current readiness | Reduced version |
|---|---|---|---|
| Frostline Crossing | terrain/weather/hazards/zones/reactions; optional forced movement if sliding matters; lifecycle; tactical AI; adapter playback | BLOCKING overall | seasonal overworld visuals/access + reviewed static grid + ordinary legal battle |
| Migration Corridor Bottleneck | non-DEFEAT objective support; complete movement/interception where needed; AI tactical policy; adapter; ordinary battle families | BLOCKING overall | routing solved in overworld; standard encounter with one subgroup; world writeback after legal result |
| Storm-Season Relay | battlefield Weather/hazards; lifecycle timing; ACTIVATE_OBJECT/PROTECT objective; tactical AI; adapter playback | BLOCKING overall | storm visual/world-state only; relay interaction outside grid; standard static battle if conflict occurs |

## New damage-history evidence and non-inference

The latest commit matters for future seasonal/boss mechanics because many reactions, Features and AI policies may eventually inspect recent damage.

It does not prove those downstream systems.

Do not infer:
- reactions from damage history;
- Trainer Features from lifecycle visibility;
- tactical AI from state being available;
- full damage pipeline from ordinary Move history recording;
- environmental damage from damage-history infrastructure;
- Weather support from calculation helpers;
- Minecraft playback from server-owned state.

## Current source-of-truth boundary

Python `Teffa14/AutoPTU` remains the behavioral oracle while Java parity is incomplete.

The narrative repository may author seasonal world state, desired encounters and reduced implementations. It must not recreate missing PTU environmental rules in Minecraft scripts, Cobblemon hooks or narrative code.