# Ouros Remote Sensing, Aerial Imagery & Change Detection Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon.
Date: 2026-08-25

## Purpose

Ouros already preserves individual photographs, maps, measurements, scientific claims, environmental revisions and historical records. This layer owns the missing spatial-observation boundary: repeated acquisition of a broad footprint from a remote or elevated platform, the quality and coverage of that acquisition, products derived from it, comparisons between dated products, and scoped change-detection claims.

The central chain is:

`physical world -> acquisition campaign -> acquisition -> coverage/quality -> source observation product -> derived spatial product -> comparison -> change-detection claim -> field validation -> owning-layer update if supported`

Remote sensing produces evidence. It does not write physical world truth directly.

## 1. Authority boundaries

This layer owns:

- persistent remote-observation campaigns;
- acquisition-platform identity when narratively important;
- acquisition events over spatial footprints;
- coverage, obscuration and acquisition-quality records;
- source spatial-observation products;
- derived classifications and index products;
- repeat-acquisition series;
- comparison pairs/sets;
- change-detection claims;
- field-validation links;
- processing revisions and product supersession;
- remote-observation access restrictions and sensitive-product handling;
- provenance from source acquisition through published spatial product.

This layer does not own:

- ordinary close-range photographs or camera-trap image identity -> Visual Records;
- instrument calibration, uncertainty standards or reference traceability -> Metrology;
- map editions, route representation or navigation products -> Cartography;
- hypotheses, datasets, scientific interpretation or publication truth -> Science;
- actual shoreline, river, wetland, forest, snow, urban, mining, agricultural or other environmental state -> the relevant domain layer;
- airspace permission, flight corridors or platform access -> Airspace;
- research subject/site permissions -> Research Ethics, Land Tenure, Conservation and other owning authorities;
- weather truth, cloud state or forecast -> Meteorology;
- exact time references and timestamp correction -> Timekeeping;
- actor or Pokémon identification -> Identity, Pokémon Agency and Taxonomy;
- PTU/Caelo mechanics -> authoritative rules/AutoPTU;
- Minecraft render state as remote-observation truth -> never.

## 2. Core separation

Keep these objects separate:

```text
WORLD STATE
  -> REMOTE ACQUISITION
  -> OBSERVED SIGNAL
  -> PROCESSED PRODUCT
  -> CLASSIFICATION / FEATURE EXTRACTION
  -> CHANGE COMPARISON
  -> CHANGE CLAIM
  -> FIELD VALIDATION
  -> DOMAIN INTERPRETATION
  -> OPTIONAL DOMAIN REVISION
```

Important no-inferences:

```text
remote image != map truth
remote image != ecological truth
classified pixel != confirmed object
visible animal count != population abundance
no visible animal != absence
change detected != cause known
no change detected != no physical change
cloud-free != error-free
higher resolution != automatically better evidence
new processing version != old acquisition false
old product superseded != old decision never happened
field validation disagreement != fraud
remote platform nearby != legal access
heat-like signal != Fire-type Pokémon
vegetation-like signal != Grassy Terrain
water-like signal != potable water
Minecraft chunk render != acquisition
Minecraft map item != scientific product
```

## 3. REMOTE_OBSERVATION_PROGRAM

A long-running institutional or project-specific series.

```yaml
remote_observation_program:
  program_id: null
  institution_ids: []
  purpose_refs: []
  target_region_ids: []
  supported_variable_or_feature_refs: []
  platform_family_refs: []
  method_revision_ids: []
  schedule_or_revisit_policy_ref: null
  access_policy_ref: null
  sensitivity_policy_ref: null
  started_at: null
  ended_at: null
  status: ACTIVE
```

Candidate purposes:

- BASELINE_MAPPING
- CHANGE_MONITORING
- DISASTER_RECONNAISSANCE
- HABITAT_EXTENT_MONITORING
- INFRASTRUCTURE_INSPECTION
- AGRICULTURAL_MONITORING
- SNOW_ICE_MONITORING
- WATER_EXTENT_MONITORING
- COASTAL_MONITORING
- FOREST_RECOVERY_MONITORING
- MINING_RECLAMATION_MONITORING
- URBAN_GROWTH_MONITORING
- RESEARCH_CAMPAIGN

