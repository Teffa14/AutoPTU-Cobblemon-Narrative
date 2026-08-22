# Engine Readiness Snapshot — Pass 113

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `bc22b78e0a46bd65b6d5ddc38fcabe0b8368440b`

Relevant Java evidence since Pass 112:

- Trainer Feature bookkeeping is bound to authoritative runtime state;
- generic Trainer Feature target scopes are parity-backed;
- generic trainer-target scopes are parity-backed;
- Trainer Feature temporary HP grants are authoritative and parity-backed;
- generic Trainer Feature grant-AP effects now have a Java/Python parity slice;
- the generic execution framework continues to separate effect semantics from the transaction/gate machinery.

These commits strengthen Trainer Feature/perk execution infrastructure. They do not demonstrate the full Trainer Feature catalog, environmental water mechanics, utility operations, drinking-water rules, tactical currents, pipe/pump behavior, contamination, or Minecraft adapter support.

AutoPTU `main`: `79263b8f6bce65e65b12e1dff98219d8b129b7ca`

The latest visible Python changes are Career/UI/rendering oriented and do not justify changing the tactical capability map used by this narrative repository.

## Java README evidence

The live Java README still declares these major families unfinished:

- expanded core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic battle-event/full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Representative mechanics remain representative only.

## Permanent capability categories

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent capability category is promoted in Pass 113.

## Why water-service world state is not a battle mechanic

Nothing inspected in AutoPTU-Java proves:

- potable-water state;
- drinking/dehydration rules;
- treatment chemistry;
- service pressure;
- water-main flow;
- pipe breaks;
- valve operation;
- pump operation;
- tank/reservoir utility behavior;
- contamination transport through a distribution network;
- low-pressure contamination;
- waterborne illness;
- emergency water distribution;
- moving floodwater/current physics;
- drowning/suffocation;
- slippery-surface rules;
- electrical-water hazards;
- utility-worker escort behavior;
- valve/pump objective interaction;
- water-service aware Minecraft state synchronization.

Therefore Pass 113 keeps service-chain state outside AutoPTU.

## Trainer Feature evidence boundary

The newest Java slices continue to strengthen the generic Trainer Feature execution path, including:

- prerequisites/context/frequency/resources/bookkeeping from prior slices;
- generic target scopes;
- trainer-target scopes;
- heal/Combat Stage/temporary-HP/AP effect primitives in tested contracts.

Trainer Features/perks remains PARTIAL because:

- concrete Feature coverage is incomplete;
- effect-family coverage is incomplete;
- target semantics are not the same as full catalog support;
- interrupts/reactions remain incomplete;
- environmental/movement Feature effects depend on blocked families;
- transcript parity is incomplete;
- Minecraft playback is absent.

A utility operator, engineer, water technician, researcher or Water-type partner does not gain any PTU Feature automatically.

## Pass 113 encounter dependency map

### Intake Access Interruption — FULL

