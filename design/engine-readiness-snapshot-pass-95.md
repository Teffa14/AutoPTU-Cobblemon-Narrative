# Engine Readiness Snapshot — Pass 95

Status: Implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Evidence inspected

AutoPTU-Java live head inspected:
`784c74790b9cb1ec1723d89027724bbac885897f`

Latest relevant Java change:
`Execute stale delayed targets from authoritative geometry (#130)`

Observed behavior in that slice:

- matured delayed hits whose original combatant target no longer exists can fall back to the stored target anchor;
- the stored anchor is expanded through the authoritative effective-target resolver;
- geometry, footprints, LoS and target eligibility are recomputed against current battle state;
- any combatants currently selected by that geometry receive normal delayed-hit execution bindings;
- a stale delayed hit with no effective current target resolves to no target and is removed instead of remaining queued forever;
- resource accounting remains on the original action rather than double-spending action/frequency at delayed maturity;
- tests cover stale-target retargeting and empty-resolution behavior.

Source:
https://github.com/Teffa14/AutoPTU-Java/commit/784c74790b9cb1ec1723d89027724bbac885897f

Java README still states that the port is incomplete and explicitly leaves full battle-state expansion, full damage, status controller, terrain/hazards/forced movement/reactions, complete hook registries, transcript parity, tactical AI and Minecraft/Cobblemon adapter work unfinished.

Source:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

