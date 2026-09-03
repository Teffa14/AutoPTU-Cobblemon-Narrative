# Ouros human disturbance and habituation gradient contract

Status: PROPOSED DESIGN CONTRACT
Date: 2026-09-03
Pass: 236

## Purpose

Represent repeated human exposure as persistent ecology state without treating proximity as taming, hostility or combat.

## Core invariants

1. Species baseline remains a prior, not a script.
2. Harmless exposure, harmful exposure, resource subsidy and welfare cost are distinct dimensions.
3. Behavioral tolerance does not imply ecological health.
4. Minecraft/Cobblemon observations can provide inputs but cannot author canonical population truth.
5. Any structured tactical encounter requires an explicit Ouros handoff to AutoPTU.
6. Individual learning may diverge from population-level tendency.

## Disturbance vector

Each ecology site may expose a population to a normalized vector:

```text
foot_traffic
vehicle_or_machine_noise
artificial_light
food_or_waste_subsidy
deliberate_feeding
pursuit_or_harassment
capture_pressure
battle_pressure
construction_pressure
```

Do not collapse this vector into a universal danger score before species/individual response is evaluated.

## Persistent response state

Recommended state shape:

```text
population_id
site_id
human_tolerance_baseline
harmless_exposure_memory
harmful_exposure_memory
resource_subsidy_affinity
vigilance_pressure
avoidance_pressure
activity_shift_pressure
welfare_cost
capture_conflict_pressure
last_exposure_tick
last_harmful_tick
last_observation_tick
```

Persistent individuals may override population values with their own exposure memories.

## Evaluation order

```text
species/population baseline
+ individual exposure history
+ current life stage/condition
+ nesting/juvenile context
+ current disturbance vector
+ recent alarm/territorial state
+ available natural resources
+ anthropogenic resource subsidy
= behavioral pressure set
```

Candidate world intents:

```text
TOLERATE
OBSERVE
RETREAT
REROUTE
HIDE
SHIFT_ACTIVITY_WINDOW
FORAGE_NEAR_HUMANS
EXPLOIT_ANTHROPOGENIC_RESOURCE
WARN
DEFEND
RELOCATE
```

These are ecology intents. They are not PTU statuses and must not directly change battle stats.

## Habituation and sensitization

Repeated low-harm exposure may increment `harmless_exposure_memory` and lower avoidance for compatible populations/individuals.

Repeated harmful exposure may increment `harmful_exposure_memory`, increase avoidance, shift activity or create sensitization.

Both memories decay over time using implementation-configured curves. The contract intentionally does not freeze a numeric formula yet.

An individual may become more tolerant while `welfare_cost` remains elevated. Projection code must therefore never infer welfare from approach distance alone.

## Anthropogenic resource subsidy

Human sites can create food, shelter, warmth, artificial water or waste resources.

A subsidy may:
- increase local occupancy;
- change feeding time;
- attract competitors/predators;
- increase conflict/capture exposure;
- reduce natural foraging behavior;
- create dependency or ecological traps.

`HIGH_LOCAL_ABUNDANCE != HEALTHY_HABITAT`

## Cobblemon/Minecraft projection

Safe projection outputs include:
- whether a persistent actor is eligible to be visible;
- preferred distance band from player traffic;
- hiding/retreat presentation intent;
- activity-window bias;
- use of an authored anthropogenic resource point;
- delayed reappearance after disturbance.

Unsafe authority leaks include:
- Minecraft entity death deciding canonical death;
- vanilla damage changing canonical HP;
- generic despawn deciding emigration;
- pathfinding failure deciding capture/escape;
- proximity alone creating a battle.

## Observation pipeline

Players/NPCs may observe indicators such as:
- approach distance before retreat;
- repeated use of the same human-adjacent resource;
- day/night activity shifts;
- site abandonment;
- vigilance frequency;
- return latency after disturbance.

Observation creates evidence. It does not reveal hidden ecology state perfectly.

## Structured encounter handoff

### Reduced version: available now

The ecology layer selects explicit combatants only after an escalation condition is met. Transit, nearby noncombatants, nests and population accounting remain world-state concerns. AutoPTU receives a conventional bounded battle with static terrain and verified mechanics only.

### Intended rich version

A conflict may include retreat corridors, defended juveniles, human infrastructure, reaction zones, forced movement, time pressure and non-KO objectives.

Permanent capability dependencies:
- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end.

## Implementation acceptance

Pass 236 is implementation-ready at world-state level when a deterministic fixture can prove:
- harmless exposure can increase tolerance without changing population size;
- harmful exposure can increase avoidance independently;
- welfare cost is independent from visible tolerance;
- disturbance memories decay rather than reset on chunk unload;
- the same population can shift activity or presentation without being cloned by generic spawning;
- battle handoff remains explicit.

## Canon status

This contract is proposed. It does not alter the canon-approved Sendero Fletchling species record or authorize new species for Marea.
