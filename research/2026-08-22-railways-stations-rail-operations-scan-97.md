# Railways, Stations & Rail Operations Research Scan — Pass 97

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is established Ouros canon or a PTU rules source.
Date: 2026-08-22

## Why this pass exists

The repository already has broad Travel/Transport, Technology/Infrastructure, Workplaces, Demography, Urban Public Space, Road Ecology, Freight/Illicit Networks and Crisis layers. The internal file inventory was inspected before choosing this topic.

The existing Travel layer explicitly reserves `RAIL_OR_TRANSIT if canon supports it`, but treats rail as one possible connection/service type rather than a persistent operational system. The repository did not contain a dedicated railway/station layer in `design/`, `research/` or `proposals/`.

Pass 97 therefore studies rail as a world-state connector rather than as a new movement mechanic.

## Source-use rule

External Pokémon stories, fangames and real rail material are inspiration sources only.

They may support structures such as:
- stations acting as gateways and social hubs;
- separate passenger and freight flows;
- track capacity and dispatch conflicts;
- yards, sidings and transfer points;
- service disruption and recovery;
- grade-crossing conflicts;
- moving-train mysteries;
- rail corridors altering settlements and wildlife movement.

They do not establish Ouros law, fares, train speeds, braking formulas, vehicle damage, collision damage, timetable rules, PTU movement, pursuit rules or tactical railway hazards.

## Sources and reusable lessons

### 1. Gare de Lumiose as an arrival gateway

Source: Pokémon.com, “Explore Pokémon Legends: Z-A Locations in Pokémon TCG Artwork,” 16 June 2026.
https://www.pokemon.com/us/pokemon-news/explore-pokemon-legends-z-a-locations-in-pokemon-tcg-artwork

Pokémon Legends: Z-A begins with the player arriving at Gare de Lumiose. The useful structure is not the specific station or plot. It is the station as a threshold between regional travel and local city life.

Reusable lessons:
- an arrival station can be one of a settlement's strongest first impressions;
- arrival state can expose maps, service notices, local news, lodging, onward transport and NPC activity without requiring a quest giver;
- station reconstruction or relocation can change which district becomes a gateway to the region;
- the station can remain socially important even when no battle occurs there.

### 2. Battle Subway: one rail institution can serve several functions

Source: Pokémon.com, “Remember the Region: Unova Spotlight,” August 2026.
https://www.pokemon.com/us/features/remember-the-region-unova-spotlight

The Battle Subway combines a rail facility, multiple lines, a specialized competitive institution and a real connection to Anville Town.

Reusable lessons:
- different lines can have different purposes without requiring separate world systems;
- a station can contain a battle institution while still functioning as transportation infrastructure;
- a terminal or interchange can create identity through destinations, line histories and public records;
- operational rail state and formal battle results should remain independent.

Do not copy Battle Subway rules, line names, bosses or reward structures.

### 3. Rail yard and moving-train pursuit

Source: Pokémon.com, “Battle for the Underground!”
https://www.pokemon.com/us/animation/seasons/14/episode-48-battle-for-the-underground

The episode uses subway tunnels, a railcar, a moving train, decoys, a rail yard and Anville Town as linked spaces during one incident.

Reusable lessons:
- a rail incident can move through several operational spaces rather than remain in one arena;
- yards and sidings are distinct locations with their own access and information state;
- a moving train can be a temporary location whose cars form a sequence of rooms;
- decoy routing works best when the network topology is already understandable to players.

For Ouros, any moving-train combat remains implementation-blocked until movement, vehicle/world projection and tactical AI contracts exist. The narrative can still use an onboard investigation with a static encounter snapshot.

### 4. A Pokémon can disrupt rail infrastructure without being an antagonist

Source: Pokémon.com, “Mind-Boggling Dynamax!”
https://www.pokemon.com/us/animation/seasons/23/episode-5-mind-boggling-dynamax

A Snorlax obstructs a railroad crossing and creates an urgent infrastructure problem. The useful pattern is conflict caused by incompatible physical presence rather than hostile intent.

