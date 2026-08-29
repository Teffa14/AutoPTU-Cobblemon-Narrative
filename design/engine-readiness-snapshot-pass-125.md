# Engine Readiness Snapshot — Pass 125

Status: EVIDENCE SNAPSHOT. This file records current evidence and does not promote capability families from isolated representative mechanics.
Date: 2026-08-29

## Read-only heads inspected

AutoPTU-Java current head: `80f08b5d66f3451f70743ac0d4717f3a3dd21a0b` — `Derive intercept Justified bonus from server state (#275)`.

Compared with Pass 124 head `82b9dd92ac8fd0cc47a6e53e24017fc20ebd04f6`, the current slice freezes one more authority input for the concrete Intercept route.

`RuntimeInterceptCheckInputFactory` now derives the exact `Justified [Errata]` bonus from server-owned runtime ability state rather than accepting that conclusion from an adapter-facing input. The Python contract exporter pins the exact bonus value used by the legacy authority, and tests distinguish the exact errata ability name from a similarly named ability. Acrobatics/Athletics and Coaching were already server-derived in the prior slice.

Terrain remains an explicit internal input whose authoritative environment contract has not been frozen. This is material progress for one Intercept path, not evidence that complete movement, abilities or terrain/reactions are complete families.

AutoPTU current head: `d97c45e76647642105fee3ff1b9b80a38e092778` — `Career: preserve clean roster normalization identity`.

The latest observed AutoPTU work remains Career persistence/browser-state hardening. It adds no tactical battle coverage.

## Permanent capability map

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No capability family is promoted in Pass 125.

## Intercept evidence update

Current bounded evidence now supports a concrete chain in which:
- a real interception sequence can enter the PRE-target registry;
- successful Intercept movement uses the resolved interceptor position for that route;
- target replacement reaches the authoritative Move pipeline;
- Acrobatics and Athletics inputs come from server-owned `CombatantRuleContent`;
- Coaching automatic-success state comes from server-owned temporary effects;
- exact `Justified [Errata]` presence and its pinned bonus come from server-owned ability state;
- similarly named `Justified` does not satisfy the exact errata contract;
- the input factory remains core-only;
- terrain remains explicitly unfrozen.

Still not verified by this evidence:
- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- every Intercept timing/window;
- environmental displacement;
- generalized competing reactions;
- generalized reaction ordering;
- broad terrain modifier authority;
- every Ability registration or behavior;
- every Coaching/Trainer Feature pathway;
- every Move or Item registration;
- objective-aware AI tactical policy;
- semantic adapter playback.

## Pass 125 narrative readiness

The extreme-heat/cooling-access continuity model is primarily world-state and provenance infrastructure.

READY without new tactical capability:
- persistent heat-episode identity;
- source-linked observed-condition bundles;
- versioned heat-impact assessments when canon supplies an issuer/method;
- cooling-access site identity;
- building-open versus cooling-function separation;
- planned versus actual operating windows;
- qualitative access/capacity observations;
- power, water, staffing and accessibility dependencies;
- owner-system response handoffs;
- activity schedule changes;
- aggregate health handoffs without diagnosis leakage;
- Pokémon behavior observations;
- recovery checkpoints;
- closure with downstream work still open;
- archival/provenance mysteries;
- long-term legacy of temporary support sites and changed schedules.

`Five Times the Heat “Ended”`, `Four Open Buildings, Two Useful Rooms`, `The Empty Trail at Twelve`, `Two Heat Maps, Different Questions` and `The Courtyard Behind the Old Hall` are READY as narrative/world-state content.

## Encounter readiness — Cooling Hall Access Withdrawal

Targeting/footprints/range/LoS — VERIFIED.

Base movement legality — VERIFIED.

Complete movement including push/pull/knockback/interception/forced movement — PARTIAL when staff/civilian withdrawal, Intercept or forced displacement occurs during combat.

Core calculations — VERIFIED.

Action economy/initiative — VERIFIED.

Full turn/round lifecycle — PARTIAL if withdrawal or closing windows are staged in turns.

Full stateful damage pipeline — PARTIAL for selected governed combat effects only.

Status lifecycle — PARTIAL for selected governed statuses only. Generic heat illness remains UNKNOWN.

Terrain/weather/hazards/zones/reactions — BLOCKING for any live heat/exposure zone, changing shade, hot-surface rule, protected corridor reaction or environmental displacement.

Move-specific behavior — PARTIAL.

Abilities — PARTIAL. Current Justified evidence is one exact Intercept modifier, not broad Ability coverage.

Items — PARTIAL.

Trainer Features/perks — PARTIAL. Coaching evidence remains bounded to the concrete Intercept route.

AI legal-action infrastructure — VERIFIED.

AI tactical policy — BLOCKING for PROTECT/WITHDRAW behavior.

Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative semantic evacuation/site-state/environmental playback.

Reduced form: READY. Pause or close public service before BattleSpec creation. Remove staff, civilians, sensitive equipment and noncombatants. Use static reviewed exterior geometry. Heat remains world context only and applies no tactical modifier. Battle victory may secure immediate access but cannot reopen the site, diagnose anyone or close the episode.

## Encounter readiness — Early-Morning Market Diversion

Full-form pressure:
- complete movement — PARTIAL for active vendor/courier withdrawal, Intercept or forced displacement;
- full turn/round lifecycle — PARTIAL for timed departure or relocation windows;
- terrain/weather/hazards/zones/reactions — BLOCKING if heat, shade, exposure or generalized crossing reactions become tactical;
- damage/status — PARTIAL only for exact governed combat mechanics; generic heat/dehydration effects remain UNKNOWN;
- AI tactical policy — BLOCKING for CLEAR_ROUTE/PROTECT/WITHDRAW;
- adapter/playback — BLOCKING for semantic relocation and schedule-state playback.

