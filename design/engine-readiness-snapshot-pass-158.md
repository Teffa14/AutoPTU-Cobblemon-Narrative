# Engine Readiness Snapshot — Pass 158

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `7c9c6025cbbe12e6669ab58787d493017a634907`
Date: 2026-08-30

## Read-only engine heads inspected

AutoPTU-Java:

`d5d06f4a5e646b00cd09da09c59707f5fa24acdd` — `Internalize Intercept attempt planning at PRE-target boundary` via merged PR #292.

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

No files in either engine repository were modified by Pass 158.

AutoPTU-Java advanced since Pass 157. AutoPTU did not.

## New Java evidence

The current Java head moves another part of Intercept planning behind the authoritative PRE-target boundary.

The inspected commit changes `RuntimeInterceptPreResolutionTargetHook` so external orchestration no longer passes a prepared list of Intercept attempts. External orchestration may identify the normalized Intercept kind and provide canonical combatant rule content. The runtime internally performs candidate discovery, expiry cleanup, candidate ordering, attack-line geometry, Shift legality, RNG/resource use and displacement.

Tests also assert that adapters cannot inject prepared attempts or attack-line coordinates through the hook plan. An active `no_intercept` condition is applied by the internal planner before the spatial sequence in the inspected regression coverage.

This is valuable evidence for server-owned Intercept authority and reduces another avenue for Minecraft/Cobblemon to determine tactical facts.

It remains localized evidence. It does not prove the whole complete-movement or reaction families.

Still unverified globally include:

- every Push source;
- Pull;
- general Knockback;
- every Intercept form and ordering interaction;
- arbitrary forced movement;
- escort/rescue semantics;
- object carrying;
- dynamic objectives and zones;
- moving barriers or vehicles;
- generalized reaction windows and ordering;
- tactical protect/deny/withdraw/delay policy;
- full semantic adapter/playback coverage.

The AutoPTU head remains presentation-only and explicitly states that it changes no battle rules or outcomes.

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

No category is promoted by Pass 158.

## Pressure Drill: Protect the Marker — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for static legal movement
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL if the drill relies on displacement or Intercept
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for changing objective phases or round-scoped drill rules
- full stateful damage pipeline — PARTIAL as selected combat content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING for a semantic protect/deny zone or generalized reaction windows
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for understanding protect, deny, bait, delay or route-control goals
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative objective-state presentation

Overall full status: BLOCKED.

Reduced status: READY at narrative-contract level if selected Moves, Abilities, Items and Features are individually audited.

Reduced constraints:

- marker is static scenery and carries no tactical rules state;
- fixed arena geometry;
- explicit combatants;
- conventional reviewed battle contract;
- coach observations are derived from authoritative battle events after resolution;
- permitted result: `STATIC_SPARRING_COMPLETED` plus bounded observations.

Hard safeguards:

`SPARRING_COMPLETED != PROTECTION_MASTERY`

`BATTLE_WON != TRAINING_OBJECTIVE_SATISFIED`

`COACH_FEEDBACK != MECHANICAL_BONUS`

## Positioning Labyrinth Scrimmage — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for static geometry
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL if displacement or Intercept matters
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for between-round layout changes
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING for changing walls, semantic route zones or reaction windows
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for route-control or pedagogical objective awareness
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for dynamic geometry and semantic playback

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- all blockers are frozen before initiative;
- no moving walls, sliding zones or scripted displacement;
- ordinary audited targeting and movement only;
- permitted result: `FIXED_LAYOUT_SCRIMMAGE_COMPLETED`.

`FIXED_LAYOUT_SCRIMMAGE_COMPLETED != POSITIONING_MASTERY`

## Partner Rotation Exercise — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL as selected content requires
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for staged participant changes under one encounter lifecycle
- full stateful damage pipeline — PARTIAL if state persists between stages
- status lifecycle — PARTIAL if state persists between stages
- terrain/weather/hazards/zones/reactions — BLOCKING if any partner-specific stage uses them
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for adaptive partner-specific behavior
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative staged handoff playback

