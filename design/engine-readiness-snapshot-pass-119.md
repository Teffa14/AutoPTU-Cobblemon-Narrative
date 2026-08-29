# Engine Readiness Snapshot — Pass 119

Status: EVIDENCE SNAPSHOT. This file records live implementation evidence used by narrative authoring. It does not change engine capability status by itself.
Date: 2026-08-29

## Read-only repositories inspected

AutoPTU-Java head inspected:

`87fbcb2ab75b4642c762017a037a6c0dccb9d8ad`

Latest commit/PR #268: `Bridge real interception sequence into PRE-target registry`.

AutoPTU head inspected:

`1fa17fbb9b6904f19c449ccd358dbfc04dd2f659`

Latest merge: `Career: lazy-load pending battle recovery`.

Neither read-only repository was modified by Pass 119.

## Change since Pass 118

AutoPTU-Java has no newer head than Pass 118. Its latest evidence remains the concrete core-only Intercept path integrated through the PRE-target registry and authoritative Move pipeline.

AutoPTU advanced from `b0a5769b79f2e7b7bd18fb1e0c87ee42a145d4c6` to `1fa17fbb9b6904f19c449ccd358dbfc04dd2f659`. The current change lazy-loads the pending-battle recovery UI path inside Career. It is route-splitting/loading work and provides no new tactical capability evidence.

Pass 119 therefore makes no capability promotion or demotion.

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

## Why air-quality continuity does not change the capability map

The core Pass 119 system is informational world-state continuity:

- monitor/network identity;
- observation provenance;
- coverage claims;
- monitoring gaps;
- plume observations;
- versioned spatial products;
- temporary deployments;
- downstream handoffs;
- revision and historical continuity.

None of those require a battle mechanic.

A tactical airborne condition is a separate problem. It becomes mechanical only if a governing PTU/Caelo source defines an exact effect and current runtime evidence verifies all capability families required to execute it.

## Targeting/footprints/range/LoS remains VERIFIED only for the proven baseline

The engine project's permanent map currently verifies targeting/footprints/range/LoS for its established baseline.

Pass 119 must not stretch that label into dynamic smoke or haze behavior.

Examples requiring additional evidence:

- visibility changing by environmental zone;
- LoS blocked by a moving plume;
- accuracy changes from haze;
- range changes from airborne material;
- target legality changing when a smoke boundary moves.

Those behaviors depend on the exact environmental rule and the currently BLOCKING `terrain/weather/hazards/zones/reactions` family. A render fog effect cannot supply the missing rule.

## Complete movement remains PARTIAL

The Java runtime proves a specific Intercept sequence that can enter PRE-target processing, execute the existing interception spatial/RNG/resource sequence, move a successful interceptor to its resolved interception position, preserve original target context, replace the effective defender and continue through authoritative Move resolution.

That does not prove the complete movement family.

Still unverified as complete families:

- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- environmental displacement;
- movement caused by wind or airborne effects;
- all Intercept triggers/windows/candidate sources;
- collision/landing behavior across all displacement sources;
- generalized competing reactions;
- protected withdrawal or escort movement as a system.

Pass 119 encounters therefore keep staff and civilians outside BattleSpec in their reduced forms.

## Terrain/weather/hazards/zones/reactions remains BLOCKING

A mechanically active air-quality scene could require:

- spatial smoke/haze/gas zones;
- changing visibility regions;
- temporary exclusion cells;
- environmental exposure zones;
- reactions triggered by entering/leaving a zone;
- wind-linked movement of a condition;
- protected clean/covered areas;
- overlapping Weather and airborne-condition effects.

Current evidence does not establish a generalized authoritative family that can model these interactions.

Therefore Pass 119 does not attach mechanics to smoke particles, haze, odor, dust, ash, visible plumes or monitoring-map cells.

## Full turn/round lifecycle remains PARTIAL

Rich air-condition encounters might eventually depend on:

- a condition changing at a round boundary;
- delayed exposure checks;
- a temporary safe route closing after a lifecycle event;
- phased withdrawal;
- a monitoring operation completing after a defined sequence;
- environmental state being revised during combat.

Current live evidence does not prove every lifecycle seam and ordering interaction required for these scenarios.

Reduced variants complete monitoring shutdown, staff withdrawal and world-state handoffs before BattleSpec.

## Damage and status remain PARTIAL

Pass 119 does not infer that poor air automatically causes:

- damage;
- Poison;
- Burn;
- Sleep;
- Confusion;
- Slowed movement;
- accuracy penalties;
- Injury;
- respiratory conditions;
- cumulative exposure;
- healing requirements.

A specific environmental effect may eventually use the existing damage/status pipelines, but only after the exact governing rule and corresponding runtime behavior are verified.

Ordinary combat may continue using currently supported mechanics. Environmental narrative context cannot manufacture additional effects.

## Move-specific behavior, abilities, items and Trainer Features remain PARTIAL

The following names or concepts must not be generalized from flavor:

- Haze;
- Defog;
- Smog;
- Clear Smog;
- Poison Gas;
- smoke-producing species flavor;
- filtration masks/equipment;
- weather-changing Moves;
- purification or sensing abilities;
- environmental Trainer Features.

Each interaction requires exact PTU/Caelo authority and concrete runtime evidence.

