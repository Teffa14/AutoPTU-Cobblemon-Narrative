# Ouros Research Scan — Demography, Migration & Population Change — Pass 60

Status: research only. Not canon. External sources are inspiration/evidence sources, not authority for PTU mechanics.

Date: 2026-08-20

## Why this pass exists

The repository already models housing, workplaces, interregional mobility, tourism, crisis displacement, settlement growth, transport, public works and institutions. What is missing is a shared population layer that can answer:

- who normally lives in a settlement;
- who is temporarily present;
- who commutes rather than resides;
- who recently arrived or left;
- which population changes are observed versus inferred;
- how a discovery, crisis, new route or institution changes local demand;
- how to preserve individual NPC continuity without simulating every resident;
- how demographic change becomes visible in Minecraft without spawning an entire census.

## New source findings

### 1. Pokémon Legends: Arceus — Jubilife Village as a settlement formed by arrivals

Official source:
https://legends.arceus.pokemon.com/en-ca/story/

The official story page describes Jubilife Village as the base of the Galaxy Expedition Team, whose members came from various regions to study Hisui. The settlement also contains multiple specialized corps and services.

Reusable structure:

- a settlement can be populated by people with different regions of origin;
- institutional purpose can be a major migration driver;
- one settlement can grow around a shared expedition/research project;
- service capacity and resident composition can be linked without implying nationality or citizenship systems.

Do not copy Galaxy Team, Jubilife, Hisui or its characters into Ouros.

### 2. Pokémon Legends: Z-A — redevelopment changes human/Pokémon use of one city

Official sources:
https://legends.pokemon.com/en-us/news/adventure
https://legends.pokemon.com/en-au/story-world/lumiose-city

Lumiose City is undergoing redevelopment intended to support coexistence between humans and Pokémon. New green areas and Wild Zones are inserted into an already active urban environment with cafés, restaurants, shopping areas, parks and waterfronts.

Reusable structure:

- urban change can alter where residents, visitors and Pokémon spend time;
- population pressure should be modeled by zone, not only by settlement total;
- new infrastructure can redistribute daily presence without changing residence;
- human and Pokémon occupancy can interact without sharing one population model.

### 3. PTU Campaign Seed: Mysterious Ruins — discovery-driven population growth

Source:
https://pokemontabletop.com/campaign-seeds-mysterious-ruins/

The campaign seed explicitly proposes that outside discovery of a local ruin can produce an explosion in population, immigration, tourism, merchant activity and growth from town toward city.

Reusable structure:

- one discovery can create multi-system demographic pressure;
- new residents and temporary visitors should remain distinct;
- housing, shops, transport and jobs can change because of population inflow;
- growth can become a long arc rather than a one-time settlement upgrade.

This source is especially relevant because it is directly PTU campaign-design material.

### 4. Pokémon Coda — immigrant-founded districts and cultural persistence

Source:
https://eeveeexpo.com/coda/

The public project description presents Prima City as a diverse metropolis built through immigration, with districts shaped by people arriving from different places. Johtotown is described as a district founded by people from Johto and neighboring regions, while tourism creates pressure around local culture.

Reusable structure only:

- migration can create districts with persistent cultural identity;
- visitor pressure and resident identity are separate state;
- later arrivals need not erase earlier settlement layers;
- one city can have multiple demographic histories at once.

Do not import Prima City, Johtotown, characters, Team Pepper or plot.

### 5. Pokémon Libertas — moving into a region as a player premise

Source:
https://eeveeexpo.com/threads/7403/

The project begins with the player moving into a region to start a new life/journey.

Reusable structure:

- arrival can be a persistent change of residence rather than tourism;
- newcomer orientation can be meaningful without treating the character as incompetent;
- moving should update housing, local knowledge, services and social context separately.

### 6. Minecraft settlement-generation research

Sources:
https://arxiv.org/abs/1803.09853
https://arxiv.org/abs/2103.14950

The GDMC settlement-generation work emphasizes settlements that adapt to the existing map and are functional, believable and holistic rather than stamped from a fixed template.

Reusable structure:

- population growth should alter a settlement only where geography and infrastructure permit;
- new housing and services should follow physical constraints;
- visual growth should be driven by world-state demand rather than arbitrary expansion.

### 7. Population/migration simulation research — use only at a coarse level

Sources:
https://arxiv.org/abs/2109.03182
https://arxiv.org/abs/2412.20691

Agent/population models show that migration responds to environmental conditions, density, risk and incentives. They also show how quickly complexity grows when individual agents are simulated.

Reusable lesson for Ouros:

- use explicit migration drivers and coarse cohorts;
- keep important named actors as individuals;
- avoid simulating every unnamed resident as an autonomous agent;
- preserve causal explanations for large population shifts.

Do not import real-world demographic categories or assumptions into Ouros automatically.

## Proposed high-level design lessons

1. Residence, presence and origin must remain separate.
2. Population estimates are observations, not perfect truth.
3. Named NPCs remain individual entities; background population may use cohorts.
4. Temporary visitors, seasonal workers, students, commuters, evacuees and permanent residents must not be collapsed into one count.
5. Growth needs causal drivers such as jobs, institutions, discoveries, transport or safety.
6. Decline also needs causes; do not depopulate a town only to make it dramatic.
7. Displacement caused by crisis is not automatically permanent migration.
8. Arrival from another region does not imply nationality/citizenship/legal status.
9. Cultural identity can persist across migration but cannot be inferred from origin alone.
10. Multiplayer privacy matters: exact household/residence records may be private even when aggregate population is public.
11. Census-like records can be incomplete, delayed or politically disputed without changing world truth.
12. Pokémon population ecology remains separate from human/NPC demography, though both can affect shared locations.

## Narrative structures worth reusing

- boomtown after discovery;
- research settlement built around one institution;
- seasonal-worker influx;
- commuter settlement around a transport hub;
- settlement aging after young workers leave;
- housing shortage after an event-driven influx;
- former temporary lodging becoming permanent neighborhood;
- evacuees who later choose whether to return;
- multi-district city with different settlement histories;
- new route causing one district to grow while another loses foot traffic;
- institution closure creating gradual out-migration;
- school/academy expansion creating temporary residents;
- conservation policy redistributing where people can stay or work;
- revived settlement after restoration of transport/services;
- census mismatch caused by commuters, visitors or stale records.

## PTU / Caelo mechanical boundary

No source in this scan authorizes new PTU mechanics.

Do not generate:

- migration Skill checks;
- social bonuses based on population size;
- crowd combat modifiers;
- housing bonuses;
- morale modifiers;
- encounter difficulty scaling from population counts;
- legal residence rules;
- citizenship systems;
- demographic stat bonuses;
- automatic Pokémon obedience based on settlement norms.

PTU/Caelo rules remain authoritative for any Skill, Feature, item, battle or capture mechanic.

## Copyright / originality boundary

External works in this scan are used for abstract structure only. Ouros must not copy:

- named cities or districts;
- characters;
- dialogue;
- distinctive plots;
- unique factions;
- proprietary mechanics;
- passages of prose.

## Research gaps for later passes

- exact PTU/Caelo rules relevant to crowd scenes, social Skill checks and large-group encounters;
- Minecraft implementation strategy for cohort presence without thousands of NPCs;
- whether Cobblemon exposes stable APIs useful for separate Pokémon population-state projection;
- privacy model for resident records in multiplayer;
- how settlement population estimates are published or disputed in canon;
- whether Ouros regions have formal census institutions at all.