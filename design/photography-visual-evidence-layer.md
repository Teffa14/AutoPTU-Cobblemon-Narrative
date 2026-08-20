# Photography, Visual Evidence & Documentary Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros needs a durable model for photographs, video, camera traps, screenshots, scientific image records, documentary footage and public visual media.

The model must let one visual object move through research, cases, media, archives, museums and public memory without collapsing observation into truth.

## Core separation

```text
world event or physical scene
        ↓
capture opportunity
        ↓
primary visual record
        ↓
technical metadata and provenance
        ↓
classification / interpretation
        ↓
derivative edits and annotations
        ↓
publication / exhibit / case use
        ↓
actor knowledge and public belief
```

No lower layer should silently rewrite an upper layer.

## 1. Primary visual record

```yaml
visual_record:
  visual_record_id: null
  media_type: still|burst|video|scan|battle_replay_ref|other
  capture_time: null
  capture_location_id: null
  capture_actor_id: null
  capture_device_id: null
  source_asset_ref: null
  source_hash_or_integrity_ref: null
  camera_position_ref: null
  orientation_ref: null
  visible_subject_refs: []
  uncertain_subject_refs: []
  environmental_context_refs: []
  linked_event_refs: []
  access_policy_ref: null
  sensitive_location: false
  provenance_refs: []
  lifecycle_state: active
```

This record describes the capture. It does not certify the interpretation.

## 2. Capture context

A visual record can only support claims within its actual coverage.

Useful context fields:

```yaml
capture_context:
  context_id: null
  visual_record_id: null
  field_of_view_ref: null
  obstruction_refs: []
  lighting_state: null
  weather_state_ref: null
  time_of_day_ref: null
  camera_motion_state: null
  known_sensor_limitations: []
  observation_duration: null
  trigger_method: manual|motion|scheduled|event|unknown
  operator_notes: null
```

Ouros should avoid fake photographic certainty. A frame can show one side of a room while saying nothing about what happened outside the frame.

## 3. Classification record

```yaml
visual_classification:
  classification_id: null
  visual_record_id: null
  classifier_actor_or_system_id: null
  subject_candidate_ref: null
  classification_kind: species|individual|behavior|object|location|event|other
  confidence_band: low|medium|high|reviewed
  evidence_notes: []
  contradictory_classification_refs: []
  expert_review_ref: null
  created_at: null
  superseded_by: null
```

Multiple classifications may coexist.

A high-confidence classification can support a hypothesis. It does not create a new canonical Pokémon entity unless identity rules are satisfied.

## 4. Individual Pokémon re-identification

A visual match can become useful for persistent wildlife.

```yaml
visual_identity_match:
  match_id: null
  visual_record_id: null
  candidate_pokemon_id: null
  matching_features: []
  conflicting_features: []
  confidence_band: null
  corroborating_record_refs: []
  reviewed_by: null
  status: proposed|supported|confirmed|rejected
```

Never create a persistent Pokémon entity only because an automated classifier thinks two similar Pokémon are the same individual.

Reliable identity can come from authored marks, existing canonical identifiers, tagged research records, repeated distinctive features or other validated evidence.

## 5. Derivative visual object

```yaml
visual_derivative:
  derivative_id: null
  parent_visual_record_id: null
  parent_derivative_id: null
  transformation_kind: crop|brightness|contrast|annotation|redaction|composite|caption|filter|other
  transformation_notes: []
  created_by: null
  created_at: null
  intended_use: research|case|publication|exhibit|personal|accessibility|other
  integrity_status: documented|incomplete|unknown
```

A crop is allowed. A caption is allowed. A redaction is allowed.

The system must preserve that these are derivatives.

## 6. Research use

Visual records can connect to the science layer as observations.

Examples:

- behavior observed at a nesting site;
- migration timing;
- repeat appearance of an individual;
- plant response around a Pokémon population;
- habitat use at night;
- absence of detections from a functioning monitored corridor.

The science layer decides whether that evidence supports a hypothesis.

A photograph does not bypass sampling design, replication or uncertainty.

## 7. Camera-trap network

```yaml
camera_station:
  station_id: null
  location_id: null
  operator_institution_id: null
  device_id: null
  deployed_at: null
  removed_at: null
  operational_state: active|degraded|offline|missing|retired
  coverage_description: null
  trigger_mode: null
  maintenance_refs: []
  access_policy_ref: null
  sensitive_location: false
  dataset_refs: []
```

A network can feed:

- wildlife monitoring;
- route-use studies;
- conservation work;
- research programs;
- crisis assessment;
- case evidence;
- infrastructure inspection.

A camera station is a technical asset. Existing technology/infrastructure rules should govern outages and maintenance.

## 8. Empty frames and missing data

Never equate no detection with proven absence.

Store:

```yaml
visual_sampling_window:
  station_id: null
  window_start: null
  window_end: null
  expected_operational_time: null
  confirmed_operational_time: null
  captured_record_count: 0
  unknown_data_loss: false
  interpretation_refs: []
```

This supports stories where the absence itself becomes interesting only after equipment and baseline are checked.

## 9. Case and evidence integration

A case may attach a visual record through the existing evidence system.

The case layer remains responsible for:

- custody;
- access;
- evidence status;
- hypothesis links;
- accusation boundaries.

This layer contributes:

- source capture;
- visual provenance;
- derivatives;
- classifications;
- technical limitations.

A photograph of an actor near a location does not prove guilt or motive.

## 10. Media and publication integration

A publication may use a derivative rather than the primary record.

Store the relationship:

```yaml
visual_publication_use:
  publication_id: null
  visual_source_ref: null
  derivative_ref: null
  caption_claim_ref: null
  crop_context_loss_notes: []
  permission_or_access_ref: null
```

The caption is a claim. The visual record is a source. They are not the same object.

## 11. Archive and museum integration

Archives can preserve original media, derivatives, contact sheets, field notes and catalog records.

Museums can display a reproduction without relocating the source object.

Historic photographs can expose:

- vanished buildings;
- old infrastructure;
- former habitats;
- uniforms from earlier periods;
- previous owners/custodians;
- forgotten public events;
- misidentified specimens;
- landscape change.

Historic visual evidence should remain subject to date, provenance and interpretation.

## 12. Player photography and privacy

Player-created images need explicit privacy boundaries.

Do not automatically create public records from:

- screenshots taken inside a private home;
- private messages rendered in UI;
- another player's private inventory;
- hidden case evidence;
- private dream/psychic content;
- redacted research locations;
- backstage or medical areas with restricted access.

A future Minecraft adapter should expose only server-authorized visual metadata to world systems.

## 13. Photography as play

Photography can produce meaningful play without becoming a new combat stat.

Possible loops:

- document three distinct behaviors;
- revisit a route under different season/time state;
- set and maintain camera traps;
- compare an old photo to a changed location;
- identify which visual source a newspaper reused;
- reconstruct a route from sequential images;
- document restoration work;
- photograph a recurring Pokémon without attempting capture;
- collect public-event history;
- build a visual field guide.

If a Skill check is required, PTU/Caelo must determine the governing Skill and exact resolution.

## 14. Chronicler boundary

Python AutoPTU has Chronicler archive and Cinematic Analysis runtime behavior.

That does not mean:

- every camera user is a Chronicler;
- taking a screenshot creates an archive record;
- a visual record grants Targeted Profiling;
- battle footage grants legal scouting information automatically;
- visual documentation is mechanically perfect.

A future implementation may connect validated visual records to Chronicler mechanics only when the exact Feature contract is ported and the action is legal.

## 15. Battle documentary records

AutoPTU battle results should come from semantic engine events, not inferred from rendered pixels.

Recommended split:

```text
AutoPTU authoritative battle transcript
        ↓
replay/documentary metadata
        ↓
Minecraft/Cobblemon visual playback
        ↓
optional recorded media object
```

A screenshot of a battle is a visual record.

The transcript remains the authoritative mechanical record.

## 16. Encounter implementation contracts

### A. Camera Trap Recovery

Narrative premise:
A research station stops reporting after previously recording unusual movement through a protected corridor.

Full version:
- enter a dynamic corridor;
- locate the device;
- protect or recover equipment;
- wildlife can route around combatants;
- environmental state can alter access;
- encounter AI reacts to retreat paths.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED baseline;
- base movement legality: VERIFIED baseline;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if interception/forced displacement is used;
- core calculations: VERIFIED baseline;
- action economy/initiative: VERIFIED baseline;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING for dynamic corridor hazards;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Reduced version:
The search and device recovery occur in overworld state. If battle occurs, AutoPTU receives a static arena. The device remains outside tactical resolution. After the legal battle result, world state records whether the station was reached and recovered.

### B. Historic Photograph Survey

Narrative premise:
An archive photograph appears to show a vanished structure beside a route that has changed over decades.

Full version:
Mostly noncombat. If the site is occupied by hostile or territorial Pokémon, a battle can occur while survey objectives remain external to the grid.

Dependencies:
- static battle requires only currently verified/basic families plus any exact Moves/Abilities selected;
- no custom camera mechanics required;
- no dynamic terrain required unless later authored.

Reduced version:
Already the preferred implementation. Visual comparison, surveying and interpretation remain overworld/research actions.

### C. Press Gallery Incident

Narrative premise:
During a public battle or festival, an unexpected incident produces multiple conflicting photographs and eyewitness accounts.

Full version:
If the incident becomes tactical, civilians move, exits matter and actors may attempt to protect or reach zones.

Additional dependencies:
- complete movement/interception: BLOCKING for true evacuation traffic;
- terrain/weather/hazards/zones/reactions: BLOCKING if venue hazards change;
- AI tactical policy: BLOCKING for objective-aware civilians/opponents;
- adapter/playback: BLOCKING.

Reduced version:
Resolve the battle as a normal legal encounter. Generate visual records from documented camera positions and world-state events after authoritative resolution. Public interpretation occurs through media/public-memory systems.

## 17. Minecraft/Cobblemon boundary

Minecraft may render cameras, photographs, frames, galleries and viewing stations.

It must not become the authority for:

- PTU damage;
- hit/crit/status;
- proof that a Pokémon is the same individual;
- evidence authenticity;
- Player knowledge;
- hidden-case truth;
- Chronicler Feature activation;
- battle scouting bonuses.

The adapter should transmit identifiers and presentation data, then consume authorized results.

## Canon promotion checklist

Before any visual system becomes canon:

1. Define available camera technology by region.
2. Define privacy/access conventions.
3. Extract exact PTU/Caelo Chronicler and relevant Skill rules.
4. Decide how image provenance is stored.
5. Define sensitive-location redaction policy.
6. Confirm Minecraft/Cobblemon technical hooks.
7. Confirm whether battle replays derive from semantic transcripts.
8. Define how persistent Pokémon identity can be visually corroborated.
9. Ensure edited copies never overwrite primary records.
10. Ensure no generated visual interpretation silently becomes world truth.
