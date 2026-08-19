# Engine readiness snapshot — pass 27

Status: read-only evidence snapshot for narrative encounter design.

## Repositories inspected

- AutoPTU-Java: read-only
- AutoPTU Python: read-only
- AutoPTU-Cobblemon-Narrative: writable destination only

## Live Java head inspected

AutoPTU-Java head at the time of this pass:

`d8809213d819eea7c9f142fe4b930c35f0614e05`

Commit: `Port authoritative phase transitions through lifecycle hooks (#54)`

This adds semantic phase-change events, authoritative START/COMMAND/ACTION/END phase advancement, phase exposure to lifecycle hooks and Python-oracle parity tests.

This is strong evidence that lifecycle infrastructure is becoming more authoritative. It does not prove every turn/round rule family, every phase-triggered Move/Ability/Feature, reactions, hazards or Trainer Features.

## Python evidence inspected

AutoPTU Python remains the rule oracle for the incomplete Java port. The latest repository activity inspected in this pass was centered on Career/browser-state work rather than changing the battle capability classification used here.

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

### BLOCKING for rich encounter design

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- Trainer Features/perks
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Why lifecycle remains PARTIAL

The current Java head now owns actor/phase state and phase transitions through lifecycle hooks, and recent commits also added turn-end boundaries, round damage/injury history rotation, delayed-hit scheduling/binding and temporary-effect state.

Those are meaningful bounded slices. They do not establish that all Python lifecycle semantics have been ported. In particular, a lifecycle hook seam is infrastructure; it does not imply all rule families that eventually use that seam exist.

## Pass-27 relevance

The language/translation layer is mostly world-state and can progress independently of battle-engine completion.

### Safe now

- store inscriptions and copies
- store transcriptions
- store competing decipherment models
- store translations and confidence/provenance
- update actor knowledge
- unlock overworld dialogue or research state
- change non-combat door/quest state when the Minecraft adapter eventually supports it

### Requires explicit implementation contracts

If decipherment becomes a timed combat objective, escort, race, protect-zone, interactable console or changing-hazard encounter, the concept must declare exact dependencies.

Typical blocking families are:

- AI tactical policy for objective-aware enemies
- complete movement/interception for pursuit or physical blocking
- terrain/weather/hazards/zones/reactions for changing chambers
- Minecraft/Cobblemon/Craftics playback for physical puzzle state and battlefield synchronization

Trainer Features/perks remain blocking if a puzzle or translation concept relies on a mechanical Trainer Feature rather than narrative/world-state reasoning.

## No-inference rules

- Authoritative phase transitions do not mean reactions are complete.
- Delayed-hit queue support does not mean all delayed Moves are complete.
- One Ability or item hook does not prove the full Ability/item registry.
- Battle LoS does not prove overworld vision or puzzle perception.
- Java having semantic TrainerFeatureEvent support does not prove Trainer Feature rules are implemented.
- A narrative console interaction does not become a legal PTU combat action unless the engine defines it.

## Recommended reduced-version policy

For Pass-27 encounters, keep decipherment and puzzle manipulation outside tactical combat by default. Use AutoPTU only for legal standard battles that occur around the narrative problem. Promote interactions onto the grid only when the exact objective, movement, reaction and adapter contracts are verified.