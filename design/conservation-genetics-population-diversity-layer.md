# Conservation genetics & population diversity layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

This layer tracks population-level genetic evidence and management history without turning genetics into a combat stat, rarity score, breeding-value score or hidden purity mechanic.

It sits between Conservation, Wild Collectives, Island Biogeography, Migration, Biosecurity, Taxonomy, Breeding/Lineage, Science, Museums/Collections and Research Ethics.

Breeding/Lineage remains responsible for known parentage and institutional breeding records. This layer is responsible for population-level evidence and assessments.

## Core separation

Keep these concepts separate:

- species/form identity;
- persistent individual identity;
- known pedigree/parentage;
- sampled genetic data;
- abundance estimate;
- effective breeding population estimate;
- relatedness assessment;
- diversity assessment;
- bottleneck/founder-effect hypothesis;
- gene-flow evidence;
- conservation interpretation;
- management action;
- PTU mechanical state.

A population can be numerous and still have a narrow founder history. A small population can retain meaningful diversity. Neither condition grants mechanical bonuses or penalties.

## Primary objects

### POPULATION_GENETICS_CASE

```yaml
population_genetics_case:
  case_id: null
  population_id: null
  species_or_taxon_ref: null
  geographic_scope_ids: []
  opened_at: null
  research_question: null
  sample_set_ids: []
  demographic_dataset_refs: []
  historical_baseline_refs: []
  assessment_revision_ids: []
  management_context_refs: []
  privacy_or_sensitivity_scope: restricted
  status: OPEN
```

This object never creates a new Pokémon species/form or changes battle data.

### GENETIC_SAMPLE_SET

```yaml
genetic_sample_set:
  sample_set_id: null
  case_id: null
  collection_window: null
  method_ref: null
  sampled_entity_ids_confirmed: []
  sampled_entity_ids_uncertain: []
  sample_count: null
  source_types: []
  lab_or_analysis_ref: null
  quality_notes: []
  representativeness_limits: []
  research_ethics_refs: []
  custody_refs: []
```

Possible source types may include non-invasive field samples, clinical samples used under permitted secondary-use rules, museum material or explicitly authorized research samples.

Do not invent sampling procedures, collection legality or invasive handling.

### POPULATION_DIVERSITY_ASSESSMENT

```yaml
population_diversity_assessment:
  assessment_id: null
  population_id: null
  valid_for_window: null
  sample_set_ids: []
  method_ref: null
  diversity_summary: UNKNOWN
  relatedness_summary: UNKNOWN
  effective_population_estimate: null
  uncertainty_notes: []
  comparison_population_ids: []
  historical_comparison_refs: []
  author_ids: []
  review_status: DRAFT
```

Prefer qualitative/banded summaries until Ouros canon defines what numerical detail is worth exposing.

### FOUNDER_EVENT

```yaml
founder_event:
  founder_event_id: null
  recipient_population_id: null
  source_population_ids: []
  candidate_individual_ids: []
  transferred_individual_ids: []
  release_event_refs: []
  date_range: null
  purpose: REINTRODUCTION | ASSISTED_COLONIZATION | RECOVERY | RESEARCH | UNKNOWN
  selection_basis_refs: []
  uncertainty_notes: []
```

A founder event is historical provenance. It does not imply that all descendants are known or that lineage is complete.

### GENE_FLOW_OBSERVATION

```yaml
gene_flow_observation:
  observation_id: null
  source_population_id: null
  recipient_population_id: null
  evidence_type: GENETIC | MOVEMENT_PLUS_GENETIC | PEDIGREE | UNKNOWN
  evidence_refs: []
  estimated_window: null
  confidence: LOW | MEDIUM | HIGH
  interpretation_notes: []
```

Migration observations alone can create a hypothesis of gene flow, but not confirmation.

### BOTTLENECK_ASSESSMENT

```yaml
bottleneck_assessment:
  assessment_id: null
  population_id: null
  proposed_window: null
  evidence_refs: []
  candidate_causes: []
  confidence: LOW | MEDIUM | HIGH
  alternative_explanations: []
  supersedes_assessment_id: null
```

`candidate_causes` may include historical exploitation, habitat fragmentation, founder event, disaster, disease, isolation or unknown. The Case system handles allegations when human misconduct is suspected.

## Reintroduction and recovery lifecycle

A population restoration project may move through:

BASELINE → SOURCE_ASSESSMENT → AUTHORIZATION → TRANSLOCATION/RELEASE → INITIAL_SURVIVAL → ESTABLISHMENT → RECRUITMENT → MULTI_GENERATION_MONITORING → REVIEW

Genetic evidence can enter at several stages.

A release is not automatically a successful reintroduction.
Establishment is not automatically long-term viability.
Abundance recovery is not automatically diversity recovery.

## Historical baselines

Museums, archives and older scientific material can revise what institutions believe about former population diversity.

Historical samples need their own provenance.

A later result such as `historical_diversity_higher_than_previously_estimated` changes the assessment. It never rewrites the historical world state or converts a surviving individual into a different species/form.

## Relationship to Breeding/Lineage

Breeding/Lineage can know exact parentage for institutional Eggs and offspring.

