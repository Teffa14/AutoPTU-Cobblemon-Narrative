# Engine Readiness Snapshot — Pass 77

Status: implementation evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`2ca88352fbf5ca4d07bd795c49533dc26c41f5c6`

Latest visible commit:

`Add canonical initiative rollover rebuilder (#111)`

Parent inspected in Pass 76:

`becdfc6f7f8130c38d4e0834c49041c94aa0b5de`

The new slice adds an authoritative `InitiativeRoundRebuilder` implementation that composes already parity-tested runtime projection, initiative assembly, cleanup and installation directly from server-owned `BattleRuntimeState`. The implementation rejects mismatched rounds and does not accept a precomputed initiative order from Minecraft/Cobblemon.

AutoPTU Python oracle inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its latest visible commit remains Career-oriented (`Career: make roster recovery deterministic`) and does not change the tactical classification below.

## What the new Java slice proves

The new initiative rollover slice provides stronger evidence that:

- initiative round rebuild is server authoritative;
- initiative assembly can be reconstructed from canonical battle state;
- cleanup/install ordering is part of the battle core;
- Minecraft/Cobblemon should not supply initiative order during rollover;
- action economy/initiative remains a robust VERIFIED family.

It does not prove:

- all START/END lifecycle behavior;
- complete status expiry;
- full damage pipeline;
- complete Weather/Terrain application or duration;
- hazards/zones;
- visibility/smoke/gas mechanics;
- forced movement/interception;
- tactical AI;
- Minecraft adapter/playback.

## Java README boundary

The current AutoPTU-Java README still explicitly lists these major areas as unfinished:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- full status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the primary no-overclaim guardrail.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

Range, areas, footprints, target anchors and geometric line of sight remain documented complete for the ported surface.

Pass 77 guardrail:

Geometric LoS does not establish atmospheric visibility. Haze, smoke, dust and gas cannot shorten LoS or modify Accuracy without a separate verified visibility/environment rule.

### base movement legality

Shift movement for Overland/Swim/Sky, terrain costs, blockers, Wallrunner, sprint, landing-fit and Jump foundations remain implemented according to the current README.

Atmospheric conditions do not modify those movement rules unless a verified PTU environment mechanic says so.

### core calculations

Representative PTU tables and primitives remain implemented: Damage Base, type steps, stages, accuracy, crit, Burn, weather DB and modifier/rounding primitives.

A weather DB primitive does not prove environmental atmosphere mechanics.

### action economy/initiative

VERIFIED and strengthened in Pass 77.

Current evidence includes typed turn flow, deterministic initiative ordering, runtime-derived initiative entries/order modes and now a canonical round-rollover rebuilder that derives, cleans and installs the new order from `BattleRuntimeState`.

No promotion of full lifecycle follows from this.

### AI legal-action infrastructure

The deterministic legal `BattleChoice` surface remains implemented for currently supported actions/targets/movement/action-budget filtering.

It does not establish tactical choice quality or air-hazard awareness.

## PARTIAL

### full turn/round lifecycle

The port has substantial phase, round, initiative, cleanup and effect-hook infrastructure. The repository still does not claim complete lifecycle or BattleSpec -> BattleTranscript parity.

### full stateful damage pipeline

Selected accuracy/damage/post-damage slices exist, but the README continues to list full damage resolution as unfinished.

### status lifecycle

Specific status application/phase/expiry behavior has parity evidence. The complete status controller remains unfinished.

Pass 77 guardrail:

Existing Poisoned behavior does not establish environmental toxic exposure.

### move-specific behavior

Move metadata/contracts and selected behaviors exist. The full Move library is not ported.

Pass 77 guardrail:

Even if `Poison Gas` is or becomes implemented as a Move, that does not make regional air pollution equivalent to that Move.

### abilities

Multiple Ability hook families and representatives exist with parity tests. Full coverage is not demonstrated.

Pass 77 guardrail:

A battle Ability such as Neutralizing Gas, Overcoat or a selected Poison interaction cannot be generalized into an overworld atmospheric simulation.

### items

Representative item state/effects exist. Full item behavior remains incomplete.

### Trainer Features/perks

Trainer runtime state, hook infrastructure and multiple representative Features exist. Full Class/Feature/Edge/Order coverage is not demonstrated.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

The README still lists forced movement/reactions as unfinished. Any encounter where a plume pushes actors, evacuation lines require interception or atmospheric forces move combatants remains blocked.

### terrain/weather/hazards/zones/reactions

Still BLOCKING as a family.

Canonical `BattleEnvironmentState` contains semantic Weather/Terrain data and some calculations consume those inputs, but complete Terrain, Weather, hazard, zone and reaction behavior is not established.

Pass 77 specifically requires this category for any attempt to model:

- toxic gas zones;
- smoke zones;
- dust zones;
- visibility zones;
- atmospheric damage;
- dynamic plume movement;
- environmental status application;
- changing safe-air areas.

Until verified, atmospheric conditions remain world state/presentation outside battle.

### AI tactical policy

Legal actions exist. Scoring/policy remains explicitly unfinished. AI cannot yet be assumed to understand evacuation, safe-air zones, plume avoidance, environmental objectives or monitor protection.

### Minecraft/Cobblemon/Craftics adapter/playback support

