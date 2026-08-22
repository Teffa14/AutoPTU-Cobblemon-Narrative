# Groundwater, Aquifers, Wells & Springs Research Scan — Pass 109

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. Not a PTU rules source.

Date: 2026-08-22

## Why this pass exists

The repository already has `freshwater-watersheds-hydrology-layer.md`, which deliberately models groundwater only as a linked coarse system. It can say that a spring weakens while a river looks normal, or that surface and groundwater are connected, but it does not own aquifer storage, recharge areas, wells, pumping drawdown, well interference, groundwater travel time, spring capture, monitoring networks, or historical well fields.

No dedicated groundwater/aquifer layer exists in the current design inventory. This pass fills that gap without replacing Freshwater, Geology, Sanitation, Estuaries, Aridity, Volcanism, Agriculture, Health Surveillance, Infrastructure, or Science.

## Source scan

### Pokémon — “A Watershed Moment!”

Source: Pokémon.com, Season 19 Episode 15, “A Watershed Moment!”
https://www.pokemon.com/us/animation/seasons/19/episode-15-a-watershed-moment

High-level pattern:
- a damaged landscape cannot recover simply because people want it to;
- characters investigate for an underground water source;
- the source exists physically but is blocked;
- releasing it changes later ecological conditions rather than instantly restoring a mature forest;
- repair, hydrology, Pokémon cooperation, and ecological recovery form one causal chain.

Reusable Ouros lesson:
An underground-water discovery can be the middle of a restoration arc, not the reward screen at the end. Finding water establishes a new dependency. It does not prove sustainable yield, water quality, long-term recharge, ownership, or universal access.

Copyright boundary:
Do not copy Robon, the episode’s characters, location, dialogue, exact obstruction, or plot sequence. Reuse only the abstract pattern investigation → source discovery → intervention → delayed ecological response.

### Pokémon Brilliant Diamond / Shining Pearl — Grand Underground / Fountainspring Cave

Source: official Pokémon BDSP Trainer’s Guide
https://diamondpearl.pokemon.com/en-au/trainersguide/grandunderground/

High-level pattern:
- underground spaces can contain persistent water-rich environments distinct from surface geography;
- subterranean water can structure habitat and species presence;
- underground exploration is spatially connected to multiple surface settlements while retaining its own geography.

Reusable Ouros lesson:
Aquifers, caves, underground streams, springs, and surface catchments should be related through explicit links rather than treated as the same water body. A cave pool can be ecologically important without being the regional aquifer itself.

Copyright boundary:
Do not copy Sinnoh geography, Fountainspring Cave layouts, encounters, items, or progression.

### USGS — groundwater recharge areas, pumping and travel time

Source: USGS Scientific Investigations Report 2010-5232, “Contributing recharge areas, groundwater travel time, and groundwater quality…”
https://pubs.usgs.gov/publication/sir20105232

High-level findings:
- pumping patterns can alter groundwater flow;
- adding or changing wells can alter which areas contribute recharge to a well field;
- groundwater travel time matters when connecting a source area to a later observation at a well;
- a well samples a moving system, not a static underground tank.

Reusable Ouros lesson:
A new municipal or agricultural well should be able to change the groundwater system over time. Two wells can interact. A contaminant or recharge event may appear after a delay. A historical map of contributing areas can become obsolete while remaining correct for its date.

### US EPA — aquifer recharge versus aquifer storage and recovery

Source: US EPA, “Aquifer Recharge and Aquifer Storage and Recovery”
https://www.epa.gov/uic/aquifer-recharge-and-aquifer-storage-and-recovery

High-level findings:
- aquifer recharge and storage/recovery are related but distinct operations;
- introducing water underground can change water quality and aquifer chemistry;
- storing water underground does not mean it returns unchanged;
- recharge projects require monitoring rather than a simple `water +N` outcome.

Reusable Ouros lesson:
If Ouros ever uses managed recharge, infiltration basins, recharge wells, or underground storage, the project needs source-water provenance, monitoring, recovery records, and follow-up. “We put water underground” does not prove “we safely increased supply.”

Do not import US law, regulatory classes, numeric standards, or real-world legal frameworks into Ouros.

### US EPA — current Red Hill groundwater monitoring example

Source: US EPA, “How far has contamination spread in the aquifer? Is it moving toward our drinking water?” Updated 2026-05-22.
https://www.epa.gov/red-hill/how-far-has-contamination-spread-aquifer-it-moving-toward-our-drinking-water

