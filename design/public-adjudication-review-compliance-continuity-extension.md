# Ouros Adjudication, Review & Compliance Continuity Extension

Status: PROPOSED. Not established canon.
Date: 2026-08-29

## Purpose

This extension preserves the procedural history of a contested matter after an authored institution receives authority to decide it. It stores notice, scope, record manifests, findings, decision versions, review requests, remand or rehearing, implementation and later compliance.

It does not define Ouros institutions or universal procedure. Every deciding body, mandate, available outcome and review route must come from canon.

## Existing-system boundaries

Case & Authority owns incident intake, investigation, evidence, hypotheses, custody and case handoffs.

Agreements & Mediation owns voluntary negotiation, commitments, truces and repair plans.

Civic Governance owns proposals about future collective public state and public consultation.

Media, Public Notices, Public Memory and Archives own publication, circulation, remembered interpretation and long-term record access.

This layer owns only the continuity of an authored deciding process. No object grants its own authority.

## Required separations

COMPLAINT_FILED != FACT_PROVEN
NOTICE_SENT != NOTICE_RECEIVED
HEARING_SCHEDULED != HEARING_HELD
EVIDENCE_SUBMITTED != EVIDENCE_CONSIDERED
FINDING_RECORDED != WORLD_TRUTH_CREATED
DECISION_ISSUED != IMPLEMENTATION_COMPLETE
REVIEW_REQUESTED != REVIEW_GRANTED
REVIEW_GRANTED != ORIGINAL_RECORD_ERASED
REMAND != FINAL_RESOLUTION
CONDITION_PERFORMED != CONDITION_VERIFIED
COMPLIANCE_VERIFIED != FORGIVENESS
MATTER_CLOSED != EVERY_HISTORICAL_QUESTION_ANSWERED

## Matter state

```yaml
adjudication_matter:
  matter_id: null
  source_case_ids: []
  source_dispute_ids: []
  deciding_body_id: null
  mandate_ref: null
  subject_refs: []
  party_ids: []
  affected_actor_ids: []
  matter_scope: null
  requested_outcomes: []
  available_outcome_refs: []
  current_proceeding_id: null
  current_decision_id: null
  status: INTAKE
  canon_reference_ids: []
```

Candidate status vocabulary:
INTAKE, NOTICE_PENDING, RECORD_BUILDING, HEARING_PENDING, UNDER_DECISION, DECIDED, REVIEW_WINDOW, UNDER_REVIEW, REMANDED, IMPLEMENTING, COMPLIANCE_REVIEW, CLOSED, CLOSED_WITH_UNRESOLVED_QUESTIONS.

`available_outcome_refs` must always be authored by canon.

## Proceeding and scope

```yaml
adjudication_proceeding:
  proceeding_id: null
  matter_id: null
  proceeding_type_ref: null
  deciding_body_id: null
  decider_actor_ids: []
  mandate_ref: null
  scope_questions: []
  issues_explicitly_out_of_scope: []
  opened_at: null
  closed_at: null
  record_manifest_id: null
  session_ids: []
  decision_id: null
  privacy_state: authored
  status: OPEN
```

A later review may address only one issue from the earlier proceeding. Scope is explicit and versioned.

## Notice continuity

```yaml
adjudication_notice:
  notice_id: null
  proceeding_id: null
  notice_type_ref: null
  issued_by_id: null
  intended_recipient_ids: []
  issued_at: null
  delivery_route_id: null
  delivery_event_id: null
  receipt_state: UNKNOWN
  public_copy_id: null
  correction_ids: []
```

Candidate receipt states: UNKNOWN, SENT, DELIVERED, RECEIPT_ACKNOWLEDGED, DELIVERY_FAILED, RETURNED, SUPERSEDED.

A posted Minecraft notice can be stale while the authoritative server record has already changed.

## Record manifest

```yaml
review_record_manifest:
  manifest_id: null
  proceeding_id: null
  created_at: null
  evidence_refs: []
  testimony_record_refs: []
  prior_decision_refs: []
  public_record_refs: []
  admitted_later_material_refs: []
  excluded_from_scope_refs: []
  completeness_claim_id: null
  revision_ids: []
```

The manifest answers what information was actually before the deciding body at that time. New evidence discovered later does not silently enter an old manifest.

## Session record

```yaml
adjudication_session:
  session_id: null
  proceeding_id: null
  location_id: null
  started_at: null
  ended_at: null
  participant_ids: []
  support_ids: []
  testimony_record_ids: []
  evidence_considered_ids: []
  procedural_requests: []
  unresolved_questions: []
  session_outcome: null
```

A region may use a council room, League panel, guild board, research authority, stewardship body or another canon-authored venue. The generic layer does not require a courtroom format.

## Findings and decision lineage

```yaml
adjudication_finding:
  finding_id: null
  proceeding_id: null
  subject_question: null
  conclusion_claim_id: null
  evidence_refs: []
  contrary_evidence_refs: []
  uncertainty_notes: []
  finding_scope: null
  status: ACTIVE
  preserved_on_review: null
```

Candidate later states: ACTIVE, PRESERVED, MODIFIED, VACATED, SUPERSEDED, UNRESOLVED_AFTER_REVIEW.

```yaml
adjudication_decision:
  decision_id: null
  proceeding_id: null
  issued_at: null
  deciding_body_id: null
  finding_ids: []
  outcome_refs: []
  condition_ids: []
  implementation_owner_ids: []
  effective_state: null
  review_route_ref: null
  public_summary_id: null
  parent_decision_id: null
  status: ISSUED
```

