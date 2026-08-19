# Engine Readiness Snapshot — Pass 19

Status: implementation evidence snapshot. Not canon. This file supersedes Pass 18 for current narrative dependency classification.

Snapshot basis: `Teffa14/AutoPTU-Java` main through commit `6c357d59061be2eae7bbbb85f401750acd7cf686` (`Add payload-bearing temporary effect state (#46)`). Python AutoPTU remains the project-designated behavior oracle while Java parity is incomplete.

## Permanent capability categories

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: BLOCKING
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: BLOCKING
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

## Evidence added since Pass 18

Java now stores payload-bearing temporary-effect entries in authoritative battle state, exports parity fixtures from the Python oracle, tests those payloads cross-language, and exercises payload cleanup through round lifecycle parity.

This is useful lifecycle infrastructure because temporary effects can now carry structured payload data rather than only simple presence/absence state.

It does not upgrade `full turn/round lifecycle` to VERIFIED.

Still unproven as complete families include:

- broad delayed-effect ordering;
- complete status duration and cure lifecycle;
- battlefield weather/terrain/hazard lifecycle;
- complete reaction/interrupt ordering;
- comprehensive Ability, Item, Move and Trainer Feature trigger coverage;
- complete semantic battle transcript parity.

## Representative hook evidence remains partial

Current live Java also contains:

- authoritative ordered damage-hook infrastructure;
- a parity-backed Burn damage modifier path;
- a parity-backed Pink Pearl held-item damage hook;
- a parity-backed Mega Launcher pre-damage Ability hook;
- an authoritative lifecycle hook registry;
- round lifecycle ownership;
- authoritative move-frequency usage state;
- canonical combatant movesets/geometry/affiliation used by legal-action generation.

These are representative slices.

Therefore:

- `abilities` remains PARTIAL;
- `items` remains PARTIAL;
- `move-specific behavior` remains PARTIAL;
- `full stateful damage pipeline` remains PARTIAL;
- `full turn/round lifecycle` remains PARTIAL.

No individual slice upgrades a permanent family.

## Communications-pass interpretation

The new media/communications layer is primarily world-state infrastructure and does not require battle-core support for routine messages, news, bulletins, reports, corrections, channel coverage or delivery records.

Mechanically rich communications encounters require stricter classification.

### Relay Tower Defense — FULL

Required families:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if displacement around repair zones matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL if repair phases are timed inside combat
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL if status conditions alter objective participation
- terrain/weather/hazards/zones/reactions: BLOCKING if electrical zones, exposed equipment or reactions matter
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for objective-aware pressure on technicians/relay zones
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

REDUCED form can run as a standard static encounter followed by an overworld repair state change.

### Courier Breakthrough — FULL

Narrative escort/interception requires:

- complete movement including interception/forced movement: BLOCKING
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

A reduced form can keep the courier outside combat and use a standard chokepoint encounter.

### Broadcast Studio Evacuation — FULL

If hazards move or evacuation must occur during initiative, dependencies include:

- full turn/round lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

A reduced form resolves evacuation in overworld state and isolates one static tactical battle.

## Evidence discipline

Do not infer engine support from narrative feasibility.

- A server can store a communications outage without tactical signal-jamming rules.
- A Minecraft relay structure can exist visually without battle hazards.
- A timed narrative deadline does not prove combat lifecycle support for timed objectives.
- A legal action list does not prove enemies understand escort, defend, hold-zone or sabotage objectives.
- Payload-bearing temporary effects do not prove every delayed Move, Ability, status or Trainer Feature interaction.
- Headless Java battle events do not prove Cobblemon playback.

Future narrative passes should use this snapshot until newer live evidence supersedes it.
