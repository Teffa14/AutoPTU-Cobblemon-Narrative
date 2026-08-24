# Institutional Succession, Vacancies & Handoffs Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon. No political or PTU rules are created here.
Date: 2026-08-24
Pass: 153

## Purpose

Ouros needs institutions to survive changes in personnel across years of Chronicle. This layer owns the transition between officeholders: vacancy, acting coverage, selection, assumption of office, transfer of authority, operational handoff and historical continuity.

It does not decide how every institution selects leaders. That procedure must be authored locally or supplied by an existing governing layer.

## Authority boundaries

Civic Governance owns the mandate and decision procedure of civic bodies.

Workplaces owns staffing, ordinary occupational roles, shifts and assignments.

Aging/Retirement owns an actor's retirement or reduction in participation.

Credentials owns licenses, permissions and access eligibility.

Institutional Review owns compliance findings, suspension/review and appeals where authored.

Battle Institutions owns Gym/League challenge contracts and formal battle consequences.

Archives/Public Memory owns historical/public records.

Identity owns actor names and aliases.

This layer owns the succession transaction connecting those states.

## Core separation

```text
institution
  -> institutional office
  -> officeholding term
  -> vacancy/absence state
  -> temporary delegation if authorized
  -> succession procedure
  -> candidate/nominee status
  -> selection outcome
  -> authority and operational handoff
  -> assumption of office
  -> public/record reconciliation
  -> preserved historical term
```

The office is not the actor. A title is not a Skill. Selection is not assumption. Acting authority is not permanent appointment. Mentorship is not entitlement.

## 1. INSTITUTIONAL_OFFICE

```yaml
institutional_office:
  office_id: null
  institution_id: null
  public_title: null
  office_domain: null
  mandate_ref: null
  authority_scope_refs: []
  required_credential_refs: []
  succession_procedure_ref: null
  acting_authority_policy_ref: null
  continuity_priority: normal
  current_term_id: null
  current_state: OCCUPIED
  historical_term_ids: []
  canon_status: proposed
```

Candidate `office_domain` values may include battle institution leadership, museum direction, research-station leadership, civic service coordination, transport operations, emergency command, guild/craft leadership or another authored institutional function.

The generator must not invent an office merely because an NPC is important.

## 2. OFFICEHOLDING_TERM

```yaml
officeholding_term:
  term_id: null
  office_id: null
  holder_actor_id: null
  term_kind: permanent|fixed_term|acting|interim|temporary|unknown
  started_at: null
  ended_at: null
  assumption_event_ref: null
  departure_event_ref: null
  authority_scope_refs: []
  credential_refs: []
  public_title_revision_ref: null
  predecessor_term_id: null
  successor_term_id: null
  status: ACTIVE
```

A holder may have multiple non-contiguous terms. A return therefore creates a new term, not a rewrite of the old one.

## 3. VACANCY_EVENT

```yaml
vacancy_event:
  vacancy_id: null
  office_id: null
  detected_at: null
  effective_from: null
  trigger_type: resignation|retirement|death_confirmed|suspension|credential_loss|absence|term_end|transfer|unknown
  trigger_ref: null
  expected_duration: null
  continuity_required: null
  public_reason_visibility: restricted
  status: ACTIVE
```

`death_confirmed` may only be used when the Memorials/identity authority has valid confirmation. Missing, unreachable or absent are not death.

A vacancy does not imply crisis. Some offices may remain safely empty.

## 4. ACTING_ASSIGNMENT

```yaml
acting_assignment:
  acting_assignment_id: null
  office_id: null
  actor_id: null
  start_time: null
  expected_end_time: null
  actual_end_time: null
  delegated_authority_refs: []
  excluded_authority_refs: []
  source_procedure_ref: null
  triggering_vacancy_ref: null
  credential_refs: []
  status: ACTIVE
```

An acting holder receives only the authority actually delegated.

Forbidden shortcut:

`acting = all powers of permanent holder`

## 5. SUCCESSION_PROCEDURE

The procedure is a referenceable, versioned local rule.

