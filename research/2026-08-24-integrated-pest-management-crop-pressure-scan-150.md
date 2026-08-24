# Research Scan 150 — Integrated Pest Management, Crop Pressure & Agricultural Coexistence

Status: research/provenance only. Not established Ouros canon.
Date: 2026-08-24

## Why this scan exists

The repository already has Food/Agriculture, Interspecies Ecology, Flora, Soil, Biosecurity, Toxicology, Food Safety and Working Pokémon. Food mentions `pest warning`, but there is no dedicated owner for scouting a field, distinguishing damage from cause, deciding whether action is justified, recording interventions or checking what happened afterward.

This pass researches that missing layer. It does not define pesticides, crop yields, Pokémon population control or PTU combat effects.

## Existing Ouros boundaries inspected

`design/food-agriculture-hospitality-layer.md` owns agricultural sites, cultivation cycles and harvest context. It already allows narrative activities such as pollination support and pest warning but explicitly keeps mechanical capability validation separate.

`design/interspecies-ecological-relations-layer.md` owns ecological relations and pressure. It requires evidence before causal claims and states that tactical battle outcomes do not automatically become ecological outcomes.

Related authorities remain unchanged:

- Flora owns flowering, recruitment and vegetation trajectories.
- Soil owns compaction, erosion and land restoration.
- Biosecurity owns introduced-species/translocation questions.
- Toxicology owns hazardous-agent exposure and source attribution.
- Food Safety owns downstream handling/traceback after harvest.
- Pokémon Agency and Working Pokémon own individual agency, assignments and consent/participation.

## Public Pokémon material

### How Are You Gonna Keep ’Em Off of the Farm?

Source: Pokémon official animation page.
https://www.pokemon.com/us/animation/seasons/24/episode-4-how-are-you-gonna-keep-em-off-of-the-farm

A farm experiences an apparent Diglett/Dugtrio problem. Investigation finds that the group had been displaced from a nearby hill by loud music and moved onto the farm afterward.

Reusable structure:

observed agricultural conflict -> identify the organisms -> investigate why pressure changed -> find an external driver -> resolve the driver or access problem rather than treating the visible Pokémon as the whole cause.

Ouros lesson: an organism causing crop or soil pressure at a site can still be responding to another disturbance. `target_organism` must not become `root_cause` automatically.

### The Apple Corp!

Source: Bulbapedia episode summary, used only for high-level structure.
https://bulbapedia.bulbagarden.net/wiki/EP179

Hungry Pichu enter an orchard because wild fruit is scarce. The final arrangement changes the relationship between orchard and Pokémon rather than simply removing the group.

Reusable structure:

resource shortage outside managed land -> foraging pressure inside managed land -> initial blame -> ecological explanation -> negotiated/coexistence outcome.

Ouros lesson: agricultural losses can be downstream of landscape-scale resource change. A management response can alter access or incentives instead of requiring capture, KO or eradication.

### Awakening the Sleeping Giant!

Source: Pokémon official animation page.
https://www.pokemon.com/us/animation/seasons/17/episode-18-awakening-the-sleeping-giant

Camphrier Town maintains a recurring harvest relationship with Snorlax: after harvest, Snorlax clears roots and the community treats the event as useful rather than as crop destruction.

Reusable structure:

the same feeding/removal behavior can be harmful in one phase of a cultivation cycle and useful in another.

Ouros lesson: management classification must be scoped by place, season and objective. The same species cannot carry a permanent global `PEST` tag.

### Greedent

Source: official Pokédex.
https://www.pokemon.com/us/pokedex/greedent

Greedent is strongly associated with gathering berries. This supports authored foraging pressure where appropriate but does not prove crop damage, theft, population density or intent at a specific Ouros farm.

### Applin

Source: official Pokédex.
https://www.pokemon.com/us/pokedex/applin

Applin lives inside an apple and feeds on it, while its presence is also described as strengthening the apple skin against rot. This is useful specifically because the interaction is not reducible to a clean harmful/beneficial binary.

Ouros lesson: visible occupation or feeding can coexist with another ecological effect. Management should preserve competing observations rather than force a single label.

## Public PTU / actual-play material

### Late Starters — Episode 10, Thank You Berry Much

Source: public podcast index.
https://podbay.fm/p/late-starters-a-pokemon-tabletop-rpg-adventure

The episode premise uses many wild Rattata eating a berry farmer’s crop and asks the party to help the farmer deal with the orchard pressure.

