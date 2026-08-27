# Engine Readiness Snapshot — Pass 78

Status: implementation evidence snapshot, not canon.

Date: 2026-08-27

## Scope

This snapshot supports `design/puzzles-environmental-mechanisms-persistent-state-extension.md` and the mechanically rich Pass 78 candidates.

It preserves the binding authority boundary in `design/cobblemon-runtime-authority-boundary.md`:

- Ouros owns persistent puzzle/world facts;
- AutoPTU owns tactical facts and battle resolution;
- Minecraft/Cobblemon provides overworld embodiment, interaction and playback;
- Cobblemon battle-state/participant/controller code never becomes authoritative for Ouros combat.

## Repositories inspected

Writable:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Inspected revisions

AutoPTU-Java `main`:

`a2a2b7fc040bacd0242de615b774d63890952225`

Latest inspected change:

`Freeze held-item START slot ordering (#239)`

AutoPTU Python `main`:

`11c4aea350193d2ed0940ec5a8ada09e44b6d291`

Latest inspected change:

`Career: train the full active squad each season`

The Python change is Career/progression behavior and does not establish a new tactical capability family relevant to puzzle-battle hybrids.

## Live Java evidence

The current Java README continues to define the intended architecture clearly:

- AutoPTU-Java decides legal actions and battle results;
- Minecraft/Cobblemon/Craftics adapt world state and render resulting events;
- Java remains a core library rather than the Minecraft mod;
- Python remains the oracle while parity work is incomplete.

Current implemented/verified slices still include:

- targeting, areas, footprints, anchors and LoS;
- Shift and Jump movement legality;
- Damage Base and type-effectiveness tables;
- calculation primitives;
- d20 accuracy resolution;
- combat-stat resolution;
- typed turn flow/action budget;
- deterministic initiative;
- legal autobattler action-space generation.

The README still explicitly lists as unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- StatusController, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic battle-event emission and full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The new Java head adds deterministic held-item START slot-order ownership with parity/tests. This strengthens a bounded Item/lifecycle slice. It does not establish complete Items, lifecycle, statuses or any environmental family.

## Permanent capability map

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
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Pass 78 makes no category promotion.

## Why ordinary puzzles do not need tactical capability promotion

A world-state puzzle can operate without entering the battle engine when it only changes persistent overworld facts such as:

- door state;
- passage availability;
- bridge orientation;
- lift presentation;
- a mechanism indicator;
- which static arena variant will be used later;
- a documented site clue;
- a reset/bypass record;
- a Maintenance or Travel handoff.

These are implementation/world-state concerns, not proof of PTU battle families.

Ouros can therefore progress puzzle content while the tactical adapter remains incomplete.

## Cobblemon/Minecraft reuse for Pass 78

Aggressive safe reuse remains desirable for:

- blocks and structure variants;
- doors, trapdoors and mechanism visuals;
- pistons or similar animation surfaces when suitable;
- sound and particles;
- Pokémon overworld models/entities/animations;
- interaction events;
- networking and client synchronization;
- UI prompts;
- world coordinates and collision geometry as observed input;
- persistent props;
- visual indication of solved/partial/reset states.

Required authority direction:

`Ouros puzzle/world state -> reviewed transition -> Minecraft/Cobblemon projection`

For battle hybrids:

`Ouros world state -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon projection`

Forbidden:

`Minecraft block/Cobblemon battle state -> invent or mutate authoritative AutoPTU battle fact`

A redstone or client-side mechanism may be a presentation implementation. It must not be the only source from which canonical puzzle completion or tactical state can be reconstructed.

## Feedback/playback versus tactical adapter

Pure puzzle feedback can be implemented before full battle playback if it is only a world-state projection.

Examples:

- control click accepted -> mechanism animation/sound;
- remote door opened -> state indicator changes;
- module solved -> central light/marker changes;
- reset executed -> world props return to the stored baseline.

This does not move `Minecraft/Cobblemon/Craftics adapter/playback support` out of BLOCKING because that permanent category concerns authoritative AutoPTU battle projection and input collection, not ordinary world-state animation.

## Pokémon-assisted puzzle solutions

No broad capability family is promoted by Pass 78.

Before using an individual Pokémon to operate a mechanism, source/runtime review must establish the exact behavior. A visual Cobblemon animation is insufficient evidence.

Potential governing evidence may come from:

- legal movement capabilities;
- a specific Move with validated overworld interpretation;
- an Ability;
- an Item;
- a Trainer Feature/perk;
- another explicit PTU/Caelo rule intended for Ouros.

The narrative layer cannot infer field utility from species, type, body size or Move name alone.

## Dynamic topology remains blocked tactically

A rotating platform, gate, bridge or wall can change overworld geometry today.

