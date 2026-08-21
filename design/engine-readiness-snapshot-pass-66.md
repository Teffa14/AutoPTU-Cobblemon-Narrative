# Engine Readiness Snapshot — Pass 66

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

`3d7adc9ed7c3ca49d847c45f024046f62a5e159c`

Latest inspected commit:

`Assemble authoritative initiative order (#99)`

Canonical URL:

https://github.com/Teffa14/AutoPTU-Java/commit/3d7adc9ed7c3ca49d847c45f024046f62a5e159c

New bounded evidence since Pass 65:

- Java now composes previously parity-tested Trainer and Pokémon initiative entries into one authoritative initiative order;
- active/fainted filtering is applied at that boundary;
- Parental Bond child entries are excluded by the assembly contract;
- round-scoped initiative modifiers are applied before sorting;
- temporary-effect cleanup requests are returned by the resolver;
- Trick Room ordering and League trainer-before-Pokémon ordering are part of the assembled result;
- a Python fixture exporter, Java parity test, Gradle property and CI workflow verify this slice against the pinned oracle.

This strengthens the already-VERIFIED `action economy / initiative` family.

It does not prove:

- complete round lifecycle;
- all status/Ability/Feature timing;
- full semantic BattleTranscript parity;
- terrain/weather/hazard execution;
- forced movement or reactions;
- tactical AI policy;
- Minecraft/Cobblemon adapter behavior;
- volcanic or geothermal tactical mechanics.

## Java README boundary

The current README still states that Python AutoPTU remains authoritative while the Java port is incomplete.

It continues to list unfinished broad work including:

- core combatant/grid battle state expansion;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/item/perk/Trainer Feature hook registries;
- semantic battle-event and full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This boundary is decisive for volcanic encounters.

A parity-tested initiative order does not create lava, ash, gas, unstable ground, eruption phases or environmental AI.

## Python AutoPTU live evidence

Current inspected Python main head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible work remains Career-focused.

Project evidence contains narrow environment-related behavior such as terrain labels, weather handling and selected capability/Feature interactions.

Those examples remain narrow.

They do not prove a generic volcano subsystem or Java parity for one.

## Permanent capability map

| Permanent capability family | Pass 66 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Dedicated geometry, targeting, footprints, anchors and LoS coverage exists. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers and fit predicates exist. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement, interception and broad movement reactions remain unfinished. |
| core calculations | VERIFIED | PTU tables, combat stages, accuracy primitives, crit probability and selected modifiers exist. |
| action economy / initiative | VERIFIED | Typed turn flow plus parity-tested initiative primitives, rebuild/advance and assembled ordering exist. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure is substantial, but complete status/Ability/Feature/reaction/delayed-effect coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Multiple damage/post-damage slices exist while the README still lists full damage as unfinished. |
| status lifecycle | PARTIAL | Multiple status contracts and timing slices exist; complete controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Selected primitives/consumers do not establish a complete Java battlefield environment system. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; complete PTU Move behavior does not. |
| abilities | PARTIAL | Multiple Ability hooks exist; full registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog behavior remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered/lifecycle infrastructure plus selected Features exist; complete catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-action generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware scoring/policy for withdraw, avoid-zone, protect, route or interactable objectives remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core and does not yet own Minecraft projection/playback. |

## Pass 66-specific overworld blockers

`OVERWORLD_VOLCANIC_SYSTEM_STATE = BLOCKING`

A volcanic system needs persistent identity and versioned activity independent of loaded chunks.

`OVERWORLD_VOLCANO_MONITORING_NETWORK = BLOCKING`

Stations, calibration, coverage and outages need server-owned records.

`OVERWORLD_GEOTHERMAL_FIELD_STATE = BLOCKING`

Spring/vent output, groundwater links and settlement dependencies require a dedicated persistent graph.

`OVERWORLD_VOLCANIC_UNREST_ASSESSMENT = BLOCKING`

Physical activity, observation, interpretation and institutional alert state must remain separate.

