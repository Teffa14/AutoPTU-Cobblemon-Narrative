# Seismic Monitoring, Catalog Revisions and Aftershock Evidence — Research Scan 164

Status: RESEARCH / PROVENANCE ONLY. NON-CANON.

Date researched: 2026-08-25

## Deduplication correction

Final repository comparison exposed an existing authority that the initial search did not return: Pass 71 already provides `design/seismic-faults-ground-failure-layer.md` and `proposals/2026-08-21-seismic-faults-ground-failure-seeds-71.md`.

Pass 71 already owns seismic regions, fault segments, seismic-event identity, observations, warning/prediction separation, shaking footprints, aftershock sequences, surface deformation, liquefaction/ground-failure state and trigger attribution.

Pass 164 therefore does not create another seismic or ground-failure authority. Its useful new scope is narrower: monitoring-network history, automatic versus reviewed detections, source-solution revisions, felt-report provenance, event-catalog vintages and QA links to Metrology/Timekeeping.

The duplicate protocol drafted earlier in this run was removed and replaced by `design/seismic-event-catalog-monitoring-revision-protocol.md`.

## New scientific sources and lessons

### Magnitude and local intensity are different evidence products

U.S. Geological Survey, “Earthquake Magnitude, Energy Release, and Shaking Intensity.”
https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity

USGS distinguishes one event-size estimate from many local intensity values. Intensity varies by place, including distance and local geology. Pass 71 already models local shaking footprints; Pass 164 adds provenance for the observations and source-solution revisions used to update those footprints.

Design consequence: an early event solution and a later reviewed solution can disagree while referring to the same physical event. Earlier reports remain historically real because institutions may have acted on them.

### Felt reports remain location-specific observations

U.S. Geological Survey, “The Modified Mercalli Intensity Scale.”
https://www.usgs.gov/programs/earthquake-hazards/modified-mercalli-intensity-scale

Felt/effect observations are useful local evidence, but Ouros should not import Modified Mercalli as canon automatically. The reusable structure is location-specific observation → derived assessment, with method and uncertainty retained.

### Site conditions affect shaking and observed damage

U.S. Geological Survey:
- https://www.usgs.gov/faqs/how-do-earthquakes-affect-buildings
- https://earthquake.usgs.gov/research/eqproc/grdshaking.php

Local geology, soil and structure characteristics affect outcomes. Pass 164 should therefore never use damage reports as a direct magnitude calculator. Architecture/Public Works remain authoritative for structural condition.

### Liquefaction requires specific conditions

U.S. Geological Survey:
- https://www.usgs.gov/faqs/what-liquefaction
- https://www.usgs.gov/programs/earthquake-hazards/what-are-effects-earthquakes

Liquefaction occurs in susceptible loose, water-saturated sediments during strong shaking. Pass 71 already owns liquefaction/ground failure. Pass 164 only contributes event/source/observation provenance to that assessment.

This reinforces a guardrail: `wet ground`, `sand`, `riverbank` or `high groundwater` alone never creates liquefaction state.

### After-event sequences need review, not simple timestamp grouping

U.S. Geological Survey:
- https://earthquake.usgs.gov/research/eqproc/posteqmotions.php
- https://www.usgs.gov/publications/loma-prieta-california-earthquake-october-17-1989-aftershocks-and-postseismic-effects

Large earthquakes can be followed by many later events and postseismic effects. Pass 71 already owns the aftershock sequence object. Pass 164 adds the review history that decides whether a candidate event is included, rejected or left unresolved.

Temporal order alone is insufficient evidence for sequence membership.

### ShakeMap illustrates derived spatial products

U.S. Geological Survey, ShakeMap.
https://earthquake.usgs.gov/data/shakemap/

ShakeMap combines observations and models into near-real-time ground-motion/intensity products. Ouros can reuse the architecture only if its canon supports comparable instrumentation. Any such product must preserve input observations, processing revision and uncertainty. It remains a derived product, not raw world truth.

## Pokémon and narrative sources

### Pokémon Mystery Dungeon: Rescue Team DX

Official Pokémon sources:
- https://www.pokemon.com/us/pokemon-video-games/pokemon-mystery-dungeon-rescue-team-dx/
- https://mysterydungeon.pokemon.com/en-us/world/

