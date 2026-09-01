# Engine Readiness Snapshot — Pass 172

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-01

## Read-only heads inspected

AutoPTU-Java main: `cc5522b72f63ad283153251db5fef4502b860db9`.
Head message: `Freeze combatant distance geometry for shadow tag (#311)`.

AutoPTU pinned oracle remains: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Neither engine repository was modified by this pass.

## Java evidence added since Pass 171

PR #311 freezes two additional geometry contracts from the Python oracle:

- `_combatant_distance_to_coord` in `battle_state.py`;
- `footprint_distance` plus the footprint-size mapping and Chebyshev metric in `targeting.py`.

The CI parity workflow now exports and tests these contracts alongside the existing forced-movement oracle fixtures.

This strengthens evidence for footprint-sensitive geometry used by Shadow Tag candidate-step validation.

It is still representative evidence, not complete family coverage.

No permanent capability category is promoted.

## Permanent capability map

VERIFIED
- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL
- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Why no promotion from PR #311

The new contracts prove additional geometry parity around one forced-movement/Shadow Tag path. They do not prove:

- all Push/Pull cases;
- general Knockback;
- every Intercept variant and ordering interaction;
- all status/Ability/Item/Feature displacement sources;
- arbitrary forced movement;
- terrain/weather displacement;
- escort/rescue semantics;
- protected-object carrying;
- vehicles/platforms;
- crowd routing;
- generalized reactions;
- objective-aware tactical policy.

## Pass 172 class-questline dependency review

### Supply Route Breakthrough

FULL: BLOCKED.

Potential dependencies:
- complete movement for breakthrough/escort/interception/forced displacement;
- full lifecycle for route-control objectives;
- terrain/weather/hazards/zones/reactions if route conditions alter tactics;
- exact Move/Ability/Item/Trainer Feature parity;
- AI tactical policy for route denial/protection;
- adapter/playback for semantic shipment/vehicle representation.

REDUCED: READY at narrative-contract level after individual combat audit.
The shipment remains outside BattleSpec. Allowed output: `IMMEDIATE_SUPPLY_ROUTE_CLEAR`.

### Field Research Perimeter

FULL: BLOCKED when researchers, samples, dynamic hazards or timed observations are tactical objectives.

Potential dependencies:
- complete movement if escort/intercept/displacement occurs;
- full lifecycle for sustained objectives;
- terrain/weather/hazards/zones/reactions;
- exact move/ability/item/feature behavior;
- AI tactical policy;
- adapter/playback.

REDUCED: READY at narrative-contract level after audit. Researchers and samples remain outside BattleSpec. Allowed output: `IMMEDIATE_FIELD_RESEARCH_PERIMETER_CLEAR`.

### Capture Intervention

FULL: PARTIAL/BLOCKED depending exact encounter.

Potential dependencies:
- targeting/footprints/range/LoS — VERIFIED as family baseline;
- base movement legality — VERIFIED;
- complete movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- status lifecycle — PARTIAL;
- move-specific behavior — PARTIAL;
- items, including capture item behavior — PARTIAL;
- Trainer Features/perks for Capture Specialist effects — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED: only exact capture/battle mechanics individually verified against current engine evidence may be used. Investigation, ecology and intervention decisions should resolve in narrative world state before compiling the tactical scene.

### Chronicler + Duelist Rival Battle

FULL ADVANCED VERSION: BLOCKED if the opponent must exploit replay history, player tendencies or semantic objectives through tactical policy.

REDUCED: ordinary audited battle can be READY when chosen Moves, Abilities, Items, Features and statuses are individually supported. Chronicler archives and rivalry history remain narrative inputs; they do not silently alter tactical AI.

## Class mechanics boundary

Pass 172 establishes narrative class arcs, not mechanical class implementation.

The read-only Trainer Class Validation currently lists 69 classes total, with 61 classes under `Missing Mechanics`, 23 ambiguous unlockable OR branches and no explicit multi-class mentions in that validation artifact.

Therefore:

- narrative coverage and engine implementation coverage must be tracked separately;
- a class can have a rich questline while its mechanics remain incomplete;
- a class quest cannot substitute for missing runtime mapping;
- respec-safe narrative history cannot preserve mechanical permissions after the authoritative build removes a class;
- every mechanical action must be revalidated against current PTU/Caelo and runtime evidence.

## Multiclass/respec engine boundary

The narrative architecture may store:
- current class references as read-only mirrors of authoritative progression state;
- historical class participation;
- completed class quests;
- NPC/faction relationships;
- knowledge and world consequences.

It may not decide or mutate:
- class legality;
- class prerequisites;
- Feature ownership;
- Skill Ranks;
- Edges;
- Moves;
- Abilities;
- combat permissions.

Those remain authoritative progression/runtime concerns.

## Adapter boundary

Minecraft/Cobblemon/Craftics may display class-linked NPCs, institutions, workshops, archives, kitchens, guild spaces, faction facilities, quest markers and aftermath.

It may not decide:
- current PTU class ownership;
- class respec results;
- quest completion;
- faction membership authority;
- battle outcomes;
- PTU rewards;
- world consequences.

## Promotion rule

Permanent capability categories change only when broad live tests/contracts prove the family. PR #311 materially strengthens geometry parity evidence but does not justify a category promotion.