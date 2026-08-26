# Pokémon Courtship, Mate Choice & Pair Formation Layer

Status: PROPOSED SYSTEMS DESIGN / NON-CANON
Pass: 179

## Purpose

This layer owns observed and assessed reproductive-social behavior before a Wild Nesting episode or authoritative PTU/Caelo breeding transaction exists.

It answers questions such as:

- did a persistent Pokémon perform a display toward another individual?
- was the interaction reciprocal, tolerated, ignored, interrupted or followed by withdrawal?
- did the same individuals repeatedly associate across days, seasons or years?
- did a pair-like association form, persist, dissolve or remain uncertain?
- did a display site remain important after the original participants disappeared?
- did a public festival or research program observe the same display tradition without proving mating or parentage?

It must not determine breeding eligibility, mating success, Eggs, parentage, Infatuation, mechanical Attraction, gender, permanent monogamy or capture eligibility.

## Authority boundary

Use this chain:

`signal / approach observation -> display episode -> response observation -> repeated association evidence -> pair-formation assessment -> continuity / dissolution review -> optional handoff to Wild Nesting or Breeding mechanics`

Existing authorities remain authoritative:

- Pokémon Agency: persistent individual identity, custody, partnership, release and agency.
- Wild Collectives: group identity and persistent social organization.
- Breeding/Egg/Nursery: PTU/Caelo breeding resolution, Egg state, custody, hatch and mechanically established lineage.
- Wild Nesting / Parental Care / Juvenile Dispersal: reproductive sites, nesting episodes, Eggs/young, caregiver observations, dependency and dispersal.
- Seasonality: recurring phenology and seasonal windows.
- Spatial Ecology: home range, site fidelity, overlap and territoriality.
- Soundscapes / Passive Acoustics: acoustic evidence.
- Olfactory Landscapes: scent evidence.
- Lightscapes / Visual Records: light and visual-display evidence.
- Social Learning: transmission of learned display traditions when evidence supports it.
- Research Ethics: intrusive observation, playback, baiting, handling and study design.
- Conservation: access, disturbance controls and management decisions.
- PTU / AutoPTU: mechanical Attract, Infatuation, Skills, Moves, Abilities and battle consequences.
- Minecraft/Cobblemon: visible presentation after authoritative world state exists.

## Core non-equivalences

`COURTSHIP DISPLAY != MATING`

`MATING OBSERVATION != EGG`

`PAIR ASSOCIATION != GENETIC PARENTAGE`

`PAIR ASSOCIATION != PERMANENT MONOGAMY`

`REPEATED PROXIMITY != PAIR FORMATION`

`WITHDRAWAL != HOSTILITY`

`DISPLAY SITE != TERRITORY`

`PTU INFATUATION != COURTSHIP`

`ATTRACT MOVE != MATE CHOICE`

`BEAUTY / CUTE STAT != REPRODUCTIVE PREFERENCE`

## Primary entities

### COURTSHIP_BEHAVIOR_PROFILE

Persistent analytical container for an individual, pair candidate set or local population.

```yaml
courtship_behavior_profile:
  courtship_profile_id: null
  subject_pokemon_entity_ids: []
  species_refs: []
  population_ref: null
  temporal_scope_ref: null
  seasonal_context_ref: null
  spatial_context_refs: []
  display_site_refs: []
  display_episode_refs: []
  pair_formation_assessment_refs: []
  pair_continuity_refs: []
  signal_channel_refs: []
  disturbance_context_refs: []
  research_program_refs: []
  canon_status: proposed
```

This profile is descriptive. It is not a stat block.

### DISPLAY_SITE

A persistent place where courtship-like or pair-maintenance displays have been observed.

```yaml
display_site:
  display_site_id: null
  geometry_ref: null
  site_type: OPEN_GROUND | WATER_EDGE | CANOPY | CAVE | RIDGE | URBAN_SITE | OTHER
  first_observed_at: null
  last_observed_at: null
  site_revision_refs: []
  associated_pokemon_entity_ids: []
  associated_population_refs: []
  evidence_refs: []
  public_access_state_ref: null
  conservation_state_ref: null
  confidence: provisional
```

A site can remain important after specific participants stop using it.

A display site is not automatically a nesting site or territory.

### DISPLAY_EPISODE

One bounded observed sequence.

```yaml
display_episode:
  display_episode_id: null
  observed_at_start: null
  observed_at_end: null
  location_ref: null
  actor_pokemon_entity_ids: []
  receiver_candidate_ids: []
  signal_channels: [VISUAL]
  behavior_sequence_refs: []
  audience_or_competitor_refs: []
  disturbance_context_ref: null
  observer_or_device_refs: []
  recording_refs: []
  interpretation_state: UNINTERPRETED
  confidence: null
```

