# Research Pass 69 — Flora, Pollination, Seed Dispersal & Vegetation Dynamics

Status: RESEARCH ONLY. Not canon. External material is used for provenance, high-level structures, and design lessons. Do not copy protected prose, characters, distinctive plots, or source-specific dialogue into Ouros.

Date: 2026-08-20

## Why this pass exists

Ouros already has systems for agriculture, food, soil, conservation, wildfire, seasonality, freshwater, biosecurity, interspecies ecology, wild collectives, and settlement change. What is still missing is a persistent model for the vegetation itself and the ecological processes that connect plants to Pokémon.

Without that layer, a restored meadow, an orchard, a post-fire slope, a wetland edge, and a flower-rich urban park all risk collapsing into the same generic `plants_present=true` state.

This pass focuses on:

- flowering windows;
- pollination networks;
- nectar/pollen resources;
- seed dispersal;
- plant recruitment;
- vegetation succession;
- floral-resource continuity across seasons;
- disturbance and recovery;
- Pokémon–plant associations;
- restoration trajectories;
- plant provenance and local adaptation.

It does not create a botanical combat subsystem.

## Existing Ouros layers checked before writing

The branch was inspected before this pass. Relevant existing systems include:

- `design/food-agriculture-hospitality-layer.md`
- `design/conservation-protected-areas-stewardship-layer.md`
- `design/interspecies-ecological-relations-layer.md`
- `design/biosecurity-introduced-species-translocation-layer.md`
- soil/erosion/restoration design from Pass 67
- seasonality/calendar design from Pass 24
- wildfire/fire-ecology design from Pass 64
- light/night-ecology design from Pass 68
- wild-collective agency
- freshwater/hydrology
- material provenance
- science/research/discovery
- world-state/Chronicle architecture

The new layer should provide a shared vegetation state consumed by those systems rather than duplicate them.

## Pokémon source findings

### Combee — nectar gathering and group behavior

Official Pokédex material describes Combee as continually gathering nectar from flowers for Vespiquen. It also describes large nocturnal sleeping aggregations.

Source:
https://www.pokemon.com/us/pokedex/combee

Reusable structure:

A Pokémon population may depend on the spatial and seasonal distribution of floral resources. Nectar availability can affect where collectives forage without implying that every flower patch is mechanically valuable or that every Combee is a pollinator in exactly the same way.

Ouros use:

- flowering sites can become foraging destinations;
- loss of a flowering corridor can change collective routes;
- apiaries and orchards can intersect wild Combee activity;
- flowering restoration can alter observations before it alters any spawn projection.

Do not infer:

- automatic crop-yield bonuses;
- automatic Honey generation outside exact rules;
- Vespiquen ownership over every Combee group;
- a universal pollination mechanic from Honey Gather.

### Cutiefly — pollen/nectar use and bloom detection

Official Pokédex material says Cutiefly feeds on nectar and pollen and can identify flowers that are about to bloom in some entries.

Sources:
https://www.pokemon.com/us/pokedex/cutiefly
https://www.pokemon.com/uk/pokedex/cutiefly

Reusable structure:

Wild Pokémon behavior can act as an observation channel for phenology. A researcher might notice Cutiefly movement before a mass bloom without assuming Cutiefly causes the bloom.

Ouros use:

- biological indicators can become evidence;
- unusual absence from a normal flowering site can generate a field question;
- bloom forecasting can use multiple evidence sources: temperature, plant buds, prior records, and Pokémon activity.

### Ribombee — pollen as crafted material

Official Pokédex material describes Ribombee producing pollen puffs that people value.

Source:
https://www.pokemon.com/us/pokedex/ribombee

Reusable structure:

A species can connect wild ecology to material culture and trade. That connection should preserve individual agency and item rules.

Ouros use:

- specialist workshops or caretakers may study or trade naturally produced material where canon permits;
- overharvest pressure can become a stewardship issue;
- provenance matters if a material comes from a wild population versus an institutional partner.

