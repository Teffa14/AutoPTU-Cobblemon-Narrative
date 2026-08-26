# Engine Readiness Snapshot — Pass 180

Status: ENGINE EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-26
Narrative scope: Pokémon coloration, camouflage, mimicry and visual signaling

## Read-only engine heads inspected

AutoPTU-Java head inspected:

`b66fcb4dac909c2f44bf6caf54a15f8da82e3e0a`

Latest inspected slice:

`Add effective Accuracy stage projection primitive (#217)`

This slice adds a calculation primitive for effective Accuracy-stage projection and follows the previous Accuracy/Evasion stage work. It improves a narrow calculation boundary. It does not implement camouflage, concealment, visual detection, invisibility, Stealth policy, mimicry, perception AI or Minecraft appearance authority.

AutoPTU Python head inspected:

`ad9c202ec9e3982c6797bd38b14df8f647852fc9`

Its latest inspected change is Career validation work and does not change battle-readiness conclusions.

Python's Ability tracker records `Color Change` as implemented: when hit, the user changes Type to the triggering Move's Type. This is a specific battle Ability contract. It is not ecological color matching.

## Permanent capability map

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

A representative Ability, Status path, secondary effect, Combat Stage calculation or Move Special never promotes its whole family.

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions as a complete family
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

The current Java README still lists core combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, remaining hook registries, full transcript parity, tactical AI and Craftics/Cobblemon integration as incomplete.

## Pass 180 mechanics boundary

Coloration and camouflage are narrative/world-state systems unless an exact PTU mechanic is invoked.

Explicit prohibitions:

`background match -> Evasion bonus`

`camouflage -> Accuracy penalty`

`stillness -> invisible`

`masquerade -> surprise round`

`visual warning pattern -> Intimidate`

`dynamic hue shift -> Color Change Ability trigger`

`Kecleon ecological color shift -> Type change`

`Sudowoodo tree mimicry -> Grass Type`

`Foongus resemblance -> automatic lure mechanic`

`bright coloration -> Poisoned / fear / panic`

`appearance similarity -> Form classification`

`Minecraft skin / shader state -> biological appearance truth`

## Why battle LoS is insufficient

The VERIFIED LoS system answers whether a battle geometry permits a particular tactical relation.

Biological detectability can depend on:

- observer position;
- viewing direction;
- distance;
- light spectrum/intensity;
- substrate/background;
- movement or stillness;
- observer prior knowledge;
- body outline/pattern;
- camera characteristics;
- weather/visibility;
- whether the question is localization or identification.

Reusing battle LoS as camouflage science would silently invent rules.

## Encounter dependency matrix

### Concealed Subject Survey — FULL

Targeting / footprints / range / LoS: VERIFIED for any actual battle.

Base movement legality: VERIFIED.

Complete movement: BLOCKING if researchers or wildlife must cross, withdraw, reposition under interception or leave dynamically.

Core calculations: VERIFIED for ordinary battle calculations.

Action economy / initiative: VERIFIED.

Full turn / round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL if an exact Status is invoked.

Terrain / weather / hazards / zones / reactions: BLOCKING if substrate, light, fog, vegetation or concealment zones are expected to alter tactical legality/effects.

