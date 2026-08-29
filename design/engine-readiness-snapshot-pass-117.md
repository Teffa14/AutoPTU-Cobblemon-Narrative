# Engine Readiness Snapshot — Pass 117

Status: EVIDENCE SNAPSHOT. This file records live implementation evidence used by narrative authoring. It does not change engine capability status by itself.
Date: 2026-08-28

## Read-only repositories inspected

AutoPTU-Java head inspected:

`87fbcb2ab75b4642c762017a037a6c0dccb9d8ad`

Latest commit/PR #268: `Bridge real interception sequence into PRE-target registry`.

AutoPTU head inspected:

`7b4c3d603bd8c2ddd0b47faf7b8691c307e259f9`

Latest commit: `Career: prefetch continue-career route on intent`.

Neither read-only repository was modified by Pass 117.

## Change since Pass 116

There is no newer AutoPTU-Java or AutoPTU head than the revisions already inspected in Pass 116.

Therefore Pass 117 makes no capability promotion or demotion.

The Java evidence remains important but bounded: one real Intercept path now composes with the PRE-target registry and authoritative Move pipeline. That cannot be generalized into complete movement, generalized reactions or full tactical objective support.

The AutoPTU change remains Career web prefetch/performance behavior and adds no tactical evidence.

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

## Why complete movement remains PARTIAL

Current Java evidence verifies a concrete interception route that can:

- discover/select an interceptor candidate from the supplied attempt plan;
- run the existing interception spatial/RNG/resource sequence;
- move a successful interceptor to its resolved interception position;
- preserve the originally declared target as historical context;
- replace the effective defender in PRE-target handling;
- emit semantic target-replacement evidence;
- leave target and interceptor position unchanged on a failed attempt;
- continue through defender-bound preparation and the authoritative Move pipeline.

This does not verify:

- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- collision/landing behavior across all sources;
- environmental displacement;
- every Intercept trigger/window/candidate source;
- generalized reaction competition and ordering.

A narrative encounter requiring those behaviors stays PARTIAL/BLOCKING as appropriate.

## Why terrain/weather/hazards/zones/reactions remains BLOCKING

A health investigation can conceptually involve contaminated spaces, exposure zones, ventilation changes, protective areas or delayed effects. No such concept may enter BattleSpec merely because the narrative layer records it.

Current evidence does not verify a generalized authoritative family covering:

- environmental exposure zones;
- contamination spread;
- infectious zones;
- dynamic quarantine barriers;
- ventilation/airborne battlefield effects;
- delayed symptom zones;
- generalized competing reaction windows;
- environmental status application.

The entire family therefore remains BLOCKING for rich health-related tactical content.

## Why status lifecycle remains PARTIAL

The project has meaningful status implementation evidence, but no current evidence establishes a universal disease/infection framework or every status lifecycle needed by an authored health event.

Pass 117 must not infer:

- illness = Poison;
- infection = persistent status;
- exposure = status application;
- symptoms = combat stage changes;
- recovery = status removal;
- quarantine = status duration.

Any exact condition requires source-level PTU/Caelo review plus current runtime tests.

## Why full turn/round lifecycle remains PARTIAL

A future condition might involve delayed onset, periodic checks, phase changes or effects triggered at defined lifecycle points.

Existing lifecycle seams and representative paths do not verify every delayed health/environment effect or its ordering relative to Moves, Abilities, Items, Trainer Features and reactions.

No delayed symptom or infection clock should be simulated inside rounds without exact rules and tests.

## Why tactical policy remains BLOCKING

The new encounter concepts use intents such as:

- WITHDRAW;
- PROTECT;
- CLEAR_ROUTE;
- ESCAPE;
- preserve access while noncombatants leave.

AI legal-action infrastructure can provide legal options. It does not prove policy that understands these objectives, values protected actors, coordinates withdrawals or chooses tactical positions for non-DEFEAT goals.

Reduced variants therefore remove patients, staff, records and other protected subjects from the tactical grid before battle.

## Why adapter/playback remains BLOCKING

