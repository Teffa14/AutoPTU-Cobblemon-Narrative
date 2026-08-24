# Ouros Visual Records, Photography & Imaging Provenance Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon.
Date: 2026-08-23

## Purpose

Ouros already knows how to store observations, publications, archives, identities, scientific measurements, sensitive research and public memory. This layer defines the missing visual-record boundary: how a photograph, video frame, scan or camera-trap image comes into existence, what it actually depicts, how it is transformed, how it is catalogued and which later claims may rely on it.

The central rule is simple:

`physical scene -> capture event -> source visual record -> derived visual record -> observation/identification claims -> publication/archive use`

No later step rewrites an earlier one.

## 1. Visual record

```yaml
visual_record:
  visual_record_id: null
  record_type: STILL_IMAGE
  source_capture_id: null
  parent_visual_record_id: null
  storage_asset_ref: null
  checksum_or_integrity_ref: null
  created_at: null
  created_by_actor_id: null
  owning_or_custody_refs: []
  access_state: PRIVATE
  sensitivity_tags: []
  preservation_state: CURRENT
```

Candidate record types:

- STILL_IMAGE
- VIDEO_CLIP
- VIDEO_FRAME
- FILM_FRAME
- SCAN
- CAMERA_TRAP_IMAGE
- INSTITUTIONAL_STILL
- SCIENTIFIC_IMAGE
- PUBLICITY_IMAGE
- PORTRAIT
- DOCUMENTARY_IMAGE

This object is the durable image identity. Publication state belongs to Media. Institutional collection state belongs to Archives/Museums.

## 2. Capture event

```yaml
image_capture_event:
  capture_id: null
  device_id: null
  operator_actor_id: null
  location_id: null
  raw_timestamp: null
  corrected_time_ref: null
  position_or_station_ref: null
  viewing_direction_band: null
  environmental_state_refs: []
  subject_candidate_refs: []
  intervention_context_id: null
  access_authorization_refs: []
  created_visual_record_ids: []
```

A capture event records where and how the image was made. It does not decide what every visible subject is.

## 3. Capture intervention context

```yaml
capture_intervention_context:
  intervention_context_id: null
  observer_distance_band: null
  subject_awareness_observed: UNKNOWN
  subject_response_observed: NONE
  remote_capture: false
  bait_or_food_used: false
  call_or_music_used: false
  flash_or_light_used: false
  scan_or_sensor_used: false
  staged_or_directed: false
  physical_approach: false
  pursuit_observed: false
  battle_or_crisis_context: false
  method_notes: null
```

Suggested subject-response values:

- NONE
- ORIENTED_TOWARD_OBSERVER
- APPROACHED
- RETREATED
- STARTLED
- STOPPED_ACTIVITY
- CHANGED_ROUTE
- DEFENSIVE_RESPONSE
- UNKNOWN

These fields describe what was observed. They do not infer stress, fear, aggression or consent beyond evidence.

## 4. Original versus derivative

```yaml
visual_derivative:
  derivative_record_id: null
  source_record_id: null
  transformation_type: null
  created_at: null
  created_by_actor_id: null
  transformation_parameters_ref: null
  content_added: false
  content_removed: false
  evidence_use_restriction: null
```

Candidate transformations:

- CROP
- ROTATE
- BRIGHTNESS_CONTRAST
- COLOR_CORRECTION
- NOISE_REDUCTION
- SHARPEN
- RESIZE
- ANNOTATION
- REDACTION
- COMPOSITE
- STICKER_FRAME_FILTER
- PUBLICATION_LAYOUT
- FORMAT_MIGRATION

Editing is not automatically falsification. Evidence users must know which version they are looking at and what transformations occurred.

A decorative derivative can remain culturally important while being unsuitable for exact scientific interpretation.

## 5. Image observation

```yaml
visual_observation:
  visual_observation_id: null
  visual_record_id: null
  observer_actor_id: null
  observed_at: null
  region_or_bbox_ref: null
  observation_type: null
  observed_properties: []
  confidence: null
  method: HUMAN_REVIEW
  supersedes_observation_id: null
```

Candidate observation types:

- ACTOR_PRESENT
- POKEMON_PRESENT
- OBJECT_PRESENT
- STRUCTURE_PRESENT
- BEHAVIOR_VISIBLE
- DAMAGE_VISIBLE
- TRACK_OR_SIGN_VISIBLE
- WEATHER_VISIBLE
- TEXT_OR_MARK_VISIBLE
- UNKNOWN_SUBJECT_VISIBLE

An image observation states what a reviewer thinks is visibly present. It is not an identity or causation conclusion.

## 6. Visual identification claim

```yaml
visual_identification_claim:
  claim_id: null
  visual_observation_id: null
  proposed_entity_ref: null
  proposed_species_ref: null
  basis_tags: []
  comparison_record_ids: []
  confidence: null
  reviewer_ids: []
  status: PROVISIONAL
  competing_claim_ids: []
```

Possible basis tags:

- DISTINCTIVE_MARKING
- KNOWN_EQUIPMENT
- LOCATION_AND_TIME
- BODY_SHAPE
- COLOR_PATTERN
- SCAR_OR_FEATURE
- ASSOCIATED_ACTOR
- TAG_OR_MARKER
- REPEATED_APPEARANCE
- EXPERT_REVIEW

Guardrails:

- same species + same nickname does not prove same Pokémon;
- same clothing does not prove same person;
- a blurry silhouette does not prove a rare species;
- a photographed actor near damage does not prove they caused it;
- a photographed Pokémon near a nest does not prove parentage;
- visual resemblance does not prove regional form or taxonomic novelty.

Identity resolution remains owned by Identity/Pokémon Agency/Taxonomy as applicable.

## 7. Camera and imaging device state

```yaml
imaging_device:
  device_id: null
  device_type: null
  owner_or_custodian_refs: []
  model_or_design_ref: null
  calibration_ref: null
  clock_ref: null
  storage_state_ref: null
  current_location_ref: null
  operational_state: READY
  last_verified_at: null
```

Candidate operational states:

- READY
- DEPLOYED
- OUT_OF_POWER
- STORAGE_FULL
- CLOCK_UNCERTAIN
- DAMAGED
- OBSTRUCTED
- RETRIEVED
- LOST
- UNKNOWN

A working camera does not guarantee a useful image. A calibrated device does not guarantee correct subject identification.

Timekeeping and Metrology remain authoritative for clocks, references and measurement quality.

## 8. Camera-trap deployment

```yaml
camera_trap_deployment:
  deployment_id: null
  device_id: null
  site_id: null
  installed_at: null
  intended_end_at: null
  retrieved_at: null
  trigger_method: null
  coverage_geometry_ref: null
  target_question_ref: null
  authorization_refs: []
  ethics_protocol_refs: []
  active_window_revisions: []
  maintenance_event_ids: []
  produced_record_ids: []
```

### Camera-trap rules

A deployment must preserve:

- where it was aimed;
- when it was active;
- downtime;
- obstruction;
- clock uncertainty;
- maintenance;
- whether lure/bait/call was used;
- whether the camera itself altered behavior;
- whether the site later changed physically.

No image during a deployment does not mean no Pokémon used the wider habitat.

No image during a documented downtime means almost nothing about occupancy.

## 9. Visual encounter / sequence record

```yaml
visual_sequence:
  sequence_id: null
  capture_or_deployment_ref: null
  ordered_visual_record_ids: []
  sequence_start: null
  sequence_end: null
  continuity_confidence: null
  missing_interval_refs: []
  interpretation_claim_ids: []
```

A burst or sequence can support motion/order claims only within its actual temporal coverage.

Do not infer what happened between missing frames.

## 10. Sensitive-location handling

```yaml
visual_location_disclosure:
  visual_record_id: null
  exact_location_visibility: RESTRICTED
  public_location_band: null
  restriction_reason_refs: []
  authorized_audience_refs: []
  redacted_derivative_id: null
```

This is important for:

- nests and Eggs;
- threatened populations;
- sacred/restricted sites;
- private homes;
- clinics;
- research subjects;
- evidence scenes;
- secure infrastructure;
- archaeological sites;
- rare-species locations.

The image may be publishable while exact coordinates remain restricted.

## 11. Human and Pokémon privacy / agency boundary

A photograph can be physically valid and still have restricted use.

For people, defer to Identity, Research Ethics, institutional policy and any future privacy canon.

For Pokémon:

- a wild Pokémon being visible does not make repeated pursuit acceptable;
- a partner being photographable does not imply consent to every publication context;
- a working Pokémon assignment does not grant unlimited publicity rights;
- a photographed Pokémon is not captured, owned, registered or available for capture because of the image.

Do not create an invented numeric consent score.

## 12. Research integration

Photography can create evidence for Science when the research method supports it.

Examples:

- first documented flowering date;
- repeated presence at a crossing;
- identifiable individual revisiting a site;
- progression of shoreline/forest/structure change;
- observed behavior under stated conditions;
- instrument panel state at a known time;
- damage progression between inspections.

The scientific claim remains separate from the image itself.

## 13. Media and public-memory integration

Media owns publication events.

Public Memory owns lasting social interpretations.

This layer supplies:

- source image;
- derivative used;
- caption/identification claim references;
- location disclosure state;
- capture context;
- provenance.

A viral image may be authentic and still be captioned incorrectly.

A corrected caption does not erase the earlier viral publication from Chronicle.

## 14. Archives and museums integration

Archives/Museums may preserve a visual record as a collection object.

The visual record remains the same underlying entity while:

- catalogue descriptions change;
- new identities are proposed;
- the file is migrated to new storage;
- a print is exhibited;
- a derivative is published;
- a negative/original is restricted;
- later research changes its interpretation.

A print, negative, scan and edited publication image can all be separate material/digital objects linked through provenance.

## 15. Public photography feedback loops

A photograph can change the world after publication.

Example chain:

`rare-looking image -> media attention -> visitor increase -> wildlife disturbance -> route/access response -> altered behavior -> later observations`

Each step must come from explicit systems. The photograph itself does not spawn crowds or alter wildlife automatically.

## 16. Visual-record uncertainty

Recommended confidence dimensions:

- capture authenticity;
- timestamp quality;
- location quality;
- subject visibility;
- identity confidence;
- behavioral-interpretation confidence;
- transformation provenance completeness;
- sequence continuity.

Do not collapse them into one score.

## 17. Minecraft projection

Minecraft may present:

- handheld camera items/models;
- tripods or fixed camera props;
- shutters/flash animation;
- photo UI;
- gallery walls;
- camera-trap blocks;
- images or thumbnails;
- restricted-coordinate redactions;
- retrieval/maintenance interactions.

Minecraft must not decide:

- who is in the image;
- whether an image proves a claim;
- whether a rare Pokémon was present outside captured frames;
- whether the photograph is original;
- whether editing invalidates it;
- whether publication is authorized;
- whether a wild Pokémon is capturable;
- whether a camera gives Perception or combat bonuses.

## 18. PTU boundary

Project evidence confirms Chronicler archive behavior exists in AutoPTU Python. This layer does not reinterpret ordinary photographs as Chronicler records automatically.

Any exact Photographer/Chronicler, Perception, Pokémon Education, Researcher, item or equipment mechanics must be validated separately against the project PTU/Caelo corpus and live implementation.

No camera-based bonus is implied by this design.

## 19. Encounter handoff

Most photography gameplay should remain overworld/non-combat.

When combat occurs, the server should freeze a battle snapshot and hand only battle-relevant actors/state to AutoPTU.

A camera, photographer, image archive or camera trap remains outside the tactical grid unless there is a validated reason to model it mechanically.

## 20. Failure-forward outcomes

A photography objective can end with:

- useful image, uncertain identity;
- clear image, behavior disturbed;
- no image, deployment technically successful;
- image obtained after the target left its expected route;
- wrong timestamp later corrected;
- original lost but verified derivative preserved;
- viral image later recaptioned;
- image too sensitive to publish;
- aesthetically poor image that is scientifically valuable;
- beautiful image that has little evidentiary value.

These are valid outcomes, not automatic quest failures.

## 21. Open canon decisions

Still unresolved:

- regional camera technology;
- whether film and digital systems coexist;
- institutional camera-trap networks;
- publication/privacy norms;
- sensitive wildlife-location policy;
- exact rules for photographing partnered Pokémon;
- whether visual records can be player-created persistent assets at scale;
- storage limits and archival compression policy;
- any PTU/Caelo Photographer/Chronicler mechanics;
- whether video/photography ever becomes a formal career circuit in Ouros.

Until reviewed, all examples remain proposed.