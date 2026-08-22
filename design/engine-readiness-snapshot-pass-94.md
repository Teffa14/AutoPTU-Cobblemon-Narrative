# Engine Readiness Snapshot — Pass 94

Status: Implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Evidence inspected

AutoPTU-Java live head inspected:
`f094111f248f3a6bfe78d835e8f4bce115f84ef7`

Latest relevant Java change:
`Match Python effective target HP eligibility (#129)`

Observed behavior in that slice:

- delayed target resolution recomputes affected geometry from current authoritative state;
- combatants with non-positive HP are excluded from effective target collection;
- the path deliberately does not invent an additional generic `active` filter because Python does not do so at that stage;
- footprint overlap and LoS remain part of effective target selection;
- delayed execution policy records these target-eligibility semantics;
- parity tests freeze the behavior against the Python oracle.

Source:
https://github.com/Teffa14/AutoPTU-Java/commit/f094111f248f3a6bfe78d835e8f4bce115f84ef7

Java README remains explicit that the port is incomplete. It still lists core battle-state expansion, full damage, status controller, terrain/hazards/forced movement/reactions, complete hook registries, full transcript parity, tactical AI and Minecraft/Cobblemon adapter work as unfinished.

Source:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

AutoPTU Python live head inspected:
`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its latest visible work remains Career-oriented and does not justify changing the tactical capability map.

Available Python evidence also includes:

- `can_swim()` as a concrete movement-capability boundary;
- separate Naturewalk labels;
- a Wilderness Guide branch for `ocean` / `wetlands` that applies specific effects only when that Trainer Feature exists and resolves legally.

These are narrow rules. They do not establish a kelp/seagrass environment subsystem.

## Permanent capability categories

### VERIFIED

#### targeting / footprints / range / LoS

Static geometry, range, footprints and geometric line of sight remain verified at the established project level.

Pass 94 non-inference:
Kelp blades, seagrass, holdfasts, restoration stakes or drifting mats do not become blockers, cover or concealment unless the server projects supported geometry into the battle snapshot.

The newest delayed-target slice strengthens target eligibility and geometry behavior for that path. It does not establish vegetation-driven visibility.

#### base movement legality

Shift/Jump and established Overland/Swim/Sky legality remain verified at the project level.

Pass 94 non-inference:
Swim legality does not prove current handling, underwater 3D navigation, vegetation drag, entanglement, breathing, depth pressure or movement through changing canopy density.

#### core calculations

Established PTU calculation primitives remain verified.

#### action economy / initiative

Established action economy and initiative remain verified.

#### AI legal-action infrastructure

Deterministic legal-choice generation remains verified.

This does not prove ecological movement policy, retreat behavior, protection priorities or route planning through submerged vegetation.

### PARTIAL

#### full turn / round lifecycle

Lifecycle ownership has substantial representative evidence for phases, round progression, field progression, initiative rollover and delayed-hit maturity.

Still partial because representative slices do not prove every START/END trigger, reaction, delayed Move, duration, Status, Ability, Feature and transcript interaction.

Pass 94 implication:
A kelp canopy changing during battle cannot be justified from lifecycle alone. An external verified environment event contract would still be required.

#### full stateful damage pipeline

Delayed combatant hits can re-enter authoritative accuracy, geometry, damage, post-damage hooks, HP and history behavior for verified slices.

The newest change adds effective-target HP eligibility for target collection.

Still partial because the README explicitly lists full damage as unfinished.

#### status lifecycle

Representative status application, phase and cleanup behavior exists.

Still partial because the complete controller remains unfinished.

Submerged vegetation prose cannot create Stuck, Slowed, Poisoned, Tripped or other statuses.

#### move-specific behavior

Delayed-hit behavior has increasingly strong representative contracts, including live target position, target collection, LoS, resource semantics and effective-target HP eligibility.

Still partial because the complete Move library is not ported.

#### abilities

Representative Ability hooks exist with parity fixtures.

Still partial because the complete registry is not ported.

Skrelp/Dragalge/Dhelmise species flavor does not prove any required Ability behavior is implemented in Java.

#### items

Representative held-item behavior exists.

Still partial because item coverage remains incomplete.

#### Trainer Features / perks

Representative Feature infrastructure and multiple concrete Features exist.

Still partial because the catalog and broad interrupt/reaction families remain incomplete.

The Python Wilderness Guide ocean/wetlands branch cannot be treated as Java parity unless that exact Feature slice is implemented and tested.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Still blocking as a complete family.

Pass 94 implications:

- currents cannot move combatants through verified forced movement;
- kelp cannot drag or pull actors;
- vegetation cannot entangle movement;
- swimmers cannot use verified tactical withdrawal corridors based on ecosystem behavior;
- researchers or juveniles cannot be escorted/intercepted using complete movement rules;
- drifting vegetation cannot push targets.

#### terrain / weather / hazards / zones / reactions

Still blocking as a complete family.

Canonical field-state ownership and progression exist for representative field entries, but the README still lists terrain/hazards/reactions as incomplete and no kelp/seagrass contract exists.

Pass 94 does not infer:

- kelp = cover;
- kelp = Rough/Slow Terrain;
- seagrass = Grass Terrain;
- shallow meadow = Water Terrain;
- dense canopy = Accuracy penalty;
- rotten seaweed = Poisoned;
- drifting kelp = zone;
- grazer patch = hazard;
- holdfast = Stuck;
- kelp canopy = weather protection;
- restoration plot = buff zone.

#### AI tactical policy

Still blocking.

No current evidence proves reliable AI for:

- WITHDRAW;
- REACH_TRANSECT;
- PROTECT_DIVER;
- AVOID_JUVENILES;
- PROTECT_SAMPLE_SITE;
- LEAVE_RESTORATION_PLOT;
- NONLETHAL_DISENGAGE;
- MOVE_THROUGH_CANOPY;
- USE_HABITAT_AS_COVER.

#### Minecraft / Cobblemon / Craftics adapter and playback

Still blocking.

No verified adapter contract currently turns:

- vegetation extent revisions;
- kelp vertical habitat bands;
- seagrass-bed state;
- canopy loss/recovery;
- nursery assessments;
- grazer pressure;
- restoration cohorts;
- detached vegetation events

into authoritative battle state and semantic playback without duplicating PTU rules.

## Pass 94 submerged-vegetation-specific blockers

`OVERWORLD_SUBMERGED_VEGETATION_SYSTEM_STATE`
Persistent system/unit identity across disturbance, loss, restoration and regrowth.

`OVERWORLD_VEGETATION_EXTENT_REVISIONS`
Versioned spatial extent with method/provenance rather than current Minecraft blocks as truth.

`OVERWORLD_SUBMERGED_STRUCTURE_REVISIONS`
Canopy/meadow/barren/recovering structure and vertical ecological bands.

`OVERWORLD_SUBMERGED_CONDITION_OBSERVATIONS`
Dated observations of density, breakage, sediment cover, grazing signs and condition.

`OVERWORLD_RECRUITMENT_STATE`
Evidence-backed recruitment/survival rather than visual planting success.

`OVERWORLD_NURSERY_ASSESSMENT`
Population-specific nursery claims with evidence and review.

`OVERWORLD_GRAZER_PRESSURE_STATE`
Grazer observations separated from moral labels and causal claims.

`OVERWORLD_RESTORATION_COHORT_PROVENANCE`
Source, placement, survival and recruitment history for restoration cohorts.

`OVERWORLD_DETACHED_VEGETATION_HANDOFF`
Attached habitat to floating Open-Ocean habitat without duplicating identity.

`SUBMERGED_VEGETATION_TO_COBBLEMON_PROJECTION`
Coarse ecological opportunities without loaded-entity truth or rare-spawn exploits.

`SUBMERGED_VEGETATION_TO_BATTLE_SNAPSHOT`
Freeze only supported static geometry/mechanics at encounter start.

## Encounter readiness

### Kelp Transect Recovery

Reduced version:
Feasible as overworld storm/monitoring resolution plus a static underwater arena and ordinary battle if needed.

Full version blockers:

- complete movement for current or vegetation displacement;
- terrain/weather/hazards/zones/reactions for kelp-driven tactical state;
- tactical AI for WITHDRAW / REACH_TRANSECT / PROTECT_DIVER;
- adapter/playback;
- submerged-vegetation-to-battle snapshot;
- any specific Move/Ability/Feature not individually parity-tested.

### Seagrass Nursery Survey

Reduced version:
Feasible as research world state plus optional fixed adjacent encounter.

Full version blockers:

- terrain/weather/hazards/zones/reactions for blade density, turbidity or shallow-water tactical effects;
- tactical AI for AVOID_JUVENILES / WITHDRAW / PROTECT_SAMPLE_SITE;
- adapter/playback;
- nursery assessment and Cobblemon projection.

### Barren Restoration Watch

Reduced version:
Feasible as conservation/science world state plus conventional combat only when independently justified.

Full version blockers:

- complete movement for protected corridors and ecological withdrawal;
- terrain/weather/hazards/zones/reactions for vegetation/grazer field state;
- tactical AI for NONLETHAL_WITHDRAW / PROTECT_PLOT;
- adapter/playback;
- restoration cohort state and grazer-pressure handoffs.

## Safe implementation policy for Pass 94

Until the missing families exist, the server should:

1. resolve habitat state before battle;
2. select a stable tactical footprint;
3. project only geometry and mechanics already supported by Java;
4. keep ecological actors that do not need to fight outside the battle roster;
5. run AutoPTU as the single authority for battle legality and outcomes;
6. write battle results back into world state without inventing population collapse, habitat damage or recovery.

## No promotions in Pass 94

The newest Java slice is meaningful but narrow. It improves delayed target eligibility and authoritative target collection. It does not justify promoting lifecycle, damage, move-specific behavior or environment families to VERIFIED.

Permanent map remains:

VERIFIED:
- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks.

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## Unresolved mechanical questions

- Exact PTU/Caelo handling of underwater visibility and line of sight.
- Exact Swim, Gilled/breathing and underwater travel rules that Ouros will inherit.
- Whether any verified Terrain labels map to kelp/seagrass habitat.
- Whether Naturewalk has an applicable marine subtype in the chosen corpus.
- Whether Wilderness Guide ocean/wetlands behavior will be ported to Java and under what exact terrain contract.
- How static 2D battle snapshots represent ecological verticality without pretending to support full 3D movement.
- Whether dynamic vegetation/current state will ever be allowed to change during a battle or only between encounters.

No Caelo-specific answer is asserted without primary text.