High-level pattern:
- contamination can be consistently detected near a source while detections farther away remain intermittent;
- monitoring network geometry limits what can be concluded;
- adding wells can reduce uncertainty about plume extent;
- absence of detection at one point is not proof that the aquifer is clean everywhere.

Reusable Ouros lesson:
Groundwater mysteries should support uncertainty shaped by where wells actually are. A sparse monitoring network can produce honest institutional disagreement without anyone lying.

### US EPA — well contamination pathways

Source: US EPA, “Potential Well Water Contaminants and Their Impacts”
https://www.epa.gov/privatewells/potential-well-water-contaminants-and-their-impacts

High-level pattern:
Surface runoff, snowmelt, waste systems, underground tanks, fertilizers, and other sources can reach groundwater by different pathways.

Reusable Ouros lesson:
A contaminated well should not automatically identify its source. Investigation can compare surface infiltration, subsurface leakage, upstream recharge, infrastructure failure, geological pathways, and sampling error.

No real contaminant thresholds or medical effects are imported as Ouros rules.

### US EPA — Enhanced Aquifer Recharge research

Source: US EPA, “Enhanced Aquifer Recharge Research”
https://www.epa.gov/water-research/enhanced-aquifer-recharge-research

High-level pattern:
- aquifer material can transform water chemistry;
- water that is already treated may still interact with minerals underground;
- characterization and monitoring matter before claiming a recharge project is safe or successful.

Reusable Ouros lesson:
The subsurface is not a neutral storage inventory. Geology and groundwater must remain linked. A restoration or supply project can generate scientific work years after construction.

### Current public PTU campaign ecosystem

Source: Kairos Isles PTU Wiki
https://kairosptu.wiki.gg/

The living-world structure remains useful as a general reference for persistent locations, downtime, homes, quests, and shared campaign state. No groundwater-specific Kairos mechanic was found in this scan, so no such rule is attributed to it.

Source: Pokémon Tabletop official blog “About” page
https://pokemontabletop.com/about/

The official PTU blog is explicitly a GM inspiration/development resource. This scan did not find a new official PTU groundwater subsystem. Therefore no groundwater checks, DCs, hazards, Features, or environmental effects are inferred from PTU memory.

## Design structures extracted

1. Groundwater is delayed causality. Recharge, pumping, contamination, and recovery can produce consequences much later than the initiating event.
2. Observation geometry matters. What institutions know depends on which wells, springs, gauges, and samples exist.
3. Wells are interfaces, not aquifers. A well can fail while the aquifer remains; a well can function while regional storage declines.
4. Springs are outlets with history. A spring can shift flow, weaken, become intermittent, or respond to distant recharge.
5. Pumping creates relationships. One user’s extraction can change another user’s well or spring without deliberate interference.
6. Recharge is not immediate storage. Rainfall, snowmelt, irrigation, wetlands, and managed recharge can reach different aquifers at different rates.
7. Water quantity and water quality stay separate.
8. A contaminant detection does not prove source attribution.
9. Groundwater and surface water exchange requires authored/validated connection edges.
10. Minecraft block water is presentation. Loaded water blocks cannot become the groundwater authority.

## Narrative opportunities

Groundwater supports mysteries with slow evidence rather than arbitrary twists: a spring weakening over three summers; an orchard well remaining stable while a nearby public well falls; a new rail cut changing recharge; an old industrial site becoming relevant decades later; a recharge project succeeding in quantity but creating a new chemistry question; a cave stream responding to rainfall days before a town spring does; a well field drawing from a recharge area that crosses several land-use zones.

These stories naturally connect Science, Freshwater, Geology, Aridity, Cryosphere, Stormwater, Estuaries, Sanitation, Agriculture, Public Works, Supply Chains, Land Tenure, Health Surveillance, and Public Memory.

## PTU / Caelo mechanical boundary

This research does not establish:
- drowning or dehydration;
- Swim rules;
- groundwater Terrain;
- water-pressure damage;
- contaminated-water Poisoned;
- well or pump HP;
- Groundshaper effects;
- Water-type sensing abilities;
- Survival or Education DCs;
- healing spring effects;
- Pokémon-generated purification;
- battle Weather from groundwater;
- underground currents or forced movement.

Any such mechanic requires the exact PTU/Caelo source text and current AutoPTU/AutoPTU-Java implementation evidence.

The full primary Caelo corpus was not reliably accessible during this run. Super PTU Online Helper was not exposed as an invokable capability. No output is attributed to either source.