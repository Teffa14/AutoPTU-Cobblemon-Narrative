# Engine Readiness Snapshot — Pass 70

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.

Date: 2026-08-21

## Repositories inspected

Read-only:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`4e1492a642350e0d657dba8587e358a2f669b59c`

Latest inspected commit:

`Derive Pokemon initiative context from authoritative runtime state (#103)`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/4e1492a642350e0d657dba8587e358a2f669b59c

### New bounded evidence since Pass 69

The initiative candidate projection now derives additional state from `BattleRuntimeState`, including canonical trainer initiative modifier and several temporary-effect flags used by existing initiative contracts.

This strengthens the already VERIFIED `action economy / initiative` family and reduces caller-owned semantic inputs.

It does not prove:

- fishing mechanics;
- hooked or line-tension state;
- aquatic escape behavior;
- moving boats;
- dynamic currents;
- hatchery/aquaculture mechanics;
- spawning zones;
- stock assessment;
- complete environment behavior;
- tactical AI for withdraw/protect/forage;
- Minecraft/Cobblemon projection.

## Python AutoPTU live evidence

Current inspected Python head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible work remains Career-focused and does not change this run's tactical capability classification.

Existing project-file evidence confirms Python has explicit capture resolution and aquatic movement slices. That does not establish a general Fishing/Aquaculture subsystem.

## PTU/Caelo evidence relevant to Pass 70

Available project evidence confirms explicit capture rules, movement modes and authored Pokémon capabilities.

The primary Caelo corpus was not reliably retrievable for exact fishing-rule extraction in this run. No new Fishing Rod, bait, net, Survival, angling, harvest or hatchery mechanic is asserted.

## Permanent capability map

| Permanent capability family | Pass 70 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Geometry, target anchors, footprints, ranges and LoS are implemented with parity evidence. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers and fit predicates have bounded implementation evidence. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Broad forced movement, interception and related movement reactions remain unfinished. |
| core calculations | VERIFIED | Core PTU tables/stages/accuracy and selected modifiers have implementation evidence. |
| action economy / initiative | VERIFIED | Ordering, runtime projection, round progression and initiative assembly/install have strong parity coverage. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure is substantial; complete status/Ability/Feature/reaction/delayed coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Multiple damage and post-damage slices exist; full pipeline remains unfinished. |
| status lifecycle | PARTIAL | Several status contracts exist; full controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Canonical environment state exists, but broad behavior, transitions, hazards and reactions are not complete. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; catalog behavior is incomplete. |
| abilities | PARTIAL | Multiple Ability hooks exist; complete registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog does not. |
| Trainer Features / perks | PARTIAL | Registry/runtime infrastructure plus selected Features exist; complete catalog is not proven. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-choice generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware decisions for withdraw, protect, escort, avoid zone, forage or interact remain future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a headless rules core; runtime projection/playback is not complete. |

## Pass 70-specific overworld blockers

`OVERWORLD_FISHERY_PROFILE = BLOCKING`

A persistent fishery object linking population, water body, use, management and history does not yet exist in server authority.

`OVERWORLD_FISHING_EFFORT_STATE = BLOCKING`

Fishing pressure and effort need persistent records independent of encounter count.

`OVERWORLD_CATCH_OBSERVATION_LEDGER = BLOCKING`

Catch/release/escape/sample observations need provenance and method context.

`OVERWORLD_STOCK_ASSESSMENT = BLOCKING`

Population trend must be derived from evidence rather than loaded entities.

`OVERWORLD_FISHERY_MANAGEMENT_MEASURES = BLOCKING`

Seasonal/zone/method restrictions need scope, authority, reason and review state.

`OVERWORLD_BYCATCH_NON_TARGET_STATE = BLOCKING`

Non-target contacts need observation/care/custody handling without invented Injury or Status results.

`OVERWORLD_AQUACULTURE_SITE_STATE = BLOCKING`

Hatchery/pond/facility capacity, staffing and water dependencies are not modeled authoritatively.

