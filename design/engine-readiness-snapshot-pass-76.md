# Engine Readiness Snapshot — Pass 76

Status: implementation evidence snapshot for narrative dependency planning. This document does not change AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`becdfc6f7f8130c38d4e0834c49041c94aa0b5de`

Latest visible commit:

`Derive initiative ordering modes from canonical state`

The two newest initiative slices since Pass 75 are:

- `02574de120c546ba49c771e56937344e60e9b80b` — assemble initiative entries from authoritative runtime state, including canonical Trainers without a bound Pokémon;
- `becdfc6f7f8130c38d4e0834c49041c94aa0b5de` — store Trick Room and League ordering modes in canonical `BattleEnvironmentState` and derive initiative ordering from that state.

AutoPTU Python oracle inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its most recent visible changes remain Career-oriented and do not change the tactical capability classification below.

## Important new Java evidence

The current Java head moves another initiative decision under battle-core authority.

`BattleEnvironmentState` now stores:

- Weather string;
- Terrain name;
- Tailwind teams;
- grounded state;
- mounted pairs;
- Trick Room ordering mode;
- League battle ordering mode.

`RuntimeInitiativeOrderAssembly.fromState(state)` now derives ordering modes from canonical runtime/environment state instead of accepting those values ad hoc from a renderer/controller boundary.

This is meaningful architecture progress because Minecraft/Cobblemon should not determine initiative ordering.

It does not prove:

- full turn/round lifecycle;
- complete Weather behavior;
- complete Terrain behavior;
- vertical/elevation combat;
- flight-route state;
- passenger flight;
- aerial collision/interception;
- full Trainer Feature coverage;
- tactical AI.

## Permanent capability categories

### VERIFIED

`targeting/footprints/range/LoS`

Representative geometry, anchors, range, areas, footprints and line-of-sight are documented complete in the current Java README.

Guardrail for Pass 76: geometric LoS does not equal visibility through cloud/fog, altitude-aware sight, aerial observation coverage or overworld line-of-sight.

`base movement legality`

Current Java README marks Shift movement for Overland/Swim/Sky, terrain cost, blockers, Wallrunner, sprint, landing-fit, plus Jump movement as implemented.

Guardrail: Sky movement legality does not prove passenger transport, carrying capacity, endurance, long-range flight or multi-altitude tactical space.

`core calculations`

Damage Base tables, type effectiveness, stages, accuracy primitives, weather DB, crit primitives, Burn and modifier/rounding primitives have representative parity-backed implementation.

`action economy/initiative`

This category remains VERIFIED and has become more server-authoritative during the latest slices. Typed turn flow, deterministic ordering, Trick Room/League ordering and current runtime-derived initiative assembly are present.

`AI legal-action infrastructure`

The deterministic legal action-space contract remains implemented for the currently supported Shift/targeting/action-budget surfaces.

### PARTIAL

`full turn/round lifecycle`

Substantial lifecycle infrastructure exists, including phases, round transitions, state cleanup, initiative turns and multiple status/Ability/Feature hooks. The repository still does not claim complete BattleSpec → BattleTranscript lifecycle parity.

`full stateful damage pipeline`

Several pieces and post-damage Ability hooks exist, but the Java README still lists full damage resolution as unfinished.

`status lifecycle`

There are verified slices for specific statuses and status-phase infrastructure. The full controller remains unfinished.

`move-specific behavior`

The port has move metadata/contracts and selected behavior. The complete PTU Move library is not implemented.

`abilities`

Multiple representative Abilities and hook families are implemented with parity tests. This does not establish full Ability coverage.

`items`

Representative held-item state/effects exist. Complete item behavior remains incomplete.

`Trainer Features/perks`

Java has Trainer runtime state, lifecycle/perk hook infrastructure, Defense Mastery, Link Feature slices, Rider initiative-related slices and other representatives. Full class/Feature/Edge/Order coverage is not demonstrated.

### BLOCKING

`complete movement including push/pull/knockback/interception/forced movement`

Current README still identifies forced movement and reactions as unfinished. Aerial encounter concepts requiring interception, falling displacement, wind displacement or movement between altitude layers must remain blocked.

`terrain/weather/hazards/zones/reactions`

Canonical semantic environment state now exists and some calculations consume it. The README still lists terrain, hazards and reactions as unfinished. This category remains BLOCKING as a complete family.

