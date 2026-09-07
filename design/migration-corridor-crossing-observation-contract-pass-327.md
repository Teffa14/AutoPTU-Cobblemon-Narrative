# Migration corridor & crossing observation contract — Pass 327

Status: DESIGN / IMPLEMENTATION-FACING
Date: 2026-09-07
Canon effect: NONE. This contract governs representation of proposed content; it does not establish a specific Ouros location or species.

## Purpose

Represent seasonal population movement across persistent landscapes without treating Minecraft pathfinding, spawn location, one sighting or infrastructure completion as omniscient ecological truth.

The contract separates physical connectivity, temporal movement state, observations, NPC knowledge, institutional decisions and tactical execution.

## Core invariants

`POPULATION_PRESENT != POPULATION_MIGRATING`

`CORRIDOR_EXISTS != CORRIDOR_CURRENTLY_USED`

`CROSSING_OPEN != CROSSING_USED`

`CROSSING_USED != CROSSING_SUFFICIENT_FOR_POPULATION`

`FAILED_APPROACH != CROSSING_STRUCTURE_FAILURE`

`ONE_SUBGROUP_OBSERVED != WHOLE_POPULATION_STATE`

`MINECRAFT_PATHFINDING != ECOLOGICAL_AUTHORITY`

## Authoritative layers

### 1. Population identity

A persistent ecological population or authored subgroup may have a stable ID. It must not be inferred merely because several nearby Pokémon share species.

Example fields:
- population ID;
- species identity when canon-approved;
- seasonal habitat relationships;
- known subgroup identity if evidence exists;
- provenance for population classification.

### 2. Corridor segment

A corridor is an authored spatial relationship among habitat features. It can contain barrier segments, approaches, stopovers and crossing structures.

Suggested fields:
- corridor ID;
- segment IDs;
- endpoint habitat IDs;
- stopover IDs;
- barrier feature IDs;
- crossing feature IDs;
- current physical state;
- history lineage.

A corridor should not be reduced to one path spline when several routes remain plausible.

### 3. Temporal movement window

Movement relevance changes with semantic time.

Suggested values may include:
- `EXPECTED`
- `ACTIVE`
- `LATE_RELATIVE_TO_BASELINE`
- `EARLY_RELATIVE_TO_BASELINE`
- `COMPLETED`
- `UNRESOLVED`

These are world-state descriptors and do not create PTU bonuses, Initiative effects or encounter rates.

### 4. Crossing physical state

Represent infrastructure condition separately from observed ecological use.

Examples:
- `OPEN`
- `RESTRICTED`
- `MAINTENANCE_ONLY`
- `BLOCKED`
- `CONDITION_UNRESOLVED`

Approach features, fencing, drainage, vegetation and nearby disturbance can each have independent state.

### 5. Observation

Every ecological claim entering NPC knowledge should derive from an observation or received report with provenance.

Useful observation kinds:
- successful crossing observed;
- approach without crossing observed;
- attempted crossing observed;
- road-surface presence observed;
- stopover occupancy observed;
- tracks/sign observed with source unresolved;
- maintenance completion observed or recorded;
- crossing obstruction observed;
- changed approach habitat observed;
- no observation during a defined watch window.

Absence of observation is not automatic evidence of absence.

Minimum provenance:
- observation ID;
- feature or population scope;
- semantic time/window;
- observer or source;
- method/channel;
- confidence or uncertainty notes;
- parent record if relayed;
- whether a later event can make it stale.

### 6. Actor receipt and belief

Use the existing global NPC memory/communication contracts.

A ranger receiving a driver report learns that the driver reported an observation. The ranger does not automatically gain direct sensory evidence.

A maintenance worker knowing that the underpass is structurally clear does not automatically know that a migrating population used it.

A public notice does not imply universal receipt or belief.

### 7. Institutional decision

Road operators, habitat stewards, researchers or local authorities may make feature-scoped decisions using an explicit evidence set.

Examples:
- temporary reduced-speed window;
- observation shift added;
- one maintenance activity deferred;
- one approach restored;
- stopover access restricted to people;
- crossing left unchanged pending evidence;
- follow-up review scheduled.

Each decision preserves:
- decision ID;
- authority/actor;
- evidence references;
- feature/population scope;
- semantic time;
- obligations created;
- review condition;
- later revision lineage.

### 8. Consequence

Consequences should modify actual world features or obligations rather than rewrite ecological history.

Examples:
- route schedule change;
- maintenance task creation;
- observation coverage increase;
- changed public notice;
- approach restoration work;
- later migration evidence;
- institutional trust/reputation change when supported by existing systems.

