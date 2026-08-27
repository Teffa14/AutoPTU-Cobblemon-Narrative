# Ouros Wildlife Monitoring, Re-identification, Tagging & Telemetry Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Ouros already supports persistent Pokémon identities, wild collectives, scientific observations, camera traps, protected-area monitoring, equipment custody and digital records. This extension connects those systems across long periods of field observation.

It models how researchers or stewards may repeatedly identify the same wild Pokémon, associate a physical or visual marker with that individual, deploy a monitoring device for a bounded interval, collect detections, recognize gaps, recover or retire equipment and update research or stewardship state without converting monitoring into capture, ownership or omniscient knowledge.

The central design goal is longitudinal continuity. A wild Pokémon can matter for months of play while remaining wild and while researchers remain uncertain about where it is between verified observations.

## Boundary with existing systems

Science owns the research question, method, dataset, hypothesis, analysis, review and publication.

Photography owns visual records, camera stations and visual re-identification evidence.

Soundscape/Acoustic Ecology owns acoustic observations and acoustic-site interpretation.

Wild Collective Agency owns population/collective/subgroup state.

Pokémon Agency owns persistent Pokémon identity, custody, active Trainer state, partnership, capture/release history and association continuity.

Conservation owns stewardship policy, protected-area management and management review.

Shared Equipment and Material Culture own device instances, custody and physical provenance.

Technology/Infrastructure owns receiver stations as physical assets, power, faults and maintenance.

Digital Systems owns stored telemetry records, access, versions and system logs.

Travel/Expedition owns field access and expedition logistics.

Care owns medical/welfare cases when monitoring activity creates a health concern.

This extension owns the longitudinal association among subject identity, monitoring method, device deployment, detection, re-sighting, track interpretation and monitoring-program continuity.

## Core separation

Keep these states distinct:

```text
persistent Pokémon or provisional subject identity
        ↓
identity evidence
        ↓
monitoring method
        ↓
mark/device identity
        ↓
deployment interval
        ↓
raw detections / re-sightings
        ↓
quality review
        ↓
track or presence interpretation
        ↓
research/stewardship claim
        ↓
management or narrative consequence
```

No arrow permits an automatic reverse inference.

A detection does not prove the Pokémon remained there afterward.

A silent device does not prove disappearance, death or migration.

A tag does not create ownership.

A research subject does not become a battle participant because a device reports its location.

## 1. Monitoring subject

A monitoring program may begin before exact persistent identity is proven.

```yaml
monitoring_subject:
  monitoring_subject_id: null
  pokemon_entity_id: null
  provisional_subject_label: null
  species_claim_refs: []
  identity_state: provisional
  identity_evidence_refs: []
  conflicting_identity_refs: []
  collective_candidate_refs: []
  home_range_claim_refs: []
  current_monitoring_status: inactive
  sensitivity_policy_ref: null
  created_event_id: null
  last_confirmed_observation_id: null
```

Suggested `identity_state` values:

- PROVISIONAL
- SUPPORTED
- CONFIRMED_FOR_PROGRAM
- MERGED_WITH_EXISTING_ENTITY
- SPLIT_FROM_PRIOR_IDENTITY
- DISPUTED
- RETIRED

`CONFIRMED_FOR_PROGRAM` means the research program has enough evidence to treat observations as one individual. It does not establish legal ownership, capture status or universal public identity.

If the subject maps to an established `pokemon_entity`, that entity remains the durable identity owner.

## 2. Identification evidence

Different methods can support the same identity claim.

```yaml
individual_identity_evidence:
  evidence_id: null
  monitoring_subject_id: null
  method_type: null
  source_ref: null
  observed_features: []
  contradicting_features: []
  collected_at: null
  collected_location_id: null
  confidence_band: low
  reviewer_ids: []
  status: active
```

Candidate methods:

- NATURAL_VISUAL_MARK
- REPEATED_VISUAL_PATTERN
- ARTIFICIAL_VISIBLE_MARK
- DEVICE_IDENTIFIER
- ACOUSTIC_SIGNATURE only when evidence supports individual distinction
- VERIFIED_CAPTURE_OR_CARE_RECORD
- AUTHORED_UNIQUE_FEATURE
- MULTI_SOURCE_MATCH
- OTHER_REVIEWED_METHOD

Species, sex, size or level alone should rarely be sufficient for individual identity.

A Cobblemon entity UUID may be stored as implementation provenance while the entity is loaded. It must not be treated as the sole narrative identity proof because entity lifecycle, migration, despawn/reload and adapter implementation may change.

## 3. Monitoring method

```yaml
wildlife_monitoring_method:
  method_id: null
  research_method_ref: null
  method_family: null
  target_question_ids: []
  disturbance_profile: unknown
  direct_contact_required: false
  equipment_refs: []
  required_authorization_refs: []
  welfare_review_refs: []
  known_detection_limits: []
  known_identity_limits: []
  data_latency_profile: null
  canon_status: proposed
```

Candidate method families:

- DIRECT_REOBSERVATION
- NATURAL_MARK_REIDENTIFICATION
- PHOTOGRAPHIC_REIDENTIFICATION
- CAMERA_STATION
- PASSIVE_ACOUSTIC_STATION
- TRACE_OR_SIGN_SURVEY
- VISIBLE_MARK
- RADIO_STYLE_TAG if canon supports it
- ACOUSTIC_TAG if canon supports it
- LOCATION_SENSOR if canon supports it
- ARCHIVAL_SENSOR if canon supports it
- OTHER_AUTHORED_METHOD

The presence of a method type in the schema does not establish that Ouros possesses that technology.

## 4. Physical mark or device instance

A tag/device has its own identity and provenance.

```yaml
monitoring_device_instance:
  device_id: null
  material_item_instance_ref: null
  device_class: null
  serial_or_identifier: null
  operator_institution_id: null
  current_custodian_id: null
  current_location_id: null
  service_state: available
  calibration_or_test_refs: []
  maintenance_refs: []
  deployment_ids: []
  recovery_ids: []
  data_system_ref: null
  retired_at: null
```

The same device may have several deployments over its lifetime.

A serial identifies the device. It does not permanently identify one Pokémon.

## 5. Deployment interval

This is the central Pass 79 record.

```yaml
monitoring_deployment:
  deployment_id: null
  monitoring_subject_id: null
  pokemon_entity_id: null
  device_or_mark_id: null
  method_id: null
  deployment_start_event_id: null
  deployment_start_time: null
  deployment_end_event_id: null
  deployment_end_time: null
  deployment_location_id: null
  deploying_actor_ids: []
  authorization_refs: []
  welfare_or_care_refs: []
  attachment_or_marking_observation_refs: []
  expected_duration_claim: null
  confirmed_active_windows: []
  uncertain_windows: []
  resulting_status: active
  provenance_refs: []
```

Suggested resulting states:

- ACTIVE
- ENDED_RECOVERED
- ENDED_OBSERVED_REMOVED
- ENDED_DEVICE_RELEASED
- ENDED_DEVICE_FAILED
- ENDED_DEVICE_LOST
- END_TIME_UNCERTAIN
- INVALIDATED

A deployment ends when the association between subject and device/mark ends, not merely when the database stops receiving detections.

## 6. Marking/deployment event

Direct contact must be represented as a world event rather than hidden database mutation.

```yaml
marking_or_deployment_event:
  event_id: null
  monitoring_subject_id: null
  method_id: null
  device_or_mark_id: null
  location_id: null
  timestamp: null
  participating_actor_ids: []
  authorization_refs: []
  capture_or_restraint_mechanical_ref: null
  care_or_welfare_observations: []
  completion_state: null
  followup_requirements: []
```

Pass 79 does not define restraint, sedation, capture, handling or attachment mechanics. If a method needs them, governing PTU/Caelo rules and project canon must be reviewed separately.

The default content generator should prefer non-contact monitoring when it satisfies the research question.