Possible signal channels:

- visual posture or movement;
- light;
- sound;
- scent/chemical;
- object presentation;
- site preparation;
- coordinated movement;
- mixed/unknown.

Signal channels remain linked to their evidence authorities.

### COURTSHIP_INTERACTION_OBSERVATION

Stores concrete behavior rather than a conclusion.

```yaml
courtship_interaction_observation:
  observation_id: null
  display_episode_id: null
  actor_pokemon_entity_id: null
  target_or_context_ref: null
  behavior: APPROACH | DISPLAY | FOLLOW | PARALLEL_MOVE | PRESENT_OBJECT | CALL | SCENT_SIGNAL | LIGHT_SIGNAL | TOUCH | RETREAT | IGNORE | INTERRUPT | OTHER
  observed_at: null
  source_refs: []
  confidence: null
```

Terms are descriptive categories. They do not prove intent.

### RESPONSE_OBSERVATION

```yaml
response_observation:
  response_id: null
  preceding_observation_ref: null
  responder_pokemon_entity_id: null
  response: APPROACH | REMAIN | RECIPROCAL_DISPLAY | FOLLOW | WITHDRAW | IGNORE | INTERRUPTED | UNKNOWN
  latency_band: null
  source_refs: []
  disturbance_context_ref: null
  confidence: null
```

A response is not a preference score.

### DISPLAY_FUNCTION_ASSESSMENT

Interpretation of what a recurring display may be doing.

```yaml
display_function_assessment:
  assessment_id: null
  display_episode_refs: []
  candidate_functions:
    courtship: POSSIBLE
    pair_maintenance: POSSIBLE
    territorial: POSSIBLE
    social_coordination: POSSIBLE
    unknown_other: POSSIBLE
  assessment_state: UNRESOLVED
  evidence_for_refs: []
  evidence_against_refs: []
  assessor_ref: null
  confidence: null
  supersedes_assessment_id: null
```

Multiple functions can remain plausible simultaneously.

### PAIR_FORMATION_ASSESSMENT

A cautious assessment that two persistent individuals formed a pair-like association for a bounded period.

```yaml
pair_formation_assessment:
  pair_assessment_id: null
  pokemon_entity_ids: []
  assessment_window_ref: null
  repeated_association_refs: []
  reciprocal_behavior_refs: []
  shared_site_refs: []
  separation_or_withdrawal_refs: []
  state: POSSIBLE | PROBABLE | ESTABLISHED_FOR_SCOPE | NOT_SUPPORTED | UNRESOLVED
  reproductive_outcome_state: UNKNOWN
  parentage_state: UNKNOWN
  confidence: null
  assessor_ref: null
```

`ESTABLISHED_FOR_SCOPE` means only that the pair-like association is sufficiently supported for that period.

It does not mean lifetime bond, mating, parentage or exclusive pairing.

### PAIR_CONTINUITY_REVIEW

```yaml
pair_continuity_review:
  review_id: null
  prior_pair_assessment_id: null
  review_window_ref: null
  reobservation_refs: []
  association_state: CONTINUED | INTERRUPTED | DISSOLVED_OBSERVED | NOT_REOBSERVED | REFORMED_POSSIBLE | UNKNOWN
  separation_context_refs: []
  migration_context_refs: []
  nesting_context_refs: []
  confidence: null
```

`NOT_REOBSERVED` is not `DISSOLVED`.

### COURTSHIP_SITE_TRADITION_ASSESSMENT

Optional bridge for repeated local displays that persist across individuals or generations.

```yaml
courtship_site_tradition_assessment:
  assessment_id: null
  display_site_id: null
  population_ref: null
  repertoire_revision_refs: []
  cross_cohort_evidence_refs: []
  social_learning_handoff_ref: null
  state: REPEATED_LOCAL_PATTERN | TRANSMISSION_POSSIBLE | TRADITION_SUPPORTED | UNRESOLVED
```

Social Learning remains authoritative for actual transmission claims.

## Courtship, mating and nesting boundary

This layer can record `MATING_BEHAVIOR_OBSERVED` only when an authored observer or source clearly supports that literal behavior and Research Ethics permits storing it.

Even then:

- it does not create an Egg;
- it does not establish genetic parentage;
- it does not determine PTU breeding compatibility;
- it does not determine offspring species, Ability, Nature, Moves, gender or hatch timing.

If a later wild nesting episode appears, Wild Nesting creates that episode from its own evidence.

