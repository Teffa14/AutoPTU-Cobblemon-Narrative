# Ecosystem Engineering and Habitat Legacy Layer

Status: PROPOSED SYSTEM DESIGN
Date: 2026-09-03
Pass: 224
Research provenance: `research/2026-09-03-ecosystem-engineers-habitat-legacy-scan-224.md`

## Purpose

Extend the existing interspecies ecology layer with persistent physical habitat modification created by wild Pokémon populations or individuals.

`HABITAT_ENGINEERING` already exists as a relation type. This file defines what world state that relation can create, how long it persists, how it affects other populations, and how Minecraft presents it without becoming ecological authority.

## Core separation

Keep these states distinct:

```text
ENGINEER_POPULATION_OR_INDIVIDUAL
ENGINEERING_BEHAVIOR_PRESSURE
ENGINEERED_STRUCTURE
HABITAT_EFFECT
SPECIES_RESPONSE
HUMAN_RESPONSE
TACTICAL_ENCOUNTER
```

An engineer can leave a structure behind. The structure can remain after the engineer emigrates or dies. The habitat effect can outlast the structure. These are separate persisted facts.

## Engineered structure schema

Candidate `ENGINEERED_HABITAT_STRUCTURE`:

```text
structure_id
structure_type
builder_population_refs[]
builder_individual_refs[]
ecosystem_id
habitat_patch_id
created_window
last_maintenance_window
physical_state
functional_state
persistence_profile
material/resource_refs[]
hydrology_or_soil_effect_refs[]
access_effect_refs[]
dependent_population_refs[]
conflict_or_management_refs[]
world_projection_ref
provenance
revision
```

Candidate structure types include:

```text
DAM_OR_WEIR
BURROW_NETWORK
SOIL_TILLAGE_PATCH
NEST_COMPLEX
CANAL_OR_TRENCH
MOUND_OR_BANK
TREE_FELLING_PATCH
SHELTER_CAVITY
SUBSTRATE_REWORKING
OTHER_SOURCE_BACKED_ENGINEERING
```

Do not create a universal list of Pokémon engineers. Add species only with source-backed evidence and Ouros regional approval.

## Lifecycle

Candidate states:

```text
FORMING
ACTIVE_MAINTAINED
MATURE
DEGRADED
ABANDONED_FUNCTIONAL
ABANDONED_FAILING
BREACHED_OR_COLLAPSED
LEGACY_SUCCESSION
RECOVERED_OR_REPLACED
```

Ordinary chunk unload does not change lifecycle state.

Lifecycle transitions occur through world windows, explicit events or authoritative interventions.

## Maintenance pressure

Some structures require recurring builder presence.

```text
maintenance_probability = f(
  builder_abundance,
  resident_fraction,
  resource_access,
  season,
  disturbance,
  structure_condition,
  species_behavior_profile
)
```

A decline in builder abundance can therefore create delayed physical consequences instead of an instant world reset.

## Habitat effects

A structure can affect multiple state families:

```text
water_depth_or_flow
soil_condition
sediment_retention
vegetation_opening
woody_debris
shelter_availability
nesting_or_breeding_sites
resource_access
movement_cost_or_route_access
predator_prey_overlap
human_infrastructure_conflict
fire_drought_flood_exposure
```

Effects must be explicit and source-backed. A dam-like structure does not automatically grant every real-world beaver effect.

## Habitat succession

Abandonment can create new content.

Example generic sequence:

```text
active impoundment
-> maintenance stops
-> structure degrades
-> water regime shifts
-> exposed sediment/vegetation colonization
-> new patch composition
-> different species use the site
```

The old state remains part of local history and may leave physical evidence.

## Population feedback

The engineering layer writes into existing ecology systems rather than creating replacement population logic.

Possible outputs:

```text
resource_pressure_delta
habitat_suitability_delta
migration_or_distribution_pressure
nesting_site_capacity_change
predation_overlap_change
human_disturbance_change
```

Those values influence existing demographic and interspecies systems. They never manufacture members directly.

