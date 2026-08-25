# Engine Readiness Snapshot — Pass 157

Status: READ-ONLY EVIDENCE SNAPSHOT for narrative dependency planning.
Date: 2026-08-24

## Live heads inspected

- AutoPTU-Java main: `3caac611a987322a70dbdc34c56d613b96dadb92`
- AutoPTU Python main: `5ab2c175be6542b867f1676cf6848b9b15fd346f`

AutoPTU-Java advanced since Pass 156. The new Java head adds a POST-damage Move-special runtime bridge. The commit carries Python `damage_dealt` through move-special context, exposes a runtime-owned POST-damage seam and gates the transport contract against the Python oracle.

This is useful evidence for move-special ordering and transport after damage resolution.

It is not evidence that all POST-damage effects, moves, abilities, statuses, reactions or environmental interactions exist.

AutoPTU Python's inspected head is a Career resilience change that guards stalled battle retry clicks. It does not alter the tactical capability classification.

## Permanent capability classification

### VERIFIED

- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

### PARTIAL

- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks.

### BLOCKING as complete families

- complete movement including push / pull / knockback / interception / forced movement;
- terrain / weather / hazards / zones / reactions;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter and playback.

The new POST-damage bridge does not promote any complete family. It provides a bounded authoritative seam for handlers that still need individual parity evidence.

## PTU Fishing evidence boundary

PTU 1.05 publicly contains explicit Fishing rules and Fishing Rod equipment. The current project search did not expose a dedicated AutoPTU fishing runtime subsystem that could be treated as an end-to-end authoritative Minecraft integration.

Therefore Pass 157 distinguishes:

- PTU Fishing as a rules procedure that must be validated/implemented exactly when invoked;
- Fisheries management as overworld world state;
- Pokémon capture/custody as Pokémon Agency / authoritative capture logic;
- Minecraft fishing presentation as non-authoritative until an adapter exists.

No new fishing check, rod behavior, encounter table, capture bonus or handling rule is invented by the narrative repository.

## Pass 157 encounter dependency matrix

### Spawning Run Closure at Reedmouth — FULL

VERIFIED dependencies already available:

- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

BLOCKING dependencies:

- complete movement if an aquatic group, civilians or anglers must cross, withdraw, intercept or preserve a moving lane inside the grid;
- terrain/weather/hazards/zones/reactions if current, water depth, dynamic banks or protected-zone mechanics modify tactical state;
- AI tactical policy for `CROSS`, `WITHDRAW`, `PROTECT_ROUTE`, `CLEAR_ROUTE`;
- Minecraft/Cobblemon/Craftics adapter/playback for group movement, crowd state, corridor semantics and world-state handoff.

PARTIAL only if explicitly required:

- move-specific behavior;
- abilities;
- items;
- status lifecycle;
- Trainer Features/perks.

REDUCED version closes fishing access and advances migration/crowd movement in world state before opening a static conventional battle.

### Bycatch Release at South Pier — FULL

VERIFIED:

- targeting;
- base movement legality;
- core calculations;
- action economy;
- legal-action enumeration.

BLOCKING:

- complete movement for `WITHDRAW_TO_WATER`, release-lane protection or interception;
- AI tactical policy for non-hostile withdrawal/protection objectives;
- adapter/playback for pier staff, gear, release lane and disposition handoff;
- terrain/weather/hazards/zones/reactions if water, gear or protected lanes become tactical effects.

PARTIAL if used:

- items, if hooks/nets/handling equipment are actual battle items;
- move-specific behavior / abilities / status lifecycle if an exact PTU interaction is required.

REDUCED version completes the release in world state and removes the non-target Pokémon from tactical participation before battle. No restraint, injury or survival result is invented.

### Survey Net Recovery After Storm — FULL

BLOCKING:

- complete movement for technician/device approach, wildlife withdrawal or moving objectives;
- terrain/weather/hazards/zones/reactions for active water/debris/storm effects;
- AI tactical policy for `RETRIEVE_DEVICE`, `PROTECT_TECHNICIAN`, `WITHDRAW`, `REACH_EXIT`;
- adapter/playback for device location and semantic objectives.

Items remains PARTIAL if the survey device is modeled as an actual tactical item.

REDUCED version resolves Freshwater/Weather and equipment recovery outside battle, then uses static adjacent geometry if a confrontation remains.

### Landing Discrepancy at Harbor Market

No battle-engine dependency is required.

Fisheries, Supply Chains, Markets, Metrology, Archives and Science can compare:

- landing records;
- effort records;
- market inventory provenance;
- stored stock;
- survey results;
- unit definitions;
- reporting delays.

The outcome may remain unresolved. A battle result cannot establish abundance or fraud.

## Fisheries-specific engine non-inferences

Current evidence does not authorize:

- Minecraft fishing as PTU Fishing;
- Minecraft bobber success as authoritative catch;
- loaded Cobblemon count as stock abundance;
- capture/KO/despawn as fishery removal;
- fishing access as capture permission;
- a landing record as Pokémon ownership;
- Water-type as an aquatic harvest resource;
- aquatic Pokémon as food;
- Swim as fishing proficiency;
- Schooling as stock assessment truth;
- Pack Mon as schooling behavior;
- nets/hooks/lines as Stuck, Restrained or forced movement;
- deep water as drowning;
- currents as forced movement;
- rough water as Accuracy penalties;
- release as proof of no injury;
- release as proof of injury;
- a seasonal closure as proof of spawning;
- a spawning observation as automatic closure;
- catch rate as population size;
- market availability as local abundance;
- block/chest contents as fishery inventory authority.

## Why the new POST-damage bridge does not change Fisheries FULL encounters

The Java head now has a runtime-owned bridge for POST-damage Move-special handlers. Pass 157 FULL encounters are primarily gated by movement objectives, environmental water state, tactical AI and adapter/playback.

A POST-damage seam cannot supply:

- migration/crossing policy;
- water physics;
- release handling;
- crowd evacuation;
- non-hostile withdrawal AI;
- fishery-management logic;
- capture authority;
- stock assessment.

The Minecraft adapter must not imitate those missing systems with custom damage, status or movement rules.

## PTU / Caelo source boundary

The project continues to treat PTU/Caelo material as rules authority when available. PTU 1.05 Fishing is visible publicly, but the complete primary Caelo corpus was not reliably exposed through the task's accessible project sources during this pass.

Super PTU Online Helper was not exposed as an invocable capability.

No missing Caelo fishing, aquatic handling, capture, current, drowning, net, restraint, boating or harvest rule has been invented.

## Narrative implementation consequence

Pass 157 can advance immediately through:

- fishery management-unit history;
- activity and effort ledgers;
- independent surveys;
- stock-assessment revisions with uncertainty;
- catch/effort indices;
- non-target interaction records;
- release disposition history;
- seasonal/area control revisions;
- migration/stock boundary hypotheses;
- public fishing-event history;
- landing provenance where canon permits a harvested resource;
- reduced static-battle encounter versions.

FULL fisheries encounters remain gated behind exact capability families rather than delegated to Minecraft.