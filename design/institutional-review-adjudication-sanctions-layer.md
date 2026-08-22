# Ouros Institutional Review, Adjudication, Sanctions & Appeals Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Ouros already separates incidents, evidence, custody, negotiation, credentials, competition results, finance and public memory. This layer adds a bounded institutional decision process for situations where an authored organization has authority to review a rule, standard, credential, event result, inspection or internal complaint.

It is not a universal court system.

It does not create criminal law, arrest powers, prisons, universal fines, universal property seizure, police procedure, citizenship law or a regional judiciary.

The layer exists so that a Gym inspection, Contest protest, tournament rules issue, access suspension, professional review or conservation-permit dispute can have persistent procedural history without reducing the result to `guilty = true` or `reputation -20`.

## 1. Core separation

Keep these states independent:

incident/evidence → what is known or alleged;

rule/version → what written or authored standard is being applied;

mandate → who is allowed to decide this bounded question;

review proceeding → what process actually occurred;

finding → what the reviewer concluded from the evidence;

rule interpretation → how the reviewer understood the standard;

decision → the institution's formal result;

remedy/sanction → what state change the decision orders;

compliance/enforcement → whether the ordered state change happened;

appeal/review → whether another authorized process revisited the decision;

world truth → what actually happened in the world.

No arrow above means equivalence.

## 2. Institutional review case

```yaml
institutional_review:
  review_id: null
  institution_id: null
  reviewing_body_id: null
  mandate_ref: null
  subject_actor_ids: []
  subject_institution_ids: []
  subject_activity_ids: []
  linked_case_ids: []
  linked_dispute_ids: []
  linked_credential_ids: []
  linked_event_ids: []
  rule_issue_ids: []
  evidence_package_ids: []
  participant_ids: []
  status: INTAKE
  opened_at: null
  closed_at: null
  confidentiality_state: scoped
  public_summary_id: null
  decision_id: null
  review_history_ids: []
  canon_status: proposed
```

Suggested states:

- INTAKE
- JURISDICTION_REVIEW
- EVIDENCE_GATHERING
- NOTICE_PENDING
- RESPONSE_WINDOW
- HEARING_OR_REVIEW
- DECISION_PENDING
- DECIDED
- REVIEW_REQUESTED
- UNDER_REVIEW
- REMANDED
- CLOSED
- CLOSED_NO_MANDATE
- CLOSED_NO_ACTION

A review can close because the institution lacks authority. That is a valid outcome.

## 3. Rule issue

A proceeding must identify the exact standard being considered.

```yaml
rule_issue:
  rule_issue_id: null
  review_id: null
  rule_ref: null
  rule_version: null
  effective_from: null
  effective_until: null
  allegation_or_question: null
  scope: null
  initiating_claim_ids: []
  disputed_interpretation_ids: []
  retroactivity_allowed: false
  source_refs: []
```

Candidate scopes:

- EVENT_CONDUCT
- COMPETITION_ELIGIBILITY
- RESULT_VALIDITY
- GYM_OR_INSTITUTION_STANDARD
- CREDENTIAL_STANDARD
- ACCESS_OR_PERMIT_CONDITION
- PROFESSIONAL_OR_STAFF_STANDARD
- GRANT_OR_FUNDING_CONDITION
- SAFETY_OR_OPERATIONAL_STANDARD
- INTERNAL_GOVERNANCE_RULE
- OTHER_AUTHORED_STANDARD

A current rule must not be silently applied to an old event if it was not in force then.

## 4. Jurisdiction and mandate check

Before evidence is weighed, the system verifies whether the reviewing body can decide this question.

```yaml
review_mandate_check:
  mandate_check_id: null
  review_id: null
  institution_id: null
  mandate_ref: null
  geographic_scope_refs: []
  activity_scope_refs: []
  actor_scope_refs: []
  rule_scope_refs: []
  temporal_scope_refs: []
  result: PENDING
  reasons: []
  decided_by_id: null
  decided_at: null
```

Possible results:

- VALID
- INVALID
- PARTIAL
- TRANSFER_REQUIRED
- CONFLICTED
- UNRESOLVED

No institution receives authority because the generator needs a dramatic hearing.

## 5. Notice and participation

A review should preserve who knew what process was happening and what opportunity they actually had to respond.