Reusable structure:

small livelihood problem -> visible wild aggregation -> field response -> party involvement.

For Ouros, the important improvement is to make the diagnostic layer persistent. Before selecting an intervention, the world should be able to ask whether the aggregation is new, whether fruit loss is actually above baseline, what conditions changed, and what happened after intervention.

### PTU Campaign Structure guidance

Source: Pokémon Tabletop Wiki mirror of campaign guidance.
https://pokemontabletop.fandom.com/wiki/Campaign_Structure

The guidance recommends maintaining varied activities and preserving room for standalone scenarios rather than making every session part of the central threat.

Ouros lesson: an orchard-pressure investigation can remain a local professional problem. It does not need to reveal a criminal faction or escalate into a regional conspiracy.

## Integrated pest management research

### EPA Integrated Pest Management Toolkit 2021

Source:
https://www.epa.gov/system/files/documents/2021-07/integrated-pest-management-toolkit-2021_2.pdf

Useful structural concepts:

- inspection is systematic examination rather than one sighting;
- monitoring is repeated observation used to support decisions;
- an action threshold is the point at which conditions justify intervention;
- environmental conditions can make a site more attractive or vulnerable;
- prevention, documentation and evaluation are part of management;
- chemical treatment is not the only possible response.

The document concerns real-world facilities and regulation. Ouros should import only the information architecture, not US law, certification, pesticide labels or health claims.

### USDA National Roadmap for Integrated Pest Management

Source:
https://www.ars.usda.gov/arsuserfiles/opmp/ipm%20road%20map%20final.pdf

Useful structural lesson: effective management combines identification, monitoring, prevention and multiple possible control approaches while considering environmental and economic consequences.

Ouros adaptation: interventions should be typed and reviewed. A cultural, physical, habitat, biological or chemical intervention can have different downstream authorities and non-target questions.

## Core design lessons extracted

1. `PEST` is a scoped management role, not a species trait.
2. Damage observation and cause identification are separate records.
3. Presence alone does not require intervention.
4. Monitoring effort must be preserved; no detections do not automatically mean absence.
5. Thresholds should be versioned because site objectives, seasons and evidence can change.
6. Prevention and habitat/site modification should be first-class interventions, not merely flavor before combat.
7. Biological control or translocation must hand off to Biosecurity/Conservation and Pokémon Agency where relevant.
8. Chemical interventions require Toxicology/Air Quality/Soil/Freshwater review; this layer must never invent exposure effects.
9. Beneficial and non-target organisms need observations of their own.
10. A management action requires post-intervention monitoring. `action completed` is not `problem solved`.
11. A Pokémon battle can remove an immediate confrontation but cannot determine crop-loss attribution or long-term control success.
12. Loaded Cobblemon entity count cannot become infestation or population truth.

## PTU / Caelo mechanical guardrails

Public PTU material confirms many concrete Moves, Abilities, Items and Trainer Features exist, but this scan did not find an authoritative project rule that creates a generic agricultural-pest subsystem.

Do not infer:

- Bug Type = pest;
- Grass Type = crop benefit;
- Poison Type = pesticide resistance;
- Honey Gather/Harvest = agricultural yield simulation;
- Bug Bite = crop consumption in the overworld;
- Sweet Scent = guaranteed pest attraction;
- Naturewalk = farming skill;
- damaging a wild Pokémon = crop protection outcome;
- a pesticide-like narrative substance = Poisoned, Badly Poisoned, damage or a hazard zone.

Any exact PTU effect must remain in the authoritative battle engine and be validated independently.

## Source novelty / duplication check

The branch inventory through Pass 149 was inspected before writing. No dedicated integrated-pest-management or crop-pressure layer was present. Existing agricultural, ecological, toxicological and biosecurity files were treated as upstream/downstream authorities instead of being duplicated.

## Candidate handoffs

Food/Agriculture -> crop/site objective and cultivation stage.
Flora/Soil -> vegetation and land condition.
Pest Management -> scouting, pressure assessment, threshold and intervention history.
Interspecies Ecology -> ecological relation and broader population pressure.
Biosecurity -> introduced organism/translocation or biological-control release.
Toxicology/Air Quality/Freshwater/Soil -> hazardous-agent exposure or environmental contamination.
Food Safety -> post-harvest lot/food consequences.
Pokémon Agency/Working Pokémon -> individual Pokémon participation.
Battle -> only a bounded confrontation after the world state has already defined the scenario.