# Scientific Research, Evidence, Publication & Replication Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-31

## Purpose

This extension preserves scientific work as durable world state from a bounded research question through evidence collection, analysis, interpretation, review, publication, replication and correction.

It does not replace Observation, Archives, Material Culture, Case/Custody, Media, Public Memory, Travel/Expedition or any subject-domain system. It links those owner systems into an auditable scientific lineage.

It does not invent a universal science minigame, experiment DC, grant economy, ethics regime, publication law, Researcher progression loop or laboratory crafting system.

## Core authority rule

Scientific records are claims about evidence, not world truth by themselves.

`WORLD_FACT != RESEARCH_CLAIM`

`OBSERVATION != INTERPRETATION`

`INTERPRETATION != CONSENSUS`

`PUBLICATION != TRUTH`

`REPLICATION_FAILURE != FRAUD`

`CORRECTION != ORIGINAL_RECORD_ERASED`

## Research project

```yaml
research_project:
  project_id: null
  institution_refs: []
  lead_actor_refs: []
  contributor_refs: []
  sponsor_refs: []
  subject_domain_refs: []
  research_question_refs: []
  project_started_at: null
  project_closed_at: null
  current_method_version_ref: null
  evidence_collection_refs: []
  dataset_refs: []
  analysis_refs: []
  claim_refs: []
  publication_refs: []
  replication_refs: []
  correction_refs: []
  dependency_refs: []
  status: ACTIVE
```

Possible project states:

PROPOSED, ACTIVE, PAUSED, FIELDWORK, ANALYSIS, REVIEW, PUBLISHED, REPLICATION_PENDING, CLOSED, ABANDONED, DISPUTED.

Status is workflow only. It does not imply quality.

## Research question

```yaml
research_question:
  question_id: null
  project_id: null
  question_text_ref: null
  subject_refs: []
  originating_knowledge_gap_refs: []
  conflicting_claim_refs: []
  prior_work_refs: []
  answer_state: OPEN
```

Possible answer states:

OPEN, PARTIALLY_SUPPORTED, SUPPORTED_UNDER_SCOPE, NOT_SUPPORTED_UNDER_SCOPE, INCONCLUSIVE, REFRAMED, CLOSED.

A question should emerge from a real knowledge gap, anomaly, contradiction or authored institutional goal.

`QUESTION_OPEN != HIDDEN_ANSWER_PREAUTHORED`

## Method / protocol version

```yaml
research_method_version:
  method_version_id: null
  project_id: null
  predecessor_version_ref: null
  created_at: null
  author_refs: []
  observation_requirements: []
  sampling_requirements: []
  instrument_refs: []
  intervention_refs: []
  exclusion_rules: []
  processing_plan_ref: null
  analysis_plan_ref: null
  safety_or_access_refs: []
  mechanics_gate_refs: []
  status: CURRENT
```

The method records what investigators intended to do. Actual execution is recorded separately.

`METHOD_PLANNED != METHOD_EXECUTED`

`METHOD_CHANGED != EARLIER_DATA_INVALID`

## Evidence collection episode

```yaml
research_collection_episode:
  collection_episode_id: null
  project_id: null
  method_version_ref: null
  started_at: null
  ended_at: null
  location_refs: []
  collector_refs: []
  observation_refs: []
  sample_refs: []
  instrument_output_refs: []
  environmental_state_refs: []
  intervention_refs: []
  deviation_refs: []
  disturbance_refs: []
  access_authorization_refs: []
  completeness: UNKNOWN
```

Observation owns the observation event. Material Culture / Archives / Case systems own physical samples and custody. This record only links them into the research context.

`SAMPLE_COLLECTED != SAMPLE_OWNED`

`SAMPLE_HELD != COLLECTION_AUTHORIZED`

`POKEMON_OBSERVED != POKEMON_OWNED`

`POKEMON_TAGGED != POKEMON_COMBATANT`

## Sample and specimen research link

```yaml
research_sample_link:
  research_sample_link_id: null
  project_id: null
  underlying_object_or_specimen_ref: null
  collection_episode_ref: null
  sample_kind_ref: null
  source_subject_ref: null
  provenance_refs: []
  custody_refs: []
  condition_refs: []
  subsample_refs: []
  analysis_use_refs: []
  archive_ref: null
```

The research layer does not create custody law, ownership or specimen-handling mechanics.

## Dataset version

```yaml
research_dataset_version:
  dataset_version_id: null
  project_id: null
  predecessor_version_ref: null
  created_at: null
  included_observation_refs: []
  included_sample_measurement_refs: []
  excluded_record_refs: []
  exclusion_reason_refs: []
  transformation_refs: []
  missingness_notes: []
  provenance_refs: []
  archive_ref: null
  status: CURRENT
```

`RAW_RECORD != CLEANED_DATA`

`CLEANED_DATA != ANALYSIS_RESULT`

`DATASET_UPDATED != PRIOR_DATASET_ERASED`

A project can retain several legitimate dataset versions.

## Analysis episode

```yaml
research_analysis_episode:
  analysis_id: null
  project_id: null
  dataset_version_ref: null
  method_version_ref: null
  analyst_refs: []
  started_at: null
  completed_at: null
  transform_refs: []
  calculation_refs: []
  output_refs: []
  anomaly_refs: []
  limitation_refs: []
  mechanics_gate_refs: []
  status: COMPLETE
```

Exact calculations with PTU consequences require governing source validation. Narrative analysis may organize observations without inventing PTU mechanics.

## Interpretation and scientific claim

```yaml
scientific_claim:
  claim_id: null
  project_id: null
  claim_text_ref: null
  claim_scope_ref: null
  supporting_analysis_refs: []
  supporting_observation_refs: []
  contradicting_refs: []
  limitation_refs: []
  author_refs: []
  confidence_band: null
  created_at: null
  status: PROPOSED
```

Possible states:

PROPOSED, INTERNALLY_SUPPORTED, DISPUTED, PUBLISHED, PARTIALLY_CORRECTED, WITHDRAWN, SUPERSEDED.

Confidence is a metadata band, not a probability oracle.

`CLAIM_CONFIDENT != CLAIM_TRUE`

`CLAIM_DISPUTED != CLAIM_FALSE`

## Internal review

```yaml
research_review_episode:
  review_id: null
  project_id: null
  reviewed_object_ref: null
  reviewer_refs: []
  review_type: INTERNAL
  opened_at: null
  closed_at: null
  concern_refs: []
  requested_revision_refs: []
  response_refs: []
  outcome: REVISION_REQUESTED
```

Review types may include INTERNAL, EXTERNAL, EDITORIAL, REPLICATION_REVIEW or INSTITUTIONAL, but exact institutions and procedures are authored world state.

`REVIEW_PASSED != WORLD_TRUTH_CONFIRMED`

`REVIEW_CRITICISM != MISCONDUCT_FINDING`

## Publication record

Media owns actual publication and delivery. Scientific Research owns the scientific lineage attached to that publication.

```yaml
research_publication_link:
  publication_link_id: null
  project_id: null
  publication_record_ref: null
  title_ref: null
  author_refs: []
  claim_refs: []
  dataset_version_refs: []
  method_version_refs: []
  publication_date: null
  review_refs: []
  correction_refs: []
  citation_dependency_refs: []
  status: PUBLISHED
```

`PUBLISHED != RECEIVED_BY_ALL_ACTORS`

`PUBLISHED != ACCEPTED_BY_ALL_RESEARCHERS`

`PUBLISHED != CANONICAL_TRUTH`

## Replication project link

```yaml
research_replication:
  replication_id: null
  source_project_ref: null
  source_claim_refs: []
  replicating_project_ref: null
  method_equivalence_ref: null
  new_evidence_refs: []
  result_scope_ref: null
  outcome: INCONCLUSIVE
  completed_at: null
```

Possible outcomes:

SUPPORTED_UNDER_SCOPE, NOT_SUPPORTED_UNDER_SCOPE, PARTIAL, INCONCLUSIVE, METHOD_NOT_COMPARABLE.

`REPLICATION_SUPPORTED != ORIGINAL_STUDY_PERFECT`

`REPLICATION_NOT_SUPPORTED != FRAUD_PROVEN`

## Correction, expression of concern and retraction lineage

```yaml
research_record_revision:
  revision_id: null
  target_publication_or_claim_ref: null
  revision_type: CORRECTION
  initiated_at: null
  effective_at: null
  reason_refs: []
  affected_claim_refs: []
  unaffected_claim_refs: []
  replacement_or_superseding_refs: []
  authority_or_editor_ref: null
  public_notice_ref: null
  status: EFFECTIVE
```