```yaml
review_notice:
  notice_id: null
  review_id: null
  recipient_ids: []
  issued_at: null
  delivered_at: null
  delivery_packet_id: null
  issues_identified: []
  evidence_disclosure_refs: []
  response_deadline: null
  attendance_requirement: null
  confidentiality_terms: []
  acknowledgement_ids: []
```

A sent notice is not a received notice. Communications owns delivery state.

Missing notice does not automatically void a decision unless the authored process says it does.

## 6. Evidence package

Case evidence remains under the Case layer. This layer stores what evidence the reviewer actually considered.

```yaml
review_evidence_package:
  package_id: null
  review_id: null
  evidence_refs: []
  excluded_evidence_refs: []
  exclusion_reasons: []
  expert_or_technical_refs: []
  battle_transcript_refs: []
  public_record_refs: []
  submitted_by_ids: []
  frozen_at: null
  superseded_by: null
```

A later appeal can have a different package.

A battle transcript can prove battle events within its implemented authority. It cannot prove motive, institutional intent or off-grid conduct.

## 7. Reviewer and conflict records

```yaml
reviewer_assignment:
  assignment_id: null
  review_id: null
  reviewer_id: null
  role: null
  mandate_ref: null
  conflict_disclosure_ids: []
  recusal_state: NONE
  assignment_started_at: null
  assignment_ended_at: null
```

Possible roles:

- INSPECTOR
- JUDGE
- PANEL_MEMBER
- TECHNICAL_REVIEWER
- MEDICAL_REVIEWER
- RULES_REVIEWER
- ADMINISTRATIVE_REVIEWER
- COMMUNITY_REPRESENTATIVE
- OBSERVER

Roles are institutional labels, not PTU Trainer Classes.

A conflict disclosure does not prove corruption. It can produce recusal, limited participation or no change according to the authored process.

## 8. Hearing / review session

```yaml
review_session:
  session_id: null
  review_id: null
  session_type: null
  participant_ids: []
  reviewer_ids: []
  location_id: null
  started_at: null
  ended_at: null
  evidence_presented_refs: []
  statements_submitted_refs: []
  questions_recorded_refs: []
  procedural_ruling_ids: []
  unresolved_items: []
  transcript_access_state: restricted
```

Candidate types:

- DOCUMENT_REVIEW
- INSPECTION
- TECHNICAL_REVIEW
- FORMAL_HEARING
- COMPETITION_PROTEST
- CREDENTIAL_REVIEW
- RESULT_REVIEW
- EMERGENCY_INTERIM_REVIEW

Not every review needs a courtroom scene.

Most ordinary matters should compress to records unless a meaningful player decision exists.

## 9. Findings

Findings stay granular.

```yaml
institutional_finding:
  finding_id: null
  review_id: null
  proposition: null
  evidence_refs: []
  counterevidence_refs: []
  finding_state: UNRESOLVED
  confidence_note: null
  scope_note: null
  decided_by_ids: []
  decided_at: null
```

Suggested states:

- CONFIRMED
- NOT_ESTABLISHED
- UNRESOLVED
- OUTSIDE_SCOPE
- ADMITTED
- STIPULATED
- PROCEDURALLY_UNUSABLE
- SUPERSEDED

`NOT_ESTABLISHED` is not the same as `FALSE`.

`CONFIRMED` is the institution's finding, not an automatic rewrite of Chronicle world truth.

## 10. Rule interpretation

```yaml
rule_interpretation:
  interpretation_id: null
  review_id: null
  rule_ref: null
  rule_version: null
  question: null
  interpretation_summary: null
  reasoning_refs: []
  precedent_refs: []
  dissent_refs: []
  effective_scope: null
  superseded_by: null
```

This object allows two honest institutions or reviewers to disagree about what an authored rule means.

A later clarification can supersede interpretation without erasing earlier decisions.

## 11. Institutional decision

```yaml
institutional_decision:
  decision_id: null
  review_id: null
  issued_by_ids: []
  issued_at: null
  rule_issue_ids: []
  finding_ids: []
  interpretation_ids: []
  disposition: null
  remedy_order_ids: []
  effective_from: null
  effective_until: null
  review_route_refs: []
  public_summary_id: null
  private_reasoning_refs: []
  status: ACTIVE
```

