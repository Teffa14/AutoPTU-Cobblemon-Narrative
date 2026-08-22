# Engine Readiness Snapshot — Pass 92

Status: Implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Evidence inspected

AutoPTU-Java live head inspected:
`ce990c84ad133f9b0b56f774e2a59c8cb0c4d90b`

Latest relevant Java change:
`Track live target position for delayed combatant hits`

Observed behavior in that slice:

- delayed hits with a still-resolved combatant target use that combatant's current authoritative position when they mature;
- stored target position remains fallback/context rather than overriding a live target;
- affected-area geometry is recomputed through targeting logic;
- footprint overlap and line of sight are re-evaluated at maturity;
- target identity remains authoritative where the target id still resolves;
- parity tests freeze this behavior against the Python oracle.

Source:
https://github.com/Teffa14/AutoPTU-Java/commit/ce990c84ad133f9b0b56f774e2a59c8cb0c4d90b

Java README remains explicit that the port is incomplete. It still lists full combat state, full damage, status controller, terrain/hazards/forced movement/reactions, complete hook registries, full transcript parity, tactical AI and Minecraft/Cobblemon adapter work as unfinished.

Source:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

AutoPTU Python remains the authoritative oracle while the port is incomplete. No new Python evidence observed in this run justifies changing the permanent capability classification.

## Permanent capability categories

### VERIFIED

#### targeting / footprints / range / LoS

Static geometry, range, footprints and geometric LoS remain verified at the established project level.

Pass 92 non-inference:
A standing tree, stacked timber, forestry machine or slash pile is not automatically a blocker until the battle snapshot explicitly projects supported geometry.

#### base movement legality

Basic movement legality remains verified at the established project level.

Pass 92 non-inference:
Base movement does not prove movement over rolling logs, active machinery, unstable slopes or dynamic work zones.

#### core calculations

Established calculation primitives remain verified.

#### action economy / initiative

Established action economy and initiative remain verified.

#### AI legal-action infrastructure

Deterministic legal-choice generation remains verified.

This does not prove forestry-specific tactical goals such as WITHDRAW, CLEAR_ZONE, PROTECT_WORKER, REACH_EXIT or AVOID_HAZARD.

### PARTIAL

#### full turn / round lifecycle

Lifecycle ownership is increasingly broad, including initiative rollover, field progression and delayed-hit maturity.

Still partial because representative slices do not prove every START/END trigger, duration, reaction, delayed Move, status, Ability, Feature and transcript interaction.

#### full stateful damage pipeline

Delayed combatant hits can re-enter authoritative target, accuracy, damage, hook, HP and history paths for verified slices.

Still partial because the README continues to list full damage as unfinished.

#### status lifecycle

Representative status application/phase/cleanup behavior exists.

Still partial because the complete status controller is unfinished.

#### move-specific behavior

Delayed-hit behavior has substantial representative evidence.

Still partial because the full Move library is not ported.

#### abilities

Representative Ability hooks exist with parity fixtures.

Still partial because the complete registry is not ported.

#### items

Representative held-item behavior exists.

Still partial because item coverage remains incomplete.

#### Trainer Features / perks

Representative Feature infrastructure and specific Features exist.

Still partial because the catalog and reaction/interrupt families remain incomplete.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Still blocking.

Pass 92 forestry implications:

- rolling or shifting timber cannot displace combatants through verified forced movement;
- active equipment cannot push actors;
- evacuation corridors cannot rely on interception mechanics;
- falling objects cannot reposition targets;
- wildlife withdrawal routes cannot assume objective-aware movement.

#### terrain / weather / hazards / zones / reactions

Still blocking as a complete family.

Canonical field-state progress exists, but it does not establish forestry-specific hazards or terrain.

Pass 92 does not infer:

- felled log = Rough Terrain;
- stump = cover;
- slash = hazard zone;
- active machinery = damage zone;
- smoke = Accuracy penalty;
- wet skid trail = Slowed;
- exposed soil = Ground Terrain;
- tree fall = knockback;
- retained tree = protective zone;
- stream buffer = special field effect.

#### AI tactical policy

Still blocking.

No current evidence proves reliable AI for:

- WITHDRAW;
- CLEAR_ZONE;
- PROTECT_WORKER;
- PROTECT_WILDLIFE;
- REACH_EXIT;
- AVOID_MACHINE;
- HOLD_SAFE_CORRIDOR;
- DISENGAGE_WITHOUT_KO.

#### Minecraft / Cobblemon / Craftics adapter and playback

Still blocking.

No verified adapter contract currently turns:

- forestry treatment zones;
- retained-tree records;
- road/landing state;
- timber provenance;
- post-harvest assessment;
- regeneration trajectory

into authoritative battle state and semantic playback without duplicating PTU rules.

## Pass 92 forestry-specific blockers

`OVERWORLD_MANAGED_FOREST_STATE`
Persistent managed-forest identity and links to other ecological layers.

`OVERWORLD_FORESTRY_PROJECT_GRAPH`
Plans, treatment zones, operations, authority and project phase.

`OVERWORLD_TIMBER_PROVENANCE`
Source project, landing, custody, transport, processing and later Material Culture use.

`OVERWORLD_FOREST_ACCESS_HISTORY`
Roads, skid trails, landings, closures, rehabilitation and later repurpose.

`OVERWORLD_POST_HARVEST_ASSESSMENT`
Observed outcomes separated from planned treatment.

`OVERWORLD_REGENERATION_TRAJECTORY`
Multi-year natural/planted/mixed regeneration state.

`FORESTRY_TO_CANOPY_HANDOFF`
Persistent-tree and gap changes without duplicating canopy authority.

`FORESTRY_TO_SOIL_HANDOFF`
Work-area disturbance observations without directly diagnosing soil condition.

`FORESTRY_TO_FRESHWATER_HANDOFF`
Road/buffer/drainage observations without directly writing water-quality truth.

`FORESTRY_TO_DECOMPOSITION_HANDOFF`
Retained deadwood/slash history without duplicating decay state.

`FORESTRY_TO_COBBLEMON_PROJECTION`
Coarse habitat consequences without loaded-entity truth or rare-spawn exploits.

`FORESTRY_TO_BATTLE_SNAPSHOT`
Freeze only supported geometry and mechanics at encounter start.

## Encounter readiness

### Timber Landing Interruption

Reduced version: feasible as overworld evacuation + static arena + normal battle.

Full version blockers:

- complete movement for moving equipment/timber or protected lanes;
- environment family for genuine hazards/zones;
- tactical AI for withdrawal/clear-zone behavior;
- adapter/playback;
- forestry-to-battle snapshot.

### Riparian Buffer Survey

Reduced version: feasible as survey/world-state investigation with an optional fixed shoreline/forest battle.

Full version blockers:

- complete movement if routes change dynamically;
- environment family for any water/terrain effects;
- tactical AI for reach/protect objectives;
- adapter/playback.

Freshwater observations do not become battle penalties automatically.

### Regeneration Plot Night Watch

Reduced version: feasible as observation outside combat plus an optional standard encounter.

Full version blockers:

- complete movement for multiple crossing/withdrawing actors;
- AI tactical policy for observe/protect/withdraw goals;
- environment family if plot zones gain supported mechanics;
- adapter/playback.

Regeneration success is never determined solely by winning a battle.

## Exact non-inferences from latest Java head

The live delayed-target work proves only that verified delayed-hit slices rebind a surviving target to its current authoritative combatant position and recompute area geometry/LoS at maturity.

It does not prove:

- dynamic environmental blockers;
- tree destruction;
- machinery motion;
- falling-object mechanics;
- forced movement;
- civilian/worker evacuation AI;
- forestry hazards;
- forest-fire spread;
- terrain creation from world blocks;
- ecological writeback;
- Minecraft adapter behavior.

## Capability summary

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

## PTU/Caelo questions still unresolved

The available runtime did not expose a reliable complete Caelo corpus for this pass.

Do not invent rules for:

- tree cutting;
- falling timber;
- environmental smoke;
- forestry machinery;
- log obstacles;
- forest-specific Survival checks;
- Naturewalk interactions;
- Groundshaper forestry use;
- Cut-like Move use outside their actual rules;
- environmental damage from work sites.

Any future mechanic must be checked against the authoritative PTU/Caelo text and live engine implementation before promotion.