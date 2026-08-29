# Engine Readiness Snapshot — Pass 115

Status: EVIDENCE SNAPSHOT. This file records live implementation evidence used by narrative authoring. It does not change engine capability status by itself.

Date: 2026-08-28

## Read-only repositories inspected

AutoPTU-Java head inspected:

`fedf0b21cafb2d3e56ddbb3f0d3487353ce6d74c`

Commit/PR #266: `Route pre-resolution replacement through authoritative move pipeline`.

AutoPTU head inspected:

`e300e70bb608b95a3abff36599e0269627c9716e`

Commit: `Career: remove obsolete 2.1 MB trainer portrait sheet`.

Neither repository was modified by Pass 115.

## Java evidence since Pass 114

Pass 114 already inspected Java head `fedf0b21cafb2d3e56ddbb3f0d3487353ce6d74c`.

No newer Java commit was present at the Pass 115 inspection point.

The current evidence therefore remains:

- declared Move legality is validated against the controller-selected target;
- the PRE-resolution target registry can replace the effective defender on the implemented path;
- defender-bound preparation is rebuilt for that effective target;
- the effective target enters the authoritative Move pipeline;
- downstream reaction context, type interaction, damage target, damage history and MoveResolved use the effective defender in the regression path;
- ordinary action economy is spent once;
- Move frequency usage is spent once.

This is strong evidence for one pre-resolution target-replacement / Intercept path.

It still does not prove complete Push/Pull, Knockback, every forced-movement source, environmental displacement, every Intercept trigger/window, generalized competing reactions, all environmental zones, all Move/Ability/Item/Trainer Feature registrations, full objective policy or Minecraft semantic playback.

No capability family is promoted.

## AutoPTU evidence since Pass 114

Pass 114 inspected AutoPTU head:

`bbbb31417bc7c6c216c7f80fab049bd630a97d49`

AutoPTU has since advanced to:

`e300e70bb608b95a3abff36599e0269627c9716e`

The new commit removes the now-obsolete large trainer portrait sheet after the lazy/deterministic portrait-loading work introduced immediately before it.

This is Career UI/performance/assets cleanup.

It does not add or verify tactical targeting, movement, calculations, lifecycle, damage, statuses, terrain/hazards/reactions, Move behavior, Abilities, Items, Trainer Features, tactical policy or Minecraft/Cobblemon/Craftics battle authority.

No capability promotion follows.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No permanent category is promoted in Pass 115.

## Pass 115 authoring boundary

Coastal-change continuity can progress primarily as persistent world-state/evidence management.

The following are currently authorable without dynamic environmental combat simulation:

- stable shoreline-sector identity;
- dated shoreline/backshore observations;
- ordinary tide-state references supplied by Maritime;
- versioned coastal-change interpretations;
- event and footprint revisions;
- erosion/deposition/overwash/cliff-change claims as non-mechanical evidence labels;
- route, habitat, public-space, infrastructure and cartography handoffs;
- temporary access arrangements;
- recovery sequences;
- legacy coastline/history content;
- investigations based on maps, photos, timestamps, observations and provenance;
- static exploration on already-reviewed routes.

Active surf, moving water, unstable edges, changing sand, overwash, collapsing coastal cliffs or timed environmental phases inside BattleSpec remain mechanically constrained.

## Encounter 1 — Dune Access Withdrawal

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL for timed withdrawal or changing access
- full stateful damage pipeline: PARTIAL if an exact legal environmental damage source exists
- status lifecycle: PARTIAL if an exact legal condition applies
- terrain/weather/hazards/zones/reactions: BLOCKING for unstable/soft/wet cells, surf/overwash zones, changing restricted areas or generalized reactions
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for protection/withdrawal goals
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

Current authoring profile: REDUCED.

Reduced version:

Complete the coastal environmental change and ordinary civilian/worker withdrawal before BattleSpec creation. Exclude active surf, uncertain dune edges, unstable substrate and nonparticipants. Use a static reviewed dry clearing, hardened access or inland perimeter. A battle result may secure the immediate perimeter only. It cannot validate shoreline condition, reopen access, repair infrastructure or complete recovery.

## Encounter 2 — Newly Exposed Structure Perimeter

Full intended dependencies:

- targeting/base movement/core/action economy/legal-action infrastructure: VERIFIED at the permanent-category level;
- complete movement: PARTIAL if Intercept, escort or forced displacement matters;
- full turn/round lifecycle: PARTIAL if tide/access changes by phase;
- terrain/weather/hazards/zones/reactions: BLOCKING if surf, unstable substrate, debris or changing access affects cells;
- full stateful damage pipeline and status lifecycle: PARTIAL if an exact environmental effect can harm/condition actors;
- move-specific behavior, abilities, items, Trainer Features/perks: PARTIAL for exact interactions;
- AI tactical policy: BLOCKING for protect/hold/withdraw/custody-aware tactics;
- adapter/playback: BLOCKING.

Current authoring profile: REDUCED.

Reduced version:

Keep the exposed object outside battle state. Freeze custody and excavation decisions during combat. Use static reviewed ground. Found Property, Archives/Heritage, Case Authority or another owner system resolves identity/custody afterward. Victory never transfers ownership or proves the object's origin.

## Encounter 3 — Former Beach Road Diversion

The changed coast can already serve as narrative context around a static encounter.

Full intended dependencies become richer if designers add:

- moving civilians/traffic;
- route-control objectives;
- dynamic restricted cells;
- collapsing edge or active surf;
- overwash or current displacement;
- delayed environmental phases;
- objective-aware tactical behavior.

Those additions require:

- complete movement: PARTIAL where Intercept/forced movement applies;
- full turn/round lifecycle: PARTIAL for phased changes;
- full stateful damage pipeline: PARTIAL where damage applies;
- status lifecycle: PARTIAL where conditions apply;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- Move/Ability/Item/Trainer Feature behavior: PARTIAL when they interact;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

Current authoring profile: REDUCED.

Reduced version:

Road/Travel resolves the legal detour before combat. Noncombatants remain off-grid. Resolve a normal battle at one static verified junction or inland segment. Winning does not realign the road, authorize public access or change coastal evidence.

## Exploration — The Line Behind the Dunes

Current authoring profile: EXECUTABLE AS WORLD EXPLORATION.

The exploration can rely on:

- static current geometry;
- dated maps and photographs;
- old route/access furniture;
- public records;
- actor testimony;
- Pokémon behavior observations;
- currently verified travel paths.

It does not require BattleSpec to simulate shoreline change.

If a future version adds dynamic tide changes, surf displacement, soft-sand movement, unstable cliff edges, falling material, water-depth change or timed hazards, those dependencies must be reclassified against then-current evidence.

## PTU/Caelo mechanical unknowns for Pass 115

Current internal evidence does not verify a universal contract for:

- shoreline-retreat or accretion rates;
- wave-energy erosion;
- tide-to-erosion calculations;
- storm-surge or wave-runup arithmetic;
- dune erosion thresholds;
- overwash timing or footprint;
- barrier breach probability;
- coastal-cliff retreat/collapse formulas;
- dynamic surf/current forced movement;
- undertow;
- drowning or suffocation caused by coastal conditions;
- sand burial;
- soft-sand movement penalties by default;
- wet/slippery terrain by default;
- spray visibility penalties;
- saltwater damage/status;
- changing water depth during turns;
- exposed-object interactable/custody mechanics inside battle;
- automatic Water/Ground/Rock-type environmental immunity;
- species-derived shoreline-change sensing or prediction;
- generic Pokémon-caused erosion from flavor;
- Move/Ability/Item/Trainer Feature-powered shoreline stabilization without exact rule support;
- complete objective-aware evacuation/protection semantics.

These remain UNKNOWN rather than being implemented by narrative code or the Minecraft adapter.

## PTU/Caelo guardrail

The internal source scan remains controlling.

Caelo demonstrates that a particular authored location can carry a defined environmental mechanical identity when a governing source says so.

That evidence does not authorize universal conversions such as:

- sand block = Slow Terrain;
- surf visual = forced movement;
- changing Minecraft waterline = tactical tide;
- dune/cliff texture = collapse hazard;
- spray particles = LoS penalty;
- Water type = coastal immunity;
- Ground/Rock type = stable footing;
- Pokémon digging animation = erosion event;
- native Minecraft drowning = PTU damage/status.

Before a coastal environmental effect enters BattleSpec mechanically, authoring needs both:

1. an exact governing PTU/Caelo rule for the intended effect; and
2. current tests/contracts for every permanent capability family the effect requires.

## Minecraft/Cobblemon/Craftics authority boundary

Presentation may use beach/dune builds, water, vegetation, barriers, observation markers, old/new paths, exposed props, NPCs, Pokémon, sounds, particles and map UI.

Ouros decides the persistent world facts.

AutoPTU decides combatants, legal actions, tactical positions, HP/status changes and outcome.

The adapter plays back those facts.

Native Minecraft/Cobblemon state may never become a parallel PTU rules engine.