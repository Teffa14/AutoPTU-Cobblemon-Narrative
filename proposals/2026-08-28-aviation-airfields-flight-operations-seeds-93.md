# Ouros Aviation, Airfields & Flight Operations Seeds — Pass 93

Status: NON-CANON PROPOSALS. Requires continuity, originality, PTU/Caelo and implementation review before promotion.

Research basis:
- `research/2026-08-28-aviation-airfields-flight-operations-scan-93.md`

Systems basis:
- `design/aviation-airfields-flight-operations-continuity-extension.md`
- `design/travel-transport-expedition-layer.md`
- `design/transit-hubs-passenger-cohorts-extension.md`
- `design/weather-forecast-preparedness-operational-extension.md`
- `design/cobblemon-runtime-authority-boundary.md`

No proposal below establishes that Ouros currently has aircraft or airfields.

## The Flight That Left Empty

A departure was publicly announced and cargo records show an outbound handoff, but the expected passenger cohort never boarded. The service still departed for an operational reason that can be reconstructed from records.

Useful systems: Aviation, Transit Hubs, Material Culture, Communications, Personal Records.

The mystery is about what the operation actually carried and why. It does not presume crime.

## Cargo Arrived Before Passenger Service

A small landing site begins receiving freight before ordinary passenger access starts. Local shops, a clinic, researchers and residents adapt to that asymmetry.

Possible long-term consequence: the settlement develops routines around the cargo day, and passenger opening later changes those routines again.

## One Board, Two Departure Times

A physical board and a newer information channel disagree. Both were correct at different points because one preserves an earlier revision.

The investigation asks what different actors reasonably knew at each time rather than treating one source as fake.

## The Pilot Is Here, the Aircraft Is Not

A recurring worker arrives for the shift, but the transport asset is elsewhere after a diversion, maintenance hold or positioning movement. Several downstream commitments must be renegotiated.

This can be resolved without combat through schedules, alternate transport and communication.

## Diverted Flight, Unmoved Luggage

A passenger operation diverts, while separately routed luggage or parcels continue toward the original destination. The resulting custody problem creates several legitimate handoffs and conflicting expectations.

Courier and Material Culture own the items. Aviation contributes only the movement history.

## The Old Airstrip Became a Habitat Route

A decommissioned strip has acquired recurring ecological use. A proposal to reopen it temporarily triggers survey, public discussion, route planning and possibly relocation of the proposed activity rather than wildlife.

A battle, if any, cannot authorize reopening or erase the habitat record.

## The Runway Light Works on the Wrong Schedule

Workers report that the physical light functions, but its visible operating window no longer matches the published one after a prior schedule change. The fault may be technical, informational or procedural.

Technology/Maintenance owns the device. Aviation owns the operational discrepancy. Public Notices owns what was published.

## The Emergency Landing Everyone Calls a Crash

A transport asset made an unplanned landing and public retellings rapidly call it a crash. Physical inspection, crew testimony and later records may support a less dramatic account.

The hook is about claim propagation and provenance, not disaster spectacle.

## The Pokémon Is Flying Near the Strip

A recognizable wild Pokémon repeatedly crosses part of a landing-area approach during a particular seasonal window. Some workers treat it as an operational issue; others believe the service schedule changed first and created the overlap.

Science/Conservation must establish chronology and ecological interpretation. The Pokémon is never drafted into work or combat because of proximity.

## The Destination That Became a Diversion Habit

A small field receives several unscheduled arrivals over a season. Temporary staffing, food service, local transport and public information adapt. Residents start behaving as though the field is a normal stop even though no scheduled service has been established.

This creates a useful distinction between repeated exceptional use and formal route state.

## Five Reports, Three Flights

Mystery seed.

Five apparent movement records exist for the same day. Cross-checking timestamps, cargo events, board revisions, photographs and destination observations may reveal only three actual flight operations. A maintenance taxi/positioning movement could explain one report; a cancelled announced departure could explain another.

