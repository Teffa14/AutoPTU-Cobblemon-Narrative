# Derelict Fishing Gear Recovery Contract — Pass 333

Status: DESIGN / REUSABLE WORLD CONTRACT
Date: 2026-09-07
Canon effect: NONE

## Purpose

This contract defines how Ouros can represent lost, abandoned or otherwise unattended fishing gear as a persistent world object without collapsing object identity, historical ownership, current position, wildlife effects, response authority and PTU tactical mechanics into one state.

The contract is reusable for nets, lines, pots, traps and similar authored objects when later canon approves them.

## Authority boundaries

Narrative/world state owns:

- persistent object identity;
- reported and observed positions;
- provenance claims;
- registry/archive links;
- report delivery;
- institutional decisions;
- custody/recovery history;
- feature access state;
- ecological observations as attributed evidence.

AutoPTU owns battle legality and combat outcomes after an explicit handoff.

Minecraft/Cobblemon/Craftics presents authoritative state. It may not infer ownership, liability, entanglement rules, ecological truth, damage, statuses or NPC knowledge from rendered blocks/entities.

## Core invariants

`GEAR_IDENTITY != CURRENT_LOCATION`

`GEAR_MARK != CURRENT_OWNER`

`HISTORICAL_OWNER_RECORD != CURRENT_CAUSAL_RESPONSIBILITY`

`GEAR_LOST != GEAR_ABANDONED_DELIBERATELY`

`GEAR_PRESENT != WILDLIFE_HARM_CONFIRMED`

`WILDLIFE_INTERACTION_OBSERVED != ALL_IMPACT_KNOWN`

`RECOVERY_LOCATION != LOSS_LOCATION`

`GEAR_RECOVERED != INCIDENT_HISTORY_ERASED`

`GEAR_REMOVED_FROM_FEATURE != GEAR_DISPOSED`

`MINECRAFT_OBJECT_LOCATION != PROVENANCE_TRUTH`

`NPC_FACTION_MEMBERSHIP != INCIDENT_KNOWLEDGE`

## Persistent object record

Minimum world record:

```text
DerelictGearObject
  gear_id
  object_type_claims[]
  identifier_observations[]
  registry_refs[]
  ownership_claims[]
  deployment_claims[]
  loss_reports[]
  position_observations[]
  transfer_or_drift_events[]
  snag_events[]
  wildlife_observations[]
  habitat_observations[]
  access_decisions[]
  recovery_assessments[]
  recovery_events[]
  custody_events[]
  current_world_state
```

Every claim must carry provenance and semantic time.

## Observation model

A gear observation records:

- observer;
- feature ID;
- semantic observation time;
- object ID if identity is established, otherwise provisional object reference;
- visible type/extent;
- identifier evidence actually visible;
- wildlife interaction directly seen;
- access/navigation concern directly seen;
- confidence/limitations;
- source media or report reference where appropriate.

Observation does not automatically create:

- ownership;
- deployment history;
- intent;
- criminal responsibility;
- exact age;
- exact hazard geometry;
- PTU entanglement status.

## Identity resolution

A newly observed gear fragment may initially have a provisional ID.

Later evidence can establish that two observations concern the same persistent object or debris mass. Identity resolution creates a relation/revision record rather than rewriting old reports.

If two marked sections from different origins become physically entangled into one debris mass, preserve component identity where evidence supports it.

`DEBRIS_MASS_ID != SINGLE_ORIGIN_ASSUMPTION`

## Identifier and archive lookup

A visible gear mark can produce:

```text
identifier observation
  -> archive/registry query
  -> matching record(s)
  -> interpretation
  -> explicit communication
```

A registry match may support a historical ownership or authorization claim for a defined period. It does not establish uninterrupted custody through the present.

A failed search means only that no matching record was found in the searched collection/version under the search conditions.

`NO_RECORD_FOUND != NO_RECORD_EXISTS`

## Position lineage

Every known position is an observation or authored transfer event with time.

Never store only `gear.current_position` and discard history.

Useful sequence:

```text
observed at feature A
  -> reported lost near feature B
  -> later observed at feature C
  -> storm/current transfer authored
  -> snagged at feature D
  -> recovered to staging feature E
```

This allows NPCs to disagree honestly because they possess different segments of the object's history.

## Wildlife / habitat evidence

Keep current effects independent from origin.

Possible attributed observations:

- animal contacted gear;
- animal appeared constrained by gear;
- fresh biological material found on gear;
- gear abrading/snagging a habitat feature;
- no direct interaction observed during a defined watch window;
- previously observed interaction no longer visible.

Do not promote these observations into universal ecological conclusions.

## Response decisions

An institution may issue feature-scoped decisions based on the evidence it has actually received.

Candidate authored states:

- `OPEN`
- `MONITORING`
- `RESTRICTED`
- `SPECIALIST_ACCESS_ONLY`
- `RECOVERY_STAGING`
- `CLOSED`

Possible decisions:

- request specialist assessment;
- restrict navigation near one feature;
- stabilize gear pending recovery;
- recover immediately;
- recover in stages;
- monitor because immediate removal would create unacceptable authored risk;
- transfer recovered gear to custody;
- reopen a feature after current risk is addressed.

These decisions do not create PTU mechanics by themselves.

## Recovery lineage

Recovery must be an event chain, not deletion.

```text
assessment
  -> authorization
  -> attempt
  -> outcome
  -> object/component position update
  -> custody state
  -> feature consequence
  -> follow-up observation
```