## 7. Receiver or observation station

Receiver networks build on existing technical assets.

```yaml
monitoring_station_projection:
  station_id: null
  technical_asset_ref: null
  location_id: null
  supported_method_ids: []
  coverage_claim_ref: null
  operational_state_ref: null
  last_verified_operational_at: null
  maintenance_refs: []
  dataset_refs: []
```

The Technology/Infrastructure layer owns whether the station has power, hardware faults or physical damage.

Pass 79 only uses that operational evidence when interpreting detections or gaps.

## 8. Detection event

```yaml
monitoring_detection:
  detection_id: null
  deployment_id: null
  device_id: null
  station_id: null
  raw_source_ref: null
  observed_at: null
  received_at: null
  approximate_location_ref: null
  measurement_refs: []
  signal_or_detection_quality: unknown
  automated_identity_claim_ref: null
  review_state: unreviewed
  invalidation_reason: null
```

A detection answers a bounded question: a system recorded something associated with this device at this time under these operating conditions.

It does not establish exact continuous movement between detections.

## 9. Direct re-sighting

```yaml
monitoring_resighting:
  resighting_id: null
  monitoring_subject_id: null
  pokemon_entity_id: null
  observation_id: null
  visual_record_refs: []
  acoustic_record_refs: []
  timestamp: null
  location_id: null
  identity_assessment_ref: null
  behavior_observation_refs: []
  visible_device_or_mark_state: unknown
  observer_ids: []
```

A re-sighting may confirm that:

- the individual is alive/present at that observation;
- a mark/device is still visibly present;
- a device appears absent;
- the individual occupies a location outside an assumed route;
- the automated record was likely assigned incorrectly.

It does not reveal unseen movement before or after the sighting.

## 10. Detection gaps

Gaps are first-class evidence.

```yaml
monitoring_gap:
  gap_id: null
  deployment_id: null
  gap_start: null
  gap_end_or_open: null
  expected_detection_basis_refs: []
  receiver_operational_evidence_refs: []
  device_health_evidence_refs: []
  direct_resighting_refs: []
  candidate_explanations: []
  resolved_explanation_ref: null
  status: unresolved
```

Candidate explanations can include:

- SUBJECT_OUTSIDE_COVERAGE
- RECEIVER_OFFLINE
- DEVICE_FAILURE
- DEVICE_REMOVED_OR_RELEASED
- DEVICE_LOST
- DATA_DELAY
- DATA_IMPORT_GAP
- SIGNAL_OBSTRUCTION
- IDENTITY_ASSIGNMENT_ERROR
- EXPECTATION_WAS_WRONG
- UNKNOWN

The generator must not select death, capture, injury or migration merely because a signal stops.

## 11. Track segment and interpolation boundary

```yaml
monitoring_track_segment:
  track_segment_id: null
  monitoring_subject_id: null
  deployment_id: null
  start_observation_ref: null
  end_observation_ref: null
  supporting_detection_refs: []
  direct_observation_refs: []
  route_interpretation_ref: null
  interpolation_state: none
  confidence_band: null
  environmental_annotation_refs: []
```

If a UI draws a line between two detections, the system must preserve whether that line is:

- observed path;
- plausible route;
- straight visual interpolation;
- modelled estimate;
- unknown connection.

A pretty map must not become stronger evidence than the underlying records.

## 12. Individual versus collective inference

```yaml
individual_collective_inference:
  inference_id: null
  individual_subject_ids: []
  collective_or_population_id: null
  observed_pattern: null
  supporting_evidence_refs: []
  counterexample_refs: []
  sampling_limitations: []
  current_interpretation: null
  review_status: proposed
```

One individual taking a new route can trigger a research question.

Several independent individuals repeating the route can strengthen it.

Neither event automatically rewrites collective state without Science/Conservation review.

## 13. Device recovery

