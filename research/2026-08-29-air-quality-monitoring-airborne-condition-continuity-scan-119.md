# Air-Quality Monitoring & Airborne-Condition Continuity Research — Pass 119

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. Not a PTU rules source.
Date: 2026-08-29

## Research question

How can Ouros preserve air-quality observations, monitoring coverage, uncertainty, smoke/haze/plume reports, revised assessments and downstream operational responses without duplicating Pollution, Weather, Wildfire, Volcanic Monitoring, Community Health, Public Notices or tactical PTU mechanics?

## Repository inspection and gap

The recursive repository inventory was inspected before authoring. Existing adjacent systems already cover substantial parts of the problem:

- `waste-sanitation-recycling-pollution-layer.md` owns generic contamination observations, environmental source claims and cleanup provenance, including observations whose medium is air.
- `wildfire-fire-response-incident-continuity-extension.md` owns fire incidents, smoke reports associated with those incidents, fire sectors and response history.
- `volcanic-monitoring-eruption-ashfall-recovery-continuity-extension.md` owns volcanic observations, plumes, ashfall observations and eruption assessment history.
- `weather-forecast-preparedness-operational-extension.md` owns weather observations, meteorological forecasts and their revision/distribution history.
- `community-health-surveillance-cluster-investigation-continuity-extension.md` owns aggregate health signals and cluster investigations, while explicitly leaving environmental air truth to its owner system.
- Communications/Public Notices own message dissemination and receipt.
- Care owns diagnosis, treatment and individual health state.
- Travel/Road/Rail/Aviation/Maritime/Workplace/Facility owner systems decide their own restrictions and reopening.

No dedicated layer preserves the operational information chain between an airborne observation and those owner systems. The missing continuity is:

monitor site or observer -> bounded observation -> quality/provenance review -> spatial interpretation -> versioned air-condition assessment -> information handoff -> owner-system response -> later revision/closure/legacy.

The new layer therefore specializes air-quality monitoring continuity. It does not replace the generic Pollution observation model or any source-specific incident model.

## Public Pokémon sources

### Gringey City / “Sparks Fly for Magnemite”

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Gringy_City
- https://bulbapedia.bulbagarden.net/wiki/EP030

The animated-series location is an industrial settlement whose long-running pollution forms part of its social and environmental identity. The same episode also contains a Pokémon health problem that is initially interpreted one way and later explained by a different mechanism.

Reusable Ouros structures:

- persistent environmental degradation can change settlement reputation, population and routine rather than appearing only during a single quest;
- environmental context can coexist with unrelated infrastructure and medical problems;
- proximity in time does not prove that an environmental condition caused a health observation;
- a polluted-looking settlement can produce multiple independent investigations whose evidence must remain separate.

Transformation boundary:

Do not copy the city, characters, blackout plot, Grimer event, Pikachu diagnosis, resolution or dialogue. Ouros uses only the high-level structure of a settlement carrying environmental history while several systems fail or recover independently.

### Pokémon Mystery Dungeon: summit smog/fog as a location-state cue

Source:
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Mystery_Dungeon:_Explorers_of_Sky/Chapter_22

The summit sequence demonstrates a location whose familiar identity is altered by persistent fog/smog and changed Pokémon occupancy.

Reusable Ouros structure:

A place can become narratively unfamiliar because visibility, atmosphere, occupancy and public interpretation changed. Returning later can reveal recovery or a new equilibrium.

Hard guardrail:

The specific cause, characters, species conflict and dungeon sequence are not imported. Visible haze in Ouros is evidence or presentation unless an authored environmental rule gives it a tactical effect.

### Haze as a named Move proves why visuals cannot become environment rules

Source:
- https://bulbapedia.bulbagarden.net/wiki/Haze_(move)

Haze is a specific Pokémon Move with defined battle effects. Its visual concept does not authorize generic environmental haze to reproduce those effects.

Reusable guardrail:

A visual word shared between the overworld and a Move does not make the overworld condition an invocation of that Move. Any Move-derived interaction remains under exact move-specific behavior and must be backed by PTU/Caelo rules plus runtime support.

## Public PTU/community material

### Pokémon Tabletop Torkoal spotlight

Source:
- https://pokemontabletop.com/pokemon-spotlight-torkoal/

This public community article contains variant/homebrew smoke mechanics for particular Torkoal concepts.

Use for Ouros:

It is valuable primarily as a provenance warning. Pokémon Tabletop community material can combine setting flavor and mechanical additions. A public tabletop article is not automatically governing PTU/Caelo evidence for Ouros. Its smoke effects, variant typing, abilities and mechanical consequences are not imported.

The reusable structural idea is narrower: an individual or locally authored Pokémon lineage may have a documented relationship to airborne material if canon and rules explicitly establish it. Species identity alone is insufficient.

## Operational research used only for abstraction

### AirNow: different products can legitimately disagree

