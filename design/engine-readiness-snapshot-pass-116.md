# Engine Readiness Snapshot — Pass 116

Status: EVIDENCE SNAPSHOT. This file records live implementation evidence used by narrative authoring. It does not change engine capability status by itself.
Date: 2026-08-28

## Read-only repositories inspected

AutoPTU-Java head inspected:

`87fbcb2ab75b4642c762017a037a6c0dccb9d8ad`

Commit/PR #268: `Bridge real interception sequence into PRE-target registry`.

AutoPTU head inspected:

`7b4c3d603bd8c2ddd0b47faf7b8691c307e259f9`

Commit: `Career: prefetch continue-career route on intent`.

Neither repository was modified by Pass 116.

## Java evidence since Pass 115

Pass 115 inspected Java head `fedf0b21cafb2d3e56ddbb3f0d3487353ce6d74c`.

Java has since advanced to `87fbcb2ab75b4642c762017a037a6c0dccb9d8ad` through PR #268.

The new code adds a core-only PRE-target hook for Intercept. The hook takes an authoritative pre-resolution target context, invokes the existing interception spatial/RNG/resource sequence, and when an interception succeeds returns the interceptor as the replacement target plus a semantic `RuleEffectEvent` describing target replacement.

The regression evidence verifies at least one real path where:

- an interceptor candidate is discovered/selected by the supplied attempt plan;
- the existing spatial interception sequence runs;
- a successful attempt moves the interceptor to the resolved interception position;
- the original defender remains in its original position;
- the generic PRE-target result changes to the interceptor;
- a semantic Intercept target-replacement event is emitted;
- a failed attempt leaves target and interceptor position unchanged;
- the hook/planner remain core-internal rather than adapter-public authority.

Combined with the immediately preceding Java work, the evidence chain is now stronger for one concrete Intercept route: declared Move legality -> PRE-target interception sequence -> effective target replacement -> defender-bound re-preparation -> authoritative Move pipeline.

This remains representative evidence, not proof of the entire movement/reaction family.

It does not verify every Intercept trigger or candidate source, broad Push/Pull, broad Knockback, every forced-movement source, environmental displacement, generalized competing reactions, all reaction ordering, all Move/Ability/Item/Trainer Feature registrations, environmental zones, objective policy or Minecraft semantic playback.

No permanent capability family is promoted.

## AutoPTU evidence since Pass 115

Pass 115 inspected AutoPTU head `e300e70bb608b95a3abff36599e0269627c9716e`.

AutoPTU has advanced through several Career web route-prefetch commits to `7b4c3d603bd8c2ddd0b47faf7b8691c307e259f9`.

The current commit warms the Career API and SeasonHub chunks only after pointer/focus intent on Continue Career while keeping them outside synchronous Home startup. Regression coverage checks the lazy/prefetch boundary.

This is Career web performance/navigation work. It does not add or verify tactical targeting, movement, calculations, lifecycle, damage, statuses, terrain/hazards/reactions, Move behavior, Abilities, Items, Trainer Features, tactical policy or Minecraft/Cobblemon/Craftics battle authority.

No capability promotion follows.

## Permanent capability map

VERIFIED:

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No permanent category is promoted in Pass 116.

## Pass 116 authoring boundary

Wastewater continuity can progress substantially as persistent world-state and evidence management without simulating hydraulics or exposure inside battle.

Currently authorable:

- stable wastewater-system identity;
- collection sectors and authored source connections;
- explicit network links and paths;
- lift/pump-station operating records as world facts;
- treatment-facility and authored-stage state;
- treatment operations and verification handoffs;
- release/receiving handoff records;
- overflow/bypass observations without automatic mechanical consequence;
- monitoring coverage and gaps;
- isolation and temporary arrangements;
- restoration sequences;
- downstream owner-system handoffs;
- legacy network history;
- mysteries using maps, timestamps, observations, aliases and provenance;
- static inspected service-space exploration.

Active wastewater, currents, pits, gases, moving machinery, pressure, changing liquid depth, environmental exposure and contamination inside BattleSpec remain constrained.

## Encounter 1 — Lift Station Access Withdrawal

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL if withdrawal windows or changing access matter
- full stateful damage pipeline: PARTIAL if an exact environmental damage source is used
- status lifecycle: PARTIAL if an exact legal condition is used
- terrain/weather/hazards/zones/reactions: BLOCKING for wet/technical/confined zones, machinery effects or generalized reactions
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for protection/withdrawal objectives
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

Current authoring profile: REDUCED.

Reduced version:

Complete staff withdrawal and station isolation before BattleSpec creation. Keep wastewater, wet wells, pumps, energized equipment and controls outside the grid. Use a reviewed static dry approach. Victory can secure the immediate access only. It cannot restart the station, verify flow, repair equipment or restore the collection sector.

## Encounter 2 — Treatment Gallery Perimeter

Full intended dependencies become mechanically relevant if designers include active treatment surfaces, liquids, changing barriers, machinery, exposure or timed process changes.

Those additions require terrain/weather/hazards/zones/reactions and may additionally require complete movement, lifecycle, damage and status support depending on the exact governing rule.

Targeting/base movement/core/action economy/legal-action infrastructure remain VERIFIED at the permanent-category level. Move behavior, Abilities, Items and Trainer Features remain PARTIAL for exact interactions. Tactical policy and adapter/playback remain BLOCKING for richer protection/environment behavior.

Current authoring profile: REDUCED.

Reduced version:

Freeze treatment state before combat. Remove workers, controlled materials and active process surfaces. Keep technical machinery inert or off-grid. Resolve a conventional encounter in a static inspected corridor. Winning does not complete treatment, verify output or authorize release.

## Encounter 3 — Outfall Inspection Diversion

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: PARTIAL if Intercept, escort or forced displacement matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL if access changes by phase
- full stateful damage pipeline/status lifecycle: PARTIAL if an exact receiving-water or exposure rule applies
- terrain/weather/hazards/zones/reactions: BLOCKING for currents, wet-edge zones or generalized reactions
- move-specific behavior/abilities/items/Trainer Features: PARTIAL for exact interactions
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for protect/escort/withdraw behavior
- adapter/playback: BLOCKING

Current authoring profile: REDUCED.

Reduced version:

Withdraw the inspection party before BattleSpec. Keep active release and receiving water out of combat. Use stable dry reviewed ground. Victory may secure the immediate perimeter for later inspection. It cannot verify discharge, establish pollution, alter receiving-system state or reopen downstream access.

## Exploration — The Old Alignment Under the Market

Current authoring profile: EXECUTABLE AS WORLD EXPLORATION.

The exploration relies on static reviewed access, current and historical maps, persistent infrastructure IDs, renovation records, photographs, work logs, actor testimony and Pokémon observations.

It does not require dynamic liquids, toxic zones, gas, pressure, moving machinery or active treatment.

Any future version adding those effects must be reclassified against then-current PTU/Caelo evidence and engine contracts.

## PTU/Caelo mechanical unknowns for Pass 116

Current project evidence does not verify a universal contract for:

- sanitary wastewater flow/current;
- gravity/pressure sewer calculations;
- pump suction or pressure;
- wastewater depth changes during turns;
- automatic drowning or suffocation in wastewater spaces;
- automatic Poison, infection or disease from exposure;
- generic contaminant damage;
- odor or gas status effects;
- low-oxygen/confined-space mechanics;
- slippery/wet sewer terrain by default;
- treatment chemistry;
- treatment efficiency or timing;
- overflow probability;
- automatic environmental harm from a bypass record;
- moving machinery as a tactical hazard;
- valves/gates/pumps as universal battle interactables;
- automatic Poison-type or Water-type environmental immunity;
- species-derived contamination sensing or wastewater processing;
- Move/Ability/Item/Trainer Feature-powered sewage treatment without exact rule support;
- complete objective-aware evacuation/protection semantics.

These remain UNKNOWN rather than being implemented by narrative code or the Minecraft adapter.

## PTU/Caelo guardrail

The internal source scan remains controlling. A Caelo location may carry a defined environmental mechanical identity when the governing source explicitly defines it. That does not authorize conversions such as sewer water = Poison zone, wet floor = Slow Terrain, pump visual = forced movement, gas particles = status, Grimer presence = contamination, Water type = immunity or Minecraft suffocation = PTU damage.

Before any wastewater environmental effect enters BattleSpec mechanically, authoring needs an exact governing PTU/Caelo rule and current verified/partial implementation evidence for every permanent capability family involved.

## Minecraft/Cobblemon/Craftics authority boundary

Presentation may use service tunnels, pipes, pump buildings, access covers, treatment structures, barriers, signage, liquid visuals, particles, sound, NPCs and Pokémon.

Ouros decides persistent topology, operational facts, observations, handoffs and combatant selection.

AutoPTU decides legal actions, tactical positions, HP/status changes and outcome.

The adapter plays back those authoritative facts.

Native water spread, redstone machinery, piston movement, poison, suffocation, fall damage, entity collision or block adjacency may never become a parallel PTU rules engine.