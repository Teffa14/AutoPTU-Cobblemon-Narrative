# Engine Readiness Snapshot — Pass 49

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only Python oracle
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live heads

### AutoPTU-Java

Inspected head:

`59f48a5be4446bef66959ba577d330e18696ad43`

Latest inspected change:

`Freeze Aura Storm post-damage parity contract`

This commit adds a pure Aura Storm/Aura Storm [Errata] post-damage resolution contract and freezes representative cases against the Python AutoPTU oracle. The implementation comment explicitly says this contract exists before wiring the Ability into the live registry.

This strengthens evidence for:

- parity-first Ability porting;
- post-damage contract design;
- move-keyword-dependent effects;
- Injury-dependent Ability behavior;
- Aura Break/Aura Storm interaction contracts.

Do not infer from it:

- live registry wiring for Aura Storm;
- complete Ability coverage;
- complete post-damage hooks;
- full damage resolution;
- complete Injury mechanics;
- complete Move behavior;
- broad reactions;
- terrain/weather/hazards;
- tactical AI;
- Minecraft/Cobblemon/Craftics playback.

The preceding Java sequence also established a canonical Move-keyword contract, Python exporter, parity test, Gradle wiring and CI gate. This improves metadata parity but does not prove executable behavior for every Move.

The current Java README still explicitly lists as unfinished:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- semantic battle-event emission and full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

### Python AutoPTU

Inspected head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest visible Python work is Career/roster-recovery work and does not justify promotion of any Java tactical family.

Python remains the behavioral oracle while the Java port is incomplete.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Battle targeting, area geometry, footprints, target anchors, range and line-of-sight retain strong deterministic evidence.

This does not verify overworld sight, leisure-site detection or NPC perception.

#### base movement legality

Represented Overland/Swim/Sky Shift legality, terrain costs, blockers, Wallrunner, sprint, jump and landing-fit boundaries retain strong evidence.

This does not verify escorts, dynamic crowd navigation, moving wild groups or pathfinding across the Minecraft overworld.

#### core calculations

Damage Base tables, type-effectiveness steps, combat stages, accuracy stages and established calculation primitives remain verified.

#### action economy / initiative

Typed phases, action budgets and deterministic initiative/League ordering remain verified.

#### AI legal-action infrastructure

The engine can enumerate/filter deterministic legal battle choices.

This does not prove objective-aware, retreat-aware or social/ecological policy.

### PARTIAL

#### full turn / round lifecycle

Typed phases, actor/phase state, cleanup, round histories, delayed-hit infrastructure and selected status/Ability/perk hooks provide meaningful slices.

Complete lifecycle coverage remains unproven.

#### full stateful damage pipeline

Several calculation and post-damage hook slices are authoritative. The newest Aura Storm contract is still explicitly pre-live-registry and therefore does not complete this family.

#### status lifecycle

Selected status applications, metadata and phase behavior exist. The full controller remains incomplete.

#### move-specific behavior

Move-keyword parity and selected concrete Move slices exist. The complete Move catalogue remains unproven.

#### abilities

Several concrete Ability interactions are parity-tested. Aura Storm now has a frozen pre-wiring contract. Representative Abilities do not prove the family.

#### items

Held-item state and selected item hooks exist. The complete item family remains partial.

#### Trainer Features / perks

Ordered infrastructure and selected concrete Trainer Features exist with parity evidence. The complete catalogue remains partial.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

The Java README still groups forced movement with unfinished combat systems. Any encounter relying on dynamic displacement, escort interception or movement reactions remains blocked on this family.

#### terrain / weather / hazards / zones / reactions

Broad battlefield environmental state remains unfinished. Narrow hooks do not establish general weather phases, hazards, zone control, attacks of opportunity or environmental interactables.

#### AI tactical policy

Legal choice generation exists. Objective prioritization, retreat, protection, escort, route-clearing and scenario-aware policy remain blocking.

#### Minecraft / Cobblemon / Craftics adapter and playback

AutoPTU-Java remains a rules-core library. The README still defers Minecraft/Cobblemon/Craftics integration until a parity-safe vertical slice exists.

## Pass 49 downtime implications

Most Pass 49 systems can advance without new battle mechanics:

- downtime windows;
- routines;
- hobbies;
- personal projects and milestones;
- personal collections;
- journals/scrapbooks;
- routine deviations;
- leisure preferences;
- casual shared activities;
- low-weight Chronicle callbacks;
- visual Minecraft changes to approved personal projects once an adapter exists.

None of these state objects grants PTU progression or modifies combat by itself.

## Downtime mechanical non-inferences

Narrative downtime cannot automatically:

- heal HP;
- remove Injuries;
- refresh AP;
- refresh Scene/Daily frequencies;
- increase Friendship/Loyalty;
- raise Skills or stats;
- grant XP;
- teach Moves;
- activate Training Features;
- create Digestion/Food Buffs;
- accelerate Eggs;
- produce crafting yields;
- create fishing/capture bonuses;
- alter Initiative or combat stages;
- grant battle buffs because a character relaxed.

Any such effect requires the relevant PTU/Caelo rule and actual implementation evidence.

## Encounter dependency — Picnic Site Disturbance

Reduced version:

Resolve the shifted wild route through overworld/wild-collective state. Remove picnic objects from battle authority. If conflict becomes a battle, instantiate a conventional static legal encounter and write the authoritative result back to routine and ecological state.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING if the scenario allows route interception or dynamic displacement;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL for phase-sensitive versions;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if statuses matter;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic campsite/environment state;
- move-specific behavior — PARTIAL when exact Moves are selected;
- abilities — PARTIAL when exact Abilities are selected;
- items — PARTIAL when mechanical items are selected;
- Trainer Features/perks — PARTIAL when exact Features are selected;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for withdrawal/protection/objective behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## Encounter dependency — Evening Walk Chokepoint

Reduced version:

Resolve route obstruction and detour in overworld state. If a battle remains unavoidable, instantiate a normal static encounter. Record only that the usual route changed.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING for dynamic chokepoint passage or pursuit;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL if timed;
- terrain/weather/hazards/zones/reactions — BLOCKING if route objects become tactical zones/interactables;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for REACH_EXIT/WITHDRAW behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## Encounter dependency — Shoreline Hobby Night

Reduced version:

Observation and leisure stay in overworld state. Do not invent fishing rules. If combat occurs, use a static arena with ordinary supported land/Swim geometry where legal.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED for represented ordinary Swim/land movement;
- complete movement including forced movement — BLOCKING if currents/displacement become tactical movement;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL for timed environmental behavior;
- terrain/weather/hazards/zones/reactions — BLOCKING for currents, weather phases or dynamic shoreline hazards;
- move-specific behavior — PARTIAL if exact Moves interact with water/environment;
- abilities — PARTIAL if exact Abilities matter;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for retreat/objective behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## Aura Storm no-inference gate

The latest Java commit is a valuable parity contract, but its own source states that it is frozen before live registry wiring.

Therefore this snapshot does not claim:

- Aura Storm is fully executable in Java battle runtime;
- all Aura-keyword Moves are complete;
- Aura Break is fully complete;
- Ability becomes VERIFIED;
- the full damage pipeline becomes VERIFIED.

Future narrative encounters using Aura Storm, Aura Break or any exact Aura-keyword interaction must cite runtime wiring/tests rather than this contract alone.

## Promotion rule

A permanent capability family moves upward only when runtime wiring, representative deterministic contracts, tests and Python-oracle parity establish the family. One concrete Ability, one metadata contract or one hook does not promote a complete category.
