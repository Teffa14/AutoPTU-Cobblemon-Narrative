# Ouros Museums, Collections, Exhibitions & Conservation Layer

Status: Proposed systems design. Not established canon.

## Purpose

Ouros already tracks persistent objects, archaeological context, archives, public memory, photographs, custody, transport and institutional decisions. This layer owns the institutional life of collection objects: accession, cataloguing, storage, conservation, loans, exhibitions, label revisions, research access and disposition.

The goal is to let museums accumulate history without turning them into static quest hubs or omniscient lore databases.

## Core separation

Use this chain:

physical object -> provenance/custody -> accession decision -> collection record -> condition/conservation -> storage/location -> exhibition/research use -> later revision/disposition

Keep these states independent:
- possession;
- ownership claim;
- collection membership;
- catalogued identity;
- current location;
- display status;
- research eligibility;
- conservation condition;
- public interpretation;
- legal/institutional authority.

## 1. Museum or collection institution

```yaml
collection_institution:
  institution_id: null
  location_ids: []
  collection_scope_tags: []
  public_gallery_ids: []
  storage_location_ids: []
  conservation_space_ids: []
  research_space_ids: []
  accession_authority_role_ids: []
  loan_authority_role_ids: []
  collections_staff_ids: []
  current_capacity_state: null
  public_access_state: OPEN
  policy_revision_ids: []
```

A museum can be closed to visitors while collections work continues.

## 2. Collection object link

Do not duplicate physical objects. Link the institutional collection state to the existing `item_instance_id`, fossil/sample/specimen record or other persistent object identity.

```yaml
collection_object_link:
  collection_link_id: null
  object_id: null
  institution_id: null
  collection_unit_id: null
  accession_case_id: null
  collection_status: null
  catalog_record_ids: []
  condition_report_ids: []
  conservation_treatment_ids: []
  loan_ids: []
  exhibition_assignment_ids: []
  research_access_ids: []
  current_location_record_id: null
  restricted_information_refs: []
```

Suggested statuses:
- TEMPORARY_CUSTODY
- PENDING_ACCESSION
- ACCESSIONED
- RESEARCH_DEPOSIT
- INCOMING_LOAN
- OUTGOING_LOAN
- RETURN_PENDING
- DEACCESSION_REVIEW
- DEACCESSIONED
- DISPOSED_OR_TRANSFERRED

## 3. Accession case

```yaml
accession_case:
  accession_case_id: null
  institution_id: null
  object_ids: []
  proposed_source_actor_id: null
  proposed_transfer_type: null
  provenance_refs: []
  custody_refs: []
  collection_fit_assessment: null
  care_capacity_assessment: null
  restrictions: []
  unresolved_claim_ids: []
  decision_state: PENDING
  decision_record_id: null
```

A donation offer is not an accession. Physical delivery is not an accession. Accession is an institutional decision.

## 4. Catalogue record

```yaml
catalog_record:
  catalog_record_id: null
  collection_link_id: null
  record_revision: 1
  title_or_name: null
  object_type: null
  description: null
  maker_or_origin_claim_ids: []
  date_or_period_claim_ids: []
  provenance_refs: []
  archaeological_context_refs: []
  taxonomy_refs: []
  language_translation_refs: []
  linked_object_ids: []
  confidence_notes: []
  created_at: null
  supersedes_record_id: null
```

Catalogue revisions preserve older descriptions. A new attribution does not rewrite the historical record.

## 5. Object location history

```yaml
object_location_event:
  event_id: null
  object_id: null
  from_location_id: null
  to_location_id: null
  purpose: null
  custodian_ids: []
  timestamp: null
  shipment_or_handoff_refs: []
  condition_report_id: null
```

Purposes may include storage, gallery display, conservation, research, photography, outgoing loan, return, emergency relocation or quarantine/hold where separately authorized.

Minecraft block position is a projection, not authoritative collection location history.

## 6. Condition report

```yaml
condition_report:
  condition_report_id: null
  object_id: null
  observer_ids: []
  timestamp: null
  observed_features: []
  damage_or_change_observations: []
  environmental_context_refs: []
  imaging_refs: []
  comparison_to_prior_report: null
  interpretation_claim_ids: []
```

