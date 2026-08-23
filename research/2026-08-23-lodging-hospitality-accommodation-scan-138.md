# Lodging, Hospitality & Accommodation Research Scan — Pass 138

Status: research/provenance only. Not canon.
Date: 2026-08-23

## Why this scan exists

The repository already has a Food, Agriculture & Hospitality layer, but its hospitality coverage is centered on food venues, kitchens, service events and culinary traditions. Repository search before this pass found no dedicated model for lodging reservations, room inventory, check-in/check-out, guest stays, housekeeping readiness, accommodation constraints, room sharing, overflow lodging, no-shows, waitlists or guest/Pokémon accommodation.

This scan therefore treats lodging as a distinct persistent-world concern that connects Travel, Tourism, Care, Accessibility, Identity, Credentials, Currency/Payments, Public Events, Emergency Services, Architecture and Pokémon Agency without moving those systems into the hotel layer.

The goal is not to build a hotel-management simulator. The goal is to give Ouros enough state to remember where people stayed, what capacity existed, what was promised, what was actually ready, what changed during crises/events and how a place of lodging can become a recurring social and narrative anchor.

## Source 1 — Pokémon Legends: Z-A official Hotel Z material

Source:
- Pokémon Legends: Z-A — New Adventures in Lumiose City
- https://legends.pokemon.com/en-au/story-world/lumiose-city
- Pokémon Legends: Z-A — Team MZ: Protecting the Peace in Lumiose City
- https://legends.pokemon.com/en-au/news/team-mz

Relevant structure:
- The protagonist stays at an old hotel, Hotel Z.
- The hotel functions as a base of operations across many adventures rather than as a one-time cutscene.
- A major supporting character lives and works there and helps the owner.
- Lodging, employment, social relationships and adventure structure can share the same physical place while remaining separate systems.

Reusable lesson for Ouros:
- A hotel, inn, hostel or lodge can be a persistent hub with staff shifts, recurring guests, room history, deliveries, notices, social scenes and changing neighborhood context.
- A lodging venue can matter even when no room-related quest is active.
- Living at a workplace is a separate state from being employed there.

Do not copy:
- Hotel Z itself, Team MZ, its staff, characters, redevelopment plot or specific story beats.

## Source 2 — Hotel Grand Lake / Lakeside Resort

Source:
- Bulbapedia — Hotel Grand Lake
- https://bulbapedia.bulbagarden.net/wiki/Hotel_Grand_Lake

Relevant structure:
- The resort is physically distributed across multiple bungalows and terraces instead of being one building.
- It hosts Coordinators during major events and also contains a restaurant and reception functions.
- The game presents a state where rooms are fully booked while the lobby can still provide rest/healing support.
- The resort becomes part of the social infrastructure around competitions.

Reusable lesson for Ouros:
- `lodging_property` and `room_unit` should be separate. One property can include multiple buildings, cottages, bunkrooms, cabins or campsites.
- Event demand can fill sleeping capacity while common spaces remain operational.
- A venue can serve temporary populations during tournaments, festivals, expeditions or emergencies without those visitors becoming residents.
- Lodging capacity should connect to Demography as temporary presence, not settlement population.

Do not copy:
- Resort layout, Seven Stars Restaurant rules, named NPCs or specific rewards.

## Source 3 — Cinnabar tourism saturation and lodging overflow

Source:
- Bulbapedia — EP058 “Riddle Me This”
- https://bulbapedia.bulbagarden.net/wiki/EP058

Relevant structure:
- Tourism growth changes the identity of Cinnabar Island.
- Pokémon Center lodging and resort rooms can be fully booked.
- Travelers must choose an alternate overnight solution when capacity is exhausted.
- Tourism pressure also changes unrelated institutions and local behavior.

Reusable lesson for Ouros:
- “No room available” should come from occupancy/capacity state, not arbitrary narrative denial.
- Overflow can redirect travelers to camping, another settlement, public shelter, host families or transport rescheduling when those options exist.
- Lodging saturation can be a consequence of a festival, tournament, research boom, disaster displacement or tourism season.
- A capacity problem can matter without becoming a combat encounter.

Do not copy:
- Cinnabar’s tourism plot, Big Riddle Inn or Blaine’s story.

## Source 4 — Resort hotel and wildlife warning pattern

