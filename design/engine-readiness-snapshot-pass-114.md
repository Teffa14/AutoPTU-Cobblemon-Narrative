# Engine Readiness Snapshot — Pass 114

Status: EVIDENCE SNAPSHOT. This file records live implementation evidence used by narrative authoring. It does not change engine capability status by itself.

Date: 2026-08-28

## Read-only repositories inspected

AutoPTU-Java head inspected:

`fedf0b21cafb2d3e56ddbb3f0d3487353ce6d74c`

PR/commit #266: `Route pre-resolution replacement through authoritative move pipeline`.

AutoPTU head inspected:

`bbbb31417bc7c6c216c7f80fab049bd630a97d49`

PR #222 merge: `Career: lazy-load trainer portraits and drop 2.1 MB sheet`.

Neither repository was modified by Pass 114.

## Java change since Pass 113

Pass 113 inspected Java head:

`f54ebc6862c3238e4e424da879fa99a93c0c46c1`

Java has since advanced to:

`fedf0b21cafb2d3e56ddbb3f0d3487353ce6d74c`

The new slice wires the previously prepared pre-resolution effective target into the authoritative move runtime pipeline.

The commit adds an `applyAuthoritativeMoveWithPreResolutionTargets` composition seam. The declared Move choice is first validated against the controller-selected target. The PRE-resolution target registry may then replace the effective defender. The effective choice and defender-bound preparation enter the ordinary authoritative move pipeline without treating the replacement as a new controller declaration.

The regression test verifies that:

- the replacement target becomes the defender observed by downstream pre-damage reaction handling;
- defender-bound type interaction comes from the effective target;
- damage is applied to the interceptor/effective target rather than the originally protected target;
- damage history records the effective defender;
- the semantic Intercept event appears before final Move resolution;
- MoveResolved identifies the effective target;
- ordinary action economy is spent once;
- Move frequency usage is spent once.

This is meaningful live evidence that one target-replacement path now runs through more of the authoritative Move pipeline rather than existing only as a detached helper.

## Why no capability family is promoted

PR #266 remains narrow evidence around a particular pre-resolution target-replacement composition seam.

It does not demonstrate broad completion of:

- Push/Pull;
- Knockback;
- every forced-movement source;
- environmental displacement;
- every Intercept trigger/window/contest;
- generalized competing reactions;
- generalized reaction ordering across all reaction families;
- every Move registration;
- every Ability registration;
- every Item registration;
- every Trainer Feature/perk registration;
- full environmental terrain/hazard/zone semantics;
- complete full-turn/round lifecycle;
- complete stateful damage/status behavior;
- objective-aware tactical policy;
- semantic Minecraft/Cobblemon/Craftics playback.

A registry that can host a source type does not prove every source of that type exists.

A tested effective-target path does not prove the complete movement/reaction family exists.

## AutoPTU change since Pass 113

Pass 113 inspected AutoPTU head:

`f1c81f5a20dfdbd4986e1c28083d9bbeb2f71bd1`

AutoPTU has advanced to:

`bbbb31417bc7c6c216c7f80fab049bd630a97d49`

PR #222 changes Career trainer portrait loading. It removes the multi-megabyte portrait sheet, selects deterministic role-specific trainer sprites and loads images lazily/asynchronously. Tests lock the lightweight loading contract and selected trainer sprite behavior.

This is UI/performance/presentation work.

It does not add targeting, movement, combat calculations, turn lifecycle, damage, status, environmental reactions, AI policy or Minecraft adapter semantics.

No tactical capability promotion follows.

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

No permanent category is promoted in Pass 114.

## Pass 114 authoring boundary

Slope-instability continuity is primarily world-state and evidence management.

The following can proceed without dynamic environmental combat simulation:

- slope-sector identity;
- observations;
- monitoring gaps;
- assessments and revisions;
- failure-event records;
- footprint revisions;
- route/infrastructure handoffs;
- debris-clearing history;
- stabilization/verification handoffs;
- route-access decisions by owner systems;
- legacy route/history content;
- investigations based on maps, timestamps and provenance.

Active slope movement inside BattleSpec is a separate problem and remains mechanically constrained.

## Encounter 1 — Switchback Withdrawal

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL for timed withdrawal or changing conditions
- full stateful damage pipeline: PARTIAL if falling material can damage
- status lifecycle: PARTIAL if an exact legal condition applies
- terrain/weather/hazards/zones/reactions: BLOCKING for active falling-rock zones, unstable cells, dynamic exclusion areas or generalized reactions
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for objective-aware withdrawal/protection behavior
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

Current authoring profile: REDUCED.

Reduced version:

Complete ordinary withdrawal before BattleSpec creation. Keep the unstable slope, active debris, workers, vehicles and nonparticipating Pokémon outside the tactical grid. Use a static reviewed road turnout or safe edge. No falling-rock, collapse, sliding or changing-zone rule runs during combat. A battle result may secure the immediate perimeter only. Slope assessment and Road Operations remain authoritative for access.

## Encounter 2 — Survey Marker Perimeter

Full intended dependencies:

- verified targeting/base movement/core/action economy/legal-action infrastructure;
- PARTIAL complete movement if Intercept, escort or forced movement matters;
- PARTIAL turn lifecycle for timed protection windows;
- BLOCKING terrain/hazards/zones/reactions if cells change state or equipment creates tactical zones;
- PARTIAL damage/status if environmental effects can harm or condition actors;
- PARTIAL Move/Ability/Item/Trainer Feature behavior for any exact interactions;
- BLOCKING AI tactical policy for protection/exclusion/withdrawal goals;
- BLOCKING adapter/playback.

