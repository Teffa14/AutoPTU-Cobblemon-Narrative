# Research Scan 99 — Winter Mountain Pass, Snow & Avalanche Operations

Status: RESEARCH / PROVENANCE ONLY. This file does not establish Ouros canon or PTU mechanics.
Date: 2026-08-28
Narrative baseline inspected before writing: `aee7933fe23c789fb249e2de254188e6e8063895`.

## Why this pass

The repository already has Weather Forecast & Preparedness, Roads/Bridges/Detours, Crisis/Rescue/Recovery, Geology, Travel and Wildfire continuity. The recursive repository inventory contained no dedicated snowpack, avalanche, winter-pass or snow-clearance layer, and repository search returned no existing research package for avalanche/snowpack/winter-pass operations.

The gap is therefore operational rather than meteorological: preserve what is known about snow on a specific mountain route, what sectors are usable, what was observed or cleared, what access decision followed, what later changed, and why a route did or did not reopen.

## Public Pokémon sources

### Sinnoh Route 216 and Route 217

Sources:
- Bulbapedia, Sinnoh Route 216: https://bulbapedia.bulbagarden.net/wiki/Sinnoh_Route_216
- Bulbapedia, Sinnoh Route 217: https://bulbapedia.bulbagarden.net/wiki/Sinnoh_Route_217

Reusable structure:
- persistent winter conditions can change the ordinary experience of a route;
- deep snow and low visibility can matter to travel even when the route still exists;
- a remote lodge or other small refuge can make a harsh corridor socially playable rather than merely punitive;
- travelers, local residents and wild Pokémon continue to inhabit the same landscape under severe conditions.

Transformation for Ouros:
- preserve route identity while access and observed conditions change;
- allow refuges, observation posts, crews or local knowledge to become recurring nodes;
- separate severe overworld conditions from tactical PTU Weather unless an exact mapping is validated.

Not imported:
- Sinnoh geography or NPCs;
- automatic hail in every battle;
- exact movement penalties from the video games;
- assumptions that a visual blizzard always creates PTU Hail.

### Twist Mountain and Unova seasonal change

Sources:
- Bulbapedia, Twist Mountain: https://bulbapedia.bulbagarden.net/wiki/Twist_Mountain
- Bulbapedia, Season game mechanic: https://bulbapedia.bulbagarden.net/wiki/Season_(game_mechanic)

Reusable structure:
- seasonal snow can both open and close access;
- accumulation can create temporary traversable surfaces while burying other entrances;
- the same authored location can have materially different route topology across seasons without becoming a different place.

Transformation for Ouros:
- model authored winter access revisions against persistent route/sector IDs;
- record temporary snow-created access as its own state rather than silently rewriting geometry;
- preserve the old and later configurations for memory, navigation, ecology and future quests.

Not imported:
- Unova calendar cadence;
- exact ice-tile behavior;
- fossil/NPC content;
- game-specific traffic-cone gating.

### Mount Coronet as a regional mountain corridor

Source:
- Bulbapedia, Mount Coronet: https://bulbapedia.bulbagarden.net/wiki/Mount_Coronet

Reusable structure:
- one mountain mass can connect multiple settlements while becoming progressively more rugged;
- internal caves, exterior snowfields and built crossings can coexist in one travel system;
- sacred, historic and transportation meaning can overlap without being the same authority.

Transformation for Ouros:
- a winter operations layer should hand off to Myth/Archaeology, Travel, Roads and Conservation rather than own all meanings of a mountain corridor.

### Snover seasonal movement

Source:
- Bulbapedia, Snover: https://bulbapedia.bulbagarden.net/wiki/Snover_(Pok%C3%A9mon)

Reusable structure:
- a species can change elevation or distribution across cold seasons;
- repeated winter observations can become ecological evidence instead of encounter-table decoration.

Transformation for Ouros:
- winter closures or snow-clearing work can intersect wildlife observations;
- Conservation/Wildlife decides whether those observations support a migration or habitat claim.

Not imported:
- a universal seasonal behavior for all Snover in Ouros;
- a rule that nearby Ice-type Pokémon predict avalanche conditions.

## Tabletop and community sources

### Pokémon Journeys Winter Playtest

Source:
- Pokémon Tabletop RPG, “Pokemon Journeys Winter Playtest”: https://pokemontabletop.com/pokemon-journeys-winter-playtest/

The public playtest describes a multi-session adventure centered on being stranded on a mountain during a blizzard. It is not PTU 1.05 rules evidence, but it is useful tabletop design evidence from the broader Pokémon tabletop community.

Reusable structure:
- severe winter travel can sustain several sessions through shelter, navigation, resource decisions, encounters and changing route knowledge;
- the mountain itself can remain the continuity object while individual scenes vary;
- survival pressure does not require every obstacle to become combat.

Not imported:
- playtest-specific rules;
- its characters, jokes, encounter sequence or exact module plot;
- any survival statistic or cold-damage rule.

## PTU 1.05 cross-check

Sources:
- PTU 1.05 Core, Movement and Positioning excerpt: https://peda.net/p/josajoki/fista/ohjeet/ptu/pokemon-tabletop-united-1.05-core%3Afile/download/c109e0ecc0ac41065575a4a324183b80189a2c70/Pokemon%20Tabletop%20United%201.05%20Core.pdf
- PTU community reference for Ice moves: https://pturpg.wikidot.com/ice

Relevant governing evidence:
- PTU explicitly defines Slow Terrain and gives deep snow and even ice as examples that can qualify; movement through Slow Terrain costs extra movement distance.
- PTU separately defines battlefield Weather such as Hail and exact Move effects such as Hail, Blizzard and Avalanche.