One implemented Move, Ability, Item or Feature does not promote its whole family.

## AI legal actions versus tactical policy

AI legal-action infrastructure remains VERIFIED for exposing legal actions.

Pass 119 full encounter concepts may require objectives such as:

- WITHDRAW;
- PROTECT_STAFF;
- CLEAR_ROUTE;
- HOLD_ACCESS;
- AVOID_ZONE;
- ESCAPE;
- defend a static monitoring perimeter while another actor leaves.

Current evidence does not establish tactical policy that understands these objectives, values environmental zones or coordinates protected withdrawal.

AI tactical policy therefore remains BLOCKING.

## Adapter/playback remains BLOCKING

A future semantic adapter would need to distinguish authoritative state from presentation for:

- smoke/haze particles;
- visibility presentation;
- temporary monitoring equipment;
- monitoring-site shutdown;
- staff withdrawal;
- dynamic zone boundaries if ever supported;
- Intercept playback;
- reconnect/reload during a staged encounter;
- exact combatant identity and position;
- final result write-back to Ouros.

Minecraft fog, particles, potion effects, fire blocks, entity collision and native environmental damage cannot become substitute PTU rules.

Cobblemon BattleState remains forbidden as combat authority.

## PTU/Caelo authoring boundary

Internal project research currently demonstrates that Caelo can attach a mechanical environmental identity to a location when the governing source explicitly defines it. Toxic Ravine remains the known example.

That evidence does not establish a universal subsystem for:

- smoke;
- haze;
- particulate exposure;
- industrial pollution;
- airborne volcanic material;
- wildfire smoke;
- odor;
- atmospheric toxins;
- visibility reduction;
- species immunity or sensing.

Any such mechanic stays UNKNOWN until the relevant PTU/Caelo source and runtime contract are checked directly.

## Currently authorable without missing tactical families

Pass 119 can safely author:

- monitoring networks and institutions;
- permanent or temporary monitoring sites;
- site operational state;
- bounded observations;
- monitoring gaps;
- plume observations as evidence;
- versioned spatial interpretation products;
- revision and supersession history;
- information handoffs;
- conflicting-but-compatible maps;
- public memory of prior episodes;
- Pokémon behavior observations as ecological evidence;
- static exploration of former/current monitoring sites;
- long-term settlement changes caused by downstream owner decisions;
- conventional static battles adjacent to the narrative premise after civilians/staff/environmental mechanics are removed from BattleSpec.

Not currently justified from live battle evidence:

- generic smoke/haze LoS mechanics;
- generic air-exposure damage/status;
- dynamic plume zones;
- environment-driven forced movement;
- moving visibility boundaries;
- automatic Move/Ability/Item/Feature interaction with world air;
- objective-aware AI protection/withdrawal;
- semantic Minecraft environmental playback with authoritative battle synchronization.

## Encounter 1 — Hilltop Monitoring Site Withdrawal

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED baseline; dynamic visibility requires exact environmental support
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL if a validated airborne effect causes damage
- status lifecycle: PARTIAL if a validated effect applies status
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for WITHDRAW/PROTECT
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

Current profile: REDUCED.

Reduced version:

Secure or shut down the authored equipment and withdraw the monitoring team before BattleSpec. Keep the air-condition episode as world state only. Ouros selects explicit combatants for a static hilltop arena. Victory may secure the immediate perimeter; it cannot validate readings, restore coverage, identify a pollution source or clear a downstream restriction.

## Encounter 2 — Community Hall Access Perimeter

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED baseline
- base movement legality: VERIFIED
- complete movement: PARTIAL for escort/Intercept/forced movement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL if withdrawal/access changes during rounds
- full stateful damage pipeline: PARTIAL for exact validated effects only
- status lifecycle: PARTIAL for exact validated effects only
- terrain/weather/hazards/zones/reactions: BLOCKING for protected routes or airborne zones
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for PROTECT/WITHDRAW/HOLD_ACCESS
- adapter/playback: BLOCKING

Current profile: REDUCED.

Reduced version:

Move civilians and information staff behind an authored secure boundary before combat. Exclude any air-quality modifier from BattleSpec. Resolve a static exterior encounter. Victory can establish immediate access security; it cannot declare the hall safe for every use, end the air episode or prove public receipt of a notice.

## Encounter 3 — Sampling Roof Diversion

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED baseline
- base movement legality: VERIFIED
- complete movement: PARTIAL if displacement/Intercept matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL for timed route or condition changes
- full stateful damage pipeline: PARTIAL if an exact environment effect exists
- status lifecycle: PARTIAL if an exact environment effect exists
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for CLEAR_ROUTE/ESCAPE
- adapter/playback: BLOCKING

Current profile: REDUCED.

Reduced version:

Complete the sample/record handoff and remove staff before BattleSpec. Use reviewed static rooftop/access geometry with no active environmental modifier. Battle victory secures only the immediate alternate route.

## Pass 119 readiness conclusion

Air-quality monitoring can advance substantially as worldbuilding now because its valuable narrative state is mostly evidence, provenance, institutional response and long-term memory.

The mechanically rich version remains intentionally gated. Current evidence supports conventional static encounters after environmental operations are separated from combat. Dynamic airborne hazards, visibility effects, exposure rules, objective-aware AI and Minecraft semantic playback remain outside the verified capability set.