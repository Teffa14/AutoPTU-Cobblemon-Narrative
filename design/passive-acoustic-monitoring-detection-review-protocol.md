# Ouros Passive Acoustic Monitoring, Detection, and Review Protocol

Status: proposed protocol extension. Not established canon.

Authority: subordinate to `design/soundscapes-acoustic-ecology-layer.md`.

Pass: 167.

## Purpose

The Soundscapes layer already owns acoustic sources, sound events, recordings, listening sites, learned profiles, baselines and acoustic interpretations. This protocol adds the operational and evidentiary workflow required when Ouros uses autonomous or repeated passive listening as a monitoring method.

The central rule is:

```text
recording effort
→ raw audio
→ candidate detection
→ review
→ validated acoustic observation
→ aggregate monitoring product
→ interpretation
```

No step silently proves the next.

## 1. Authority boundaries

This protocol owns:

- passive-acoustic monitoring programs;
- recorder deployments;
- planned versus realized recording effort;
- uptime and recording gaps;
- automated detection candidates;
- detector/model revisions;
- human/expert review state;
- duplicate-event linkage;
- acoustic coverage revisions;
- validated detection series;
- comparability assessments;
- aggregate acoustic monitoring products.

Existing authorities retain ownership of:

- Soundscapes: sound event, acoustic recording, acoustic profile, acoustic observation and acoustic baseline;
- Science: hypothesis, analysis, dataset interpretation and publication;
- Metrology: calibration and measurement traceability;
- Timekeeping: clock state and corrected timestamps;
- Research Ethics: authorization, protected sites and subject protection;
- Community Science: public submissions and volunteer observation programs;
- Wildlife Telemetry: devices attached to individually identified subjects;
- Diel Activity / Seasonality: biological timing interpretation;
- Migration: migration episodes and corridors;
- Wild Collective Agency: collective identity;
- Pokémon Agency: individual identity and agency;
- Technology: actual recorder, sensor, storage and communications capabilities;
- Minecraft/Cobblemon: presentation only.

## 2. Passive acoustic monitoring program

```yaml
passive_acoustic_program:
  program_id: null
  operator_institution_ids: []
  purpose_refs: []
  target_profile_ids: []
  target_question_ids: []
  geographic_scope_ids: []
  start_date: null
  end_date: null
  method_revision_ids: []
  deployment_ids: []
  privacy_policy_ref: null
  ethics_or_access_refs: []
  status: PROPOSED
```

Candidate statuses:

- PROPOSED
- AUTHORIZED
- ACTIVE
- PAUSED
- COMPLETED
- ARCHIVED

Program purpose never creates a species fact. A program targeting a rare call does not establish that the species is present.

## 3. Method revision

Long-running programs must version their method.

```yaml
acoustic_method_revision:
  method_revision_id: null
  program_id: null
  effective_from: null
  effective_until: null
  recorder_requirements: []
  recording_schedule_spec: null
  file_format_or_quality_class: null
  detector_model_refs: []
  review_protocol_ref: null
  site_selection_method: null
  notes: null
```

Changing recorder hardware, microphone placement, sampling schedule, classifier or site-selection method creates a new revision.

Historical data stays attached to the method used at the time.

## 4. Recorder deployment

```yaml
acoustic_recorder_deployment:
  deployment_id: null
  program_id: null
  listening_site_id: null
  device_id: null
  installed_at: null
  recovered_at: null
  intended_recording_window: null
  actual_recording_window: null
  duty_cycle_ref: null
  placement_description: null
  device_orientation_ref: null
  metrology_state_ref: null
  clock_state_ref: null
  power_or_storage_state_refs: []
  environmental_context_refs: []
  access_method_ref: null
  deployment_status: null
```

Candidate deployment statuses:

- PLANNED
- INSTALLED
- RECORDING
- PARTIAL_DATA
- RECOVERED
- LOST_DEVICE
- FAILED_DEPLOYMENT
- UNKNOWN_STATE

A deployment can remain scientifically useful even if it ends early.

## 5. Recording effort

```yaml
acoustic_recording_effort:
  effort_id: null
  deployment_id: null
  scheduled_start: null
  scheduled_end: null
  realized_start: null
  realized_end: null
  scheduled_duration_class: null
  realized_duration_class: null
  duty_cycle_ref: null
  gaps: []
  coverage_quality: null
  source_recording_ids: []
```

Recording effort must survive as its own object because absence evidence depends on it.

A site with 100 hours of valid recordings and a site with 5 minutes cannot be compared by raw detection count without later analysis.

## 6. Data gap

```yaml
acoustic_data_gap:
  gap_id: null
  effort_id: null
  start_time: null
  end_time: null
  cause_state: null
  supporting_refs: []
  confidence: null
```

