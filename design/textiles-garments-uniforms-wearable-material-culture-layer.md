# Ouros Textiles, Garments, Uniforms & Wearable Material Culture Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This layer models textiles and wearable objects as persistent parts of world history without turning appearance into authority or combat mechanics.

It covers fiber/textile provenance, garment construction, fit, alterations, repairs, care, uniform issue/return, secondhand continuity, wearable presentation and handoff to museums/archives when an ordinary object becomes historically significant.

It does not replace PTU equipment, Fashionista, armor, accessory or crafting rules.

## 1. Authority boundaries

This layer owns:

- textile-specific material lineage after raw material sourcing;
- fabric/textile batches used in wearable construction;
- garment/wearable specifications and revisions;
- construction history for individually important garments;
- fit/alteration history;
- repair and maintenance history;
- uniform pattern history;
- issue/return/reassignment state;
- wearable-use observations when they matter to Chronicle;
- secondhand continuity for wearable objects;
- garment retirement/storage state;
- handoff metadata toward Museum/Archive preservation.

It does not own:

- generic persistent item identity/provenance -> Material Culture;
- industrial production runs and quality disposition -> Manufacturing;
- procurement/inventory/storage/freight -> Supply Chains;
- sale/listing/payment -> Markets/Finance;
- jobs and role assignments -> Workplaces;
- actual authorization/eligibility -> Credentials;
- actor names/private identity -> Identity;
- event costumes as event programming -> Festivals/Performance;
- collection accession/conservation policy -> Museums;
- Pokémon identity/agency/custody -> Pokémon Agency;
- PTU equipment/Armor/Accessories/Fashionista mechanics -> PTU/Caelo/AutoPTU;
- Minecraft skins/armor slots as rules authority -> never.

## 2. Core separation

Never collapse these states:

```text
MATERIAL_EXISTS
TEXTILE_PRODUCED
GARMENT_CONSTRUCTED
GARMENT_FITTED
GARMENT_ISSUED
GARMENT_WORN
GARMENT_REPAIRED_OR_ALTERED
GARMENT_RETURNED_OR_TRANSFERRED
GARMENT_RETIRED
GARMENT_ACCESSIONED
```

Important no-inferences:

```text
uniform worn != credential
uniform worn != employment
insignia present != current rank
costume != profession
style != identity
appearance != wealth
wearable possession != authority
winter garment != cold immunity
protective-looking garment != PTU Armor
repair != mechanical stat change
Pokémon accessory != consent forever
Minecraft visual != PTU equipment state
```

## 3. TEXTILE_MATERIAL_BATCH

Use a textile batch only when provenance matters beyond ordinary inventory.

```yaml
textile_material_batch:
  textile_batch_id: null
  parent_material_batch_ids: []
  source_material_refs: []
  source_pokemon_entity_ids: []
  source_site_ids: []
  processing_run_ids: []
  composition_claims: []
  dye_or_finish_refs: []
  quantity_band: null
  provenance_confidence: null
  current_custody_ref: null
  canon_state: PROPOSED
```

A Pokémon-derived fiber reference never implies that collection was harmless, voluntary or repeatable. Those questions belong to Pokémon Agency/Care and authored material-source rules.

## 4. GARMENT_INSTANCE

Important wearable objects retain one persistent identity.

```yaml
garment_instance:
  garment_instance_id: null
  material_culture_item_id: null
  garment_type: null
  design_spec_revision_id: null
  textile_batch_ids: []
  construction_event_id: null
  current_condition_ref: null
  current_fit_ref: null
  current_custody_ref: null
  current_owner_claim_ref: null
  current_issue_assignment_id: null
  repair_event_ids: []
  alteration_event_ids: []
  care_event_ids: []
  transfer_event_ids: []
  museum_or_archive_ref: null
  mechanical_item_ref: null
  history_event_ids: []
```

The same coat remains the same instance after patching, relining, resizing or transfer unless the physical object is actually transformed into a new item according to Material Culture policy.