Move-specific behavior: PARTIAL.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features / perks: PARTIAL.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_RESEARCHER`, `REACH_OBSERVATION_POINT` and non-hostile wildlife behavior.

Minecraft / Cobblemon / Craftics adapter/playback: BLOCKING.

REDUCED contract:

Coloration and Visual Records resolve observation/detection outside battle. Researchers and non-hostile wildlife leave the battle area. AutoPTU receives a static legal arena with no camouflage modifier.

### Masquerade-Site Crowd Incident — FULL

Targeting / footprints / range / LoS: VERIFIED for an independent confrontation.

Base movement legality: VERIFIED.

Complete movement: BLOCKING for actual crowd evacuation, voluntary wild withdrawal and crossing under tactical pressure.

Core calculations: VERIFIED.

Action economy / initiative: VERIFIED.

Lifecycle / damage / Status / Move / Ability / Item / Trainer Feature families: PARTIAL when invoked.

Terrain / weather / hazards / zones / reactions: BLOCKING only if barriers, darkness, debris or visibility conditions are actual tactical mechanics.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `CLEAR_ROUTE`, `AVOID_WILDLIFE`.

Adapter/playback: BLOCKING.

REDUCED contract:

Public Space clears visitors through world state. The masquerading Pokémon may leave without becoming a combatant. A separate hostile encounter, if any, begins afterward on static geometry.

### Color-Shift Research Station Emergency — FULL

Targeting / footprints / range / LoS: VERIFIED for ordinary combat.

Base movement legality: VERIFIED.

Complete movement: BLOCKING for evacuation and mobile technicians.

Core calculations: VERIFIED.

Action economy / initiative: VERIFIED.

Lifecycle / damage / Status / Move / Ability / Item / Feature families: PARTIAL when used.

Terrain / weather / hazards / zones / reactions: BLOCKING if equipment failure, smoke, broken infrastructure or controlled-light zones have tactical effects.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `EVACUATE`, `PROTECT_TECHNICIAN`, `REACH_EXIT`.

Adapter/playback: BLOCKING.

REDUCED contract:

Research shuts the station down and removes all non-combatants before a battle snapshot. Appearance observations remain attached to their timestamps. No battle result explains the color shift.

### Was It Ever a New Form? — NON-COMBAT

No battle-engine capability is required.

Taxonomy, Evolution/Form, Seasonal Coverings, Visual Records, Care and Coloration compare evidence. A final state of `UNRESOLVED` is legitimate.

## Color Change evidence boundary

The Python oracle records a concrete `Color Change` Ability path that changes Type after being hit by a triggering Move.

Therefore:

- mechanical Color Change must be executed only through authoritative battle rules;
- ecological hue shifts do not call that Ability;
- the Ability firing does not create an appearance-history record unless an actual narrative observation separately exists;
- Kecleon's official flavor can support authored ecological observations while its PTU Ability retains independent mechanics.

## Other visually named mechanics

Any Ability, Move, Item or Feature with camouflage-, illusion-, color-, stealth-, concealment- or mimicry-adjacent wording remains subject to its exact PTU/Caelo contract.

Do not infer functionality from names.

Foundry/PTR2e material present inside AutoPTU is not automatically authoritative for PTU 1.05/Caelo.

## Minecraft adapter boundary

Minecraft/Cobblemon may eventually render:

- authorized texture/color revisions;
- an already-authored masquerade posture;
- display lighting;
- substrate context;
- known persistent individuals;
- visual observations already established by world state.

It must not derive:

- camouflage effectiveness from pixel similarity;
- species identity from texture;
- Form state from resource-pack variants;
- stealth success from invisibility flags;
- concealment from biome tint;
- warning function from bright coloration;
- individual identity from skin alone;
- population frequency from loaded entities.

## Engine changes observed since Pass 179

The newest inspected Java commit is `b66fcb4d...`, which adds effective Accuracy-stage projection. This follows the prior effective Accuracy/Evasion projection work.

This changes no permanent category classification for Pass 180.

The newest inspected Python head `ad9c202e...` is Career validation work and does not change tactical readiness.

## Unresolved mechanical questions

- whether Caelo changes Color Change, Illusion, Stealth, Perception or visually related Abilities/Features;
- whether PTU/Caelo has any explicit non-combat concealment rule that should be surfaced rather than invented;
- whether future AI policy can support searching, withdrawal and uncertain target knowledge;
- whether battle state will ever represent hidden/unknown combatants and, if so, under what authoritative contract;
- how Minecraft should display dynamic coloration without giving the adapter authority over the state.

## Canon questions

- which Ouros species or populations have authored camouflage/mimicry behavior;
- which individuals have persistent documented appearance histories;
- which appearance changes are mechanical Forms versus ordinary biological variation;
- which visual signals have known functions;
- which famous resemblance explanations are folklore, research hypotheses or established truth;
- how habitat change affects detectability over years;
- which sensitive populations should have appearance/location evidence redacted.

No answer above is established as canon by this snapshot.