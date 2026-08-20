# Cartography, Surveying & Wayfinding Research — Pass 43

Status: research/provenance only. Not Ouros canon. External sources are design references, not PTU rules sources.

## Why this pass exists

The repository already models travel connections, route knowledge, research observations, geography-dependent ecology, media/public information, language systems and changing infrastructure. What it does not yet model explicitly is the map itself as a versioned information artifact.

That distinction matters because a route can physically exist while:

- no public map includes it;
- one player has mapped it and another has not;
- a published map is outdated;
- a cave connection is known only from one entrance;
- a map contains a correct landmark but a wrong route;
- two maps disagree because they were surveyed at different dates;
- a landmark moved, collapsed, flooded or became seasonally inaccessible;
- a player annotation is useful but unverified.

This pass studies mapping as gameplay rather than treating maps as perfect omniscient UI.

## Sources reviewed

### Pokémon Brilliant Diamond / Shining Pearl — Town Map and Location Info

Official source:
https://diamondpearl.pokemon.com/en-ca/trainersguide/fundamentals/sinnoh/

The Town Map exposes known locations and can surface previously visited Honey Trees and Berry plants. This is useful because the map remembers specific discovered places rather than acting only as a static image of Sinnoh.

Reusable design lesson:

A map can store persistent player knowledge and revisit cues without revealing every meaningful location in advance.

Do not copy UI, icons, exact progression gates or Honey Tree mechanics.

### Pokémon Brilliant Diamond / Shining Pearl — Grand Underground

Official source:
https://diamondpearl.pokemon.com/en-au/trainersguide/grandunderground/

The Grand Underground uses unknown map markers that gain more specific identity after first entry. Different underground zones are also accessible from different surface positions.

Reusable structures:

- unknown-but-detected locations;
- discovery changing map representation;
- one underground network having multiple surface access points;
- terrain identity becoming known through direct exploration;
- map information increasing without the physical world itself changing.

This is especially relevant to Minecraft caves and dungeon networks.

### Pokémon Legends: Arceus — Survey Corps

Official source:
https://legends.arceus.pokemon.com/en-au/story/

The Survey Corps repeatedly leaves a hub, studies field areas and returns with knowledge. Its official framing supports exploration and surveying as institutional work rather than only travel between battles.

Reusable structure:

survey assignment -> field observation -> verified return/report -> institutional knowledge update.

Do not import the Galaxy Team, Hisui plot or Pokédex progression.

### Pokémon Sword / Shield — Wild Area

Official source:
https://swordshield.pokemon.com/en-au/gameplay/wild-area/

The Wild Area emphasizes camera-controlled exploration of a large connected region where conditions and Pokémon vary by location and weather.

Reusable lesson:

Navigation data should coexist with direct environmental observation. A complete minimap should not make looking at the actual world irrelevant.

### PTU campaign retrospective — Over There!

Source:
https://pokemontabletop.com/over-there-a-world-war-one-pokemon-campaign-a-retrospective/

The GM built a roamable world map with events, barriers and regions that changed over time. Players explored to learn surroundings and locate objectives. The damaged bridge and changing territorial pressure made geography itself part of campaign state.

Reusable structures:

- map as campaign state;
- player exploration revealing operational geography;
- changing barriers modifying future routes;
- unknown target location creating search play;
- time pressure making route choice matter.

Do not copy the campaign's Legendary structure or plot.

### PTU adventure — A Song of Ice and Ire

Source:
https://pokemontabletop.com/wiki/index.php/Quest%3AASOIAI_Adventure_Mechanics

This adventure represents its region as map nodes connected by paths. Unexplored nodes consume time; once explored and mapped, safe routes can be crossed more quickly, while dangerous areas can still require active exploration.

This is a particularly useful structural precedent for Ouros:

unknown space -> explored space -> mapped route -> routine traversal compression.

That pattern matches the existing Ouros Travel layer without forcing a new travel mechanic.

Note: this page belongs to Pokémon Odyssey-era material rather than the project's supplied PTU 1.05/Caelo rules authority. It is used only as design inspiration.

### Pokémon Tabletop community mapping guidance

Source:
https://pokemontabletop.com/

The public community guidance for maps emphasizes that exploration areas and routes should include descriptions and useful terrain/context rather than exist only as images.

Reusable lesson:

A useful map record needs semantic information about places and routes, not just coordinates.

### Public Pokémon roleplay — Treasures of Todeno

Source:
https://forums.pokecharms.com/threads/the-treasures-of-todeno.23600/

