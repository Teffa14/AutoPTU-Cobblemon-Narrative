# Research Scan — Metrology, Calibration & Measurement Standards — Pass 118

Status: research/provenance only. Not Ouros canon. Not PTU/Caelo rules authority.

## Why this pass exists

The narrative repository already has strong layers for Science, Meteorology, Air Quality, Astronomy, Cartography, Manufacturing, Hydrology, Groundwater, Seismic monitoring, Technology and institutional review. All of those layers create or consume measurements. None currently owns the cross-cutting question: what instrument produced a value, against what reference, under what valid range, when was it checked, what uncertainty applies, and whether two records are actually comparable.

This pass therefore studies measurement traceability as a worldbuilding and mystery tool. The intent is not to build a laboratory simulator or to import real-world regulation.

## Internal repo findings

`design/science-research-discovery-layer.md` already distinguishes world truth from observation, measurement, datasets, hypotheses and publications. Its `measurement` record already includes `method_id`, `instrument_id` and `uncertainty`, but instrument calibration is deliberately not modeled in detail.

`design/meteorology-forecasting-weather-layer.md` already stores `calibration_state`, sensor health and quality flags for weather observations. It also warns that a failed sensor can still create a record without that record becoming weather truth.

`design/manufacturing-production-quality-layer.md` already separates process execution, in-process observations, nonconformance and release. It does not own whether the measuring device used during an inspection was fit for the measurement.

Multiple later layers use gauges, monitoring stations, cameras, samplers, telescopes, benchmarks or sensor networks. A common metrology layer can support them without duplicating their domain logic.

No existing `design/*-layer.md` contains `metrology`, `calibration` or `measurement standards` in its filename or authority boundary.

## Source 1 — Pokémon Legends: Arceus research as accumulated observation

Source: The Pokémon Company, “A Look at the Early Days of Pokémon Research in Pokémon Legends: Arceus,” 8 March 2022.
https://www.pokemon.com/us/pokemon-news/a-look-at-the-early-days-of-pokemon-research-in-pokemon-legends-arceus

The official retrospective emphasizes that Hisui's Pokédex is assembled from repeated field tasks and observations rather than instant perfect knowledge. Researchers may catch several members of a species, observe repeated behavior and later consolidate notes into a more complete record.

Reusable structure for Ouros:

- knowledge can improve through repeated observations without any single observation becoming universal truth;
- raw field notes and later institutional records should remain distinguishable;
- old observations remain historical evidence after interpretations improve;
- different eras can produce records with different tools and precision.

Do not import the game's research-level counters or task quotas as Ouros mechanics.

## Source 2 — Pokémon Legends: Arceus Survey Corps

Source: official Pokémon Legends: Arceus site.
https://legends.arceus.pokemon.com/en-ca/story/

The Survey Corps exists specifically to study how Pokémon live. Field assignments return to an institutional base where observations are consolidated. This supports a repeatable loop of field work -> record -> institutional interpretation without requiring every science scene to become a combat encounter.

Ouros adaptation:

A regional measurement network can have technicians, field observers, analysts and archivists whose jobs remain different. A person who reads a gauge does not need to be the person who decides what the reading means.

## Source 3 — PTU official campaign structure: research institutions can evolve

Source: Pokémon Tabletop RPG official blog, “Campaign Seeds: The Road to Tomorrow.”
https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

The campaign seed explicitly supports research programs that grow through new facilities, expert recruitment and different scientific priorities. The useful structure is institutional evolution: players can influence what a research organization is capable of studying without turning every improvement into a character stat bonus.

Ouros adaptation:

Measurement capability can be institutional world state. A region can begin with sparse manual gauges, later establish reference stations, and eventually build a cross-regional comparison network. This changes what questions can be answered, not the underlying world truth.

## Source 4 — PTU science-fiction material as toolkit, not authority for this layer

Source: Pokémon Tabletop RPG forum / official PTU supplement discussion, “Do Porygons Dream of Mareep?”
https://www.tapatalk.com/groups/pokemon_tabletop/ptu-do-porygons-dream-of-mareep-t4672.html

The supplement is framed as a toolkit for science-fiction campaigns. It supports the general principle that technology level and scientific institutions can vary by campaign. No calibration, sensor or measurement rule from that supplement was imported here because the project’s authoritative PTU/Caelo corpus was not recoverable in this runtime.

## Source 5 — NIST: traceability belongs to measurement results

Source: NIST Technical Note 2156, “Metrological Traceability Frequently Asked Questions and NIST Policy.”
https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2156.pdf

High-level design lessons:

- traceability concerns a measurement result, not a magical permanent property of an instrument;
- a result is related to a reference through a documented chain;
- uncertainty is part of that chain;
- a calibration result applies to a particular device/specimen at a particular time and does not prove that every similar device performs the same way.

Ouros adaptation:

`CALIBRATED` should never mean “always correct.” A calibration event must have scope, date, range/method and a reference. A later impact, repair, environmental exposure or drift can justify a new check without rewriting historical records.

No SI units, legal standards, NIST institutions or real certification regimes are imported into Ouros.

## Source 6 — NOAA: calibration checks and independent sensors

Source: U.S. IOOS, “Manual for Real-Time Quality Control of In-Situ Current Observations,” Appendix B.
https://repository.library.noaa.gov/view/noaa/21151/noaa_21151_DS1.pdf