```yaml
monitoring_device_recovery:
  recovery_id: null
  device_id: null
  deployment_id: null
  found_event_id: null
  found_location_id: null
  finder_actor_ids: []
  subject_present: false
  physical_condition_observation_ref: null
  custody_handoff_ref: null
  data_recovery_ref: null
  deployment_end_assessment_ref: null
```

A recovered device without the Pokémon can mean many things.

Do not infer that the Pokémon is dead, captured or injured.

If the device enters ordinary found-property handling, the Found Property layer can own custody while Pass 79 preserves its research/deployment relationship.

## 14. Welfare and disturbance history

Monitoring can itself affect the observed system.

```yaml
monitoring_disturbance_review:
  review_id: null
  program_id: null
  method_id: null
  subject_ids: []
  observed_response_refs: []
  care_or_welfare_refs: []
  method_change_refs: []
  unresolved_questions: []
```

A method can be reduced, paused or replaced because researchers suspect it changes behavior even before causality is proven.

This creates useful gameplay: improve the method rather than simply “get a stronger tracker.”

## 15. Data access and sensitive locations

Exact movement data may reveal vulnerable nests, refuges, sacred locations or private research activity.

```yaml
monitoring_data_access_profile:
  dataset_ref: null
  public_summary_ref: null
  precise_location_access_policy_ref: null
  delayed_release_policy_ref: null
  redaction_refs: []
  sensitivity_reason_claim_refs: []
```

No universal privacy law is assumed.

The schema merely allows canon institutions to distinguish a public migration summary from precise current coordinates.

## 16. Research-program loop

A robust monitoring program can create content across many visits:

1. identify a bounded research question;
2. establish a baseline with direct observation or passive stations;
3. decide whether an individual-level method is justified;
4. deploy a mark/device only if canon and method permit it;
5. collect detections and re-sightings;
6. verify receiver/device health;
7. analyze gaps and route hypotheses;
8. compare several individuals where appropriate;
9. revise the method or stewardship decision;
10. recover/retire/redeploy equipment;
11. return months later and compare the new state with the old record.

The same program can remain interesting without escalating into combat.

## 17. Minecraft/Cobblemon embodiment

Use Cobblemon aggressively for presentation and world continuity where safe.

Good reuse includes:

- Pokémon overworld entities, models, forms and animations;
- cries and ambient behavior presentation;
- existing entity interaction hooks;
- visible held/attached cosmetic research markers if technically and aesthetically appropriate;
- blocks/entities for monitoring stations;
- particles and sounds for receiver feedback;
- item models for devices;
- map/UI presentation;
- networking and synchronization;
- world coordinates and observed entity location;
- persistence hooks;
- spawn/ecology integration where the owning ecology system authorizes it.

Do not duplicate assets or locomotion presentation that Cobblemon already supplies.

### Authority boundary

Cobblemon/Minecraft may report an observed overworld position to Ouros.

Ouros decides whether the observation maps to an established monitoring subject.

A research signal may cause Ouros to create a world objective such as “check receiver station 4” or “survey this valley.”

If a battle occurs, Ouros explicitly authors the candidate encounter facts and AutoPTU receives the approved BattleSpec.

Cobblemon battle-state code never chooses monitored Pokémon as combatants merely because their overworld entities are nearby.

Cobblemon battle-state code never owns HP, statuses, initiative, targets, tactical positions, legality or battle results.

Required flow:

`Ouros monitoring/world state -> encounter decision -> AutoPTU BattleSpec/state/result -> adapter -> Cobblemon/Minecraft presentation`

## 18. Telemetry and encounter generation

A monitoring detection can create a lead, not a guaranteed encounter.

Example:

- receiver detects Subject 17 in a valley at 03:10;
- player arrives at 09:00;
- the subject may have moved;
- tracks, camera records, other Pokémon, weather or a broken station may be what the player actually finds;
- if the same Pokémon is observed and a tactical encounter is authored, Ouros chooses whether it participates;
- AutoPTU resolves the battle if one begins.

Never teleport the Pokémon to the last telemetry coordinate just to satisfy a quest marker.

## 19. Mechanically rich encounter contracts

