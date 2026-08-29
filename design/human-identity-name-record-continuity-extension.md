# Ouros Human Identity, Name & Record Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Ouros already has persistent actors, cover identities, credentials, private records, family and household relationships, residence, interregional recognition, case authority and Pokémon identity. Those systems repeatedly need to answer a narrower question: when several records use different names, spellings, identifiers or historical values, which records refer to the same human actor and what is safe to disclose?

This extension provides neutral continuity for human actor identity. It does not create a universal civil registry, passport system, citizenship model, legal-name regime, Trainer-license system, biometric infrastructure or document-verification rules.

The design principle is simple: the simulation may know that two records belong to one actor while individual institutions and NPCs know only what their evidence and permissions support.

## Authority boundary

`actor_id` is an internal Ouros continuity key. It is not automatically an in-world number.

Infiltration owns cover identities, deceptive presentations, suspicion and covert-access consequences.

Credentials owns licenses, permits, certificates, badges, role authorizations and recognition of those instruments.

Personal Records owns letters, diaries, correspondence, oral histories and private documentary material.

Archives/Museums owns archival custody, accession and access to holdings.

Family/Kinship owns family relationships. Household and Residential systems own household/residence state.

Interregional Mobility owns host/home context and cross-region recognition. Arrival Inspection may consume identity references for a scoped check only where a mandate already exists.

Case Authority owns allegations, investigative findings and evidence custody when a case exists.

Education, Care, Employment, Library, Transport and other service owners own their own local records and access decisions.

Pokémon Agency owns persistent Pokémon identity, custody, registration claims, Original/active Trainer relationships and partnership history.

This extension owns only the continuity graph linking human actor identity references, names, locally issued identifiers, record versions and scoped verification evidence.

## 1. Persistent human actor identity

```yaml
human_identity_record:
  actor_id: null
  identity_record_id: null
  current_public_name_ref: null
  current_private_or_authoritative_name_refs: []
  historical_name_refs: []
  contextual_name_refs: []
  institutional_identifier_refs: []
  record_linkage_claim_refs: []
  correction_event_refs: []
  verification_episode_refs: []
  privacy_profile_ref: null
  provenance_refs: []
  canon_status: proposed
```

`actor_id` persists even when every visible name changes.

Hard rules:

`DISPLAY_NAME_CHANGED != ACTOR_CHANGED`

`SAME_NAME != SAME_ACTOR`

`DIFFERENT_NAME != DIFFERENT_ACTOR`

`INTERNAL_ACTOR_ID != PUBLIC_IDENTIFIER`

The generator must never print or expose `actor_id` as if characters can see it unless canon explicitly maps it to an in-world identifier.

## 2. Name record

```yaml
human_name_record:
  name_ref: null
  actor_id: null
  rendered_name: null
  component_refs: []
  script_or_language_ref: null
  name_context: public|private|professional|artistic|academic|family|local|historical|institutional|other
  use_state: CURRENT|FORMER|CONTEXTUAL|DISPUTED|UNKNOWN
  effective_from: null
  effective_until: null
  source_refs: []
  visibility: private_or_authored
  supersedes_ref: null
  notes_ref: null
```

`name_context` describes where a form is used. It does not make that form legal, false or more authentic than another.

Potentially legitimate variations include shortened forms, titles, transliterations, spelling differences, professional names, stage names, pen names and former names. None exist in a specific Ouros culture until authored.

## 3. Name history is append-only

When a current name changes, preserve prior records.

A Chronicle event created in year 3 under Name A stays historically correct even if the actor uses Name B in year 8.

Rendering rules may choose to show:

- the historical name as recorded at the event;
- the current name with a historical-note indicator;
- a privacy-safe generic label;
- both forms when the viewing actor has permission and the story requires it.

The underlying event is never silently rewritten.

`CURRENT_NAME != NAME_USED_AT_EVENT_TIME`

`NAME_UPDATED != OLD_RECORD_FALSE`

## 4. Institutional identifiers remain scoped

```yaml
institutional_person_identifier:
  identifier_ref: null
  actor_id: null
  issuer_institution_id: null
  identifier_kind: null
  identifier_value_ref: protected
  issued_at: null
  active_from: null
  active_until: null
  status: ACTIVE|SUPERSEDED|REVOKED|ARCHIVED|UNKNOWN
  allowed_use_scope_refs: []
  visibility: protected
  provenance_refs: []
```

