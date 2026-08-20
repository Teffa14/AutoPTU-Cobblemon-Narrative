# Engine Readiness Snapshot — Pass 44

Status: implementation evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU are read-only from this repository.

Inspected AutoPTU-Java head: `96cc7139271811eda57789843ab6030c7aa8af09`

Inspected Python AutoPTU head: `e4bb0ca38b7018710af476ce365d515a387de4e7`

## Why this snapshot exists

Narrative content must not treat one implemented representative mechanic as proof that an entire subsystem is implemented.

The permanent capability families remain the dependency boundary.

## Current capability map

### VERIFIED

- targeting / footprints / range / line of sight
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

### BLOCKING for concepts that require the full family

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / broad reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## New Java evidence since Pass 43

AutoPTU-Java commit `96cc7139271811eda57789843ab6030c7aa8af09` ports Defiant and Competitive through the authoritative combat-stage reaction path.

The inspected change adds:

- Defiant as a post-apply combat-stage reaction;
- Competitive as a post-apply combat-stage reaction;
- recursive re-entry through `CombatStageMutationService` rather than direct stage mutation;
- source/attacker checks;
- applied-delta-aware behavior;
- parity fixtures against the pinned Python oracle;
- tests for clamped stage drops and recursive stage changes.

This extends real evidence for two permanent families:

- Abilities: more individual Ability behavior is now implemented and parity-tested.
- Broad reactions: one specific combat-stage reaction path has additional representatives.

Neither family is complete.

## No promotion from the new slice

Abilities remain PARTIAL.

Defiant, Competitive and Simple do not prove:

- every Ability;
- contact-triggered Abilities;
- weather/terrain Abilities;
- movement-triggered Abilities;
- damage-triggered Abilities;
- status-triggered Abilities;
- switch/entry/exit Abilities;
- item-interaction Abilities;
- every recursive stage interaction.

Terrain/weather/hazards/zones/reactions remains BLOCKING as a broad family.

The new combat-stage reaction path does not prove:

- interception;
- attacks of opportunity;
- forced-movement reactions;
- hazard triggers;
- zone control;
- weather transitions;
- reaction timing across all Moves/Abilities/Trainer Features;
- Minecraft synchronization of any of those systems.

## Current Java README boundary

The current AutoPTU-Java README still marks these large areas incomplete:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic battle-event emission and full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The README continues to state that Minecraft/Cobblemon/Craftics should consume the Java core rather than own PTU rules.

## Python head evidence

The newest inspected Python AutoPTU head is `e4bb0ca38b7018710af476ce365d515a387de4e7`.

Its newest visible commits are Career-layer changes around roster recovery and do not justify changing the tactical capability categories used here.

Python remains the source oracle while Java is incomplete.

## Fashion layer implementation conclusion

Most Pass 44 systems can advance before battle parity is complete.

Narrative/world-state features that do not require AutoPTU include:

- garment instances;
- wardrobes;
- outfits;
- fashion workplaces;
- design patterns;
- commissions;
- uniform issue records;
- visual-culture profiles;
- style movements;
- wear history;
- public recognition records;
- fashion events;
- historic garment provenance;
- repair/alteration history;
- cosmetic Pokémon grooming records;
- per-player appearance preferences.

Mechanical clothing effects remain unavailable until they are individually validated against PTU/Caelo and implemented by the authoritative engine.

## Fashion-specific no-inference rules

- A cosmetic garment does not become a PTU item with an effect.
- A visually protective coat does not grant Damage Reduction.
- A stage costume does not grant Contest Appeal.
- A uniform does not prove current institutional membership.
- A disguise does not grant Guile or Stealth success.
- A Pokémon accessory does not alter Loyalty, happiness, stats or Moves.
- A Minecraft cosmetic slot cannot become the authority for PTU equipment legality.
- A working Trainer Feature registry does not prove a Fashionista-related Feature.

## Pass 44 encounter dependencies

### Backstage Evacuation

Reduced version:

- evacuation occurs as world state;
- civilians and performers stay outside the tactical grid;
- AutoPTU receives a static ordinary encounter.

Full version capability map:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING when corridor control or displacement matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for dynamic backstage hazards or protected corridors
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for evacuation-aware behavior
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

### Wardrobe Transit Chokepoint

Reduced version:

- cargo stays outside the grid;
- players clear a static encounter;
- delivery and custody update afterward.

Full version capability map:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for escort/chokepoint play
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full lifecycle: PARTIAL
- full stateful damage: PARTIAL
- statuses: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if route obstruction becomes tactical
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for cargo-protection or route-denial objectives
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

### Atelier Security Mix-Up

This concept is primarily social/investigative.

Reduced version:

- clothing modifies presented identity only;
- observer belief is handled by narrative state plus validated social mechanics when available;
- no tactical disguise mechanic is invented;
- if combat begins, AutoPTU receives a normal legal battle state.

Potential full tactical dependencies if guards, withdrawal or non-KO protection objectives become relevant:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception: BLOCKING when guard positioning or escape interception is mechanical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- full damage/status/move/ability/item/Feature families: use only validated implemented slices
- terrain/weather/hazards/zones/reactions: BLOCKING if detection zones or reactive security become tactical
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for arrest/withdrawal/protect-objective behavior
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

## Implementation priorities exposed by Pass 44

Fashion itself does not create a new engine priority.

The encounter contracts reinforce existing priorities:

1. complete movement/interception/forced movement;
2. objective-aware tactical AI;
3. terrain/hazard/zone/reaction support;
4. complete item/Feature registries when mechanically relevant equipment is introduced;
5. Minecraft/Cobblemon/Craftics playback and cosmetic-state presentation.

A separate overworld appearance system can be built before these battle families are complete, provided it remains cosmetic/world-state only.

## Permanent classification after Pass 44

VERIFIED:

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL:

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING:

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / broad reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback
