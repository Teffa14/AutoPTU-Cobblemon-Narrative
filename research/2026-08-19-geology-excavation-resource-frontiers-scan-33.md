# Research Scan 33 — Geology, Excavation, Fossils, Mines & Resource Frontiers

Status: RESEARCH ONLY. Not Ouros canon.

Date: 2026-08-19

## Why this pass exists

The repository already covers archaeology, material provenance, conservation, infrastructure, science, public works, workplaces, travel, crisis response and dungeon state. It did not yet have a dedicated model for the ground itself as persistent world state: strata, mineral deposits, excavations, mines, quarries, caves used as workplaces, fossil contexts, depletion, instability, subsurface access and the conflicts created when the same underground place is simultaneously a resource, habitat, heritage site and route.

This pass studies those structures without importing external plots or mechanics.

## Source set

### Official Pokémon — Oreburgh as mine + museum + Gym ecosystem

Source:
https://www.pokemon.com/us/animation/seasons/10/episode-15-shapes-of-things-to-come

The official episode summary presents Roark simultaneously as Gym Leader and mining foreman. Oreburgh mining produces coal and fossil discoveries, and fossils can move into a museum/revival workflow.

Reusable structure:
- one geological site can support employment, research, public education and battle culture;
- discoveries can move through institutions instead of becoming immediate player loot;
- a named professional can have multiple roles tied to the same local identity;
- a fossil find can create consequences outside the excavation itself.

Do not copy Roark, Oreburgh, Cranidos or the episode plot into Ouros.

### Official Pokémon — Mining Museum and revived fossils as institutional state

Sources:
https://www.pokemon.com/uk/animation/seasons/10/episode-16-a-gruff-act-to-follow
https://www.pokemon.com/uk/animation/seasons/10/episode-18-oer-the-rampardos-we-watched

The Mining Museum is more than a display room. It stores scientific equipment, fossils and revived Pokémon. A failure or theft involving that infrastructure produces consequences for scientists, the city and Pokémon.

Reusable structure:
- fossil recovery, analysis, storage, revival and care are different stages;
- institutions can have specialized equipment whose loss creates a service outage;
- revived prehistoric Pokémon should become persistent living entities with care/custody state rather than disposable rewards;
- scientific infrastructure can generate cases, crisis response and later public memory.

### Official Pokémon — excavation boom as a world event

Source:
https://www.pokemon.com/us/animation/seasons/1/episode-43-attack-of-the-prehistoric-pokemon

A fossil discovery at Grampa Canyon triggers a large excavation boom that attracts many explorers.

Reusable structure:
- one verified discovery can radically change visitor pressure on a site;
- rumor, public reporting and scientific confirmation can create different levels of influx;
- an excavation boom can affect safety, habitat disturbance, lodging, transport, markets and stewardship;
- discovery is therefore a possible regional event, not merely an item roll.

### Official Pokémon — Grand Underground mining loop

Source:
https://diamondpearl.pokemon.com/en-au/trainersguide/grandunderground/

The Grand Underground supports repeated digging for fossils, stones, shards, plates and other valuables, with some materials feeding other game systems.

Reusable structure:
- different geological sites can have different yield families;
- underground exploration can support recurring optional play;
- a recovered material can connect to crafting, museums, research or trade;
- repeated excavation needs anti-grind and depletion/restoration rules in Ouros rather than infinite identical nodes.

The mining minigame itself is not imported as an Ouros mechanic.

### PTU-adjacent public rules discussion — fossil quarries

Source:
https://1e.ptr.wiki/Rules/Playtests/Class-Reworks/Researcher

This is not governing PTU/Caelo authority for Ouros. It is a discovery source only.

The public Researcher rework explicitly proposes fossil quarries as campaign locations where characters can search for fossils and other useful geological items, with competence affecting what can be found.

Reusable structure:
- fossil hunting can be an intentional profession/interest rather than a one-time treasure drop;
- quarries can have tiers of discovery without guaranteeing a fossil every visit;
- ordinary findings can still make an expedition worthwhile;
- skill and expertise should affect resolution only through governing PTU/Caelo rules, not through invented Ouros DCs.

