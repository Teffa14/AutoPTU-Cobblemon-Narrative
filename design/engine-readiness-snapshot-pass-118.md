# Engine Readiness Snapshot — Pass 118

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU were inspected read-only.

## Live heads inspected

AutoPTU-Java `main`: `e5439ac27a77cc41300435ed352cf4baf41f1269`

This is one commit beyond the Pass 117 head `cdb229db787ac93f28745f796c1d9944546676cc`.

Newest relevant Java evidence:

- declarative target-owned Ability prevention rules now cover the pinned status-application boundary for Inner Focus -> Flinch, Immunity -> Poison family, Insomnia -> Sleep family and Vital Spirit -> Sleep family;
- the contract explicitly respects Ability suppression;
- the parity test explicitly does not infer Own Tempo confusion prevention, Oblivious infatuation/enraged prevention or Run Away slowed/stuck/trapped prevention at this particular boundary;
- previous slices already support canonical ordered stacked status entries and generic Trainer Feature `apply_status`/`remove_status` effects;
- this strengthens status/Ability evidence but remains representative coverage, not a complete status controller or Ability catalog.

AutoPTU `main`: `ff84ec8d78390f51ca8c86bfc51f8d0db5af791e`

Newest visible Python work keeps transient Career featured-battle generation failures retryable and avoids poisoning the deterministic idempotency key. It is Career/service resilience work and does not promote a tactical capability category.

## Java README evidence

The live Java README still lists these major tasks as unfinished:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The README continues to define Java as the future authoritative battle core and Minecraft/Cobblemon/Craftics as consumers/renderers rather than owners of PTU rules.

## Permanent capability categories

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 118.

## Why the new Java status-prevention slice does not promote categories

The new commit proves a narrow declarative contract for four Ability/status relationships at one status-application boundary. It does not prove:

- all status families;
- all status application sources;
- all status immunities;
- full duration/expiry behavior;
- all Ability suppression semantics;
- all Ability interactions;
- terrain/weather/status coupling;
- reaction/interrupt semantics;
- complete status event emission;
- complete transcript parity.

Therefore `status lifecycle` and `abilities` remain PARTIAL.

## Why metrology is outside the battle core

Nothing inspected in Java or Python establishes authoritative overworld systems for:

- measurement standards;
- calibration events;
- calibration validity scope;
- instrument drift;
- measurement uncertainty;
- reference standards;
- survey benchmarks/datums;
- traceability chains;
- out-of-tolerance review;
- reference-system revisions;
- measurement correction records;
- inter-institution comparison campaigns.

These belong to persistent world/science/institutional state.

AutoPTU owns battle measurements such as range, LoS, stats, HP and initiative under its own rules. The metrology layer must never override those values because an overworld instrument reports something different.

## Pass 118 encounter dependency map

### Benchmark Ridge Recovery — FULL

Narrative objective:

Inspect a potentially disturbed survey benchmark while maintaining a safe route for survey staff and allowing local Pokémon to withdraw.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for dynamic escort/withdrawal and displacement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if unstable ground is tactically active
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `PROTECT`, `REACH_POINT`, `WITHDRAW`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Resolve slope safety and staff movement in overworld state. Inspect the benchmark outside battle authority. If confrontation remains, freeze one safe geometry and run a conventional static battle. Battle outcome cannot determine whether the benchmark moved or whether historical measurements remain usable.

### Three Gauges at Southworks — FULL

Narrative objective:

Make an infrastructure area safe while technicians investigate three disagreeing pressure/flow measurements.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for moving technicians/protected lanes
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if machinery/pressure becomes a tactical hazard
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `CLEAR_AREA`, `PROTECT`, `WITHDRAW`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Technology places the plant in a safe world-state mode first. Keep technicians and gauges outside the grid. Run a static battle only if a real confrontation remains. Compare measurement records after combat. Victory never chooses the correct gauge or diagnoses the fault.

### Reference Caravan Chokepoint — FULL

Narrative objective:

Protect a traveling calibration team and reference equipment while clearing a blocked route during a limited comparison window.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for true escort/route control
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only when a real environmental effect is tactical
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `ESCORT`, `CLEAR_ROUTE`, `WITHDRAW`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Keep staff/reference equipment outside battle state under Supply Chains/Custody. Use Travel to determine route availability. Run a static battle only to resolve an actual combat obstacle. The caravan proceeds afterward if the route is authoritative open.

## New overworld blockers introduced by Pass 118

These belong outside AutoPTU-Java:

- `MEASUREMENT_VARIABLE_REGISTRY`
- `INSTRUMENT_IDENTITY_STATE`
- `INSTRUMENT_METROLOGY_STATE`
- `REFERENCE_STANDARD_STATE`
- `CALIBRATION_EVENT_HISTORY`
- `CALIBRATION_SCOPE_STATE`
- `CALIBRATION_CHECK_HISTORY`
- `MEASUREMENT_UNCERTAINTY_STATE`
- `MEASUREMENT_RESOLUTION_STATE`
- `DETECTION_LIMIT_STATE`
- `TRACEABILITY_CHAIN_STATE`
- `REFERENCE_SYSTEM_VERSION_HISTORY`
- `SURVEY_BENCHMARK_STATE`
- `OUT_OF_TOLERANCE_REVIEW_STATE`
- `MEASUREMENT_CORRECTION_HISTORY`
- `COMPARISON_CAMPAIGN_STATE`
- `METROLOGY_TO_SCIENCE_HANDOFF`
- `METROLOGY_TO_MANUFACTURING_HANDOFF`
- `METROLOGY_TO_METEOROLOGY_HANDOFF`
- `METROLOGY_TO_CARTOGRAPHY_HANDOFF`
- `METROLOGY_TO_TECHNOLOGY_HANDOFF`
- `METROLOGY_TO_MINECRAFT_PROJECTION`
- `METROLOGY_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 118

Do not infer:

- calibrated instrument -> always correct;
- current calibration -> valid for every measurement range;
- precise display -> accurate value;
- same unit -> same datum/reference;
- same instrument model -> same calibration state;
- sensor disagreement -> sabotage;
- sensor disagreement -> one device must be broken;
- out-of-tolerance finding -> every historical record is false;
- new calibration -> rewrite old raw observations;
- changed survey reference -> landscape moved;
- Minecraft coordinate -> authoritative Cartography datum;
- telescope/scope -> battle Accuracy bonus;
- clock -> initiative bonus;
- pressure/temperature reading -> PTU hazard/Weather;
- Electric Pokémon -> electrical reference standard;
- Nosepass/Probopass -> survey-grade compass;
- Rotom -> universal instrument diagnostics;
- Porygon -> software-validation authority;
- generic Ability status-prevention contract -> scientific sensor mechanics;
- generic status handler -> environmental exposure or measurement mechanic.

## PTU/Caelo validation state

The narrative repository did not expose the project’s primary Caelo Core/Player/encounter/character-creation source corpus during this run.

Super PTU Online Helper was not exposed as an invocable capability.

Public PTU sources were used only for narrative/campaign context. No mechanical rule was validated for:

- Technology Education measurement checks;
- Researcher/Scientist instrument bonuses;
- equipment accuracy/precision bonuses;
- Survey/Perception DCs;
- Pokédex measurement authority;
- Pokémon capabilities as instrument replacements.

Those remain blocked pending the project’s authoritative PTU/Caelo text.

## Pass 118 conclusion

The live Java change adds real status/Ability parity evidence but leaves the permanent capability map unchanged. Metrology can advance entirely as overworld provenance now, while mechanically rich field encounters use reduced static-battle versions until complete movement, tactical environments, tactical AI and Minecraft playback are implemented.