Narrative objective:
Allow technicians to inspect an intake while preserving uncertainty about whether nearby wild Pokémon, infrastructure or source state caused the reduced flow.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for technician movement, withdrawal routes and protected access
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if water, machinery, access zones or environmental state receive tactical mechanics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_TECHNICIAN`, `REACH_CONTROL`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Technicians withdraw and isolate the intake in world state. Freeze one dry safe arena adjacent to the facility. AutoPTU receives only actual combatants. Inspection and service restoration resume afterward.

### Main Break at Market Street — FULL

Narrative objective:
Handle a distribution-main failure overlapping with an urban disturbance without letting battle outcome become the repair result.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING for worker/civilian evacuation, route clearing and interception
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where invoked
- terrain/weather/hazards/zones/reactions: BLOCKING if excavation, flowing water, equipment or protected zones become tactical
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `PROTECT_WORK_ZONE`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Close the street and evacuate noncombatants in world state. Isolate the failed main. If confrontation remains, use a dry static adjacent arena. Technical repair is resolved separately.

### Emergency Tank Transfer — FULL

Narrative objective:
Move emergency water through a constrained route to a temporary distribution point while normal service is unavailable.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED for ordinary combatants
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING for convoy/cargo route protection
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where invoked
- terrain/weather/hazards/zones/reactions: BLOCKING only if validated environmental mechanics are part of the route
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `PROTECT_ROUTE`, `REACH_EXIT`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Keep tankers/cargo outside the grid. Resolve one static chokepoint battle if necessary. Supply Chains and Water Service then resolve delivery and custody.

## New overworld blockers introduced by Pass 113

These belong outside AutoPTU-Java:

- `WATER_SERVICE_SYSTEM_STATE`
- `RAW_WATER_SOURCE_HANDOFF`
- `WATER_INTAKE_IDENTITY_AND_OPERATION`
- `WATER_TREATMENT_SITE_STATE`
- `WATER_TREATMENT_PROCESS_REVISION`
- `FINISHED_WATER_STORAGE_STATE`
- `WATER_DISTRIBUTION_ZONE_STATE`
- `WATER_NETWORK_LINK_HISTORY`
- `SERVICE_POINT_STATE`
- `WATER_QUALITY_OBSERVATION_PROVENANCE`
- `WATER_QUALITY_ASSESSMENT_HISTORY`
- `WATER_SERVICE_INCIDENT_GRAPH`
- `WATER_LEAK_CASE_STATE`
- `NETWORK_ISOLATION_AND_VALVE_AUTHORITY`
- `WATER_SERVICE_ADVISORY_HANDOFF`
- `EMERGENCY_WATER_DISTRIBUTION_STATE`
- `WATER_SERVICE_RECOVERY_REVIEW`
- `WATER_DEMAND_REVISION_STATE`
- `WATER_SERVICE_RESILIENCE_MEASURES`
- `GROUNDWATER_TO_WATER_SERVICE_HANDOFF`
- `FRESHWATER_TO_WATER_SERVICE_HANDOFF`
- `TECHNOLOGY_TO_WATER_SERVICE_HANDOFF`
- `SUPPLY_CHAIN_TO_WATER_SERVICE_HANDOFF`
- `WATER_SERVICE_TO_HEALTH_SURVEILLANCE_HANDOFF`
- `WATER_SERVICE_TO_COMMUNICATIONS_HANDOFF`
- `WATER_SERVICE_TO_MINECRAFT_PROJECTION`
- `WATER_SERVICE_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 113

Do not infer:

- visible water -> potable water;
- full source/reservoir -> adequate service;
- working intake -> working treatment;
- working treatment -> working distribution;
- one working zone -> entire settlement working;
- normal pressure -> accepted water quality;
- low pressure -> contamination occurred;
- clear water -> safe water;
- smell/taste complaint -> toxicity;
- advisory -> contamination confirmed;
- lack of advisory -> water safe;
- one sample -> whole-network truth;
- source finding -> every endpoint affected;
- endpoint finding -> source caused it;
- Water-type -> purification capability;
- Water Gun/Hydro Pump -> potable water;
- Rain Dance -> municipal supply;
- Hydration/Rain Dish/Water Absorb -> treatment or drinking rules;
- Poison-type presence -> contamination;
- Ground-type presence -> pipe break;
- Electric-type presence -> pump outage;
- pipe break -> sabotage;
- moved valve -> malicious action;
- battle victory -> intake repaired;
- battle victory -> water safe;
- emergency water delivered -> normal service restored;
- Minecraft block water level -> authoritative service pressure;
- Minecraft valve model -> authorized operational state.

## PTU/Caelo validation state

No reliable primary Caelo source or Super PTU Online Helper capability was available for a potable-water subsystem during this run.

No generic PTU drinking-water subsystem was validated.

Unresolved mechanics therefore remain blocked:

- drinking/dehydration;
- water purification;
- contamination/exposure;
- Water-type utility work;
- pump/valve interaction;
- pipe/main damage;
- environmental water hazards;
- currents;
- drowning/suffocation;
- any Skill or Trainer Feature used for municipal water operations.

Do not invent outputs from unavailable sources.

## Mechanical/canon questions still unresolved

- Which settlements have centralized treatment/distribution?
- Which use wells, springs, cisterns or local systems?
- Who operates each service?
- What technology level is normal?
- What is considered an acceptable water-quality assessment in-universe?
- Which service records are public?
- Which critical facilities maintain local reserves?
- How much network topology is worth persisting?
- How should old mains and tanks remain represented after physical Minecraft redevelopment?
- Which Pokémon have authored relationships with source/intake/storage infrastructure?
- Can any Pokémon serve institutional utility roles, and under what consent/agency model?
- What exact PTU/Caelo rules govern drinking, environmental contamination, purification and water-related hazards?

Until these are resolved, drinking-water service remains authoritative overworld state that may feed only validated frozen battle snapshots into AutoPTU.