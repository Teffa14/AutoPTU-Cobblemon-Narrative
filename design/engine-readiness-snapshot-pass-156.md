# Engine Readiness Snapshot — Pass 156

Status: READ-ONLY EVIDENCE SNAPSHOT for narrative dependency planning.
Date: 2026-08-24

## Live heads inspected

- AutoPTU-Java main: `5f0df19c14e1e2a9b2bfc64522cf704b483e564e`
- AutoPTU Python main: `9e644edec3235586276fadae6a94a1250a783b05`

AutoPTU-Java advanced since Pass 155. The new Java head wires PRE-damage Move Specials into the live authoritative Move pipeline. The preceding slices froze Move-special registry ordering and added a runtime bridge that passes a mutable result through the registry while keeping hit/crit/damage/type-multiplier mutation inside battle authority.

This is meaningful evidence for move-specific execution ordering and a portion of reaction/hook plumbing.

It is not evidence that every Move Special, reaction, forced-movement instruction, status, hazard, environmental effect or interrupt is implemented.

AutoPTU Python's current head remains a Career persistence/resilience change that repairs malformed active-roster state. It does not alter the tactical capability classification.

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

The live PRE-damage Move-special integration does not promote reactions or complete movement. Individual Perception, Telepathy, Parry, Sway, Shell Shield, status-prevention and forced-movement-instruction contracts remain representative slices.

## Pass 156 encounter dependency matrix

### Working Face Evacuation — FULL

VERIFIED dependencies already available:
- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

BLOCKING dependencies:
- complete movement if workers or Pokémon must cross threatened space, withdraw, intercept or be displaced dynamically;
- terrain/weather/hazards/zones/reactions if unstable ground, falling material, dust, water, dynamic machinery or protected work areas change tactical state;
- AI tactical policy for `EVACUATE`, `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_WORKER`;
- Minecraft/Cobblemon/Craftics adapter/playback for workers, equipment, objectives and scene-state handoff.

Potential PARTIAL dependencies only if explicitly used:
- items;
- abilities;
- Trainer Features/perks;
- move-specific behavior;
- status lifecycle.

REDUCED version evacuates workers and shuts down machinery before battle, then uses a stable static arena.

### Fossil Find Perimeter — FULL

VERIFIED:
- targeting;
- base movement legality;
- core calculations;
- action economy;
- legal-action enumeration.

BLOCKING:
- complete movement for withdrawal/perimeter crossing;
- AI tactical policy for `WITHDRAW`, `PROTECT_ROUTE`, `AVOID_FIND`;
- adapter/playback.

Environmental family is required only if rock instability, dust, machinery or protected zones gain real tactical effects.

REDUCED version stabilizes/removes the fossil from tactical state and moves workers out before combat. Battle result never establishes fossil custody.

### Reclamation Survey After Storm — FULL

BLOCKING:
- complete movement;
- terrain/weather/hazards/zones/reactions if erosion, water, debris or unstable slopes are mechanically active;
- AI tactical policy for `WITHDRAW`, `PROTECT_TECHNICIAN`, `REACH_EXIT`;
- adapter/playback.

REDUCED version resolves storm/slope state first and uses static adjacent geometry.

### Care-and-Maintenance Access Review

No battle-engine dependency is required. Mining, Subterranean Systems, Credentials, Worker Associations, Groundwater and other relevant authorities can return an access decision without combat.

## Mining-specific engine non-inferences

Current evidence does not authorize:

- mine-cart collision damage;
- conveyor forced movement;
- generic Push/Pull execution from industrial machinery;
- falling-rock or cave-in damage;
- crushing gates or moving walls;
- dust Accuracy penalties;
- gas/suffocation;
- automatic Poisoned;
- darkness penalties beyond exact validated PTU rules;
- water inflow as current/forced movement;
- mud as Rough Terrain/Tripped/Slowed;
- blasting mechanics;
- resource extraction from attacks;
- Groundshaper as mine-development authority;
- Rock/Ground/Steel Pokémon as mining-qualified;
- Rolycoly as a fuel-production mechanic;
- worker or wildlife objectives from legal-action enumeration alone;
- Minecraft block drops as production state;
- block placement as reclamation success.

## Why the new PRE-damage evidence does not change Mining FULL encounters

The Java head now runs registered PRE-damage Move Specials inside the authoritative move pipeline. Mining concepts such as cave-ins, blasting, machinery, retreat lanes, dynamic dust or water would require broader environment, movement and tactical-policy systems.

A narrative adapter must not imitate those missing families by creating custom Minecraft damage, movement or status rules.

## PTU / Caelo source boundary

The project continues to use PTU/Caelo material as mechanical authority when available. Full primary Caelo material was not reliably exposed during this run. Super PTU Online Helper was not exposed as an invocable capability.

No missing mining, blasting, excavation, darkness, gas, dust, carrying, tool, occupational or environmental mechanic has been invented.

## Narrative implementation consequence

Pass 156 can advance immediately through:

- exploration records;
- working-area state;
- extraction provenance;
- material handoffs;
- care-and-maintenance;
- closure planning;
- progressive rehabilitation;
- post-closure monitoring;
- worker/Pokémon role history;
- fossils/research handoffs;
- reduced static-battle encounter versions.

FULL mine encounters remain gated behind exact capability families rather than delegated to Minecraft.