# Engine Readiness Snapshot — Pass 113

Status: EVIDENCE SNAPSHOT. This file records live implementation evidence used by narrative authoring. It does not change engine capability status by itself.
Date: 2026-08-28

## Read-only repositories inspected

AutoPTU-Java head inspected:

`f54ebc6862c3238e4e424da879fa99a93c0c46c1`

PR #264 / commit: `Validate declared move before pre-resolution target replacement`.

AutoPTU head inspected:

`f1c81f5a20dfdbd4986e1c28083d9bbeb2f71bd1`

PR #221 / merge: `Career: harden malformed initial battle grid`.

Neither repository was modified by this pass.

## Java live evidence

Java advanced from Pass 112 head `9f63f0a81af45af2fbc87928b96c1cec4fcff4b0` to `f54ebc6862c3238e4e424da879fa99a93c0c46c1`.

The new server-owned boundary revalidates the controller's declared Move choice against the declared target before invoking PRE-resolution target replacement. After that legality gate succeeds, a replacement such as Intercept may replace the effective defender and rebuild defender-bound preparation without pretending the replacement is a second controller declaration.

Tests added in the commit cover declared-target legality before target replacement and the validated preparation path.

This is meaningful composition work across legal declaration and one pre-resolution target-replacement path. It remains narrow evidence.

It does not demonstrate completion of:

- broad Push/Pull;
- broad Knockback;
- every forced-movement source;
- environmental displacement;
- generalized competing reactions;
- generalized reaction ordering outside implemented target-replacement paths;
- every Move registration;
- every Ability registration;
- every Item registration;
- every Trainer Feature/perk registration;
- complete environmental hazard/zone semantics;
- objective-aware tactical policy;
- semantic Minecraft/Cobblemon/Craftics playback.

Do not promote a permanent family because one representative path is increasingly well composed.

## AutoPTU live evidence

AutoPTU advanced from Pass 112 head `6776984aa4a19449b85858a8bc61a18671e5551b` to `f1c81f5a20dfdbd4986e1c28083d9bbeb2f71bd1`, PR #221.

Career now treats a legacy initial battle state as structurally usable only when `combatants` is an array and the grid is an object with finite positive width and height. Malformed inputs fall back to a small valid empty BattleFrame shape.

This is replay/API stability and backward-compatibility hardening. It does not add tactical targeting, movement, damage, status, reactions, AI policy or adapter semantics.

No capability promotion follows.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No permanent category is promoted in Pass 113.

## Pass 113 concept boundary

Volcanic monitoring and recovery are primarily overworld information/world-state systems.

Observations, assessments, notices, access reviews, ashfall reports and downstream recovery handoffs remain outside AutoPTU unless an actual encounter deliberately requires tactical environmental effects.

The narrative layer must not convert volcano presentation into battle rules.

## Encounter 1 — Monitoring Ridge Withdrawal

Full intended dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL for timed withdrawal
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when exact legal effects apply
- terrain/weather/hazards/zones/reactions: BLOCKING for generalized reactions, ash/heat/unstable-ground effects or changing restricted zones
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for withdrawal/protection behavior
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

Additional objective contract: withdrawal/protection semantics are not verified as a complete tactical policy.

Reduced version:

Complete staff withdrawal before BattleSpec creation. Keep active volcanic processes, monitoring equipment and unstable sectors outside the grid. Resolve combat in a static reviewed clearing with explicit combatants. Victory can establish only immediate route security. Volcanic assessment and access decisions continue in their own world-state workflows.

## Encounter 2 — Ashfall Shelter Perimeter

Full intended dependencies:

The verified core remains available. Protection/Intercept/forced movement remains PARTIAL when used. Generalized reactions, ash zones, obscuration zones or active environmental restrictions require the BLOCKING environmental family. Objective-aware protection needs BLOCKING tactical policy. Semantic playback remains BLOCKING.

If ash is intended to change LoS, movement, damage or status, authoring also needs:

- an exact governing PTU/Caelo rule for that effect;
- targeting/range/LoS support if visibility changes: VERIFIED family, but the specific ash rule is unverified;
- full stateful damage pipeline where damage applies: PARTIAL;
- status lifecycle where a status applies: PARTIAL;
- complete movement where forced/slowed displacement applies: PARTIAL;
- full turn/round lifecycle for accumulating or delayed phases: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING.

Reduced version:

Move noncombatants to an authored covered or post-event inspected location before battle. Keep ash as world-state evidence and inert presentation. Resolve a static perimeter fight. The result does not certify health, occupancy, transport, cleanup or utility state.

## Encounter 3 — Old Flow Observation Route

Full intended dependencies:

If hardened volcanic terrain is tactically inert, the encounter can use verified static geometry.

