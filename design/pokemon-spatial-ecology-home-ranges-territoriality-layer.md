# Pokémon Spatial Ecology, Home Ranges, Site Fidelity & Territoriality Layer

Status: PROPOSED SYSTEMS DESIGN / NON-CANON
Pass: 176

## Purpose

This layer owns derived local spatial-use state for wild or released persistent Pokémon, pairs, populations and collectives when the movement is not itself a migration episode.

It exists to answer questions such as:

- what area has this individual repeatedly used during a defined period?
- which places receive disproportionate use?
- did the same Pokémon return to a site in later seasons or years?
- do two assessed use areas overlap?
- is there evidence that part of a range is actively defended?
- was an unusual observation a short excursion or the beginning of a persistent range shift?

It must not create invisible territory walls, omniscient tracking, universal aggression or battle mechanics.

## Authority boundary

Use this chain:

`observation evidence -> spatial-use assessment -> core-use assessment -> site-fidelity comparison -> overlap/territoriality assessment -> revision -> downstream consequence`

Existing authorities remain authoritative:

- Pokémon Agency: persistent individual identity, custody, partnership, release and agency.
- Wild Collectives: collective identity and social organization.
- Wildlife Migration: migration patterns, episodes, corridors and stopovers.
- Wild Nesting / Juvenile Dispersal: reproductive sites, dependency and natal dispersal.
- Urban Wildlife: synanthropy, attractants, urban conflict and coexistence.
- Telemetry: devices, detections, fixes and movement segments.
- Field Signs: tracks, marks, scent evidence and other physical traces.
- Soundscapes / Passive Acoustics: calls, recordings and acoustic detections.
- Photography / Community Science / Remote Sensing: their own evidence records.
- Land Tenure: human boundaries, property, access and use rights.
- Conservation: management objectives and interventions.
- PTU/AutoPTU: battle legality and mechanics.

This layer consumes evidence from those systems. It cannot rewrite them.

## Core non-equivalences

`HOME RANGE != TERRITORY`

`CORE USE AREA != HOME RANGE`

`SITE FIDELITY != CONTINUOUS RESIDENCE`

`RANGE OVERLAP != SOCIAL RELATIONSHIP`

`TERRITORIALITY != OWNERSHIP`

`EXCURSION != RANGE SHIFT`

`OBSERVED RANGE != COMPLETE RANGE`

## Primary entities

### `SPATIAL_USE_PROFILE`

Persistent analytical container for one subject and one meaningful life/history period.

Suggested fields:

```yaml
spatial_use_profile:
  spatial_use_profile_id: null
  subject_type: INDIVIDUAL
  pokemon_entity_ids: []
  collective_refs: []
  population_refs: []
  species_refs: []
  temporal_scope_ref: null
  life_stage_context_ref: null
  migration_context_ref: null
  nesting_context_ref: null
  urban_context_ref: null
  home_range_revision_refs: []
  core_use_revision_refs: []
  site_fidelity_assessment_refs: []
  overlap_assessment_refs: []
  territoriality_assessment_refs: []
  excursion_refs: []
  range_shift_review_refs: []
  evidence_summary_refs: []
  canon_status: proposed
```

A profile is not a Pokémon stat.

### `HOME_RANGE_ASSESSMENT_REVISION`

A versioned estimate of routine space use during a bounded period.

```yaml
home_range_assessment_revision:
  revision_id: null
  spatial_use_profile_id: null
  valid_observation_window: null
  geometry_ref: null
  geometry_type: COARSE_POLYGON
  estimation_method_ref: null
  source_observation_refs: []
  source_telemetry_fix_refs: []
  effort_and_coverage_refs: []
  sample_size_band: null
  coverage_gaps: []
  uncertainty_ref: null
  confidence: provisional
  supersedes_revision_id: null
  reviewer_refs: []
```

The geometry is analytical. It is not a barrier.

Old revisions remain historically valid for the evidence available at that time.

### `CORE_USE_AREA_REVISION`

Represents locations receiving disproportionate repeated use within a wider assessment.

