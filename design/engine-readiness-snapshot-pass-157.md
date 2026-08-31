# Engine Readiness Snapshot — Pass 157

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `dd633d5df4ecb352a3165883301a898434295aba`
Date: 2026-08-30

## Read-only engine heads inspected

AutoPTU-Java:

`28c099cde811646ea1ddae66f676b45ad848666b` — `Merge pull request #291 from Teffa14/parity/intercept-authoritative-candidate-plan / Compose Intercept discovery into authoritative attempt planning`

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`

No files in either engine repository were modified by Pass 157.

AutoPTU-Java advanced since Pass 156. AutoPTU did not.

## New Java evidence

The current AutoPTU-Java head adds `RuntimeInterceptAttemptPlanner` and tests/workflow coverage around that planner.

The planner composes:

- candidate discovery from authoritative `BattleRuntimeState` plus canonical combatant rule content;
- Python-compatible temporary-effect cleanup;
- candidate ordering through the shared footprint-geometry contract;
- internal spatial attempts derived after discovery rather than caller-prepared candidate plans.

The adapter supplies canonical combatant content rather than prepared Intercept candidates.

This strengthens the server-owned Intercept path and reduces another opportunity for Minecraft/Cobblemon to decide tactical candidates or ordering.

The evidence is still localized. It does not prove every member of the complete-movement or reaction families.

Still unverified globally:

- every Push source;
- Pull;
- general Knockback;
- every Intercept form and ordering interaction;
- arbitrary forced movement;
- escort/rescue movement;
- object carrying;
- moving carts or vehicles;
- dynamic gates;
- crop/terrain collision semantics;
- weather-driven movement;
- generalized reaction windows;
- tactical protect, flee, delay, herd or access-denial policy.

The AutoPTU head remains presentation-only and explicitly does not change battle rules or outcomes.

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

No category is promoted by Pass 157.

## Orchard Storm-Damage Perimeter — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for static legal movement
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL if falling debris, edge displacement or constrained Intercept matters
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for changing storm/debris phases
- full stateful damage pipeline — PARTIAL as selected battle content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING for active weather, falling hazards, wet/obstructed zones or reaction windows
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for withdraw, protect, route-control or area-denial behavior
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative dynamic-weather/hazard playback

Overall full status: BLOCKED.

Reduced status: READY at narrative-contract level if selected Moves, Abilities, Items and Features are individually audited.

Reduced constraints:

- storm ends before initiative;
- no active weather mechanics;
- workers, produce and semantic crop objects remain outside BattleSpec;
- static safe geometry only;
- explicit combatants;
- permitted tactical result: `IMMEDIATE_ORCHARD_APPROACH_CLEAR`.

Hard safeguards:

`APPROACH_CLEAR != HARVEST_SAVED`

`BATTLE_WON != DAMAGE_ASSESSED`

`BATTLE_WON != PRODUCTION_RESTORED`

## Irrigation Gate Access Corridor — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for static movement
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL if current or forced displacement matters
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for changing water or gate phases
- full stateful damage pipeline — PARTIAL as selected battle content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING for current, depth, changing water, gate zones or reaction windows
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for access denial, withdrawal or gate-control objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative moving-water/gate playback

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- water and service state are frozen by Ouros before initiative;
- gate, controls, crops and technicians remain outside BattleSpec;
- static geometry;
- explicit combatants;
- permitted result: `IMMEDIATE_IRRIGATION_GATE_ACCESS_CLEAR`.

`ACCESS_CLEAR != GATE_OPERATED`

`ACCESS_CLEAR != WATER_DELIVERED`

`BATTLE_WON != CROP_RECOVERED`

## Harvest Cart Staging Perimeter — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL; object carrying, escort and vehicle/cart semantics remain unverified
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for staged departures or arrival timing
- full stateful damage pipeline — PARTIAL as selected battle content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if moving lanes, loading zones or dynamic hazards matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for escort, delay, diversion, withdrawal or protection objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for moving carts/cargo and authoritative tactical playback

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- carts and cargo are stationary and outside BattleSpec;
- workers remain outside BattleSpec;
- no carrying, escort or vehicle objective;
- static geometry;
- explicit combatants;
- permitted result: `IMMEDIATE_HARVEST_STAGING_APPROACH_CLEAR`.

`APPROACH_CLEAR != CART_DEPARTED`

`BATTLE_WON != SHIPMENT_DELIVERED`

`BATTLE_WON != GOODS_TRANSFERRED`

## Ranch Holding-Perimeter Incident — full version

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for ordinary static movement
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL; escort/herding/rescue semantics remain unverified
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for staged evacuation or gate changes
- full stateful damage pipeline — PARTIAL as selected combat content requires
- status lifecycle — PARTIAL as selected combat content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if dynamic gates, holding zones or reaction windows matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protect, escort, herd, capture, withdraw or route-control semantics
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for authoritative noncombatant movement and dynamic gate playback

Overall full status: BLOCKED.

Reduced status: READY only if Ouros establishes before initiative that all noncombatant work Pokémon/animals are already in a safe holding area.

Reduced constraints:

- noncombatants remain outside BattleSpec;
- gates remain static scenery;
- no herd, escort, capture or rescue objective;
- explicit combatants only;
- permitted result: `IMMEDIATE_RANCH_PERIMETER_CLEAR`.

Hard safeguards:

`PERIMETER_CLEAR != NONCOMBATANT_OWNERSHIP_CHANGED`

`TACTICAL_FAILURE_WITHOUT_HARM_CONTRACT != NONCOMBATANT_HARM_CONFIRMED`

`BATTLE_WON != RANCH_OPERATION_RESTORED`

## Agriculture authority boundary

Pass 157 gives Narrative continuity authority only over authored or evidence-supported records such as:

- production-site identity and ordinary role;
- production-cycle history;
- expected windows as claims or approved facts;
- individual Pokémon work participation;
- harvest events;
- post-harvest stage history;
- observed loss events and their scopes;
- explicitly authored production dependencies;
- local supply observations;
- temporary substitutions;
- recovery episodes.

It does not give Narrative authority to manufacture:

- universal crop timers or yield formulas;
- food-consumption/starvation mechanics;
- crop disease or soil simulation;
- universal spoilage rules;
- irrigation physics;
- generic pollination dependencies;
- generic Pokémon labor capabilities by species or type;
- domestication or ownership rules;
- automatic price changes;
- food-safety law;
- farming licenses or land law;
- Move/Ability/Feature effects on agricultural output without source verification.

## Minecraft/Cobblemon/Craftics boundary

Presentation may show authored fields, berry plots, paddocks, orchards, crates, workers, work Pokémon, seasonal visual changes, damaged plants, closed irrigation gates and later recovery.

Minecraft crop growth, breeding, mob AI, pathfinding, redstone, block destruction, water simulation or Cobblemon BattleState cannot decide:

- whether a production cycle advanced;
- harvest quantity or quality;
- food availability;
- ownership or custody;
- Pokémon work consent/role;
- irrigation success;
- shortage or recovery;
- combatants;
- PTU HP/status/damage;
- tactical outcomes.

## PTU/Caelo unresolved questions

Remain UNKNOWN until source-checked and approved:

- exact agricultural uses of Skills;
- any farming-specific Trainer Features;
- exact Move/Ability interactions with cultivation, weather protection, irrigation, harvesting or storage;
- food and starvation rules if any are intended for Ouros;
- Pokémon ownership/custody consequences of long-term work participation;
- crop growth/yield mechanics;
- spoilage mechanics;
- ranching/domestication assumptions;
- agricultural inspection, land tenure or food regulation;
- any universal Skill Check capable of determining yield, safety or causal truth.

## Pass conclusion

The new Java Intercept planner improves authoritative candidate planning but does not remove the blockers that matter to rich agricultural encounters: dynamic weather/hazards, complete movement, escort/carry semantics, tactical AI policy and authoritative adapter playback remain insufficiently verified.

Therefore Pass 157 makes no capability promotion and keeps rich versions blocked while preserving reduced static BattleSpec variants.