# Engine Readiness Snapshot — Pass 87

Status: implementation evidence snapshot, not canon.
Date: 2026-08-28

## Scope

Supports:
- `design/forestry-managed-woodland-harvest-restoration-extension.md`;
- `proposals/2026-08-28-forestry-managed-woodland-seeds-87.md`.

Writable repository:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Internal project review

The complete recursive Narrative tree at Pass 86 head `7e15eb9a03a87aebed94cd19926d000c11d7a8e8` was inspected before topic selection. GitHub returned `truncated=false`.

The inventory showed that geology/excavation already had dedicated research, design and proposals from Pass 33. That candidate topic was rejected as duplicate.

No forestry/managed-woodland design/research/proposal set existed. Relevant neighboring systems were opened or checked before authoring, including Conservation, Material Culture, Food/Agriculture, Workplaces, Worksite Safety, Pokémon Work, Travel, Wild Ecology, Weather/Crisis, Waste/Pollution, Geology and the Cobblemon authority boundary.

## Binding runtime authority

Ouros owns:
- woodland identity and world-state history;
- observations and provenance;
- management/intervention records;
- route/work/ecology handoffs;
- encounter composition and explicit participant manifest;
- persistent narrative consequences.

AutoPTU owns:
- tactical participants and teams;
- target/action legality;
- tactical positions and movement;
- initiative/action economy;
- HP/status/combat stages/effects;
- damage/healing;
- Move/Ability/Item/Trainer Feature behavior;
- reactions/interception;
- tactical AI;
- battle result.

Minecraft/Cobblemon/Craftics may adapt or present:
- logs/leaves/saplings and other blocks;
- paths, fences, gates, signs and worksite props;
- Pokémon entities, models, forms, poses, animations and cries;
- weather/particles/sounds as presentation;
- interaction/network transport;
- entity tracking/persistence hooks;
- semantic playback of AutoPTU events;
- reviewed world-state changes after Ouros authorizes them.

Required direction:

