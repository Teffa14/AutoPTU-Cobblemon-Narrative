# Engine Readiness Snapshot — Pass 102

Status: implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Live evidence inspected

AutoPTU-Java head observed during this pass:

`fa307e722c4912b50a4d1e59b7b6a98fc29a55cc`

Latest relevant commit:

`Port generic Trainer Feature prerequisite gates (#137)`

This slice adds a Python-parity primitive for selecting Trainer Feature identities and resolving prerequisite gates such as minimum Trainer level, required classes/subclasses and required prior Features. The implementation explicitly states that frequency, cooldowns, context conditions, resources, AP spending, usage accounting and effect application remain separate contracts.

This is useful evidence that Trainer Feature discovery/prerequisite logic is moving under Java battle authority.

It does not prove:

- the complete Trainer Feature catalog;
- Feature timing/interrupt behavior;
- full Feature effects;
- social/artistic Features;
- painting/restoration mechanics;
- overworld creative Skills;
- crowd, object or public-space mechanics.

AutoPTU main observed during this pass:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Recent visible Python work remains Career-oriented and does not justify a tactical capability promotion.

The Java README continues to state that Python remains authoritative while the port is incomplete and still lists major unfinished work including full battle state/damage/status behavior, terrain/hazards/forced movement/reactions, complete hook registries/transcript parity, tactical AI and Minecraft/Cobblemon integration.

## Permanent capability map

### VERIFIED

`targeting / footprints / range / LoS`

Static tactical targeting geometry, footprint overlap, range and geometric LoS remain verified.

Pass 102 non-inference:

- a mural is not a tactical wall unless its physical surface is projected into battle geometry;
- a painted line is not a targeting boundary;
- graffiti does not block LoS;
- a sculpture is not cover by default;
- a scaffold is not targetable/interactable until a battle-object contract exists.

`base movement legality`

Established Shift/Jump and known movement-mode legality remain verified.

Pass 102 non-inference:

- painted arrows do not change movement legality;
- public-art paths are not tactical routes automatically;
- scaffolding does not create climbable movement unless exact geometry/rules support it;
- a Grafaiai mark does not create avoidance movement.

`core calculations`

Established calculation primitives remain verified.

Pass 102 adds no artistic score, reputation formula, restoration quality formula, pigment potency formula or morale modifier.

`action economy / initiative`

Established action economy/initiative remain verified.

The latest Java evidence is about Trainer Feature prerequisites, not initiative, and does not change this category.

Pass 102 non-inference:

- artist role -> initiative bonus;
- conservation worker -> extra action;
- public recognition -> action budget;
- protecting artwork -> priority.

`AI legal-action infrastructure`

Legal-choice generation remains verified.

This does not prove policy objectives such as:

- AVOID_ARTWORK;
- WITHDRAW_FROM_SURVEY;
- PROTECT_WORKERS;
- CLEAR_EXIT;
- HOLD_PERIMETER;
- DEESCALATE;
- PRESERVE_OBJECTIVE;
- LEAVE_MARKED_SITE.

### PARTIAL

`full turn / round lifecycle`

Representative phase ordering, round-start cleanup, delayed hits, field-effect progression, initiative rebuilding, Trainer AP/action reset, declared-action cleanup and Feature ordering slices exist.

Still PARTIAL because complete START/END effects, durations, interrupts, Status/Ability/Feature interactions and full transcript behavior remain unproven.

Public-art revision history is overworld time and must not be encoded as battle-round lifecycle.

`full stateful damage pipeline`

Representative authoritative damage paths exist.

Still PARTIAL.

Pass 102 non-inference:

- damaged mural -> HP damage;
- falling paint can -> damage;
- broken sculpture -> damage zone;
- scaffolding failure -> Injury;
- vandalized wall -> combat object damage.

`status lifecycle`

Representative Status slices exist.

Still PARTIAL.

Pass 102 non-inference:

- Grafaiai marking -> Poisoned;
- paint cloud -> Blinded;
- strong smell -> Confused;
- restoration solvent -> Poisoned;
- artistic shock -> Fear/Enraged;
- pigment on invisible target -> automatic Invisibility removal.

Any such interaction needs exact PTU/Caelo rules plus Java parity for the concrete behavior.

`move-specific behavior`

Representative Move slices exist.

Still PARTIAL.

`Sketch` is specifically not inferred from Smeargle's overworld painting behavior. If an encounter depends on Sketch, exact behavior must be verified first.

`abilities`

Representative Ability hooks exist.

Still PARTIAL.

Grafaiai's Poison Touch does not make surfaces it painted into Poison hazards. Technician/Own Tempo/Unburden likewise do not become artistic or public-space mechanics.

`items`

Representative held-item behavior exists.

Still PARTIAL.

Paint, brushes, cleaning materials, scaffolding, plaques, cameras and restoration equipment remain world/material objects unless an exact PTU Item definition exists.

`Trainer Features / perks`

Still PARTIAL, with stronger infrastructure evidence this pass.

The new generic prerequisite gate verifies part of Feature discovery/eligibility against Python. It does not prove Feature frequency, context, resources, AP, usage, timing or effect application.

Pass 102 non-inference:

- artist/restorer/curator/street photographer = PTU Feature;
- public-art participation grants Skill Ranks;
- a commissioned artist gains social bonuses;
- a restoration specialist can alter battle objects;
- a Trainer Feature prerequisite resolver implements the complete Trainer Feature family.

### BLOCKING

`complete movement including push / pull / knockback / interception / forced movement`

Still BLOCKING as a complete family.

Pass 102 impact:

- no true in-grid worker/civilian evacuation;
- no dynamic pursuit around a marked site;
- no protected routing around scaffolding;
- no forced displacement away from artwork;
- no live moving perimeter around a restoration project.

`terrain / weather / hazards / zones / reactions`

Still BLOCKING as a complete family.

Pass 102 impact:

- paint does not create slippery terrain;
- toxic-looking pigment does not create a Poison zone;
- a conservation perimeter does not become a tactical protected zone;
- scaffolding does not create hazard state automatically;
- rain on wet paint does not create a tactical effect;
- painted markings do not create reaction triggers;
- sculptures/walls do not become cover because they are art.

`AI tactical policy`

Still BLOCKING.

Legal actions alone do not make actors preserve artwork, avoid civilians, withdraw from observation, protect a surface, de-escalate or pursue a non-KO objective.

`Minecraft / Cobblemon / Craftics adapter and playback`

Still BLOCKING.

There is no verified end-to-end contract for projecting visual surfaces, mark revisions, temporary scaffolding, crowd state, protected work areas, Pokémon mark observations or semantic objectives into Minecraft while preserving Chronicle/world authority and AutoPTU-Java battle authority.

## Pass 102 specific overworld blockers

`VISUAL_SURFACE_IDENTITY`
Persistent surface identity independent of current texture/block projection.

`VISUAL_MARK_IDENTITY`
Stable artwork/mark ID across weathering, repainting, removal and restoration.

`VISUAL_MARK_REVISION_HISTORY`
Append-only layered revisions/palimpsest state.

`VISUAL_AUTHORSHIP_ATTRIBUTION`
Confirmed creators and evidence-backed hypotheses remain separate.

`PUBLIC_ART_PROJECT_STATE`
Commission, funding, contributors, consultation, execution and review without conflating those roles.

`VISUAL_DEPICTION_CLAIMS`
Depicted assertions remain separate from historical/canonical truth.

`POKEMON_VISUAL_MARK_OBSERVATION`
Species/individual hypotheses for marks such as Grafaiai patterns without automatic identity or mechanics.

`VISUAL_CONSERVATION_RESTORATION_STATE`
Condition/treatment history and choices without object-HP simulation.

`VISUAL_LANDMARK_RECOGNITION`
Repeated public/navigation use without automatically creating official place names or reputation.

`PLAYER_CREATED_SHARED_ART_MODERATION`
Permission, ownership/access, consent and moderation for persistent player-created visual state.

`PUBLIC_ART_TO_TOURISM_PUBLIC_SPACE`
Observed downstream effects route through existing Tourism/Public Space systems.

`PUBLIC_ART_TO_MINECRAFT_PROJECTION`
Chunk reload cannot restore old revisions, duplicate installations or erase Chronicle history.

`PUBLIC_ART_TO_BATTLE_SNAPSHOT`
A visually complex site can freeze a safe tactical arena without inventing paint/scaffold/art rules inside AutoPTU.

## Encounter dependency summary

### Underpass Mural Restoration — FULL

VERIFIED foundations:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL families if actually invoked:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING families:

- complete movement/interception/forced movement for workers/civilians and protected routing;
- terrain/weather/hazards/zones/reactions for interactive work zones/barriers;
- AI tactical policy for preserve/withdraw/avoid-objective goals;
- Minecraft/Cobblemon/Craftics adapter/playback.

REDUCED viability:

Viable with current foundations if workers leave first, scaffolding/art remain noninteractive world state, and AutoPTU receives a conventional static battle arena.

### Grafaiai Mark Survey — FULL

VERIFIED foundations:

- targeting geometry;
- base movement legality;
- core calculations;
- initiative;
- legal-action infrastructure.

PARTIAL if used:

- Status/Ability/Move behavior for any exact poison, concealment or other mechanic.

BLOCKING:

- complete movement for dynamic withdrawal/pursuit;
- tactical policy for non-KO wildlife goals;
- environment/zones if surfaces become tactical objects;
- Minecraft playback.

REDUCED viability:

Survey/identity inference stays overworld. A battle, if any, is conventional and static. Painted surfaces have no tactical poison effect.

### Plaza Overpaint Dispute — FULL

VERIFIED foundations:

- static targeting/LoS;
- base movement legality;
- calculations;
- initiative;
- legal-choice generation.

BLOCKING:

- crowd/civilian movement;
- protected-object or de-escalation policy;
- dynamic barriers/zones;
- adapter/playback.

REDUCED viability:

Evidence review, dispute and crowd clearing occur in world state. Only an optional conventional confrontation enters AutoPTU.

## Promotion decision

No permanent category is promoted in Pass 102.

The latest Java commit strengthens `Trainer Features / perks` evidence by moving generic prerequisite checks into a parity-tested Java contract, but that family remains PARTIAL because timing, resources, frequency, usage and effect application are not broadly proven.

The new public-art layer is predominantly overworld/world-state work and can advance independently of missing battle families when reduced encounter contracts are used.
