# Biosecurity, Introduced Species & Translocation Layer

Status: proposed systems design. Not established Ouros canon.

Date: 2026-08-20

## Purpose

This layer extends conservation, science, transport, custody, ecology and case systems with persistent ecological provenance.

It answers:

- where a newly observed population may have come from;
- whether arrival was natural, deliberate, accidental or still unknown;
- whether the population is temporary or established;
- what effects are actually observed;
- which pathways remain open;
- what people believe about the arrival;
- what management actions are being considered;
- what remains unresolved.

It must never reduce all unfamiliar Pokémon to pests or targets.

## Core separation

Keep these concepts distinct:

```text
species identity
-> individual Pokémon identity
-> local population/collective
-> observation
-> origin/provenance hypothesis
-> arrival pathway
-> establishment state
-> spread state
-> ecological-impact evidence
-> public belief
-> management decision
-> mechanical PTU state
```

A species can be introduced without causing harm.
A species can expand naturally into a new area.
A newly observed Pokémon can be a lost individual rather than a population.
A harmful local condition can be caused by infrastructure or habitat change rather than by the newcomer.

## 1. Biosecurity case

```yaml
biosecurity_case:
  biosecurity_case_id: null
  focal_species_ids: []
  focal_population_or_collective_ids: []
  first_observation_event_ids: []
  affected_location_ids: []
  provenance_hypothesis_ids: []
  pathway_ids: []
  establishment_assessment_id: null
  spread_assessment_id: null
  impact_assessment_ids: []
  management_review_ids: []
  public_information_packet_ids: []
  case_status: OPEN
  canon_status: proposed
```

Suggested case states:

- OPEN
- MONITORING
- PATHWAY_INVESTIGATION
- ESTABLISHMENT_REVIEW
- IMPACT_REVIEW
- MANAGEMENT_ACTIVE
- STABLE_NO_ACTION
- RESOLVED
- REOPENED

A case can remain unresolved for years of world time.

## 2. Observation record

```yaml
arrival_observation:
  observation_id: null
  observer_ids: []
  location_id: null
  timestamp: null
  species_claim: null
  individual_identity_claims: []
  count_or_range: null
  behavior_observed: []
  reproduction_evidence: []
  media_refs: []
  photo_or_sensor_refs: []
  confidence: unresolved
```

A photograph can support presence.
It does not prove origin.

## 3. Provenance hypothesis

```yaml
population_provenance_hypothesis:
  hypothesis_id: null
  focal_population_id: null
  hypothesis_type: null
  source_location_candidates: []
  pathway_candidates: []
  supporting_evidence_ids: []
  contradicting_evidence_ids: []
  confidence: unresolved
  review_status: active
```

Candidate hypothesis types:

- NATIVE_PREVIOUSLY_UNRECORDED
- NATURAL_RANGE_EXPANSION
- DELIBERATE_AUTHORIZED_INTRODUCTION
- DELIBERATE_UNAUTHORIZED_RELEASE
- CAPTIVE_ESCAPE
- NURSERY_OR_BREEDING_ESCAPE
- TRANSPORT_HITCHHIKER
- CARGO_ASSOCIATED
- POST_CRISIS_DISPLACEMENT
- PORTAL_OR_ANOMALOUS_CROSSING
- UNKNOWN

Do not turn a hypothesis into a case allegation without separate evidence.

## 4. Arrival pathways

```yaml
arrival_pathway:
  pathway_id: null
  origin_ref: null
  destination_ref: null
  pathway_type: transport|cargo|nursery|release|escape|natural_corridor|storm_displacement|anomaly|unknown
  linked_service_ids: []
  linked_shipment_ids: []
  linked_actor_ids: []
  active_window: null
  evidence_ids: []
  status: suspected
```

Pathways can intersect existing systems:

- ferry routes;
- cargo lines;
- nurseries;
- research expeditions;
- conservation relocations;
- tourism;
- illicit networks;
- disaster displacement;
- anomalous spaces.

The pathway is not automatically wrongdoing.

## 5. Establishment state

```yaml
establishment_assessment:
  assessment_id: null
  focal_population_id: null
  observation_window: null
  repeated_presence_evidence: []
  reproduction_evidence: []
  juvenile_observation_refs: []
  persistence_evidence: []
  range_change_refs: []
  conclusion: unresolved
```

Candidate conclusions:

- SINGLE_OR_TRANSIENT
- REPEATED_PRESENCE
- BREEDING_SUSPECTED
- BREEDING_SUPPORTED
- SELF_SUSTAINING_SUPPORTED
- LONG_ESTABLISHED
- UNRESOLVED