Overall full status: BLOCKED as one continuously mutating BattleSpec.

Reduced status: READY.

Reduced constraints:

- each pairing is a separate BattleSpec;
- Ouros performs an explicit session checkpoint between battles;
- no HP, status, initiative, item consumption or tactical state crosses BattleSpecs unless a separately verified contract authorizes it;
- each authoritative result links back to one training thread.

Hard safeguard:

`SAME_TRAINING_SESSION != SAME_BATTLE_STATE`.

## Intercept Demonstration — intended full version

The current Java evidence makes this concept especially useful for documenting the difference between a verified representative mechanic and a verified family.

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL despite stronger Intercept evidence
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING as a generalized family even though one Intercept path is increasingly internalized
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Overall full status: BLOCKED as a guaranteed rich pedagogical scenario.

Reduced status: READY.

Reduced constraints:

- encounter completion does not depend on Intercept firing;
- if Intercept legally occurs through the current authoritative path, Narrative may preserve the actual semantic event for review;
- Minecraft/Cobblemon cannot fabricate an Intercept trigger, candidate, position or success to make the lesson happen;
- a missed demonstration may simply produce an inconclusive practice observation.

Hard safeguards:

`INTERCEPT_SLICE_IMPLEMENTED != COMPLETE_MOVEMENT_VERIFIED`

`INTERCEPT_EVENT_OBSERVED != GENERAL_REACTION_SUPPORT_VERIFIED`

`INTENDED_LESSON != SCRIPTED_TACTICAL_OUTCOME`

## Training/progression authority boundary

Pass 158 gives Narrative continuity authority only over authored or evidence-supported facts such as:

- stated practice goals;
- practice plans and revisions;
- sessions that actually occurred;
- participants, observers and venues;
- authoritative battle references;
- attributed coach feedback;
- bounded demonstrations;
- interruptions and resumptions;
- references to separately authorized PTU/Caelo progression transactions.

It does not give Narrative authority to manufacture:

- Trainer XP;
- Pokémon XP;
- Skill Ranks;
- Edges;
- Features;
- Tutor Points;
- Move learning;
- Ability changes;
- stat changes;
- Retraining outcomes;
- Loyalty changes;
- injury policy;
- formal qualification;
- tactical AI adaptation;
- universal coaching bonuses.

## PTU/Caelo evidence boundary

Public PTU references show that Mentor/Move Tutor effects and Retraining use explicit prerequisites, costs, target restrictions and transaction rules. Therefore the narrative training layer must never replace those mechanics with “trained for enough sessions.”

Remain UNKNOWN until project source-check and adoption review:

- exact Caelo modifications to Mentor, Move Tutor or Tutor Points;
- exact Caelo Retraining changes;
- sparring injury/recovery policy;
- any Caelo downtime training rewards;
- whether specific Skills/Features permit teaching outside the public PTU Mentor structure;
- any mechanical effect from coaching, drills or repeated practice;
- any formal requirement that ties session count to advancement.

## Minecraft/Cobblemon/Craftics boundary

Presentation may show approved training venues, coaches, learners, practice props, fixed blockers, session schedules, animations and semantic battle playback after Ouros/AutoPTU decide the state.

Minecraft/Cobblemon/Craftics cannot decide:

- combatants;
- BattleSpec roster;
- PTU HP/status/damage;
- legal training rewards;
- mastery;
- Tutor legality;
- Retraining completion;
- Intercept candidates or outcome;
- coach correctness;
- qualification;
- tactical AI policy.

## Pass conclusion

The Java PRE-target Intercept boundary is materially stronger than in Pass 157: candidate and attempt materialization is now internal to authoritative runtime orchestration, including discovery, cleanup, ordering, geometry, Shift legality, RNG/resource use and displacement. This does not justify promotion of complete movement, generalized reactions or tactical AI.

Training concepts therefore use static reduced variants for current implementation planning, while all progression effects remain explicit handoffs to PTU/Caelo-authoritative transactions.