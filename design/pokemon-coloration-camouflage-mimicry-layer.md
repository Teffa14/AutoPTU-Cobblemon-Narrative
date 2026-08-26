# Ouros Pokémon Coloration, Camouflage & Mimicry Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon.
Date: 2026-08-26

## Purpose

This layer models persistent visual appearance strategies in Pokémon and other biological actors: background matching, disruptive patterning, masquerade, countershading, dynamic color change, conspicuous signals, false-target markings and uncertain visual resemblance.

It does not own species identity, Form changes, images, courtship, seasonal molt, territoriality or battle effects.

The core boundary is:

`physical appearance -> observed visual state -> context -> repeated observations -> functional hypothesis -> reviewed interpretation`

No step automatically creates a PTU mechanic.

## Authority boundaries

This layer owns:

- observed coloration/pattern state;
- context-specific resemblance;
- dynamic appearance-change observations;
- camouflage/mimicry functional hypotheses;
- visual-signal repertoire history;
- observer-detection context when the question is biological appearance rather than camera provenance;
- longitudinal revisions to those interpretations.

Other systems remain authoritative:

- Pokémon Agency: individual identity, custody, partnership, agency;
- Taxonomy: species/form determination;
- Evolution/Form: mechanical Form/evolution transitions;
- Seasonal Coverings: molt, shed and covering replacement;
- Visual Records: images, captures, derivatives and visual-identification claims;
- Courtship: reproductive-display interpretation;
- Care: health/welfare diagnosis;
- Social Learning: transmitted behavior;
- Spatial Ecology: range/territory interpretation;
- PTU engine: Stealth, Accuracy/Evasion, Abilities, Moves, Status and all combat effects.

## 1. Appearance profile

```yaml
pokemon_appearance_profile:
  appearance_profile_id: null
  pokemon_entity_id: null
  species_ref: null
  authored_baseline_ref: null
  current_revision_id: null
  established_at: null
  status: PROVISIONAL
```

The profile belongs to the persistent individual when individual history matters. Population-level patterns use a separate population assessment and never overwrite individuals.

## 2. Appearance observation

```yaml
appearance_observation:
  observation_id: null
  subject_ref: null
  observed_at: null
  location_id: null
  observer_actor_id: null
  visual_record_refs: []
  substrate_context: null
  light_context: null
  weather_context: null
  distance_band: null
  movement_state: null
  coloration_description: null
  pattern_description: null
  silhouette_description: null
  conspicuous_features: []
  confidence: null
  intervention_context_ref: null
```

Observations record what was visible. They do not encode purpose.

Candidate movement states:

- STILL
- SLOW_MOVEMENT
- ACTIVE_MOVEMENT
- DISPLAYING
- FEEDING
- RESTING
- WITHDRAWING
- UNKNOWN

## 3. Appearance-state revision

```yaml
appearance_state_revision:
  revision_id: null
  subject_ref: null
  effective_interval: null
  previous_revision_id: null
  observed_traits: []
  dynamic_change_state: STABLE
  evidence_refs: []
  confidence: null
```

Dynamic states:

- STABLE
- GRADUAL_SHIFT
- RAPID_SHIFT
- REVERSIBLE_SHIFT
- SEASONAL_RECURRING
- CONTEXT_DEPENDENT
- UNKNOWN

A shift can exist without being a Form change. If mechanical Form state changes, hand off to Evolution/Form.

## 4. Functional interpretation

```yaml
visual_function_assessment:
  assessment_id: null
  subject_or_population_ref: null
  appearance_revision_refs: []
  proposed_function: null
  context_scope: null
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  competing_assessment_ids: []
  status: UNRESOLVED
  reviewed_at: null
```

Candidate functions:

- BACKGROUND_MATCHING
- DISRUPTIVE_PATTERNING
- COUNTERSHADING
- MASQUERADE_OBJECT_RESEMBLANCE
- FALSE_TARGET_OR_DECOY_PATTERN
- WARNING_OR_DETERRENT_SIGNAL
- SOCIAL_SIGNAL
- COURTSHIP_RELATED_SIGNAL
- THERMAL_OR_PHYSIOLOGICAL_CORRELATE
- HEALTH_OR_CONDITION_CORRELATE
- UNKNOWN_OR_MULTIFUNCTIONAL

These values are interpretations. They are never direct battle tags.

## 5. Detection study

```yaml
visual_detection_trial:
  trial_id: null
  protocol_ref: null
  subject_ref: null
  observer_ref: null
  context_ref: null
  opportunity_window: null
  localized_at: null
  identified_at: null
  identity_confidence: null
  observer_prior_knowledge_ref: null
  result: null
```

Candidate results:

- NOT_LOCALIZED
- LOCALIZED_NOT_IDENTIFIED
- IDENTIFIED_TO_BROAD_GROUP
- IDENTIFIED_TO_SPECIES
- INDIVIDUAL_ID_PROPOSED
- INVALID_TRIAL

