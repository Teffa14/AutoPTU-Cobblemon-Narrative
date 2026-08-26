# Engine Readiness Snapshot — Pass 174

Status: evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU are read-only in this task.

## Live heads inspected

AutoPTU-Java: `fb93d3a4e6633d17a5a79f3095b141f887d4f258`

Recent Java work includes live generic secondary Status execution through Move Specials, authoritative accuracy-roll transport, secondary-status composition and canonical prevention routing.

AutoPTU Python: `ef0143b900ab671b1f0e061318278058b87fe403`

Recent Python work is Career presentation/persistence hardening and does not change tactical capability classification.

## Java evidence boundary

The Java README still states that the following remain unfinished as full systems:

- core combatant/grid battle state;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The new secondary-Status work is meaningful evidence for a particular execution path. It is not evidence that every Status, Move, Ability, prevention interaction or lifecycle edge case is complete.

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

### BLOCKING as complete families

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## Pass 174 PTU-specific cross-check

The project corpus contains PTU Ability data and Python tests/implementation logs for many individual Abilities. Searchable data includes `Shed Skin` and `Seasonal` concepts.

Do not infer Java parity for those abilities from their existence in the Python corpus.

Do not use PTR2e/Foundry `Seasonal` reference text as PTU/Caelo authority. The AutoPTU repository contains multiple source/reference families and its own Ability log explicitly treats PTUDatabase/CSV data as primary over Foundry where available.

## Encounter dependency — Molt-Site Access Disturbance

FULL version:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL if used
- terrain/weather/hazards/zones/reactions — BLOCKING if tactical environment is used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:

World state evacuates civilians/researchers and resolves wildlife withdrawal. AutoPTU receives only a static legal battle after the ecological movement is complete.

## Encounter dependency — Seasonal Crossing Window

FULL version requires:

- complete movement — BLOCKING for crossing/withdrawal/interception;
- AI tactical policy — BLOCKING for non-hostile movement objectives;
- adapter/playback — BLOCKING;
- environmental family — BLOCKING only if weather/road state must have tactical effects.

REDUCED version stops transport and completes wildlife movement in world state before any battle.

## Investigation dependency — Shed-Skin Identity Survey

No battle engine required for the intended form.

Relevant world authorities:

- Field Signs
- Taxonomy
- Science / Research Ethics
- Visual Records
- Pokémon Agency
- Material Culture / Museums if material is collected

A separate battle can use verified basic targeting/movement/action infrastructure but cannot decide identity, provenance or molt stage.

## Mechanical guardrails for Pass 174

- Biological shedding never triggers PTU `Shed Skin` automatically.
- A molt observation never cures Status.
- A visible seasonal coat never chooses a mechanical Form.
- World season does not activate battle mechanics until an explicit authoritative engine contract consumes that state.
- Minecraft biome, texture, particles and dropped items cannot infer PTU season, Form, Ability, Status cure or biological completion.
- One implemented secondary Status path does not promote the Status family.
- One implemented Ability elsewhere does not promote Abilities as a whole.

## Unresolved rules/canon questions

- Does final Caelo alter PTU `Shed Skin` or season-dependent Abilities?
- Which Pokémon in Ouros have authored seasonal covering cycles?
- Which apparent seasonal changes are actual mechanical Forms?
- Does the final adapter need a world-season input contract for battle rules?
- Are shed materials ever legal research samples, cultural objects or commodities?
- Which molt sites, if any, are established canon at campaign start?
- What welfare observations require Care review rather than routine biological recording?

No answer was invented where primary Caelo material was unavailable.