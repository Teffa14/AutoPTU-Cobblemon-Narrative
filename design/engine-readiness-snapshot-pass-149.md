# Engine Readiness Snapshot — Pass 149

Status: ENGINE EVIDENCE SNAPSHOT. Read-only evidence and dependency classification only. This file does not modify AutoPTU-Java or AutoPTU and does not promote a capability from one representative mechanic.

Date: 2026-08-30

## Live repositories inspected

### AutoPTU-Java — read only

Observed `main` head:

`6b7a8b111f567bce39102606ff494fdc3dd57c15`

Commit:

`Internalize Intercept check input at spatial boundary (#286)`

No newer commit was observed during Pass 149.

The commit internalizes Intercept check materialization at the authoritative spatial boundary and strengthens server ownership of a complicated Intercept path. The surrounding live evidence also shows server-owned PTU geometry for Intercept distance and localized reuse of shared forced-movement application for successful melee Intercept Push 1, collisions and partial stops.

This remains localized evidence. It does not verify every Push/Pull/Knockback source, arbitrary collision case, escort movement, object carrying, moving platforms, environmental forced movement, generalized reaction ordering, dynamic zones or tactical objective policy.

### AutoPTU — read only

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

No newer commit was observed during Pass 149.

The commit is explicitly presentation-only and states that battle rules and outcomes do not change. It is not evidence that the Minecraft/Cobblemon/Craftics adapter/playback family is complete.

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

No permanent category changes during Pass 149.

## Campaign-scale rule

Campaign convergence is primarily Ouros world-state orchestration and therefore does not itself require a new tactical capability.

A convergence becomes engine-dependent only when the authored scene asks AutoPTU to perform exact tactical behavior. The existence of several narrative threads in one location does not grant multi-objective AI, reinforcements, escort logic, withdrawal logic, reactive zones or cross-battle state carryover.

## Three-Front Convergence Perimeter

Full-version intent:

Several independently active threads cause multiple groups to reach one fixed site with different objectives. Opponents may prioritize route control, evidence withdrawal or protection; reinforcements and terrain pressure may depend on prior world state.

Dependency matrix:

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | explicit targeting and spatial relationships |
| base movement legality | VERIFIED | ordinary legal movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | interception, body-blocking consequences, displacement if used |
| core calculations | VERIFIED | ordinary PTU calculations |
| action economy/initiative | VERIFIED | ordinary tactical sequencing |
| full turn/round lifecycle | PARTIAL | reinforcement/objective timing if in-battle |
| full stateful damage pipeline | PARTIAL | persistent battle damage state |
| status lifecycle | PARTIAL | exact status interactions if used |
| terrain/weather/hazards/zones/reactions | BLOCKING | dynamic pressure, unsafe zones or generalized reactions if used |
| move-specific behavior | PARTIAL | exact selected move semantics |
| abilities | PARTIAL | exact selected ability semantics |
| items | PARTIAL | battle item semantics as used |
| Trainer Features/perks | PARTIAL | exact feature semantics/interrupts |
| AI legal-action infrastructure | VERIFIED | legal candidate actions |
| AI tactical policy | BLOCKING | prioritizing different objectives and coordinated withdrawal/holding behavior |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | authoritative dynamic presentation/handoff incomplete |

Full version: BLOCKED.

Reduced version: READY.

Reduction contract:

- Ouros resolves which threads and actors actually reached the scene before BattleSpec;
- neutral actors, evidence packages, records and semantic world objects remain outside tactical state;
- one explicit opposing combatant set and static geometry enter AutoPTU;
- no dynamic reinforcements, objective-aware target switching, reactive zones or scripted withdrawal;
- AutoPTU may establish only a reviewed narrow fact such as `IMMEDIATE_CONVERGENCE_ROUTE_CLEAR` or `TACTICAL_DEFEAT_CONFIRMED`;
- Ouros then re-evaluates each contributing thread through its owning system.

## Parallel Objective Relay

Full-version intent:

Two tactical stages belong to the same major convergence and later tactics react to what happened in the earlier stage.

Relevant capabilities:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- move-specific behavior — PARTIAL
- abilities — PARTIAL as used
- items — PARTIAL as used
- Trainer Features/perks — PARTIAL as used
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING if later opponents adapt objectives/tactics
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for seamless stateful handoff

Full version: BLOCKED where it assumes unsupported cross-BattleSpec tactical continuity or objective-aware adaptation.

Reduced version: READY.

Use the Pass 148 multi-stage contract:

A -> Ouros transition -> B.

At the boundary:

- freeze A's authoritative result;
- extract only explicitly allowed world/tactical facts;
- do not silently carry HP, statuses, initiative, temporary terrain, reaction resources, move-use state, item use, Trainer Feature state or positions;
- evaluate the next situation in Ouros;
- construct B from explicit reviewed initial state.

## The Opponent Leaves Before the Finale

Full-version intent:

A persistent adversary decides to disengage because their current objective has been achieved, become impossible or no longer justifies continued risk.

Relevant capabilities:

- targeting/footprints/range/LoS — VERIFIED where pursuit targeting matters
- base movement legality — VERIFIED
- complete movement including interception/forced movement — PARTIAL
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for mid-battle encounter-end semantics
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for objective-aware risk/escape choice
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative mid-battle withdrawal presentation/handoff

Full autonomous version: BLOCKED.

Reduced version: READY.

Ouros evaluates the adversary's plan before combat using actor knowledge, resources, access and current goals. If withdrawal already occurred, the expected battle disappears. If battle begins, Minecraft/Cobblemon cannot later infer escape from entity motion or despawn. Withdrawal after commitment requires an authoritative tactical result or future reviewed handoff.

## Rich convergence mechanics that remain dependency-sensitive

The campaign layer must continue to declare exact capabilities when it uses:

- multiple objective-aware enemy groups: AI tactical policy;
- tactical reinforcements: lifecycle + action economy/initiative + AI legal actions + tactical policy + playback;
- escort/protect movement: complete movement and potentially tactical policy/reactions;
- escape/withdraw during combat: complete movement + lifecycle + tactical policy + playback;
- dynamic weather or terrain during a finale: terrain/weather/hazards/zones/reactions + lifecycle;
- knockback into hazards: complete movement + terrain/hazards/zones/reactions;
- Trainer Feature interrupts: Trainer Features/perks + appropriate reaction/lifecycle support;
- delayed move effects: lifecycle + move-specific/status/ability family as relevant;
- persistent state between separate BattleSpecs: exact serialization contracts for every carried family;
- moving vehicles/platforms: complete movement + terrain/zones/reactions + adapter/playback plus a reviewed platform contract.

## Narrative orchestration that is READY without new battle support

The following Pass 149 systems are world-state/data features and can advance independently of tactical completeness:

- multiple dormant/active arc threads;
- campaign pressure salience;
- convergence eligibility checks;
- actor reach/knowledge/motivation validation;
- setup/payoff ledger;
- recontextualization preserving prior facts;
- payoff retirement;
- aftermath windows;
- thread transformation;
- multiple participation-lane hooks;
- invalidating a planned finale when its prerequisites disappear.

These systems must still respect their owning world-state layers, but they do not need Minecraft or AutoPTU to invent additional battle rules.

## PTU / Caelo assumptions kept UNKNOWN

Pass 149 does not invent:

- a universal campaign timer;
- a universal `main quest` state;
- mandatory villain progress when players perform side activities;
- universal act/season/finale thresholds;
- a generic boss-finale rules package;
- cross-BattleSpec HP/status/initiative persistence;
- universal tactical retreat conditions;
- generic reinforcement timing;
- generic multi-faction battle AI;
- generic protect/escort semantics;
- a universal Skill Check for recognizing foreshadowing, preventing escalation or forcing convergence;
- Gym progression as a mandatory campaign clock;
- battle victory as automatic faction collapse, mystery resolution, public belief change or arc completion.

## Minecraft/Cobblemon/Craftics boundary

The presentation layer may show consequences Ouros has already established:

- actors arriving or leaving;
- signs of escalating pressure;
- changed camps or routes;
- a recurring rival in a location;
- static finale scenery;
- post-battle damage presentation;
- aftermath changes;
- models, animations, particles, sound and dialogue surfaces.

It must not decide:

- which threads converge;
- whether a faction plan advanced;
- which actors know about the event;
- who becomes a combatant;
- target legality;
- PTU HP/status/positions;
- tactical withdrawal;
- reinforcement legality;
- objective success;
- faction defeat;
- arc resolution;
- world consequences.

Cobblemon BattleState remains outside Ouros battle-state authority.

## Readiness conclusion

Pass 149 changes no permanent capability status.

Its campaign-scale connective systems are implementation-independent world-state work and can advance now. Mechanically rich convergence battles remain blocked exactly where they depend on tactical policy, generalized reactions/dynamic terrain, unsupported full lifecycle or adapter playback. Reduced forms remain READY because they resolve convergence in Ouros, pass only explicit combatants and static tactical facts to AutoPTU, and return narrow authoritative results to world-state owners.