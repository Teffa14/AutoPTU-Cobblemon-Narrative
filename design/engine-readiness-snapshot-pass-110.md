# Engine Readiness Snapshot — Pass 110

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `473067bdd5b22f755014e53235e3b647d662902a`

Recent relevant Java slices:

1. `Port generic Trainer Feature heal effects (#145)` — adds parity-backed generic Trainer Feature heal-effect execution.
2. `Port Trainer Feature combat stage effects (#146)` — adds parity-backed generic Trainer Feature combat-stage effects and makes runtime accuracy stage mutable where required.
3. The immediately preceding slices already provided target scopes, authoritative bookkeeping, prerequisite/context/frequency/resource gates, and transaction ordering.

These are substantial improvements to Trainer Features/perks infrastructure. They still do not establish complete Feature catalog coverage, ritual/sacred mechanics, Legendary interaction, generic blessings/curses, broad reactions, environmental semantics, or Minecraft playback.

AutoPTU `main`: `8e5dea0cbafecb19dfa800918f7cbe2fe99fcd20`

Recent Python changes inspected are deployment and Career/friendship persistence oriented. They do not justify changing the tactical capability map.

## Java README evidence

The current Java README still lists the following as unfinished:
- core combatant/grid battle state expansion;
- full damage resolution pipeline;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- full move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Representative implementation remains representative only.

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

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## Why Pass 110 does not create sacred-site mechanics

Nothing in the newly inspected Java commits proves:
- ritual execution;
- sacred-site effects;
- divine/Legendary intervention;
- prayer or blessing mechanics;
- curse mechanics;
- pilgrimage rewards;
- shrine-triggered Weather or Terrain;
- relic powers;
- automatic Aura or supernatural perception;
- crowd/procession objectives;
- moving pilgrims or escorts;
- Legendary spawn conditions;
- sacred-site-aware tactical AI;
- projection of belief/custody/observance state into Minecraft or AutoPTU.

Generic heal or combat-stage Feature effects only prove that exact effect families when a concrete Trainer Feature legally invokes them. They do not authorize narrative healing, blessings, ritual buffs, sacred Accuracy bonuses, or “holy ground” stage changes.

## Current Trainer Feature evidence

Java now has parity-backed generic infrastructure for:
- prerequisite gates;
- context gates;
- frequency/cooldown gates;
- generic resource gates/consumption;
- usage/cooldown bookkeeping;
- transaction ordering;
- authoritative runtime bookkeeping;
- generic target-scope resolution for tested cases;
- generic heal effects;
- generic combat-stage effects for tested cases.

Trainer Features/perks remains PARTIAL because:
- concrete Feature catalog coverage is incomplete;
- effect families remain incomplete;
- target/effect semantics for many Features are unported;
- interrupts/reactions remain incomplete;
- movement/environment effects depend on other incomplete families;
- semantic playback to Minecraft is absent.

A sacred-site narrative must therefore cite a concrete Feature before using any heal/stage effect. Cultural meaning is never sufficient.

## Pass 110 encounter dependency map

### Shrine Approach Evacuation — FULL

