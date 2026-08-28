# Engine Readiness Snapshot — Pass 93

Status: implementation-readiness evidence for Narrative authoring. This file does not establish Ouros canon or claim complete engine support beyond cited live evidence.

Date: 2026-08-28

## Evidence inspected

Narrative baseline before Pass 93:
- `Teffa14/AutoPTU-Cobblemon-Narrative` main at `f0c611d6e177563150c6fec84587826b72902735`.
- Recursive repository tree inspected with `truncated=false` before choosing the new research gap.
- Pass 92 snapshot and directly overlapping Travel, Transit Hubs, Interregional Mobility, Weather and Cobblemon authority-boundary documents reviewed.

Read-only engine repositories:
- `Teffa14/AutoPTU-Java` main at `538b0ed5e81e427e94397382f5a33a763a776bab`.
- `Teffa14/AutoPTU` main at `2de71fb314ca573806b96c538d4fc2b34c755b78`.

Neither engine repository was modified by Pass 93.

## Live Java delta since Pass 92

There is no newer AutoPTU-Java commit than the one already inspected for Pass 92.

Current latest Java evidence remains #253, `Freeze intercept resource mutation contract`, at `538b0ed5e81e427e94397382f5a33a763a776bab`.

That slice freezes authoritative resource mutation around Intercept, including relevant prepared/temporary state and action-budget consumption. It strengthens the existing Intercept chain but does not prove the complete movement family, all reactions, broad knockback, all forced-movement sources or full tactical lifecycle.

The current Java README still states the architectural target clearly: AutoPTU-Java decides legal actions and battle results; Minecraft/Cobblemon/Craftics later adapt world state and render events. Broad pending work still includes core combatant/grid state, full damage resolution, status controller, terrain, hazards, forced movement/reactions, registries, full transcript parity, tactical AI and the Minecraft/Cobblemon adapter.

## Python AutoPTU delta

Python AutoPTU advanced to `2de71fb314ca573806b96c538d4fc2b34c755b78` through Career browser-performance work that lazy-loads secondary routes.

This is useful application/runtime performance work. It does not add evidence for a tactical capability family and therefore causes no readiness promotion.

## Permanent capability map

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

No family is promoted in Pass 93.

## Why complete movement remains PARTIAL

Current evidence now covers substantial permanent slices including:
- Shift and Jump legality;
- Push/Pull forced displacement;
- collision and partial-stop behavior;
- authoritative position mutation;
- Intercept candidate discovery;
- eligibility;
- attempt gates;
- check resolution;
- geometry;
- committed interceptor movement;
- one melee Intercept plus Push 1 composition;
- temporary-effect cleanup;
- candidate materialization;
- resource mutation/consumption contract.

Still missing or insufficiently general:
- complete end-to-end reaction lifecycle for all relevant cases;
- competing reaction ordering/conflicts;
- broad knockback coverage;
- every forced-displacement origin;
- broad Move integration;
- broad Ability integration;
- broad Item integration;
- broad Trainer Feature/perk integration;
- environment-driven displacement;
- objective-aware tactical AI;
- full semantic transcript/playback coverage in Minecraft.

One mature Intercept path cannot be used as evidence that the whole category is VERIFIED.

## Aviation-specific readiness consequences

Pass 93 adds no aviation mechanics to the engine.

The following must remain narrative/world state or presentation unless later evidence proves corresponding tactical support:
- wind and turbulence;
- runway surface effects;
- moving aircraft/vehicle platforms;
- aircraft collision;
- crash/fall consequences;
- propeller/engine or machinery hazards;
- visibility and cloud tactical effects;
- takeoff/landing motion;
- aerial altitude layers;
- emergency evacuation objectives;
- passenger/cargo protection objectives.

A Minecraft aircraft animation, moving entity or visible weather system cannot supply any of those rules.

## Encounter readiness — Runway Perimeter Withdrawal

Full version requirements:

```yaml
encounter: Runway Perimeter Withdrawal
requirements:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Current authoring profile: REDUCED.

Reduced form:
- halt all aircraft movements through world state;
- remove workers and other noncombatants before BattleSpec creation;
- exclude the active landing area and machinery;
- use a static reviewed arena;
- allow only explicitly selected Ouros combatants;
- keep wind/weather/vehicle presentation mechanically neutral;
- resolve reopening after battle through owning world systems.

## Encounter readiness — Diverted Cargo Apron Interruption

Full version particularly depends on:
- complete movement: PARTIAL;
- objective-aware AI tactical policy: BLOCKING;
- reaction/zone behavior if operational geometry matters: BLOCKING;
- adapter/playback: BLOCKING.

Current authoring profile: REDUCED.

Cargo, workers and vehicles remain outside the tactical grid. A static encounter may create a `safe_access_available` outcome, but it cannot deliver cargo, complete custody transfer or move an aircraft.

## Encounter readiness — Old Airstrip Wildlife Conflict

The premise can already exist as world-state investigation because Science/Conservation/Travel continuity does not require tactical implementation.

If a battle is authored, its reduced form uses a static legal arena and explicit combatant selection. Any future territorial/withdrawal-aware full form remains dependent on AI tactical policy and possibly terrain/zones/reactions.

## PTU/Caelo boundary for air travel

PTU 1.05 evidence reviewed for Pass 93 supports Sky as a movement capability and discusses mounted transport in terms of the actual individual's size, Power and equipment.

That evidence does not establish:
- piloting;
- aircraft operation;
- passenger capacity;
- aircraft speed/fuel/endurance;
- takeoff or landing checks;
- aerial vehicle combat;
- crash/collision rules;
- universal Trainer carriage by Flying Pokémon.

Narrative content must not invent these rules. If future canon uses Pokémon-assisted air transport, the exact individual must pass the governing PTU/Caelo and implementation checks.

## Cobblemon authority boundary

Pass 93 preserves the binding direction:

`Ouros aviation/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Safe or likely reusable surfaces remain visual/overworld infrastructure such as blocks, lights, boards, entities, models, flying poses, animations, sounds, particles, UI, networking, coordinates and synchronization.

Any feature that chooses tactical actors, legality, HP/status, positions, tactical weather, collision damage, AI decisions or results remains `BATTLE_AUTHORITY_FORBIDDEN` unless it is merely projecting AutoPTU-owned state.

## Promotion gate for aviation-rich encounters

Do not promote the full versions merely because an aircraft can be rendered or moved in Minecraft.

A full runway/apron encounter requiring dynamic hazards or evacuation needs current evidence for the exact mechanic families. At minimum, authored dynamic terrain/hazard/reaction behavior needs `terrain/weather/hazards/zones/reactions` above BLOCKING; objective-aware opponents need `AI tactical policy` above BLOCKING; in-world authoritative presentation needs adapter/playback above BLOCKING.

If a design also relies on complete Intercept/knockback/forced movement, that exact slice must be verified rather than inferred from the existence of representative Intercept tests.

## Unresolved implementation questions

- Which PTU/Caelo Skills or Features, if any, govern piloting or aviation work?
- Does the governing source set define any usable vehicle framework for aircraft?
- What exact rules govern mounted Sky transport outside battle for an individual Pokémon?
- What altitude/fall rules are intended for Ouros if airborne tactical play is ever promoted?
- How should a future adapter represent moving world vehicles without allowing Minecraft physics to become battle authority?
- How should battle playback remain stable when a visual transport asset is moving while AutoPTU uses a tactical reference frame?
- Which Cobblemon APIs for flying poses/entities are `SAFE_REUSE`, `ADAPTER_REQUIRED` or unrelated to the desired integration?

These remain open rather than receiving invented answers.