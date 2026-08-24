# Botanical Gardens, Living Collections & Seed Banks Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Pass: 152

## Purpose

This layer owns institutional stewardship of living plant material after an explicit acquisition or collection event: accession identity, provenance, living specimens, propagules, seed-bank lots, propagation history, duplicate holdings, horticultural care, curatorial purpose, viability review and collection continuity.

It does not replace the Flora layer. Flora owns ecological vegetation state, flowering, dispersal, recruitment, succession and restoration outcomes in the landscape.

It does not replace Museums. Museums owns preserved/nonliving collection objects and exhibition custody. A dried voucher or historical tool can hand off there while a living accession remains here.

## Core separation

Never collapse these states:

wild population or cultivated source
→ collection/acquisition event
→ accession record
→ living specimen / seed lot / propagule holding
→ propagation event
→ derivative specimen
→ horticultural care and observation
→ curatorial interpretation/use
→ transfer / duplicate holding / deaccession
→ possible restoration handoff

Taxon identity, accession identity and individual living specimen identity are different.

A plant can be alive while its label is wrong.

A seed can be stored while its viability is unknown.

A duplicate can exist at another institution without transferring ownership of the original accession.

## 1. Botanical institution

```yaml
botanical_institution:
  institution_id: null
  settlement_id: null
  site_ids: []
  collection_program_ids: []
  greenhouse_asset_ids: []
  seed_bank_asset_ids: []
  nursery_site_ids: []
  research_program_ids: []
  education_program_ids: []
  public_access_policy_ref: null
  partner_institution_ids: []
  historical_revision_ids: []
  canon_status: proposed
```

Potential forms include botanic garden, arboretum, conservation nursery, institutional greenhouse, university garden, community seed collection, research living collection or regional propagation facility.

No institution type creates Skills, Trainer Features or legal authority automatically.

## 2. Accession

```yaml
living_accession:
  accession_id: null
  institution_id: null
  taxon_determination_ids: []
  received_at: null
  acquisition_event_id: null
  provenance_class: unknown
  source_location_ref: null
  source_actor_or_institution_ref: null
  propagule_type: null
  source_population_ref: null
  restriction_refs: []
  current_collection_status: active
  living_specimen_ids: []
  seed_lot_ids: []
  derivative_accession_ids: []
  duplicate_holding_ids: []
  evidence_refs: []
```

Suggested provenance classes:

- WILD_ORIGIN
- WILD_DERIVED
- GARDEN_OR_INSTITUTION_ORIGIN
- CULTIVATED_OR_COMMERCIAL_ORIGIN
- HISTORIC_COLLECTION_UNKNOWN
- UNKNOWN

These are documentation states. They do not establish native status, legality, genetic quality or conservation value by themselves.

## 3. Acquisition / collection event

```yaml
botanical_acquisition_event:
  event_id: null
  occurred_at: null
  acquisition_type: field_collection|institution_transfer|donation|purchase|propagation|historic_reconciliation|other
  source_ref: null
  collector_actor_ids: []
  authorization_refs: []
  research_ethics_refs: []
  biosecurity_refs: []
  taxon_claim_ref: null
  locality_claim_ref: null
  quantity_or_material_class: null
  field_observation_refs: []
  voucher_ref: null
  notes: null
```

A field collection never means the wild population has been fully sampled or harmed. Conservation/Research Ethics decides whether collection was appropriate when canon requires that review.

## 4. Living specimen

```yaml
living_specimen:
  specimen_id: null
  accession_id: null
  current_location_id: null
  planted_or_container_state: null
  origin_propagation_event_id: null
  planted_at: null
  current_condition_state: unknown
  phenology_observation_ids: []
  care_record_ids: []
  taxon_determination_ids: []
  material_use_ids: []
  display_label_revision_ids: []
  current_status: living
  ended_at: null
  end_reason: null
```

Suggested status values:

- LIVING
- DORMANT
- UNDER_REVIEW
- LOST
- DEAD_CONFIRMED
- TRANSFERRED
- DEACCESSIONED
- UNKNOWN

A dead specimen does not erase accession history. It may have descendants, samples, photographs, labels or a preserved voucher.

## 5. Propagation event

