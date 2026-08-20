# Engine Readiness Snapshot — Pass 54

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

`Teffa14/AutoPTU-Java` was inspected read-only at:

`98b5aca32262f902f2260ab73b6d22a8b6e468d5`

`Teffa14/AutoPTU` was inspected read-only at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The narrative repository remains the only writable destination.

## Java change since Pass 53

Pass 53 inspected Java at:

`dc8cc6677dcfcf830fb176458b05ad08dba9b526`

The new live head is:

`98b5aca32262f902f2260ab73b6d22a8b6e468d5`

Newest change:

`Make post-damage hooks RNG-ready with Python parity`

Observed implementation evidence:

- authoritative `PythonRandom` can be bound to post-damage hook context;
- RNG-consuming post-damage behavior is resolved inside the core rather than supplied by Minecraft/client code;
- a declarative random-d10 post-damage Ability family was added;
- selected behavior is frozen against Python oracle fixtures;
- Aura Break [Errata] adjustment remains integrated with that authoritative post-damage state.

This strengthens:

- selected Ability implementation evidence;
- selected full-state damage-hook evidence;
- authoritative RNG ownership.

It does not prove:

- full Ability coverage;
- full damage parity;
- complete status lifecycle;
- rewind support;
- RNG snapshot/restore;
- deterministic replay of a prior turn;
- temporal loops;
- Future Sight/Doom Desire family completeness;
- time-travel mechanics;
- timeline branching;
- Minecraft playback.

The Java README still states that Python is authoritative while the port is incomplete. It still lists core battle state, full damage, status controller, terrain, hazards, forced movement, reactions, complete hook registries, semantic transcript parity, tactical AI and Minecraft/Cobblemon adapter work as unfinished.

## Python state

Live Python head remains:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The newest observed commit is Career roster determinism work. No authoritative whole-world temporal branch/rewind contract was identified in this pass.

Python remains the rules oracle for ported battle behavior. It is not evidence that Ouros world-state time travel exists.

## Permanent capability map

### VERIFIED

Targeting / footprints / range / LoS.

Base movement legality.

Core calculations.

Action economy / initiative.

AI legal-action infrastructure.

### PARTIAL

Full turn / round lifecycle.

Full stateful damage pipeline.

Status lifecycle.

Move-specific behavior.

Abilities.

Items.

Trainer Features / perks.

The new RNG-ready post-damage Ability slice strengthens `full stateful damage pipeline` and `abilities`, but neither category is promoted.

### BLOCKING

Complete movement including push / pull / knockback / interception / forced movement.

Terrain / weather / hazards / zones / broad reactions.

AI tactical policy.

Minecraft / Cobblemon / Craftics adapter and playback.

## Temporal-specific blockers outside the permanent categories

Time-travel concepts add several contracts not represented by the permanent battle-family taxonomy.

### World-state temporal context contract — BLOCKING

No verified project contract currently provides:

- PRIMARY/historical/possible-future/branch context identity;
- causal divergence handling;
- immutable historical state versions;
- branch creation/selection;
- cross-context knowledge scoping.

### Battle rewind/checkpoint contract — BLOCKING

No verified Java contract currently proves:

- snapshotting a complete battle at an arbitrary checkpoint;
- restoring HP/Injuries/statuses/stages/temporary effects/queued effects/action budgets;
- restoring initiative/phase position safely;
- regenerating legal choices after restoration;
- restoring hook-local state.

### RNG rewind/replay policy — BLOCKING

The newest Java slice proves authoritative RNG can be consumed by selected post-damage hooks.

That makes rewind design more explicit, not more complete.

A battle rewind would need a decision between policies such as:

- restore the RNG state and reproduce the same future rolls;
- preserve consumed RNG and allow a new outcome;
- seed each loop iteration independently.

No policy is currently verified.

### Temporal entity-transfer contract — BLOCKING

No verified combat/runtime contract moves one persistent combatant between temporal contexts during a battle while preserving identity, queued effects and transcript ordering.

