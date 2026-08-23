# Narrative Research Scan — Pass 131: Climate Baselines, Long-Term Change & Adaptation

Status: RESEARCH / PROVENANCE ONLY. Not established canon.
Date: 2026-08-23

## Why this pass exists

The repository already has strong authorities for short and medium temporal scales:

- `seasonality-calendar-phenology-layer.md` owns recurring calendar phases, expected seasonal conditions and phenology;
- `meteorology-forecasting-weather-layer.md` owns actual weather, observations, forecasts and forecast verification;
- domain layers such as Cryosphere, Wildfire, Freshwater, Coastal Geomorphology, Coral Reefs, Alpine Ecology, Urban Heat and Wildlife Migration own their physical/ecological state.

What was still missing was a longitudinal authority for statements such as:

- what counted as a regional climate normal in a particular era;
- whether a ten- or thirty-year series shows a trend;
- whether two institutions are comparing against the same baseline;
- whether a change is a one-year anomaly, an oscillation, a persistent shift or still uncertain;
- how institutions plan under several plausible futures without treating one scenario as prophecy;
- how long-term change reaches other Ouros systems without becoming a direct PTU battle mechanic.

This pass therefore researches climate baselines, historical comparison, trend assessment, regime-shift candidates and adaptation planning. It does not create climate canon for Ouros.

## Repository overlap review

The full `design/`, `research/` and `proposals/` inventories were inspected before selecting this topic. No existing file owns dated climate normals, baseline editions, multi-year climate trend assessments, scenario sets or cross-domain adaptation plans.

Important boundaries:

- Meteorology remains the authority for weather events and forecasts.
- Seasonality remains the authority for recurring annual cycles.
- Metrology remains the authority for calibration, traceability and comparability of measurements.
- Science remains the authority for datasets, hypotheses and publication history.
- Each environmental layer remains the authority for the physical response in its own domain.

## Source 1 — NOAA climate normals: a baseline is a dated reference frame

Source: NOAA National Centers for Environmental Information, “1991–2020 U.S. Climate Normals — Annual/Seasonal Normals.”
URL: https://www.ncei.noaa.gov/pub/data/cdo/documentation/normals-annualseasonal-1991-2020_documentation.pdf

Reusable structure:

Climate “normal” can be represented as a versioned statistical product rather than timeless world truth. NOAA’s conventional normals use a thirty-year period, combine many observing records and attach completeness/quality flags. That is valuable for Ouros because a baseline can have:

- a reference interval;
- a variable and spatial scope;
- source observations/stations;
- a method/version;
- quality/completeness state;
- a publication date.

Design lesson:

Changing the baseline must not rewrite the observations. The same summer can be described as +1.2 relative to one dated baseline and +0.7 relative to a later baseline without contradiction. Chronicle should preserve both statements with their baseline references.

Do not import NOAA’s exact thirty-year requirement, flags or variable catalogue into Ouros. Those are real-world implementation choices, not Pokémon canon.

## Source 2 — NPS adaptation planning: historical baselines may stop being adequate targets

Source: U.S. National Park Service, “Climate Adaptation Planning.”
URL: https://www.nps.gov/im/adaptation-planning.htm

Source: U.S. National Park Service, “Park-specific Climate Futures.”
URL: https://www.nps.gov/subjects/climatechange/climatefutures.htm

Reusable structure:

Long-term monitoring can reveal that restoring every system to a historical snapshot is no longer feasible or useful. Adaptation planning can instead compare several plausible futures and choose actions that are robust across more than one.

For Ouros this suggests separating:

- historical reference state;
- desired management goal;
- plausible future scenarios;
- vulnerability assessment;
- chosen adaptation action;
- observed result years later.

A scenario is not a forecast and a forecast is not prophecy.

Design lesson:

A town may raise a bridge, change a planting calendar or relocate a seasonal trail before scientists agree on one exact future. The important narrative question is what evidence was available and why the institution chose that action at that time.

## Source 3 — NPS long-term monitoring: climate change is cross-domain, not one meter

Source: U.S. National Park Service, “How Monitoring Informs Park Conservation in a Changing Climate.”
URL: https://home.nps.gov/im/climate-and-conservation.htm

Source: U.S. National Park Service, “Project Profile: Analyze Monitoring and Inventory Data for Climate Vulnerability Analysis and Adaptation Planning.”
URL: https://www.nps.gov/articles/ira-projectprofile-imd-analyzevitalsigns.htm

Reusable structure:

Long-term indicators can come from many systems at once: vegetation, aquatic resources, wildlife, fire, hydrology and other monitored resources. A climate assessment does not need to duplicate all those states. It can reference their authoritative series.

Ouros implication:

There should be no global `climate_health = 63`. A region can show earlier flowering, less persistent snowpack, unchanged annual precipitation, hotter nights and stable fish counts at the same time.

## Source 4 — USGS phenology: timing shifts require comparable long-term records

Source: U.S. Geological Survey, “Standardized phenology monitoring methods to track plant and animal activity for science and resource management applications.”
URL: https://www.usgs.gov/publications/standardized-phenology-monitoring-methods-track-plant-and-animal-activity-science-and

Reusable structure:

Long-term phenological records are useful for detecting shifts, but comparisons become weak when sites or methods differ. This supports a climate layer that references method/version and monitoring effort rather than treating every observation as directly comparable.

