# Pokémon Popularity as Spawn Accessibility Input — Pass 230

Status: RESEARCH / DESIGN INPUT. Does not change species canon or native spawn legality.
Date: 2026-09-03

## Purpose

Record a defensible source for Pokémon popularity and define how popularity may influence world placement without overriding Minecraft/Cobblemon habitat compatibility or Ouros ecology.

## Source baseline

A current official-source baseline available for a global popularity ranking is Pokémon of the Year 2020, published by The Pokémon Company through `pokemon2020.pokemon.com`.

The worldwide top ranks published there include:

1. Greninja — 140,559 votes
2. Lucario — 102,259
3. Mimikyu — 99,077
4. Charizard — 93,968
5. Umbreon — 67,062
6. Sylveon — 66,029
7. Garchomp — 61,877
8. Rayquaza — 60,939
9. Gardevoir — 60,596
10. Gengar — 60,214

The same source provides generation/region rankings and further worldwide positions. The ranking is dated and must therefore be stored with provenance rather than treated as timeless truth.

Source:
- Pokémon of the Year 2020 official results: https://pokemon2020.pokemon.com/en-us/

## Design interpretation

Popularity is a player-experience input, not an ecological permission system.

Correct authority order:

```text
native Minecraft/Cobblemon habitat compatibility
+ Ouros ecology and population plausibility
+ progression/safety constraints
+ popularity accessibility pressure
= candidate placement near player entry corridors
```

Incorrect order:

```text
popular Pokémon
-> force spawn near world spawn regardless of habitat
```

## Spawn accessibility objective

The global world-design pass should maximize early discoverability of popular species where naturally compatible habitat can exist near the initial player region.

This can be achieved mainly by selecting the initial player-region geography and biome mix, not by rewriting species spawn definitions.

Examples:

- if a popular species requires forest or temperate conditions, place an adequately large compatible forest/temperate ecosystem within early travel distance;
- if a popular species is aquatic, ensure coast, river or lake access is reachable from the initial region;
- if a popular species is cave/night/special-condition dependent, make that habitat discoverable without flattening its rarity or conditions;
- legendary, mythical, dangerous or progression-gated species must not become ordinary early generic spawns merely because they rank highly.

## Ranking tiers

Do not hard-code one top-N list directly into worldgen. Normalize popularity into an input record:

```yaml
species_id: null
ranking_source: pokemon_of_the_year_2020
rank_global: null
votes: null
rank_generation: null
accessibility_priority: null
eligibility_notes: []
```

Suggested policy bands for later tuning:

```text
A: highest popularity — strongly prefer compatible habitat in the early-world biome portfolio
B: high popularity — prefer reachable compatible habitat in the first major region/adjacent regions
C: normal — no special world-spawn proximity pressure
SPECIAL: legendary/mythical/boss/progression-sensitive — popularity never authorizes generic early spawning
```

Exact cutoffs remain unresolved until the full usable ranking is imported and crossed with Cobblemon spawn data.

## Required cross-check

Before the final world seed and player spawn are frozen, generate a report:

```text
popular species
-> Cobblemon native spawn details
-> required biome tags/context/time/weather/structure
-> nearest compatible habitat from proposed player spawn
-> travel distance
-> progression restrictions
-> ecology viability
```

The seed/config should be penalized if too many high-priority ordinary species require extreme travel despite compatible biome families being available elsewhere in the candidate world.

## Important separation

Popularity can influence:
- where the initial player region is selected;
- which biome families should be represented nearby;
- route accessibility to compatible habitats;
- early encounter discoverability within native/legal details;
- which species are prioritized for ecology authoring and encounter polish.

Popularity must not directly override:
- native biome conditions;
- time/weather/light/context restrictions;
- rarity/bucket without reviewed balancing;
- persistent population truth;
- legendary/mythical/progression gating;
- explicit local ecology contradictions.

## Next implementation evidence

Import or generate the complete official ranking dataset that is usable for all supported Cobblemon species, then cross it against the pinned Cobblemon spawn pool and the biome portfolio of each candidate global seed.

If a newer official broad global ranking is identified, add it as a separate provenance source rather than silently replacing the 2020 ranking.
