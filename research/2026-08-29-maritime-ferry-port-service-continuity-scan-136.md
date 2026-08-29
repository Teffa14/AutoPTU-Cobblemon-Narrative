# Ouros Narrative Research — Maritime Ferry, Port & Passenger-Service Continuity — Pass 136

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is automatically Ouros canon.
Date: 2026-08-29

## Scope

This pass follows the repository-wide inventory and targeted searches for `ship`, `maritime`, `ferry`, `harbor`, `boarding`, `terminal` and related concepts. Existing Travel/Transport already recognizes WATERWAY and SEA_LANE connections, public transport, service disruptions, harbors and ferry examples. Aviation, rail/urban transport, roads, ropeways, courier/logistics, crisis/rescue, weather, coastal navigation aids and construction have dedicated continuity layers. The missing surface is ordinary passenger-vessel service from terminal state through boarding, departure, intermediate stops, arrival, disembarkation, rerouting and recovery.

This pass therefore does not create generic ocean navigation, naval combat, sailing physics, ship HP, drowning mechanics, weather rules or ownership law. It creates evidence for a future Ouros continuity owner that can hand those questions to the systems that already own them.

## Existing internal boundary

`design/travel-transport-expedition-layer.md` already establishes several rules that this pass preserves:

- physical route state and service state are separate;
- public transport is a world service rather than universal fast travel;
- a harbor may be a staging site;
- SEA_LANE and WATERWAY are descriptive connections, not mechanics;
- service disruption should create choices instead of arbitrary waiting;
- route ecology and transport operations may affect one another;
- exact carrying capacity, vehicle rules, hazard effects and movement legality remain external.

The new work must specialize that framework without taking ownership away from Travel, Weather, Crisis/Rescue, Coastal Navigation Aids, Maintenance, Construction, Cargo/Material Culture or Pokémon Agency.

## Source 1 — Seagallop ferries

Source:
https://bulbapedia.bulbagarden.net/wiki/Seagallop_Ferry

Relevant high-level structure:

The Sevii Islands are connected by a family of ferries rather than one universal vessel. Different services connect different island groups and mainland Kanto. Access depends on a pass that identifies which destinations are currently available to the traveler. The fiction therefore distinguishes network topology, individual service/vessel identity and passenger authorization.

Reusable Ouros lesson:

A maritime network should preserve at least four independent facts: the sea connection exists, a service serves it, a particular sailing is planned or operating, and a specific traveler is authorized or booked when local canon requires that distinction.

Do not import the Tri-Pass, Rainbow Pass, named vessels, progression gates, routes or event-ticket structure.

Useful transformed invariants:

`ROUTE_EXISTS != SERVICE_OPERATING`

`SERVICE_OPERATING != THIS_SAILING_DEPARTED`

`PASS_OR_BOOKING_VALID != PASSENGER_BOARDED`

`VESSEL_ASSIGNED != VESSEL_DEPARTED`

## Source 2 — S.S. Aqua

Sources:
https://bulbapedia.bulbagarden.net/wiki/S.S._Aqua
https://www.serebii.net/pokearth/johto/ssaqua.shtml

Relevant high-level structure:

The S.S. Aqua connects two distant regions and operates on recurring days. The vessel is also a temporary playable location with cabins, crew and passengers rather than a pure loading screen.

Reusable Ouros lesson:

A repeated sailing can be both transportation and a persistent social location. The schedule can matter without forcing every crossing into a full scene. Routine sailings should compress, while sailings with a relevant passenger, disruption, investigation, ecological observation, delivery or time-sensitive event can expand.

Do not import the exact weekly timetable, ticket requirements, rewards or onboard Trainer placements.

## Source 3 — S.S. Tidal

Source:
https://bulbapedia.bulbagarden.net/wiki/S.S._Tidal

Relevant high-level structure:

The S.S. Tidal serves more than one destination depending on access state, and the voyage contains cabins and optional battles. Arrival is a distinct transition from the onboard period.

Reusable Ouros lesson:

