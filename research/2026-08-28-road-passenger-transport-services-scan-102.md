# Road Passenger Transport Services Research — Pass 102

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file establishes Ouros canon.
Date: 2026-08-28

## Scope

The complete recursive Narrative repository inventory was inspected at baseline `7b5dd013657dd3b2983db1ac84f8693bbdf05686`; GitHub reported `truncated=false`. Relevant existing layers were then reviewed directly.

Travel already owns generic transport services, journeys and connection viability. Roads/Bridges owns road access. Transit Hubs owns passenger cohorts and temporary co-presence. Railway, aviation and port passes specialize their own operational modes. No dedicated road-passenger-service continuity layer exists for taxis, buses, shuttles, hired rides or Pokémon-operated public road services.

This pass fills that narrow gap. It does not create vehicle physics, traffic simulation, ticket law, fares, driver licensing or PTU mount rules.

## Public Pokémon sources

### Lumiose City — Lumi Cab and Gogoat Shuttle

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Lumiose_City
- https://bulbapedia.bulbagarden.net/wiki/Lumi_Cab
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_as_transport

Reusable structures:
- one city supports two distinct passenger-service grammars at the same time;
- Lumi Cab provides point-to-point service to named destinations;
- Gogoat Shuttle follows a bounded corridor with ordered stops and passenger-selected alighting;
- service availability can depend on external infrastructure: Lumi Cab is unavailable during Lumiose's blackout in X/Y;
- a Pokémon-powered service can have its own operating pattern without granting the passenger direct control of the Pokémon;
- in Legends: Z-A, the older Gogoat service has ceased because changed urban/wild-Pokémon conditions make operation unsuitable, while an actor is attempting to restore it.

Transformation for Ouros:
Road passenger service must preserve service pattern, stop set, dispatch/availability state and dependencies separately from the physical road. A road can remain OPEN while one service is SUSPENDED. A Pokémon-assisted public service can exist without transferring ownership or tactical control of the exact Pokémon to passengers.

Rejected:
- Kalos names, prices, style discounts and destination lists;
- battle-for-nonpayment behavior;
- any assumption that Gogoat specifically operates Ouros transit;
- any automatic species-to-job mapping.

### Exeggutor Express and Mount Hokulani

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Alola_Route_10
- https://bulbapedia.bulbagarden.net/wiki/Mount_Hokulani
- https://bulbapedia.bulbagarden.net/wiki/Transportation_in_the_Pok%C3%A9mon_world

Reusable structures:
- a road segment can terminate at a public service that completes access to a difficult destination;
- the bus stop is a persistent access point rather than a generic fast-travel menu;
- disruption at the stop changes practical connectivity even though the lower road still exists;
- a service can be routine enough to compress after first use.

Transformation for Ouros:
A service may be necessary for a particular connection while leaving the underlying route graph explicit. Travel decides whether the journey is viable; Road Passenger Operations supplies the current service facts.

Rejected:
- Mount Hokulani geography, characters, criminal event and fixed bus design;
- any universal rule that mountain access requires buses.

### Pokémon Rejuvenation — Truck connections

Sources:
- https://rejuvenation.wiki.gg/wiki/East_Gearen_City
- https://rejuvenation.wiki.gg/wiki/Neo_East_Gearen_City
- https://rejuvenation.wiki.gg/wiki/Hiyoshi_City
- https://rejuvenation.wiki.gg/wiki/Hiyoshi_Pass

Reusable structures:
- a comparatively informal road carrier can coexist with formal rail and other links;
- the same transport relationship can survive a city's restoration and changed surrounding state;
- small settlements and passes can participate in a road-service network without needing a major terminal.

Transformation for Ouros:
Road services can range from formal scheduled lines to limited local operators. The data model should not assume every service has a station building or high-capacity vehicle.

Rejected:
- named locations, NPCs, exact destinations, plot progression and fan-game rules.

### PTU community scene — Dragonite buses at Horizon Academy

Source:
- https://www.tapatalk.com/groups/pokemon_tabletop/schoolwide-event-opening-ceremonies-t6518.html

Reusable structure:
A PTU community scene uses multiple Pokémon-associated buses to establish collective arrival, temporary crowd pressure and institutional scheduling in one image. The useful lesson is social/logistical: transport can deliver cohorts and make a place temporarily busy.

This is not governing PTU 1.05 evidence. It does not prove vehicle capacity, Dragonite labor rules, driving checks or combat rules.

## PTU 1.05 / Caelo boundary

Public PTU resources confirm the current 1.05 corpus remains the governing rules source, while prior Ouros research already extracted the relevant movement boundary: individual Pokémon movement and mounted transport depend on explicit capabilities and the exact individual; species/type alone is insufficient.

Nothing inspected establishes a universal PTU subsystem for:
- taxis or buses;
- road vehicle speed/capacity;
- driving or dispatch checks;
- traffic initiative;
- braking, collision or crash damage;
- boarding as a battle action;
- fare enforcement;
- passenger injury from vehicle motion;
- mechanical bonuses for professional drivers;
- public Pokémon transit eligibility by species.

Caelo-specific transport rules remain UNKNOWN unless direct project evidence establishes them.

## Design lessons

The durable state is not “fast travel unlocked.” It is a chain of facts:

service exists → a service pattern is published → an individual run/dispatch is expected → a pickup becomes available → passengers board → the run departs → stops are served or skipped → passengers alight → the run closes.

Each transition can diverge from the plan. A road may be open while the operator lacks staff. A vehicle may be present while boarding is suspended. A published stop can be temporarily skipped. A passenger may miss one run without the route itself disappearing.

Transport information and transport truth also need separation. A sign, timetable, dispatcher statement and observed vehicle are evidence about a service; none alone proves departure or arrival.

## Cobblemon/Minecraft implications

Safe reuse candidates include roads, stops, shelters, signs, vehicles as presentation assets where available, Pokémon overworld entities/models/forms/poses/animations/cries, UI, sounds, particles, networking, entity tracking and persistence hooks.

Adapter review is required for stable service/run/stop identity, authoritative boarding intent, projecting cancellations/reroutes into signs/barriers, passenger abstraction, and converting any combat location into an explicit AutoPTU arena.

Minecraft movement never proves a completed trip. A visible Pokémon at a stop never becomes a transit worker or combatant automatically. Cobblemon/Minecraft battle-state/controller logic never selects combatants or resolves PTU consequences.

## Originality and canon boundary

All outputs from Pass 102 remain proposed. No source service, operator, route, character, fare, vehicle design, fan-game location or community-campaign institution is imported into Ouros. Only reusable operational structures are retained.