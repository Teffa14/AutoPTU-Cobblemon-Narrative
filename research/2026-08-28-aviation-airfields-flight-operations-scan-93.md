# Aviation, Airfields & Flight Operations Research — Pass 93

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file establishes Ouros canon.
Date: 2026-08-28

## Purpose

Pass 93 investigates how an airfield, flight service or airborne transport network can become persistent world state without turning aviation into universal fast travel, inventing PTU flight rules, or assuming that Ouros canon contains any specific aircraft technology.

The current Narrative repository already contains Travel, Transit Hubs, Interregional Mobility, Weather, Technology, Workplaces, Cargo/Material Culture and Pokémon Work. The missing coordination layer is narrower: persistent airfield identity, landing-area state, individual flight operations, ground/air handoffs, weather holds, diversions, operational notices and long-term reuse of aviation sites.

The complete repository tree was inspected before selecting this subject. The tree at `f0c611d6e177563150c6fec84587826b72902735` reported `truncated=false`. No existing design, research or proposal file was found for airports, aviation or airfields. Waste/sanitation was explicitly rejected as a candidate after the complete inventory revealed the existing Pass 52 layer.

## Public Pokémon sources

### 1. Mistralton City and Mistralton Cargo Service

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Mistralton_City_Runway
- https://bulbapedia.bulbagarden.net/wiki/Mistralton_City_Cargo_Service

Observed reusable structures:
- one city can be spatially organized around an airfield rather than treating the airport as an isolated menu;
- cargo handling, aircraft, runway, control functions and ordinary community activity coexist at the same location;
- the runway has time-dependent use rather than being permanently inaccessible scenery;
- agriculture around the field connects a local production system to outbound cargo;
- a transport facility can also be a social landmark and workplace.

Transformation for Ouros:
An aviation site should have several independently queryable states. A terminal may be open while a landing area is unavailable. Cargo can be staged while no flight is ready. A service can be suspended while the physical field remains intact. Nearby production, commerce or neighborhoods can respond to service changes through their own systems.

Do not import Skyla, Mistralton, its precise schedule, its planes, its Gym, its cargo pattern or its regional geography into Ouros.

### 2. Lentimas Town

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Lentimas
- https://www.serebii.net/pokearth/unova/lentimastown.shtml

Observed reusable structures:
- a small settlement can be connected to a larger hub through a specific air link;
- arrival by air can change the practical connection graph of a region;
- the destination runway is much smaller than the origin hub;
- the return connection remains a world service rather than requiring the player to own a flying Pokémon.

Transformation for Ouros:
Air links should be ordinary `travel_connection` and `transport_service` inputs when canon supports them. A remote landing site does not need the same facilities as a major hub. Access to a region can therefore depend on a functioning service without making that service the only possible long-term route.

### 3. Mistralton in the animation

Source:
- https://www.serebii.net/anime/epiguide/bestwishes/728.shtml

Observed reusable structure:
The airport/cargo facility functions as a recognizable civic destination whose schedules, staff and other institutional uses shape who is present and when.

Transformation for Ouros:
An airfield can have recurring workers, visitors and institutional users. Transit Hubs should own temporary passenger/co-presence scenes; Aviation should only provide the operational flight and field state that makes those scenes plausible.

No episode plot, dialogue or character behavior is copied.

## PTU community sources

### 4. Pokémon: World Tour — PTU campaign pitch

Source:
- https://startplaying.games/adventure/clu4b22ct00ip08lc4q1o3eqd

Observed reusable structures:
- a mobile airborne base can give a long campaign a recurring home between regions;
- the vehicle can support exploration, social continuity and repeated returns;
- movement between distant cultures becomes part of campaign structure rather than merely a loading transition.

Important rejection:
The campaign advertises custom airship and sky-battle mechanics. Those are not governing Ouros rules and are not evidence that PTU/AutoPTU currently supports vehicle combat, aerial hazards, moving-platform battles or ship-to-ship resolution.