`OVERWORLD_CULTURE_COHORT_STATE = BLOCKING`

Background cohorts need coarse state while important Pokémon retain individual identity.

`OVERWORLD_STOCKING_RELEASE_GRAPH = BLOCKING`

Release source, location, objective and later monitoring need append-only provenance.

`OVERWORLD_POST_RELEASE_MONITORING = BLOCKING`

Survival/movement/reproduction observations need Science integration and uncertainty.

`OVERWORLD_SPAWNING_WINDOW_STATE = BLOCKING`

Spawning windows require authored ecology + Seasonality + observation rather than calendar inference alone.

`OVERWORLD_FISHERY_TO_FRESHWATER = BLOCKING`

Hydrology must remain authoritative for river/lake state. Fisheries can consume it but not rewrite it directly.

`OVERWORLD_FISHERY_TO_MARITIME = BLOCKING`

Vessel/sea-lane state remains Maritime authority.

`OVERWORLD_FISHERY_TO_CONSERVATION = BLOCKING`

Management decisions and protected populations need explicit inter-layer contracts.

`OVERWORLD_FISHERY_TO_FOOD = BLOCKING`

Resource provenance must cross into Food/Material state without turning Pokémon entities into food batches.

`OVERWORLD_FISHERY_TO_BIOSECURITY = BLOCKING`

Stocking/translocation can create biosecurity questions and must not bypass that review.

`OVERWORLD_FISHERY_TO_COBBLEMON = BLOCKING`

Players must not be able to manipulate rare spawns directly by changing visible fishing effort or loaded entities.

`OVERWORLD_FISHERY_TO_BATTLE = BLOCKING`

Fishing context cannot create hooked/grappled/status/terrain effects without exact validated rules.

## Critical distinction: Swim legality versus fishing mechanics

Java's base movement legality includes bounded Swim handling.

That means the engine can reason about certain legal movement on water maps.

It does not mean Java can:

- simulate fishing lines;
- pull Pokémon between tiles;
- create hook tension;
- resolve nets;
- model schools as stock state;
- model fishery effort;
- determine spawning closures;
- perform hatchery releases;
- calculate catch probability from fishing method.

Those systems remain separate.

## Encounter dependency review

### Spawning Reach Closure

Full version:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING if actors dynamically cross/withdraw
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full lifecycle — PARTIAL
- damage — PARTIAL
- statuses — PARTIAL where an exact rule applies
- terrain/weather/hazards/zones/reactions — BLOCKING for protected/mechanical zones or current-sensitive behavior
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Reduced version:

Resolve closure, visitors and aquatic movement before combat. Freeze a static shoreline map. The spawning area remains world state and presentation unless a later exact PTU contract projects it mechanically.

### Hatchery Intake Failure

Full version additionally depends on:

- interactable objective semantics — BLOCKING outside the permanent capability map;
- dynamic water projection — BLOCKING;
- wildlife withdrawal/protection policy — BLOCKING under AI tactical policy;
- adapter/playback — BLOCKING.

Reduced version:

Resolve intake operation via Infrastructure + Freshwater first. If conflict remains, use a fixed legal arena. No current, flood, water-quality or intake effect is recreated as tactical rules.

### Fishing Festival Overflow

Full version additionally depends on:

- moving boats/noncombatants — BLOCKING under complete movement + adapter;
- objective-aware competition policy — BLOCKING under AI tactical policy;
- live fishing-objective semantics — BLOCKING outside current battle contracts.

Reduced version:

Run fishing effort, catches, releases and scoring in the event/world-state layer. Open AutoPTU only for a discrete battle. Battle damage never becomes the fishing score.

## Current safe implementation strategy

Worldbuilding can proceed now with:

- fishery history;
- stock/catch observations;
- public festivals;
- hatchery institutions;
- release provenance;
- management discussions;
- famous persistent aquatic Pokémon;
- gear/workshop culture;
- research programmes.

Mechanically rich fishing battles should remain reduced/static until exact PTU/Caelo fishing rules and engine support exist.
