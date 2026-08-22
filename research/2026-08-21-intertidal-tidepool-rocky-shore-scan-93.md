# Pass 93 Research — Intertidal, Tidepool & Rocky-Shore Ecology

Status: RESEARCH / PROVENANCE. Not Ouros canon. No PTU mechanic is established here.

## Why this pass exists

The repository already contains dedicated layers for Maritime, Open Ocean, Estuaries/Tidal Wetlands, Coastal Geomorphology, Coral Reefs, Fisheries, Conservation, Tourism, Seasonality and Freshwater. The full design/research/proposals trees were inspected before writing. No dedicated layer existed for the ecological and narrative interface exposed and submerged by the ordinary tide cycle: rocky intertidal zones, tidepools, low-tide access windows, pool isolation, splash/high/mid/low zonation, repeated transects, human trampling/collection pressure, and the difference between a shoreline being physically present and being temporarily accessible.

This pass therefore owns neither open-ocean conditions nor shoreline geomorphology. It focuses on the living edge between them.

## Source findings

### 1. Official Pokémon species can support intertidal behavior without creating universal rules

Pokémon Pokédex — Binacle
https://www.pokemon.com/uk/pokedex/binacle
Inspected 2026-08-21.

Useful pattern: two Binacle attach to a suitable rock and gather food during high tide. This gives Ouros a species-specific example where substrate identity and tidal phase can matter to observation. It does not prove that every Binacle colony occupies an intertidal zone, that rocks grant cover, or that high tide applies a battle bonus.

Pokémon Pokédex — Pyukumuku
https://www.pokemon.com/us/pokedex/pyukumuku
Inspected 2026-08-21.

Useful pattern: Pyukumuku inhabits warm shallow water and can remain on land for long periods because of its protective slime. This supports repeated shallow-water/shore observations and temporary exposure without deriving dehydration rules, land penalties or a generic shoreline capability.

Pokémon Pokédex — Wimpod
https://www.pokemon.com/el/pokedex/wimpod
Inspected 2026-08-21.

Useful pattern: Wimpod form colonies, remain alert, scatter when threatened and act as scavengers. For Ouros this can create low-tide colony observations, disturbance-response records and cleanup/scavenging ecology. It must not be generalized into a tactical swarm, shared initiative, automatic Run Away behavior or a scripted retreat unless PTU/AutoPTU verifies that exact mechanic.

### 2. Rocky intertidal habitat is strongly zoned by exposure time, wave action and biological interactions

NOAA repository — Ecological Linkages: Marine and Estuarine Ecosystems of Central and Northern California, Rocky Intertidal Communities
https://repository.library.noaa.gov/view/noaa/17789/noaa_17789_DS1.pdf
Inspected 2026-08-21.

Reusable structure: splash, high, middle and low intertidal zones experience different durations of exposure and submersion. Distribution also depends on wave action, drying, temperature, predation and competition. Ouros should represent coarse ecological bands and observed occupancy, not a universal four-row map template.

Monterey Bay National Marine Sanctuary — Final Management Plan, Rocky Shores
https://sanctuaries.noaa.gov/jointplan/fmp/101408mbnmsfmp.pdf
Inspected 2026-08-21.

Reusable structure: zonation is real but highly variable. Wave exposure and local geometry can shift or blur zones. Low tide also turns the habitat into an unusually accessible research/education space. This argues against a deterministic `height -> species list` rule.

### 3. Tidepools are temporary refuges and research sites whose state changes with the tide

National Park Service — Life in the Rocky Intertidal Zone
https://home.nps.gov/cabr/learn/upload/Life-in-the-Intertidal-Accessible-Guide.pdf
Inspected 2026-08-21.

Reusable structure: tidepools are created by changing water levels and include high, middle and low zones. New/full-moon alignments can produce extreme tides. The same site can therefore have different access, exposure and observable communities at different times without changing its persistent identity.

Important management lesson: visitor handling matters. Organisms can be harmed by being moved even short distances, and collection may be restricted. Ouros can use stewardship, visitor pressure and research etiquette as story material. It must author local rules rather than import real-world law.

### 4. Intertidal systems are useful because accessibility and vulnerability coexist

NOAA — Rocky Intertidal Climate Vulnerability summary
https://repository.library.noaa.gov/view/noaa/13953/noaa_13953_DS1.pdf
Inspected 2026-08-21.

