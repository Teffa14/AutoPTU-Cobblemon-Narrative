# Karst Hidden Drainage and Tracing Scan — Pass 330

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-07

## Repository deduplication and scope

The current recursive repository tree, CURRENT_FOCUS.md, canon governance, source inventory, Pass 329 research/proposal/readiness material, and repository-wide searches were inspected before authoring this note. Recent passes already cover drought and groundwater recovery, excavation/mining, hydrothermal plumbing, floodplain pulse, tidal access, migration corridors, wildfire, snowpack, volcanic ash remobilization, and survey control. Searches for `karst`, `sinkhole`, `swallet`, `resurgence`, `dye trace`, and close variants did not expose a dedicated prior workstream.

This pass therefore studies hidden hydrologic connectivity in karst landscapes. Its design value is not cave spectacle alone. It is evidence about relationships that cannot be inferred from surface proximity: a disappearing stream can connect to a distant spring, one apparent outlet can belong to a different recharge area than expected, and a surface incident can create downstream consequences where no visible channel exists.

## Public sources and reusable structures

### National Park Service — Sequoia & Kings Canyon karst hydrology

Source: https://www.nps.gov/seki/learn/nature/caves_karsthydro.htm

NPS describes dye tracing as a principal method for determining where water entering sink points later emerges. Receptors placed at springs and caves can confirm hydrologic connections that are not visible at the surface. The documented systems can cross apparent surface watershed boundaries and involve multiple sinks and springs.

Reusable Ouros structures:

- surface adjacency must not imply underground connectivity;
- a confirmed tracer recovery establishes a connection between an injection event and a recovery feature, but does not automatically define every intermediate path;
- multiple traces over time can build a connection graph rather than a single global `CONNECTED` flag;
- a spring can receive contributions from more than one recharge source;
- an unsuccessful recovery is evidence with limits, not proof that no connection exists under every hydrologic condition.

### National Park Service — Mammoth Cave hydrological activity

Source: https://www.nps.gov/maca/learn/nature/hydrological-activity.htm

NPS explains that water in karst can disappear underground, travel through cave systems, and reappear at springs. Because the route is hidden, pollution or other transported material can move beyond the place where responders can directly observe it. Dye tracing allows managers to map groundwater basins and underground flow paths.

Reusable Ouros structures:

- `LAST_VISIBLE_LOCATION != CURRENT_LOCATION` for transported material;
- incident response can depend on a hidden connection map maintained by an institution;
- public-facing surface maps, maintenance maps, and hydrologic connection maps can disagree without one being fraudulent because they answer different questions;
- an NPC who witnessed a spill entering a sinkhole does not automatically know which spring will be affected;
- response decisions should preserve which connection evidence was actually available at decision time.

### National Park Service — Wind Cave disappearing stream / unexpected tracer result

Source: https://www.nps.gov/wica/learn/education/classrooms/the-sink.htm

NPS describes a disappearing stream where dye was expected to appear in Wind Cave but instead was detected in park well water. The useful design lesson is the failed expectation: geological proximity and an intuitive route did not predict the observed connection.

Reusable Ouros structures:

- an expert hypothesis can be reasonable and still be disproved by later evidence;
- a tracer result can redirect an investigation toward a socially important dependent feature such as a well;
- a negative result at the expected site and a positive result elsewhere should remain separate observations with their own provenance;
- discovering a hidden connection can create new obligations without retroactively making earlier actors negligent if the connection was not reasonably established.

### USGS — Little Sequatchie / Pryor Cove tracing study

Sources:
- https://www.usgs.gov/data/mapping-karst-groundwater-flow-paths-and-delineating-recharge-areas-springs-little-sequatchie
- https://pubs.usgs.gov/publication/sir20245089/full

USGS reports repeated dye injections used to delineate recharge areas for several springs. Traces travelled long subsurface distances and sometimes reached a spring different from the nearby outlet originally expected. The work also shows shared recharge boundaries and varying travel times.

Reusable Ouros structures:

- repeated observations matter because one trace does not exhaust the system;
- connection strength, travel time, hydrologic condition, and confidence can be recorded independently;
- two springs can share part of a recharge area while remaining distinct persistent features;
- an apparent nearest-neighbor explanation is not sufficient evidence;
- delayed recovery can support revisit loops where a test started in one quest produces evidence later.

### USGS — Oregon Caves groundwater tracing, published January 15, 2026