This makes a major distinction explicit: noticing something and knowing what it is are different outcomes.

No detection trial generates battle Accuracy/Evasion.

## 6. Mimicry / resemblance claim

```yaml
resemblance_claim:
  claim_id: null
  subject_ref: null
  model_or_background_ref: null
  resemblance_type: null
  basis_refs: []
  proposed_function: null
  origin_hypothesis: null
  status: PROVISIONAL
```

Candidate resemblance types:

- OBJECT_MASQUERADE
- SPECIES_RESEMBLANCE
- HUMAN_OBJECT_RESEMBLANCE
- SUBSTRATE_MATCH
- SHAPE_RESEMBLANCE
- PATTERN_RESEMBLANCE
- UNKNOWN

A resemblance can be real while its origin remains unknown.

Example: a Foongus may visibly resemble a Poké Ball while the historical/evolutionary explanation remains unresolved.

## 7. Visual signal episode

```yaml
visual_signal_episode:
  episode_id: null
  actor_ref: null
  recipients_observed: []
  start_at: null
  end_at: null
  signal_traits: []
  behavior_context_ref: null
  response_observation_refs: []
  proposed_function_refs: []
```

This object is useful for conspicuous coloration that appears during warning, social, courtship, territorial or unknown contexts.

Courtship remains authoritative if reproductive interpretation becomes the question.

## 8. Population-level assessment

```yaml
population_appearance_assessment:
  assessment_id: null
  population_ref: null
  interval: null
  sampled_individual_refs: []
  sample_effort_ref: null
  trait_distribution_summary: null
  habitat_context_ref: null
  interpretation_refs: []
  confidence: null
```

A handful of photographed individuals never defines the whole population.

Loaded Minecraft entities never define trait frequencies.

## 9. Longitudinal change

Long-term histories can record:

- urban development reducing background match;
- wildfire or vegetation succession changing substrate context;
- snow-duration changes altering seasonal mismatch windows;
- repeated use of a specific display substrate;
- individual color-change response under different contexts;
- public folklore that outlives its scientific support;
- newly available imaging methods changing observer detection rather than the Pokémon.

The state change belongs where the evidence supports it. A new camera does not create a new coloration state.

## 10. Key guardrails

### Appearance is not combat math

Never infer:

`camouflage -> +Evasion`

`background match -> Accuracy penalty`

`stillness -> invisible`

`masquerade -> surprise round`

`visual display -> Intimidate`

`bright colors -> Poisoned on contact`

`warning pattern -> fear/panic`

`concealment -> Stealth success`

Any exact PTU effect must come from an implemented Move, Ability, Item, Feature, Skill rule or other authoritative mechanic.

### Kecleon boundary

Kecleon's ecological hue change is world-state observation.

PTU/AutoPTU Color Change is a battle Ability that changes Type when triggered by a Move.

The two may coexist on the same individual but never call each other implicitly.

### Sudowoodo boundary

Tree masquerade does not grant invisibility, Grass typing, Naturewalk, Stealth rank or a custom detection DC.

### Taxonomy boundary

Unusual coloration does not prove:

- regional Form;
- new species;
- evolution;
- mutation;
- shiny-like mechanical state;
- illness.

Taxonomy, Evolution/Form and Care decide those questions.

### Minecraft boundary

Minecraft/Cobblemon may render an appearance revision already authorized by world state.

It must not derive biological truth from:

- skin/texture selected by a client;
- shader lighting;
- biome color;
- entity invisibility flag;
- outline/glow effects;
- resource-pack changes;
- render distance;
- mob pathfinding;
- particle state.

## 11. Handoffs

Visual Records receives links when an observation is supported by an image.

Taxonomy receives unusual-trait cases when identity/form classification is questioned.

Care receives possible condition-linked changes without diagnosis being assumed.

Courtship receives social/reproductive-display interpretations.

Seasonal Coverings receives changes caused by molt/coat replacement.

Social Learning receives behavior-linked visual strategies only if transmission is evidenced.

Public Memory receives folklore, famous appearances and outdated explanations.

## 12. Narrative design value

This layer supports mysteries where the answer is not necessarily a hidden attacker or supernatural effect.

Examples:

- the Pokémon was present in every photograph but was not recognized;
- an apparent new Form is ordinary dynamic coloration;
- a famous warning pattern has no demonstrated defensive function;
- urban renovation makes a formerly effective background match fail;
- two populations look different because observers sampled different substrates/times;
- an old guide correctly describes a pattern no longer common in the changed landscape.

The system should frequently produce revisions rather than revelations.

## 13. Canon status

No species-specific Ouros appearance behavior is canonized by this document.

Official Pokémon examples are research precedents only until Ouros population canon explicitly adopts them.

No mechanical camouflage rule is introduced.