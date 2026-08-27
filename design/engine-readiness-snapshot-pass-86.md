# Engine Readiness Snapshot — Pass 86

Status: implementation evidence snapshot, not canon.
Date: 2026-08-28

## Scope

Supports:
- `design/fisheries-aquatic-harvest-landing-stewardship-extension.md`;
- `proposals/2026-08-28-fisheries-aquatic-harvest-seeds-86.md`.

Writable repository:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Internal project review

The full recursive narrative tree at Pass 85 head `01f744213f1ee9cc93faee24557b9fb1662c6e19` was inspected before topic selection. GitHub returned the tree with `truncated=false`.

Adjacent content opened directly before writing:
- Maritime, Coasts & Underwater Depths;
- Food, Agriculture & Hospitality;
- Conservation, Protected Areas & Stewardship;
- Pass 85 engine snapshot;
- Cobblemon Runtime Authority Boundary;
- Pass 34 maritime research;
- Pass 18 food/agriculture research.

The new extension fills the already declared fishing/fishery operational gap rather than replacing those layers.

## Binding authority boundary

Ouros owns:
- fishery/aquatic-use world state;
- activity, landing and release records;
- ecological observations and provenance;
- explicit encounter composition and combatant manifest;
- persistent consequences/handoffs.

AutoPTU owns:
- tactical participants;
- legal actions/targets;
- tactical position and movement;
- initiative/action economy;
- HP/status/combat stages/effects;
- damage/healing;
- Move/Ability/Item/Trainer Feature rules;
- reactions/interception;
- tactical AI;
- battle result.

Minecraft/Cobblemon/Craftics may own/adapt:
- Poké Rod item/model and bobber presentation;
- cast/reel interaction presentation;
- bubbles, sounds, particles and animation;
- bait attachment UI/serialization where reviewed;
- Pokémon models/forms/poses/cries;
- docks/boats/blocks/props;
- interaction/network transport;
- semantic playback of AutoPTU state/events.

Required direction:

`Ouros fishery/ecology state -> reviewed fishing/encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden direction:

`Cobblemon Poké Rod spawn/BattleState/nearby entity -> automatic Ouros tactical participant or battle truth`

## Current live revisions inspected

AutoPTU-Java `main`:

`effe4d1d40ae3876924b60a7846b7a083bf12ee3`

Latest inspected change:
`Derive intercept attempt inputs from authoritative state (#248)`

Recent relevant movement/Intercept sequence:
- `b8960e98b8ca25ff318b88b3383c0a3f9f4f1de3` — Intercept attempt gate;
- `1649cdba59117221d6eb18080a49765cc8521c3b` — melee Intercept Push 1 composition;
- `c6bff5893c680dd7aef2995317f7fb6a88fd849d` — successful Intercept movement commit;
- `6eabd9846f26127ba8498eadd7412d1c5e9cb144` — Intercept geometry ordering;
- `bb5185ddf230b97c9f798c0b6576d0d520c99694` — Intercept check resolution;
- `3177594f92df4c5a86023ba0cb5fbac3da195e4e` — Intercept eligibility;
- `0706679f4540a0f2249ccfa95fdc86dff0fcf7ea` — forced-displacement stop reasons;
- `46b03107a566deba55b9f01d2bb571632870719b` — Push/Pull forced-displacement execution.

AutoPTU Python `main`:

`4ab6d692acb0e3145022f1cab480e89567afb92b`

Recent Python work enforces a raster safety budget before Full renderer startup. This is Career/browser rendering robustness, not a new tactical family.

## Java #248 evidence

The latest Java slice moves more Intercept-attempt input derivation into authoritative runtime state.

The commit sequence states that Java now owns/materializes inputs such as:
- canonical move priority;
- cannot-miss move trait resolution;
- target/attempt information used by Intercept policy;
- runtime ownership tests around those values.

This reinforces a project-critical boundary: Minecraft/Cobblemon adapters must not synthesize PTU Intercept eligibility or bonuses from presentation data.

It strengthens the existing Intercept pipeline but does not establish a complete general reaction system.

## Java README caution

The current README still explicitly describes AutoPTU-Java as the battle-rules engine and Minecraft/Cobblemon/Craftics as consumers/adapters. It continues to list broad incomplete work including:
- core combatant/grid battle state;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- semantic BattleSpec -> BattleTranscript parity;
- tactical AI scoring/policy;
- Craftics/Cobblemon adapter.

Focused commits after the checklist provide stronger evidence for their exact slices, but do not complete the families.

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

Pass 86 makes no category promotion.

## Why complete movement remains PARTIAL

Positive evidence includes:
- Shift/Jump movement legality;
- Push/Pull execution;
- collision/bounds/occupied-footprint partial stops;
- authoritative position mutation;
- Intercept attempt gate;
- Intercept eligibility;
- Intercept check resolution;
- candidate geometry/attack-line ordering;
- successful reaction movement commitment;
- one melee Intercept + Push 1 composition;
- authoritative derivation of more attempt inputs in #248.

Still missing for family-level VERIFIED:
- complete trigger integration across attack families;
- competing reaction ordering/conflict handling;
- complete redirection semantics;
- broad knockback coverage;
- all forced-movement sources;
- broad Move/Ability/Item/Feature integration;
- terrain/environment displacement interactions;
- complete semantic transcript coverage;
- tactical AI reasoning;
- Minecraft/Cobblemon playback.

## Why terrain/weather/hazards/zones/reactions remains BLOCKING

Intercept is a concrete reaction-like pipeline slice. It does not prove the permanent combined family.

Still missing/not family-complete:
- general reaction registry/lifecycle;
- competing reactions;
- tactical terrain ownership/state;
- tactical weather controller;
- hazards/zones with lifecycle;
- environment-driven status/damage/movement;
- tactical AI handling;
- adapter playback.

Tide, current, rain, wet docks, slippery surfaces, wave action or fishing-line obstruction therefore remain world/presentation facts unless an exact reviewed AutoPTU mapping exists.

## Cobblemon fishing evidence and classification

Current public Cobblemon documentation describes:
- Poké Rods;
- fishing using a bobber interaction similar to vanilla fishing;
- bubbles/reel timing;
- possible Pokémon/item/nothing outcomes;
- bait attachment;
- Lure/Luck of the Sea effects;
- cast/reel statistics;
- fishing-specific Pokémon patterns and spawn access.

This creates strong reuse opportunities and a strong authority hazard.

Preliminary design classifications:

```yaml
cobblemon_fishing_surface:
  rod_models_items: SAFE_REUSE_CANDIDATE
  bobber_animation_audio_particles: SAFE_REUSE_CANDIDATE
  cast_reel_input_hooks: ADAPTER_REQUIRED
  bait_ui_storage: ADAPTER_REQUIRED
  fishing_statistics: ADAPTER_REQUIRED
  internal_spawn_pool_selection_as_overworld_input: ADAPTER_REQUIRED
  internal_spawn_pool_selection_as_tactical_participant_authority: BATTLE_AUTHORITY_FORBIDDEN
  internal_battle_state_or_controller: BATTLE_AUTHORITY_FORBIDDEN
  exact_classes_and_events: UNKNOWN_REVIEW_REQUIRED
```

No exact API classification is final until implementation source is inspected.

## Fishing/PTU execution boundary

PTU 1.05 already defines a fishing procedure involving rod class, bait/lure, periodic bite checks, an Athletics reel-in check and possible subsequent capture/attack interaction.

That means a future Ouros executable fishing path should not substitute arbitrary Minecraft/Cobblemon odds for PTU when the PTU mechanic is meant to govern the scene.

A safe architecture may eventually:
1. use Cobblemon rod/bobber presentation;
2. collect cast/reel intent/context through the adapter;
3. resolve the governing PTU/Caelo/AutoPTU fishing step through an approved service;
4. bind any resulting Pokémon actor into Ouros world state;
5. create a BattleSpec only if a tactical encounter is explicitly required;
6. project the result back through Cobblemon.

Until that path is implemented, a Poké Rod spawn cannot automatically be treated as the tactical encounter manifest.

## Pass 86 encounter — Working-Waterfront Withdrawal

Full dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced contract:
- stop landing/work activity in Ouros world state;
- remove workers, customers, batches and gear from tactical space;
- create an explicit combatant manifest;
- use a static dock/shore arena;
- make tide/current/weather/slick surfaces non-tactical;
- resolve combat in AutoPTU;
- let the owning world systems decide reopening and downstream consequences afterward.

## Pass 86 encounter — Cove Release Window

Full profile uses the same permanent families.

Especially important blockers:
- objective-aware tactical AI;
- authoritative release/protect/withdraw objective support;
- water/terrain/environment controller if conditions matter;
- complete reaction/movement integration;
- adapter distinction between release actor/background wild actors and combatants.

Reduced contract:
- release target stays outside tactical state;
- release is a separate world action;
- any combat uses explicit selected participants nearby;
- AutoPTU result cannot itself mark the release complete.

## Pass 86 encounter — Fishing Contact Turns Hostile

Unique implementation need:
A reviewed fishing-to-encounter handoff must exist.

Required sequence:
- governing PTU/Caelo fishing resolution or approved equivalent produces a contact;
- Ouros creates/binds the exact persistent/generated actor;
- Ouros explicitly chooses whether tactical combat begins;
- AutoPTU creates/owns the battle;
- Cobblemon presents the actor and semantic events.

Current state:
BLOCKED for full Minecraft execution by adapter/playback and by lack of a reviewed fishing handoff. An ordinary manually authored battle using a static arena can still preserve the narrative premise as a reduced version.

## Noncombat Pass 86 systems usable before tactical completion

The following can exist as narrative/world-state design now:
- fishery-site identity;
- activity history;
- effort observations;
- landing-site identity;
- landing events;
- release records;
- equipment incidents/handoffs;
- market-name versus exact-identity provenance;
- landing reconciliation;
- stewardship-policy references;
- research/monitoring handoffs;
- cultural practice history;
- Three Boats, Two Landing Records mystery;
- long-term working-waterfront arcs.

Full Minecraft embodiment still requires adapter work, but none requires Cobblemon BattleState authority.

## PTU/Caelo questions exposed

Review required before implementation for:
- final governing fishing procedure and any Caelo differences;
- rod/bait/lure mapping to actual persistent items;
- fishing timing and Athletics resolution in the game loop;
- contact-to-attack/encounter transition;
- capture/release sequencing;
- water/shore movement context;
- Trainer Features affecting fishing;
- fishing-related equipment behavior;
- any actual food/resource harvest rules beyond Pokémon capture;
- water encounter/location constraints.

## Canon questions left open

- Which regions/settlements fish or harvest aquatic resources?
- What is actually harvested?
- Are Pokémon ever part of food production, and under what setting rules?
- What welfare norms exist?
- Which organizations operate landing sites?
- Who has authority to restrict activity?
- Do quotas, licenses or landing requirements exist anywhere?
- Which traditions are occupational, recreational, ceremonial or scientific?
- What technology and vessel scale is normal?
- Which Cobblemon fishing APIs can be reused without battle authority leakage?

No answer is promoted to canon by this snapshot.