## Human and institutional conflict

One structure may simultaneously:

- improve wetland habitat;
- flood a footpath;
- alter a farm water intake;
- create breeding habitat for another species;
- reduce downstream flow;
- protect a dry-season refuge;
- require a route detour.

Do not reduce the situation to `good ecosystem engineer` or `pest`.

This supports disputes between residents, conservation staff, farmers, route managers and researchers while all parties can have legitimate evidence.

## World projection

Minecraft/Cobblemon receives semantic states such as:

```text
ACTIVE_DAM_STAGE_2
BURROW_NETWORK_DENSE
SOIL_TILLAGE_RECENT
LEGACY_WET_MEADOW
```

The adapter may place/remove approved blocks, water-state representations, vegetation variants, path obstructions, signs and ambient actors.

Minecraft block physics never independently decides that a canonical ecosystem structure failed or formed.

## Encounter: The Crossing That Changed

Premise: a familiar route crossing becomes deeper/wider because an engineer population has altered local hydrology.

Full version can support:

- physical rerouting around water;
- optional confrontation with territorial builders;
- rescuing a stranded actor;
- opening or closing a human-built bypass;
- later consequences depending on whether the structure is preserved, breached or managed.

Permanent capability dependencies if combat/control occurs:

- targeting/footprints/range/LoS: REQUIRED
- base movement legality: REQUIRED
- complete movement including push/pull/knockback/interception/forced movement: REQUIRED only if those effects are used
- core calculations: REQUIRED for combat
- action economy/initiative: REQUIRED for combat
- full turn/round lifecycle: REQUIRED for full tactical encounter
- full stateful damage pipeline: REQUIRED for damaging encounter
- status lifecycle: REQUIRED only if statuses are used
- terrain/weather/hazards/zones/reactions: REQUIRED for mechanically authoritative water/terrain/hazard interactions beyond simple world navigation
- move-specific behavior: REQUIRED for used Moves
- abilities: REQUIRED for used Abilities
- items: REQUIRED for used Items
- Trainer Features/perks: REQUIRED when invoked
- AI legal-action infrastructure: REQUIRED for combat AI
- AI tactical policy: REQUIRED for autonomous rich tactical choices
- Minecraft/Cobblemon/Craftics adapter/playback: REQUIRED for visible structure and world response

Reduced version:

- the structure exists as server-authored world state;
- Minecraft presents altered water/path geometry;
- the player investigates traces, talks with NPCs and takes a detour;
- no tactical hazard semantics, forced movement, statuses or hidden PTU effects are assumed;
- any battle that occurs uses only currently verified basic contracts.

Narrative premise remains intact: the route changed because a living population physically changed its habitat.

## Encounter: Who Owns the Waterline?

A human infrastructure operator wants an engineered structure removed because it affects access or flow. A conservation/research actor argues that the structure now supports dependent habitat.

The player can gather observations, map affected patches and document actual consequences before any intervention.

This encounter can run without battle mechanics. If intervention provokes a live encounter, inherit the exact capability families used.

## Species candidate boundary

Bibarel and Diglett have public official-lore support for habitat-modifying behavior. They are candidates only.

Before Marea placement, require:

```text
official species status
+ Ouros regional/content enablement
+ source-backed local habitat suitability
+ explicit population placement
```

No species is added to Marea by this design document.

## Acceptance checks

1. Removing the last engineer from a patch does not instantly erase its structure.
2. Chunk unload does not alter structure lifecycle.
3. Structure degradation is persisted once per due window.
4. Habitat effects can help one population and hinder another simultaneously.
5. A structure can generate human conflict without any battle.
6. Builder population decline can cause delayed landscape change.
7. A breached structure can enter legacy succession instead of resetting to pristine terrain.
8. Minecraft cannot canonize structure failure from visual block changes alone.
9. A real battle at the structure still uses AutoPTU authority.
10. No Pokédex flavor text silently grants combat mechanics.

## Canon status

PROPOSED. Existing Marea canon remains unchanged.