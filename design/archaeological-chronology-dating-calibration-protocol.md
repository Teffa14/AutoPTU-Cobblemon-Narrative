# Archaeological Chronology, Dating, and Calibration Protocol

Status: proposed systems design. Not established Ouros canon.

Authority note: this protocol extends `design/myth-archaeology-sacred-sites-layer.md`. That layer remains the authority for archaeological sites, contexts, observations, interventions and historical claims.

## Purpose

This protocol defines how Ouros stores chronological evidence without turning every old object into an exact date.

It owns chronology records, dating attempts, relative-order constraints, sample/result linkage, calibration/reference revisions and chronology assessments.

It does not own the physical site, artifact identity, collection custody, laboratory equipment, language interpretation, PTU Skills or historical truth.

## Core separation

Keep this chain explicit:

```text
ARCHAEOLOGICAL_CONTEXT
  -> CHRONOLOGICAL_QUESTION
  -> MATERIAL / RELATIONSHIP SUITABLE FOR A METHOD
  -> SAMPLE OR RELATIVE OBSERVATION
  -> ANALYTICAL RESULT
  -> CALIBRATION / REFERENCE REVISION
  -> DATE INTERVAL OR ORDERING CONSTRAINT
  -> EVENT-LINK HYPOTHESIS
  -> CHRONOLOGY ASSESSMENT
  -> HISTORICAL CLAIM
```

Critical no-inferences:

```text
sample age != deposit age
deposit age != structure construction date
structure date != occupation date
artifact manufacture date != discard/deposition date
old material in young context != context is old
young material in old-looking structure != structure is young
wall age != inscription age
absolute-looking number != exact historical truth
calibrated interval != single year
recalibration != new historical event
method disagreement != fraud
no usable date != site has no age
solved ruin puzzle != chronology proven
Minecraft depth != archaeological age
```

## CHRONOLOGICAL_QUESTION

```yaml
chronological_question:
  chronology_question_id: null
  site_id: null
  target_subject_ids: []
  question_type: null
  target_event_type: null
  requested_precision: null
  reason_for_question: null
  related_historical_claim_ids: []
  status: OPEN
```

Candidate question types include relative sequence, earliest possible date, latest possible date, occupation interval, construction phase, repair phase, abandonment interval and event correlation.

## RELATIVE_ORDER_CONSTRAINT

Relative chronology is first-class data.

```yaml
relative_order_constraint:
  constraint_id: null
  earlier_subject_id: null
  later_subject_id: null
  relationship_type: null
  observation_ids: []
  context_integrity_assessment: null
  confidence: null
  status: ACTIVE
```

Relationship types can include BELOW_UNDISTURBED, CUTS, SEALED_BY, BUILT_AGAINST, OVERLIES, CONTAINS_REDEPOSITED_MATERIAL, REUSES_MATERIAL_FROM and CROSS_DATED_WITH.

A constraint can later be revised if disturbance, intrusion or context mixing is documented.

## DATING_ATTEMPT

```yaml
dating_attempt:
  dating_attempt_id: null
  chronology_question_id: null
  method_family: null
  directly_dated_subject_id: null
  inferred_event_target_id: null
  sample_id: null
  institution_id: null
  analyst_or_lab_ref: null
  method_revision: null
  raw_result_ref: null
  result_status: null
  limitations: []
  provenance: []
```

Suggested `result_status` values:

- USABLE
- PARTIALLY_USABLE
- NO_USABLE_DATE
- CONTAMINATED_OR_MIXED_SAMPLE_SUSPECTED
- REFERENCE_SEQUENCE_INSUFFICIENT
- REQUIRES_REVIEW
- SUPERSEDED_INTERPRETATION

The old attempt remains in history after a new attempt is performed.

## DATE_ESTIMATE_REVISION

```yaml
date_estimate_revision:
  date_estimate_revision_id: null
  dating_attempt_id: null
  estimate_type: null
  central_estimate: null
  interval_low: null
  interval_high: null
  confidence_or_probability_representation: null
  calendar_or_relative_system_ref: null
  calibration_or_reference_revision: null
  assumptions: []
  excluded_intervals: []
  supersedes_revision_id: null
  published_at: null
```

Ouros can use qualitative bands where exact numbers would create false precision.

## SAMPLE_TO_EVENT_LINK

