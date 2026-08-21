# Geomagnetism, Magnetic Navigation & Interference Research Scan

Status: RESEARCH / PROVENANCE ONLY. Not canon. Not a PTU rules source.

Pass: 81

Date: 2026-08-21

## Why this pass exists

The repository already has dedicated layers for Astronomy, Meteorology, Technology, Cartography, Aerial corridors, Communications, Anomalous Spaces and multiple physical-landscape systems. Search across the narrative repository found no dedicated geomagnetic or electromagnetic world-state layer.

This creates a real gap. Several Pokémon have authored magnetic behavior, compasses and navigation can depend on a field that changes by location and time, geomagnetic events can affect technology, and aurora can be visible evidence of space weather. None of those facts should be collapsed into Electric-type flavor or a generic battle hazard.

The intended reusable structure is:

physical magnetic field -> observation -> local anomaly or long-term revision -> instrument/navigation effect -> ecological or technological consequence -> actor interpretation -> possible tactical projection only when PTU/AutoPTU explicitly supports it.

## Repository overlap check

This pass does not replace:

- Astronomy for celestial events, observatories and sky visibility;
- Meteorology for weather and atmospheric forecasts;
- Technology for power grids, devices and physical infrastructure;
- Communications for radio/data delivery;
- Cartography for maps and route knowledge;
- Travel/Aerial/Maritime for route eligibility and transport services;
- Geology for magnetic minerals and bedrock provenance;
- Science for hypotheses, datasets and publication;
- Pokémon Agency for persistent individual Pokémon;
- AutoPTU for Magnet Pull, Magnet Rise, Magnetic Flux or any other exact battle mechanic.

## Source findings

### Official Pokémon: Nosepass

Official Pokédex material describes Nosepass as possessing a magnetic nose that functions as a highly reliable compass and also notes that it may increase magnetism and draw nearby iron objects when threatened.

Source: https://www.pokemon.com/us/pokedex/nosepass

Reusable lessons:

- a Pokémon can provide a navigation affordance through authored species behavior;
- a navigation partner can matter outside battle without becoming a universal compass mechanic for all Rock or Steel Pokémon;
- magnetic attraction toward objects is species-specific evidence, not proof of generic environmental forced movement.

Do not import:

- arbitrary range;
- guaranteed navigation in every magnetic environment;
- automatic metal-object manipulation;
- tactical pull effects unless PTU rules verify them.

### Official Pokémon: Probopass

Official Pokédex material states that Probopass radiates a magnetic field powerful enough to interfere with nearby electrical appliances and controls three Mini-Noses by magnetic force.

Source: https://www.pokemon.com/us/pokedex/probopass

Reusable lessons:

- Pokémon presence may plausibly become one hypothesis for local instrumentation failure;
- repeated equipment faults can create an investigation before the responsible cause is known;
- a Pokémon's known biological capability can coexist with an infrastructure incident without proving it caused the specific incident.

Do not import:

- a universal electronics-disabling radius;
- EMP damage;
- hacking or device-control powers;
- automatic disruption whenever Probopass spawns.

### Official Pokémon: Magnemite and Magnezone

Magnemite is explicitly described as emitting electromagnetic waves and hovering through that mechanism. Magnezone is described as having evolved through exposure to a special magnetic field and as transmitting/receiving unexplained signals.

Sources:

- https://www.pokemon.com/us/pokedex/magnemite
- https://www.pokemon.com/us/pokedex/magnezone

Reusable lessons:

- magnetic-field locations can be meaningful ecological/evolutionary sites;
- recurring signal observations around a species can support research mysteries;
- field exposure, species behavior and technological interference should stay as separate evidence streams until connected.

Do not import:

- a generic evolution trigger for Ouros without exact PTU/Caelo confirmation;
- alien-signal explanations;
- universal radio access;
- automatic Levitate/Sky behavior beyond authoritative species data.

### Official Pokémon: Clefairy

Official Pokédex material describes Clefairy gatherings under a full moon where the surrounding area can be enveloped in an abnormal magnetic field.

Source: https://www.pokemon.com/us/pokedex/clefairy

Reusable lessons:

- a rare biological/social event can create a temporary measured anomaly;
- lunar timing, group behavior and magnetic observation may correlate without the system assuming which causes which;
- the same event can connect Astronomy, Pokémon ecology and Science without becoming a combat effect.

Do not import:

- automatic Moon Stone generation;
- battle Gravity;
- forced levitation;
- Legendary or extraterrestrial causation.

### PTU campaign-design precedent

The official PTU campaign seed `The Road to Tomorrow` explicitly suggests using Magnemite and Voltorb to help restore old machines during rebuilding. The useful high-level pattern is that Pokémon capabilities can support infrastructure and exploration outside battle when the fiction and rules permit it.

Source: https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

Reusable lesson:

A Pokémon's authored relationship to electricity or machinery can create jobs, expeditions and settlement dependencies without turning that species into a generic resource node.

### Public PTU campaign anecdote: cave consequences

A public PokémonTabletop campaign anecdote describes an unstable cave where a Magnemite's loud action contributed to a collapse ruling. This is not a rules source and the GM explicitly used a campaign-specific environmental roll. The reusable lesson is narrower: devices, Pokémon actions and unstable environments can combine into consequences, but a narrative repository must never reinterpret one table's ruling as universal PTU physics.

