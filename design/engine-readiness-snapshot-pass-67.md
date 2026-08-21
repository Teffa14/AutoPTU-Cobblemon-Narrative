# Engine Readiness Snapshot — Pass 67

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

`e5fa51e0de6dc53c78ba6826e4266e901a4b0313`

Latest inspected commit:

`Commit initiative assembly cleanup atomically (#100)`

Canonical URL:

https://github.com/Teffa14/AutoPTU-Java/commit/e5fa51e0de6dc53c78ba6826e4266e901a4b0313

New bounded evidence since Pass 66:

- Java now has an `InitiativeAssemblyInstaller` boundary that validates the assembled initiative result before mutating runtime state;
- initiative-related temporary-effect cleanup requests are applied only after the whole mutation set validates;
- the canonical initiative order is committed to server-owned runtime state with the cursor reset;
- unknown combatant identities fail closed before cleanup is applied;
- Trainer initiative slots remain intentionally unsupported by the current turn runner at this boundary and fail instead of being silently skipped;
- dedicated Java tests cover successful installation and atomic failure behavior.

This strengthens the already-VERIFIED `action economy / initiative` family and improves runtime-authority discipline.

It does not prove:

- complete turn/round lifecycle;
- complete Trainer turn execution;
- complete status/Ability/Feature timing;
- full damage resolution;
- terrain or soil-condition execution;
- hazards, zones or broad reactions;
- forced movement/interception;
- tactical AI policy;
- Minecraft/Cobblemon adapter behavior.

## Java README boundary

The current Java README still states that Python AutoPTU remains authoritative while the port is incomplete.

It continues to list unfinished work including:

- core combatant/grid battle-state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/item/perk/Trainer Feature hook registries;
- semantic battle-event and full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This is decisive for Pass 67.

A parity-tested initiative installer does not create mud, erosion, compaction, unstable slopes, sediment zones or soil-restoration mechanics.

## Python AutoPTU live evidence

Current inspected Python `main` head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible work remains Career-focused rather than a new tactical subsystem.

Project evidence includes narrow ground/terrain behavior.

Most relevant to this pass, Python `battle_state.py` contains a `Mold the Earth` path that requires the specific Trainer Feature and Groundshaper capability. Under that exact implementation it can reshape affected tiles and create Spikes.

Python also contains Naturewalk-aware terrain checks.

These are narrow authored mechanics.

They do not establish a generic soil-health, erosion, mud, compaction or restoration subsystem, and they do not prove Java parity for those behaviors.

## Permanent capability map

| Permanent capability family | Pass 67 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Dedicated geometry, targeting, footprints, anchors and LoS coverage exists. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers and fit predicates exist. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement, interception and broad movement reactions remain unfinished. |
| core calculations | VERIFIED | PTU tables, combat stages, accuracy primitives, crit probability and selected modifiers exist. |
| action economy / initiative | VERIFIED | Typed turn flow plus parity-tested initiative primitives, ordering, rebuild/advance and atomic runtime installation exist. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure is substantial, but complete Trainer execution and status/Ability/Feature/reaction/delayed-effect coverage are not proven. |
| full stateful damage pipeline | PARTIAL | Multiple damage/post-damage slices exist while the README still lists full damage as unfinished. |
| status lifecycle | PARTIAL | Multiple status contracts and timing slices exist; complete controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Selected primitives/consumers do not establish a complete Java battlefield environment system. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; complete PTU Move behavior does not. |
| abilities | PARTIAL | Multiple Ability hooks exist; full registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog behavior remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered/lifecycle infrastructure plus selected Features exist; complete catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-action generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware scoring/policy for withdraw, protect, avoid-zone, route or interactable objectives remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core and does not yet own Minecraft projection/playback. |

## Pass 67-specific overworld blockers

`OVERWORLD_SOIL_LAND_UNIT_STATE = BLOCKING`

The server needs coarse persistent soil units independent of loaded Minecraft blocks.

`OVERWORLD_SOIL_CONDITION_VERSIONING = BLOCKING`

Physical, chemical and biological assessment state needs revision history rather than one mutable quality score.

`OVERWORLD_SOIL_OBSERVATION_PROVENANCE = BLOCKING`

Measurements, images, samples and contextual observations need timestamped provenance.

`OVERWORLD_EROSION_SEDIMENT_GRAPH = BLOCKING`