Reduced form: READY. Complete the market relocation before battle. Keep vendors, goods and visitors off-grid. Resolve a static junction encounter. Market hours and operating state remain owned by the market/event/commercial systems.

## Encounter readiness — Observation Roof Perimeter

Full-form pressure:
- complete movement — PARTIAL for staff withdrawal or Intercept;
- lifecycle — PARTIAL for staged evacuation;
- terrain/weather/hazards/zones/reactions — BLOCKING for any live environmental heat effect, changing safe area or generalized reaction;
- object-specific damage/protection remains UNKNOWN without an exact object contract;
- AI tactical policy — BLOCKING for PROTECT/WITHDRAW;
- adapter/playback — BLOCKING for semantic observation-site shutdown and environmental display tied to authoritative events.

Reduced form: READY. Finish the observation, secure records/equipment and remove staff first. Use static reviewed access geometry. Winning cannot validate a weather reading or establish heat causality.

## PTU/Caelo boundary

The internal source scan supports exact authored environmental mechanics when a governing source explicitly defines them. Toxic Ravine remains the project’s known example.

That precedent does not create a generic extreme-heat subsystem.

Remain UNKNOWN without exact governing evidence and implementation tests:
- heat damage per round;
- dehydration tracks;
- fatigue/exhaustion caused by ambient temperature;
- automatic Burn, Poison, Sleep, Confusion or other status from heat;
- hot-ground movement penalties;
- sunlight/heat-derived LoS or accuracy modifiers;
- cumulative exposure;
- mechanical cooling zones;
- nighttime recovery mechanics;
- Type-derived heat immunity;
- Fire-type universal climate immunity;
- Water/Ice-type universal cooling capability;
- species-derived heat forecasting;
- generic heat relief from Moves;
- Sunny Day or Drought as long-duration overworld climate authority;
- Trainer Features granting universal heat-response competence.

Narrative descriptions such as hot, scorching, desert, shade or cool place do not establish a tactical effect.

## Boundary with existing narrative systems

Weather owns observations, forecasts and revisions.

Seasonality owns climate expectation.

Travel owns journey/route decisions.

Care owns individual diagnosis, treatment and recovery.

Community Health owns aggregate health investigation.

Electric Grid owns power service and technical restoration evidence.

Drinking Water owns potable-water state.

Facility Maintenance owns repair and verification of equipment.

Public Space, Education, Workplace, Hospitality, Commercial and Temporary Event systems own their own operating decisions.

Crisis/Rescue owns emergency rescue and stabilization.

Pass 125 stores the cross-system heat episode, cooling-access continuity and response lineage. It does not replace those authorities.

## Minecraft/Cobblemon boundary

Minecraft/Cobblemon may render:
- intense light or heat-haze visuals;
- shade structures;
- altered NPC schedules;
- temporary indoor gathering spaces;
- water/support points when canonized;
- public notices;
- fans/vents/cooling equipment appropriate to regional technology;
- Pokémon routines selected by Ouros world state.

These surfaces are presentation.

Biome temperature does not apply PTU heat damage. Sunlight rendering does not create Sunny Day. Fire proximity does not establish exposure. Water blocks do not prove potable water or cooling treatment. Potion effects do not substitute for PTU status. Fire-type species do not receive generic ambient-heat immunity by renderer logic. Cobblemon BattleState remains outside combatant selection, legality, HP/status, positions, heat state and outcomes.

## Current implementation-safe pattern

For any scene whose narrative premise involves heat but whose exact tactical environment is unsupported:
1. resolve the weather observation and owner-system operational decision in Ouros world state;
2. complete civilian/staff withdrawal and secure sensitive objects before BattleSpec creation;
3. select explicit combatants in Ouros;
4. create a static reviewed arena with no inferred heat mechanic;
5. let AutoPTU resolve only supported battle facts;
6. use the adapter only to present authoritative state/events;
7. return to owner systems for reopening, care, repair or episode closure.

## Unresolved mechanical questions

- Is there any exact PTU/Caelo ambient-heat mechanic applicable to Ouros locations?
- If so, what is its source, scope, lifecycle and interaction with battle Weather?
- Which Moves, Abilities, Items or Trainer Features interact with that exact mechanic?
- Can environmental visibility/heat haze ever affect LoS under a governed rule?
- Are there exact carrying/escort contracts needed for heat-response encounters?
- What objective-aware AI policies are required for PROTECT/WITHDRAW/CLEAR_ROUTE?
- What semantic adapter events are required for evacuation, cooling-site state and schedule changes?

## Unresolved canon questions

- Which Ouros regions experience recurring unusual or prolonged heat?
- What terminology and assessment methods exist locally?
- Which institutions can issue heat-specific notices or open temporary support sites?
- What cooling/ventilation technologies exist by region?
- Which public buildings or outdoor spaces have documented heat-response roles?
- What privacy rules govern welfare-check programs, if any exist?
- Which historical episodes changed schedules, routes or public spaces permanently?
- Which individual Pokémon have documented trained roles rather than inferred species-wide abilities?

## Readiness result

Heat episode/provenance continuity: READY.

Cooling-access operational state: READY when the underlying institution/site is canonized.

Cross-system schedule/service handoffs: READY.

Provenance mysteries and static exploration: READY.

Reduced Cooling Hall Access Withdrawal: READY.

Reduced Early-Morning Market Diversion: READY.

Reduced Observation Roof Perimeter: READY.

Full forms remain PARTIAL/BLOCKING where complete movement, staged lifecycle, environmental zones/reactions, objective-aware tactical policy, object interaction or semantic playback are required.