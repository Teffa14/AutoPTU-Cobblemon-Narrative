# Engine Readiness Snapshot — Pass 88

Status: implementation-evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`f4a5232b406fe0c80137e4d1d2f8408771ab4ba0`

Latest visible commit:

`Run canonical field progression during ROUND_START`

AutoPTU Python `main` inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest visible Python changes remain Career-oriented and do not justify tactical capability promotions.

## New evidence relative to the peatland design

No newer Java head appeared after Pass 87 during this inspection.

The relevant current Java evidence remains:

- canonical `BattleEnvironmentState` owns duration-bearing terrain/zone/room entries;
- field progression runs through authoritative `ROUND_START` lifecycle;
- field expiry can emit semantic events and perform verified cleanup;
- lifecycle-level field progression is checked against Python-oracle fixtures;
- Minecraft/controller code does not own field expiry.

This is genuine environmental lifecycle infrastructure.

It does not implement peatland hydrology, bog/fen classification, water-table changes, unstable mats, peat fire, wetland visibility, dynamic water, mud, sinking or restoration mechanics.

## AutoPTU-Java README boundary

Current `main` still describes the following as unfinished:

- broader core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full semantic battle-event/transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the anti-overclaim boundary.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

VERIFIED for implemented static geometry.

Pass 88 guardrail:

Geometric LoS does not prove visibility through mist, smoke, tall wetland vegetation or across a changing water surface.

### base movement legality

VERIFIED for the implemented Shift/Jump and Overland/Swim/Sky surface contracts.

Pass 88 guardrail:

A wetland label does not create a movement cost. Peat, moss, mud, floating vegetation, saturated soil, boardwalks and drainage ditches require exact terrain/blocker contracts before they affect battle movement.

### core calculations

VERIFIED for ported calculation primitives.

Pass 88 guardrail:

There is no generic peat, bog, fen, water-table, smoke, subsidence, sinking or restoration modifier.

### action economy/initiative

VERIFIED for the implemented initiative/action surface.

Pass 88 guardrail:

Water-table changes, restoration operations and survey windows remain overworld/world-state clocks unless a verified battle mechanic explicitly models them.

### AI legal-action infrastructure

VERIFIED for supported legal choices.

It does not provide tactical policy goals such as:

- REACH_WEIR;
- PROTECT_RESEARCHER;
- WITHDRAW_FROM_UNSAFE_PEAT;
- FIND_STABLE_PATCH;
- AVOID_SMOLDERING_ZONE;
- CROSS_BOARDWALK;
- HOLD_SAFE_HUMMOCK;
- EVACUATE_SURVEY_TEAM.

## PARTIAL

### full turn/round lifecycle

PARTIAL.

Java now includes substantial typed phase/round state, initiative rollover, delayed-hit infrastructure and canonical field progression at `ROUND_START`.

It still does not prove every phase effect, switch/send-out path, reaction, duration, field interaction, delayed behavior, cleanup path or transcript event.

### full stateful damage pipeline

PARTIAL.

Normal and delayed-hit resolution increasingly derive data from authoritative runtime state and apply verified post-damage hooks.

Pass 88 guardrail:

Peat fire, sinking, smoke, falling through a mat, contaminated water or boardwalk failure cannot deal HP damage unless an exact verified PTU rule path produces that damage.

### status lifecycle

PARTIAL.

Representative application, phase and expiry slices exist.

Pass 88 guardrail:

Peatland narration cannot create Burned, Poisoned, Tripped, Stuck, Slowed, Confused, Injured or any other Status.

### move-specific behavior

PARTIAL.

Representative Move contracts and delayed-hit behavior exist.

Pass 88 guardrail:

A Move that manipulates water, earth, vegetation, smoke, terrain, forced movement or structures must be individually verified before a peatland encounter depends on it.

### abilities

PARTIAL.

Representative Ability hooks have parity evidence.

Pass 88 guardrail:

Water Absorb, Storm Drain, Swift Swim, Dry Skin, Damp, Arena Trap, species flavor or wetland-associated lore cannot be generalized into peatland immunity, stable footing or restoration behavior.

### items

PARTIAL.

Representative held-item behavior exists.

Pass 88 guardrail:

Water-level loggers, peat probes, boardwalk tools, sample jars, pumps, gates and restoration equipment remain world-state assets unless they correspond to an implemented PTU Item.

### Trainer Features/perks

PARTIAL.

Representative Features and hook infrastructure exist.

Pass 88 guardrail:

Survival, researcher, ranger, engineering, ecology or wetland expertise does not grant automatic movement or hazard resistance without exact PTU/Caelo text and Java implementation.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

BLOCKING as a family.

Pass 88 FULL encounter needs may include:

- displacement around failing surface patches;
- intercepting an actor before entering an unsafe zone;
- rescue extraction from a hazardous edge;
- dynamically changing routes as water level changes;
- movement around a failed boardwalk;
- retreat to verified stable ground.

None is authorized by the existing base movement implementation alone.

### terrain/weather/hazards/zones/reactions

BLOCKING as a family despite the new canonical field-state lifecycle infrastructure.

Current Java evidence proves storage/progression/expiry wiring for generic field entries. It does not prove:

- peat or mire terrain;
- mud/saturated-ground terrain;
- water-level zones;
- smoke zones;
- underground/smoldering fire hazards;
- unstable-mat hazards;
- entry/exit reactions;
- water-control interactables;
- dynamic hydrologic transitions;
- full Weather lifecycle;
- Minecraft initialization of a peatland field state.

### AI tactical policy

BLOCKING.

Legal actions exist, but there is no verified scoring/policy for safe-ground seeking, evacuation, restoration-objective interaction, smoke avoidance or wildlife withdrawal.

### Minecraft/Cobblemon/Craftics adapter/playback

BLOCKING.

There is no verified end-to-end contract that converts persistent peatland revisions into an AutoPTU battle snapshot and then replays terrain/hydrology/state changes in Minecraft without duplicating PTU rules.

# Pass 88 encounter dependency summary

## Rewetting Weir Inspection

Reduced version can run using the static-combat surface after overworld resolution.

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL if a normal battle invokes them:

- full turn/round lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING for the full version:

- complete movement if changing access/interception/rescue is required;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## Smoldering Peat Edge

Reduced version:

Wildfire/Crisis resolves the safe perimeter before battle. The combat arena is static and verified safe.

Full version additionally needs:

- terrain/weather/hazards/zones/reactions for active unsafe/smoke zones;
- complete movement if evacuation/interception/displacement matters;
- AI tactical policy for hazard avoidance/withdrawal;
- adapter/playback for semantic field events.

Any environmental damage/status also requires a verified PTU/Caelo rule and a corresponding implemented damage/status path.

## Floating Mat Survey

Reduced version:

Route assessment happens outside battle. AutoPTU begins only on a selected stable patch.

Full version needs:

- complete movement if surface failure changes positions;
- terrain/weather/hazards/zones/reactions for unstable patches;
- tactical AI for route preference/withdrawal;
- adapter/playback for changing geometry or surface state.

# Peatland-specific non-inferences

The following claims are prohibited without explicit evidence:

`wetland` → PTU terrain

`bog` → Slow Terrain

`fen` → groundwater battle effect

`mud` → Stuck

`peat` → sinking

`floating mat` → falling

`dark water` → Poisoned

`smoke` → Accuracy penalty

`peat fire` → Burned

`moss` → healing

`Wooper` → Swim/withdrawal policy for the whole group

`Ducklett` → bog-moss spawn bonus

`Stunfisk` → soil/mineral truth

## Python evidence boundary

Python AutoPTU remains the designated oracle while the Java port is incomplete.

The available runtime evidence shows concrete movement modes such as Swim/Sky and capability-driven movement decisions, but no inspected evidence establishes a general peatland/bog/fen subsystem.

Therefore a narrative biome label cannot be translated into PTU behavior by the Minecraft adapter.

# Overworld blockers introduced by Pass 88

These are outside the battle core and still need implementation in the future persistent-world layer:

- `PEATLAND_SYSTEM` identity/version history;
- peat extent/depth evidence;
- peatland-type assessments;
- water-table revision history;
- drainage legacy graph;
- water-control links;
- subsidence observations;
- verified peat-fire involvement;
- rewetting-project state and reviews;
- peatland-access profiles;
- peatland Pokémon-use observations;
- Peatland → Freshwater synchronization;
- Peatland → Soil synchronization;
- Peatland → Wildfire synchronization;
- Peatland → Road Ecology synchronization;
- Peatland → Cobblemon projection;
- Peatland → frozen battle snapshot;
- Peatland → Minecraft projection.

# Rules/canon questions still unresolved

- Exact PTU/Caelo treatment of wetlands, marsh, mud or bog-like terrain.
- Exact Naturewalk labels and effects relevant to these environments.
- Exact Survival/skill procedures for route finding, field sampling or unstable ground.
- Whether Caelo modifies any of those rules.
- Which Ouros peatlands are authored canon rather than procedurally proposed.
- Whether any peatland fire, extraction or restoration history predates the campaign.
- Which Pokémon have authored regional relationships to those sites.
- How coarse water-table state should advance while chunks are unloaded.
- Whether battles will ever support dynamic hydrology or always freeze a safe tactical snapshot.

Full primary Caelo text was not reliably recoverable during this runtime. No Caelo-specific peatland rule is asserted in this snapshot.