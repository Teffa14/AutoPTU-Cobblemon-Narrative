# Urban Heat, Microclimate & Thermal Comfort Research Scan — Pass 85

Status: RESEARCH ONLY. Not Ouros canon. Not a PTU rules source.

Date: 2026-08-21

## Why this pass exists

The repository already has layers for Meteorology, Air Quality, Architecture, Urban Public Space, Flora, Health Surveillance, Energy Infrastructure, Light, Hydrology and Accessibility.

What was missing was a dedicated contract for fine-scale thermal differences inside settlements.

A regional forecast can say that a city is hot while individual streets, plazas, rooftops, parks, waterfronts and interiors differ strongly because of shade, vegetation, building geometry, surface materials, water, wind exposure and stored heat.

This pass researches that gap without creating automatic PTU heat damage or Weather.

## Source 1 — Pokémon Legends: Z-A official Lumiose material

Source:
https://legends.pokemon.com/en-au/story-world/lumiose-city

Supporting source:
https://legends.pokemon.com/en-us/news/adventure

The official Lumiose material describes a major urban redevelopment where shopping streets, cafés and restaurants coexist with waterfronts, verdant parks and newly constructed Wild Zones intended to help people and Pokémon share the city.

Reusable high-level structures:

- urban redevelopment can alter habitat and public-space distribution without replacing the entire city;
- greenery can be treated as infrastructure and habitat rather than decoration;
- a city can contain multiple strongly different local environments within one regional weather system;
- the same redevelopment project can affect people, transport, Pokémon habitat, commerce and public life at once.

Ouros transformation:

Do not copy Quasartico, Lumiose districts, Wild Zone layouts or Z-A plot elements. Use the broader principle that changing urban form can alter local environmental conditions and Pokémon use of space.

## Source 2 — EPA: What Are Heat Islands?

Source:
https://www.epa.gov/heatislands/what-are-heat-islands

EPA identifies several drivers of urban heat islands:

- reduced vegetation and water;
- heat-absorbing built materials;
- building/street geometry that restricts heat release and wind;
- waste heat from vehicles, buildings and industry;
- weather and geography.

It also distinguishes surface heat islands from atmospheric heat islands and notes that temperatures can vary substantially inside the same city.

Reusable design lesson:

Do not store a single `city_temperature_modifier`.

Ouros should be able to represent:

regional weather
-> district thermal pattern
-> site observation
-> actor exposure / operational consequence

without collapsing those states into one number.

## Source 3 — EPA: Benefits of Trees and Vegetation

Source:
https://www.epa.gov/heatislands/benefits-trees-and-vegetation

EPA describes shade and evapotranspiration as separate cooling processes and also notes links to stormwater, air quality, building energy demand and habitat.

Reusable structure:

A tree canopy project can produce multiple connected consequences:

- more shade;
- changed thermal observations;
- changed runoff;
- habitat value;
- changed maintenance demand;
- altered public-space use;
- lower building cooling demand where world technology supports it.

Ouros should store those consequences separately rather than apply a generic `greenery bonus`.

## Source 4 — EPA: Heat Islands FAQ / measurement and reduction

Source:
https://www.epa.gov/heatislands/frequent-heat-island-questions-and-resources

Source:
https://www.epa.gov/heatislands/guide-reducing-heat-islands

The material distinguishes heat waves from heat islands. A heat wave is a weather event; an urban heat island is a persistent or recurring local thermal pattern created by land cover, materials and urban form.

This distinction is critical for the existing Ouros Meteorology layer.

Ouros rule:

`HEAT_EVENT` from Meteorology and `URBAN_THERMAL_PATTERN` from this layer must remain different objects.

They can interact, but neither silently creates the other.

## Source 5 — NOAA community heat mapping

Source:
https://www.nesdis.noaa.gov/events/nedtalk-extreme-heat-mapping-heat-islands-cities

Source:
https://www.noaa.gov/news-release/federal-agencies-communities-to-map-heat-inequities-in-14-us-cities

NOAA-supported campaigns use mobile observations of temperature, humidity, time and position to reveal fine-scale differences inside cities. These measurements can inform later decisions about shade, trees and heat planning.

Reusable structures:

- repeated transects rather than one permanent sensor;
- morning, afternoon and evening observations as separate evidence;
- community-contributed measurements with provenance;
- maps created from observations rather than assumed from land-cover tags;
- later mitigation projects evaluated against prior baselines.

This maps cleanly to the existing Science, Cartography and Public Works layers.

## Source 6 — NOAA Richmond heat mapping case

Source:
https://www.climate.gov/news-features/climate-case-studies/where-do-we-need-shade-mapping-urban-heat-islands-richmond

The Richmond project documented large within-city differences and linked hotter areas to more impervious surfaces and less tree canopy.

