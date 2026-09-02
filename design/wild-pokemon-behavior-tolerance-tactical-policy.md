# Wild Pokémon behavior, tolerance and tactical policy

Status: PROPOSED SYSTEM DESIGN — NOT CANON-APPROVED SPECIES BEHAVIOR
Date: 2026-09-02

## Purpose

Ouros needs a wild-Pokémon decision layer that does not reduce wildlife to `AGGRESSIVE / PASSIVE` and does not let Minecraft invent animal behavior.

The policy should derive a wild Pokémon's response from four ordered inputs:

1. species-grounded behavior;
2. the actual capabilities and current state of the individual Pokémon;
3. the actual capabilities, approach and demonstrated actions of the Trainer or other actor interacting with it;
4. local context, including habituation to dense human/Pokémon population and current environmental/social conditions.

Trainer Features, Edges, Skills and legal tactical actions may then modify what the Pokémon perceives, how alarming the approach is, what options are available and how a confrontation develops.

This file defines the decision architecture. It does not grant any Move, Ability, Feature, Edge, Skill effect or battle action that PTU/AutoPTU has not verified.

## Canon compatibility

The first visible Sendero Fletchling canon explicitly states that the actor is not always aggressive and that later ecology may introduce individual variation and population state. This proposal extends that boundary instead of changing the frozen Fletchling blueprint.

A species behavior profile must never overwrite canonical mechanical identity. Species tendencies describe likely interpretation and response, while the individual blueprint continues to own level, stats, Moves, Ability, capabilities, status, Injuries and other PTU facts.

## Core decision order

### 1. Species behavior prior

Every species/population may eventually define source-backed behavioral tendencies such as:

- territoriality;
- flocking, schooling, pack or solitary preference;
- nesting/breeding-site defense;
- predator avoidance;
- curiosity;
- scavenging/food-seeking;
- diurnal/nocturnal activity;
- flight distance;
- warning/display behavior;
- willingness to tolerate observation;
- tendency to defend young, partner, group or resource;
- response to noise, sudden movement, confinement or pursuit;
- familiarity with human settlements.

These are priors, not deterministic scripts.

Species behavior requires provenance. Pokédex flavor, PTU/Caelo material, ecology research and approved Ouros canon may inform it, but contradictory sources must remain visible rather than silently merged.

### 2. Individual Pokémon capability and state

The engine then constrains the behavioral prior using the actual individual.

Relevant inputs may include, when authoritative:

- movement capabilities: Overland, Sky, Swim, jumping and other verified mobility;
- usable Moves;
- Ability;
- Size/footprint and Power-related facts where implemented;
- senses and special capabilities;
- HP, Injuries and Status Afflictions;
- current action economy;
- held item, if any;
- current group/collective relation;
- current location and escape routes;
- persistent individual history, if canonically recorded.

Example:

A species may normally prefer withdrawal when approached, but an individual with a protected nest, an Injury that prevents its normal escape method or a nearby dependent may choose warning, obstruction or defense instead.

No narrative layer may fabricate a mechanical limitation to force the desired scene.

### 3. Compare against the Trainer/actor

Wild behavior should react to what the Trainer can do and what the Trainer actually does.

Potential inputs include:

- distance and approach vector;
- speed of approach;
- direct pursuit versus parallel movement;
- visibility / line of sight;
- whether the Trainer blocks an escape path;
- whether Pokémon are visibly deployed;
- relative apparent threat supported by actual game state;
- prior actions toward this individual or population;
- legal Skill actions;
- legal Features and Edges;
- legal Move/Item effects;
- attempts to conceal, calm, distract, trap, hinder, restrain or inflict a status condition.

The policy must distinguish capability from action.

A Trainer who *could* restrain the Pokémon is not treated as having restrained it. A Trainer who knows a Feature does not receive its effect until its activation/conditions are valid.

## Habituation and population-density tolerance

Tolerance should vary by location/population context.

A species that normally avoids close human presence may tolerate smaller distances in:

- dense towns;
- busy ports;
- markets;
- routes with constant foot traffic;
- parks or plazas;
- research sites with repeated non-threatening observation;
- settlements where the local population has a long history of coexistence.

Conversely, individuals in remote breeding grounds, feeding sites, shelters or recently disturbed habitat may tolerate much less intrusion.

Proposed contextual object:

```yaml
wild_tolerance_context:
  population_id: null
  location_id: null
  baseline_human_exposure: LOW | MODERATE | HIGH
  habituation_band: LOW | MODERATE | HIGH
  protected_resource_refs: []
  active_social_context: []
  recent_disturbance_refs: []
  authored_modifiers: []
```

This object modifies thresholds. It does not erase species behavior.

