# Ouros Narrative Research — Stormwater, Drainage & Flood-Control Continuity — Pass 108

Status: RESEARCH ONLY. This file records provenance and design lessons. Nothing here is automatically Ouros canon.
Date: 2026-08-28

## Scope and repository-gap check

The complete recursive repository tree was inspected at baseline `7a58c7123a0ad4d7427e77788bbf9ab4f7f3a0c6` and returned `truncated=false`.

Adjacent systems were checked before selecting this topic:

- Water Management already owns managed freshwater systems such as dams, reservoirs, intakes, canals, gates, spillways and diversions.
- Drinking-Water Continuity owns treatment and distribution after an authorized source-water handoff.
- Waste/Sanitation owns wastewater, contamination observations, cleanup, waste treatment and wastewater overflow state.
- Weather owns forecasts and observed weather.
- Roads/Bridges owns traveler-facing road closure, detour and reopening state.
- Facility Maintenance owns asset condition, inspection, repair and verification.
- Crisis/Rescue owns emergency response and recovery cases.
- Infrastructure Outage owns multi-service cascade and restoration dependencies.

No dedicated layer was found for stormwater collection and drainage as an operational network: catchment sectors, inlets/catch basins, storm-drain links, culverts, detention/retention assets, drainage pump stations, outfalls, temporary pumping, blockage observations and staged post-flood restoration.

Pass 108 therefore studies that narrow gap. It does not create a hydraulic simulator and does not merge sanitary wastewater with storm drainage.

## Public Pokémon sources

### Castelia Sewers — seasonal topology and persistent below-grade space

Source: https://bulbapedia.bulbagarden.net/wiki/Castelia_Sewers

Black 2/White 2 uses Castelia's underground network as a persistent explorable place with multiple surface connections. Water state changes seasonally: some areas are flooded in some seasons and dry in others, changing which passages are accessible.

Reusable lesson:

- below-grade infrastructure can remain the same named place while access topology changes;
- a wet state and a dry state can each expose different routes;
- underground infrastructure can connect ordinary urban spaces, hidden access and wildlife without becoming a disposable dungeon.

Ouros transformation:

A drainage corridor may preserve stable identity across rainfall events and seasons while access observations, closure state and safe inspection paths change. Minecraft water level must not become the authority for access or PTU terrain.

Excluded:

- Castelia's exact map;
- Hugh, Colress, Team Plasma or story sequence;
- encounter tables, items or rewards;
- any inference that Ouros sanitary sewers and storm drains share the same topology.

### Pokémon Ranger Waterworks — infrastructure as mission space without species causation

Source: https://bulbapedia.bulbagarden.net/wiki/Waterworks

Source cross-check: https://www.pokepedia.fr/Aqueducs

Pokémon Ranger uses Fall City's underground Waterworks as an operational urban space where Rangers investigate and remove displaced Grimer. The later reveal separates the visible Pokémon presence from the actual cause of that presence.

Reusable lesson:

Infrastructure missions become stronger when the player first sees a symptom, then gathers enough context to separate location, affected service, Pokémon presence and causal responsibility.

Ouros transformation:

A blocked or occupied drain can be investigated without declaring the nearby Pokémon responsible. Drainage observations, ecological observations and case claims must keep separate provenance.

Excluded:

- Ranger capture mechanics;
- Grimer as a default drainage species;
- the Go-Rock Squad plot;
- any universal sanitation or toxicity rule.

### “Leading a Stray!” — drains as habitat and urban connection

Source: https://bulbapedia.bulbagarden.net/wiki/Leading_A_Stray

The anime depicts an underground drain/sewer area supporting a persistent group of Pokémon beneath an active city. Surface access points connect the hidden space to ordinary urban life.

Reusable lesson:

Underground utility space can simultaneously be infrastructure, route, shelter/habitat and social territory. Those roles should coexist through references rather than one system silently owning all of them.

Ouros transformation:

Drainage owns only operational water-removal state. Conservation/Wildlife owns habitat interpretation. Residential, Roads and Public Space own consequences above ground. Pokémon presence alone does not establish ownership, blockage, contamination or hostility.

Excluded:

- the episode's Pokémon group structure and leader;
- its rescue sequence;
- any assumption that urban drains are normally inhabited.

### “Absol-ute Disaster” — warning evidence versus blamed cause

Source: https://bulbapedia.bulbagarden.net/wiki/Absol-ute_Disaster

A settlement blames an Absol for repeated destructive events before later evidence shows the Pokémon was warning about a developing flood threat rather than causing it.

Reusable lesson:

Environmental continuity needs explicit separation between warning observations, public attribution, actual physical cause and later causal review.

Ouros transformation:

A Pokémon repeatedly appearing near an inlet, culvert, creek crossing or flood-prone street can become a clue or observation history without becoming the cause. A post-event investigation may revise public understanding without deleting the earlier belief from Public Memory.

Excluded:

- Absol's exact role or powers as a universal flood sensor;
- the episode's characters and boulder solution;
- flood-diversion mechanics from anime action.

