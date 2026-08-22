# Engine Readiness Snapshot — Pass 109

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `f793666236a19d3c09547e5603a4fa3ec595c899`

Recent relevant Java slices:

1. `Bind Trainer Feature bookkeeping to runtime state (#143)` — moves Trainer Feature execution bookkeeping into authoritative runtime state.
2. `Port generic Trainer Feature target scopes (#144)` — adds parity-backed generic Trainer Feature target resolution and matches Python target truthiness/ID semantics across tested target-scope cases.

These are meaningful improvements to Trainer Features/perks infrastructure. They do not establish complete Feature catalog coverage, concrete environmental effects, Groundshaper semantics, groundwater sensing, tactical objectives, interrupts, or Minecraft playback.

AutoPTU `main`: `e386f3fe9eb83e181be77b1e2869459cdeff78d6`

Recent Python changes inspected are Career/persistence oriented and do not justify changing the tactical capability map.

## Java README evidence

The current Java README still lists the following as unfinished:
- core combatant/grid battle state expansion;
- full damage resolution pipeline;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- full move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Representative implementation remains representative only.

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

## Why Pass 109 does not promote environmental capability

Groundwater is overwhelmingly an overworld/world-state concern.

Nothing in the newly inspected Java commits proves:
- dynamic water levels;
- underground currents;
- flood or seep hazards;
- water-quality effects;
- groundwater-triggered Weather or Terrain;
- Groundshaper well/spring creation;
- environmental Poisoned;
- moving technicians or wildlife objectives;
- groundwater-aware tactical AI;
- projection of aquifer state into Minecraft or AutoPTU.

The existing verified `Swim`/base movement work is not evidence for groundwater mechanics. A legal Swim shift in an authored grid does not prove changing water depth, pumping, spring discharge, water pressure, or aquifer flow.

## Current Trainer Feature evidence

Java now has parity-backed generic infrastructure for:
- prerequisite gates;
- context gates;
- frequency/cooldown gates;
- generic resource gates/consumption;
- usage/cooldown bookkeeping;
- transaction ordering around a concrete effect callback;
- authoritative runtime bookkeeping;
- generic target-scope resolution for the tested cases.

Trainer Features/perks remains PARTIAL because:
- concrete Feature effect coverage is incomplete;
- catalog coverage is not established;
- interrupts/reactions remain incomplete;
- movement/environment effects depend on other incomplete families;
- semantic playback to Minecraft is absent.

Therefore a hypothetical groundwater-related Trainer Feature remains blocked by its concrete effect even though the generic dispatcher infrastructure is stronger.

## Pass 109 encounter dependency map

### Wellfield Access After Storm — FULL

Narrative objective:
Reach selected monitoring points after a storm while preserving the groundwater investigation as evidence-driven world state.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED for ordinary battle targeting
- base movement legality: VERIFIED for static legal movement
- complete movement including interception/forced movement: BLOCKING for moving technicians, protected corridors, rescue-style positioning, or displacement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if stormwater, unstable ground, floodwater, or protected sampling areas gain tactical mechanics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `REACH_SAMPLE_POINT`, `WITHDRAW`, `PROTECT_TECHNICIAN`, or evidence-preservation priorities
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
- resolve storm access and route safety in overworld state;
- move technicians/noncombatants before battle;
- collect samples through Science/Groundwater state;
- freeze one static legal arena if combat remains;
- keep groundwater findings independent of battle result.

### Dry Spring Survey — FULL

Narrative objective:
Investigate why a reliable spring stopped flowing while wild Pokémon still use nearby habitat.

Dependencies:
- ordinary static battle primitives can operate at current VERIFIED/PARTIAL scope;
- complete movement: BLOCKING if wild Pokémon dynamically withdraw/cross the map;
- terrain/weather/hazards/zones/reactions: BLOCKING if spring flow or unstable wet ground changes tactical geometry/effects;
- AI tactical policy: BLOCKING for `WITHDRAW`, `OBSERVE`, `AVOID`, or `CLEAR_ROUTE` behavior;
- adapter/playback: BLOCKING for authoritative world/battle synchronization.