### Caelo internal source — route-specific excavation sites

Internal sources supplied to the project:
- `Caelo Region Location & Encounter List.pdf`
- `caelo rulebook merged.pdf`
- related Caelo errata/resource bundle

The supplied Caelo material already contains excavation sites with Easy/Moderate/Hard difficulty labels, route-specific fossil/item tables and locations whose geology is part of their environmental identity.

Important boundary:
- those exact DCs, tables and site contents belong to Caelo material;
- they are useful evidence that excavation fits the PTU/Caelo play style;
- Ouros must not silently copy Caelo route tables or assume those DC values are universal.

### Eevee Expo — Pokémon Mineral

Source:
https://eeveeexpo.com/threads/8356/

Pokémon Mineral builds an entire small fangame around fossil discovery and revival.

Reusable structure:
- fossil specialization can support a complete career fantasy;
- repeated digs can feed a larger research arc;
- revival choices can create persistent consequences around specific Pokémon;
- cave accessibility and excavation progress can be part of the adventure structure.

Do not copy the fangame's characters, Noble Pokémon, plot or unique mechanics.

### Eevee Expo — mining resources and Mining Rig

Sources:
https://eeveeexpo.com/threads/6579/
https://eeveeexpo.com/resources/1907/

These community tools demonstrate that fangame creators repeatedly treat mining as a reusable resource loop and sometimes automate extraction over time.

Reusable lesson for Ouros:
- resource extraction can have infrastructure state;
- extraction rate, site capacity and maintenance should remain authored/systemic state rather than narrative free loot;
- automation creates consequences: staffing, power demand, noise, habitat disturbance, maintenance and depletion.

Do not import their item tables, production rates or scripts.

### Public Pokémon RP — fossil mission archive

Source:
https://gaiaonline.com/guilds/viewtopic.php?page=last&t=21937061

A public Pokémon RP mission archive uses deep excavation as a mission framing device for fossil recovery.

Reusable structure:
- excavation can support a bounded mission with a clear expedition objective;
- depth itself can create staging, navigation and return-plan concerns;
- fossil recovery can be separated from revival and ownership.

Do not reuse its prose or mission details.

### Public roleplay design — mining as activity plus interruptions

Source:
https://www.smogon.com/forums/threads/role-playing-approval-center-update-5-12-13.86090/page-2

A historical community proposal models mining as repeated work punctuated by nearby scenarios, strange sounds, discovered objects and raids on supplies.

Useful abstract lesson:
- productive activity becomes more interesting when the surrounding site continues to act;
- not every excavation complication should be a battle;
- site occupancy, queues, tools, theft, discoveries and hazards can create different types of scene.

Do not import its combat/resource rules.

### Public Pokémon RP — cave ecology around a sought fossil

Source:
https://pokemonuranium.co/forum/showthread.php?pid=73594

A public play-by-post scene places a fossil objective beyond caves already occupied and actively used by wild Pokémon.

Reusable structure:
- a valuable underground target does not erase the current ecology of the cave;
- accessing one layer may require passing through another group's habitat or territory;
- the fossil objective and the living encounter can be related without making the Pokémon guards of human treasure.

Do not reproduce its characters, location or plot.

## High-value design conclusions

### Geological context should persist separately from loot

A fossil or ore node should come from a geological context that can remain after the item is removed.

Useful fields include:
- formation or strata reference;
- site depth band;
- geological age claim;
- confidence level;
- associated fossils/minerals;
- disturbance state;
- access state;
- stability observations;
- water/gas/temperature observations;
- habitat overlap;
- heritage overlap;
- extraction history.

This prevents the world from becoming a set of anonymous resource blocks.

### Finding, extracting and interpreting are different actions

A player may detect something without extracting it.

A recovered object may be genuine while its interpretation is wrong.

A fossil may be scientifically important but unsuitable for revival.

A rich deposit may be physically accessible but protected, unsafe or economically impractical.

These distinctions connect geology to science, cases, conservation, governance and material provenance.

### Fossils need context provenance

For significant fossils, track:
- exact site and layer;
- finder;
- extraction event;
- current custodian;
- preparation/analysis history;
- institutional claims;
- public disclosure state;
- revival eligibility as an unresolved mechanical/scientific field until validated.

