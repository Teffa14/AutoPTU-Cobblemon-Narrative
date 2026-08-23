# Wildlife Migration, Stopovers & Corridor Research — Pass 124

Status: research/provenance only. Not Ouros canon. External stories are inspiration sources, not rules sources.

## Why this pass exists

The repository already has several pieces of migration state, but no single layer owns migration as a longitudinal ecological process.

Existing boundaries inspected before writing:

- `seasonality-calendar-phenology-layer.md` owns calendar phase, expected windows, phenology and arrival/departure observations;
- `wild-collective-agency-layer.md` can persist a herd/flock/school and references `seasonal_route_ids`;
- `aerial-airspace-flight-corridors-layer.md` can represent aerial migration corridors;
- `island-biogeography-endemism-dispersal-layer.md` owns colonization, dispersal and stepping-stone function;
- `road-ecology-crossings-linear-infrastructure-layer.md` owns linear-infrastructure barrier/crossing effects;
- `travel-transport-expedition-layer.md` owns human routes/services;
- `field-signs-tracking-spoor-layer.md` owns physical evidence of movement.

Missing responsibility: persistent migration episodes, stopovers, route revisions, migration-wave observations, migration barriers, partial migration, failed/aborted movements, interannual route fidelity and the distinction between a known species-level migration and what a particular population actually did this year.

## Source 1 — Pokémon official animation: Beautifly migration

Source: Pokémon.com, “Goodbye, Friend!”
https://www.pokemon.com/us/animation/seasons/23/episode-22-goodbye-friend

The episode explicitly frames Beautifly migration as a research target with a narrow observation window. A north wind matters to timing, but the episode does not imply that wind mechanically controls every Beautifly.

Reusable structure:

- a migration can create a short scientific window;
- weather can be a trigger candidate or operating condition without being proven universal causation;
- missing the window can mean waiting until the next migration rather than spawning substitute content;
- researchers, tourism, transport and conservation can all react to the same movement event.

Ouros adaptation:

A migration episode should have expected and observed windows. A forecast may influence preparation. Actual departure remains world state established by observation or authored progression.

## Source 2 — Pokémon official animation: annual Chinchou migration

Source: Pokémon.com, “Takin’ it on the Chinchou”
https://www.pokemon.com/us/animation/seasons/5/episode-3-takin-it-on-the-chinchou

This is one of the strongest migration precedents in Pokémon. The migration is annual, follows an inherited route to an old nesting ground, intersects a human settlement and has an established local protective practice.

Reusable structure:

- migration route can outlive major geological change;
- a destination may remain important even after the landscape around it changes;
- local institutions or families can develop recurring stewardship around a migration;
- a predictable migration can create vulnerability to poaching or disruption;
- the same event can be ecology, public tradition, logistics and conservation at once.

Ouros adaptation:

Migration routes should have their own history and route revisions. A road, quarry, bridge or new settlement can intersect a route without erasing the route’s older history.

## Source 3 — Pokémon official animation: Butterfree reproductive migration

Source: Pokémon.com, “Bye Bye Butterfree”
https://www.pokemon.com/us/animation/seasons/1/episode-20-bye-bye-butterfree

The episode presents a seasonal group movement tied to mating and sea crossing. Ash’s Butterfree leaves a Trainer relationship to join the migrating group.

Reusable structure:

- migration may intersect Pokémon agency and release/partnership history;
- a Trainer-linked Pokémon can choose to join a broader ecological cycle;
- a migrating aggregation is not automatically a permanent collective with fixed membership;
- reproductive or life-stage context can motivate movement without granting a combat buff.

Ouros adaptation:

A persistent Pokémon may enter or leave a migration episode while retaining the same `pokemon_entity_id`. Joining a migration does not imply permanent membership or loss of prior history.

## Source 4 — Pokémon official animation: flock continuity and temporary separation

Source: Pokémon.com, “True Blue Swablu”
https://www.pokemon.com/us/animation/seasons/7/episode-24-true-blue-swablu

The story uses a temporarily separated Swablu and a flock that later reappears. The individual can rejoin the group rather than being treated as permanently abandoned or available for capture simply because it was temporarily alone.

Reusable structure:

- temporary separation from a migrating or traveling group is not proof of abandonment;
- search/reunion can be a noncombat objective;
- the visible flock at one moment is not necessarily the entire population;
- a returning group can resolve an apparent custody dilemma.

Ouros adaptation:

Migration observations should preserve `temporarily separated`, `unknown group location` and `rejoined` as distinct outcomes.

## Source 5 — USGS 2026 migration corridor and stopover mapping

Source: U.S. Geological Survey, “Ungulate Migrations of the Western United States, Volume 6” (2026)
https://pubs.usgs.gov/sir/2026/5123/sir20265123.pdf

