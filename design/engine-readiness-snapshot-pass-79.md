# Engine Readiness Snapshot — Pass 79

Status: implementation evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`fe9cfc5e073f444d5ef3182265f5313b4bb48e51`

Latest visible commit:

`Freeze delayed-hit execution call-chain contract (#113)`

Parent inspected in Pass 78:

`3906892c11129c419e702d87ff71db071c12050f`

The new Java slice freezes how a matured delayed hit enters target resolution and then re-enters the ordinary move-action resolver. It adds Python-oracle parity coverage for that call chain.

AutoPTU Python oracle inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its latest visible commit remains Career-oriented (`Career: make roster recovery deterministic`) and does not change the tactical classification below.

## What Pass 79's new Java evidence proves

The latest Java commit strengthens evidence that:

- delayed-hit execution has an explicit language-neutral contract;
- matured delayed hits enter target resolution rather than a special lower-level damage path;
- target ID and target position are forwarded through that boundary;
- target resolution is expected to re-enter the normal move-action resolver;
- Python parity now checks the call-chain policy.

It does not prove:

- complete delayed-hit runtime execution for every Move;
- all frequency/action-economy interactions for delayed Moves;
- all delayed target invalidation cases;
- full move-specific behavior;
- full turn/round lifecycle;
- full damage/status pipelines;
- herd movement or retreat behavior;
- stampede/trampling;
- dynamic grassland terrain;
- tactical AI;
- Minecraft/Cobblemon playback.

## Java README boundary

The live README still explicitly lists as unfinished:

- core combatant/grid battle-state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the primary no-overclaim guardrail.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

Range, target anchors, areas, footprints and geometric LoS remain verified for the ported surface.

Pass 79 guardrail:

Geometric LoS does not establish visibility through tall grass, herd bodies as cover, dust raised by movement or sight changes caused by vegetation height.

### base movement legality

Current evidence covers Shift legality using Overland/Swim/Sky, terrain costs, blockers, Wallrunner, sprint, Jump foundations and landing fit.

Pass 79 guardrail:

This does not prove herd movement, group crossing, stampede flow, fence interactions, mounted herding or actor displacement by other moving creatures.

### core calculations

PTU calculation primitives remain verified for the implemented surface.

Pass 79 guardrail:

A `grassland` environment label or terrain-cost primitive does not create grazing, pasture, forage, trampling, cover or grass-height mechanics.

### action economy/initiative

VERIFIED.

Canonical initiative entry/order, ordering modes, round rebuild and default lifecycle rollover remain server-authoritative.

The delayed-hit call-chain contract does not promote full lifecycle.

### AI legal-action infrastructure

Deterministic `BattleChoice` legality remains available for supported actions and targets.

It does not establish herd goals such as CROSS, WITHDRAW, KEEP_DISTANCE, RETURN_TO_HANDLER, PROTECT_CALF or AVOID_ROAD.

## PARTIAL

### full turn/round lifecycle

Java has substantial phase, round, cleanup, initiative and effect-hook infrastructure. Pass 79 adds stronger delayed-hit call-chain evidence, but complete lifecycle and BattleSpec -> BattleTranscript parity remain unfinished.

### full stateful damage pipeline

Multiple damage, accuracy and post-damage slices exist. Full resolution remains explicitly unfinished.

### status lifecycle

Selected application, phase and expiry behavior has parity evidence. The complete controller remains unfinished.

Pass 79 guardrail:

No generic `trampled`, `panicked`, `stampeded`, `exhausted from grazing`, `herd morale` or `pasture fatigue` status exists by implication.

### move-specific behavior

Selected move contracts and behaviors exist. The delayed-hit call-chain contract improves one family of move execution but does not demonstrate the full Move library.

### abilities

Multiple Ability hook families and representatives exist with parity. Full coverage is not demonstrated.

Pass 79 guardrail:

Sap Sipper, Run Away, Reckless, Fluffy or species flavor cannot be reused as generic grazing/herd simulation primitives.

### items

Representative held-item state/effects exist. Full item behavior remains incomplete.

### Trainer Features/perks

Runtime state, hook infrastructure and representative Features exist. Full Classes/Features/Edges/Orders are not demonstrated.

Pass 79 guardrail:

No generic shepherding, ranching, mounted-herding or grassland-management Feature is assumed implemented.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

Still BLOCKING as a family.

Pass 79 needs this category for:

- actors physically intercepting a herd;
- stampede or crowd displacement;
- forced relocation caused by moving groups;
- tactical containment at gates/fences;
- crossing-lane control;
- rescue/protection where civilians/herds move during combat.

Reduced versions should resolve herd routes before battle and freeze one static geometry.

### terrain/weather/hazards/zones/reactions

Still BLOCKING as a family.

Pass 79 specifically requires this category for any future authored mechanic involving:

- grass-height cover;
- trampled/worn zones;
- dynamic pasture/vegetation terrain;
- dust zones from herd movement;
- wallow/mud hazards;
- fire-grazing battlefield transitions;
- fence/gate interactables with tactical effects;
- reaction windows around moving herd actors.

Until verified, grassland condition remains world state and presentation outside tactical rules.

### AI tactical policy

Still BLOCKING.

Legal actions exist, but AI cannot be assumed to understand:

- herd crossing/withdrawal;
- keeping a collective together;
- protecting juveniles;
- avoiding roads or handlers;
- moving toward water/forage;
- de-escalation;
- surrender/return-to-handler goals;
- observation objectives.

### Minecraft/Cobblemon/Craftics adapter/playback support

Still BLOCKING.

The Java README continues to state that the project is not yet a Minecraft mod and that the adapter follows a parity-safe core slice.

Minecraft must not decide grazing pressure, herd identity, pasture condition or PTU environmental effects.

# Pass 79 grassland-specific authority boundary

Available project evidence supports these narrow statements:

- Python AutoPTU recognizes a semantic `grassland` environment label;
- selected authored effects read that label;
- tactical movement foundations include Overland and Naturewalk-related state in the Python oracle;
- Java has verified static movement legality for the currently ported surface;
- Java has verified action economy/initiative foundations;
- Java now has a parity-frozen delayed-hit call-chain contract.

Those facts do not establish a generic grassland/rangeland subsystem.

No verified general subsystem was found for:

- grazing pressure;
- browsing;
- pasture capacity;
- herd route planning;
- managed-herd ownership/custody behavior;
- forage consumption/recovery;
- trampling;
- stampede;
- grass-height cover;
- wallowing;
- watering behavior;
- herd leadership;
- group morale;
- shepherding;
- fence/gate containment;
- range-rest recovery;
- grazing-driven Cobblemon spawning.

Caelo primary material was not reliably available for a dedicated grazing/rangeland rule during this run, so no Caelo-specific mechanic is asserted.

# Pass 79 encounter dependencies

## Waterpoint Crossing — FULL

Required capability categories and live state:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED for static movement;
- complete movement/push/pull/knockback/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if exact PTU statuses are involved;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

Resolve collective timing and movement in world state before battle. Use one static arena containing only actual combatants. No stampede, herd morale, trampling or dynamic waterpoint occupancy mechanic is inferred.

## Burn Patch Survey — FULL

Required capability categories:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception — BLOCKING for moving-group goals;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- stateful damage/status/move/Ability/item/Feature families — PARTIAL as applicable;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:

Resolve Wildfire/Flora/grassland state first. Freeze one safe geometry. Survey progress remains world state. AutoPTU is invoked only for a conventional conflict.

## Broken Fence at Dusk — FULL

Required capability categories:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- damage/status/move/Ability/item/Feature families — PARTIAL;
- terrain/hazards/zones/reactions — BLOCKING for dynamic gates/road control;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:

Resolve herd location, road closure and fence repair outside battle. Any hostile encounter occurs separately on a fixed map.

# Pass 79 overworld blockers

These are outside the Java battle core and remain BLOCKING as world-system contracts:

- `GRASSLAND_SYSTEM` persistent state;
- grazing-unit spatial/history state;
- herbivore-use observations;
- managed-herd identity/custody links;
- grazing-pressure revisions;
- congregation hotspots;
- herd-route revisions;
- range-use plans;
- fire/drought/soil/freshwater coupling;
- grassland → Cobblemon projection;
- grassland → battle snapshot projection.

# No-inference rules

- Implemented delayed-hit execution contracts do not imply herd AI.
- `grassland` labels do not imply Grassy Terrain.
- short grass does not imply Rough Terrain or easier movement.
- tall grass does not imply cover or concealment.
- a herd does not share initiative unless an exact rule says so.
- loaded Cobblemon count does not define herd population.
- Sap Sipper does not simulate grazing.
- Run Away does not implement group withdrawal.
- Pack Mon, if present in rules, must be validated individually and cannot be inferred from narrative group membership.
- Mountable must be validated per rules and does not imply passenger transport or ranch work.

# Unresolved mechanical/canon questions

- Exact PTU/Caelo text for Naturewalk (Grassland), Pack Mon, Mountable and any herd-handling Features.
- Whether any authored rule treats tall grass, pasture or trampled ground as tactical terrain.
- Whether any future AutoPTU objective vocabulary should include CROSS, WITHDRAW, ESCORT, CONTAIN or PROTECT_GROUP.
- How wild-collective identity maps to representative Cobblemon entities.
- How managed-herd custody/ownership should be represented outside battle.
- Which Ouros regions have grasslands, ranching cultures or long-lived herd routes at campaign start.
- How much grassland recovery advances offline.
- How grassland state couples with Wildfire, Aridity, Soil, Freshwater and Flora without double-authority.