Reusable lessons:
- the immediate objective may be to clear or protect a route rather than defeat a Pokémon;
- dispatch, public warnings and route closure can matter before any encounter begins;
- a railway can intersect wildlife movement, sleeping/rest sites, migration or changing urban development;
- successful resolution can be rerouting, delay, withdrawal or restoring safe passage.

Do not infer Dynamax, train impact damage or moving-train timing rules.

### 5. Trains can be transient social spaces and mysteries

Source: Pokémon.com, “The Spectral Express!”
https://www.pokemon.com/us/animation/seasons/25/episode-1-the-spectral-express

The useful pattern is the train as a temporary social location during a transfer journey. Boarding, transfer, carriage sequence and arrival all shape the episode.

Reusable lessons:
- a passenger can know their destination but still board the wrong service;
- carriage occupancy can create temporary social graphs among strangers;
- an onboard incident can end when the train arrives rather than with a conventional dungeon boss;
- transfer stations can produce missed connections, reunions, handoffs and information gaps.

The supernatural material is not reused.

### 6. Fangame: the train itself as a bounded mystery location

Source: Eevee Expo, “THEFT on the MAGNET TRAIN EXPRESS,” 2020.
https://eeveeexpo.com/threads/2662/

This completed fangame builds a short mystery around a blackout and a search from one end of a train to the other. Public feedback also noted that searching objects was enjoyable but clues needed stronger gameplay consequences.

Reusable lessons:
- train cars provide natural spatial sequencing for a compact mystery;
- a service disruption can transform ordinary transit into a temporary adventure site;
- clue collection should affect hypotheses, access, interviews or resolution rather than exist as decorative clicking;
- moving-location mysteries benefit from a hard arrival/departure clock.

Do not copy its disappearance, characters, dialogue, twists or endings.

### 7. Rail systems are constrained networks, not arbitrary fast travel

Source: Federal Railroad Administration, Railroad 101 Videos.
https://railroads.dot.gov/rail-network-development/training-guidance/railroad-101-videos

FRA distinguishes train types/performance, track configuration, basic operations and signaling. The important high-level lesson is that infrastructure and operations jointly determine usable capacity.

Reusable lessons for Ouros:
- a physical track can exist while service is unavailable;
- a train can be ready while no route slot exists;
- maintenance vehicles and inspections can consume network capacity;
- single-track, double-track, sidings and junctions create different operational possibilities;
- service delays should propagate through explicit dependencies, not random timers.

No real-world formulas or regulations are imported.

### 8. Interlockings, route authority and dispatch create causal delays

Source: FRA technical material on railroad capacity/interlockings/centralized traffic control.
https://railroads.dot.gov/sites/fra.dot.gov/files/fra_net/1308/rich_vol_1.pdf

The reusable abstraction is that junctions cannot route incompatible movements simultaneously. Dispatchers use track assignments, sidings and priorities to manage conflicts.

Ouros can simplify this into coarse route-slot state:
- AVAILABLE;
- RESERVED;
- OCCUPIED;
- BLOCKED;
- MAINTENANCE;
- UNKNOWN.

This is world simulation state only. It is not a tactical initiative system.

### 9. Grade crossings are interfaces between two mobility systems

Source: Federal Railroad Administration, Highway-Rail Grade Crossing Safety, updated 24 June 2025.
https://railroads.dot.gov/railroad-safety/divisions/crossing-safety-and-trespass-prevention/railroad-crossing-safety

The useful design point is that a crossing is where rail state and road/pedestrian state must coordinate. A crossing can be physically present but unavailable to road traffic while a train movement has priority.

Reusable lessons:
- crossings deserve persistent IDs and incident history;
- blocked crossings can affect emergency response, commuting and wildlife routes;
- warnings and barriers are presentation of authoritative route state, not the authority themselves;
- maintenance or failure at one crossing can create secondary pressure elsewhere.

Do not import U.S. law or crossing standards into Ouros canon.

### 10. Rail resilience links transport to crises and long recovery

Source: Federal Railroad Administration, “FRA Climate and Sustainability: Rail Resiliency,” 2024.
https://railroads.dot.gov/sites/fra.dot.gov/files/2024-07/FRA%20Resiliency%20Bulletin%20July%202024_%20PDFa.pdf

