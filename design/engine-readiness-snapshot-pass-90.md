# Engine Readiness Snapshot — Pass 90

Status: Implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Evidence inspected

AutoPTU-Java live head inspected:
`bffc16b3642738757e3c8eb09fbd9a4921e9beba`

Latest relevant Java change:
`Run combatant delayed hits during ROUND_START`

Observed behavior in that slice:
- delayed-hit maturity is registered as a ROUND_START lifecycle hook;
- field progression runs before delayed-hit maturity;
- due combatant-target delayed hits re-enter authoritative resolution;
- action/frequency cost is not consumed again;
- resulting damage updates authoritative HP/history;
- tests assert the lifecycle ordering and resolution path.

Source:
https://github.com/Teffa14/AutoPTU-Java/commit/bffc16b3642738757e3c8eb09fbd9a4921e9beba

Java README remains explicit that the port is incomplete and Python AutoPTU is still the oracle. It still lists full damage, status controller, terrain/hazards/forced movement/reactions, complete registries, AI policy and Minecraft/Cobblemon adapter work as unfinished.

Source:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

AutoPTU Python live head inspected:
`e4bb0ca38b7018710af476ce365d515a387de4e7`

Recent Python changes remain Career-oriented and do not justify changing the tactical capability map.

## Permanent capability categories

### VERIFIED

#### targeting / footprints / range / LoS
Evidence remains broad enough for the currently ported targeting geometry and legality contracts.

Important non-inference for Pass 90:
Geometric LoS does not prove visibility through rain, mist, sewer darkness, spray or pollution.

#### base movement legality
Evidence supports basic Overland/Swim/Sky movement legality, terrain costs, blockers, Wallrunner, sprint, jump boundaries and fit predicates described by the Java project.

Important non-inference for Pass 90:
Base movement does not prove dynamic floodwater, current displacement, slippery surfaces, water-depth changes or evacuation movement.

#### core calculations
Damage Base/type/evasion/accuracy/stage primitives and related calculation slices remain verified at the established project level.

#### action economy / initiative
The initiative/action-economy family remains verified. Recent work further strengthens runtime-owned initiative and delayed-hit resource accounting.

#### AI legal-action infrastructure
The deterministic legal `BattleChoice` / action-space infrastructure remains verified as a legality surface.

This does not prove tactical selection quality.

### PARTIAL

#### full turn / round lifecycle
Recent evidence is stronger:
- canonical field ROUND_START progression exists;
- delayed-hit maturity now executes automatically during ROUND_START after field progression;
- initiative rebuild/installation and several phase hooks are authoritative.

Still partial because representative lifecycle slices do not prove every START/END effect, duration, delayed effect, reaction, status, Ability, Feature and transcript interaction.

#### full stateful damage pipeline
Delayed combatant hits can now re-enter authoritative accuracy/damage/hook/HP/history resolution.

Still partial because the README continues to list full damage resolution as incomplete and representative hooks do not cover every modifier/order interaction.

#### status lifecycle
Representative status application/phase/cleanup behavior exists, but the complete status controller remains unfinished.

#### move-specific behavior
Coverage continues to grow, especially around delayed-hit semantics.

Still partial because one delayed family and other representative Moves do not prove the full Move library.

#### abilities
Representative Ability hooks and parity fixtures exist.

Still partial because the complete Ability registry is not ported.

#### items
Representative held-item behavior exists.

Still partial because complete item behavior/registry is not ported.

#### Trainer Features / perks
Representative Feature registries and specific Features exist.

Still partial because the catalog and interrupt/reaction families remain incomplete.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement
Still blocking.

Pass 90 implications:
- moving floodwater cannot push combatants;
- a current cannot carry an actor;
- emergency flow cannot alter position;
- wildlife/civilian escape lanes cannot rely on interception;
- a moving debris field cannot use forced movement.

#### terrain / weather / hazards / zones / reactions
Still blocking as a complete family.

Recent field-state progress is real but insufficient for promotion.

Pass 90 does not infer:
- rain = PTU Weather;
- floodwater = terrain/hazard;
- runoff plume = Poisoned zone;
- culvert = cover;
- wet pavement = Slow/Rough Terrain;
- pump/electrical failure = hazard;
- detention basin water = combat modifier;
- green infrastructure = Grass Terrain or healing.

#### AI tactical policy
Still blocking.

The legal-action list exists, but the engine does not yet prove AI capable of understanding objectives such as:
- WITHDRAW;
- PROTECT_WORKER;
- REACH_DRY_ZONE;
- CLEAR_OBJECTIVE;
- AVOID_HAZARD;
- HOLD_POSITION_WITHOUT_KO;
- CROSS_ZONE.

#### Minecraft / Cobblemon / Craftics adapter and playback
Still blocking.

No verified adapter contract currently turns:
- settlement rainfall;
- drainage-network state;
- basin level;
- overflow state;
- runoff plume;
- green-infrastructure condition

into an authoritative battle environment and semantic playback without duplicating PTU rules.

## Pass 90 stormwater-specific blockers

These are outside or above the battle core and remain BLOCKING until implemented:

`OVERWORLD_STORMWATER_DISTRICT_GRAPH`
Persistent drainage-zone identity and connectivity.