```yaml
core_use_area_revision:
  core_use_revision_id: null
  spatial_use_profile_id: null
  home_range_revision_id: null
  geometry_refs: []
  associated_site_refs: []
  recurring_resource_refs: []
  roost_or_den_refs: []
  observation_basis_refs: []
  seasonal_or_diel_context_refs: []
  confidence: null
```

A core-use area may surround food, shelter, a roost, water, a mate/collective, a nesting site or an unknown driver. Do not invent the driver from geometry alone.

### `SITE_FIDELITY_ASSESSMENT`

Compares repeated use of a place across meaningful periods.

```yaml
site_fidelity_assessment:
  assessment_id: null
  subject_ref: null
  site_ref: null
  comparison_period_refs: []
  confirmed_use_windows: []
  confirmed_absence_observation_windows: []
  no_coverage_windows: []
  return_observation_refs: []
  current_assessment: UNKNOWN
  confidence: null
  explanatory_hypothesis_refs: []
```

Candidate assessment values:

- REPEATED_USE_SUPPORTED
- SEASONAL_RETURN_SUPPORTED
- INTERMITTENT_USE_SUPPORTED
- PREVIOUS_USE_ONLY
- CURRENT_USE_UNCONFIRMED
- SITE_CHANGE_SUPPORTED
- INSUFFICIENT_EVIDENCE
- UNKNOWN

`CURRENT_USE_UNCONFIRMED` is not abandonment.

### `SPATIAL_OVERLAP_ASSESSMENT`

Compares two or more spatial-use products without assuming social meaning.

```yaml
spatial_overlap_assessment:
  overlap_assessment_id: null
  subject_refs: []
  spatial_revision_refs: []
  overlap_geometry_ref: null
  overlap_band: null
  temporal_overlap_supported: unknown
  co_occurrence_observation_refs: []
  social_interpretation_refs: []
  resource_overlap_refs: []
  current_interpretation: UNRESOLVED
  confidence: null
```

Possible interpretations remain hypotheses:

- SHARED_RESOURCE_USE
- CO-TERRITORIAL_USE
- TEMPORAL_PARTITIONING
- INCIDENTAL_OVERLAP
- POSSIBLE_COMPETITION
- POSSIBLE_SOCIAL_ASSOCIATION
- OBSERVATION_ARTIFACT
- UNRESOLVED

No interpretation is automatic from the polygon.

### `TERRITORIAL_BEHAVIOR_EVENT`

Stores an observed defense/display event rather than a permanent species label.

```yaml
territorial_behavior_event:
  event_id: null
  actor_refs: []
  occurred_at: null
  location_ref: null
  target_actor_refs: []
  target_species_claim_refs: []
  behavior_tags: []
  resource_or_site_context_refs: []
  acoustic_observation_refs: []
  scent_or_mark_refs: []
  chase_or_displacement_observation_refs: []
  combat_ref: null
  outcome_ref: null
  observer_refs: []
  evidence_refs: []
  confidence: null
```

Candidate descriptive behavior tags:

- VOCAL_DISPLAY
- VISUAL_DISPLAY
- PATROL
- SCENT_OR_MARKING
- APPROACH
- FOLLOW
- CHASE
- BLOCK_ACCESS
- PHYSICAL_CONFRONTATION
- TOLERATED_ENTRY
- RETREAT_AFTER_DISPLAY
- UNKNOWN

These tags do not execute PTU mechanics.

### `TERRITORIALITY_ASSESSMENT`

A reviewed claim that a subject appears to defend some area or resource under defined conditions.

```yaml
territoriality_assessment:
  assessment_id: null
  subject_refs: []
  defended_area_geometry_ref: null
  defended_site_refs: []
  defended_resource_refs: []
  temporal_scope_ref: null
  tolerated_actor_refs: []
  target_pattern_claims: []
  supporting_event_refs: []
  contradictory_event_refs: []
  current_assessment: POSSIBLE
  confidence: null
  supersedes_assessment_id: null
```

Suggested states:

- INSUFFICIENT_EVIDENCE
- POSSIBLE
- SUPPORTED_FOR_SCOPE
- NOT_SUPPORTED_FOR_SCOPE
- SEASONAL_OR_CONTEXTUAL
- SUPERSEDED
- UNRESOLVED

