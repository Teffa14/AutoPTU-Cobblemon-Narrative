# Ouros Vertical Circulation & Lift Service Seeds — Pass 111

Status: NON-CANON PROPOSALS. These are candidate situations, mysteries, encounters and arcs. Nothing here silently establishes regional technology, institutions, mechanics or lore.

Date: 2026-08-28

## Use principles

These seeds assume only that a future canon location explicitly contains a relevant vertical conveyance. Do not spawn elevators or similar technology into every settlement.

Each seed should resolve against current facility, accessibility, maintenance, infrastructure, access-control and actor state. The same template can therefore produce different consequences in different buildings.

## The Lift Works, the Floor Does Not

A conveyance has returned to normal service, but one landing remains closed because the destination itself has an unresolved facility restriction.

Useful tension:

People hear “the lift is fixed” and reasonably assume the floor reopened. Staff must distinguish route restoration from destination reopening.

Possible consequences:

- stale public notice;
- appointment moved to another floor;
- delivery reaches the landing but cannot complete its downstream handoff;
- an NPC believes a repair was incomplete when the actual blocker belongs elsewhere.

No battle required.

## The Building Is Open, the Route Is Not

A multi-level public facility stays operational while one vertical route is out of service.

The meaningful state comes from actor differences. One visitor still has a usable route. Another requires an accommodation or relocated service. A delivery uses a separate freight path. Staff habits change around the temporary arrangement.

Accessibility owns individual impact. The seed must not assume stairs are an acceptable fallback.

## The Car Is Here, Boarding Is Closed

A unit is physically at the landing and visible through Minecraft presentation, but boarding is restricted during testing, inspection, maintenance or another authored condition.

The mystery is social rather than mechanical: why do people keep reporting that the lift is “working” when operators say it is unavailable?

Both observations can be correct within different scopes.

## The Destination Changed Names

Renovation changed the public names or uses of several floors. Old residents, current signage, delivery records and maintenance logs use different labels.

The player must map names to stable location and landing IDs rather than decide that one witness is lying.

This seed supports archives, civic buildings, clinics, hotels, large markets or research facilities without requiring a combat encounter.

## The Temporary Ground-Floor Desk Stayed

During a prolonged vertical-route outage, one service relocated to the ground floor. The lift eventually returned, but the temporary desk became popular enough that the institution considers keeping it.

Possible owner systems:

- Care for a clinic service;
- Commercial Services for a customer counter;
- Civic Governance for a public desk;
- Event Operations for registration;
- Hospitality for guest service.

The vertical layer only records the historical trigger and route state.

## The Freight Route Became the Social Route

A passenger lift outage redirects some authorized traffic through a service corridor or freight route. Workers, regular visitors and Pokémon form new routines there.

After normal service resumes, those relationships remain. This allows a temporary infrastructure state to create lasting character continuity without forcing the workaround to remain physically active.

## The Old Lift Is Still on Every Plan

A decommissioned shaft or unit remains on old maps and building memories long after a replacement route exists.

Possible uses:

- historical exploration;
- incorrect delivery instructions;
- conflicting evacuation maps awaiting owner review;
- an archive room whose old access description still references the retired landing;
- a Pokémon using a quiet decommissioned area, subject to normal ecology evidence rather than causal assumptions.

The old shaft is not automatically a tactical hazard.

## The Power Returned First

An upstream outage ends, but the vertical system remains in TESTING or SERVICE_VERIFIED rather than AVAILABLE.

Residents or visitors see lights return and expect the lift immediately. The story exposes the restoration chain without simulating electrical engineering.

Infrastructure owns power state. Maintenance owns technical verification. Vertical service owns route availability. Accessibility owns actor consequences.

## The Passenger Arrived, the Appointment Did Not

A trip is completed successfully to the correct floor, but the downstream service moved during an earlier outage and the public information is stale.

This is useful for showing that transportation completion and service completion are independent events.

The resolution may update signage, communications or appointment state rather than create combat.

## The Pokémon Waits at the Same Landing Every Day

A recurring Pokémon is observed near one landing at the same time each day.

Possible explanations must remain evidence-driven: a familiar worker arrives then, food is nearby, the area is warm, a human relationship exists, or something else entirely.

Do not infer that the species understands elevator schedules, operates the lift or belongs to anyone.

## The Restricted Floor Has More Visitors Than Records Suggest

Entry logs, witness accounts and trip histories appear inconsistent.

The resolution may reveal legitimate differences between:

- authorized staff;
- accompanied visitors;
- maintenance access;
- trips that stopped without passengers exiting;
- old floor labels;
- incomplete records.

Do not default to trespass or conspiracy.

## Mystery — Five Arrival Times, Three Trips

Five people provide different times for “the elevator arrived.”

The provenance model separates:

- unit arrival at origin;
- boarding completion;
- departure;
- arrival at destination;
- exit completion.

Several statements can be correct. The investigation reconstructs actual trip IDs and timestamps instead of awarding truth points.

## Mystery — Four Floor Names, Two Landings

