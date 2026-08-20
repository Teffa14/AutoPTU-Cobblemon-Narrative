# Engine Readiness Snapshot — Pass 65

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

`7ae49515a2bb22bc5b7a1da0fb1afe38643c243b`

Latest inspected commit:

`Port trainer initiative entry construction (#98)`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/7ae49515a2bb22bc5b7a1da0fb1afe38643c243b

This follows the Pass 64 inspected head:

`3e26f9d856da02a23403164f49bb46ea296ecd99` — `Port trainer initiative speed resolution (#97)`.

New bounded evidence since Pass 64:

- a dedicated Java resolver now constructs Trainer `InitiativeEntry` values from already-authoritative Trainer Speed and initiative bonus inputs;
- Tailwind contributes the exact pinned Python-oracle modifier for this contract;
- blank Trainer identity is rejected;
- Python fixtures cover base, Tailwind, identifier fallback, negative bonus and zero values;
- the parity suite is wired through Gradle and CI.

This strengthens the already-VERIFIED action economy / initiative family.

It does not prove:

- complete Trainer initiative rebuild behavior beyond this bounded entry contract;
- full turn/round lifecycle;
- complete Trainer Feature behavior;
- runtime snow, ice, glacier or avalanche state;
- terrain/weather/hazard execution;
- tactical AI;
- Minecraft/Cobblemon projection.

No permanent capability family is promoted by Pass 65.

## Java README boundary

The current AutoPTU-Java README still states that Python AutoPTU remains authoritative while the Java port is incomplete.

It still lists unfinished broad work including:

- core combatant/grid battle state expansion;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/item/perk/Trainer Feature hook registries;
- semantic battle-event and full BattleSpec -> BattleTranscript parity;
- tactical AI scoring/policy;
- Craftics/Cobblemon adapter.

That boundary is decisive for cryosphere encounters because dynamic snow, ice, avalanche, crevasse and meltwater mechanics would depend on several unfinished families.

## Python AutoPTU live evidence

Current inspected Python main head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible work remains Career-focused (`Career: make roster recovery deterministic`).

Available project evidence contains specific cold-environment behavior in Python:

- tile labels containing tundra, snow or ice can be classified as a tundra environment for selected environment-dependent behavior;
- hail/snow weather has explicit damage/immunity handling for selected types/Abilities/effects;
- `Frozen Domain` exists as a specific hazard that performs an Acrobatics check on entry and may apply Tripped on failure;
- selected Trainer Features reference Ice Moves, `Naturewalk (Tundra)` and tundra-linked effects;
- `Wilderness Guide` contains specific tundra/desert handling.

These examples must remain narrow.

They do not prove:

- general snow-depth movement rules;
- ice-slip mechanics;
- avalanche mechanics;
- crevasse mechanics;
- hypothermia or ambient cold damage;
- snow-blindness rules;
- frozen-water load limits;
- glacier movement inside battle;
- Java parity for the full relevant Python behavior.

## Permanent capability map

| Permanent capability family | Pass 65 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Dedicated geometry, targeting, footprints, anchors and LoS coverage exists. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers and fit predicates exist. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement, interception and broad movement reactions remain unfinished. |
| core calculations | VERIFIED | PTU tables, combat stages, accuracy primitives, crit probability and selected modifiers exist. |
| action economy / initiative | VERIFIED | Typed turn flow, deterministic ordering, initiative rebuild/advance slices and parity-tested Pokémon/Trainer initiative construction exist. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure is substantial, but complete status/Ability/Feature/reaction/delayed-effect coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Multiple damage/post-damage slices exist while the README still lists full damage as unfinished. |
| status lifecycle | PARTIAL | Multiple status contracts and timing slices exist; complete controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Selected primitives/consumers and Python examples do not establish a complete Java battlefield environment system. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; complete PTU Move behavior does not. |
| abilities | PARTIAL | Multiple Ability hooks exist; full registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog behavior remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered/lifecycle infrastructure plus selected Features exist; complete catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-action generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware scoring/policy for withdraw, shelter, avoid-zone or route objectives remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core and does not yet own Minecraft projection/playback. |

## Pass 65-specific overworld blockers

Cryosphere state is primarily persistent-world infrastructure until tactical environment contracts exist.

`OVERWORLD_CRYOSPHERE_STATE = BLOCKING`

The server needs a regional cryosphere object that persists independently of loaded Minecraft chunks.

`OVERWORLD_SNOWPACK_VERSIONING = BLOCKING`

Snowpack needs revisioned, coarse state capable of retaining earlier weather history and local observations without simulating every snow layer block.

`OVERWORLD_GLACIER_GEOMETRY_HISTORY = BLOCKING`

A glacier needs stable identity plus versioned terminus/coverage geometry. Minecraft ice blocks cannot be the identity store.

`OVERWORLD_FREEZE_THAW_STATE = BLOCKING`

Water, ground and relevant infrastructure need a coarse freeze/thaw state separate from generic Weather.

`OVERWORLD_AVALANCHE_ASSESSMENT = BLOCKING`

Terrain, snowpack observations, forecasts and scoped hazard assessments need distinct records. A forecast must not become canonical certainty.