### Temporal reward idempotency — narrative/world-state design only

Pass 54 proposes idempotent reward claims for loops. This is not yet an AutoPTU-Java battle mechanic.

## Encounter readiness — Clocktower Echo

Narrative premise: a bounded interval repeats around a clocktower.

### REDUCED

Run each attempt as a newly instantiated legal static encounter. Reset only authored local world-state objects. Preserve only explicitly permitted knowledge/clues. Keep unique rewards idempotent.

This avoids battle rewind entirely.

### FULL

Rewind the tactical encounter itself.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/forced movement/interception — BLOCKING when spatial state must restore across complex movement;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED baseline;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if dynamic battlefield state participates;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING if opponents learn or adapt across iterations;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- battle rewind/checkpoint contract — BLOCKING;
- RNG rewind/replay policy — BLOCKING.

## Encounter readiness — Tomorrow's Evacuation

Narrative premise: an authenticated record from a possible future warns about a coming facility crisis.

### REDUCED

Treat the record as a provenance-bearing claim. Investigate current causes. If combat occurs, resolve a normal battle in current world state.

This version does not require physical time travel.

### FULL

Maintain a computed alternate/possible future whose state responds to current causal interventions.

Additional dependency:

- authoritative future-state projection/causal-delta contract — BLOCKING.

Battle dependencies vary by the actual current encounter.

## Encounter readiness — Threshold Pursuit

Narrative premise: an actor attempts to cross a temporal boundary during confrontation.

### REDUCED

Cross before or after battle. The grid contains actors from one temporal context only.

### FULL

Allow crossing during tactical resolution.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full damage/status/move/Ability/item/Feature families — respective PARTIAL categories where used;
- terrain/weather/hazards/zones/reactions — BLOCKING for an active temporal boundary zone;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for pursuit/escape objectives;
- adapter/playback — BLOCKING;
- temporal entity-transfer contract — BLOCKING.

## Encounter readiness — Archive From Tomorrow

Preferred implementation is non-combat.

Required narrative systems:

- archive provenance;
- temporal context/provenance;
- actor knowledge;
- scientific/case verification;
- public-information propagation.

No battle category needs to be claimed unless current world state independently produces an encounter.

## Temporal non-inference gate

Never infer that:

- authoritative RNG means a turn can be rewound safely;
- a delayed effect means time travel exists;
- a possible future is canonical future state;
- a temporal vision is physical traversal;
- strange initiative/order behavior permits global time manipulation;
- an Ability touching lifecycle or delayed damage proves a temporal subsystem;
- restoring a Minecraft region restores PTU battle state;
- restoring PTU state restores world Chronicle/history;
- the same Pokémon can be duplicated by loading an earlier world snapshot;
- a time loop grants repeated XP/items/captures;
- Celebi or Dialga caused a temporal anomaly without canon approval.

## Reduced-version recommendation

For initial Ouros implementation, temporal stories should prefer:

- historical reconstruction;
- possible-future records;
- visions with provenance;
- temporal windows used outside combat;
- between-scene crossings;
- loop attempts instantiated as fresh encounters from an authored checkpoint.

Avoid live battle rewind and cross-time tactical movement until dedicated authoritative contracts exist.

## Canon/mechanics questions still unresolved

- Exact PTU/Caelo rules for Celebi, Dialga and temporal powers.
- Exact delayed-Move behavior and Java parity coverage relevant to time-themed encounters.
- Whether physical time travel is part of Ouros canon at all.
- Whether divergent branches are playable or only provenance/history structures.
- What actor memories survive an approved divergence or loop.
- How a loop handles player-controlled irreversible choices.
- Whether RNG should repeat after a rewind.
- How to prevent item/Pokémon duplication across historical snapshots.
- How Cobblemon preserves one persistent entity across temporal instances.
- Whether multiplayer actors can occupy different temporal contexts simultaneously.
