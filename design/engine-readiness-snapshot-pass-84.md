# Engine Readiness Snapshot — Pass 84

Status: implementation evidence snapshot, not canon.

Date: 2026-08-27

## Scope

This snapshot supports:

- `design/settlement-abandonment-return-reoccupation-extension.md`;
- `proposals/2026-08-27-settlement-abandonment-return-reoccupation-seeds-84.md`.

Writable repository:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Binding authority boundary

The project rule remains mandatory.

Ouros owns:

- settlement occupancy and use state;
- persistent actor/Pokémon identity;
- household/institution/world facts;
- explicit encounter composition and combatant manifest;
- noncombat consequences and system handoffs.

AutoPTU owns:

- tactical combatants;
- legal actions and targets;
- tactical positions and movement;
- initiative/action economy;
- HP/status/combat stages/effects;
- damage/healing;
- Move/Ability/Item/Trainer Feature mechanics;
- tactical AI;
- battle result.

Minecraft/Cobblemon/Craftics owns or adapts:

- overworld embodiment;
- Pokémon models/forms/textures;
- poses/animations/cries/sounds/particles;
- blocks, vegetation and settlement props;
- client/server synchronization and networking;
- interactions/UI;
- playback of AutoPTU semantic state/events.

Required direction:

`Ouros settlement/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden direction:

`Cobblemon BattleState / entity proximity / despawn / animation -> participant, settlement or tactical authority`

## Current revisions inspected

AutoPTU-Java `main`:

`1649cdba59117221d6eb18080a49765cc8521c3b`

Latest inspected commit:

`Compose melee intercept Push 1 with forced movement (#246)`

Immediately relevant previous commit:

`c6bff5893c680dd7aef2995317f7fb6a88fd849d` — `Commit successful intercept movement authoritatively (#245)`

Previously established movement evidence still includes:

- `6eabd9846f26127ba8498eadd7412d1c5e9cb144` — Intercept geometry ordering;
- `bb5185ddf230b97c9f798c0b6576d0d520c99694` — Intercept check resolution;
- `3177594f92df4c5a86023ba0cb5fbac3da195e4e` — Intercept eligibility;
- `0706679f4540a0f2249ccfa95fdc86dff0fcf7ea` — forced-displacement stop reasons;
- `46b03107a566deba55b9f01d2bb571632870719b` — Push/Pull forced-displacement execution and position mutation.

AutoPTU Python `main`:

`60031b186648ceb9d0cdc59eded5a136eef87b21`

Latest inspected work persists automatic Career Light Mode fallback. The immediately preceding work also protects private opponent roster-size information during replay. These are presentation/privacy robustness changes, not new tactical capability families.

## New Java evidence since Pass 83

### Commit #245 — authoritative Intercept movement commit

`InterceptMovementApplication` now proves a concrete parity-gated transition after server-owned geometry and the Intercept check have already resolved.

Evidence includes:

- successful Intercept check commits the chosen intercept position to `BattleRuntimeState`;
- failed check leaves the interceptor at its origin;
- reaction movement does not consume the ordinary Shift action bucket;
- the chosen intercept position is expected to come from server-owned legal Shift geometry;
- Python oracle parity explicitly checks those facts.

This is stronger than Pass 83's geometry-only evidence because tactical position now changes authoritatively.

### Commit #246 — melee Intercept Push 1 composition

The Java runtime now composes a specific melee-interception follow-up in Python order:

1. Interceptor movement/line commit;
2. Push 1 of the protected target through `ForcedMovementApplication`;
3. final interceptor move to the protected target's original anchor.

The result retains forced-displacement details so callers can later emit collision/partial-stop semantics without recomputing geometry.

Parity/tests establish:

- the protected target is the forced-movement target;
- the interceptor is the source;
- the instruction is Push 1;
- line movement precedes the Push;
- Push precedes final anchor commitment;
- blocked Push retains the Python-observed final interceptor-anchor behavior;
- failed Intercept leaves both combatants unchanged.

This is a substantial end-to-end slice of melee Intercept movement plus Push.

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

Pass 84 makes no category promotion.

## Why complete movement remains PARTIAL

Current positive evidence now includes:

- Shift and Jump legality;
- Push/Pull forced movement;
- collision/bounds/occupied-footprint partial stopping;
- large-footprint handling for the implemented forced-displacement slice;
- authoritative runtime position mutation;
- Intercept eligibility;
- Intercept check arithmetic;
- Intercept candidate ordering and attack-line geometry;
- successful Intercept movement commitment;
- separation from the ordinary Shift bucket;
- one parity-backed melee Intercept Push 1 composition.

Still insufficient for family-level VERIFIED:

- complete Intercept trigger lifecycle inside general battle resolution;
- reaction timing, conflicts and ordering across reaction sources;
- complete redirection semantics across attack families;
- full knockback coverage;
- all Push/Pull/forced-movement sources;
- broad Move integration;
- broad Ability integration;
- broad Item integration;
- broad Trainer Feature integration;
- environment/terrain interaction with displacement;
- semantic transcript coverage for the complete family;
- tactical AI reasoning about Intercept/forced movement;
- Minecraft/Cobblemon playback.

A narrative encounter may depend on the exact verified slice, but it may not claim generic complete movement or generic reaction support.

## Why terrain/weather/hazards/zones/reactions remains BLOCKING

The bundle still lacks the broad battlefield controllers and lifecycle required by the permanent capability category.

Intercept evidence demonstrates pieces of one reaction-like path. It does not establish:

- a general reaction registry/lifecycle;
- competing reactions;
- terrain ownership/state;
- tactical Weather controller;
- hazard lifecycle;
- zone lifecycle;
- environment-driven damage/status/movement;
- broad AI handling;
- adapter playback.

Visible settlement ruin, unstable flooring, vegetation, water, smoke, wind or weather therefore remains world/presentation state unless an explicit reviewed AutoPTU mapping exists.

## Java README caution

The current AutoPTU-Java README still describes the following broad work as pending:

- core combatant/grid battle state;
- full damage pipeline and remaining accuracy state;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- tactical AI scoring/policy;
- Craftics/Cobblemon adapter.

The focused commits after that checklist are stronger evidence for their exact slices. They do not silently complete the broad families.

## Pass 84 encounter — Return Survey at Old Main Street

Intended full dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL according to roster;
- terrain/weather/hazards/zones/reactions — BLOCKING if unstable settlement conditions become tactical;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

The new Intercept slice is useful but does not make the full encounter production-ready. The intended scene needs noncombatant withdrawal, objective-aware behavior, reviewed environmental state and Minecraft distinction between world actors and selected combatants.

Reduced executable contract:

- Ouros pauses the survey;
- surveyors/noncombatants leave the tactical area through world state;
- unsafe building zones remain excluded rather than becoming fake tactical hazards;
- Ouros creates an explicit combatant manifest;
- AutoPTU resolves a static legal encounter;
- survey/maintenance/return readiness resumes afterward;
- battle victory cannot certify a building, route or settlement zone.

## Pass 84 encounter — Reclaimed Courtyard Conflict

Intended full dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle/damage/status/Move/Ability/Item/Feature families according to actual roster — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if territorial/quiet-space zones become tactical;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for territorial/escape priorities;
- adapter/playback — BLOCKING.

Reduced executable contract:

- returning residents leave before battle creation;
- observed ecological use remains world state;
- Ouros selects only active opponents/combatants;
- AutoPTU resolves a reviewed static arena;
- Conservation/Public Space/Residential decide later use;
- victory does not erase wild use, create ownership or authorize reopening.

## Pass 84 noncombat systems executable now

The following Pass 84 material can exist as narrative/world-state without new combat capabilities:

- settlement continuity phase history;
- zone-level occupancy/use records;
- public-label versus occupancy-truth separation;
- remnant resident records;
- temporary operational use;
- institutional displacement/location history;
- return-readiness evidence packets;
- household return candidates linked to Residential;
- ecology-overlap observations;
- reopening events and notices;
- Occupancy Map Reconciliation mystery;
- Chronicle/Public Memory writeback;
- dense-location reuse decisions.

Full in-world materialization remains limited by the Minecraft/Cobblemon adapter state, but none of these records require Cobblemon battle authority.

## PTU/Caelo mechanical questions exposed by Pass 84

Exact source/runtime review remains required before settlement-return encounters rely on:

- unstable-floor or collapse mechanics;
- fall damage;
- smoke or low-visibility effects;
- weather penalties;
- terrain movement costs beyond already verified movement primitives;
- environmental statuses/damage;
- carrying/rescue mechanics;
- protected-target reactions;
- complete Intercept semantics;
- knockback around edges or structures;
- Pokémon field Moves used for repair/clearing;
- abilities that alter terrain/weather;
- Trainer Feature interrupts;
- object interaction during combat.

Narrative ruin state cannot manufacture any of these rules.

## Cobblemon implementation opportunity

Pass 84 should maximize safe reuse for settlement embodiment.

Concrete APIs still need code-level classification, but useful target surfaces include:

- persistent Pokémon entity projection;
- models/forms/textures;
- idle/movement/look/cry presentation;
- blocks and decorative palettes for phased settlement variants;
- vegetation/state changes;
- signs/notice boards;
- doors and interactable props;
- entity tracking and synchronization;
- NPC/Pokémon scheduling presentation;
- client/server networking;
- UI for access/return status;
- persistence hooks for stable Ouros settlement/actor IDs;
- world geometry observations passed through an explicit adapter.

Every concrete Cobblemon API remains classified as SAFE_REUSE, ADAPTER_REQUIRED, BATTLE_AUTHORITY_FORBIDDEN or UNKNOWN_REVIEW_REQUIRED.

Cobblemon's own battle participant/state/controller logic is never a target dependency for Ouros.

## Canon questions left open

- Which approved Ouros settlements have experienced depopulation, evacuation or long closure?
- Which causes are already compatible with canon history?
- What authority can declare an area open, closed or safe?
- What records identify former/current residents?
- How are empty residences handled culturally or institutionally?
- Can institutions maintain displaced operations indefinitely?
- Which settlements have developed meaningful wild Pokémon use during low human occupancy?
- What services are considered prerequisites for return in each region?
- What privacy protections apply to occupancy/return records?
- Which places deliberately choose a smaller or different future instead of full restoration?

No answer is promoted to canon by this snapshot.
