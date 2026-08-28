# Research Scan 100 — Hospitality, Lodging & Guest-Stay Continuity

Status: RESEARCH / PROVENANCE ONLY. This file does not establish Ouros canon or PTU mechanics.
Date: 2026-08-28
Narrative baseline inspected before writing: `74bb82828015eaafb4a93ec683189685ed66822a`.

## Why this pass

The recursive repository inventory and repository search were inspected before writing. Existing layers already cover Travel, Transit Hubs, Commercial Services, Care/Recovery, Community Aid, Crisis, Public Notices, Facility Maintenance, Weather, Winter Refuges and other adjacent systems. No dedicated hotel, inn, lodging, accommodation, guest-stay or hospitality-continuity layer was found.

The missing continuity is operational and social: where a traveler is actually staying, whether a reservation became a stay, what room or facility is usable, which services are available, what changed during the stay, what information staff and guests possess, and what remains true after checkout.

This pass does not assume that Ouros has modern hotels, Pokémon Centers with bedrooms, resorts, inns or hostels everywhere. Those remain canon choices.

## Public Pokémon sources

### Kalos hotels — rotating guests across a regional network

Sources:
- Bulbapedia, Kalos hotels: https://bulbapedia.bulbagarden.net/wiki/Kalos_hotels
- Bulbapedia, Hotel Camphrier: https://bulbapedia.bulbagarden.net/wiki/Hotel_Camphrier
- Bulbapedia, Couriway Hotel: https://bulbapedia.bulbagarden.net/wiki/Couriway_Hotel

Reusable structure:
- the same travelers can recur across several lodging locations;
- their current accommodation can change while their identity and relationship history persist;
- repeated conversations across different hotels can gradually reveal character information;
- guest presence can be tied to time without converting a building into a static NPC container.

Transformation for Ouros:
- persistent guest/traveler IDs survive movement between establishments;
- a stay record references one establishment and one time window instead of rewriting the actor's identity;
- recurring guests can produce social continuity, rumors, favors and callbacks across settlements;
- checkout leaves historical evidence rather than erasing the visit.

Not imported:
- Kalos geography;
- exact six-day/seven-day rotations;
- gifts, O-Powers, NPC identities or room layouts;
- deterministic calendar schedules for all Ouros travelers.

### Cinnabar lodging saturation and fallback

Source:
- Bulbapedia, EP058 “Riddle Me This”: https://bulbapedia.bulbagarden.net/wiki/EP058

Reusable structure:
- a destination can have multiple accommodation providers with finite availability;
- a Pokémon Center and commercial resorts can both be full;
- failure to obtain lodging changes traveler behavior without blocking the region itself;
- an alternative inn can become relevant only after the initial preferred options fail.

Transformation for Ouros:
- `reservation_requested`, `space_available`, `reservation_confirmed`, `checked_in` and `actually_occupied` remain different facts;
- saturation can redirect travelers toward camping, community shelter, another district or another establishment;
- temporary crowding can become a world-state consequence of events, weather or transport disruption.

Not imported:
- Big Riddle Inn, Blaine, Cinnabar's plot or tourism history;
- a universal rule that Pokémon Centers provide overnight rooms;
- exact occupancy or pricing.

### Kalos hotel access interrupted by a crisis

Source:
- Bulbapedia, Geosenge Town / Hotel Marine Snow: https://bulbapedia.bulbagarden.net/wiki/Geosenge_Town

Reusable structure:
- a lodging establishment may physically exist while access is temporarily blocked;
- a crisis elsewhere in the settlement can alter guest access without changing the establishment's identity;
- later reopening should preserve the interruption as history.

Transformation for Ouros:
- building condition, guest-service status, entrance access and room availability are separate fields;
- Crisis/Authority systems may restrict access; Hospitality records the effect on stays and reservations.

Not imported:
- Team Flare, ultimate weapon, exact cause or plot sequencing.

### Pokémon Concierge — guests, staff and individualized service

Sources:
- Bulbapedia, Pokémon Concierge episode “Welcome to the Pokémon Resort!”: https://bulbapedia.bulbagarden.net/wiki/PC04
- Bulbapedia, Watanabe: https://bulbapedia.bulbagarden.net/wiki/Watanabe
- Bulbapedia, “A Pokémon to Help Me!”: https://bulbapedia.bulbagarden.net/wiki/PC05