```yaml
propagation_event:
  propagation_event_id: null
  parent_accession_ids: []
  parent_specimen_ids: []
  material_type: seed|cutting|division|spore|tissue|other
  started_at: null
  completed_at: null
  method_ref: null
  operator_actor_ids: []
  quantity_class: null
  outcome_observation_ids: []
  derivative_specimen_ids: []
  derivative_seed_lot_ids: []
  provenance_inherited: true
  notes: null
```

Propagation is an institutional event, not a Minecraft growth event.

Successful propagation does not imply successful field establishment.

## 6. Seed-bank lot

```yaml
seed_bank_lot:
  seed_lot_id: null
  accession_id: null
  source_event_id: null
  parent_specimen_ids: []
  collected_at: null
  storage_asset_id: null
  storage_position_ref: null
  storage_condition_refs: []
  quantity_band: null
  viability_observation_ids: []
  sampling_history_ids: []
  duplicate_holding_ids: []
  restriction_refs: []
  current_state: stored
```

Suggested states:

- STORED
- UNDER_TEST
- PARTIALLY_USED
- DEPLETED
- TRANSFERRED
- VIABILITY_UNCERTAIN
- NONVIABLE_ASSESSED
- LOST
- DEACCESSIONED

`NONVIABLE_ASSESSED` is an institutional conclusion tied to evidence and method. It must not retroactively rewrite previous successful germination events.

## 7. Viability observation

```yaml
seed_viability_observation:
  observation_id: null
  seed_lot_id: null
  observed_at: null
  method_ref: null
  sample_size_ref: null
  raw_result_ref: null
  interpreted_band: null
  metrology_refs: []
  uncertainty_notes: []
  observer_ids: []
  evidence_refs: []
```

Possible qualitative bands:

- HIGH
- MODERATE
- LOW
- NOT_DETECTED_IN_SAMPLE
- UNKNOWN

Do not create universal real-world germination percentages unless an authored project requires them.

A test is destructive or non-destructive only when the chosen method says so.

## 8. Duplicate holding

```yaml
duplicate_holding:
  duplicate_id: null
  source_accession_id: null
  holding_institution_id: null
  transferred_material_ref: null
  transfer_event_id: null
  received_at: null
  local_accession_id: null
  relationship_state: active
  provenance_link_preserved: true
  restriction_refs: []
```

A duplicate is not a backup save. It can die, be mislabeled, diverge taxonomically or become unavailable independently.

## 9. Living-collection program

```yaml
living_collection_program:
  program_id: null
  institution_id: null
  purpose_tags: []
  accession_ids: []
  target_taxon_refs: []
  provenance_priorities: []
  duplication_strategy_refs: []
  research_use_refs: []
  education_use_refs: []
  conservation_use_refs: []
  public_display_refs: []
  risk_register_ids: []
  review_history_ids: []
```

Purpose tags may include RESEARCH, EDUCATION, CONSERVATION_BACKUP, HORTICULTURAL_RESEARCH, PUBLIC_DISPLAY, HISTORIC_COLLECTION, RESTORATION_SOURCE and CULTURAL_COLLECTION.

A collection can have several purposes at once.

## 10. Horticultural care

```yaml
horticultural_care_record:
  care_id: null
  specimen_or_collection_ref: null
  observed_at: null
  operator_ids: []
  observation_refs: []
  action_type: null
  material_input_refs: []
  water_service_refs: []
  climate_control_refs: []
  pest_management_refs: []
  followup_at: null
  outcome_refs: []
```

Candidate actions include watering, potting, pruning, support, propagation preparation, shade adjustment, relocation within the institution and monitoring.

Do not infer horticultural Skill checks or bonuses. PTU/Caelo authority is required where mechanics are invoked.

## 11. Collection risk

```yaml
living_collection_risk:
  risk_id: null
  institution_or_program_id: null
  risk_type: null
  affected_accession_ids: []
  observation_refs: []
  mitigation_ids: []
  duplicate_holding_ids: []
  current_state: monitored
```

Candidate risks:

- single-location concentration;
- greenhouse utility dependency;
- drought/water restriction;
- storm damage;
- wildfire exposure;
- pest/disease pressure;
- record/provenance loss;
- old age of key specimen;
- seed viability decline;
- staffing/knowledge loss;
- access pressure;
- unknown.

Risk is not a random-drama generator. It supports authored or causally valid consequences.

## 12. Taxonomy and labels

Taxonomy owns scientific determinations.

This layer stores which determination the accession currently uses and which label was shown at a given time.

