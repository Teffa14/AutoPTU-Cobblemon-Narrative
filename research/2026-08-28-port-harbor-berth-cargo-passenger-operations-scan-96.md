# Ouros Research — Port, Harbor, Berth, Cargo & Passenger Operations — Pass 96

Status: RESEARCH ONLY. This file is provenance and design evidence. It does not establish Ouros canon.
Date: 2026-08-28

## Purpose

Pass 34 established maritime regions, harbors, sea lanes, vessels, submerged locations, tides, salvage and marine habitats. Later passes added fisheries, lighthouses/navigation aids, courier logistics, transit cohorts, batch traceability, public notices, maintenance and transport operations. The remaining gap is narrower: what happens operationally at the waterfront when a specific vessel call uses a specific berth and people, cargo, information and services must actually transfer.

This pass therefore researches port-call continuity, berth identity, partial harbor operation, embarkation/disembarkation, cargo handoff, manifest discrepancies, missed connections, temporary holds and the persistent consequences of changing how a waterfront works.

No source below is imported as Ouros canon. Names, characters, exact plots, proprietary mechanics and distinctive dialogue remain external.

## Existing internal boundary

The current repository already assigns authority as follows:

- Maritime owns harbors, sea lanes, vessels and maritime environmental context.
- Travel owns routes, journey state, schedules and transport-service operation.
- Transit Hubs owns temporary passenger co-presence and scene expansion.
- Courier owns shipment identity, custody transfers and physical delivery legs.
- Material Culture owns item identity and provenance.
- Batch Traceability owns post-distribution trace/hold/correction state.
- Facility Maintenance owns inspection, repair and technical verification.
- Public Notices owns physical projection of authoritative information.
- Workplaces owns staffing and professions.
- Crisis owns emergency state and recovery.
- AutoPTU owns tactical legality and outcomes.

A port-operations layer must coordinate those systems rather than become a second copy of them.

## Public sources inspected

### Pokémon Black/White — Castelia City ocean piers

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Ocean_Piers
- https://bulbapedia.bulbagarden.net/wiki/Castelia_City

Castelia's waterfront contains multiple distinct piers. Different piers host different vessels and destinations. A cruise vessel uses a dedicated dock; other ferries use their own points; some vessel appearances are temporary.

Reusable design lessons:

- a harbor is not one homogeneous interaction node;
- berth/pier identity can matter even when every pier belongs to the same city;
- service destination, access requirement and vessel presence can vary independently by berth;
- a vessel's departure should leave a historical call record rather than erasing its prior presence;
- waterfront geography can support both routine transport and unusual one-off calls.

Do not import Castelia's pier names, exact destinations, event gating, Team Plasma material or Royal Unova content.

### Liberty Pass / Liberty Pier

Source:
- https://bulbapedia.bulbagarden.net/wiki/Liberty_Pass

The Liberty Pass demonstrates a clean separation between vessel availability and passenger authorization: the boat may physically exist at the pier while a particular traveler cannot use the service until a required credential is recognized.

Reusable design lesson:

- `vessel present`, `service operational`, `traveler authorized`, `boarding completed` and `journey departed` are separate facts;
- a credential should point to the existing credentials/authorization system rather than become a hard-coded harbor flag.

The event-exclusive item and its game-specific distribution are not imported.

### Pokémon Diamond/Pearl/Platinum and animation — Canalave Harbor

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Canalave_City
- https://bulbapedia.bulbagarden.net/wiki/Harbor_Inn

Canalave uses a harbor as an access point to several distinct destinations. Animation material also presents canals, bridges and a large harbor interacting spatially with boat traffic.

Reusable design lessons:

- a harbor can support several destination services through one waterfront while preserving service-level identity;
- an urban crossing can interact with water traffic without making either transport network subordinate to the other;
- port operations can be embedded in normal city geography instead of existing as an isolated dungeon zone.

Do not import Canalave's characters, island plots, legendary events or exact bridge technology.

### Pokémon Ranger: Shadows of Almia — cargo ship and hidden harbor