Candidate dispositions:

- NO_ACTION
- REQUIRE_CORRECTION
- UPHOLD_RESULT
- AMEND_RESULT
- INVALIDATE_RESULT
- REQUIRE_REINSPECTION
- CONDITIONALLY_APPROVE
- DENY_APPROVAL
- SUSPEND_SCOPE
- REVOKE_SCOPE
- RESTORE_SCOPE
- REMAND_FOR_NEW_REVIEW
- REFER_TO_OTHER_INSTITUTION

No generic `GUILTY` disposition is required.

## 12. Remedy / sanction order

A consequence should identify which other system owns the state change.

```yaml
remedy_order:
  remedy_order_id: null
  decision_id: null
  target_ids: []
  remedy_type: null
  owner_system: null
  effective_from: null
  expires_at: null
  conditions: []
  verification_refs: []
  status: PENDING
  applied_event_id: null
```

Candidate types:

- WARNING_RECORD
- CORRECTIVE_ACTION
- REINSPECTION
- RESULT_CHANGE
- EVENT_DISQUALIFICATION
- ACTIVITY_SUSPENSION
- CREDENTIAL_REVIEW
- ACCESS_RESTRICTION
- FUNDING_REVIEW
- RESTITUTION_OR_REPAIR
- TRAINING_OR_SUPERVISION_REQUIREMENT
- REINSTATEMENT
- PUBLIC_CORRECTION

The owner system performs the actual state change.

Examples:

- Credentials owns credential suspension/restoration.
- Battle Institutions owns qualification/standings state.
- Contests owns formal Contest results.
- Finance owns grant/funding state.
- Agreements owns a voluntary repair agreement.
- Public Memory/Media owns published summaries and corrections.

This layer records why the order exists.

## 13. Interim measures

Some authored institutions may need temporary state while review is pending.

```yaml
interim_measure:
  measure_id: null
  review_id: null
  ordered_by_id: null
  authority_ref: null
  measure_type: null
  target_ids: []
  reason_refs: []
  started_at: null
  expires_at: null
  review_required_at: null
  status: ACTIVE
```

Examples could include temporary access restriction or event pause.

Interim action is not a final finding.

## 14. Review, appeal and rehearing

```yaml
review_request:
  request_id: null
  challenged_decision_id: null
  requested_by_ids: []
  requested_at: null
  allowed_route_ref: null
  grounds: []
  new_evidence_refs: []
  rule_interpretation_challenges: []
  procedural_challenges: []
  remedy_challenges: []
  status: PENDING
```

Possible grounds:

- NEW_EVIDENCE
- WRONG_RULE_VERSION
- RULE_INTERPRETATION
- PROCEDURAL_ERROR
- CONFLICT_OF_INTEREST
- REMEDY_SCOPE
- MISTAKEN_IDENTITY
- IMPLEMENTATION_ERROR
- OTHER_AUTHORED_GROUND

```yaml
review_outcome:
  review_outcome_id: null
  request_id: null
  reviewing_body_id: null
  outcome: null
  replacement_decision_id: null
  reasoning_refs: []
  issued_at: null
```

Candidate outcomes:

- DENIED
- AFFIRMED
- AMENDED
- OVERTURNED
- REMANDED
- MOOT
- OUTSIDE_SCOPE

Old decisions remain in Chronicle.

## 15. Reinstatement and restoration

A sanction ending does not delete that it occurred.

```yaml
reinstatement_event:
  reinstatement_id: null
  source_decision_id: null
  target_id: null
  restored_scope_refs: []
  effective_at: null
  conditions_satisfied_refs: []
  credential_or_permission_refs: []
  public_correction_refs: []
```

Restoration should be explicit so the world does not leave a character permanently blocked after a decision expires or is overturned.

## 16. Rules can themselves become the dispute

If participants disagree about whether the rule should exist, the problem may move to Civic Governance, Battle Institution governance, Contest governance, club governance or another authored rule-making process.

This layer can record:

`rule applied correctly`

while a separate process records:

`community wants the rule changed`.

Do not make every unpopular outcome evidence that the reviewer acted improperly.

## 17. Public knowledge and privacy

A decision can have multiple information layers:

- private evidence package;
- participant-access decision;
- internal reasoning;
- public disposition;
- redacted public summary;
- rumor/public memory.

