# Engine Readiness Snapshot — Pass 140

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This snapshot records live implementation evidence checked while adding service reservation, ticket, pass and admission continuity.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 140:

`f3d73f65f16fcbc14b383c9236d783da8e4d2c8a`

The full recursive narrative repository tree was inspected before topic selection and returned `truncated: false`.

The selected gap was checked against existing systems including:

- Service Access / Queues / Appointments;
- Credentials / Authorizations / Recognition;
- Finance / Sponsorship / Risk;
- Travel / Transport and specialized transport continuity layers;
- Event Operations;
- Material Culture;
- Human Identity;
- Place Reference;
- PTU/Caelo source research.

The gap is connective. Existing systems already own service operations, slots/queues, institutional authority, payment, physical artifacts and actor identity. They did not provide a cross-domain continuity record for a bounded service entitlement from issuance through representation, validation, use, reissue, supersession and disruption.

## AutoPTU-Java live evidence

Current head inspected:

`5f8c23950e5689a771b9c9d0772e7cc60e9a8197`

Commit:

`Add server-owned terrain skill-check resolver (#282)`

This is newer than the AutoPTU-Java evidence recorded in Pass 139.

The commit adds `TerrainSkillCheckBonusResolver`, described in source as resolving the reusable portion of Python `BattleState._terrain_skill_check_bonus` and `_matches_naturewalk_terrain` from server-owned facts rather than accepting a precomputed adapter bonus.

The inspected diff shows explicit handling for eligible skills including Athletics, Acrobatics, Stealth, Perception and Survival, a Survivalist gate, Naturewalk labels, terrain-context labels and the localized +2 Survivalist/Naturewalk bonus. Dedicated resolver tests are added to the Intercept parity workflow.

This is meaningful implementation progress. It provides stronger evidence that one terrain-context skill-check bonus can now be resolved server-side from owned facts and parity-gated against the Python oracle.

It does not establish the full permanent `terrain/weather/hazards/zones/reactions` family.

Specifically, this commit does not by itself verify:

- generalized terrain objects or tactical terrain state;
- terrain creation/removal;
- movement-cost or movement-legality changes from all terrain;
- weather creation, duration, replacement or expiration;
- hazards and their full lifecycle;
- dynamic zones;
- generalized reactions;
- reaction ordering or competing reaction windows;
- environmental Push/Pull/Knockback;
- all Naturewalk consequences outside the specific helper contract;
- every Survivalist interaction;
- objective-aware tactical AI;
- semantic Minecraft/Cobblemon playback of terrain facts.

Therefore no permanent family receives a promotion from this commit alone.

The commit does strengthen localized evidence inside two already non-VERIFIED areas:

- `Trainer Features/perks` remains PARTIAL, with improved evidence for the exact Survivalist/Naturewalk interaction covered by the resolver;
- `terrain/weather/hazards/zones/reactions` remains BLOCKING as a family, with a now-verified narrow terrain-context input path insufficient to establish the rest of that combined capability.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during Pass 140.

The commit explicitly states that its change is presentation-only and does not alter battle rules or outcomes. It synchronizes cached Pixi dimensions after viewport resize.

This does not establish semantic adapter/playback for reservations, tickets, passes, validation, service access, boarding, admission, payment or entitlement use.

## Permanent capability map — Pass 140

No category receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Static targeting and spatial legality remain sufficient for reduced encounters after noncombat service-access state is resolved outside BattleSpec.

`base movement legality`

Baseline movement remains verified for conventional reviewed BattleSpecs.

`core calculations`

Previously established parity-backed calculation infrastructure remains verified at its current baseline.

`action economy/initiative`

Baseline tactical action economy and initiative remain verified. Initiative has no authority over queue priority, reservation order, admission, entitlement validation or service boarding.

`AI legal-action infrastructure`

Legal-action enumeration/validation remains verified. It does not provide objective-aware evacuation, escort, perimeter defense or corridor-clearing policy.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

Specific Intercept paths have strong evidence, but the combined family remains partial. Broad Push, Pull, Knockback, every forced-movement source, escort movement and generalized movement reactions remain unverified.

