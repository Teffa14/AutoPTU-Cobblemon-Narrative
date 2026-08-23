# Engine Readiness Snapshot — Pass 121

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU were inspected read-only.

## Live heads inspected

AutoPTU-Java `main`: `46b8873df5839cca1b57106a16248c457d93f5fe`

Newest Java slice freezes a consumable Safeguard status-prevention contract against the Python oracle. It follows the previous Ability-based status-prevention work and adds evidence that a field/status-prevention boundary can be consumed authoritatively when applicable. This is representative status-controller progress only. It does not complete all statuses, field effects, durations, stacking, immunities, reactions or Move/Ability interactions.

AutoPTU `main`: `c3e67a718fca2d92ecc8316cfa98f757977f7986`

Newest Python change fixes a Color Change same-type battle crash by keeping event emission inside the actual type-change guard. This is a focused Ability regression fix. It does not by itself promote the Ability category or any other permanent capability family.

## Java README evidence

The live README still lists these major areas as incomplete:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature registries;
- semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Permanent capability categories

VERIFIED:
- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL:
- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING:
- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 121.

## Why emergency dispatch belongs outside the battle core

Nothing inspected establishes authoritative overworld systems for:

- emergency service registries;
- dispatch centers;
- incoming incident queues;
- triage/priority assessment;
- unit readiness/availability;
- unit assignment and routing;
- staging;
- mutual-aid activation;
- operational objective tracking;
- patient/rescue handoffs;
- demobilization;
- after-action review;
- responder coverage maps;
- emergency communications interoperability;
- responder Pokémon institutional participation.

These belong to persistent world/server state. AutoPTU should receive only the frozen tactical encounter once world-state coordination has established who is actually present and what battle-relevant conditions are valid.

## Pass 121 encounter dependency map

### Station Access Fire — FULL

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for actual fire/smoke behavior
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for WITHDRAW/PROTECT/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: world state evacuates responders, secures equipment and freezes a safe static tactical room. Fire/smoke remain world-state hazards only. AutoPTU resolves conventional combatants. Crisis/Emergency Services then re-evaluate station availability.

### Mountain Rescue Handoff — FULL

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for escort/handoff movement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if snow/cliff/wind hazards are tactical
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for REACH_OBJECTIVE/WITHDRAW/PROTECT
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: rescue, stabilization and transport movement remain overworld state. A separate static encounter can pause the transfer. Care/Transport resumes the handoff afterward.

### Mutual-Aid Chokepoint — FULL

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if a validated incident hazard enters battle
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for CLEAR_ROUTE/WITHDRAW/PROTECT
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: dispatch resolves arrival order and civilians/wildlife clear the route in world state. Services keep separate authority. AutoPTU receives a static conventional encounter if a confrontation remains.

## New overworld blockers introduced by Pass 121

- `EMERGENCY_SERVICE_REGISTRY`
- `RESPONSE_UNIT_STATE`
- `UNIT_READINESS_AND_AVAILABILITY`
- `INCIDENT_REQUEST_QUEUE`
- `TRIAGE_PRIORITY_REVISION`
- `DISPATCH_ASSIGNMENT_STATE`
- `UNIT_ROUTE_AND_ARRIVAL_STATE`
- `INCIDENT_OPERATION_GRAPH`
- `OPERATIONAL_OBJECTIVE_STATE`
- `STAGING_SITE_STATE`
- `MUTUAL_AID_ACTIVATION`
- `RESPONSE_RESOURCE_REQUESTS`
- `RESPONDER_HANDOFF_LEDGER`
- `DEMOBILIZATION_STATE`
- `AFTER_ACTION_REVIEW_STATE`
- `EMERGENCY_COVERAGE_MODEL`
- `EMERGENCY_COMMUNICATION_INTEROP`
- `RESPONDER_POKEMON_PARTICIPATION_STATE`
- `CRISIS_TO_DISPATCH_HANDOFF`
- `COMMUNICATIONS_TO_DISPATCH_HANDOFF`
- `DISPATCH_TO_TRAVEL_HANDOFF`
- `DISPATCH_TO_CARE_HANDOFF`
- `DISPATCH_TO_SUPPLY_CHAIN_HANDOFF`
- `DISPATCH_TO_MINECRAFT_PROJECTION`
- `INCIDENT_TO_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 121

Do not infer:
- emergency report -> hazard truth;
- dispatch priority -> canonical severity;
- responder uniform -> universal authority;
- unit assignment -> arrival;
- arrival -> access;
- staging -> combat buff;
- leadership title -> Command Skill/Feature;
- Water-type/Water Move -> firefighting effectiveness;
- Flying/Sky -> passenger extraction legality;
- healing Move -> clinical authorization;
- battle victory -> rescue complete;
- battle victory -> evacuation complete;
- Fainted opponent -> site safe;
- unit unavailable -> negligence;
- delayed response -> misconduct;
- mutual aid -> merged institutions;
- responder Pokémon -> service property;
- alarm -> confirmed emergency;
- after-action finding -> retroactive rewrite of incident truth.

## PTU/Caelo validation state

No complete primary Caelo corpus was recoverable from the accessible project sources during this run. Super PTU Online Helper was not exposed as an invocable capability.

Pass 121 therefore does not validate or invent:
- firefighting rules;
- rescue/carry rules;
- civilian mechanics;
- panic/fear status;
- medical triage bonuses;
- emergency vehicle movement;
- command radius;
- responder Features;
- hazard damage;
- smoke effects;
- evacuation Skill checks;
- Pokémon institutional obedience.