Reusable structure:
- Pokémon can be guests in their own right rather than inventory attached to a Trainer;
- staff schedules and absences can change service capacity;
- recurring visitors can be recognized across stays;
- staff can provide individualized activities or care without every service becoming a medical mechanic;
- a storm can strand staff away from the property while guests remain present.

Transformation for Ouros:
- guest parties can contain people, Pokémon or mixed groups according to canon and custody rules;
- staffing, guest responsibility and service availability are explicit records;
- a Pokémon guest is never inferred to be owned by another guest merely because they arrived together;
- Care/Recovery owns medical claims; Hospitality owns the stay and service arrangement.

Not imported:
- named characters, specific resort, massages or individual episode plots;
- automatic trust/relaxation bonuses;
- species-based guest behavior.

### Pokémon Paradise Resort — reservation, check-in, care and play remain separate

Source:
- Bulbapedia, SM086 “I Choose Paradise!”: https://bulbapedia.bulbagarden.net/wiki/I_Choose_Paradise%21

Reusable structure:
- a popular resort can require prior reservation;
- a guest can check in before choosing or receiving optional services;
- care facilities, leisure facilities and lodging identity can coexist while remaining distinct operational areas;
- a recurring Pokémon customer demonstrates that guest identity need not be Trainer-centric.

Transformation for Ouros:
- reservation status never proves service completion;
- care or treatment records reference Care/Recovery, not Hospitality mechanics;
- service areas may be partially available while the establishment remains open.

### Hot-spring hotel with an infrastructure failure

Source:
- Bulbapedia, DP063 “Hot Springing a Leak!”: https://bulbapedia.bulbagarden.net/wiki/DP063

Reusable structure:
- a lodging property's signature service can fail while the building and staff remain present;
- investigation of a service outage can connect hospitality to infrastructure and neighboring development;
- restoring a utility can change guest service without being the same event as repairing the building.

Transformation for Ouros:
- a property can be OPEN with selected amenities UNAVAILABLE;
- Infrastructure/Water/Maintenance owns the technical cause and repair;
- Hospitality records guest-facing service consequences and later restoration.

Not imported:
- Team Rocket, Swinub investigation, exact water-diversion plot or battles.

### Old Chateau — apparent lodging is not proof of legitimate hospitality

Source:
- Bulbapedia, Pokémon Generations “The Old Chateau”: https://bulbapedia.bulbagarden.net/wiki/The_Old_Chateau

Reusable structure:
- a traveler can believe they have been offered lodging when the evidence is unreliable;
- appearance, invitation and apparent occupancy can conflict with the actual physical state of a location.

Transformation for Ouros:
- `offer_claim`, `host_identity`, `facility_state`, `guest_belief` and `verified_stay` remain separate;
- supernatural, Psychic, illusion or deception explanations require owner-system evidence and are not inferred by Hospitality.

Not imported:
- ghosts, characters, hallucinations or plot outcome.

## Fan-game source

### Pokémon Rejuvenation — hotel as recurring quest/social space

Source:
- Rejuvenation Wiki, Minccino Event: https://rejuvenation.wiki.gg/wiki/Minccino_Event

Reusable structure:
- guest rooms, lobby and nearby public space can support a quest that changes location several times while remaining anchored to one establishment;
- hotel staff/occupants can provide continuity beyond a single overnight transaction.

Transformation for Ouros:
- lodging establishments can host recurring minor incidents, social scenes and investigations;
- room access does not imply ownership of occupants, Pokémon or property;
- combat, if any, is composed separately by Ouros.

Not imported:
- Minccino, Team Xen, encounter sequence, reward or level data.

## Pokémon tabletop/community sources

### ASOIAI resort adventure — lodging as a persistent operational base

Source:
- Pokémon Tabletop Wiki, ASOIAI Adventure Mechanics: https://pokemontabletop.com/wiki/index.php/Quest:ASOIAI_Adventure_Mechanics

Reusable structure:
- a resort can function as a persistent base between excursions;
- heating/supply state can affect whether normal recovery operations are available;
- repeated daily returns allow the same property to accumulate operational consequences;
- wild Pokémon raids can degrade supplies without making the base itself a battle engine.

Guardrail:
- this is broader Pokémon tabletop design material, not governing PTU 1.05 rules evidence for Ouros;
- its Resort Supply, stamina and Camp Phase mechanics are not imported.

### Fan-design discussion: Pokémon Center upper-floor lounge

