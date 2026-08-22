# Engine Readiness Snapshot — Pass 111

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `473067bdd5b22f755014e53235e3b647d662902a`

Current relevant Java evidence:

- generic Trainer Feature prerequisite/context/frequency/resource/usage transaction infrastructure exists for tested slices;
- generic Trainer Feature heal effects have parity-backed execution;
- generic Trainer Feature Combat Stage effects have parity-backed execution;
- runtime Accuracy Combat Stage is mutable where those effects require it.

The live Java head is unchanged from Pass 110. No category is promoted in Pass 111.

AutoPTU `main`: `f22cdbb831a2749c12c11a5122827c1e69a3c094`

The latest inspected Python commit adds Career frontend recovery from stalled battle loading. It explicitly treats a technical retry as a non-loss state. This is Career/UI work and does not change the tactical capability map.

## Java README evidence

The current Java README still says the following families are unfinished:

- expansion of core combatant/grid battle state;
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

## Why manufacturing does not create battle mechanics

Nothing inspected in Java proves:

- conveyor-belt movement;
- industrial forced movement;
- machine collision damage;
- furnace/heat zones;
- steam hazards;
- chemical/gas exposure;
- electrical floor hazards;
- moving production-line objectives;
- workers/civilians as tactical escort actors;
- cargo escort/interception objectives;
- process-machine HP;
- manufacturing-quality effects on battle items;
- factory-aware tactical AI;
- Minecraft projection of production lots or WIP into battle state.

A factory location must therefore remain presentation/world state unless a concrete PTU mechanic is verified and supported by the relevant capability family.

## Trainer Feature evidence boundary

Java now has substantial generic Trainer Feature execution infrastructure, including tested generic heal and Combat Stage effects. Trainer Features/perks remains PARTIAL because:

- concrete Feature catalog coverage is incomplete;
- many effect families are unported;
- interrupts/reactions remain incomplete;
- environment/movement effects depend on incomplete families;
- Minecraft playback is absent.

A manufacturing role such as machinist, engineer, operator, inspector or crafter does not grant a Trainer Feature. A job title also does not prove Technology Education or another Skill Rank.

## Pass 111 encounter dependency map

### Assembly Line Emergency Stop — FULL

Narrative objective:
Stop an operational incident safely while workers withdraw, technicians reach a control point and unexpected Pokémon behavior is resolved without making the factory itself an arbitrary combat trap.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for moving workers, moving carriers, protected corridors, displacement or conveyor-style movement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if heat, steam, machinery, conveyors, exclusion areas or similar factory state receives tactical mechanics
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `EVACUATE`, `REACH_SHUTOFF`, `PROTECT_TECHNICIAN`, `WITHDRAW`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Stop machinery and evacuate staff in authoritative world state before combat. Freeze one safe static factory-floor arena. Use AutoPTU only for remaining combatants. Resume diagnosis, WIP and quality disposition afterward.

### Quality Hold Warehouse Transfer — FULL

Narrative objective:
Protect or isolate a held lot during a separate confrontation without making the battle outcome decide whether the output is acceptable for use.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED for ordinary battle geometry
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING for moving cargo, escort or interception
- core calculations/action economy: VERIFIED
- lifecycle/damage/status/move/ability/item/Feature families: current PARTIAL scope when invoked
- terrain/weather/hazards/zones/reactions: BLOCKING only if warehouse conditions become tactical mechanics
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `PROTECT_CARGO`, `INTERCEPT`, `CLEAR_ROUTE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Secure the lot outside the battle grid under explicit hold/custody state. Run a static chokepoint battle. Resume transfer after combat. Release/rework/rejection remains controlled by production evidence, never victory.

### Rework Cell Disturbance — FULL

Narrative objective:
Protect workers and preserve the exact identity/genealogy of WIP while a rework operation is interrupted.

Dependencies:

- targeting/base movement/core/action economy: current VERIFIED scope
- complete movement: BLOCKING for worker/WIP movement and interception
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where invoked
- terrain/weather/hazards/zones/reactions: BLOCKING if active machinery or process zones gain mechanics
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_WORKER`, `REACH_EXIT`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Pause the rework operation in world state. Move workers and WIP to a safe authoritative state. Use one static battle if conflict remains. Resume the same rework record afterward.