Source: https://www.reddit.com/r/PokemonTabletop/comments/onnt2p

### Geomagnetic field: changes with place and time

NOAA NCEI states that Earth's magnetic field differs by location and changes over time. Magnetic declination also changes by place and date, and compasses can become unreliable in regions where the horizontal field is weak.

Sources:

- https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions
- https://www.ncei.noaa.gov/products/world-magnetic-model
- https://www.ngdc.noaa.gov/geomag/declination.shtml

Reusable lessons:

- magnetic navigation should use a versioned local model, not a timeless global north offset;
- an old map's magnetic correction can have been correct when published;
- navigation disagreement can come from outdated magnetic information rather than incompetence or supernatural causes;
- a compass anomaly can be local, regional, temporary or instrument-specific.

### Magnetic observatories

USGS describes observatories using multiple magnetometers and redundant measurements. The sites are deliberately protected from local magnetic interference because instruments are sensitive to nearby disturbances.

Sources:

- https://www.usgs.gov/programs/geomagnetism/introduction-geomagnetism
- https://www.usgs.gov/programs/geomagnetism/science/instrumentation
- https://www.usgs.gov/programs/geomagnetism/science/observatories

Reusable lessons:

- magnetic monitoring can become an institutional/scientific loop;
- local construction, machinery or Pokémon activity near an instrument can contaminate observations without changing the regional field;
- redundancy allows data-quality investigations rather than binary sensor-good/sensor-bad state.

### Geomagnetic storms and infrastructure

NOAA Space Weather Prediction Center documents that geomagnetic storms can disrupt navigation accuracy, radio systems and power-grid operation, while also producing aurora. The effect depends on the event and the affected technology.

Sources:

- https://www.spaceweather.gov/phenomena/geomagnetic-storms
- https://www.spaceweather.gov/impacts
- https://www.spaceweather.gov/noaa-scales-explanation

Reusable lessons:

- aurora can be visible evidence while the important gameplay consequences occur in communications, navigation or infrastructure;
- a regional geomagnetic event can create several independent incidents without becoming a battle Weather condition;
- visual spectacle and mechanical battle state should remain separate;
- a power outage during an aurora does not prove the aurora itself damaged the grid without infrastructure evidence.

## Design patterns worth carrying into Ouros

### Versioned magnetic maps

A region can accumulate magnetic-field surveys and declination revisions. Old explorer journals may require the correction that was valid at the time they were written.

### Instrument contamination mysteries

A monitoring station may show an anomaly because of actual field change, nearby machinery, a magnetic Pokémon, damaged calibration, construction or bad timestamps. Investigation should preserve these hypotheses until evidence resolves them.

### Navigation disagreement without incompetence

Two competent route-finders can report different magnetic bearings because they used different map editions, dates, instruments or locations.

### Temporary anomaly events

A Pokémon gathering, geomagnetic storm or local field disturbance can be temporary. The event may leave data, public memory, route disruptions and follow-up research even after the field returns to baseline.

### Aurora without magical causation

Aurora can support festivals, tourism, photography, research, public-memory events and travel disruption. It does not automatically trigger Psychic/Fairy/Legendary behavior, rare spawns or PTU Weather.

### Electromagnetic interference with provenance

Device failure must remain an incident with evidence. Nearby Probopass/Magnemite, a geomagnetic event or a new industrial installation can be hypotheses rather than instant truth.

## Copyright and transformation boundary

No external plot, character, dialogue, location or distinctive scene is copied into Ouros proposals.

Pokémon species facts are retained only as factual reference points. PTU campaign anecdotes are used only for abstract encounter-design lessons. NOAA/USGS material informs the structure of observation, mapping and infrastructure consequences rather than importing real institutions into Ouros canon.

## PTU / AutoPTU mechanical guardrails

Available Python AutoPTU evidence contains a concrete `Magnet Pull` temporary-effect path that can constrain movement relative to a source. That is evidence for that implemented PTU mechanic only.

It does not establish:

- generic environmental magnetic pull;
- compass behavior;
- equipment interference;
- metal-object hazards;
- geomagnetic Weather;
- aurora mechanics;
- evolution through magnetic fields;
- navigation bonuses;
- electromagnetic damage.

A separate secondary file in the user's library describes main-series `Magnet Pull`, `Magnet Rise`, `Magnet Bomb` and `Magnetic Flux`, but it is not accepted here as primary PTU/Caelo authority.

The complete primary Caelo corpus was not reliably retrievable during this pass. No Caelo-specific magnetism rule is asserted.

## Research gaps

Future work should extract the exact PTU/Caelo text for:

- Magnet Pull;
- Magnet Rise;
- Magnetic Flux;
- Magnet Bomb;
- Telekinetic/Levitate interactions if relevant;
- any Technology Education or Survival interaction with navigation instruments;
- Nosepass/Probopass/Magnemite/Magneton/Magnezone capabilities in the pinned Pokédex;
- any evolution rules that mention special magnetic fields.

Future world research should also decide whether Ouros has a stable global magnetic model, regional anomaly belts, magnetic observatories, magnetic-pole analogues or only local authored phenomena.