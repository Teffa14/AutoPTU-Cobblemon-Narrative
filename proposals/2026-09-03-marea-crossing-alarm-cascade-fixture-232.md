# Marea Crossing Alarm Cascade Fixture — Pass 232

Status: PROPOSED IMPLEMENTATION FIXTURE. Does not change canon.
Date: 2026-09-03

## Purpose

Exercise `design/ecological-information-propagation-contract.md` inside existing Marea/Sendero geography without fixing unverified species or biome bindings before the global-world substrate is frozen.

This is a reusable ecology scenario family, not a fixed quest plot.

## Semantic sites

```yaml
site_refs:
  - marea.sendero_lower_shelf
  - marea.sendero_seasonal_crossing
  - marea.estacion_mirador_observation_network
coordinate_binding: migrate_after_global_world_lock
minecraft_biome_binding: unresolved
species_binding: unresolved_until_native_habitat_validation
```

Canonical coordinates remain untouched.

## Scenario family — Crossing Alarm Cascade

Several approved local populations share a narrow crossing or adjacent refuge network.

One visible actor detects a threat or disturbance and emits a signal. Nearby receivers do not gain exact knowledge of the cause. Each evaluates the cue according to its own species prior, local history, sensory access and relevance.

Possible visible result:

```text
primary disturbance
-> first actor warns/flees
-> second population seeks cover
-> third population becomes vigilant but does not flee
-> one habituated population ignores the signal
-> route briefly appears empty
-> later activity returns unevenly
```

No population change is required.

## Authoritative world-state fixture

```yaml
id: marea.fixture.crossing_alarm_cascade.01
type: ecological_information_cascade
scope:
  ecology_cell_ids:
    - sendero_crossing_unbound
    - sendero_lower_shelf_unbound
primary_stimulus:
  class: disturbance_or_threat
  hidden_from_observers: true
signal_event:
  class: alarm
  source_species_id: unresolved
  strength: moderate
  expires_after: short
receivers:
  - species_id: unresolved_receiver_a
    baseline_recognition: high
    threat_relevance: high
    candidate_intents: [hide, flee, warn]
  - species_id: unresolved_receiver_b
    baseline_recognition: moderate
    threat_relevance: moderate
    candidate_intents: [freeze, observe, relocate]
  - species_id: unresolved_receiver_c
    baseline_recognition: low
    habituation: elevated
    candidate_intents: [tolerate, observe]
population_delta: none_by_default
mechanical_handoff:
  mode: none_by_default
```

## Player-facing evidence

The player can encounter consequences before seeing the primary cause:
- several normally visible actors disappear into cover within seconds of each other;
- one species remains visible and attentive instead of fleeing;
- a second warning event appears downstream;
- tracks or recent feeding signs show animals were present immediately before the silence;
- Mirador observers record a synchronized visibility drop without evidence of demographic loss;
- later observations show different return times by population.

The player must infer whether the first visible signal was the cause, a response, or merely correlated with the real disturbance.

## Investigation structure

```text
notice synchronized behavioral change
-> identify first observable emitter if possible
-> compare receiver responses
-> inspect likely stimulus direction
-> collect trace / route / timing evidence
-> update sender-reliability hypothesis
-> observe a later signal event
-> confirm, weaken or reject hypothesis
```

A single observation should rarely prove a durable interspecies information edge.

## PTU-compatible field actions

Where the active Ouros rules profile permits them:
- Survival can read tracks, recent habitat use and common local Pokémon context;
- Perception can notice signal timing, direction and receiver reactions;
- Stealth can let a field researcher remain present without becoming the dominant disturbance.

Checks expose evidence. They do not reveal hidden population numbers or the exact internal response formula.

## Player interventions

### Observe without interference

No tactical handoff.

Potential result:
- better evidence quality;
- local signal reliability estimate gains a sample;
- no direct pressure change.

### Remove a human disturbance source

No battle required.

Potential result:
- fewer alarm events;
- faster recovery of normal exposure;
- later comparison can distinguish chronic disturbance from predator pressure.

### Deliberately replay or imitate a warning cue

PROPOSED / REQUIRES REVIEW.

This may become a research or management action only if the active rules profile and species-specific evidence support it. It must carry habituation/false-alarm costs and cannot become a universal crowd-control button.

### Follow the cascade toward the hidden cause

Reduced version:
- overworld investigation ends at a location/evidence objective;
- no chase outcome is inferred from Minecraft velocity or entity contact.

Full version may use a pursuit or defensive encounter only after explicit Ouros handoff.

### Structured defensive escalation

Narrative premise: an alarm cascade concentrates several actors near cover and one actor escalates when the player blocks a retreat or reaches the threat source.

Reduced battle version:
- one ordinary legal AutoPTU encounter;
- simple terrain;
- no bespoke reinforcement reaction chain;
- no forced displacement requirement;
- ecological consequences written only after the authoritative result.

Reduced dependency audit:
- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- AI legal-action infrastructure: VERIFIED;
- exact moves/abilities/statuses: verify individually;
- AI tactical policy: BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

Full intended version can include multiple receivers arriving, retreat lanes, forced displacement, reactions, environmental zones and species-specific defensive abilities.

Full-version dependency audit:
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING.

## Persistent consequences

Possible reviewed outcomes:
- a receiver population learns that one sender is locally reliable;
- repeated irrelevant alarms reduce response strength;
- human traffic creates chronic false-positive pressure;
- a route-management change lowers alarm frequency;
- researchers identify a high-value sentinel population for future surveys;
- juveniles begin with species priors but require local experience to learn a sender association;
- repeated cross-species response becomes a candidate `EAVESDROPS_ON` or `WARNS` edge rather than instant canon.

## Worldgen binding rule

After the global Ouros world is generated and frozen, this fixture must bind to:
- actual coordinates;
- actual Minecraft biome IDs/tags;
- legal native Cobblemon species envelopes;
- real cover/noise/route geometry.

If those facts do not support the scenario at the legacy Marea anchors, use an explicit migration mapping. Do not silently change canon coordinates.

## Success criteria

The fixture is valid when:
- the same signal produces different receiver behavior;
- the player can observe a cascade without learning hidden truth automatically;
- no population is created or destroyed merely because actors hide/reappear;
- sender reliability can change with local history;
- the scenario works without combat;
- battle escalation, if used, declares exact capability dependencies;
- no Minecraft event directly writes tactical outcomes;
- species bindings remain unresolved until native habitat validation.

## Open questions

- sample threshold before a local learned information edge can persist;
- maximum chain depth before propagation is cut off;
- whether downstream receivers can retransmit a signal with degraded confidence;
- how Mirador distinguishes synchronized hiding from actual departure;
- which approved local species are plausible sentinel emitters after world/spawn binding;
- whether intentional human playback belongs under field research, management, Trainer Features or a separate interaction system.
