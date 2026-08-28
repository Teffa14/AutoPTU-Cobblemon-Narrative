# Railway Operations, Stations & Network Continuity Research Scan — Pass 91

Status: research/provenance only. Not established Ouros canon.
Date: 2026-08-28

## Scope

This pass investigates railways as persistent world infrastructure rather than as a one-scene fast-travel device. The useful design space is the interaction between physical track, service patterns, stations, control information, maintenance, energy dependencies, workers, passenger routines, wildlife overlap, closures, restoration and long-term reuse.

Nothing in this note establishes that Ouros currently has a railway, monorail, subway, maglev or any specific rail technology. Concrete networks remain canon questions.

## Internal duplicate review

The complete recursive tree of `Teffa14/AutoPTU-Cobblemon-Narrative` was inspected at head `ffc05aecf950793cc9c9d20f1b985d7c692a1f3b`; GitHub returned `truncated=false`.

Existing systems already cover important neighboring responsibilities:

- `design/travel-transport-expedition-layer.md` owns connection graphs, journeys, transport services, service disruptions and route restoration. It already lists `RAIL_OR_TRANSIT if canon supports it` as a possible connection type.
- `design/transit-hubs-passenger-cohorts-extension.md` owns temporary passenger communities and in-transit scenes.
- `design/technology-energy-infrastructure-layer.md` owns technical assets, energy/control networks, faults and operators.
- `design/facility-maintenance-repair-inspection-extension.md` owns condition, work orders, repair and reopening evidence.
- `design/infrastructure-outage-restoration-extension.md` owns multi-service outage cascades and restoration sequencing.
- `design/public-notices-signage-world-information-extension.md` owns passenger-facing notices and physical information surfaces.
- `design/interregional-mobility-recognition-layer.md` explicitly avoids inventing passports, visas, customs or sovereign-border mechanics.
- `design/cobblemon-runtime-authority-boundary.md` fixes AutoPTU as tactical authority.

No existing file owns rail-specific persistent operational topology: track sections, junctions, service patterns, station/line revision history, turnbacks, partial operation, decommissioned alignments or the difference between control indications and physical rail truth.

## Sources and transformed design lessons

### Magnet Train — Pokémon Gold/Silver/Crystal and HeartGold/SoulSilver

Source: Bulbapedia, “Magnet Train”
https://bulbapedia.bulbagarden.net/wiki/Magnet_Train

Useful structure:
- a major intercity rail service exists independently from the player;
- service can remain unavailable because an upstream energy dependency is unresolved;
- physical line, power availability and passenger access are separate facts;
- a pass controls access after operation resumes;
- construction and station placement can leave long-term urban consequences.

Transformation for Ouros:
A rail service should consume explicit dependency state from Technology/Infrastructure rather than treating `track exists` as equivalent to `train runs`. Access credentials, payment, route viability and operating state remain separate records.

Do not copy:
- Kanto/Johto geography;
- 550 km/h specification;
- Machine Part quest;
- Copycat or named characters;
- the exact Pass system.

### Magnet Train in Pokémon Adventures

Source: Bulbapedia, “Magnet Train” and “The Last Battle IX”
https://bulbapedia.bulbagarden.net/wiki/Magnet_Train
https://bulbapedia.bulbagarden.net/wiki/PS175

Useful structure:
A railway can become a moving story location whose operational failure matters independently from combat happening onboard. The train itself, its route and stopping problem remain world-state concerns while battles can occur inside it.

Transformation for Ouros:
A moving train may contain a tactical encounter, but vehicle speed, braking, collision and route control cannot be improvised as battle mechanics. The train can be stopped or isolated in world state before a reduced encounter until moving-platform and hazard rules are verified.

### “Frozen on Their Tracks!” — Pokémon the Series: Diamond and Pearl

Source: Bulbapedia episode summary
https://bulbapedia.bulbagarden.net/wiki/DP130

Useful structure:
- an unexpected signal can halt an otherwise routine service;
- crew investigate operational state instead of assuming sabotage;
- working Pokémon can have visible transport roles;
- the incident is meaningful because a normal operating baseline existed first.

Transformation for Ouros:
Signal indications should be records/observations with provenance. A red signal may correctly represent a protected section, a fault, stale state or another cause. Working Pokémon remain individual actors with validated role assignments through Pokémon Work; species or Type never grants automatic rail capability.

### Battle Subway control incidents — Pokémon the Series: Black & White

Sources: Bulbapedia, “Crisis from the Underground Up!” and “Battle for the Underground!”
https://bulbapedia.bulbagarden.net/wiki/BW047
https://bulbapedia.bulbagarden.net/wiki/BW048

Useful structure:
Operational displays can become unreliable. Apparent train positions or sensor contacts can differ from physical reality, creating an investigation that depends on reconciling control data with direct observation.

Transformation for Ouros:
A control-board contact is an `operational_indication`, not canonical proof that a physical train occupies a section. Telemetry, staff reports, platform observations and direct inspection may disagree without forcing a supernatural explanation.

### “A Trip Down Memory Train!” — Pokémon the Series: Black & White