`full turn/round lifecycle`

Ordinary tactical progression exists. Generalized staged passenger withdrawal, synchronized civilian movement, boarding windows and objective-driven timed phases remain unverified.

`full stateful damage pipeline`

Substantial implemented behavior exists, but the permanent family remains partial.

`status lifecycle`

Exact implemented statuses can be used only where their contracts apply. This pass creates no generic denied-entry, invalid-ticket, late, no-show or disrupted-service tactical status.

`move-specific behavior`

Representative Move implementations do not establish family completeness. No Move automatically validates, duplicates, consumes or waives a ticket/pass.

`abilities`

Representative Ability implementations do not establish family completeness. No Ability creates automatic travel entitlement, identity verification or admission authority.

`items`

Items remain partial. A narrative paper ticket, pass card, stamp or token does not become a PTU combat Item without exact source support.

`Trainer Features/perks`

The new AutoPTU-Java terrain resolver strengthens evidence for the exact Survivalist/Naturewalk terrain skill-check interaction it covers. The full Trainer Features/perks family remains partial. No Feature creates universal fare, admission, reservation, validation or institutional authority.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

The new generic server-owned terrain skill-check bonus resolver is a real narrow implementation advance. The permanent category remains blocking because it combines much broader requirements: tactical terrain lifecycle, weather, hazards, zones and generalized reactions. Rich admission-boundary encounters can require protected lanes, changing obstacles or reaction windows not established by the new helper.

`AI tactical policy`

Rich variants can require PROTECT, WITHDRAW, CLEAR_ROUTE, HOLD_POSITION or escort-aware behavior. Legal-action infrastructure does not establish those policies.

`Minecraft/Cobblemon/Craftics adapter/playback support`

No live evidence establishes semantic projection for entitlement identity, holder binding, reservation state, ticket representation, validation, consumption, reissue, cancellation, boarding or admission.

## Encounter review — Boarding Gate Withdrawal

Full intended objective:

Passenger validation or boarding is underway when an independent threat appears. The owning service pauses processing while ordinary passengers and staff withdraw and combatants secure the approach.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for protected lanes, dynamic obstacles or generalized reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Validation and boarding pause before BattleSpec creation.
2. Passengers, validators, private records, controlled tokens and noncombatant Pokémon leave the tactical grid.
3. Ouros selects explicit combatants.
4. AutoPTU receives static reviewed geometry.
5. Tactical victory may create only `IMMEDIATE_GATE_APPROACH_CLEAR` or an equivalently narrow physical fact.
6. The service owner separately decides whether validation/boarding resumes.
7. The entitlement layer separately preserves validity/use state.

`TACTICAL_VICTORY != ENTITLEMENT_VALIDATED`.

`APPROACH_CLEAR != BOARDING_AUTHORIZED`.

## Encounter review — Ticket Office Access Chokepoint

Full intended objective:

A disrupted service has a temporary replacement or rebooking desk. An independent tactical threat blocks the public approach.

Full dependencies match Boarding Gate Withdrawal if moving civilians, protected corridors, forced displacement or objective-aware AI are active.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Customers, staff, financial records and entitlement records are secured outside BattleSpec.
2. AutoPTU resolves a conventional encounter on static approach geometry.
3. Tactical victory may create only `IMMEDIATE_PUBLIC_APPROACH_CLEAR`.
4. Reservation change, entitlement reissue and monetary settlement remain separate post-battle owner decisions.

`TACTICAL_VICTORY != REBOOKING_COMPLETED`.

`TACTICAL_VICTORY != REFUND_APPROVED`.

## Encounter review — Special-Admission Perimeter

Full intended objective:

A service or remote activity requires a broad pass plus a specific special entitlement. An unrelated tactical encounter occurs outside the admission perimeter.

Full version becomes dependent on the rich families only if moving perimeter zones, escort, hazards or generalized reactions are desired.

Reduced version status: READY.

Reduced contract:

1. Entitlement/prerequisite evaluation occurs before combat.
2. Validators, visitors and records remain outside BattleSpec.
3. AutoPTU receives explicit combatants and static geometry.
4. Tactical victory may secure the immediate exterior perimeter.
5. The admission owner separately retains or changes the access decision only from non-battle evidence/rules.

`BATTLE_RESULT != PREREQUISITE_SATISFIED`.

## Encounter review — Departure Change Corridor

Full intended objective:

A gate, platform or berth assignment changes after travelers already hold valid reservations. An independent threat affects the corridor between old and new service points.

Dependencies:

- complete movement — PARTIAL if dynamic escort/interception is desired;
- full lifecycle — PARTIAL for staged passenger movement;
- terrain/weather/hazards/zones/reactions — BLOCKING for changing obstacles/protected lanes;
- AI tactical policy — BLOCKING for objective-aware corridor control;
- adapter/playback — BLOCKING for semantic service-point change projection.

Reduced version status: READY.

Reduced contract:

1. Place Reference and service owners resolve the new service point before combat.
2. Travelers are moved in world state before BattleSpec creation.
3. Combat occurs only after the corridor is cleared of civilians.
4. Victory may create `IMMEDIATE_CORRIDOR_CLEAR`.
5. The owning service separately manages allocations, boarding and itinerary updates.

`CORRIDOR_CLEAR != RESERVATION_UPDATED`.

## PTU / Caelo mechanical guardrails

The project source scan supports authored persistent activities, Jobs, travel/exploration and exact environmental mechanics when governing sources define them. It does not establish a universal service-entitlement subsystem.

Remain UNKNOWN unless exact PTU/Caelo evidence is found:

- universal fare tables;
- generic ticket/pass Items;
- reservation Skill Checks;
- ticket-validation Skill Checks;
- generic forgery detection;
- no-show penalties;
- refund rules;
- transferability rules;
- seat/cabin/berth allocation mechanics;
- generic admission checks;
- Battle victory granting service access;
- automatic discounts/access from League rank, Badges, Trainer Classes or Features;
- species/Type/Move/Ability-derived free travel or institutional privilege;
- universal digital ticketing technology.

The new terrain resolver likewise must not be stretched into unrelated narrative checks. A server-owned Survivalist/Naturewalk bonus for eligible terrain skill checks does not imply that Survival, Perception or any other Skill can validate tickets, navigate bureaucracy, determine fare eligibility or authenticate documents.

## Minecraft / Cobblemon guardrails

Minecraft may project ticket counters, gates, route boards, queue rails, old paper props, temporary service desks, closed doors and NPC routines already decided by Ouros.

Minecraft state is observational/presentation state unless an authored adapter contract explicitly maps it back into an Ouros world fact.

A held item stack does not prove ticket validity.

A scoreboard tag does not become a diegetic pass.

An open gate does not grant access.

A button press does not consume a ticket.

A Cobblemon entity standing beyond a gate does not prove valid admission.

Cobblemon BattleState remains non-authoritative for combatant selection, battle legality, HP/status, tactical position and narrative service consequences.

## Canon questions remaining open

- Which regions or institutions use reservations, tickets or passes?
- Which services are open admission?
- Which entitlements are bearer-based, named, group-bound or invitation-bound?
- Which physical/digital representations exist in-setting?
- Which issuers retain recoverable records?
- Which systems permit reissue or transfer?
- What disruption/rebooking practices exist?
- What financial refund practices exist?
- Which League/event venues separate spectator access from competitor eligibility?
- Which recurring commuter, student, festival or civic passes exist?
- Which historical tickets have become archival/material-culture objects?

All remain UNKNOWN/PROPOSED until canon work establishes them.

## Pass 140 conclusion

AutoPTU-Java gained meaningful new server-owned terrain-context skill-check infrastructure at head `5f8c23950e5689a771b9c9d0772e7cc60e9a8197`. The evidence is narrow enough that no permanent category is promoted.

The new narrative entitlement concepts remain fully implementable in reduced form because their core continuity is world-state data rather than battle semantics. Rich encounters continue to expose exact dependencies instead of requiring Minecraft or Cobblemon to duplicate missing PTU battle rules.
