# Ouros Research Scan — Pass 76: Aerial Airspace, Flight Corridors & Sky Ecology

Status: RESEARCH ONLY. Not canon. External sources are inspiration/evidence sources, not PTU rules authorities.
Date: 2026-08-21

## Why this pass exists

The repository already models travel, transport services, meteorology, light, astronomy, forest canopy, wild collectives, seasonal migration and communication infrastructure. `design/travel-transport-expedition-layer.md` even reserves `AIR_ROUTE` as a possible connection type.

What it does not yet model is the sky as persistent world state.

There is no dedicated contract for:

- air corridors and approach/departure zones;
- passenger flight services;
- aerial survey routes;
- migratory flyways and stopover sites;
- altitude bands and route knowledge;
- interactions between wild Flying Pokémon and transport infrastructure;
- temporary closures caused by weather or ecological activity;
- aerial observation coverage;
- airborne communication and beacon conflicts;
- safe distinction between PTU tactical Sky movement and overworld aviation.

This pass fills that gap without turning `Sky speed` into a universal passenger-flight rule.

## Source findings

### 1. Official Pokémon — Corviknight and Galar Flying Taxi

Source:
https://swordshield.pokemon.com/en-us/pokemon-galar-region/corviknight/

The official Sword/Shield site states that Corviknight's flying ability and intelligence are used by Galar Taxi to transport people between towns.

Reusable structure:

A Pokémon-assisted aerial route can be an institutional service with operators, schedules, destinations and recurring Pokémon assets. That service can exist independently from whether a player personally owns a Pokémon capable of flight.

Ouros transformation:

- public aerial transport can be a `transport_service` specialization;
- individual service Pokémon retain persistent identity;
- route availability can depend on staffing, weather, destination access and ecological constraints;
- the presence of a Flying-type Pokémon never proves passenger capacity;
- a passenger service does not imply unrestricted access to every location under its path.

Do not copy Galar Taxi, its corporate identity, branding or specific setting into Ouros.

### 2. Official Pokémon — Hisuian Braviary as aerial survey mobility

Sources:
https://legends.arceus.pokemon.com/en-gb/gameplay/
https://legends.arceus.pokemon.com/en-au/pokemon/braviary/

Legends: Arceus uses Hisuian Braviary for long-distance aerial traversal. The official gameplay page also emphasizes that the elevated viewpoint helps survey Pokémon and items below. The species page describes a seasonal arrival from farther north during winter.

Reusable structures:

- aerial mobility can change what information a field team can gather;
- a flight route can be a survey method rather than only transport;
- seasonal aerial presence can intersect with migration research;
- solitary and group movement patterns should remain species-specific.

Ouros transformation:

An aerial survey records an observation footprint, not omniscient map knowledge. Cloud, terrain, canopy, darkness, distance and observer attention can reduce what was actually seen. A player who crosses a valley from above may learn different facts than a party travelling through the valley floor.

### 3. Official PTU blog — aviation conflict caused by Pokémon communication

Source:
https://pokemontabletop.com/pokemon-spotlight-mareep-family/

The PTU blog's Mareep-family spotlight proposes a hook in which pilots report dangerous light interference over busy airspace. The cause is a population of Mareep/Flaaffy/Ampharos attempting to communicate with aircraft lights.

Reusable structures:

- an infrastructure/ecology conflict can result from benign Pokémon behavior;
- the first framing of an incident may be wrong about intent;
- airlines, pilots, researchers and local residents can all hold legitimate interests;
- resolution can involve communication, route changes, shielding, timing or habitat management rather than combat.

This is a particularly strong precedent for Ouros because it intersects existing Light, Communications, Travel, Ecology and Institutional layers.

No named place, NPC, exact sequence or prose from the source should be transplanted.

### 4. Official PTU blog — vertical battlefield design is a special mechanical case

Source:
https://pokemontabletop.com/gym-design-signature-elements/

The PTU Gym-design article contains an intentionally vertical arena using airborne Pokémon and floating platforms. It also defines special safety handling for falling within that authored challenge.

Reusable lesson:

Vertical tactical spaces need explicit rules. A worldbuilding document cannot assume that a 3D overworld flight path maps directly into the current tactical engine.

