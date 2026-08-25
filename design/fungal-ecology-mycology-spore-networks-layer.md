# Fungal Ecology, Mycology & Spore Networks Layer — Pass 158

Status: PROPOSED SYSTEMS LAYER. Not canon.

## Purpose

This layer owns persistent fungal ecology in Ouros: fungal organism/colony identity, substrate associations, mycelial evidence, fruiting episodes, fungal surveys, samples, ecological-role assessments, spore observations and harvest observations.

It does not own:

- plant identity/condition: Flora;
- soil condition: Soil;
- decomposition process state: Decomposition;
- forest operations/deadwood management: Forest Management;
- interspecies effects: Interspecies Ecology;
- food safety/edibility: Food Safety and PTU Item rules;
- toxins/exposure: Toxicology;
- taxonomy publication authority: Taxonomy;
- access/harvest rights: Land Tenure / institutional authority;
- market listings: Markets;
- battle Status, Moves or Abilities: AutoPTU/PTU.

## Core evidence chain

`substrate/site state -> fungal observation -> candidate organism/colony link -> survey/sample -> identification/role assessment -> fruiting/history revision -> ecological/institutional handoff`

Never collapse this into `mushroom_seen = fungus_state_known`.

## Persistent objects

### FUNGAL_SYSTEM

```yaml
fungal_system:
  fungal_system_id: null
  system_kind: null
  spatial_scope_ref: null
  substrate_scope_refs: []
  taxon_claim_refs: []
  first_observed_at: null
  current_assessment_ref: null
  observation_refs: []
  sample_refs: []
  fruiting_episode_refs: []
  role_assessment_refs: []
  confidence: null
  source_refs: []
```

Candidate `system_kind` values:

- SINGLE_OBSERVED_FRUITING_PATCH
- PERSISTENT_LOCAL_COLONY_CANDIDATE
- ROOT_ASSOCIATED_SYSTEM
- WOOD_DECAY_SYSTEM
- SOIL_OR_LITTER_SYSTEM
- HOST_ASSOCIATED_SYSTEM
- CULTIVATED_SYSTEM
- UNKNOWN

A `FUNGAL_SYSTEM` is an evidence object. It does not claim that all visible fruiting bodies share one genetic individual unless evidence supports that interpretation.

### FUNGAL_OBSERVATION

```yaml
fungal_observation:
  observation_id: null
  fungal_system_ref: null
  observed_at: null
  observer_refs: []
  location_ref: null
  substrate_ref: null
  observation_kind: null
  visible_extent: null
  fruiting_body_count_band: null
  developmental_state: null
  environmental_context_refs: []
  media_refs: []
  sampling_effort_ref: null
  notes: null
  confidence: null
```

Possible `observation_kind` values include:

- FRUITING_BODY
- MYCELIAL_OR_HYPHAL_EVIDENCE
- ROOT_ASSOCIATION
- WOOD_DECAY_SIGN
- SPORE_DEPOSITION
- CULTURE_OR_LAB_OBSERVATION
- MOLECULAR_OR_OTHER_SAMPLE_RESULT
- HOST_ASSOCIATION
- NOT_DETECTED

`NOT_DETECTED` must preserve effort and method.

### FRUITING_EPISODE

```yaml
fruiting_episode:
  fruiting_episode_id: null
  fungal_system_ref: null
  began_or_first_detected_at: null
  ended_or_last_detected_at: null
  spatial_extent_ref: null
  observed_abundance_band: null
  observation_refs: []
  weather_context_refs: []
  substrate_state_refs: []
  disturbance_context_refs: []
  interpretation_refs: []
  confidence: null
```

A fruiting episode is visible reproductive activity, not the birth/death of the underlying system.

### FUNGAL_SAMPLE

```yaml
fungal_sample:
  sample_id: null
  source_observation_ref: null
  fungal_system_ref: null
  collected_at: null
  collection_method_ref: null
  material_kind: null
  substrate_or_host_ref: null
  custody_refs: []
  analysis_refs: []
  remaining_material_state: null
  authorization_ref: null
  source_refs: []
```

