# Engine Readiness Snapshot — Pass 92

Status: implementation evidence snapshot, not canon.
Date: 2026-08-28

## Scope

Supports:
- `design/coastal-navigation-aids-lighthouses-beacon-continuity-extension.md`;
- `proposals/2026-08-28-coastal-navigation-aids-lighthouse-beacon-seeds-92.md`.

Writable repository:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Internal project review

Before Pass 92, the current Narrative tree was inspected at head `51eae1907e1861d0a90b1cbc99c48e894d44a606`.

The root tree confirmed the repository contains only README plus `design/`, `research/` and `proposals/` project layers. The design tree was inspected completely and reported `truncated=false`. Research and proposals inventories were also inspected before selecting the new subject.

Direct overlap review included:
- Maritime/Coasts/Depths;
- Cartography/Survey/Wayfinding;
- Technology/Energy/Infrastructure;
- Facility Maintenance;
- Infrastructure Outage/Restoration;
- Weather Forecast/Preparedness;
- Public Notices;
- Soundscapes/Acoustic Ecology;
- Travel/Transport/Expedition;
- Fisheries;
- Cobblemon Runtime Authority Boundary;
- Encounter Implementation Contracts;
- Pass 91 readiness evidence.

Maritime already permits navigation assets, lighthouses and buoys. Cartography owns charts. Technology owns technical condition. No existing system owned the temporal identity/characteristic/observation/notice/verification lifecycle of an individual aid. Pass 92 fills only that coordination gap.

## Binding runtime authority

Ouros owns:
- navigation-aid semantic world state;
- registry/history facts chosen for canon;
- route/service world-state inputs;
- explicit encounter composition;
- which observed Pokémon become tactical participants;
- nonbattle consequences and handoffs.

AutoPTU owns:
- combatants and teams;
- legal actions and targets;
- tactical positions and movement;
- initiative/action economy;
- HP, statuses, stages and temporary effects;
- damage/healing;
- Moves, Abilities, Items and Trainer Features;
- Push/Pull/knockback/Intercept/forced movement/reactions;
- tactical AI;
- authoritative battle results.

Minecraft/Cobblemon/Craftics may present/adapt:
- lighthouse/building geometry;
- lights, glass, platforms, buoys, signs and props;
- Pokémon/NPC models, forms, poses, animations and cries;
- particles and sounds;
- day/night/weather presentation;
- UI/networking/synchronization;
- reviewed observation/interaction hooks;
- semantic playback of AutoPTU results.

Required direction:
`Ouros navigation/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`.

Forbidden shortcuts:
- Minecraft lamp/redstone state deciding canonical aid operation;
- Cobblemon entity proximity creating a Pokémon work assignment;
- nearby Pokémon becoming battle participants automatically;
- Cobblemon BattleState/controller deciding participants, HP, status, position or results;
- visible fog creating PTU Accuracy penalties;
- moving water, cliff visuals, sparks or horn sounds creating tactical hazards without AutoPTU authority.

## PTU/Caelo boundary

Pass 92 establishes no:
- Navigation Skill bonus;
- lighthouse signal-range formula;
- fog/darkness Accuracy rule;
- sound-signal status effect;
- cliff/fall/surf/wave damage;
- current-driven displacement;
- beacon machinery electrical/heat hazard;
- vessel reroute check;
- rescue/piloting DC;
- Pokémon beacon eligibility;
- Trainer Feature for lighthouse work;
- automatic benefit for Ampharos or Electric-type Pokémon.

Any of those require governing PTU/Caelo source review plus current runtime evidence.

## Live revisions inspected

AutoPTU-Java `main`:
`538b0ed5e81e427e94397382f5a33a763a776bab`

Latest change:
`Freeze intercept resource mutation contract (#253)`

AutoPTU Python `main`:
`18532b43969190388065b9d94a02cfef2a7bb72e`

Latest change:
`Career: reject duplicate prepared battle IDs before season resolution`

The Python change is Career-state integrity work and does not establish a tactical capability family.

## New Java evidence in Pass 92

Java #253 freezes a Python-oracle contract around Intercept resource mutation. The exporter checks the authoritative `_attempt_intercept` path for:
- `intercept_ready`;
- `coaching_intercept`;
- `sentinel_stance`;
- removal of those temporary effects;
- Shift action consumption;
- extra-action consumption paths.

This is useful because a complete Intercept ultimately needs correct resource mutation and temporary-effect consumption.

However, #253 primarily freezes/guards the oracle contract. It does not prove that every Intercept path, competing reaction, knockback source, environment interaction, transcript event, AI policy or Minecraft playback path is complete in Java.

No broad family is promoted by this commit.

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

Pass 92 makes no family-level promotion.

## Why complete movement remains PARTIAL

