# Engine Readiness Snapshot — Pass 88

Status: implementation evidence snapshot, not canon.
Date: 2026-08-28

## Scope

Supports:
- `design/hot-springs-bathhouses-thermal-leisure-continuity-extension.md`;
- `proposals/2026-08-28-hot-springs-bathhouses-seeds-88.md`.

Writable repository:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Internal project review

The complete recursive Narrative tree at Pass 87 head `83170825f938bd08aa26b98186daf7ed3592954d` was inspected before topic selection. GitHub returned `truncated=false`.

A cave-system candidate was rejected after opening `design/geology-excavation-resource-frontier-layer.md`, because that layer already owns `CAVE_SYSTEM`, underground occupancy, subsurface connections, access state, survey, flooding, collapse and cave-rescue concepts.

The selected Pass 88 gap was thermal-site/bathhouse continuity. Neighboring systems checked before authoring include Geology, Tourism, Food/Hospitality, Care, Facility Maintenance, Public Space, Seasonality, Encounter Contracts and the Cobblemon runtime authority boundary.

## Binding runtime authority

Ouros owns:
- thermal-place identity and history;
- source/facility observations and provenance;
- persistent access/service state;
- ecological/social use records;
- explicit encounter composition and participant manifest;
- noncombat consequences and handoffs.

AutoPTU owns:
- tactical participants/teams;
- target/action legality;
- tactical position/movement;
- initiative/action economy;
- HP, status, stages and effects;
- damage/healing;
- Move/Ability/Item/Trainer Feature behavior;
- forced movement/interception/reactions;
- tactical AI;
- battle result.

Minecraft/Cobblemon/Craftics may adapt or present:
- water/block geometry;
- particles, sounds and environmental visuals;
- doors/signs/barriers and facility props;
- Pokémon entities, models, forms, poses, animations and cries;
- interaction/network transport;
- entity tracking/synchronization;
- semantic playback of AutoPTU events;
- reviewed world-state changes authorized by Ouros.

Required direction:

`Ouros thermal/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden shortcuts:

`Cobblemon nearby entity/BattleState/controller -> automatic tactical participant or battle truth`

`Minecraft hot-water/steam block -> automatic PTU healing, status, hazard or forced movement`

## PTU rest/healing boundary reviewed

PTU 1.05 already defines Rest, Extended Rest, Injury recovery limits and Pokémon Center healing.

Pass 88 therefore does not create:
- hot-spring HP healing;
- accelerated Injury removal;
- automatic status curing;
- AP/Move-frequency refresh outside PTU Rest rules;
- mineral-water or sauna buffs.

A soak may contribute to ordinary downtime only if the authoritative PTU rest/time path says the activity qualifies. The thermal-place layer does not resolve that mechanically.

## Live revisions inspected

AutoPTU-Java `main`:

`56a1563cd4a15e0cbb1e9f855587a86fa096d048`

Latest change:
`Materialize intercept candidates from authoritative rule content (#250)`

AutoPTU Python `main`:

`300dac43584bc551c4dc5aacff974f789d8dccb0`

Latest Python change:
`Career: keep Full FX inside raster budget after viewport resize (#195)`

The Python change is browser/renderer safety work. It is not evidence of a new tactical capability family.

## Java #250 evidence

Commit #250 adds `CombatantRuleContent` and `RuntimeInterceptCandidateDiscoveryFactory` so candidate-discovery inputs are materialized from server-owned battle/content state rather than adapter-supplied booleans.

The new path derives/interprets evidence such as:
- generic PTU capabilities;
- Loyalty;
- controller identity;
- HP/living state;
- team relation;
- authoritative statuses;
- Weaponize/Living Weapon;
- prepared Intercept temporary effects;
- Sentinel stance;
- Shift action budget and extra Shift count.

The class-level contract explicitly describes this content as server-owned and not derived from Minecraft/Cobblemon entities.

This is valuable evidence for the Ouros authority boundary and strengthens the Intercept pipeline. It does not establish complete Intercept execution or the full reaction/movement family.

## README caution

Current AutoPTU-Java README continues to establish:
- AutoPTU-Java decides legal actions and battle results;
- Minecraft/Cobblemon/Craftics adapt world state and render events.

Its broad incomplete checklist still includes:
- core combatant/grid battle state;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full BattleSpec -> BattleTranscript parity;
- tactical AI scoring/policy;
- Craftics/Cobblemon adapter.

Focused later commits provide stronger evidence for exact slices, especially forced movement and Intercept. They do not prove the whole permanent categories.

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

Pass 88 makes no category promotion.

## Why complete movement remains PARTIAL

Positive evidence includes:
- Shift and Jump legality;
- Push/Pull authoritative forced displacement;
- bounds, blocker and occupied-footprint partial stops;
- authoritative position mutation;
- Intercept attempt gating and authoritative input derivation;
- Intercept eligibility and check resolution;
- candidate geometry/attack-line ordering;
- successful reaction movement commitment;
- one melee Intercept + Push 1 composition;
- candidate discovery across Weaponize, prepared Intercept and Sentinel;
- candidate materialization from server-owned rule content in #250.

Still missing for family-level VERIFIED:
- complete live trigger integration across attack families;
- complete candidate ordering/selection/commit composition in all cases;
- competing reaction ordering/conflict handling;
- broad knockback coverage;
- all forced-movement sources;
- broad Move/Ability/Item/Feature integration;
- environment-driven displacement interactions;
- complete semantic transcript coverage;
- tactical AI reasoning;
- Minecraft/Cobblemon playback.

## Why terrain/weather/hazards/zones/reactions remains BLOCKING

The Intercept sequence is significant reaction work, but the permanent category also requires much broader behavior.

Still absent or family-incomplete:
- general reaction registry/lifecycle and competing reactions;
- tactical terrain ownership/state;
- tactical weather controller;
- hazards/zones with lifecycle;
- environment-driven status/damage/movement;
- thermal/water/steam mappings;
- tactical AI handling;
- adapter playback.

Therefore visible hot water, steam, wet tiles, pool edges, geothermal vents or source temperature remain world/presentation state unless a specific authoritative PTU/Caelo + AutoPTU mapping is later verified.

## Thermal-site encounter — Thermal Source Access Withdrawal

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

Reduced implementation profile:
- maintenance/survey workers withdraw before BattleSpec creation;
- source, pipes and thermal assets stay outside tactical targeting;
- Ouros selects exact combatants;
- fixed stable arena only;
- heat/steam/water remain visual/world state;
- no scripted environmental damage/status/displacement;
- technical investigation resumes after AutoPTU resolution.

## Thermal-site encounter — Bathhouse Evacuation Perimeter

Full dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if facility/wet/steam zones matter;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced implementation profile:
- all civilians evacuate before tactical resolution;
- bath zones close through Ouros world state;
- battle uses a dry fixed service/access arena;
- no civilian-protection objective is claimed mechanically;
- no slippery floor, scalding, steam concealment or pool interaction is scripted;
- reopening remains a Facility/Maintenance/Ecology decision after combat.

## Thermal-site encounter — Warm-Outflow Boundary Dispute

Full dependencies emphasize:
- complete movement — PARTIAL for withdrawal/Intercept;
- terrain/weather/hazards/zones/reactions — BLOCKING for water/thermal boundary effects;
- AI tactical policy — BLOCKING for territorial/withdrawal priorities;
- adapter/playback — BLOCKING;
- ordinary geometry/core/action families — VERIFIED;
- lifecycle/damage/status/moves/abilities/items/features — PARTIAL as applicable.

Reduced implementation profile:
Maintenance pauses first. Workers leave. Conservation and facility systems preserve the no-work boundary. If battle occurs, Ouros explicitly chooses participants and AutoPTU resolves a static ordinary arena. Winning does not authorize clearance, displacement of wildlife or reopening.

## Cobblemon-specific implementation caution

Pass 88 identifies useful presentation candidates but does not classify concrete Cobblemon classes/APIs without code inspection in the integration repository.

Likely reusable surfaces:
- water/block presentation;
- particles/sounds;
- Pokémon entity/model/form/pose/cry presentation;
- doors/signs/barriers;
- interactions;
- UI/networking;
- tracking/synchronization/persistence hooks.

World geometry or entity observations may require an adapter before they become Ouros facts or BattleSpec inputs.

Anything functioning as Cobblemon BattleState, participant/controller/side selection, tactical legality or battle outcome remains `BATTLE_AUTHORITY_FORBIDDEN`.

## Unresolved mechanical questions

- When exactly does a bath visit qualify as PTU Rest under the project’s chosen interpretation?
- Are any PTU/Caelo Moves, Abilities, Items or Trainer Features explicitly relevant to thermal water outside ordinary combat rules?
- Which validated mechanics, if any, can represent tactical steam, heat, hot water or submerged/wet surfaces?
- What complete Intercept/reaction behavior remains before evacuation/protection scenarios are authoritative?
- What semantic events are required for safe Minecraft playback?
- Which concrete Cobblemon thermal/water/presentation APIs are safe to reuse in the integration repo?

## Unresolved canon questions

- Which Ouros regions have geothermal springs?
- What bathing customs exist by culture?
- Who operates/stewards sources and bath facilities?
- Which sites are neighborhood amenities versus visitor destinations?
- What reopening/inspection practices exist?
- What therapeutic stories or claims exist, if any?
- Where does wild Pokémon use overlap thermal infrastructure?

No answer is promoted by this snapshot.
