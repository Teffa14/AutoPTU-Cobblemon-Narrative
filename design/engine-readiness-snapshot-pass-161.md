# Engine Readiness Snapshot — Pass 161

Status: READ-ONLY EVIDENCE SNAPSHOT for narrative dependency planning.
Date: 2026-08-25

## Narrative change in this pass

Pass 161 adds a subordinate world-state protocol rather than a new regional-law authority:

- `research/2026-08-25-interregional-crossing-processing-clearance-scan-161.md`
- `design/interregional-crossing-processing-clearance-protocol.md`
- `proposals/2026-08-25-interregional-crossing-processing-clearance-seeds-161.md`

The protocol extends Interregional Mobility and Credentials. It coordinates existing decisions from Travel, Supply Chains, Postal, Biosecurity, Pokémon Agency, Land Tenure, Institutional Review and Cases/Illicit Networks.

It does not establish national borders, citizenship, passports, visas, immigration law, customs law, tariffs, detention/search powers or universal police authority.

## Live engine heads inspected

AutoPTU-Java `main`:

`2c83099de0f558a6e387f39174c0223f8e1668e6`

Latest inspected commit:

`Add move-special END_ACTION runtime bridge (#192)`

The commit freezes a runtime-owned END_ACTION move-special bridge and Python-compatible aggregation/order behavior. Recent surrounding work already includes PRE_DAMAGE and POST_DAMAGE move-special bridges and mutable result-state preservation.

This strengthens evidence for move-specific hook ordering and engine ownership. It does not prove the complete Move catalog, full damage pipeline, complete reactions, complete statuses, complete forced movement or Minecraft integration.

AutoPTU Python `main`:

`05363c11b0a174ef8ffee89e94ceb6273766f3d9`

Latest inspected commit:

`Career: harden leaderboard visible trainer names (#107)`

That change is Career/UI persistence hardening. It does not change tactical readiness.

## Java README boundary

The live Java README still marks these major systems incomplete:

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

Pass 161 therefore makes no category promotion.

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

## Crossing-processing mechanical boundary

The new protocol is overworld orchestration state. Current engine evidence does not authorize:

- defeating a guard to grant permission;
- battle victory to grant clearance;
- a Move check to validate a credential;
- Charm, Guile, Command or Perception as generic checkpoint DCs;
- Pokémon capture as a transfer authorization;
- Poké Ball possession as ownership proof;
- held items as declarations/manifests;
- Minecraft inventory contents as cargo truth;
- Minecraft gate/redstone state as access authority;
- Minecraft scoreboard state as credential authority;
- party entity count as authoritative passenger/consignment state;
- tactical LoS as inspection/screening visibility;
- AI legal-action infrastructure as queueing, staff workflow or clearance policy;
- an exact status/ability/move feature as evidence that its entire capability family is implemented.

## Encounter dependency matrix

### Checkpoint Evacuation During Wildlife Movement — FULL

VERIFIED baseline:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement for civilians/wildlife that must `CROSS`, `WITHDRAW`, reroute or interact with interception;
- AI tactical policy for `EVACUATE`, `CROSS`, `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_SITE`;
- Minecraft/Cobblemon/Craftics adapter/playback for crowds, protected lanes, wildlife objectives and world-state handoff.

CONDITIONAL BLOCKING:

- terrain/weather/hazards/zones/reactions when a moving protected lane, storm, terrain change or other validated environmental mechanic affects the battle.

CONDITIONAL PARTIAL:

- full lifecycle for richer multi-round objective state;
- full stateful damage for complete ordinary attack fidelity;
- status lifecycle for an exact Status;
- move-specific behavior for an exact Move;
- abilities for an exact Ability;
- items for an exact battle-semantic Item;
- Trainer Features/perks for an exact Feature.

REDUCED:

Crossing Processing suspends normal operations. World state moves civilians away and resolves the wildlife passage first. If a separate hostile confrontation remains, AutoPTU receives a static arena away from the crossing lane. Processing resumes afterward from the preserved session state.

### Secondary Inspection Bay Interruption — FULL

VERIFIED baseline:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement if staff/custodians/objects must move through contested tactical space;
- AI tactical policy for `PROTECT_CUSTODIAN`, `REACH_EXIT`, `CLEAR_ROUTE`, `WITHDRAW`;
- adapter/playback for cargo/custody semantics, staff and postbattle handoff.