Do not invent PTU effects from Pokédex flavor.

### Butterfree — floral-resource search

Official Pokédex material describes Butterfree seeking nectar and locating flower patches with small amounts of pollen.

Source:
https://www.pokemon.com/us/pokedex/butterfree

Reusable structure:

Flower patches can be connected into a landscape-scale resource network rather than treated as isolated decorative blocks.

Ouros use:

- corridors of flowering resources can affect migration/foraging observations;
- a restored patch may matter because it closes a gap between existing sites;
- a vanished patch can change movement without proving population decline.

### Eldegoss — seed dispersal and nutrient association

Official Pokédex material describes Eldegoss spreading nutrient-rich seeds on the wind. The Sword/Shield site explicitly links those seeds with regional soils and plants.

Sources:
https://www.pokemon.com/us/pokedex/eldegoss
https://swordshield.pokemon.com/en-us/pokemon-galar-region/eldegoss/

Reusable structure:

Seed movement can be a persistent ecological process. Pokémon can be one possible vector among wind, water, human transport, restoration projects, and other species.

Ouros use:

- seed-source provenance;
- dispersal observations;
- colonization fronts after disturbance;
- questions about whether a newly established patch came from local seed, a restoration mix, or Pokémon-mediated dispersal.

Do not infer that an Eldegoss automatically enriches any Minecraft block or produces a crop bonus.

### Flabébé / Floette / Florges — persistent relationships with flowers and gardens

Official Pokédex material ties these species closely to flowers and flower gardens.

Sources:
https://www.pokemon.com/us/pokedex/flabebe
https://www.pokemon.com/us/pokedex/floette
https://www.pokemon.com/us/pokedex/florges

Reusable structure:

Some Pokémon can have long-lived relationships with specific plant communities or garden sites. That supports persistent locations and recurring individuals without granting ownership of the site.

Ouros use:

- garden stewardship;
- plant-community identity;
- historical gardens that change with settlements;
- flower-color or species associations as observations, not automatic mechanical typing.

### Budew — plant-like phenology as biological indicator

Official Pokédex material says Budew is sensitive to temperature changes and that opening its bud can signal spring.

Source:
https://www.pokemon.com/us/pokedex/budew

Reusable structure:

Phenological indicators can come from Pokémon as well as plants. This ties Seasonality to Science and Observation.

Do not translate this into a universal calendar oracle.

## Public PTU campaign findings

### Campaign log #24 — vegetation disturbance changes encounter context

A public PTU campaign recap describes a player cutting down a tree, provoking concern from a Pokémon protecting eggs, and later planting trees as part of de-escalating the situation.

Source:
https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

Reusable structure:

- vegetation can be habitat, not scenery;
- a player-caused landscape action can change an encounter before initiative starts;
- restoration can be a negotiated consequence rather than a reward screen;
- eggs/nesting context can alter choices without requiring combat.

Do not copy the source characters, Pokémon identity, dialogue, or plot sequence into Ouros.

### Campaign log #22 — plant health can connect ecology, community and mystery

A public recap describes a settlement problem connected to a large tree whose condition was contributing to local water stress. The party investigated and addressed the plant problem rather than simply fighting an enemy.

Source:
https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t

Reusable structure:

A plant-health mystery can connect:

- field observation;
- local tradition;
- hydrology;
- Pokémon knowledge;
- community response;
- restoration.

Ouros should preserve uncertainty longer than the recap did. A stressed tree, low streamflow, and a local belief should remain separate evidence objects until causality is established.

## Restoration and ecology research

### Pollination is an ecological process, not only a species trait

FAO materials emphasize pollination as an ecosystem service and explicitly connect pollinator conservation with habitat restoration and agricultural resilience.

Sources:
https://www.fao.org/4/i1046e/i1046e00.pdf
https://www.fao.org/fileadmin/templates/nr/documents/CGRFA/SIS_BFA_Biodiversity_and_Global_Challenges.pdf

Design lesson:

Ouros should model pollination as a relationship network among flowering resources, pollinator activity, timing, and habitat continuity. It should not attach a permanent `pollinator=true` buff to a species and stop there.

### Restoration needs the right plants across the right times

US Forest Service research on pollinator restoration emphasizes plant mixes that provide floral resources across the landscape and growing season, and notes that different pollinators use different plants.

Sources:
https://research.fs.usda.gov/treesearch/65659
https://research.fs.usda.gov/treesearch/63732

Design lesson:

A meadow can be successful in total plant cover yet still fail to support a particular pollinator window. Ouros should support seasonal resource continuity rather than a single vegetation score.

### Plants solve multiple landscape problems at once

NRCS Plant Materials work describes vegetation supporting erosion control, water quality, forage, wildlife habitat, pollinators and post-fire restoration.

Source:
https://www.nrcs.usda.gov/plant-materials/cp

Design lesson:

One restoration project can create several causal edges:

planting → soil cover → erosion change
planting → floral resource window → pollinator use
planting → habitat structure → wildlife use
planting → future seed source → succession

The project should not need four separate arbitrary quests to represent those consequences.

### Succession is not guaranteed to return to one endpoint

Ecological teaching literature warns against treating succession as a single deterministic path that always returns a disturbed site to its previous state.

Source:
https://www.esa.org/tiee/vol/v3/experiments/floristic/pdf/floristic.pdf

Design lesson:

Ouros should use branching vegetation trajectories. Fire, soil history, seed availability, grazing, hydrology, introduced species and restoration can push two similar sites toward different outcomes.

## Main design conclusions

1. Vegetation needs persistent identity above individual Minecraft blocks.
2. Flowering and seed windows should be versioned through the calendar/phenology system.
3. Pollination should be represented as observed interactions and resource connectivity, not automatic yield multiplication.
4. Seed dispersal requires source/provenance uncertainty.
5. Restoration needs baseline, intervention, follow-up and trajectory, not `restored=true`.
6. Pokémon may be pollinators, seed vectors, browsers, gardeners, nectar users, habitat engineers or observers depending on authored evidence.
7. A single species may interact with plants differently across regions or seasons.
8. Loaded Cobblemon entities must not become the source of truth for plant-population state.
9. A visual flower block does not prove a mechanical berry, Food Item, Grassy Terrain or healing effect.
10. Habitat manipulation can change encounter context before combat begins.

## PTU / AutoPTU boundary notes

File-library evidence shows Python AutoPTU contains exact behavior for `Harvest` when interacting with berry Food Buffs and Weather. That is a battle/food-rule slice, not an overworld plant-growth system. It must not be repurposed as generic harvest or regeneration logic.

The file-library corpus also shows Naturewalk terrain matching in Python. That proves selected movement/habitat mechanics exist in the oracle, not that standing in vegetation grants a free exploration or stealth benefit in Java/Minecraft.

Relevant source evidence:
- `battle_state.py` — Harvest handling and Naturewalk matching in the uploaded project corpus.

No new Caelo-specific plant rule is asserted in this pass unless directly verified against the primary Caelo files.

## Copyright and provenance policy

Store URLs, titles and abstract structural lessons.

Do not copy:

- campaign dialogue;
- source NPCs;
- distinctive story beats in the same sequence;
- fangame locations or factions;
- long Pokédex passages;
- copyrighted prose.

External ecology research may inform system structure, but Ouros cultures and stewardship practices must be authored independently rather than reskinned from specific real communities.

## Candidate next research directions

- fungal ecology and decomposition;
- mycorrhizal/plant–fungus relationships at a high ecological level;
- canopy structure and forest vertical layers;
- browse pressure and herbivory;
- seed banks and long-dormant recruitment;
- orchard/wild-flower interface;
- invasive-plant management as a Biosecurity extension;
- exact PTU/Caelo rules for Honey Gather, Harvest, Naturewalk, Plant-related capabilities, Grass terrain and relevant Moves/Abilities.