The narrative generator may only instantiate an identifier kind that canon or an existing system already establishes.

A school number, clinic number, library membership number, tournament registration number or local Trainer record could all exist independently if authored.

`IDENTIFIER_UNIQUE_WITHIN_ISSUER != UNIVERSALLY_UNIQUE`

`IDENTIFIER_MATCH != WHOLE_IDENTITY_PROVEN`

`CREDENTIAL_NUMBER != CIVIL_IDENTITY_NUMBER`

## 5. Identity attribute claim

Some records assert attributes about a person without becoming identity authorities.

```yaml
identity_attribute_claim:
  claim_id: null
  subject_actor_id: null
  attribute_kind: null
  asserted_value_ref: null
  asserting_source_ref: null
  observed_or_effective_time: null
  confidence_or_status: UNKNOWN
  visibility: private_or_authored
  superseded_by_ref: null
```

Examples may include a historical spelling, an institutional name form or a reported former address when another layer owns the underlying fact.

The extension must reference authoritative owner state rather than duplicate it.

Residence belongs to Residential. Employment belongs to Workplaces. Family belongs to Family/Kinship. Credential status belongs to Credentials.

## 6. Record-linkage claim

```yaml
identity_record_linkage_claim:
  linkage_id: null
  candidate_record_refs: []
  proposed_actor_id: null
  linkage_state: UNREVIEWED|SUPPORTED|VERIFIED_FOR_SCOPE|DISPUTED|REJECTED|UNRESOLVED
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  matching_attributes_used: []
  matching_rule_ref: null
  reviewed_by_refs: []
  reviewed_at: null
  scope_ref: null
  visibility: protected
  superseded_by_ref: null
```

A linkage answers whether records refer to the same actor within a stated scope. It does not automatically validate every claim inside those records.

`RECORDS_LINKED != ALL_FIELDS_CORRECT`

`RECORDS_LINKED != RECORDS_PUBLIC`

`ONE_LINKAGE_VERIFIED != EVERY_INSTITUTION_ACCEPTS_LINKAGE`

A linkage can remain unresolved without blocking unrelated services that do not need the disputed attribute.

## 7. Homonym collision

```yaml
homonym_collision:
  collision_id: null
  rendered_name_ref: null
  candidate_actor_ids: []
  affected_record_refs: []
  first_detected_at: null
  resolution_state: OPEN|PARTIALLY_RESOLVED|RESOLVED|ACCEPTED_AMBIGUITY
  disambiguating_evidence_refs: []
  owner_institution_id: null
```

The system must support accepted ambiguity. Historical records may never contain enough evidence to identify which of two same-named actors was involved.

`AMBIGUOUS != CORRUPTED`

`AMBIGUOUS != FRAUDULENT`

## 8. Name discrepancy record

```yaml
name_discrepancy:
  discrepancy_id: null
  actor_or_candidate_refs: []
  record_refs: []
  rendered_forms: []
  detected_at: null
  discrepancy_kind: spelling|formatting|translation|former_name|contextual_name|possible_homonym|possible_mislink|unknown
  current_interpretation: null
  evidence_refs: []
  requires_action_from_ref: null
  state: OPEN|EXPLAINED|CORRECTED|DISPUTED|UNRESOLVED
```

The discrepancy kind is a working classification, not proof.

`NAME_DISCREPANCY != DECEPTION`

`NAME_DISCREPANCY != DOCUMENT_FORGERY`

`NAME_DISCREPANCY != ACTOR_MISMATCH`

If evidence suggests an intentional cover operation, hand off to Infiltration. If evidence suggests falsified evidence in an authorized investigation, Case Authority may become relevant.

## 9. Correction event

```yaml
identity_record_correction_event:
  correction_id: null
  affected_record_ref: null
  affected_actor_id: null
  prior_value_ref: null
  corrected_value_ref: null
  correction_kind: transcription|formatting|linkage|name_update|source_update|other
  requested_by_ref: null
  decided_by_ref: null
  mandate_or_policy_ref: null
  supporting_evidence_refs: []
  decision_time: null
  effective_time: null
  propagated_to_refs: []
  pending_propagation_refs: []
  visibility: protected
```

