# Ecology Observation and Intervention Contract

Status: PROPOSED DESIGN. Not established Ouros canon.
Date: 2026-09-03

## Purpose

Define how persistent ecological state becomes player-facing content without exposing omniscient world truth and without requiring every ecological interaction to enter AutoPTU combat.

This contract implements one mandatory area from `design/ecology-development-program.md`: ecology-driven quests/events plus the observation/NPC-knowledge seam needed to support them.

It depends on:
- `design/global-species-interaction-graph.md`
- `design/cobblemon-native-spawn-projection-contract.md`
- `design/global-world-generation-spec.md`
- `research/2026-09-03-ecological-encounter-observation-loop-scan-230.md`

## Core rule

Ouros separates authoritative ecological truth from what any observer knows.

```text
persistent ecology truth
-> observable manifestations
-> observer-specific evidence
-> hypotheses
-> intervention
-> ecological consequence
-> later verification
```

No quest, NPC or UI surface should expose the authoritative cause merely because the ecology service knows it.

## Ecological truth record

A local ecological process may be represented as:

```yaml
process_id: null
ecosystem_id: null
process_type: null
state: active
cause_refs: []
affected_species: []
affected_resources: []
pressure_vectors: []
started_at: null
expected_decay_or_recovery: null
provenance_refs: []
```

Examples of `process_type`:

```text
resource_depletion
resource_pulse
predation_pressure
territorial_displacement
nesting_pressure
human_disturbance
habituation
pollution_or_water_quality
migration_arrival
seasonal_departure
disease_or_parasite_pressure
succession_recovery
```

These types describe world-state processes. They do not create PTU statuses or battle effects automatically.

## Observable manifestation

The ecology service converts world truth into signals that are physically or institutionally observable.

```yaml
manifestation_id: null
process_id: null
channel: null
location_ref: null
species_id: null
resource_ref: null
strength: null
visibility_conditions: []
valid_from: null
valid_until: null
```

Allowed initial channels:

```text
visual_presence
visual_absence
track_or_trace
feeding_sign
nesting_sign
alarm_behavior
territorial_mark
resource_damage
resource_condition
water_or_soil_condition
carcass_or_scavenge_sign
sound_or_call
human_report
instrument_reading
historical_record
```

A manifestation may be ambiguous. Several causes can produce similar evidence.

## Observer evidence packet

Evidence is generated per observer or observing institution.

```yaml
evidence_id: null
observer_id: null
manifestation_id: null
observed_at: null
location_ref: null
raw_observation: null
interpretation_tags: []
confidence: null
skill_or_capability_refs: []
source_chain: []
shareability: null
```

`raw_observation` should remain close to what was actually perceived.

Example:

```yaml
raw_observation: "fresh bark damage around three sap-bearing trees"
interpretation_tags:
  - recent_feeding_or_resource_use
confidence: moderate
```

Do not encode `caused_by_wurmple` unless that attribution was actually observed or inferred through a supported reasoning step.

## Trainer capability effects

Trainer Skills, Edges and Features may alter:
- detection chance;
- precision;
- confidence;
- classification detail;
- track age estimation;
- ability to distinguish species traces;
- ability to approach without disturbance;
- ability to constrain or redirect actors safely when mechanically supported.

They must not grant unrestricted access to hidden ecology truth.

PTU Survival is a primary baseline for wilderness scouting, tracking and resource discovery. Other skills/features may participate only when verified by the active rules profile.

## Hypothesis record

Players and NPCs can maintain competing explanations.

```yaml
hypothesis_id: null
subject_process_scope: null
claim: null
supporting_evidence_ids: []
contradicting_evidence_ids: []
confidence: null
status: open
created_by: null
created_at: null
```

Possible statuses:

```text
open
strengthened
weakened
falsified
confirmed_enough_for_action
resolved
```

`confirmed_enough_for_action` does not mean metaphysical certainty. It means the actor/institution considers the evidence sufficient to intervene.

## Intervention record

An intervention changes ecological pressures through declared world-state effects.

```yaml
intervention_id: null
actor_ids: []
target_process_ids: []
method: null
required_capabilities: []
immediate_world_effects: []
possible_tactical_handoff: null
expected_observable_outcomes: []
verification_after: null
risk_refs: []
```

Initial intervention families:

```text
withdraw_or_avoid
protect_or_close_route
restore_cover
restore_resource
remove_disturbance
redirect_waste_or_food
repair_water_access
relocate_human_activity
wait_for_temporal_window
observe_only
capture_or_restrain_if_legal
structured_battle_if_escalated
```

Interventions that assert capture, restraint, status, damage, forced movement or battle outcomes must be resolved by the appropriate authoritative mechanical system.

## Consequence record

The ecology ledger applies semantic consequences after an intervention.

```yaml
consequence_id: null
intervention_id: null
process_id: null
population_pressure_delta: null
visibility_pressure_delta: null
resource_state_delta: null
disturbance_delta: null
habituation_delta: null
territorial_pressure_delta: null
recovery_timer_change: null
reason_refs: []
```

Exact numerical models remain separate from this contract.

A visible Pokémon disappearing after intervention is not itself proof that population declined.

## Delayed verification

Each intervention should define at least one expected future observation when practical.

