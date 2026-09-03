# Marea Native Habitat Projection Fixture — Pass 227

Status: PROPOSED IMPLEMENTATION FIXTURE. Does not change canon or approve candidate species.
Date: 2026-09-03

Depends on:
- `design/ecology-development-program.md`
- `design/cobblemon-native-spawn-projection-contract.md`
- `design/global-species-interaction-graph.md`
- `proposals/2026-09-03-marea-sendero-species-interaction-matrix-226.md`

## Purpose

Translate the first Marea ecology work into a fixture that can eventually be evaluated against the actual Minecraft biome and installed Cobblemon spawn data.

The fixture deliberately does not invent biome IDs for Marea. The physical world must report the real Minecraft biome at each canonical cell, and the adapter must resolve the active Cobblemon biome/tag memberships and spawn details.

## Runtime cell contract

Each ecological cell needs a native environment binding:

```yaml
cell_id: marea.sendero_lower_shelf
minecraft_world: null
minecraft_dimension: null
minecraft_biome_id: null
resolved_biome_tags: []
observed_block_tags: []
structure_ids: []
authored_zone_ids: []
resolution_status: runtime_required
```

These fields are measured/resolved from the actual map. They are not prose lore.

## Existing Marea cells

`marea.puerto_bruma_populated_edge`, `marea.sendero_lower_shelf`, `marea.sendero_vegetated_band`, and `marea.loma_clara_cultivation_edge` remain ecology cells for reasoning and persistence.

They are not Minecraft biomes and must never be passed to Cobblemon as if they were biome IDs.

Each cell instead binds to the Minecraft biome/tag state underneath its coordinates.

## Species projection records

### Fletchling

Local status: CANON PRESENT as a persistent individual in the lower Sendero context.

```yaml
species_id: fletchling
cell_id: marea.sendero_lower_shelf
population_projection_mode: persistent_individual_first
native_spawn_details: runtime_lookup
native_habitat_compatibility: unresolved_until_map_lookup
generic_spawn_allowed: unresolved
persistent_individual_reserved: true
ecology_modifiers:
  population_pressure: null
  ecological_weight_multiplier: null
  visibility_multiplier: null
```

The existing persistent individual must not be duplicated because a generic Fletchling spawn detail is legal at the same location.

### Squawkabilly

Local status: PROPOSED.

```yaml
species_id: squawkabilly
candidate_cells:
  - marea.puerto_bruma_populated_edge
  - marea.sendero_lower_shelf
native_spawn_details: runtime_lookup
native_habitat_compatibility: unresolved
activation_requires:
  - species_local_approval
  - actual_native_spawn_compatibility_or_reviewed_datapack_change
  - authored_contested_resource_for_territorial_loop
```

No amount of ecological territorial logic can activate generic Squawkabilly spawning if the installed native spawn envelope rejects the actual Marea biome/context.

### Wurmple

Local status: PROPOSED.

```yaml
species_id: wurmple
candidate_cells:
  - marea.sendero_vegetated_band
native_spawn_details: runtime_lookup
native_habitat_compatibility: unresolved
activation_requires:
  - species_local_approval
  - physical_vegetation_cover_established
  - actual_native_spawn_compatibility_or_reviewed_datapack_change
  - authored_tree_or_sap_resource_for_foraging_loop
```

If Wurmple becomes locally valid, predator pressure may reduce `visibility_multiplier` without asserting an immediate demographic decline.

### Swellow

Local status: PROPOSED.

```yaml
species_id: swellow
candidate_cells:
  - marea.sendero_vegetated_band
  - marea.sendero_lower_shelf
native_spawn_details: runtime_lookup
native_habitat_compatibility: unresolved
activation_requires:
  - species_local_approval
  - actual_native_spawn_compatibility_or_reviewed_datapack_change
  - prey/resource overlap for trophic activity
```

### Taillow

Local status: PROPOSED CONDITIONAL.

The current matrix already gates Taillow on forest-compatible overlap. Pass 227 strengthens that gate: a narrative statement that an area is vegetated is insufficient. The actual Minecraft biome/tag plus installed Cobblemon spawn conditions must support the species, unless a reviewed datapack/world change expands native eligibility.

```yaml
species_id: taillow
candidate_cells:
  - marea.sendero_vegetated_band
native_spawn_details: runtime_lookup
native_habitat_compatibility: unresolved
activation_requires:
  - species_local_approval
  - physical_map_cover_approval
  - native_spawn_envelope_match
```

### Scatterbug

Local status: PROPOSED LATER.

Scatterbug remains deferred. Any later activation follows the same native envelope rule and must bind plant-resource ecology to actual Minecraft/Cobblemon-observable microhabitat facts where possible.

## First end-to-end spawn fixture

The first implementation target should use Fletchling because a persistent local individual already exists.

Expected sequence:

```text
1. Resolve the real Minecraft biome at lower Sendero.
2. Expand relevant biome tags from the installed datapack set.
3. Find all active Cobblemon Fletchling spawn details compatible with that context.
4. Record their IDs, bucket, base weight, presets and conditions.
5. Reserve the canonical persistent Fletchling identity.
6. Evaluate whether anonymous generic Fletchling population projection is also allowed in that cell.
7. Apply local ecology modifiers only to anonymous eligible details.
8. Materialize/reconcile visible entities without cloning the persistent individual.
9. Record telemetry: cell, native detail ID, native weight, ecology modifiers, entity identity.
```

This fixture tests the architecture without requiring a new species to become canon.

## Second fixture: Wurmple visibility under predator pressure

Enable only after Wurmple and a compatible predator are approved locally and the native spawn envelope validates both.

Baseline:

```yaml
population_pressure: 1.0
visibility_multiplier: 1.0
ecological_weight_multiplier: 1.0
```

Predator pressure phase:

```yaml
population_pressure: 1.0
visibility_multiplier: reduced
 ecological_weight_multiplier: context_dependent
```

The test passes only if visible exposed encounters fall while the persistent population state can remain unchanged.

No numeric multiplier is canonized by this fixture.

## Failure conditions

The implementation should fail validation when:

- an Ouros cell name is used as a Minecraft biome ID;
- a species is made eligible only because a narrative habitat label resembles a biome;
- ecology expands a native spawn envelope without an explicit reviewed datapack/world decision;
- visible spawn counts are written back as population truth without reconciliation;
- a persistent named individual is cloned by anonymous generic spawning;
- all spawn details for a species are flattened into one universal local rate;
- a proposed species becomes canon merely because Cobblemon permits it to spawn there.

## Mechanical dependencies

Ambient fixture dependency:
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING until live native spawn-data lookup, dynamic ecology projection and identity reconciliation are verified.

No AutoPTU tactical capability is required for the spawn-validation fixture itself.

If territorial or predator encounters escalate into battle, use the capability declarations already required by the interaction matrix and encounter contracts. Do not infer full support from representative mechanics.

## Next evidence needed

The highest-value implementation evidence is the actual Marea world biome/tag state plus the exact Cobblemon version/datapack spawn rows for Fletchling and the proposed local roster.

Until that exists, all biome compatibility fields in this file remain explicitly unresolved rather than being guessed from prose.
