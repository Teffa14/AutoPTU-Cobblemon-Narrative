# Environmental DNA, Presence Inference & Sampling Provenance Scan — Pass 332

Status: RESEARCH / PROVENANCE. Not Ouros canon.
Date: 2026-09-07

## Repository inspection before research

The current recursive repository tree at `437c0228c949a3d17c7675b2b4f9b02483dba2e3` was inventoried before authoring. `CURRENT_FOCUS.md`, canon governance, the playable foundation, the current Kairos source index, the Pass 331 telemetry work, recent investigation/environmental passes and repository-wide searches for environmental DNA, eDNA, metabarcoding, genetic samples, sample contamination and species-detection inference were reviewed.

No dedicated environmental-DNA or sample-to-presence provenance owner was found. Existing observation, archive, communication and wildlife-telemetry systems remain reusable dependencies rather than substitute owners.

Canon remains untouched. This file is research only.

## Public research sources

### U.S. Geological Survey — eDNA overview

Source: https://www.usgs.gov/science/science-topics/edna

Reusable lessons:

- environmental DNA is genetic material shed into the environment by living or formerly living organisms;
- material can come from cells, mucus, gametes, feces, carcasses and other biological traces;
- eDNA is valuable for detecting rare, invasive or difficult-to-observe organisms;
- detecting DNA does not by itself reveal the complete current state of the organism that produced it.

Ouros abstraction:

`DNA_DETECTED != SUBJECT_CURRENTLY_PRESENT_AT_SAMPLE_POINT`

The sample can be genuine while the inferred current location, abundance or time of presence remains uncertain.

### U.S. Geological Survey — transport, sediment accumulation and persistence

Source: https://www.usgs.gov/publications/influence-sediment-and-stream-transport-detecting-a-source-environmental-dna

Reusable lessons:

- eDNA can be transported by flowing water away from its source;
- sediment can retain material differently from the water column;
- settling, resuspension, dispersion and decay affect what a sample means;
- DNA may remain detectable after the source organism has left;
- ambient hydrology matters when inferring source location or abundance.

Ouros abstraction:

`SAMPLE_LOCATION != SOURCE_LOCATION`

A downstream positive can justify follow-up without proving that the detected Pokémon occupied the exact sampled feature during the collection window.

### U.S. Geological Survey — field sampling protocols

Source: https://www.usgs.gov/publications/environmental-dna-sampling-protocol-filtering-water-capture-dna-aquatic-organisms

Reusable lessons:

- collection, filtration, preservation and handling are distinct stages;
- protocol details and equipment matter for reproducibility;
- sample identity must survive transport from field collection into later analysis;
- field workflows can be standardized without pretending that every result is certain.

Ouros abstraction:

Sample provenance should preserve at minimum collection feature, collection time, collector, container/sample identity, processing lineage and analysis result. A laboratory result without field lineage is incomplete evidence.

### U.S. Geological Survey — occupancy and replicate sampling

Source: https://www.usgs.gov/publications/estimating-occupancy-and-abundance-stream-amphibians-using-environmental-dna-filtered

Reusable lessons:

- repeated subsamples can improve precision;
- low-density species can be detected when traditional observation misses them;
- concentration can correlate with density under some studied conditions, but interpretation depends on protocol and context;
- sampling design matters when moving from detection to stronger ecological claims.

Ouros abstraction:

`ONE_POSITIVE_SAMPLE != POPULATION_ESTIMATE`

Repeated observations can increase confidence while preserving uncertainty instead of triggering a binary omniscient conclusion.

### U.S. National Park Service — multi-marker fish-community surveys

Source: https://www.nps.gov/articles/aps-19-1-6.htm

Reusable lessons:

- eDNA can complement or replace some expensive capture-based surveys for broad inventory work;
- multiple genetic markers can reduce the risk of spurious detections;
- community-level survey results are generated from samples rather than direct sightings.

Ouros abstraction:

A result can support a species-level claim with an explicit confidence basis while remaining distinct from individual identification, current count, sex, health, intent or exact position.

### U.S. National Park Service — repeated spring inventories

Source: https://www.nps.gov/articles/000/sodn_edna_inventories.htm

Reusable lessons:

- repeated seasonal sampling can improve detection probability;
- water volume and environmental conditions can change how easily DNA is detected;
- managers combine recurring samples across sites rather than treating one collection as permanent truth.

Ouros abstraction:

`NEGATIVE_SAMPLE != SPECIES_ABSENT`

A negative observation should preserve sampling conditions and its limited temporal/spatial scope.

### Pokémon official material — New Pokémon Snap ecological survey

Source: https://newpokemonsnap.pokemon.com/en-us/
Source: https://newpokemonsnap.pokemon.com/en-au/create-photodex/

Reusable high-level structure:

New Pokémon Snap frames repeated expeditions as an ecological survey. Observations accumulate in a research record, repeated visits reveal different behavior, and the same environment can yield new information over time.

Ouros use:

Reuse only the repeated-survey structure: field expedition, observation capture, evidence return, research record, revisitation and changing interpretation. Do not copy Lental, Professor Mirror, Illumina, NEO-ONE, Photodex scoring, routes, encounters or dialogue.

### PTU actual-play source — Pokémon: Adventures in the Millennium

Source: https://www.podchaser.com/podcasts/pokemon-adventures-in-the-mill-702825

The public show description identifies the campaign as Pokémon Tabletop United and divides its long-running story into named acts, including a substantial science-themed arc.

Reusable high-level structure:

- a PTU campaign can sustain an investigation topic across many sessions instead of resolving it in one encounter;
- scientific or technical inquiry can function as a story arc alongside Trainer growth;
- revisiting evidence after later discoveries can change the meaning of earlier scenes.

Ouros use:

Use only the long-form investigation cadence. Do not copy characters, Sinnoh material, episode plots, titles, dialogue or distinctive campaign events.

## Design synthesis for Ouros

Environmental DNA is useful because it creates strong evidence without granting exact-location omniscience.

A durable evidence chain can be:

`subject/species source -> shedding event -> environmental medium -> transport/decay/resuspension -> sample collection -> sample custody -> processing -> assay/result -> analyst interpretation -> explicit recipient -> institutional decision -> follow-up sample or direct observation`

Every arrow can change what the evidence supports.

Important separations:

- `DNA_DETECTED != SUBJECT_CURRENTLY_PRESENT`
- `SAMPLE_LOCATION != SOURCE_LOCATION`
- `SPECIES_DETECTION != INDIVIDUAL_IDENTIFICATION`
- `DETECTION != ABUNDANCE`
- `DETECTION != BREEDING_POPULATION`
- `NEGATIVE_SAMPLE != SPECIES_ABSENT`
- `OLD_MATERIAL != NEW_OCCUPANCY`
- `SEDIMENT_POSITIVE != WATER_COLUMN_POSITIVE`
- `LAB_RESULT != FIELD_PROVENANCE`
- `DERIVED_MAP != RAW_SAMPLE_SET`
- `ONE_ASSAY_RESULT != INSTITUTIONAL_CONCLUSION`

## Narrative opportunities

### The positive downstream sample

A rare or disputed Pokémon signature appears downstream from a managed wetland. The result is real, but transport makes the source ambiguous. Follow-up work shifts from “find the Pokémon at this exact bank” to comparing tributaries, sampling windows and direct observations.

### The species that left before anyone looked

A positive sample triggers a field visit that finds nothing. Sediment, delayed processing or recent departure explains how both observations can be correct. The result can still alter a habitat-management decision without requiring a direct sighting.

### Conflicting matrices

Water samples are negative while sediment is positive, or the reverse. Different teams can hold compatible evidence about different environmental compartments.

### The clean repeat

A first positive is followed by several negatives. Possible explanations include transient passage, transport from elsewhere, sample contamination, environmental dilution, assay error or a real low-density population. The story remains about evidence quality before blame.

### The map that became too certain

An institution converts sample points into a public “species range” map that visually implies continuous occupancy. Later field evidence forces a correction. Publication, receipt and belief history remain separate from the raw sample archive.

## Battle implementation boundary

eDNA itself is world-state evidence. It does not require a combat mechanic.

A mechanically rich follow-up encounter could later include moving water, rescue, unstable banks, concealment, weather, territorial behavior, time-sensitive sampling, equipment protection or a wild Pokémon that should not simply be defeated. Those additions must remain gated by the permanent capability families.

Reduced implementation:

- collect or resolve samples between scenes as semantic world events;
- preserve sample IDs, collection features, times, custody and result lineage;
- keep transport/decay as authored world-state evidence rather than fluid simulation;
- use ordinary verified targeting/range/LoS only where no special concealment rule is required;
- use ordinary base movement only;
- keep species-presence claims outside Minecraft entity existence;
- never let spawning, despawning or chunk presence decide ecological truth.

## PTU / Caelo source boundary

The inspected narrative repository continues to expose comparative material under `sources/kairos`. `sources/kairos/KAIROS_SOURCE_INDEX.md` routes research/utility classes, world population/ecosystem guidance, movement, hazards and terrain/weather into the supplied Kairos compilation but explicitly states that the index is only a routing aid and Kairos rules are not automatically Ouros law.

No adopted `sources/caelo` rules source was found in the inspected tree.

This pass therefore defines no numerical rules for Researcher, Survival, Perception, Education Skills, sample collection, laboratory analysis, species detection, tracking, movement, water, weather, contamination, Moves, Abilities, Items or Trainer Features.

Public ecology science and Pokémon/PTU material support narrative structure only. Mechanical authority remains with the project's adopted PTU/Caelo/AutoPTU evidence.

## Copyright boundary

No protected dialogue, named plotline, encounter map, distinctive character or campaign storyline is copied. Research sources are preserved for provenance while Ouros material uses transformed structural lessons only.