Source:
- Bulbapedia — BW003 “A Sandile Gusher of Change!”
- https://bulbapedia.bulbagarden.net/wiki/BW003

Relevant structure:
- A family resort has an established relationship with local Sandile.
- The Pokémon begin behaving differently and disrupting guest use of the resort.
- The apparent nuisance is later understood as warning behavior connected to a physical hazard.

Reusable lesson for Ouros:
- Lodging venues can have long-term ecological relationships with nearby Pokémon populations.
- A guest complaint, closure or unusual Pokémon behavior is an observation, not a diagnosis or cause.
- Hospitality operations can intersect with hazard monitoring, conservation and evacuation without turning wild Pokémon into hotel property.

Do not copy:
- Sandile/geyser plot or named characters.

## Source 5 — Pokémon Center lodging as journey infrastructure

Source:
- Bulbapedia — Pokémon Center
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Center

Relevant structure:
- Pokémon Centers are repeatedly depicted as offering lodging, food, waiting spaces and recovery infrastructure to traveling Trainers.
- They also function as communication and package destinations.

Reusable lesson for Ouros:
- Some lodging can be institutional rather than commercial.
- A bed may be part of a journey-support service rather than a conventional hotel transaction.
- Lodging, clinical care, postal delivery and communications may share a facility but should keep separate records and permissions.

Caution:
- This source aggregates portrayals across media. Treat the institutional pattern as inspiration unless the project’s Caelo canon explicitly defines Center lodging.

## Source 6 — PTU public campaign: hotel as a bounded social space

Source:
- Something Awful — [Pokemon Tabletop United] Mr Fuji’s Wild Ride
- https://forums.somethingawful.com/showthread.php?threadid=3795270

Relevant structure:
- The campaign uses a hotel as a detailed place with reception, room keys, dining schedules, room-service accounting and house rules around Pokémon and battles.
- The accommodation creates a bounded social environment before any major tactical event.

Reusable lesson for Ouros:
- House rules can be explicit world-state policies without becoming universal laws.
- Individual properties can differ in what Pokémon they can safely accommodate due to architecture, staffing or facilities.
- A guest can know a rule without agreeing with it; violating a rule can create an operational or institutional problem without automatically becoming a crime.
- Room keys/access credentials should not be treated as ownership.

Do not copy:
- The hotel branding, room specifications, numerical height restriction, meal times, pricing or plot.

## Source 7 — PTU official campaign seed: ordinary innkeepers as PCs

Source:
- Pokémon Tabletop RPG — Campaign Seeds: Mysterious Ruins
- https://pokemontabletop.com/campaign-seeds-mysterious-ruins/

Relevant structure:
- The official PTU blog explicitly presents innkeepers alongside farmers and breeders as ordinary community roles capable of anchoring a campaign.

Reusable lesson for Ouros:
- Lodging operations can be a player career or institution rather than background scenery.
- A player-run inn can accumulate Chronicle through travelers, local knowledge, supply disruptions, seasonal demand and returning guests without every stay becoming a quest.

Do not copy:
- Oran Valley, its buried ruins, gods or plot events.

## Source 8 — Hotel operations as state-machine inspiration

Sources:
- Oracle Hospitality OPERA Cloud — Reservations controls
- https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.2/ocsuh/c_opera_controls_reservations.htm
- Oracle Hospitality OPERA Cloud — Checking in Reservations
- https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.2/ocsuh/t_checking_in_reservations.htm
- Oracle Hospitality OPERA Cloud — Managing Reservation Queue Status
- https://docs.oracle.com/en/industries/hospitality/opera-cloud/22.2/ocsuh/t_arrivals_in-house_adding_reservation_to_queue.htm
- Oracle Hospitality OPERA Cloud — Managing Waitlist Reservations
- https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.3/ocsuh/t_managing_reservations_waitlist.htm

Relevant structure:
- Reservation state and room state are different.
- A reservation can be confirmed while the assigned room is not yet ready.
- Waitlisting can exist when requested inventory is unavailable.
- Check-in can include room assignment and completion as distinct steps.
- Shared reservations and accompanying guests are separate records.
- Past stays retain history including cancelled/no-show/checked-out states.

