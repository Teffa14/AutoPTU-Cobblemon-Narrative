# Engine Readiness Snapshot — Pass 112

Status: EVIDENCE SNAPSHOT. This file records live implementation evidence used by narrative authoring. It does not change engine capability status by itself.
Date: 2026-08-28

## Read-only repositories inspected

AutoPTU-Java head inspected:

`9f63f0a81af45af2fbc87928b96c1cec4fcff4b0`

PR #262 / commit: `Rebind move preparation after pre-resolution target replacement`.

AutoPTU head inspected:

`6776984aa4a19449b85858a8bc61a18671e5551b`

PR #220 / merge: `Career: harden malformed initial battle combatants`.

Neither repository was modified by this pass.

## Java live evidence

Java remains at the same head as Pass 111. The server-owned pre-resolution path applies target replacement and then rebuilds target-bound move preparation from the effective authoritative defender before accuracy RNG. Tests cover rebinding of target identity/anchor, defense and evasion for the redirected target and preserve the adapter boundary.

This materially strengthens one narrow Intercept/target-replacement composition path. It does not prove completion of the permanent `complete movement including push/pull/knockback/interception/forced movement` family.

Still not demonstrated as complete families:

- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- environmental displacement;
- generalized competing reactions;
- generalized reaction ordering outside implemented target-replacement paths;
- every Move registration;
- every Ability registration;
- every Item registration;
- every Trainer Feature/perk registration;
- complete environmental hazard/zone semantics;
- objective-aware tactical policy;
- semantic Minecraft/Cobblemon/Craftics playback.

A representative hook, registry or implemented reaction path does not promote a permanent category.

## AutoPTU live evidence

AutoPTU advanced from Pass 111 to `6776984aa4a19449b85858a8bc61a18671e5551b`, PR #220.

The merge hardens legacy Career battle transcripts at the API boundary. An `initial_state` is now accepted as structurally usable only when it is an object whose `combatants` field is an array; missing, null or malformed state falls back to an empty valid BattleFrame shape. Associated tests were updated.

This is replay/client stability and backward-compatibility work. It does not add tactical targeting, movement, reactions, damage, status, AI policy or adapter semantics.

No capability promotion follows.

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

No permanent category is promoted in Pass 112.

## Pass 112 concept boundary

Cold-chain continuity is primarily overworld state. Monitoring, storage condition, equipment readiness, custody and batch disposition do not belong inside AutoPTU unless an actual battle mechanic is deliberately authored and supported by an exact governing rule.

The narrative system must never translate a cold room, freezer, refrigerated vehicle, ice block, frost visual or biome temperature into PTU battle effects by itself.

## Encounter 1 — Loading-Bay Withdrawal

Full intended version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL if timed withdrawal matters
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL where exact legal effects apply
- terrain/weather/hazards/zones/reactions: BLOCKING for generalized reactions or operational restricted zones
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for withdrawal/protection behavior
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

Additional objective contract: withdrawal/protection semantics are not verified as a complete tactical policy.

Reduced version:

Stop the physical transfer before BattleSpec creation. Evacuate workers and civilians through overworld state. Keep controlled goods, vehicles and active handling/refrigeration equipment outside the grid or as inert, non-targetable scenery. Use a static reviewed loading bay with explicit combatants. Victory can establish only `IMMEDIATE_LOADING_BAY_SECURED`. Courier, Storage, Cold Chain and Batch Traceability resume their own workflows afterward.

## Encounter 2 — Backup-Room Perimeter

Full intended version dependencies:

The verified core remains available. Intercept/forced movement remains PARTIAL when used. Generalized reactions and any technical/environmental restricted areas require the BLOCKING `terrain/weather/hazards/zones/reactions` family. Objective-aware equipment/route protection needs BLOCKING tactical policy. Semantic playback remains BLOCKING.

If the full concept attempts to make low temperature, condensation, a slippery surface, electrical equipment, a refrigerant-like substance or any other technical condition change battle state, it also requires:

- an exact PTU/Caelo governing rule for that effect;
- full stateful damage pipeline where damage applies: PARTIAL;
- status lifecycle where a status applies: PARTIAL;
- complete movement where forced/sliding displacement applies: PARTIAL;
- the environmental family: BLOCKING.

Reduced version:

Verify/isolate the room as world state before battle. Keep equipment, controlled subjects and technicians outside BattleSpec. Resolve a static dry corridor/yard encounter. The tactical result secures access only. Facility verification and controlled-subject movement happen later.

## Encounter 3 — Interrupted Courier Diversion