Transformation for Ouros:
If Ouros ever canonizes an aircraft or airship as a mobile base, use the existing Travel `mobile_base` model plus an aviation operational record. Combat on or around it remains gated by exact engine capabilities.

### 5. PTU One-Shot Ideas discussion

Source:
- https://www.tapatalk.com/groups/pokemon_tabletop/ptu-one-shot-ideas-t5633.html

Observed reusable structures:
- one location/problem can combine exploration, puzzle evidence and mystery instead of requiring repeated battles;
- transport technology can be the consequence of an investigation rather than the starting assumption;
- a short scenario benefits from a small number of meaningful encounters supported by NPC goals.

Transformation for Ouros:
Aviation mysteries should often be solved through logs, route evidence, cargo provenance, weather records, maintenance history and actor testimony before any tactical encounter. The air vehicle itself does not need to become a boss object.

No creature, reveal, plot or distinctive scenario from the source is imported.

## PTU 1.05 mechanical boundary

Sources:
- https://anyflip.com/tcye/paot/basic/201-250
- https://pokemontabletop.fandom.com/wiki/Playing_The_Game

Relevant governing observations:
- PTU has explicit movement capabilities including Sky;
- mounted transport depends on the actual Pokémon, including practical size, Power and sometimes equipment;
- being a flying species is therefore insufficient evidence that an individual can carry a Trainer;
- the rules discuss mounted movement and Intercept interactions, but this does not establish aircraft operation, vehicle capacity, aviation safety, fuel, navigation, runway rules or vehicle combat.

Pass 93 therefore establishes no:
- pilot Skill or piloting DC;
- aircraft speed, endurance, fuel or cargo formula;
- passenger capacity;
- takeoff/landing check;
- runway length requirement;
- crash, fall, decompression or collision damage;
- turbulence or crosswind modifier;
- aerial-combat altitude system;
- vehicle HP;
- automatic passenger-carrying permission for any species;
- bonus for Flying-type Pokémon;
- weather-to-flight formula;
- Trainer Feature that grants aircraft operation.

Any such mechanic needs direct PTU/Caelo review and current AutoPTU evidence.

## Design lessons extracted

Air transport becomes useful narrative infrastructure when several layers remain separate: physical landing site, operator/service, exact trip, passengers, cargo, forecast, observed conditions, maintenance, public information and final arrival/departure facts.

A field can be physically usable while a service is suspended. A flight may be delayed even when the airport remains open. Cargo can arrive without its intended passenger cohort. A destination can receive a diversion without becoming a permanent scheduled stop. A former strip can become habitat, public space or another facility while retaining its history.

A forecast remains evidence available to an operator; it does not decide the future. A control-board entry or announced departure does not prove that a flight actually occurred. An aircraft seen overhead does not prove its origin, destination, passengers or cargo.

## Cobblemon/Minecraft reuse implications

Strong design-level reuse candidates:
- building blocks, runway/apron geometry and lighting presentation;
- signs, boards, maps, barriers and doors;
- world coordinates and day/night presentation;
- weather visuals;
- Pokémon entities, models, forms, flying poses, animations and cries;
- particles, sounds, UI, networking and synchronization.

Adapter review is required for:
- boarding/interacting intent;
- projecting service/flight state into boards, gates and barriers;
- mapping observed world weather into narrative observations without making it tactical Weather;
- persistent aircraft or mobile-base entity references if the integration stack provides them;
- recording arrival/departure observations with provenance.

Battle authority remains forbidden for Cobblemon battle-state/controller code. Nearby flying Pokémon, passengers, workers or visible entities never become combatants automatically.

## Originality and canon boundary

All Ouros material derived from this pass must remain proposed until reviewed. The sources above contribute high-level structures only. No named Pokémon-world airport, operator, aircraft, route, character, fan-campaign vehicle, plot, dialogue or custom mechanic is promoted to Ouros canon.