```yaml
succession_procedure:
  procedure_id: null
  office_id: null
  version: null
  valid_from: null
  valid_to: null
  initiation_conditions: []
  eligible_proposer_or_nominator_refs: []
  candidate_requirements: []
  selection_steps: []
  required_review_refs: []
  decision_authority_ref: null
  challenge_or_exam_ref: null
  assumption_conditions: []
  review_or_dispute_route_ref: null
  source_refs: []
```

The placeholders are intentional. Ouros must not assume election, hereditary transfer, combat challenge, board appointment, seniority or nomination as a universal rule.

## 6. SUCCESSION_CANDIDACY

```yaml
succession_candidacy:
  candidacy_id: null
  office_id: null
  actor_id: null
  status: considered|nominated|applied|invited|training|eligible|ineligible|withdrawn|selected|not_selected
  initiated_at: null
  basis_refs: []
  eligibility_refs: []
  training_or_shadowing_refs: []
  review_refs: []
  actor_acceptance_state: unknown
  public_visibility: restricted
```

Being considered is not appointment. Being trained is not a promise. Public speculation is not candidacy.

An actor may decline.

## 7. SELECTION_EVENT

```yaml
selection_event:
  selection_event_id: null
  office_id: null
  procedure_version_ref: null
  candidate_ids: []
  selected_actor_id: null
  decision_authority_ref: null
  authoritative_result_refs: []
  decided_at: null
  effective_assumption_time: null
  conditions_remaining: []
  public_notice_ref: null
  status: DECIDED
```

If a battle is part of an authored procedure, `authoritative_result_refs` may point to the AutoPTU battle result. The battle result is an input. It does not independently create the officeholding term.

## 8. AUTHORITY_HANDOFF

```yaml
authority_handoff:
  handoff_id: null
  office_id: null
  outgoing_actor_id: null
  incoming_actor_id: null
  effective_at: null
  authority_refs_transferred: []
  authority_refs_retained_temporarily: []
  authority_refs_not_transferred: []
  unresolved_authority_questions: []
  source_refs: []
  status: IN_PROGRESS
```

Authority transfer is different from operational knowledge transfer.

## 9. OPERATIONAL_HANDOFF_PACKAGE

```yaml
operational_handoff_package:
  handoff_package_id: null
  office_id: null
  from_actor_id: null
  to_actor_id: null
  active_project_refs: []
  scheduled_commitment_refs: []
  open_case_refs: []
  risk_or_warning_refs: []
  custody_transfer_refs: []
  credential_access_refs: []
  private_archive_refs: []
  contact_network_refs: []
  unwritten_knowledge_notes: []
  acknowledged_items: []
  missing_items: []
  completed_at: null
```

Missing information creates uncertainty. It does not prove sabotage, negligence or incompetence.

## 10. ACCESS AND CREDENTIAL RECONCILIATION

Appointment does not automatically update every downstream system.

Potential reconciliation targets:

- building access;
- digital accounts;
- signature/approval authority;
- custody permissions;
- challenge scheduling;
- public directory;
- emergency contact trees;
- payment authorization;
- restricted collection/research access.

Credentials/Digital Systems/Payments remain authoritative for those changes.

This layer stores the requested handoff and whether each downstream authority confirmed it.

## 11. PUBLIC_TRANSITION_NOTICE

```yaml
public_transition_notice:
  notice_id: null
  office_id: null
  old_holder_id: null
  new_or_acting_holder_id: null
  published_at: null
  claimed_effective_at: null
  source_channel_ref: null
  text_artifact_ref: null
  correction_refs: []
  public_status: current
```

Publication is informational state. It does not itself create authority.

An old sign, website or scoreboard can remain historically accurate for its publication date while being obsolete for current use.

## 12. CONTINUITY_REVIEW

```yaml
continuity_review:
  review_id: null
  office_id: null
  triggering_transition_refs: []
  services_maintained: []
  services_interrupted: []
  handoff_failures: []
  handoff_successes: []
  undocumented_dependencies: []
  proposed_process_changes: []
  adopted_change_refs: []
  reviewed_at: null
```

A successful transition can reduce future content. Institutions may learn enough that the next vacancy becomes routine.

## 13. Former holder state

Leaving office never deletes the actor.

Possible later relationships include advisor, emeritus title, occasional substitute, critic, private citizen, mentor, researcher, competitor or no continuing relationship at all.

None should be inferred automatically.