Source erosion and downstream transport/deposition need linked but separate events.

`OVERWORLD_COMPACTION_HISTORY = BLOCKING`

Repeated traffic, construction and visitor pressure need cumulative event history without automatically asserting harmful compaction.

`OVERWORLD_LAND_RESTORATION_PROJECTS = BLOCKING`

Restoration needs baseline, interventions, monitoring and follow-up state.

`OVERWORLD_SOIL_TO_AGRICULTURE = BLOCKING`

Agriculture needs a safe read contract for soil state without using it to invent crop yields.

`OVERWORLD_SOIL_TO_FRESHWATER = BLOCKING`

Erosion/sediment links into catchment observations require server-owned causal edges.

`OVERWORLD_SOIL_TO_COBBLEMON = BLOCKING`

Soil/habitat changes need a non-exploitable projection into Pokémon presence rather than direct spawn manipulation.

`OVERWORLD_SOIL_TO_BATTLE = BLOCKING`

A revisioned adapter is required before a soil label becomes an exact PTU terrain/effect.

`OVERWORLD_SOIL_TO_MINECRAFT = BLOCKING`

Minecraft may render ruts, bare soil, recovery vegetation or closures, but block state must not become soil-condition authority.

## Encounter dependency review

### Hillside Survey After Rain

Full version:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. forced movement/interception — BLOCKING if slope changes or gullies displace actors
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL if any exact effect is used
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for withdraw/avoid-zone goals
- adapter/playback — BLOCKING

Reduced version:

Survey the slope and decide route access in world state. Freeze one stable mapped arena before combat. Rills, mud and erosion have no tactical effect. Run a conventional static encounter only if a real confrontation remains.

### Orchard Compaction Study

Full version:

- static targeting/base movement/core/initiative — VERIFIED
- lifecycle/damage/status/Abilities/items/Features — PARTIAL as applicable
- dynamic muddy/compacted/sample-protection zones — BLOCKING under terrain/weather/hazards/zones/reactions
- displacement/interception — BLOCKING if actors or equipment need protected movement
- tactical AI — BLOCKING for protect/avoid/interact goals
- adapter/playback — BLOCKING

Reduced version:

Sampling, traffic closure and drainage investigation stay outside battle. Keep orchard rows and instruments outside the grid. If combat occurs, use a fixed service lane and ordinary legal battle rules.

### Sediment Fan Reopening

Full version:

- static targeting/base movement/core/initiative — VERIFIED
- sediment/debris zones — BLOCKING
- displacement/collapse movement — BLOCKING under complete movement
- lifecycle — PARTIAL if conditions change by round
- tactical AI — BLOCKING for route/withdraw objectives
- adapter/playback — BLOCKING

Reduced version:

Freshwater + Soil assessment selects one safe corridor before battle. Freeze that geometry. Sediment creates no Slow Terrain, Rough Terrain, Accuracy penalty, Tripped, damage or forced movement unless a precise validated rule is later wired.

## Pass 67 rule cautions

Do not infer or invent:

- Rough Terrain because soil looks bare, loose or eroded;
- Slow Terrain because the overworld looks muddy;
- Spikes from ordinary digging;
- fall, slip, sink or gully checks;
- compaction movement penalties;
- erosion or sediment damage;
- dust Accuracy penalties;
- Ground-type bonuses from soil condition;
- crop-yield or growth bonuses from narrative fertility;
- automatic Groundshaper from species flavor;
- automatic Naturewalk from habitat;
- contamination statuses from soil description;
- Legendary-triggered restoration;
- Minecraft block type as PTU terrain authority.

The Python `Mold the Earth` implementation is a particularly useful non-inference check: it proves that an exact Feature + capability path can create specific terrain/hazard state. It does not authorize narrative soil state to reproduce that outcome.

## Pass 67 conclusion

The latest Java commit makes initiative-state installation more authoritative and atomic. That improves a family already marked VERIFIED, but it does not move the environment, movement, tactical-AI or adapter families required by a dynamic soil encounter.

Soil worldbuilding can advance safely now through persistent observations, erosion/sediment chains, restoration projects, agricultural context and reduced static encounters.

Dynamic mud, collapsing ground, erosion hazards, slope displacement, protected sampling zones and soil-driven battlefield effects remain gated behind explicit PTU/Caelo rules plus environment, movement, lifecycle, tactical-AI and adapter implementation.
