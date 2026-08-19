# Ouros Archives, Museums, Collections & Preservation Layer

Status: Proposed systems design. Not established canon.

## Purpose

Ouros already tracks public memory, archaeology, scientific evidence, item provenance, media, myths and institutional history. This layer defines what happens when an institution deliberately preserves knowledge or physical objects over time.

The key rule is separation. A collection item can exist physically, be held by one institution, be catalogued incorrectly, be interpreted in several ways and be displayed under a simplified public story at the same time.

## 1. Collection institution

```yaml
collection_institution:
  institution_id: null
  institution_type: null
  location_ids: []
  mission_claim_ids: []
  collecting_scope_tags: []
  staff_role_ids: []
  storage_location_ids: []
  public_gallery_ids: []
  restricted_area_ids: []
  reading_room_ids: []
  conservation_capacity: null
  catalog_system_id: null
  access_policy_id: null
  current_backlog_ids: []
  active_exhibit_ids: []
```

Candidate types:
- LIBRARY
- ARCHIVE
- MUSEUM
- RESEARCH_COLLECTION
- GYM_ARCHIVE
- LEAGUE_ARCHIVE
- CLUB_ARCHIVE
- CIVIC_RECORDS_OFFICE
- PRIVATE_COLLECTION
- MOBILE_EXHIBITION

The type does not grant authority outside the institution's authored mandate.

## 2. Collection object

```yaml
collection_object:
  collection_object_id: null
  underlying_entity_ref: null
  object_class: null
  provenance_event_ids: []
  ownership_claim_ids: []
  current_custodian_id: null
  physical_location_id: null
  condition_state: null
  catalog_record_ids: []
  interpretation_ids: []
  display_history_ids: []
  loan_history_ids: []
  evidence_case_ids: []
  stewardship_claim_ids: []
  access_state: STORED
```

Candidate object classes:
- document;
- book;
- field notebook;
- photograph/recording;
- fossil/specimen;
- artifact;
- trophy;
- battle record;
- map;
- tool;
- personal object;
- replica;
- digital record;
- living data collection reference.

Mechanical item state remains separate.

## 3. Catalog record

```yaml
catalog_record:
  catalog_record_id: null
  collection_object_id: null
  institution_id: null
  accession_id: null
  title_or_label: null
  creator_claim_ids: []
  date_claim_ids: []
  origin_claim_ids: []
  classification_tags: []
  description_claim_ids: []
  provenance_summary_ids: []
  confidence_band: null
  created_by_actor_id: null
  created_at: null
  supersedes_record_id: null
  status: CURRENT
```

States may include CURRENT, SUPERSEDED, DISPUTED, INCOMPLETE, SEALED and LOST.

A catalog record is an institutional claim. It is never world truth by itself.

## 4. Replica and authenticity state

```yaml
authenticity_assessment:
  assessment_id: null
  object_id: null
  assessor_ids: []
  method_claim_ids: []
  conclusion: unresolved
  confidence_band: null
  evidence_ids: []
  competing_assessment_ids: []
  public_status: null
```

Possible conclusions:
- UNRESOLVED
- ORIGINAL
- REPLICA
- RECONSTRUCTION
- PARTIAL_ORIGINAL
- MISIDENTIFIED
- MODERN_COPY
- ALTERED

A legitimate reconstruction is not fraud. A staff mistake is not sabotage. A real object can be catalogued as a replica, and a replica can be displayed honestly.

## 5. Accession and intake

```yaml
collection_intake:
  intake_id: null
  object_id: null
  institution_id: null
  source_actor_ids: []
  source_event_ids: []
  transfer_type: null
  custody_start: null
  ownership_change: false
  temporary_restrictions: []
  condition_report_id: null
  provenance_gap_ids: []
  review_state: PENDING
```

Transfer types can include donation, loan, field collection, excavation custody, evidence transfer, institutional transfer, temporary deposit and recovered-property holding.

Intake must reuse case/evidence custody when the object is active evidence.

## 6. Loan state

```yaml
collection_loan:
  loan_id: null
  object_ids: []
  lender_id: null
  borrower_id: null
  purpose: null
  authorized_by_ids: []
  start_time: null
  expected_return_time: null
  transport_dependency_ids: []
  condition_before_id: null
  condition_after_id: null
  restrictions: []
  status: PLANNED
```

Loan changes custody and location, not ownership by default.

This integrates with travel, logistics, insurance-like risk only if Ouros later defines such systems, and public-event schedules.

## 7. Exhibit lifecycle

