# Intertidal access and tidal-window research — Pass 324

Status: RESEARCH / PROVENANCE, NOT CANON
Date: 2026-09-07

## Purpose

Find reusable structures for Ouros in coastlines where access, ecology and evidence change with the tide. This pass deliberately avoids duplicating the hydraulic-control focus of Pass 314 and the floodplain-event focus of Pass 321. The new design problem is periodic exposure and submergence of the same persistent features.

## Repository duplication check

The recursive repository inventory was inspected before authoring. No existing file dedicated to tides, tidal flats, intertidal zones, tidepools or tide-window access was observed. Recent environmental passes already cover hydraulic works, acoustic masking, artificial light, olfactory traces, geomagnetic navigation, reclaimed extraction landscapes, burn mosaics, floodplains, bloom timing and layered snowpack. Pass 324 therefore opens a distinct coastal timing domain.

Canon governance remains unchanged: research is evidence, proposals are candidates, design files define architecture, and only `canon/` establishes approved Ouros world facts.

## Public source findings

### National Park Service — rocky intertidal zones and tidepools

Sources:
- https://www.nps.gov/cabr/learn/nature/tidepools.htm
- https://www.nps.gov/subjects/oceans/intertidal.htm
- https://www.nps.gov/acad/planyourvisit/tidepooling.htm

Reusable structure:
- the same physical shore alternates between submerged and exposed states;
- high, middle and low intertidal bands have different exposure histories and ecological communities;
- low tide creates a bounded exploration window rather than permanent access;
- apparently inert surfaces can contain living organisms adapted to waiting for water to return;
- safe human access depends on timing and local surface conditions, not only map geometry.

Ouros transformation:
A coastal route, cave mouth, reef shelf, survey point or service crossing can be physically real at all times while its traversability, observability and ecological meaning vary by tide phase. World state must preserve feature identity across those phases.

Do not import real-world tide schedules, safety thresholds or species distributions as game rules.

### NOAA Ocean Service — tidepools and intertidal definition

Sources:
- https://oceanservice.noaa.gov/facts/tide-pool.html
- https://oceanservice.noaa.gov/facts/intertidal-zone.html

Reusable structure:
- tidepools are isolated seawater pockets left after the tide recedes;
- intertidal habitat spans rocky ledges, beaches and mudflats;
- exposure history changes water chemistry, temperature, oxygen and access.

Ouros transformation:
A receding tide can reveal information without revealing final truth. A newly exposed pool, stranded object, footprint-like mark, shell accumulation or maintenance feature is an observation with a timestamp. It does not establish what happened at high tide or what will remain after the next cycle.

### NPS Glacier Bay and Acadia — access windows and changing opportunity

Sources:
- https://home.nps.gov/glba/planyourvisit/tides.htm
- https://home.nps.gov/acad/planyourvisit/tidepooling.htm

Reusable structure:
- tide timing changes travel opportunity and difficulty;
- low-tide exploration is a limited window;
- a route that is usable now may become unsuitable later without any structural failure.

Ouros transformation:
This supports semantic-time route windows. A valid decision can expire because the world phase changes, not because the earlier decision was wrong.

### Pokémon main-series design — Shoal Cave

Source:
- https://bulbapedia.bulbagarden.net/wiki/Shoal_Cave

Source type: community documentation of an official game location; not an Ouros rules source.

Reusable structure:
Shoal Cave changes accessible geometry between high and low tide. The core lesson is not its timetable or item loop. The useful pattern is a persistent dungeon whose topology changes predictably with world time, encouraging revisits under another environmental phase.

Ouros transformation:
Keep the location persistent and allow different evidence, routes and encounters to become available at different tidal states. Avoid a simple clock-key puzzle where the only interaction is waiting for a door to open.

### Pokémon official species material — Wiglett

Source:
- https://www.pokemon.com/br/pokedex/wiglett

The official Pokédex describes Wiglett as a species adapted to its environment, able to detect a specific nearby predator by scent and hide in sand.

