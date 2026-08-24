# Engine Readiness Snapshot — Pass 155

Status: READ-ONLY EVIDENCE SNAPSHOT for narrative dependency planning.
Date: 2026-08-24

## Live heads inspected

- AutoPTU-Java main: `2207b04fdf0b9c13fbbb0f6357008db976bdf2f7`
- AutoPTU Python main: `9e644edec3235586276fadae6a94a1250a783b05`

AutoPTU-Java's current head adds a PRE-damage move-special runtime bridge. It passes a mutable move-special result through the generic registry and returns typed hit/crit/damage/type-multiplier values while keeping mutation authority inside the battle runtime. This is meaningful evidence for move-special execution ordering and a portion of reactions/hooks.

It is not evidence that every Move special, reaction, status, hazard or environmental mechanic is implemented.

AutoPTU Python's current head is a Career persistence/resilience change that repairs malformed active-roster state. It does not alter the tactical capability classification.

## Permanent capability classification

### VERIFIED

- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

### PARTIAL

- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks.

### BLOCKING as complete families

- complete movement including push / pull / knockback / interception / forced movement;
- terrain / weather / hazards / zones / reactions;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter and playback.

The PRE-damage bridge does not promote the reactions family. Previously ported individual reactions, follow-up seams, Sway/Perception/Shell Shield contracts and forced-movement instructions likewise remain representative slices rather than family completion.

## Pass 155 encounter dependency matrix

### Headgate Failure During Delivery Window — FULL

Uses VERIFIED targeting, base movement legality, core calculations, action economy and legal-action enumeration.

BLOCKING dependencies:
- complete movement if technicians or wildlife cross threatened space dynamically;
- terrain/weather/hazards/zones/reactions if water, mud or changing access modifies combat state;
- AI tactical policy for `PROTECT_TECHNICIAN`, `REACH_CONTROL`, `WITHDRAW`;
- Minecraft/Cobblemon/Craftics playback for authoritative handoff and scene representation.

REDUCED version avoids these dependencies by stopping water and relocating noncombatants in world state before battle.

### Canal Breach at Orchard Reach — FULL

BLOCKING:
- complete movement;
- environmental family for changing breach/water/debris effects;
- tactical AI;
- adapter/playback.

REDUCED version freezes the breach before combat and uses stable adjacent geometry.

### Wildlife at the Lateral During Drought Rotation — FULL

BLOCKING:
- complete movement for CROSS/WITHDRAW behavior;
- AI tactical policy for non-KO objectives;
- adapter/playback.

Environmental family is required only if water depth, mud or moving water becomes mechanically active.

REDUCED version resolves ecological movement outside the grid and opens a conventional static battle only if conflict remains.

### Delivery Record Reconciliation

No battle-engine dependency. This is a world-state investigation involving Irrigation, Metrology, Archives and hydrology authorities.

## Explicit non-inferences for irrigation

Current engine evidence does not authorize:
- canal current as forced movement;
- wet soil or mud as Rough Terrain, Slowed or Tripped;
- floodwater as damage or drowning;
- irrigation gates as moving tactical walls;
- Water-type Moves as measured agricultural flow;
- Rain Dance as water-supply state;
- Water Absorb / Storm Drain as irrigation infrastructure;
- Water-type species as worker qualification;
- a PRE-damage move-special bridge as generic environment/reaction support.

## PTU / Caelo source boundary

The project continues to use PTU/Caelo source material as mechanical authority when available. Full primary Caelo material was not reliably exposed during this run, and Super PTU Online Helper was not exposed as an invocable capability. No missing irrigation, current, mud, Water Move, Survival or occupational rule has been invented to compensate.

## Narrative implementation consequence

Pass 155 can advance now using persistent world-state irrigation operations and REDUCED battle handoffs. FULL canal/headgate encounters remain gated behind exact engine families rather than delegated to the Minecraft adapter.
