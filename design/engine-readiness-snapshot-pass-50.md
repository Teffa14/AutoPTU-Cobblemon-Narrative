# Engine Readiness Snapshot — Pass 50

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only Python oracle
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live heads

### AutoPTU-Java

Inspected head:

`9e1c918f33faa45c4c8832ba457cc36b875267c7`

Latest inspected change:

`Extract shared Aura Break errata bonus adjustment`

The new slice extracts a reusable Aura Break [Errata] bonus-adjustment contract. It inspects server-owned temporary effects, handles expiry, preserves the source ID and routes Aura Storm [Errata] through the shared adjustment. Tests cover matching, mismatch, expiry and snapshot iteration semantics.

This is useful evidence for:

- server-owned temporary-effect state;
- focused post-result Ability contracts;
- parity-first extraction of shared Ability behavior;
- expiry/source metadata handling.

Do not infer from it:

- complete Aura Break runtime behavior;
- complete Aura Storm runtime wiring;
- complete Ability coverage;
- complete damage pipeline;
- complete temporary-effect handling;
- complete reaction coverage;
- terrain/weather/hazards;
- forced movement/interception;
- tactical AI;
- Minecraft/Cobblemon/Craftics playback.

The current Java README continues to state that Python AutoPTU is authoritative while the port is incomplete and still lists as unfinished:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- semantic battle-event emission/full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

### Python AutoPTU

Inspected head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest visible Python work is Career/roster-recovery work. It does not justify promotion of any Java tactical family.

Python remains the behavioral oracle while Java is incomplete.

Read-only Python battle-state evidence also shows `Phasing` and `Teleporter` being recognized for specific tactical behavior such as grapple escape. This does not prove portal creation, arbitrary teleport destinations or inter-dimensional overworld travel.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Strong deterministic evidence remains for battle targeting, areas, footprints, target anchors, range and line-of-sight.

This does not verify non-Euclidean overworld visibility or portal sightlines.

#### base movement legality

Strong evidence remains for represented Overland/Swim/Sky movement, ordinary terrain cost/blocker handling, Wallrunner, sprint, jump and landing-fit boundaries.

This does not verify teleport edges, portal traversal, moving platforms or topology changes.

#### core calculations

Damage Base tables, type-effectiveness steps, combat stages, accuracy stages and established calculation primitives remain verified.

#### action economy / initiative

Typed phases, action budgets and deterministic initiative/League ordering remain verified.

#### AI legal-action infrastructure

The engine can enumerate/filter deterministic legal battle choices.

This does not prove that AI understands exits, portals, objectives, evacuation or anomaly state.

### PARTIAL

#### full turn / round lifecycle

Typed phases, actor/phase state, cleanup, delayed-hit infrastructure, round histories and selected hooks provide significant slices. Complete lifecycle behavior remains unproven.

#### full stateful damage pipeline

Several calculation/post-damage contracts exist. The latest Aura Break work is a narrow shared adjustment and does not complete full damage resolution.

#### status lifecycle

Selected application, metadata and phase behavior exist. The complete controller remains incomplete.

#### move-specific behavior

Move-keyword parity plus selected concrete Move slices exist. The whole catalogue remains partial.

#### abilities

Several Ability families/interactions have parity-tested slices. Aura Break/Aura Storm work strengthens focused evidence but does not prove the family.

#### items

Held-item state and selected hooks exist. The complete item catalogue remains partial.

#### Trainer Features / perks

Ordered infrastructure and selected concrete Features exist with parity evidence. The complete catalogue remains partial.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

The Java README still lists forced movement among unfinished systems. Live portal traversal, moving platforms that reposition actors and interception-based exits remain blocked on this family.

#### terrain / weather / hazards / zones / reactions

Broad battlefield environmental state remains unfinished. A spatial distortion acting as a grid zone, disappearing platform, active portal tile or reconfiguration phase must therefore remain outside battle or use a reduced static version.

#### AI tactical policy

Legal choice generation exists. Objective prioritization, portal retreat, exit seeking, protection and exploration-aware policy remain blocking.

#### Minecraft / Cobblemon / Craftics adapter and playback

Java remains a rules-core library. World instancing, portal rendering, topology swaps, dimension changes and replay/writeback are not yet authoritative adapter features.

## Pass 50 dimensional-space implications

Most Pass 50 state can advance without new battle mechanics:

- anomalous-space identity;
- anchors;
- portal/access-edge records;
- destination certainty;
- return contracts;
- crossing records;
- topology versions;
- semantic anchors;
- survey evidence;
- spatial-rule claims;
- ecology spillover records;
- generated-layout feasibility checks performed before a battle instance exists.

These systems must not grant battle movement, teleportation or hazards by themselves.

## Teleporter / Phasing non-inference gate

Python AutoPTU recognizes `Teleporter`/`Phasing` in selected tactical contexts.

Do not infer:

- portal creation;
- arbitrary range/destination;
- inter-dimensional crossing;
- ally or cargo transport;
- map-wide fast travel;
- bypass of locked routes;
- automatic battle escape;
- time travel;
- Minecraft wall bypass.

An exact PTU/Caelo rule plus Java runtime/test evidence is required before any of those become mechanical behavior.

## Encounter dependency — Folding Causeway

Reduced version:

Freeze one connectivity-validated topology for the battle. Spatial changes occur between scenes only. Use ordinary supported movement and a static encounter. Advance to the stable survey anchor in overworld/world state after battle.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING if route shifts reposition actors;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL for timed changes;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when exact statuses are used;
- terrain/weather/hazards/zones/reactions — BLOCKING for disappearing/reappearing platforms or active anomaly zones;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for REACH_ANCHOR/WITHDRAW;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## Encounter dependency — Portal Ecology Spillover

Reduced version:

Resolve crossings before battle. Any Pokémon already on the ordinary side use the normal static encounter path. The portal is not a tactical tile. Preserve the same persistent Pokémon IDs in capture/retreat/world-state writeback.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for live crossing/interception;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL if the portal opens/closes by round;
- terrain/weather/hazards/zones/reactions — BLOCKING for an active portal zone;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for crossing/retreat goals;
- adapter/playback — BLOCKING.

## Encounter dependency — Mirror Facility Survey

Reduced version:

Instantiate a separate authored static location for the visit. All unusual door transitions occur outside battle. If combat begins, create a conventional static grid and preserve the facility differences as world-state facts only.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for live teleport-edge movement;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL for timed transformations;
- terrain/weather/hazards/zones/reactions — BLOCKING for geometry changes/interactables;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- Trainer Features/perks — PARTIAL when exact Features are used;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for investigation/protection objectives;
- adapter/playback — BLOCKING.

## Reconfiguring-dungeon implementation gate

A changing dungeon can be generated narratively before battle mechanics are complete only if the exploration layer guarantees:

- deterministic seed/version storage;
- stable semantic anchors;
- entry-to-objective-to-exit connectivity validation;
- objective-order feasibility;
- persistent-item placement protection;
- no procedural progression bypass;
- no destructive topology swap while a static battle is active.

If those checks do not exist, use authored/static layout variants rather than procedural generation.

## Aura Break no-inference update

Pass 50 recognizes the newest Java head `9e1c918f...` as additional focused evidence for shared post-result Ability contracts. It does not promote Ability, damage, lifecycle or reactions to VERIFIED.

## Promotion rule

A permanent capability family moves upward only when live runtime wiring, representative deterministic contracts, tests and Python-oracle parity establish the family. A shared Aura Break contract, a Teleporter check in one maneuver or one portal presentation in Minecraft cannot promote an entire category.