`OVERWORLD_VOLCANIC_EVENT_FOOTPRINTS = BLOCKING`

Lava, ash/tephra, gas, hydrothermal and slope events require separate versioned footprints.

`OVERWORLD_ASH_TEPHRA_STATE = BLOCKING`

Airborne ash, deposited material and later resuspension cannot be inferred from Minecraft particles.

`OVERWORLD_VOLCANISM_TO_FRESHWATER = BLOCKING`

Hydrothermal changes and volcanic deposits need validated links into catchment state.

`OVERWORLD_VOLCANISM_TO_TRAVEL = BLOCKING`

Access closures and route eligibility must be institutional/world-state decisions, not visual terrain checks alone.

`OVERWORLD_VOLCANISM_TO_COBBLEMON = BLOCKING`

Volcanic habitat state needs a non-exploitable projection into Pokémon presence.

`OVERWORLD_VOLCANISM_TO_BATTLE = BLOCKING`

A revisioned adapter is required before volcanic state becomes PTU terrain, Weather, hazards, zones or reactions.

`OVERWORLD_VOLCANISM_TO_MINECRAFT = BLOCKING`

Minecraft needs safe projection for vents, ash, geothermal sites, closures and cooled lava without becoming the authority for geology or battle rules.

## Encounter dependency review

### Observatory Evacuation

Full version:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. forced movement/interception — BLOCKING if evacuees move through the grid
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for withdraw/protect goals
- adapter/playback — BLOCKING

Reduced version:

Evacuate staff and records through world state first. Use a fixed safe summit platform. Ash, gas, steam, heat and falling material remain non-mechanical. Run a conventional static battle only if a real confrontation remains.

### Geothermal Intake Failure

Full version:

- static targeting/core/initiative — VERIFIED
- lifecycle/damage/status/Abilities/items/Features — PARTIAL as applicable
- dynamic steam, hot-water zones or machinery hazards — BLOCKING under terrain/weather/hazards/zones/reactions
- displacement/interception — BLOCKING if required
- tactical AI — BLOCKING for avoid-zone/withdraw/interact goals
- adapter/playback — BLOCKING

Reduced version:

Investigate machinery and spring flow outside battle. Freeze one dry platform. Service restoration happens through world-state actions, not an attack on a Minecraft block.

### Ashfall Pass Reopening

Full version:

- static geometry/targeting/base movement/core/initiative — VERIFIED
- changing ash/weather conditions — BLOCKING under terrain/weather/hazards/zones/reactions
- lifecycle — PARTIAL if conditions change by round
- complete movement — BLOCKING if slide/displacement/interception exists
- tactical AI — BLOCKING for route/withdraw goals
- adapter/playback — BLOCKING

Reduced version:

Survey deposit state before combat. Freeze one stable route segment. Ash has no tactical effect until an exact validated rule exists.

## Pass 66 rule cautions

Do not infer or invent:

- lava or magma damage;
- magma-tile movement permissions;
- ambient heat damage;
- volcanic-gas status effects;
- ash Accuracy penalties;
- automatic Rough/Slow Terrain from ash;
- eruption probabilities;
- random volcanic strikes;
- falling-rock or pyroclastic-flow rules;
- lahar displacement/damage;
- steam-blast damage;
- hot-spring healing;
- Fire-type immunity to volcanic hazards;
- Water-type penalties near geothermal heat;
- automatic Sunny Day, Harsh Sun or any Weather state;
- Ground/Rock/Fire bonuses based on location flavor;
- Legendary-caused eruptions.

## Pass 66 conclusion

The newest Java slice closes more of initiative assembly, but the families needed for a tactically dynamic volcano remain unchanged.

Volcanic worldbuilding can advance safely now through persistent monitoring, geothermal dependencies, historical event footprints, access decisions and reduced static encounters.

Dynamic lava, ash, gas, unstable terrain, eruption phases and evacuation objectives remain gated behind environment, movement, lifecycle, tactical-AI and adapter work.