An institutional finding remains separate from hidden world truth and raw evidence.

## Review request and review edge

```yaml
adjudication_review_request:
  review_request_id: null
  decision_id: null
  requested_by_ids: []
  submitted_at: null
  authored_route_ref: null
  stated_review_questions: []
  new_evidence_refs: []
  request_status: PENDING
  resulting_proceeding_id: null
```

Candidate request states: PENDING, ACCEPTED, DENIED, WITHDRAWN, OUT_OF_SCOPE, SUPERSEDED.

```yaml
decision_review_edge:
  edge_id: null
  from_decision_id: null
  review_proceeding_id: null
  to_decision_id: null
  relation: null
  preserved_finding_ids: []
  vacated_finding_ids: []
  remanded_question_ids: []
  created_at: null
```

Candidate relation vocabulary: AFFIRMED, MODIFIED, VACATED, PARTIALLY_VACATED, REMANDED_FOR_MORE_FACTS, REHEARING_REQUIRED, REPLACED_AFTER_REHEARING.

These labels describe lineage. They do not create a universal Ouros procedure.

## Remand continuity

```yaml
remand_instruction:
  remand_id: null
  source_review_proceeding_id: null
  destination_body_id: null
  questions_to_reconsider: []
  preserved_finding_ids: []
  vacated_finding_ids: []
  additional_record_needs: []
  created_proceeding_id: null
  status: PENDING
```

A remand creates unfinished work. It does not rewind the world or delete the earlier chronology.

## Implementation and compliance

```yaml
adjudication_condition:
  condition_id: null
  decision_id: null
  responsible_actor_or_institution_ids: []
  required_state_or_action_ref: null
  dependency_refs: []
  due_or_review_trigger: null
  verification_route_refs: []
  status: PENDING
```

Candidate states: PENDING, READY, IN_PROGRESS, PERFORMANCE_REPORTED, VERIFIED_COMPLETE, VERIFIED_PARTIAL, BLOCKED_BY_DEPENDENCY, CONTESTED, SUPERSEDED, ENDED.

```yaml
adjudication_compliance_event:
  compliance_event_id: null
  condition_id: null
  observed_at: null
  actor_ids: []
  event_type: null
  evidence_refs: []
  interpretation_claim_ids: []
```

Performance, verification and closure remain separate events.

## Pokémon participation boundary

A Pokémon may be an affected individual, source of an observation, accused actor, protected actor or participant when a valid communication route exists.

Never infer species-wide truth detection, responsibility, comprehension of formal conditions or consent. Aura, telepathy, scent, foresight or similar capabilities can influence fact-finding only when exact PTU/Caelo evidence and character state support the route.

Battle victory never proves an allegation or completes a decision process.

## Narrative structures

Five Dates on One Decision: hearing date, issue date, delivery date, effective date and implementation date all exist. Different NPCs use different dates when saying the matter was decided.

The Finding That Survived: a review changes one part of a decision but preserves another finding. Public rumor incorrectly says the whole record vanished.

The Record Was Complete Yesterday: a newly authenticated record appears later. The earlier manifest was complete for its time, and the new evidence becomes a review trigger.

A Town Learns What Review Changes: an ordinary local decision resolves one question, later evidence produces a scoped review, some findings survive, one issue returns for new fact-finding, and temporary arrangements become part of community history before a later decision changes one obligation.

## Encounter contract — Record Transfer Diversion

Premise: an authenticated record package must reach an authored reviewing body while an unrelated incident blocks the route.

Full dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL for escort/interception
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL if departure windows matter
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if protected corridors or reaction zones are used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for PROTECT/WITHDRAW/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING for semantic escort/handoff playback

Reduced version: complete custody transfer in world state before BattleSpec creation. Keep the package and custodian outside combat. Run a conventional static encounter at the chokepoint. Victory restores immediate access only.

## Encounter contract — Hearing Hall Evacuation

Full version may require withdrawal, Intercept, timed departure, protected boundaries, generalized reactions, objective-aware AI and semantic playback.

Reduced version: adjourn the session first, move participants and records to authored safe state, then resolve a static exterior battle. The proceeding remains adjourned until its owner reschedules it.

## Encounter contract — Compliance Site Perimeter

Full version may require protecting workers or a controlled handoff with non-defeat objectives.

Reduced version: pause the compliance action, move workers and controlled objects outside BattleSpec, resolve a conventional battle, then let the owner system determine whether work resumes and whether later verification succeeds.

## PTU/Caelo boundary

The continuity model itself needs no new combat mechanic.

Remain UNKNOWN without exact governing evidence: generic restraint procedures, detention timelines, formal testimony checks, lie detection, species-derived truth detection, universal social Skill thresholds for hearings, universal review procedures, adjudicative authority granted by Trainer Features, or Moves/Abilities/Items that automatically prove or disprove testimony.

PTU social Skills may apply only where the actual rule permits the check. A roll cannot create institutional mandate, world truth or player consent.

## Minecraft/Cobblemon boundary

Minecraft can render meeting halls, notice boards, archives, waiting areas, courier routes, public summaries and changed access after a decision. These are playback and presentation.

The adapter never decides authority, record scope, findings, review acceptance, compliance verification or closure. Cobblemon BattleState does not own adjudication state.

## Promotion rule

A proposal using this layer may become canon only after review confirms that the deciding institution exists, its mandate covers the exact matter, available outcomes and any review route are authored, privacy and notice assumptions are supported, no real-world procedure was silently imported, Pokémon capability claims are governed, and every tactical scene stays within verified engine capability or uses its reduced form.
