# Engine Readiness Snapshot — Pass 119

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU were inspected read-only.

## Live heads inspected

AutoPTU-Java `main`: `5d9e5069fa0c68432825a48be25fff6ba245d305`

Newest relevant Java evidence:

- status application now routes target-owned Ability prevention through a declarative resolver;
- `RuntimeCombatantState` owns canonical Ability-suppression state;
- the status application boundary respects suppression rather than letting adapters inject that state;
- tests cover Inner Focus -> Flinch, Immunity -> Poison/Badly Poisoned, Insomnia -> Sleep and Vital Spirit -> Sleep;
- tests also prove that suppressing Abilities disables that prevention path;
- this strengthens `status lifecycle` and `abilities` evidence but remains representative coverage rather than a complete status controller or Ability catalog.

AutoPTU `main`: `753c05b6bd9f5aa010186e42bdb033554ef71d0c`

Newest visible Python changes preserve and test a pre-battle rollback checkpoint for Career when a battle becomes stuck. This is Career/service resilience work and does not promote a tactical capability category.

## Java README evidence

The live Java README still lists the following major work as incomplete:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Java remains the intended authoritative battle core while Minecraft/Cobblemon/Craftics remain adapters/renderers rather than owners of PTU rules.

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

No permanent category is promoted in Pass 119.

## Why the latest status/Ability slice does not promote categories

The new Java commit proves a specific target-owned status-prevention path and its suppression boundary. It does not prove:

- all statuses;
- all status application sources;
- all status immunities;
- all Ability suppression lifecycle semantics;
- all Ability effects;
- duration and expiry for every status;
- status interactions with terrain/weather;
- reactions/interrupts;
- complete event emission;
- full transcript parity.

Therefore `status lifecycle` and `abilities` remain PARTIAL.

## Why taxonomy is outside the battle core

Nothing inspected in Java or Python establishes authoritative overworld systems for:

- taxon concepts;
- taxonomic revisions;
- historical/synonym names;
- provisional identifications;
- classification disputes;
- field-guide/Pokédex edition history;
- reference-library versions;
- occurrence-record re-determination;
- scientific split/merge history;
- regional population-differentiation claims.

These belong to persistent world/science/archive state.

A battle must already receive an authoritative mechanical species/form record for each combatant. Narrative uncertainty about how researchers classify or name that Pokémon must not make the battle engine infer Types, stats, Moves, Abilities, capabilities or evolution links.

## Pass 119 encounter dependency map

### Archive Specimen Retrieval — FULL

Narrative objective:

Recover access to an archive specimen needed for a classification review while keeping staff and collection objects safe during an unrelated incident.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if staff/specimen movement becomes tactical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if the archive incident has a real tactical hazard
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `PROTECT`, `WITHDRAW`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Archives secures staff and specimen custody before battle. Freeze one safe room as the arena. Resolve only the actual combat obstacle. Taxonomic review happens after combat and victory cannot establish the specimen's identity.

### Three-Candidate Field Survey — FULL

Narrative objective:

Collect corroborating evidence where tracks/calls fit several candidate species while minimizing disturbance.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED if combat begins
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for true pursuit/withdrawal paths
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if an environmental effect is tactically active
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `AVOID`, `PROTECT_YOUNG`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Tracking, calls, samples and observation effort remain in overworld state. If a confrontation occurs, use a static legal battle with only involved combatants. The survey may legitimately end unresolved.

### The Public “New Form” Incident — FULL

Narrative objective:

Protect an unusual-looking Pokémon and manage a crowd after media claims it is a newly discovered regional form, while leaving classification to later scientific review.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for crowd and withdrawal lanes
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if a real tactical environmental effect exists
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `CLEAR_AREA`, `PROTECT`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Public Space/Tourism redirects the crowd and Pokémon Agency resolves the individual's movement outside the grid. If a threat remains, open a conventional static battle. No battle outcome can establish a new form.

## New overworld blockers introduced by Pass 119

These belong outside AutoPTU-Java:

- `TAXON_CONCEPT_REGISTRY`
- `TAXON_REVISION_HISTORY`
- `NAME_USAGE_HISTORY`
- `TAXONOMIC_DETERMINATION_HISTORY`
- `DETERMINATION_CONFIDENCE_STATE`
- `IDENTIFICATION_REFERENCE_SET_REGISTRY`
- `TAXONOMY_DISPUTE_STATE`
- `TAXONOMY_SPLIT_MERGE_HISTORY`
- `OCCURRENCE_DETERMINATION_CROSSWALK`
- `MECHANICAL_TAXON_BINDING`
- `POPULATION_DIFFERENTIATION_CLAIMS`
- `PUBLIC_POKEDEX_EDITION_STATE`
- `TAXONOMY_TO_ARCHIVES_HANDOFF`
- `TAXONOMY_TO_SCIENCE_HANDOFF`
- `TAXONOMY_TO_CONSERVATION_HANDOFF`
- `TAXONOMY_TO_BIOSECURITY_HANDOFF`
- `TAXONOMY_TO_COBBLEMON_PROJECTION`

## Hard non-inferences for Pass 119

Do not infer:

- resemblance -> same species;
- resemblance -> evolutionary relationship;
- regional population difference -> regional form;
- unusual coloration -> Shiny or new form;
- local behavior -> new Ability;
- taxonomic split -> new PTU mechanical species;
- scientific merge -> change to individual Pokémon identity;
- old name -> false historical observation;
- Pokédex label -> omniscient species truth;
- archive label -> world truth;
- one signal/sample -> currently present live Pokémon;
- one rare observation -> globally rare species;
- population differentiation -> combat modifier;
- provisional classification -> new spawn table;
- taxonomic uncertainty -> Accuracy/evasion/status modifier;
- newly described taxon -> capture bonus;
- classification dispute -> faction hostility;
- Ability-suppression status boundary -> taxonomy or identification mechanics.

## PTU/Caelo validation state

The project’s primary Caelo Core/Player/encounter/character-creation source corpus was not recoverable from the accessible file library during this run.

Super PTU Online Helper was not exposed as an invocable capability.

Public PTU Pokédex/community sources were used only to establish content-version context and narrative structures. No mechanical rule was validated for:

- Pokémon Education identification checks;
- Researcher Features;
- Pokédex scan accuracy;
- specimen identification;
- taxonomy;
- regional-form recognition;
- unknown-Pokémon handling;
- Fakemon creation.

Generation 9 official Pokémon examples used by the research are narrative references only and do not imply that the current PTU 1.05/Gen 8 mechanical dataset contains those species.

## Design consequence

Pass 119 establishes a critical boundary for future Ouros discovery stories:

```text
physical individual/population
    -> observation/sample/media
    -> taxonomic determination
    -> taxon concept/revision
    -> institutional position
    -> public name/field guide
    -> actor knowledge
```

The classification can change while the observed event, persistent Pokémon identity and historical record stay fixed. Battle rules remain bound to the separately verified mechanical species/form record.