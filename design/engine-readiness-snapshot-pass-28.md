# Engine readiness snapshot — pass 28

Status: read-only evidence snapshot for narrative encounter design.

## Repositories inspected

- `Teffa14/AutoPTU-Java`: read-only
- `Teffa14/AutoPTU`: read-only
- `Teffa14/AutoPTU-Cobblemon-Narrative`: writable destination only

## Live Java head inspected

AutoPTU-Java head at the time of this pass:

`d8809213d819eea7c9f142fe4b930c35f0614e05`

Commit: `Port authoritative phase transitions through lifecycle hooks (#54)`

Recent bounded Java evidence includes:

- server-owned active actor and phase state;
- authoritative START / COMMAND / ACTION / END phase transitions;
- semantic phase-change events;
- turn-end lifecycle cleanup;
- round damage-history rotation;
- round Injury-history rotation;
- delayed-hit scheduling and canonical move/target binding;
- move-damage history writeback;
- Python-oracle parity fixtures for those bounded slices.

This is substantial lifecycle progress. It still does not prove every turn/round trigger, reaction, delayed Move, status interaction, Ability hook, Trainer Feature interrupt or battlefield subsystem.

## Java README evidence

The current AutoPTU-Java README continues to list these major families as unfinished:

- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- semantic full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Python AutoPTU remains the authority while the Java port is incomplete.

## Live Python head inspected

Latest AutoPTU head observed during this pass:

`54e4fa8ccbe0e555afef8b4b3713e7568608e5d3`

Recent Python commits are primarily Career/browser-state and captured-identity persistence work rather than evidence that changes the tactical capability map below.

The Python repository remains the oracle source. Its existence does not mean Java or the Minecraft adapter can execute every Python behavior today.

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

## Why lifecycle remains PARTIAL

The Java engine now owns more authoritative temporal state than in earlier passes. That materially improves the port, especially for future phase-triggered effects and delayed operations.

However, infrastructure and representative fixtures do not equal category completion.

Examples of invalid inference:

- phase transitions exist -> all phase-triggered Moves/Abilities/Features exist;
- delayed-hit scheduling exists -> every delayed Move executes correctly;
- damage history rotates -> the full damage pipeline exists;
- Injury history rotates -> every Injury rule exists;
- one Ability or item hook exists -> the full registry exists;
- semantic lifecycle events exist -> reactions are complete.

## Pass-28 relevance

Most conservation/stewardship state can progress independently of battle completion.

### Safe narrative/world-state work now

- persistent protected/managed area records;
- habitat objectives and management plans;
- access-policy state;
- stewardship actor roles;
- monitoring programs;
- restoration project state;
- corridor state;
- public visitor information;
- coexistence incidents;
- release/relocation proposals as unresolved world state;
- aggregate ecological observations;
- management reviews;
- Minecraft representation plans that do not claim implemented adapter support.

### Battle-facing concepts that remain limited

Corridor escorts, moving wildlife, evacuation, protect-zone goals, interactable restoration equipment, dynamic habitat hazards, objective-aware enemies and interception all require capability families beyond the currently verified core.

## Pass-28 encounter dependency table

### Corridor Crossing

Required for FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING when dynamic environmental lanes are used
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING if relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: migration movement remains in overworld/world-state; AutoPTU only resolves a static legal encounter.

### Restoration Site Disturbance

Required for FULL version:

- terrain/weather/hazards/zones/reactions: BLOCKING
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- complete movement/forced movement: BLOCKING if battlefield equipment moves actors
- lifecycle/damage/status/Move/Ability/Item categories remain PARTIAL where used.

Reduced version: equipment stabilization and restoration progress stay outside the tactical grid.

### Survey Team Withdrawal

Required for FULL version:

- complete movement/interception/forced movement: BLOCKING
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- terrain/weather/hazards/zones/reactions: BLOCKING if environmental danger drives the withdrawal
- full lifecycle: PARTIAL

Reduced version: survey staff remain outside the grid while the players resolve a conventional static battle that opens or secures the route.

## Capture/release boundary

The conservation layer must not create a parallel capture system.

The supplied Caelo material already defines Wild Pokémon encounters as mechanically meaningful battles and has explicit Poké Ball/capture resolution. Narrative policy may explain why an institution requests restraint, supervision or monitoring, but capture rolls, hit checks, Ball behavior and any actual ownership transition must remain in the authoritative mechanics.

The current Java README does not establish a complete capture/release/ownership pipeline for the Minecraft runtime. Treat those as implementation questions rather than narrative shortcuts.

## Overworld ecology boundary

Java battle LoS, movement legality and actor footprints do not prove:

- Cobblemon spawn-control hooks;
- stable wild-Pokémon identity through despawn/reload;
- migration AI;
- protected-zone access enforcement;
- visitor-policy UI;
- habitat restoration visualization;
- ownership transfer after release;
- objective-aware NPC or wild-Pokémon pathing.

Those remain adapter/world-simulation work.

## No-inference rules for Pass 28

- A protected-area designation does not create a capture modifier.
- A visitor closure does not despawn wild Pokémon.
- A successful restoration project does not automatically increase rare spawns.
- A newly observed species is not automatically invasive.
- A rehabilitated Pokémon is not automatically owned by its caregiver.
- A persistent wild collective does not automatically receive Pack Mon mechanics.
- A conservation encounter does not gain escort/protect/withdraw objectives until the engine defines those objectives.
- A Ranger-like narrative role does not imply PTU Trainer Features exist in Java.

## Promotion guidance

Worldbuilding can safely continue using the REDUCED encounter versions in Pass 28.

Promote a conservation concept to its FULL tactical version only when the exact dependencies are evidenced by tests/contracts at the current Java revision and, where necessary, by a functioning Minecraft/Cobblemon/Craftics adapter.