## 5. GARMENT_SPECIFICATION

```yaml
garment_specification:
  garment_spec_revision_id: null
  garment_family_id: null
  revision_label: null
  intended_use_contexts: []
  construction_notes: []
  material_requirements: []
  fit_dimension_refs: []
  visual_marking_refs: []
  uniform_pattern_ref: null
  mechanical_rule_ref: null
  effective_from: null
  supersedes_revision_id: null
```

Visual similarity does not establish that two garments share a specification.

## 6. CONSTRUCTION_EVENT

```yaml
garment_construction_event:
  construction_event_id: null
  garment_instance_id: null
  artisan_or_run_ref: null
  location_id: null
  textile_batch_ids: []
  pattern_revision_id: null
  observed_methods: []
  start_time_ref: null
  completion_time_ref: null
  quality_or_condition_observation_ids: []
  mechanics_review_required: true
```

Construction can be artisanal, institutional or manufacturing-backed. This layer records garment-specific continuity; Manufacturing owns repeatable production execution.

## 7. FIT_PROFILE and ALTERATION_EVENT

Fit is a wearable/material relation, not a body-stat rule.

```yaml
fit_profile:
  fit_profile_id: null
  garment_instance_id: null
  actor_id: null
  observed_at: null
  fit_notes: []
  mobility_observations: []
  comfort_claims: []
  measurement_refs: []
  author_id: null
  status: OBSERVED
```

```yaml
alteration_event:
  alteration_event_id: null
  garment_instance_id: null
  previous_fit_profile_id: null
  intended_actor_id: null
  alteration_type: null
  material_added_refs: []
  material_removed_refs: []
  artisan_ref: null
  resulting_fit_profile_id: null
  reversible: null
  source_event_id: null
```

No fit observation modifies Speed, Evasion, Jump or movement unless an exact PTU item/rule is invoked.

## 8. REPAIR and CARE

```yaml
wearable_repair_event:
  repair_event_id: null
  garment_instance_id: null
  damage_or_condition_observation_ids: []
  repair_method: null
  replacement_material_refs: []
  repairer_ref: null
  resulting_condition_ref: null
  visible_revision_note: null
  source_event_id: null
```

```yaml
wearable_care_event:
  care_event_id: null
  garment_instance_id: null
  care_type: CLEANING|DRYING|STORAGE|PEST_ISOLATION|CONSERVATION_PREP|OTHER
  performed_by_ref: null
  location_id: null
  observation_ids: []
  outcome_ref: null
```

Routine maintenance usually compresses into background state. Chronicle should expand it when a repair changes provenance, identity, access, public memory or future decisions.

## 9. UNIFORM_PATTERN

A uniform pattern is institutional presentation, not authority.

```yaml
uniform_pattern:
  uniform_pattern_id: null
  institution_id: null
  revision_id: null
  role_context_refs: []
  visual_description_ref: null
  insignia_refs: []
  expected_garment_spec_refs: []
  issue_policy_ref: null
  effective_from: null
  retired_at: null
  canon_state: PROPOSED
```

Old uniforms can remain in private hands, secondhand markets, archives or museums after the institution changes its design.

## 10. UNIFORM_ISSUE_ASSIGNMENT

```yaml
uniform_issue_assignment:
  uniform_issue_assignment_id: null
  garment_instance_id: null
  institution_id: null
  assigned_actor_id: null
  role_assignment_ref: null
  credential_ref: null
  issued_at: null
  expected_return_at: null
  returned_at: null
  issue_status: ISSUED
  source_event_id: null
```

Candidate states:

- RESERVED
- ISSUED
- TEMPORARY_LOAN
- RETURN_REQUESTED
- RETURNED
- LOST_REPORTED
- RETIRED_FROM_SERVICE
- TRANSFERRED_TO_COLLECTION

A still-valid credential can exist after a uniform was returned. A uniform can remain physically present after the underlying role ended.

## 11. SECONDHAND_TRANSFER

Wearables can accumulate several owners/custodians.