Still BLOCKING. The Java repository states it is not a Minecraft mod yet and plans adapter integration after a parity-safe slice.

Minecraft must not decide PTU air effects.

# Air-quality-specific engine boundary

Available Python evidence contains real combat behavior for Poisoned/Badly Poisoned and selected Ability/Feature interactions.

Available prior Caelo evidence contains at least one explicitly authored location effect involving Poison Gas and Poisoned.

That proves the following narrow principle:

An atmosphere may have PTU mechanical consequences when the authoritative rule/location definition explicitly defines them.

It does not prove a generic subsystem for:

- air-quality indices;
- smoke exposure;
- industrial emissions;
- volcanic gas exposure;
- dust inhalation;
- biological aerosols;
- atmospheric source attribution;
- pollutant transport;
- deposition;
- visibility loss;
- respiration/suffocation;
- Poison-type environmental immunity;
- air purification by Galarian Weezing;
- atmospheric monitoring.

# Pass 77 encounter dependencies

## Monitor Ridge Retrieval — FULL

Required capability families:

- targeting/footprints/range/LoS — VERIFIED for geometry only;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING if moving evacuation/wildlife routes enter combat;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for smoke/visibility/exposure effects;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version gate:

Resolve plume position, monitor outage, visibility and travel in overworld state. If combat occurs, start it on a static validated arena after arrival. No smoke damage, haze Accuracy modifier or moving plume exists in AutoPTU.

## Filter House Alarm — FULL

Required:

- targeting — VERIFIED;
- base movement — VERIFIED;
- complete movement — BLOCKING for evacuation/interception;
- core calculations — VERIFIED;
- initiative — VERIFIED;
- lifecycle — PARTIAL;
- damage — PARTIAL;
- statuses — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for unsafe-air zones/dynamic ventilation;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal actions — VERIFIED;
- tactical AI — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version gate:

Facility fault, technicians, ventilation and atmospheric investigation remain world state. Any combat uses a static clean/validated space. No gas mechanic is inferred.

## Haze Over the Marsh — FULL

Required:

- targeting/range/LoS — VERIFIED geometrically, not atmospherically;
- base movement — VERIFIED;
- complete movement/interception — BLOCKING if wildlife movement becomes tactical;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL;
- damage/statuses — PARTIAL where normal battle mechanics require them;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move/ability/item/Feature behavior — PARTIAL;
- AI legal actions — VERIFIED;
- tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version gate:

Sampling, source attribution and ecological observations remain outside battle. A discrete confrontation can use a standard static arena with no haze modifier.

# Pass 77 overworld blockers

These are separate from AutoPTU-Java's battle-core families.

`ATMOSPHERIC_REGION_STATE` — BLOCKING.

`AIR_QUALITY_EPISODE_GRAPH` — BLOCKING.

`ATMOSPHERIC_SOURCE_EVENT_STATE` — BLOCKING.

`PLUME_REVISION_STATE` — BLOCKING.

`AIR_MONITOR_NETWORK` — BLOCKING.

`AIR_OBSERVATION_PROVENANCE` — BLOCKING.

`SOURCE_ATTRIBUTION_GRAPH` — BLOCKING.

`AIR_ADVISORY_STATE` — BLOCKING.

`ATMOSPHERIC_EXPOSURE_STATE` — BLOCKING.

`ATMOSPHERIC_DEPOSITION_STATE` — BLOCKING.

`AIR_QUALITY_TO_METEOROLOGY_CONTRACT` — BLOCKING.

`AIR_QUALITY_TO_HEALTH_SURVEILLANCE_CONTRACT` — BLOCKING.

`AIR_QUALITY_TO_SOIL_FRESHWATER_FLORA_CONTRACT` — BLOCKING.

`AIR_QUALITY_TO_COBBLEMON_PROJECTION` — BLOCKING.

`AIR_QUALITY_TO_BATTLE_SNAPSHOT` — BLOCKING.

# No-inference rules for future agents

Do not promote full lifecycle because initiative rollover is now canonical.

Do not promote terrain/weather/hazards/zones/reactions because environment state stores Weather/Terrain.

Do not treat geometric LoS as atmospheric visibility.

Do not map haze to Accuracy.

Do not map smoke to damage.

Do not map pollution to Poisoned.

Do not infer Poison/Steel environmental immunity from a specific Caelo Poison Gas rule unless that exact rule governs the encounter.

Do not infer Galarian Weezing purification mechanics from Pokédex lore.

Do not infer Koffing as the cause of a gas episode solely from presence.

Do not let Minecraft particles, fog or sky color become battle-authoritative.

Do not infer an atmospheric source from one monitor reading.

Do not infer illness from atmospheric exposure.

# PTU/Caelo extraction gate

Before a mechanically active atmospheric encounter is promoted, extract and lock exact governing text for any relevant:

- environmental Poison Gas effects;
- Poisoned / Badly Poisoned;
- Poison-type and Steel-type immunity where the specific rule states it;
- smoke/gas rules if present;
- suffocation/respiration rules if present;
- Blinded/Accuracy/visibility rules if present;
- Overcoat or indirect-effect protection if relevant;
- Weather interactions;
- Moves/Abilities/Capabilities/Trainer Features used to generate, remove or resist atmospheric effects.

Until those texts and Java parity exist, the REDUCED encounter versions are the executable design target.
