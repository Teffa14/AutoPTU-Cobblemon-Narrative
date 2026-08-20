# Engine Readiness Snapshot — Pass 51

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only Python oracle
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live heads

### AutoPTU-Java

Inspected head:

`cdcff66c6b38a87fbe2388146ff45c36d3fc4817`

Latest inspected change:

`Own canonical injury history in battle runtime state`

The new slice moves current Injury history into server-owned `BattleRuntimeState`, shares that same state with the round controller/lifecycle, and tests that round snapshots use the canonical runtime object.

This strengthens evidence for:

- authoritative battle-state ownership;
- round-history persistence inside the battle core;
- lifecycle access to Injury history;
- reducing duplicate state between runtime and controller layers.

Do not infer from it:

- complete Injury rules;
- complete status lifecycle;
- complete healing/recovery;
- ecological vulnerability or predation behavior;
- AI decisions based on Injuries;
- death or consumption semantics;
- full damage resolution;
- complete battle transcript parity;
- Minecraft/Cobblemon persistence.

The current Java README continues to state that Python AutoPTU is authoritative while the port is incomplete and still lists as unfinished:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- semantic battle-event/full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

### Python AutoPTU

Inspected head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest visible Python work is Career roster-recovery behavior. It does not justify promoting any Java tactical family.

Python remains the behavioral oracle while Java is incomplete.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Deterministic evidence remains strong for battle targeting, areas, footprints, target anchors, range and line of sight.

This does not verify overworld wildlife vision, hunting perception, acoustic detection or long-distance tracking.

#### base movement legality

Strong evidence remains for represented Overland/Swim/Sky movement, ordinary terrain cost/blocker handling, Wallrunner, sprint, jump and landing-fit boundaries.

This does not verify pursuit AI, interception, retreat goals, flock/herd movement or ecological migration.

#### core calculations

Damage Base tables, type-effectiveness steps, combat stages, accuracy stages and established calculation primitives remain verified.

#### action economy / initiative

Typed phases, action budgets and deterministic initiative/League ordering remain verified.

#### AI legal-action infrastructure

The engine can enumerate/filter deterministic legal battle choices.

This does not prove that AI understands ecological goals such as hunt, protect, forage, withdraw, cross a corridor or defend a nest.

### PARTIAL

#### full turn / round lifecycle

Typed phases, actor/phase state, cleanup, delayed-hit infrastructure, damage history, Injury history and selected hooks now provide substantial slices.

The new canonical Injury-history ownership improves state coherence. Complete lifecycle behavior remains unproven.

#### full stateful damage pipeline

Several calculation and post-damage contracts exist. Canonical Injury history is adjacent state evidence, not proof that all damage/Injury creation and downstream rules are implemented.

#### status lifecycle

Selected status application, metadata and phase behavior exist. Complete controller behavior remains incomplete.

#### move-specific behavior

Move-keyword parity and selected concrete Move slices exist. Full catalogue behavior remains partial.

#### abilities

Several Ability families/interactions have parity-tested slices. Complete Ability coverage remains partial.

#### items

Held-item state and selected hooks exist. Complete item behavior remains partial.

#### Trainer Features / perks

Ordered infrastructure and selected concrete Features exist with parity evidence. Complete catalogue behavior remains partial.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

The Java README still lists forced movement as unfinished.

Ecological scenes requiring live pursuit, interception, route blocking, forced retreat, herding or displacement remain blocked on this family.

#### terrain / weather / hazards / zones / reactions

Broad battlefield environmental state remains unfinished.

Nesting zones, feeding zones, storm debris, currents, fire, toxic areas or dynamically changing habitat effects must remain outside battle or use a reduced static implementation unless exact mechanics are verified.

#### AI tactical policy

Legal choice generation exists. Ecological goal selection does not.

The engine does not yet prove policy for:

- hunting a target;
- protecting young;
- defending a resource;
- withdrawing after a condition;
- crossing a corridor;
- investigating an object/resource;
- avoiding a species;
- prioritizing escape over damage.

#### Minecraft / Cobblemon / Craftics adapter and playback

Java remains a rules-core library.

Persistent population movement, spawning, visible predation, nesting, route use, individual identity after despawn and ecological writeback are not yet authoritative adapter features.

## Pass 51 ecological-relations implications

Most Pass 51 world state can advance without new battle mechanics:

- ecological relation records;
- supporting/contradicting evidence;
- confidence and alternative explanations;
- resource dependencies;
- observed co-occurrence;
- predation/scavenging claims;
- pressure trends;
- seasonal relation windows;
- survey freshness;
- mixed-species association state;
- causal edges between habitat/resource/population observations.

These systems must not grant tactical bonuses or force combat behavior.

## Critical non-inference gate — Injury is not predation state

Java now owns current Injury history authoritatively.

Do not infer:

- Injured Pokémon automatically become prey;
- predators can detect Injury automatically;
- low HP creates ecological targeting priority;
- Injury causes flee behavior;
- Injury means disease, age or weakness in narrative terms;
- a predator gains damage/accuracy against an Injured target;
- a Fainted or Injured target is consumed;
- Injury history should persist into population ecology without an explicit world-state writeback.

An exact PTU/Caelo rule plus concrete Java runtime evidence would be required for any mechanical relationship.

## Encounter dependency — Feeding Corridor Disturbance

Reduced version:

Resolve corridor/resource pressure as world state. If one immediate subgroup becomes hostile, instantiate only those combatants in a conventional static AutoPTU battle. Resolve crossing, nesting and population movement before/after the fight.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING for live crossing, interception or herding;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when exact statuses are used;
- terrain/weather/hazards/zones/reactions — BLOCKING for tactical habitat/resource zones;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for CROSS/PROTECT/WITHDRAW priorities;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## Encounter dependency — Opportunistic Scavengers

Reduced version:

Resolve arrival timing and resource interaction in world state. If a subgroup becomes aggressive, run one static legal encounter. Never select targets automatically from HP/Injury state.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for approach/withdrawal/interception;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL for timed arrivals;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if storm debris or resource zones matter tactically;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for investigate-resource/withdraw behavior;
- adapter/playback — BLOCKING.

## Encounter dependency — Nest Defense Survey

Reduced version:

Keep nest, eggs/young, most wildlife and survey objective outside the battle grid. If battle becomes unavoidable, instantiate only the immediate aggressive subgroup. Survey state and route choice are resolved in overworld/world state.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING for live passage and defended access;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for defended zones, terrain interactions or environmental pressure;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for DEFEND_NEST/WITHDRAW/PASS_THROUGH goals;
- adapter/playback — BLOCKING.

## Ecological battle-writeback contract

A tactical transcript may produce authoritative facts such as:

- participants;
- positions/events recorded by the engine;
- legal Move use;
- damage;
- statuses;
- Fainted state;
- Injuries when authoritative;
- battle outcome.

The ecology layer may then decide whether any separate world-state consequences are warranted.

It must not mechanically derive from the transcript alone:

- death;
- consumption;
- permanent population loss;
- predator/prey identity;
- fear;
- migration;
- nesting abandonment;
- trophic cascade;
- hatred or revenge;
- ownership/association change.

Those require explicit narrative/ecological state and evidence.

## Reduced-version policy for ecological encounters

Until the blocking families are implemented:

1. choose a stable static battlefield;
2. instantiate only actors actually entering combat;
3. keep nests, young, food resources, migration flows and civilians outside tactical authority unless represented by verified mechanics;
4. resolve ecological movement and pressure in world state before/after battle;
5. use AutoPTU only for legal combat;
6. write back only facts the battle engine actually proves;
7. let the ecological layer interpret consequences conservatively.

## Pass 51 conclusion

The latest Java change improves authoritative Injury state ownership and therefore strengthens the engine boundary.

It does not unlock ecological AI.

The new interspecies-relations layer can advance now because most of its value lies in persistent evidence, observation and causal world state. The richer encounter versions remain visibly blocked on complete movement, environmental state, tactical AI and Minecraft/Cobblemon playback.