# Service Access, Queues & Appointments Research — Pass 70

Status: research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-27

## Scope

This pass investigates the operational gap between a service existing and an actor actually receiving it: requests, eligibility checks, registration, appointment slots, walk-ins, queues, check-in, waiting, rescheduling, cancellation, no-shows, service start and completion.

The repository tree was inspected recursively before writing. Ouros already has service ownership in Care, Travel, Storefronts, Battle Institutions, Events, Education, Workplaces, Libraries, Shared Equipment and other layers. Several of those layers contain local reservation or schedule fields. What is missing is a reusable coordination contract for access demand and time allocation that does not steal authority from the underlying service.

Pass 70 therefore targets service-access continuity, not a universal bureaucracy or ticketing economy.

## Existing-repository boundary

Relevant owners remain:

- `design/care-recovery-welfare-layer.md` — care cases, clinical capacity, treatment legality and urgency;
- `design/travel-transport-expedition-layer.md` and `design/transit-hubs-passenger-cohorts-extension.md` — departures, route/service capacity and passenger movement;
- `design/commercial-services-storefront-continuity-extension.md` — whether a commercial service is operating and what it offers;
- `design/battle-institutions-challenge-circuits-layer.md` — challenge eligibility, format and battle authority;
- `design/temporary-public-event-operations-extension.md` — event activities and their schedules;
- `design/workplaces-professions-staffing-layer.md` — staff availability and assignments;
- `design/shared-equipment-lending-issued-assets-extension.md` — reservations for exact shared assets;
- `design/libraries-publications-editions-circulation-extension.md` — circulation and reservations for copy instances;
- `design/public-notices-signage-world-information-extension.md` — physical projection of published schedules and notices;
- `design/observation-settlement-time-layer.md` — world time and observed schedules.

Pass 70 must not duplicate specialized asset/library reservation state, invent medical triage, create prices or define legal eligibility. It records the access lifecycle around an owning service.

## Source 1 — PTU official Gym registration separated from execution

Source: Pokémon Tabletop RPG, “Gym Design: Unconventional Challenges.”
https://pokemontabletop.com/gym-design-unconventional-challenges/

Observed pattern:

The PTU design article explicitly suggests a Gym Leader who allows challengers to register, then initiates the actual challenge later at an unexpected time. Registration and execution are therefore distinct states, and the waiting period can itself become playable narrative space.

Reusable lesson:

A confirmed request does not need to mean immediate service. A world can preserve `registered`, `waiting`, `called`, `started` and `completed` independently. The delay may matter because other schedules continue to advance.

Transformation for Ouros:

An approved Gym, specialist, laboratory, workshop or civic service can accept a request now and perform it later. Pass 70 stores the access state and timing refs; the owning layer decides what the service actually does.

## Source 2 — PTU community arena receptionist and social waiting

Source: Pokémon Tabletop community RP, Arena Commons.
https://www.tapatalk.com/groups/pokemon_tabletop/arena-commons-t6475-s140.html

Observed pattern:

A receptionist signs multiple characters up for a specific fight while other interactions occur in the shared waiting space.

Reusable lesson:

A queue or signup list can be social world state rather than a loading screen. Waiting creates opportunities for rivals, witnesses, rumors, staffing changes and schedule conflicts.

Transformation for Ouros:

A service lobby can materialize only the small set of story-relevant waiting actors while the rest remain an aggregate cohort. The community scene is inspiration only and supplies no authoritative PTU rule.

## Source 3 — Contest Hall reception, practice and finite participation

Source: Bulbapedia, Contest Hall / Pokémon Contest.
https://bulbapedia.bulbagarden.net/wiki/Contest_Hall
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Contest

Observed pattern:

Contest Halls use reception counters for entry, can separate normal and linked participation, and in Sinnoh also expose a distinct practice counter. Multiplayer contests have bounded participant counts.

Reusable lesson:

One venue can expose several access channels with different purposes, eligibility and capacity. “At the building” does not mean “entered in the event.” Registration, practice, spectator access and competition participation should remain separate.

Transformation for Ouros:

A canon-approved venue may have multiple `service_access_channel` records that point to the same place but different owning services.

## Source 4 — Battle Frontier check-in as a multi-step intake pipeline

Source: Bulbapedia, Battle Frontier / Battle Hall.
https://bulbapedia.bulbagarden.net/wiki/Battle_Frontier_(Generation_IV)
https://bulbapedia.bulbagarden.net/wiki/Battle_Hall

Observed pattern:

Frontier facilities use attendants to select format, validate an entered Pokémon, preserve streak context and then escort the participant to a battle room. The service is a pipeline rather than one interaction.

Reusable lesson:

Access may require check-in data that belongs to the service owner. The coordinator should preserve the result of that validation, but it must not invent eligibility rules itself.

Transformation for Ouros:

Pass 70 can record `eligibility_check_ref`, `checked_in_at`, `called_at` and `service_started_at`. Battle Institutions remains authoritative for legal roster, format and challenge state.

## Source 5 — Busy Pokémon Centers show capacity and staffing pressure

Sources: Bulbapedia, Nurse Joy; “The Joy of Pokémon”; “Pinch Healing!”
https://bulbapedia.bulbagarden.net/wiki/Nurse_Joy
https://bulbapedia.bulbagarden.net/wiki/EP092
https://bulbapedia.bulbagarden.net/wiki/EP462

Observed pattern:

The animation repeatedly depicts Centers or care networks where one Nurse Joy is overloaded, absent from another duty, making rounds across islands, or otherwise unable to provide every service at once.

Reusable lesson:

Service availability and immediate access are different. An operating facility can be at reduced effective capacity. Waiting time, referral or delayed intake can emerge from staffing and workload without fabricating a new crisis.

Transformation for Ouros:

Care owns clinical capacity, urgency and treatment. Pass 70 can translate the owning layer’s result into queue state, estimated windows or referral handoffs. It cannot rank patients using a hidden medical score.

## Source 6 — Real Pokémon Center virtual queue: waiting does not guarantee inventory

Source: Pokémon Center Support, “Pokémon Center Virtual Queue,” updated 2025-10-15.
https://support.pokemoncenter.com/hc/en-us/articles/37286495522452-Pok%C3%A9mon-Center-Virtual-Queue

Observed pattern:

The official retail service distinguishes position in a virtual queue, estimated wait and later access from actual product availability. It also warns that estimates vary with demand.

Reusable lesson:

A queue entry grants a place in an access process, not the underlying outcome. Estimated time is a forecast, not a promise. A service can still become unavailable before the actor reaches the front.

Transformation for Ouros:

Use explicit `estimate_generated_at`, `estimate_window` and `estimate_basis_ref` where needed. Never treat an estimate as authoritative future fact.

This is operational design inspiration from a real Pokémon-branded service, not in-universe canon.

## Source 7 — Safari-style bounded admission

Source: Bulbapedia walkthrough, Hoenn Safari Zone.
https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Emerald/Part_20

Observed pattern:

Entry is a distinct transaction with bounded session conditions. Access ends after a defined limit even though the location still exists.

Reusable lesson:

A service slot can authorize a bounded session rather than permanent access. Check-in, active session and session end are distinct from physical presence at the location.

Transformation for Ouros:

Only use such limits where an established Ouros service actually has them. Pass 70 supplies lifecycle structure, not admission prices, time limits or capture rules.

## Cross-source patterns

### Request, acceptance and execution are separate

An actor can request service, receive a confirmed place and still not have begun the service.

### Capacity belongs to the owner

The queue coordinator can consume a capacity result. It must not decide why a clinic, ferry, workshop or event has one, four or zero available slots.

### Priority needs provenance

If one actor moves ahead of another, store the policy or decision reference. Never infer priority from wealth, reputation, species, Trainer class or narrative importance.

### Waiting is world time

While a player waits, departures can leave, weather can change, NPC schedules can advance and other actors can enter or leave the same space. Waiting should compress when nothing interesting can happen.

### Estimates are not promises

A predicted start window can change when capacity, staffing or preceding sessions change.

### Specialized reservations stay specialized

An appointment to use a service may point to an equipment reservation, room allocation or library hold, but Pass 70 must not replace those records.

### A queue is not automatically visible as individual NPCs

Large demand should usually be represented as counts/cohorts plus only story-relevant actors. Minecraft does not need dozens of persistent waiting entities to preserve queue state.

## Anti-copy and canon rules

Do not copy named Gym Leaders, Contest officials, episode plots, exact facility rules, fees, time limits or competition progression.

Do not assume Ouros has numbered tickets, digital booking, universal identity cards, reservation deposits, cancellation fees, emergency triage protocols or walk-in rights.

Do not infer that a missed appointment is negligence, that priority is favoritism, or that a long wait means poor staffing.

## PTU/Caelo boundary

Pass 70 is primarily narrative/world-state coordination. It cannot create PTU battle eligibility, healing legality, item effects, Trainer Feature permissions or encounter timing rules.

If an appointment leads to battle, Battle Institutions and AutoPTU still own the legal battle input and result. If service interruption becomes a tactical encounter, any civilians, dynamic queue movement, protection objectives, forced movement, reactions, terrain/weather or tactical AI must be classified against the permanent engine capability map.

## Pass 70 design target

Create a reusable service-access extension with stable service-channel refs, access requests, appointment/slot allocation, walk-in queue entries, check-in, call/start/completion timestamps, explicit priority provenance, wait estimates, cancellation/rescheduling/no-show state, group handling, capacity handoffs and world-time consequences.

Add original non-canon situations where service access itself creates continuity or investigation without turning every wait into a quest.