# Engine Readiness Snapshot — Pass 90

Status: implementation evidence snapshot, not canon.
Date: 2026-08-28

## Scope

Supports:
- `design/astronomy-observatories-celestial-observation-extension.md`;
- `proposals/2026-08-28-astronomy-observatories-celestial-observation-seeds-90.md`.

Writable repository:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Internal project review

Before writing Pass 90, the complete recursive Narrative repository tree was inspected at Pass 89 head `7279f1bc6219190b3f8eb90b8d068f4a9c1ba3eb`. GitHub reported `truncated=false`, so the full current path inventory was available for duplicate-gap review.

Neighboring systems directly inspected or cross-checked included:
- Science, Research & Discovery;
- Seasonality, Calendar & Phenology;
- Myth, Archaeology & Sacred Sites;
- Weather Forecast & Preparedness;
- Cartography/Survey;
- Photography/Visual Evidence;
- Technology/Energy/Infrastructure;
- Public Events/Tourism;
- Anomalous Spaces;
- Material Culture/Geology;
- Encounter Implementation Contracts;
- Cobblemon Runtime Authority Boundary;
- Pass 89 readiness evidence.

The selected gap was persistent astronomical observation: observing sites, observing windows, sessions, detections/non-detections, public skywatching, sky-to-ground search leads and the operational history of observatories. The design intentionally delegates scientific method, calendar, weather, mythology, asset maintenance, field mapping and physical sample provenance to their existing owners.

## Binding runtime authority

Ouros owns:
- world date/time references supplied by the Calendar system;
- observatory and observing-session world state;
- predictions as claims/records;
- detection and non-detection provenance;
- public event handoffs;
- explicit encounter composition;
- terrestrial search leads generated from reviewed analysis;
- noncombat consequences and owning-system handoffs.

AutoPTU owns:
- battle participants and teams;
- targeting and action legality;
- tactical positions/movement;
- initiative/action economy;
- HP, statuses, stages and temporary effects;
- damage/healing;
- Moves, Abilities, Items and Trainer Features;
- forced movement, Intercept and reactions;
- tactical AI;
- battle result.

Minecraft/Cobblemon/Craftics may present/adapt:
- day/night sky and reviewed celestial visuals;
- cloud/weather presentation;
- particles and sounds;
- observatory structures, glass, doors, books, signs, screens and props;
- overworld Pokémon/NPC models, forms, poses, animations and cries;
- UI, networking and synchronization;
- reviewed interaction hooks;
- semantic playback of authoritative battle events.

Required direction:

`Ouros celestial/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden shortcuts:
- `Cobblemon nearby entity/BattleState/controller -> participant selection or tactical truth`;
- `Minecraft weather/darkness/meteor visual -> automatic PTU Weather, Hazard, Accuracy, damage or status`;
- `visual streak -> automatic meteorite object or encounter`.

## PTU/Caelo boundary for Pass 90

Pass 90 creates no:
- Astronomy Skill;
- telescope Skill bonus;
- constellation Feature;
- lunar/stellar combat buff;
- meteor hazard table;
- custom cosmic damage type;
- night Accuracy penalty;
- automatic meteorite effect;
- sky-event evolution/form rule;
- Legendary/Mythical encounter permission.

Any exact mechanical use of instrument operation, star navigation, celestial interpretation, environmental visibility, meteor impacts, celestial forms or related Trainer Features requires explicit governing PTU/Caelo review and implementation evidence.

## Live revisions inspected

AutoPTU-Java `main`:

`62108bb23fbaee3d64a0af50c6ae8581cfbedb60`

Latest change:
`Fix intercept cleanup first-family semantics (#252)`

AutoPTU Python `main`:

`ede7b3b60080c8cfca053265dc62465c7cd9bc98`

Latest change:
`Career: reject duplicate battle transcripts before season resolution (#196)`

## Java #252 evidence

Commit #252 corrects the authoritative Intercept candidate-cleanup application to match Python's first-family temporary-effect removal semantics.

The implementation now:
- consumes cleanup counts produced by Intercept discovery;
- removes the first live occurrence of the relevant temporary-effect family to mirror Python behavior;
- handles `no_intercept` and `sentinel_stance` cleanup through server-owned runtime state;
- prevents removal beyond existing family occurrences;
- includes updated Java tests and Python-side parity coverage.

The source contract again states that Minecraft/Cobblemon never performs this cleanup.

This strengthens parity and correctness inside the existing Intercept/temporary-effect slice. It does not establish complete movement, general reactions or full status lifecycle.

## Python #196 evidence

The Python Career engine now fails closed when duplicate battle transcript IDs are supplied before season-resolution mutation.

This improves persistent Career-state integrity and transcript handling. The commit explicitly preserves valid battle semantics and does not add a new tactical capability family.

## Current Java README caution

The live README continues to establish:
- Java is a battle-rules library before it is a Minecraft mod;
- Python AutoPTU remains the source oracle while the port is incomplete;
- AutoPTU-Java decides legal actions and battle results;
- Minecraft/Cobblemon/Craftics adapt world state and render resulting events.

Its broad pending checklist still includes:
- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy work;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Focused later commits provide stronger evidence for exact Push/Pull/Intercept slices than this broad checklist, but they do not prove family-wide completion.

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

Pass 90 makes no family-level promotion.

## Complete movement remains PARTIAL

Positive evidence still includes:
- Shift and Jump legality;
- authoritative Push/Pull forced displacement;
- collisions, bounds and occupied-footprint partial stops;
- position mutation;
- Intercept attempt policy;
- Intercept eligibility;
- Skill-check resolution;
- geometry/attack-line placement;
- reaction movement commitment;
- one melee Intercept + Push 1 composition;
- candidate discovery from Weaponize, prepared Intercept and Sentinel;
- candidate materialization from server-owned state/content;
- authoritative discovery-related expiry cleanup;
- corrected first-family cleanup semantics in #252.

Still missing for VERIFIED:
- broad live trigger integration across relevant attacks/actions;
- complete competing-reaction ordering/conflict handling;
- broad knockback coverage;
- all forced-movement sources;
- broad Move/Ability/Item/Trainer Feature integration;
- environment-driven displacement interactions;
- complete semantic transcript coverage;
- tactical AI handling;
- Minecraft/Cobblemon playback.

## Status lifecycle remains PARTIAL

#252 concerns temporary-effect cleanup semantics for an Intercept discovery path.

It does not prove:
- all persistent/volatile status lifecycles;
- all durations/save checks;
- all phase hooks;
- all Item/Ability/Feature interactions;
- complete semantic event ordering;
- all cleanup families.

## Terrain/weather/hazards/zones/reactions remains BLOCKING

This category is the main blocker for a mechanically rich astronomy encounter.

Not established family-wide:
- general reaction registry/lifecycle;
- multiple competing reactions;
- tactical terrain ownership/state;
- tactical weather controller;
- darkness/visibility as authoritative battlefield state;
- hazards and zones;
- delayed environmental impacts;
- meteor/heat/debris effects;
- environment-driven damage/status/movement;
- AI reasoning over those states;
- adapter playback.

Therefore Pass 90 treats:
- clouds;
- darkness;
- wind;
- meteor showers;
- impact debris;
- artificial light;
- exposed ridges;
- unstable impact ground
as world/visual/static state unless the exact tactical behavior is later verified.

## Encounter capability profile — Ridge Observatory Withdrawal

Full-version dependencies:
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
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Full version remains blocked because visitor withdrawal, changing route safety, environmental visibility, reaction behavior and objective-aware autonomous behavior need unsupported families.

Reduced version can preserve the premise by:
- stopping the observing session before tactical resolution;
- evacuating staff/visitors and equipment through world state;
- excluding unsafe edges through static arena geometry;
- choosing exact combatants in Ouros;
- running a reviewed static AutoPTU encounter;
- leaving sky/weather/darkness presentational;
- resolving reopening afterward.

## Encounter capability profile — Meteor-Fall Search Perimeter

Full-version dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when any status interaction matters;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:
- field team leaves the grid first;
- suspected impact material remains outside battle targeting;
- unsafe impact core is closed via world state;
- battle uses static reviewed terrain;
- Science/Geology resume investigation after the authoritative result;
- victory does not create, locate, authenticate or transfer a meteorite.

## Noncombat capability profile — Amateur Observation Reconciliation

No battle capability dependency is required.

It uses:
- world timestamps;
- observation provenance;
- photographs/records;
- sky-region/direction notes;
- weather/visibility observations;
- actor knowledge;
- Science analysis handoff.

Any Skill check must still come from an approved PTU/Caelo mapping rather than a new astronomy mechanic.

## Adapter implications

Astronomy is a strong candidate for broad Cobblemon/Minecraft reuse without conceding battle authority.

Potential reusable presentation:
- day/night cycle;
- sky and clouds;
- particles/sounds for reviewed authored events;
- observatory structures and interactive props;
- entities/models/forms/animations/cries;
- books/maps/signs/displays;
- UI/networking/synchronization;
- world coordinates/time.

Adapter work still required for:
- authoritative observation-session creation;
- session/instrument provenance;
- authored celestial-event synchronization;
- public schedule projection;
- search-region handoffs;
- semantic battle playback.

No Minecraft/Cobblemon BattleState code is permitted to fill those authority gaps.

## Unresolved mechanical questions

- Which PTU/Caelo Skill, if any, governs operating specific scientific instruments?
- Which Skill covers astronomical interpretation versus navigation by stars?
- Are any approved Caelo locations or encounter tables tied to celestial timing?
- Do any adopted Moves, Abilities, Items or Trainer Features explicitly interact with lunar/stellar/celestial conditions?
- Is darkness or low visibility defined mechanically in the governing source set, and how much has AutoPTU ported?
- What rules would govern impact heat, falling debris or shockwave displacement if a future scenario needs them?
- What exact adapter events can present an authored celestial event without relying on Cobblemon battle code?

## Unresolved canon questions

- Which Ouros regions have permanent observatories or skywatch sites?
- What instrument technologies exist in each region?
- Which celestial cycles are established world facts?
- What constellations are scientific mappings versus cultural traditions?
- Which institutions maintain public ephemerides or observing calendars?
- Are there dark-sky practices, restrictions or conflicts anywhere?
- What meteorite collections or impact sites already exist in approved lore?
- What Pokémon behavior is genuinely tied to celestial conditions rather than folklore?
- Which phenomena belong to ordinary astronomy and which, if any, are true anomalies?

None of these questions are promoted to canon by Pass 90.