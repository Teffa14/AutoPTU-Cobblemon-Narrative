# Engine Readiness Snapshot — Pass 62

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.

Date: 2026-08-20

## Repositories inspected

Read-only:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`7d7d55795e18d177c217ef75acff98622a4e9746`

Latest inspected commit:

`Port round-scoped initiative modifiers (#94)`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/7d7d55795e18d177c217ef75acff98622a4e9746

The commit follows Pass 61 head `daa8956f913322fd7a17c3374f838303d0aa4a4e`.

New evidence includes:

- a pure initiative-round modifier parity boundary;
- Rocket Initiative handling in that slice;
- initiative-penalty application/expiry handling;
- the Inner Focus [Errata] exception in that resolver;
- temporary-effect cleanup reporting;
- Python oracle fixture export;
- Java parity tests and CI wiring;
- explicit room-effect dependency in the fixture model.

This is useful evidence for the already-VERIFIED action economy / initiative family and for the PARTIAL lifecycle family.

It does not prove weather, terrain, hazards, forced movement or broad reactions.

## Java README boundary

The current README still states that Python AutoPTU is authoritative while the port is incomplete.

It still lists unfinished broad work including:

- core combatant/grid battle state expansion;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- tactical AI scoring/policy;
- Craftics/Cobblemon adapter.

README:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

## Python AutoPTU live evidence

Current inspected Python head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest work remains Career-focused (`Career: make roster recovery deterministic`).

No newer Python tactical commit was observed in this run.

Available project-file evidence from the Python battle state contains freshwater/river/lake environment labels, Swim movement handling and selected terrain-linked behavior. Those exact oracle slices do not prove Java parity for river currents, floods or dynamic water state.

## Permanent capability map

| Permanent capability family | Pass 62 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Dedicated geometry, targeting, footprint, anchor and LoS coverage exists. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers and fit predicates exist. Static Swim legality does not prove currents or changing water levels. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement/interception and broad movement reactions remain unfinished. |
| core calculations | VERIFIED | PTU tables, combat stages, accuracy primitives, crit probability and selected modifiers exist. |
| action economy / initiative | VERIFIED | Typed turn flow, deterministic initiative/order, authoritative progress/rollover and parity-tested initiative-entry/round-modifier slices are evidenced. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure continues to improve, but complete status/Ability/Feature/reaction/delayed-effect coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Multiple damage/post-damage slices exist while the README still lists full damage as unfinished. |
| status lifecycle | PARTIAL | Multiple status contracts and timing slices exist; complete controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Static movement terrain costs and weather calculation primitives do not prove runtime terrain, flood phases, currents, hazards, zones or broad reactions. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; complete PTU Move behavior does not. |
| abilities | PARTIAL | Multiple Ability hooks exist; full registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog behavior remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered/lifecycle infrastructure plus selected Features exist; complete catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-action generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware scoring/policy remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core and does not yet own Minecraft projection/playback. |

## Pass 62-specific overworld blockers

Freshwater hydrology is primarily an overworld/world-state concern.

`OVERWORLD_CATCHMENT_GRAPH = BLOCKING`

The server needs persistent upstream/downstream reach connectivity, tributaries, wetland/floodplain edges and groundwater links.

`OVERWORLD_WATER_REGIME_STATE = BLOCKING`

The server needs coarse current and historical state for flow, level, reconnection, drying and flood pulses.

`OVERWORLD_WATER_CONTROL_OPERATIONS = BLOCKING`

Dams, gates, pumps, levees, reservoirs and diversions need server-owned operating state and event history.

`OVERWORLD_HYDROLOGY_OBSERVATION_MODEL = BLOCKING`

Gauge/sensor/manual observations need method, time, units, uncertainty and data-quality state.

`OVERWORLD_GROUNDWATER_SURFACE_LINKS = BLOCKING`

Springs, aquifers and surface reaches need explicit edges before delayed or subsurface effects can be generated.

`OVERWORLD_HYDROLOGY_TO_COBBLEMON_PROJECTION = BLOCKING`

Catchment state can eventually shape freshwater habitat/spawn context, but loaded entities cannot become authoritative population evidence and the mapping must resist rare-spawn exploitation.

`OVERWORLD_HYDROLOGY_TO_BATTLE_PROJECTION = BLOCKING`

The adapter needs a revisioned snapshot contract mapping world-state water conditions only into mechanics the Java core can actually execute.

## Encounter dependency review

### Sluice Gate Survey

Full version requires:

- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING if current displaces actors or Pokémon flee through lanes;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for changing inundation/current effects;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for retreat/protect/reach-gate objectives;
- Minecraft/Cobblemon/Craftics playback — BLOCKING;
- hydrology observation/control writeback — BLOCKING outside battle core.

Reduced version:

Inspect gauges, debris and gate state in overworld. Freeze one water-level map before combat. Run a conventional static battle only when conflict occurs. Resolve gate operations and downstream effects after battle as server-owned world state.

### Floodplain Reconnection

Full version requires dynamic water/terrain state and objective-aware movement.

Key blockers:

- complete movement/interception/forced movement — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI tactical policy — BLOCKING;
- Minecraft playback — BLOCKING.

Reduced version:

Advance the floodplain between encounters in coarse world-state phases. Each battle receives one stable snapshot. Battle results describe the encountered individuals only; catchment-scale ecological effects require later observations.

### Dry-Season Ford

Full version may require current-sensitive movement, route objectives and rescue/withdrawal behavior.

Reduced version:

Resolve route eligibility before battle. Use a static exposed-ford arena. Do not invent Slowed, Tripped, knockback, drowning or Swim checks from visual water.

## Why the new initiative commit does not affect hydrology blockers

The round-scoped initiative resolver is a bounded parity slice.

It strengthens initiative and lifecycle evidence.

It does not provide:

- river current vectors;
- flood-level changes during battle;
- water-zone entry/exit reactions;
- dynamic terrain conversion;
- forced movement from water;
- drowning/suffocation;
- bridge/gate interactable objectives;
- AI route planning around rising water;
- Minecraft water-state synchronization.

Therefore no freshwater encounter should use those effects until separate contracts are verified.

## PTU / Caelo caution

Pass 62 creates no mechanical freshwater rule.

Do not infer or invent:

- current speed;
- movement penalties from water depth;
- drowning/suffocation;
- flood damage;
- mud penalties;
- forced movement from flow;
- environmental Poison/Paralysis/Slowed/Tripped;
- fishing bonuses;
- Water-type bonuses;
- rain mechanics;
- dam-collapse damage;
- irrigation or crop bonuses;
- Pokémon control over regional water state;
- capture modifiers in wetlands or rivers.

The project-supplied primary Caelo corpus was not reliably retrievable in this automation runtime. No new Caelo-specific freshwater, terrain, movement or hazard rule is asserted.

## Snapshot conclusion

Pass 62 does not justify a permanent capability promotion.

Java head `7d7d55795e18d177c217ef75acff98622a4e9746` strengthens the already-VERIFIED action economy / initiative category and adds another bounded lifecycle parity slice. Lifecycle remains PARTIAL.

Freshwater worldbuilding can advance safely because catchment connectivity, water regime, infrastructure operations, observations and downstream consequences live outside the battle core. Rich river/flood encounters remain blocked primarily by complete movement, terrain/weather/hazards/zones/reactions, tactical AI and Minecraft playback.