Media can report a decision incorrectly without changing the decision record.

A public sanction does not authorize release of private medical, family, mental, research or custody information.

## 18. Multiplayer player-agency rules

The system may impose authored world consequences on a PC only when the institution has a valid mandate and the triggering facts/rules support them.

The system must not use social mechanics to force a PC to:

- confess;
- agree with a finding;
- feel remorse;
- forgive;
- reveal private memories;
- waive review;
- change ideology;
- become loyal to an institution;
- accept a voluntary settlement.

A player can choose to ignore an institutional order. The world may then respond through authored access, eligibility, reputation or institutional state. The engine still must not rewrite the player's internal beliefs.

## 19. Pokémon agency

A Pokémon must not become a procedural object merely because it belongs to a Trainer.

Possible institutional subjects include:

- a Trainer's conduct;
- an institution's treatment of Pokémon;
- custody/ownership claims where canon supports them;
- a Pokémon's eligibility for an event under authored rules;
- welfare/safety evidence.

A reviewer cannot infer a Pokémon's consent, fear, loyalty or wishes from ownership alone.

Psychic powers, Telepathy, Thought Detection or similar mechanics cannot become universal truth machines. Exact PTU/Caelo mechanics, privacy boundaries and Java implementation must be verified first.

## 20. Cross-layer contracts

### Case / Authority / Custody

Provides incident reports, evidence, claims, witnesses, custody and mandate references.

This layer never silently modifies evidence.

### Agreements / Mediation / Repair

A voluntary agreement can resolve or narrow a dispute before/after review.

A decision is not an agreement merely because all parties comply.

### Credentials / Permissions / Eligibility

Owns credential/permission state after a valid remedy order.

### Battle Institutions

Owns Gym/circuit records, standings, qualification and challenge history.

This layer may review institutional standards or protested results when the institution has authored review rules.

### Contest / Performance

Owns formal Contest outcomes and career records. This layer can order a result review or disqualification only where Contest rules authorize it.

### Finance / Grants

Owns balances, grants and sponsorship state. This layer can issue a review outcome; it does not move money directly.

### Conservation / Protected Areas

Owns visitor/stewardship policy. This layer can review a permit or alleged violation only under an authored mandate.

### Workplaces / Education / Clubs

May have their own bounded internal standards. Do not infer universal employment, school or club discipline procedures.

### Public Memory / Media / Archives

Preserve decisions, corrections and historical context. Publication does not create institutional validity.

## 21. PTU / AutoPTU authority boundary

AutoPTU-Java is battle authority, not adjudication authority.

A battle may produce authoritative evidence such as:

- participants;
- ordered semantic events within implemented coverage;
- result;
- damage/status state within implemented coverage;
- resource use where implemented.

The institutional layer must not ask Minecraft to reinterpret that transcript.

The battle result alone never proves:

- cheating;
- intent;
- unsafe institutional practice;
- credential fraud;
- breach of a non-battle rule;
- proportional sanction.

## 22. Permanent capability dependencies

Most institutional review is overworld/world-state logic and does not require the battle engine.

Mechanically rich scenes may depend on:

`targeting / footprints / range / LoS`
Verified foundation for ordinary static combat.

`base movement legality`
Verified foundation for ordinary static movement.

`complete movement including push / pull / knockback / interception / forced movement`
Required for live escort, extraction, protected corridors, pursuit during a hearing disruption or moving-crowd evacuation.

`core calculations`
Verified for ordinary battle calculations. No adjudication score is created.

`action economy / initiative`
Verified for ordinary combat order. A reviewer does not gain initiative priority from authority.

`full turn / round lifecycle`
Partial. Required only if a mechanically timed battle effect depends on unverified lifecycle behavior.

`full stateful damage pipeline`
Partial. Required for exact combat consequences, never for institutional punishment.

`status lifecycle`
Partial. No review outcome creates a Status.

`terrain / weather / hazards / zones / reactions`
Blocking as a complete family. Required for dynamic protected zones, hazards or reactions in a disrupted venue.

`move-specific behavior`
Partial; exact Move only.

`abilities`
Partial; exact Ability only.

`items`
Partial; exact mechanical item only.

`Trainer Features / perks`
Partial. Generic prerequisite/context/frequency infrastructure exists, but no social/institutional Feature should be assumed implemented.