An old plan, a renovation notice, a resident and a maintenance record use four names. Stable landing IDs show that only two physical destinations are involved and both were renamed during different periods.

This mystery creates history without requiring a secret room.

## Exploration — The Floor That Changed Names

Intended form:

A public building has accumulated renovations, temporary closures and renamed floors. The player reconstructs the vertical route history from maps, notices, staff memory and maintenance records, then uses the current verified route graph to reach the correct destination.

Implementation-now form:

All movement occurs through static, already verified corridors, stairs or an abstracted completed lift trip. No moving platform, shaft hazard, timed door or mechanical puzzle enters AutoPTU.

Future richer form:

If adapter playback eventually supports semantic moving-platform state and the necessary hazard/reaction contracts are verified, the building may visually represent more of the trip. That is optional and does not change the investigation premise.

## Encounter — Lift Lobby Withdrawal

Narrative premise:

A localized Pokémon conflict blocks a lobby while noncombatants need the area cleared so an already planned alternate route can function.

Full version:

The objective may involve withdrawal/protection behavior, multiple exits, Intercept, forced movement and generalized reactions. Dynamic doors, restricted cells or shaft-edge risk would additionally require the terrain/hazards/zones/reactions family. Tactical AI must understand protection and withdrawal. Adapter playback must preserve the distinction between world route state and battle positions.

Reduced version:

Complete civilian relocation before BattleSpec creation. Isolate the lift and exclude shaft/door mechanics. AutoPTU resolves a standard battle in a static lobby with explicit combatants. Winning produces only `IMMEDIATE_LOBBY_SECURED` or an equivalent world fact.

The fight does not restore the lift, grant floor access or complete later travel.

## Encounter — Machine-Room Perimeter

Narrative premise:

Authorized maintenance staff cannot reach an already isolated technical area because a Pokémon incident occupies the access corridor.

Full version:

If active equipment remains mechanically relevant, this depends on terrain/hazards/zones/reactions, complete movement, tactical objective policy and semantic playback. Any damage/status effect also requires a governing PTU/Caelo contract and the relevant pipeline support.

Reduced version:

The equipment remains shut down outside the BattleSpec. Workers stay out of combat. Resolve only the static corridor. Victory sets the access perimeter state; Maintenance performs the later assessment and work.

## Encounter — Split-Floor Diversion

Narrative premise:

A closed landing has shifted foot traffic to another route, and a conflict threatens the temporary junction.

Full version:

A live stream of withdrawing actors would require protection/withdrawal objective semantics, Intercept/forced movement, generalized reactions and tactical policy.

Reduced version:

Move all nonparticipants through the diversion first. Resolve a static junction battle afterward. The same narrative premise survives without representing crowd movement tactically.

## Long arc — A Building Learns Its Routes

Phase 1 establishes ordinary life before any outage: recurring residents, workers, deliveries, appointments, public floors, staff floors, alternate routes and Pokémon that appear for unrelated daily reasons.

Phase 2 introduces a limited vertical-service problem. Different actors experience different consequences. One service relocates. One delivery route changes. One regular visitor stops appearing because their route no longer works for them.

Phase 3 develops the workaround. A previously quiet floor or stair landing gains traffic. Staff from different departments meet more often. A temporary desk becomes useful. Rumors and stale signage create small provenance problems.

Phase 4 separates technical recovery from social recovery. Work finishes, testing occurs, service returns, and destination restrictions or downstream services recover on their own schedules.

Phase 5 revisits the building later. The old workaround has left relationships, labels, habits or institutional changes. A new problem can use this history without repeating the original outage.

There is no `building_access_level` or `lift_upgrade_level`. Continuity comes from persistent routes, actors, records and consequences.

## Faction and NPC candidates

These are role shapes only, not canon characters.

A building route coordinator knows how normal activity changes when one route disappears but does not automatically possess technical authority.

A maintenance liaison translates verified work state into service availability without being the person who decides accessibility accommodations.

A long-term resident remembers older floor names and route changes but can be wrong about current authorization.

A delivery worker knows practical freight paths and recurring bottlenecks but does not prove building ownership or security policy.

An accessibility coordinator owns actor-specific accommodation decisions and should never be reduced to “the person who manages the lift.”

A recurrent Pokémon may become associated with a landing through observed routine, but species alone never grants employment, ownership or mechanical competence.

## Mechanical dependency summary

The reduced noncombat and static-arena material can advance with current verified targeting, base movement, core calculations, action economy and legal-action infrastructure where combat occurs.

Mechanically rich versions depend on the still-PARTIAL complete movement family when Intercept/Push/Pull/Knockback/forced movement matters; PARTIAL turn lifecycle, damage, status, Move, Ability, Item and Trainer Feature families when their exact mechanics matter; and the BLOCKING terrain/weather/hazards/zones/reactions, AI tactical policy and Minecraft/Cobblemon/Craftics adapter/playback families for dynamic lift-space encounters.

No seed treats one working Intercept path as proof that the entire movement/reaction family exists.