### Receiver Ridge Withdrawal

Narrative premise:

A field team reaches a receiver station during a monitoring window and discovers that territorial wild Pokémon are occupying the safe approach. The research goal is to retrieve the station log and leave without turning the monitoring program into a capture operation.

Intended full version:

- researchers withdraw toward established exits;
- battle participants have explicit roles;
- territorial opponents may prefer denial/withdrawal behavior over KO pursuit;
- terrain and weather can matter if governing rules support them;
- interception/forced movement may matter around a narrow ridge;
- AI understands WITHDRAW/CLEAR_ROUTE objectives;
- Minecraft renders the AutoPTU-owned tactical state.

Full dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement when selected content uses it;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle for selected combatants;
- terrain/weather/hazards/zones/reactions if active environment rules are selected;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:

Researchers leave the tactical area before battle. The receiver remains a protected overworld object outside targeting. The party resolves a static ordinary encounter on reviewed geometry. After authoritative resolution, Ouros decides whether access to the station is safe enough to retrieve data. No ridge hazard, weather modifier, protection mechanic or forced movement is invented.

### Tag Recovery at the Waterline

Narrative premise:

A detached monitoring device is detected or found near a shoreline used by the monitored Pokémon’s collective. Recovering the device matters because it contains data, but the Pokémon itself is not automatically present.

Intended full version:

- recovery location can be a tactical objective;
- water/shore terrain may alter legal routes if supported;
- wild Pokémon may defend space or withdraw;
- the device remains a noncombat research object;
- AI reasons about territory rather than treating the tag as loot.

Reduced version:

The device is recovered as an overworld interaction before or after a conventional legal battle. It never occupies a targetable tactical slot. Water is static geometry unless validated movement rules apply. The device recovery does not locate the original subject or close the deployment interpretation automatically.

### Re-sighting Without Capture

This is primarily a noncombat encounter.

The player attempts to establish identity through observation, visual records and timing while minimizing disturbance. The strongest result may be a confirmed re-sighting with no battle, no capture and no device deployment.

If the Pokémon becomes aggressive or another threat intervenes, a separate battle contract is instantiated. The research identity claim remains based on observation evidence, not on who appears in the battle transcript.

## 20. Anti-false-completion rules

- A tag ID does not equal Pokémon identity forever.
- A device can be redeployed.
- A signal does not create an exact live waypoint unless the actual system supports that claim.
- No signal does not prove absence.
- A receiver outage does not prove the subject changed route.
- A re-sighting does not reveal the path taken between observations.
- One tracked individual does not define a species or collective.
- A monitoring subject remains wild unless separate authoritative state changes that.
- Marking does not create ownership, Loyalty or battle-control rights.
- Research contact does not authorize capture.
- A Cobblemon entity UUID is implementation provenance, not sufficient narrative identity authority.
- A nearby Cobblemon Pokémon is not automatically a combatant.
- A research database cannot feed hidden opponent knowledge to tactical AI.
- Tracking information cannot bypass actor-knowledge boundaries.
- A recovered tag without its subject does not establish death or injury.
- A field device cannot grant invented PTU bonuses.
- Visible weather or terrain cannot become tactical mechanics through Minecraft scripting while AutoPTU lacks those families.

## 21. Canon gates

Before this extension becomes concrete canon, Ouros needs decisions about:

- whether artificial wildlife tagging exists at all;
- which technologies exist by region and institution;
- whether attachment is visible, temporary, implanted, external or never used;
- what authorization and welfare review exist;
- which Pokémon/species/body forms can safely support which method;
- whether precise movement data is restricted;
- how research subjects are publicly named or anonymized;
- who maintains receiver networks;
- how devices are recovered and reused;
- what technologies can operate underwater, underground or over long distance;
- how natural markers are documented;
- whether any monitoring practice is culturally unacceptable in specific places;
- how individual tracking intersects protected habitats and sacred sites.

Until reviewed, all technologies and institutions introduced by Pass 79 remain proposals.