The vessel location should be modeled explicitly during meaningful journeys. `AT_TERMINAL`, `BOARDED`, `UNDERWAY`, `AT_INTERMEDIATE_STOP`, `ARRIVED_AT_BERTH` and `DISEMBARKED` are useful separate narrative phases even when the UI compresses several of them.

A battle aboard a vessel must never silently decide whether the vessel arrived, whether a passenger disembarked or whether cargo/records transferred unless those transitions are authored separately.

## Source 4 — Pokémon Unbound S.S. Marine

Sources:
https://unboundwiki.com/items/key-items/ss-ticket/
https://unboundwiki.com/locations/ss-marine/
https://unboundwiki.com/locations/seaport-city/

Provenance note: Pokémon Unbound is a fan game. It is used only for high-level structural inspiration.

Relevant high-level structure:

The fan game treats a port as a larger urban node containing a terminal, shipyard, marketplace and other services. The ship can also contain an optional timed activity while still functioning as transportation.

Reusable Ouros lesson:

A port district should not collapse into one `FERRY_TERMINAL` marker. Terminal operations, maintenance/shipyard work, public space, markets, freight/courier handoffs and passenger service can coexist but retain different owners and clocks.

A journey may contain optional activity without forcing every passenger to participate or changing the service's authoritative transport state.

No locations, characters, challenge timers, rewards or plot beats are imported.

## Source 5 — Pokémon-world water transportation overview

Source:
https://bulbapedia.bulbagarden.net/wiki/Water_transportation_in_the_Pok%C3%A9mon_world

Relevant high-level structure:

Pokémon fiction repeatedly uses ships, ferries and other water transport with different service models: scheduled regional links, special-access voyages and destination-specific vessels.

Reusable Ouros lesson:

Do not define one universal ferry template. Regions may differ in network density, ticketing, frequency, vessel scale, passenger/cargo mix and how much of a crossing is playable. Those differences are canon questions, not defaults.

## Source 6 — Australian Maritime Safety Authority passenger monitoring

Source:
https://www.amsa.gov.au/vessels-operators/domestic-commercial-vessels/passenger-safety-domestic-commercial-vessels

Relevant operational pattern:

AMSA guidance separates embarkation, disembarkation, onboard passenger counts, recordkeeping and response when a person is unaccounted for. Counts may happen at different operational points depending on the service.

Reusable Ouros lesson:

Passenger-service continuity should preserve observed or recorded counts as time-bounded evidence. A boarding count, onboard count, arrival count and disembarkation count can disagree without any one record automatically being fraudulent. A discrepancy opens a reconciliation question.

No Australian legal threshold, mandatory field, safety duty, certificate class or enforcement regime is imported.

Transformed boundaries:

`BOOKED_PASSENGER != BOARDED_PASSENGER`

`BOARDED_COUNT != CURRENT_ONBOARD_COUNT`

`ARRIVAL_COUNT != DISEMBARKATION_COMPLETE`

`COUNT_DISCREPANCY != PERSON_OVERBOARD_CONFIRMED`

`UNACCOUNTED_FOR_REPORT != MISSING_PERSON_CONFIRMED`

## Source 7 — AMSA operational and emergency procedures

Sources:
https://www.amsa.gov.au/vessels-operators/domestic-commercial-vessels/how-develop-safety-management-system
https://www.amsa.gov.au/changes-marine-order-504/new-sms-requirements/operational-and-emergency-procedures
https://www.amsa.gov.au/tenders/emergency-plans

Relevant operational pattern:

The guidance treats routine onboard procedures, changing conditions, passenger briefing, emergency preparedness, assembly points and specific emergencies as related but distinct records and procedures.

Reusable Ouros lesson:

A service can continue normally while emergency plans merely exist as preparedness state. A drill does not imply an incident. A disruption does not mean every emergency category occurred. If a real incident occurs, the response state should be linked to the actual cause and observation chain.

No real-world legal requirement is imported.

## Design lessons extracted

### Terminal state is not vessel state

A terminal may be open while one sailing is cancelled. A vessel may be ready while the assigned berth is unavailable. A departure may be delayed while boarding has already begun. Port public space may remain open while passenger operations are suspended.

### Sailing identity matters