Full intended version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL when route protection/Intercept is used
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL for timed route objectives
- damage/status: PARTIAL as normally applicable
- terrain/weather/hazards/zones/reactions: BLOCKING for generalized reactions or active environmental/vehicle zones
- move/ability/item/Trainer Feature behavior: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Active vehicle motion, refrigeration machinery or temperature-changing cargo are not currently supported as automatic tactical mechanics.

Reduced version:

Stop the carrier outside the tactical area. Custody remains unchanged during combat. Shipment and vehicle do not enter BattleSpec. Resolve a static route-junction encounter. Victory secures the junction only; Courier decides subsequent route/custody state and Cold Chain preserves condition evidence.

## Cold-chain mechanical unknowns

Current PTU/Caelo plus live engine evidence does not verify a universal contract for:

- refrigerated/frozen temperature thresholds;
- spoilage timers;
- food-safety state changes from temperature;
- medicine potency degradation from exposure;
- cold-room or freezer damage;
- automatic Frozen or other statuses from storage environments;
- slippery-floor forced movement from visual ice;
- thermal inertia or warm-up/cool-down arithmetic;
- refrigerated-vehicle thermal performance;
- active refrigeration equipment as tactical objects;
- cold-chain repair or certification Skill checks;
- environmental effects from condensation or technical fluids;
- Ice-type immunity/tolerance to occupational cold;
- species-derived refrigeration output;
- Move/Ability/Item/Trainer Feature-powered cooling without exact rules;
- rescue/carry rules for workers or controlled goods during active combat.

These remain UNKNOWN rather than being fabricated by Narrative or the Minecraft adapter.

## PTU/Caelo guardrail

The internal source scan remains controlling. Caelo can define mechanical identity for specific authored locations or circumstances where the governing source explicitly supplies an effect. This does not authorize a universal `cold room = ice terrain`, `freezer = damage`, `temperature excursion = item invalid` or `Ice Pokémon = refrigeration` rule.

Before a temperature-controlled environment enters BattleSpec mechanically, authoring needs both:

1. an exact governing PTU/Caelo source for the intended effect; and
2. current engine tests/contracts supporting every permanent capability family that effect requires.

Otherwise the condition remains overworld state, inert scenery or is removed from the reduced tactical arena.

## Minecraft/Cobblemon/Craftics boundary

Presentation can reuse cold-room structures, insulated doors, containers, storage props, refrigeration machinery models, vehicles, lights, alarms, gauge/screen UI, frost/condensation particles, sounds, NPCs, Pokémon models/forms/poses/animations/cries, networking, tracking and persistence hooks.

The adapter must preserve authoritative IDs for controlled subject, continuity record, segment, observation, storage zone, shipment/custody handoff and excursion review where those objects exist.

Presentation must not infer authority from visuals:

- Minecraft biome temperature does not establish a condition observation;
- frost or ice blocks do not prove controlled-subject continuity;
- redstone power does not prove refrigeration readiness;
- chest/item location does not prove custody transfer;
- a moving minecart/vehicle does not prove shipment-leg completion;
- Minecraft ice/slipperiness does not execute PTU forced movement;
- powder-snow/freezing damage does not substitute for the PTU damage/status pipeline;
- particles do not create exposure or status;
- an Ice-type Pokémon near equipment does not maintain refrigeration;
- Cobblemon BattleState/controller logic does not select combatants or decide legality, HP/status, positions or results.

Ouros owns world facts and combatant selection. AutoPTU owns tactical legality and resolution. Minecraft/Cobblemon/Craftics presents authoritative outcomes.

## Canon questions carried forward from Pass 112

Unresolved setting questions include:

- which Ouros regions use temperature-controlled storage/transport and which technologies they use;
- which foods, medicines, research samples or other goods have authored condition requirements;
- who operates controlled facilities and transport services;
- what monitoring methods exist by region/institution;
- whether backup cooling or passive storage methods exist and where;
- how evidence/records are shared at custody handoffs;
- which institution owns disposition for each controlled subject type;
- which historical cold facilities were demolished, converted or repurposed;
- what temporary continuity sites became permanent institutions;
- individual Pokémon work roles, if any, with explicit canon/mechanical support.

## Promotion rule

Do not promote `complete movement including push/pull/knockback/interception/forced movement` because the Intercept target-replacement path is increasingly well composed. Do not treat hook-source enums or extensible registries as proof of all reactions/Abilities/Items/Features. Do not promote environmental mechanics, tactical policy or adapter support without broad tested contracts.

Pass 112 therefore leaves the permanent map unchanged.