`OVERWORLD_DEGLACIATION_SUCCESSION = BLOCKING`

Newly exposed ground needs coarse succession state and links to Geology/Conservation/Wildlife.

`OVERWORLD_CRYOSPHERE_TO_FRESHWATER = BLOCKING`

Validated melt/freeze events need a safe bridge into catchment state. Weather must not directly rewrite river flow.

`OVERWORLD_CRYOSPHERE_TO_TRAVEL = BLOCKING`

Route eligibility requires an explicit contract that converts snow/ice observations and institutional decisions into Travel state without using visual snow blocks as authority.

`OVERWORLD_CRYOSPHERE_TO_COBBLEMON = BLOCKING`

The server needs a non-exploitable projection from snowpack/snowline/deglaciation state into coarse Pokémon presence. Loaded entities cannot become ecological truth.

`OVERWORLD_CRYOSPHERE_TO_BATTLE = BLOCKING`

A revisioned adapter is required before regional snow/ice state becomes PTU terrain, Weather, hazards, zones or reactions. Only exact validated effects may cross this boundary.

`OVERWORLD_CRYOSPHERE_TO_MINECRAFT = BLOCKING`

Minecraft needs safe visual/physical projection for snow cover, ice, glacier geometry, route barriers, shelters, meltwater and exposed ground without becoming the authority for rules or regional state.

## Encounter dependency review

### Windslab Traverse

Full version requires:

- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement incl. push/pull/knockback/interception/forced movement — BLOCKING if slide/displacement/interception exists;
- core calculations — VERIFIED;
- action economy / initiative — VERIFIED;
- full turn / round lifecycle — PARTIAL if conditions update during combat;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain / weather / hazards / zones / reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features / perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for REACH_SHELTER, WITHDRAW or AVOID_ZONE behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- cryosphere/travel writeback — BLOCKING outside battle core.

Reduced version:

Resolve snowpack assessment and route selection before battle. Freeze one stable shelf as static geometry. Keep avalanche risk, deep snow and wind outside tactical mechanics or visual-only. If a legal confrontation occurs, run a conventional static encounter and apply route consequences afterward through persistent world state.

### Meltwater Ice Cave

Full version could require:

- targeting/range/LoS — VERIFIED;
- base movement — VERIFIED;
- complete movement — BLOCKING for displacement/current/unstable-ice movement;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL if water/ice changes by round;
- damage/status — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- tactical AI — BLOCKING for reach-exit/withdraw/survey goals;
- adapter/playback — BLOCKING.

Reduced version:

Validate one safe cave revision before battle. Freeze water level and geometry. Keep research, mapping, extraction and changing meltwater in overworld state. Start a standard static battle only for a genuine confrontation.

### Snowbound Relay Cabin

Full version could require:

- weather-linked visibility or zones — BLOCKING under terrain/weather/hazards/zones/reactions;
- dynamic entrances or displacement — BLOCKING if complete movement is required;
- protect/withdraw goals — AI tactical policy BLOCKING;
- standard targeting/core/initiative — VERIFIED;
- lifecycle/damage/status/Abilities/items/Features — PARTIAL as applicable;
- adapter/playback — BLOCKING.

Reduced version:

Resolve storm, route access and cabin condition before combat. Use fixed cabin/exterior geometry. Weather remains presentation-only unless exact validated mechanics are selected. Staff, equipment and shelter remain world-state objects.

## PTU / Caelo caution

Pass 65 creates no cryosphere mechanic.

Do not infer or invent:

- cold damage or hypothermia;
- snow-depth movement penalties;
- automatic Slow/Rough Terrain from snow;
- ice-slip checks;
- automatic Tripped on ice;
- avalanche trigger probabilities;
- avalanche damage;
- forced movement from sliding snow/ice;
- snow-blindness Accuracy penalties;
- crevasse fall rules;
- glacier-collapse mechanics;
- thin-ice load rules;
- drowning under ice;
- Hail/Snow Weather from overworld snowfall;
- Ice-type immunity to environmental cold;
- Fire-type penalties from ambient cold;
- Rain Dance/Sunny Day regional snowpack effects;
- Heater capability effects beyond exact governing text;
- Naturewalk (Tundra) effects beyond exact governing text;
- special capture modifiers for cold-stressed or displaced Pokémon.

The available Python evidence for hail/snow, tundra mappings, Frozen Domain and selected winter Features is specific implementation evidence only.

The project-supplied full Caelo corpus was not reliably retrievable during this run. No new exact Caelo snow, ice, avalanche, cold-exposure, frozen-water or glacier rule is asserted.

## Snapshot conclusion

Pass 65 does not justify a permanent capability promotion.

Java head `7ae49515a2bb22bc5b7a1da0fb1afe38643c243b` strengthens the already-VERIFIED action economy / initiative family with a parity-tested Trainer initiative-entry construction contract.

Cryosphere-rich tactical encounters remain limited primarily by complete movement, terrain/weather/hazards/zones/reactions, tactical AI and Minecraft adapter/playback.

Worldbuilding can nevertheless advance immediately by keeping snowpack, glaciers, freeze/thaw, route eligibility, ecology and meltwater as persistent world state and projecting only static, validated encounter facts into AutoPTU.