CONDITIONAL BLOCKING:

- terrain/weather/hazards/zones/reactions if machinery, structural damage, spill, smoke or another exact environmental effect changes tactics.

CONDITIONAL PARTIAL:

- items if a protected object is also an exact PTU battle Item;
- exact Status/Move/Ability/Feature families when invoked.

REDUCED:

The held consignment remains outside the grid. Staff evacuate first. AutoPTU resolves a static conventional encounter in cleared space. The pre-existing specialist review resumes afterward; a battle outcome does not decide the pending clearance question.

### Emergency Crossing Lane — FULL

VERIFIED baseline:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement for evacuees/responders moving through the tactical area;
- AI tactical policy for `EVACUATE`, `REACH_EXIT`, `PROTECT_RESPONDER`, `CLEAR_ROUTE`;
- adapter/playback for noncombatants, lane semantics and overworld continuation.

CONDITIONAL BLOCKING:

- terrain/weather/hazards/zones/reactions if the underlying crisis produces a validated tactical environment.

REDUCED:

Emergency Services resolves civilian/responder movement before combat. Crossing Processing records the temporary lane revision. Any remaining threat is resolved in a static perimeter fight. Clearance/permission state is not modified by battle victory.

### Declaration Reconciliation Review

No battle-engine dependency.

Relevant authorities can compare:

- declaration revisions;
- Identity/Credentials records;
- Travel service history;
- Supply Chains/Postal state;
- custody/provenance state;
- Timekeeping records;
- crossing timestamps.

Valid results include clerical mismatch, superseded record, emergency reroute, different process-stage interpretation, specialist referral, unresolved evidence or a separate Case referral if independent evidence supports one.

## Why AI legal-action VERIFIED does not solve checkpoint encounters

The verified AI family can construct/filter legal tactical choices. It does not choose narrative objectives such as:

- protect a technician;
- open a route for civilians;
- withdraw without pursuing;
- escort a noncombatant;
- preserve a wildlife corridor;
- hold position while a crossing clears;
- distinguish a bystander from an opponent because of world semantics.

Those decisions require AI tactical policy, which remains BLOCKING.

## Why base movement VERIFIED does not solve evacuation

Base movement legality can determine whether a normal Shift is legal under supported movement modes and geometry.

Evacuation/full crossing scenes can require:

- noncombatant movement objectives;
- interception;
- forced movement;
- reactive movement;
- dynamic lanes;
- moving protected actors;
- safe exits that matter as objectives rather than only legal tiles.

Complete movement remains BLOCKING as a family.

## Latest move-special evidence

Java’s current move-special sequence includes runtime-owned seams around PRE_DAMAGE, POST_DAMAGE and END_ACTION plus mutable result-state/order contracts.

That is good architectural evidence for `move-specific behavior` as PARTIAL.

It does not prove every Move or hook phase. It also does not prove complete `terrain/weather/hazards/zones/reactions`, even when some individual reaction paths have parity tests.

## PTU/Caelo source boundary

No generic PTU checkpoint, border, declaration or clearance subsystem was verified for Pass 161.

The Pokémon League Reception Gate is narrative/game-world precedent for bounded eligibility checks, not a PTU rule implementation.

No complete primary Caelo corpus defining cross-region processing was available in the inspected project repositories. Super PTU Online Helper was not exposed as an invocable capability. No result is attributed to either.

Future use of Charm, Guile, Command, Perception, Pokémon Education, Technology Education, Trainer Features, specific Items or Pokémon capabilities at a crossing requires exact source and runtime validation.

## New overworld contracts introduced by Pass 161

Future world-state work may need:

- persistent crossing-facility identity;
- facility revisions;
- processing-session state;
- declaration provenance;
- external-authority check references;
- screening decisions;
- specialist referrals;
- scoped holds;
- clearance decisions;
- physical release/handoff events;
- coarse process load;
- outage/fallback state;
- process-history revisions;
- Crossing -> Credentials/Interregional Mobility handoff;
- Crossing -> Travel handoff;
- Crossing -> Supply Chains/Postal handoff;
- Crossing -> Biosecurity handoff;
- Crossing -> Pokémon Agency handoff;
- Crossing -> Cases/Illicit Networks only when separate evidence warrants it;
- Crossing -> Minecraft projection without moving authority into blocks/entities.

These are overworld blockers/contracts, not evidence that battle-engine categories changed.