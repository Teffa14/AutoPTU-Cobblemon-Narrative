# Ouros Narrative Research — Vertical Circulation & Lift Service Continuity — Pass 111

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file establishes Ouros canon.

Date: 2026-08-28

## Why this gap was selected

The repository inventory was inspected recursively before writing and the returned tree was complete (`truncated=false`) at narrative head `ffbf372fdbc6c17d66c5f76c2c61b6e841f65201`.

Existing ownership already covers nearby concerns:

- `accessibility-participation-accommodations-layer.md` owns actor-specific access needs and already permits an `access_route_variant` to reference a lift and its service dependency.
- `facility-maintenance-repair-inspection-extension.md` owns faults, assessments, work orders, repairs, verification and reopening of facility assets.
- `infrastructure-outage-restoration-extension.md` owns upstream service loss, backup continuity and downstream restoration handoffs.
- travel/transit layers own journeys between authored locations, not the internal operating lifecycle of a building lift.

No dedicated layer was found for the operational continuity of elevators, platform lifts, freight lifts or other authored vertical conveyances inside a facility. The useful gap is therefore narrow: preserve the identity and service state of a vertical route while leaving accessibility, maintenance, technical repair and tactical movement under their existing authorities.

## Public Pokémon source 1 — Silph Co. across generations

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Silph
- https://strategywiki.org/wiki/Pok%C3%A9mon_HeartGold_and_SoulSilver/Saffron_City

Relevant high-level pattern:

Silph Co. is a multi-floor location whose accessible extent changes between games. In HeartGold/SoulSilver the elevator is described as broken/unsafe and the upper floors are unavailable through normal play. The same building therefore persists while one vertical circulation service changes the accessible graph.

Reusable Ouros lesson:

A building, destination floor and vertical route must have separate state. A facility can remain open while one internal route is unavailable. A route outage can materially change access without destroying or closing the whole building.

Rejected copying:

Do not import Silph Co., Steven Stone, Rotom's Room, its floor plan, dialogue, rewards or corporate history.

## Public Pokémon source 2 — Lift Key / Elevator Key

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Lift_Key
- https://bulbapedia.bulbagarden.net/wiki/Elevator_Key

Relevant high-level pattern:

Pokémon games repeatedly separate the physical presence of an elevator from authorization to operate it. The Team Rocket Hideout Lift Key and Lysandre Labs Elevator Key activate otherwise inaccessible vertical transport.

Reusable Ouros lesson:

`SERVICE_OPERABLE`, `ACTOR_AUTHORIZED`, `DESTINATION_AUTHORIZED` and `TRIP_COMPLETED` must be different facts. An operational car does not grant every actor access to every landing. Conversely, access authorization does not prove that the equipment is currently available.

Rejected copying:

Do not import villain organizations, branded keys, specific locked floors, reward placement or plot gates.

## Public Pokémon source 3 — Pokémon Reborn Obsidia Department Store

Sources:
- https://pokemon-reborn.fandom.com/wiki/Obsidia_Department_Store
- https://pokemon-reborn.fandom.com/wiki/Department_Store_Stickers_Sidequests

Relevant high-level pattern:

The store uses one persistent elevator while access to higher floors expands through a separate membership/sticker progression. The elevator's physical existence, its operation and the actor's entitlement to a destination are separable.

Reusable Ouros lesson:

Destination permission can change independently of route state. This is useful for staff floors, archives, treatment areas, observation decks, residential floors, service basements or other authored restrictions without turning the lift itself into an access-control authority.

Rejected copying:

Do not import the sticker system, shop inventory, floor progression, sidequests, Porygon reward or Reborn characters.

## Public operational source — outage and return-to-service separation

Sources:
- https://www.safework.nsw.gov.au/hazards-a-z/lifts-escalators-and-moving-walkways
- https://www.technicalsafetybc.ca/technologies/elevating-devices/elevating-devices-assessments
- https://www.tssa.org/elevator-availability-faqs-elevator-owners

These are external operational references, not Ouros law or engineering standards.

High-level reusable observations:

A malfunction can cause a lift to be deliberately taken out of service. Repair/maintenance activity, outage records and return to service can be separate events. Some real-world regimes also require outstanding maintenance/testing or other verification before public operation resumes.