Reusable lesson for Ouros:
- Avoid one `has_room=true` flag.
- Keep booking intent, reservation confirmation, room assignment, room readiness, physical occupancy and completed stay separate.
- Keep room availability separate from whether a particular room is clean, accessible, under maintenance or held for another need.
- Preserve cancelled/no-show history instead of deleting it.

Do not import:
- Credit-card requirements, deposits, taxes, rates, identification law, vendor-specific statuses, commercial hotel law or any Oracle-specific operational policy.

## High-level architecture extracted from the research

Useful world-state chain:

```text
travel/event need
    -> accommodation request
    -> availability assessment
    -> reservation / waitlist / decline
    -> room-or-space assignment
    -> readiness validation
    -> arrival / check-in
    -> active stay
    -> incidents / service changes / room changes
    -> check-out / departure / no-show / cancellation
    -> housekeeping/maintenance transition
    -> historical stay record
```

Each arrow is independently observable and may fail without invalidating prior history.

## Narrative patterns worth reusing

### 1. The same room across years

A specific room can accumulate history: ordinary stays, a championship season, flood damage, renovation, accessibility retrofit and later historical recognition. The room remains the same persistent unit while revisions change.

### 2. Event saturation without contrived danger

A major Contest or League event can legitimately fill a settlement’s beds. Players may need to choose between a campsite, distant lodging, a host arrangement or rescheduling transport. No villain is necessary.

### 3. The booking exists but the room is not ready

A maintenance problem, prior late departure or cleaning backlog can delay occupancy while the reservation remains valid. This creates small social/operational scenes without fabricating theft or fraud.

### 4. Pokémon accommodation is individual and facility-specific

A property may have ordinary rooms, outdoor partner spaces, quiet rooms, aquatic access, reinforced courtyards or no ability to host certain movement/body requirements. This should be based on physical capability and facility state, not broad species stereotypes.

### 5. Return guests create continuity

Recurring Trainers, researchers, performers, workers and families can reappear through the same lodging venue. Staff may recognize them based on documented prior stays without implying friendship.

### 6. Crisis conversion

A hostel, school dormitory or hotel can temporarily function as emergency accommodation. Crisis/Emergency Services own the incident and evacuation; Lodging owns temporary bed/room allocation and stay records.

### 7. A lodging venue can decline, recover or change role

A resort can become worker housing, student housing, research lodging, a shelter, apartments or a museum/heritage property. Architecture owns the physical adaptive reuse. Lodging owns historical stays while the property served that function.

## Guardrails for Ouros

- Reservation does not equal occupancy.
- Occupancy does not equal residence.
- Residence does not equal ownership.
- A room key does not create ownership or general authority.
- Being seen in a hotel does not imply romance, friendship, conspiracy or shared travel.
- Two people sharing a booking does not establish a private relationship label.
- A guest record is private operational data by default.
- A Pokémon accompanying a guest does not become property of the venue.
- A Pokémon remaining at the venue after a Trainer departs requires separate custody/agency state.
- House rules are property policies, not regional criminal law.
- A complaint is an observation, not proof.
- A missing item in a room does not prove theft.
- A damaged room does not establish who caused the damage.
- “No vacancy” must reflect actual allocation/capacity state when the simulation cares about it.
- A visual Minecraft bed does not create authoritative sleeping capacity.
- Destroying a bed block does not erase a reservation or historical stay record.
- Sleeping/resting in narrative state does not create PTU Sleep status.
- Lodging does not automatically heal HP, Injuries, fatigue or Status.

## PTU/Caelo mechanics boundary

No reliable project-local Caelo source was recovered in this run for lodging, sleep, rest duration, Pokémon accommodations, Trainer fatigue or room benefits.

Public PTU material was used only for setting/campaign inspiration. This scan does not define:
- sleep/rest mechanics;
- Trainer fatigue;
- healing from lodging;
- room-quality bonuses;
- camping checks;
- Pokémon carrying/space requirements;
- Pokémon Center lodging legality;
- hospitality Skill checks;
- prices or lodging economy;
- house-rule enforcement mechanics.

Super PTU Online Helper was not available as an invocable capability in this runtime. No output is attributed to it.

## Originality boundary

The sources above contribute high-level structures only. Ouros proposals must use original places, staff, institutions, architecture, incidents, guest histories and story arcs. No protected dialogue, distinctive plot, exact hotel layout, named hotel, character or unique narrative sequence should be reproduced.