The manual separates quality assurance from downstream quality control and notes that instruments may need calibration checks after shipment or environmental exposure. It also supports comparison across independent sensors as one way to detect problems.

Reusable Ouros structures:

- four instruments agreeing can strengthen confidence without making any one device infallible;
- a recently calibrated sensor can still be damaged after calibration;
- a failed check creates an investigation, not an automatic fraud/sabotage conclusion;
- method diversity can help distinguish shared bias from local device failure.

## Source 7 — USGS: reference datums and historical comparability

Source: USGS Techniques and Methods 3-A7, “Basic Requirements for Collecting Stage Data.”
https://pubs.usgs.gov/tm/tm3-a7/tm3a7.pdf

The source describes stream gauges referenced to a datum and the value of independent permanent reference marks. It also notes that reference/datum relationships can require resurvey when the physical channel changes.

Ouros adaptation:

A number such as “river height 2.4” is incomplete without knowing the reference surface/version. Two historical maps or gauges can produce different values while both are internally correct for their own datum. A flood, subsidence, bridge rebuild or relocated benchmark can therefore generate a record-version mystery without needing anyone to falsify data.

## Reusable narrative structures

### 1. The instruments disagree

Three instruments report different values. Plausible explanations include:

- different locations;
- different timestamps;
- different methods;
- different calibration references;
- one instrument drifted;
- one instrument was disturbed;
- the measured phenomenon genuinely varies spatially;
- a unit/reference version changed;
- a transcription or conversion error occurred.

The narrative should not choose sabotage simply because disagreement exists.

### 2. The old record was correct then

A historical measurement can remain valid even after standards or datums change. The game should preserve the original value plus the reference context instead of silently rewriting it into the latest convention.

### 3. Calibration creates continuity

A calibration laboratory, reference station or traveling standards team can connect many regions and professions. Their work can generate small recurring stories: missing reference artefacts, inaccessible benchmarks, damaged transfer instruments, seasonal comparison campaigns, interregional standardization and archive corrections.

### 4. Precision must be earned

Ouros should avoid fake precision. A village using visual river marks may know “below normal / normal / high” long before it supports centimeter-scale measurements. A newer institution may later add finer observations. The older record remains useful within its actual resolution.

### 5. The tool changes the observation

Some measurements can disturb the subject or environment. This should hand off to Research Ethics when relevant. A sensor that attracts Pokémon, a camera trap altered by visitor behavior or a sampling device that changes flow can all create method effects.

### 6. Shared standards create interregional stories

Two regions may maintain compatible measurements, partially compatible ones, or independent traditions. Harmonization can be a scientific/institutional project without implying one region was foolish or fraudulent.

## Character and institution archetypes

- field technician who knows the station’s practical history better than its formal documentation;
- archivist who can reconstruct which reference revision an old dataset used;
- instrument maker whose devices are reliable within a narrow range but overused outside it;
- calibration specialist who travels between remote stations;
- researcher who correctly distrusts a measurement but incorrectly guesses the reason;
- local observer whose coarse long-term record exposes a problem missed by a newer precise network;
- standards committee with legitimate disagreement about interoperability;
- apprentice who discovers that a famous dataset used a superseded reference, without proving the scientific conclusion wrong.

## Quest and mystery hooks

- recover a reference marker after a landslide before a regional survey begins;
- compare three gauges after a river changed course;
- determine why a weather station developed a bias only during cold mornings;
- transport a fragile transfer standard to an observatory before a comparison window closes;
- reconstruct the reference system used by a century-old mining map;
- investigate a manufacturing hold where product measurements fail only on one inspection station;
- discover whether an apparent groundwater decline is real or a changed well reference;
- reconcile two astronomy archives whose timestamps use different historical standards;
- inspect whether a sensor failure followed a Pokémon encounter, construction vibration or ordinary component drift without presuming cause.

## Mechanical boundaries

This research creates no PTU/Caelo mechanic.

Do not infer:

- calibration -> Technology Education bonus;
- precise instrument -> Accuracy bonus;
- telescope -> Perception bonus;
- calibrated scale -> capture or breeding modifier;
- benchmark -> movement/range authority inside AutoPTU;
- sensor warning -> automatic battle Weather/Terrain/Status;
- instrument disagreement -> Guile check or criminal case;
- Pokémon with magnetic/electric/psychic capabilities -> universal measurement powers;
- Pokédex data -> omniscient species truth.

If a battle occurs, AutoPTU-Java remains authoritative for battle mechanics. Measurement systems can provide world-state inputs only through an explicit future contract.

## PTU/Caelo validation state

The narrative repository search did not expose the project’s primary Caelo rulebooks, Player’s Guide, encounter list or character-creation source files. Super PTU Online Helper was not available as an invocable capability in this runtime.

Public PTU material was used only for campaign-design context. No Skill DC, Technology Education effect, Researcher Feature, Pokédex mechanic, equipment bonus or sensor rule was imported.

## Design conclusion

Metrology is a high-value connective layer because Ouros already contains dozens of systems that depend on measurements. The durable pattern is:

physical phenomenon -> instrument/method -> calibration/reference context -> observation -> uncertainty/quality state -> dataset -> interpretation -> decision.

That chain creates mysteries, institutional memory and long-term scientific progress without changing world truth to match whatever a gauge currently displays.