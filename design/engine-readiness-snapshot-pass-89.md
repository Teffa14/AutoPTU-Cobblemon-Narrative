# Engine Readiness Snapshot — Pass 89

Status: implementation-evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`a2931ccc3dd37119a94445f44fb833c755d311c1`

Latest visible commit:

`Freeze delayed target binding contract`

AutoPTU Python `main` inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible Python changes remain Career-oriented and do not justify tactical capability promotions.

## New Java evidence since Pass 88

Pass 88 inspected Java at:

`f4a5232b406fe0c80137e4d1d2f8408771ab4ba0`

The new Java head adds a stricter delayed-hit targeting contract backed by the pinned Python oracle.

Current evidence shows that:
- due delayed hits continue through target resolution and then the normal Move-action resolver;
- stored target id and target position are forwarded through the delayed-hit boundary;
- target position does not automatically rewrite the Move into Tile targeting;
- when both a target id and target position exist, the combatant target identity remains authoritative while the stored target anchor can remain relevant;
- Java parity tests fail closed when canonical state cannot resolve required Move/target information.

This is meaningful evidence for `full turn/round lifecycle` and `move-specific behavior`, with some indirect support for the stateful attack-resolution path.

It does not implement island ecology, migration, group movement, open-ocean travel, stepping-stone behavior, escape policy, population simulation, terrain/weather behavior or Minecraft playback.

## AutoPTU-Java README boundary

Current Java README still lists as unfinished:
- broader core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic battle-event/transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the anti-overclaim boundary.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

VERIFIED for implemented static tactical geometry.

Pass 89 guardrail:

Geometric LoS does not prove:
- visibility between islands;
- spotting range at sea;
- visibility through weather/haze;
- detection of migrating groups;
- survey effectiveness;
- knowledge that another island population exists.

### base movement legality

VERIFIED for implemented Shift/Jump and supported Overland/Swim/Sky surface contracts.

Pass 89 guardrail:

Battle movement values do not prove long-distance dispersal or travel capability.

Do not infer:
- Sky movement -> can fly between islands;
- Swim movement -> can cross open-ocean channels;
- Jump -> cliff/island traversal;
- Wallrunner -> volcanic/cliff travel;
- loaded movement mode -> seasonal migration endurance.

### core calculations

VERIFIED for ported calculation primitives.

Pass 89 guardrail:

There is no generic calculation for:
- island isolation;
- colonization probability;
- local extinction;
- stepping-stone importance;
- endemism;
- dispersal distance;
- island rarity;
- population persistence.

### action economy/initiative

VERIFIED for the implemented action/initiative surface.

Pass 89 guardrail:

Inter-island migration and colonization are world-state processes. They do not consume battle actions unless a specific tactical encounter explicitly represents one local step.

### AI legal-action infrastructure

VERIFIED for supported legal choices.

It does not provide tactical goals such as:
- CROSS_CHANNEL;
- REACH_SHORE;
- WITHDRAW_TO_SEA;
- PROTECT_STEPPING_STONE;
- ESCORT_MIGRATING_GROUP;
- AVOID_RESEARCH_TEAM;
- LEAVE_ISLAND;
- REACH_ROOST;
- RETREAT_FROM_CAPTURE_PRESSURE.

## PARTIAL

### full turn/round lifecycle

PARTIAL.

Java now includes substantial authoritative round/phase state, initiative rollover, delayed-hit execution infrastructure, field progression and cleanup paths.

The new delayed-hit target-binding contract strengthens this category.

It still does not prove every:
- phase trigger;
- duration;
- switch/send-out case;
- delayed effect;
- reaction;
- field interaction;
- status interaction;
- transcript event.

### full stateful damage pipeline

PARTIAL.

Normal and delayed-hit execution increasingly use authoritative runtime state and verified hooks.

Pass 89 guardrail:

Island conditions cannot produce damage through narrative labels.

No automatic damage from:
- surf;
- waves;
- reefs;
- cliffs;
- storms;
- exhaustion from dispersal;
- exposure during channel crossing;
- crowding at roosts;
- territorial pressure.

### status lifecycle

PARTIAL.

Representative application/phase/expiry slices exist.

Pass 89 guardrail:

Island context cannot create:
- Slowed;
- Tripped;
- Stuck;
- Confused;
- Injured;
- Burned;
- Poisoned;
- any other Status.

### terrain/weather/hazards/zones/reactions — still BLOCKING overall

See BLOCKING section below. Field-state lifecycle infrastructure exists, but it is insufficient for promotion.

### move-specific behavior

PARTIAL.

Representative Move contracts exist, including increasingly precise delayed-hit behavior.

Pass 89 guardrail:

Any Move relied on for:
- travel;
- forced movement;
- weather manipulation;
- terrain creation;
- rescue;
- teleportation;
- water crossing;
- flight;
- relocation;
requires individual verification.

### abilities

PARTIAL.

Representative Ability hooks have parity evidence.

Pass 89 guardrail:

Do not generalize Ability names or species flavor into dispersal rules.