The RP uses a labeled region map plus separate area maps and broad encounter-type information. It demonstrates how community play often relies on a shared spatial reference before individual scenes begin.

Reusable lesson:

Shared regional maps and local expedition maps can have different levels of detail and authority.

No names, map art, zones or narrative content are imported.

### Game cartography research — Toups Dugas et al.

Source:
https://research.monash.edu/en/publications/making-maps-available-for-play-analyzing-the-design-of-game-carto/

The study distinguishes readonly maps used mainly for wayfinding from game cartography interfaces that players can modify persistently for planning and coordination.

Reusable lesson:

Player-authored annotations can be gameplay state rather than disposable UI.

### Player cartography as record of experience

Source:
https://pureportal.bcu.ac.uk/en/publications/on-off-and-in-the-map-materialising-game-experiences-through-play/

This work treats player-created maps as records that preserve the history of play rather than only navigation tools.

Reusable lesson:

A map can become part of the Chronicle: annotations, corrections and historical editions can show where earlier players explored and what they believed at the time.

### Mapping without replacing environmental awareness

Source:
https://research.manchester.ac.uk/en/publications/cartography-location-based-gaming-and-the-legibility-of-mixed-rea/

This research explores map designs that reduce total reliance on the screen and encourage attention to the physical environment.

Reusable lesson for Minecraft:

maps should help players orient and plan, while landmarks, signs, terrain silhouettes, sound, weather and visible infrastructure remain useful in-world navigation cues.

## PTU / Caelo cross-check

The supplied PTU/Caelo corpus remains the rules authority.

Relevant established project constraints from earlier source review:

- PTU supports meaningful exploration and recommends sessions where player choices influence outcomes.
- Caelo locations can have explicit access requirements and environmental state.
- Caelo treats route/location information as part of a structured living world.
- Pokémon capabilities such as Naturewalk and Tracker exist in the supplied Pokédex material, but a narrative map cannot grant those capabilities.
- Any Survival, Perception, navigation, tracking or exploration check must use the actual governing PTU/Caelo rule text when implemented.

No navigation DC, map bonus, scouting bonus, automatic route discovery, hidden-location detection rule or travel-speed modifier is introduced here.

## Reusable Ouros structures

### 1. Geography and representation must remain separate

The true world graph is authoritative geography.

A map is one representation of that geography made by a specific source at a specific time.

### 2. Map knowledge can be incomplete without using artificial fog everywhere

Unknown map state can mean:

- not surveyed;
- detected but not identified;
- mapped approximately;
- mapped confidently;
- formerly mapped but now stale;
- disputed;
- deliberately withheld;
- inaccessible to the current actor.

### 3. Map editions should persist

A map from five years ago can remain useful evidence even after becoming operationally obsolete.

Old maps can support archaeology, infrastructure history, missing routes, habitat change and cases.

### 4. Player annotations need provenance

A marker added by a player can be true, mistaken, speculative or outdated.

The marker should preserve author, timestamp and source context.

### 5. Surveying should create evidence, not truth by fiat

Survey work can produce measurements, observations and proposed geometry. Institutional review or repeated travel may raise confidence, but the system should preserve uncertainty.

### 6. Route familiarity should reduce repetition

This aligns with the existing Travel layer. Once a route is known, safe and current, routine traversal can compress. Mapping does not create fast travel by itself.

### 7. Spatial knowledge can be private or shared

Multiplayer characters may know different entrances, hazards, landmarks or shortcuts. Sharing a map transfers information, not physical access.

### 8. Sensitive locations require redaction support

Conservation sites, private residences, medical locations, protected archaeology and hidden faction facilities may need maps that omit or generalize coordinates.

### 9. Maps can be historical artifacts

Map editions, survey notes and trail logs should integrate with Archives, Public Memory and Material Provenance rather than be overwritten when corrected.

## Copyright / transformation boundary

This pass does not copy game maps, fan maps, location layouts, dialogue, distinctive plots or prose. It extracts only high-level structures about discovery, map knowledge, surveying, versioning and navigation.

## Open research directions

- PTU/Caelo exact text for Survival, Perception and any navigation-related Features or Edges.
- Whether Caelo has explicit map, guide, trail, wilderness or route-check procedures beyond the location-access material already reviewed.
- Minecraft/Cobblemon hooks for persistent per-player map markers, discovered POIs and server-authored waypoints.
- Accessibility requirements for map information beyond visual-only presentation.
- Whether AutoPTU-Java ever needs spatial-survey information, or whether all cartography should remain outside the battle core.
