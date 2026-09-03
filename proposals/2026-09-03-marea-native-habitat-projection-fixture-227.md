# Marea Native Habitat Projection Fixture — Pass 227

Status: PROPOSED IMPLEMENTATION FIXTURE. Does not change canon or approve candidate species.
Date: 2026-09-03

Depends on:
- `design/ecology-development-program.md`
- `design/cobblemon-native-spawn-projection-contract.md`
- `design/global-species-interaction-graph.md`
- `proposals/2026-09-03-marea-sendero-species-interaction-matrix-226.md`
- `research/2026-09-03-cobblemon-1.7.1-marea-spawn-envelope-audit-228.md`

## Purpose

Translate the first Marea ecology work into a fixture evaluated against actual Minecraft biome state and pinned Cobblemon spawn data. Ouros ecological cells refine native habitats; they never replace Minecraft/Cobblemon biome semantics.

## Runtime cell contract

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

These fields are measured from the actual map. They are not prose lore.

## Native spawn-detail evidence from Cobblemon 1.7.1

This fixture now records exact details from public branch `Delta-Academy-MC/Cobblemon:academy-1.7.1`. The actual Ouros installation must still pin/verify its own version and datapacks.

### Fletchling — CANON persistent individual, generic population unresolved

Observed native detail:

```yaml
spawn_detail_id: fletchling-1
presets: [natural, treetop]
spawnable_position_type: grounded
bucket: common
level: 3-28
base_weight: 5.4
required_biome_tags:
  - '#cobblemon:is_forest'
  - '#cobblemon:is_sky'
  - '#cobblemon:is_taiga'
skylight: 8-15
time: day
```

Projection rule:
- the canonical persistent lower-Sendero Fletchling can remain authored even when generic native compatibility is unresolved;
- generic Fletchling spawning is permitted only if the actual cell resolves to a matching native detail;
- the persistent identity must be reserved before any anonymous population materialization.

### Taillow — PROPOSED CONDITIONAL

Observed native detail:

```yaml
spawn_detail_id: taillow-1
presets: [natural, treetop]
bucket: common
level: 2-27
base_weight: 9.0
required_biome_tags:
  - '#cobblemon:is_sky'
  - '#cobblemon:is_temperate'
forbidden_biome_tags:
  - '#cobblemon:is_spooky'
skylight: 8-15
time: day
```

Correction to prior fixture assumptions: native eligibility is not specifically forest-gated. Any ecology requirement for vegetation/prey remains a separate Ouros layer.

### Swellow — PROPOSED

Observed native detail:

```yaml
spawn_detail_id: swellow-1
presets: [natural, treetop]
bucket: common
level: 22-46
base_weight: 1.0
required_biome_tags:
  - '#cobblemon:is_sky'
  - '#cobblemon:is_temperate'
forbidden_biome_tags:
  - '#cobblemon:is_spooky'
skylight: 8-15
time: day
```

Taillow and Swellow share the same broad biome envelope in the inspected source but retain distinct level ranges and base weights. Ouros must never collapse them into one local bird spawn rate.

### Squawkabilly — PROPOSED, stronger Puerto Bruma candidate

Relevant native details:

```yaml
spawn_detail_id: squawkabilly-2
presets: [urban, natural, treetop]
bucket: common
level: 17-42
base_weight: 6.0
required_biome_tags:
  - '#cobblemon:is_overworld'
forbidden_biome_tags:
  - '#cobblemon:is_freezing'
  - '#cobblemon:is_sandy'
skylight: 8-15
time: day
weather: not_raining
```

```yaml
spawn_detail_id: squawkabilly-3
presets: [natural, treetop]
base_weight: 6.0
required_biome_tags:
  - '#cobblemon:is_overworld'
required_structures:
  - '#minecraft:village'
forbidden_biome_tags:
  - '#cobblemon:is_freezing'
  - '#cobblemon:is_sandy'
time: day
weather: not_raining
```

```yaml
spawn_detail_id: squawkabilly-4
base_weight: 10.0
required_biome_tags:
  - '#cobblemon:is_sky'
time: day
```

Puerto Bruma should therefore be tested first against `squawkabilly-2`, not assumed to be a village. Settlement canon does not imply a Minecraft `#minecraft:village` structure tag.

### Scatterbug — PROPOSED LATER

Observed primary detail:

```yaml
spawn_detail_id: scatterbug-1
presets: [natural, foliage]
bucket: common
level: 1-20
base_weight: 7.0
required_biome_tags:
  - '#cobblemon:is_floral'
  - '#cobblemon:is_plains'
  - '#cobblemon:is_savanna'
skylight: 8-15
```

