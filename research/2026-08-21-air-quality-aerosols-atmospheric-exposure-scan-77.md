# Air Quality, Aerosols & Atmospheric Exposure Research Scan — Pass 77

Status: RESEARCH ONLY. Not canon. External sources are preserved for provenance and structural inspiration. No external prose, plot, character, rule or institution is imported wholesale.

Inspected: 2026-08-21.

## Why this pass exists

The repository already contains dedicated layers for meteorology, wildfire, aridity/dust, volcanism, waste/pollution, outbreak surveillance, light/visibility, freshwater, flora and infrastructure. Those layers can all produce or respond to airborne material, but none currently owns the persistent atmospheric state between source, transport, measurement, exposure, deposition and consequence.

This pass therefore focuses on air quality as a cross-system information and world-state layer rather than another generic pollution system.

The reusable chain is:

`source event -> airborne constituent/plume -> transport/mixing -> observation -> interpretation -> exposure/deposition -> ecological/social response -> later verification`

A visible haze is an observation. It does not identify the pollutant, the source or a PTU effect by itself.

## Pokémon evidence

### Galarian Weezing: species-specific air interaction

Official Pokémon material describes Galarian Weezing consuming polluted air and poisonous gases, removing toxins and expelling cleaner air. The Pokédex also connects its regional form with a historical period of industrial air pollution.

Sources:

- https://swordshield.pokemon.com/en-us/pokemon-galar-region/weezing/
- https://www.pokemon.com/us/pokedex/weezing

Reusable structure:

- a Pokémon species can have a specific relationship with an atmospheric stressor;
- that relationship can become part of regional history and ecology;
- the same species may produce both beneficial and hazardous outputs depending on context;
- institutional use of such a Pokémon should require authored canon and PTU capability/mechanical review rather than being inferred from Pokédex flavor.

Guardrail:

Galarian Weezing lore does not mean every Poison-type filters pollution. It also does not prove an overworld purification rate, radius, capacity, ownership relationship or automatic battle effect.

### Koffing: hazardous gas is species lore, not generic air-quality mechanics

The official Pokédex describes Koffing as containing poisonous gases and notes that those gases are lighter than air.

Source:

- https://www.pokemon.com/us/pokedex/koffing

Reusable structure:

- an individual Pokémon can itself be an atmospheric source;
- source identity, plume observation and health/mechanical consequence should remain separate;
- a Pokémon observed near a gas incident is not automatically the cause unless evidence establishes that link.

Guardrail:

The tactical Move `Poison Gas`, a Koffing's biological lore and a regional air-quality incident are three different objects.

## PTU/Caelo evidence available to this project

Previously recovered Caelo material contains at least one explicit environment where `POISON GAS` is a mechanically authored site effect and applies the PTU Poisoned condition under stated rules. That precedent matters because it demonstrates the correct authority boundary: an environmental atmosphere becomes a mechanical battle effect only when the governing rules/location definition explicitly says so.

The current Python AutoPTU evidence also contains real Poisoned/Badly Poisoned lifecycle behavior and selected Ability/Trainer Feature interactions. These are narrow tactical rules. They do not establish a general atmospheric exposure engine.

Therefore:

- visual smoke != Poisoned;
- haze != Accuracy penalty;
- odor != status condition;
- industrial emissions != `Poison Gas` Move;
- volcanic gas != automatic Poisoned;
- wildfire smoke != automatic tick damage;
- Galarian Weezing presence != automatic purification.

The full primary Caelo corpus was not reliably recoverable in this run, so no new Caelo-specific environmental rule is asserted beyond previously recovered project evidence.

## Air-quality science used as design reference

### Airborne particles can travel and later deposit

US EPA describes particulate matter as particles and droplets suspended in air. Fine particles can strongly reduce visibility and may travel before settling onto ground or water. Depending on composition, deposition can affect lakes, streams, soils, forests, crops and ecosystem diversity.

