# Engine Readiness Snapshot — Pass 162

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `15666044162555ab9d6b73bec5a5c696acc2fbd6`
Date: 2026-08-31

## Read-only engine heads inspected

AutoPTU-Java:

`44537da6e93595f7533a734acc447d7623840c4d` — merged PR #300, `Freeze forced movement runtime callsite inventory`.

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

No engine file was modified by Pass 162.

## New Java evidence — PR #300

The latest AutoPTU-Java change is deliberately a boundary freeze before runtime binding, not evidence that complete forced movement is finished.

The inspected commit states that it:

- freezes the Python forced-movement runtime binding inventory;
- asserts Java forced movement remains runtime-unbound;
- gates future runtime binding against both engines;
- freezes callsite roles and context;
- adds a `ForcedMovementRuntimeBindingContractTest`.

The test scans Java production sources for calls to `RuntimeForcedMovementMoveApplication.apply` outside the implementation class and currently expects an empty callsite list. Its assertion explains the intent: Java forced-movement ordering must remain unbound until the pinned `battle_state` callsite order is frozen.

This is valuable architectural progress because it prevents accidental adapter/runtime ordering drift. It is also explicit negative evidence against promoting the permanent complete-movement family today.

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

No category is promoted in Pass 162.

## Why complete movement remains PARTIAL

Prior passes have positive evidence for server-owned Intercept planning, canonical combatant rule content, generic Push/Pull move metadata, stale-target revalidation, shared displacement/partial-stop logic and a Thrust Ability modifier branch.

PR #300 now freezes where Python invokes forced movement and ensures Java does not silently bind the path before ordering parity is understood.

Still not globally verified:

- production runtime binding of the generic forced-movement path;
- all Push/Pull sources and orderings;
- general Knockback;
- every Intercept variant and ordering interaction;
- arbitrary forced movement from statuses, terrain, Features or other sources;
- escort/rescue;
- object carrying;
- crowd routing;
- moving vehicles/platforms;
- generalized reaction windows;
- dynamic tactical objectives.

Therefore any rich electoral encounter that depends on escort, crowd withdrawal, protected-object movement or route-control remains blocked on exact families.

## AutoPTU evidence

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head explicitly describes viewport coordinate synchronization as presentation-only and says no battle rule or outcome changes. It creates no new mechanical evidence.

## PTU/Caelo electoral boundary

Internal source priority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List.

Pass 162 found no internal authority establishing a universal election subsystem.

UNKNOWN until exact source and current implementation review:

- universal voting/election Skill Checks;
- Charm, Command, Guile or Intimidate directly generating votes;
- election eligibility from Trainer class, level, Badge count or League rank;
- election victory from a battle result;
- Cheerleader, Coordinator or supporter mechanics becoming electoral support;
- Pokémon Loyalty representing voter support;
- Trainer Features granting civic mandate;
- Psychic/Aura truth verification for ballots or candidate claims;
- Moves/Abilities/Items authenticating electoral records;
- mechanical rewards for candidacy, turnout or office;
- any Caelo-specific political procedure.

The electoral continuity extension therefore remains narrative/procedural world state unless a specific mechanic is separately sourced and implemented.

## Encounter A — Polling Place Access Perimeter

Full version capability requirements:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected attacks require
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if dynamic hazards or protected zones matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protect/withdraw/route-control semantics
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic crowd/site playback

Overall full status: BLOCKED.

Reduced status: READY at narrative-contract level when the selected ordinary combat content is individually audited.

Before initiative, Ouros pauses the voting site and removes voters, staff, ballot material and other noncombatants from BattleSpec. Static geometry only. Permitted tactical output: `IMMEDIATE_POLLING_PLACE_APPROACH_CLEAR`.

Forbidden inference:

`BATTLE_WON != VOTING_RESUMED`

`BATTLE_WON != BALLOTS_CAST`

`BATTLE_WON != ELECTORAL_SUPPORT`

## Encounter B — Ballot Transport Chokepoint

Full version requires protected-object/escort semantics, complete movement, lifecycle, AI tactical policy and semantic adapter playback. Those requirements are not currently verified.

Overall full status: BLOCKED.

Reduced status: READY.