Reusable structure:
Coastal species may respond to local substrate and threats through species-specific behavior. A future Ouros coast can use this only after local ecology and PTU capability checks approve the species and behavior.

Non-import boundary:
Do not infer universal scent ranges, sand-burrowing permissions, reaction actions, encounter bonuses or tactical detection from flavor text.

### Pokémon Tabletop United actual play — Pokémon World Tour: United

Source:
- https://podcasts.apple.com/au/podcast/pokemon-world-tour-united/id1154176782

The public listing identifies the show as a Pokémon Tabletop United actual-play campaign, active from 2016 through 2026, with a long-running journey and recurring guests.

Reusable structure:
A PTU campaign can sustain long continuity across travel, revisits, major events and returning characters. For Ouros, a tidal site should therefore accumulate consequences and later uses rather than exist as a single-use environmental puzzle.

No characters, dialogue, plot events or encounter sequences are copied.

### Fan-game / ROM-hack exploration reference

A broad search surfaced several island and coastal fan projects, but source quality was uneven. One result describing a supposed older ROM hack with shifting tides did not provide sufficiently trustworthy primary provenance. It is intentionally excluded from the design basis rather than treated as evidence merely because the concept was convenient.

This exclusion is part of provenance discipline: weak discovery results do not become research authority.

## Reusable Ouros design lessons

### Persistent feature, changing access

Use one stable feature ID for a reef shelf, cave mouth, causeway, tidepool terrace or maintenance platform. Store phase-dependent access separately.

`FEATURE_IDENTITY != CURRENT_ACCESS_STATE`

### Window validity

An observation or access decision can be valid only for a defined semantic-time window. When the tide state changes, the old observation remains historically true but may become stale for current routing.

### Exposure reveals evidence, not omniscience

Low water may reveal marks, debris, footprints, nests, repair work, stranded material or hidden entrances. Each is evidence with provenance. Exposure does not reveal who caused it or what happened while submerged.

### Ecological bands should not collapse into one coast state

Upper, middle and lower features may differ at the same moment. An exposed upper shelf does not imply a lower passage is exposed. A flooded channel does not imply the whole coast is inaccessible.

### Revisits should change interpretation

Return at another tide phase to compare:
- route geometry;
- what evidence remains;
- what was moved or erased;
- which species are observable;
- whether an institutional notice is still current;
- consequences of an earlier access decision.

### Avoid real-world forecasting gameplay

Ouros can author deterministic or explicit tidal world states. It should not require players to perform real tidal prediction or use simplified real-world coastal safety formulas.

## PTU / Caelo cross-check boundary

Current repository source inventory exposes `sources/kairos`. Its index routes movement/terrain to pp. 382+, hazards to p. 401, terrain/weather to pp. 404+, Fishing to p. 368 and world/encounter guidance to later chapters. The index explicitly says it is a routing aid and that Kairos is comparative evidence rather than automatic Ouros law.

No adopted `sources/caelo` directory was visible in the inspected recursive tree. Therefore Pass 324 does not author Swim costs, current rules, drowning, slippery footing, underwater LoS, tide mechanics, fishing modifiers, aquatic rescue, water-terrain effects, Move effects, Ability effects, Item effects or Trainer Feature privileges.

## Research-to-content candidates

Primary candidate:
`The Staircase the Sea Borrowed`

Core premise:
A stepped coastal route and adjacent survey shelf are usable during one tide phase and submerged during another. Conflicting reports about whether the route is open can both be accurate if they refer to different windows or different route features.

Secondary reusable candidates:
- a tidal archive entrance revealed only briefly, with records that can be inspected without making the archive itself supernatural;
- a shellfish or seaweed harvest dispute where legal access, ecological recovery and tide timing are separate facts;
- a rescue cache placed above one historic waterline but below a later storm-debris mark;
- an intertidal Pokémon observation program whose counts depend on exposure phase and observer timing;
- a ferry landing where a low-water service route exists separately from the passenger route.

All remain research-level until separately proposed or canon-approved.