This layer must not assume that wild populations have full pedigrees.

Rules:
- a known family tree is not a population-genetic assessment;
- matching Egg Groups do not prove gene flow;
- PTU inheritance rules do not define wild-population allele frequencies;
- Nature, Ability, Moves and stats are not proxies for genetic diversity;
- rare mechanical traits are not automatically rare genetic variants in world state.

## Relationship to Island Biogeography

Island isolation can create a reason to investigate population structure.

It does not automatically mean inbreeding, low diversity, endemism or a bottleneck.

A stepping-stone island, ferry corridor or natural migration event may later matter because new immigrants are observed, but the genetic consequence remains an evidence question.

## Relationship to Migration and Road Ecology

Restored corridors can support movement between populations.

Movement does not automatically equal breeding contribution.

Suggested handoff:

`migration observation → candidate connectivity event → sampling/repeated observations → gene-flow assessment`

This lets a wildlife overpass, river corridor or restored wetland matter years later without granting immediate numerical bonuses.

## Relationship to Biosecurity

A newly arrived population may be native recolonization, deliberate reintroduction, accidental introduction or unauthorized release.

Biosecurity owns provenance/pathway questions for introductions. Conservation Genetics can later assess population structure if appropriate.

Do not use genetic similarity alone to decide legality or blame.

## Research ethics and sensitive data

Population genetics can expose sensitive locations and individual histories.

Possible restricted fields:
- nest/den coordinates;
- sample locations for threatened populations;
- known parentage of protected individuals;
- planned translocation routes;
- museum sample identifiers linked to sensitive sites.

Research Ethics owns consent/authorization for samples. Museums owns access to collection material. Identity and Pokémon Agency own persistent subject identity.

## Minecraft projection

Minecraft/Cobblemon may show:
- tagged research stations;
- observation blinds;
- sample-drop boxes;
- restored corridors;
- release-site infrastructure;
- seasonal notices;
- specific persistent Pokémon when authorized;
- public-facing population summaries.

Minecraft must never derive genetic truth from entity count, IV-like data, spawn rarity, visible family groups or nearby forms.

## Anti-exploit rules

Players must not be able to manufacture a diversity assessment by:
- repeatedly spawning/capturing/despawning Pokémon;
- moving captured Pokémon into a wild area;
- breeding large numbers of Eggs;
- releasing rare forms;
- editing Minecraft tags/names;
- manipulating encounter tables;
- farming one sample source indefinitely.

Sampling must reference persistent world entities/populations and valid research state.

## Encounter contracts

### Corridor Sampling Day — full version

Premise: a restored wildlife crossing appears to have connected two previously separated populations. Researchers need samples/observations while Pokémon continue moving through the corridor.

Mechanical dependencies:
- targeting/footprints/range/LoS: VERIFIED for any discrete battle;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING if wild actors must cross/withdraw during combat;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING for protected lanes or dynamic crossing effects;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for CROSS/WITHDRAW/PROTECT_SAMPLE objectives;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Reduced version: resolve wildlife passage and sampling before battle. If a confrontation occurs, freeze one legal arena away from the corridor. Genetic interpretation happens later from world-state evidence.

### Founder Release Perimeter — full version

Premise: a small authorized release group is entering restored habitat while an unrelated disturbance threatens the perimeter.

Full version needs complete movement, objective-aware AI and adapter/playback if released Pokémon must reach habitat exits without being treated as enemy combatants.

Reduced version: complete the physical release in world state, move released Pokémon outside the tactical grid, then resolve any independent combat around a static perimeter.

A battle victory cannot make the release genetically successful.

### Archive Sample Retrieval — reduced-first concept

Premise: a historical museum sample may revise the inferred baseline of a population.

Primary gameplay is archival/custody research. If conflict occurs during transport, the specimen remains outside the battle grid under custody rules.

This concept can run with VERIFIED targeting/base movement/core calculations/action economy/AI legality for the battle portion. Any escort/interception version remains dependent on complete movement and AI tactical policy.

## Capability boundary

Pass 143 does not promote any engine family.

Current live evidence supports VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

Current live evidence remains PARTIAL for:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

Current live evidence remains BLOCKING for:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

The Java engine may contain representative reaction/area-move slices. That does not verify the whole family.

## Canon questions

Before promotion, humans should decide:
- whether Ouros institutions perform genetic monitoring at all;
- what technology and terminology they use;
- which populations begin with known bottlenecks/founder histories;
- whether any reintroduction projects predate the player;
- what data is public versus sensitive;
- whether numerical genetic metrics are visible to players;
- whether wild-population pedigrees are ever tracked individually;
- how released/captive-bred Pokémon transition into wild population records;
- whether population genetics can ever influence management without becoming a breeding optimization game.

## Mechanical questions

Still require authoritative PTU/Caelo validation:
- Breeding and Egg Group rules;
- inheritance and offspring rules;
- Breeder/Hatcher/Researcher Features;
- capture/release/relocation mechanics;
- any Caelo conservation or population rules.

No genetic diversity stat, inbreeding penalty, breeding bonus, rarity bonus, spawn modifier, evolution trigger or combat modifier is proposed.