# Ouros Research — Maritime Coasts, Sea Lanes & Underwater Depths — Pass 34

Status: Research only. Not established Ouros canon.
Date: 2026-08-19

## Research purpose

This pass examines maritime play as a persistent world system rather than treating water only as a travel mode or battlefield terrain.

The repository already contains dedicated layers for travel/transport, conservation, geology, crisis response, infrastructure, cases/custody, settlements, workplaces and seasonal ecology. The remaining gap is the maritime state that connects them: coasts, harbors, sea lanes, underwater spaces, vessels, salvage, marine habitats, tidal access and the consequences of operating across a three-dimensional water environment.

No external prose, characters or plots are imported into Ouros. Sources are retained for provenance and only high-level structures are reused.

## Sources inspected

### Official Pokémon — Hoenn underwater exploration

Source: https://www.pokemon.com/us/pokemon-news/remember-the-region-hoenn-spotlight

The 2026 Hoenn retrospective emphasizes that a large part of the region is water, that surface routes are crossed through Surf, and that Hoenn added true underwater exploration through Dive to reach Seafloor Cavern.

Reusable design lesson:
- surface-water traversal and underwater traversal are separate access states;
- a water route can hide a second navigation layer beneath it;
- submerged locations can be meaningful destinations rather than decorative extensions of an ocean biome;
- reaching an underwater dungeon can depend on validated traversal capability without making every Water-type Pokémon equivalent.

Do not import Surf/Dive eligibility into Ouros until PTU/Caelo and adapter rules are validated.

### Official Pokémon — Mantine Surf / island connections

Sources:
- https://www.pokemon.com/uk/strategy/alola-impresses-with-new-activities
- https://www.pokemon.com/uk/pokemon-video-games/pokemon-ultra-sun-and-pokemon-ultra-moon

Mantine Surf serves as both inter-island transport and a recreational/competitive activity. The route contains obstacles and performance goals rather than functioning only as fast travel.

Reusable design lesson:
- the same marine corridor can support public travel, sport, tourism and wildlife interactions;
- transport infrastructure can become culture;
- a route may have operators, rules, records and local identity without becoming a new battle subsystem.

### Official Pokémon — Bubbly Basin, Pokémon Pokopia

Sources:
- https://www.pokemon.com/us/news/dive-deep-with-the-pokemon-pokopia-expansion-pass-dlc
- https://www.pokemon.com/us/news/dive-into-pokemon-pokopia-expansion-pass-part-1-bubbly-basin

In August 2026 Pokémon Pokopia added an underwater settlement that can be rebuilt and explored, including underwater construction and multiplayer visitation.

Reusable design lesson:
- underwater areas can contain persistent civic space, not only caves or encounter maps;
- building rules can differ meaningfully by environment;
- a submerged town can connect housing, infrastructure, ecology, social systems and exploration;
- multiplayer underwater spaces need their own access and visibility constraints.

Do not assume Minecraft construction underwater is mechanically safe or performant until the adapter layer is tested.

### PTU campaign retrospective — Wakino Privateers

Source: https://pokemontabletop.com/wakino-privateers-a-game-of-love-extreme-power-levels-and-actually-not-that-much-piracy/

Wakino Privateers ran for roughly three and a half years in an archipelago. Its setup connected piracy, island-level legal loopholes, state response and travel across culturally distinct islands.

Reusable design lesson:
- archipelagos naturally generate jurisdiction boundaries, logistics and information delays;
- maritime crime may exploit gaps between local authorities rather than requiring an omnipotent villain faction;
- islands can share a region while retaining distinct institutions, histories and priorities;
- a sea campaign works when ports and settlements matter as much as ship-to-ship conflict.

No Wakino names, organizations, jokes, characters or plot events should be copied.

### PTU campaign — Tales of Visiwa

Source: https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

Visiwa is another island-region campaign, with dangerous wilderness, certified exploration and cultural/historical layers.

Reusable design lesson:
- island geography can reinforce uneven accessibility and professional expedition roles;
- coastal regions should not become a collection of interchangeable beach biomes;
- maritime routes should connect to inland wilderness, shrines, settlements and regional history.

### Fangame — Pokémon Gaia

Source: https://www.eeveeexpo.com/gaia/

Pokémon Gaia publicly lists Dive and underwater maps alongside hidden grottos and secret temples.

Reusable design lesson:
- underwater traversal works best when it reveals otherwise inaccessible geography and secrets;
- depth can be an exploration axis comparable to cave elevation or mountain ascent;
- submerged areas should justify revisits through changed access, discoveries or world state rather than being a one-use corridor.

Do not import Gaia locations, relics, enemy groups, custom Pokémon, Moves or items.

### Fangame / short-form marine activity examples

Sources:
- https://www.eeveeexpo.com/expo-news/
- https://eeveeexpo.com/resources/268/

