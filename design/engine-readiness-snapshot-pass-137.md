# Engine Readiness Snapshot — Pass 137

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records live AutoPTU-Java and AutoPTU evidence relevant to the textile, garment, uniform and wearable-material concepts added in Pass 137. Both engine repositories remain read-only for this task.

A representative mechanic never promotes an entire capability family by itself.

## Inspected heads

AutoPTU-Java:

`28f141be5471e23f660fb2cda09bab02244ee62e`

Latest inspected commit:

`Run pre-damage reactions in authoritative move pipeline (#167)`

This slice runs the currently supported pre-damage reaction composition inside the authoritative Move pipeline and tests ordering in the live runtime. It follows Pass 136 evidence where threatened-area geometry was derived from authoritative state.

AutoPTU Python:

`01a9b1c70af504b77f5b8441f7283d5957987190`

Latest inspected Python commit:

`Career: default compact touch battles to Light Mode (#75)`

This changes Career rendering defaults while preserving authoritative battle mechanics. It does not alter the tactical classifications below.

## PTU wearable/Fashionista evidence boundary

Public PTU material confirms Fashionista is a real Trainer Class and that clothing/equipment recipes can have exact mechanical effects within that rules family.

That is a reason for stronger separation, not permission to generalize.

Pass 137 does not assume Java parity for:

- the Fashionista class catalog;
- Fashionista recipes;
- Accessories;
- Armor;
- equipment slots;
- clothing-based Evasion/Save effects;
- environmental protection from garments;
- Pokémon cosplay/outfit mechanics.

Ordinary narrative clothing remains non-mechanical unless an explicit validated `mechanical_rule_ref` exists.

## Java README boundary

The current AutoPTU-Java README still explicitly lists as unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The new pre-damage reaction slice narrows one path but does not override this repository-level boundary.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

Substantial parity-backed targeting geometry exists.

This geometry cannot be reused to infer clothing fit, fabric size, garment coverage or uniform recognition.

### base movement legality — VERIFIED

Ordinary Shift legality remains verified for the ported scope.

A coat, uniform, costume or fit observation does not modify movement unless an exact PTU rule does so.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

Narrow reaction movement and Push/Pull instruction parsing/exposure exist, but complete generic forced movement/interception remains unfinished.

Pass 137 FULL encounters therefore cannot rely on moving civilian custodians, live escorts or route-control objectives inside battle.

### core calculations — VERIFIED

Core calculation primitives remain verified for the ported scope.

Textile wear, fit, warmth, durability, provenance and conservation are not battle calculations.

### action economy/initiative — VERIFIED

Action budget and initiative infrastructure remain verified.

Changing clothes, repairing garments or issuing uniforms does not consume battle actions unless an exact PTU mechanic says so.

### full turn/round lifecycle — PARTIAL

Round/lifecycle slices, delayed effects, temporary effects and selected reaction paths exist.

The complete lifecycle remains unfinished.

### full stateful damage pipeline — PARTIAL

The latest Java slice integrates supported pre-damage reactions into the authoritative Move pipeline.

The README still marks full damage incomplete.

Narrative clothing cannot intercept damage, reduce DB or create shields without an exact verified equipment effect.

### status lifecycle — PARTIAL

Selected application/prevention/suppression/timing paths exist.

Clothing cannot prevent Burned, Frozen, Poisoned or other Status by description alone.

### terrain/weather/hazards/zones/reactions — BLOCKING

Reaction implementation is progressing, including an authoritative pre-damage path.

The combined family remains incomplete. Garments do not create safe zones, weather protection, reaction windows or environmental immunity by narrative declaration.

### move-specific behavior — PARTIAL

Representative Move paths exist, but catalog coverage remains incomplete.

Any garment-related scene invoking a specific Move still depends on exact parity evidence for that Move.

### abilities — PARTIAL

Individual Ability families have growing concrete evidence.

Leavanny, Wooloo, Burmy or another species having relevant Pokédex behavior does not execute an Ability effect unless the rules explicitly define one.

### items — PARTIAL

This is the most important battle-family boundary for Pass 137.

Item/equipment coverage is incomplete. A garment may exist physically and visually without being an AutoPTU item. If a future garment maps to Armor, Accessory, Held Item or other equipment, that exact rule and Java behavior must be validated.