The FRA document treats floods, wildfire, severe storms, infrastructure failure and maintenance as causes of disruption to rail assets and service.

Reusable lessons:
- the same physical network can have several degraded-service states;
- a washed-out section can reroute passengers, freight and staff differently;
- repair does not automatically restore the old timetable;
- resilience improvements made during quiet periods can matter in a later crisis.

### 11. Rail corridors can affect wildlife movement

Source: U.S. DOT / North Carolina Statewide Multimodal Freight Plan 2023, discussion of potential rail-freight habitat impacts.
https://www.transportation.gov/sites/dot.gov/files/2023-12/NCDOT_SMFP_FullReport_Final_4212023_June.pdf

The report notes that railways can fragment habitat and affect wildlife movement, while crossings/underpasses may need dedicated study.

Reusable lessons:
- a rail corridor can be a barrier, neutral feature or movement route depending on species and place;
- one observed crossing does not prove restored connectivity;
- abandoned rights-of-way can acquire new ecological functions;
- wildlife and service operation should be modeled as interacting systems rather than a generic `rail = bad` flag.

Real-world mortality rates or management rules are not imported.

### 12. Station safety and access are separate from train movement

Sources:
- FRA, Pedestrian and Motorist Safety at Highway-Rail Grade Crossings.
  https://railroads.dot.gov/highway-rail-crossing-and-trespasser-programs/pedestrian-motorist
- FRA, guidance discussing warnings, platform improvements and access controls near stations.
  https://railroads.dot.gov/elibrary/fra-issues-guidance-improving-safety-highway-rail-grade-crossings-and-preventing-railroad

Reusable lessons:
- station access, platform access and track access are different permissions;
- passenger information should reflect service state but should not silently become the source of truth;
- an accessible route to a platform is a station property independent of whether a train is running;
- crowd management and emergency egress belong to the overworld/public-space systems until battle support exists.

## PTU/Caelo boundary

The project source set remains the mechanical authority. This pass does not create:
- vehicle speeds;
- train HP;
- collision damage;
- braking distances;
- boarding Skill DCs;
- conductor Features;
- rail-specific Trainer classes;
- ride bonuses;
- passenger limits;
- freight weights;
- chase rules;
- moving-platform rules;
- forced movement from trains;
- electricity or third-rail hazards;
- track Terrain;
- signal-hacking checks;
- railway ownership law;
- fare or ticket law.

The available File Library search did not surface a reliable primary Caelo rule excerpt for trains or vehicle operations in this run. No Caelo-specific rail rule is asserted.

## Internal consistency findings

The existing repository already provides the systems rail should reference rather than duplicate:
- Travel owns general connections, journeys and transport-service abstraction.
- Technology owns technical assets, control systems, maintenance and faults.
- Workplaces owns staffing and shifts.
- Demography owns commuters and temporary presence.
- Urban Public Space owns station forecourts and crowd use.
- Road Ecology owns effects of linear infrastructure on habitat where applicable.
- Freight/Illicit Networks own provenance and diversion of cargo.
- Crisis owns emergency response and recovery.
- Communications owns notices and delivery of service information.
- Accessibility owns passenger access needs.
- Cartography owns maps and route knowledge.

Pass 97 should add rail-specific topology and operational state between those layers rather than reimplement them.

## Candidate design conclusions

1. Keep `rail corridor`, `service`, `train`, `station`, `platform`, `route slot`, `cargo`, `passenger` and `actor knowledge` separate.
2. Model service disruption causally through assets and slots.
3. Treat stations as persistent social/institutional places even when no train is present.
4. Allow a train to become a temporary location without making vehicle physics part of the battle core.
5. Store timetable versions and public notices separately from actual movement state.
6. Support passenger, freight, maintenance and emergency movements as different service purposes.
7. Preserve line history: abandoned platforms, rerouted tracks and former terminals remain world memory.
8. Keep railway wildlife interactions evidence-based and location-specific.
9. Use FULL/REDUCED encounter contracts whenever the intended scene requires moving trains, escort objectives, timed crossings, forced movement or dynamic terrain.
10. Never let Minecraft minecarts or redstone become PTU authority by accident.
