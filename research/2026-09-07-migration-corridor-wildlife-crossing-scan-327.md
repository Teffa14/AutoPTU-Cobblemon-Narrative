# Migration corridors, stopovers & wildlife crossings scan — Pass 327

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-07
Canon effect: NONE. External material below is inspiration/evidence, not Ouros canon or PTU rules authority.

## Why this slice

The recursive repository inventory and repository-wide searches were reviewed before authoring. Existing work already covers travel, transport, wild collectives, route state, seasonal phenology, floodplains, winter access, infrastructure continuity, survey control and introduced-species management. No dedicated workstream was found for migration corridors, stopover dependence, wildlife-crossing structures, crossing observations or the difference between a physically available crossing and one actually used by a population.

This slice focuses on a reusable world problem: a road, rail line, canal or other linear barrier can remain operational for people while changing ecological connectivity. A mitigation structure can also remain physically intact while becoming less useful because approach habitat, disturbance, water, fencing, maintenance or seasonal timing changed.

## Source 1 — USGS: fish and wildlife migration corridors

URL: https://www.usgs.gov/publications/land-air-and-water-us-geological-survey-science-supporting-fish-and-wildlife

USGS describes migration as movement between habitats used for feeding, reproduction and raising young. Corridors can be species-specific and can be disrupted by development or by natural disturbances such as drought, fire and flooding.

Reusable Ouros structures:
- migration is a relationship between multiple seasonal habitats, not a single spawn point;
- a corridor has temporal windows and species-specific relevance;
- a disturbance can reduce corridor usefulness without erasing either endpoint habitat;
- the same route may matter differently to different populations;
- later observation can reveal changed movement rather than a simple population disappearance.

## Source 2 — USGS: corridor and stopover use

URL: https://www.usgs.gov/publications/corridor-and-stopover-use-hawaiian-goose-branta-sandvicensis-intratropical-altitudinal

USGS research on Hawaiian geese separates migration corridors from stopovers and shows that movement patterns can vary in timing, direction and number of intermediate stops.

Reusable Ouros structures:
- `CORRIDOR_USED != NONSTOP_TRANSIT`;
- temporary stopover sites can be disproportionately important despite short occupancy;
- one failed stopover can alter arrival timing without blocking the entire corridor;
- different subpopulations can use the same broad landscape differently;
- a monitoring system should preserve observation time and population identity.

No species, location or statistical model from the study is imported into Ouros.

## Source 3 — FHWA: wildlife crossing structures

URL: https://www.fhwa.dot.gov/clas/ctip/wildlife_crossing_structures/ch_4.aspx

FHWA describes wildlife crossings as structures intended both to reconnect habitat and reduce road mortality. It distinguishes overpasses, underpasses, modified culverts, canopy crossings and other forms, and emphasizes that suitability depends on species, terrain, habitat, water and human disturbance.

Reusable Ouros structures:
- `CROSSING_EXISTS != CROSSING_SUITABLE_FOR_EVERY_SPECIES`;
- a crossing can serve wildlife, humans or both, depending on design and management;
- approach habitat and fencing can matter as much as the opening itself;
- crossing placement is a landscape decision rather than a universal spacing rule;
- infrastructure maintenance can alter ecological function without closing the human route.

Do not import US engineering standards or legal requirements as Ouros law.

## Source 4 — NPS: Tucson Mitigation Corridor

URL: https://www.nps.gov/sagu/learn/nature/connections-tucson-mitigation-corridor.htm

NPS describes a corridor where infrastructure would interrupt wildlife movement and multiple crossing structures were used to maintain linkage across the barrier. Monitoring later documented use by several species.

Reusable Ouros structures:
- mitigation can be a network rather than one heroic structure;
- different crossing points can have different evidence histories;
- maintenance records and wildlife observations can disagree in scope without either being false;
- crossing use should be observed, not assumed from construction completion;
- a project can create durable stewardship obligations after its original construction arc ends.

## Source 5 — NPS Glacier map-a-thon

URL: https://www.nps.gov/glac/learn/news/19-39.htm

Glacier National Park asked residents to contribute observations of where, when and which species crossed or attempted to cross a transport corridor. The observations were used to identify candidate mitigation locations.

Reusable Ouros structures:
- community knowledge can enter an institutional evidence system through explicit reports;
- failed crossing attempts are data, not only successful crossings;
- repeated observations can reveal a bottleneck;
- public reports require provenance, time and species identity;
- crowdsourced evidence can guide investigation without becoming automatic world truth.

