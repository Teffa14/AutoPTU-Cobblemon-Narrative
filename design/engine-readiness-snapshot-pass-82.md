# Engine Readiness Snapshot — Pass 82

Status: implementation evidence snapshot, not canon.

Date: 2026-08-27

## Scope

This snapshot supports `design/local-sidequest-ecology-location-reuse-extension.md` and the mechanically rich Pass 82 candidates.

Writable repository:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Binding authority boundary

The project runtime boundary remains mandatory.

Ouros owns:

- persistent world facts;
- hook/thread state;
- actor knowledge;
- encounter composition;
- which actors become tactical participants;
- world-state consequences outside combat.

AutoPTU owns:

- tactical combatants;
- legality;
- initiative/action economy;
- movement and targeting rules;
- HP/status/effects;
- damage and rule hooks;
- tactical results.

Minecraft/Cobblemon/Craftics owns/adapts:

- world embodiment;
- models/forms/textures;
- animations/cries/sounds/particles;
- blocks and geometry;
- interaction surfaces;
- networking/client synchronization;
- UI and playback.

Required direction:

`Ouros world/thread state -> explicit BattleSpec -> AutoPTU authoritative state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden direction:

`Cobblemon BattleState/participants/HP/status/outcome -> Ouros or AutoPTU authority`

A Cobblemon entity appearing in a local cell cannot create a sidequest, become a combatant or resolve a thread merely because it is loaded.

## Current revisions inspected

AutoPTU-Java `main`:

`bb5185ddf230b97c9f798c0b6576d0d520c99694`

Latest inspected commit:

`Freeze and port intercept check resolution (#243)`

Immediately preceding relevant commit:

`3177594f92df4c5a86023ba0cb5fbac3da195e4e` — Intercept eligibility contract.

Earlier relevant movement commits already captured by Passes 80-81:

- forced displacement Push/Pull resolver;
- runtime position mutation;
- blockers/bounds/combatant collision stop reasons;
- large-footprint handling for the displacement slice.

AutoPTU Python `main`:

`b91d58a0aee8b595d1c843b9bf8aceb1686a2a4c`

Latest inspected work:

Career leaderboard trainer-name projection/persistence.

That Python work changes Career presentation/state projection, not tactical capability families.

## New Java evidence since Pass 81

Commit #243 adds a parity-gated `InterceptCheckResolution` contract.

The Java implementation establishes deterministic arithmetic for the Python interception skill check:

- d20 input;
- best of Acrobatics/Athletics ranks;
- Justified bonus input;
- terrain intercept bonus input;
- DC equal to distance multiplied by three;
- success on total greater than or equal to DC;
- Coaching can force success without altering the arithmetic result.

The implementation documentation explicitly requires skill ranks, Justified, terrain, Coaching and RNG to come from server-owned battle state/RNG. Minecraft/Cobblemon must not supply already-resolved PTU bonuses.

This is meaningful progress in interception.

It still does not establish complete end-to-end interception execution across every reaction/timing call site.

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

Pass 82 makes no category promotion.

## Why complete movement remains PARTIAL

Evidence now includes several real slices:

- ordinary Shift/Jump legality;
- Push/Pull forced displacement;
- collision/bounds/occupied-footprint stop behavior;
- runtime position mutation;
- Intercept candidate eligibility;
- Intercept skill-check arithmetic.

Still missing or not sufficiently proven for the whole family:

- complete Intercept trigger/execution path;
- reaction ordering/conflicts;
- target redirection consequences;
- complete knockback coverage;
- every forced-movement source;
- integration across Moves, Abilities, Items and Trainer Features;
- environment interactions;
- tactical AI choices around interception;
- complete semantic transcript/playback.

Therefore an encounter may rely on an exact implemented Push/Pull slice when named precisely, but a premise whose success depends on full reactive Intercept remains dependent on a PARTIAL family plus currently missing reactions/AI/playback.

## Terrain caution

The new Intercept check accepts a `terrainBonus` input.

That does not prove the terrain/weather/hazards/zones/reactions family.

It only proves that the arithmetic contract can consume a terrain-related intercept modifier once authoritative state has produced it.

Current Java README still lists terrain, hazards and reactions as pending broad work.

Pass 82 therefore keeps the environment family BLOCKING.

## Current Java README boundary

The live README still states:

- AutoPTU-Java decides legal actions and battle results;
- Minecraft/Cobblemon/Craftics adapt world state and render events;
- core combatant/grid battle state remains pending;
- full damage remains pending;
- status controller remains pending;
- terrain, hazards, forced movement and reactions remain on the broad pending checklist;
- hook registries remain incomplete;
- BattleSpec to BattleTranscript parity remains incomplete;
- tactical AI scoring/policy remains pending;
- Craftics/Cobblemon adapter remains pending.

Specific later commits can provide real slices inside a broad pending family. They do not justify declaring the family complete.

## Pass 82 encounter — Market-Lane Clear Route

Intended full version requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL according to roster;
- terrain/weather/hazards/zones/reactions — BLOCKING if market/environment elements become tactical;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Why the full version is not production-ready:

Its intended identity depends on active civilian withdrawal, objective-aware territorial behavior and possibly reactive interception in a narrow lane. Current engine evidence does not prove the full combination.

Reduced version:

- all noncombatants exit before tactical state;
- protected goods remain outside battle authority;
- Ouros freezes a reviewed static arena;
- AutoPTU receives only explicit combatants;
- conventional legal battle resolution occurs;
- route/public-space/ecology systems decide reopening afterward;
- no crowd escort, scripted Intercept, knockback or destructible-object mechanics are emulated in Minecraft.

## Pass 82 encounter — Revisit at the Footbridge

Intended full version requires the same core battle families and may additionally depend on:

- complete movement — PARTIAL;
- reactions/environment family — BLOCKING if crossing protection or terrain interaction is mechanical;
- tactical AI — BLOCKING for withdrawal/territorial priorities;
- adapter/playback — BLOCKING.

Reduced version:

Pedestrian rerouting and bridge availability resolve as Ouros world state before battle. Noncombatants remain outside the grid. The bridge/nearby ground is static geometry. AutoPTU resolves selected combatants. The later world-state writeback records whether crossing use, ecology or access changes.

## Pass 82 noncombat content

Most Pass 82 orchestration does not require tactical capabilities.

The following can execute as narrative/world-state logic now:

- candidate derivation from existing world state;
- foreground/ambient/latent classification;
- saturation budgeting;
- hook merge;
- repeatability guard;
- revisit-delta comparison;
- commitment priority;
- quiet-content compression;
- thread retirement;
- NPC narrative-instantiation tiers;
- location overuse checks;
- World Pulse integration;
- discovery-surface selection through existing systems.

These systems must still preserve actor knowledge, provenance and canon boundaries.

## Cobblemon reuse profile for Pass 82

SAFE_REUSE candidates:

- overworld NPC/Pokémon entities;
- models/forms/textures;
- animations, cries, particles and sounds;
- signs, books, containers and display blocks;
- UI for local optional threads;
- map markers as presentation only;
- world geometry;
- entity tracking/schedules where safe;
- interaction callbacks;
- networking/client synchronization;
- persistence hooks;
- visible shop/service/location variants.

ADAPTER_REQUIRED:

- turning Ouros thread state into UI/marker changes;
- maintaining local NPC identity across unload/reload;
- projecting schedule/routine changes without inventing state;
- instantiating explicit AutoPTU combatants from an Ouros encounter decision;
- mapping AutoPTU events back to Cobblemon animations/entities;
- reconnect/reload restoration from authoritative Ouros/AutoPTU state.

BATTLE_AUTHORITY_FORBIDDEN:

- Cobblemon deciding who participates because entities are nearby;
- Cobblemon internal battle teams defining Ouros actor participation;
- Cobblemon HP/status/position defining AutoPTU state;
- Cobblemon AI selecting authoritative tactical actions;
- Cobblemon victory/defeat flags resolving a thread;
- Cobblemon capture resolution replacing AutoPTU/PTU legality;
- entity despawn/chunk unload removing an AutoPTU combatant;
- internal mod BattleState creating or closing a sidequest.

## PTU/Caelo boundary for local sidequests

Pass 82 introduces no mechanical sidequest rewards or activity currencies.

No automatic effect comes from:

- accepting optional content;
- completing many local requests;
- visiting a district repeatedly;
- helping the same NPC several times;
- clearing a local battle;
- using downtime;
- reading a public notice;
- being recognized as a regular.

Any future mechanical reward must be validated against the governing PTU/Caelo sources and current AutoPTU support.

No homebrew burnout/social-capital mechanics from community sources are imported.

## Testing implications

Future local-orchestration implementation should verify:

1. A valid hook can exist without becoming foreground content.
2. Hook selection cannot read omniscient actor knowledge.
3. Saturation suppresses presentation rather than deleting source state.
4. Merged hooks preserve separate downstream owners.
5. A completed or failed battle cannot be cloned without a meaningful revisit delta.
6. World Pulse can resolve a low-urgency local issue without player involvement.
7. A request marker disappearing does not delete underlying world state.
8. An NPC can participate in several narrative roles under one persistent identity.
9. No PTU stat block is created merely because an NPC becomes a local foreground actor.
10. Cobblemon proximity/load state cannot select tactical participants.
11. Reduced encounters remain executable without tactical AI, reactions or adapter completeness.
12. A later engine promotion can upgrade the full version without rewriting the narrative premise.

## Unresolved mechanics

- complete Intercept execution beyond eligibility/check arithmetic;
- reaction timing and conflicts;
- complete knockback/forced-movement coverage;
- terrain/weather/hazard controller;
- full lifecycle/damage/status coverage;
- complete Move/Ability/Item/Trainer Feature registries;
- tactical AI policy for withdrawal/protect/territorial objectives;
- full semantic transcript;
- Minecraft/Cobblemon/Craftics adapter/playback.

## Unresolved canon

- which settlements receive local-content-cell profiles;
- culturally appropriate discovery surfaces by region;
- how much optional content is public versus socially discovered;
- which NPCs should be recurring multi-role residents;
- how much off-screen resolution is acceptable in shared multiplayer spaces;
- which locations should be protected from narrative overuse;
- how persistent UI markers work in-world;
- which recurring wild Pokémon have enough evidence for persistent individual identity.

No unresolved answer is promoted by this snapshot.
