# Engine Readiness Snapshot — Pass 29

Status: read-only evidence snapshot for narrative encounter design.

## Repositories inspected

- `Teffa14/AutoPTU-Java`: read-only
- `Teffa14/AutoPTU`: read-only
- `Teffa14/AutoPTU-Cobblemon-Narrative`: writable destination

## Live Java head inspected

AutoPTU-Java head during this pass:

`957e7eaa0ce056b8fc6f2f66aba7f24440c2c2be`

Commit: `Consume pending status skips after phase hooks (#55)`

New bounded evidence since Pass 28:
- lifecycle hooks can emit a structured pending status-skip request;
- ordered hook resolution aggregates that request alongside semantic events;
- the round controller consumes the request for its authoritative current actor;
- Java tests compare the status-skip ordering contract against Python.

This strengthens full-turn/lifecycle infrastructure and status/lifecycle integration.

It does not establish a complete status controller, every phase-triggered status, reactions, Trainer Features or full BattleSpec-to-transcript parity.

## Java README evidence

The current README still states that Python AutoPTU is authoritative while the port remains incomplete.

It lists these major families as unfinished:
- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Live Python head inspected

AutoPTU head observed during this pass:

`54e4fa8ccbe0e555afef8b4b3713e7568608e5d3`

The latest Python changes are Career/API portability work and do not materially change the tactical capability classification below.

Python remains the source oracle. Python behavior cannot be treated as already available in Java or Minecraft.

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

## Why status/lifecycle remain PARTIAL

Pass 29 adds real parity evidence around pending status skips emitted from lifecycle hooks. That is meaningful progress.

Invalid inferences remain:
- one pending-skip contract exists -> the complete status controller exists;
- status skip ordering exists -> every Sleep/Flinch/Paralysis-style rule is ported;
- lifecycle hooks exist -> all Ability/Feature interrupts exist;
- ordered hooks exist -> reactions exist;
- event aggregation exists -> full semantic transcript parity exists.

The category upgrades only when representative coverage plus boundary contracts demonstrate the full family.

## Pass-29 relevance

Technology/infrastructure world state can progress mostly outside tactical battle.

Safe work now:
- technical assets and service dependencies;
- operational states;
- maintenance history;
- faults and diagnostic claims;
- operator schedules and institutions;
- fallback plans;
- puzzle state with explicit resets;
- infrastructure incident propagation;
- device provenance;
- Pokémon-machine observations stored as unresolved mechanical claims;
- Minecraft representation plans that do not claim adapter support.

Battle-facing limitations remain substantial for machinery that changes the grid.

## Encounter dependency table

### Substation Cascade

FULL version dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if machinery can displace or intercept
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING if technical interventions rely on them
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: power isolation happens before the tactical encounter. The arena is static and legal. Post-battle world state records whether access, inspection or repair became possible.

### Pump Hall Emergency

FULL version dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- terrain/weather/hazards/zones/reactions: BLOCKING for changing water/environment state
- complete movement: BLOCKING if water or machinery forces displacement
- lifecycle: PARTIAL for timed changes
- AI tactical policy: BLOCKING for objective-aware contesting
- adapter/playback: BLOCKING
- move/ability/item families remain PARTIAL when relied upon.

Reduced version: pump controls and water state remain overworld/world-state actions. AutoPTU resolves only a static encounter securing the route.

### Factory Safe Shutdown

FULL version dependencies:
- explicit tactical objective semantics for ordered machine controls: not yet evidenced
- terrain/weather/hazards/zones/reactions: BLOCKING if machine state creates hazards
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- complete movement: BLOCKING if machinery moves actors
- lifecycle: PARTIAL for timed/ordered effects
- Trainer Features/perks: BLOCKING if operators act through PTU Features.

Reduced version: the machine puzzle remains outside combat with reset/recovery state. Any battle is a separate static encounter.

## Technology Skill boundary

Python AutoPTU and supplied PTU data include Technology Education as an authoritative Skill concept. That does not prove Java currently exposes every Skill check, technical Feature or repair rule needed by the world layer.

Narrative content may store:
- that an actor works as a technician;
- that an institution considers them qualified;
- that a machine needs diagnosis;
- that a repair is planned.

It may not fabricate a Technology Education rank, DC, bonus or repair result.

## Pokémon-machine boundary

Official Pokémon sources provide narrative precedents for Rotom entering specific machines and for Electric-type Pokémon interacting with power infrastructure.

That does not prove any of these exist as current AutoPTU-Java mechanics:
- universal machine possession;
- electricity generation values;
- shock hazards;
- control-system access;
- machinery damage;
- field-object interaction;
- Rotom-specific device APIs.

Treat these as authored world-state interactions until exact PTU/Caelo mechanics and Java contracts exist.

## Minecraft infrastructure boundary

Verified battle movement and LoS do not prove:
- block-machine state synchronization;
- persistent power networks;
- pipes/cables simulation;
- interactable control panels;
- facility failover logic;
- chunk-safe machine timers;
- service-capacity UI;
- persistent Rotom/device associations;
- object HP or destructible machinery;
- automated NPC technician behavior.

These remain adapter/world-simulation work.

## No-inference rules for Pass 29

- A blackout does not create Electric damage.
- A broken machine does not create a Technology Education check until an authored mechanic calls for one.
- A Rotom near a device does not mean it controls the device.
- A power plant does not imply battlefield hazard zones.
- A factory conveyor does not imply forced movement.
- A security system does not imply overworld LoS/stealth AI.
- A maintenance worker title does not prove Trainer Features or Skill ranks.
- A backup generator does not have invented fuel duration or capacity math.
- A machine puzzle cannot be embedded into combat until interactable-object semantics exist.
- One new status/lifecycle hook does not upgrade the whole status family.

## Promotion guidance

Technology and infrastructure stories can safely ship as world-state systems plus REDUCED encounters first.

Promote a machinery-heavy encounter to FULL tactical form only after the exact capability families it requires have current Java parity evidence and the Minecraft/Cobblemon/Craftics adapter can preserve the same authoritative state without duplicating PTU rules.