The program says why observations are collected. It does not define the underlying world state.

## 4. ACQUISITION_PLATFORM

Platform technology is authored and setting-dependent.

```yaml
acquisition_platform:
  platform_id: null
  platform_type: null
  owner_or_operator_ids: []
  technical_asset_ref: null
  supported_sensor_refs: []
  operating_scope_ref: null
  airspace_or_access_refs: []
  metrology_refs: []
  current_operational_state: UNKNOWN
  history_event_ids: []
```

Candidate platform types:

- FIXED_OVERLOOK
- TOWER_MOUNTED
- BALLOON
- AIRSHIP
- CREWED_AIRCRAFT
- SMALL_REMOTE_CRAFT
- POKEMON_ASSISTED_SURVEY_PLATFORM
- HIGH_ALTITUDE_PLATFORM
- ORBITAL_PLATFORM
- OTHER_AUTHORED

No platform type is canon merely because it appears here.

Real-world satellite systems are research inspiration only. Ouros does not gain orbital sensing unless canon explicitly establishes it.

A Pokémon-assisted platform requires explicit individual agency, capability and institutional-role handling. Species flavor alone cannot establish carrying capacity, legal flight or willingness.

## 5. REMOTE_ACQUISITION

A single dated observation over a footprint.

```yaml
remote_acquisition:
  acquisition_id: null
  program_id: null
  platform_id: null
  sensor_ids: []
  started_at: null
  ended_at: null
  raw_timestamp_refs: []
  corrected_time_refs: []
  nominal_footprint_ref: null
  achieved_coverage_ref: null
  viewing_geometry_ref: null
  environmental_context_refs: []
  access_authorization_refs: []
  operator_actor_ids: []
  source_product_ids: []
  acquisition_state: COMPLETE
```

Candidate states:

- PLANNED
- PARTIAL
- COMPLETE
- ABORTED
- LOST
- UNUSABLE_FOR_STATED_PURPOSE
- ARCHIVED

A completed acquisition may still have poor or incomplete coverage.

## 6. COVERAGE_QUALITY_RECORD

Coverage is first-class evidence.

```yaml
coverage_quality_record:
  coverage_record_id: null
  acquisition_id: null
  valid_coverage_geometry_ref: null
  obscured_geometry_refs: []
  missing_geometry_refs: []
  resolution_or_scale_band: null
  viewing_angle_band: null
  cloud_or_weather_obscuration_ref: null
  smoke_or_aerosol_obscuration_ref: null
  canopy_obscuration_ref: null
  shadow_or_terrain_obscuration_ref: null
  platform_motion_issue_ref: null
  sensor_issue_refs: []
  processing_quality_flags: []
  quality_notes: null
```

Do not collapse all quality dimensions into a single score.

Suggested coverage interpretations:

- OBSERVED_CLEARLY_FOR_SCOPE
- OBSERVED_WITH_LIMITATIONS
- PARTIALLY_OBSCURED
- NOT_OBSERVED
- OBSERVED_AT_INSUFFICIENT_RESOLUTION
- GEOMETRICALLY_UNCERTAIN
- TEMPORALLY_UNCERTAIN

`NOT_OBSERVED` remains distinct from `ABSENT`.

## 7. SOURCE_SPATIAL_PRODUCT

The immediate durable product derived from an acquisition.

```yaml
source_spatial_product:
  product_id: null
  acquisition_id: null
  product_type: null
  processing_revision_id: null
  spatial_reference_ref: null
  footprint_ref: null
  resolution_or_scale_ref: null
  source_asset_refs: []
  visual_record_refs: []
  metrology_refs: []
  quality_record_ids: []
  created_at: null
  superseded_by_product_id: null
  preservation_state: CURRENT
```

Candidate product types:

- SOURCE_IMAGE_MOSAIC
- ORTHORECTIFIED_IMAGE
- ELEVATION_OR_SURFACE_PRODUCT
- THERMAL_PRODUCT
- MULTISPECTRAL_PRODUCT
- RADAR_LIKE_PRODUCT
- MANUAL_AERIAL_SKETCH
- POINT_OR_TRANSECT_PRODUCT
- OTHER_AUTHORED

These labels describe data products, not PTU effects.

Visual Records can retain constituent image artifacts while this layer owns the broader spatial acquisition/product relationship.

## 8. PROCESSING_REVISION

Processing methods must be versioned.

```yaml
remote_processing_revision:
  processing_revision_id: null
  method_family_ref: null
  version_label: null
  effective_from: null
  calibration_or_reference_refs: []
  correction_steps: []
  known_limitations: []
  supersedes_revision_id: null
  validation_refs: []
```

A new revision can improve geometric alignment, correction or classification without rewriting the source acquisition.

Historical products remain valid records of what institutions used at the time.

## 9. DERIVED_SPATIAL_PRODUCT

Derived products transform source observations into interpreted spatial information.

```yaml
derived_spatial_product:
  derived_product_id: null
  source_product_ids: []
  processing_revision_id: null
  product_family: null
  output_geometry_ref: null
  output_class_or_value_ref: null
  confidence_or_quality_refs: []
  masking_refs: []
  validation_refs: []
  created_at: null
  supersedes_product_id: null
```

Candidate families:

- WATER_EXTENT_CLASSIFICATION
- VEGETATION_EXTENT_CLASSIFICATION
- SNOW_ICE_EXTENT_CLASSIFICATION
- BURN_SCAR_CANDIDATE
- SHORELINE_CANDIDATE
- LAND_COVER_CLASSIFICATION
- SURFACE_TEMPERATURE_ESTIMATE
- STRUCTURE_OR_ROAD_CANDIDATE
- HABITAT_EXTENT_CANDIDATE
- CHANGE_MASK
- OTHER_AUTHORED

The word `candidate` matters. Derived products do not establish cause.

## 10. REPEAT_ACQUISITION_SERIES

Repeated coverage creates Chronicle value.

```yaml
repeat_acquisition_series:
  series_id: null
  program_id: null
  region_or_site_ref: null
  acquisition_ids: []
  comparability_assessment_ids: []
  intended_revisit_policy_ref: null
  actual_revisit_history: []
  known_gap_intervals: []
  status: ACTIVE
```

A series can include gaps caused by weather, outages, access, platform changes, archive loss or funding changes.

A gap does not imply the world stopped changing.

## 11. COMPARABILITY_ASSESSMENT

Change detection requires enough comparability between products.

```yaml
comparability_assessment:
  assessment_id: null
  product_ids: []
  assessed_at: null
  assessor_ids: []
  geometric_comparability: null
  temporal_comparability: null
  spectral_or_signal_comparability: null
  resolution_comparability: null
  processing_revision_compatibility: null
  seasonal_context_compatibility: null
  quality_limitations: []
  conclusion: SUFFICIENT_FOR_SCOPE
```

Candidate conclusions:

- SUFFICIENT_FOR_SCOPE
- SUFFICIENT_WITH_LIMITATIONS
- INSUFFICIENT_COMPARABILITY
- REQUIRES_REPROCESSING
- UNRESOLVED

Two images can look different because the world changed, because the acquisition context changed, because the processing changed, or some combination.

## 12. CHANGE_DETECTION_CLAIM

Change claims are scoped evidence objects.

```yaml
change_detection_claim:
  change_claim_id: null
  comparison_product_ids: []
  comparability_assessment_id: null
  target_feature_or_region_ref: null
  change_type: null
  detected_geometry_ref: null
  earliest_possible_time: null
  latest_possible_time: null
  confidence_or_support_ref: null
  status: CANDIDATE_CHANGE
  alternative_explanation_refs: []
  field_validation_refs: []
  owning_domain_handoff_ref: null
```