## Source 6 — Pokémon Sawsbuck species material

Reference: official-series Pokédex text reproduced across current Pokédex databases; Black/Black 2-era entries state that Sawsbuck migrate according to the seasons and that their seasonal appearance is used as a sign of seasonal change.

Supporting public reference: https://pokemondb.net/pokedex/sawsbuck

Reusable Ouros structures:
- Pokémon canon already supports at least one species whose ecology includes seasonal migration;
- seasonal appearance can become an observation channel without granting mechanical foresight;
- migration timing can become culturally meaningful to nearby communities;
- herd leadership or route choice must still be species-grounded and observed, not inferred from one Pokédex line.

This does not define PTU movement speed, Overland capability, herd bonuses, encounter frequency or Sawsbuck behavior in Ouros.

## Source 7 — Pokémon Wild Area official design

URL: https://swordshield.pokemon.com/en-us/gameplay/wild-area/

The official Wild Area material establishes that Pokémon presence can vary with location and weather in a broad connected wilderness.

Reusable Ouros lesson:
- repeated traversal of one landscape can reveal different ecological states;
- changing encounter composition can communicate world state;
- the player can learn a region through revisits rather than one-time route completion.

No Galar geography, weather table or encounter data is imported.

## Source 8 — Pokémon Rollout! PTU actual play

URL: https://www.podchaser.com/podcasts/pokemon-rollout-238076

Public listings identify Pokémon Rollout! as a long-running real-play Pokémon Tabletop United campaign with more than two hundred published episodes.

Reusable Ouros lesson:
- PTU can sustain recurring locations, relationships, investigations and battles across long continuity;
- an ecological corridor problem can recur after many sessions because infrastructure, NPC obligations and population movement persist;
- a later visit should expose accumulated consequences rather than reset the route.

No characters, dialogue, plots, gyms or episode content are imported.

## Source 9 — fan ROM-hack development example: Legends of Hoenn / Agent Oak

URL: https://github.com/alvarodms/agentoak

The public project describes migration as a world-scale premise that changes encounter tables, weather incidents, NPC observations and later regional interpretation.

Reusable Ouros lesson:
- migration can be communicated through multiple systems at once: sightings, changed local abundance, institutions, travel reports and environmental events;
- not every migration event needs to become a battle;
- repeated cross-references between NPCs can make ecological change legible when each NPC only knows what they observed or received.

The project's characters, dialogue, regional forms, plot beats and encounter tables are not imported.

## Original Ouros design lessons

1. Population movement, route connectivity and crossing use are separate facts.
2. A corridor is time-dependent and population-specific.
3. A crossing may be physically open while ecologically ineffective.
4. A crossing may be ecologically useful while the adjacent human route remains restricted.
5. Stopovers can matter even when occupancy is brief.
6. Failed crossing attempts and diverted movement are evidence.
7. Maintenance completion does not prove wildlife use.
8. Observation of use does not prove every member of a population crossed.
9. NPCs know only observations, reports and records actually received.
10. Minecraft entities or pathfinding traces are presentation unless admitted as authoritative observations.

## PTU / Caelo cross-check boundary

The narrative repository currently exposes `sources/kairos`; no adopted `sources/caelo` directory was visible in the current source inventory. The project README requires exact source validation before inventing movement rates, environmental penalties, encounter mechanics, Features, item behavior or Pokémon capabilities.

This research therefore does not define:
- Sawsbuck movement, herd or migration mechanics;
- Overland/Swim/Sky rates;
- tracking or Survival DCs;
- road-collision damage;
- panic, stampede or herd statuses;
- forced movement near vehicles;
- interception/rescue actions;
- weather movement modifiers;
- crossing-specific bonuses;
- Trainer Feature or Ability effects.

Any such behavior remains UNVERIFIED until checked against project-authoritative PTU/Caelo material and current AutoPTU evidence.

## Candidate implementation direction

Use migration corridors as persistent world-state relationships:

`population identity -> seasonal habitat need -> corridor segment -> stopover dependency -> barrier/crossing state -> observation -> actor receipt -> interpretation -> institutional response -> later movement evidence`

This fits the global NPC AI because rangers, road crews, researchers, residents and logistics actors can receive different evidence, make different bounded decisions and revisit the same corridor without creating omniscient ecological knowledge.