`AI legal-action infrastructure`
Verified for ordinary legal choices.

`AI tactical policy`
Blocking for goals such as PROTECT_REVIEWER, WITHDRAW, PRESERVE_EVIDENCE, AVOID_CIVILIANS or CLEAR_EXIT.

`Minecraft / Cobblemon / Craftics adapter and playback`
Blocking for authoritative world-to-battle projection and semantic playback.

## 23. Encounter contracts

### Inspection Day Interruption

Premise:

A battle institution is undergoing a scheduled inspection. During the inspection, an unrelated disturbance threatens staff and visitors. The inspection must later distinguish what the institution did before the disturbance from emergency improvisation during it.

FULL version:

- civilians evacuate dynamically;
- staff protect exits/evidence;
- combatants may withdraw or clear corridors;
- post-battle review consumes the authoritative transcript plus inspection observations.

Dependencies:

- targeting/range/LoS — VERIFIED;
- base movement — VERIFIED;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- AI legal-action infrastructure — VERIFIED;
- complete movement/interception/forced movement — BLOCKING;
- terrain/hazards/zones/reactions — BLOCKING if venue hazards exist;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED version:

Evacuate civilians in world state first. Freeze a safe inspection arena. Run a conventional static encounter. Afterward, the review separately records pre-incident inspection evidence, emergency actions and battle transcript. The disturbance does not automatically excuse or condemn the institution.

### Protested Exhibition Result

Premise:

A public exhibition ends normally, but a participant later challenges whether an equipment/roster/eligibility rule was followed.

FULL version:

No special battle mechanics are required if the underlying match was already resolved. The content lives in evidence, rule-version review and institutional consequence.

Dependencies:

- existing battle transcript coverage as evidence — PARTIAL according to exact subsystem used;
- Trainer Features/items/moves/abilities only if the disputed rule depends on their exact implementation;
- adapter/playback only for reliable replay/presentation, not for the decision itself.

REDUCED version:

Review the recorded roster, rule version, authoritative result and available evidence. Possible outcomes include uphold, amend, invalidate, no action or re-run only if the authored event rules allow it. Never re-simulate a match merely to get a preferred result.

### Credential Review Under Evacuation

Premise:

A field specialist's credential is already under scheduled review when a crisis interrupts the proceeding. The specialist may still be the best-qualified person available to assist during the emergency.

FULL version:

A dynamic rescue could include protected routes and objective-aware actors.

Dependencies:

- complete movement — BLOCKING;
- environment family if hazard mechanics are required — BLOCKING;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED version:

The review enters `SUSPENDED_FOR_EMERGENCY` world state. Any temporary emergency permission is granted explicitly by Credentials/Authority. Rescue state is resolved outside the grid or through static conventional battles. The later review resumes without treating emergency usefulness as automatic proof that every credential requirement was satisfied.

## 24. Mechanical and narrative no-inference rules

Never generate automatically:

- criminal guilt;
- arrest power;
- prison sentence;
- universal fines;
- property seizure;
- forced confession;
- psychic truth verification;
- lie-detection DCs;
- testimony bonuses;
- judge bonuses;
- hearing initiative;
- sanction damage;
- credential suspension from a battle loss;
- disqualification from ordinary Fainted/Injury;
- institutional corruption because a decision is unpopular;
- intent from outcome;
- guilt from refusal to speak;
- guilt from requesting review;
- innocence from missing evidence;
- automatic escalation from prior unrelated penalties.

## 25. Canon questions intentionally unresolved

- Which Ouros institutions have formal inspection or review powers?
- Does the League maintain an inspection body, or do regions use different arrangements?
- Which competitions have protest/review procedures?
- Can clubs, schools, research institutes or conservation bodies suspend their own permissions?
- Which decisions can be reviewed by another body?
- Are any review sessions public?
- What information must remain private?
- What remedies exist beyond correction, access changes, result changes and reinspection?
- Does Ouros have any broader civil/criminal justice system at all?
- What rules govern restitution or damaged property?
- What PTU/Caelo Skills or Features can assist fact-finding without overriding player agency?
- What exact mechanics, if any, govern surrender, testimony, restraint or institutional authority?

Until authored, these remain unresolved.