Recommended states:

- NO_CHANGE_DETECTED_FOR_SCOPE
- CANDIDATE_CHANGE
- CHANGE_SUPPORTED
- CHANGE_CONFIRMED_FOR_SCOPE
- ARTIFACT_OR_PROCESSING_DIFFERENCE
- INSUFFICIENT_COMPARABILITY
- UNRESOLVED

`CHANGE_CONFIRMED_FOR_SCOPE` still does not automatically explain cause.

## 13. Change-time interval

Remote sensing often constrains when something changed without observing the exact event.

Example:

```text
acquisition A: bridge present on May 3
acquisition B: bridge absent on May 11
```

The evidence supports a change interval between those dates. It does not establish May 7, a particular storm, sabotage, or a specific actor unless other evidence supports that claim.

Store intervals rather than invented exact timestamps.

## 14. FIELD_VALIDATION_LINK

Remote anomalies can generate optional field work.

```yaml
field_validation_link:
  validation_id: null
  change_claim_id: null
  validation_type: null
  field_observation_ids: []
  sample_ids: []
  visual_record_ids: []
  instrument_result_ids: []
  performed_at: null
  coverage_ref: null
  conclusion: UNRESOLVED
  limitations: []
```

Candidate validation outcomes:

- SUPPORTS_REMOTE_CLAIM
- PARTIALLY_SUPPORTS
- DOES_NOT_SUPPORT_FOR_SCOPE
- REMOTE_ARTIFACT_SUPPORTED
- FIELD_OBSERVATION_TOO_LATE
- SITE_INACCESSIBLE
- MIXED_RESULT
- UNRESOLVED

Field validation can itself be incomplete or disturbed by later change.

## 15. Handoff to owning domain layers

A remote claim may propose a handoff to:

- Coastal Geomorphology for shoreline change;
- Fluvial Geomorphology for channel migration;
- Freshwater for water extent;
- Cryosphere for snow/ice persistence;
- Wildfire for burn history;
- Forest Management/Canopy for forest change;
- Wetlands/Estuaries/Peatlands for habitat extent;
- Mining for quarry/mine geometry and reclamation;
- Urban systems for built expansion;
- Agriculture for crop/field state;
- Conservation for habitat monitoring;
- Road/Rail/Infrastructure for corridor change;
- Climate only through sufficiently long, methodologically valid evidence.

The receiving layer decides whether its own state is revised.

## 16. Sensitive observation and access

Remote acquisition can create information about places the operator could not physically enter.

That does not erase access, privacy or stewardship rules.

```yaml
remote_product_access_policy:
  product_id: null
  exact_geometry_visibility: RESTRICTED
  public_generalization_ref: null
  restriction_reason_refs: []
  authorized_audience_refs: []
  redacted_or_generalized_product_ids: []
```

Potentially sensitive cases include:

- nests and reproductive sites;
- threatened populations;
- sacred/restricted places;
- private homes;
- secure infrastructure;
- archaeological/paleontological sites;
- research subjects;
- emergency operations;
- rare-species locations.

Remote observation never implies permission to enter or publish exact coordinates.

## 17. Wildlife-disturbance boundary

A distant/passive acquisition and a close low-altitude survey are not equivalent.

If a platform can disturb wildlife, preserve:

- platform distance/altitude band;
- noise/light context;
- repeated-pass history;
- observed behavioral response;
- ethics/access restrictions;
- any resulting route/roost/nest observation.

Research Ethics, Airspace and the relevant wildlife layer own the consequences.

Do not infer disturbance merely because a platform existed nearby.

## 18. Pokémon-assisted surveys

Pokémon may participate in remote observation only when world state supports the individual role.

Possible authored roles include:

- carrying approved equipment;
- transporting an observer;
- reaching a survey station;
- maintaining a platform;
- retrieving a sensor;
- assisting with field validation.

Working Pokémon/Pokémon Agency own assignment, participation and refusal.

No species automatically grants:

- survey quality;
- georeferencing;
- image resolution;
- Technology Education;
- Pokémon Education;
- mapping precision;
- carrying capacity;
- legal airspace access;
- remote identification.

## 19. Minecraft projection

Minecraft may present:

- observation towers;
- aerial survey vehicles or authored platforms;
- fixed survey stations;
- map-table interfaces;
- dated image layers;
- before/after overlays;
- cloud or obscuration icons;
- generalized change polygons;
- field-validation waypoints;
- equipment retrieval interactions.

Minecraft must not decide:

- what territory was truly observed from render distance;
- whether an unloaded chunk changed;
- whether a pixel/classification is correct;
- whether a visible Pokémon count is population truth;
- whether a shoreline/forest/wetland actually changed;
- whether a derived product proves causation;
- whether an area is safe, potable, contaminated or mechanically hazardous;
- whether a remote product grants map knowledge to every actor;
- whether a remote platform grants combat LoS or Accuracy.

Server world state remains authoritative.

## 20. Player knowledge

A remote product can exist without every player knowing it.

Track separately:

- product existence;
- institution access;
- publication state;
- player access;
- player interpretation;
- field-validation participation;
- public-memory effects.

Receiving a map overlay does not grant perfect route knowledge or species identification.

## 21. Routine compression

Remote-observation programs can run for years without generating a quest every revisit.

Compress routine acquisitions when:

- coverage is normal;
- no new candidate change appears;
- no access or equipment decision is needed;
- no sensitive publication issue arises;
- no field validation is requested.

Expose play when:

- a new change claim matters;
- products disagree;
- an important acquisition is missing;
- a platform needs field intervention;
- a site requires validation;
- publication/access creates a decision;
- a historical product changes interpretation of an old event.

## 22. Failure-forward outcomes

Remote-observation gameplay can end with:

- clear change, unknown cause;
- no change detected within resolution limits;
- missing coverage;
- cloud/smoke obstruction;
- processing artifact;
- two products that cannot be compared safely;
- field confirmation;
- field contradiction;
- site already changed again before validation;
- sensitive result that cannot be published precisely;
- old imagery that changes a historical interpretation;
- useful baseline with no immediate quest.

All are valid Chronicle outcomes.

## 23. PTU/Caelo mechanical boundary

No generic PTU remote-sensing subsystem is established by this design.

Remote observation does not grant:

- combat LoS;
- Accuracy bonuses;
- initiative bonuses;
- surprise;
- automatic Pokémon identification;
- encounter-table manipulation;
- spawn modifiers;
- Weather/Terrain detection with battle authority;
- targeting outside the current battle rules;
- navigation checks or route certainty;
- map-based Trainer Features.

Any exact Move, Ability, Item, Feature, Skill or Capability invoked by an encounter must be validated separately against the project PTU/Caelo corpus and live engine.

## 24. Encounter handoff

Most remote-sensing gameplay belongs outside battle.

Before AutoPTU handoff:

1. resolve acquisition/coverage state;
2. resolve platform/operator position outside the tactical grid when possible;
3. freeze the relevant world geometry;
4. remove noncombatant technicians and sensitive equipment from tactical authority;
5. hand only real combatants and validated battle state to AutoPTU;
6. after battle, return to the remote-observation claim and continue validation.

A battle outcome never confirms a spatial change claim.

## 25. Open canon questions

Still unresolved:

- which remote-observation technologies exist in Ouros;
- whether orbital platforms exist at all;
- which institutions operate regional programs;
- whether different regions use different platforms and resolutions;
- how much historical imagery exists before the campaign;
- which products are public, restricted or commercial;
- how player organizations can commission surveys;
- how often acquisitions advance offline;
- how large datasets are represented without unnecessary simulation;
- whether Pokémon-assisted platforms are common, rare or absent;
- which exact PTU/Caelo Skills/Features/equipment can support survey work;
- how remote products connect to player map UI without becoming omniscient.

Until reviewed, all technology, examples and entities in this document remain proposed.