Source:
- Reddit r/PokemonRMXP, “The Pokélounge”: https://www.reddit.com/r/PokemonRMXP/comments/1vetx2y/the_pok%C3%A9lounge/

Reusable structure:
- a lodging/rest space can become a low-pressure social node for travelers waiting on other services;
- NPC turnover can produce trades, conversations and side quests without another combat hub.

Transformation for Ouros:
- if a canon facility combines rest, waiting and social functions, each service still has separate ownership and state;
- the idea is retained only as community design evidence.

## PTU 1.05 cross-check

Sources:
- PTU 1.05 Core, Resting / Pokémon Centers excerpt: https://anyflip.com/tcye/paot/basic/251-300
- PTU 1.05 Core, Action Points / Extended Rest context: https://anyflip.com/tcye/paot/basic/201-250

Relevant governing evidence:
- PTU defines rest as a period without rigorous physical or mental activity;
- ordinary rest can restore HP under the governing limits;
- an Extended Rest requires at least four continuous hours and refreshes specific PTU resources/effects;
- Pokémon Centers provide a distinct advanced healing service with their own timing and Injury interaction;
- traveling for extended periods generally does not count as rest.

Critical boundary for Ouros:
- `having a room` does not automatically mean `rest occurred`;
- `checked in for four hours` does not prove an uninterrupted Extended Rest;
- sleeping visuals in Minecraft cannot refresh PTU resources by themselves;
- a hospitality facility is not automatically a Pokémon Center;
- a Pokémon Center does not automatically provide lodging unless setting canon says so;
- Care/AutoPTU must remain the authority for PTU healing/rest consequences where relevant.

## Design lessons extracted

1. A reservation, confirmed booking, check-in, room assignment, physical occupancy, rest and checkout are different events.
2. Guest identity must persist across properties and repeated visits.
3. Guest parties may contain humans and Pokémon without implying ownership relationships.
4. Availability can fail at the establishment, building, room, bed, amenity or service level.
5. A property can remain open while one amenity is unavailable.
6. Staff shortages can reduce service without closing the whole location.
7. Crowding can redirect travel patterns and create social consequences.
8. Recurring guests are useful continuity carriers across settlements.
9. A lodging interruption should leave history after reopening.
10. Guest privacy and access are separate from world omniscience.
11. Apparent hospitality can be disputed evidence rather than verified fact.
12. PTU rest/healing effects must be earned through governing rules, never inferred from a bed block or room timer.
13. Battle outcomes should secure a space or route only; they should not complete check-in, evict guests, transfer property or grant rest.
14. Reduced tactical variants should move uninvolved guests out of the BattleSpec before combat.

## Candidate Ouros boundary

Research-supported candidate only:

`Travel arrival -> reservation/availability -> Hospitality check-in/occupancy -> optional Care/Commercial/Leisure services -> PTU rest only when governing conditions are met -> checkout/departure -> persistent stay history`

Travel owns journeys and destination arrival. Commercial Services owns sales/payment where applicable. Care/Recovery owns treatment. Facility Maintenance owns asset failures/repairs. Crisis owns emergency evacuation/shelter activation. Housing owns permanent residence if such a layer is established. Hospitality would own temporary guest-stay continuity only.

## Canon questions intentionally unresolved

- Which Ouros settlements have hotels, inns, hostels, lodges, guesthouses, campgrounds or resorts?
- Do any Pokémon Centers offer overnight accommodation?
- Can Pokémon independently book or occupy guest accommodation, and under what legal/custody framework?
- How are reservations, prices, deposits, privacy and identification handled?
- Do communities provide free traveler lodging, pilgrimage lodging or emergency beds?
- What kinds of accessibility accommodations exist?
- Which hospitality jobs can individual Pokémon perform when explicitly established?
- Which regions treat camping as ordinary travel practice rather than commercial lodging?

## Mechanical questions intentionally unresolved

- Exact AutoPTU hooks for starting/completing PTU rest outside battle.
- Whether interrupted sleep/rest needs engine event tracking.
- How world time maps to four continuous hours without accidental double counting.
- Whether Pokémon Center healing is represented through a dedicated nonbattle service API.
- Any Trainer Feature, Ability or Item interactions with sleep/rest outside combat.
- Whether a battle interruption invalidates an in-progress Extended Rest and at what exact timestamp.
- Whether beds, tents or shelters have any PTU mechanical effect beyond enabling circumstances for rest.

These remain UNKNOWN until governing PTU/Caelo rules and engine contracts are verified.