Current authoring profile: REDUCED.

Reduced version:

Complete survey setup or withdrawal outside combat. Keep instruments and unstable sectors out of BattleSpec. Resolve any hostile/territorial contact on a stable static platform or clearing. Victory does not validate readings, repair monitoring, stabilize the slope or change assessment state.

## Encounter 3 — Debris Fan Diversion

The historical deposit can already support an encounter when treated as inert reviewed geometry.

If designers add loose footing, sliding material, mud, dust, falling debris, changing cover, renewed flow or dynamic route loss, the encounter gains explicit dependencies on:

- terrain/weather/hazards/zones/reactions: BLOCKING;
- complete movement: PARTIAL where displacement/sliding applies;
- full turn/round lifecycle: PARTIAL for delayed/phased changes;
- full stateful damage pipeline: PARTIAL where damage applies;
- status lifecycle: PARTIAL where conditions apply;
- move-specific behavior, abilities, items, Trainer Features/perks: PARTIAL when they interact;
- AI tactical policy: BLOCKING when agents must reason about changing environmental risks;
- adapter/playback: BLOCKING.

Reduced version:

Treat the old debris fan as static ordinary geometry. Its slope-event history, route effects, ecology and public memory remain active world-state content, but no environmental battle mechanic is inferred.

## PTU/Caelo mechanical unknowns for Pass 114

Current evidence does not verify a universal contract for:

- natural landslide timing;
- landslide probability/susceptibility as a game statistic;
- rainfall-trigger thresholds;
- earthquake-trigger formulas;
- volcanic-trigger formulas;
- slope angle or material-strength calculations;
- active rockfall trajectories;
- falling-rock environmental damage;
- burial or suffocation from debris;
- debris-flow forced movement;
- dynamic collapse cells;
- unstable-edge checks;
- mud/debris Slow Terrain by default;
- dust visibility or respiratory status;
- structural collapse caused by slope movement;
- road-clearing rates;
- stabilization engineering;
- automatic Rock/Ground-type environmental immunity;
- species-derived landslide sensing or prediction;
- generic Pokémon-caused landslide effects from flavor;
- Move/Ability/Item/Trainer Feature-powered slope control without exact rule support;
- rescue/carry during active mass movement;
- complete objective-aware evacuation/protection semantics.

These remain UNKNOWN rather than being implemented by the narrative layer or Minecraft adapter.

## PTU/Caelo guardrail

The internal source scan remains controlling.

Caelo proves that a specific authored location can have a defined mechanical environmental identity when a governing source says so.

It does not authorize universal conversions such as:

- gravel block = unstable terrain;
- falling block = PTU damage;
- mud = Slow Terrain;
- cliff = fall hazard;
- dust particles = LoS/status effect;
- water flow = debris-flow forced movement;
- Rock/Ground type = safe from slope failure.

Before a slope effect enters BattleSpec mechanically, authoring needs both:

1. an exact governing PTU/Caelo rule for the intended effect; and
2. current tests/contracts for every permanent capability family the effect requires.

Otherwise the condition remains overworld state, inert scenery or excluded tactical geometry.

## Minecraft/Cobblemon/Craftics boundary

Presentation may reuse:

- cliffs, scree, boulders and debris;
- old/new road alignments;
- blocked tunnels or paths;
- barriers and signs;
- survey/monitoring props;
- particles and sounds;
- NPC crews;
- Pokémon entities, models, forms, poses, animations and cries;
- maps/UI;
- networking, tracking and persistence hooks.

The adapter must preserve authoritative IDs for sectors, observations, failure events, footprint revisions, impact handoffs and access references when those objects exist.

Presentation must not infer battle/world authority from native behavior:

- Minecraft falling blocks do not execute PTU damage;
- gravel/sand physics do not decide a slope event;
- native knockback does not execute PTU forced movement;
- water spread does not resolve debris-flow movement;
- Minecraft suffocation does not implement burial mechanics;
- pathfinding does not complete evacuation or rescue;
- a physical block pile disappearing does not prove clearing/verification;
- an open road in geometry does not prove Road Operations reopened it;
- redstone does not establish monitoring truth;
- nearby Pokémon are not selected as combatants by proximity;
- Cobblemon BattleState/controller logic does not decide participants, legality, HP/status, positions or outcomes.

Ouros owns world facts and combatant selection. AutoPTU owns tactical legality and resolution. Minecraft/Cobblemon/Craftics presents authoritative outcomes.

## Canon questions carried forward from Pass 114

Unresolved setting questions include:

- which Ouros regions contain meaningful slope-instability history;
- which roads, railways, settlements, water systems or habitats intersect those sectors;
- which major historical events permanently changed regional topology;
- which monitoring technologies exist;
- which institutions or local actors collect observations;
- who may issue slope assessments or access recommendations;
- who owns route closure/reopening decisions in each region;
- what stabilization technologies and work practices belong in canon;
- how abandoned alignments are reused;
- how slope events affect local memory and place naming;
- which individual Pokémon have documented relationships with affected sites;
- whether any exact PTU/Caelo environmental slope mechanics should be authored for specific locations.

## Promotion rule

PR #266 strengthens one authoritative target-replacement path by routing the effective defender through the ordinary Move pipeline and preserving single-owner resource use.

That is not evidence that all complete movement, reactions, environmental mechanics or AI policy now exist.

Pass 114 therefore leaves the permanent capability map unchanged.
