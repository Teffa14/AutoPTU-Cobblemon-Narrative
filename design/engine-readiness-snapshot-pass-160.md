# Engine Readiness Snapshot — Pass 160

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `de30653dc78698bada82288a8e61c1908dd8ba57`
Date: 2026-08-31

## Read-only engine heads inspected

AutoPTU-Java:

`e8bbd584cd55654b72d52117ee410d7e738f93b6` — merged PR #297, `Revalidate forced-movement target before displacement`.

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

No files in either engine repository were modified by Pass 160.

AutoPTU-Java advanced after Pass 159. AutoPTU did not.

## New Java evidence

The inspected current Java diff strengthens generic forced-movement authority beyond the earlier Intercept-only slices.

`RuntimeForcedMovementMoveApplication` is described as the server-owned bridge from a currently legal combatant-target move to generic Push/Pull execution.

Before displacement, core now:

- receives a declared `MoveChoice` rather than a caller-selected source/target/move tuple;
- resolves the move from the combatant's canonical server-owned moveset;
- revalidates actor, target and move choice against current battle state;
- checks current targeting/range/anchor legality through `MoveChoiceRevalidation`;
- rejects a stale or out-of-range target before position mutation;
- derives a forced-movement instruction from canonical move metadata;
- delegates actual displacement to the shared forced-movement application path.

The merged tests shown in the diff cover at least:

- Push derived from authoritative move effects with shared partial-stop behavior;
- Pull derived from authoritative move metadata;
- out-of-range target rejection before movement;
- stale target anchor rejection before movement;
- rejection of a move not owned by the source combatant;
- requirement for a server-owned canonical moveset.

This is material progress for generic Push/Pull authority and stale-choice safety.

It does not verify the entire permanent movement family.

Still unverified globally include:

- exhaustive Push move coverage;
- exhaustive Pull move coverage;
- general Knockback semantics and all sources;
- every Intercept variant and ordering interaction;
- arbitrary forced movement from non-move sources;
- escort/rescue movement;
- object carrying;
- crowd routing;
- moving vehicles/platforms/scenery;
- generalized reaction windows;
- dynamic objective zones;
- tactical protect/deny/withdraw/evacuate policy.

Therefore the permanent category `complete movement including push/pull/knockback/interception/forced movement` remains PARTIAL.

The AutoPTU head remains explicitly presentation-only. Its commit message states that viewport-resize coordinate synchronization changes presentation and no battle rules or outcomes.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No permanent capability category is promoted by Pass 160.

## Why forced movement remains PARTIAL

The new evidence is broader than Pass 159 because a generic Push/Pull move bridge now uses canonical move metadata and revalidates the current move choice before displacement.

That is enough to record positive evidence for specific Push/Pull execution paths.

It is not enough to declare the family complete. The category intentionally contains Push, Pull, Knockback, Interception and other forced movement. Representative implementations do not prove exhaustive coverage, ordering, source interactions, lifecycle integration or adapter playback.

Pass 160 therefore follows the project's permanent rule: no category promotion from one or several representative mechanics without evidence that the full category contract is covered.

## Supporter mechanics qualification

Public PTU reference material contains explicit Trainer Classes and Features. Cheerleader appears as a battling-style class in the public PTU class index. Public community material also contains non-core Fan Club/Celebrity designs.

For Ouros this produces a strict separation:

- supporter membership is narrative/social state;
- cheering in fiction has no automatic mechanical output;
- applause does not grant AP, movement, accuracy, damage, Skill modifiers, initiative or reputation;
- a supporter NPC is not automatically a Cheerleader-class Trainer;
- a crowd cannot trigger a Feature unless the exact actor, Feature, trigger, cost, target and engine implementation are verified;
- community Fan Club/Idol Score/Celebrity designs are not imported as PTU/Caelo authority.

Caelo-specific retention or modification of Cheerleader, Coordinator, Fame, social Features or campaign reputation remains unresolved until exact project source material is reviewed.

## Encounter A — Away Support Arrival Chokepoint

Narrative premise: a visiting supporter group reaches an access area while a separate hostile or wild-Pokémon incident blocks the immediate route.

Required capability families for the full version:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for static legal geometry
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL for contested route control and displacement
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for staged arrival/withdrawal phases
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if access zones, generalized reactions or active hazards matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for route control, delay, protect and withdrawal decisions
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative crowd/arrival playback

Overall full status: BLOCKED.

Reduced status: READY at narrative-contract level if selected combat content is individually audited.

Reduced constraints:

- supporters, venue staff and noncombatant Pokémon remain outside BattleSpec;
- their safe holding state is established before initiative;
- arena geometry is fixed;
- explicit combatants only;
- no crowd-routing, escort or evacuation objective occurs inside AutoPTU;
- permitted battle output: `IMMEDIATE_ARRIVAL_ACCESS_CLEAR`.

Hard safeguards:

`IMMEDIATE_ARRIVAL_ACCESS_CLEAR != SUPPORTERS_ENTERED_VENUE`

`BATTLE_WON != ATTENDANCE_CONFIRMED`

`CROWD_VISIBLE != CROWD_TACTICALLY_SIMULATED`

## Encounter B — Supporter Archive Recovery Perimeter

Narrative premise: an archive or club room containing supporter-created records must become physically approachable during a separate incident.

Full-version needs may include:

- complete movement for rescue/object movement;
- full turn/round lifecycle for timed deterioration;
- terrain/weather/hazards/zones/reactions for smoke, unstable access or changing danger;
- AI tactical policy for denial/protection objectives;
- adapter/playback for semantic archive and hazard state.

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- archive material and custodians remain outside BattleSpec;
- no object carrying, fire/smoke, collapsing shelves or rescue semantics are simulated;
- geometry is static;
- permitted result: `IMMEDIATE_ARCHIVE_APPROACH_CLEAR`.

Hard safeguards:

`IMMEDIATE_ARCHIVE_APPROACH_CLEAR != ARCHIVE_RECOVERED`

`BATTLE_WON != ARTIFACT_CUSTODY_TRANSFERRED`

`ARCHIVE_DAMAGED_VISUALLY != CANONICAL_RECORD_DESTROYED`

## Encounter C — Venue Exit Separation Perimeter

Narrative premise: two supporter communities need distinct exit routes after an event while one immediate perimeter contains a tactical threat.

Full version requires crowd routing, protected objectives, generalized reactions, complete withdrawal semantics and objective-aware tactical policy.

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- supporter communities are never tactical units;
- their exit plans are authored outside BattleSpec;
- battle occurs on a fixed perimeter among explicit combatants only;
- permitted result: `IMMEDIATE_EXIT_PERIMETER_CLEAR`.

Hard safeguards:

`IMMEDIATE_EXIT_PERIMETER_CLEAR != SUPPORTER_GROUPS_EXITED`

`PERIMETER_CLEAR != SUPPORTER_GROUPS_RECONCILED`

`SUPPORTER_GROUP_PROXIMITY != HOSTILITY`

## Encounter D — Public Figure Departure Corridor

Narrative premise: a retiring, transferring or visiting public figure needs a physically clear departure corridor during an unrelated hostile incident.

Full version can require escort, contested withdrawal, Intercept, forced movement, generalized reactions and tactical protect policy.

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- public figure and supporters move outside BattleSpec before initiative;
- explicit combatants resolve a static chokepoint;
- AutoPTU may establish only `IMMEDIATE_DEPARTURE_CORRIDOR_CLEAR`.

Hard safeguards:

`IMMEDIATE_DEPARTURE_CORRIDOR_CLEAR != DEPARTURE_COMPLETED`

`DEPARTURE_COMPLETED != SUPPORTER_RELATIONSHIP_ENDED`

`BATTLE_RESULT != RETIREMENT_DECISION`

## AI boundary

AI legal-action infrastructure remains VERIFIED at the permanent-category level.

AI tactical policy remains BLOCKING for the new full encounter versions because they ask agents to understand semantic objectives such as:

- protect a route rather than maximize damage;
- delay without necessarily engaging every target;
- withdraw when access is clear;
- avoid noncombatant supporter areas;
- distinguish archive denial from ordinary KO priority;
- preserve separation between supporter groups.

Legal-action enumeration alone does not demonstrate those policies.

## Adapter/playback boundary

Minecraft/Cobblemon/Craftics may present already-authoritative supporter state through crowds, banners, signs, queues, clothing, meeting points, seating sections and travel arrivals.

It may not derive:

- supporter membership from skin, proximity or entity tags;
- loyalty from repeated attendance;
- hostility from crowd collision;
- PTU buffs from cheering animations;
- combatants from nearby crowd entities;
- faction membership from colors;
- boycott success from despawned entities;
- public belief from client-visible text;
- route success from Minecraft pathfinding.

Because semantic adapter/playback authority is not verified end to end, the permanent category remains BLOCKING.

## PTU/Caelo unresolved mechanics

UNKNOWN until exact source review:

- whether Caelo retains or modifies Cheerleader Features;
- any Caelo Fame, celebrity, reputation or supporter-specific subsystem;
- any Coordinator or performance Feature that interacts with audiences outside formal Contest rules;
- whether Charm, Command or Intimidate have authored supporter-management uses in this campaign;
- any mechanic that changes crowd disposition directly;
- any Feature that creates followers, fan clubs or entourage NPCs;
- any reward/progression rule tied to attendance or public popularity;
- any mechanically authoritative supporter liaison or sponsorship effect.

Community-created Fan Club/Celebrity mechanics found during research remain non-authoritative evidence and must not be silently adopted.

## Canon unresolved questions

The following setting facts remain UNRESOLVED:

- which Ouros Trainers, Gyms, performers, institutions or other public figures have durable supporter communities;
- whether any supporter organizations are formal associations;
- which venues have dedicated supporter sections or customs;
- which group practices have become true traditions;
- which fan-created artifacts are established Material Culture objects;
- whether any current faction originated from a supporter organization;
- what technology supports remote fan communities or watch events in each region;
- whether any public figure has an established liaison role;
- which supporter splits, mergers, boycotts or travel traditions are historical canon;
- what player-character consent boundary applies when public success creates proposed supporter attention.

## Pass 160 conclusion

The new narrative concepts can proceed now through supporter identity, membership provenance, local practices, group transitions, artifacts, media links, away travel and public-attention continuity without requiring new battle mechanics.

Mechanically rich crowd, escort, evacuation, object-recovery and route-control versions remain blocked by the exact families listed above. Reduced static encounters preserve the narrative premise without forcing Minecraft or Narrative to implement missing PTU rules.

No engine capability category is promoted in this pass.