A recurring service can create many sailings. Each sailing needs its own planned origin, destination, intermediate stops, assigned vessel if relevant, planned departure, actual departure, current phase, arrival and completion history.

### Stop calls are events

Intermediate calls should be explicit when they matter. Passengers can embark and disembark at different stops. Cargo may transfer. Crew may change. A route can be partially served without completing the entire planned pattern.

### Arrival and disembarkation must remain separate

A vessel can arrive at a berth while passengers are still onboard. A berth can become temporarily unavailable after arrival. A passenger can choose not to disembark at an intermediate stop. The world state should therefore avoid `ARRIVED => EVERYONE_OFF` shortcuts.

### Passenger reconciliation is evidence work

A manifest, booking list, boarding count, onboard count and disembarkation count answer different questions. None should overwrite the others. Corrections should be new records linked to prior evidence.

### Vessel identity and service identity are different

A service can substitute vessels. One vessel can perform several services over time. Maintenance history belongs to the asset owner; route/sailing history belongs to service continuity.

### Maritime disruption should branch, not dead-end

Possible operational outputs include delayed departure, berth change, skip-stop, short-turn, substitute vessel, transfer to another service, return to origin, temporary suspension or full cancellation. Which options exist is region- and system-specific canon.

### Weather remains an external owner

A service may record `WEATHER_DEPENDENCY` or `WEATHER_RESTRICTION_REF`, but this layer never decides wind, wave, visibility or storm mechanics. Weather supplies the observed or forecast state; maritime service records the operational response.

### Coastal navigation aids remain an external owner

Beacon, lighthouse and aid-to-navigation state can constrain or inform maritime operations. This layer consumes those records but cannot declare a beacon operational merely because a vessel sailed successfully.

### Search and rescue remains an external owner

An unaccounted-for passenger can create a handoff to Crisis/Rescue when the governing Ouros institution decides that escalation is warranted. Passenger-service continuity preserves counts, timestamps, locations and handoff history; it does not invent rescue authority or search mechanics.

## PTU/Caelo mechanical cross-check boundary

The repository's supplied-mechanics policy already prohibits inventing overworld movement rules, travel speeds, carrying limits, transport capacities, navigation checks, hazard damage, weather penalties, drowning/suffocation rules or rescue actions. No governing PTU/Caelo evidence located during this pass authorizes universal shipboard combat modifiers or maritime traversal math.

Treat the following as UNKNOWN unless exact source and implementation contracts are found:

- generic ship movement per round;
- vessel HP, Armor, Damage Reduction or collision damage;
- rocking-deck penalties;
- slippery-deck checks;
- wave forced movement;
- knockback over rails;
- falling-overboard rules;
- drowning or suffocation timers;
- swimming current checks;
- seasickness statuses;
- generic boarding actions;
- gangway balance checks;
- generic rescue/carrying actions;
- cargo-crate cover or HP;
- mooring-line mechanics;
- anchor mechanics;
- navigation DCs;
- piloting profession mechanics;
- Type-derived sailor competence;
- Water-type immunity to maritime hazards;
- Flying-type automatic overboard recovery;
- Moves or Abilities that automatically steer, tow, stabilize or navigate a vessel;
- Trainer Features that create port authority.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon can present docks, gangways, vessels, terminal signs, NPC queues, berth changes, cargo props, weather already decided by Ouros, passengers entering/leaving and Pokémon routines.

Presentation does not create authority. Entity proximity to a gangway does not prove boarding. A boat entity moving does not establish a valid sailing. A player standing on a vessel does not establish a ticket, booking or manifest entry. A despawn does not prove disembarkation. Water blocks do not create PTU currents, drowning, wave push or movement penalties. Cobblemon BattleState remains outside combatant selection, legality, HP/status, tactical positions and narrative consequence authority.

## Originality and provenance conclusion

Pass 136 supports a dedicated maritime passenger-service continuity extension without importing protected plots or real-world law. The reusable material is structural: network topology, sailing phases, counts as evidence, terminal/vessel separation, service disruption and persistent social life aboard recurring routes.

All Ouros-specific names, institutions, routes, vessels, rules and historical events remain proposed or unknown until canon review.