A supported assessment can still contain tolerated occupants and overlap.

### `EXCURSION_EVENT`

Records movement beyond an established use area without immediately revising the range.

```yaml
excursion_event:
  excursion_id: null
  subject_ref: null
  baseline_home_range_revision_ref: null
  first_observed_outside_at: null
  last_observed_outside_at: null
  outside_location_refs: []
  movement_evidence_refs: []
  returned_to_baseline_use: unknown
  associated_driver_hypothesis_refs: []
  current_interpretation: UNRESOLVED
```

An excursion may later support prospecting, displacement, resource tracking, dispersal, migration participation, release exploration or a range shift. The responsible downstream authority decides when appropriate.

### `RANGE_SHIFT_REVIEW`

```yaml
range_shift_review:
  review_id: null
  subject_ref: null
  prior_home_range_revision_ref: null
  candidate_new_evidence_refs: []
  persistent_landscape_change_refs: []
  repeated_use_evidence_refs: []
  competing_hypothesis_refs: []
  decision: NO_REVISION_YET
  resulting_home_range_revision_ref: null
  confidence: null
```

Candidate decisions:

- NO_REVISION_YET
- TEMPORARY_EXCURSION_SUPPORTED
- PARTIAL_SHIFT_SUPPORTED
- RANGE_EXPANSION_SUPPORTED
- RANGE_CONTRACTION_SUPPORTED
- RANGE_RELOCATION_SUPPORTED
- DATA_NOT_COMPARABLE
- UNRESOLVED

## Evidence weighting and observation effort

Spatial products are only as complete as their observation process.

A valid assessment should retain:

- observation methods;
- dates and times;
- spatial coverage;
- daylight/night bias;
- weather restrictions;
- receiver/camera/observer availability;
- inaccessible areas;
- public-location redaction;
- device failure windows;
- sampling frequency;
- individual-identification confidence.

Never compare two home-range products as equivalent if their methods or coverage are materially incompatible without a comparison note.

## Site fidelity versus residency

A Pokémon may:

- return to the same winter site every year;
- use one roost repeatedly but forage elsewhere;
- leave for weeks and return;
- shift among several core-use areas;
- remain inside the same broad home range while changing daily routes;
- revisit a former range after release or retirement from partnership.

None of these creates legal residence or ownership.

Demography owns human residency concepts. Migration owns long-distance seasonal movement when that threshold is met.

## Territory and human space

Pokémon territoriality can cross:

- farms;
- roads;
- parks;
- houses;
- protected areas;
- mines;
- waterways;
- property boundaries;
- public paths;
- construction sites.

The behavior does not invalidate human legal state. Likewise, a fence, deed or municipal line does not define the Pokémon's behavioral boundary.

Potential conflicts are resolved by the relevant authority: Land Tenure, Urban Wildlife, Road Ecology, Conservation, Crisis, Workplaces or another system.

## Territorial communication

Possible evidence can include:

- calls or repeated acoustic patterns;
- scent marks;
- scratches or visual marks;
- patrol routes;
- repeated chases;
- postural displays;
- defended feeding sites;
- repeated tolerance of some individuals and exclusion of others.

Soundscapes, Olfactory/Field Signs and Photography own those observations. This layer only assesses their spatial relationship.

A call is not a border. A scent mark is not a border. A scratch is not a border.

## Collective territoriality

Some authored populations may defend space as pairs or groups.

If so:

- Wild Collectives owns who belongs to the collective;
- this layer may associate territorial events with the collective;
- individual exceptions remain possible;
- a group boundary does not grant Pack Mon, shared initiative or tactical coordination;
- tolerated outsiders do not automatically join the collective.

## Former partners and released Pokémon

A released persistent Pokémon may later establish or reuse a local range.

Allowed state:

- same `pokemon_entity_id`;
- release history preserved;
- later sightings connected if identity evidence supports it;
- site fidelity or range assessment built from new wild observations.

Forbidden inference:

- range near former Trainer -> partnership restored;
- site return -> Loyalty;
- old training location -> ownership;
- territorial defense near former home -> protecting former Trainer.

