# Engine Readiness Snapshot — Pass 159

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `fde03b46c9f9cec28784319460c59737810c4447`
Date: 2026-08-31

## Read-only engine heads inspected

AutoPTU-Java:

`7c9a4b3ae628e64a6ddf5186552335f35f8330df` — merged PR #295, `Internalize canonical combatant rule content for Intercept`.

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

No files in either engine repository were modified by Pass 159.

AutoPTU-Java advanced since Pass 158. AutoPTU did not.

## New Java evidence

The current Java head moves canonical combatant rule content used by Intercept into a shared server-owned `CombatantRuleContentRegistry`.

The inspected diff states that the registry is an immutable canonical PTU rule-content snapshot keyed by combatant id. It contains rule content used by runtime families such as capabilities, Loyalty, controllers, skills, Trainer Features, and Naturewalk data. Rule families resolve content from this server-owned snapshot instead of accepting rule-specific or per-invocation maps from Minecraft/Cobblemon adapters.

The Intercept PRE-target hook no longer lets external orchestration inject combatant rule-content maps into a plan. Candidate discovery, temporary-effect cleanup, ordering, attack-line geometry, Shift legality, RNG/resource use, displacement, and now the canonical content source used by this slice remain within core-owned runtime boundaries.

This strengthens the authority boundary around the currently implemented Intercept path.

It remains localized evidence. It does not prove that every feature named in `CombatantRuleContent` is fully implemented, nor does it prove the complete movement or generalized reaction families.

Still unverified globally include:

- all Push sources;
- Pull;
- general Knockback;
- all Intercept variants and ordering interactions;
- arbitrary forced movement;
- escort/rescue movement;
- object carrying;
- dynamic objectives;
- moving scenery, platforms, vehicles, doors, or barriers;
- generalized hazards/zones/reaction windows;
- tactical protect/deny/withdraw/evacuate policy;
- full performance/Contest mechanics;
- full semantic Minecraft/Cobblemon/Craftics playback.

The AutoPTU head remains explicitly presentation-only and states that no battle rules or outcomes change.

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

No category is promoted by Pass 159.

## Important Contest/Coordinator qualification

PTU public rules evidence shows that Coordinator and Contest mechanics exist as specific rules, including Appeal Rolls and Contest-triggered Features.

That does not establish that AutoPTU-Java currently implements the complete Contest subsystem or every Coordinator Feature.

Therefore:

- formal PTU Contest outcomes are UNKNOWN at runtime until exact rules and tests are inspected;
- Narrative may preserve an externally authoritative formal result once it exists;
- Narrative may not simulate Appeal scores, Contest effects, Coordinator Features, Tutor Point spending, or official ranks on its own;
- Minecraft/Cobblemon may not manufacture those outcomes from animations or audience UI.

## Backstage Evacuation Corridor — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for static geometry
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL for contested route control, forced displacement, or Intercept
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for staged evacuation phases
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if danger zones, collapsing scenery, fire, smoke, or generalized reactions matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protect/withdraw/route-control objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative evacuation-state playback

Overall full status: BLOCKED.

Reduced status: READY at narrative-contract level if selected combat content is individually audited.

Reduced constraints:

- audience, crew, performers, props, and noncombatant Pokémon reach an authored safe room before initiative;
- fixed arena geometry;
- explicit combatants only;
- no rescue/escort objective inside BattleSpec;
- permitted result: `IMMEDIATE_BACKSTAGE_ACCESS_ROUTE_CLEAR`.

Hard safeguards:

`BACKSTAGE_ACCESS_ROUTE_CLEAR != AUDIENCE_EVACUATED`

`BATTLE_WON != PERFORMANCE_RESUMED`

`POKEMON_PERFORMER_PRESENT != COMBATANT`

## Rigging Access Perimeter — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED for static geometry
- base movement legality — VERIFIED for static legal movement
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL if falls, displacement, or Intercept matter
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL if machinery changes by phase
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING for suspended hazards, falling scenery, dynamic machinery, danger zones, or reaction windows
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for machinery-control or access-denial intent
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for dynamic stage machinery state

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- rigging is powered down before initiative;
- suspended objects are static noninteractive scenery;
- no fall, crush, moving-platform, or machinery hazard rules;
- permitted result: `IMMEDIATE_RIGGING_ACCESS_CLEAR`.