Ouros transformation:

Preserve state transitions such as `OUT_OF_SERVICE -> UNDER_WORK -> TESTING -> SERVICE_VERIFIED -> AVAILABLE` without importing legal deadlines, inspection jurisdiction, technical standards, capacity rules, certification regimes or occupational requirements.

## Design lessons extracted

### Facility state and vertical-route state are separate

`BUILDING_OPEN` does not imply `EVERY_VERTICAL_ROUTE_AVAILABLE`.

A clinic can remain open while one lift is unavailable. A tower can keep using stairs while a freight lift is isolated. A residential building can have a severe access consequence for one household even when most occupants can still reach their floors by another route.

Accessibility owns the actor-specific consequence.

### Equipment condition and service availability are separate

`REPAIR_COMPLETE` does not imply `SERVICE_VERIFIED`.

Maintenance owns the fault and repair record. A vertical-circulation layer should consume the verification handoff and then expose the resulting route availability.

### Car/platform presence and trip state are separate

`CAR_AT_LANDING` does not imply `BOARDING_AUTHORIZED`.

`DOOR_OPEN` does not imply `DESTINATION_ACCESSIBLE`.

`PASSENGER_BOARDED` does not imply `TRIP_DEPARTED`.

`CAR_ARRIVED` does not imply `PASSENGER_EXITED`.

These distinctions allow interruptions, restricted landings, passenger assistance and stale reports without requiring a simulation of elevator machinery.

### Authorization belongs to another authority

A lift may carry different authorization rules for different destinations, but this layer does not invent legal, employment, security, residential or commercial rights. It stores an `access_authority_ref` or consumes a decision from the owning system.

### Power/service dependencies are explicit

A lift can depend on authored power, control, staffing, access or building conditions. Power restoration does not automatically restore lift service. Infrastructure emits a restoration handoff; the conveyance still needs its own readiness state if canon requires it.

### Alternative routes remain first-class

When a lift is unavailable, a building graph may still contain stairs, ramps, another lift or an exterior route. The vertical-circulation layer exposes route state; Accessibility evaluates whether a usable route exists for a particular actor.

### Temporary workarounds can become narrative history

An outage can move appointments downstairs, redirect deliveries, shift foot traffic, create a staffed assistance point or make an overlooked stair landing socially important. These changes can persist after repair as memories, habits or later callbacks.

## PTU/Caelo cross-check

The controlling internal source scan remains `research/2026-08-18-source-scan.md`. It establishes that PTU/Caelo can support authored location identity and specific environmental effects when governing material explicitly defines them. It does not establish a universal elevator subsystem.

No governing project evidence was found for generic PTU/Caelo rules for:

- elevator speed or travel time;
- capacity/load calculations;
- door timing;
- emergency braking;
- elevator-shaft falling damage;
- moving-platform initiative;
- crushing/trapping hazards;
- power-loss behavior;
- rescue from a stalled car;
- mechanical repair checks;
- freight-handling bonuses;
- Pokémon operation privileges derived from species or Type.

Those remain UNKNOWN unless exact governing rules and implementation evidence are later found.

## Battle implementation implication

A fight inside a moving car, on a moving platform, across opening/closing doors, beside an active shaft or during a fall would depend on more than base movement. Such concepts may require complete movement, timed turn/round lifecycle, hazards/zones/reactions, full damage/status handling, move-specific hooks, tactical policy and adapter playback.

The safe reduced pattern is to stop/isolate the conveyance first, remove passengers and technical interactions, and instantiate a static landing/lobby/service corridor as the AutoPTU arena.

## Research exclusions

This pass does not copy protected dialogue, floor layouts, villain plots, named characters, quests or puzzle solutions. Real-world safety sources are used only for abstract separation between outage, work, testing/verification and return to operation. They do not establish Ouros regulation or technical procedure.

## Candidate canon questions

Ouros still needs authored decisions about which settlements use lifts or other vertical conveyances, what technologies exist, who operates them, whether residential/public/service devices differ, how destination authorization works, what fallback routes are customary, how accessibility is handled regionally, which historic buildings contain decommissioned shafts, and whether any individual Pokémon have explicit trained roles around vertical transport.