Do not invent numerical ecological thresholds unless a later simulation model supplies them.

## 6. Spread state

```yaml
spread_front:
  spread_front_id: null
  focal_population_id: null
  source_area_id: null
  newly_observed_area_ids: []
  first_detection_times: []
  corridor_or_pathway_refs: []
  barrier_refs: []
  confidence: unresolved
```

Spread can be discontinuous.

A new record far away can represent:

- transport;
- a second introduction;
- observer error;
- an unrecognized corridor;
- the same persistent individual;
- true population expansion.

## 7. Impact assessment

```yaml
biosecurity_impact_assessment:
  impact_assessment_id: null
  focal_population_id: null
  observation_window: null
  affected_population_ids: []
  affected_resource_ids: []
  affected_infrastructure_ids: []
  observed_changes: []
  causal_hypothesis_ids: []
  alternative_explanations: []
  evidence_ids: []
  conclusion: unresolved
```

Possible impact dimensions:

- food competition;
- nesting competition;
- predation;
- scavenging;
- habitat modification;
- water/soil interaction;
- crop/stored-food use;
- infrastructure damage;
- beneficial resource use;
- new mutualistic relationship;
- visitor pressure caused by rarity;
- disease/exposure association;
- no detected impact.

Mixed outcomes are valid.

## 8. Do not use one universal invasive flag

Avoid:

```yaml
invasive: true
```

Prefer evidence-bearing state:

```yaml
management_classification:
  classification_id: null
  focal_population_id: null
  classification_term: null
  issuing_actor_id: null
  evidence_basis_ids: []
  scope_location_ids: []
  effective_from: null
  review_date: null
```

Different institutions can use different terms until canon resolves their authority.

## 9. Management response

Candidate actions:

- monitoring only;
- pathway inspection;
- shipping or nursery protocol change;
- temporary containment of a confirmed escape;
- attractant removal;
- habitat restoration;
- targeted relocation;
- public guidance;
- temporary visitor restriction;
- research sampling;
- protection of the newcomer from opportunistic capture;
- acceptance of a long-established population;
- no action.

Management should record objectives and review dates.

## 10. Translocation

Translocation must preserve Pokémon identity and custody history.

```yaml
pokemon_translocation_event:
  translocation_id: null
  pokemon_entity_ids: []
  population_or_collective_id: null
  source_location_id: null
  destination_location_id: null
  stated_reason: null
  authorization_ref: null
  custody_transition_refs: []
  release_event_refs: []
  post_release_monitoring_ids: []
  outcome_status: unresolved
```

Rules:

- relocation is not automatically beneficial;
- relocation does not create ownership;
- a released Pokémon keeps the same persistent identity;
- a destination population does not automatically accept the newcomer;
- capture mechanics must remain PTU/Caelo-authoritative.

## 11. Escape events

```yaml
escape_event:
  escape_event_id: null
  source_site_id: null
  pokemon_entity_ids: []
  species_ids: []
  custody_state_before: null
  last_confirmed_time: null
  detection_time: null
  escape_cause_hypotheses: []
  containment_actions: []
  recovered_entity_ids: []
  unresolved_entity_ids: []
```

An escaped individual is not an established population.

## 12. Public information and stigma

Media can create pressure before science resolves the case.

Possible effects:

- collectors travel to the site;
- residents demand action;
- businesses market the sighting;
- false reports multiply;
- legitimate conservation work becomes harder;
- an introduced population becomes culturally accepted;
- native species are incorrectly blamed for impacts.

The media layer remains responsible for publication and correction history.

## 13. Interaction with illicit networks

A biosecurity case can uncover smuggling or unauthorized release.

It must not assume it.

Use:

```text
unusual species observation
-> pathway evidence
-> shipment/custody anomaly
-> case evidence
-> allegation only when supported
```

Do not create villains merely to explain ecological novelty.

## 14. Interaction with outbreak surveillance

Species movement and health movement are separate.

A newly arrived population can be associated with a health signal.
That association does not prove transmission.

The health-surveillance layer owns:

- case definitions;
- exposure records;
- clinical diagnosis;
- outbreak hypotheses.

Biosecurity owns ecological provenance and movement pathways.

## 15. Minecraft/Cobblemon projection

Potential visible states:

- newly observed wild Pokémon in a zone;
- observation markers;
- temporary survey camps;
- port inspection activity;
- nursery containment gates;
- seasonal monitoring signs;
- altered aggregate spawn context when adapter support exists;
- individual tagged/released Pokémon when persistent identity support exists;
- temporary closure or visitor routing.

Loaded entities must not become the source of truth for population size.

## 16. Offline advancement

