# Engine Readiness Snapshot — Pass 175

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-01

## Read-only heads inspected

AutoPTU-Java main: `8e5204b19f4aa83d96c573635be52c6e0e9092a3`.
Head message: `Bind Shadow Tag through generic forced-movement step constraints (#312)`.

AutoPTU oracle head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.
Its latest visible work is Career/presentation state repair and viewport-coordinate synchronization; no newer tactical authority evidence was found in this pass.

Neither engine repository was modified.

## New Java evidence since the previous narrative readiness snapshot

PR #312 adds a reusable candidate-step constraint path inside forced displacement. Runtime temporary-effect state can project a constraint, and the shared displacement resolver checks each candidate anchor before applying the step. Shadow Tag is the currently demonstrated rule family. The commit also adds execution fixtures against the Python oracle and CI parity coverage for the final displacement outcome.

This is meaningful evidence for one composition path:
- server-owned temporary effect;
- projected forced-movement constraint;
- footprint-distance check;
- per-step displacement veto;
- oracle-checked execution result.

It does not prove complete movement as a permanent capability family.

## Permanent capability map used by Pass 175

VERIFIED for covered contracts:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING as complete families:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

## Why complete movement remains PARTIAL

The latest evidence verifies Shadow Tag candidate-step restrictions in forced displacement. It does not demonstrate broad parity for:
- all Push/Pull sources;
- all Knockback behavior;
- every Intercept rule and ordering interaction;
- arbitrary forced movement from Moves, Abilities, Items and Features;
- movement across all terrain/hazard interactions;
- simultaneous/multi-actor displacement;
- tactical escort/procession semantics;
- protected corridors;
- carried objects or actors;
- crowd movement;
- vehicle/platform movement;
- generalized movement reactions.

No permanent category is promoted in this pass.

## Pass 175 encounter dependency review

### Bruma Yard Measure Day — full scored exhibition

Potential full-version dependencies:
- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED;
- complete movement — PARTIAL if ring control/interception/forced movement is used;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL for round-scored/timed formats;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING if the opponent must optimize event-specific score/state;
- adapter/playback — BLOCKING as a complete family.

FULL status: BLOCKED/PARTIAL.

Reduced version:
An ordinary audited battle can be compiled after exact mechanic validation. Record comparison and “measure the change” presentation happen outside BattleSpec. No festival-only tactical rule is invented.

### Crossing Lantern Line — wild route interruption

Potential full-version dependencies:
- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED;
- complete movement — PARTIAL for retreat corridors/interception/push/pull/knockback;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL for sustained safe-passage objectives;
- full damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if crossing conditions matter tactically;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for corridor-control behavior;
- adapter/playback — BLOCKING.

FULL status: BLOCKED.

Reduced version:
Residents withdraw before battle compilation. Route state and evacuation remain narrative/world state. A separately audited ordinary battle may output only `IMMEDIATE_EVENT_ROUTE_CLEAR`.

### Sendero Open Day — noncombat route program

Core version uses:
- location discovery;
- quest objective state;
- existing claims/provenance;
- service dispatch;
- communication/public-memory state.

No tactical capability category is required unless an optional encounter is attached.

Status: READY at narrative-contract level, subject to the actual Minecraft interaction surfaces available in the writable RPG project; this pass does not claim the adapter family is complete.

### Tideglass Revision Night

Core version uses archive/public-memory/claim systems and dialogue/quest objectives. No battle capability required.

Status: READY at narrative-contract level.

## Adapter boundary

The festival design intentionally keeps battle semantics out of Minecraft/Cobblemon/Craftics.

Adapters may display:
- temporary stalls/signage;
- NPC schedules;
- crowds as presentation actors;
- event decorations;
- route markers;
- archive displays;
- quest interactions;
- battle playback after an authoritative result exists.

They may not decide:
- PTU movement legality;
- crowd buffs/debuffs;
- weather combat modifiers;
- ring-out legality;
- battle outcomes;
- historical truth;
- quest completion without server-owned objective state;
- public-memory revisions without canonical service writes.

## Promotion rule

Future movement-category promotion requires broad live tests/contracts for the family, not additional representative mechanics alone. The Shadow Tag work materially improves reusable forced-movement infrastructure, but Pass 175 keeps the permanent map unchanged.
