# Engine Readiness Snapshot — Pass 162

Status: READ-ONLY EVIDENCE SNAPSHOT for narrative dependency planning.
Date: 2026-08-25

## Narrative change in this pass

Pass 162 adds a subordinate wildlife-rehabilitation protocol rather than a new Care, Conservation or Pokémon Agency authority:

- `research/2026-08-25-wildlife-rehabilitation-release-readiness-monitoring-scan-162.md`
- `design/wildlife-rehabilitation-release-readiness-monitoring-protocol.md`
- `proposals/2026-08-25-wildlife-rehabilitation-release-monitoring-seeds-162.md`

Care remains authoritative for diagnosis/treatment/recovery.

Conservation remains authoritative for release/relocation policy and site stewardship.

Pokémon Agency remains authoritative for persistent identity, custody, association and release transitions.

Pass 162 owns readiness evidence, release-plan operations, release attempts, temporary support and post-release monitoring history.

## Live engine heads inspected

AutoPTU-Java `main`:

`10fd20bfd513898a6f8f157a9b469db993444974`

Latest inspected commit:

`Finalize move-special END_ACTION per declaration (#194)`

The current sequence extends recent PRE_DAMAGE and POST_DAMAGE move-special work with action-scoped END_ACTION aggregation/finalization. This is useful evidence for runtime ownership and move-special ordering.

It does not prove the complete Move catalog, complete damage pipeline, status controller, generic reactions, complete forced movement, AI tactical policy or Minecraft integration.

AutoPTU Python `main`:

`05363c11b0a174ef8ffee89e94ceb6273766f3d9`

Latest inspected commit:

`Career: harden leaderboard visible trainer names (#107)`

This is Career/UI persistence hardening and does not change tactical readiness.

## Java README boundary

The live README still identifies these major migration tasks as incomplete:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Pass 162 therefore makes no category promotion.

## Permanent capability classification

### VERIFIED

- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

### PARTIAL

- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks.

### BLOCKING as complete families

- complete movement including push / pull / knockback / interception / forced movement;
- terrain / weather / hazards / zones / reactions;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter and playback.

## Rehabilitation mechanical boundary

Current engine evidence does not authorize the narrative protocol to infer or implement:

- release readiness from HP alone;
- release readiness from absence of Status or Injuries;
- a Medicine check as universal release approval;
- Loyalty thresholds for release;
- a Command check to force a wild patient to leave an enclosure;
- a battle victory as release authorization;
- a Pokémon approaching a Trainer as capture consent;
- capture as a rehabilitation outcome by default;
- telemetry as exact real-time Pokémon state;
- a support feeder as a spawn modifier;
- sanctuary residence as ownership;
- post-release non-detection as death;
- Minecraft despawn as migration or failed release;
- Minecraft gates/lead entities as custody truth;
- battle LoS as telemetry/field-monitoring coverage;
- AI legal-action infrastructure as non-hostile release/withdrawal behavior.

## Encounter dependency matrix

### Release Site Evacuation — FULL

VERIFIED baseline:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement for staff/release candidate movement through a contested space, interception or dynamic protected routes;
- AI tactical policy for `EVACUATE`, `WITHDRAW`, `PROTECT_CANDIDATE`, `CLEAR_ROUTE` and non-hostile route choice;
- Minecraft/Cobblemon/Craftics adapter/playback for candidate identity, noncombatants, release equipment, route semantics and world-state handoff.

CONDITIONAL BLOCKING:

- terrain/weather/hazards/zones/reactions if the disruption includes a tactically meaningful storm, fire, flood, unstable ground, smoke or protected zone.

CONDITIONAL PARTIAL:

- full lifecycle for richer multi-round objectives;
- full stateful damage for complete attack fidelity;
- status lifecycle for exact Status use;
- move-specific behavior for exact Move use;
- abilities for exact Ability use;
- items for exact battle Items;
- Trainer Features/perks for exact Feature use.

REDUCED:

World state pauses release and moves the candidate plus staff to safety before combat. AutoPTU resolves a static conventional encounter away from the release operation. The readiness assessment and authorization are preserved. Site evidence is reassessed only if the disruption materially changed the site.

### Telemetry Retrieval at Ridge — FULL

VERIFIED baseline:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement if researchers need a protected approach, extraction route, interception handling or objective-based withdrawal;
- AI tactical policy for `REACH_DEVICE`, `PROTECT_RESEARCHER`, `WITHDRAW`, `CLEAR_ROUTE`;
- adapter/playback for device identity, technician position and postbattle handoff.

CONDITIONAL BLOCKING:

- terrain/weather/hazards/zones/reactions if cliffs, storm conditions, unstable terrain or other exact hazards alter the battle.