Sources:

- https://www.epa.gov/pm-pollution/health-and-environmental-effects-particulate-matter-pm
- https://www.epa.gov/wildfire-smoke-course/wildfire-smoke-complex-mixture

Reusable structure:

A source can affect locations far away. Ouros should therefore allow an air-quality event to have separate source geometry, plume/transport geometry and deposition footprint.

A downstream region can experience haze or deposition even if the source is outside the loaded Minecraft area.

### Different indicators describe different atmospheric problems

National Park Service monitoring uses separate indicators for particulate matter, ozone, visibility, nitrogen/sulfur deposition and other air-quality concerns rather than one universal pollution score.

Sources:

- https://www.nps.gov/articles/air-analysis-methods-latest.htm
- https://www.nps.gov/im/sodn/air-quality.htm

Reusable structure:

Ouros should not store only `air_quality = bad`.

Possible coarse dimensions include:

- particulate load;
- visibility impairment;
- irritant/toxic constituent claim;
- ozone-like reactive pollution if authored;
- wet/dry deposition;
- odor report;
- smoke fraction/source hypothesis;
- biological aerosol/spore observation;
- instrument confidence;
- public advisory state.

These are world-model dimensions, not PTU modifiers.

### Atmosphere can affect ecology without immediate visible damage

NPS and EPA sources describe atmospheric pollution affecting vegetation, surface water, soils, wildlife and scenic visibility. Nitrogen/sulfur deposition and ozone can produce effects over time that are not equivalent to an acute exposure event.

Sources:

- https://www.nps.gov/articles/airprofiles-ever.htm
- https://www.nps.gov/yose/learn/nature/airquality.htm
- https://www.epa.gov/eco-research/ecosystems-and-air-quality
- https://www.epa.gov/air-quality/air-animals-and-plants

Reusable structure:

A short-term air episode and a long-term deposition trend need different clocks.

Examples:

- a smoke plume affects visibility today;
- repeated deposition changes a sensitive pond or vegetation unit over seasons;
- an industrial source is reduced but old deposition remains in soil/water records;
- improved visibility does not prove ecological recovery.

### Wildfire smoke is a mixture, not a single status

EPA treats wildfire smoke as a mixture containing particulate matter and gaseous pollutants, with PM2.5 receiving special attention for health effects. Ozone may also form downwind under some atmospheric conditions rather than being emitted directly by fire.

Sources:

- https://www.epa.gov/wildfire-smoke-course/wildfire-smoke-complex-mixture
- https://www.epa.gov/wildfire-smoke-course/why-smoke-health-concern

Reusable structure:

Wildfire -> smoke source does not mean the entire plume has one constant composition or effect. Meteorology can change transport and chemistry after the fire event itself.

This makes cross-layer stories possible without inventing medical mechanics:

`wildfire event -> plume -> monitor readings -> public advisory -> travel/observatory change -> later deposition survey`

## Narrative structures worth reusing

### Source attribution as a mystery

A poor-air episode can have several plausible sources:

- wildfire smoke transported from another region;
- dust from an exposed dry basin;
- industrial combustion;
- volcanic emissions;
- construction dust;
- pollen/spores;
- waste-treatment incident;
- multiple sources at once.

The player can investigate source attribution without every case becoming sabotage.

### Monitoring-network stories

Air-monitoring stations create useful persistent infrastructure:

- sensor outages;
- calibration problems;
- mobile sampling;
- disagreements between nearby monitors;
- old datasets with different methods;
- public dashboards;
- coverage gaps;
- maintenance jobs;
- instruments relocated after urban growth.

The interesting question is often whether the measurement represents the region, not whether it is simply true/false.

### Forecast versus observation

Meteorology predicts transport conditions. Air-quality monitoring observes atmospheric state. They should link but remain independent.

A forecast can correctly predict winds yet still miss the source magnitude. A plume can arrive earlier because the source changed. A monitor can show clean air while a nearby valley traps pollutants outside its coverage.

