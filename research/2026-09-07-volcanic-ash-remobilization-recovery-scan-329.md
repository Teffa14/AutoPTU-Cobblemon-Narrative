# Volcanic Ash Remobilization and Recovery Scan — Pass 329

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-07

## Repository deduplication and scope

The full recursive repository tree, CURRENT_FOCUS.md, README.md, the Pass 328 readiness snapshot, source inventory, and repository-wide search results were inspected before authoring this note. Recent work already covers reclaimed extraction landscapes, wildfire mosaics, seasonal floodplains, pollinator phenology, winter snowpack, tidal windows, introduced-species management, survey control, migration corridors, and hydrothermal feature change. Repository searches for `volcanic ash`, `ashfall`, `lahar`, `remobilization`, and close variants did not expose a dedicated prior workstream.

This pass therefore studies a different persistent-world problem: deposited volcanic ash can remain part of the landscape after the primary eruptive event and can later be moved again by wind, water, traffic, cleanup, drainage, or disposal. The design value is provenance over time: a new deposit does not by itself identify a new eruption, and successful cleanup of one feature does not imply that the wider system no longer contains mobile ash.

## Public sources and reusable structures

### USGS — Remobilization of Ash by Wind

Source: https://volcanoes.usgs.gov/volcanic_ash/Remobilization_by_wind.html

USGS explains that unconsolidated ash deposits remain susceptible to wind erosion, transport, and redeposition after ashfall. It documents long-lived resuspension in the Novarupta-Katmai region and severe recurring impacts to exposed communities after other eruptions.

Reusable Ouros structures:

- Primary event time and secondary remobilization time must be separate events.
- Material can leave one persistent feature and arrive at another without a new source event.
- A field report of fresh airborne ash can be correct while an observatory report of no fresh eruptive pulse is also correct.
- Dry periods, wind exposure, vegetation, and storage locations can change which features contribute material later.
- Repeated observations should preserve source feature, receiver feature, time window, and confidence rather than collapsing into one global `ASH_PRESENT` truth.

### USGS — Remobilization of Ash by Water

Source: https://volcanoes.usgs.gov/volcanic_ash/Remobilization_by_water.html

USGS describes deposited ash being eroded, transported, and redeposited downslope when mixed with sufficient water; substantial secondary lahars can occur after the original ashfall.

Reusable Ouros structures:

- Rain or runoff can activate stored material after a quiet interval.
- Downstream evidence can be younger than the ash source material.
- A route, culvert, intake, channel, and storage slope can have different current states even when they share one historical event.
- Full dynamic secondary-flow simulation is optional. The world model can author a between-scene transfer event and preserve its provenance until the tactical engine supports the required movement/hazard families.

### USGS — Roads and Highways

Source: https://volcanoes.usgs.gov/volcanic_ash/roads_highways.html

USGS records post-ashfall transportation problems including reduced visibility from remobilization by wind or traffic, reduced traction, obscured markings, vehicle impacts, clogged roadside drainage, and erosion problems when drainage becomes impaired. It also documents management responses such as temporary closure, reduced traffic, speed restrictions, convoys, and cleanup coordination.

Reusable Ouros structures:

- A road authority can legitimately reopen a corridor under one operating condition and later revise that decision after a different feature changes.
- Vehicle traffic can be an active world-system input because it can resuspend material; this does not need to be represented as a combat rule in the reduced implementation.
- Access decisions can be scoped by route segment, traffic class, time window, or maintenance state.
- Road condition, visibility, drainage, and vehicle operability are separate observations and should not be inferred from one another.

### USGS — Ash Disposal

Source: https://volcanoes.usgs.gov/volcanic_ash/ash_disposal.html

USGS advises that removed ash should be disposed of where wind or water will not redistribute it and where it does not create a new public hazard.

Reusable Ouros structures:

- Cleanup creates a material-lineage problem. `removed from road` can produce `stored at disposal feature` rather than `removed from world`.
- A cleanup stockpile, ditch, back slope, bagged storage area, or disposal site can become a later evidence source.
- A maintenance crew can have completed its assigned task correctly while a later systems-level consequence emerges elsewhere.
- Institutional records should preserve where material was moved, by whom, under what instruction, and which later actors received that information.

