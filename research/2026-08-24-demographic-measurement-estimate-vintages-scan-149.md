# Pass 149 Research — Demographic Measurement, Estimate Vintages & Coverage

Status: RESEARCH / PROVENANCE ONLY. Not established Ouros canon.
Date: 2026-08-24

## Scope after duplication check

Pass 60 already owns demography, migration and population change. This pass does not create a second demography system. It targets a narrower unresolved problem inside that layer: how Ouros preserves population measurements, estimate vintages, coverage gaps, geography revisions and later methodological corrections without rewriting earlier Chronicle state.

## New source findings

Official Pokémon Legends: Arceus material gives a useful long-horizon settlement example. Jubilife Village is described as only two years old, populated in part by Galaxy Team members who came from multiple regions, and as the place that eventually develops into Jubilife City. The reusable structure is settlement history whose population knowledge and institutions become more complete over time, not a static NPC count.

Sources:
- https://legends.arceus.pokemon.com/en-au/story/
- https://www.pokemon.com/us/pokemon-news/a-look-at-the-early-days-of-pokemon-research-in-pokemon-legends-arceus

A public PTU discussion suggests allowing a regional disruption to affect different towns through different population/service consequences such as rebuilding or resupply rather than repeating one global quest. The useful abstraction is settlement-scoped pressure and recovery, not its specific antagonist.

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/ztr88m/

U.S. Census material is used only as an abstract measurement reference. Its “usual residence” concept separates where a person normally lives from where that person happens to be at one moment. Ouros should preserve the same conceptual distinction without importing U.S. law.

Source:
- https://www.census.gov/content/dam/Census/programs-surveys/decennial/2020-census/2020-Census-Residence-Criteria.pdf

Population-estimate methodology provides the more important architecture. Estimates are tied to a base, data sources, geography and methodological vintage. Later vintages can revise previous years because better inputs or methods became available. A revised series does not imply that the earlier publication was fraudulent or that everyone physically moved between the two publications.

Sources:
- https://www.census.gov/content/dam/Census/programs-surveys/international-programs/select-topics-in-international-population-health/population-estimates-and-projections.pdf
- https://www.census.gov/content/dam/Census/newsroom/press-kits/2024/paa/paa2024-paper-modernizing-popestimates-base.pdf

## Extension lessons for Pass 60

- Every population estimate should identify `reference_time`, `published_at`, `method_revision`, `geography_revision` and provenance.
- Preserve raw observations separately from the published estimate built from them.
- A later revision supersedes an estimate for current use but never deletes the historical value that actors actually saw.
- Coverage gaps should remain explicit. `NOT_COUNTED` is not `NOT_RESIDENT`.
- Boundary changes can alter population totals even when no actor moves.
- Temporary visitors, commuters, evacuees and residents away on assignment are common sources of discrepancy and already belong in Pass 60’s conceptual model.
- Loaded Minecraft actors remain presentation only and cannot be used as sampling frames or census truth.
- Estimate precision should match evidence. Broad bands are preferable to fake exact counts when the world lacks a reliable enumeration system.

## PTU / Caelo check

The File Library query did not recover a primary Caelo source defining settlement populations, census rules or residence. It returned the project’s earlier narrative-arc package, which points back to PTU 1.05 and the pinned AutoPTU oracle as mechanical authorities. No demographic PTU combat rule was identified.

Super PTU Online Helper was not exposed as an invocable capability during this run. No result is attributed to it.

## Canon safety

This research establishes no Ouros census bureau, citizenship system, legal residency category, household definition, sensitive demographic categories, fertility/mortality model or exact settlement count. Those remain authored decisions.