Possible outcomes:

- no attempt;
- attempted / no movement;
- stabilized;
- partial recovery;
- full recovery;
- recovery stopped;
- object transferred to staging;
- object transferred to custody;
- disposed/reused only after an authored downstream event.

## NPC knowledge contract

Mara, Nerea, Taro and any future actor may only reason from evidence received or directly observed.

Example:

- Nerea observes wildlife interaction at T1.
- Taro finds an archive match at T2.
- Mara receives Nerea's report at T3.
- Mara receives Taro's result at T4.

Mara cannot use the archive match in a T3 decision unless it was delivered before that decision.

Historical reports remain historically accurate records of what was known then even when later evidence changes the interpretation.

## Institutional disagreement

Two decisions can be locally rational under different evidence sets.

Example:

- operations restrict ferry approach because gear location is confirmed;
- archive staff refuse to name a responsible owner because the mark only proves a historical registry relation;
- research staff recommend documenting habitat incorporation before full removal.

No actor must be made dishonest to generate conflict.

## Battle handoff boundary

World layer may request a battle when a localized confrontation exists.

Allowed handoff inputs include:

- static battle geometry;
- participating combatants;
- explicitly verified ordinary battle rules;
- a narrow objective only where the engine can represent it legally.

World layer must not hand the adapter an instruction such as “make net entangle target” unless the exact PTU/item/hazard/status behavior is verified and implemented in authoritative core.

## Full mechanical version dependencies

### targeting / footprints / range / LoS

Needed if water, netting, spray, cover or rescue geometry changes target acquisition. Ordinary verified LoS does not establish those special cases.

### base movement legality

Ordinary audited movement can be used on static legal terrain. Swimming, wading, climbing rigging or unstable-edge traversal need separate evidence.

### complete movement

Required for current-driven movement, pulling, forced displacement, interception, rescue movement, dragging gear or knockback interactions.

### core calculations

Ordinary verified calculations are usable for standard combat. No gear-tension, cutting or rescue formula is inferred.

### action economy / initiative

Ordinary primitives are usable. Special rescue/cutting actions require explicit authoritative definitions.

### full turn / round lifecycle

Required for timed gear shifts, tide/current pulses, delayed recovery steps, scheduled machinery or multi-phase environmental changes.

### full stateful damage pipeline

Required for any verified crushing, impact, environmental or gear damage that persists through battle state.

### status lifecycle

Required for any real PTU condition representing restraint/entanglement or another persistent effect. This contract authors no such status.

### terrain / weather / hazards / zones / reactions

Required for dynamic water, unsafe edges, net hazard zones, reaction windows or shelter/exclusion zones with tactical effect.

### move-specific behavior

Each Move used to cut, free, pull, push, manipulate water, alter terrain, rescue or sense remains individually gated.

### abilities

No Ability receives anti-entanglement, rescue, navigation or gear-manipulation authority from species flavor.

### items

Any cutter, rope, float, recovery tool or protective equipment with tactical effect requires authoritative item behavior.

### Trainer Features / perks

Any Feature that modifies rescue, item use, movement, reactions, command or environmental work requires verified execution for that Feature and trigger.

### AI legal-action infrastructure

Ordinary audited legal-action infrastructure can support ordinary battle choices.

### AI tactical policy

Rich objectives require policy for protecting a subject, retreating, avoiding harm, escorting workers, prioritizing gear or accepting non-defeat outcomes.

### Minecraft / Cobblemon / Craftics adapter/playback

Needs end-to-end support to render authoritative movement, hazards, objective state and outcomes without becoming a second rules engine.

## Reduced implementation contract

The reduced version is preferred until rich dependencies are verified.

World layer handles:

- gear discovery;
- provenance;
- access restrictions;
- reports;
- archive queries;
- wildlife observations;
- specialist assessment;
- recovery between scenes;
- custody;
- aftermath.

If combat occurs:

- use static geometry;
- block unsafe cells;
- do not instantiate a custom net hazard;
- do not assign an unverified entanglement condition;
- keep rescue subjects outside BattleSpec unless objective support is verified;
- use ordinary verified targeting, movement, calculations, initiative and legal actions;
- return only a narrow semantic result.

Possible result:

`IMMEDIATE_SITE_SAFE_FOR_RECOVERY_TEAM`

That result does not mean:

- gear origin solved;
- wildlife fully rescued;
- net removed;
- liability established;
- habitat restored.

## Adapter rules

Minecraft/Cobblemon/Craftics may render:

- visible gear models;
- buoys/markers;
- barriers;
- workers;
- recovery staging;
- wildlife entities when authoritative world state places them there;
- visual changes after recovery.

It may not infer:

- that visual contact equals PTU restraint;
- damage from collision;
- ownership from texture/label;
- NPC knowledge from proximity;
- successful recovery from object despawn;
- ecological recovery from absence of rendered debris.

## Persistence tests to add when implemented

1. Gear moves between features without losing earlier position history.
2. A registry match does not overwrite current owner as fact.
3. An NPC cannot use an undelivered archive result.
4. Partial recovery preserves unrecovered component state.
5. Removing the rendered object does not delete incident history.
6. Battle completion emits only the contracted semantic result.
7. Reload preserves object identity, report times, custody and decisions.
8. Multiple gear components can merge into one debris mass without collapsing provenance.

## Canon gate

This contract is reusable design architecture only. It does not establish that the proposed Puerto Bruma incident occurred, that local fishing exists, that any named actor owned gear or that any species was harmed.