Example:

```text
repair damaged water access
-> immediate disturbance rises temporarily
-> after two in-world days, exposed activity near alternate watering point should fall
-> after five in-world days, vegetation/water-use signs should stabilize if hypothesis was correct
```

The verification can:
- support the hypothesis;
- show no meaningful change;
- expose a second pressure;
- reveal that the original diagnosis was wrong.

This creates ecological stories from persistent state rather than scripted success flags.

## Quest/event binding

An ecology-driven quest should bind to evidence and processes rather than hard-coded narrative stages alone.

```yaml
quest_id: null
trigger_evidence_rules: []
known_evidence_ids: []
available_hypotheses: []
intervention_options: []
followup_observation_rules: []
resolution_conditions: []
```

A quest can begin when:
- enough independent evidence accumulates;
- one institution receives a report;
- a threshold process persists for a duration;
- a player personally observes a significant manifestation;
- multiple observers report contradictory evidence requiring investigation.

## Resource-node first authoring

For multi-species ecology scenes, author the resource or environmental pressure before selecting visible actors.

Preferred flow:

```text
resource / refuge / disturbance
-> eligible local species
-> active interaction edges
-> temporal conditions
-> observable manifestations
-> player-facing scene
```

This keeps scenes causally grounded.

## Nesting and juvenile escalation

Nesting pressure receives a dedicated rule because it changes tolerance sharply.

Possible manifestations before combat:
- repeated warning calls;
- blocking behavior;
- distraction displays;
- relocation of juveniles;
- retreat to cover;
- territorial circling;
- refusal to leave a resource or shelter.

Escalation should consider species baseline, individual state, distance, exits, cover, previous disturbance and Trainer behavior.

No automatic battle occurs solely because a player enters a nesting zone.

## Human settlement ecology

Settlement behavior can create ecological processes.

Examples:

```text
market waste schedule
-> scavenger concentration
-> habituation
-> conflict around closing time
```

```text
seasonal crop harvest
-> temporary resource pulse
-> herbivore concentration
-> predator follow-through
-> producer complaints
```

```text
popular feeding custom
-> artificial concentration
-> changed territorial boundaries
-> dependence/conflict pressure
```

Human routines therefore need timestamps and locations when they materially affect ecology.

## Worldgen dependency

This contract can be implemented at schema/policy level before the global planet is frozen.

Implementation-facing local bindings require the selected world:

```text
frozen coordinate
-> real Minecraft biome/tags
-> resource/site geometry
-> ecological process placement
-> visible manifestation projection
```

Marea examples remain migratable until the global worldgen seed/config is approved.

## AutoPTU handoff

Most observation and intervention logic remains in Ouros world state.

Structured handoff occurs only when an intervention or behavior reaches a mechanical boundary such as:
- combat begins;
- capture attempt begins;
- restraint or immobilization becomes mechanical;
- damage/status is applied;
- forced movement matters;
- exact initiative/action economy matters.

### Reduced encounter profile

A reduced defensive encounter should restrict itself to mechanics supported by current audited contracts:
- ordinary targeting/range/LoS;
- base movement;
- core calculations;
- action economy/initiative;
- ordinary legal-action generation;
- simple move/ability/status subsets only when individually verified.

Avoid bespoke terrain reactions, complex pursuit, reinforcement policy, Trainer interrupt chains or unsupported world playback.

### Full ecological encounter profile

A full version may require:
- complete movement including forced movement/interception;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics semantic playback/writeback.

Each concrete encounter must declare only the categories it actually consumes.

## Current engine readiness

Read-only AutoPTU-Java head checked for this contract: `61321c3ab798993be25e10f287e7a375e5db3b63`.

Current classification remains:

VERIFIED within audited contracts:
- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

MIXED / PARTIAL / BLOCKING outside verified slices:
- terrain / weather / hazards / zones / reactions.

BLOCKING as complete family:
- AI tactical policy.

PARTIAL / BLOCKING end-to-end:
- Minecraft / Cobblemon / Craftics adapter/playback support.

The recent authoritative tile-trap work remains a bounded verified slice and does not promote the complete terrain/hazard family.

## Validation fixtures

Future deterministic fixtures should verify:

1. two observers can receive different evidence from the same ecological truth;
2. an NPC cannot cite a manifestation they did not observe or receive;
3. improved Survival can increase evidence precision without revealing hidden cause directly;
4. a visible species can be a downstream symptom while another process is causal;
5. an intervention can reduce visibility without reducing population;
6. a wrong hypothesis can produce no improvement or a new observable consequence;
7. a successful ecological intervention produces follow-up evidence after the expected delay;
8. nesting pressure changes warning/avoidance/escalation probabilities without forcing battle;
9. settlement routines can modify local ecological pressure;
10. entering AutoPTU writes back semantic outcomes without letting Minecraft presentation author tactical truth.

## Open questions

- canonical evidence confidence scale;
- skill-check and passive-observation policy;
- evidence expiry/decay;
- institution trust and conflicting reports;
- how observation state persists for large player populations;
- how public/shared discoveries avoid becoming universal omniscience;
- precise interface between ecological AI intent and Minecraft entity behavior;
- exact AutoPTU handoff payload for ecological escalation.