This structure records the correction without inventing who has authority to make it. `mandate_or_policy_ref` must already exist.

`CORRECTION_REQUESTED != CORRECTION_APPROVED`

`CORRECTION_APPROVED != EVERY_COPY_UPDATED`

`DOWNSTREAM_RECORD_STALE != DOWNSTREAM_RECORD_FRAUDULENT`

`CORRECTED_VALUE != HISTORICAL_VALUE_AT_ALL_TIMES`

## 10. Scoped identity verification episode

```yaml
identity_verification_episode:
  verification_id: null
  subject_actor_or_claim_ref: null
  requesting_institution_id: null
  purpose_ref: null
  authority_or_service_basis_ref: null
  required_attribute_refs: []
  evidence_presented_refs: []
  evidence_validation_refs: []
  presenter_binding_refs: []
  linkage_refs: []
  result: PENDING|VERIFIED_FOR_SCOPE|NOT_VERIFIED|INSUFFICIENT|CONFLICTING|CANCELLED
  result_scope_ref: null
  decided_at: null
  expiry_or_recheck_ref: null
  disclosure_record_refs: []
```

This adapts only the high-level separation between evidence validation, presenter binding and authorization.

It does not define acceptable documents, required number of records, biometrics, identity assurance levels or technical authentication.

`EVIDENCE_VALIDATED != PRESENTER_VERIFIED`

`PRESENTER_VERIFIED != AUTHORIZED_FOR_SERVICE`

`VERIFIED_FOR_SCOPE != UNIVERSALLY_VERIFIED`

Credentials or the service owner decides authorization after identity requirements are satisfied.

## 11. Disclosure is a separate event

```yaml
identity_disclosure_event:
  disclosure_id: null
  subject_actor_id: null
  disclosed_attribute_refs: []
  recipient_actor_or_institution_id: null
  purpose_ref: null
  authority_or_consent_ref: null
  source_record_refs: []
  disclosed_at: null
  visibility_limit_ref: null
  onward_sharing_rule_ref: null
```

No default rule authorizes disclosure merely because the simulation contains the fact.

`KNOWN_TO_SYSTEM != KNOWN_TO_NPC`

`KNOWN_TO_ONE_INSTITUTION != KNOWN_TO_REGION`

`FORMER_NAME_LINKED != FORMER_NAME_PUBLIC`

`PRIVATE_LINKAGE != PUBLIC_ALIAS`

## 12. Observer belief remains local

The Infiltration layer already has `observer_identity_belief`. This extension can provide evidence references to update that belief but must not collapse belief into truth.

A shopkeeper may recognize a regular under an old nickname while an academy knows a formal record and a newspaper uses a professional name.

All three can be locally correct presentations of one actor.

## 13. Public name versus current service name

```yaml
identity_presentation_context:
  context_id: null
  actor_id: null
  venue_or_institution_ref: null
  preferred_display_name_ref: null
  required_record_name_ref: null
  public_name_ref: null
  privacy_notes_ref: null
  effective_time: null
```

This exists to avoid repeatedly replacing one universal `name` field.

A UI can render the appropriate form according to viewer, context and chronology.

## 14. Historical documents

Historical documents should preserve what they actually said.

If a 20-year-old roster contains `M. Arlen` and a later archive establishes that this refers to actor `A17`, the original document remains `M. Arlen`.

The system adds a linkage annotation rather than editing the old text.

`DOCUMENT_TEXT != CURRENT_NORMALIZED_IDENTITY_DISPLAY`

Archive custody and annotation policy remain with Archives/Museums.

## 15. Interregional handoff

When records cross regions, preserve both source representation and host interpretation.

```yaml
cross_region_identity_mapping:
  mapping_id: null
  actor_id: null
  source_region_id: null
  host_region_id: null
  source_identity_refs: []
  host_record_refs: []
  recognized_linkage_refs: []
  unresolved_discrepancy_refs: []
  recognition_decision_ref: null
  status: PENDING|RECOGNIZED_FOR_SCOPE|PARTIAL|NOT_RECOGNIZED|UNRESOLVED
```

Interregional Mobility owns the recognition decision. This extension preserves the identity mapping and discrepancy evidence.

No passports, citizenship or border authority are implied.

## 16. Credentials handoff

A credential can be genuine while its holder linkage remains unresolved, or the holder can be verified while the credential is expired or out of scope.

