# Engine readiness snapshot — pass 143

Status: implementation-readiness evidence for narrative design. Not Ouros canon.

## Live repositories inspected

AutoPTU-Java head inspected: `edf8db216ab88a10b896f2bb144cf5d08de49d8e` — `Test Telepathy in authoritative area execution (#171)`.

AutoPTU Python head inspected: `928c31a7b72243434536fdf05731ced421403f08` — Career persistence/market sanitization work. No tactical-family promotion follows from that Career change.

AutoPTU-Java README still states that the Python implementation is authoritative while the port is incomplete and still lists full combat state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, transcript parity, tactical AI and Minecraft/Cobblemon adapter work as incomplete.

## New Java evidence since pass 142

The current Java head adds a runtime regression for Telepathy inside authoritative multi-target area execution.

The tested path demonstrates that, for this representative case:
- a tile-aimed area action expands to ordered targets using authoritative battle state;
- an allied Telepathy user can take the already-ported pre-damage escape reaction;
- the reaction changes that combatant's authoritative position;
- the reacting combatant avoids damage in that case;
- the reaction does not spend the normal Shift action;
- the enemy target still receives normal damage processing;
- the declared Move consumes its Standard action and frequency once.

This is meaningful evidence for area-move execution and one pre-damage reaction path. It is not evidence that all reactions, forced movement, terrain/hazards or complex objective movement are implemented.

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

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions as a complete family
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

Do not promote a category because one representative mechanic works.

## Pass 143 encounter dependency review

### Corridor Sampling Day — FULL

Requires:
- VERIFIED targeting/footprints/range/LoS;
- VERIFIED base movement legality;
- BLOCKING complete movement if wild actors must cross/withdraw during combat;
- VERIFIED core calculations;
- VERIFIED action economy/initiative;
- PARTIAL lifecycle/damage/status/move/ability/item/Feature families when exact effects are used;
- BLOCKING terrain/weather/hazards/zones/reactions if the corridor is represented as a protected or dynamically changing tactical lane;
- VERIFIED AI legal-action infrastructure;
- BLOCKING AI tactical policy for CROSS/WITHDRAW/PROTECT_SAMPLE;
- BLOCKING adapter/playback.

REDUCED: resolve migration/sampling in world state before battle, freeze a static arena away from the corridor, then use conventional AutoPTU combat.

### Founder Release Perimeter — FULL

Requires BLOCKING complete movement, BLOCKING tactical AI and BLOCKING adapter/playback if released Pokémon must reach exits without being normal hostile combatants.

REDUCED: complete release first, remove released Pokémon from the grid, then resolve any independent threat in a static encounter.

### Archive Sample Retrieval

The research/custody portion is non-combat. A static battle can run using currently VERIFIED core families. Any escort/interception implementation remains dependent on complete movement and tactical AI.

## Genetics-specific non-inferences

The battle engine currently provides no population-genetics subsystem.

Do not infer:
- IVs/stats/Natures/Abilities as genetic-diversity metrics;
- Egg Groups as population structure;
- visible spawn count as census or effective population size;
- capture history as pedigree completeness;
- a released Pokémon as confirmed gene flow;
- rarity as genetic uniqueness;
- a bottleneck as a combat penalty;
- a founder population as a breeding bonus;
- area-move/reaction support as ecology simulation.

## PTU/Caelo source boundary

Public PTU material confirms explicit breeding concepts such as Egg Groups and offspring rules, but Pass 143 found no authoritative project rule that maps wild-population genetic diversity to combat state.

The complete Caelo source corpus was not recoverable from available project sources during this run. Super PTU Online Helper was not exposed as an invocable tool. No rule is invented from either source.

## New overworld blockers

- `POPULATION_GENETICS_CASE_STATE`
- `GENETIC_SAMPLE_PROVENANCE`
- `DIVERSITY_ASSESSMENT_REVISION_HISTORY`
- `FOUNDER_EVENT_GRAPH`
- `GENE_FLOW_EVIDENCE`
- `BOTTLENECK_ASSESSMENT`
- `HISTORICAL_SAMPLE_BASELINE_HANDOFF`
- `CONSERVATION_GENETICS_TO_MIGRATION`
- `CONSERVATION_GENETICS_TO_ISLAND_BIOGEOGRAPHY`
- `CONSERVATION_GENETICS_TO_BREEDING_LINEAGE`
- `CONSERVATION_GENETICS_TO_COBBLEMON`
- `CONSERVATION_GENETICS_TO_BATTLE_SNAPSHOT`

These belong to persistent world-state services, not AutoPTU-Java battle rules.

## Outcome

Pass 143 can advance immediately as narrative/world-state architecture. The reduced encounter versions preserve the premise without duplicating missing PTU rules in Minecraft. Mechanically rich versions remain explicitly gated behind the exact incomplete capability families they require.