If the design introduces active heat, lava/magma, volcanic gas, unstable crust, falling material, delayed venting, moving flow or changing zones, it requires:

- terrain/weather/hazards/zones/reactions: BLOCKING;
- full stateful damage pipeline: PARTIAL where damage applies;
- status lifecycle: PARTIAL where conditions apply;
- complete movement: PARTIAL where displacement/sliding/collapse movement applies;
- full turn/round lifecycle: PARTIAL where phases or delayed effects apply;
- move/ability/item/Trainer Feature behavior: PARTIAL when those systems interact;
- AI tactical policy: BLOCKING if agents must reason around changing environmental risks;
- adapter/playback: BLOCKING.

Reduced version:

Treat the old flow field as stable static terrain with no special tactical effect. Investigation uses maps, observations and historical provenance outside combat. Any encounter uses ordinary reviewed geometry.

## Volcanic mechanical unknowns

Current PTU/Caelo plus live engine evidence does not verify a universal contract for:

- natural volcanic eruption timing;
- eruption prediction mechanics;
- volcanic alert thresholds;
- ashfall visibility penalties;
- ash inhalation or respiratory status;
- ash accumulation modifying movement;
- lava/magma environmental damage;
- proximity heat damage;
- volcanic gas exposure;
- lahar or lava-flow forced movement;
- unstable crater edges;
- falling ejecta or volcanic-bomb damage;
- dynamic fissures;
- structural collapse from eruption;
- delayed eruption/vent phases;
- automatic Fire- or Ground-type environmental immunity;
- species-derived eruption sensing;
- Pokémon-caused eruption control from flavor alone;
- Move/Ability/Item/Trainer Feature-powered volcanic control without exact rules;
- rescue/carry under active volcanic hazards;
- objective-aware evacuation/withdrawal semantics.

These remain UNKNOWN rather than being fabricated by Narrative or the Minecraft adapter.

## PTU/Caelo guardrail

The internal source scan remains controlling. Caelo demonstrates that a specific location can have mechanical identity when the governing source explicitly defines the effect. That does not authorize universal rules such as `lava block = PTU damage`, `ash = LoS penalty`, `volcano = heat zone`, `Fire type = safe`, or `Absol = eruption predictor`.

Before any volcanic condition enters BattleSpec mechanically, authoring needs both:

1. an exact governing PTU/Caelo source for the intended effect; and
2. current engine tests/contracts supporting every permanent capability family that effect requires.

Otherwise the condition remains overworld state, inert scenery or is removed from the reduced tactical arena.

## Minecraft/Cobblemon/Craftics boundary

Presentation can reuse volcanic terrain, lava/fire visuals, ash/smoke/steam particles, monitoring structures, signs, barriers, old flow fields, route changes, NPC crews, Pokémon models/forms/poses/animations/cries, sounds, UI, networking, tracking and persistence hooks.

The adapter must preserve authoritative IDs for volcanic system, monitoring node, observation, assessment, episode, ashfall observation, access sector and recovery handoff where those objects exist.

Presentation must not infer authority from visuals:

- Minecraft lava does not execute PTU damage by default;
- Minecraft fire does not automatically inflict Burn;
- smoke/ash particles do not create status or LoS penalties;
- native weather does not create volcanic ashfall state;
- falling blocks do not execute PTU damage or collapse rules;
- native entity knockback does not execute PTU forced movement;
- a Fire- or Ground-type Pokémon inside a hot area does not prove immunity;
- redstone does not establish monitoring truth, assessment or notice authority;
- a closed gate does not prove the scientific reason for closure;
- Cobblemon BattleState/controller logic does not select combatants or decide legality, HP/status, positions or results.

Ouros owns world facts and combatant selection. AutoPTU owns tactical legality and resolution. Minecraft/Cobblemon/Craftics presents authoritative outcomes.

## Canon questions carried forward from Pass 113

Unresolved setting questions include:

- which Ouros regions contain volcanic systems;
- which are active, background-active, dormant or historical according to authored setting terms;
- which settlements, routes, farms, habitats, sacred sites, resorts or institutions depend on them;
- which monitoring technologies exist;
- who operates observation networks;
- who may issue scientific assessments, public warnings and access restrictions;
- whether ash has cultural, agricultural, industrial or ritual uses anywhere;
- which historical episodes changed routes, settlements or habitats;
- how long post-event monitoring/review persists;
- what volcanic folklore exists and how it relates to evidence;
- individual Pokémon relationships with volcanic sites;
- any exact mechanical volcanic effects supported by PTU/Caelo.

## Promotion rule

PR #264 strengthens the legal declaration → pre-resolution target replacement composition path. It does not complete all Intercept, forced movement or reaction semantics. Do not promote movement/reactions, environmental mechanics, tactical policy or adapter support without broad tested contracts.

Pass 113 therefore leaves the permanent map unchanged.
