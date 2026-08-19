# Seasonality, Calendar & Phenology Research — Pass 24

Status: research/provenance only. Not Ouros canon.

Date: 2026-08-19

## Research question

How can Ouros use recurring time, seasons, daylight, ecological cycles and annual events to make the Minecraft/Cobblemon world feel persistent without turning the game into a real-time FOMO scheduler or silently inventing PTU weather mechanics?

This pass deliberately avoids repeating the existing regional-clock, public-event, agriculture, wild-collective, travel, crisis and research layers. The missing system is the shared calendar/season substrate those layers can read from.

## Existing Ouros overlap inspected

The repository already contains:

- `design/observation-settlement-time-layer.md`: regional clocks, action windows and bounded time pressure;
- `design/public-memory-event-legacy-layer.md`: recurring public-event editions and schedules;
- `design/food-agriculture-hospitality-layer.md`: cultivation cycles, seasonal food context and venue availability;
- `design/wild-collective-agency-layer.md`: seasonal routes, migration groups, resource dependencies and ecological lifecycle;
- `design/travel-transport-expedition-layer.md`: route/service state and journey compression;
- `design/crisis-rescue-recovery-layer.md`: weather warnings, hazards and recovery;
- `design/science-research-discovery-layer.md`: observation, datasets and hypotheses;
- `design/encounter-implementation-contracts.md`: permanent battle capability families and reduced/full encounter policy.

Pass 24 therefore focuses on a canonical world calendar, region-specific seasonal profiles, daylight bands, phenological observations, recurrence, seasonal expectation versus anomaly, and offline/multiplayer time policy.

## Source 1 — Pokémon Black/White seasonal world changes

Source: The Pokémon Company International, "Remember the Region: Unova Spotlight".

URL: https://www.pokemon.com/us/features/remember-the-region-unova-spotlight

The current official retrospective describes Unova seasons as more than visual decoration. It notes landscape color changes, weather changes, seasonal encounter availability, some season-exclusive Pokémon appearances, season-dependent access to areas, Deerling/Sawsbuck seasonal forms, a Season Research Lab, and Trainers who appear only during specific seasons.

Reusable structural lessons:

- season can alter a location's presentation, access and encounter ecology through one shared world-state variable;
- seasonal change can create research content without needing a crisis;
- NPC schedules can be seasonal rather than permanently static;
- a season should influence multiple systems coherently instead of only changing textures;
- not every seasonal difference should be tactical combat state.

Copyright boundary: use only the high-level idea that seasonal state coordinates multiple systems. Do not copy Unova map layouts, named seasonal NPCs, dialogue or quest text.

## Source 2 — Seasonal traversal in Unova routes

Sources:

- Bulbapedia, Season game mechanic: https://bulbapedia.bulbagarden.net/wiki/Season_(game_mechanic)
- Bulbapedia, Unova Route 8: https://bulbapedia.bulbagarden.net/wiki/Unova_Route_8
- Bulbapedia, Unova Route 20: https://bulbapedia.bulbagarden.net/wiki/Unova_Route_20

These references document route geometry and access changing with seasonal conditions: accumulated snow, frozen puddles and autumn leaves can make some spaces traversable or expose paths/items that are inaccessible at other times.

Reusable structural lesson:

A route can have `seasonal_variant_state` that changes overworld traversal while preserving the same location identity. This is preferable to creating four duplicate route objects.

Important Ouros limit:

A Minecraft route becoming visually frozen does not automatically make its AutoPTU grid Ice Terrain or create a PTU movement penalty. Tactical terrain must be validated separately.

## Source 3 — PTU community winter-event guidance

Source: Pokémon Tabletop RPG official community-event material, winter festivals and celebrations.

URLs:

- https://pokemontabletop.com/
- https://pokemontabletop.com/category/community-events/