Observation and cause remain separate. A crack after transport does not prove transport caused it.

## 7. Conservation treatment

```yaml
conservation_treatment:
  treatment_id: null
  object_id: null
  authorization_id: null
  treatment_goal: null
  pre_condition_report_id: null
  intervention_steps: []
  materials_used_batch_ids: []
  completed_by_ids: []
  completion_time: null
  post_condition_report_id: null
  reversibility_or_limit_notes: []
```

Conservation does not make an object mechanically stronger or historically more authentic.

## 8. Exhibition project

```yaml
exhibition_project:
  exhibition_id: null
  institution_id: null
  title: null
  curatorial_question: null
  lifecycle_state: PLANNING
  host_schedule: []
  object_assignment_ids: []
  replica_or_cast_ids: []
  label_revision_ids: []
  accessibility_plan_refs: []
  environmental_requirement_refs: []
  public_event_refs: []
  opening_time: null
  closing_time: null
```

Suggested lifecycle:
- PROPOSED
- PLANNING
- OBJECT_SELECTION
- PREPARATION
- INSTALLATION
- OPEN
- TEMPORARILY_CLOSED
- DEINSTALLATION
- TRAVELLING
- CLOSED
- ARCHIVED

## 9. Exhibition object assignment

```yaml
exhibition_object_assignment:
  assignment_id: null
  exhibition_id: null
  object_id: null
  display_role: null
  display_location_id: null
  mount_or_case_id: null
  loan_id: null
  label_revision_id: null
  display_start: null
  display_end: null
```

`ON_DISPLAY` never means `OWNED_BY_HOST`.

## 10. Label and interpretation revisions

```yaml
exhibit_label_revision:
  label_revision_id: null
  exhibition_id: null
  object_ids: []
  language_version_refs: []
  claim_ids: []
  evidence_refs: []
  uncertainty_notes: []
  public_memory_refs: []
  supersedes_revision_id: null
  effective_from: null
```

A gallery can change its interpretation while preserving photographs and records of the old label.

## 11. Loans

```yaml
museum_loan:
  loan_id: null
  lender_institution_or_actor_id: null
  borrower_institution_id: null
  object_ids: []
  loan_scope: null
  start_time: null
  due_time: null
  custody_handoff_ids: []
  transport_refs: []
  condition_report_ids: []
  restrictions: []
  status: AGREED
```

Suggested states:
- PROPOSED
- AGREED
- PREPARING
- IN_TRANSIT
- RECEIVED
- ON_LOAN
- RETURN_IN_TRANSIT
- RETURNED
- OVERDUE_REVIEW
- TERMINATED

Loans may use Postal/Transport/Supply Chain handoffs but should not duplicate those systems.

## 12. Replicas, casts and reconstructions

```yaml
replica_relation:
  replica_object_id: null
  source_object_id: null
  relation_type: CAST
  maker_id: null
  creation_event_id: null
  intended_use: DISPLAY
  fidelity_claims: []
```

Possible relation types:
- CAST
- REPLICA
- RECONSTRUCTION
- STUDY_COPY
- DISPLAY_MODEL
- DIGITAL_RECONSTRUCTION_REFERENCE

A replica can later become historically significant in its own right.

## 13. Research access

```yaml
collection_research_access:
  access_id: null
  object_ids: []
  researcher_ids: []
  approved_method_ids: []
  prohibited_actions: []
  sample_authorization_refs: []
  start_time: null
  end_time: null
  output_dataset_refs: []
```

Display permission does not authorize sampling. General museum access does not authorize collection storage access.

## 14. Deaccession and disposition

```yaml
deaccession_review:
  review_id: null
  institution_id: null
  object_ids: []
  reason_claims: []
  provenance_review_refs: []
  claim_conflict_refs: []
  alternative_destination_ids: []
  decision_state: PENDING
  final_disposition_event_id: null
```

The generator must not invent legal disposal rights. Possible authored outcomes may include return, institutional transfer, repatriation-like return where canon establishes the relationship, or continued retention pending review.

## 15. Living Pokémon boundary

A living Pokémon cannot be represented as a museum collection object.

Museums may hold:
- fossils;
- photographs;
- casts;
- shed material where ethically and mechanically valid;
- historical equipment;
- records;
- non-living specimens where canon and ethics permit;
- objects associated with a known Pokémon.