CONDITIONAL PARTIAL:

- exact Move/Ability/Item/Feature families when used.

REDUCED:

Travel and Wayfinding resolve the approach outside battle. If conflict remains, AutoPTU receives a static safe arena. Device recovery/inspection occurs afterward through Metrology/Visual Records. Device failure writes a monitoring gap; it does not write a Pokémon outcome.

### Return to the Rehabilitation Yard — FULL

VERIFIED baseline:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement for crowd/wildlife movement through shared space;
- AI tactical policy for `WITHDRAW`, `REACH_SAFE_AREA`, `CLEAR_ROUTE`, `DO_NOT_PURSUE` and de-escalation behavior;
- adapter/playback for visitors, facility gates, persistent released-Pokémon identity and semantic objectives.

CONDITIONAL BLOCKING:

- terrain/weather/hazards/zones/reactions only if a separate environmental incident has a validated tactical effect.

REDUCED:

Facility/Public Space state closes the affected area and redirects visitors. The returned Pokémon remains outside tactical combat unless a separate authoritative encounter exists. Any unrelated fight happens on a static map. The return is then reviewed by Care, Conservation and Pokémon Agency without automatic recapture.

### Release Readiness Review

No battle-engine dependency.

Relevant world authorities can compare:

- bounded Care recovery summaries;
- observed movement/feeding/behavior evidence;
- Pass 146 dependency/juvenile evidence when relevant;
- release-site conditions;
- Wild Collective/Migration state;
- Biosecurity findings;
- Research Ethics limits;
- monitoring feasibility;
- previous release attempts and returns.

Possible outcomes remain narrative/operational until exact governing mechanics exist.

## Why verified base movement does not solve release scenes

Base movement legality can answer whether a supported Shift is legal under the current tactical contract.

A release/rehabilitation scene can instead require:

- a noncombatant to move toward an exit rather than toward an enemy;
- a wild Pokémon to withdraw without being pursued;
- a protected route;
- interception;
- dynamic separation between visitors and wildlife;
- an objective such as reach enclosure, device or safe habitat;
- movement whose success writes to world state rather than combat victory.

Those require complete movement and tactical policy, which remain BLOCKING.

## Why AI legal-action VERIFIED does not solve rehabilitation behavior

The verified family can construct/filter legal tactical choices.

It does not decide that a wild Pokémon should:

- leave rather than fight;
- avoid people;
- return to an enclosure;
- remain near a collective;
- protect a juvenile;
- approach supplemental food;
- ignore a former Trainer;
- stop pursuing after reaching safety.

Those are tactical-policy or authored world-behavior questions.

## Latest move-special evidence

Java now has runtime-owned ordering around PRE_DAMAGE, POST_DAMAGE and END_ACTION Move Specials, including action-scoped END_ACTION accumulation/finalization.

This strengthens `move-specific behavior` as PARTIAL.

It does not promote the family because the complete Move catalog and hook registries remain unfinished.

The work also does not make `terrain/weather/hazards/zones/reactions` complete merely because individual reaction paths or hook phases have tests.

## PTU/Caelo source boundary

The official PTU site still exposes PTU 1.05 as the public rules baseline and explicitly recognizes non-violent wild Pokémon interaction as valid GM territory.

No generic rehabilitation, release-readiness, soft-release or post-release monitoring subsystem was verified from the project-accessible PTU data for Pass 162.

No complete primary Caelo corpus defining these procedures was available in the inspected project repositories.

Super PTU Online Helper was not exposed as an invocable capability.

Future mechanical use of Medicine Education, Command, Loyalty, capture/release, restraint, sedation, transport, Items, Trainer Features or species capabilities must be validated against exact source and runtime evidence.

## New overworld contracts introduced by Pass 162

Future world-state work may need:

- rehabilitation-program identity;
- readiness assessments with evidence scope;
- context-specific habituation/dependency assessments;
- release-site operational assessments;
- release plans and contingencies;
- temporary support infrastructure with taper/end state;
- release-attempt history;
- post-release monitoring series;
- explicit non-detection effort;
- return/recapture/re-care events;
- scoped outcome assessments;
- Care -> Rehabilitation handoff;
- Rehabilitation -> Conservation authorization handoff;
- Rehabilitation -> Pokémon Agency release/custody handoff;
- Rehabilitation -> Biosecurity/Research Ethics handoff;
- Rehabilitation -> Migration/Wild Collectives/Conservation Genetics observations;
- Rehabilitation -> Visual Records/Metrology/Tracking monitoring handoff;
- Rehabilitation -> Minecraft projection without transferring authority to entities/blocks.

These are overworld contracts. They are not evidence that battle-engine capability categories changed.