### 9. AutoPTU handoff

World-level migration reasoning ends before tactical resolution.

When structured battle mechanics are required, issue the existing explicit `REQUEST_AUTOPTU` handoff with only admitted world facts.

The handoff may include static map geometry, participant identity, ordinary route obstacles and an objective description only where current AutoPTU contracts can legally express them.

The world planner must not simulate missing PTU rules while AutoPTU is authoritative.

### 10. Minecraft / Cobblemon / Craftics presentation

The adapter may present:
- visible Pokémon groups;
- crossings and fences;
- road traffic;
- tracks or signs;
- NPC observers;
- notices and maintenance work;
- admitted semantic events.

Presentation cannot decide:
- migration status;
- population identity;
- crossing success counts;
- route legality;
- PTU movement legality;
- damage/status outcomes;
- NPC knowledge;
- causal explanation.

## Reduced implementation contract

The reduced version uses semantic-time authored movement events.

A simple loop can operate with:
- persistent corridor/crossing IDs;
- explicit physical state;
- observation records;
- NPC receipt through existing communication systems;
- decisions and obligations;
- later revisits that add new evidence.

No continuous animal path simulation is required.

If tactical combat occurs, keep the map static and use ordinary verified targeting, movement, calculations and action economy only.

## Rich implementation dependency map

### Targeting / footprints / range / LoS

Ordinary static targeting is usable within verified contracts. Vegetation occlusion, darkness, dust, fog, traffic or species-specific sensing requires exact additional evidence.

### Base movement legality

Ordinary authored walkable terrain is usable within verified contracts. Crossing slopes, squeezing, climbing, jumping, swimming or specialist traversal require exact rules/implementation evidence.

### Complete movement including push/pull/knockback/interception/forced movement

Required for traffic displacement, panicked forced movement, rescue/interception, knockback near road edges or moving-barrier interactions.

### Core calculations

Ordinary deterministic battle arithmetic is usable. No migration probability, crossing score or collision formula is introduced here.

### Action economy / initiative

Ordinary supported combat actions are usable. Observation, traffic control and infrastructure work remain world-level activities unless separately implemented.

### Full turn / round lifecycle

Required for timed gate cycles, changing traffic windows, delayed barrier movement, scheduled hazard changes or environmental phases inside tactical time.

### Full stateful damage pipeline

Required for any vehicle collision, falling, crushing or environmental damage.

### Status lifecycle

Required for any persistent PTU condition. `MIGRATION_WINDOW_ACTIVE`, `FAILED_APPROACH_OBSERVED` and related values are world states, never battle statuses.

### Terrain / weather / hazards / zones / reactions

Required for dynamic road hazards, moving vehicles as hazard zones, weather-driven corridor changes, reactive closures, escape windows or environmental reactions.

### Move-specific behavior

Every Move remains individually gated.

### Abilities

Every Ability remains individually gated. Species flavor cannot create migration bonuses or hazard immunity.

### Items

Tracking tags, signs, gates, cameras or instruments may exist narratively. Mechanical item effects require exact support.

### Trainer Features / perks

Research, tracking, survival, ranger-like or technical effects require exact project-authoritative validation.

### AI legal-action infrastructure

Ordinary supported legal actions may be enumerated. Custom escort, protect, herd, traffic-control or rescue actions require admitted implementations.

### AI tactical policy

General autonomous policy for civilians, fleeing wild populations, moving hazards, escort/rescue or multi-objective crossing encounters remains blocking until live evidence proves it.

### Minecraft / Cobblemon / Craftics adapter/playback

Dynamic populations, traffic and crossing playback remain partial/blocking end-to-end unless admitted semantic event/state contracts exist.

## PTU / Caelo boundary

No adopted `sources/caelo` directory was visible in the narrative source inventory during Pass 327. `sources/kairos` remains comparative material only.

Before any rich implementation, verify project-authoritative definitions for relevant movement capabilities, tracking/perception, terrain, weather, collision/fall damage, interception/rescue, Moves, Abilities, Items and Trainer Features.

## Testing direction

Useful future regressions:

- a structurally open crossing does not automatically set population use;
- one successful observation does not mark whole-population migration complete;
- a failed crossing attempt remains evidence after restart;
- a maintenance report reaches only explicit recipients;
- a later correction does not erase the earlier notice;
- an observation becomes stale only after an explicit later event/window rule;
- Minecraft pathing cannot write authoritative migration state;
- reduced encounters never call unsupported forced movement or hazard rules.