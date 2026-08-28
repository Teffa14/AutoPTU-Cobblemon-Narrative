# Ouros Port & Harbor Narrative Seeds — Pass 96

Status: NON-CANON PROPOSALS. These are reusable authored candidates only.
Date: 2026-08-28

All names below are working titles, not established Ouros places, institutions or characters.

## The Berth Changed, the Cargo Did Not

A scheduled vessel is reassigned from one berth to another after a maintenance restriction. The cargo paperwork still names the original berth, while the physical shipment was correctly staged at the new one.

Playable structure:

- compare berth allocation revisions;
- inspect current notices;
- reconcile shipment/custody timestamps;
- determine whether the mismatch is stale information or an actual missing handoff;
- update the correct operational record without rewriting the cargo's provenance.

Possible consequence:

A business or courier changes its receiving procedure after discovering that workers were treating berth numbers as permanent identifiers.

No battle required.

## The Vessel Is Here, Boarding Is Not

A ferry is visible at the pier but passengers are being held in the terminal.

Possible causes remain open until evidence resolves them:

- service authorization delay;
- crew/staffing dependency;
- navigation restriction;
- maintenance verification;
- destination-side problem;
- superseded timetable;
- unknown cause.

The scene teaches that physical presence is not operational permission.

## The Temporary Landing Became Familiar

A primary passenger berth closes for a limited period. A smaller landing handles reduced service long enough that nearby vendors, regular travelers and couriers reorganize around it.

After the original berth reopens, the temporary location has a constituency and a history.

Long-term choices can concern future use, but the system does not assume who has authority to decide.

## Three Manifests, Two Actual Loads

Mystery pattern.

Three surviving records appear to describe three cargo movements. Reconciliation may show that one document was an earlier revision, one was the operational copy and one describes a return load.

Evidence can include:

- authored timestamps;
- revision lineage;
- photographs;
- custody handoffs;
- warehouse observations;
- vessel call times;
- courier records;
- batch or item-instance provenance.

The resolution can remain partly uncertain. A discrepancy does not require fraud.

## The Cargo Arrived, the Delivery Did Not

A needed shipment is physically discharged from a vessel but remains at the port because the next custody transfer has not happened.

Downstream consequences can affect:

- a workshop repair;
- an event;
- a care facility;
- a research expedition;
- a storefront;
- an infrastructure project.

The player can investigate or coordinate the handoff, but entering the port does not grant custody or ownership.

## The Passenger Service Came Back First

A waterfront recovers from a disruption in phases. Passenger operations resume at one safe berth while cargo handling remains restricted elsewhere.

Local actors disagree about whether "the port is open." All can be speaking accurately about different functions.

The scenario works as a public-information and actor-knowledge problem rather than a hidden-truth puzzle.

## The Ship Everyone Calls Late Was Re-Scheduled

Regular locals remember the old timetable. A revised service now arrives later by design, but old signs and personal routines persist.

The player can encounter:

- a current timetable;
- a superseded but readable sign;
- a worker who knows the new pattern;
- a traveler relying on memory;
- a courier commitment written against the old connection.

The interesting consequence is how a small schedule revision propagates through ordinary life.

## One Berth, Two Kinds of Day

A berth supports routine transport most days but is periodically used for an event, research operation, fisheries landing or other canon-supported purpose.

The system should preserve operating episodes rather than permanently reclassifying the berth after each use.

## The Warehouse Outlived Its Trade

A warehouse remains after the traffic that created it disappeared.

Possible later uses:

- storage for another industry;
- repair workspace;
- public market;
- archive or collection storage;
- emergency staging;
- habitat edge;
- partial abandonment.

A later proposal to restore waterfront service must account for the intervening use rather than treating the building as empty legacy geometry.

## The Wildlife Is Near the Pier

People begin attributing a delay or damaged equipment to Pokémon repeatedly observed near a berth.

Investigation separates:

- direct observations;
- actual damage evidence;
- maintenance history;
- ecology observations;
- rumor;
- operational cause.

Possible outcomes include a genuine interaction, an unrelated technical fault, several contributing causes or insufficient evidence.

No species stereotype resolves the case.

## The Wrong Vessel at the Right Berth

A familiar berth contains a vessel locals do not recognize.

The call may be legitimate and temporary: research, maintenance, emergency, charter, replacement service or another canon-supported purpose.

The hook works because residents know the normal operating pattern. Unusual does not mean hostile.

## Four Passenger Counts, One Cohort

An operational reconciliation compares four estimates of the same arriving group.

Differences can arise because observations were taken:

- before boarding completed;
- after an intermediate stop;
- at disembarkation;
- after some passengers left the terminal.

The system uses Transit Hub cohorts unless exact identity matters. It does not manufacture a missing-person case solely from aggregate counts.