The PTU community event explicitly encouraged winter celebrations grounded in Pokémon-world phenomena, such as a small-town festival tied to local seasonal Pokémon activity, and advised that a seasonal location can contain multiple hooks rather than a single linear adventure.

Reusable structural lessons:

- annual traditions can arise from local ecology instead of importing a real-world holiday unchanged;
- one seasonal event can support social scenes, competitions, exploration, research and optional adventure hooks simultaneously;
- event material should be reusable and adaptable when players take unexpected paths;
- real-world cultural inspiration deserves research and sensitivity instead of superficial reskinning.

Copyright boundary: do not copy submitted community adventures or named festival material. Only the design guidance is reused.

## Source 4 — Pokémon Shifting Skies seasonal exploration

Source: Eevee Expo project page for Pokémon Shifting Skies.

URL: https://eeveeexpo.com/shifting-skies/

The public project description uses four seasonal versions of its world and gives maps different interaction opportunities depending on season. Its release notes also describe season-dependent traversal, berry growth, hibernation-cave interactions and scouting.

Reusable structural lessons:

- seasonal state can unlock different interaction verbs in the same map;
- a seasonal transition itself can advance long-running world objects such as plants;
- seasonal opportunities can encourage return visits to known locations;
- scouting before interaction is useful when ecology changes over time.

Do not import:

- the project's +10% seasonal stat bonuses;
- its exact battle progression;
- its berry timing or trap rules;
- its characters, plot, inventions or map-specific solutions.

Those are project-specific mechanics and are not PTU/Caelo authority.

## Source 5 — Pokémon Essentials community weather/season architecture

Source: Eevee Expo Weather System resource.

URL: https://eeveeexpo.com/resources/1411/

The resource supports zone-specific weather probabilities per season, real-time or fictional-time modes, seasonal map appearance, and season-aware battle backgrounds. This is useful as implementation research because it separates:

- global/fictional time source;
- geographic weather zones;
- seasonal probability configuration;
- visual map changes;
- battle presentation.

Reusable design lesson:

Ouros should similarly separate calendar, regional climate expectation, actual current weather, visual presentation and tactical battlefield weather. One field called `season_weather` would be too ambiguous.

Do not copy its code or probability tables.

## Source 6 — Pokémon GO Seasons as a content-cadence example

Source: The Pokémon Company International, "Explore Precious Paths in the New Season of Pokémon GO".

URL: https://www.pokemon.com/us/pokemon-news/explore-precious-paths-in-the-new-season-of-pokemon-go

Pokémon GO uses multi-month Seasons to coordinate changing encounters, bonuses and events.

Reusable lesson:

A season can act as a broad content frame containing smaller events rather than requiring every seasonal change to be a unique quest.

Ouros caution:

Live-service scarcity should not be copied blindly. A persistent RPG should avoid making important character, canon or one-time story content inaccessible because the real-world player missed a date. Seasonal recurrence, archived consequences, delayed alternatives and local world-time control are preferable.

## Source 7 — Recent game-studies work on seasonality

Source: Laura op de Beke, "Global weirding and dark seasonality in video games", published online 2025 and in volume 35 issue 1 in 2026.

URLs:

- https://journals.sagepub.com/doi/10.1177/0961463X251351718
- https://research-portal.uu.nl/en/publications/global-weirding-and-dark-seasonality-in-video-games/

The paper treats seasonality as both system and audiovisual world design. It also discusses "season creep": expected biological and climatic timings shifting gradually, and games where dangerous or unseasonal weather becomes part of a new seasonal norm.

Reusable structural lessons:

- players can learn seasons from phenological signs, not only a UI label;
- seasonal expectation and actual observed conditions should be distinct;
- an early bloom, delayed migration or unusual freeze can become meaningful because a normal baseline exists;
- visual/audio environmental change matters even when it has no tactical modifier;
- long-term environmental uncertainty can support investigation and adaptation rather than only disaster spectacle.

Ouros caution:

Do not procedurally turn every anomaly into climate-collapse drama. Unseasonal observations should require explicit state, evidence and causes or remain unresolved observations.

## Source 8 — Seasonal real-time world design as a contrast case

Source: Game Developer discussion of Animal Crossing's clock-synchronized world.

URL: https://www.gamedeveloper.com/design/-i-animal-crossing-i-s-strange-unresolved-conflict

The article describes seasonal visual change, time-of-day routines and changing species availability as contributors to a world that feels continuously alive.

Reusable lesson:

Temporal variation can make familiar locations worth revisiting without adding new geography.

Ouros caution:

Real-time synchronization is not automatically suitable for a multiplayer narrative world. A server-authoritative fictional calendar is safer unless real-time linkage is deliberately chosen.

## PTU/Caelo cross-check

The supplied Caelo Player's Guide distinguishes wild encounters by `Morning`, `Day` and `Night`. It also treats scenes and travel timeskips as explicit narrative-time changes. Those rules support keeping time bands as explicit state rather than inferring them from prose.

The PTU Core Rulebook and Pokédex include terrain, movement and special capabilities such as Naturewalk and Groundshaper. The Caelo location material also contains locations with explicit environmental mechanical effects. Therefore:

- a seasonal overworld variant cannot grant Naturewalk or any Capability;
- snow, frozen water, high wind or heat cannot impose tactical movement/status/damage rules without a governing PTU/Caelo mechanic and current AutoPTU support;
- species availability and behavior changes must come from authored ecology/encounter data or observations, not generic type stereotypes;
- `Morning/Day/Night` availability may be narrative/world-state input, but any combat consequence still belongs to the battle engine.

## New design conclusions for Ouros

### 1. Calendar is not weather

Store these separately:

`world_date`
→ `regional_season_profile`
→ `expected_climate_band`
→ `actual_weather_state`
→ `phenological_observations`
→ `overworld_variant`
→ optional validated `battlefield_weather_state`

### 2. Regions do not need identical four-season calendars

A desert, alpine island, tropical coast and industrial city may have different locally meaningful cycles. Candidate profile labels can be authored per region without forcing `spring/summer/autumn/winter` everywhere.

### 3. Phenology should be evidence-bearing

Flowering, migrations, spawning, roosting, emergence, hibernation, leaf fall or thaw should be represented as observed events with expected windows and confidence, not omniscient automatic truth.

### 4. Annual recurrence should remember previous editions

A recurring ecological or civic event should query prior editions and current world state. The second year of a migration or festival should not reset to year one.

### 5. Seasonal changes should favor dense-world reuse

Known routes, towns and dungeons can gain new access, populations, schedules, services and visual identity during a different season. This strengthens the existing dense-world rule.

### 6. Missed windows need graceful handling

If a player misses a seasonal event while offline:

- the world may advance and record the result;
- public records and NPC memory can preserve what happened;
- the event may recur later;
- critical personal arcs should offer another authored route when appropriate;
- the system should avoid punishing offline players with irreversible loss of core character content.

### 7. Anomaly requires a baseline

An "early migration" is meaningful only if the world has an expected migration window and evidence of previous timing. Otherwise it is simply the first observation.

## Research gaps

Future research should inspect:

- exact PTU/Caelo weather duration and battlefield rules before tactical seasonal encounters are promoted;
- time-of-day encounter handling in the current Python oracle;
- Cobblemon's authoritative time, weather and spawn hooks;
- server versus Minecraft-world calendar synchronization;
- persistence rules for daylight and offline passage of time;
- whether Ouros wants region-local calendars, one global calendar, or both;
- how much historical season data is needed before anomaly detection becomes useful.

## Copyright/provenance policy

This pass uses public descriptions and high-level systems only. No protected dialogue, map layouts, distinctive characters, scripts, puzzle solutions or full plot summaries were copied. Fangame mechanics are inspiration references, never PTU rules authority.