# Engine Readiness Snapshot — Pass 164

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `d447224b0a6f199ec389f958447cf293a80d71f8`
Date: 2026-08-31

## Read-only engine heads inspected

AutoPTU-Java:

`c4430969589577ef65d8409387b1f145f2910f45` — merged PR #302, `Freeze forced movement runtime instruction dataflow`.

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

No engine repository was modified by Pass 164.

## New Java evidence — PR #302

PR #302 extends the forced-movement parity contract again.

The inspected commit updates `tools/python/export_forced_movement_runtime_binding_contract.py` so the parity export can trace statements inside the relevant enclosing Python runtime function that use the `instruction` value. The trace records line, load/store-style context and compact rendered statements, and the CI workflow now emits the extra runtime trace artifact alongside the existing binding contract.

This matters because future Java production binding can be compared not only against the existence and local ordering of the pinned Python callsite, but also against the dataflow around the forced-movement instruction object.

This is positive implementation evidence for parity infrastructure.

It is not evidence that Java has now production-bound every forced-movement path. The previous Pass 163 snapshot explicitly recorded that `RuntimeForcedMovementMoveApplication.apply` remained without a production callsite outside its implementation class. PR #302 traces the Python instruction flow; it does not by itself prove that the missing Java runtime binding has been completed.

Therefore complete movement remains PARTIAL.

## Permanent capability map

VERIFIED:

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted in Pass 164.

## Why complete movement remains PARTIAL

Positive evidence accumulated across recent Java work includes:

- shared targeting and line geometry;
- server-owned Intercept candidate discovery and attempt planning;
- canonical combatant rule content used by Intercept;
- authoritative generic Push/Pull move metadata;
- current-state target and anchor revalidation before tested forced displacement;
- shared displacement and partial-stop behavior for tested branches;
- server-owned forced-movement Ability modifier handling for tested Thrust behavior;
- a frozen Python runtime callsite inventory;
- frozen local ordering context around that callsite;
- now a trace of instruction dataflow in the enclosing Python runtime function.

Still not globally verified:

- production Java binding of the complete forced-movement application path;
- full runtime-order parity after such binding;
- every Push source;
- every Pull source;
- general Knockback;
- every Intercept variant and ordering interaction;
- arbitrary forced movement from statuses, terrain, weather, Items, Features and other sources;
- escort/rescue movement;
- protected-object carrying;
- crowd routing;
- moving vehicles or platforms;
- generalized reaction windows;
- dynamic tactical objectives.

The employment encounters introduced in this pass therefore cannot assume that protect/escort/withdrawal movement is complete simply because representative Push/Pull/Intercept infrastructure exists.

## AutoPTU evidence

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head explicitly states that the viewport coordinate synchronization change is presentation-only and does not alter battle rules or outcomes.

It provides no new mechanical capability evidence for Pass 164.

## PTU/Caelo employment boundary

Internal source priority remains:

- PTU Core Rulebook;
- Pokédex material;
- Caelo Player's Guide;
- Caelo rulebook / errata;
- character-creation material;
- Caelo Region Location & Encounter List.

Public PTU reference material confirms that Trainer Classes include explicit Professional mechanical classes such as Chef, Chronicler, Fashionista, Researcher and Survivalist. This reinforces the existing project boundary: a narrative occupation or employer title must not be treated as a mechanical Trainer Class.

UNKNOWN until exact project-source and implementation review:

- a universal employment/profession subsystem;
- generic wages or salary formulas;
- downtime earnings rules adopted by Caelo;
- universal job-performance Skill Checks;
- interview, hiring or promotion DCs;
- employment-based Trainer XP;
- automatic Skill Rank, Edge, Feature, Class or Move rewards from work tenure;
- Trainer Level, Badge or class prerequisites for ordinary employment;
- mechanical bonuses from employer reputation;
- unemployment mechanics;
- retirement mechanics;
- leave mechanics;
- contract or dismissal mechanics;
- occupational licenses created by PTU mechanics;
- any Caelo-specific ranger, researcher, League, craft or professional-employment procedure;
- Pokémon employment status or wage rules;
- Loyalty changes from human employment events;
- compensation calculations outside the authoritative money system.