Ouros rule:

Aerial world state and aerial battle state remain separate until AutoPTU-Java has verified contracts for altitude/elevation, forced movement, falling, landing, vertical reach and relevant reactions.

### 5. Real-world flyways — routes are broad ecological corridors, not rails in the sky

Source:
https://www.fws.gov/sites/default/files/documents/2024-04/1558.pdf

U.S. Fish & Wildlife material describes migratory flyways as broad routes rather than narrow fixed highways. Timing and altitude can vary with season, temperature, weather and terrain. Stopover habitats matter because animals do not necessarily travel an entire route in one uninterrupted movement.

Reusable structure:

Ouros aerial migration should be represented as corridor probability + timing + stopover dependence rather than fixed invisible rails.

Potential state:

- broad flyway geometry;
- seasonal passage windows;
- observed altitude bands;
- important roost/feeding/rest sites;
- weather sensitivity;
- confidence and observation history.

This connects directly to Seasonality, Meteorology, Freshwater, Forest Canopy, Conservation and Wild Collective state.

### 6. Aviation/wildlife safety — conflict concentrates around low altitude and key habitat

Sources:
https://www.faa.gov/Air_traffic/publications/media/AIM-Chg-2-dtd-3-21-24.pdf
https://www.faa.gov/airports/airport_safety/wildlife/wildlife-strike-report-1990-2024

FAA material shows that wildlife conflict with aircraft is strongly affected by altitude, migration period and nearby habitat. It also emphasizes reporting wildlife activity rather than treating each incident as an isolated event.

Reusable structures:

- approach/departure areas deserve their own state;
- incident reporting can create a dataset that changes future route policy;
- route design can respond to migration without declaring wildlife hostile;
- an airport-like facility may interact with wetlands, waste sites, water bodies or roosts outside its physical boundary.

Ouros must not copy real aviation regulations. These sources are used only to understand dependency structure and monitoring logic.

### 7. Fangame/community discovery — sky regions work best when they are places, not empty transit

Source:
https://eeveeexpo.com/threads/201/

An Eevee Expo region-design discussion includes a planned sky-island region as a distinct geographic part of the world. The useful design lesson is that a sky destination can have ecology, routes, identity and exploration structure instead of functioning only as a fast-travel menu.

Ouros transformation:

If Ouros eventually includes floating or elevated settlements, they should use Location/Settlement/Architecture/Travel contracts like any other place. They must not automatically bypass geographic progression simply because they are above ground.

The specific region, names and aesthetic ideas from the thread are not imported.

### 8. Community PTU discussions show why raw movement capability needs a boundary

Source:
https://www.reddit.com/r/PokemonTabletop/comments/qqeuqs

A public PTU discussion about Mantine illustrates ambiguity that can arise when a mechanical Sky capability conflicts with intuitive overworld expectations.

Reusable lesson:

The narrative server needs an explicit overworld traversal contract rather than extrapolating every PTU battle capability into travel simulation.

This reinforces an existing Ouros rule:

`Sky movement in battle` does not automatically mean `safe passenger flight`, `long-range flight`, `hover indefinitely`, `carry cargo`, `fly through storms`, or `use public air routes`.

Reddit is treated as community discussion, not rules authority.

## PTU/Caelo cross-check

### Available Caelo evidence

Previously recovered Caelo Player's Guide material establishes a battle-specific sky limit: participants may fly above the limit, but cannot spend a Standard Action while above it; the same rule applies to Levitate movement. This is an encounter-balancing rule, not an overworld aviation model.

Caelo also distinguishes Wild Encounters by time of day and uses location-specific access requirements. Those concepts support aerial schedules and seasonal access, but do not supply passenger/cargo or long-distance flight rules.

### Available AutoPTU Python evidence

The available Python battle-state implementation has explicit `sky` and `levitate` movement checks and a `can_fly()` boundary. It also contains concrete Trainer Feature behavior such as Celerity requiring a Flying-type or Sky/Levitate-capable target.

This is narrow tactical evidence.

It does not prove:

- passenger eligibility;
- carrying capacity;
- air-route range;
- fatigue/endurance;
- weather-safe travel;
- altitude simulation;
- vertical tactical layers;
- flight corridors;
- migration behavior;
- aerial traffic control;
- collision or bird-strike style mechanics.

