# Engine Readiness Snapshot — Pass 112

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `63526aa2dce83d0faa22b364705cd36f590d964b`

Relevant new Java evidence since Pass 111:

- server-owned temporary HP now exists on runtime combatants;
- a generic temporary-HP grant primitive matches Python behavior for tested cases;
- Trainer Feature generic effects can grant temporary HP through the authoritative runtime;
- Heal Block / Heal Blocked and `temp_hp_locked` gates are covered in the parity-backed slice;
- grants stack additively in the tested Python-compatible contract.

This strengthens Trainer Feature effect execution and shared runtime state. It does not demonstrate the full Trainer Feature catalog, full healing/damage interaction, complete status lifecycle, environmental effects or urban-wildlife mechanics.

AutoPTU `main`: `f22cdbb831a2749c12c11a5122827c1e69a3c094`

The latest visible Python work remains Career/UI oriented and does not change the tactical capability map used here.

## Java README evidence

The current Java README still declares the following families unfinished:

- core combatant/grid battle state expansion;
- full damage resolution pipeline;
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

No category is promoted in Pass 112.

## Why urban wildlife does not create battle mechanics

Nothing inspected in Java proves:

- crowd/flock movement policy;
- noncombat wildlife withdrawal behavior;
- nest/roost protection zones;
- food-attractant movement;
- habituation-based targeting or capture changes;
- urban Terrain;
- garbage/compost Poison hazards;
- electrical outlet hazards;
- lighting-based accuracy or movement changes;
- civilian evacuation AI;
- deterrent status effects;
- wildlife-aware Minecraft spawn synchronization;
- encounter de-escalation policy;
- coexistence intervention mechanics.

World-state observations and management responses must therefore remain outside AutoPTU until a concrete battle mechanic is verified.

## Trainer Feature evidence boundary

Java now has a growing generic execution framework plus tested effect families including heal, Combat Stage changes and temporary HP grants. Trainer Features/perks remains PARTIAL because:

- concrete Feature coverage is incomplete;
- effect families are incomplete;
- interrupts/reactions remain incomplete;
- movement/environment Feature effects rely on blocked families;
- transcript parity is incomplete;
- Minecraft playback is absent.

No urban-wildlife profession, researcher role, ranger role, sanitation role or technician role grants a PTU Feature automatically.

## Pass 112 encounter dependency map

### Rooftop Roost Maintenance Conflict — FULL

Narrative objective:
Resolve a maintenance/wildlife conflict while workers withdraw and the roost remains a protected world-state object rather than a target to defeat.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for worker evacuation, alternate roost routes and interception
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if roof edges, wind, protected areas or environmental state receive tactical meaning
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_ROUTE`, `CLEAR_WORK_ZONE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Stop maintenance and evacuate workers first. Exclude the roost from the combat arena. Freeze one legal rooftop map and use AutoPTU only for actual combatants. Resolve roost status and work authorization after battle.

### Market Feeding Surge — FULL

Narrative objective:
Reduce an attractant-driven aggregation without treating every background Pokémon as an enemy.

Dependencies:

- targeting/base movement/core/action economy: current VERIFIED scope
- complete movement: BLOCKING for background group movement, civilian evacuation and route clearing
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where invoked
- terrain/weather/hazards/zones/reactions: BLOCKING only if stalls, crowd zones or environmental state gain tactical mechanics
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `DISPERSE`, `WITHDRAW`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Close the relevant market zone and resolve background population movement in world state. Evacuate civilians. If a smaller actual confrontation remains, use one static battle. Update attractant/intervention records afterward; do not mark the whole population defeated.

### Utility Alcove Joltik Investigation — FULL

Narrative objective:
Investigate overlapping Joltik observations and utility anomalies while preserving uncertainty about causality.

Dependencies:

- targeting/base movement/core/action economy: VERIFIED in current ordinary scope
- complete movement/interception: BLOCKING for small access routes, technician movement or wildlife withdrawal
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where invoked
- terrain/weather/hazards/zones/reactions: BLOCKING if electrical infrastructure receives tactical effects
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_TECHNICIAN`, `REACH_CONTROL`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Inspect and isolate the electrical asset first in world state. Freeze power state and use a non-hazardous static arena if combat occurs. Technical diagnosis remains independent from battle outcome.

## New overworld blockers introduced by Pass 112

These belong outside AutoPTU-Java:

- `URBAN_WILDLIFE_PROFILE_STATE`
- `URBAN_WILDLIFE_USE_SITE_IDENTITY`
- `ATTRACTANT_RESOURCE_STATE`
- `HABITUATION_OBSERVATION_HISTORY`
- `FOOD_CONDITIONING_EVIDENCE`
- `URBAN_ROOST_NEST_IDENTITY`
- `JUVENILE_PRESENCE_AND_CARE_INFERENCE`
- `URBAN_WILDLIFE_CONFLICT_INCIDENTS`
- `COEXISTENCE_INTERVENTION_HISTORY`
- `INTERVENTION_FOLLOW_UP_OBSERVATIONS`
- `URBAN_WILDLIFE_PUBLIC_PERCEPTION_HANDOFF`
- `URBAN_WILDLIFE_TO_WASTE_HANDOFF`
- `URBAN_WILDLIFE_TO_LIGHT_HANDOFF`
- `URBAN_WILDLIFE_TO_SOUND_HANDOFF`
- `URBAN_WILDLIFE_TO_TECHNOLOGY_HANDOFF`
- `URBAN_WILDLIFE_TO_ARCHITECTURE_HANDOFF`
- `URBAN_WILDLIFE_TO_ROAD_ECOLOGY_HANDOFF`
- `URBAN_WILDLIFE_TO_DIEL_ACTIVITY_HANDOFF`
- `URBAN_WILDLIFE_TO_COBBLEMON_PROJECTION`
- `URBAN_WILDLIFE_TO_MINECRAFT_PROJECTION`
- `URBAN_WILDLIFE_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 112

Do not infer:

- urban-adapted -> domesticated;
- habituated -> friendly;
- food-conditioned -> aggressive;
- repeated observation -> ownership;
- feeding -> partnership/Loyalty;
- flock -> Pack Mon;
- aggregation -> population increase;
- city habitat -> Urban Terrain;
- nest/roost -> defensive bonus;
- juvenile alone -> abandoned;
- resident complaint -> proven harm;
- complaint -> hostile AI;
- waste association -> Poisoned;
- Trubbish presence -> contamination cause;
- Joltik near an outlet -> electrical hazard;
- Dustox near lights -> accuracy penalty;
- light attraction -> forced movement;
- deterrent -> Fear/Flinch/status;
- successful battle -> coexistence problem solved;
- successful battle -> population removed;
- successful battle -> causal hypothesis confirmed.

## PTU/Caelo validation state

No reliable primary Caelo file was recovered for an urban-wildlife subsystem during this run. The public PTU GM advice reviewed supports urban encounter framing and non-KO wild encounter endpoints but does not define a generic synanthropy/habituation rules family.

Therefore unresolved mechanical questions remain blocked:

- whether any PTU/Caelo rule modifies capture, approach or tracking after repeated feeding;
- exact noncombat withdrawal/surrender behavior;
- handling of nests/juveniles;
- restraint/relocation rules;
- tracking or Perception rules for repeated urban sign;
- any Ranger/Researcher/Survival Feature relevant to coexistence;
- any environmental rule for light, waste or utility interactions.

Do not invent the output of unavailable Caelo material or Super PTU Online Helper.

## Mechanical/canon questions still unresolved

- Which urban Pokémon populations exist before campaign start?
- Which species/population behaviors are authored versus discoverable?
- Which settlements monitor urban wildlife?
- Which institutions have authority to change attractants or restrict access?
- How common is intentional feeding?
- What counts as a confirmed active roost/nest?
- How much behavioral state advances while chunks are unloaded?
- How should repeated group presence project into Cobblemon without creating a spawn exploit?
- How should a persistent individual remain identifiable across despawn/reload?
- Which intervention outcomes are public?
- What exact PTU/Caelo rules govern tracking, withdrawal, restraint, capture, release, relocation and noncombat Pokémon handling?

Until these are resolved, urban-wildlife coexistence remains world-state ecology feeding only validated battle snapshots into AutoPTU.