Pass 164 therefore remains a narrative continuity layer unless a particular job scene invokes an exact verified PTU/Caelo mechanic.

## Encounter A — First-Day Access Interruption

Narrative premise:

A newly starting worker and a supervisor need access to the workplace while a separate tactical conflict occupies the approach.

Full version capability requirements:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected combat content requires
- status lifecycle — PARTIAL as selected combat content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if changing access, active hazards or reactive protection matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protect/withdraw/route-control semantics
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic noncombat staff and onboarding playback

Overall full status: BLOCKED.

Reduced status: READY at narrative-contract level when the selected ordinary battle content is individually audited.

Before initiative, Ouros moves the new worker, supervisor and onboarding materials outside BattleSpec and freezes static geometry. AutoPTU may resolve only the explicitly selected combatants.

Permitted output:

`IMMEDIATE_WORKPLACE_APPROACH_CLEAR`

Forbidden inferences:

`IMMEDIATE_WORKPLACE_APPROACH_CLEAR != EMPLOYMENT_STARTED`

`BATTLE_WON != ONBOARDING_COMPLETED`

`BATTLE_WON != NEW_WORKER_PROVEN_COMPETENT`

## Encounter B — Shift Handover Perimeter

Narrative premise:

Outgoing and incoming workers overlap during a shift/responsibility handoff when a tactical incident begins nearby.

Full version capability requirements:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as roster requires
- status lifecycle — PARTIAL as roster requires
- terrain/weather/hazards/zones/reactions — BLOCKING if the site has active tactical hazards or reaction windows
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for safe-withdrawal/protection objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic staff, credential and equipment playback

Overall full status: BLOCKED.

Reduced status: READY.

The handoff pauses before initiative. All noncombat staff, keys, credentials, task records and issued property remain outside BattleSpec. Static combat may return only:

`IMMEDIATE_HANDOVER_PERIMETER_CLEAR`

Forbidden inferences:

`BATTLE_WON != HANDOVER_COMPLETE`

`BATTLE_WON != RESPONSIBILITY_TRANSFERRED`

`OUTGOING_WORKER_PRESENT != EMPLOYMENT_STILL_ACTIVE`

## Encounter C — Departure-Day Equipment Return Perimeter

Narrative premise:

A worker whose tenure is ending is returning issued property when an unrelated confrontation blocks access to the return point.

Full version capability requirements:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if active site conditions matter
- move-specific behavior — PARTIAL; audit required
- abilities — PARTIAL; audit required
- items — PARTIAL; battle Items only; employment equipment is not automatically a PTU Item
- Trainer Features/perks — PARTIAL; audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protected-object/escort objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic custody/equipment playback

Additional missing semantic capability:

protected-object carrying/escort is not verified as a complete engine family.

Overall full status: BLOCKED.

Reduced status: READY.

The issued property is secured outside BattleSpec before initiative. AutoPTU resolves a conventional static confrontation and can return only:

`IMMEDIATE_RETURN_POINT_ACCESS_CLEAR`

Forbidden inferences:

`ACCESS_CLEAR != EQUIPMENT_RETURN_ACCEPTED`

`EQUIPMENT_RETURNED != EMPLOYMENT_SEPARATION_COMPLETE`

`EQUIPMENT_NOT_RETURNED != MISCONDUCT`

## Encounter D — Emergency Coverage Access Chokepoint

Narrative premise:

A staff member assigned to temporary coverage must reach a thinly staffed service location while a local confrontation blocks the route.

Full version capability requirements:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected attacks require
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when route conditions are tactical
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for clear-route/protect/withdraw semantics
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for worker/service playback

Overall full status: BLOCKED.

Reduced status: READY.

