# Engine Readiness Snapshot — Pass 91

Status: Implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Evidence inspected

AutoPTU-Java live head inspected:
`ce990c84ad133f9b0b56f774e2a59c8cb0c4d90b`

Latest relevant Java change:
`Track live target position for delayed combatant hits`

Observed behavior in that slice:

- a delayed hit with a live combatant target uses that target's current authoritative position when it matures;
- stored target position remains fallback/context rather than overriding a still-resolved combatant target;
- affected area geometry is recomputed through targeting logic;
- combatant footprint overlap and line of sight are re-evaluated for area propagation;
- target identity remains authoritative where a target id still resolves;
- parity tests freeze the contract against Python behavior.

Source:
https://github.com/Teffa14/AutoPTU-Java/commit/ce990c84ad133f9b0b56f774e2a59c8cb0c4d90b

Java README remains explicit that the port is incomplete and Python AutoPTU is still the oracle. It continues to list full combatant/grid state, full damage, status controller, terrain/hazards/forced movement/reactions, complete hook registries, full transcript parity, tactical AI policy and Minecraft/Cobblemon adapter work as unfinished.

Source:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

AutoPTU Python live head inspected:
`e4bb0ca38b7018710af476ce365d515a387de4e7`

Recent Python changes remain Career-oriented and do not justify changing the tactical capability map.

## Permanent capability categories

### VERIFIED

#### targeting / footprints / range / LoS

Evidence remains broad for currently ported static geometry and legality. The latest delayed-hit work strengthens the fact that live target position, area geometry, footprint overlap and LoS are recomputed at resolution time for that slice.

Pass 91 non-inference:
Geometric LoS does not prove underwater visibility, turbidity, bloom opacity, depth vision or refraction.

#### base movement legality

Basic Overland/Swim/Sky movement legality, terrain costs, blockers, Wallrunner, sprint, jump boundaries and fit predicates remain verified at the established project level.

Pass 91 non-inference:
Swim legality does not prove depth layers, currents, diving, oxygen, pressure, water-column movement or boat/platform movement.

#### core calculations

Damage Base/type/evasion/accuracy/stage primitives remain verified at the established level.

#### action economy / initiative

Initiative/action economy remains verified. Recent lifecycle work continues to strengthen runtime ownership without changing the category boundary.

#### AI legal-action infrastructure

The deterministic legal `BattleChoice` / action-space infrastructure remains verified.

It does not prove tactical decision quality or non-KO objective handling.

### PARTIAL

#### full turn / round lifecycle

The project has increasingly broad lifecycle ownership, including field progression, delayed-hit maturity and initiative rollover.

Still partial because representative slices do not prove every START/END trigger, duration, reaction, delayed Move, status, Ability, Feature and transcript interaction.

#### full stateful damage pipeline

Delayed combatant hits can re-enter authoritative accuracy/damage/hook/HP/history resolution and now bind live targets more accurately.

Still partial because the README continues to list full damage resolution as incomplete.

#### status lifecycle

Representative status application/phase/cleanup behavior exists.

Still partial because the complete status controller is unfinished.

#### move-specific behavior

Delayed-hit behavior has stronger evidence, including live-target geometry rebinding.

Still partial because representative delayed Moves and other slices do not prove the full Move library.

#### abilities

Representative Ability hooks and parity fixtures exist.

Still partial because the complete registry is not ported.

#### items

Representative held-item behavior exists.

Still partial because full item behavior and registry coverage are incomplete.

#### Trainer Features / perks

Representative Feature infrastructure and specific Features exist.

Still partial because the catalog and interrupt/reaction families remain incomplete.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Still blocking.

Pass 91 lake implications:

- currents cannot carry combatants;
- moving boats/platforms cannot displace combatants through authoritative forced movement;
- wild Pokémon cannot rely on true withdrawal/interception corridors;
- depth transitions cannot reposition actors;
- floating debris cannot push actors.

#### terrain / weather / hazards / zones / reactions

Still blocking as a complete family.

Canonical field-state progress is real but insufficient for promotion.

Pass 91 does not infer:

- freshwater lake = Water Terrain;
- bloom = Poisoned zone;
- low oxygen = damage/status;
- deep water = movement penalty;
- turbidity = Accuracy/LoS penalty;
- turnover = field change;
- cold/warm layer = Weather;
- littoral vegetation = cover;
- sediment plume = Rough Terrain.

#### AI tactical policy

Still blocking.

The engine does not yet prove AI capable of reliable objectives such as:

- WITHDRAW;
- RECOVER_EQUIPMENT;
- PROTECT_RESEARCHER;
- REACH_STATION;
- AVOID_ZONE;
- HOLD_PLATFORM;
- CROSS_WATER;
- DISENGAGE_WITHOUT_KO.

#### Minecraft / Cobblemon / Craftics adapter and playback

Still blocking.

No verified adapter contract currently turns:

- lake mixing state;
- depth profile;
- transparency;
- bloom observation;
- oxygen assessment;
- littoral-zone revision;
- bathymetry revision

into an authoritative battle environment and semantic playback without duplicating PTU rules.

## Pass 91 lake-specific blockers

These remain outside or above the battle core until implemented.

`OVERWORLD_LAKE_SYSTEM_STATE`
Persistent lake identity and links to Freshwater systems.

`OVERWORLD_LAKE_BATHYMETRY_REVISIONS`
Versioned coarse depth/basin structure.

`OVERWORLD_LAKE_ZONE_GRAPH`
Littoral, pelagic, deep-water, inflow/outflow and other ecological zones.

`OVERWORLD_WATER_COLUMN_STATE`
Mixed/stratified/turnover state with provenance.