```yaml
exhibit:
  exhibit_id: null
  institution_id: null
  theme_claim_ids: []
  object_ids: []
  interpretation_panel_ids: []
  guest_lender_ids: []
  lifecycle_state: PROPOSED
  opening_time: null
  closing_time: null
  target_audience_tags: []
  accessibility_state: null
  security_state: null
  conservation_constraints: []
  public_memory_outputs: []
  research_question_outputs: []
```

Lifecycle:
PROPOSED → RESEARCHING → INSTALLING → OPEN → CLOSING → DEINSTALLING → ARCHIVED.

Exhibit text can simplify or contest history. It cannot alter historical truth.

## 8. Interpretation panel

```yaml
interpretation_panel:
  panel_id: null
  exhibit_id: null
  source_claim_ids: []
  public_text_summary: null
  uncertainty_tags: []
  omitted_claim_ids: []
  revision_history_ids: []
  author_or_editor_ids: []
```

A panel should be able to say "unknown," "disputed" or "one interpretation" rather than forcing certainty.

## 9. Library/archive holding

```yaml
archival_holding:
  holding_id: null
  creator_or_source_ids: []
  date_range: null
  format_tags: []
  extent_band: null
  provenance_ids: []
  arrangement_state: null
  finding_aid_id: null
  digitization_state: null
  access_restrictions: []
  linked_event_ids: []
  linked_case_ids: []
  linked_family_ids: []
```

Holdings should be discoverable through metadata even when the content is restricted.

## 10. Finding aids and research navigation

```yaml
finding_aid:
  finding_aid_id: null
  institution_id: null
  scope_ids: []
  subject_tags: []
  location_tags: []
  actor_tags: []
  date_ranges: []
  cross_reference_ids: []
  completeness_state: null
```

Research gameplay should usually ask players to navigate relationships among records rather than pixel-hunt one hidden document.

## 11. Access policy

```yaml
collection_access_policy:
  policy_id: null
  institution_id: null
  public_spaces: []
  supervised_spaces: []
  restricted_spaces: []
  restricted_collection_ids: []
  valid_reason_tags: []
  review_actor_ids: []
  appeal_or_exception_process_ref: null
```

Potential restriction reasons:
- preservation risk;
- active case/evidence;
- patient/privacy information;
- sensitive ecological coordinates;
- cultural stewardship;
- donor/loan condition;
- safety;
- conservation work;
- unresolved ownership/custody.

The generator must not invent restrictions only to create a locked-door quest.

## 12. Conservation treatment

```yaml
conservation_treatment:
  treatment_id: null
  object_id: null
  conservator_ids: []
  observed_condition_ids: []
  proposed_action_ids: []
  approved_action_ids: []
  treatment_event_ids: []
  reversible: null
  before_record_ids: []
  after_record_ids: []
  uncertainty_notes: []
  mechanics_review_required: true
```

Narrative conservation cannot repair a mechanical item, revive a fossil, cleanse a supernatural effect or restore a rules-relevant object without PTU/Caelo/AutoPTU authority.

## 13. Backlog and uncatalogued material

```yaml
collection_backlog:
  backlog_id: null
  institution_id: null
  intake_ids: []
  approximate_scope: null
  priority_reasons: []
  staffing_dependency_ids: []
  storage_risk_ids: []
  current_state: STABLE
```

Backlogs generate strong noncombat content:
- identify provenance;
- reconnect detached labels;
- compare old field notebooks;
- locate donor records;
- stabilize material after a crisis;
- discover that several items belong to one expedition or case.

Do not make every backlog contain a legendary artifact.

## 14. Return, repatriation and contested stewardship

```yaml
return_review:
  review_id: null
  object_ids: []
  claimant_ids: []
  current_custodian_id: null
  ownership_claim_ids: []
  stewardship_claim_ids: []
  provenance_evidence_ids: []
  institutional_position_ids: []
  proposed_resolution_ids: []
  status: OPEN
```

Ouros must author its own cultures, laws and institutions before determining outcomes.

No real-world people or Indigenous cultures should be copied into fictional disputes for aesthetic flavor.

## 15. Deaccession and loss

An institution can stop holding an object without erasing history.

Candidate events:
- RETURNED
- TRANSFERRED
- DEACCESSIONED
- DESTROYED
- LOST
- STOLEN
- RECLASSIFIED
- REUNITED_WITH_SOURCE_COLLECTION

Every state change preserves prior records and provenance.

## 16. Public memory interaction

Museums and archives can shape public memory by selection and framing.