If a Trainer-directed breeding transaction occurs, Breeding/Egg/Nursery resolves it through PTU/Caelo rules.

## Pair-bond privacy and agency

For partnered or formerly partnered Pokémon, pair-association observations do not transfer authority to a Trainer.

Never infer:

- Trainer permission to breed;
- Trainer ownership of wild partners or offspring;
- obligation to remain near a former Trainer;
- Loyalty change from joining or leaving a pair association;
- capture eligibility because an individual is alone;
- abandonment because one member disappears temporarily.

## Signal evidence

### Acoustic

Calls remain Soundscape/Passive Acoustic records. Playback used during research must be recorded as an intervention because it can alter behavior.

### Olfactory

Scent remains Olfactory Landscape evidence. Species lore such as Illumise/Volbeat does not create a generic attraction radius.

### Visual/light

Photography and Lightscape preserve image/light provenance. A light sequence can support a display assessment without becoming a move effect or battle zone.

### Objects and structures

Objects presented, moved or arranged during display retain Material Culture identity where appropriate. A display court or constructed structure may overlap with Cognition/Tool Use or Spatial Ecology.

## Disturbance and interrupted choice

Courtship behavior can change because of:

- observers;
- tourists;
- predators;
- competing signallers;
- construction;
- artificial light;
- noise;
- altered scent fields;
- weather;
- habitat change;
- migration timing;
- illness or injury;
- individual absence;
- research playback or baiting.

An interrupted episode records the interruption. It must not be labeled rejection unless the evidence supports that narrower conclusion.

## Public festivals and cultural observation

A settlement may celebrate a recurring display season without knowing or controlling reproductive outcomes.

Useful world-state objects can include:

```yaml
public_display_event:
  event_id: null
  display_site_id: null
  scheduled_window_ref: null
  public_viewing_area_ref: null
  conservation_buffer_ref: null
  tourism_state_ref: null
  actual_display_observation_refs: []
  cancellation_reason_ref: null
  public_memory_refs: []
```

The festival can continue even in a year when the display is late, reduced or absent.

## PTU mechanics boundary

PTU 1.05 has explicit mechanics for Attract and Infatuation.

Those mechanics are battle/rules state.

This layer never writes `Infatuated` because two Pokémon display toward one another.

Likewise:

- `Cute Charm` is an Ability, not mate-choice ecology;
- `Oblivious` is a battle Ability, not proof an individual never forms reproductive associations;
- `Cute` or `Beauty` Contest values do not become mate-choice weights;
- Charm does not become a wildlife mating roll;
- `Attract` does not establish a persistent relationship after battle unless a separate narrative observation supports one.

## Minecraft/Cobblemon projection

Allowed direction:

`authoritative courtship state -> optional animations / particles / pathing / visible gatherings`

Forbidden reverse direction:

`two entities near each other -> pair formed`

`heart particles -> mating`

`Minecraft breeding hearts -> PTU breeding resolved`

`entity following -> preference`

`despawn -> rejection / pair dissolution`

`same spawn cluster -> family`

Any Cobblemon breeding or daycare capability must hand off to PTU/Caelo mechanics before it changes Ouros lineage state.

## Long-term Chronicle value

Courtship can create durable history without producing offspring every time.

A display site can:

- shift after vegetation growth;
- become quieter after a road closes;
- become famous through tourism;
- lose a landmark used during approach;
- persist after original participants disappear;
- change repertoire after social learning;
- be protected after repeated disturbance;
- become scientifically reinterpreted years later;
- stop being used and later recover.

Pair histories can similarly change without tragedy:

- seasonal reunion;
- temporary separation;
- one member taking a different migration route;
- pair association ending;
- later re-association;
- a persistent individual pairing with another partner;
- incomplete evidence during unobserved years.

## Canon guardrails

Until canon approves specific populations or institutions:

- no species is assigned a universal mating system;
- no individual receives a permanent mate preference profile;
- no pair is assumed exclusive;
- no display is assumed sexual;
- no festival is established as existing;
- no nesting result is inferred;
- no breeding season is invented;
- no PTU mechanic is triggered by narrative behavior;
- no modern gender/sexuality assumptions are projected onto Pokémon behavior beyond mechanically established data needed by the rules.

## Recommended initial implementation

Implement this as narrative/world state first.

The minimum useful version needs:

- persistent display sites;
- display episodes;
- concrete approach/response observations;
- pair-formation assessments with uncertainty;
- continuity reviews;
- handoffs to existing evidence systems;
- zero automatic mechanical consequences.

That gives Ouros seasonal callbacks, recognizable wild individuals and richer ecological stories without creating another breeding subsystem.