Reusable narrative structure:

A citywide forecast may be broadly correct while a neighborhood-scale problem remains hidden until players or institutions perform a local survey.

Quest forms:

- map heat at different times;
- compare street canyons, parks and waterfronts;
- investigate why one block remains warm after sunset;
- test whether a mitigation project changed measured conditions;
- locate a failed or biased monitoring route;
- compare resident reports with instrument data.

## Source 7 — Pokémon Tabletop: Mysterious Ruins

Source:
https://pokemontabletop.com/campaign-seeds-mysterious-ruins/

The campaign seed emphasizes everyday investment in a town, community-scale change and the possibility that growth transforms a small settlement over time.

Reusable Ouros lesson:

Environmental change matters more when players already know and use the affected spaces.

A shaded plaza, market lane, workshop block or neighborhood park can accumulate years of history before a thermal problem becomes important.

Do not turn every heat-related observation into an emergency quest.

## Source 8 — Pokémon Tabletop: The Road to Tomorrow

Source:
https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

This campaign seed treats players as builders whose infrastructure and institutional choices can shape future society.

Reusable Ouros lesson:

A cooling project should have persistent consequences and trade-offs rather than functioning as a one-time quest reward.

Possible long-term project families:

- tree-canopy restoration;
- shaded market retrofits;
- reflective or redesigned roofs where technologically appropriate;
- water/shade integration;
- transit-stop redesign;
- schoolyard/clinic courtyard adaptation;
- conversion of obsolete paved space into mixed habitat/public space.

No real-world policy system should be copied wholesale into Ouros.

## Source 9 — PTU first-session environmental design

Source:
https://pokemontabletop.com/gm-advice-your-first-ptu-session/

PTU GM guidance encourages environmental objects and terrain opportunities that players can notice and use during encounters.

Important boundary:

That guidance supports authored environmental affordances. It does not justify automatically converting a hot street, shaded alley or fountain into PTU terrain effects.

Any tactical consequence still requires an exact PTU/AutoPTU contract.

## Source 10 — Eevee Expo urban mapping / environmental design example

Source:
https://eeveeexpo.com/ironmapper/season-6/trial-1/

The public mapping exercise includes a future Verdanturf concept where wind, cleaner air, energy infrastructure and Pokémon-friendly park space are designed together.

Only the high-level integration pattern is reusable:

urban climate + infrastructure + public space + Pokémon ecology can be designed as one connected system.

Do not copy the map, tiles, city implementation or creator-specific lore.

## Reusable design conclusions

### 1. Fine-scale observations matter

A district average should not overwrite measurements from a shaded courtyard, roof, station platform or waterfront.

### 2. Day and night can tell different stories

Stored heat may make a paved district remain warm after sunset even when another place was hotter during the afternoon.

This can connect to Night Ecology, Public Space and Energy demand.

### 3. Surface temperature and air temperature are different

A hot roof surface does not prove every nearby actor is under the same thermal exposure.

### 4. Shade is spatial

A tree or awning can alter a path or waiting area without changing an entire district.

### 5. Cooling interventions have side effects

Vegetation may also affect:

- water demand;
- maintenance;
- pollen/flowering;
- habitat;
- visibility;
- public-space programming;
- historic structures;
- access routes.

### 6. Heat should create decisions before it creates damage

Examples:

- shift a market schedule;
- open a shaded waiting room;
- reroute a walking tour;
- delay maintenance;
- move a festival setup;
- prioritize a tree-canopy project;
- investigate equipment failure caused by operating conditions;
- compare two retrofit proposals.

None requires invented PTU HP loss.

## Copyright and provenance guardrails

- Do not reproduce protected game dialogue, maps or plots.
- Do not copy real-city policies as fictional law without separate worldbuilding review.
- Preserve source links in research notes.
- External environmental sources inform systems design, not Ouros canon.
- Pokémon examples provide structural inspiration only.

## PTU / AutoPTU boundary

This research does not establish:

- heat damage;
- dehydration;
- fatigue;
- Burned;
- Sunny Day;
- harsh sunlight;
- Fire-type resistance to ambient heat;
- Ice-type weakness to ambient heat;
- Accuracy penalties;
- Slowed;
- terrain costs;
- air-conditioning bonuses;
- shade bonuses;
- water-cooling bonuses;
- thermal vision;
- automatic Pokémon spawn changes.

Those require PTU/Caelo authority and engine evidence.

## Candidate next searches

- Pokémon species with authored urban heat or cooling behavior;
- public PTU city campaigns with neighborhood-scale environmental state;
- shade structures and courtyards in hot-climate settlement design;
- nighttime urban ecology under thermal gradients;
- cooling-center and service-capacity design patterns;
- green-roof habitat interactions;
- urban water features and heat/stormwater trade-offs.