Reduced version:
Survey the spring, wells, vegetation, and route state before combat. If conflict occurs, freeze one static arena and keep all causal hypotheses outside battle.

### Recharge Basin Night Watch — FULL

Narrative objective:
Keep a pilot managed-recharge operation safe while wildlife uses the temporarily wet site.

Dependencies:
- complete movement/interception/forced movement: BLOCKING for moving wildlife corridors and controlled crossings
- terrain/weather/hazards/zones/reactions: BLOCKING for dynamic water level, wet zones, or operational hazards
- AI tactical policy: BLOCKING for `WITHDRAW`, `AVOID_ZONE`, `CLEAR_ROUTE`, `PROTECT_ASSET`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- ordinary combat targeting/calculations/action economy remain usable at their current scopes

Reduced version:
Pause recharge operations, resolve wildlife movement in world state, freeze basin condition, then open a conventional static battle only if a distinct confrontation remains.

## New overworld blockers introduced by Pass 109

These belong outside AutoPTU-Java:

- `GROUNDWATER_SYSTEM_IDENTITY`
- `AQUIFER_UNIT_GEOMETRY_HISTORY`
- `GROUNDWATER_STORAGE_STATE`
- `RECHARGE_ZONE_AND_EVENT_STATE`
- `GROUNDWATER_WELL_STATE`
- `WITHDRAWAL_AND_DRAWDOWN_HISTORY`
- `WELL_INTERFERENCE_ASSESSMENT`
- `SPRING_DISCHARGE_HISTORY`
- `GROUNDWATER_MONITORING_NETWORK`
- `GROUNDWATER_OBSERVATION_PROVENANCE`
- `GROUNDWATER_FLOW_TRAVEL_TIME_CLAIMS`
- `GROUNDWATER_QUALITY_CASE_GRAPH`
- `GROUNDWATER_PLUME_REVISION_HISTORY`
- `MANAGED_RECHARGE_PROJECT_STATE`
- `GROUNDWATER_TO_FRESHWATER_HANDOFF`
- `GROUNDWATER_TO_ESTUARY_HANDOFF`
- `GROUNDWATER_TO_GEOLOGY_CAVE_VOLCANISM_HANDOFF`
- `GROUNDWATER_TO_SANITATION_HEALTH_HANDOFF`
- `GROUNDWATER_TO_AGRICULTURE_SETTLEMENT_HANDOFF`
- `GROUNDWATER_TO_MINECRAFT_PROJECTION`
- `GROUNDWATER_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 109

Do not infer:
- well -> aquifer extent;
- visible water -> groundwater storage;
- cave water -> municipal supply;
- spring -> healing effect;
- spring -> permanent flow;
- rainfall -> immediate recharge;
- drought -> uniform aquifer decline;
- low well -> exhausted aquifer;
- pump failure -> aquifer failure;
- contamination detection -> known source;
- contamination -> Poisoned or damage;
- groundwater plume -> tactical hazard zone;
- groundwater flow -> forced movement/current;
- Water type -> groundwater sensing;
- Ground type -> digging/well capability;
- Groundshaper -> permission or mechanics for aquifer alteration;
- managed recharge -> instant supply increase;
- Minecraft water block -> groundwater truth;
- battle victory -> scientific, access, ownership, or water-allocation conclusion.

## Mechanical/canon questions still unresolved

- Which groundwater systems exist in Ouros at campaign start?
- Which settlements materially depend on wells or springs?
- Who owns/operates monitoring wells versus supply wells?
- How coarse should groundwater storage and recharge be for offline progression?
- Which springs have authored cultural significance?
- Which surface/groundwater links are known at start versus discovered later?
- Can player projects change recharge zones or well-field behavior?
- How should coastal pumping interact with the Estuaries salinity model?
- What level of chemistry should the world track without becoming a laboratory simulator?
- Which PTU/Caelo Skills/Features/Capabilities govern subsurface investigation, Groundshaper, environmental water, Swim, or relevant sensing?
- Should any groundwater state ever enter battle as an environment effect, or should most consequences be frozen before AutoPTU begins?

The full primary Caelo corpus was not reliably accessible during this run. Super PTU Online Helper was not exposed as an invokable capability. No rules or outputs were invented from either source.