# Ouros Taxonomy, Species Classification & Nomenclature Layer

Status: proposed systems design. Not established canon. Not PTU/Caelo rules authority.

## Purpose

Ouros needs to support genuine biological discovery without treating the Pokédex as omniscient or allowing narrative generation to invent mechanical Pokémon content.

This layer owns classification state around observed Pokémon and populations:

- species/form determinations;
- provisional classifications;
- taxon concepts and revisions;
- synonyms and historical names;
- uncertain or disputed identifications;
- specimen/observation determinations;
- institutional acceptance state;
- regional/common/local names;
- reference-library versions;
- crosswalks between old and current labels.

It does not own:

- the mechanical species/form definition used by AutoPTU;
- evolution eligibility or resolution;
- population ecology;
- individual Pokémon identity;
- scientific observations themselves;
- public media framing;
- museum custody;
- genetics mechanics;
- Fakemon creation.

## Authority boundary

```text
WORLD / POKÉMON AGENCY / ECOLOGY
  physical individual or population
          |
SCIENCE / FIELD SIGNS / PHOTO / SAMPLE
  observation and evidence
          |
TAXONOMY LAYER
  determination + concept + revision + names
          |
SCIENCE / ARCHIVES / CONSERVATION / BIOSECURITY
  interpretation and management use
          |
MEDIA / EDUCATION / PUBLIC MEMORY
  public presentation and actor knowledge
```

AutoPTU species/form keys remain mechanical authority whenever battle rules need species data.

## Core separation

Keep these entities distinct:

```text
pokemon_entity_id
population_id
observation_id
specimen_or_sample_id
taxonomic_determination_id
taxon_concept_id
taxon_revision_id
name_usage_id
mechanical_species_key
public_label
```

A change to one does not silently mutate the others.

Example:

A photograph from Year 2 is labeled “regional Diglett.” In Year 5, researchers determine that the photographed Pokémon belongs to a different species concept. The photo, location, timestamp and photographed individual remain unchanged. The determination gains a superseding revision. Historical copies can still display the old label with an annotation.

## 1. Taxon concept

A taxon concept is the persistent classification entity used by Ouros institutions.

```yaml
taxon_concept:
  taxon_concept_id: null
  concept_rank: species
  current_revision_id: null
  mechanical_species_key: null
  mechanical_form_key: null
  canon_status: proposed
  origin: canonical_content
  created_at: null
  retired_at: null
```

Suggested `concept_rank` values:

- species;
- form;
- population_group;
- unresolved_complex;
- higher_group;
- provisional_candidate.

Only authored/canonical content may bind a new concept to a new `mechanical_species_key` or `mechanical_form_key`.

Procedural discovery may create `provisional_candidate` records but cannot create battle mechanics.

## 2. Taxon revision

Taxonomy changes through append-only revisions.

```yaml
taxon_revision:
  taxon_revision_id: null
  taxon_concept_id: null
  revision_number: 1
  accepted_name_id: null
  parent_or_related_concept_ids: []
  relationship_claims: []
  diagnostic_summary: null
  evidence_ids: []
  institution_positions: []
  effective_from: null
  supersedes_revision_id: null
  status: active
```

Possible `status` values:

- proposed;
- under_review;
- institutionally_accepted;
- disputed;
- superseded;
- withdrawn;
- unresolved.

A revision never rewrites the evidence that existed before it.

## 3. Name usage

Names are persistent records with context.

```yaml
name_usage:
  name_usage_id: null
  taxon_concept_id: null
  display_name: null
  name_type: institutional
  language_or_region_id: null
  valid_from: null
  valid_to: null
  source_id: null
  status: current
  notes: null
```

Suggested name types:

- institutional;
- common;
- regional;
- local;
- historical;
- archival;
- provisional_field_name;
- superseded;
- mistaken_historical_usage.

Ouros does not need to import a real-world scientific nomenclatural code. Stable IDs matter more than Latin-style names.

## 4. Taxonomic determination

Every identification attaches to evidence rather than replacing it.

```yaml
taxonomic_determination:
  determination_id: null
  subject_type: observation
  subject_id: null
  proposed_taxon_concept_id: null
  proposed_revision_id: null
  determination_level: species
  confidence_state: moderate
  method_ids: []
  reference_set_ids: []
  determiner_actor_ids: []
  institution_id: null
  determined_at: null
  evidence_ids: []
  alternative_candidate_ids: []
  rationale_summary: null
  status: active
  supersedes_determination_id: null
```

Suggested `confidence_state` values:

- tentative;
- low;
- moderate;
- high;
- confirmed_against_authoritative_content;
- unresolved.

Do not encode confidence as “percent truth” unless a specific scientific method genuinely produces a meaningful probability and the project chooses to expose it.

## 5. Mechanical identity bridge

Taxonomy is not allowed to manufacture PTU content.

```yaml
mechanical_taxon_binding:
  taxon_concept_id: null
  mechanical_species_key: null
  mechanical_form_key: null
  source_dataset_revision: null
  authority_source: autoptu_or_project_canon
  verified_at: null
```