Ouros implication:

Five earlier blossom dates can be meaningful evidence only if the observation series has adequate provenance. A new observer using a different route or definition should not silently extend an older series.

## Source 5 — Pokémon official Pokédex: climate history can leave biological legacy

Source: The Pokémon Company, Corsola Pokédex.
URL: https://www.pokemon.com/us/pokedex/corsola

The official Pokédex includes a Galarian Corsola entry where sudden climate change is part of the species/form’s historical explanation.

Reusable structure:

Environmental change can leave long-lived biological and cultural traces that remain visible after the original event. Collections, fossils, archives, distribution records and living populations can all preserve different pieces of that history.

Strict transformation rule:

Ouros must not copy Galar’s event, invent a climate-extinct Corsola population, create a regional form, change Types/Abilities, or assume climate change mechanically causes evolution. The reusable lesson is only that ecological history may outlive the event that produced it.

## Source 6 — Public PTU campaign premise: long environmental change can become regional history

Source: public /r/PokemonTabletop campaign recruitment post, “Looking for players for an ongoing PTU game,” 2024-12-17.
URL: https://www.reddit.com/r/PokemonTabletop/comments/1hgbuha

The campaign premise describes a region reshaped by increasingly severe environmental disasters and then revisited decades later.

Reusable structure:

A campaign can begin after a long environmental transition has already changed settlements, routes, institutions and collective memory. Players do not need to arrive at year zero of every problem.

Transformation rule:

Do not copy the region, cataclysm, sealed-vault premise, persistent storm, chronology or plot. Ouros can instead use ordinary multi-year change whose consequences accumulate gradually through existing systems.

## Source 7 — Pokémon Climate Redux: useful anti-pattern and useful structure

Source: Pokémon Climate Redux community wiki, “New Features.”
URL: https://pokemon-climate-redux.fandom.com/wiki/New_Features

The fan project explicitly links climate/environment themes to Gym quests, disasters and proposed environmental variants.

Useful high-level lesson:

Environmental change can be distributed through many local institutions rather than confined to one scientist NPC.

Anti-pattern for Ouros:

Do not require every Gym or route to produce an environmental crisis quest. Do not create new forms, evolution methods, battle conditions or disaster mechanics merely to signal climate themes. A persistent world needs many normal years, quiet observations and successful adaptations that never become battles.

## Cross-source design conclusions

### 1. Baselines need identity and revisions

A baseline is a comparison product. It should have its own ID, time window, method and publication state. Old editions remain valid historical records.

### 2. Climate evidence is assembled from other authoritative systems

Temperature series may come from Meteorology; snow duration from Cryosphere; first flowering from Flora/Phenology; migration timing from Wildlife Migration; lake turnover from Limnology; shoreline position from Coastal Geomorphology. The climate layer references these observations rather than rewriting them.

### 3. One event does not prove a trend

A heatwave, flood, cold snap or storm is weather/hazard state. A trend requires a time series and an explicit assessment. The generator must not use one dramatic event as automatic proof of long-term change.

### 4. A trend does not prove a cause

Attribution can remain uncertain or multi-causal. Land use, sensor moves, infrastructure, ecological feedback, natural variability and wider climate change can coexist as hypotheses.

### 5. Adaptation is a decision under uncertainty

A community can adapt before certainty is perfect. Chronicle should preserve the evidence, scenarios and tradeoffs available when the choice was made.

### 6. Historical “normal” is not automatically the restoration target

Some projects may preserve a historical state. Others may protect function, connectivity or cultural value under changed conditions. The target must be authored, not assumed.

### 7. No direct climate-to-battle shortcut

Long-term climate state must never directly set AutoPTU Weather, Terrain, Status, damage, Accuracy, initiative or forced movement. A current battle receives only currently valid environmental mechanics after the owning world layer and PTU/AutoPTU rules validate them.

### 8. No direct climate-to-spawn shortcut

A trend can motivate ecological monitoring. Actual distribution/abundance changes belong to Wild Collectives, Migration, Biosecurity, Island Biogeography or other ecological authorities. Minecraft entity counts are not climate evidence.

## Candidate data concepts emerging from research

- `CLIMATE_BASELINE`
- `CLIMATE_BASELINE_REVISION`
- `CLIMATE_ANOMALY_RECORD`
- `CLIMATE_INDICATOR_SERIES_LINK`
- `CLIMATE_TREND_ASSESSMENT`
- `CLIMATE_ATTRIBUTION_CLAIM`
- `CLIMATE_REGIME_SHIFT_CASE`
- `CLIMATE_VULNERABILITY_PROFILE`
- `CLIMATE_SCENARIO_SET`
- `CLIMATE_ADAPTATION_PLAN`
- `CLIMATE_ADAPTATION_ACTION`
- `CLIMATE_ADAPTATION_REVIEW`

## PTU/Caelo boundary

No public narrative source is treated as a rules source.

The project’s full named Caelo corpus was not recoverable as an invocable source in this runtime. Super PTU Online Helper was also not exposed as a callable capability. Therefore this pass does not assert:

- climate-based Skill DCs;
- environmental damage;
- heat/cold exposure rules;
- climate-caused Status;
- weather creation;
- migration speed;
- regional-form creation;
- evolution triggers;
- spawn modifiers;
- climate-related Trainer Feature effects.

Those remain pending authoritative PTU/Caelo and engine validation.