### Rules authority warning

Any future exact use of Mountable, Sky, Levitate, Teleporter, Falling, Jump, Flying Ace Features, Rider Features, wind/weather or aerial combat must be checked against the project's PTU/Caelo source set and current AutoPTU implementation.

## New system boundary suggested by this research

Ouros should distinguish:

1. `AIRSPACE_REGION` — persistent spatial sky region.
2. `AIR_CORRIDOR` — a known or managed route through it.
3. `AERIAL_SERVICE_ROUTE` — an institution/operator currently serving a corridor.
4. `AERIAL_MIGRATION_CORRIDOR` — ecological movement probability over time.
5. `AERIAL_OBSERVATION` — what an observer actually saw from air or ground.
6. `AERIAL_INCIDENT` — route conflict, near miss, unexpected gathering, navigation issue or closure.
7. `AERIAL_ACCESS_ASSESSMENT` — whether a particular actor/service may use a route now.
8. `BATTLE_AERIAL_SNAPSHOT` — the separate validated tactical representation, if any.

These objects should link to Travel, Meteorology, Light, Communications, Seasonality, Conservation, Wild Collectives, Canopy, Astronomy, Cartography and Crisis.

## Design lessons for Ouros

Aerial space should not be empty fast travel. It can accumulate memory through routes, services, survey history, migration events, landmarks, closures and incidents.

A flight can be important because of what the party learns, not because a random battle interrupts it.

Wildlife/transport conflicts should preserve uncertain intent. A flock near a service lane can be migrating, feeding, roosting, displaced, curious, territorial or coincidental.

Changing a route may move the problem elsewhere. Rerouting around a roost could cross a night migration path, increase service time or reduce access to another settlement.

Air corridors should have editions/history like roads and maps. A route that was safe ten years ago may be obsolete after settlement growth, habitat change or a new service hub.

Altitude should remain coarse world state until a real 3D battle contract exists.

## Copyright/provenance boundary

This pass keeps only high-level systems, public factual descriptions and design observations.

It does not reproduce protected dialogue, scene prose, characters, quest scripts, fangame plots or distinctive narratives.

## Research gaps

- Exact PTU/Caelo Mountable and passenger rules.
- Exact PTU/Caelo Sky/Levitate/falling rules beyond currently recovered snippets.
- Whether AutoPTU-Java will eventually represent elevation as discrete bands or continue to project aerial encounters onto a single tactical layer.
- Cobblemon support for persistent flying entities, altitude-aware spawning and server-owned flight paths.
- Whether Ouros will have mechanical vehicles, Pokémon-drawn/assisted flight, airships, or only Pokémon-based services.
- Which regions should have major migration flyways before player intervention.
- Whether any elevated/floating settlements are part of authored canon.

## Sources inspected this pass

- Official Pokémon Sword/Shield Corviknight page — https://swordshield.pokemon.com/en-us/pokemon-galar-region/corviknight/
- Official Pokémon Legends: Arceus gameplay — https://legends.arceus.pokemon.com/en-gb/gameplay/
- Official Pokémon Hisuian Braviary page — https://legends.arceus.pokemon.com/en-au/pokemon/braviary/
- PTU Pokémon Spotlight: Mareep Family — https://pokemontabletop.com/pokemon-spotlight-mareep-family/
- PTU Gym Design: Signature Elements — https://pokemontabletop.com/gym-design-signature-elements/
- U.S. Fish & Wildlife flyway education resource — https://www.fws.gov/sites/default/files/documents/2024-04/1558.pdf
- FAA Aeronautical Information Manual bird-hazard section — https://www.faa.gov/Air_traffic/publications/media/AIM-Chg-2-dtd-3-21-24.pdf
- FAA Wildlife Strikes report, 1990–2024 — https://www.faa.gov/airports/airport_safety/wildlife/wildlife-strike-report-1990-2024
- Eevee Expo region-design discussion — https://eeveeexpo.com/threads/201/
- Public PTU community Sky-capability discussion — https://www.reddit.com/r/PokemonTabletop/comments/qqeuqs