`HOLDER_VERIFIED != CREDENTIAL_VALID`

`CREDENTIAL_AUTHENTIC != HOLDER_VERIFIED`

`CREDENTIAL_VALID != REQUEST_AUTHORIZED`

Credentials owns the latter decisions.

## 17. Family and residence handoff

Identity verification cannot establish family or residence merely by matching a name.

`SAME_SURNAME != FAMILY_RELATIONSHIP`

`SAME_ADDRESS != SAME_HOUSEHOLD`

`OLD_ADDRESS_RECORD != CURRENT_RESIDENCE`

Family/Kinship and Residential own those states.

## 18. Pokémon relationship handoff

Human identity and Pokémon partnership must remain separate.

`TRAINER_NAME_MATCH != POKEMON_OWNERSHIP`

`ORIGINAL_TRAINER_METADATA != CURRENT_CUSTODY`

`CURRENT_CUSTODY != ACTIVE_TRAINER`

`POKEMON_PROXIMITY != HUMAN_IDENTITY_PROOF`

Pokémon Agency owns the relationship graph.

## 19. Canon-state labels

Every instantiated identity structure should distinguish:

- CANON_APPROVED: explicitly established by project canon;
- PROPOSED: available design candidate not yet canon;
- UNCERTAIN: evidence exists but identity/linkage is unresolved;
- HISTORICAL_RECORD: source-preserved statement about a past state;
- LOCAL_BELIEF: actor/institution belief, not authoritative truth.

The generator must never upgrade PROPOSED or UNCERTAIN state silently.

## 20. Quest grammar

Identity continuity quests should normally use this sequence:

1. A practical mismatch appears in a service or historical record.
2. The player identifies which exact question needs resolution.
3. Relevant records are located through their owner systems.
4. Evidence is compared without exposing irrelevant private attributes.
5. A linkage, correction or accepted ambiguity is recorded.
6. Downstream owners receive only the facts they need.
7. The Chronicle preserves both old and new record states.

The quest should not begin with an assumption of forgery.

## 21. Mystery grammar

Good identity mysteries can resolve to:

- one actor with two legitimate name forms;
- two actors with the same name;
- one stale copied record;
- one historical record using an old form;
- a translation or transcription mismatch;
- an unresolved linkage that remains unresolved;
- a real cover identity already owned by Infiltration;
- a credential mismatch unrelated to identity;
- two genuine records created under different local rules.

This produces mystery without making every clerical discrepancy malicious.

## 22. NPC archetypes

### The Record Linker

Knows how local archives, schools, clinics or clubs historically labeled people. Useful but not omniscient.

### The Same-Name Regular

Shares a common name with another local person and has spent years receiving the wrong assumptions.

### The Former-Name Professional

Publicly known under one current form while older professional records use another.

### The Cross-Region Returnee

Has records produced under two institutional naming conventions. Their story makes regional difference visible without requiring a border plot.

### The Privacy-Conscious Archivist

Can confirm that a linkage exists without disclosing the underlying private attribute.

### The Downstream Clerk

Operates a perfectly legitimate service whose copied dataset has not yet received an upstream correction.

## 23. Environmental storytelling

Minecraft presentation can show:

- old plaques or sign-in books with historical names;
- updated office directories;
- archived event posters;
- school photos with old captions;
- library cards or membership props where canon establishes them;
- a notice board carrying a corrected spelling;
- two institutional systems using different current display forms;
- former business signage tied to the same recurring NPC.

These visuals are evidence presentation only.

A Minecraft nametag does not establish canonical identity. A skin does not prove identity. UUID/entity identity does not automatically become an in-world identifier. Proximity does not establish family, ownership or credential status.

## 24. Encounter concept — Registry Counter Withdrawal

Full intended version:

A tactical threat appears near an institution while staff and visitors are handling an identity-related appointment. Staff must withdraw while protecting ordinary civilians and preventing sensitive records from becoming active tactical objects.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL for escort, Intercept and forced displacement
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for staged withdrawal
- full stateful damage pipeline — PARTIAL if attacks occur
- status lifecycle — PARTIAL for implemented legal statuses only
- terrain/weather/hazards/zones/reactions — BLOCKING for protected exits, dynamic access lanes or generalized reactions
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for PROTECT/WITHDRAW/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic appointment/record-state playback