For Pass 76 specifically, a Weather string in `BattleEnvironmentState` does not prove clouds, wind corridors, turbulence, aerial hazards, visibility, route closures or Weather duration/application.

`AI tactical policy`

Legal choices exist, but scoring/policy over those choices remains explicitly unfinished.

`Minecraft/Cobblemon/Craftics adapter/playback support`

The repository still says it is not a Minecraft mod yet. The adapter is planned after a parity-safe vertical slice.

## Aerial-specific engine boundary

The Python oracle contains explicit `sky`/`levitate` movement concepts and available evidence includes a `can_fly()` path. It also contains Feature behavior such as Celerity requiring Flying type or Sky/Levitate movement.

This is battle evidence only.

No inspected Java or Python evidence establishes a general authoritative subsystem for:

- overworld airspace regions;
- passenger flight eligibility;
- cargo capacity;
- long-distance flight endurance;
- route schedules;
- migratory flyways;
- altitude bands outside tactical movement;
- aerial traffic conflict;
- wildlife/transport collision rules;
- aircraft/airship physics;
- overworld weather-safe flight;
- true 3D battle layers.

## Pass 76 encounter dependencies

### Ridge Approach Interruption — FULL

Required:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- abilities — PARTIAL if species mechanics are required;
- Trainer Features/perks — PARTIAL if used;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version gate:

Resolve corridor use and service approach in world state. Run only actual combatants on a static legal arena. No altitude/wind/interception mechanics.

### Beacon Ridge Night Watch — FULL

Required:

- targeting/LoS — VERIFIED, but not darkness/visibility;
- base movement — VERIFIED;
- complete movement — BLOCKING for aerial displacement/interception;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL if tools affect battle;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version gate:

Beacon repair, night visibility and technicians remain overworld state. Battle receives static geometry with no invented darkness penalties.

### Migration Corridor Survey — FULL

Required:

- targeting/footprints/range/LoS — VERIFIED;
- base movement — VERIFIED;
- complete movement/interception — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full damage — PARTIAL;
- statuses — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version gate:

Migration traffic remains out of battle. AutoPTU resolves only the discrete conflict with actual combatants.

## Overworld blockers added by Pass 76

These are not battle-core responsibilities:

`AIRSPACE_REGION_STATE` — BLOCKING.

`AIR_CORRIDOR_GRAPH` — BLOCKING.

`AERIAL_SERVICE_OPERATION` — BLOCKING.

`AERIAL_PASSENGER_ELIGIBILITY` — BLOCKING pending PTU/Caelo rules and server authority design.

`MIGRATION_FLYWAY_STATE` — BLOCKING.

`AERIAL_STOPOVER_STATE` — BLOCKING.

`AERIAL_OBSERVATION_COVERAGE` — BLOCKING.

`AERIAL_INCIDENT_HISTORY` — BLOCKING.

`AERIAL_NAVIGATION_AIDS` — BLOCKING.

`AIRSPACE_TO_COBBLEMON_PROJECTION` — BLOCKING.

`AIRSPACE_TO_BATTLE_SNAPSHOT` — BLOCKING.

## Caelo/PTU evidence gate

Available project/file evidence previously recovered from Caelo defines a battle-oriented sky limit and states that the same rule applies to Levitate. The available Python oracle provides tactical Sky movement and specific feature/capability interactions.

That evidence does not answer the major overworld questions.

Before personal Pokémon flight becomes executable, extract and lock the exact governing text for:

- Sky movement;
- Levitate movement;
- Mountable/passenger interaction;
- falling;
- carrying/weight if relevant;
- Rider/Flying-related Trainer Features;
- weather interactions;
- any Caelo-specific modifications.

## No-inference rules for future agents

Do not promote `terrain/weather/hazards/zones/reactions` because `BattleEnvironmentState` stores Weather/Terrain.

Do not promote `full lifecycle` because initiative is increasingly complete.

Do not promote `Trainer Features/perks` because some Rider/initiative features have parity.

Do not infer long-range flight from Sky movement.

Do not infer 3D combat from Sky movement legality.

Do not infer passenger capacity from Flying type, size, Sky speed or species appearance.

Do not let Minecraft decide initiative, altitude legality, Weather effects or flight capability.