Examples of invalid inference:
- Levitate -> cross-ocean travel;
- Swift Swim -> long-distance marine migration;
- Run Away -> tactical withdrawal policy;
- Drizzle -> creates regional island climate;
- Drought -> creates regional aridity;
- Storm Drain -> controls currents;
- Pressure -> population pressure;
- Dancer -> ecological island differentiation.

### items

PARTIAL.

Representative held-item behavior exists.

Pass 89 guardrail:

Maps, tags, field notebooks, transmitters, sample containers, ferries, research boats and survey equipment remain world-state assets unless they correspond to a verified PTU Item effect.

### Trainer Features/perks

PARTIAL.

Representative Feature infrastructure and concrete slices exist.

Pass 89 guardrail:

Survival/navigation/ecology expertise does not grant automatic inter-island travel, perfect surveys or movement immunity without exact PTU/Caelo text and Java parity.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

BLOCKING as a family.

Full island encounters may need:
- crossing movement;
- interception near shorelines;
- escorting moving groups;
- retreat/escape routes;
- forced movement from waves/wind if mechanically valid;
- rescue from edges;
- multi-stage movement between land/water surfaces.

Base movement does not authorize these mechanics.

### terrain/weather/hazards/zones/reactions

BLOCKING as a family despite canonical field-state progression infrastructure.

Current evidence proves storage/progression/expiry wiring for some semantic field entries.

It does not prove:
- complete Weather lifecycle;
- coastal surf zones;
- changing tides;
- wind corridors;
- reef hazards;
- island-specific terrain;
- channel-current mechanics;
- entry/exit reactions;
- dynamic shoreline transitions;
- stepping-stone zones;
- Minecraft initialization of an island/environment snapshot.

### AI tactical policy

BLOCKING.

Legal choices exist. Verified tactical policy does not yet exist for:
- withdrawal;
- migration;
- crossing;
- roost seeking;
- protecting young/site use;
- avoiding disturbance;
- escape instead of KO;
- escorting a group through a chokepoint.

### Minecraft/Cobblemon/Craftics adapter/playback

BLOCKING.

There is no verified end-to-end contract for:

persistent archipelago population state
-> selected Minecraft/Cobblemon entities
-> frozen AutoPTU encounter snapshot
-> semantic battle transcript
-> ecological/world-state writeback.

Loaded Cobblemon entities must not become the population census.

# Pass 89 encounter dependency summary

## Stepping-Stone Survey

Reduced version can run using static battle capabilities after overworld survey/migration resolution.

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL if normal battle effects invoke them:
- full turn/round lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING for full version:
- complete movement if groups move through the arena;
- terrain/weather/hazards/zones/reactions if coastal conditions matter;
- AI tactical policy for WITHDRAW/REACH_EXIT/PROTECT_SITE;
- Minecraft/Cobblemon/Craftics adapter/playback.

## Recolonization Shore

Reduced version:
- population observation and endemism/establishment inference remain world state;
- battle uses static legal geometry only when a confrontation actually occurs.

Full version additionally needs:
- complete movement for escape/withdrawal;
- AI tactical policy that can prefer leaving to KO;
- terrain/weather/hazards/zones/reactions if shoreline state matters;
- adapter/playback.

## Channel Crossing Window

Reduced version:
- Seasonality/Open Ocean decides whether the crossing window exists;
- crossing occurs outside battle;
- any battle is a frozen snapshot on one side of the channel.

Full version additionally needs:
- complete movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy for CROSS/WITHDRAW/PROTECT;
- adapter/playback.

# New overworld blockers for Pass 89

These are outside the Java battle core and should not be implemented there:

- `ARCHIPELAGO_ECOLOGY_GRAPH`
- `ISLAND_HABITAT_MOSAIC_STATE`
- `ISLAND_SURVEY_EFFORT_LEDGER`
- `POPULATION_OCCUPANCY_HISTORY`
- `COLONIZATION_RECOLONIZATION_CASE_GRAPH`
- `LOCAL_EXTIRPATION_ASSESSMENT`
- `ENDEMISM_ASSESSMENT`
- `STEPPING_STONE_FUNCTION_STATE`
- `DISPERSAL_PATHWAY_HYPOTHESES`
- `ISLAND_POPULATION_DIFFERENTIATION_CLAIMS`
- `ISLAND_ECOLOGY_TO_COBBLEMON_PROJECTION`
- `ISLAND_ECOLOGY_TO_BATTLE_SNAPSHOT`

# Live-head conclusion

The new Java head strengthens delayed-hit target semantics and keeps the adapter from inventing its own delayed target behavior.

That is valuable engine progress.

It does not reduce any of the main blockers for island biogeography.

The permanent classification therefore remains:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

# PTU/Caelo validation debt

Before island encounters rely on them, extract and verify exact rules for:
- Sky;
- Swim;
- Mountable;
- Naturewalk;
- Teleporter;
- movement between water/land surfaces;
- escape/withdrawal;
- capture/release;
- relocation/translocation;
- Survival/navigation;
- Weather/Terrain interactions.

The complete primary Caelo corpus was not reliably accessible in this runtime. No Caelo-specific island mechanic is claimed.