They may:
- commemorate an event;
- omit a participant;
- update an old caption;
- host competing interpretations;
- display replicas while originals remain stored;
- publish a correction;
- loan a significant item to another region.

None of these actions rewrite validated Chronicle facts.

## 17. Science interaction

Research collections can support repeatable science.

A specimen or record may connect to:
- sample provenance;
- datasets;
- prior methods;
- old classifications;
- replication attempts;
- revised hypotheses.

A catalog correction can become a scientific event without becoming a mechanical reward.

## 18. Archaeology and language interaction

Artifacts and texts should retain:
- excavation context;
- transcription versions;
- translation versions;
- interpretation versions;
- stewardship claims;
- conservation history.

A translation update changes interpretation state, not the physical artifact.

## 19. Minecraft representation

Use coarse visible state:
- open/closed galleries;
- rotating exhibits;
- storage rooms that exist but do not instantiate every item;
- named curators, librarians and conservators;
- public reading rooms;
- restricted doors with authored reasons;
- exhibit panels/books/interfaces linked to structured records;
- returned/removed objects visibly absent;
- renovation or disaster recovery states;
- traveling exhibition crates;
- digitization/work tables.

Do not require every book or artifact to exist as a unique Minecraft item entity.

## 20. Encounter implementation contracts

### A. Gallery Lockdown

Narrative premise: a public exhibition suffers an incident while visitors are still inside. Players must secure a safe route and protect collection state without treating every object as a combat prop.

FULL version requires:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING if escort/chokepoint behavior is tactical;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- status lifecycle: PARTIAL for selected legal statuses;
- terrain/weather/hazards/zones/reactions: BLOCKING if cases, smoke, collapsing fixtures or alarm zones alter combat;
- abilities/items: PARTIAL as selected combatants require;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for objective-aware attackers/guards;
- adapter/playback: BLOCKING.

REDUCED version: evacuation and collection protection resolve in overworld/world state. AutoPTU receives a stable arena after civilians and fragile objects are removed from tactical interaction.

### B. Archive Water Intrusion

Narrative premise: a damaged archive is threatened by rising water while a separate encounter blocks access to a pump/control route.

FULL version requires dynamic terrain/hazards, REACH/ACTIVATE objective support, objective-aware AI and adapter playback: BLOCKING.

REDUCED version: players choose which holdings to stabilize in world state, then fight a standard legal encounter on a dry/static map before or after operating the infrastructure outside the grid.

### C. Traveling Exhibit Intercept

Narrative premise: an institutional loan shipment is delayed or attacked during transport; ownership does not change because the players recover it.

FULL version requires interception/forced movement and protect/breakthrough objective support plus tactical AI: BLOCKING.

REDUCED version: transport stops, exhibit crates remain outside the battle grid, and the party clears a static chokepoint. Custody updates only after the battle transcript resolves.

## 21. PTU/Caelo boundary

Narrative records may propose research, cataloging, identification, handling and security scenes, but exact checks/effects require governing source validation.

Do not invent:
- Education DCs;
- Chronicler/Researcher/Scientist Feature effects;
- artifact identification bonuses;
- fossil revival rules;
- supernatural relic effects;
- item repair/restoration mechanics;
- security/disguise bonuses;
- Trainer Feature interrupts;
- hazard damage.

## 22. Generation guardrails

1. Collection record is not canonical truth.
2. Custody is not ownership.
3. Display is not ownership.
4. Replica is not automatically fraud.
5. A curator can be wrong without being corrupt.
6. Restriction needs a causal, recorded reason.
7. Missing provenance is a research problem, not automatic evidence of theft.
8. An exhibit may simplify history but cannot overwrite the Chronicle.
9. Valuable does not mean mechanically powerful.
10. Old does not mean magical.
11. A museum object is not loot merely because the player can reach it.
12. Returned or transferred objects keep historical provenance.
13. Never infer sensitive cultural ownership without authored canon.
14. Prefer recoverable cross-reference puzzles over arbitrary hidden switches.
15. Keep battles away from fragile collection objects until the rules engine explicitly supports those tactical interactions.

## 23. Implementation priority

1. collection object + catalog record;
2. accession/custody integration;
3. exhibit lifecycle;
4. archival holdings + finding aids;
5. access policy;
6. loan history;
7. catalog revision/supersession;
8. conservation treatment history;
9. backlog generator;
10. public-memory integration;
11. Minecraft visible-state mapping;
12. richer tactical contracts only after engine capabilities exist.