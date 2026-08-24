# Road Passenger Transit, Taxis & Shuttles — Research Scan 140

Status: RESEARCH / PROVENANCE ONLY. Not canon.
Date: 2026-08-23

## Research question

What reusable structures can Ouros borrow from Pokémon, PTU-adjacent play and real transit operations to make buses, taxis, shuttles and road-based passenger services persistent world systems rather than generic fast-travel buttons?

This pass was selected after inspecting the existing narrative inventory. `travel-transport-expedition-layer.md` already owns generic connections and `PUBLIC_TRANSPORT`, while Rail, Maritime and Airspace have dedicated operational layers. No dedicated road-passenger-transit layer existed.

## Pokémon references

### Lumi Cab — Lumiose City

Source: Bulbapedia, `Lumi Cab`.
https://bulbapedia.bulbagarden.net/wiki/Lumi_Cab

Reusable structure:

- a named urban transport service can become part of city identity;
- destinations are organized spatially rather than represented as an abstract teleport list;
- service availability can depend on infrastructure state;
- fare, access and service operation are separate concerns.

Important non-transfer:

The X/Y fare formula, style discount and unpaid-fare battle are game-specific. Ouros should not import those prices or make debt automatically trigger combat.

### Gogoat Shuttle — Lumiose City

Source: Bulbapedia, Lumiose City transportation section.
https://bulbapedia.bulbagarden.net/wiki/Lumiose_City

Reusable structure:

- a Pokémon-assisted passenger service can have fixed stops and a limited corridor;
- a flat-fare shuttle and point-to-point taxi can coexist inside the same city;
- the Pokémon carrying passengers is part of an operated service rather than automatically owned by each rider;
- stop placement creates a legible urban movement network.

Important non-transfer:

Do not infer Gogoat carrying capacity, work hours, Mountable legality, speed, obedience or passenger safety from the game abstraction. Any Ouros service involving working Pokémon must pass through Pokémon Agency and Working Pokémon institutional-role state.

### Lumiose as a transport-rich city

Source: Pokémon.com, `Illuminating Lumiose City`, published 2025-10-09.
https://www.pokemon.com/us/features/illuminating-lumiose-city

Reusable structure:

A large Pokémon city can support several movement layers simultaneously: walking, urban road services, rail and other infrastructure. Transport can therefore help define district identity and daily routine instead of existing only as a menu function.

## Fan-game / community design reference

### Pokémon Burning Scales

Source: public GitHub repository description.
https://github.com/Benitex/Pokemon-Burning-Scales

The project deliberately focuses on a compact open world around major cities and fills that smaller geography with sidequests and repeat interactions.

Reusable lesson:

A dense urban region benefits from repeatable infrastructure and routine services because the player revisits the same streets many times. A bus stop, taxi rank or shuttle route can accumulate history across many unrelated stories.

No plot, characters or quest text are reused.

## Transit operations references

### Service reliability and headways

Source: U.S. Federal Transit Administration, Metro Rapid service-quality evaluation.
https://www.transit.dot.gov/research-innovation/metro-rapid-demonstration-program-evaluation-report-appendix-b-service-quality

Reusable abstractions:

- scheduled service and delivered service are different;
- headway is the time gap between successive vehicles;
- bunching can produce long waits and uneven passenger loading even when the nominal schedule has enough trips;
- crowding can itself increase delay and reinforce unreliability.

Ouros should therefore avoid a single `bus_running=true` flag. A route may be operating while service quality is degraded.

### Schedule-based versus headway-based control

Source: FTA, `Characteristics of Bus Rapid Transit for Decision-Making`.
https://www.transit.dot.gov/sites/fta.dot.gov/files/CBRT_2009_Update_0.pdf

Reusable abstraction:

Low-frequency services may be managed around scheduled arrival times, while high-frequency services may be managed around spacing between vehicles. This supports two distinct types of passenger expectation in Ouros without importing any real-world threshold.

### Demand-responsive service

Source: FTA, `What Are the Requirements for Demand-Responsive Service?`
https://www.transit.dot.gov/what-are-requirements-demand-responsive-service

Reusable abstraction only:

Demand-responsive transport differs from fixed-route service because trip requests, response time, service area, hours and capacity all matter. This is useful for rural shuttles, accessible transport, emergency replacement services or low-demand settlement links.

Do not import U.S. disability law or regulatory standards. Ouros Accessibility remains the governing narrative layer for accommodations.

## Design conclusions for Ouros

1. Physical road state and passenger-service state remain separate.
2. Route topology, stops, schedules/headways, vehicle assignments and passenger demand require persistent state when narratively relevant.
3. A service can be OPERATING while degraded by bunching, pass-ups, crowding, missing vehicles, staff shortage or detours.
4. A taxi can be demand-responsive while a shuttle follows a fixed corridor; both can use the same roads.
5. Passenger information is its own state. A service can be rerouted before every traveler learns about the change.
6. Transfers matter. Missing a connection can be a meaningful consequence without creating combat.
7. Accessibility is actor- and stop-specific; a route being generally accessible does not prove every boarding point currently works for every traveler.
8. Working Pokémon in transit services keep individual identity, agency, workload and availability state.
9. Vehicle or Pokémon presence in Minecraft never proves a service is authorized, available or on schedule.
10. Routine transit should compress. Expand only when delay, access, crowding, route change, social contact, investigation or consequence creates a meaningful decision.

## PTU/Caelo boundary

No road-transit mechanic was assumed from PTU flavor or general Pokémon canon.

This pass does not invent:

- vehicle speeds;
- collision damage;
- boarding checks;
- passenger capacity formulas;
- driving Skills;
- Mountable carrying rules;
- fatigue;
- road terrain effects;
- pursuit rules;
- traffic initiative;
- transport combat modifiers.

The full Caelo corpus and Super PTU Online Helper were not available as reliable invocable sources in this runtime. Any later mechanic must be checked against the project source set before canon or implementation.