Guardrail:
- the existence of deep-snow Slow Terrain does not prove every winter surface is Slow Terrain;
- the existence of Hail does not mean ordinary snowfall, a blizzard visual, blowing snow or an avalanche automatically becomes Hail;
- the Move named Avalanche is a combat Move and provides no general environmental avalanche subsystem;
- environmental cold, burial, suffocation, snow-slide displacement, falling damage, visibility penalties and rescue mechanics require separate governing evidence.

## Real-world operational references used only for information architecture

### Avalanche.org forecast model

Source:
- Avalanche.org, Avalanche Forecast: https://avalanche.org/avalanche-encyclopedia/human/resources/avalanche-forecast/

Useful architecture:
- a forecast has a geographic scope and validity window;
- it communicates assessed danger, identified problems, weather/snowpack information and travel advice;
- forecast information is decision support, not a guarantee about one exact slope.

Ouros transformation:
- winter condition products should reference scope, issue time, source observations and validity window;
- access owners make their own route decisions from that evidence.

Not imported:
- North American danger scales, legal duties, thresholds or terminology as Ouros canon.

### Avalanche Canada Mountain Information Network

Sources:
- Avalanche Canada MIN overview: https://avalanche.ca/mountain-information-network
- Avalanche Canada MIN introduction: https://avalanche.ca/news/introduction-mountain-information-network

Useful architecture:
- location-specific public observations can be separated by weather, snowpack, avalanche and incident report type;
- crowdsourced observations can be valuable evidence without becoming authoritative truth;
- geolocation and timestamp matter strongly when reconciling apparently conflicting mountain reports.

Ouros transformation:
- local travelers, Rangers, crews, residents or researchers may submit winter observations;
- each observation keeps provenance and does not automatically alter the authoritative access state.

### National Park Service mountain-road operations

Sources:
- Mount Rainier Winter Safety: https://home.nps.gov/mora/planyourvisit/winter-safety.htm
- North Cascades Winter Safety: https://home.nps.gov/noca/planyourvisit/winter-safety.htm
- Glacier National Park 2024 Spring Operations: https://www.nps.gov/glac/learn/news/glacier-national-park-announces-2024-spring-operations.htm
- Glacier avalanche rescue/closure example: https://www.nps.gov/glac/learn/news/media-21-10.htm

Useful architecture:
- road opening can depend on hazard assessment as well as physical clearing;
- a cleared section may need to be cleared again after new weather;
- avalanche paths above a road can matter even when the hazard source is not visible from the traveled surface;
- response may deliberately wait for a safer operational window before rescue or access work proceeds.

Ouros transformation:
- `cleared` and `open` remain separate;
- clearing work is revisioned and can be superseded by new accumulation or slide debris;
- access decisions can reference observed conditions outside the road footprint;
- a route may reopen partially or remain restricted after the immediate obstruction is removed.

Not imported:
- US agency procedures, road standards, public safety law, plowing specifications or avalanche-control practice.

## Design lessons extracted

1. Snow is persistent world state, not a one-scene visual effect.
2. A mountain corridor needs stable sector identity so observations and access decisions can refer to the same place across days and seasons.
3. Snow accumulation can close, expose or create routes; each change must preserve history and provenance.
4. Forecast, observation, operational assessment, clearing attempt and access decision are different records.
5. “No avalanche observed” is not evidence that a slope is safe.
6. A reported slide is not automatically an authored environmental attack.
7. A cleared road may remain closed for another reason.
8. A reopened road may close again because new accumulation changes the evidence.
9. Wildlife presence near a pass can be ecologically meaningful without being the cause of a closure.
10. Local observations can be useful while remaining non-authoritative.
11. Harsh winter travel can support shelter, investigation, route planning, rescue and social scenes without constant combat.
12. Reduced tactical versions should freeze the winter incident state before AutoPTU begins.

## Candidate Ouros boundary

Research-supported candidate only:

`Seasonality/Weather observations -> winter mountain assessment -> route owner access decision -> Travel viability`

Crisis owns rescue/stabilization. Roads owns road/crossing operational state. Facility Maintenance/Public Works own repair and engineered assets. Conservation owns ecological interpretation. The proposed winter layer should own snow/avalanche observation continuity, winter-sector assessment, clearing history and winter access evidence only.

## Canon questions intentionally unresolved

- Which Ouros regions have persistent seasonal snow?
- Which high passes exist and which are maintained?
- Which institutions, if any, issue winter mountain assessments?
- Are there formal warning categories?
- What technologies exist for snow clearing, observation or communications?
- Are there maintained shelters, patrol posts or seasonal camps?
- Which Pokémon have explicitly established individual winter-work roles?
- Do any sacred or protected mountain zones constrain clearing or access?

## Mechanical questions intentionally unresolved

- When exact authored snow qualifies as PTU Slow Terrain.
- Whether any source defines ice-specific trip/fall behavior beyond Slow Terrain.
- Environmental avalanche displacement, burial, damage, suffocation or extraction.
- Snowfall/blizzard-to-PTU-Weather mapping.
- Visibility/LoS penalties from blowing snow.
- Cold exposure, exhaustion or hypothermia.
- Falling/cornice/collapse rules.
- Snow-clearing Move/Capability conversions.
- Avalanche rescue/carry actions.
- Dynamic changing snow zones during battle.

These remain UNKNOWN until governing PTU/Caelo rules and engine contracts are verified.