### Trainer Features/perks — PARTIAL

Generic Feature infrastructure and selected effects exist, but catalog coverage remains incomplete.

Fashionista is a real PTU class. That does not prove Java execution parity for its recipes or Features.

### AI legal-action infrastructure — VERIFIED

Legal battle-choice construction/filtering exists for the ported scope.

It does not understand garment custody, securing historical textiles, staff evacuation or credential confusion as tactical goals.

### AI tactical policy — BLOCKING

No complete objective-aware policy exists for Pass 137 goals such as:

- `PROTECT_CUSTODIAN`;
- `CLEAR_ROUTE`;
- `WITHDRAW`;
- `EVACUATE_WORKSHOP`;
- `SECURE_OBJECT`;
- `REACH_EXIT`.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

No parity-safe adapter exists.

Minecraft must not infer from skins, armor slots, models or textures:

- PTU equipment state;
- Fashionista effects;
- credentials;
- employment;
- authority;
- material provenance;
- garment condition;
- weather protection;
- Pokémon consent.

## Pass 137 encounter dependencies

### Heritage Garment Transfer — FULL

Requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for live custodian movement/interception;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL if exact mechanics invoke it;
- terrain/weather/hazards/zones/reactions — BLOCKING when an environmental/reaction requirement exists;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL if the garment has a mechanical equipment role;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED:

Complete or pause custody in world state. Remove the historical garment and civilian custodians from the grid. Freeze a static arena and resolve only actual combatants. Resume transfer/provenance afterward.

### Festival Costume Workshop Interruption — FULL

Dynamic staff evacuation/workspace protection requires complete movement, AI tactical policy and adapter/playback. Environmental families enter only if an exact tactical hazard exists.

REDUCED:

Stop work and secure garments in world state. Evacuate staff. Use a static combat arena if a confrontation remains. Production completion is resolved afterward.

### Uniform Mix-Up at Field Station

Primarily non-combat.

Identity, employment and authority are resolved through Identity/Workplaces/Credentials. A separate static battle can use currently verified basics if needed. Battle victory cannot resolve institutional identity.

## Pass 137 world-system blockers

The narrative layer now identifies these non-battle implementation contracts as needed before full Minecraft realization:

- `TEXTILE_BATCH_PROVENANCE`;
- `WEARABLE_ITEM_IDENTITY`;
- `GARMENT_REVISION_HISTORY`;
- `FIT_AND_ALTERATION_STATE`;
- `CARE_AND_REPAIR_HISTORY`;
- `UNIFORM_PATTERN_HISTORY`;
- `UNIFORM_ISSUE_ASSIGNMENT`;
- `POKEMON_WEARABLE_AGENCY_HANDOFF`;
- `WEARABLE_TO_MATERIAL_CULTURE`;
- `WEARABLE_TO_MANUFACTURING`;
- `WEARABLE_TO_SUPPLY_CHAIN`;
- `WEARABLE_TO_MARKET`;
- `WEARABLE_TO_CREDENTIALS`;
- `WEARABLE_TO_MUSEUMS`;
- `WEARABLE_TO_MINECRAFT_PROJECTION`;
- `WORLD_WEARABLE_TO_BATTLE_ITEM_PROJECTION`.

These belong outside the battle core except for the final explicit projection of a validated mechanical item.

## Unresolved mechanics/canon questions

- Which textile fibers/materials actually exist in Ouros at campaign start?
- Are Wooloo-derived textiles or other Pokémon-derived materials part of regional canon, and under what agency/care rules?
- Which institutions have authored uniforms?
- Which wearable traditions are ordinary fashion, professional dress, festival costume or historical artifact?
- How are Pokémon wearables consented to, removed and stored?
- Which PTU/Caelo Fashionista, Armor, Accessory and clothing rules are in the final project ruleset?
- Which of those exact mechanics have Java parity?
- How should cosmetic-only Minecraft clothing remain visibly distinct from authoritative PTU equipment?

The complete Caelo corpus was not reliably available in this runtime. Super PTU Online Helper was not exposed as an invokable capability. No missing rule is filled by invention.