Rules:

- a canonical binding can drive battle setup;
- a provisional concept cannot;
- an unresolved local population uses the existing verified mechanical species/form if one exists;
- narrative differences remain world state until explicitly authored into mechanics;
- Generation 9 reference material is not automatically present in the current PTU dataset.

## 6. Form versus species

Regional/form identity needs an explicit relationship.

```yaml
form_relationship:
  form_taxon_concept_id: null
  base_species_concept_id: null
  relationship_type: canonical_regional_form
  source_id: null
  mechanical_binding_verified: false
```

Allowed relationship types should be authored, for example:

- canonical_regional_form;
- canonical_forme;
- canonical_sexual_dimorphism_if_mechanically_relevant;
- observed_population_variant;
- unresolved_variant;
- resemblance_only.

`observed_population_variant` and `unresolved_variant` do not create Types, stats, Moves, Abilities or evolution changes.

## 7. Resemblance and convergent classification

```yaml
resemblance_claim:
  claim_id: null
  subject_taxon_concept_id: null
  comparison_taxon_concept_id: null
  resemblance_dimensions: []
  evidence_ids: []
  proposed_explanation: null
  status: hypothesis
```

Possible dimensions:

- body_plan;
- coloration;
- movement;
- habitat_use;
- call;
- tracks;
- feeding_behavior;
- construction_behavior.

A resemblance claim is never a mechanical inheritance relationship.

## 8. Occurrence and determination history

Occurrence records remain tied to original evidence.

```yaml
occurrence_record:
  occurrence_id: null
  observation_id: null
  location_id: null
  observed_at: null
  original_determination_id: null
  current_preferred_determination_id: null
  historical_name_usage_ids: []
  media_ids: []
  specimen_or_sample_ids: []
  privacy_scope: null
```

This makes historical distribution maps reproducible.

If a species is split later, old occurrence records can be:

- reassigned with evidence;
- marked ambiguous;
- left at a broader concept;
- excluded from a specific population analysis without deleting them.

## 9. Reference set and identification method

```yaml
identification_reference_set:
  reference_set_id: null
  name: null
  revision: null
  reference_type: comparative_collection
  taxon_concept_ids: []
  geographic_scope_ids: []
  method_scope: []
  curator_ids: []
  limitations: []
  effective_from: null
```

Reference types can include:

- field_guide;
- museum_collection;
- photographic_archive;
- call_library;
- track_library;
- specimen_collection;
- molecular_reference_library;
- historical_pokedex_edition;
- institutional_expert_panel.

An incomplete reference set can yield a legitimate unresolved result.

## 10. Classification dispute

```yaml
taxonomy_dispute:
  dispute_id: null
  taxon_concept_ids: []
  question: null
  position_records: []
  shared_evidence_ids: []
  contested_evidence_ids: []
  unresolved_questions: []
  review_events: []
  current_state: open
```

Disagreement can persist for years.

The generator must not create corruption, rivalry or bad faith merely because two institutions classify evidence differently.

## 11. Split and merge history

Taxon concepts may be reinterpreted.

```yaml
taxonomy_change_event:
  change_event_id: null
  change_type: split
  source_concept_ids: []
  resulting_concept_ids: []
  effective_revision_ids: []
  rationale_claim_ids: []
  affected_dataset_ids: []
  affected_publication_ids: []
  migration_status: planned
```

Suggested change types:

- split;
- merge;
- reassignment;
- form_recognition;
- form_rejection;
- synonymization;
- correction_of_misidentification.

No change event modifies battle rules until mechanical bindings are reviewed separately.

## 12. Public Pokédex and field-guide projection

A public Pokédex is a presentation layer over current knowledge.

```yaml
pokedex_entry_projection:
  edition_id: null
  taxon_concept_id: null
  displayed_name_id: null
  classification_summary: null
  verified_observation_ids: []
  public_media_ids: []
  uncertainty_notes: []
  restricted_information_redacted: true
  mechanical_data_source: null
```

Rules:

- public entries may lag behind research;
- sensitive nesting coordinates remain governed by Conservation/Research Ethics;
- exact mechanical stats come from authoritative game content, not scientific inference;
- actor-owned Pokédex knowledge can differ from the institution's full archive.

## 13. Individual identity survives reclassification

A persistent Pokémon never receives a new entity ID merely because taxonomy changes.

```text
pokemon_entity_id = stable
species/form classification = revisable metadata around that entity
mechanical species/form = authoritative battle binding
```

Evolution remains owned by the Evolution layer. If an individual evolves, the same entity can legitimately change mechanical species through that governed process. Taxonomic reclassification alone does not trigger Evolution.

## 14. Population differentiation

Island Biogeography and ecology may discover local differences.

```yaml
population_differentiation_claim:
  population_ids: []
  difference_dimensions: []
  evidence_ids: []
  taxonomy_implication: none
  status: observed
```

Difference dimensions can include:

- activity timing;
- diet;
- call;
- migration;
- average morphology;
- coloration distribution;
- habitat preference;
- behavior around people.

