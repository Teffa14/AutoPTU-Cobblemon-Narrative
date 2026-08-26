# Engine Readiness Snapshot — Pass 56

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live evidence

Newest inspected AutoPTU-Java commit:

`b35f09bbcc4246b1846e57c5c4f9bb5771d474e8` — Materialize temporary Accuracy inputs from runtime state (#220).

The Java README still states that the repository is not yet a Minecraft mod and that Python AutoPTU remains authoritative while parity work is incomplete. It still lists core combatant/grid battle state, full damage resolution, status controller, terrain, hazards, forced movement, reactions, hook registries, full transcript parity, AI scoring/policy and the Craftics/Cobblemon adapter as unfinished.

Newest inspected Python AutoPTU commit:

`1a9e271ebba878ed4676379d28f6a6ed2add245f` — Career: reject coerced battle collection entries (#150).

Recent Python changes on 2026-08-26 harden persisted battle presentation and reject malformed transcript/presentation collections. They improve robustness around existing authoritative output but do not establish new Java combat capability families.

## Permanent capability map

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

No Pass-56 evidence justifies promoting a category.

## Residential non-inference gates

A residence does not grant healing, rest, training, crafting, breeding or Feature benefits unless an authoritative rules layer explicitly supplies them.

Occupancy does not prove ownership.

A household does not imply family, romance or friendship.

A Pokémon living near a home does not imply capture, ownership or Loyalty.

Observed environmental preference does not become a PTU modifier.

A blocked stairwell in overworld state does not automatically become difficult terrain or a hazard in AutoPTU.

A neighborhood route can change world-state availability without creating movement bonuses.

A residential evacuation can resolve before combat so civilians do not require unsupported escort mechanics.

## Encounter review — Stairwell Evacuation

Intended version may require:
- narrow-space routing;
- civilian evacuation objectives;
- interception;
- forced displacement;
- changing blocked exits;
- hazard tiles;
- AI that understands escape/protection objectives.

Dependency state:
- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:
Resolve resident evacuation and access closure in narrative state before battle. Instantiate only legal combatants on a fixed map. Do not simulate civilians, moving exits, interception objectives or dynamic hazards. The authoritative battle result updates building access and follow-up state.

## Encounter review — Courtyard Habitat Conflict

Intended version may require:
- territorial or withdrawal objectives;
- dynamic occupied areas;
- escape routes;
- environmental interaction;
- AI that understands non-KO goals;
- embodied residential state in Minecraft.

The same BLOCKING families apply to dynamic zones, objective-aware tactical policy and adapter/playback. Forced movement/interception remains blocking if used. Lifecycle, damage, status, moves, abilities, items and Trainer Features remain partial.

Reduced version:
Clear residents from the tactical area first. Run a static legal encounter with only active combatants. Resolve coexistence, repair, stewardship or relocation consequences afterward through narrative world state.

## Noncombat review — Three Homes Survey

This concept requires no battle mechanics when implemented as observation and world-state comparison.

It can read:
- authored residence state;
- route/service availability;
- settlement capability;
- observed environmental conditions;
- existing Pokémon observations;
- maintenance history;
- accessibility state;
- civic/public-works dependencies.

It must not generate PTU DCs, Pokémon mechanical housing bonuses or hidden ownership rules.

A fully embodied apartment-viewing loop still depends on Minecraft/Cobblemon/Craftics adapter/playback, but the decision logic itself can exist in narrative/server UI state now.

## Pass-56 outcome

Residential life is currently safest to advance through persistent world state, observation, relocation records, household routines, service dependencies and callbacks. Rich tactical residential incidents should retain reduced static versions until forced movement, hazards/zones, tactical AI and adapter/playback are implemented.

Capability classifications remain unchanged from Pass 55.