`OVERWORLD_DEPTH_PROFILE_OBSERVATIONS`
Depth-specific measurements, quality flags and station identity.

`OVERWORLD_LAKE_OXYGEN_ASSESSMENTS`
Scoped reviewed assessments separated from raw readings.

`OVERWORLD_BLOOM_OBSERVATION_AND_HYPOTHESIS`
Visible/sampled bloom evidence separated from cause or toxicity claims.

`OVERWORLD_LAKE_TURNOVER_EVENTS`
Seasonal/intermittent mixing history.

`LAKE_TO_FRESHWATER_HANDOFF`
Consume catchment/inflow/outflow state without duplicating watershed authority.

`LAKE_TO_FISHERIES_HANDOFF`
Provide evidence/zone changes without directly rewriting stock truth.

`LAKE_TO_HEALTH_SURVEILLANCE_HANDOFF`
Provide validated/suspected exposure context without leaking private case data.

`LAKE_TO_COBBLEMON_PROJECTION`
Project coarse habitat consequences without loaded-entity or rare-spawn exploits.

`LAKE_TO_BATTLE_SNAPSHOT`
Freeze only mechanically supported lake context at encounter start.

`LAKE_TO_MINECRAFT_PROJECTION`
Render lake revisions, monitoring infrastructure and visual state without making water blocks authoritative limnology.

## Encounter readiness

### Deep Station Recovery

Reduced version: feasible as overworld boat/equipment state plus a fixed platform or shoreline battle.

Full version blockers:

- complete movement if platforms/currents move actors;
- terrain/weather/hazards/zones/reactions for water-column mechanics;
- AI tactical policy for recovery/withdrawal objectives;
- adapter/playback;
- lake-to-battle snapshot.

### Littoral Bloom Survey

Reduced version: feasible as sampling and bloom investigation outside combat plus optional standard shoreline battle.

Full version blockers:

- environment family;
- objective-aware AI;
- complete movement if shore/water boundaries change;
- adapter/playback.

Status lifecycle being PARTIAL does not permit a bloom to inflict Poisoned or another Status.

### Turnover Night Survey

Reduced version: feasible as timed overworld survey with independent static encounters.

Full version blockers:

- full lifecycle remains PARTIAL;
- environment family BLOCKING;
- AI tactical policy BLOCKING;
- adapter/playback BLOCKING.

## Exact non-inferences from latest Java head

The live-target delayed-hit work proves that, for that verified slice, a surviving target id follows the combatant's current authoritative position and affected area geometry/LoS are recomputed at maturity.

It does not prove:

- currents;
- dynamic lake zones;
- water depth;
- moving platforms;
- underwater LoS;
- visibility through turbidity;
- area hazards from blooms;
- environmental damage;
- oxygen or temperature effects;
- tactical withdrawal policy;
- all delayed Moves;
- tile-target delayed behavior in every case;
- complete transcript parity.

## Python oracle evidence relevant to Pass 91

The available Python battle state contains a concrete `Secret Power` environment mapping where `freshwater`, `pond`, `creek`, `river` and `lake` labels map to the move's defined speed-penalty-style effect.

It also exposes explicit `can_swim()` capability/movement checks.

These are narrow authoritative behaviors.

They do not prove a general lake environment subsystem.

## Capability table

| Capability family | Pass 91 state | Lake relevance |
| --- | --- | --- |
| targeting / footprints / range / LoS | VERIFIED | Static battle geometry; delayed live-target geometry improved |
| base movement legality | VERIFIED | Basic legal Swim/movement on frozen arena |
| complete movement / forced movement / interception | BLOCKING | Currents, moving platforms, withdrawal corridors |
| core calculations | VERIFIED | Existing legal calculations only |
| action economy / initiative | VERIFIED | Standard combat sequencing |
| full turn / round lifecycle | PARTIAL | Timed/delayed/field slices exist; incomplete family |
| full stateful damage pipeline | PARTIAL | No lake-derived damage allowed |
| status lifecycle | PARTIAL | No bloom/oxygen status inference |
| terrain / weather / hazards / zones / reactions | BLOCKING | Primary blocker for dynamic lake battle spaces |
| move-specific behavior | PARTIAL | Use only verified Moves/environment-specific mappings |
| abilities | PARTIAL | Use only verified Abilities |
| items | PARTIAL | Use only verified Items |
| Trainer Features / perks | PARTIAL | Survey/field use needs exact rules |
| AI legal-action infrastructure | VERIFIED | Legal choices can be enumerated |
| AI tactical policy | BLOCKING | Cannot trust recover/withdraw/protect policy yet |
| Minecraft/Cobblemon/Craftics adapter/playback | BLOCKING | No authoritative lake projection yet |

## Mechanical questions still unresolved

- Exact PTU/Caelo Swim and underwater rules.
- Drowning/suffocation rules, if applicable.
- Whether deep/shallow water has formal tactical distinctions.
- Exact visibility handling underwater.
- Whether any PTU/Caelo rule models current/flow as forced movement.
- Which Skills/Features can operate profiling or sampling equipment.
- Exact fishing/capture behavior across shore versus open water.
- Whether Caelo defines lake-specific encounter tables or environmental states.
- Whether future Java field-state contracts should represent any validated water effect or keep most lake state outside combat.

## Planning conclusion

Lake worldbuilding can advance immediately because bathymetry, profiles, mixing state, research stations, ecological zones, bloom observations, advisories and long-term science are overworld state.

Dynamic lake combat should remain reduced/static until complete movement, environmental behavior, tactical AI and the adapter are proven.