Research Ethics, Museums/Collections or Botanical Gardens may become downstream authorities depending on context.

### ECOLOGICAL_ROLE_ASSESSMENT

```yaml
ecological_role_assessment:
  assessment_id: null
  fungal_system_ref: null
  scope_ref: null
  role_claims: []
  evidence_refs: []
  alternative_interpretation_refs: []
  confidence: null
  reviewed_at: null
  supersedes_assessment_id: null
```

Candidate role claims:

- SAPROTROPHIC_ASSOCIATION
- MYCORRHIZAL_ASSOCIATION
- PATHOGENIC_ASSOCIATION
- ENDOPHYTIC_OR_OTHER_SYMBIOTIC_ASSOCIATION
- FOOD_RESOURCE_ASSOCIATION
- SPORE_VECTOR_RELATIONSHIP
- UNKNOWN

These are scoped claims, not immutable species labels.

### SPORE_OBSERVATION

```yaml
spore_observation:
  spore_observation_id: null
  candidate_source_refs: []
  observed_at: null
  location_ref: null
  method_ref: null
  medium_ref: null
  concentration_or_abundance_band: null
  taxon_or_identity_claim_refs: []
  exposure_case_refs: []
  later_growth_refs: []
  confidence: null
```

A spore observation does not imply PTU `Spore`, `Effect Spore`, Sleep, Poisoned or Paralysis.

### FUNGAL_HARVEST_OBSERVATION

```yaml
fungal_harvest_observation:
  harvest_observation_id: null
  fungal_system_ref: null
  occurred_at: null
  actor_refs: []
  location_ref: null
  material_removed_ref: null
  quantity_band: null
  authorization_ref: null
  purpose_claim: null
  destination_refs: []
  later_ecological_observation_refs: []
```

This records removal. It does not decide whether the harvested material is a PTU Mushroom Item, safe food or legal market stock.

## Identity and uncertainty rules

Visible mushrooms can belong to one system, several systems or an unresolved set. Keep `POSSIBLE_SAME_SYSTEM`, `LIKELY_SAME_SYSTEM`, `CONFIRMED_LINK` and `UNRESOLVED` distinctions if the campaign needs them.

A known patch can stop fruiting and remain historically present. A later patch nearby does not automatically inherit the same identity.

Taxonomic re-identification updates a determination/claim, not the original observation.

## Fruiting, seasonality and climate

Seasonality/Climate owns recurring environmental timing and long-term change. Fungal Ecology owns observed fruiting history.

Allowed handoff:

`weather/season context -> fungal observation -> repeated fruiting history -> scientific interpretation`

Forbidden handoff:

`rain happened -> mushrooms spawn`.

No rare-spawn modifier should be generated from this layer.

## Substrate and decomposition handoff

Decomposition owns the physical decomposition state. Fungal Ecology may observe a fungus associated with a log, litter, carcass-associated substrate or other organic material.

Do not infer decomposition rate from a mushroom model alone.

Likewise, a visible conk on timber can trigger a Forestry/Architecture inspection without declaring the structure unsafe.

## Mycorrhizal handoff

Flora owns the plant and its condition. Soil owns soil state. Fungal Ecology owns evidence for the association.

Use:

`root/site observation -> sample/assessment -> scoped association claim -> later plant/soil comparison`.

Do not use:

`mushroom near tree -> tree receives buff`.

## Host-associated Pokémon fungi

Paras/Parasect-style relationships must be authored from species/canon evidence. Store:

```yaml
pokemon_fungal_association:
  association_id: null
  pokemon_entity_ref: null
  fungal_system_ref: null
  relationship_kind: null
  observation_refs: []
  species_basis_ref: null
  state_revision_refs: []
  confidence: null
```

This world-state record never replaces the Pokémon's PTU Ability, Move, Type, HP or Status.

## Minecraft projection

Minecraft/Cobblemon may render:

- mushroom/fungus blocks;
- decayed substrates;
- colored particles where presentation is appropriate;
- survey markers;
- collection signs;
- seasonal visible fruiting patches.

It may not determine:

- organism identity;
- fruiting history;
- mycelial extent;
- edibility;
- toxicity;
- taxonomic identity;
- PTU Item identity;
- Status application;
- spawn rates;
- population abundance;
- ecological function.

Block removal does not erase Chronicle history. Chunk reload does not restore an old fruiting revision.

## Encounter contracts

### Fruiting Chamber Survey

Narrative premise: a cave chamber that has been surveyed for years produces an unusually extensive fruiting event after a hydrological change. Researchers need samples and route access while resident Pokémon respond to disturbance.

FULL version may require:

- complete movement for technicians/Pokémon withdrawing or crossing within the grid;
- terrain/weather/hazards/zones/reactions only if spores, slick substrate, darkness or cave conditions have verified tactical rules;
- status lifecycle and move-specific behavior if an actual Pokémon uses Spore or another Status Move;
- abilities if Effect Spore/Illuminate or another exact Ability matters;
- AI tactical policy for `WITHDRAW`, `PROTECT_SAMPLE_ROUTE`, `CLEAR_ROUTE`, `REACH_EXIT`;
- adapter/playback for researchers, sample points and semantic objectives.

REDUCED version: sampling and any exposure decision happen in world state first. Researchers leave the chamber. The battle, if one remains, uses a static dry/clear arena with no ambient spore effect. Exact Pokémon Moves/Abilities are allowed only when current runtime evidence verifies them.

### Deadwood Plot Disturbance

Narrative premise: a long-running forest study loses access when visitors enter a retained-deadwood plot during a major fruiting week and wild Pokémon begin using the same space.

FULL version depends mainly on complete movement, tactical AI and adapter/playback for non-hostile withdrawal/crowd clearing. Environmental mechanics are optional and must be verified individually.

REDUCED version resolves visitors and wildlife movement outside battle, then opens a conventional static confrontation only if an independent threat remains.

### Orchard Root Association Survey

Narrative premise: an orchard's declining section also shows a changed fungal community. Several explanations remain plausible: root association change, irrigation, soil state, crop pressure or unrelated seasonal fruiting.

This is primarily a non-combat investigation using Flora, Soil, Irrigation, IPM, Science, Metrology and Fungal Ecology. A battle result cannot establish causation.

### Harvest Closure Dispute

Narrative premise: a famous seasonal mushroom patch has poor visible fruiting for a second year. A community harvest tradition, commercial buyers and conservation staff disagree over whether a temporary closure is justified.

This can remain fully non-combat. Land Tenure, Markets, Public Memory, Science and Fungal Ecology own the relevant decisions. A closure never proves fungal decline; poor fruiting never proves organism loss.

## Engine non-inferences

Do not infer:

- `Spore` Move from ambient spores;
- `Effect Spore` from touching a fungal block;
- Sleep/Poisoned/Paralysis from a fruiting chamber;
- powder Move geometry from particle clouds;
- Illuminate from bioluminescent scenery;
- Grassy Terrain from fungal abundance;
- Rough Terrain from mushrooms;
- cover from shelf fungi;
- healing from mycorrhizae;
- damage from decomposition;
- fungal infection from Parasect presence;
- PTU mushroom Item identity from harvested world objects.

## Canon questions reserved

- Which fungal systems are known at campaign start?
- Does Ouros maintain a formal mycological institute, herbarium/fungarium or only local expertise?
- Which species have authored fungal relationships beyond official Pokémon precedent?
- Which wild fungi are culturally harvested, cultivated or protected?
- How much mycelial/soil sampling technology exists regionally?
- Are any fungal hazards authored in setting canon, and if so what exact PTU/Caelo mechanics govern them?
- How are PTU mushroom Items acquired/identified in the final ruleset?

Until those are approved, this layer stays PROPOSED and evidence-first.
