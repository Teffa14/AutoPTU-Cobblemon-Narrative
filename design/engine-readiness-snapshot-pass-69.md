# Engine Readiness Snapshot — Pass 69

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text, or engine acceptance gates.

Date: 2026-08-20

## Repositories inspected

Read-only:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`8674adb94e6614a5a9f8f3b73d6f194ba75006f0`

Latest inspected commit:

`Move initiative environment into authoritative runtime state (#102)`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/8674adb94e6614a5a9f8f3b73d6f194ba75006f0

### New bounded evidence since Pass 68

Java now owns a canonical `BattleEnvironmentState` inside `BattleRuntimeState`.

The state currently carries semantic battle inputs including:

- weather;
- terrain name;
- Tailwind-active teams;
- grounded state by combatant.

The initiative projection now reads those values from server-owned runtime state rather than trusting caller-provided environment values. Tests include rejection/ignoring of forged external environment data for initiative projection.

This is an important authority-boundary improvement.

It strengthens:

- action economy / initiative;
- authoritative runtime-state ownership;
- the future adapter boundary for environment snapshots.

It does not prove:

- Weather creation, duration, transition or cleanup;
- Terrain creation, duration, transition or cleanup;
- Grassy Terrain behavior;
- hazards;
- zones;
- environmental plant effects;
- dynamic vegetation;
- plant-generated cover;
- pollen or spore mechanics;
- broad reactions;
- complete environment-to-battle projection;
- Minecraft/Cobblemon adapter behavior.

A server-owned string such as `terrainName = "Grassy Terrain"` is not equivalent to a complete Grassy Terrain rules implementation.

## Python AutoPTU live evidence

Current inspected Python head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible work remains Career-focused.

No newer Python tactical change modifies the permanent capability map during this run.

File-library evidence from the existing project corpus confirms bounded Python behavior relevant to this pass:

- `Harvest` has specific berry Food Buff behavior and weather interaction;
- Naturewalk matching exists for authored terrain labels;
- selected flower/Grass moves and abilities exist in data/runtime contexts.

These are exact slices.

They do not prove:

- overworld plant growth;
- pollination;
- seed dispersal;
- crop yields;
- vegetation succession;
- Java parity for those broader concepts.

## PTU / Caelo evidence relevant to Pass 69

Primary file-library evidence available in this project includes exact PTU/Caelo concepts such as Naturewalk, terrain-sensitive capabilities and authored Moves/Abilities.

No new Caelo-specific rule for pollination, plant growth, Honey generation, floral resources or overworld seed dispersal is asserted here without exact source extraction.

The narrative system therefore keeps all flora ecology outside mechanical authority until a specific rule is validated.

## Permanent capability map

| Permanent capability family | Pass 69 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Geometry, targeting, footprints and LoS coverage exist. |
| base movement legality | VERIFIED | Shift/Jump legality, movement modes, terrain costs, blockers and fit predicates exist. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement, interception and broad movement reactions remain unfinished. |
| core calculations | VERIFIED | PTU tables, stages, accuracy primitives, crit probability and selected modifiers exist. |
| action economy / initiative | VERIFIED | Initiative ordering, rebuild/advance/install, candidate projection and canonical environment consumption for initiative are parity-tested. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure is substantial, but complete Trainer/status/Ability/Feature/reaction/delayed coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Several damage/post-damage slices exist while full damage remains unfinished. |
| status lifecycle | PARTIAL | Multiple status contracts exist; complete controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Canonical environment storage exists, but broad field behavior and transitions remain unverified. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; complete behavior does not. |
| abilities | PARTIAL | Multiple Ability hooks exist; full registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog does not. |
| Trainer Features / perks | PARTIAL | Infrastructure plus selected Features exist; complete catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-action generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware scoring/policy for withdraw, protect, avoid-zone, forage, guard resources or interactables remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core and does not own Minecraft projection/playback. |

## Pass 69-specific overworld blockers

`OVERWORLD_VEGETATION_UNIT_STATE = BLOCKING`

Persistent coarse vegetation units do not yet have an authoritative server model.

`OVERWORLD_VEGETATION_REVISION_HISTORY = BLOCKING`

Plant-community change must be versioned rather than inferred from current loaded blocks.

`OVERWORLD_FLOWERING_RESOURCE_WINDOWS = BLOCKING`

Bloom/nectar/pollen windows need Seasonality integration and observation history.

`OVERWORLD_POLLINATION_OBSERVATION_GRAPH = BLOCKING`

Flower visits, pollen carrying and confirmed transfer need provenance and confidence.

`OVERWORLD_SEED_SOURCE_PROVENANCE = BLOCKING`

Seed batches and wild source candidates need provenance/custody state.

`OVERWORLD_SEED_DISPERSAL_GRAPH = BLOCKING`

Wind, water, Pokémon, human, vehicle and restoration pathways need explicit evidence.

`OVERWORLD_PLANT_RECRUITMENT_STATE = BLOCKING`

New occurrence, establishment and decline need coarse persistent state.