Eevee Expo coverage includes short games centered on surfing/fishing and a community resource for Pokémon exploration assignments.

Reusable design lesson:
- fishing, scouting and coastal excursions can support small sessions that do not require combat;
- expedition results should be stateful and attributable rather than anonymous random loot;
- a marine activity may be recreational, economic, scientific or social depending on context.

### Public PTU recruitment example — island survival

Source: https://rpol.net/display.cgi?date=1577355423&gi=4&ti=38430

A public PTU campaign pitch uses a strategic island, storm disruption, communications failure, engineering needs and hostile wildlife as the foundation for base-building survival.

Reusable design lesson:
- remoteness amplifies infrastructure and resupply decisions;
- losing communications, transport or safe water routes can change the entire campaign loop;
- island survival should expose dependencies rather than merely increase random encounter frequency.

The campaign's military framing and story are not imported.

## Structural findings for Ouros

### 1. Water needs layers

Recommended world distinction:

- COASTAL_EDGE
- SURFACE_WATER
- OPEN_SEA
- SUBMERGED_SHALLOWS
- DEEP_WATER
- SUBMERGED_STRUCTURE
- SEAFLOOR_ROUTE

These are narrative/environmental labels only until PTU/Caelo and Minecraft mechanics define exact traversal.

### 2. Sea lane is not the same object as water

A navigable lane needs its own state:

- endpoints;
- operator/service links;
- expected hazards;
- navigation knowledge;
- seasonal access;
- traffic level;
- emergency alternatives;
- marine ecology overlaps;
- jurisdiction/stewardship overlaps.

The ocean can be physically present while a service is suspended, a lane is avoided, or a harbor is closed.

### 3. Tides and currents should be world state before mechanics

Tide/current state can alter:

- which caves are physically exposed;
- which docks can be used;
- where floating debris travels;
- which Pokémon are observed;
- when a salvage site can be approached;
- whether an underwater entrance is visible.

It must not automatically create movement penalties or forced movement inside AutoPTU until exact rules and engine support exist.

### 4. Salvage needs provenance and custody

A recovered object can be:

- lost property;
- cargo;
- archaeological material;
- evidence;
- hazardous equipment;
- a scientific sample;
- an abandoned object;
- a disputed claim.

Recovery is an event. Ownership is a separate claim. Custody is a separate record.

### 5. Shipwrecks are multi-layer sites

One wreck can simultaneously be:

- a navigation hazard;
- ecological habitat;
- historical site;
- salvage site;
- investigation scene;
- dungeon-like location;
- memorial/public-memory object.

The system should allow these meanings to accumulate instead of assigning one permanent category.

### 6. Marine Pokémon should affect the world through observed behavior

Useful non-combat states include:

- following vessels;
- nesting/roosting near coastal infrastructure;
- changing migration routes;
- using wrecks as habitat;
- reacting to noise or traffic;
- visiting fishing grounds;
- gathering around currents or food sources.

Do not infer hostility, ownership, willingness to transport people or PTU capabilities from species flavor alone.

### 7. Underwater settlements require infrastructure contracts

A submerged settlement may need authored answers for:

- breathable spaces;
- access points;
- communication;
- power;
- food/supply delivery;
- emergency evacuation;
- medical response;
- visitor access;
- construction/maintenance;
- local Pokémon coexistence.

Do not solve these with generic fantasy technology unless Ouros canon defines it.

## PTU/Caelo boundary

Existing project evidence confirms that the Python oracle distinguishes Swim movement and ocean/wetlands terrain-linked effects. This is evidence that aquatic state exists in PTU implementation; it is not proof of a complete maritime ruleset.

Relevant project/source considerations to validate before implementation:
- Swim capability and water movement;
- Gilled and breathing-related capabilities;
- Mountable/travel eligibility;
- underwater visibility/line-of-sight if any;
- Dive or semi-invulnerable Move behavior;
- drowning/suffocation rules if applicable;
- harsh weather and ocean terrain;
- fishing/capture rules;
- Caelo travel between islands and boat services;
- Caelo regional water encounter tables.

Narrative generation must not invent any of these mechanics.

## Copyright and provenance rule

This pass retains only source metadata and high-level structural lessons. It does not reproduce dialogue, campaign scenes, distinctive characters, island names for reuse, dungeon layouts, proprietary scripts or fan-created mechanics.

## Research directions for later passes

- locate public PTU sea/ship combat logs with actual encounter reports;
- inspect PTU/Caelo exact drowning, underwater and Gilled rules;
- inspect Cobblemon/Fabric APIs for persistent aquatic entities and boats;
- test whether unloaded-chunk marine movement can be represented as coarse world state;
- research fishing communities, lighthouses, ferry operations and marine research as additional non-combat institutions;
- determine whether Ouros needs true depth coordinates for underwater narrative locations or only linked sub-locations.
