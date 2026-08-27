# Engine Readiness Snapshot — Pass 85

Status: implementation evidence snapshot, not canon.

Date: 2026-08-27

## Scope

This snapshot supports:

- `design/ranch-managed-groups-pasture-continuity-extension.md`;
- `proposals/2026-08-27-ranch-managed-groups-pasture-seeds-85.md`.

Writable repository:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Internal project evidence reviewed

The complete recursive narrative repository tree at Pass 84 was inspected before selecting this topic. Adjacent systems reviewed directly include:

- Food/Agriculture/Hospitality;
- Breeding/Eggs/Nursery/Lineage;
- Pokémon Work Role Participation;
- Seasonality/Calendar/Phenology;
- Conservation/Protected Areas/Stewardship;
- Encounter Implementation Contracts;
- Pass 84 engine snapshot;
- Cobblemon runtime authority boundary.

The new ranch layer was written as an extension between these systems rather than a replacement.

## Binding authority boundary

Ouros owns:

- rural-site and managed-group world state;
- persistent actor/Pokémon identity;
- group membership observations and count reconciliation;
- paddock/pasture/use state;
- explicit encounter composition and combatant manifests;
- noncombat consequences and system handoffs.

AutoPTU owns:

- tactical combatants;
- legality and targets;
- tactical positions/movement;
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
- fences, gates, paths, vegetation and rural props;
- interactions/UI;
- networking/client-server synchronization;
- playback of AutoPTU semantic state/events.

Required direction:

`Ouros rural/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden direction:

`Cobblemon BattleState / nearby entities / despawn / animation / pathing -> participant or tactical authority`

## Current revisions inspected

AutoPTU-Java `main`:

`b8960e98b8ca25ff318b88b3383c0a3f9f4f1de3`

Latest inspected commit:

`Freeze and port intercept attempt gate (#247)`

Recent movement/interception evidence retained from Pass 84:

- `1649cdba59117221d6eb18080a49765cc8521c3b` — melee Intercept Push 1 composition;
- `c6bff5893c680dd7aef2995317f7fb6a88fd849d` — successful Intercept position commit;
- `6eabd9846f26127ba8498eadd7412d1c5e9cb144` — Intercept geometry ordering;
- `bb5185ddf230b97c9f798c0b6576d0d520c99694` — Intercept check resolution;
- `3177594f92df4c5a86023ba0cb5fbac3da195e4e` — Intercept eligibility;
- `0706679f4540a0f2249ccfa95fdc86dff0fcf7ea` — forced-displacement stop reasons;
- `46b03107a566deba55b9f01d2bb571632870719b` — Push/Pull forced-displacement execution.

AutoPTU Python `main`:

`a4f12530b6aac36763c50c5a3cb484a966c842fb`

Recent Python work bounds Career battle-transcript cache retention and persists Light Mode fallback. These are browser/presentation robustness changes and do not establish a new tactical capability family.

## New Java evidence since Pass 84

### Commit #247 — Intercept attempt gate

The Java runtime now has a parity-gated `InterceptAttemptPolicy` that owns attempt-level restrictions before candidate geometry, skill checks or movement.

The focused contract proves:

- cannot-miss attacks are rejected as Intercept attempts in this slice;
- area attacks are rejected;
- ordinary melee and ranged target kinds are distinguished from unsupported target kinds;
- Priority/Interrupt attempts use a speed gate;
- the interceptor must be strictly faster for that Priority/Interrupt path;
- these inputs must come from canonical battle/move state;
- adapters must not decide Intercept legality.

This is important evidence for the exact Intercept pipeline and reinforces the project's authority boundary.

It does not prove the entire reaction family.

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

Pass 85 makes no category promotion.

## Why complete movement remains PARTIAL

Positive evidence now includes:

- Shift and Jump legality;
- Push/Pull forced movement;
- collision/bounds/occupied-footprint partial stops;
- authoritative forced-position mutation;
- Intercept attempt gating;
- Intercept eligibility;
- Intercept d20/check arithmetic;
- candidate ordering and attack-line geometry;
- successful movement commitment;
- separation of reaction movement from the ordinary Shift bucket;
- one parity-backed melee Intercept Push 1 composition.

Still missing for family-level VERIFIED:

- complete general Intercept trigger lifecycle inside battle resolution;
- competing reaction timing/conflicts;
- complete redirection semantics across attack families;
- full knockback coverage;
- all Push/Pull/forced-movement sources;
- broad Move integration;
- broad Ability integration;
- broad Item integration;
- broad Trainer Feature integration;
- terrain/environment interaction with displacement;
- complete semantic transcript coverage;
- tactical AI reasoning about these mechanics;
- Minecraft/Cobblemon playback.

The ranch encounter designs may cite the exact existing Intercept/Push slices but cannot claim complete movement as generally verified.

## Why terrain/weather/hazards/zones/reactions remains BLOCKING

The latest Intercept gate is evidence for one reaction-like sequence. It does not establish a general reaction controller or the combined terrain/weather/hazard/zone family.

Still absent or not family-complete:

- general reaction registry and lifecycle;
- competing reactions;
- tactical Terrain ownership/state;
- tactical Weather controller;
- hazards and zones with lifecycle;
- environment-driven damage/status/movement;
- broad AI handling;
- adapter playback.

A muddy paddock, open gate, fence, wind, rain, slope or wildlife buffer therefore remains overworld/world-state presentation until an explicit AutoPTU mapping is reviewed.

## Java README caution

The current AutoPTU-Java README still lists broad work as pending, including:

- core combatant/grid battle state;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- tactical AI scoring/policy;
- Craftics/Cobblemon adapter.

The focused commits #240-#247 are stronger evidence for their exact movement/Intercept slices than the older checklist wording. They do not complete the broad families.

## Pass 85 encounter — Paddock Withdrawal

Full dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL according to roster;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

The attempt gate improves a useful Intercept slice. The intended full scene still needs objective-aware AI, moving background actors, reviewed environmental state, general reaction lifecycle and adapter playback.

Reduced executable contract:

- Ouros pauses the managed group outside tactical space;
- workers/noncombatants leave through world state;
- only explicitly selected Pokémon/Trainers become combatants;
- AutoPTU resolves a static legal arena;
- ranch/route state resumes afterward;
- no stampede, escort HP, scripted collision or fake weather mechanic is introduced.

## Pass 85 encounter — Grazing Route Wildlife Conflict

Full dependencies use the same overall profile.

Particularly important missing pieces:

- AI tactical policy for territorial/withdrawal intent;
- objective support for CLEAR_ROUTE/WITHDRAW as authoritative battle logic;
- general reactions/forced-movement integration;
- environment controller if terrain/weather is meant to matter;
- adapter distinction between moving managed Pokémon and tactical participants.

Reduced executable contract:

- the managed group stops outside the encounter segment;
- wild ecology remains world state;
- Ouros selects explicit combatants;
- AutoPTU resolves a static battle if combat is actually required;
- Conservation/Travel/Ranch systems decide route continuation afterward;
- victory cannot erase habitat use or create route ownership.

## Pass 85 noncombat systems executable now

These records do not require new tactical mechanics:

- rural managed-site identity;
- aggregate managed-group identity;
- exact important member references;
- membership observations;
- count reconciliation;
- paddock/pasture zone-use state;
- planned group movement;
- observed movement events;
- temporary refuge/relocation;
- Care/work/production handoffs;
- wild-overlap observations;
- seasonal pasture windows;
- service availability handoffs;
- Morning Count Reconciliation mystery;
- long-term rural-site history.

Full Minecraft embodiment remains adapter-dependent, but none requires Cobblemon BattleState authority.

## PTU/Caelo questions exposed by Pass 85

Source/runtime review is required before using:

- specific assisted or mounted movement;
- carrying/dragging limits;
- complete Intercept triggers/reactions;
- stampede or collision damage;
- fence/edge knockback rules;
- terrain movement penalties;
- tactical Weather;
- environmental statuses/damage;
- Command/Loyalty consequences;
- breeding or Egg production;
- mechanical milk/food output;
- abilities that manage groups, terrain or weather;
- Trainer Features that alter rural work or battle;
- capture rules within managed or protected-use areas.

Narrative ranch state cannot manufacture any of these mechanics.

## Cobblemon implementation opportunity

Useful surfaces to classify later at code level:

- persistent Pokémon entity projection;
- species/forms/models/textures;
- idle/movement/look/cry presentation;
- group presentation across paddock variants;
- entity tracking and synchronization;
- fences/gates/paths/vegetation/water blocks;
- sounds and particles;
- interaction/UI for observed counts and operational status;
- persistent identity mapping between Ouros IDs and current entities;
- world geometry observations through a reviewed adapter.

Every concrete Cobblemon API remains classified as SAFE_REUSE, ADAPTER_REQUIRED, BATTLE_AUTHORITY_FORBIDDEN or UNKNOWN_REVIEW_REQUIRED.

Cobblemon battle participant/state/controller logic is never a dependency target.

## Canon questions left open

- Which Ouros regions have ranch/pastoral institutions?
- Which managed Pokémon relationships are ownership, custody, partnership or communal stewardship?
- What products/services exist?
- Which species are commonly managed, if any?
- What terms do local cultures use for these institutions/groups?
- How do seasonal pasture routes interact with wild corridors and public roads?
- Which rural institutions provide Care or Nursery support?
- Which individual work roles require formal review or credentials?
- How much of a large group should Minecraft materialize simultaneously?

No answer is promoted to canon by this snapshot.
