# Engine Readiness Snapshot — Pass 168

Status: evidence snapshot for narrative dependency planning. Not a rules source and not canon.

Date: 2026-08-25

Narrative focus: archaeological chronology, dating, calibration and stratigraphic sequence.

## Read-only engine evidence inspected

AutoPTU-Java main head inspected: `3d9be13bfd3c89361e58c35e2df6a3265b57f93b` — `Preserve move-special effect-roll temporary state (#198)`.

Recent Java work now includes generic move-special effect-roll modifiers and temporary-state preservation around those rolls, after earlier PRE_DAMAGE, POST_DAMAGE and END_ACTION runtime bridges. This is meaningful evidence for a narrow portion of move-special ordering and state ownership.

It does not demonstrate a complete Move catalog, complete Abilities/Items/Trainer Features, full Status lifecycle, generic reactions, forced movement, tactical AI or Minecraft integration.

AutoPTU-Java README still explicitly leaves these major families incomplete:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- remaining move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

AutoPTU Python main head inspected: `bae915ff074e1c39d05dd2fa7ab88655bf92ab60` — Career replay-timer cleanup. Its commit message explicitly preserves canonical combat behavior. It does not change battle-readiness classification.

## Permanent capability map

`VERIFIED`

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

`PARTIAL`

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

`BLOCKING`

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No category is promoted in Pass 168.

## Why Pass 168 is mostly engine-independent

Archaeological dating is a world-state evidence workflow. Relative sequence, sample provenance, date intervals, calibration revisions and historical interpretation do not require AutoPTU.

The battle engine becomes relevant only when an excavation, archive transfer or exposed site produces a separate confrontation.

A battle transcript can support facts such as `the route was cleared` or `the PCs won the confrontation` when the encounter contract allows it. It can never determine:

- sample age;
- context age;
- construction date;
- whether a material was reused;
- whether a context was redeposited;
- calibration choice;
- which historical interpretation is correct.

## Encounter dependency matrix

### Sealed Context Evacuation — FULL

Targeting/footprints/range/LoS: VERIFIED if ordinary combat occurs.

Base movement legality: VERIFIED for ordinary legal shifts.

Complete movement: BLOCKING. Required when researchers, custodians or wildlife must withdraw through threatened space, when interception matters, or when evacuation is a tactical objective.

Core calculations: VERIFIED for ordinary supported combat calculations.

Action economy/initiative: VERIFIED.

Full turn/round lifecycle: PARTIAL if the encounter relies on complete lifecycle state.

Full stateful damage pipeline: PARTIAL when damage is used.

Status lifecycle: PARTIAL for any actual Status effect.

Terrain/weather/hazards/zones/reactions: BLOCKING if unstable floors, collapse, dust, protected excavation cells or reaction movement have tactical meaning.

Move-specific behavior: PARTIAL whenever a specific Move beyond verified generic behavior matters.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features/perks: PARTIAL.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_RESEARCHER`, `CLEAR_ROUTE` or `REACH_EXIT` behavior.

Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version: resolve evacuation and archaeological closure in world state first. Use a static legal battle arena only if a confrontation remains.

### Sample Transfer Through Relic Passage — FULL

The battle-facing VERIFIED/PARTIAL categories are unchanged.

Complete movement: BLOCKING for moving custody objectives or interception.

AI tactical policy: BLOCKING for `PROTECT_CUSTODIAN`, `REACH_DESTINATION`, `WITHDRAW` or objective-preserving behavior.

Adapter/playback: BLOCKING.

Environment family: BLOCKING only if the passage changes tactically during the confrontation.

REDUCED version: complete custody handoff outside combat. Battle occurs before departure or after the sample has been secured.

### Stratigraphic Collapse After Storm — FULL

Complete movement: BLOCKING for evacuation and safe-route objectives.

Terrain/weather/hazards/zones/reactions: BLOCKING if collapse, falling, unstable ground, dust, debris or restricted cells alter legal tactical state.

AI tactical policy: BLOCKING.

Adapter/playback: BLOCKING.

Any Status, Ability, Item, Trainer Feature or Move-specific interaction remains PARTIAL unless an exact current contract is verified.

REDUCED version: Crisis/Archaeology resolves collapse state, documentation and evacuation outside battle. AutoPTU receives an adjacent static arena with no custom environmental rules.

### Which Date Belongs to the Temple? — NON-COMBAT

No battle-engine family is required. Archaeology, Metrology, Languages, Museums and Science can resolve or leave the chronology `UNRESOLVED` entirely through world state.

## Recent Java evidence must not be over-generalized

The current head preserves temporary state for move-special secondary-effect rolls. This does not prove:

- all secondary effects exist;
- all effect-roll modifiers are ported;
- all Status applications are correct;
- all Ability interactions are correct;
- all Trainer Feature interrupts exist;
- complete reaction dispatch exists;
- arbitrary archaeological environmental effects can be represented as battle hooks.

Likewise, verified battle LoS cannot be reused as archaeological visibility, excavation coverage or dating certainty.

## Pass 168 world-state blockers

These are narrative/runtime implementation questions outside AutoPTU battle parity:

- persistent chronological-question state;
- relative-order constraint graph;
- context-integrity assessment;
- dating-attempt and sample provenance;
- reference chronology/calibration revisions;
- date-estimate revision history;
- sample-to-event linkage;
- chronology assessment versioning;
- handoff to Archives/Museums/Public Memory;
- privacy/access controls for restricted or sacred sites;
- Minecraft projection of phase/revision state without inferring chronology from blocks.

## Mechanical guardrails

Do not create archaeological Skill DCs, dating bonuses, instant analysis, sample timers, puzzle-solving bonuses, supernatural age sensing, exact calendar dates from Occult Education, or Minecraft block-age inference.

PTU 1.05 publicly allows Occult Education to matter for magical ancient ruins in some campaigns, while explicitly allowing ruins to be mundane in others. That campaign-dependent Skill framing is not a chronology engine.

Caelo-specific archaeology/dating rules were not recovered reliably in this pass. Super PTU Online Helper was not available as an invocable capability. No output from either is invented.

## Promotion decision

No permanent capability category changes state in Pass 168.
