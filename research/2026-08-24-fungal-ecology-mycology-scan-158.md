# Fungal Ecology & Mycology Research Scan — Pass 158

Status: RESEARCH / PROVENANCE ONLY. Not canon.
Date: 2026-08-24

## Why this pass exists

The repository-wide search before writing found no dedicated fungal/mycology authority and no existing `fungus`, `mushroom` or `mycelium` layer in the narrative repository. Relevant neighboring authorities already exist for Flora, Soil, Decomposition, Forest Management, Botanical Gardens, Toxicology, Food Safety, Taxonomy, Subterranean Systems and Interspecies Ecology. Pass 158 therefore fills the narrower missing responsibility: persistent fungal organisms/colonies, fruiting episodes, substrate associations, mycelial evidence, spores as observations, and fungal ecological roles without duplicating those adjacent systems.

This research is not a PTU rules source and does not modify canon.

## Source register

### Official Pokémon Pokédex — Paras and Parasect

Sources:
- https://www.pokemon.com/us/pokedex/paras
- https://www.pokemon.com/us/pokedex/parasect

Reusable structure:

Paras and Parasect provide a species-specific example where a fungal organism has a persistent relationship with a Pokémon host. Paras is described with mushrooms taking most of the nutrition while it feeds on roots; Parasect is described as having the host drained by the mushroom and the mushroom apparently controlling behavior.

Ouros use:

- allow authored host/fungus relationships where species evidence supports them;
- keep host identity and associated fungal state separate;
- allow the relationship to change across life stage/evolution when canon explicitly says it does;
- never generalize this relationship to all fungi, all Grass-types or all mushroom-like Pokémon.

Do not copy Parasect's exact biological story into an original species or NPC arc.

### Official Pokémon Pokédex — Shiinotic

Source:
- https://www.pokemon.com/uk/pokedex/shiinotic

Reusable structure:

Shiinotic provides a species-specific case where visible light/spores can be associated with predation and sleep. This is useful as a guardrail because the same visual motif can exist as ecology, observation, warning signage or a battle mechanic depending on the exact context.

Ouros use:

- a glowing fungal-looking site does not automatically become a sleep hazard;
- Shiinotic presence may justify an authored encounter premise;
- actual Sleep application must come from the exact PTU Move/Ability/runtime contract, not from ambient mushroom blocks or narrative spores.

### Official Pokémon Pokédex — Amoonguss

Source:
- https://www.pokemon.com/el/pokedex/amoonguss

Reusable structure:

Amoonguss provides a species-specific link between released spores and later mushroom-like growth. Its Pokédex also frames Poké Ball mimicry as uncertain in effectiveness, which is useful evidence discipline: observed resemblance and successful deception are separate claims.

Ouros use:

- record a spore-release observation separately from later growth;
- preserve uncertainty over whether two observations are causally linked;
- never infer Effect Spore, Poisoned, Sleep or Paralysis from environmental growth alone.

### Kairos Isles PTU living-world encounter tables

Source:
- https://kairosptu.wiki.gg/wiki/Pok%C3%A9mon_Encounter_Tables

Reusable structure:

The public PTU living world distinguishes a dedicated Mushroom Forest from neighboring forest identities and gives it a different encounter composition, including Paras, Foongus, Shroomish and Morelull. The useful lesson is not the percentages. It is that fungal habitat identity can be regional and persistent rather than a one-room gimmick.

Ouros transformation:

- a fungal grove can have its own observation history, seasonal fruiting and associated Pokémon without becoming a dungeon;
- habitat associations remain authored/proposed and never write spawn truth directly;
- no Kairos rates, relic species, map layout or campaign-specific content is imported.

### PTU public rules mirrors / project source evidence — mushrooms, Spore, Effect Spore

Public reference inspected:
- https://pturpg.wikidot.com/consumables

Project evidence inspected read-only:
- `Teffa14/AutoPTU` search results for `Tiny Mushroom` expose PTU audit/source and item data.
- `Teffa14/AutoPTU` search results for `Effect Spore` expose an authoritative Python hook path under `auto_ptu/rules/hooks/abilities/contact_effects.py` as well as source/audit records.

Rules boundary:

PTU has explicit mushroom consumables with identification/effects, a Move named Spore, and an Ability named Effect Spore. These are discrete mechanics. Pass 158 does not redefine their DCs, action costs, outcomes, Status semantics or targeting.

The existence of those mechanics is exactly why the overworld fungal system must not invent a generic `spore cloud = Sleep/Poison/Paralysis` rule.

### National Park Service — mushrooms and fruiting bodies

Source:
- https://www.nps.gov/shen/learn/nature/mushrooms.htm

Reusable ecological structure:

NPS distinguishes the visible mushroom as a fruiting body from a larger fungal organism supported by hyphae/mycelium in its substrate. Moist conditions influence visible mushroom development, and fungi can remain ecologically present when no fruiting body is visible.

Ouros transformation:

- fungal organism identity persists across fruiting and non-fruiting periods;
- fruiting-body observations are episodes, not population truth;
- lack of visible mushrooms is `NOT_DETECTED`, not automatic absence;
- substrate state matters and is versioned separately.