Large-scale population state can advance coarsely while chunks are unloaded.

Possible periodic updates:

- persistence check;
- new observation opportunities;
- spread-front update;
- pathway closure/reopening;
- management-review clock;
- ecological-impact evidence accumulation.

Do not simulate every birth, death, capture or predation event.

## 17. PTU/Caelo boundary

This layer creates no combat mechanic.

Do not infer:

- capture bonuses;
- encounter XP modifiers;
- automatic hostility;
- morale;
- pack bonuses;
- forced surrender;
- relocation Skill checks;
- poison/disease status;
- ecological damage from ordinary attacks;
- removal requirements.

Exact mechanical effects remain blocked behind governing PTU/Caelo rules and verified engine implementation.

## 18. Permanent capability categories

Encounter contracts use the same project-wide families:

- targeting/footprints/range/LoS;
- base movement legality;
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
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## 19. Encounter contract A — Cargo-Hitchhiker Discovery

Narrative premise:

Workers open a legitimate shipment and discover several unfamiliar wild Pokémon that appear to have traveled with the cargo. No one yet knows whether this is a single accidental arrival or part of an established pathway.

FULL version:

- Pokémon attempt to escape through multiple exits;
- players may block routes, withdraw or protect workers;
- cargo creates changing lanes;
- AI understands escape rather than fighting to KO;
- world state records which individuals escaped and where.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if cargo lanes change;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:

Resolve escape paths in overworld state before combat. If conflict occurs, freeze cargo geometry and run one static legal encounter. Record captured, withdrawn, escaped or observed individuals only through authoritative outcomes and explicit world-state actions.

## 20. Encounter contract B — Nursery Escape Perimeter

Narrative premise:

Several Pokémon are missing from a nursery after infrastructure damage. The immediate objective is recovery and evidence preservation, not defeating them.

FULL version:

- multiple mobile objectives;
- perimeter exits;
- civilians/workers;
- non-KO recovery goals;
- objective-aware AI;
- possible weather or damaged-structure hazards.

Dependencies:

- complete movement/interception — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING when environmental damage matters;
- AI tactical policy — BLOCKING;
- playback — BLOCKING;
- lifecycle/status/damage/Move/Ability/item/Feature families — PARTIAL as exact participants require;
- base targeting/calculations/initiative/legal-action infrastructure — VERIFIED where applicable.

REDUCED version:

The search occurs in overworld state. Each located Pokémon remains a persistent entity. Only a genuine confrontation becomes a static AutoPTU battle. Recovery/custody is resolved outside the grid.

## 21. Encounter contract C — Wetland Spread Survey

Narrative premise:

A new Water-type population has appeared at several points along a wetland system. Players must collect observations and determine whether one expanding population or multiple arrival events explain the pattern.

FULL version:

- moving wild groups;
- changing water routes;
- optional sampling/observation objectives;
- withdrawal behavior;
- weather/terrain state can matter.

Dependencies:

- targeting/LoS — VERIFIED;
- base movement including Swim legality — VERIFIED;
- complete movement/interception — BLOCKING for moving groups;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- damage/status/Move/Ability/item/Feature families — PARTIAL as used;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic wetland effects;
- AI tactical policy — BLOCKING;
- playback — BLOCKING.

REDUCED version:

Survey and population inference occur outside battle. Use static legal encounters only when individual wild interactions become conflicts. The result writes back observations, not automatic population conclusions.

## 22. Design guardrails

- Never label a species invasive from a single sighting.
- Never label a species invasive merely because it is foreign.
- Never infer introduction from abundance alone.
- Never infer wrongdoing from a suspected human pathway.
- Never convert public fear into ecological evidence.
- Never convert capture success into proof that removal was justified.
- Never erase persistent Pokémon identity during relocation or release.
- Never duplicate PTU capture, tracking, terrain or status rules in Minecraft scripts.
- Never create a universal eradication objective.
- Never assume all members of a species have the same effect on every habitat.
- Never treat a range expansion caused by climate/seasonality as the same thing as deliberate release.

## 23. Integration with existing layers

Conservation owns management areas and stewardship decisions.

Science owns observation programs, datasets and hypothesis review.

Wild collective/population systems own group persistence.

Interspecies ecology owns predator/competitor/mutualistic relationships.

Travel, maritime and transport systems own pathways.

Nursery/custody systems own captive provenance.

Illicit networks own smuggling/diversion only when evidence supports it.

Cases own allegations and evidence of wrongdoing.

Health surveillance owns disease/exposure questions.

Media owns public narratives.

Biosecurity connects these systems around ecological provenance, establishment, spread and evidence-driven response.