Semantic Java events do not prove a Minecraft/Cobblemon/Craftics implementation that can:

- reconstruct the authoritative battle state;
- animate Intercept without applying mechanics twice;
- show non-DEFEAT objectives;
- preserve withdrawal/protection outcomes;
- synchronize reconnect/reload;
- represent restricted zones without inventing tactical authority;
- write authoritative battle results back to Ouros world state.

Cobblemon battle state remains explicitly forbidden as the authority substitute.

## Pass 117 authoring boundary

Community-health surveillance can progress almost entirely as persistent evidence/world-state logic without needing disease simulation.

Currently authorable:

- aggregate health signals;
- source/provenance references;
- cluster candidates;
- versioned working case definitions;
- investigation-only surveillance classifications;
- common-exposure hypotheses;
- explicitly authored transmission hypotheses without mechanical execution;
- monitoring gaps;
- public/private information boundaries;
- owner-system handoffs;
- notice revision history;
- closure/reopening records;
- long-term institutional memory;
- mysteries based on chronology, geography, scope and provenance;
- static exploration of records and locations.

Not currently justified from live evidence:

- generic infection mechanics;
- proximity transmission;
- dynamic exposure zones;
- automatic statuses from health-world state;
- timed incubation in battle;
- symptom phases;
- disease-based environmental damage;
- quarantine as a tactical mechanic;
- objective-aware evacuation/protection AI;
- Minecraft-side infection or exposure simulation.

## Encounter 1 — Field Observation Site Withdrawal

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL if timed withdrawal/access phases are used
- full stateful damage pipeline: PARTIAL only if an exact verified environmental damage source is introduced
- status lifecycle: PARTIAL only if an exact verified condition is introduced
- terrain/weather/hazards/zones/reactions: BLOCKING for generalized exposure/reaction zones
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for PROTECT/WITHDRAW
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

Current authoring profile: REDUCED.

Reduced version:

Complete staff withdrawal and evidence handoff before BattleSpec. Protected records or samples remain world-state/custody objects outside the grid. Resolve a static conventional encounter with explicit combatants. A victory can secure the immediate perimeter. It cannot classify cases, verify exposure, preserve a sample by implication, treat anyone or close the cluster investigation.

## Encounter 2 — Clinic Annex Access Perimeter

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: PARTIAL for Intercept/forced movement around exit and service lanes
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL if access windows change over time
- full stateful damage pipeline: PARTIAL for ordinary battle resolution; any health-related environmental damage requires exact separate evidence
- status lifecycle: PARTIAL; no generic illness mapping allowed
- terrain/weather/hazards/zones/reactions: BLOCKING for dynamic restricted/exposure zones and generalized reactions
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for protection/withdrawal/service-access goals
- adapter/playback: BLOCKING

Current authoring profile: REDUCED.

Reduced version:

Move patients, staff and protected clinical material behind an authored safe boundary before combat. Use a static external approach. Winning may create `IMMEDIATE_ANNEX_ACCESS_SECURED`. Care remains responsible for facility service and patient state. The health layer remains responsible only for investigation evidence.

## Encounter 3 — Records Transfer Diversion

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: PARTIAL for escort/escape/interception
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL if escape windows or timed route changes exist
- damage/status: PARTIAL for ordinary combat; no sample/health effect inferred
- terrain/weather/hazards/zones/reactions: BLOCKING if route hazards or reaction protection are used
- move-specific behavior/abilities/items/Trainer Features: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for ESCAPE/PROTECT/CLEAR_ROUTE
- adapter/playback: BLOCKING

Current authoring profile: REDUCED.

Reduced version:

Move restricted records or authored samples to secure off-grid custody before combat. AutoPTU resolves only the route threat. Courier, Cold Chain, Science or another owner system resumes transfer afterward. Battle victory never implies chain-of-custody completion or sample validity.

## Exploration — The Clinic Ledger That Changed the Map

Current authoring profile: EXECUTABLE AS WORLD EXPLORATION.

Requirements:

- stable location IDs and aliases;
- dated records;
- privacy-aware access;
- chronology;
- map/document comparison;
- actor testimony;
- provenance.

No missing tactical family is required unless an unrelated battle is added.

## PTU/Caelo mechanical unknowns for Pass 117

Current project evidence does not verify universal contracts for:

- infectious-disease simulation;
- transmission by proximity, touch, shared tile, line of sight or party membership;
- human-to-human transmission;
- Pokémon-to-Pokémon transmission beyond exact named canon mechanics;
- cross-species transmission;
- incubation timing;
- contagiousness windows;
- symptom progression;
- diagnosis checks;
- exposure checks;
- quarantine/isolation duration;
- automatic Poison, Burn, Sleep, Paralysis, Confusion or other status from illness;
- generic disease damage;
- environmental contamination zones;
- airborne exposure;
- automatic recovery at a Pokémon Center;
- species or Type immunity;
- species-derived outbreak sensing;
- generic protective equipment effects;
- Move/Ability/Item/Trainer Feature-powered diagnosis, treatment, sterilization or prevention without exact rule support;
- battle-objective semantics for health-operation evacuation or protection.

These remain UNKNOWN rather than being fabricated in narrative code or Minecraft.

## Pokérus-specific guardrail

Pokérus is a named Pokémon mechanic with its own canon behavior in specific games. It demonstrates why named phenomena must be source-bounded.

Pass 117 does not import Pokérus mechanics into Ouros and does not generalize them to any other condition.

If Ouros ever canonizes Pokérus or an adapted equivalent, PTU/Caelo source priority and engine support must be reviewed separately.

## Privacy implementation requirement

Engine readiness is not only battle readiness.

Before a production health-surveillance system ships, persistence/API contracts also need to prove that:

- private case references do not leak through public aggregate objects;
- public summaries cannot reconstruct protected identities unintentionally;
- investigation access scopes survive persistence/reload;
- superseded definitions remain historical;
- deleting/closing a cluster does not erase required source provenance;
- public notice payloads contain only approved fields.

These are narrative/data-system requirements, not new permanent battle capability categories.

## Minecraft/Cobblemon/Craftics authority boundary

Allowed presentation:

- clinics and temporary observation sites;
- public-safe notice boards;
- staff/NPC routine changes;
- queue states;
- barriers and room-access presentation;
- sealed sample/record props;
- Pokémon presence;
- authored particles/sounds/UI.

Forbidden authority:

- entity proximity decides contact/exposure;
- chunk membership decides transmission;
- Minecraft potion effects create PTU illness;
- a particle collision creates status;
- Cobblemon healing closes a care or cluster record;
- native death/damage proves disease outcome;
- Cobblemon BattleState selects cases or combatants;
- Minecraft pathfinding proves exposure chronology.

The governing direction remains:

Ouros world facts -> AutoPTU battle specification/resolution where battle exists -> adapter -> Minecraft/Cobblemon presentation.

## Promotion gates for richer Pass 117 encounters

Field Observation Site Withdrawal may move beyond reduced form only when the exact needed slices are proven, including:

- required Intercept/forced-movement behavior;
- objective-aware withdrawal/protection policy;
- generalized reaction ordering if used;
- adapter semantic playback for those outcomes;
- any exact environmental condition rule if a tactical exposure zone is included.

Clinic Annex Access Perimeter requires the same objective and adapter support for a rich version.

Records Transfer Diversion additionally requires tested escape/escort semantics if the protected custodian remains on-grid.

No environmental health mechanic is required to preserve any of the three narrative premises. Reduced versions therefore remain the preferred current implementation profile.

## Readiness conclusion

Pass 117 makes substantial narrative progress without requiring engine promotion. Community-health surveillance is primarily an evidence, privacy, chronology and institutional-handoff system. Its worldbuilding can ship ahead of generalized disease or hazard mechanics.

The permanent capability map remains unchanged from Pass 116. Any future health-themed combat mechanic must identify the exact PTU/Caelo rule and prove each permanent capability family it actually uses rather than treating one representative status, Intercept path or visual effect as proof of the whole category.