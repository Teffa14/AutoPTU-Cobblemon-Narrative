# Engine Readiness Snapshot — Pass 33

Status: read-only evidence snapshot for narrative encounter design.

## Repositories inspected

- `Teffa14/AutoPTU-Java`: read-only
- `Teffa14/AutoPTU`: read-only
- `Teffa14/AutoPTU-Cobblemon-Narrative`: writable destination

## Live Java head inspected

AutoPTU-Java head during this pass:

`48083562c03b50e2e6601b3c52101f7a91934cac`

Commit:
`Port Strange Tempo Confusion START phase branch`

Immediately preceding relevant commit:

`0d36b72ef366ae80af1fb1c65f5461273369b500`

`Port Flinch START phase effect through status registry (#58)`

Relevant new evidence since Pass 32:

- Flinch START-phase handling is ported through the reusable status-phase registry;
- the bounded Flinch phase behavior is compared against the Python oracle;
- Strange Tempo's Confusion START-phase branch is ported;
- the Strange Tempo branch checks Sleep/Asleep and `sleep_blocked` before control handling;
- canonical ability identity resolution is used for Strange Tempo;
- parity fixtures freeze the bounded Python behavior;
- the Strange Tempo branch emits a semantic ability event and intentionally does not create a pending turn skip.

This is real progress for status/ability interaction inside the lifecycle.

It does not establish complete Confusion, Flinch, status or Ability coverage.

## Current Java README evidence

The Java README still states that Python AutoPTU remains authoritative while the port is incomplete.

It still marks the following as unfinished:

- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The project remains a Java battle-core library rather than a Minecraft mod.

## Live Python head inspected

Latest AutoPTU head observed during this pass:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Commit:
`Career: make roster recovery deterministic`

Recent Python commits around this head concern Career flow and roster recovery.

They do not establish new Java tactical capability.

Python remains the rules oracle where explicitly pinned by migration tests. Python capability is not equivalent to Java/Minecraft readiness.

## Permanent capability classification

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items

### BLOCKING for mechanically rich encounter design

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- Trainer Features/perks
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Delta from Pass 32

Java advanced from `5576e433b7b2f9e87fad7c669bd008b992b9bb62` to `48083562c03b50e2e6601b3c52101f7a91934cac`.

Two bounded status/ability slices landed after the generic status-phase registry:
- Flinch START-phase handling;
- Strange Tempo interaction with Confusion at START.

This strengthens evidence inside:
- full turn/round lifecycle: still PARTIAL;
- status lifecycle: still PARTIAL;
- abilities: still PARTIAL;
- move-specific behavior: no broad promotion.

No permanent category is promoted to VERIFIED.

Python advanced through Career-oriented work. That does not change Java battle readiness.

## Pass-33 relevance

The geology/excavation layer is primarily persistent world and location state.

Safe implementation-independent work includes:
- geological-site records;
- strata/context provenance;
- excavation projects;
- resource-body state;
- fossil-context records;
- discovery/publication state;
- museum custody and provenance links;
- coarse depletion state;
- mine/worksite staffing links;
- subsurface connection graphs;
- public discovery booms;
- restoration/repurposing state.

Those can advance without battle-engine completion.

## Cave geometry boundary

Java verifies substantial grid targeting, footprints, LoS and base movement legality.

That does not prove:
- cave-in hazards;
- falling-rock reactions;
- unstable ledges;
- current-driven movement;
- mine-cart forced movement;
- gas zones;
- suffocation;
- drowning;
- changing support structures;
- destructible walls;
- dynamic excavation inside battle.

Those require other capability families.

## Environmental hazard boundary

The following narrative descriptions remain world-state descriptions until mechanically validated:
- unstable gallery;
- flooded tunnel;
- poor air;
- geothermal heat;
- loose debris;
- collapsing support;
- sharp drop;
- unstable fossil bed;
- moving machinery.

Minecraft must not implement their PTU consequences independently while `terrain/weather/hazards/zones/reactions` is BLOCKING.

## Fossil boundary

Engine status does not establish:
- fossil discovery checks;
- fossil extraction checks;
- revival eligibility;
- revival species resolution;
- revived Pokémon stats/moves/abilities;
- ownership/custody;
- preparation time;
- revival equipment behavior.

Those belong to PTU/Caelo rules plus world/application systems.

## Encounter dependency table

### Collapsed Survey Gallery

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING when rescue/repositioning matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- RESCUE/REACH_SAFE_ZONE objective semantics: not verified

REDUCED version:

Resolve collapse/stability in overworld state. Battle occurs in a fixed stable chamber with normal legal combatants. Rescue targets remain out of tactical state. Route access changes after authoritative resolution plus a separate world-state decision.

### Fossil Bed Disturbance

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception: BLOCKING only when protection/escort is tactical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for fragile-context zones
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- PROTECT_CONTEXT/WITHDRAW objective semantics: not verified

REDUCED version:

The fossil bed stays outside the battle grid and cannot be damaged by tactical simulation. Any encounter occurs in an adjacent ordinary arena. Scientific documentation and recovery choices remain overworld state.

### Flooded Lower Working

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED for supported tactical modes only
- complete movement/forced movement/interception: BLOCKING when currents/rescue matter
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for rising water/current/pump zones
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- ACTIVATE_OBJECT/ESCAPE objective semantics: not verified

REDUCED version:

Water level and pump state remain outside battle. Use a dry static arena if combat occurs. After resolution, maintenance state decides whether the route reopens, remains closed or escalates into a crisis.

## Status/ability no-inference rule

The new Flinch and Strange Tempo slices demonstrate specific behavior only.

They do not prove:
- complete Confusion lifecycle;
- complete Flinch interactions;
- every Ability that modifies a status;
- every START-phase status;
- environment-applied statuses;
- hazard-triggered status application;
- cave gas or water conditions;
- status-aware tactical AI.

## AI boundary

AI legal-action infrastructure is VERIFIED.

AI tactical policy remains BLOCKING.

Therefore a wild Pokémon can eventually receive legal available actions from the core, but current evidence does not prove that it will strategically:
- protect a nest/fossil context;
- escape a collapsing gallery;
- avoid unstable ground;
- intercept a survey crew;
- prioritize an exit;
- activate machinery;
- retreat from rising water.

Reduced encounters must not depend on those behaviors.

## Adapter boundary

Minecraft/Cobblemon/Craftics adapter/playback remains BLOCKING.

Current Java evidence does not establish:
- persistent cave geometry synchronization;
- fossil nodes;
- excavation-state playback;
- mine-cart interaction;
- water-level synchronization;
- structural supports;
- protected-context blocks;
- mining-permission checks;
- revived-fossil entity provenance;
- underground NPC work schedules.

These remain future application-layer contracts.

## No-inference rules for Pass 33

- Java base terrain costs do not make terrain/hazards VERIFIED.
- Status registry progress does not create environmental status mechanics.
- Strange Tempo does not prove the Ability registry is complete.
- Flinch does not prove the status controller is complete.
- A Minecraft cave does not automatically map to a PTU hazard.
- Breaking a Minecraft block does not automatically equal a legal excavation action.
- A Rock/Ground Pokémon is not automatically a mining tool.
- A fossil item does not automatically become a revived Pokémon.
- Python Career updates do not prove Java fossil/crafting systems.