```yaml
display_label_revision:
  label_revision_id: null
  specimen_or_bed_id: null
  effective_from: null
  effective_to: null
  displayed_name_ref: null
  provenance_summary_ref: null
  interpretation_ref: null
  public_access_state: null
  supersedes: null
```

An old label can be historically authentic and currently taxonomically outdated.

## 13. Wild-population handoff

Flora/Conservation remain authoritative for wild state.

Possible flow:

```text
wild population observation
→ authorized collection event
→ living accession / seed lot
→ propagation and curation
→ proposed restoration material
→ Conservation/Biosecurity review
→ restoration planting event
→ Flora recruitment/establishment monitoring
```

The botanical layer stops at the institutional holding and transfer. It does not write `ESTABLISHED` into the landscape.

## 14. Seed dispersal and Pokémon

Eldegoss, Combee, Flabébé/Floette/Florges, Comfey and other Pokémon may create authored ecological observations.

Hard boundaries:

- wind-dispersed seeds do not become accessioned automatically;
- a Pokémon carrying pollen or seeds does not establish source provenance automatically;
- Florges garden lore does not create healing;
- Flower Veil is a battle Ability, not horticultural protection;
- Honey Gather remains its exact mechanical rule, not garden productivity;
- a Pokémon helping staff must pass through Pokémon Agency / Working Pokémon and remains voluntary.

## 15. Biosecurity

Movement between institutions can require a Biosecurity handoff when canon defines risk or restrictions.

This layer records material identity and transfer intent.

Biosecurity decides whether movement is permitted and what introduced-status questions exist.

Do not infer that a botanic garden is exempt from ecological consequences.

## 16. Museums / herbarium handoff

When living material becomes a preserved voucher, fixed sample, historical label or other nonliving collection object, Museums/Archives owns that object.

The provenance graph should retain the accession link.

A living accession and a herbarium voucher can document the same collection event without being the same item.

## 17. Visitor / education boundary

Public display may include:

- interpreted beds;
- historic trees;
- glasshouses;
- research plots visible from paths;
- seed-bank exhibits distinct from actual stored material;
- seasonal flowering displays;
- plant/Pokémon observation stations.

Tourism owns visitor pressure. Education owns teaching programs. Public Memory owns remembered events.

A popular plant is not necessarily conservation-important; a conservation-important accession can remain off display.

## 18. Minecraft projection

Minecraft may render:

- planted beds;
- labeled specimens;
- glasshouses;
- nursery benches;
- seed-bank rooms;
- climate-control machinery;
- restricted research plots;
- seasonal appearance;
- empty spaces left after specimen loss;
- staff and visitors;
- persistent Pokémon when canon permits.

Minecraft must not own:

- accession identity;
- provenance;
- viability;
- propagation success;
- collection restrictions;
- conservation value;
- wild-population status;
- taxonomic truth;
- PTU Terrain or Status;
- spawn rarity.

Breaking or placing a plant block cannot directly create, clone, kill or deaccession a living accession.

## 19. Routine compression

Compress normal watering, routine stocktake and ordinary greenhouse care.

Surface the system when:

- provenance is missing or disputed;
- a significant accession changes condition;
- viability review alters a conservation plan;
- duplicate holdings matter after a loss;
- taxonomy changes the interpretation of a collection;
- a player chooses horticulture/research as a long-term project;
- utilities threaten a collection;
- a Pokémon relationship changes;
- public access conflicts with conservation/research needs;
- a restoration handoff creates a consequential choice.

The garden should often function normally without generating quests.

## 20. Encounter contract — Glasshouse Utility Failure

Narrative premise:

A major glasshouse loses part of its environmental-control system while staff are isolating vulnerable collections. A separate Pokémon confrontation blocks one access lane.

FULL version requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for moving staff, evacuation lanes or forced displacement;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL only when exact supported rules occur;
- terrain/weather/hazards/zones/reactions — BLOCKING if heat, broken glass, flooding, protected beds or equipment create tactical effects;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `WITHDRAW`, `PROTECT_STAFF`, `CLEAR_ROUTE`, `REACH_EXIT`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:

Staff enters safe mode, isolates utilities and moves vulnerable accessions before combat. AutoPTU receives one static safe arena with plants as non-mechanical scenery. After battle, Technology and this layer resolve collection losses or recovery from authoritative state.

## 21. Encounter contract — Seed Bank Transfer Chokepoint

Narrative premise:

A duplicate seed-bank lot is scheduled for transfer to a second institution while an unrelated encounter blocks the handoff route.

FULL version requires complete movement for a moving custodian/transfer objective, tactical AI for `PROTECT_CUSTODIAN`, `CLEAR_ROUTE` or `WITHDRAW`, and adapter/playback for the transfer state. Items remain PARTIAL if the container itself gains mechanics.

REDUCED version:

The seed lot remains outside the battle grid under custody. Players clear a static chokepoint. Supply Chains/Postal completes the physical transfer afterward. Battle success does not change viability or provenance.

## 22. Encounter contract — Storm-Damaged Conservation Nursery

Narrative premise:

A storm damages access around a conservation nursery. Staff must assess living accessions while wild Pokémon displaced by the storm use the same perimeter.

FULL version requires complete movement, tactical AI and adapter/playback. Terrain/weather/hazards/zones/reactions remains BLOCKING if floodwater, debris, glass or unstable structures are tactical.

REDUCED version:

Resolve storm state, staff movement and accession assessment outside battle. Freeze a dry stable area if conflict remains. No plant damage, water hazard or weather effect is invented inside AutoPTU.

## 23. Non-combat contract — Accession Provenance Review

A historic accession has conflicting labels and no surviving original field notebook.

Possible outputs include:

- provenance confirmed;
- provenance narrowed but uncertain;
- two plausible source histories retained;
- taxon revised while provenance remains unresolved;
- accession retained with uncertainty warning;
- deaccession review opened.

No battle is required and no Skill check is invented by this layer.

## 24. Permanent capability map

Current planning status from live AutoPTU-Java evidence:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING as a complete family
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter / playback — BLOCKING

Exact narrow reaction contracts do not promote the environment/reaction family as a whole.

## 25. Hard non-inferences

Do not infer:

- botanical garden -> Grassy Terrain;
- greenhouse -> Grass-type bonus;
- Florges garden -> healing zone;
- Comfey presence -> healing item production;
- Eldegoss -> institutional seed collector;
- Combee -> automatic Honey production;
- Flower Veil -> plant protection;
- Seed Sower -> overworld propagation;
- seed bank -> infinite seeds;
- viable seed -> guaranteed germination;
- germinated seed -> successful restoration;
- living collection -> wild population;
- rare accession -> rare Cobblemon spawn;
- plant block count -> collection size;
- bone meal -> propagation event;
- block destruction -> accession death;
- greenhouse climate control -> battle Weather;
- horticultural care -> HP recovery;
- collection staff role -> PTU Skill Rank or Feature.

## 26. New overworld blockers

- BOTANICAL_INSTITUTION_STATE
- LIVING_ACCESSION_IDENTITY
- ACCESSION_PROVENANCE_GRAPH
- LIVING_SPECIMEN_HISTORY
- PROPAGATION_EVENT_HISTORY
- SEED_BANK_LOT_STATE
- VIABILITY_OBSERVATION_HISTORY
- DUPLICATE_HOLDING_NETWORK
- COLLECTION_PROGRAM_STATE
- HORTICULTURAL_CARE_HISTORY
- LIVING_COLLECTION_RISK_REGISTER
- TAXONOMY_TO_ACCESSION_HANDOFF
- BIOSECURITY_TRANSFER_HANDOFF
- FLORA_CONSERVATION_REINTRODUCTION_HANDOFF
- MUSEUM_VOUCHER_HANDOFF
- AUTHORITATIVE_COLLECTION_TO_MINECRAFT_PROJECTION
- COLLECTION_TO_FROZEN_BATTLE_SNAPSHOT

## 27. Canon questions left open

- Which Ouros settlements have botanic gardens, arboreta, nurseries or seed banks at campaign start?
- Which institutions can collect wild plant material and under what authored authority?
- What plant taxa and historic accessions are already culturally or scientifically important?
- How much accession-level detail should be visible to normal players?
- Which collection records are public, research-only or sensitive because they reveal wild localities?
- How are duplicate holdings coordinated across regions?
- What storage technology exists for long-term seed banking?
- Which Pokémon have authored, voluntary horticultural roles?
- How does Ouros decide when an accession can become restoration source material?
- Does Caelo define any relevant horticultural, botanical, Survival, Pokémon Education, Researcher, Naturewalk, Berry or Feature mechanics?

No answer is assumed until canon/rules evidence exists.