Candidate causes:

- BATTERY_EXHAUSTED
- STORAGE_FULL
- CLOCK_FAILURE
- MICROPHONE_DAMAGE
- WEATHER_OBSCURATION
- WATER_INTRUSION
- DEVICE_MOVED
- DEVICE_OBSTRUCTED
- FILE_CORRUPTION
- COMMUNICATION_FAILURE
- UNKNOWN

A gap does not imply the target stopped calling.

## 7. Raw recording integrity

The existing Soundscapes `acoustic_recording` remains the recording authority.

Pass 167 adds review-facing metadata only:

```yaml
recording_integrity_review:
  review_id: null
  recording_id: null
  deployment_id: null
  integrity_state: null
  clipping_state: null
  noise_state: null
  timestamp_quality_ref: null
  usable_for_target_profiles: []
  unusable_for_target_profiles: []
  notes: null
```

A recording may be usable for a loud low-frequency source and unusable for a quieter high-frequency source.

## 8. Candidate detection

Automated detection creates a candidate, never an acoustic fact.

```yaml
acoustic_detection_candidate:
  candidate_id: null
  recording_id: null
  detector_id: null
  detector_revision: null
  target_profile_id: null
  detected_start: null
  detected_end: null
  confidence_class: null
  feature_summary: null
  review_state: PENDING
  source_refs: []
```

Candidate review states:

- PENDING
- AUTO_FILTERED
- HUMAN_REVIEW_PENDING
- VALID_FOR_SCOPE
- MISCLASSIFIED
- NON_TARGET_SOUND
- DUPLICATE_EVENT
- INSUFFICIENT_AUDIO
- UNRESOLVED

Do not store classifier probability as species truth.

## 9. Detection review

```yaml
acoustic_detection_review:
  detection_review_id: null
  candidate_id: null
  reviewer_actor_or_system_id: null
  reviewed_at: null
  method_revision_ref: null
  source_audio_refs: []
  comparison_profile_refs: []
  determination: null
  determined_profile_id: null
  source_identity_claim_id: null
  confidence: null
  notes: null
```

Important distinction:

```text
call pattern identified
≠ source species confirmed
≠ individual identified
```

Mimicry, overlapping calls, machinery, echoes and edited/public recordings can all break those equivalences.

## 10. Duplicate acoustic event linkage

One sound event can be detected by multiple devices.

```yaml
acoustic_event_linkage_review:
  linkage_id: null
  candidate_or_detection_ids: []
  proposed_sound_event_id: null
  timing_evidence_refs: []
  location_evidence_refs: []
  profile_evidence_refs: []
  determination: SAME_EVENT | DISTINCT_EVENTS | UNRESOLVED
  confidence: null
```

Multiple recorders hearing one chorus does not create multiple independent biological events.

## 11. Acoustic coverage revision

Coverage is a claim derived from deployments and observations. It is never a perfect radius.

```yaml
acoustic_coverage_revision:
  coverage_revision_id: null
  program_id: null
  site_or_area_id: null
  valid_window: null
  target_profile_ids: []
  deployment_ids: []
  known_obstruction_refs: []
  environmental_context_refs: []
  detectable_context_notes: []
  unsampled_area_refs: []
  confidence: null
```

Coverage may differ by:

- frequency range;
- source loudness;
- time of day;
- vegetation;
- wind;
- rain;
- water depth;
- topography;
- building geometry;
- microphone placement;
- device revision.

No universal “heard within X blocks” contract is created here.

## 12. Non-detection assessment

```yaml
acoustic_non_detection:
  non_detection_id: null
  target_profile_id: null
  effort_ids: []
  coverage_revision_id: null
  relevant_activity_window_refs: []
  environmental_context_refs: []
  assessment_state: null
  interpretation_claim_ids: []
```

Candidate states:

- VALID_NON_DETECTION_FOR_SCOPE
- EFFORT_INSUFFICIENT
- COVERAGE_INSUFFICIENT
- TARGET_NOT_EXPECTED_TO_SIGNAL
- RECORDING_GAP
- METHOD_NOT_COMPARABLE
- UNRESOLVED

`VALID_NON_DETECTION_FOR_SCOPE` still does not mean ABSENT.

## 13. Detection series

```yaml
acoustic_detection_series:
  series_id: null
  program_id: null
  target_profile_id: null
  valid_from: null
  valid_until: null
  validated_detection_ids: []
  non_detection_ids: []
  effort_ids: []
  method_revision_ids: []
  comparability_assessment_ids: []
```

A detection series can support:

- timing shifts;
- repeated site use;
- seasonal presence hypotheses;
- restoration monitoring;
- migration-window comparisons;
- urban-noise studies;
- long-term public-memory archives.