### Exposure versus diagnosis

Outbreak/health surveillance already separates exposure from diagnosis. Air Quality should emit possible exposure records, not medical conclusions.

A person or Pokémon being present in a plume does not create a disease, Injury or PTU Status.

### Visibility as information

Haze changes what characters can observe at long range, but the current battle engine's verified LoS is geometric. Narrative visibility should remain outside tactical LoS until an explicit visibility contract exists.

This connection can still drive:

- delayed aerial surveys;
- astronomy cancellations;
- photography ambiguity;
- ferry/air-route caution;
- scenic-tourism impacts;
- missing landmark reports.

## Cross-layer integration opportunities

Meteorology -> plume transport and dispersion context.

Wildfire -> smoke source event.

Aridity -> dust source event.

Volcanism -> ash/gas source event.

Waste/Technology -> industrial or treatment source event.

Outbreak/Health -> exposure signal only, never automatic diagnosis.

Flora -> long-term ozone/deposition observations and pollen/biological aerosols when authored.

Freshwater/Soil -> wet/dry deposition recipient state.

Astronomy/Photography/Cartography -> visibility and observation-quality context.

Travel/Aerial/Maritime -> advisories, delays and route visibility.

Public Media -> advisories, corrections, rumors and source claims.

Conservation -> sensitive receptor areas and monitoring goals.

## Copyright / transformation policy

Pokémon sources are used for high-level factual species/world precedents only. No dialogue, episode scene text or distinctive plot is copied.

EPA/NPS material is used to understand environmental process structure. Ouros should not copy real regulatory thresholds, U.S. agency structures, AQI categories or legal frameworks unless deliberately authored later.

The purpose of the real-world research is to derive believable causal graphs, not reproduce contemporary environmental regulation.

## Design conclusions

1. Air quality needs persistent state independent from Weather.
2. A source, a plume, a measurement and an effect are separate entities.
3. Air-quality state should be spatial and temporal rather than one region-wide scalar.
4. Different pollutants/observations need different evidence and clocks.
5. Deposition connects atmosphere to soil/water long after the visible plume disappears.
6. Species-specific atmospheric behavior must remain species-specific.
7. Atmospheric exposure never creates PTU Status, damage or Accuracy effects without explicit validated rules.
8. Minecraft particles/fog are presentation, not authority.
9. Reduced encounter versions should freeze or exclude atmospheric mechanics until Java has verified environment/hazard support.
10. Source attribution, monitor reliability and delayed ecological consequence can generate long arcs without requiring a villain.

## Source register

- Pokémon Sword/Shield official Galarian Weezing page: https://swordshield.pokemon.com/en-us/pokemon-galar-region/weezing/
- Official Weezing Pokédex: https://www.pokemon.com/us/pokedex/weezing
- Official Koffing Pokédex: https://www.pokemon.com/us/pokedex/koffing
- EPA wildfire smoke composition: https://www.epa.gov/wildfire-smoke-course/wildfire-smoke-complex-mixture
- EPA wildfire smoke health background: https://www.epa.gov/wildfire-smoke-course/why-smoke-health-concern
- EPA particulate environmental effects: https://www.epa.gov/pm-pollution/health-and-environmental-effects-particulate-matter-pm
- EPA ecosystems and air quality: https://www.epa.gov/eco-research/ecosystems-and-air-quality
- EPA air, animals and plants: https://www.epa.gov/air-quality/air-animals-and-plants
- NPS Air Quality Analysis Methods: https://www.nps.gov/articles/air-analysis-methods-latest.htm
- NPS air quality ecological background: https://www.nps.gov/im/sodn/air-quality.htm
- NPS Everglades air profile: https://www.nps.gov/articles/airprofiles-ever.htm
- NPS Yosemite air quality: https://www.nps.gov/yose/learn/nature/airquality.htm