Current positive evidence includes substantial real slices:
- Shift/Jump legality;
- Push/Pull displacement;
- collision/bounds/partial-stop behavior;
- position mutation;
- Intercept attempt eligibility/policy;
- Intercept check resolution;
- attack-line geometry;
- candidate discovery/materialization;
- expiry cleanup;
- committed reaction movement;
- melee Intercept + Push 1 composition;
- latest resource-mutation oracle contract.

Still missing for family-wide VERIFIED:
- broad live Intercept trigger integration across all relevant attacks;
- competing-reaction ordering/conflicts;
- complete resource mutation implementation evidence for every path;
- broad knockback coverage;
- every forced-movement origin;
- Move/Ability/Item/Trainer Feature integration across the family;
- environment-driven displacement;
- complete transcript semantics;
- tactical AI handling;
- Minecraft playback.

A lighthouse/cliff encounter therefore cannot script a gust, wave, edge or machine as knockback.

## Why terrain/weather/hazards/zones/reactions remains BLOCKING

Pass 92 full encounters may eventually want:
- fog or darkness affecting visibility;
- cliff-edge consequences;
- surf/current zones;
- electrical or hot machinery;
- signal/sound-related zones only if governing rules support them;
- protective/interception reactions around workers;
- environmental damage or forced movement.

No family-wide authoritative runtime exists for these assumptions.

Reduced versions keep all such conditions as presentation/world state or exclude the geometry from battle.

## Encounter capability profile — Beacon Head Withdrawal

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

Reduced version:
- crew exits before battle;
- unsafe cliff/machinery is outside the tactical arena;
- weather is visual/world state;
- Ouros explicitly selects combatants;
- AutoPTU runs a static legal encounter;
- Maintenance/Conservation resolve site access afterward.

## Encounter capability profile — Buoy Maintenance Window

Intended full version additionally wants:
- water-sensitive movement;
- WITHDRAW/CLEAR_ROUTE objective logic;
- Intercept/forced movement;
- possible current/weather state;
- territorial/withdrawal-aware tactical AI;
- adapter playback.

Major limitations:
- complete movement remains PARTIAL;
- terrain/weather/hazards/zones/reactions is BLOCKING;
- AI tactical policy is BLOCKING;
- adapter/playback is BLOCKING.

Reduced version keeps workers, craft and aid outside tactical targeting and uses one static reviewed arena.

## Encounter capability profile — Fog-Signal Station Perimeter

Intended full version could eventually require:
- authoritative reduced-visibility behavior;
- sound/zone mechanics if the governing sources define them;
- reactions/Intercept;
- objective-aware AI;
- adapter playback.

Reduced version keeps fog/sound as observations and presentation. The staff exits first. AutoPTU resolves static combat only for immediate perimeter access. Soundscapes and Maintenance investigate the signal afterward.

## Noncombat profile — Two Lights, One Chart

No tactical battle capability is required.

Inputs can include:
- chart edition;
- aid registry entry;
- navigation notices;
- direct observations;
- timestamps;
- photographs;
- weather/visibility observations;
- harbor-light records;
- route history.

This can be implemented before the tactical adapter.

## Cobblemon reuse classification for Pass 92

Strong SAFE_REUSE candidates at the design level:
- blocks/building geometry;
- glass/lamps/doors/platforms;
- models/forms/poses/cries;
- sounds/particles;
- signs/books/maps as display surfaces;
- day/night/weather visuals;
- UI/networking/world synchronization primitives.

ADAPTER_REQUIRED:
- projecting Ouros operational state into light/sound presentation;
- turning player interactions into inspect/repair/acknowledge intent;
- recording observations with provenance;
- representing route consequences without inventing rules.

BATTLE_AUTHORITY_FORBIDDEN:
- Cobblemon battle participants/controllers/state;
- nearby-entity participant selection;
- HP/status/position/damage/result authority;
- Minecraft block/physics state generating PTU hazards or displacement.

## Open implementation questions

- Does governing PTU/Caelo material define darkness/fog visibility rules relevant to these scenes?
- Which Skills govern technical inspection, navigation or observation when a mechanical check is actually required?
- Which individual Pokémon capabilities could legitimately support navigation work?
- Does any governing rule support sound-based navigation interactions?
- How should dynamic visibility eventually enter AutoPTU without letting Minecraft weather become authority?
- What semantic events are required to render Intercept/withdrawal scenes correctly in Minecraft?
- Which Cobblemon/Minecraft light, sound and display hooks are stable enough for SAFE_REUSE versus adapter wrappers?

## Open canon questions

- Do any Ouros coasts use lighthouses, fixed lights, buoys, sound signals or remote/electronic aids?
- Are standards regional, local or incompatible between areas?
- Who operates/maintains the network?
- How are temporary changes published?
- Which aids are public landmarks?
- Is Pokémon-assisted signalling historical, current, ceremonial or absent?
- What navigation information is public versus restricted?
- How do isolated settlements receive urgent changes?

No answer is promoted to canon by Pass 92.