## Minecraft projection

Safe projections include:

- coarse recurring presence in approved sites;
- public research maps with reduced precision;
- visible but nonauthoritative scent/scratch/display props;
- observation stations;
- temporary buffers around recurring use areas;
- NPC commentary based on actor knowledge;
- persistent known individuals appearing within coarse server-authorized contexts.

Forbidden authority inversions:

- loaded entity positions become a home-range polygon;
- chunk unload becomes departure;
- repeated spawn point becomes site fidelity proof;
- vanilla pathfinding creates patrol truth;
- redstone or block boundaries create territory;
- killing/capturing one encounter clears a territory;
- a map mod reveals authoritative boundaries;
- mob aggro radius becomes territorial radius.

## Cobblemon projection

If spatial-use state later affects presence projection, the flow must be bounded:

`validated spatial-use revision -> reviewed presence projection -> Cobblemon presentation`

Anti-exploit rules:

- walking repeatedly through a chunk cannot create site fidelity;
- dropping food does not directly expand a range;
- placing markers does not define territory;
- killing, KOing or catching visible Pokémon does not instantly erase a range;
- server reload cannot duplicate persistent occupants;
- exact scientific polygons should not become rare-spawn heatmaps.

## PTU / AutoPTU boundary

This layer introduces zero battle mechanics.

Never infer:

- territorial -> hostile AI;
- territory -> battle zone;
- patrol -> free Shift;
- defended resource -> zone bonus;
- territorial display -> Intimidate;
- scent marking -> Tracker;
- territory overlap -> Pack Mon;
- pair defense -> shared initiative;
- intruder -> automatic interception;
- chase -> forced movement;
- known range -> surprise/Accuracy/initiative bonus;
- site fidelity -> Loyalty;
- core area -> capture modifier;
- boundary crossing -> reaction;
- territorial species lore -> a universal behavior for every individual.

If an authored encounter actually uses Intimidate, Intercept, Push/Pull, Status, a Move, an Ability, a Feature or any other rule, that exact mechanic must be verified independently.

## Encounter contract requirements

Every spatial-ecology encounter should record:

1. subject and evidence basis;
2. current spatial-use revision;
3. whether territoriality is observed, hypothesized or unsupported;
4. what noncombat world state changes first;
5. full battle dependencies;
6. reduced battle version when practical;
7. post-encounter evidence update separated from combat outcome.

A battle victory never means `territory cleared`.

## Suggested story grammar

`baseline use -> new observation -> evidence comparison -> overlap/excursion/display -> competing explanations -> optional intervention or battle -> follow-up -> spatial revision or no revision`

Possible normal outcomes:

- no change;
- same range, different core-use area;
- temporary excursion;
- seasonal return;
- range expansion;
- contraction;
- relocation;
- newly supported territoriality;
- territoriality hypothesis rejected;
- overlapping nonexclusive use;
- insufficient evidence.

## Hard non-inferences

Never infer:

- home range -> territory;
- territory -> legal ownership;
- territoriality -> permanent aggression;
- overlap -> friendship;
- overlap -> rivalry;
- overlap -> breeding pair;
- patrol pair -> parentage;
- site fidelity -> continuous presence;
- no sighting -> abandonment;
- one distant sighting -> range expansion;
- one road crossing -> new corridor;
- display -> combat challenge;
- call -> exact boundary;
- scent mark -> exact boundary;
- range shift -> climate cause;
- range shift -> infrastructure cause;
- former partner nearby -> reunion intent;
- Fainted -> ecological death;
- Minecraft despawn -> movement event.

## Canon gate

Before any spatial profile becomes canon, decide:

- which individuals/populations already have authored spatial behavior;
- what evidence exists before campaign start;
- what precision is visible to players;
- which sensitive ranges are redacted;
- how much spatial state progresses offline;
- which institutions can publish or review assessments;
- how territorial behavior relates to local conservation/access practice;
- whether specific species lore is locally applicable;
- whether a proposed battle uses only currently supported PTU mechanics.

Until approved, every range, territory, institution and candidate produced by Pass 176 remains proposed.