## New overworld blockers introduced by Pass 111

These belong outside AutoPTU-Java:

- `MANUFACTURING_SITE_STATE`
- `PROCESS_DEFINITION_VERSIONING`
- `PRODUCTION_RUN_STATE`
- `PROCESS_STEP_EXECUTION_HISTORY`
- `WORK_IN_PROGRESS_LOT_IDENTITY`
- `LOT_GENEALOGY_GRAPH`
- `IN_PROCESS_OBSERVATION_PROVENANCE`
- `DEVIATION_RECORD_STATE`
- `NONCONFORMANCE_CLAIM_STATE`
- `QUALITY_DISPOSITION_STATE`
- `RELEASE_EVENT_STATE`
- `REWORK_GENEALOGY`
- `SCRAP_HANDOFF`
- `RECALL_SCOPE_AND_HISTORY`
- `PRODUCTION_CHANGE_HISTORY`
- `MANUFACTURING_TO_MATERIAL_CULTURE_HANDOFF`
- `MANUFACTURING_TO_TECHNOLOGY_HANDOFF`
- `MANUFACTURING_TO_WORKPLACES_HANDOFF`
- `MANUFACTURING_TO_SUPPLY_CHAIN_HANDOFF`
- `MANUFACTURING_TO_WASTE_HANDOFF`
- `MANUFACTURING_TO_MINECRAFT_PROJECTION`
- `MANUFACTURING_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 111

Do not infer:

- factory -> hazardous terrain;
- conveyor -> forced movement;
- furnace -> Fire damage;
- steam -> Burned;
- tank/chemical process -> Poisoned;
- loud machinery -> Sonic effect;
- machine fault -> defective output;
- deviation -> defect;
- defect -> sabotage;
- hold -> failed lot;
- rework -> counterfeit item;
- recall -> crime;
- scrap -> provenance deletion;
- automated line -> perfect output;
- factory-made item -> stronger/weaker mechanical item;
- factory-made Poké Ball -> changed capture modifier;
- machine uptime -> quality release;
- successful battle -> safe restart;
- successful battle -> root cause established;
- successful battle -> lot released;
- job title -> PTU Skill/Feature;
- Pokémon helping at a site -> ownership, unlimited labor, consent to every task or a production bonus.

## PTU/Caelo validation state

No reliable primary Caelo file or project-local PTU source for industrial manufacturing/crafting rules was recovered during this run.

Therefore unresolved mechanical questions remain blocked:

- Technology Education checks;
- crafting/manufacturing prerequisites;
- process duration;
- tool/equipment requirements;
- yields;
- repairs;
- quality tiers;
- durability;
- production-related Trainer Features;
- industrial environmental hazards;
- carrying/handling of production lots.

The previous project rule remains: do not invent the output of unavailable source material or Super PTU Online Helper.

## Mechanical/canon questions still unresolved

- Which products are actually mass-produced in Ouros?
- Which regions retain artisan production for important goods?
- Which manufacturing institutions/factories exist before campaign start?
- How much lot genealogy should ordinary goods retain?
- Who has authored authority to release or hold institutional production lots?
- What information about recalls is public?
- Can player clubs/businesses operate production lines?
- Which Pokémon have authored production roles and what is their agency relationship?
- How should Minecraft show WIP and storage without duplicating or creating authoritative inventory?
- What exact PTU/Caelo rules govern Technology Education, crafting, repair, extended actions, tools and relevant Trainer Features?
- Which production changes can affect mechanical item identity versus narrative provenance only?

Until these are resolved, manufacturing remains a world-state layer feeding only validated mechanical item references into PTU/AutoPTU.