High habituation should not mean domestication, obedience, capture permission or friendship.

## Behavioral state model

Do not jump directly from idle to combat.

Proposed observable states:

- UNAWARE
- AWARE_TOLERANT
- ALERT
- WARNING
- WITHDRAWING
- EVADING
- GUARDING
- OBSTRUCTING
- PURSUING
- ENGAGING
- DISENGAGING
- TRAPPED_OR_CONSTRAINED

These are world/AI states, not PTU Status Afflictions.

A Pokémon may transition between them as the situation changes.

Example:

`AWARE_TOLERANT -> ALERT` because a Trainer changes from parallel observation to direct approach.

`ALERT -> AWARE_TOLERANT` because the Trainer stops, increases distance and succeeds with an authorized calming/non-alarming tactic.

`WARNING -> WITHDRAWING` because an escape lane opens.

`WITHDRAWING -> GUARDING` because withdrawal would expose a protected dependent.

## Alarm pressure instead of binary hostility

A useful implementation model is an internal `alarm_pressure` derived from source-backed inputs rather than a universal hostility meter.

Possible contributors:

- intrusion distance relative to current tolerance;
- sudden movement;
- pursuit;
- line-of-sight pressure;
- blocked escape path;
- loud/violent action nearby;
- observed capture attempt;
- observed damage/status attempt;
- protected resource/dependent proximity;
- known prior interaction with the same persistent individual;
- species-specific triggers.

Possible reducers:

- increased distance;
- non-pursuit posture;
- breaking line of sight when appropriate;
- opening an escape route;
- successful authorized calming/handling action;
- local habituation;
- established persistent history supported by canon state;
- species-specific non-threatening behavior.

The exact arithmetic, thresholds and rolls remain unresolved until PTU/Caelo/Kairos and engine contracts are audited.

## Trainer tactics

The Trainer should be able to influence wildlife behavior through actual tactics rather than dialogue-menu abstractions alone.

### Avoid alarming

Potential tactic families:

- control approach speed;
- maintain or increase distance;
- avoid blocking exits;
- use terrain/LoS to reduce pressure;
- wait for the Pokémon to move first;
- use an authorized Skill/Feature/Edge to calm, handle, approach or interpret behavior;
- avoid deploying an obviously threatening Pokémon unnecessarily.

### Capture/control setup

A Trainer may attempt to improve a capture opportunity by tactics that remain subject to PTU legality:

- cut off an escape route;
- use positioning to funnel movement;
- use legal trapping/restraining effects;
- hinder movement;
- apply a legal Status Affliction;
- use Moves, Abilities, Items or Features that create verified control effects;
- coordinate multiple participants.

These actions should affect wild tactical response. A Pokémon that detects containment may shift from withdrawal to evasion, obstruction or engagement depending on species prior and available capabilities.

### Interference and hindrance

A Trainer may intentionally make escape or action harder through:

- positioning;
- difficult access routes where mechanics support them;
- verified movement reduction;
- trapping effects;
- forced movement;
- status conditions;
- reactions/intercepts;
- battlefield zones/hazards where legally created.

Every such tactic inherits its exact engine dependency. Narrative AI cannot approximate a missing rule.

## Features, Edges and Skills

Features/Edges/Skills can modify several distinct layers and should not be collapsed into a generic bonus.

Possible effect classes, only after rules verification:

- better interpretation of warning/tolerance behavior;
- lower alarm caused by a legal approach;
- increased ability to remain unnoticed;
- improved handling/calming;
- better prediction of escape behavior;
- legal interception or containment option;
- improved capture preparation;
- tactical coordination with allied Pokémon;
- resistance to intimidation or environmental pressure;
- access to specialized Pokémon-interaction actions.

A Feature or Edge may change the outcome without rewriting the species profile.

The authoritative order should be:

```text
species prior
+ population/location context
+ persistent individual state/history
+ current Pokémon mechanical capabilities/state
+ observed Trainer approach/actions
+ verified Features/Edges/Skills/Move/Ability/Item effects
-> legal behavioral options
-> tactical policy selects among legal options
-> AutoPTU resolves mechanical actions
-> Minecraft/Cobblemon plays back the result
```

## Tactical policy decomposition

`AI tactical policy` should not remain a single monolithic blocker.

It can be decomposed into:

### A. Behavior interpretation policy

Can be designed now.

Chooses intent bands such as tolerate, warn, withdraw, guard, evade, obstruct or engage from authoritative world/mechanical inputs.

### B. Legal-action generation

Already tracked separately as AI legal-action infrastructure.

Must expose only actions AutoPTU currently considers legal.

### C. Tactical action selection

Chooses among those legal actions according to the current behavioral intent.

Examples:

- WITHDRAWING prioritizes legal routes that increase distance or break pursuit;
- GUARDING prioritizes maintaining access denial around the protected entity/space;
- EVADING prioritizes preventing capture/control while avoiding unnecessary commitment;
- ENGAGING may select damage, control or positioning according to species/individual capabilities;
- DISENGAGING prioritizes leaving the conflict once the trigger is gone.

This requires capability-aware policy but does not require inventing mechanics.

### D. Playback

Minecraft/Cobblemon receives semantic decisions/results and animates them. It does not decide why the Pokémon fled, whether a Feature worked or whether a trapping effect was legal.

## Encounter design impact

Mechanically rich wildlife encounters should record both full and reduced forms.

### Full form

May include:

- species-driven tolerance;
- spatial awareness and LoS;
- escape-route evaluation;
- guarding dependents/resources;
- Trainer approach tactics;
- Skill/Feature/Edge modifiers;
- trapping/hindering;
- status application;
- Move/Ability/Item control effects;
- forced movement/interception;
- terrain/weather/hazards/zones/reactions;
- capability-aware wild tactical selection.

### Reduced form

Until all required families are verified:

- evaluate species/population tolerance from server-authored state;
- expose observable warning/withdrawal behavior;
- let the Trainer change distance, approach or disengage;
- allow only already-verified Skill/Feature/action contracts;
- begin a normal BattleSpec only when an actual legal battle starts;
- do not simulate missing traps, statuses, forced movement, reactions or tactical AI off-screen;
- preserve the same narrative premise and persistent individual identity.

## Capability-family dependencies

This design touches the permanent engine families as follows.

### Required even for basic spatial wildlife behavior

- targeting / footprints / range / LoS;
- base movement legality;
- AI legal-action infrastructure;
- Minecraft/Cobblemon/Craftics adapter/playback.

### Required when behavior becomes tactical combat/control

- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI tactical policy.

A representative implemented mechanic never promotes the whole category.

## Fletchling application boundary

For `ouros.marea.encounter.sendero_lower_shelf.fletchling.0`:

- keep the existing canonical level-5 blueprint unchanged;
- do not assume permanent aggression;
- future behavior may use source-backed Fletchling tendencies plus Sendero human-exposure context;
- Big Pecks, Tackle, Growl and base movement are available only to the extent AutoPTU implements their relevant mechanics;
- no new Move, Ability, Skill effect, personality or social bond is added by this design file;
- tolerance may differ from a remote Fletchling population if Sendero canon eventually establishes frequent safe human traffic.

## Persistence

For persistent wild individuals, useful history may include bounded observed facts:

```yaml
wild_interaction_memory:
  pokemon_id: null
  actor_id: null
  event_refs: []
  observed_capture_attempts: []
  observed_damage_events: []
  observed_assistance_events: []
  observed_non_pursuit_events: []
  authored_familiarity_state: null
```

Do not infer friendship, trauma, trust or hatred from event count alone.

Any higher-level relationship state requires an approved model and appropriate evidence.

## Anti-cheat / authority boundaries

- client movement cannot directly write tolerance state;
- Minecraft entity AI cannot decide PTU legality;
- Cobblemon temperament/personality fields cannot silently become Ouros behavior truth;
- animation cannot apply Status Afflictions;
- entering a visual trap cannot mean mechanically trapped unless AutoPTU confirms the effect;
- apparent proximity cannot bypass authoritative footprints/range/LoS;
- a Feature/Edge name cannot grant an effect until its rule contract is verified;
- wild behavior decisions must be reproducible from authoritative inputs for debugging.

## Open PTU/Caelo/Kairos review

Before approving mechanical modifiers, audit exact rules for:

- Pokémon interaction/handling Skills;
- Stealth and detection;
- Charm, Command, Intuition, Survival and related Skill uses where applicable;
- Features/Edges affecting wild Pokémon interaction;
- capture rules and capture modifiers;
- trapping and restraining effects;
- movement reduction;
- Status Afflictions relevant to capture/control;
- Moves and Abilities that prevent switching/fleeing/movement;
- interception/reaction rules;
- forced movement;
- line of sight and concealment;
- Poké Ball use and range/action economy;
- any Caelo/Kairos overrides.

Record each verified modifier independently. Do not create a universal `wildlife_bonus` unless the governing rules actually support one.

## Design outcome

Wild Pokémon should appear to protect themselves, tolerate familiar activity, investigate, flee, warn, defend or fight for reasons grounded in species, individual capability, context and the Trainer's behavior.

The Trainer can change the encounter by how they approach and by the legal tools they possess.

This creates meaningful wildlife tactics before every capability family is complete, while keeping all mechanical consequences under PTU/AutoPTU authority.