The official premise uses widespread natural disasters to generate recurring rescue needs and a rescue-team institution.

Reusable structure:
`physical event -> immediate local need -> recurring response work -> later recovery/research`

Ouros should not copy the game’s cosmological mystery, characters or dungeon plots. The useful design lesson is that disaster response can generate institutional continuity without every event becoming the campaign’s central antagonist.

### Whiscash as an anti-attribution precedent

Secondary Pokédex compilation used to compare official game entries:
https://bulbapedia.bulbagarden.net/wiki/Whiscash_(Pok%C3%A9mon)

Especially useful is the Legends: Arceus entry summarized there: Whiscash creates local shaking to startle prey, and people historically mistook that behavior for the cause of earthquakes. Other official entries associate the species with tremors or earthquake prediction folklore.

Reusable Ouros pattern:
`Pokémon behavior observation -> local belief/claim -> instrument/geology comparison -> revised or unresolved interpretation`

Guardrails:
- Whiscash presence does not prove a tectonic event.
- Whiscash absence does not rule one out.
- local tremor behavior is not automatically the source of a regional seismic event.
- one apparent precursor does not establish species-wide prediction.

### PTU community warning about improvised disaster mechanics

Public PTU GM report:
https://www.reddit.com/r/PokemonTabletop/comments/onnt2p/

The report describes an earthquake exposing a cave and then uses improvised unstable-roof consequences. The reusable narrative structure is strong: a physical event can alter access and expose a new location. The mechanical lesson is the opposite: do not invent falling-rock damage or collapse rules merely because the scene implies instability.

Pass 164 encounters therefore keep dynamic collapse/debris in FULL versions behind the exact engine capability families and provide REDUCED static versions.

## PTU/Caelo cross-check

Project file search confirms that `Earthquake` exists as a concrete Move concept in available source material. That is a battle mechanic, not an environmental-seismic subsystem.

Available AutoPTU Python evidence also contains Groundshaper/Mold the Earth behavior. Those are exact battle mechanics. Neither grants regional fault manipulation, earthquake prediction, liquefaction, ground-failure authority or environmental-event simulation.

No reliable complete Caelo source defining earthquake hazards, environmental shaking, collapse, falling debris, liquefaction or aftershock mechanics was recovered in this run. Super PTU Online Helper was not exposed as an invocable capability.

## New design directions that extend Pass 71

1. Preserve `AUTOMATIC_EVENT_DETECTION` separately from reviewed Pass 71 `SEISMIC_EVENT` identity.
2. Allow automatic detections to be merged, split, rejected or reclassified without deleting raw station records.
3. Preserve versioned source solutions for origin time, location/depth and optional size estimate.
4. Keep old catalog entries because they document what institutions and residents knew at the time.
5. Treat felt reports as local observations with provenance, language/privacy and timing uncertainty.
6. Let Metrology and Timekeeping correct station data through derived revisions instead of rewriting raw records.
7. Preserve monitoring gaps as uncertainty, not conspiracy hooks by default.
8. Add explicit review history for membership in Pass 71 aftershock sequences.
9. Allow station relocations and network revisions to complicate long-term comparisons.
10. Treat a quiet year of instruments as useful Chronicle evidence.

## No-inference rules added by Pass 164

Automatic detection is not automatically a confirmed earthquake.
Catalog correction is not a second physical event.
A rejected detection is not evidence of institutional wrongdoing.
A felt report is not a magnitude estimate.
Station silence is not absence of shaking.
Station uptime is not proof that every processed estimate is correct.
A later event is not automatically an aftershock.
Whiscash behavior is not a seismometer.
The PTU Move `Earthquake` is not an environmental-event template.
Groundshaper/Mold the Earth is not tectonics.
Minecraft block destruction, vibration, TNT or camera shake never writes the event catalog.

## Open canon questions

- Does Ouros have automatic seismic detection or only reviewed institutional catalogs?
- Which regions have monitoring networks and what technology level do they use?
- Does canon use numerical magnitude/intensity systems or qualitative terminology?
- What historical station/catalog records predate the players?
- Which records are public, restricted or uncertain?
- Can player-built instruments join an institutional network after validation?
- Are any Pokémon behaviors institutionally monitored as possible precursors, and how uncertain are those claims?
- What Caelo mechanics, if any, govern environmental shaking, collapse or ground-failure consequences?