A sample must never silently become the event itself.

```yaml
sample_to_event_link:
  link_id: null
  sample_id: null
  direct_dated_process: null
  proposed_historical_event_id: null
  linkage_basis: null
  reuse_risk: null
  redeposition_risk: null
  intrusion_risk: null
  confidence: null
  status: PROPOSED
```

Examples:

- a beam may date tree growth/felling, then support a construction claim;
- charcoal may date combustion of organic material, then support a deposit-formation claim;
- a manufactured object may provide a TPQ without dating the exact burial event;
- a later repair timber may occur inside a much older building.

## REFERENCE_CHRONOLOGY

```yaml
reference_chronology:
  reference_chronology_id: null
  method_family: null
  geographic_scope_ids: []
  material_scope: null
  revision_id: null
  valid_interval_claim: null
  institution_ids: []
  source_dataset_refs: []
  limitations: []
```

This supports tree-ring master sequences, artifact-style chronologies and future authored calibration frameworks without assuming any real-world method exists in Ouros canon.

## CHRONOLOGY_ASSESSMENT

```yaml
chronology_assessment:
  chronology_assessment_id: null
  site_or_subject_id: null
  relative_constraint_ids: []
  date_estimate_revision_ids: []
  event_link_ids: []
  conflicting_evidence_ids: []
  resulting_phase_order: []
  current_intervals: []
  confidence: null
  status: null
  unresolved_questions: []
```

Suggested states:

- PROVISIONAL
- ACTIVE
- CONTESTED
- REVISED
- PARTIALLY_RESOLVED
- UNRESOLVED

A chronology assessment is an interpretation. It never replaces the underlying observations.

## Disturbance and mixed contexts

When a later trench, burrow, flood, root system, collapse, excavation or repair disturbs older deposits, record the disturbance through Archaeology/Soil/Fluvial/Architecture as appropriate.

The chronology protocol only records how that disturbance changes confidence in chronological relationships.

Never treat context disturbance as misconduct without separate case evidence.

## Reused materials

Reuse should be common enough to matter.

A centuries-old beam can be built into a later structure. An old carved stone can be reused in a wall. A repaired roof can contain younger wood than the building. A museum object can be reburied during a crisis.

This creates useful history without requiring a mystery villain.

## Calibration and revision

A recalibration or reference update creates a new `date_estimate_revision`.

It must preserve:

- the original sample;
- the raw analytical result;
- the earlier published estimate;
- the calibration/reference version used at the time;
- any decisions or public interpretations based on the old estimate.

Chronicle can therefore remember that an institution once believed a temple was 1,800 years old even if later work moves the estimate.

## Public communication

Media/Public Memory should receive a simplified claim only after Science/Archaeology chooses what can be published.

Public statements should preserve uncertainty when it matters. A range can be presented as a range. `ABOUT_2,000_YEARS_OLD` can be a public simplification while the research record retains method and interval.

A correction changes current interpretation without erasing the old headline.

## Minecraft projection

Minecraft can show layers, foundations, weathering, repair masonry, inscriptions and excavation trenches.

It cannot authoritatively decide:

- context age;
- whether a block belongs to an original phase;
- whether a timber is reused;
- whether an inscription is contemporary with a wall;
- sample suitability;
- calibration;
- event correlation.

Block depth and palette are presentation only unless backed by Chronicle state.

## PTU boundary

PTU 1.05 can make Occult Education relevant to magical ancient ruins in some campaigns, but it also explicitly allows ancient ruins to be mundane. The chronology protocol therefore never maps `old site` to Occult Education automatically.

No chronology result grants XP, Edges, Features, Skills, Tutor Points, supernatural knowledge or automatic puzzle solutions.

If a future Caelo rule defines specific archaeological procedures, this protocol should store their authoritative outcomes rather than recreate them.

## Encounter handoff rule

Archaeological dating is normally world-state investigation. AutoPTU should receive a battle only when a separate conflict genuinely occurs.

A battle result can determine access, safety or custody under an existing contract. It cannot determine the age of a sample or select the correct historical interpretation.

## Canon gates

Before canonizing specific chronology content, decide which methods exist in Ouros, which institutions operate them, which reference chronologies exist, what calendar conventions are used, what sampling is permitted at sacred/restricted sites and how much numerical precision should be exposed to players.