Removing a fossil from context can destroy information even when the object remains intact. This creates meaningful decisions without inventing bonuses.

### Underground spaces can have multiple simultaneous identities

The same cave may be:
- a wild Pokémon habitat;
- a mine;
- a transport shortcut;
- a sacred or historical site;
- a research site;
- a water source;
- a dungeon;
- a public attraction;
- a hazardous exclusion zone.

Ouros should model those claims separately rather than forcing one canonical label.

### Resource extraction needs depletion and disturbance memory

Infinite respawning ore is acceptable as a low-level Minecraft convenience only if the narrative layer does not pretend the exact same physical deposit was mined endlessly.

Narratively significant sites should support states such as:
- UNKNOWN
- SURVEYED
- ACTIVE
- PARTIALLY_EXTRACTED
- DEPLETED
- SUSPENDED
- FLOODED
- COLLAPSED
- RESTORING
- CLOSED
- REPURPOSED

The mechanical resource economy can remain abstract where exact depletion is not useful.

### Discovery booms create world events

A rare find can trigger:
- research teams;
- tourists;
- prospectors;
- speculators;
- theft risk;
- conservation pressure;
- transport demand;
- lodging demand;
- misinformation;
- public hearings;
- rival institutional claims.

The boom should depend on publication/rumor propagation from the media layer rather than happen globally the instant a player rolls well.

### Mine safety and geological hazards require an authority boundary

Narrative generation may record observations such as:
- cracked support;
- unusual heat;
- water seepage;
- unstable floor;
- gas warning from an approved sensor;
- recent collapse.

It must not invent:
- falling damage;
- suffocation rules;
- gas damage;
- cave-in damage;
- digging speeds;
- carrying limits;
- Stability DCs;
- Pokémon immunity to geological hazards.

Those need governing PTU/Caelo rules plus implementation support.

## Interaction with existing Ouros layers

Material culture:
Recovered minerals become `material_batch` provenance inputs. This pass defines where geological material comes from and what context is lost or retained.

Archaeology:
Archaeological context and geological context may overlap but are not identical. A mine can accidentally expose ruins; an ancient quarry can become archaeological evidence; a fossil is not automatically an artifact.

Science:
Survey measurements, strata descriptions and fossil analysis feed datasets/hypotheses rather than world truth directly.

Conservation:
Extraction can alter habitat, migration routes, groundwater and nesting areas, but effects must be represented as observed/validated state rather than moral labels.

Governance/public works:
Large extraction projects can require authored decision procedures, stakeholder review and infrastructure dependencies when Ouros canon defines them.

Workplaces:
Mines, quarries, museums, survey crews and laboratories can have staffing, training, shift and maintenance state.

Cases:
Theft, fraudulent provenance, unsafe operations and disputed custody can become cases without defining a universal criminal code.

Crisis:
Collapse, flooding, ventilation failure or route blockage can create crisis objects when the relevant hazard state is validated.

Dungeon grammar:
Subsurface sites can use persistent dungeon state, alternate access, return expeditions and changed ecology.

## Copyright boundary

Store titles, URLs, metadata, factual system descriptions and high-level patterns.

Do not copy:
- fanfiction or RP prose;
- episode dialogue;
- distinctive original characters;
- unique fangame plots;
- exact homebrew item tables or mechanics unless separately licensed and intentionally adopted.

## Questions for later canon/mechanics review

- Which Ouros regions are geologically distinct?
- Which deposits, fossils and stone resources are authored as region anchors?
- How much of Caelo's excavation framework should be preserved?
- Which PTU Skills, Edges, Features or Capabilities legally govern excavation and fossil work?
- How are fossil ownership, custody, museum claims and revival permission handled?
- Can revived fossil Pokémon be released, donated or institutionally cared for while preserving provenance?
- What geological hazards exist mechanically in AutoPTU versus only as overworld state?
- What Cobblemon/Minecraft hooks can represent meaningful depletion without turning the world into strip-mining simulation?
- How are subsurface spaces preserved when chunks regenerate, update or are modified by players?
