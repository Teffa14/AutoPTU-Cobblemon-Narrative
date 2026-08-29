# Engine Readiness Snapshot — Pass 136

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This snapshot records live implementation evidence checked while adding maritime ferry, port and passenger-service continuity.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 136:

`da30eef6869a868572f6bbfeaef07dea6e625053`

The recursive tree was inspected before topic selection. Repository searches were run for ship, maritime, ferry, harbor, terminal and related terms. The existing Travel/Transport layer was read directly, as was Pass 135 readiness.

The existing Travel layer already recognizes SEA_LANE/WATERWAY connections, public transport, ferry disruption examples and harbors. No dedicated continuity extension existed for sailing identity, terminal/berth state, boarding, passenger counts, stop calls, arrival/disembarkation or maritime service recovery. Pass 136 fills that specialized gap rather than duplicating generic Travel.

## AutoPTU-Java live evidence

Current head inspected:

`106dd1010eeec7ec2423688ed5eeec2274ae8d18`

Commit:

`Freeze terrain skill-check helper closure`

The commit changes `tools/python/export_intercept_check_contract.py` so the pinned `_terrain_skill_check_bonus` export also walks reachable local helper functions and freezes each helper's normalized source, calls, string literals and integer literals.

This remains strong parity-contract evidence for one localized Intercept terrain-skill-check path.

It does not establish generalized maritime terrain, deck movement, waves, currents, overboard transitions, shipboard reaction ordering or environmental forced movement.

No permanent capability category is promoted.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during this pass.

The current change remains presentation-only: cached Pixi screen dimensions are synchronized after viewport resize so subsequent tactical sprite destinations use current renderer geometry.

This does not establish maritime world-state playback, vessel movement authority, terminal/berth state, boarding/disembarkation semantics, passenger reconciliation, service scheduling or tactical-to-world consequence handoff.

## Permanent capability map — Pass 136

No category receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Baseline targeting and static spatial legality remain sufficient for reduced terminal/perimeter encounters.

`base movement legality`

Basic movement remains verified for conventional static BattleSpecs.

`core calculations`

Previously established parity-backed calculation infrastructure remains verified at its current baseline.

`action economy/initiative`

Baseline action economy and initiative remain verified.

`AI legal-action infrastructure`

Legal-action enumeration and validation remain verified. This still does not provide objective-aware maritime tactics.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

The localized Intercept path has frozen contract evidence. Broad Push, Pull, Knockback, every forced-movement source, deck displacement, overboard transitions, escort semantics and generalized movement reactions are not verified as a complete family.

`full turn/round lifecycle`

Ordinary progression exists. Staged passenger withdrawal, timed gangway closure, boarding windows and multi-phase evacuation are not established as generalized lifecycle contracts.

`full stateful damage pipeline`

Substantial implemented behavior exists, but the permanent family remains partial.

`status lifecycle`

Implemented statuses do not authorize invented seasickness, panic, drowning, soaked, unstable-footing or maritime-disruption statuses.

`move-specific behavior`

Representative Move implementations do not prove complete behavior coverage. No Move may be assumed to tow, steer, stabilize, moor, rescue or propel a vessel outside exact governing evidence.

`abilities`

Representative Ability behavior does not prove the full family. No Ability creates passenger authorization, vessel readiness, port authority, navigation truth or service restoration.

`items`

Items remain partial. Tickets, passes, manifests, ropes, lifejackets, cargo crates or navigation equipment receive no tactical effect unless exact rules support it.

`Trainer Features/perks`

Exact Features remain source-governed. No narrative profession label such as captain, sailor, dock worker or terminal operator creates PTU mechanical authority.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

Rich maritime encounters would need exact support for moving or unstable environments, protected gangway zones, waves/currents if used, dynamic obstacles, overboard state and generalized reactions. The current pinned Intercept terrain helper does not provide those capabilities.

`AI tactical policy`

Rich variants may need objective-aware behavior such as PROTECT, WITHDRAW, CLEAR_ROUTE, HOLD_POSITION, AVOID_EDGE, preserve a protected access lane or prioritize an exit rather than raw attack value. Legal-action infrastructure does not provide this policy.

`Minecraft/Cobblemon/Craftics adapter/playback support`

Current rendering evidence does not provide semantic projection for sailing phase, terminal state, berth state, boarding/disembarkation, passenger reconciliation, vessel substitution, stop calls, service disruption or tactical-to-world handoff. This family remains blocking.

## Encounter review — Gangway Withdrawal

Full intended objective:

A tactical incident intersects a terminal while boarding is underway. Passengers and staff withdraw through safe access while combatants secure the area.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL for implemented legal statuses only
- terrain/weather/hazards/zones/reactions — BLOCKING for protected gangway zones, changing geometry, waves/weather effects or generalized reactions
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version status:

BLOCKED FOR RICH SEMANTICS.

Reduced version status:

READY.

Reduced contract:

1. Maritime service pauses boarding before BattleSpec creation.
2. Ordinary passengers, unselected crew, records, controlled cargo and noncombatant Pokémon leave the tactical grid.
3. Vessel operational state remains static outside AutoPTU.
4. Ouros selects explicit combatants.
5. AutoPTU receives reviewed static terminal geometry.
6. Tactical resolution may produce only `IMMEDIATE_APPROACH_CLEAR` or an equivalent narrow physical fact.
7. Maritime service separately decides whether boarding resumes.

Victory never establishes boarding completion, passenger reconciliation, vessel departure or terminal reopening.

## Encounter review — Arrival-Side Chokepoint

Full intended objective:

A vessel has arrived but a separate tactical incident blocks passenger egress.

Rich dependencies:

- complete movement — PARTIAL for escort/Intercept/forced movement
- full lifecycle — PARTIAL for staged withdrawal
- terrain/hazards/zones/reactions — BLOCKING for protected exits or dynamic access state
- AI tactical policy — BLOCKING
- semantic adapter/playback — BLOCKING

Reduced version status:

READY.

Reduced contract:

1. Passengers remain onboard or are moved to a safe nonbattle world-state location.
2. Disembarkation is paused in maritime state.
3. Vessel, passenger records and ordinary crew remain outside BattleSpec semantics.
4. AutoPTU resolves a conventional static encounter.
5. Maritime service decides afterward whether disembarkation begins or resumes.

Victory never establishes `DISEMBARKATION_COMPLETE` or `PASSENGER_REACHED_FINAL_DESTINATION`.

## Encounter review — Substitute-Berth Access Perimeter

Full intended objective:

A sailing has been reassigned to a temporary berth, but a nearby threat prevents opening the passenger approach.

Rich dependencies:

- complete movement — PARTIAL for escort/Intercept
- full lifecycle — PARTIAL for phased access opening
- terrain/hazards/zones/reactions — BLOCKING for protected approach lanes or changing obstacles
- AI tactical policy — BLOCKING for CLEAR_ROUTE/PROTECT behavior
- adapter/playback — BLOCKING

Reduced version status:

READY.

Reduced contract:

1. Substitute berth remains operationally closed before combat.
2. Staff, passengers, signage records and service data stay outside BattleSpec.
3. Ouros provides static geometry and explicit combatants.
4. AutoPTU resolves conventional combat.
5. The maritime owner receives the narrow physical result and separately decides whether access opens.

Victory never assigns a berth, opens passenger service, authenticates a notice or changes a sailing schedule.

## Encounter review — Unaccounted-For Inquiry Perimeter

Full intended objective:

A passenger-count discrepancy is being reconciled when a separate tactical threat appears near the terminal.

Important narrative constraint:

A count discrepancy does not become a search/rescue objective unless Crisis/Rescue already owns a valid search state based on world evidence.

Reduced version status:

READY.

Reduced contract:

1. Reconciliation staff and records withdraw before BattleSpec creation.
2. Passenger inquiry state remains paused and preserved.
3. AutoPTU resolves only the nearby tactical incident.
4. Reconciliation resumes afterward from the same evidence chain.

Victory never means a person was found, never proves person-overboard and never resolves the count discrepancy.

## PTU/Caelo unresolved mechanics

The following remain UNKNOWN unless exact governing source and implementation contracts are found:

- generic ship movement per round;
- vessel HP, Armor, Damage Reduction or collision damage;
- rocking/slippery deck checks;
- wave or current forced movement;
- knockback-over-rail transitions;
- falling-overboard rules;
- drowning/suffocation timing;
- swimming/current DCs;
- seasickness statuses;
- generic gangway balance checks;
- protected-passenger reactions;
- escort actions;
- generic rescue/carrying actions;
- crate or cargo HP;
- mooring-line mechanics;
- anchor mechanics;
- piloting/navigation checks;
- profession mechanics for captain/sailor/crew;
- Type-derived maritime competence or resistance;
- Water-type automatic safety in maritime hazards;
- Flying-type automatic recovery from overboard state;
- Moves/Abilities that automatically tow, steer, stabilize or propel a vessel;
- Trainer Features that create institutional maritime authority.

## Minecraft/Cobblemon authority boundary

Minecraft/Cobblemon may present world facts already decided by Ouros:

- docks and piers;
- gangways;
- terminal signage;
- vessel models;
- passenger queues;
- NPC boarding/disembarkation animations;
- substitute berths;
- cargo props;
- public notices;
- weather presentation;
- recurring Pokémon routines.

Minecraft/Cobblemon state does not decide:

- whether a sailing exists;
- whether the vessel is assigned or ready;
- passenger authorization;
- booking or manifest truth;
- boarding completion;
- passenger count;
- disembarkation completion;
- vessel departure/arrival;
- route legality;
- maritime authority;
- service restoration;
- combatant selection;
- tactical legality;
- HP/status;
- narrative consequence.

A moving boat entity is presentation, not transport authority. Water blocks do not create PTU current, wave, drowning or forced-movement rules. Cobblemon BattleState remains outside Ouros tactical authority.

## Canon questions left open

Which regions have scheduled ferry networks?

Which terminals, islands and coastal settlements are connected?

Who operates the services?

Which services mix passengers and cargo?

What access, booking, ticketing or manifest systems exist, if any?

What passenger information is retained and who can access it?

Who can delay, cancel, divert, skip-stop, short-turn or substitute a sailing?

How are vessels inspected and maintained?

How do ports coordinate with Weather, Coastal Navigation Aids, Crisis/Rescue, Courier, Markets and Conservation?

Which recurring crew, commuters and Pokémon are named canon actors?

Which former terminals, changed berths, lost routes or shipyard projects remain visible in present-day settlements?

No answer is silently canonized by Pass 136.

## Pass 136 readiness conclusion

The maritime ferry/port continuity layer is safe to use at the world-state level.

The reduced encounter variants are READY because boarding, passenger reconciliation, vessel state, service decisions, ordinary passengers and noncombatant crew remain outside BattleSpec before conventional combat begins.

Rich shipboard or active-boarding tactical variants remain blocked by the same permanent capability families as Pass 135. The current AutoPTU-Java terrain helper closure strengthens only a localized Intercept-related contract and does not justify a family-level promotion.