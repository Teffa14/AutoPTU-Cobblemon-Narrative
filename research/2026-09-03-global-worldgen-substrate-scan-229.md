# Global Ouros Worldgen Substrate Scan — Pass 229

Status: RESEARCH / PROVENANCE. Does not change canon by itself.
Date: 2026-09-03

## Question

What Minecraft/Cobblemon world-generation substrate can support one persistent Ouros world containing all countries, regions, settlements, routes, ecosystems and future content without splitting the project into unrelated regional maps?

## Current project conflict discovered

`canon/marea-interior-map-resident-network-v2.md` currently freezes Marea anchors around x/z 2048–2224 inside `minecraft:overworld`.

Those anchors were valid for the earlier local-map implementation plan, but the project now requires a global world first. They must therefore be treated as migration-sensitive legacy anchors until the global planet layout is frozen. This research file does not silently move them and does not revoke canon. A later explicit migration decision is required.

## Worldgen candidates

### Continents — Stardust Labs

Observed public description:
- reshapes the Overworld into separated continents, large oceans and islands;
- compatible with Minecraft 1.21.x and earlier supported lines;
- designed to work with Terralith;
- medium continents are roughly kilometre-scale in blocks according to project documentation, but Ouros must benchmark actual seeds and configuration instead of assuming default sizes are adequate.

Use for Ouros:
- strong candidate for macro geography substrate;
- useful if countries and regions must occupy coherent landmasses rather than Minecraft's ordinary noise-patch geography;
- default scale is not automatically acceptable for an entire world containing many countries.

Source: https://modrinth.com/datapack/continents

### Terralith — Stardust Labs

Observed public description:
- adds 95+ biome variants while using vanilla blocks;
- compatible with Continents;
- Cobblemon recognizes many Terralith biomes through its biome-tag system.

Use for Ouros:
- strong candidate for biome diversity while preserving Cobblemon-native spawn compatibility;
- preferable to inventing an Ouros-only biome taxonomy;
- actual biome distribution and patch size need seed-level measurement before world lock.

Sources:
- https://blog.curseforge.com/terralith-mod-faqs/
- https://wiki.cobblemon.com/index.php/Pok%C3%A9mon/Spawning/Spawn_Definitions

### Tectonic

Observed use in current Minecraft/Cobblemon packs:
- terrain-generation overhaul used together with Terralith in some 1.21.1 packs;
- focuses on dramatic terrain and large-scale landforms.

Use for Ouros:
- candidate terrain-shape layer only after compatibility testing with the selected Continents/Terralith stack;
- do not add because a modpack happens to include it; verify noise/worldgen composition and seed reproducibility first.

Reference example: Ravenwolf's Cobblemon Create on Modrinth.

### Wythers / Expanded Ecosphere family

Cobblemon's own biome-definition documentation lists William Wythers biome families among recognized spawn categories.

Use for Ouros:
- alternative or complementary biome source worth benchmarking against Terralith;
- avoid stacking multiple biome overhauls merely to maximize count. More biome IDs can make ecological authoring and global distribution harder to control.

Source: Cobblemon Spawn Definitions wiki.

### Antique Atlas / Antique Atlas 4

The remembered name “antiopia” has not been verified. A plausible nearby name is Antique Atlas, but this is a map-display mod, not a planet generator.

Observed behavior:
- renders explored terrain/biomes as a stylized map;
- modern Antique Atlas 4 can use data-driven biome and structure tiles.

Use for Ouros:
- potentially useful later as the player's diegetic world map or exploration UI;
- it cannot solve global landmass generation.

Sources:
- https://github.com/AntiqueAtlasTeam/AntiqueAtlas
- https://github.com/BurnDLX/antique-atlas

## Existing Cobblemon map packs are references, not the substrate

Public adventure-map packs such as Jond's Cobblemon Adventure Maps package several hand-built Pokémon regions. That pattern is useful for studying structure density and region-scale traversal, but it does not satisfy Ouros because Ouros requires one continuous global world rather than separate imported region maps.

Source: https://www.curseforge.com/minecraft/modpacks/jonds-cobblemon-maps

## Proposed global generation stack to benchmark

Baseline candidate:

```text
Minecraft Overworld
+ Continents macro landmass layout
+ Terralith biome distribution
+ optional Tectonic terrain shaping only if compatibility is deterministic
+ Cobblemon biome tags/spawn definitions
+ Ouros authored global geography overlay
```

The stack is a benchmark target, not yet a pinned dependency.

## Scale problem

The world must be sized from content capacity rather than accepting a generator's defaults.

Required global hierarchy:

```text
planet
  -> continent / ocean basin
    -> country
      -> major region
        -> district / province
          -> settlement / route / wilderness
            -> ecological cells / authored sites
```

Minecraft biomes remain physical world facts beneath that political/narrative hierarchy.

A country is not a biome. A Pokémon region is not a biome. A biome may cross political boundaries, and one country may contain many biome families.

## Biome-size requirement

The user requirement is to avoid tiny noisy biome mosaics and aim for biome areas that read as real landscape units at play scale.

Implementation research must therefore measure, for candidate seeds/configurations:
- contiguous biome-area size in chunks and blocks;
- median and percentile biome patch sizes;
- coast length and island distribution;
- continent area distribution;
- mountain-chain continuity;
- major river continuity;
- climate transition width;
- traversal time on foot and by expected transport modes;
- Cobblemon biome-tag coverage per physical biome.

Do not interpret “1x1 real biome” as literal Earth metre-for-metre scale until the project explicitly defines the scale ratio. The important invariant now is coherent landscape-scale biome regions instead of local random patches.

## Global lock requirements

Before more local coordinates or spawn ecology are frozen, the project needs:

1. pinned Minecraft, loader and Cobblemon versions;
2. selected worldgen stack and exact versions;
3. fixed world seed/config;
4. pregenerated global survey or deterministic sampling;
5. continent/ocean atlas;
6. biome raster/index;
7. target world bounds or supported exploration envelope;
8. political/region placement plan;
9. migration plan for existing Marea coordinates;
10. generated-world checksum/version identity so future generator upgrades cannot silently rewrite geography.

## Consequence for ecology

Ecology work remains valid at the schema level, but local activation pauses until cells bind to real generated coordinates and Minecraft biome/tag state.

Cobblemon remains the native spawn substrate. Once the planet is generated, Ouros can index every biome and build species compatibility from actual world facts rather than prose assumptions.

## Next bounded implementation slice

Build a global world-generation specification and seed-evaluation contract. It should define the coordinate hierarchy, minimum continent/country/region capacities, biome-size metrics, pregeneration/index outputs and the explicit migration gate for Marea's existing fixed anchors.