Reusable structure: rocky intertidal habitats can be simultaneously accessible, scientifically valuable and sensitive to trampling, pollution, erosion, wave action, salinity and range shifts. This supports narrative conflicts where tourism, education, harvesting, restoration and conservation all have legitimate interests.

### 5. PTU community design supports biome-specific encounter zones and noncombat uses of Pokémon

Reddit /r/PokemonTabletop — Fishing tournament, help wanted
https://www.reddit.com/r/PokemonTabletop/comments/jh12kh
Inspected 2026-08-21.

Reusable structure: one public PTU discussion divides a water body into sandy shore, rocky shore/nesting area, open water, underwater and other zones, then encourages scouting and Pokémon capabilities to matter before capture. The useful lesson is spatially differentiated encounter context, not its exact species list or contest rules.

Reddit /r/PokemonTabletop — Creative early encounters
https://www.reddit.com/r/PokemonTabletop/comments/vsv8xg
Inspected 2026-08-21.

Reusable structure: a community example uses a beach route whose availability changes with the tide, with wild Pokémon activity tied to that repeating physical cycle. The principle is valuable for Ouros: a route can be conditionally available without becoming a one-time dungeon door.

Reddit /r/PokemonTabletop — Favorite nonviolent encounters
https://www.reddit.com/r/PokemonTabletop/comments/1fta66r
Inspected 2026-08-21.

Reusable structure: community answers emphasize injured Pokémon, helping travelers and other travel events that resolve without combat. Intertidal windows are especially suited to observation, rescue, research, stewardship and access problems rather than mandatory fights.

These Reddit sources are community examples, not rules authority.

## High-level reusable design lessons

1. A tidepool site should keep one persistent identity while its water coverage, access and visible occupants vary by tide.
2. Tide state and ecological zonation are related but not identical. Local geometry and wave exposure can alter the pattern.
3. Low tide can reveal temporary routes, isolated pools, stranded objects, research surfaces, footprints, nests or old infrastructure. Exposure does not automatically make them safe or collectible.
4. A tidepool observation should store the tidal phase and local condition under which it was made. Otherwise two correct surveys may look contradictory.
5. Organisms that remain in an isolated pool during low tide can create repeated individual or collective observations without implying ownership or capture availability.
6. Visitor pressure can create content through crowding, handling, collection, trampling and path formation. It should not automatically create ecological damage without evidence.
7. A low-tide path is a temporary connection in Travel/Cartography. It should never be promoted to permanent geography merely because Minecraft exposed it once.
8. Conservation closures need scope, reason and duration. A sensitive low intertidal site may be restricted while adjacent coastline remains open.
9. Storm-driven shoreline change belongs to Coastal Geomorphology. Ordinary tide exposure belongs here. Estuarine salinity belongs to Estuaries. Open-ocean currents belong to Open Ocean.
10. Tidepool stories work well when the player must decide whether to observe, rescue, collect evidence, wait, reroute, protect a site or leave it alone.

## PTU / AutoPTU guardrails

The project PTU corpus available in this runtime did not surface a dedicated tidepool mechanic. Python AutoPTU remains the rules oracle while Java is incomplete. Therefore this research does not create:

- tide damage;
- wave knockback;
- slippery-rock checks;
- automatic Rough/Slow Terrain;
- dehydration or exposure damage;
- forced Swim checks;
- drowning;
- salinity effects;
- automatic Water Terrain;
- low-tide capture bonuses;
- Wimpod colony initiative;
- Binacle high-tide buffs;
- Pyukumuku land immunity;
- automatic Naturewalk eligibility.

If a future encounter uses such mechanics, the exact PTU/Caelo rule and Java contract must be cited before promotion.

## Research-to-design handoffs

Intertidal -> Maritime: coastal access and sea-facing context.

Intertidal -> Coastal Geomorphology: substrate/shoreline revisions after storms or erosion.

Intertidal -> Estuaries: salinity and tidal-wetland systems where applicable.

Intertidal -> Coral Reef: reef condition when a reef system intersects the shore.

Intertidal -> Conservation/Tourism: visitor pressure, stewardship, closures and education.

Intertidal -> Seasonality/Astronomy: recurring tide windows may use authored calendar/astronomical inputs, but this layer should consume those inputs rather than calculate celestial mechanics itself.

Intertidal -> Cartography/Travel: temporary low-tide routes and access windows.

Intertidal -> Cobblemon: coarse presence opportunities only after server-owned ecology state is established. Loaded entities never become population truth.

Intertidal -> AutoPTU: freeze a battle snapshot only from mechanics already supported and validated.