Changing that geometry during an AutoPTU battle requires exact runtime ownership of the resulting tactical facts.

If the transition changes:

- legal tiles;
- LoS;
- range pathing;
- occupied positions;
- cover/zone state;
- movement costs;
- collision/landing;
- target legality,

then it cannot be simulated by Minecraft alone.

At minimum, dynamic environment work depends on `terrain/weather/hazards/zones/reactions`, which remains BLOCKING when environmental tactical state is involved. If actors are physically moved by the mechanism, `complete movement including push/pull/knockback/interception/forced movement` is also BLOCKING.

## Puzzle traps and punishment

Pass 78 does not authorize direct battle damage/status from puzzle failure.

A wrong input that is intended to:

- deal HP damage;
- inflict a status;
- change combat stages;
- force movement;
- trigger a reaction;
- create a timed damaging zone

requires exact PTU/Caelo legality and the relevant AutoPTU families.

Current classifications mean:

- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- complete movement — BLOCKING;
- full lifecycle — PARTIAL when timing is relevant.

Therefore the default Pass 78 puzzle failure should change world state, consume time, close/open routes, trigger a reset, create noise/attention or require another interaction when authored. It should not invent combat punishment.

## Encounter readiness — Rotating Platform Interruption

Intended full version:

- one persistent mechanism controls platform orientation;
- platform state changes tactical routes during battle;
- controls can be contested;
- dynamic geometry can affect LoS/pathing;
- rotation may relocate actors if the final design chooses that behavior;
- AI can reason about platform objectives;
- Minecraft renders AutoPTU-owned state.

Dependency status:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if rotation relocates actors;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when selected content requires it;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic tactical topology/environment state;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:

Operate the platform in overworld state before battle. Choose one static reviewed arena from the resulting orientation. Freeze mechanism state mechanically until battle completion. Resume operation afterward.

This preserves the premise without using Minecraft to move authoritative combatants.

## Encounter readiness — Gatehouse Override Under Pressure

Intended full version:

- objective includes reaching/operating controls;
- gate states change tactical routes/LoS;
- opponents understand control denial or withdrawal;
- optional interception/forced movement may contest the mechanism.

Primary blockers:

- terrain/weather/hazards/zones/reactions for dynamic gate state;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support;
- complete movement if interception/forced relocation is required.

Partial families remain relevant according to roster/content:

- full lifecycle;
- damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

Reduced version:

Resolve gate operation as an overworld interaction before combat or at explicit checkpoints between separate battles. Each gate state maps to a static arena. No mid-battle Minecraft gate event changes tactical legality.

## Noncombat puzzle content already viable conceptually

Pass 78 can progress independently of missing tactical families through:

- persistent mechanism identity;
- state snapshots;
- input/transition history;
- clue provenance;
- visual/audible feedback contracts;
- manual reset logic;
- anti-softlock state review;
- bypass records;
- multi-module aggregate state;
- remote output references;
- route/access handoffs;
- repair/reconfiguration history;
- stale public guides;
- Chronicle callbacks;
- world-state reconstruction after reconnect/reload.

Actual Minecraft integration still needs implementation work, but none of these require adopting Cobblemon battle-state authority.

## PTU/Caelo questions still unresolved

Pass 78 does not establish:

- generic puzzle-solving Skill checks or DCs;
- a universal Strength/pushing field action;
- arbitrary elemental activation of machinery;
- Move-to-overworld utility mappings;
- Trainer Feature puzzle interrupts;
- item-based technical bypass rules;
- damage/status from failed mechanisms;
- tactical object-interaction action costs;
- dynamic door/platform rules in combat;
- forced relocation caused by machinery;
- environment-triggered reactions.

Every such mechanic needs governing-source extraction and runtime evidence before authoritative use.

## Canon questions still unresolved

- which Ouros sites contain persistent mechanisms;
- which mechanisms are ancient, modern, civic, industrial or natural;
- who built and maintains them;
- what technologies are regionally plausible;
- who may reset or override them;
- which clues are public;
- which old configurations are remembered;
- which Pokémon can legally assist with particular mechanisms;
- how destructive bypasses are treated socially/institutionally;
- which solved states persist and for how long.

## Read-only conclusion

AutoPTU-Java and AutoPTU were inspected only.

The Java head advanced from Pass 77 to a parity-backed held-item START slot-order slice. That is meaningful implementation progress but remains bounded to Items/lifecycle evidence and does not change the permanent capability map.

Python remains on Career/progression work relevant to roster development, not Pass 78 tactical readiness.

The new puzzle layer can therefore make immediate worldbuilding progress through persistent overworld state, while Rotating Platform Interruption and Gatehouse Override retain reduced static-arena forms until dynamic environment, tactical AI and adapter evidence are verified.
