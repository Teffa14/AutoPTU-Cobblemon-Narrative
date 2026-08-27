# Engine Readiness Snapshot — Pass 83

Status: implementation evidence snapshot, not canon.

Date: 2026-08-27

## Scope

This snapshot supports:

- `design/pokemon-work-role-participation-extension.md`;
- `proposals/2026-08-27-pokemon-work-role-participation-seeds-83.md`.

Writable repository:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Binding authority boundary

The project integration rule remains mandatory.

Ouros owns:

- persistent Pokémon identity and world facts;
- workplace/task/assignment state;
- encounter composition;
- the explicit combatant manifest;
- noncombat consequences and service/project writeback.

AutoPTU owns:

- tactical combatants;
- legal actions and targets;
- initiative/action economy;
- tactical positions;
- movement/Intercept/forced movement rules;
- HP/status/combat stages/effects;
- damage, healing and hooks;
- battle AI decisions;
- battle result.

Minecraft/Cobblemon/Craftics owns or adapts:

- overworld embodiment;
- models/forms/textures;
- poses/animations/cries/sounds/particles;
- block geometry and props;
- interactions;
- client/server synchronization;
- networking;
- UI/playback.

Required direction:

`Ouros work/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden direction:

`Cobblemon BattleState/nearby entity/activity animation -> work or battle authority`

A Pokémon entity can be visibly performing a work animation and still remain outside a tactical encounter unless Ouros explicitly selects it.

## Current revisions inspected

AutoPTU-Java `main`:

`6eabd9846f26127ba8498eadd7412d1c5e9cb144`

Latest inspected commit:

`Freeze and port intercept geometry ordering (#244)`

Earlier immediately relevant commits:

- `bb5185ddf230b97c9f798c0b6576d0d520c99694` — Intercept check resolution;
- `3177594f92df4c5a86023ba0cb5fbac3da195e4e` — Intercept eligibility;
- `0706679f4540a0f2249ccfa95fdc86dff0fcf7ea` — forced displacement collision stop reasons;
- `46b03107a566deba55b9f01d2bb571632870719b` — Push/Pull forced displacement execution and runtime position mutation.

AutoPTU Python `main`:

`d1b079f1d1f168f79981ce559f4d3f745668e1b8`

Latest inspected work:

Career replay now reveals opponent build information progressively from authoritative reveal events and hides unrevealed build details.

That improves information-boundary truthfulness. It does not establish a new tactical capability family.

## New Java evidence since Pass 82

Commit #244 adds a reusable, parity-gated `InterceptGeometryResolution`.

The implemented contract proves these deterministic geometry slices:

- eligible interceptor candidates can be ordered by footprint distance to the target anchor;
- stable ordering is preserved for equal distances;
- if an interceptor already occupies the attack line, its current anchor is preserved;
- otherwise the attack line is intersected with legal Shift tiles;
- the nearest reachable line tile is selected using footprint distance;
- no reachable line tile yields no geometry destination.

The implementation explicitly states that the caller still owns:

- eligibility;
- legal Shift generation;
- RNG/check resolution;
- committing authoritative movement.

Passes 81-82 already verified separate parity-backed contracts for Intercept eligibility and the Intercept skill check. Together these are substantial progress toward interception.

They still do not prove complete end-to-end Intercept reaction execution.

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

Pass 83 makes no category promotion.

## Why complete movement remains PARTIAL

Current evidence now includes:

- Shift/Jump legality;
- Push/Pull forced displacement execution;
- collision, bounds and occupied-footprint stopping;
- large-footprint handling for the implemented displacement slice;
- authoritative runtime position mutation;
- Intercept eligibility;
- Intercept check arithmetic;
- Intercept candidate ordering and reachable attack-line geometry.

Still missing or not sufficiently proven for the full family:

- complete Intercept trigger lifecycle;
- reaction timing/order and conflicts;
- complete movement commit/redirection semantics for interception;
- complete knockback coverage;
- every forced-movement source;
- broad Move/Ability/Item/Trainer Feature integrations;
- environment interactions;
- tactical AI policy around interception/forced movement;
- full semantic transcript and Minecraft playback.

Therefore a candidate can name an exact implemented Push/Pull or Intercept-geometry slice when useful, but cannot claim full reactive Intercept support.

## Java README caution

The current AutoPTU-Java README still lists broad pending work for:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- tactical AI scoring/policy;
- Craftics/Cobblemon adapter.

The newer focused commits are stronger evidence for implemented sub-slices than that broad checklist, but they do not make the broad family complete.

## Pass 83 encounter — Worksite Withdrawal With Partner Pokémon

Intended full version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when required by roster;
- terrain/weather/hazards/zones/reactions — BLOCKING if worksite conditions become tactical;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL where relevant;
- Trainer Features/perks — PARTIAL where relevant;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Why full version is not production-ready:

The intended experience depends on dynamic withdrawal/protection, potentially reactive interception, non-KO territorial priorities and a presentation layer that preserves the distinction between workers and tactical participants.

Reduced executable contract:

- work is paused before battle creation;
- every human and non-selected working Pokémon evacuates through Ouros world state;
- the workplace assignment records PAUSED/HANDED_OFF/RELEASED state as appropriate;
- Ouros freezes a reviewed static arena;
- explicit combatants only are placed in the BattleSpec;
- AutoPTU resolves an ordinary legal battle;
- Workplaces/Worksite Safety/Maintenance determine reopening afterward;
- no work-role bonus, escort mechanic, crowd movement, scripted Intercept or environmental damage is faked in Minecraft.

## Pass 83 encounter — Service Route Partner Interruption

Intended full version may require:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle/damage/status/Move/Ability families according to roster — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if the route environment is tactical;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for ESCAPE/CLEAR_ROUTE/territorial priorities;
- adapter/playback — BLOCKING.

Reduced executable contract:

The service pauses before battle. The working Pokémon remains outside tactical state unless Ouros deliberately selects it as a combatant. If selected, its occupational assignment has zero tactical authority. AutoPTU resolves the standard encounter, then Travel/Courier/Science/Conservation or another owning layer decides whether the service resumes.

## Pass 83 noncombat content

The core participation system can execute as narrative/world-state logic without new tactical mechanics:

- task requirement profiles;
- work-assignment lifecycle;
- evidence snapshots;
- supervised-trial records when the trial is purely observational;
- handler/supervisor scope;
- work check-in and handoff records;
- pause/withdrawal history;
- work-history callbacks;
- integration with staffing, safety, care and equipment;
- Minecraft schedule/materialization policy;
- distinction between visible presence and active assignment.

A noncombat work outcome still must defer to the owning system. For example, this extension cannot mark a repair complete or a delivery received merely because a participation event occurred.

## PTU/Caelo mechanical questions exposed by Pass 83

Exact source review is still required before a work task relies mechanically on:

- lifting/carrying capacity;
- environmental use of Moves;
- specific out-of-battle Ability effects;
- swimming/flying/overland capabilities beyond already verified movement slices;
- Command/Loyalty interactions;
- Trainer Features governing Pokémon cooperation;
- equipment use by Pokémon;
- work/rest limitations if any are adopted;
- object manipulation with combat Actions;
- safety effects represented as tactical hazards.

Narrative evidence may support a work-assignment decision. It cannot manufacture those mechanics.

## Cobblemon implementation opportunity

Current public Cobblemon documentation confirms a data-driven Poser surface supporting poses and named animations. That is useful SAFE_REUSE evidence for work embodiment.

Pass 83 therefore encourages future adapter work to inspect concrete Cobblemon APIs for:

- persistent Pokémon entity projection;
- idle/movement/look poses;
- custom/addon work animations;
- cries/sounds;
- entity tracking and synchronization;
- interaction/menu hooks;
- worksite props and blocks.

Every concrete API still needs classification under:

- SAFE_REUSE;
- ADAPTER_REQUIRED;
- BATTLE_AUTHORITY_FORBIDDEN;
- UNKNOWN_REVIEW_REQUIRED.

No animation callback or Cobblemon battle object may become assignment or PTU authority.

## Canon questions left open

- Which Ouros institutions use Pokémon in routine work?
- Which tasks are culturally ordinary or controversial?
- What vocabulary is used for participating Pokémon?
- Are there formal supervision, rest, compensation or retirement practices?
- How are repeated wild helpers understood?
- Which human qualifications are required to supervise specific tasks?
- Which task categories require mechanical PTU/Caelo evidence?
- What public/private work-history information is retained?

No answer is promoted to canon in this snapshot.