The authorized ballot container and its custody state are frozen outside BattleSpec before initiative. Players clear a static corridor. Permitted output: `IMMEDIATE_BALLOT_ROUTE_CLEAR`.

Courier and Electoral systems decide later transport state.

`IMMEDIATE_BALLOT_ROUTE_CLEAR != BALLOTS_DELIVERED`

`BALLOTS_DELIVERED != COUNTED`

`BATTLE_FAILURE_WITHOUT_CUSTODY_CONTRACT != BALLOTS_DESTROYED`

## Encounter C — Count Center Evacuation Perimeter

Full version can require civilian withdrawal, protected rooms, lifecycle, hazards/zones/reactions and objective-aware AI.

Overall full status: BLOCKED.

Reduced status: READY.

Ouros pauses the count and secures people and election materials outside the tactical slice. A static battle can produce only `IMMEDIATE_COUNT_CENTER_PERIMETER_CLEAR`.

`BATTLE_WON != COUNT_RESUMED`

`BATTLE_WON != RESULT_AUTHENTICATED`

`BATTLE_WON != DISCREPANCY_RESOLVED`

## Encounter D — Campaign Event Incident Separation

Full version may require crowd routing, dynamic barriers, withdrawal/protection objectives and adapter playback.

Overall full status: BLOCKED.

Reduced status: READY.

Ouros adjourns the appearance and removes crowd/campaign staff before initiative. Candidate presence in the world does not automatically place that actor in BattleSpec. Any conventional audited encounter resolves immediate safety only.

`CANDIDATE_PRESENT != COMBATANT`

`BATTLE_WON != VOTES_GAINED`

`BATTLE_LOST != CANDIDATE_WITHDRAWN`

## Noncombat readiness

The core Pass 162 systems are READY as narrative world-state architecture because they require no battle rules:

- candidate episode history;
- nomination/eligibility references;
- authored option sets;
- voting-window state;
- aggregate turnout/result records;
- preliminary versus confirmed result lineage;
- recount/review provenance;
- endorsement and poll separation;
- result handoff to Civic Office;
- archive/media/public-memory links.

They remain NON-CANON until a governing local rule is promoted.

## AI boundary

AI legal-action infrastructure remains VERIFIED. AI tactical policy remains BLOCKING for rich election-site incidents because legal-action enumeration does not prove that an actor understands semantic goals such as:

- protect an exit instead of maximizing damage;
- withdraw while preserving route access;
- avoid noncombatants;
- protect a container that is not a normal combat target;
- stop contesting once a route is clear.

Electoral support, crowd sentiment or campaign affiliation must never substitute for tactical policy.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon/Craftics may display already-authoritative posters, signs, crowds, desks, sealed containers, count boards and office-holder changes.

It may not derive:

- electorate from loaded NPCs;
- candidate eligibility from skins/classes;
- votes from player proximity or interactions unless Ouros explicitly records an authorized procedure;
- winner from scoreboard or crowd size;
- ballot validity from item NBT alone;
- civic mandate from Cobblemon BattleState;
- office transition from a visible NPC replacement;
- electoral support from Pokémon behavior;
- recount/certification from UI state.

Adapter/playback remains BLOCKING as a permanent category.

## Canon questions unresolved

- Does any Ouros office actually use an election?
- Which institutions define eligibility and procedure?
- Are any choices public votes rather than office selections?
- What participation and privacy models exist by region?
- Are options candidate-based, slate-based, issue-based or something else?
- Which counting and confirmation steps exist?
- Are recount/review routes available, and under what authored rule?
- What technology or physical artifacts represent voting?
- How are remote settlements included, if at all?
- How does a confirmed result hand off into Civic Office effective dates?
- Are political affiliations formal institutions anywhere in canon?
- Which PTU/Caelo Skills or Features, if any, have validated non-tactical relevance to campaigning without directly creating votes?

## Pass 162 conclusion

The electoral layer can exist safely as dormant procedural architecture. It activates only where canon explicitly supplies a governing electoral rule. Most candidate, voting-window, count, result and transition provenance is noncombat world state and can advance immediately.

Rich polling-site, transport, evacuation and crowd encounters remain blocked by the exact permanent capability families they require. PR #300 strengthens the project's authority boundary by freezing forced-movement callsites, but it explicitly leaves Java forced-movement runtime ordering unbound; no movement or other permanent category is promoted.