### U.S. Forest Service — macrofungal ecosystem functions

Source:
- https://research.fs.usda.gov/treesearch/38089

Reusable ecological structure:

The Forest Service separates major functional roles including decomposition, disease/pathogenic relationships and symbiotic relationships with trees. Visible macrofungi are spore-bearing fruit bodies, while ecosystem function can occur beyond the visible body.

Ouros transformation:

Use role assessments such as `SAPROTROPHIC_ASSOCIATION`, `MYCORRHIZAL_ASSOCIATION`, `PATHOGENIC_ASSOCIATION`, `UNKNOWN` only as evidence-backed interpretations. Do not let visual similarity assign function automatically.

### U.S. Forest Service — mycorrhizae

Source:
- https://research.fs.usda.gov/treesearch/9995

Reusable ecological structure:

Mycorrhizae are fungus-root associations where plants and fungi exchange resources. The associations vary by fungal and plant groups; not every fungus-tree pairing has the same relationship.

Ouros transformation:

- mycorrhizal claims require a specific host/site/evidence scope;
- Flora owns plant condition and identity;
- Soil owns soil condition;
- Fungal Ecology owns the fungal association observation/assessment;
- no `healthy mushroom nearby = tree buff` inference.

### U.S. Forest Service — fungi in wood decay

Source:
- https://research.fs.usda.gov/treesearch/54715

Reusable ecological structure:

Fungi can act as decomposers, mycorrhizal partners, pathogens, wildlife food and components of nutrient cycling. Detection can be difficult and repeated surveys across years and below-ground sampling can improve detection.

Ouros transformation:

- survey effort and method must be stored;
- a single fruiting season is weak evidence of long-term absence/presence trends;
- deadwood management can affect fungal observations and should hand off to Deadwood/Forest Management rather than being rewritten here;
- fungivory and dispersal can become Interspecies Ecology claims when observed.

### U.S. Forest Service — wild edible mushroom harvest

Source:
- https://research.fs.usda.gov/treesearch/5632

Reusable social structure:

Wild mushroom harvest can create tension among ecological conservation, recreation, commercial collection and land management, and requires monitoring rather than assuming harvest is harmless or destructive.

Ouros transformation:

- harvesting access, foraging, market sale and conservation can become separate institutional questions;
- mushroom availability at a market does not prove local abundance;
- a harvest closure does not prove population collapse;
- PTU mushroom Items remain exact mechanics downstream of identification/ownership rules.

## Design conclusions

The strongest new reusable narrative structures are:

1. The visible organism is only part of the history. A famous mushroom ring can disappear while the underlying fungal organism may remain, or a new fruiting patch may appear elsewhere.
2. Fruiting is episodic. The same grove can be quiet for several years and then produce a major visible season after weather/substrate changes.
3. Function must be observed. Decomposer, pathogen and mutualist are interpretations tied to evidence, not art tags.
4. One site can contain several overlapping fungi. A visual patch should never collapse all fungal observations into one `colony` without evidence.
5. Detection effort matters. Surface surveys, fruiting-body surveys, substrate samples and root-associated studies can disagree legitimately.
6. Harvest is social as well as ecological. Foraging traditions, commercial demand, conservation rules and scientific sampling can compete over the same seasonal resource.
7. Pokémon relationships stay species- and individual-specific. Parasect, Shiinotic and Amoonguss provide useful authored precedents but do not establish generic fungal rules.
8. A quiet year is content. `No fruiting observed this season` can become meaningful longitudinal evidence without generating a quest.

## Canon and rules guardrails

Do not infer:

- mushroom block -> fungal organism identity;
- mushroom count -> population size;
- no fruiting body -> fungal absence;
- fungal growth -> Poisoned/Sleep/Paralysis;
- spores present -> Spore Move used;
- contact with a mushroom -> Effect Spore;
- luminous mushroom -> Illuminate Ability;
- fungal patch -> Rough Terrain, hazard, cover or movement penalty;
- Paras/Parasect nearby -> root disease caused by them;
- Amoonguss-like growth -> Amoonguss definitely produced it;
- mycorrhiza -> mechanical healing/stat bonus;
- deadwood fungus -> timber unsafe without a separate Forestry/Architecture assessment;
- edible-looking mushroom -> PTU Mushroom Item;
- Minecraft harvesting -> authoritative PTU Item acquisition.

## PTU/Caelo source status

The project AutoPTU repository exposes PTU mushroom/item records, Spore-related data and an Effect Spore Python hook path. These prove that exact PTU mechanics exist somewhere in the project rules/runtime corpus; they do not prove Java parity for every one of them.

The complete primary Caelo corpus was not recovered reliably through the accessible task sources during this pass. No Caelo-specific mushroom, foraging, spore, forest, toxic-environment or fungal rule is asserted here.

Super PTU Online Helper was not exposed as an invocable capability.

## Proposed Ouros direction

Create a dedicated fungal ecology authority that can persist organisms/colonies, substrate associations, fruiting episodes, surveys, samples, ecological-role assessments and harvest observations while handing plant health, soil, decomposition, toxicology, food safety, markets and battle mechanics to their existing owners.