Full version: BLOCKED FOR RICH SEMANTICS.

Reduced version: READY.

Reduced contract:

1. The institution pauses verification before BattleSpec creation.
2. Visitors, staff, private records, identity evidence and noncombatant Pokémon leave the tactical grid.
3. Ouros selects explicit combatants.
4. AutoPTU receives static reviewed geometry.
5. Battle resolution may produce only `IMMEDIATE_PUBLIC_APPROACH_CLEAR` or equivalent narrow physical state.
6. The institution separately decides whether appointments resume.

Victory never verifies identity, validates evidence, approves a correction or reveals private records.

## 25. Encounter concept — Record Transfer Chokepoint

Full intended version:

A separately authorized record-transfer operation encounters a tactical threat along its physical route.

Rich dependencies include complete movement for escort/Intercept, lifecycle for staged movement, protected-zone/reaction support, tactical policy and semantic playback.

Reduced version: READY.

Reduced contract:

1. Courier/Archives/owning institution pauses transfer outside BattleSpec.
2. The packet or storage object remains under existing custody and outside combat semantics.
3. Couriers and records withdraw to a safe world-state location.
4. AutoPTU resolves a conventional static battle.
5. The custody owner resumes or reroutes the transfer afterward.

Victory never transfers custody, authenticates records, links identities or confirms document contents.

## 26. Encounter concept — Verification Appointment Perimeter

Full intended version:

A scheduled identity-verification appointment cannot proceed because a separate tactical incident blocks physical access to the facility.

Reduced version: READY.

Reduced contract:

1. The appointment remains `PAUSED_ACCESS_BLOCKED`.
2. Applicant, verifier, evidence and private records remain outside BattleSpec.
3. Combat resolves only the physical perimeter incident.
4. The service owner decides whether and when verification resumes.

Victory never means `VERIFIED_FOR_SCOPE`.

## 27. Engine boundary

Reduced encounters are intentionally structured around currently verified baseline capability families: targeting/footprints/range/LoS, base movement legality, core calculations, action economy/initiative and AI legal-action infrastructure.

They still rely on whatever PARTIAL combat subsystems are used by the selected legal combatants, but the identity premise does not require new mechanics.

Rich versions remain blocked wherever they require complete escort/forced movement, timed withdrawal, protected zones/reactions, objective-aware tactical AI or semantic Minecraft playback.

## 28. PTU/Caelo guardrails

Do not invent:

- a universal Trainer ID or identity number;
- a universal Trainer license;
- passports, visas, citizenship or nationality mechanics;
- legal-name change procedures;
- birth-registration mechanics;
- signature mechanics;
- biometric verification;
- document-forgery DCs;
- universal identity checks using General Education, Perception, Intuition, Guile or Command;
- Aura, Telepathy or Psychic effects that establish identity automatically;
- Pokémon species that serve as universal lie detectors or identity scanners;
- Trainer Features that establish civil authority;
- battle victory as identity proof.

Exact PTU/Caelo mechanics may be used only when governing source and implementation contracts are identified.

## 29. Minecraft/Cobblemon authority boundary

Minecraft/Cobblemon may present identity-related world facts already decided by Ouros.

It does not decide:

- which actor a name refers to;
- whether two records belong to one person;
- whether an alias is deceptive;
- whether evidence is authentic;
- whether a credential is valid;
- whether a former name may be disclosed;
- family relationship;
- residence;
- Pokémon ownership/custody;
- institutional authorization;
- combatant selection;
- tactical legality;
- narrative consequence.

Minecraft UUIDs and Cobblemon entity IDs are implementation identifiers, not automatically diegetic identity documents.

## 30. Canon questions left open

Which Ouros institutions maintain persistent human records?

Do any regions issue Trainer-facing identity documents, and for what purpose?

Which identifiers are local, regional or portable?

What naming conventions exist in each culture and language?

How are former names, stage names, professional names or transliterations handled where they exist?

Who can request a correction?

Who can approve one?

Which records propagate corrections automatically, manually or never?

What identity attributes are public, private or institution-restricted?

How are children, dependents or guardians represented if canon requires those concepts?

How do regions recognize a returning person whose records use different forms?

Which historical NPCs have meaningful name or record changes already established by canon?

None of these questions is answered silently by this extension.