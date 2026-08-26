# Engine Readiness Snapshot — Pass 176

Status: live evidence snapshot for narrative dependency tagging
Date: 2026-08-26
Narrative topic: Pokémon spatial ecology, home ranges, site fidelity and territoriality

AutoPTU-Java and AutoPTU are READ-ONLY for this task.

## Live repository heads inspected

### AutoPTU-Java

Head inspected: `a9fb0d81238e69a5263f074b4a8ad8ef1905325d`
Commit: `Route seven Combat Stages through authoritative hooks (#215)`

This slice migrates the Combat Stage hook/mutation path to seven-stat identity, including Accuracy and Evasion. It applies secondary Accuracy/Evasion through the authoritative mutation service and includes parity/runtime coverage for the new path and Mirror Armor reflection.

Evidence gained:

- canonical seven-stat Combat Stage state is stronger;
- Accuracy/Evasion no longer need the previous separate side path for this contract;
- secondary Combat Stage application can use the same prevention/reflection/mutation seam for all seven stages under the tested contract;
- representative Ability prevention/reflection behavior has additional parity evidence.

Evidence not gained:

- the full Ability catalog;
- the full Move catalog;
- the full Status controller;
- generic reactions;
- generic forced movement/interception;
- complete damage resolution;
- tactical AI policy;
- Minecraft/Cobblemon/Craftics integration.

The current Java README still marks these major areas incomplete: core combatant/grid battle state, full damage resolution, status controller, terrain, hazards, forced movement, reactions, remaining move/ability/item/perk/Trainer Feature registries, full transcript parity, AI scoring/policy and Craftics/Cobblemon adapter work.

### AutoPTU Python oracle

Head inspected: `9fedd2efa5d0f2dc3229617e665533f2f2555897`
Commit: `fix(career): harden legacy decision history before render`

The newest visible Python change is Career presentation/persistence hardening. It does not justify any change to battle capability classification.

## Permanent capability map

### VERIFIED

1. targeting / footprints / range / LoS
2. base movement legality
4. core calculations
5. action economy / initiative
14. AI legal-action infrastructure

Interpretation: these families have sufficiently broad current contracts for narrative dependency planning, while still respecting the exact engine boundaries.

### PARTIAL

6. full turn / round lifecycle
7. full stateful damage pipeline
8. status lifecycle
10. move-specific behavior
11. abilities
12. items
13. Trainer Features / perks

Interpretation: representative slices exist, sometimes with strong parity tests, but one implemented mechanic or hook is never evidence that the whole family is complete.

### BLOCKING

3. complete movement including push / pull / knockback / interception / forced movement
9. terrain / weather / hazards / zones / reactions as a complete family
15. AI tactical policy
16. Minecraft / Cobblemon / Craftics adapter / playback support

Interpretation: mechanically rich encounter designs depending on these families need explicit FULL dependency tags and normally a REDUCED version.

## Why Pass 176 does not promote anything

Spatial ecology is world-state interpretation. The new Java Combat Stage slice does not implement territorial behavior, pursuit, patrol, home ranges, ecological withdrawal, site fidelity, range boundaries, non-hostile objectives or Minecraft projection.

Battle LoS must not be reused as ecological visibility or observation coverage.

Base movement legality must not be mistaken for complete movement objectives.

AI legal-action infrastructure can enumerate legal battle choices. It does not yet supply ecological/tactical policies such as:

- `WITHDRAW_FROM_INTRUDER`;
- `HOLD_DISPLAY_DISTANCE`;
- `RETURN_TO_CORE_AREA`;
- `CROSS_TO_RESOURCE`;
- `AVOID_HUMAN_TEAM`;
- `PROTECT_ROUTE_WITHOUT_KO`;
- `STOP_CHASE_AT_BOUNDARY`.

Those require AI tactical policy and, in many cases, complete movement.

## Pass 176 encounter dependency review

### Territorial Display at Shared Waterpoint — FULL

VERIFIED dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL dependencies if combat uses them:

- full lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING dependencies:

- complete movement for dynamic chase, withdrawal, crossing or interception;
- AI tactical policy for display/withdrawal/non-KO goals;
- Minecraft/Cobblemon/Craftics adapter/playback;
- terrain/weather/hazards/zones/reactions if water, mud, protected areas or environmental change has tactical meaning.

REDUCED version:

Resolve field-team evacuation and background Pokémon movement in world state. Freeze a static dry battle arena without territory/water mechanics. Use AutoPTU only for actual combatants. Update the territorial-behavior observation separately from victory.

### Range Survey at New Wildlife Crossing — FULL

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement for crossing/withdrawal/interception;
- AI tactical policy for `CROSS`, `AVOID_CONFLICT`, `WITHDRAW`, `REACH_OBSERVATION_POINT`;
- adapter/playback;
- environmental family if traffic/barriers/zones change tactical legality.

REDUCED version:

Run crossing behavior entirely as world state. If an independent conflict occurs, halt traffic/background movement and use a static legal arena.

### Familiar Individual Beyond Historic Range — FULL

VERIFIED:

- targeting/footprints/range/LoS if combat begins;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

BLOCKING:

- complete movement for follow/withdraw/interception;
- AI tactical policy for observation and avoidance objectives;
- adapter/playback;
- environmental family only if landscape state becomes tactical.

REDUCED version:

Resolve identification and movement outside combat. Preserve the distant record as an `EXCURSION_EVENT`. Open a static battle only for a separate real threat.

### Range Reconciliation Workshop

No battle engine dependency. Science, Telemetry, Metrology and spatial ecology can legitimately conclude that several spatial products have different scopes or remain unresolved.

## PTU/Caelo boundary for spatial ecology

No generic battle mechanic is introduced by Pass 176.

Explicitly forbidden narrative-to-mechanics conversions:

- territory -> Pack Mon;
- territoriality -> Intimidate;
- patrol -> free Shift;
- boundary crossing -> Intercept;
- chase -> forced movement;
- core-use area -> defensive zone;
- range overlap -> ally state;
- site fidelity -> Loyalty;
- known range -> Accuracy, Initiative, surprise or capture modifier;
- scent mark -> Tracker lock;
- species lore -> universal individual behavior;
- ecological range -> battle range.

The AutoPTU repository contains PTR2e/Foundry material for terms such as Pack Mon in addition to PTU data. Such material cannot be silently treated as PTU/Caelo authority.

A reliable complete Caelo source defining home ranges or territoriality was not recovered during this pass. Super PTU Online Helper was not available as an invocable capability.

## Adapter boundary

Minecraft may eventually render recurring presence, observation stations, public coarse maps, visible marks or local commentary. It must not generate scientific truth.

Forbidden adapter authority:

- entity positions -> home-range polygon;
- mob aggro radius -> territory radius;
- despawn -> departure;
- chunk presence -> residency;
- pathfinding loop -> patrol evidence;
- block boundary -> defended-area boundary;
- KO/capture -> territory removal;
- map marker -> ecological assessment;
- player food drops -> immediate range expansion.

## Readiness conclusion

Pass 176 is safe to advance as worldbuilding and persistent world-state design now.

Its reduced encounters can use static AutoPTU battles while all spatial interpretation remains outside the battle engine.

Its full dynamic encounters remain blocked mainly by complete movement, tactical AI and the Minecraft/Cobblemon/Craftics adapter, with the environmental family additionally blocking any version that makes water, barriers or defended zones tactically active.