AutoPTU Python live head inspected:
`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its recent work remains Career-oriented and does not justify changing the tactical capability map.

Available Python evidence includes concrete creative actions, movement/capability checks and terrain/hazard behavior in specific rules. This does not establish a generic persistent-construction subsystem.

## Permanent capability categories

### VERIFIED

#### targeting / footprints / range / LoS

Static geometry, range, footprints and geometric LoS remain verified at the established project level.

The newest delayed-target slice adds stronger evidence that stored anchors can be re-evaluated against current authoritative geometry after the originally referenced target disappears.

Pass 95 non-inference:
A dam, burrow, hive wall, tunnel entrance or nest chamber does not become cover, blocking terrain or a legal target merely because Minecraft renders it.

#### base movement legality

Established Shift/Jump and Overland/Swim/Sky movement legality remains verified.

Pass 95 non-inference:
A tunnel existing in world state does not grant Burrow, allow digging through blockers, create multi-level traversal or prove safe passage.

#### core calculations

Established PTU calculation primitives remain verified.

#### action economy / initiative

Established action economy and initiative remain verified.

Delayed-hit maturity does not double-spend the original action/frequency in the newly verified stale-target path.

#### AI legal-action infrastructure

Deterministic legal-choice generation remains verified.

This does not prove AI goals such as protecting a nursery, maintaining a dam, withdrawing through a burrow or avoiding eggs/juveniles.

### PARTIAL

#### full turn / round lifecycle

Lifecycle ownership has representative evidence for phase progression, round state, initiative, field progression and delayed-hit maturity.

The latest slice strengthens one delayed-hit branch after target disappearance.

Still partial because representative delayed behavior does not prove every delayed Move, START/END trigger, duration, reaction, Status, Ability, Feature or transcript interaction.

#### full stateful damage pipeline

Delayed combatant hits can re-enter authoritative target resolution and the normal move-resolution path for verified scenarios.

Still partial because the README explicitly leaves full damage unfinished.

A structure cannot receive HP or damage unless a future authoritative object-damage contract exists.

#### status lifecycle

Representative status application/phase/cleanup behavior exists.

Still partial because the complete controller is unfinished.

Dam water, nest material, dust, mud, silk or tunnel conditions cannot create Stuck, Slowed, Tripped, Poisoned, Burned or other statuses from narrative description.

#### move-specific behavior

Delayed-hit behavior now has strong representative contracts for live targets, stale targets, geometry recomputation, LoS, HP eligibility, resource accounting and execution.

Still partial because the complete PTU Move library is not ported.

A Move that damages terrain or objects in PTU must be individually verified before it can alter a persistent Pokémon-built structure.

#### abilities

Representative Ability hooks exist with parity tests.

Still partial because the full registry is incomplete.

Species lore about Bibarel, Durant, Excadrill, Bunnelby or Combee does not imply a battle Ability capable of construction.

#### items

Representative held-item behavior exists.

Still partial because coverage remains incomplete.

#### Trainer Features / perks

Representative Feature infrastructure and multiple concrete Features exist.

Still partial because broad coverage and reaction/interrupt families remain incomplete.

Any engineering, excavation, Survival or environmental Feature must be verified individually before use.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Still blocking as a complete family.

Pass 95 implications:

- current cannot move actors through a dam breach;
- collapsing passages cannot displace combatants;
- defenders cannot intercept movement through a nest corridor via a verified general system;
- moving construction material cannot push actors;
- burrowing cannot create new tactical routes;
- escorts through tunnels cannot rely on complete interception/protection rules.

#### terrain / weather / hazards / zones / reactions

Still blocking as a complete family.

Canonical field-state primitives and representative progression exist, but the README still lists terrain/hazards/reactions as unfinished and no Pokémon-built-structure field contract exists.

Pass 95 does not infer:

- dam = Water Terrain;
- dam break = current hazard;
- lodge = cover;
- tunnel = Rough Terrain;
- burrow = escape zone;
- silk bridge = movement bonus;
- hive wall = destructible cover;
- nest chamber = protection zone;
- mud = Slowed/Tripped;
- loose rock = collapse hazard;
- eggs/juveniles = battle objects with HP.

#### AI tactical policy

Still blocking.

No current evidence proves reliable AI for:

- PROTECT_STRUCTURE;
- PROTECT_NURSERY;
- MAINTAIN_STRUCTURE;
- WITHDRAW_TO_BURROW;
- CROSS;
- LEAVE_CONSTRUCTION_SITE;
- NONLETHAL_DISENGAGE;
- DEFEND_ENTRY;
- AVOID_EGGS_OR_JUVENILES.

#### Minecraft / Cobblemon / Craftics adapter and playback

Still blocking.

No verified adapter contract currently turns:

- persistent Pokémon-built structure IDs;
- structure physical revisions;
- builder attribution;
- occupancy revisions;
- dam/tunnel/nest geometry;
- maintenance events;
- abandonment/reuse state;
- downstream environmental-effect links

into authoritative battle state and semantic playback without duplicating PTU rules.

## Pass 95 specific blockers

`OVERWORLD_POKEMON_BUILT_STRUCTURE_STATE`
Persistent identity for dams, burrows, nests, tunnels, hives/walls, shelters and related structures.

`OVERWORLD_BUILDER_ATTRIBUTION`
Evidence-backed builder identity with uncertainty and versioning.

`OVERWORLD_STRUCTURE_PHYSICAL_REVISIONS`
Coarse geometry/condition history independent of loaded Minecraft blocks.

`OVERWORLD_STRUCTURE_OCCUPANCY`
Occupied, seasonal, vacant, abandoned and reused state with evidence.

`OVERWORLD_STRUCTURE_MAINTENANCE_HISTORY`
Observed construction/repair/expansion events and material provenance.

`OVERWORLD_STRUCTURE_FUNCTION_ASSESSMENT`
Evidence-backed nesting, shelter, nursery, storage, water-control or transit function.

`OVERWORLD_STRUCTURE_ENVIRONMENT_HANDOFF`
Safe causal handoff into Hydrology, Soil, Flora, Wild Collectives, Road Ecology and other receiving layers.

`OVERWORLD_STRUCTURE_ALTERATION_AUTHORITY`
Who may remove, modify, reroute around or preserve a structure under authored regional rules.

`OVERWORLD_STRUCTURE_TO_COBBLEMON`
Bounded projection of builders/occupants without treating loaded entities as population or occupancy truth.

`OVERWORLD_STRUCTURE_TO_BATTLE`
Frozen structure geometry and only explicitly supported PTU field/object rules when opening an encounter.

## Encounter dependency summary

### Dam Maintenance Conflict — FULL

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version is viable earlier by freezing water/crossing geometry before combat and keeping the dam non-destructible tactically.

### Tunnel Breakthrough Survey — FULL

VERIFIED on frozen geometry:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- legal-action infrastructure.

BLOCKING for intended dynamic version:
- multi-route dynamic movement and interception;
- changing/collapsing terrain;
- tactical retreat/protection policy;
- adapter/playback.

Reduced version uses overworld survey plus one validated static chamber.

### Colony Nursery Perimeter — FULL

The narrative premise can advance now, but the intended objective-driven battle remains blocked by tactical AI, complete movement and object/zone semantics.

Reduced version keeps eggs/juveniles out of battle state and uses only an outer-perimeter static encounter if combat occurs.

## No promotions this pass

The live Java head improves delayed-hit target recovery and execution. It does not justify promoting lifecycle, full damage, move-specific behavior or any environmental family to VERIFIED.

The permanent map therefore remains:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.