```yaml
wearable_transfer_event:
  transfer_event_id: null
  garment_instance_id: null
  from_actor_or_institution_ref: null
  to_actor_or_institution_ref: null
  transfer_type: SALE|GIFT|LOAN|RETURN|INHERITED_CUSTODY|DONATION|OTHER
  market_transaction_ref: null
  agreement_ref: null
  condition_at_transfer_ref: null
  transferred_at: null
```

Transfer type is descriptive. Legal ownership, inheritance and payment remain with their respective authorities.

## 12. Pokémon-authored wearables

Species-authored cases require explicit modeling.

Examples from research:

- Leavanny may create woven-leaf clothing;
- Sewaddle may create clothing by imitating that behavior;
- Burmy cloak state is biological/species-specific and is not an ordinary transferable garment;
- Wormadam's cloak becomes part of its body;
- Wooloo fleece can be a material source where canon/agency rules permit.

Use:

```yaml
pokemon_wearable_relation:
  relation_id: null
  pokemon_entity_id: null
  garment_instance_id: null
  relation_type: CREATED|WORN|CARRIED|ASSISTED_CONSTRUCTION|OBSERVED_WITH
  consent_or_behavior_observation_ids: []
  start_time_ref: null
  end_time_ref: null
  mechanical_rule_ref: null
```

Never infer obedience, ownership, Fashionista competence or mechanical protection from the relation.

## 13. Historical garments

When a wearable becomes historically important:

1. Material Culture keeps physical identity/provenance.
2. This layer keeps construction, wear, repair and alteration history.
3. Museums/Archives decide accession, cataloging, conservation and exhibition.
4. Public Memory tracks later interpretations.

A replica receives its own item identity. It does not inherit the original's provenance.

## 14. Minecraft projection

Minecraft may project:

- skins/models;
- clothing overlays;
- armor-like cosmetics;
- mannequins;
- tailoring benches;
- racks;
- laundry/drying areas;
- textile workshops;
- uniform variants.

Minecraft must never infer:

- credential state;
- current institutional membership;
- gender or private identity;
- mechanical Armor/Accessory effects;
- Fashionista effects;
- weather resistance;
- material provenance;
- Pokémon consent.

The server/world systems remain authoritative.

## 15. PTU mechanical gate

If a garment corresponds to a real PTU/Caelo item, accessory, armor, Fashionista recipe or Feature effect, store an explicit `mechanical_rule_ref` and require validated engine support.

No explicit rule reference means the wearable is narrative/material state only.

This is especially important because Fashionista is a real PTU mechanical class. Similar appearance is never sufficient evidence.

## 16. Persistence and compression

Persist only details that may matter later:

- historically important repairs;
- major alterations;
- uniform revision changes;
- source-material provenance;
- transfers between important actors;
- condition changes affecting museum/conservation decisions;
- Pokémon-created or Pokémon-worn items with meaningful agency/history.

Do not log every wash, button replacement or routine outfit change.

## 17. Cross-layer examples

### A transit coat

A transit institution changes uniform pattern. An old issued coat is returned, sold legally as surplus, repaired by a private tailor and later donated to a museum. The role/credential ended years before the physical coat disappeared.

### A Wooloo-fiber batch

A fiber batch enters Supply Chains, becomes textile through Manufacturing, is used in one garment instance, sold through Markets, altered twice and later conserved. The fiber source does not grant the garment a mechanical cold-resistance effect.

### A Leavanny-made garment

A Leavanny voluntarily creates a leaf covering for another Pokémon. Pokémon Agency records the actors and behavior; this layer records the physical garment if it persists. It remains non-mechanical unless a validated rule says otherwise.

## 18. Canon safety

Everything introduced by this document remains PROPOSED until separately approved.

Do not author universal Ouros fashion norms, gendered clothing rules, religious dress, uniforms, fiber economies or regional costumes from real-world cultures by reskinning them. Regional wearable traditions should be original and grounded in authored Ouros history, ecology, industry and institutions.