### Public PTU campaign premise — consequences can outlast the disaster

Source: https://www.reddit.com/r/PokemonTabletop/comments/1hgbuha

A public PTU campaign advertisement describes a region transformed by severe weather and disasters, with survivors relocated and later expeditions emerging into a changed world decades afterward.

This is not a rules source and its plot is not copied.

Reusable lesson:

An environmental event can change settlement access, population patterns, routes and exploration for far longer than the dramatic incident itself. Recovery state can be the campaign environment rather than a short epilogue.

Ouros transformation:

Flood-control work should leave durable detours, temporary pumps, abandoned drainage alignments, changed habitat, revised inspection routines and public memory that can matter in later arcs.

## Operational references used only for state-model inspiration

### Stormwater assets are not one monolithic object

Source: https://www.epa.gov/sites/default/files/2020-01/documents/final_draft_stormwater_finance_task_force_report_for_board_review.pdf

The EPA task-force report describes maintenance of catch basins, storm-sewer systems, pump stations, flood barriers and detention basins as distinct operational assets.

Reusable design lesson:

Ouros should model authored asset types and dependencies rather than one global `drainage_ok` flag.

No American funding model, permit, engineering standard, capacity value or compliance requirement is imported.

### Local drainage fixes can precede system-wide solutions

Source: https://www.nyc.gov/site/dep/news/23-007/dep-upgrades-drainage-infrastructure-jewel-streets-neighborhood-ease-chronic-flooding

NYC describes targeted catch-basin and storm-sewer improvements at repeatedly flooded intersections while longer-term solutions continue.

Reusable design lesson:

A localized mitigation can improve one trouble spot without proving that the wider system is fully upgraded or that future flooding is impossible.

### Culverts require explicit inspection after major events

Source: https://www.fhwa.dot.gov/infrastructure/asstmgmt/tamcs_cms06.cfm

The FHWA case study describes routine culvert inspection plus interim inspection after large storms or reported damage.

Reusable design lesson:

`water receded` and `crossing inspected` are different states. A road or trail owner can wait on drainage-asset verification even after the visible flood disappears.

No real-world inspection interval or condition-rating system is imported.

### Stormwater pumping is its own operational dependency

Source: https://www.nyc.gov/site/dep/news/19-074/to-reduce-flooding-the-prospect-expressway-stormwater-pumping-station-gets-10-million-upgrade

The source documents a dedicated stormwater pumping station serving a flood-prone transport corridor.

Reusable design lesson:

Gravity drainage and pumped drainage should be representable as different authored paths. A pump can be available while its upstream inlet, downstream path or power dependency is not.

No pump capacity, rainfall design criterion or engineering formula is imported.

## PTU / Caelo cross-check

The project's internal source scan identifies the PTU Core Rulebook, Caelo Player's Guide, Caelo Region Location & Encounter List, character-creation material, errata/extras and Pokédex material as governing sources available to the project.

Caelo demonstrates that a location may have an authored environmental mechanical condition when the source explicitly defines one. That precedent does not create a generic flood, current, drowning, slippery-surface or drainage rule.

Nothing inspected supports inventing universal mechanics for:

- rainfall-to-water-depth conversion;
- storm-drain capacity;
- culvert flow;
- catch-basin blockage probability;
- flood-current forced movement;
- drowning/suffocation;
- contaminated floodwater status effects;
- slippery pavement;
- pump output;
- structural collapse from inundation;
- debris impact damage;
- Water-type immunity to flood hazards;
- Electric-type interaction with flooded equipment;
- species-level drain-clearing or flood-warning jobs;
- Move-powered pumping, diversion or drainage;
- generic Trainer Feature bonuses to flood-control work.

Any tactical effect needs an exact PTU/Caelo rule or a separately approved encounter contract backed by current AutoPTU implementation.

## Originality and provenance rules for Pass 108

Pass 108 takes only high-level structures:

- persistent underground locations whose access changes;
- symptoms that do not prove cause;
- warning evidence separated from public blame;
- infrastructure that is both operational space and ecological interface;
- local mitigation versus system-wide recovery;
- post-event inspection before reopening;
- staged drainage restoration;
- long consequences after a weather event.

It does not copy protected prose, dialogue, map layouts, distinctive characters, encounter sequences, puzzle solutions or plots.

## Design directions produced by this scan

The strongest implementation-facing candidates are:

1. a stable stormwater/drainage network identity with authored catchment sectors;
2. separate inlet, conveyance, culvert, storage, pump and outfall records;
3. rainfall/flood observations that reference Weather without duplicating it;
4. blockage and access observations that do not assert cause;
5. temporary pumping/bypass state;
6. staged restoration where visible drainage, inspection, road reopening and downstream recovery remain separate;
7. ecology links that never convert Pokémon presence into causal truth;
8. mechanically rich flood encounters with reduced dry/static versions until environmental, forced-movement, tactical-policy and playback families mature.