Sources:
- https://pokemon.fandom.com/wiki/Cargo_Ship
- https://pokemon.fandom.com/wiki/Pok%C3%A9mon_Ranger%3A_Shadows_of_Almia

The game uses a vessel built for ordinary cargo in a context where its actual load and purpose differ from what the generic asset type would imply. The ship is loaded at a harbor, departs, and then becomes a navigable location.

Reusable design lessons:

- `asset type` does not prove current cargo or mission;
- loading activity, declared manifest, observed load and actual custody can disagree;
- a port investigation can begin with discrepancies during transfer rather than requiring omniscient knowledge of hidden contents;
- a vessel can transition from docked location to mobile scene while preserving the same asset identity.

The kidnapping plot, villain group, exact ship layout, captured Pokémon scenario and ship-sinking device are not imported.

### Public PTU module collection — White Harbor Spring Festival

Sources:
- https://www.tapatalk.com/groups/pokemon_tabletop/mini-module-collection-t7231.html
- https://www.reddit.com/r/lfg/comments/v2suxf

A public PTU mini-module collection and recruitment post use White Harbor as a recurring civic location for a spring festival with vendors, competitions, visitors and security concerns.

Reusable design lessons:

- a working harbor can become a civic event venue without stopping being transport infrastructure;
- seasonal visitor pressure can interact with normal service capacity;
- harbor scenes can support shopping, fishing, competitions, observation and investigation before any battle appears;
- a festival or crowd should be represented as temporary operating pressure rather than permanently changing the identity of the port.

No White Harbor setting details, criminal plot, event lineup, NPCs or encounters are imported.

### Pokémon Rejuvenation — distributed boat connections

Sources:
- https://rejuvenation.wiki.gg/wiki/Akuwa_Town
- https://rejuvenation.wiki.gg/wiki/Kristiline_Town

These public location pages show settlements connected by boat to several other destinations. The useful structural point is the network role: a small marine settlement can have multiple waterborne connections without becoming a large metropolitan port.

Reusable design lessons:

- port scale and network importance are separate variables;
- one settlement can have several boat service links with different destinations;
- port operations should work for a small pier, ferry landing or major harbor using the same identity principles.

No Rejuvenation story, characters, maps, field effects or custom mechanics are imported.

### Pokémon Reborn — Coral Ward waterfront decline

Source:
- https://pokemon-reborn.fandom.com/wiki/Coral_Ward

Coral Ward is described as a formerly prosperous fishing area whose waterfront declined as environmental conditions worsened.

Reusable design lessons:

- waterfront economic use can change as upstream ecological state changes;
- docks and warehouses can remain physically present after their original traffic declines;
- later reuse should inherit the old waterfront's history instead of spawning a clean replacement district.

The Reborn location, plot, characters and Misty Terrain implementation are not imported.

### Pokémon Uranium — ferry credential and recurring route convenience

Sources:
- https://pokemon-uranium.fandom.com/wiki/Ferry_Pass
- https://pokemon-uranium.fandom.com/wiki/Tandor_Luxury_Cruise

The useful structural material is the separation between a transport credential, recurring ferry access and an individual voyage that can become a social scene.

Reusable design lessons:

- recurring transport privileges should reference a credential/access system;
- a vessel can host a temporary passenger community while still belonging to a larger scheduled network;
- route convenience, passenger scene content and shipboard disruption are separate layers.

No Uranium locations, plot incidents, rewards or ship layout are imported.

## PTU / Caelo cross-check

Internal source inventory confirms the governing PTU/Caelo material available to the project includes the PTU Core Rulebook, Caelo Player's Guide, Caelo location/encounter material, character creation material, errata/extra material and Pokédex sources.

Current established evidence supports movement capabilities such as Swim and ordinary tactical movement. It does not establish a universal port-operations ruleset.

Pass 96 therefore does not invent:

- vessel speed or acceleration;
- docking checks;
- pilotage rules;
- tugboat rules;
- berth capacity math;
- crane statistics;
- cargo weight/load physics;
- customs or immigration law;
- universal passenger manifests;
- maritime licensing;
- ship HP or collision damage;
- gangway balance checks;
- fall/drowning damage;
- tides/currents as tactical modifiers;
- species/type-based authority to operate machinery;
- automatic Pokémon carrying capacity.

Any future use of those concepts requires exact PTU/Caelo/canon evidence and, when tactical, engine support.

## Structural findings for Ouros

### 1. Harbor identity and berth identity must coexist

A harbor can be open while one berth is occupied, restricted, damaged, under inspection, reserved or unavailable for a specific class of call.

The correct model is not `harbor_open = true/false` for every waterfront event.

### 2. A port call is an exact historical event

A vessel call should preserve:

- vessel identity;
- planned and actual arrival/departure windows;
- assigned and actual berth;
- service purpose;
- linked passenger journey refs;
- linked shipment/cargo refs;
- linked service/support refs;
- notices and exceptions;
- verification events.

A vessel leaving does not delete the call.

### 3. Presence, authorization, boarding and departure differ

A traveler can reach the terminal but fail authorization. A credential can be valid while the sailing is cancelled. A ship can be present while boarding is paused. Boarding can complete before actual departure.

Those states should remain independently inspectable.

### 4. Manifest is a claim, not omniscience

A cargo or passenger manifest can be:

- correct;
- incomplete;
- superseded;
- copied from an earlier plan;
- mismatched to actual transfer;
- disputed;
- unavailable;
- private/restricted according to future canon.

Physical observation and custody records remain separate evidence.

### 5. Loading/discharge is a sequence of handoffs

Port operations should reference existing shipment, custody, batch and item identities. The port layer records the operational transfer episode; it does not create a second cargo object.

Arrival at the harbor is not delivery to the final recipient.

### 6. Partial operation creates better stories than binary closure

Useful states include:

- passenger service active while cargo berth is closed;
- one ferry route suspended while another runs;
- vessel waiting offshore/elsewhere because a berth is unavailable;
- unloading complete while onward courier transfer is delayed;
- terminal open while gangway/boarding remains paused;
- harbor accessible while navigation-aid or weather restrictions affect particular calls.

### 7. Congestion should be derived from real state

Operational pressure can come from overlapping calls, delayed departures, unavailable berths, event crowds, maintenance or route disruptions. It should not be generated as random flavor if no world-state cause exists.

### 8. Old waterfront uses should persist

A berth, warehouse or ferry landing can become disused, repurposed, heritage space, habitat edge, market space or emergency landing after traffic changes. A future reopening must account for those intervening uses.

### 9. Pokémon work must remain explicit

A Pokémon seen on a dock is not automatically cargo, worker, tug substitute, security asset or combatant. Any work role must use the Pokémon Work layer and exact approved capability/role evidence.

## Narrative opportunities

High-value patterns include:

- a vessel assigned to one berth appears at another for a mundane operational reason;
- three documents describe two actual loads because one plan was superseded;
- cargo has arrived but custody has not transferred to the recipient;
- a passenger service resumes before a damaged cargo facility;
- a temporary festival berth becomes familiar and later politically/economically important;
- an old warehouse still shapes modern routing after its original trade vanished;
- a missing vessel report is actually a service-code or timetable mismatch;
- ecology changes which parts of a waterfront are used without proving a causal story by observation alone.

## Copyright and provenance rule

This pass stores source identification and high-level design lessons only. It does not reproduce protected dialogue, plot text, maps, dungeon layouts, characters or proprietary mechanics.

## Research directions left open

- exact PTU/Caelo treatment of Swim, Mounting, carrying and falling near water;
- public PTU sea-voyage logs with detailed encounter resolution rather than pitches;
- exact Cobblemon/Fabric APIs suitable for vessel/terminal presentation and stable world identifiers;
- whether Ouros canon has formal port authorities, pilotage, customs, manifests, passenger registers or cargo inspections;
- which regions have major ports, small ferry landings, fishing harbors or no formal maritime infrastructure.