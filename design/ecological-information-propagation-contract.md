# Ecological Information Propagation Contract

Status: PROPOSED DESIGN. Not canon-approved.
Date: 2026-09-03

## Purpose

Represent local information flow between wild Pokémon without granting shared omniscience and without turning ambient ecology into hidden tactical combat.

This contract extends the interaction graph with observation and response edges. It does not replace population, behavior, observation, pulse-event or AutoPTU authority contracts.

## Authority flow

```text
world/ecology stimulus
-> emitter observation or signal
-> Ouros records local signal event
-> eligible receivers evaluate signal
-> receiver behavioral intent changes probabilistically
-> Minecraft/Cobblemon projects visible response
-> Ouros decides whether structured mechanics begin
-> AutoPTU resolves only after explicit handoff
```

A Minecraft animation, proximity trigger or sound packet is presentation unless Ouros explicitly records the corresponding ecological event.

## Core signal record

```yaml
signal_id: null
ecosystem_id: null
source_actor_id: null
source_species_id: null
signal_class: null
stimulus_ref: null
created_at: null
expires_at: null
origin_position_ref: null
propagation_mode: null
base_strength: 0.0
semantic_hint: null
confidence: 0.0
source_refs: []
```

Candidate `signal_class` values:
- alarm
- warning
- territorial_display
- recruitment
- contact
- distress
- feeding_activity
- flight_or_escape_cue
- mobbing_or_group_defense
- neutral_activity_cue

These are ecology semantics, not PTU Status Afflictions.

## Receiver evaluation

```yaml
receiver_id: null
receiver_species_id: null
signal_id: null
recognition_prior: 0.0
learned_sender_reliability: 0.0
threat_relevance: 0.0
sensory_access: 0.0
recent_false_alarm_penalty: 0.0
recent_confirmed_signal_bonus: 0.0
habituation: 0.0
response_confidence: 0.0
candidate_intents: []
```

The same signal can produce different outputs for different receivers.

Conceptual rule:

```text
species recognition prior
+ individual/local learned association
+ sender reliability from receiver perspective
+ threat relevance
+ sensory access and distance
+ recent corroboration
- false-alarm history
- habituation
= response pressure
```

No single arithmetic formula is canonized by this document.

## Information edges

Add a local optional edge family beside the existing interaction graph:

```yaml
information_edge_id: null
sender_species_id: null
receiver_species_id: null
signal_classes: []
status: proposed
provenance_grade: null
source_refs: []
context_requirements: []
baseline_recognition: 0.0
local_learned_reliability: 0.0
asymmetric: true
last_updated_at: null
```

Recommended edge semantics:
- `WARNS`
- `EAVESDROPS_ON`
- `FOLLOWS_ACTIVITY_CUE`
- `IGNORES_SIGNAL`
- `LEARNED_SIGNAL_ASSOCIATION`

`EAVESDROPS_ON` does not imply reciprocal recognition.

## Propagation limits

Signal propagation must be bounded by plausible access.

Potential gates:
- distance;
- line-of-environmental-access for visual cues;
- cover/noise/weather attenuation;
- ecology-cell adjacency;
- sensory capability;
- time since emission;
- sender/receiver activity state;
- signal class.

Do not iterate across every population globally. Candidate receivers come from the local projected/ecology neighborhood only.

## State effects

A received signal may change:
- exposure;
- refuge use;
- local movement pressure;
- activity window;
- foraging pressure;
- vigilance;
- group cohesion;
- avoidance zone;
- investigation pressure;
- probability of warning/defensive escalation.

It must not directly write:
- HP;
- tactical status;
- battle position;
- initiative;
- move legality;
- capture outcome;
- defeat/death;
- forced movement result.

## False alarms and trust

A signal can be accurate, irrelevant or misleading from a receiver's perspective without requiring intentional deception.

```yaml
signal_outcome:
  corroborated: false
  threat_relevant_to_receiver: false
  receiver_response_cost: null
```

Repeated non-useful responses may increase habituation or lower learned reliability. Repeated corroborated warnings may strengthen it.

The system should distinguish:
- sender was wrong;
- sender reacted to a threat irrelevant to receiver;
- receiver misclassified signal;
- signal degraded during propagation;
- threat ended before receiver verified it.

## Persistent individual learning

Persistent individuals may retain local signal associations when justified.

```yaml
learned_signal_memory:
  sender_species_id: null
  signal_class: null
  reliability_estimate: 0.0
  sample_count: 0
  last_confirmed_at: null
  last_false_or_irrelevant_at: null
  decay_profile: null
```

Generic spawn actors do not become durable memory owners by default. Population/cohort-level priors may be stored separately.

## Observation and player research

Players and NPCs receive evidence, not the hidden receiver formula.

Possible observations:
- several species seek cover after one species calls;
- one species consistently ignores a common alarm;
- a local population begins responding after repeated co-occurrence;
- a signal causes temporary silence without demographic loss;
- downstream flight reveals a hidden threat direction.

PTU Survival, Perception and Stealth are compatible tools for observing these patterns where the active Ouros rules profile supports them.

## Interaction with ecological pulses

A pulse changes the context in which signals propagate but does not replace individual signal events.

Example:
- rain pulse compresses wildlife into one corridor;
- proximity increases the number of potential receivers;
- one alarm event therefore propagates farther through the temporary aggregation;
- population size remains unchanged.

## Structured encounter handoff

### Reduced version

The cascade ends before battle. Ouros updates exposure/avoidance and presents movement or despawn/reprojection. No tactical capability is required.

Dependency:
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

### Full defensive escalation

If several actors enter structured combat after an alarm:
- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL when used;
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
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

A movement landing-hook registry in current AutoPTU-Java is bounded evidence only. It does not authorize generic reaction chains or forced-movement behavior.

## Validation invariants

1. One signal never grants all nearby actors exact knowledge of the underlying threat.
2. Receiver response can differ by species and individual history.
3. Information flow can be asymmetric.
4. Population truth remains separate from visible activity.
5. Generic spawn/despawn does not author persistent learning.
6. Ambient response never writes tactical outcomes.
7. Structured mechanics start only through explicit Ouros handoff.
8. Unsupported rich mechanics always have a reduced world-state version.

## Open implementation questions

- typed propagation models for sound, scent, posture and movement cues;
- efficient local receiver indexing;
- persistence cost for individual signal memories;
- population-level cultural learning versus individual learning;
- decay rates and reset conditions;
- how observer confidence is computed from repeated field observations;
- whether deliberate deceptive signaling is a later separate contract.