Revision types may include CORRECTION, PARTIAL_CORRECTION, EXPRESSION_OF_CONCERN, RETRACTION, WITHDRAWAL or SUPERSESSION when the local institution supports them.

`RETRACTION != DATA_DESTROYED`

`RETRACTION != MISCONDUCT_PROVEN`

`CORRECTED_CLAIM != EARLIER_PUBLIC_RECEPTION_ERASED`

`ONE_CLAIM_RETRACTED != ENTIRE_PROJECT_INVALID`

## Downstream dependency graph

```yaml
research_dependency:
  dependency_id: null
  dependent_project_or_claim_ref: null
  source_claim_or_dataset_ref: null
  dependency_kind: EVIDENCE
  recorded_at: null
  reassessment_state: NOT_REVIEWED
  reassessment_refs: []
```

When a source changes, downstream projects become candidates for review. They do not automatically collapse.

`SOURCE_CORRECTED != DEPENDENT_CLAIM_AUTOMATICALLY_FALSE`

## Null and negative findings

Research gameplay should preserve meaningful non-discoveries.

Examples:

- the suspected migration shift is not observed during the scoped season;
- two habitats show no meaningful difference under the current method;
- a purported phenomenon cannot be reproduced;
- a sample is too degraded to answer the question;
- a field site is unsuitable for the planned observation;
- an apparent pattern disappears after correcting a dataset error.

These can close or redirect arcs without manufacturing villains or anomalies.

## Institutional portfolio

```yaml
research_institution_portfolio:
  institution_ref: null
  active_project_refs: []
  paused_project_refs: []
  archived_project_refs: []
  field_site_refs: []
  lab_space_refs: []
  archive_collection_refs: []
  staff_role_refs: []
  equipment_refs: []
  dependency_refs: []
```

Institution leadership is owned elsewhere. A project may outlive its founder or lead investigator.

## Funding and resource boundary

Ouros may track that a project lacks staff, transport, equipment access or institutional capacity if those facts already exist in world state.

Do not invent:

- grant formulas;
- publication fees;
- salaries;
- procurement law;
- research budgets;
- automatic sponsor influence;
- corruption from funding alone.

A sponsor may have motives and conditions only when authored.

## Ethical / access boundary

This extension does not create a universal ethics board or collection right.

Research involving people, owned Pokémon, wild Pokémon, restricted sites, private records or cultural materials must defer to the owner systems and local canon.

`SCIENTIFIC_VALUE != ACCESS_PERMISSION`

`RESEARCH_REQUEST != CONSENT`

`OBSERVABLE_IN_MINECRAFT != AUTHORIZED_TO_SAMPLE`

## PTU/Caelo boundary

Scientific activity can call exact PTU/Caelo mechanics only after source validation.

Do not infer:

- Researcher or Scientist Features from profession labels;
- Education Skill outcomes from prose research;
- item crafting from laboratory presence;
- Move learning from experimentation;
- Pokémon creation from generic science;
- status application from field tagging;
- Pokédex registration as proof of a hypothesis;
- Type as an instrument capability;
- Psychic/Aura effects as truth detectors;
- a Move or Ability as a generic sensor without exact rules support.

## Minecraft/Cobblemon boundary

SAFE presentation can show labs, benches, notebooks, sample containers, field stations, instruments, notice boards, specimen storage, observers and published results after Ouros has established them.

Minecraft/Cobblemon must not decide:

- research questions;
- hypothesis truth;
- sample provenance from item appearance alone;
- whether a collection was authorized;
- dataset inclusion from loaded entities;
- analysis outcomes;
- publication acceptance;
- replication success;
- scientific consensus;
- whether a Pokémon is a research subject or combatant;
- PTU effects from laboratory animations.

Authority flow remains:

`Ouros research/world facts -> explicit BattleSpec only for a separate tactical incident -> AutoPTU -> adapter -> Minecraft/Cobblemon presentation`

## Encounter contract — Field Observation Perimeter Incident

Narrative premise: an active field site becomes unsafe while a team is collecting noncombat observations.

Full intended version may include active evacuation, protected instruments, dynamic terrain/weather, wildlife withdrawal, forced movement and AI that understands protect/withdraw semantics.

Permanent dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL where selected attacks require it
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when active conditions matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full status: BLOCKED.

Reduced status: READY at narrative-contract level with individually audited combat content.

