# Engine Readiness Snapshot — Pass 128

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. AutoPTU-Java and AutoPTU inspected read-only. No engine files changed by this task.

## Inspected heads

AutoPTU-Java main: `967b16237c6ea93a939bd4acbbe67da979885a60`

Recent Java slices:
- `967b1623` — Mirror Armor Combat Stage reflection with recursive prevention/reflection context and parity gate.
- `ba4d489c` — target-owned Combat Stage Ability prevention family.
- `554b97e4` — Flower Veil / Flower Veil [Errata] Combat Stage prevention.

AutoPTU Python main observed during this pass: `8cf78e737a85f3b57e786154cf0f5781c840624a`.

Recent Python commits are Career/deployment oriented and do not justify tactical capability promotion.

## Live Java README boundary

AutoPTU-Java remains a Java 21 battle-rules library, not the Minecraft mod. Python AutoPTU remains the oracle while parity work is incomplete.

The README marks these broad foundations as present:
- targeting, range, areas, footprints and LoS;
- base Shift/Jump legality;
- core PTU calculation primitives;
- typed turn/action budget;
- deterministic initiative;
- legal autobattler action-space generation.

It still lists major unfinished work for:
- core combatant/grid battle-state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Permanent capability categories

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

Recent Mirror Armor / Combat Stage prevention work strengthens specific Ability and mutation-order contracts. It does not verify the entire Ability family or broad reaction system.

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## Pass 128 overworld blockers

The museum layer introduces world-state concerns outside the battle core:
- `COLLECTION_INSTITUTION_STATE`
- `ACCESSION_AND_COLLECTION_MEMBERSHIP`
- `CATALOGUE_REVISION_HISTORY`
- `OBJECT_LOCATION_HISTORY`
- `CONDITION_AND_CONSERVATION_HISTORY`
- `EXHIBITION_PROJECT_STATE`
- `LOAN_AND_HANDOFF_STATE`
- `REPLICA_CAST_RELATIONSHIPS`
- `COLLECTION_RESEARCH_ACCESS`
- `DEACCESSION_DISPOSITION_REVIEW`
- `COLLECTION_TO_MINECRAFT_PROJECTION`

These should be server/world-state authorities. AutoPTU should consume only battle-relevant snapshots.

## Encounter dependency mapping

### Gallery Evacuation During a Collection Incident

REDUCED version can run with present VERIFIED foundations if evacuation, object security and wildlife movement are resolved before battle and the tactical area is static.

FULL version requires:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full lifecycle — PARTIAL
- full stateful damage — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if cases, broken glass, moving displays or protected zones are mechanical
- move-specific behavior — PARTIAL; individually verify
- abilities — PARTIAL; individually verify
- items — PARTIAL; individually verify
- Trainer Features/perks — PARTIAL; individually verify
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for EVACUATE/WITHDRAW/PROTECT_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

### Travelling Exhibit Handoff Chokepoint

REDUCED version can keep the exhibit shipment outside the tactical grid and use a conventional static battle.

FULL version requires:
- complete movement/interception/forced movement — BLOCKING
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING
- exact applicable lifecycle/damage/status/Move/Ability/Item/Feature families — PARTIAL where used

### Conservation Lab Shutdown

REDUCED version can perform the equipment shutdown and evacuate staff/fragile objects before battle.

FULL version requires:
- complete movement/interception — BLOCKING if technicians move in-grid
- terrain/weather/hazards/zones/reactions — BLOCKING for fire, chemicals, electricity, shattered glass or machinery zones
- AI tactical policy — BLOCKING for CLEAR_ROUTE/PROTECT_TECHNICIAN
- adapter/playback — BLOCKING
- exact Move/Ability/Item/Feature behavior — PARTIAL and individually verified

## Guardrails specific to museums

Do not infer:
- display-case geometry -> combat cover;
- glass -> hazard;
- hanging exhibit -> falling/swinging object mechanics;
- museum mineral/fossil -> terrain or field effect;
- conservation equipment -> battle interactable;
- collection custody -> legal battle item access;
- catalog label -> world truth;
- battle victory -> recovered ownership/custody;
- fossil-restoration machine -> generic item or environmental mechanic;
- living Fossil Pokémon -> museum property;
- Java targeting LoS -> gallery security visibility;
- AI legal-action enumeration -> evacuation/retrieval policy.

## PTU/Caelo questions

The complete primary Caelo corpus was not reliably available in this runtime. Super PTU Online Helper was not exposed as an invocable capability.

Open questions:
- Which exact PTU/Caelo rules govern Fossil Researcher and fossil restoration?
- Do any exact Features govern appraisal, conservation, archaeology or artifact handling?
- Which rules govern carrying fragile objects during combat?
- Which rules govern improvised objects, falling objects or broken terrain?
- Can any museum-related artifact have a mechanical effect, and under which authored data/rule contract?
- How should restored Fossil Pokémon obtain persistent identity, custody and agency state?

No mechanics were invented to answer these questions.
