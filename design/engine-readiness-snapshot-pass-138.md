# Engine Readiness Snapshot — Pass 138

Status: ENGINE-EVIDENCE SNAPSHOT / NARRATIVE IMPLEMENTATION GUARDRAIL.
Date: 2026-08-29

This snapshot records live implementation evidence checked while adding request, dispatch and response-resource continuity.

AutoPTU-Java and AutoPTU were inspected read-only. This pass writes only to `Teffa14/AutoPTU-Cobblemon-Narrative`.

## Narrative repository inspection

Narrative head before Pass 138:

`303cb9c1ad6d07918e8ccb489c3e1a8d643899d5`

The full recursive repository tree was inspected before topic selection and returned `truncated: false`.

A lodging/hotel candidate was rejected because Pass 100 already owns that continuity surface.

The selected gap was checked directly against:

- `design/crisis-rescue-recovery-layer.md`
- `design/communications-network-relay-service-continuity-extension.md`
- `design/workplaces-professions-staffing-layer.md`
- `design/mission-dungeon-grammar.md`
- existing research inventory including `research/2026-08-18-source-scan.md`
- Pass 137 readiness

The gap is narrow: existing systems can create needs, communications, staffing assignments and player missions, but no existing layer preserves a generic resource-assignment chronology from intake through renewed availability.

## AutoPTU-Java live evidence

Current head inspected:

`9946f3a46f05ff187e0b04979351e276ab55697e`

Commit:

`Fix terrain oracle helper lexical scope (#281)`

This is newer than the Pass 137 head `106dd1010eeec7ec2423688ed5eeec2274ae8d18`.

The commit modifies the Intercept parity exporter and its CI/test coverage. The relevant change makes helper resolution respect Python lexical scope and runtime binding behavior, including later duplicate definitions replacing earlier definitions in the same scope. It also adds dedicated exporter tests and gates them in the Intercept parity workflow.

This is useful hardening for the existing localized Intercept / terrain-skill-check oracle contract.

It does not establish:

- generalized terrain state;
- terrain creation or removal;
- weather lifecycle;
- generic hazards or zones;
- generalized reactions or reaction ordering;
- broad Push/Pull/Knockback;
- every forced-movement source;
- escort semantics;
- staged withdrawal semantics;
- objective-aware tactical AI;
- dispatch, arrival or handoff semantics.

No permanent capability category is promoted by this commit.

## AutoPTU live evidence

Current head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer AutoPTU commit was present during this pass.

The change synchronizes cached Pixi dimensions after viewport resize so tactical sprite destinations use live renderer geometry. Its commit message explicitly describes it as presentation-only and states that battle rules and outcomes do not change.

It does not establish semantic projection for requests, resource assignment, arrival, check-in, field handoffs, communications loss or resource availability.

## Permanent capability map — Pass 138

No category receives a promotion.

### VERIFIED

`targeting/footprints/range/LoS`

Baseline targeting and static spatial legality remain sufficient for reduced static encounters.

`base movement legality`

Basic movement remains verified for conventional reviewed BattleSpecs.

`core calculations`

Previously established parity-backed calculation infrastructure remains verified at its current baseline.

`action economy/initiative`

Baseline tactical action economy and initiative remain verified. Initiative order must never be interpreted as dispatch priority.

`AI legal-action infrastructure`

Legal-action enumeration and validation remain verified. This does not provide objective-aware withdrawal, escort or protection policy.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

The localized Intercept path continues to gain stronger parity/freezer evidence. Broad Push, Pull, Knockback, every forced-movement source, escort movement and generalized movement reactions remain incomplete as a family.

`full turn/round lifecycle`

Ordinary battle progression exists. Generalized staged responder withdrawal, moving arrivals, timed handoffs or dispatch-linked tactical windows are not verified.

`full stateful damage pipeline`

Substantial implemented behavior exists, but the permanent family remains partial.

`status lifecycle`

Implemented statuses may be used only where their exact contracts apply. No generic panic, responder readiness, fatigue, radio-contact, injury-triage or mission status is invented here.

`move-specific behavior`

Representative Moves do not establish full family coverage. No Move automatically accepts a dispatch, authenticates a report, completes a rescue, authorizes a handoff or changes institutional priority without exact governing rules.

`abilities`

Representative Ability behavior does not prove the whole family. No Ability creates responder authority or incident truth.

`items`

Items remain partial. Radios, badges, tools, vehicles, documents or equipment receive no tactical effect unless exact rules support it.

`Trainer Features/perks`

Exact Features remain source-governed. No Feature automatically grants universal incident command, dispatch authority, rescue jurisdiction or occupational qualification.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

Rich response encounters may require protected withdrawal corridors, active hazard boundaries, changing access zones, moving objectives or generalized reactions. The Intercept terrain helper contract remains far narrower than this family.

`AI tactical policy`

Rich variants may require PROTECT, WITHDRAW, CLEAR_ROUTE, HOLD_POSITION, escort-aware behavior or avoidance of sensitive zones. Legal-action infrastructure alone does not provide those policies.

`Minecraft/Cobblemon/Craftics adapter/playback support`

Current presentation evidence does not provide semantic projection for request intake, assignment, acknowledgement, en-route status, arrival, check-in, transfer, handoff or renewed availability. This family remains blocking.

## Encounter review — Response Team Withdrawal Corridor

Full intended objective:

A noncombat field team is already working when a separate tactical threat emerges. Their assignment pauses while they withdraw and combatants secure the immediate route.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for staged withdrawal
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL for exact implemented statuses only
- terrain/weather/hazards/zones/reactions — BLOCKING for protected corridors, active boundaries or generalized reactions
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

1. Field work and dispatch state pause before BattleSpec creation.
2. Responders, controlled equipment, private records and noncombatant Pokémon withdraw from the tactical grid.
3. Ouros selects explicit combatants.
4. AutoPTU receives static reviewed geometry.
5. Tactical resolution may produce only `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR` or an equivalently narrow physical result.
6. The response-resource owner separately decides whether the team returns, transfers or closes its assignment.

`TACTICAL_VICTORY != ASSIGNMENT_COMPLETE`.

## Encounter review — Staging-Site Access Chokepoint

Full intended objective:

An assigned resource cannot immediately reach an authored staging or work site because a tactical threat blocks the approach.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement — PARTIAL if escort, Intercept or forced movement is active
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full lifecycle — PARTIAL for staged arrivals
- damage/status/move/ability/item/Feature families — PARTIAL as applicable
- terrain/hazards/zones/reactions — BLOCKING for protected arrival lanes or changing access
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- semantic adapter/playback — BLOCKING

Full version status:

BLOCKED FOR RICH SEMANTICS.

Reduced version status:

READY.

Reduced contract:

1. Resource state remains outside BattleSpec as `ARRIVAL_BLOCKED` or another authored operational state.
2. Noncombat resource members and controlled equipment remain outside the tactical grid.
3. AutoPTU resolves a conventional static encounter at the chokepoint.
4. Victory may create only `IMMEDIATE_APPROACH_CLEAR`.
5. Arrival and check-in are recorded afterward by the narrative owner if they actually occur.

`APPROACH_CLEAR != RESOURCE_ARRIVED`.

`RESOURCE_ARRIVED != RESOURCE_CHECKED_IN`.

## Encounter review — En-Route Assignment Diversion

Full intended objective:

A travelling resource receives or considers a different assignment because another problem appears nearby.

Rich dependencies:

- complete movement — PARTIAL for escort/Intercept/forced movement
- full lifecycle — PARTIAL for moving/timed decision windows
- terrain/hazards/zones/reactions — BLOCKING if the route changes tactically during battle
- AI tactical policy — BLOCKING
- semantic adapter/playback — BLOCKING

Full version status:

BLOCKED FOR RICH SEMANTICS.

Reduced version status:

READY.

Reduced contract:

1. Travel pauses at an authored world location.
2. Dispatch/priority decision occurs outside AutoPTU.
3. Resource members/equipment not selected as legal combatants remain outside BattleSpec.
4. AutoPTU resolves only a static tactical incident.
5. Travel and assignment state resume afterward.

Battle outcome never chooses which request has higher operational priority.

## Encounter review — Field Handoff Perimeter

Full intended objective:

Two response resources are transferring responsibility, information or already-authorized custody when a separate tactical threat interrupts the physical meeting.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement — PARTIAL for escort/Intercept
- action economy/initiative/core calculations — VERIFIED baselines
- lifecycle — PARTIAL for staged handoff/withdrawal
- damage/status/move/ability/item/Feature families — PARTIAL where selected combatants use them
- terrain/hazards/zones/reactions — BLOCKING for protected-object/access zones or generalized reactions
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- semantic adapter/playback — BLOCKING

Reduced version status:

READY.

Reduced contract:

1. Transfer remains `PENDING` outside battle.
2. Sensitive records, custody objects and controlled equipment remain outside BattleSpec.
3. Noncombat members withdraw.
4. AutoPTU resolves the perimeter.
5. The handoff owner separately resumes or cancels transfer.

`PERIMETER_CLEAR != HANDOFF_EFFECTIVE`.

## PTU / Caelo unresolved mechanics

Keep UNKNOWN unless exact governing source text and current implementation contracts are identified:

- universal dispatch actions;
- emergency response-time mechanics;
- generic rescue Skill checks;
- universal carry/drag/evacuation actions;
- Command automatically granting dispatch or command authority;
- Focus automatically granting incident leadership;
- General Education deciding operational priority;
- Medicine granting emergency-service authorization;
- Survival automatically locating reported actors;
- Technology Education operating every communication system;
- Trainer Classes functioning as institutional responder ranks;
- Features granting universal incident command;
- Pokémon species or Types granting responder qualification;
- automatic occupational competence from Moves or Abilities;
- radios or badges as PTU Items with invented effects;
- initiative order determining dispatch order;
- battle victory closing a request, search, repair, transport or assignment.

## Minecraft / Cobblemon guardrail

Minecraft and Cobblemon may present an already-authored operational state, such as:

- an empty crew bay;
- a staging area;
- a team travelling along an authored route;
- a coordinator NPC;
- a public job board;
- equipment being returned;
- an NPC waiting for a handoff;
- recurring Pokémon associated with a known team.

They do not author the state.

Entity coordinates do not prove arrival. Despawn does not prove departure. Proximity does not complete handoff. A held item does not transfer custody. Redstone does not create an authoritative emergency request. Cobblemon BattleState remains outside authority for combatant selection, legality, HP/status, tactical positions and narrative consequences.

## Pass 138 conclusion

The new narrative concepts can advance immediately in reduced form because dispatch/resource continuity lives outside combat and the tactical portions can be restricted to conventional static encounters.

Rich variants remain blocked by the same permanent families as prior passes. The new AutoPTU-Java commit strengthens correctness of a localized Intercept oracle-freezing path but does not justify a family-level promotion.