A living Pokémon housed, studied, employed or publicly presented by a museum remains a persistent Pokémon actor under Pokémon Agency/Care/Research Ethics.

## 16. Exhibition generation grammar

Generate an exhibit only from existing world state:

collection holdings + current interpretation + public question + staff/capacity + available loans + physical venue + accessibility + timing.

Good exhibit drivers:
- new research changes an old attribution;
- a travelling collection becomes available;
- an anniversary creates public interest;
- a recovered object completes a comparison set;
- a conservation treatment makes display possible again;
- a public misconception motivates a corrective exhibit;
- two institutions present competing interpretations side-by-side;
- a replica allows display while the original remains protected.

Do not generate an exhibit solely because the world has been quiet.

## 17. Long-term continuity

Museums should accumulate:
- accession history;
- old catalogue terms;
- conservation records;
- loan history;
- changing labels;
- retired galleries;
- storage moves;
- staff expertise;
- public controversies;
- corrected mistakes;
- famous replicas;
- objects never displayed;
- exhibitions remembered after closing.

## 18. Encounter contract pattern

Every museum encounter should state:
- which objects are authoritative world-state objects;
- whether civilians/staff remain in the tactical area;
- whether display cases/mounts are scenery or mechanics;
- whether an object can move during battle;
- whether an interactable is mechanically implemented;
- what happens to custody after combat;
- which evidence comes from AutoPTU transcript versus museum records.

Reduced-mode default:
- evacuate civilians;
- secure fragile objects when plausible;
- freeze gallery geometry;
- treat unverified display cases/mounts as non-mechanical scenery;
- let AutoPTU resolve only combatants;
- resume collection/custody state afterward.

## 19. Capability mapping

Museum-specific rich scenes may depend on:

- targeting/footprints/range/LoS — VERIFIED for static combat geometry;
- base movement legality — VERIFIED for ordinary Shift/Jump legality;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING for moving exhibits, escorts, crowd lanes or knockback interactions;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for glass, fire, falling displays, protected zones or environmental museum effects;
- move-specific behavior — PARTIAL and must be individually verified;
- abilities — PARTIAL and must be individually verified;
- items — PARTIAL and must be individually verified;
- Trainer Features/perks — PARTIAL and must be individually verified;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for protect/retrieve/evacuate/withdraw objectives;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## 20. Guardrails

Do not infer:
- museum custody -> ownership;
- accession -> public display;
- display -> research permission;
- curator title -> universal authority;
- old label -> current truth;
- new label -> old label never existed;
- replica -> fake/deceptive;
- restored object -> mechanically repaired item;
- famous object -> higher monetary value;
- museum closure -> no staff activity;
- object missing from gallery -> stolen;
- broken case -> item damage;
- battle victory -> custody resolved;
- fossil -> restoration eligibility;
- fossil restoration -> museum ownership of living Pokémon;
- exhibit mineral/artifact -> battlefield zone/effect.

## 21. Integration boundaries

- Material Culture: object identity, provenance, repair/transformation.
- Archaeology: site context and historical interpretation.
- Archives: documentation and catalogue/label records.
- Public Memory: visitor-facing narratives and legacy.
- Photography: imaging, condition photographs and derivative display copies.
- Languages: multilingual labels and terminology history.
- Supply Chains/Postal/Travel: object transport.
- Case/Custody: theft, disputed possession and evidence.
- Research Ethics: sampling and intrusive study.
- Institutional Review: accession/deaccession or contested decisions where mandated.
- Pokémon Agency/Care: all living Pokémon.
- Minecraft: physical projection only.
- AutoPTU: tactical combat authority only.

## 22. Canon questions left open

- Which museum/collection institutions exist in Ouros at campaign start?
- Which collections are public, research-only, private, sacred or community-held?
- Who can accession/deaccession objects?
- What forms of long-term storage and conservation technology exist?
- Which objects may be sampled?
- How do loans work across regions?
- Which cultural objects have restricted display/access?
- Can clubs or player institutions create collections?
- What happens when provenance becomes contested?
- How are living Fossil Pokémon separated from the fossils/material used in restoration?

No answer should be generated without authored canon or governing rules.