Sources:
- https://www.airnow.gov/fires/using-airnow-during-wildfires/
- https://www.airnow.gov/how-to-use-this-site/
- https://www.airnow.gov/fasm-v4/how-to-use/

AirNow documents that its general dial, interactive map and Fire and Smoke Map use different monitor sets, pollutants and data products. Permanent monitors, temporary monitors and additional sensors can provide different spatial coverage. Map contours are derived from multiple observations rather than direct measurements at every point.

Reusable Ouros principles:

- product identity and input set must be preserved;
- two maps can differ without either record being fraudulent;
- a point observation and a spatial interpretation are different evidence objects;
- temporary monitoring can increase coverage during an episode;
- later products should supersede earlier products without deleting them.

No AQI thresholds, pollutant limits, correction equations, monitor specifications or U.S. institutional structure are imported.

### AirNow/EPA: plume observations and ground-level measurements are separate

Sources:
- https://www.airnow.gov/fasm-v4/about/
- https://www.epa.gov/wildfire-smoke-course/where-find-air-quality-smoke-reports-fire-and-smoke-map

These public products display fire locations, smoke plumes and ground-level particle observations as distinct layers. Their coexistence is the key lesson for Ouros.

Reusable Ouros principle:

`PLUME_OBSERVED` must not silently become `GROUND_LEVEL_AIR_CONDITION_CONFIRMED` for every place beneath or near a visualized plume.

The reverse also matters: an adverse local observation need not prove that a visible distant plume is its cause.

### EPA sensor/monitor architecture

Source:
- https://www.epa.gov/air-sensor-toolbox/technical-approaches-sensor-data-airnow-fire-and-smoke-map

The public architecture distinguishes stationary long-term monitoring, temporary monitors and other sensors used to improve spatial information during smoke events.

Reusable Ouros principles:

- monitor type, operator, method and provenance matter;
- temporary deployments can exist without becoming permanent infrastructure;
- a monitoring gap is an information gap, not proof of clean or polluted air;
- additional observations can improve coverage without rewriting earlier evidence.

No real-world instrumentation requirements or data-correction methods are imported.

## PTU / Caelo cross-check

Existing project evidence in `research/2026-08-18-source-scan.md` establishes a strict environmental boundary. Caelo can give a location mechanical identity when its governing source explicitly defines that effect; Toxic Ravine is the known example. This does not establish a universal air-quality, smoke, particulate, gas, visibility or exposure subsystem.

Pass 119 therefore does not infer any of the following without exact governing evidence:

- generic smoke-based accuracy or LoS penalties;
- generic haze-based stat changes;
- automatic Poison, Burn, Sleep, Confusion or other status from bad air;
- exposure accumulation or duration thresholds;
- respiratory damage;
- species- or Type-based immunity;
- pollution sensing by species;
- filtration or purification from a Pokémon's presence;
- wind automatically clearing airborne conditions;
- Weather Moves automatically changing environmental pollution;
- Haze, Defog, Smog, Clear Smog or another Move affecting world air unless its exact rule permits the interaction;
- Trainer Feature, Ability or Item interactions without source and runtime evidence.

## Reusable Ouros principles

### Observation, interpretation and source attribution remain separate

A smell report, visible haze, monitor reading, plume image and health complaint can all be useful evidence while referring to different subjects.

Air monitoring owns what was observed and how it was interpreted spatially. Pollution/Case authority owns causal source claims. Care/Community Health owns health interpretation.

### Coverage must be explicit

An operating monitor establishes evidence for its authored observation context. It does not prove that the entire settlement, valley or route was sampled.

A missing reading becomes `UNKNOWN_FOR_INTERVAL` or another explicit gap state.

### Spatial products are versioned claims

A map derived from several sites is a product with:

- issue time;
- valid/effective window;
- input observations;
- spatial scope;
- interpolation or interpretation method reference if canon supports one;
- known gaps;
- confidence/quality note;
- supersession chain.

The system must never treat every colored map cell as a direct sensor observation.

### Visible appearance remains weak evidence

Blue sky does not prove a clean observation. Haze does not identify a source. Odor does not prove toxicity. A Pokémon leaving an area does not prove exposure or predictive ability.

### Downstream decisions remain owned by downstream systems

An air-condition assessment can be handed to a school, event, road operator, airline, workplace, clinic, conservation team or crisis coordinator. Each owner decides its own response. Improvement in the air record does not automatically reopen anything.

## Copyright and transformation boundary

External works are used only for high-level structure, state separation and design lessons. No protected dialogue, distinctive character arc, exact encounter sequence, map layout, proprietary threshold or mechanical homebrew package is reproduced.

## Research conclusion

A dedicated air-quality continuity layer is justified because the repository currently has source incidents, generic contamination, weather, health and public notices but lacks a persistent bridge for monitoring coverage and versioned airborne-condition interpretation.

The layer should be primarily informational and operational. Rich tactical airborne effects remain gated by explicit PTU/Caelo rules and the engine capability families recorded in the current readiness snapshot.