The report distinguishes individual migration paths, population-level corridors, intensity of route use and stopovers. Stopovers are identified from time spent and use concentration rather than simply drawing a line between endpoints.

Reusable structure:

- a corridor is an aggregate footprint, not one mandatory path;
- high-use and low-use portions can coexist;
- stopovers deserve separate identity from transit segments;
- migration evidence can improve as more years or individuals are observed;
- route maps need provenance and confidence.

Ouros adaptation:

Use coarse corridor segments and stopovers instead of per-block pathfinding as canonical ecological truth. Minecraft entities may visualize a movement wave but loaded entities cannot define the full corridor.

## Source 6 — USGS stopover ecology and migration timing

Source: U.S. Geological Survey Circular 1322, “Stopover Ecology and Habitat Utilization of Migrating Land Birds…”
https://pubs.usgs.gov/circ/1322/c1322.pdf

This research emphasizes multiple spatial scales of migration and shows arrival/abundance varying with weather and plant phenology. Stopover use can depend on fine habitat structure and food availability.

Reusable structure:

- migration timing can be correlated with resource pulses and weather;
- stopover quality is a separate state from corridor existence;
- a route can remain geographically open while becoming ecologically poor;
- phenology and migration should communicate without becoming the same subsystem.

Ouros adaptation:

Seasonality owns the expected timing; Flora/Food/Interspecies/Freshwater can provide resource-state inputs; Migration owns observed movement and stopover use.

## Source 7 — USGS migration under changing climate and constrained routes

Source: U.S. Geological Survey Circular 1493, “Ungulate Migration in a Changing Climate—An Initial Assessment…”
https://pubs.usgs.gov/circ/1493/cir1493.pdf

The work discusses migration corridors, stopovers, changing phenology and route constraints. Migrants may move faster, use stopovers less or detour when development or disturbance constrains established routes.

Reusable structure:

- route disruption does not have one universal outcome;
- migrants may delay, detour, compress travel or reduce stopover use;
- a successful crossing does not prove the corridor is healthy;
- multi-year monitoring is needed before declaring permanent route change.

Ouros adaptation:

Migration response should use observed route revisions and confidence rather than deterministic “barrier present -> route abandoned.”

## Source 8 — USGS “green wave” / phenology coupling

Source: USGS WLCI FY16 report
https://pubs.usgs.gov/of/2018/1048/ofr20181048.pdf

The report describes migratory animals tracking vegetation phenology and notes that drought and development can alter stopover use and movement behavior.

Reusable structure:

- the same corridor can function differently in wet and dry years;
- migration can follow moving resource quality rather than fixed calendar dates;
- a route may remain historically recognized even while timing shifts;
- resource mismatch can become a research question instead of an automatic crisis.

## PTU/community research note

Broad searches across public PTU campaign listings and logs found many campaign-level travel/ecology examples but no trustworthy PTU rules source that defines a generic migration mechanic. Public PTU material is therefore useful only for campaign structure, not migration rules.

The official PTU blog remains a campaign-design source, but no migration-specific mechanic from that material is imported here.

## Design synthesis for Ouros

The reusable migration grammar is:

`expected seasonal window -> preparatory observations -> departure/arrival evidence -> movement wave -> corridor/stopover use -> interruptions/detours -> arrival/dispersal -> post-season review -> next-year baseline`

Important separations:

- migration pattern vs this year’s migration episode;
- species-level lore vs population-level observation;
- population vs persistent collective vs visible subgroup vs tactical participants;
- corridor vs exact route;
- transit segment vs stopover;
- expected timing vs actual departure/arrival;
- route use vs route health;
- observation failure vs true absence;
- temporary separation vs abandonment;
- migration participation vs ownership/custody;
- migration world state vs PTU tactical movement.

## Hard non-inferences

Do not infer:

- Flying type -> migratory species;
- flock/herd/school -> migrating;
- seasonal encounter table change -> confirmed migration;
- one observed path -> permanent corridor;
- missing migration -> extinction;
- late migration -> climate cause;
- road crossing use once -> corridor restored;
- Pokémon alone during migration season -> abandoned;
- migrating Pokémon -> available for capture;
- migration corridor -> Naturewalk, Sky, Swim or other PTU movement benefit;
- migrating group -> Pack Mon or tactical formation;
- migration wave -> swarm mechanics;
- wind/rain -> automatic forced movement;
- Minecraft entity stream -> authoritative population size;
- battle victory -> migration route reopened.

## PTU/Caelo validation state

The accessible runtime did not expose Super PTU Online Helper. The complete primary Caelo source corpus was not reliably available through the tools used in this run. No migration-specific PTU/Caelo mechanic, Skill DC, tracking bonus, travel speed, swarm rule or movement modifier is claimed.

Mechanically rich migration encounters must therefore use only verified battle families, or a reduced static version, until exact PTU/Caelo rules and Java contracts exist.