Narrative objective:
Clear a blocked approach while visitors and wild Pokémon withdraw safely, preserving the sacred-site incident as world state rather than a battle-only event.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for moving civilians, wildlife corridors, protected lanes, or displacement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if unstable ground, weather, restricted areas, smoke, darkness, or similar states gain tactical mechanics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT`, `REACH_EXIT`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Resolve visitor evacuation and wildlife movement before battle. Freeze one static safe arena. Use AutoPTU only for combatants who remain. Update access, pilgrimage, ecology, and site history afterward.

### Relic Custody Interruption — FULL

Narrative objective:
Protect or recover a culturally important persistent object during an interrupted transfer without letting battle outcome decide ownership or legitimacy.

Dependencies:
- ordinary targeting/calculations/action economy: usable at current VERIFIED scopes
- complete movement/interception/forced movement: BLOCKING for moving-object escort/interception
- lifecycle/damage/status/move/ability/item/Feature families: current PARTIAL scope where invoked
- AI tactical policy: BLOCKING for `PROTECT_CUSTODIAN`, `INTERCEPT`, `ESCAPE_WITH_OBJECT`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Secure the object outside the grid, record custody before battle, run a static encounter, then resume or delay transfer using world-state consequences.

### Bell Ridge Night Watch — FULL

Narrative objective:
Manage an observation/observance window while unexpected wildlife activity develops nearby.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED for ordinary combat geometry
- complete movement: BLOCKING for autonomous withdrawal and crowd routing
- terrain/weather/hazards/zones/reactions: BLOCKING if darkness, weather, bells, wind, light, or field conditions receive mechanics
- AI tactical policy: BLOCKING for `WITHDRAW`, `AVOID`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- lifecycle/damage/status/moves/abilities/items/Features remain at their current PARTIAL scopes

Reduced version:
Pause observance, clear visitors, resolve wildlife movement in world state, keep supposed omens as evidence records, then use a conventional static battle only if a distinct combat conflict remains.

## New overworld blockers introduced by Pass 110

These belong outside AutoPTU-Java:

- `SACRED_SITE_IDENTITY`
- `SACRED_SITE_REVISION_HISTORY`
- `SACRED_RECOGNITION_BY_GROUP`
- `BELIEF_CLAIM_PROVENANCE`
- `SUPERNATURAL_CLAIM_TRUTH_STATUS`
- `CUSTODIANSHIP_ROLE_STATE`
- `PILGRIMAGE_ROUTE_IDENTITY`
- `PILGRIMAGE_ROUTE_REVISION`
- `PILGRIMAGE_JOURNEY_STATE`
- `RITUAL_PRACTICE_VERSIONING`
- `SACRED_OBJECT_RELATIONSHIP_STATE`
- `OMEN_ANOMALY_OBSERVATION_PROVENANCE`
- `SACRED_SITE_ACCESS_HANDOFF`
- `SACRED_SITE_TO_ARCHAEOLOGY_HANDOFF`
- `SACRED_SITE_TO_ARCHIVES_MYTHOLOGY_HANDOFF`
- `SACRED_SITE_TO_CONSERVATION_HANDOFF`
- `SACRED_SITE_TO_TOURISM_PUBLIC_MEMORY_HANDOFF`
- `SACRED_SITE_TO_MINECRAFT_PROJECTION`
- `SACRED_SITE_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 110

Do not infer:
- shrine -> Legendary spawn;
- sacred site -> confirmed supernatural truth;
- temple -> one unified religion;
- elder/custodian -> infallible authority;
- sacred object -> mechanical item effect;
- ritual -> heal/combat-stage change;
- prayer -> Trainer Feature;
- blessing -> buff;
- curse -> status;
- incense -> Weather/Terrain/status;
- bell/chime -> Sonic Move;
- sacred fire -> Fire damage;
- unusual light -> Aura;
- apparition report -> confirmed entity;
- pilgrimage completion -> XP, Feature, Loyalty, reputation, or badge;
- participation -> belief;
- access restriction -> ownership;
- wild Pokémon presence -> guardian role;
- repeated Pokémon appearance -> consent to capture or ritual use;
- one genuine anomaly -> every traditional explanation proven;
- battle victory -> theological, custodial, archaeological, ownership, or access conclusion;
- generic Java Trainer Feature heal/stage support -> permission to invent ritual healing or blessings.

## Mechanical/canon questions still unresolved

- Which sacred places, if any, are established before campaign start?
- Which communities recognize each place, and what exactly is public versus restricted knowledge?
- Which claims are cultural only, which are canonically false, and which have genuine anomalous evidence?
- How rare should Legendary-linked sacred locations be?
- Which custodians actually possess access authority?
- Can route changes caused by ecology/infrastructure preserve pilgrimage identity?
- Which sacred objects are symbolic only versus mechanically active under verified PTU/Caelo rules?
- What exact PTU/Caelo rules govern Occult Education, Aura, relics, Legendary interaction, blessings/curses, and supernatural perception?
- How should private PC belief be stored without procedural inference?
- What must Minecraft render for shared sacred spaces without making the adapter an authority on belief or mechanics?