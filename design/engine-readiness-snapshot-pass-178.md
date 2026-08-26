# Engine Readiness Snapshot — Pass 178

Status: evidence snapshot for narrative dependency classification.
Date: 2026-08-26
Pass: 178

This file does not modify AutoPTU-Java or AutoPTU. Both repositories were inspected read-only.

## Live evidence inspected

AutoPTU-Java head inspected: `a9fb0d81238e69a5263f074b4a8ad8ef1905325d`

Recent Java evidence includes:
- canonical storage of all seven Combat Stages;
- authoritative mutation/hooks for Accuracy and Evasion as well as the other Combat Stages;
- secondary Combat Stage application through the mutation service;
- Mirror Armor coverage across the seven-stage identity;
- earlier live generic secondary-Status execution and AoE secondary-Status handling.

This is useful evidence for specific stage/status/move plumbing. It is not evidence that the entire Ability, Status or Move catalog is implemented.

AutoPTU Python head inspected: `44305a1b3f06a45fbd06392a64573f287ac31555`

Its newest inspected change is Career sponsor-memory normalization and explicitly preserves authoritative battle behavior. It does not change battle-readiness classification.

## Java README boundary

The current Java README still marks the following large areas incomplete:
- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- move/ability/item/perk/Trainer Feature registries;
- full BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Therefore representative implemented contracts must not promote entire capability families.

## Permanent capability map

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
- Trainer Features/perks

### BLOCKING

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions as a complete family
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted in Pass 178.

## Why recent Combat Stage progress does not change the map

Seven Combat Stages now have stronger authoritative state and hook coverage. That proves a narrower contract:

`stage identity -> authoritative mutation path -> supported prevention/reflection hooks`

It does not prove:
- all stage-changing Moves;
- all Ability interactions;
- all Trainer Features;
- every secondary effect;
- all reaction timing;
- full transcript parity.

The category-level classifications therefore remain conservative.

## Pass 178 encounter dependency matrix

### Burn Perimeter Access Interruption — FULL

Required families:
- targeting/footprints/range/LoS: VERIFIED for battle targeting only;
- base movement legality: VERIFIED;
- complete movement: BLOCKING for dynamic `WITHDRAW`, `CROSS`, interception and changing routes;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL if an exact PTU condition is invoked;
- terrain/weather/hazards/zones/reactions: BLOCKING if active heat, smoke, fire, unstable burned ground or protected zones affect tactics;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version readiness:
- resolve fire perimeter, civilians, researchers and background wildlife in world state;
- choose stable static battle geometry;
- use only ordinary combatants and validated mechanics;
- no environmental fire/smoke rule is synthesized.

### Prescribed Burn Monitoring Day — FULL

Same permanent map as above.

Additional constraints:
- a treatment mosaic cannot be converted into terrain categories without exact validated rules;
- prescribed-burn success remains outside battle authority;
- no combat result may write ecological objective completion.

REDUCED version readiness:
- world state owns treatment/monitoring;
- optional battle occurs in a safe static clearing.

### Post-Fire Watershed Survey — FULL

Required families:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement: BLOCKING if crossing/withdrawal/interception matters;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- lifecycle/damage/status/move/ability/item/Trainer Feature families: PARTIAL when used;
- terrain/weather/hazards/zones/reactions: BLOCKING if runoff, mud, debris, unstable banks or water movement affect tactics;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for `PROTECT_RESEARCHER`, `WITHDRAW`, `CLEAR_ROUTE`, `REACH_EXIT`;
- adapter/playback: BLOCKING.

REDUCED version readiness:
- Fire Ecology, Soil and Freshwater determine survey state outside battle;
- hazardous drainage is excluded from the battle map;
- an independent fight may use adjacent stable ground.

### Fire-Regime Review

No battle-engine dependency is required.

Archives, Public Memory, Remote Sensing, Fire Ecology, Flora and Conservation can produce a revised or unresolved interpretation without combat.

## Environmental fire boundary

Pass 178 specifically does not treat any of these as available merely because the scene contains fire:

- spreading fire tiles;
- smoke visibility penalties;
- ambient Burned;
- heat damage;
- delayed ignition;
- wind-driven fire phases;
- ash zones;
- falling burned trees;
- collapse;
- fireline knockback;
- wildfire pathfinding;
- responder AI;
- civilian evacuation AI.

If a future Java contract validates one representative mechanic, only that mechanic should be promoted locally. The complete environmental family remains BLOCKING until its required contracts exist.

## PTU/Caelo guardrails

No validated evidence in this run establishes:
- a generic wildfire environmental rule;
- Fire-type ecological immunity;
- Water Move firefighting output;
- Rain Dance suppression volume;
- smoke as a PTU Status;
- charred ground as PTU Terrain;
- Flash Fire or Heatproof as environmental protection outside their exact mechanical contracts.

The full Caelo primary corpus was not reliably available in this runtime. Super PTU Online Helper was not exposed as an invocable capability. No output from either source is invented.

## Minecraft adapter boundary

Minecraft may eventually render:
- fire scar geometry;
- charred/cleared visual variants;
- closures and signs;
- monitoring plots;
- regrowth stages;
- safe/unsafe access presentation from world state.

It must not derive authoritative state from:
- vanilla fire spread;
- block count burned;
- chunk load/unload;
- particle density;
- entity despawn;
- Fire-type spawns;
- rain visuals;
- biome color;
- player-built firelines.

The authoritative direction remains:

`Ouros world state -> adapter presentation -> player-visible world`

not

`Minecraft fire simulation -> Ouros ecological truth`.