`Ouros woodland/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden shortcuts:

`Cobblemon nearby entity/BattleState/controller -> automatic tactical participant or battle truth`

`Minecraft block break -> automatic authorized harvest/yield`

## Live revisions inspected

AutoPTU-Java `main`:

`db437c1942272083200d60e928a77443bfd93b24`

Latest relevant change:
`Freeze intercept candidate discovery contract (#249)`

AutoPTU Python `main`:

`533e76eb678208cda6990f276343bf313d5d473e`

Latest Python change:
`Career: coalesce concurrent battle transcript loads (#193)`

The Python change improves Career/browser concurrency around transcript loading. It is not evidence of a new tactical capability family.

## Java #249 evidence

The new `InterceptCandidateDiscoveryResolution` freezes a parity-backed candidate-discovery policy before distance ordering, skill checks, RNG or movement.

The contract handles evidence such as:
- active/expired No-Intercept entries;
- exclusion of the protected target itself;
- living/same-team checks;
- Weaponize/Living Weapon candidate source;
- prepared Intercept entries matching ally and melee/ranged kind;
- Sentinel stance candidate discovery;
- base/extra Shift availability;
- Intercept eligibility and Loyalty requirements;
- cleanup of expired Sentinel/No-Intercept entries.

Most importantly for the Minecraft integration, the class documentation states that team, HP, ability/capability, temporary-effect, loyalty and action-budget inputs must come from `BattleRuntimeState`, and that Minecraft/Cobblemon must never mark an interceptor as prepared or eligible.

This strengthens the authoritative Intercept pipeline and the runtime boundary. It does not prove complete Intercept execution or the broader reaction family.

## README caution

The current AutoPTU-Java README still defines the architecture as:
- AutoPTU-Java decides legal actions and battle results;
- Minecraft/Cobblemon/Craftics adapt world state and render resulting events.

Its broad checklist still leaves incomplete:
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

Focused commits after that checklist give stronger evidence for their exact slices. They do not complete the permanent families.

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

Pass 87 makes no category promotion.

## Why complete movement remains PARTIAL

Positive evidence now includes:
- Shift/Jump legality;
- Push/Pull forced displacement;
- collision/bounds/occupied-footprint partial stops;
- authoritative position mutation;
- Intercept attempt gate;
- authoritative attempt-input derivation;
- Intercept eligibility;
- Intercept check resolution;
- candidate geometry/attack-line ordering;
- successful reaction movement commitment;
- one melee Intercept + Push 1 composition;
- Intercept candidate discovery across Weaponize/prepared/Sentinel sources.

Still missing for family-level VERIFIED:
- end-to-end trigger integration across attack families;
- complete candidate ordering/selection/commit composition in the live runtime;
- competing reaction ordering/conflict handling;
- broad knockback coverage;
- all forced-movement sources;
- broad Move/Ability/Item/Feature integration;
- terrain/environment displacement interactions;
- complete semantic transcript coverage;
- tactical AI reasoning;
- Minecraft/Cobblemon playback.

## Why terrain/weather/hazards/zones/reactions remains BLOCKING

The Intercept sequence is significant reaction-like progress but does not establish the combined family.

Still absent or family-incomplete:
- general reaction registry/lifecycle;
- competing reactions;
- tactical terrain ownership/state;
- tactical weather controller;
- hazards/zones with lifecycle;
- environment-driven status/damage/movement;
- tactical AI handling;
- adapter playback.

A forest storm, falling branch, smoke, fire, unstable tree, dense understory or wet ground may therefore exist as world/presentation state but cannot receive tactical damage, Accuracy, status, forced movement or zone effects without an exact reviewed AutoPTU mapping.

## Forestry-specific PTU/Caelo caution

Pass 87 does not establish universal mechanical forestry rules.

Before executable use, source review is required for any claim that a Move, Ability, Capability, Skill, Item or Trainer Feature can:
- fell or clear a tree;
- move timber;
- clear vegetation;
- control fire;
- harvest a material;
- alter terrain in combat;
- accelerate growth/restoration;
- grant a forest-specific combat modifier.

A visual action in Minecraft/Cobblemon cannot fill this gap.

## Encounter — Windthrow Route Withdrawal

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
- workers leave before BattleSpec creation;
- unstable woodland stays closed in world state;
- fixed legal arena only;
- Ouros explicitly chooses combatants;
- no scripted falling-tree, branch, wind or debris mechanics;
- post-battle clearance/restoration stays outside AutoPTU.

## Encounter — Restoration Crew Boundary Conflict

Full dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL when withdrawal/protection needs it;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for tactical vegetation/restoration zones;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced implementation profile:
- crew/tools/seedlings/noncombatants leave the tactical grid first;
- encounter uses fixed legal geometry or resolves noncombatatively;
- battle result does not determine ecological cause or management authority.

## Noncombat investigation — The Missing Cut Mark

No tactical engine dependency is required for the core investigation.

It can execute through:
- observations;
- provenance;
- work records;
- maps/boundary revisions;
- photographs;
- weather history;
- testimony.

Any later battle generated by the investigation receives its own explicit contract.

## Cobblemon forestry surface classification

Preliminary classifications only; exact classes/events require source inspection in the integration repository.

```yaml
cobblemon_forestry_surface:
  pokemon_models_forms_poses_cries: SAFE_REUSE_CANDIDATE
  vanilla_blocks_logs_leaves_saplings_paths: SAFE_REUSE_CANDIDATE
  ambient_audio_particles_weather_visuals: SAFE_REUSE_CANDIDATE
  block_change_hooks_as_world_input: ADAPTER_REQUIRED
  aggregate_woodland_to_visible_block_projection: ADAPTER_REQUIRED
  wild_spawn_entity_observations_as_world_input: ADAPTER_REQUIRED
  nearby_entity_as_tactical_participant_authority: BATTLE_AUTHORITY_FORBIDDEN
  cobblemon_battle_state_controller: BATTLE_AUTHORITY_FORBIDDEN
  exact_api_classes_events: UNKNOWN_REVIEW_REQUIRED
```

## No false completion

Pass 87 does not treat:
- one Intercept policy as full reaction support;
- a `terrainBonus` input somewhere as terrain implementation;
- visual forest geometry as PTU terrain;
- Minecraft fire as PTU hazard damage;
- block breaking as a production mechanic;
- a Pokémon animation as proof of a legal work capability;
- legal action generation as tactical AI;
- semantic Java state as Minecraft playback.

## Unresolved implementation questions

- Which exact PTU/Caelo rules, if any, govern forestry-related clearing, carrying and environmental work?
- Which Cobblemon/vanilla hooks can safely project reviewed woodland interventions without treating raw block changes as authority?
- What is the minimum semantic event set needed to animate Intercept/forced movement correctly in wooded battlefields?
- How should aggregate woodland patches map to Minecraft block persistence without tracking every tree?
- Which forest-state changes should influence Cobblemon spawn/ecology presentation, and through which adapter boundary?

No answer is promoted by this snapshot.