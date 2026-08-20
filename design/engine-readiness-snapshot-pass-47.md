# Engine Readiness Snapshot — Pass 47

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only Python oracle
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live heads

### AutoPTU-Java

Inspected head:

`9e68bde8391b057c982900d038cc9ec3a3d348f9`

Latest inspected change:

`Apply post-damage hooks in authoritative move runtime`

The head remains the same tactical evidence used by Pass 46. The change connects selected post-damage Ability hooks to authoritative move resolution before HP mutation and damage-history recording.

Do not infer from this:
- complete damage resolution;
- complete Ability coverage;
- broad reaction support;
- terrain, weather or hazard state;
- tactical objective AI;
- Minecraft/Cobblemon/Craftics playback.

The Java README still explicitly lists as unfinished:
- core battle-state expansion;
- full damage and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete move/ability/item/perk/Trainer Feature registries;
- full semantic transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

### Python AutoPTU

Inspected head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The newest Python changes remain Career-side work. They do not justify promotion of Java tactical capability families.

Python remains the behavioral oracle while the Java port is incomplete.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Battle targeting, anchors, areas, footprints, range and LoS have strong deterministic evidence.

Do not infer overworld crowd visibility, guide sight distance, patrol vision or tourist-wayfinding visibility from battle LoS.

#### base movement legality

Shift movement, Overland/Swim/Sky basics, represented terrain costs, blockers, Wallrunner, sprint, jump and landing-fit predicates have strong evidence.

Do not infer evacuation traffic, pedestrian crowd flow, queue movement, interception, currents or forced displacement.

#### core calculations

Damage Base tables, type-effectiveness steps, combat stages, accuracy stages and several modifier primitives remain verified as calculation primitives.

#### action economy / initiative

Typed phases, action budget and deterministic initiative/League ordering remain verified.

#### AI legal-action infrastructure

The engine can enumerate/filter deterministic legal battle choices.

It does not yet prove strategically good or objective-aware choice.

### PARTIAL

#### full turn / round lifecycle

Typed phases, actor/phase state, end-turn cleanup, round histories, delayed-hit infrastructure and selected status/Ability/perk dispatch provide meaningful coverage.

The complete lifecycle remains unproven.

#### full stateful damage pipeline

Current Java applies selected authoritative post-damage hooks before HP mutation/history writeback.

The full damage family remains incomplete according to the Java README.

#### status lifecycle

Selected statuses, metadata, application boundaries and phase hooks exist.

The full status controller remains incomplete.

#### move-specific behavior

Representative Move behavior exists; the complete PTU Move catalogue is not proven.

#### abilities

Multiple Ability slices and hook families are implemented and parity-tested.

Representative Abilities do not prove the full catalogue.

#### items

Held-item state and selected item hooks exist. Full item behavior is not complete.

#### Trainer Features / perks

Ordered perk infrastructure and selected Features exist. The full Trainer Feature catalogue remains partial.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Any encounter requiring dynamic crowd routing, body blocking, escort interception, knockback or forced displacement must retain this dependency.

#### terrain / weather / hazards / zones / reactions

The broad battlefield-state family remains unfinished. Selected stage or Ability hooks do not prove weather phases, moving hazards, protected zones or attacks of opportunity.

#### AI tactical policy

Retreat, evacuation, escort, protection, crowd-aware routing and scenario objectives remain blocking.

#### Minecraft / Cobblemon / Craftics adapter and playback

The Java engine remains a core library rather than a Minecraft mod. World synchronization, visitor NPC density, queue presentation, accommodation signs, trail barriers, event crowds and physical attraction state remain adapter concerns.

## Pass 47 tourism implications

Most tourism systems can advance before tactical implementation because they are world-state concerns:
- visitor presence;
- accommodation occupancy bands;
- destination reputation;
- public guide editions;
- itinerary state;
- visitor-flow drivers;
- zone-level pressure bands;
- event surges;
- closures and reroutes;
- resident-response records;
- guide-service schedules;
- visitor-centre information;
- conservation and heritage pressure links.

Do not translate these into battle modifiers.

### Scenic Ridge Closure

Reduced version: feasible as overworld closure/rerouting plus a static legal battle only if one occurs.

Full-version dependencies:
- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

### Resort Wildlife Disturbance

Reduced version: feasible as evacuation/world-state handling plus conventional static battle when required.

Full-version dependencies:
- complete movement/interception;
- AI tactical policy for wildlife retreat and staff priorities;
- terrain/weather/hazards when present;
- adapter/playback.

### Heritage Trail Bottleneck

Reduced version: feasible through world-state closures, visitor routing and a normal tactical encounter if necessary.

Full-version dependencies:
- complete movement/interception/forced movement;
- terrain/zones/broad reactions;
- AI tactical policy;
- adapter/playback.

## Promotion rule

A capability moves upward only when runtime wiring, representative deterministic contracts, tests and Python parity establish the family. One successful effect never promotes the entire category.
