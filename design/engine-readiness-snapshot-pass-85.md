# Engine Readiness Snapshot — Pass 85

Status: implementation-evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`c78ebef5203b2ab67b59ae58b3729fb2ab282cef`

Latest visible commit:

`Freeze and port field ROUND_START progression`

Previous Pass 84 head:

`fb91a65dc3bd92f49c7020ec856406df78bfc70a`

AutoPTU Python `main` inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest visible Python changes remain Career-oriented and do not justify changing the tactical capability map.

## New Java evidence since Pass 84

The current Java head adds a narrow but important field-state lifecycle slice:

- canonical field-effect entry types;
- field-effect kinds;
- semantic field-expiry events;
- global field status cleanup request;
- generic ROUND_START field progression;
- Python fixture extraction;
- parity tests and CI gate.

The commit explicitly introduces semantic expiry for canonical terrain, zone or room entries.

This is meaningful architecture for future battlefield environment state.

It does not demonstrate full terrain, weather, hazards, zones or reactions.

## Why the environment family remains BLOCKING

The permanent category is intentionally broad:

`terrain/weather/hazards/zones/reactions`

Pass 85 does not promote that family because the new evidence does not prove:

- creation/application of all field effects from Moves, Abilities, Items or Trainer Features;
- exact PTU behavior for named terrain/weather states;
- hazard damage or status application;
- zone entry/exit triggers;
- movement-cost changes;
- forced movement from field effects;
- reaction timing around zones;
- weather duration and interactions across the full library;
- field effect stacking/conflict rules;
- dynamic map changes;
- Minecraft -> server -> AutoPTU field initialization;
- complete semantic playback.

The new slice should be treated as lifecycle/state infrastructure inside a still-blocking family.

## AutoPTU-Java README boundary

The current README continues to list unfinished work for:

- core combatant/grid battle state expansion;
- full damage resolution pipeline;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic event emission and full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the anti-overclaim boundary.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

VERIFIED for implemented static geometric targeting.

Pass 85 guardrail:

Geometric LoS does not prove heat haze, glare, thermal vision, smoke/haze visibility, shade visibility or any perception modifier produced by urban microclimate.

### base movement legality

VERIFIED for implemented Shift/Jump and Overland/Swim/Sky surface.

Pass 85 guardrail:

A hot pavement, shaded arcade, cool courtyard, rooftop, fountain edge or exposed platform does not change movement legality unless an exact implemented rule says so.

### core calculations

VERIFIED for ported calculation primitives.

Pass 85 guardrail:

There is no generic `heat`, `shade`, `cool surface`, `urban canyon`, `water feature`, `tree canopy` or `thermal comfort` modifier.

### action economy/initiative

VERIFIED for the implemented initiative/action surface.

The new field ROUND_START progression does not change that classification.

Pass 85 guardrail:

Overworld survey windows, market schedules, cooling-center hours and heat alerts are world clocks, not combat initiative effects.

### AI legal-action infrastructure

VERIFIED for supported legal choices.

It does not provide policy goals such as:

- PROTECT_SENSOR;
- REACH_SHADE;
- EVACUATE_COURTYARD;
- REPAIR_RELAY;
- HOLD_SAMPLE_POINT;
- AVOID_HOT_ZONE;
- ESCORT_CIVILIAN;
- WITHDRAW_FROM_EXPOSED_AREA.

## PARTIAL

### full turn/round lifecycle

PARTIAL.

Java now has stronger ownership of battle RNG, delayed-hit lifecycle, phase/turn/round infrastructure and a generic ROUND_START field-progression slice.

It still does not prove every phase effect, duration, cleanup, switch/send-out path, delayed form, field interaction, reaction or transcript event.

### full stateful damage pipeline

PARTIAL.

Normal and delayed-hit paths increasingly derive state and resolve inside the battle core.

The README still declares full damage resolution incomplete.

Pass 85 guardrail:

Ambient heat, hot surfaces, equipment exhaust, sunlight, shade loss or cooling failure cannot cause HP damage unless a verified PTU mechanic produces it.

### status lifecycle

PARTIAL.

Selected status application, phase and expiry slices exist.

Pass 85 guardrail:

Heat cannot create Burned, Slowed, Confused, Tripped, Injured, Poisoned or any other Status from narrative description.

### move-specific behavior

PARTIAL.

Representative Move contracts and delayed-hit execution paths exist.

Pass 85 guardrail:

A Move that visually creates fire, sunlight, water, wind, shade or mist does not gain urban-thermal behavior unless that exact rule is implemented.

### abilities

PARTIAL.

Representative Ability hooks have parity evidence.

Pass 85 guardrail:

Fire-type flavor, Ice-type flavor, weather-related Abilities or species habitat do not create generic heat immunity or vulnerability.

### items

PARTIAL.

Representative held-item state/effects exist.

Pass 85 guardrail:

Fans, parasols, water bottles, cooling equipment, thermometers, awnings and survey instruments remain world-state assets unless validated as mechanical PTU Items.

### Trainer Features/perks

PARTIAL.