Hard safeguards:

`RIGGING_ACCESS_CLEAR != RIGGING_REPAIRED`

`STAGE_SCENERY != TACTICAL_HAZARD`

## Tour Convoy Roadblock — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for static ground geometry
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL; vehicle/escort/object-carrying semantics are not globally verified
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for staged convoy movement
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if road hazards, vehicle zones, or generalized reactions matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for escort, withdraw, delay, convoy protection, or route-control decisions
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative vehicle/cargo playback

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- Travel stops before BattleSpec;
- vehicles, performers, cargo, props, and noncombatants remain outside tactical state;
- fixed roadside geometry;
- explicit combatants only;
- permitted result: `IMMEDIATE_ROADBLOCK_PERIMETER_CLEAR`.

Hard safeguards:

`ROADBLOCK_PERIMETER_CLEAR != TOUR_STOP_REACHED`

`BATTLE_WON != CARGO_DELIVERED`

`VEHICLE_VISIBLE != VEHICLE_TACTICALLY_SIMULATED`

## Interrupted Outdoor Performance — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for static geometry
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL if evacuation or environmental displacement matters
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for changing incident phases
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING for active storm, smoke, fire, crowd zones, changing ground, or generalized reactions
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for evacuation/protection/withdrawal objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative incident-state playback

Overall full status: BLOCKED.

Reduced status: READY only if Ouros establishes the safe transition before initiative.

Reduced constraints:

- performance ends or pauses before BattleSpec;
- audience and noncombatant performers are outside tactical state;
- weather is visual/narrative unless a separately verified battle-weather contract is used;
- fixed geometry;
- permitted result: `STATIC_INCIDENT_PERIMETER_RESOLVED`.

Hard safeguards:

`STATIC_INCIDENT_PERIMETER_RESOLVED != PERFORMANCE_COMPLETED`

`VISUAL_WEATHER != PTU_WEATHER_STATE`

`TACTICAL_FAILURE_WITHOUT_EVACUATION_CONTRACT != CIVILIAN_HARM_CONFIRMED`

## Performance authority boundary

Narrative may establish and persist:

- works and production versions;
- casts/ensembles and role periods;
- rehearsal episodes;
- scheduled events;
- actual occurrence, interruption, cancellation, postponement, relocation, or completion;
- attributed audience response;
- reviews and public claims;
- version changes;
- tour plans and production consequences;
- links to archival/material records;
- links to separately authoritative Contest results.

Narrative may not manufacture:

- Appeal Rolls;
- Contest scores;
- Contest effects;
- official Contest ranks or rewards;
- Coordinator Feature outcomes;
- Tutor Point expenditure;
- Move learning;
- battle damage/status from stage spectacle;
- mechanical reputation from applause;
- audience unanimity;
- Pokémon consent or ownership;
- tactical combatants from stage presence.

Minecraft/Cobblemon/Craftics may present:

- performers;
- audiences;
- stages;
- props and costumes;
- lighting and visual weather;
- rehearsals;
- schedules and posters;
- applause animation;
- already-decided performance outcomes;
- already-decided venue changes.

It may not decide:

- BattleSpec roster;
- PTU HP/status/damage;
- Contest result;
- Appeal result;
- audience canonical opinion;
- whether a show occurred merely because an animation played;
- whether a stage effect is a tactical hazard;
- whether a Pokémon is willing to perform;
- progression or Feature acquisition.

## Unresolved mechanical and canon questions

- Which PTU/Caelo Contest rules version is authoritative for Ouros?
- Does Caelo alter Coordinator, Appeal, Contest, Poffin, Innovation, or Contest Move behavior?
- Which Contest mechanics exist in AutoPTU-Java with parity tests?
- Which Coordinator Features are implemented and tested?
- Does Ouros canon include formal Contest circuits, showcase circuits, theater institutions, touring companies, or regional performance traditions?
- What rules govern safe noncombat use of Moves around audiences?
- Which performance-linked social/reputation effects are authorized by existing systems?
- When should a recurring performance practice be owned by Ritual/Tradition instead of this production layer?
- Which venue safety, licensing, employment, or contract rules exist in canon rather than being inferred from real-world practice?

Pass 159 makes no canon promotions and no engine capability promotions.