Source: https://www.usgs.gov/publications/groundwater-tracing-used-delineate-recharge-areas-and-map-karst-groundwater-pathways

USGS reports 2021–2024 tracing that delineated separate recharge areas for two cave systems and identified previously unknown resurgences. The study also found variation in groundwater velocities, retention, and diffuse-flow contribution.

Reusable Ouros structures:

- a hidden connection graph can grow when new outlets are discovered rather than being authored complete from the start;
- distinct cave systems can remain hydrologically separate even when surface geography suggests a simpler relationship;
- travel time may vary enough that absence at one observation window is not final evidence;
- new resurgences can become later locations, habitats, monitoring points, or institutional responsibilities.

### Pokémon core-series structure — Union Cave

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Union_Cave
- https://www.dragonflycave.com/locations/gen2/198/

Union Cave combines a through-route, deeper optional water-accessed sections, a connection toward the Ruins of Alph, and a recurring time-gated Lapras encounter in the deepest water. The reusable lesson is structural rather than geographical: a cave can first function as ordinary transit, then gain additional meaning through later traversal capability, deeper exploration, recurring ecology, and revisits.

Reusable Ouros abstraction only:

- the same cave network can support transit, investigation, ecology, and optional deeper routes;
- a location can become more legible after the player gains new information or access rather than because the map itself changed;
- recurring presence in a deep chamber can make revisits meaningful without resetting the whole dungeon.

Do not copy Union Cave layout, Johto geography, Ruins of Alph routing, Lapras scheduling, trainer placement, items, or encounter tables into Ouros.

### PTU community reference — The Island / Perception article

Source: https://www.worldanvil.com/w/the-island-coalmusterm/a/perception-article

This publicly accessible PTU reference emphasizes a useful tabletop distinction: noticing a detail and understanding what it means can require different competencies. Ouros already has a stronger provenance architecture, so the reusable lesson is narrow and compatible: an observation can be valid while its interpretation remains unresolved.

Reusable Ouros abstraction only:

- field observation should produce evidence records before causal interpretation;
- specialist knowledge, archives, later tests, or another NPC may be required to turn an observation into a justified claim;
- a high-information clue should not automatically solve the whole investigation.

Do not import house rules, proprietary examples, text, mechanical DCs, classes, or encounter content from this world into Ouros.

## Original design synthesis for Ouros

A reusable karst investigation should model hidden hydrologic connectivity as an evidence-backed graph. Persistent features include sink points, cave reaches, wells, springs, seeps, surface channels, storage areas, and dependent infrastructure. The system should be able to know that two features are connected even when no character knows it yet.

A trace event should preserve:

- tracer/test identity;
- injection feature;
- injection semantic time;
- hydrologic condition or authored context;
- receptor/recovery feature;
- detection time;
- positive, negative, inconclusive, or not-sampled result;
- observation source;
- institutional recipient history;
- interpretation confidence;
- later revisions.

The useful narrative tension comes from bounded truth. A road crew can know that runoff entered a sinkhole. A water operator can know that a spring changed. A cave researcher can know that a receptor detected a tracer. A resident can know that a well smells or looks different. None of those facts independently establishes the full underground path.

A delayed positive result can create a second-stage quest after an apparently resolved incident. A previously unknown resurgence can become a new persistent place. A failed expected recovery can force the institution to revise maps and procedures. The player can influence who receives that revision and therefore which NPCs act on it later.

## PTU / Caelo mechanical boundary

The current narrative repository exposes the existing Kairos comparative material under `sources/kairos`. No adopted `sources/caelo` rules source is present in the inspected source inventory. Public PTU community pages and Pokémon references are not authoritative Ouros mechanics.

This pass therefore authors no mechanical values for Swimming, cave movement, climbing, darkness, low ceilings, currents, drowning, water pressure, poison/contamination, visibility, scent, Perception, Survival, Education checks, Pokémon sensing, burrowing, cave navigation, Moves, Abilities, Items, or Trainer Features.

If a tactical encounter later requires flowing-water displacement, collapse, darkness-specific LoS, environmental damage, persistent exposure, rescue, reactions, or special movement, it must route through the corresponding AutoPTU capability family and validated PTU/Caelo source material.

## Copyright and transformation boundary

All external material is reduced to factual environmental relationships, high-level campaign structures, or general design lessons. No protected dialogue, distinctive characters, maps, puzzle sequences, encounter layouts, narrative resolutions, or substantial source prose is copied into Ouros.