Representative Features and hook infrastructure exist.

Pass 85 guardrail:

Do not grant survival, medicine, endurance, technology or weather bonuses from profession flavor alone.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

BLOCKING as a family.

Pass 85 FULL encounters may need this for:

- protected survey routes;
- evacuation movement;
- chokepoints through crowds;
- intercepting actors carrying equipment;
- moving through service corridors;
- future field effects that displace combatants.

### terrain/weather/hazards/zones/reactions

BLOCKING as a family despite the new ROUND_START field-state progression slice.

Pass 85 FULL concepts may eventually need:

- validated heat or sunlight field effects;
- shaded/exposed zones;
- interactable cooling assets;
- temporary environmental zones;
- field-duration progression;
- reactions to entering/leaving a zone;
- weather interaction with urban surfaces.

The new Java commit proves only a reusable progression/expiry boundary for canonical field entries.

It does not authorize any of the effects above.

### AI tactical policy

BLOCKING.

Legal choices exist, but there is no verified scoring for thermal objectives, sensors, evacuation, cooling infrastructure, public-space protection or interactable relay goals.

### Minecraft/Cobblemon/Craftics adapter/playback

BLOCKING.

There is no verified end-to-end contract that converts server-owned urban thermal state into a legal AutoPTU battlefield field state and then replays semantic outcomes in Minecraft without duplicating PTU rules.

# Pass 85 encounter dependency summary

## Heat-Survey Station Interruption

REDUCED version can rely on:

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL if combat uses them:

- lifecycle;
- stateful damage;
- statuses;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

FULL blockers:

- complete movement/interception if actors move through protected routes;
- terrain/weather/hazards/zones/reactions for any tactical thermal field;
- AI tactical policy;
- adapter/playback.

## Cooling-Courtyard Access

REDUCED:

Evacuate noncombatants and resolve courtyard operations before battle. Use static geometry and ordinary combat.

FULL blockers:

- complete movement/interception;
- objective-aware AI;
- any validated zone/field behavior;
- adapter/playback.

## Night-Heat Relay Failure

REDUCED:

Investigation and relay manipulation remain overworld state. Combat uses a frozen rooftop/service map without heat penalties.

FULL blockers:

- interactable-object objective contract;
- tactical AI;
- field/environment mechanics if validated;
- adapter/playback.

# Pass 85 overworld blockers

These are outside the Java battle core and should not be solved inside it:

- URBAN_THERMAL_ZONE_STATE;
- THERMAL_OBSERVATION_PROVENANCE;
- SURFACE_VS_AIR_TEMPERATURE_MODEL;
- SHADE_ASSET_STATE;
- URBAN_CANOPY_THERMAL_LINK;
- WATER_THERMAL_LINK;
- ANTHROPOGENIC_HEAT_SOURCE_GRAPH;
- THERMAL_MITIGATION_PROJECT_HISTORY;
- THERMAL_SURVEY_TRANSECTS;
- THERMAL_EXPOSURE_PRIVACY;
- URBAN_HEAT_TO_PUBLIC_SPACE;
- URBAN_HEAT_TO_ENERGY;
- URBAN_HEAT_TO_HEALTH_SURVEILLANCE;
- URBAN_HEAT_TO_COBBLEMON;
- URBAN_HEAT_TO_BATTLE_SNAPSHOT.

# Specific no-inference rules

Do not infer:

- hot Minecraft blocks -> PTU heat damage;
- sunny weather -> urban heat island;
- urban heat island -> Sunny Day;
- tree canopy -> cover/evasion bonus;
- fountain -> healing/cooling bonus;
- Fire type -> ambient heat immunity;
- Ice type -> ambient heat weakness;
- dark roof -> damage zone;
- cooled building -> HP recovery;
- thermal observation -> medical diagnosis;
- heat survey -> Weather mechanics;
- field ROUND_START infrastructure -> complete terrain/weather/hazard implementation.

# Open mechanical questions

1. Which PTU/Caelo rules, if any, define extreme heat exposure outside ordinary Weather?
2. How do Sunny Day / harsh sunlight semantics map into current Python and future Java?
3. Are there explicit Items/Features for environmental heat, hydration or protective equipment?
4. Which field effects are represented by the new Java `FieldEffectKind` contract, and which exact behaviors are still missing?
5. How will a future adapter initialize validated Weather/Terrain/Zone state from a frozen world snapshot?
6. How should semantic field-expiry events be rendered without Minecraft owning duration logic?

# Open canon questions

1. Which Ouros settlements have persistent thermal patterns before player intervention?
2. Which institutions collect local heat observations?
3. Which regions use canopy, shade structures, water or building retrofits as normal practice?
4. How much thermal state advances while chunks are unloaded?
5. Which Pokémon have authored urban-thermal behavior in each region?
6. What public/private boundaries apply to health-linked exposure records?
7. How much player construction can alter a thermal zone before the server recomputes its coarse state?

Until these are resolved, thermal gameplay should prefer observation, scheduling, infrastructure, ecology and public-space decisions over invented combat penalties.