`OVERWORLD_DRAINAGE_NETWORK_STATE`
Nodes/edges, operational state, blockages and maintenance.

`OVERWORLD_SURFACE_SUMMARY_REVISIONS`
Coarse built-surface change without per-block hydrologic simulation.

`OVERWORLD_STORMWATER_EPISODES`
Rainfall event → runoff observations → storage/overflow history.

`OVERWORLD_OVERFLOW_ASSESSMENTS`
Separate observed flooding from reviewed cause.

`OVERWORLD_GREEN_INFRASTRUCTURE_STATE`
Versioned rain gardens, basins, infiltration assets and maintenance.

`OVERWORLD_STORMWATER_MONITORING`
Sensors, observations, samples and provenance.

`OVERWORLD_STORMWATER_WILDLIFE_USE`
Observed Pokémon use of drains/channels/basins without converting that into spawn truth automatically.

`STORMWATER_TO_FRESHWATER_HANDOFF`
Pass runoff/overflow consequences to the receiving-water system.

`STORMWATER_TO_SANITATION_HANDOFF`
Only for authored/verified cross-connections, combined systems or contamination incidents.

`STORMWATER_TO_COBBLEMON_PROJECTION`
Project coarse habitat/access consequences without creating rare-spawn exploits.

`STORMWATER_TO_BATTLE_SNAPSHOT`
Freeze a mechanically legal arena before battle and include only environment effects supported by authoritative rules/contracts.

`STORMWATER_TO_MINECRAFT_PROJECTION`
Render network state, wet/dry variants and maintenance state without making loaded blocks authoritative hydrology.

## Encounter readiness

### Underpass Intake Blockage

Current reduced version: feasible as world-state storm resolution + fixed dry battle platform.

Full version blockers:
- complete movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- adapter/playback;
- stormwater-to-battle projection.

### Detention Basin Wildlife Conflict

Current reduced version: feasible as observation/maintenance decision + static shoreline battle if needed.

Full version blockers:
- objective-aware withdrawal;
- dynamic shallow-water zones;
- environment projection;
- tactical AI;
- adapter/playback.

### Outfall Plume Investigation

Current reduced version: feasible as sampling world state + optional static combat.

Full version blockers:
- dynamic water/plume environment;
- movement/objective interactions if actors cross the flow;
- tactical AI;
- adapter/playback.

## Exact non-inferences from the latest Java head

The new ROUND_START delayed-hit hook proves only that due combatant-target delayed hits can mature automatically at the verified lifecycle point through the current authoritative path.

It does not prove:
- all delayed Moves;
- all tile-target delayed effects;
- environmental timers;
- stormwater/flood timers;
- hazard progression;
- current movement;
- area evacuation;
- field-effect behavior beyond currently implemented slices;
- complete transcript parity.

The existence of canonical field entries/progression also does not prove that a stormwater state may be inserted as a custom field effect.

## Mechanical questions still unresolved

- Exact PTU/Caelo drowning and suffocation rules.
- Exact treatment of deep/shallow water outside normal Swim legality.
- Whether current/flow has an existing authoritative forced-movement rule.
- Whether sewage/runoff exposure has any defined PTU status interaction.
- Exact rules for environmental electricity near water, if any.
- Which Survival/Technology/Medicine/Education Features may inspect or operate infrastructure.
- Whether Caelo modifies urban-water or flood behavior.
- How dynamic environmental state should be frozen when a Minecraft encounter starts.

## Capability table

| Capability family | Pass 90 state | Stormwater relevance |
| --- | --- | --- |
| targeting / footprints / range / LoS | VERIFIED | Static battle geometry and targets |
| base movement legality | VERIFIED | Basic legal movement on frozen arena |
| complete movement / forced movement / interception | BLOCKING | Currents, escape lanes, moving debris |
| core calculations | VERIFIED | Existing calculations only |
| action economy / initiative | VERIFIED | Standard combat sequencing |
| full turn / round lifecycle | PARTIAL | Delayed/field progression improving, incomplete family |
| full stateful damage pipeline | PARTIAL | No custom flood/runoff damage allowed |
| status lifecycle | PARTIAL | No environmental status inference |
| terrain / weather / hazards / zones / reactions | BLOCKING | Primary blocker for dynamic stormwater battle spaces |
| move-specific behavior | PARTIAL | Use only verified Moves |
| abilities | PARTIAL | Use only verified Abilities |
| items | PARTIAL | Use only verified Items |
| Trainer Features / perks | PARTIAL | Infrastructure checks need exact rules |
| AI legal-action infrastructure | VERIFIED | Legal choices can be enumerated |
| AI tactical policy | BLOCKING | Cannot trust objective/withdrawal policy yet |
| Minecraft/Cobblemon/Craftics adapter/playback | BLOCKING | No authoritative stormwater projection yet |

## Planning conclusion

Stormwater worldbuilding can advance immediately because network identity, maintenance, runoff observations, green infrastructure, habitat use and causality are overworld state.

Dynamic flood combat should not advance beyond reduced/static versions until complete movement, environment/hazard behavior, tactical AI and the adapter are proven.