Before initiative, Ouros terminates collection, removes researchers, instruments and noncombat research subjects from BattleSpec and freezes the site geometry. AutoPTU may return only `IMMEDIATE_FIELD_SITE_APPROACH_CLEAR`.

`BATTLE_WON != DATA_COLLECTION_COMPLETED`

`BATTLE_WON != HYPOTHESIS_SUPPORTED`

`BATTLE_FAILURE_WITHOUT_RESCUE_CONTRACT != RESEARCHERS_HARMED`

## Encounter contract — Sample Transfer Chokepoint

Narrative premise: a research sample must later move between an authorized collection site and a facility, but a tactical incident blocks the route.

Full version may require protected-object carrying, escort, vehicle movement, complete lifecycle and tactical route-control AI.

Full status: BLOCKED.

Reduced status: READY.

The sample and custody record stay outside BattleSpec. Players clear a static corridor. Permitted output: `IMMEDIATE_SAMPLE_ROUTE_CLEAR`.

`IMMEDIATE_SAMPLE_ROUTE_CLEAR != SAMPLE_DELIVERED`

`SAMPLE_DELIVERED != ANALYSIS_COMPLETE`

`BATTLE_WON != CUSTODY_TRANSFERRED`

## Encounter contract — Research Station Power Isolation Perimeter

Narrative premise: a service interruption affects a field or laboratory station while a separate immediate threat blocks safe access.

Full version may require electrical/environmental hazards, zones, reactions, dynamic equipment state and tactical AI.

Full status: BLOCKED.

Reduced status: READY.

Infrastructure state is frozen outside BattleSpec. AutoPTU may resolve a static perimeter only and return `IMMEDIATE_RESEARCH_STATION_ACCESS_CLEAR`.

`BATTLE_WON != POWER_RESTORED`

`POWER_RESTORED != DATA_RECOVERED`

`ACCESS_CLEAR != EXPERIMENT_RESUMED`

## Encounter contract — Wildlife Tagging Support Incident

Narrative premise: a project intends to observe or tag a wild Pokémon under an authored legal/ethical procedure, and an unrelated threat appears nearby.

Full tagging during combat is not assumed. It may depend on status, capture, item, movement, reaction and Trainer Feature semantics that require exact PTU/Caelo and engine verification.

Full status: BLOCKED unless every required mechanic for the specific tagging procedure is verified.

Reduced status: CONDITIONAL READY only when the tagging or observation episode occurs entirely outside BattleSpec before or after a conventional audited battle.

`POKEMON_VISIBLE != TAGGING_AUTHORIZED`

`BATTLE_WON != POKEMON_TAGGED`

`POKEMON_DEFEATED != SAMPLE_OBTAINED`

`TAGGING_COMPLETED != OWNERSHIP_CHANGED`

## Generation guardrails

1. Preserve raw evidence and later interpretation separately.
2. Keep method versions and actual execution distinct.
3. Record intervention/disturbance when observation conditions changed.
4. Keep physical sample custody in owner systems.
5. Do not manufacture certainty because a project needs closure.
6. Null results and failed hypotheses are valid outcomes.
7. A correction preserves prior historical reception.
8. A retraction requires an authored institutional event; it does not imply misconduct by default.
9. Do not turn every scientific disagreement into sabotage.
10. Do not turn every anomaly into a Legendary or supernatural event.
11. Do not reward publication with unsourced PTU progression.
12. Do not infer Pokémon abilities from Type or species flavor.
13. Do not use Minecraft observation as canonical sampling authority.
14. Prefer revisiting existing sites and datasets over generating disposable laboratories.
15. Link downstream reliance so old research can matter years later.

## Promotion gate

Before a concrete research program becomes canon, answer:

- Which institution or actor owns the project?
- What exact question is being asked?
- Which world facts created the knowledge gap?
- What method/protocol is authorized?
- Which observations, samples or records already exist?
- Who may collect or access them?
- Which PTU/Caelo mechanics are actually required?
- Which dataset/analysis steps are narrative only versus mechanically resolved?
- How are claims reviewed or published in this region?
- Does replication exist as a formal institution or simply as independent follow-up work?
- What correction/revision mechanisms exist?
- Which archive/media/public-memory systems receive the result?
- Which encounter version is implementable under the live capability map?

Until those questions are answered, generated content remains proposed and provenance-aware.