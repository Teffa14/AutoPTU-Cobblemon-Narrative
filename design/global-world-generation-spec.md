# Ouros Global World Generation Specification

Status: PROPOSED DESIGN. Requires explicit worldgen/canon approval before freezing geography.
Date: 2026-09-03

## Purpose

Define the world-generation contract for one persistent Ouros Overworld containing the complete global geography: all continents, oceans, countries, regions, settlements, routes, wilderness systems and future ecological content.

The project must not build independent regional maps and stitch them conceptually afterward. Regional authoring sits inside one globally generated spatial substrate.

## Authority order

```text
pinned worldgen stack + seed + config
-> immutable physical planet geometry
-> Minecraft biome IDs/tags and structures
-> Ouros geographic/political partition
-> authored settlements/routes/sites
-> ecological cells and population state
-> Cobblemon native spawn envelope
-> visible overworld actors
```

Worldgen owns physical terrain.
Ouros owns names, borders, institutions, history, authored structures and persistent ecology.
Cobblemon consumes native Minecraft/worldgen facts for spawn eligibility.

## Global hierarchy

Every authored spatial object must have one parent in this hierarchy:

```text
world: ouros.overworld
continent_or_ocean_basin
country
region
subregion_or_district
settlement_route_or_wilderness
site
microhabitat_or_ecology_cell
```

Administrative boundaries are overlays. They do not replace Minecraft biome data.

## Coordinate registry

The global registry must support:

```yaml
world_id: ouros.overworld
worldgen_version: null
seed: null
bounds_policy: null

continents: []
ocean_basins: []
countries: []
regions: []
settlements: []
routes: []
sites: []
```

Each spatial record eventually stores polygon/bounds data, not only one anchor coordinate.

Minimum fields:

```yaml
id: null
parent_id: null
name: null
coordinate_bounds: null
anchor: null
minecraft_dimension: minecraft:overworld
intersecting_biome_ids: []
intersecting_biome_tags: []
worldgen_source_refs: []
status: proposed
```

## World scale gate

No seed can be accepted only because it looks attractive near spawn.

A candidate world must demonstrate enough coherent physical space for the entire authored setting.

The evaluation must quantify:

- total usable land area inside the supported world envelope;
- number and size distribution of major landmasses;
- ocean separation between major landmasses;
- room for every planned country and major region;
- contiguous biome patch sizes;
- mountain-chain length and continuity;
- river and watershed continuity;
- coast and island diversity;
- cold/temperate/arid/tropical biome distribution;
- underground and special-biome availability where relevant;
- transport-distance feasibility.

## Biome scale policy

The project requires landscape-scale biomes rather than tiny checkerboard biome noise.

Biome suitability is measured at the generated-world level.

Required metrics per seed/config:

```yaml
biome_id: null
area_chunks: null
largest_connected_component_chunks: null
median_component_chunks: null
p90_component_chunks: null
bounding_box_blocks: null
adjacent_biome_ids: []
cobblemon_tags: []
```

The final target ratio between Minecraft blocks and real-world distance remains an explicit design decision. Do not claim literal 1:1 geographic scale until that ratio is approved.

## Candidate worldgen stack

Current benchmark baseline:

```text
Continents
+ Terralith
+ optional Tectonic after compatibility test
```

Reasons:

- Continents supplies large landmasses and oceans.
- Terralith supplies broad biome diversity while remaining compatible with Cobblemon biome tagging.
- Tectonic may improve macro terrain forms, but it must not be added until deterministic compatibility and biome distribution are benchmarked.

Alternative biome generators can replace Terralith if measurements are better. The stack is not canon until benchmarked.

## Seed evaluation protocol

For each candidate stack/version/configuration:

1. generate the same bounded survey area for multiple seeds;
2. export or inspect biome and height data;
3. calculate the required scale metrics;
4. reject worlds with fragmented biome mosaics or inadequate continent capacity;
5. shortlist seeds that meet physical requirements;
6. visually inspect coastlines, mountains, rivers and biome transitions;
7. verify Cobblemon tag coverage across representative biomes;
8. test structure generation conflicts;
9. freeze one seed/config only after country/region capacity review;
10. record the world identity and checksums.

## Pregeneration and indexing

Before detailed lore placement, the selected world should be pregenerated or deterministically surveyed over the supported global envelope.

Required outputs:

```text
world manifest
continent mask
height map
biome ID map
Cobblemon biome-tag index
river/water map
structure index
coordinate grid
worldgen version manifest
```

These outputs become implementation evidence for later placement work.

The project should never discover after years of authoring that one required climate or landmass does not exist in the world.

## Country and region placement

Countries and regions are placed only after the planet survey exists.

Placement must use physical geography:

- watersheds;
- mountain barriers;
- coasts;
- plains;
- river valleys;
- islands;
- climate/biome transitions;
- transport corridors.

Political borders may cross biomes. Biome borders must not be distorted merely to match political borders unless an explicit authored worldgen modification is approved.

## Existing Marea migration gate

`canon/marea-interior-map-resident-network-v2.md` currently freezes Puerto Bruma, Sendero del Vidrio, Loma Clara and Estación Mirador around coordinates near `(2048, *, 2048)`.

Those records cannot be silently overwritten.

Before the global world is frozen:

```text
existing Marea anchors
-> mark as legacy coordinate set
-> locate suitable Marea region in selected global world
-> compare physical geography with canon requirements
-> propose explicit coordinate migration
-> migrate all dependent NPC/quest/site references atomically
-> record old -> new coordinate mapping
```

If the selected global world happens to support Marea at the existing anchors, no migration is needed. That outcome must be verified rather than assumed.

## Ecology dependency

The global planet is now a prerequisite for implementation-facing local ecology.

Species behavior research and schemas can continue, but no local habitat compatibility should be finalized until the relevant coordinates exist in the frozen world.

After world lock:

```text
coordinate
-> actual biome ID
-> Cobblemon biome tags
-> native species spawn envelope
-> Ouros population/behavior overlay
```

## Player map layer

Map-display mods such as Antique Atlas 4, Xaero's World Map or another later choice are presentation layers only.

They may expose discovered geography, names, borders and markers, but they do not determine world generation.

A diegetic map can intentionally reveal less than the full pregenerated developer atlas.

## Required implementation tooling

The future worldgen toolchain needs at minimum:

- reproducible server/world creation from pinned versions;
- seed batch generation;
- biome/height/structure extraction;
- connected-component biome analysis;
- continent/landmass area analysis;
- image/map export for review;
- coordinate registry generation;
- regression check that the same stack/seed regenerates equivalent geography.

## Immediate project priority

Until the global substrate is selected and generated, world-map work outranks further local spawn tuning.

The next technical milestone is not another Marea habitat table. It is a reproducible global worldgen prototype and measurable seed survey.