An `emeritus` or honorary title has no authority unless separately authored.

## 14. Battle institutions

Gym or battle-office succession uses the same institutional chain with extra battle-specific handoffs.

Possible records:

```yaml
battle_office_handoff:
  office_id: null
  challenge_contract_refs: []
  scheduled_challenge_refs: []
  public_team_information_refs: []
  venue_access_refs: []
  badge_or_qualification_authority_ref: null
  league_reporting_refs: []
```

The successor's actual Pokémon, Trainer Features, Skills and battle legality remain in authoritative PTU/AutoPTU state.

The office never grants combat statistics.

## 15. Player-founded institutions

A player-founded club, Gym-like venue, business, research group or community organization may eventually define a succession procedure if governing canon permits it.

Important boundaries:

- founding does not grant perpetual ownership of every institutional asset;
- leaving does not automatically transfer ownership to the successor;
- money, land, Pokémon, items and credentials require their own authoritative handoffs;
- a PC can decline a leadership role;
- the institution can persist after the PC leaves active play.

## 16. Emergency absence and delegation

Emergency delegation may temporarily keep essential functions operating.

It must record:

- triggering absence/vacancy;
- authority source;
- scope;
- exclusions;
- activation time;
- termination condition;
- notification state.

An emergency does not authorize arbitrary permanent institutional changes.

## 17. Disputed transitions

Competing claims can exist without immediately choosing canonical truth.

```yaml
succession_dispute:
  dispute_id: null
  office_id: null
  competing_claim_ids: []
  procedure_version_refs: []
  evidence_refs: []
  review_route_ref: null
  provisional_operational_state: null
  public_claim_refs: []
  canonical_resolution_state: UNRESOLVED
```

Institutional Review/Civic Governance owns the relevant decision route. Combat cannot settle the dispute unless the authored procedure explicitly makes a battle result relevant.

## 18. Chronicle compression

Routine transitions should compress.

Expose a succession in detail when it intersects:

- player relationships;
- a genuinely consequential vacancy;
- an unclear authority boundary;
- an incomplete handoff;
- a battle institution challenge schedule;
- an active crisis/project/case;
- a disputed procedure;
- a major long-term change in institutional identity.

Do not generate a quest merely because an office changed hands normally.

## 19. Minecraft projection

Minecraft may show:

- office/name plaques;
- portraits;
- new uniforms;
- a changed NPC at a desk;
- closed rooms during transition;
- ceremony decorations;
- updated noticeboards.

Minecraft is not authoritative for officeholding.

Changing a nameplate does not appoint someone. Killing/despawning an NPC does not create a vacancy event. Reloading a chunk cannot restore a former officeholder. Possessing a key item does not create authority.

## 20. Mechanical non-inferences

This layer never authorizes:

- office title -> Trainer Class;
- leadership role -> Command rank;
- succession -> level-up;
- acting status -> extra actions;
- public support -> morale bonus;
- former leader -> Mentor Feature;
- Gym office -> custom Orders;
- ceremonial item -> battle Item effect;
- inheritance -> Pokémon ownership;
- family relationship -> succession entitlement;
- battle victory -> office unless procedure says so;
- office vacancy -> faction hostility;
- failed handoff -> sabotage;
- new leader -> tactical AI improvement.

## 21. Inter-layer handoffs

Civic Governance -> procedure/decision authority.

Workplaces -> staffing and operational assignments.

Aging/Retirement -> departure decision.

Credentials -> eligibility/access changes.

Institutional Review -> contested/suspended officeholding.

Battle Institutions -> formal challenge authority and results.

Digital Systems -> accounts/access.

Payments/Finance -> spending/approval authority if canon supports it.

Land Tenure/Material Culture -> physical property/custody.

Pokémon Agency -> any Pokémon partnership/custody affected by a personal transition.

Archives/Public Memory -> historical and public versions.

## 22. Canon gate

Before promoting any office or procedure to canon, establish:

- institution identity;
- office purpose;
- mandate;
- current holder if any;
- who may initiate succession;
- how selection actually works;
- acting-authority policy;
- credential requirements;
- review/dispute route;
- which handoffs matter;
- what remains private;
- whether battle is relevant at all.

Until then, use PROPOSED or UNRESOLVED states.