`OVERWORLD_SUCCESSION_TRAJECTORY = BLOCKING`

Disturbed sites need branching trajectories rather than deterministic reset-to-baseline.

`OVERWORLD_RESTORATION_MONITORING = BLOCKING`

Restoration requires baseline, intervention and follow-up.

`OVERWORLD_FLORA_TO_SEASONALITY = BLOCKING`

Phenological windows must consume the calendar without letting local block updates rewrite time.

`OVERWORLD_FLORA_TO_SOIL = BLOCKING`

Soil and vegetation can influence one another only through explicit persistent-world contracts.

`OVERWORLD_FLORA_TO_FRESHWATER = BLOCKING`

Hydrologic events may move seeds or alter recruitment, but Freshwater remains the water authority.

`OVERWORLD_FLORA_TO_BIOSECURITY = BLOCKING`

New plant occurrences require Biosecurity review before introduced/spreading/impact labels.

`OVERWORLD_FLORA_TO_COBBLEMON = BLOCKING`

Vegetation must not become a direct, exploitable rare-spawn control surface.

`OVERWORLD_FLORA_TO_BATTLE = BLOCKING`

A validated projection is required before vegetation becomes PTU Terrain, cover, hazard, healing or Status state.

`OVERWORLD_FLORA_TO_MINECRAFT = BLOCKING`

Minecraft may render coarse vegetation versions but cannot become ecological rules authority.

## Critical distinction: canonical environment state versus complete environment mechanics

Java now has canonical battle-environment storage.

That is a major architectural milestone.

The current evidence means:

- initiative can consume authoritative Weather/Terrain/Grounded/Tailwind semantic inputs;
- callers cannot silently override those values for initiative projection;
- future field systems have a server-owned place to attach state.

It does not mean:

- terrain/weather/hazards/zones/reactions is PARTIAL or VERIFIED as a whole;
- Grassy Terrain effects work;
- field duration works;
- vegetation can create terrain;
- Minecraft biome/blocks can write PTU environment directly;
- all Moves/Abilities reading terrain/weather are wired.

Therefore `terrain / weather / hazards / zones / reactions` remains BLOCKING.

## Encounter dependency review

### Bloom Corridor Disturbance

Full version:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING if actors cross/withdraw dynamically
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage — PARTIAL
- statuses — PARTIAL where exact rules apply
- terrain/weather/hazards/zones/reactions — BLOCKING for mechanical flowers, dynamic corridors or protected zones
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Reduced version:

Resolve vegetation, visitors and corridor access before combat. Freeze a static battle map. Flowers are presentation only unless an exact validated rule projects a field state. Use ordinary battle resolution.

### Seed Bank Recovery

Full version:

- static geometry — VERIFIED
- base movement — VERIFIED
- interactable-object objective semantics — BLOCKING outside permanent map
- complete movement — BLOCKING if protect/withdraw/interception is required
- lifecycle/damage/status/Move/Ability/item/Feature behavior — PARTIAL as applicable
- environment — BLOCKING if weather/terrain dynamically changes recovery
- tactical AI — BLOCKING
- adapter/playback — BLOCKING

Reduced version:

Resolve sample search and custody outside the grid. Samples are not destructible tactical props. Fight only if a real confrontation exists.

### Orchard Edge Foraging Conflict

Full version:

- geometry and base movement — VERIFIED
- ecological goal state — OVERWORLD BLOCKING
- complete movement/interception — BLOCKING for forage/withdraw routing
- environment zones — BLOCKING for protected crop/floral areas
- tactical AI — BLOCKING for forage/avoid/withdraw goals
- adapter/playback — BLOCKING

Reduced version:

World state selects participants and their observed context. Noncombat options happen first. If combat starts, use a static conventional arena with no automatic crop damage or pollination effect.

## Pass 69 rule cautions

Do not infer or invent:

- flowers as Grassy Terrain;
- crop yield from observed pollinator visits;
- Honey generation from Combee presence;
- automatic Honey Gather outside exact rules;
- `Harvest` as overworld crop regeneration;
- Naturewalk as generic plant stealth;
- flower healing from Florges/Comfey flavor;
- pollen Status effects from Cutiefly/Ribombee flavor;
- poison from Budew pollen unless an exact rule/event establishes it;
- automatic seed dispersal from every Grass-type;
- automatic soil improvement from Eldegoss presence;
- plant HP or destructible crops in battle;
- vegetation cover as Rough/Slow Terrain;
- plant restoration as a direct spawn multiplier;
- all Bug/Fairy Pokémon as pollinators;
- all Grass Pokémon as gardeners;
- a single capture causing a regional pollination collapse.

## Engine implication for future flora work

The new canonical `BattleEnvironmentState` is the correct architectural direction for eventual flora-to-battle projection.

A future adapter should produce a reviewed semantic snapshot such as a legal PTU Terrain state before battle starts. It should never pass raw Minecraft flower counts, biome IDs, block light, crop age, or Cobblemon spawn density directly into battle rules.

The narrative world remains responsible for ecological meaning. AutoPTU-Java remains responsible for PTU battle mechanics.