### USGS — Wastewater, Gutters, and Drains

Sources:
- https://volcanoes.usgs.gov/volcanic_ash/waste_water.html
- https://volcanoes.usgs.gov/volcanic_ash/clogging_gutters_drains.html

USGS describes ash obstructing catchpits, sumps, drains, gutters, downpipes, and stormwater systems, with rainfall capable of turning an existing deposit into a new drainage problem.

Reusable Ouros structures:

- The same historical ashfall can generate separate infrastructure quests at different dates.
- An intake or culvert can be a high-information feature because its blockage integrates material from an upstream catchment.
- Clearing a drain should produce a feature-scoped consequence and a maintenance record, not a global recovery flag.
- Later blockage can be investigated through material provenance, cleanup records, weather history, traffic history, and upstream observations.

### Pokémon — Hoenn Route 113 / volcanic ash collection

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Route_113
- https://bulbapedia.bulbagarden.net/wiki/Soot

The core-series Route 113 presents volcanic ash as a persistent environmental layer that changes the appearance and traversal texture of a route and can be collected as material for a local workshop economy.

Reusable Ouros abstraction only:

- Environmental residue can participate in everyday labor and local craft/economy after the dramatic event that produced it.
- A route can remain socially active while carrying visible evidence of a regional geological process.
- Environmental cleanup, collection, and reuse can create NPC jobs and recurring reasons to revisit the same landscape.

Do not copy Route 113 layout, Mt. Chimney, the Glass Workshop, Soot Sack mechanics, flutes, characters, item exchange rates, or Hoenn plot material into Ouros.

### PTU community worldbuilding — Pokémon Prism / Thenia

Source: https://www.worldanvil.com/w/pokemon-prism-eldritch-lord

This publicly accessible campaign world identifies a Pokémon Tabletop United campaign and presents an original region through a player handbook, world codex, timeline material, map, articles, and characters.

Reusable Ouros abstraction only:

- A PTU campaign can distribute world understanding across player-facing guidance, maps, timelines, people, and deeper reference material instead of placing all lore in one exposition source.
- Persistent institutions and environmental events benefit from layered documentation: public notice, operational record, archival source, personal observation, and later revision can each expose different information.
- This structure aligns with Ouros world-agent knowledge boundaries: access to one document type should not imply access to every historical fact.

Do not import Thenia, its pantheon, Fallers, characters, campaign premise, private campaign details, prose, or distinctive lore.

## Original design synthesis for Ouros

A reusable ash-recovery arc should model material as having spatial and temporal lineage. The primary eruption or ashfall is historical provenance. Later wind, runoff, traffic, cleanup, and disposal can create secondary transfer events. Each transfer can alter particular features without changing the historical identity of the material.

The useful investigative tension comes from actors reporting different layers of truth:

- observatory staff can report no evidence of a new primary fallout event;
- road staff can document a new deposit on a cleared segment;
- residents can report clear skies during the relevant period;
- water or drainage crews can document fresh obstruction;
- freight operators can report that the route was previously reopened under a valid decision;
- archives can identify where ash from the first cleanup was moved.

The player does not need to solve subsurface volcanology or forecast an eruption. The meaningful decision can be narrower: identify likely material lineage, determine which features need restriction or monitoring, choose what evidence justifies reopening, and create records that later NPCs can actually receive.

## PTU / Caelo mechanical boundary

The current repository inventory exposes the existing Kairos comparative source material and does not expose an adopted `sources/caelo` rules source. Public PTU-adjacent or Pokémon material is not sufficient authority for Ouros mechanics.

This research therefore authors no mechanical values for ash visibility, respiratory exposure, weather, wind, traction, difficult terrain, environmental damage, Burn, Poison, movement costs, forced movement, falling debris, lahars, rescue reactions, Survival/Education checks, Pokémon sensing, Moves, Abilities, Items, or Trainer Features.

If an encounter later needs those effects, it must route through the relevant AutoPTU capability family and an adopted PTU/Caelo rules source before becoming mechanical canon.

## Copyright and transformation boundary

All borrowed material in this note is reduced to high-level structures, factual environmental relationships, or campaign-design lessons. No protected dialogue, distinctive character, proprietary map, encounter sequence, plot resolution, or substantial prose is copied into Ouros.