The coverage worker remains a world-state actor outside BattleSpec. Ouros freezes the route geometry and AutoPTU may return only:

`IMMEDIATE_COVERAGE_ROUTE_CLEAR`

Forbidden inferences:

`BATTLE_WON != COVERAGE_STARTED`

`COVERAGE_STARTED != SERVICE_FULLY_RESTORED`

`ROUTE_CLEAR != STAFFING_NEED_RESOLVED`

## Noncombat readiness

The core Pass 164 architecture is READY as narrative world-state design because it can operate without tactical rules:

- employment opportunities and vacancies;
- applications/candidacies;
- selection records;
- offer versions;
- accept/decline/expiry state;
- pre-start and onboarding records;
- tenure start/end;
- responsibility changes;
- authored temporary leave and return;
- evidence-backed separation;
- rehire links;
- successor lineage;
- compensation references to Finance;
- employment-record correction lineage;
- simultaneous jobs and other roles;
- former-worker continuity.

All generated concrete content remains NON-CANON until reviewed.

## AI boundary

AI legal-action infrastructure remains VERIFIED.

AI tactical policy remains BLOCKING for rich employment/workplace incidents because knowing which actions are legal does not prove an actor can optimize for semantic goals such as:

- protect a noncombat worker rather than maximize damage;
- withdraw while preserving an access corridor;
- stop contesting once the route is clear;
- avoid an issued object that is not a legal combat target;
- coordinate a handover perimeter;
- escort a world-state actor who should not be represented as a combatant;
- distinguish temporary route clearance from defeating every opponent.

Employment priority, job title or seniority must never substitute for tactical policy.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon/Craftics may display already-authoritative:

- vacancy boards;
- staff rosters;
- uniforms;
- workstations;
- onboarding scenes;
- issued equipment;
- credential-return scenes;
- staff presence/absence derived from schedules;
- counters temporarily closed because Workplaces says coverage is unavailable;
- former employees appearing later in other contexts.

It may not derive:

- employment from an NPC skin;
- resignation from entity absence;
- promotion from workstation position;
- authority from possession of a credential item;
- mechanical qualification from a job title;
- PTU Trainer Class from an occupation;
- compensation from item transfer;
- tenure start from chunk loading;
- separation from despawn;
- battle participants from nearby employees;
- tactical bonuses from professional status.

Adapter/playback remains BLOCKING as a permanent category.

## Canon questions unresolved

- Which Ouros institutions use human employment rather than volunteering, public office, membership, patronage or temporary collaboration?
- Which workplaces publish vacancies publicly?
- Which use referrals, appointments or internal succession?
- Which credentials or qualifications govern specific roles?
- What employment terms and role labels exist region by region?
- Are there seasonal or fixed-duration employment relationships?
- Does any institution formally use leave categories?
- Which compensation models exist in canon?
- Is payroll or banking infrastructure present, and where?
- What records are public versus private?
- What separation labels are actually used?
- Are unions, guilds or collective bargaining institutions present at all?
- Is there any labor-law layer, or should the world remain institution-specific?
- What employment-related mechanics, if any, are actually defined in the supplied PTU/Caelo source set?
- Does Caelo alter professional Trainer Classes in ways relevant to occupational stories?
- Can Pokémon ever hold an employment-like legal/social status, or should their work continue to use the bounded participation model?
- Which current NPC career histories are strong candidates for the first canon employment-tenure migrations?

## Pass 164 conclusion

Ouros can now model human career transitions as provenance-rich world state without inventing labor law or mechanical progression. The new layer distinguishes opportunity, selection, offer, acceptance, actual start, active tenure, temporary absence, return, separation, rehire and succession while delegating staffing, money, credentials, training and tactical resolution to their existing authorities.

PR #302 strengthens the forced-movement parity contract by exposing Python instruction dataflow around the pinned runtime path. It does not prove production Java binding or complete movement parity. Consequently every mechanically rich employment encounter remains blocked by its exact missing capability families, while reduced static versions can proceed without changing the narrative premise.