The default implication is `none` until authored evidence/canon says otherwise.

## 15. Unknown and partially identified observations

Do not force species-level classification.

Valid outputs include:

- `UNKNOWN_POKEMON`;
- known family/group only;
- one of several candidate taxa;
- known species, unresolved form;
- known form, uncertain individual identity;
- evidence signal with no confirmed organism present.

This is especially important for tracks, calls, partial photographs, old specimens, eDNA-like signals and damaged archival records.

## 16. Archive integration

Archives and museums should preserve:

- original label;
- later determinations;
- catalog revisions;
- specimen/media identity;
- name history;
- publication history.

A museum exhibit can display a superseded historical label with a correction panel instead of silently replacing history.

## 17. Conservation and biosecurity integration

Management actions may need to proceed before taxonomy is fully resolved.

The system must distinguish:

```text
taxonomic uncertainty
management identity
operational precaution
canonical species truth
```

Example:

Two populations may be managed separately because evidence suggests ecological differences even while taxonomists still debate whether they are distinct species.

The converse is also possible: two differently named historical populations may later prove to be the same taxon without erasing their distinct management histories.

## 18. Minecraft/Cobblemon projection

Minecraft renders individuals/models and can expose a player-facing label.

Minecraft does not decide:

- species taxonomy;
- form recognition;
- whether a local variant is canonical;
- synonym history;
- whether two records refer to the same taxon;
- whether a specimen establishes a new species;
- whether a loaded entity proves regional presence.

If Cobblemon provides a species/form registry key, that key can support the mechanical bridge. It is not automatically the entire narrative taxonomy model.

## 19. Generation constraints

A generated taxonomic story must start from existing evidence or a real knowledge gap.

Valid triggers:

- conflicting determinations;
- unmatched specimen/sample;
- observation outside expected range;
- historical label with no current crosswalk;
- population difference documented repeatedly;
- public report of a “new species” needing verification;
- archive rediscovery;
- reference-library gap;
- field guide version mismatch.

Invalid trigger:

“The world has been quiet, so invent a new regional form.”

## 20. Hard non-inferences

Do not infer:

- resemblance -> kinship;
- same habitat -> same species;
- different habitat -> different species;
- color difference -> regional form;
- size difference -> new form;
- behavior difference -> mechanical Ability;
- local name -> separate taxon;
- new taxon concept -> new PTU species;
- taxonomic disagreement -> institutional hostility;
- rare observation -> rare species;
- one absence -> extirpation;
- one eDNA/scent/signal detection -> live Pokémon currently present;
- mechanical species key -> complete scientific knowledge;
- current accepted name -> erase historical names;
- reclassification -> change persistent Pokémon identity;
- museum label -> world truth;
- Pokédex entry -> omniscient knowledge;
- classification success -> XP/Skill/Feature reward unless PTU rules explicitly support it.

## 21. Example long-term loop

Year 1:
A field team records an unusual coastal Pokémon and provisionally files it under a familiar species.

Year 2:
A museum specimen from forty years earlier is rediscovered with the same morphology under another historical name.

Year 3:
Call recordings and habitat data show consistent differences from the familiar species.

Year 4:
Two institutions disagree about whether the population is a regional variant or separate species.

Year 5:
A canonical/authored review resolves the taxonomic question, or deliberately leaves it open.

Every observation remains usable under its original context. No PTU mechanics change unless a separate mechanical-content review authorizes them.

## 22. Implementation-facing blockers

Outside AutoPTU-Java:

- `TAXON_CONCEPT_REGISTRY`
- `TAXON_REVISION_HISTORY`
- `NAME_USAGE_HISTORY`
- `TAXONOMIC_DETERMINATION_HISTORY`
- `DETERMINATION_CONFIDENCE_STATE`
- `IDENTIFICATION_REFERENCE_SET_REGISTRY`
- `TAXONOMY_DISPUTE_STATE`
- `TAXONOMY_SPLIT_MERGE_HISTORY`
- `OCCURRENCE_DETERMINATION_CROSSWALK`
- `MECHANICAL_TAXON_BINDING`
- `POPULATION_DIFFERENTIATION_CLAIMS`
- `PUBLIC_POKEDEX_EDITION_STATE`
- `TAXONOMY_TO_ARCHIVES_HANDOFF`
- `TAXONOMY_TO_SCIENCE_HANDOFF`
- `TAXONOMY_TO_CONSERVATION_HANDOFF`
- `TAXONOMY_TO_BIOSECURITY_HANDOFF`
- `TAXONOMY_TO_COBBLEMON_PROJECTION`

## Mechanical gate

This layer creates no battle modifier.

If a taxonomic story produces combat, AutoPTU receives the already-authoritative mechanical species/form keys for the combatants. Uncertainty in what researchers call the Pokémon does not make the battle engine uncertain about the rules record used for that entity.

PTU/Caelo Skills, Researcher Features, Pokédex checks, identification checks or special information-gathering mechanics remain blocked until validated from the project's authoritative source corpus.