It does not directly support abundance without a separate model and evidence.

## 14. Comparability assessment

```yaml
acoustic_comparability_assessment:
  assessment_id: null
  series_or_dataset_ids: []
  compared_method_revision_ids: []
  comparable_dimensions: []
  non_comparable_dimensions: []
  adjustment_refs: []
  conclusion: DIRECTLY_COMPARABLE | COMPARABLE_WITH_LIMITS | TREND_ONLY | NOT_COMPARABLE | UNRESOLVED
```

Example: a new ultrasonic recorder may improve Noibat-like call detection while making raw counts incomparable with an older human-audible recorder series.

## 15. Aggregate monitoring product

```yaml
acoustic_monitoring_product:
  product_id: null
  program_id: null
  product_type: null
  source_series_ids: []
  method_revision_ids: []
  spatial_scope: null
  temporal_scope: null
  privacy_transform_ref: null
  uncertainty_notes: []
  publication_ref: null
```

Possible products:

- detection history;
- presence window estimate;
- chorus timing index;
- soundscape diversity summary;
- disturbance comparison;
- occupancy-style research input;
- restoration before/after comparison.

The narrative layer should prefer qualitative or bounded products unless a quantitative model is authored.

## 16. Sensitive location protection

Acoustic detections can reveal nesting, roosting, release or congregation sites.

Public products may:

- coarsen coordinates;
- delay publication;
- hide exact timestamps;
- publish a regional presence class;
- retain exact source data under restricted access.

The public map never needs to expose every scientific coordinate.

## 17. Mimicry and uncertain source identity

Chatot provides an official Pokémon precedent for mimicry of other Pokémon calls and human speech.

Therefore:

- a call library stores acoustic pattern, not guaranteed biological source;
- mimicry evidence creates a source-attribution problem;
- a classifier may correctly detect a target-like pattern and still be wrong about who produced it;
- an individual mimic can create repeated false “rare species” alerts;
- later confirmation revises interpretation without deleting earlier detections.

Do not create a universal mimic system for all Pokémon.

## 18. Ultrasonic and non-human frequency ranges

Noibat provides an official precedent for sound beyond normal human hearing.

A survey may therefore author equipment classes such as:

- HUMAN_AUDIBLE_ONLY
- EXTENDED_HIGH_FREQUENCY
- UNDERWATER_ACOUSTIC
- BROAD_BAND_RESEARCH

These are world-technology descriptors only until Technology canon defines them.

They do not grant exact PTU perception ranges.

## 19. Environmental interference

Pass 167 may reference weather, vegetation, urban noise and infrastructure state as explanatory context.

It must not invent acoustic physics from battle mechanics.

Forbidden shortcuts:

- battle LoS → acoustic propagation;
- wall blocker → guaranteed sound occlusion;
- Manhattan distance → hearing range;
- Rain Weather → a fixed detection penalty;
- Soundproof → mundane deafness;
- Sonic keyword → louder ambient sound;
- Noibat lore → perfect echolocation map;
- Chatot mimicry → Guile or automatic deception.

## 20. Minecraft/Cobblemon projection

Minecraft audio remains presentation.

The adapter may eventually render:

- recorder blocks/models;
- deployment UI;
- recording status indicators;
- spectrogram-like interfaces;
- captions for accessible playback;
- coarse map coverage;
- retrieval interactions;
- player-facing review queues.

It must never decide:

- that a played sound was scientifically recorded;
- source identity;
- detector confidence;
- species presence;
- recorder coverage;
- abundance;
- acoustic propagation physics;
- exact PTU Sonic effects.

Loaded entities are not a passive-acoustic census.

## 21. Chronicle writeback

A monitoring run can write:

- deployment history;
- data gaps;
- validated detections;
- unresolved calls;
- method changes;
- equipment failures;
- location-protection decisions;
- monitoring products;
- institutional interpretation changes.

It should not write:

- population count from raw detection count;
- death from silence;
- migration success from one call;
- individual identity without corroboration;
- capture eligibility;
- combat status;
- spawn multipliers.

## 22. Encounter contract A — Recorder Array Retrieval After Storm

Narrative premise: a long-running marsh array contains the only recordings spanning a severe storm. Several units are overdue for retrieval, and one site is difficult to access.

FULL version:

- technicians or PCs traverse a storm-altered route;
- wildlife can withdraw rather than fight;
- devices occupy meaningful world positions;
- a damaged path can change the safe route;
- retrieval state persists individually per recorder;
- any combat remains separate from scientific interpretation.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED for battle targeting;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if traversal, withdrawal or interception is tactical;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if a legal combat effect requires it;
- terrain/weather/hazards/zones/reactions — BLOCKING if storm debris, unstable ground or weather changes combat state;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for WITHDRAW, PROTECT_TECHNICIAN, REACH_DEVICE and CLEAR_ROUTE;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:

World state resolves the storm route, technicians, wildlife withdrawal and device locations first. Any confrontation occurs on a stable static arena using normal battle targeting and movement. Recorder recovery resolves afterward. The battle never determines whether the recordings are valid.

## 23. Encounter contract B — Rare Call Alert at Chorus Marsh

Narrative premise: an automated classifier repeatedly flags a call associated with a rarely observed Pokémon. The raw audio is genuine. Source identity remains uncertain because of overlapping choruses and possible mimicry.

FULL version:

- players compare recorder sites and time windows;
- the target source may move or remain unseen;
- a mimic or overlapping source can create misleading but authentic detections;
- the best outcome may remain UNRESOLVED;
- no battle is required.

Battle dependencies:

None for the core investigation.

If an independent encounter occurs, use only the capabilities required by that battle. Do not give the classifier or recording any combat effect.

## 24. Encounter contract C — Ultrasonic Cave Survey

Narrative premise: people hear almost nothing in a cave section, while an authored extended-frequency recorder logs repeated high-frequency patterns. The research team wants to determine whether one source, several sources or reflections explain the detections.

FULL version:

- survey equipment has placement and retrieval state;
- actors move through cave sections;
- wildlife can avoid the party;
- an actual Sonic Move or Ability only functions if possessed and supported by PTU runtime evidence;
- cave acoustics remain narrative/scientific unless a validated environmental mechanic exists.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED for battle only;
- base movement legality — VERIFIED;
- complete movement — BLOCKING if crossing/withdrawal is tactical;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL;
- damage — PARTIAL;
- status lifecycle — PARTIAL for exact status-producing Moves;
- terrain/weather/hazards/zones/reactions — BLOCKING if darkness, unstable surfaces or acoustic zones become tactical mechanics;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for SEARCH/WITHDRAW/REACH_EXIT-style behavior;
- adapter/playback — BLOCKING.

REDUCED version:

The cave survey, detector readings and wildlife movement resolve outside battle. If a confrontation occurs, freeze a legal static arena. Any sound-based combat effect must come from a specific legal Move/Ability and current engine evidence, never from the survey layer.

## 25. Encounter contract D — Hydrophone Mooring Recovery

Narrative premise: a long-term underwater listening station stopped reporting. The last uploaded file was normal. Operators need the device back before interpreting the gap.

FULL version dependencies:

- complete movement — BLOCKING for underwater traversal or dynamic withdrawal;
- terrain/weather/hazards/zones/reactions — BLOCKING if current, depth or debris affect combat;
- AI tactical policy — BLOCKING for RETRIEVE_DEVICE, WITHDRAW or PROTECT_DIVER;
- adapter/playback — BLOCKING;
- standard verified/partial families remain as classified above for any actual battle.

REDUCED version:

Freshwater/Maritime world state resolves access and recovery. Any battle occurs separately on a static validated arena. A silent hydrophone never proves ecological silence.

## 26. Permanent engine boundary

As of Pass 167, this protocol assumes the permanent categories remain:

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

A narrow implemented reaction, Sonic behavior, effect-roll modifier, Status Move, Ability or Move Special does not promote its family.

## 27. Explicit non-inferences

Do not infer any of the following:

- acoustic detection → Pokémon present at exact recorder tile;
- repeated calls → multiple individuals;
- call volume → distance;
- call similarity → same individual;
- detector confidence → truth probability stored in Chronicle;
- recorder silence → Pokémon absent;
- recorder failure → sabotage;
- mimicry → malicious intent;
- ultrasonic detection → Blindsense;
- Blindsense → recorder-like range;
- Soundproof → inability to hear mundane sounds;
- Sonic Move → environmental monitoring capability;
- loud ambient noise → Accuracy or Initiative penalty;
- acoustic disturbance → Status;
- Minecraft sound playback → authoritative sound event;
- many loaded Pokémon → high acoustic abundance;
- rare-call detection → rare spawn.

## 28. Canon decisions still required

Before this protocol can become active canon, Ouros must decide:

- which institutions operate passive-acoustic programs;
- what recorder technologies exist;
- whether underwater hydrophones exist;
- whether automated classifiers exist and how advanced they are;
- what frequency ranges devices can record;
- how site privacy works;
- which call libraries exist at campaign start;
- what data are public versus research-restricted;
- how offline world time advances recording effort;
- which Pokémon populations have authored call behavior;
- how Caelo changes Sonic, Soundproof, Blindsense or relevant equipment.

Until then, all data structures and encounters in this protocol remain proposed design candidates.