The result may remain partial if evidence is missing.

## Three Weather Holds, Two Causes

Mystery seed.

Three delays are publicly attributed to weather. Two may genuinely trace to observed conditions and one to an unrelated operational dependency that happened during the same forecast window.

Weather evidence, operator decisions and public explanations stay separate.

## A Field Learns Its Connections

Long-form arc.

Phase one establishes ordinary local rhythm before any major problem: workers, nearby businesses, cargo patterns, public access and the field's place in the settlement.

Phase two introduces a limited disruption such as a landing-area inspection, staffing gap, recurring weather hold or changed destination service.

Phase three follows consequences outside the airfield. A supplier changes dispatch timing, a researcher reroutes, a resident misses a recurring visitor, or a local market gains different stock.

Phase four adds a structural decision: adjust the service pattern, improve information flow, modify a physical area, preserve part of an old strip, or rely more heavily on another transport mode.

Phase five revisits the site after the change. The new arrangement solves some problems and creates another observable effect, such as altered visitor pressure, cargo timing or wildlife overlap.

Phase six allows old state to matter again. A former worker, old board, earlier route, decommissioned zone or archived flight record becomes relevant to a new question.

The field accumulates history. No hidden `airport_level` is required.

## Encounter concept: Runway Perimeter Withdrawal

Status: proposed.

Premise:
An immediate conflict develops near an inactive perimeter while workers or surveyors are still present.

Full intended version:
Support explicit WITHDRAW/CLEAR_ROUTE-like objectives, Intercept and other legal forced movement, several safe access lanes, objective-aware opponent behavior and authoritative playback. Weather or operational equipment affects tactics only if corresponding AutoPTU families are verified.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:
Stop all aircraft movement first. Workers withdraw entirely through world state. Exclude the active landing area and machinery from the tactical arena. Ouros chooses the participants and AutoPTU resolves a static legal encounter. Visual wind, rain, lights and vehicles have no tactical effect. Reopening remains a later operational decision.

## Encounter concept: Diverted Cargo Apron Interruption

Status: proposed.

Premise:
A diverted operation creates unusual cargo staging while a separate hostile or frightened group blocks one safe route.

Full intended version:
Objective-aware route control, withdrawal and protection behavior; legal Intercept/reactions; multiple routes; semantic playback that keeps cargo and noncombatants separate from combatants.

Dependencies are the same broad families as Runway Perimeter Withdrawal, with particular reliance on complete movement, AI tactical policy and adapter/playback. Terrain/hazards become required only if the apron, equipment or weather is intended to have mechanical effects.

Reduced version:
Shut down transport assets. Keep all cargo, vehicles and workers outside the grid. Resolve a standard static encounter nearby. Success creates `safe_access_available`; it does not complete delivery, custody transfer or unloading.

## Encounter concept: Old Airstrip Wildlife Conflict

Status: proposed.

Premise:
A former strip now overlaps a recurring wildlife route while a temporary reuse proposal is under review.

Full intended version:
Territorial/withdrawal-aware AI, optional multiple access lanes and reviewed environmental state.

Reduced version:
Run the ecological survey before any battle. If tactical resolution becomes necessary, use a static arena away from active works and include only explicitly selected participants. The final battle result cannot decide conservation policy or reopen the strip.

## Noncombat concept: Departure Reconciliation

Players compare a board revision, cargo timestamp, staff note, photograph and destination report to determine whether an announced flight actually departed.

No battle capability is required. The scene can run entirely through existing observation, records, communication and time-state systems.

## Canon questions deliberately left open

Ouros has no aviation canon established by this file. Review is still required for technology, locations, operators, route prevalence, passenger/cargo practices, airfield access, emergency procedures, former-site reuse and Pokémon work roles.

PTU/Caelo review is still required for any mechanically meaningful Sky transport, Mount use, carrying, piloting, altitude, falling, vehicle operation, collision or weather interaction.