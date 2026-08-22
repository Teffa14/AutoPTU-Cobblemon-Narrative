# Engine Readiness Snapshot — Pass 114

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `dbc1bfb14c0e0036c1cc3301d35355d36611bf4b`

Newest relevant Java evidence:

- canonical status state now preserves ordered stacked status entries rather than collapsing duplicate normalized names;
- the new status-stack contract includes replace/append/remove semantics and parity fixtures against a pinned Python oracle;
- representative Trainer Feature status application behavior is now frozen against Python for that storage contract;
- prior slices already established generic Trainer Feature prerequisites, context, frequency/cooldown, resources, bookkeeping, target scopes, heal, Combat Stage, temporary HP and AP effect primitives.

This is meaningful progress for status state and Trainer Feature infrastructure. It does not demonstrate the full status lifecycle, full Trainer Feature catalog, complete environmental rules or any fluvial mechanics.

AutoPTU `main`: `8108e0d2b876414a5e62c2021801a3692cda05b8`

The newest visible Python commits remain Career/persistence/UI oriented and do not justify a tactical capability promotion.

## Java README evidence

The live Java README still lists as unfinished:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic full transcript parity;
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

No permanent category is promoted in Pass 114.

## Status-stack evidence boundary

The latest Java slice proves that canonical status storage can preserve duplicate/stacked entries and ordered status metadata in tested contracts.

It does not prove:

- every status can stack;
- all stacking rules are implemented;
- all status durations/expiry rules are complete;
- all status application immunities are complete;
- environmental effects can create statuses;
- river mud/water/erosion can create Slowed, Tripped, Poisoned, Burned or other statuses;
- status interactions with all Moves/Abilities/Features are complete.

Therefore `status lifecycle` remains PARTIAL.

## Why fluvial geomorphology is not a battle mechanic

Nothing inspected in AutoPTU-Java proves:

- live river-channel migration;
- bank erosion;
- bank collapse;
- point-bar growth;
- sediment transport;
- island formation/loss;
- meander cutoff;
- avulsion;
- oxbow formation;
- side-channel activation;
- dynamic floodplain geometry;
- moving bridge/ferry access;
- current-driven forced movement;
- shallow/deep water transitions during battle;
- erosion-triggered falling;
- sediment-plume visibility penalties;
- river-aware tactical AI;
- Minecraft river-revision synchronization.

These remain overworld/world-state responsibilities until an explicit battle projection exists.

## Pass 114 encounter dependency map

### Cutoff Bend Survey — FULL

Narrative objective:
Collect observations around a newly active shortcut channel while wildlife attempts to leave the area safely.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `REACH_SURVEY_POINT`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Resolve high-flow/channel state before combat. Remove surveyors from the tactical grid. Freeze one bank/bar geometry and run only actual combatants.

### Oxbow Reconnection — FULL

Narrative objective:
Document temporary reconnection between the main river and an oxbow while avoiding trapping or unnecessarily fighting wildlife.

Dependencies:

- targeting/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where invoked
- terrain/weather/hazards/zones/reactions: BLOCKING if water connectivity changes grid movement
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW` / `REACH_EXIT`
- adapter/playback: BLOCKING

Reduced version:
Advance reconnection and wildlife movement in world state first. If conflict remains, freeze one shoreline snapshot and use a conventional static battle.

### Bridge on the Old Channel — FULL

Narrative objective:
Inspect a bridge still spanning a former channel while modern flow, travelers and wildlife use adjacent routes.

Dependencies:

- targeting/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception: BLOCKING for route clearing and protected movement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where invoked
- terrain/weather/hazards/zones/reactions: BLOCKING only if bank/water/structure state receives tactical mechanics
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `EVACUATE`, `CLEAR_ROUTE`, `PROTECT`
- adapter/playback: BLOCKING

Reduced version:
Resolve inspection, access and civilian movement before battle. Freeze a dry/static work perimeter adjacent to the bridge and resolve only the confrontation.

## New overworld blockers introduced by Pass 114

These belong outside AutoPTU-Java:

- `FLUVIAL_SYSTEM_GEOMORPHIC_STATE`
- `CHANNEL_GEOMETRY_REVISION_HISTORY`
- `CHANNEL_MIGRATION_ZONE_STATE`
- `BANK_SEGMENT_HISTORY`
- `FLUVIAL_BAR_IDENTITY_AND_REVISION`
- `FLUVIAL_ISLAND_IDENTITY_AND_REVISION`
- `SIDE_CHANNEL_IDENTITY_AND_STATE`
- `ABANDONED_CHANNEL_IDENTITY_AND_SUCCESSION`
- `FLUVIAL_CHANGE_EVENT_GRAPH`
- `FLUVIAL_GEOMORPHOLOGY_OBSERVATION_PROVENANCE`
- `SEDIMENT_SOURCE_CLAIM_GRAPH`
- `FRESHWATER_TO_FLUVIAL_GEOMORPHOLOGY_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_CARTOGRAPHY_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_TRAVEL_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_LAND_TENURE_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_CONSERVATION_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_INFRASTRUCTURE_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_MINECRAFT_PROJECTION`
- `FLUVIAL_GEOMORPHOLOGY_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 114

Do not infer:

- high flow -> channel migration;
- flood -> avulsion;
- erosion observation -> immediate collapse;
- bank collapse -> PTU damage;
- wet bank -> Tripped/Slowed;
- point bar -> Rough Terrain or cover;
- island -> safe zone;
- floodplain -> Water Terrain;
- side channel -> dynamic battle water;
- oxbow -> Wetlands mechanical tag;
- sediment plume -> Accuracy penalty;
- river migration -> building failure;
- newly exposed land -> unowned/public land;
- river boundary wording -> legal boundary moves automatically;
- Absol/Water/Ground-type presence -> cause of channel change;
- Water-type Move -> flood-scale river-form change;
- Ground-type Move -> regional erosion/avulsion;
- Minecraft water/block update -> authoritative geomorphic revision;
- stacked status support -> environmental status subsystem.

## PTU/Caelo validation state

No primary Caelo rule or Super PTU Online Helper capability was available as a reliable invocable source during this run.

No generic PTU fluvial-geomorphology subsystem was validated.

Potentially relevant exact rules remain pending for Swim, Naturewalk, Groundshaper, currents, falling, forced movement, shallow/deep water and environmental hazards.