Loma Clara or a Sendero vegetation cell becomes a candidate only if the actual Minecraft biome/tag and foliage context satisfy the native detail. Crop prose alone is insufficient.

### Wurmple — PROPOSED, SPAWN PROVENANCE UNRESOLVED

The expected standard `0265_wurmple.json` spawn-pool row was not present in the inspected public 1.7.1 branch and code search did not surface a standard `pokemon: wurmple` spawn detail.

Do not fabricate a habitat envelope. Before Wurmple can participate in an executable generic-population fixture, verify the exact Ouros distribution/datapack and locate its spawn provenance or approve a deliberate datapack addition.

## Existing Marea cells

These remain ecology/persistence cells, never Minecraft biomes:

- `marea.puerto_bruma_populated_edge`
- `marea.sendero_lower_shelf`
- `marea.sendero_vegetated_band`
- `marea.loma_clara_cultivation_edge`

Each cell binds to the real Minecraft biome/tag/structure/block context under its coordinates.

## First end-to-end runtime fixtures

### Fixture A — persistent Fletchling reconciliation

```text
1. Resolve real biome + tags at lower Sendero.
2. Evaluate `fletchling-1` and every installed Fletchling spawn detail independently.
3. Record native eligibility before Ouros ecology is considered.
4. Reserve the canonical persistent Fletchling identity.
5. Decide whether anonymous Fletchling population projection is also allowed.
6. Apply ecology multipliers only to native-legal anonymous details.
7. Materialize/reconcile entity identity.
8. Record detail ID, native weight, ecology modifiers, materialized entity ID and persistent reservation state.
```

Pass condition: changing the Ouros multiplier never makes an otherwise native-illegal Fletchling detail eligible.

### Fixture B — Puerto Bruma Squawkabilly native envelope

```text
1. Resolve Puerto Bruma biome tags, rain state, skylight and actual preset context.
2. Test `squawkabilly-2` independently.
3. Test `squawkabilly-3` only if a real `#minecraft:village` structure match exists.
4. Test `squawkabilly-4` only if the native `is_sky` biome tag matches.
5. Keep species status PROPOSED even if native eligibility succeeds.
```

Pass condition: a real settlement is never treated as a Minecraft village merely because humans live there.

### Fixture C — Taillow vs Swellow relative native availability

When both species are locally approved and the real biome is compatible:

```text
native eligible Taillow detail weight: 9.0
native eligible Swellow detail weight: 1.0
```

Ouros may later alter each detail through separate ecological causes. Telemetry must retain both original weights and reason refs.

Pass condition: ecology can suppress or concentrate either species without losing the distinction between their native base weights.

### Fixture D — Scatterbug foliage gate

Resolve actual biome tags plus the native `foliage` preset semantics before enabling generic Scatterbug projection.

Pass condition: `vegetated`, `farm`, `crop` or `garden` narrative labels do not themselves satisfy the native foliage requirement.

## Failure conditions

Validation fails when:
- an Ouros cell name is used as a Minecraft biome ID;
- a narrative habitat label is accepted as native compatibility evidence;
- ecology expands a native spawn envelope without a reviewed datapack/world change;
- visible spawn counts are written back as population truth without reconciliation;
- a persistent named individual is cloned by anonymous spawning;
- several spawn details are flattened into one universal species rate;
- a proposed species becomes canon merely because Cobblemon permits it;
- a settlement is treated as `#minecraft:village` without actual structure-tag evidence;
- a missing Wurmple row is silently replaced with guessed biome rules.

## Mechanical dependency

Ambient projection depends on Minecraft/Cobblemon/Craftics adapter/playback support and remains PARTIAL/BLOCKING until live biome/tag/preset lookup, dynamic spawn filtering/weight projection and identity reconciliation are verified end-to-end.

No AutoPTU tactical capability is required for these spawn fixtures. If a visible ecological interaction escalates to battle, use the permanent encounter capability matrix independently.

## Next evidence needed

Highest-value next work:
- resolve actual Marea Minecraft biome IDs and tags from the fixed world/map;
- pin the exact Ouros Cobblemon build/datapacks;
- verify runtime semantics for `natural`, `treetop`, `urban`, and `foliage` presets;
- locate Wurmple spawn provenance in the intended distribution;
- implement/read an adapter-facing diagnostic that prints cell -> biome/tags -> matching spawn-detail IDs.