## The Missed Connection That Changed a Town Visit

A delayed ferry causes a traveler, specialist, performer, researcher or courier to remain in a settlement longer than planned.

Instead of generating a generic delay scene, the world can expose a meaningful temporary consequence:

- a specialist becomes available locally;
- an appointment is missed elsewhere;
- a recurring contact appears in an unexpected place;
- an event gains or loses a participant;
- a delivery deadline needs rerouting.

The port disruption becomes a world-state connector.

## The Call That Never Became a Visit

A vessel was expected but diverted before arrival. People who planned around the call still experience consequences even though the vessel never appears at the port.

Useful state remains:

- planned call;
- diversion record;
- notices;
- missed passenger/cargo operations;
- commitments affected by the absent arrival.

Do not delete the planned call because it never became `ALONGSIDE`.

## A Port Learns Its Turnaround

Long-form persistent arc.

Phase 1 establishes ordinary waterfront rhythm: familiar workers, recurring services, known berth uses, regular passenger and cargo handoffs.

Phase 2 introduces a limited operational pressure: one berth becomes unavailable, one service changes timing, or a temporary event consumes part of the waterfront.

Phase 3 shows downstream consequences. Couriers change transfer timing, a business receives goods later, regular passengers alter routines, wildlife uses a quieter area, or workers improvise a documented workaround.

Phase 4 produces an intervention or operational revision. This may involve maintenance, revised allocation, different staging, a new notice procedure or another canon-supported response.

Phase 5 separates restoration milestones. Physical repair, technical verification, berth availability, service scheduling, passenger operation and cargo operation may resume on different dates.

Phase 6 returns later. A former temporary landing has regular users, an old timetable remains in memory, a repurposed warehouse matters to another institution, or a vessel last seen during the disruption returns under a different purpose.

The port becomes richer through history rather than an abstract `port_level`.

## Mechanically rich concept — Berth Evacuation Withdrawal

Full intention:

A conflict erupts near a working berth and the tactical objective is to clear people through safe routes while denying access to the operational area.

Dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including Intercept/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle if selected combat content uses it;
- terrain/weather/hazards/zones/reactions if dock edges, machinery or environmental conditions are mechanically active;
- selected move-specific behavior, Abilities, Items and Trainer Features as actually used;
- AI legal-action infrastructure;
- AI tactical policy for evacuation/route objectives;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version:

Suspend all port movement first. Evacuate workers, passengers and nonparticipant Pokémon in world state. Remove cargo and machinery from tactical interaction. Use a static nearby yard/quay arena away from water edges. Ouros chooses combatants explicitly. AutoPTU resolves combat only. Port and Travel decide whether the berth resumes afterward.

## Mechanically rich concept — Cargo Transfer Interruption

Full intention:

A conflict threatens an active handoff whose narrative significance comes from provenance and custody rather than from treating crates as hit-point objects.

Dependencies:

- verified targeting/base movement/core calculations/action economy/AI legal infrastructure;
- complete movement PARTIAL for route clearing and Intercept;
- lifecycle/damage/status families according to selected combat content;
- zones/reactions BLOCKING if staging boundaries become tactical;
- move/Ability/Item/Trainer Feature families only for exact selected content;
- AI tactical policy BLOCKING for protect/withdraw behavior;
- adapter/playback BLOCKING.

Reduced version:

Freeze the transfer at its last verified custody event. Move the physical cargo out of the arena. Fight in a static adjacent location. No battle outcome transfers ownership, changes custody, completes delivery or alters manifest truth. Reconcile the handoff after battle.

## Mechanically rich concept — Harbor Entrance Diversion

Full intention:

A conflict at or near a harbor entrance requires traffic to remain outside while combatants secure a route.

Dependencies:

- targeting and base movement;
- complete movement for withdrawal/route control;
- ordinary combat calculations and lifecycle;
- terrain/weather/hazards/zones/reactions if water, wind, currents or coastal structures matter mechanically;
- tactical AI;
- adapter/playback.

Reduced version:

All vessels are already held outside by Maritime/Port world state. The encounter occurs on a static shore or breakwater approach with no moving craft, water movement, drowning, collision or weather mechanic. AutoPTU resolves only explicit participants. Afterward Maritime/Travel decides whether calls wait, divert or resume.

## Canon questions intentionally left unresolved

These proposals do not decide:

- where Ouros ports exist;
- which waterfront institutions exist;
- whether passenger or cargo manifests are standard;
- what privacy applies to them;
- whether customs, immigration, pilotage or tug services exist;
- who allocates berths;
- what safety law exists;
- what cargo technology exists;
- what Pokémon work roles are legitimate;
- how maritime credentials are issued;
- which historical waterfronts were abandoned or repurposed.

Those require explicit canon or governing source evidence.