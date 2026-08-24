# Pass 149 Research — Settlement Demography, Residency & Population Change

Status: RESEARCH / PROVENANCE ONLY. Not established Ouros canon.
Date: 2026-08-24

## Why this gap

The repository already has detailed authorities for Travel, Lodging, Homes, Land Tenure, Identity, Families, Workplaces, Emergency Services and settlement public space. The Lodging layer explicitly delegates `residence/demography` to another authority, but no dedicated demography layer currently owns that state.

The missing question is not merely “how many NPCs are visible?” It is how a settlement remembers who usually lives there, who is only present temporarily, when a person relocates, how an evacuation differs from migration, how estimates are revised, and how population change affects services without turning loaded Minecraft entities into census truth.

## Source findings

### 1. Jubilife Village: a settlement can have an authored history of arrival and growth

Official Pokémon Legends: Arceus material describes Jubilife Village as the base of the Galaxy Expedition Team, whose members came from multiple regions to study Hisui. The official story page also explicitly connects the village to the later Jubilife City, turning the same place into a long-term settlement-growth precedent rather than a static hub.

A separate official Pokémon article says Jubilife Village had existed for only two years at the time of the game and describes the player gradually settling into the community. This is useful for Ouros because it separates settlement age, resident history, institutional arrivals and the later physical growth of a city.

Reusable structure:

`recent settlement -> arrivals from multiple places -> institutions establish services -> residents develop local routines -> later settlement revisions preserve earlier history`

Do not copy Galaxy Team, Hisui colonization details or Jubilife geography into Ouros.

Sources:
- https://legends.arceus.pokemon.com/en-au/story/
- https://www.pokemon.com/us/pokemon-news/a-look-at-the-early-days-of-pokemon-research-in-pokemon-legends-arceus

### 2. PTU settings work better when settlements have different pressures instead of one global population state

A public PTU GM discussion recommends showing how the same regional disruption affects the general population differently from town to town: shortages, rebuilding and resupply can create different local side stories instead of repeating one global plot beat. The useful lesson is not the specific antagonist. It is that population pressure should be scoped to settlements and periods.

A separate public PTU campaign recruitment post describes a region containing both dense southern urban areas and remote northern settlements. That simple contrast reinforces that settlement scale and service structure can differ without requiring separate rulesets.

Sources:
- https://www.reddit.com/r/PokemonTabletop/comments/ztr88m/
- https://www.reddit.com/r/lfg/comments/rh7quc/

### 3. “Usually lives here” and “is physically here now” must be separate states

The U.S. Census Bureau uses the concept of usual residence as the place where a person lives and sleeps most of the time. Ouros should not import U.S. law or census rules, but the conceptual separation is valuable: current location, overnight stay, temporary assignment and usual residence are not interchangeable.

This is especially important because the repo already models hotels, dormitories, emergency shelters, work sites, trains, ferries, research stations and first journeys. A character can be physically present at any of those places without automatically becoming a resident.

Source:
- https://www.census.gov/content/dam/Census/programs-surveys/decennial/2020-census/2020-Census-Residence-Criteria.pdf

### 4. Population estimates need vintages and methods

Census population-estimate documentation treats population numbers as estimates built from a base plus components of change and revises prior estimates as better data or methods become available. Another Census technical overview summarizes population change through births, deaths and net migration, while noting that different data providers and methods can yield different estimates.

Ouros should reuse only the architectural lesson:

- population values need `as_of` dates;
- estimates need method/provenance;
- a later estimate may revise an earlier one without making the earlier publication fraudulent;
- administrative records, direct counts and sample surveys can disagree legitimately;
- settlement-boundary revisions can change what a number means even if no person moved.

Sources:
- https://www.census.gov/content/dam/Census/programs-surveys/international-programs/select-topics-in-international-population-health/population-estimates-and-projections.pdf
- https://www.census.gov/content/dam/Census/newsroom/press-kits/2024/paa/paa2024-paper-modernizing-popestimates-base.pdf

## Ouros design lessons

1. Persistent actors keep the same `actor_id` when they move. Relocation changes residence state, not identity.
2. Residence is an episode with start/end uncertainty, not a permanent property of the actor.
3. Physical presence is observation state. It may support but does not define residence.
4. Lodging stays, hospital stays, work assignments, travel legs, festival visits and emergency shelter stays do not automatically establish residence.
5. Displacement and relocation are distinct. A flood evacuation can last months without becoming a permanent move.
6. Return is its own event. Returning to visit is not the same as re-establishing usual residence.
7. Population estimates must be versioned. Chronicle can preserve what institutions believed at the time.
8. Minecraft entity count is presentation only. Loaded villagers/NPCs are never a demographic census.
9. Service pressure can be caused by temporary population. A festival, migration-season workforce or evacuation can stress water, lodging or transit without changing resident population.
10. Do not infer protected or sensitive traits from address, settlement, household membership, name, origin or movement history.

## PTU / Caelo cross-check

The accessible File Library search did not recover the project’s primary Caelo Player’s Guide, Caelo rulebook/errata or Region Location & Encounter List for a reliable population/residency rule. It instead surfaced the project’s earlier narrative-arc research package, which correctly treats PTU 1.05 and the pinned AutoPTU oracle as rules sources rather than narrative assumptions.

No PTU combat mechanic is required to define settlement residence or population estimates. If a future Caelo source contains authored settlement populations, legal residency concepts, citizenship, age rules or travel restrictions, those sources must override procedural assumptions in this proposal.

Super PTU Online Helper was not exposed as an invocable capability in this run. No output is attributed to it.

## Canon safety

Nothing in this research establishes:

- exact populations for any Ouros settlement;
- citizenship, nationality or legal-residence systems;
- mandatory census participation;
- household definitions;
- family relationships;
- age structure;
- fertility or mortality rates;
- immigration law;
- ethnicity, religion, class or other sensitive demographic categories;
- population-based encounter rates or spawn modifiers.

All such decisions remain authored canon questions.