Source: Bulbapedia
https://bulbapedia.bulbagarden.net/wiki/BW140

Useful structure:
Old stations, unused lines, switches and rolling stock can survive after normal service ends. Infrastructure can acquire historical, social or ecological meaning before demolition or reuse.

Transformation for Ouros:
Decommissioned railway state remains persistent. An old cutting can become habitat; a platform can become a public-space or heritage site; a junction can remain a maintenance access route; eventual reopening must reconcile the new uses rather than erase them.

### Coumarine City monorail

Source: Bulbapedia, “Coumarine City”
https://bulbapedia.bulbagarden.net/wiki/Coumarine_City

Useful structure:
Rail transit can shape the internal geography of one settlement by connecting physically separated districts rather than only linking regions.

Transformation for Ouros:
A railway layer must support urban feeder/shuttle services, not only long-distance lines. A station can be a real local dependency for access to jobs, clinics, markets or public space without becoming a border checkpoint.

### Galar rail network

Sources: Bulbapedia railway/location material
https://bulbapedia.bulbagarden.net/wiki/Galar
https://bulbapedia.bulbagarden.net/wiki/White_Hill_Station

Useful structure:
Stations can combine transport, retail and route choice; later world expansion can add additional stations and track to a previously known network.

Transformation for Ouros:
Network topology needs revision history. A new branch or restored stop should update Travel connectivity and service patterns while preserving earlier maps, notices and memories as historically correct for their dates.

### Pokémon Reborn — Underground Train System / Railnet Reconstruction

Sources: Pokémon Reborn Wiki
https://pokemon-reborn.fandom.com/wiki/Underground_Train_System
https://pokemon-reborn.fandom.com/wiki/Railnet_Reconstruction_Project

Classification: fan-game structural inspiration only.

Useful structure:
A damaged rail system can be restored through a longer project and materially alter access across an existing city after completion.

Transformation for Ouros:
Rail restoration should generate staged handoffs: public-works decision, procurement, physical repair, technical testing, station readiness, service commissioning, passenger information and later effects on traffic/ecology/economy. “Project funded” does not instantly mean “service operating.”

Do not copy project prices, items, NPCs, maps or quest sequence.

### “Off The Rails!” — community PTU adventure

Source: r/PokemonTabletop public post
https://www.reddit.com/r/PokemonTabletop/comments/1e08i69

Classification: PTU community narrative inspiration, not rules authority.

Useful structure:
A derailment can become a repair/logistics/exploration shell rather than a compulsory combat gauntlet. Missing parts, local Pokémon and alternate solutions can sustain play while the vehicle remains a persistent objective.

Transformation for Ouros:
A rail incident can branch into inspection, recovery, negotiation, ecology, procurement or ordinary battle depending on current state. No generic “derailment damage,” repair DC, spare-parts table or species behavior is imported.

### Pokémon Tabletop campaign feature — two trains as scenario framing

Source: Pokémon Tabletop RPG campaign-features archive
https://pokemontabletop.com/category/campaign-features/

Classification: community campaign inspiration.

Useful structure:
A train can create an immediate bounded cast and force unfamiliar groups to share a survival/problem-solving context. The transferable lesson is the temporary-community pressure of a stranded vehicle, already compatible with Transit Hubs.

No historical-war setting, characters, factions or anomaly plot is imported.

## PTU/Caelo mechanical boundary

No governing PTU/Caelo evidence inspected in this pass justifies inventing:

- train-driving or signalling Skill DCs;
- vehicle speed, braking distance or capacity math;
- derailment/collision damage;
- moving-platform movement rules;
- boarding/disembarking actions in combat;
- train-car object HP;
- powered-rail hazards;
- generic electricity damage from rail assets;
- discounts, fares or pass prices;
- Pokémon-powered traction outputs;
- repair bonuses from job title or species;
- custom conductor/engineer Features.

PTR2/PTR material surfaced in web search is not the governing PTU/Caelo rules source for Ouros and is not used to establish mechanics.

## Design conclusions

1. Rail physical topology and service operation need separate persistent state.
2. Power/control dependencies should be consumed from Technology rather than duplicated.
3. A control indication is evidence, not physical truth.
4. Partial operation is more interesting than a binary open/closed flag: short-turning, single-section suspension, turnback, shuttle operation and station bypass can preserve world activity.
5. Network revisions need history so old maps, passenger memories and signage can remain temporally correct.
6. Stations should remain real locations with non-transport functions, but their shops, queues, notices and social scenes stay owned by existing systems.
7. Decommissioned infrastructure can become habitat, heritage, public space or service access; later reopening must acknowledge those accumulated uses.
8. Train incidents should generate inspection, logistics, ecological and social choices before defaulting to combat.
9. Working Pokémon require individual role evidence and never become transport machinery or battle participants by proximity.
10. A moving train must never force Minecraft/Cobblemon to become a second physics or PTU battle engine.

## Canon status

Everything above is research or proposed design guidance. Pass 91 establishes no railway, operator, station, fare system, technology, pass, working Pokémon practice or rail history in Ouros.