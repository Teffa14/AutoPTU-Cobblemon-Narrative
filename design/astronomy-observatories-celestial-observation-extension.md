# Ouros Astronomy, Observatories & Celestial Observation Extension

Status: proposed systems design. Not established canon.

## Purpose

Ouros already has a scientific method, an authoritative calendar, observed weather, mythology, archives, photography, cartography, public events, tourism, technology, maintenance and anomaly handling. This extension coordinates the persistent operational state of astronomical observation across those systems.

It owns:
- observing sites and their sky-access context;
- observing assets and readiness references;
- predicted observing windows;
- observation sessions;
- exact detections and non-detections;
- public observing events as observation-facing state;
- astronomical interpretation handoffs;
- celestial-event follow-up into terrestrial fieldwork.

It does not replace Science, Calendar, Weather, Myth, Technology, Event Operations, Cartography, Geology or Material Culture.

## Authority boundaries

Science owns:
- research questions;
- datasets;
- hypotheses;
- analyses;
- claims;
- review and publication.

Seasonality/Calendar owns:
- world date and time;
- recurring temporal cycles;
- authoritative local time context.

Weather owns:
- observed atmospheric conditions;
- forecasts and operational weather notices.

Myth/Deep History owns:
- constellation traditions;
- celestial myths;
- ritual interpretations;
- historical claims.

Technology/Maintenance owns:
- equipment identity;
- power/service dependencies;
- repair and operational condition.

Cartography owns:
- mapped search regions;
- survey products;
- spatial revisions.

Geology/Material Culture owns:
- recovered meteorite or impact material;
- provenance of physical samples;
- physical custody/condition handoffs.

Event Operations/Tourism owns:
- visitor capacity;
- public-event logistics;
- queues, access and destination pressure.

Ouros Astronomy owns the observation-specific coordination between those systems.

## Core separation

Keep this sequence explicit:

```text
world time
  -> predicted observing window
  -> actual site access / instrument readiness / sky visibility
  -> observation session
  -> detection or non-detection records
  -> Science dataset / analysis
  -> research claim
  -> publication / public interpretation / mythic comparison
  -> optional field-search lead
```

Never collapse it into:

```text
meteor scheduled -> meteor item spawns
```

or:

```text
constellation visible -> supernatural claim true
```

## 1. Observing site

```yaml
celestial_observing_site:
  site_id: null
  location_id: null
  site_type: null
  institution_ids: []
  observing_asset_ids: []
  sky_access_profile_id: null
  ordinary_access_state: OPEN
  public_access_state: CLOSED
  maintenance_refs: []
  infrastructure_refs: []
  weather_station_refs: []
  light_interference_observation_ids: []
  field_site_refs: []
  historical_observation_ids: []
  public_memory_refs: []
  status: ACTIVE
```

Possible site types:
- research_observatory;
- mountain_observing_station;
- radio_observation_site;
- university_rooftop;
- community_skywatch_site;
- historical_observing_platform;
- mobile_field_station;
- temporary_observing_camp.

These are worldbuilding categories, not a canon technology list.

## 2. Observing asset

An asset is a persistent world object referenced through Technology/Equipment/Maintenance.

```yaml
observing_asset_ref:
  asset_id: null
  asset_type_claim: null
  owning_system_ref: null
  installed_site_id: null
  current_operational_state: null
  calibration_record_refs: []
  maintenance_refs: []
  access_scope_refs: []
  supported_method_tags: []
```

The extension never invents a mechanical bonus from an instrument.

An asset can be operational while a session fails because:
- the target was not visible;
- weather changed;
- the observing window was wrong;
- staff were unavailable;
- the instrument pointed elsewhere;
- the hypothesis was wrong;
- the event simply produced no detectable signal.

## 3. Celestial subject reference

A subject reference identifies what observers think they are trying to observe.

```yaml
celestial_subject_ref:
  subject_ref_id: null
  public_label: null
  scientific_label_claim_ids: []
  mythic_subject_refs: []
  identity_confidence: provisional
  canonical_world_fact_refs: []
  known_observation_ids: []
  unresolved_identity_questions: []
```

The object can remain provisionally identified for years.

Do not force every light, radio signal, streak or recurring pattern into a known object class.

## 4. Predicted observing window

```yaml
observing_window:
  window_id: null
  subject_ref_ids: []
  generated_by_actor_or_institution_ids: []
  prediction_method_ref: null
  location_scope_ids: []
  start_world_time: null
  end_world_time: null
  expected_visibility_conditions: []
  confidence: provisional
  revision: 1
  supersedes_window_id: null
  source_measurement_ids: []
  publication_refs: []
  status: UPCOMING
```

Candidate states:
- UPCOMING;
- ACTIVE;
- MISSED;
- OBSERVED;
- CLOUD_OBSCURED;
- SITE_UNAVAILABLE;
- CANCELLED;
- SUPERSEDED;
- CLOSED_WITHOUT_DETECTION.

A window is a prediction object. It never guarantees the target appears.

## 5. Session

```yaml
observation_session:
  session_id: null
  site_id: null
  window_id: null
  start_world_time: null
  end_world_time: null
  observer_ids: []
  instrument_ids: []
  method_refs: []
  weather_observation_refs: []
  sky_visibility_observation_refs: []
  access_state_ref: null
  detection_ids: []
  non_detection_ids: []
  media_refs: []
  field_note_refs: []
  dataset_handoff_ids: []
  status: COMPLETE
```

A session can be scientifically useful even when no target is detected.

## 6. Sky visibility observation

```yaml
sky_visibility_observation:
  observation_id: null
  site_id: null
  observed_at: null
  observer_ids: []
  cloud_observation_refs: []
  artificial_light_observation_refs: []
  horizon_obstruction_refs: []
  qualitative_visibility_band: null
  instrument_specific_notes: []
  source_refs: []
```

No `visibility_band` becomes a PTU Accuracy modifier by itself.

## 7. Light-interference state

This extension can store evidence that artificial light affected observation.

```yaml
light_interference_observation:
  observation_id: null
  site_id: null
  source_location_refs: []
  observed_at: null
  observer_ids: []
  measurement_refs: []
  affected_method_refs: []
  confidence: provisional
  related_public_space_refs: []
  related_infrastructure_refs: []
  mitigation_proposal_refs: []
```

Any decision to alter street lighting belongs to Civic/Infrastructure systems.

Astronomy can supply evidence, not unilateral authority.

## 8. Detection record

```yaml
celestial_detection:
  detection_id: null
  session_id: null
  observer_or_instrument_ids: []
  timestamp: null
  site_id: null
  subject_ref_id: null
  detection_type: null
  raw_record_refs: []
  direction_or_region_ref: null
  qualitative_strength: null
  identity_claim_ids: []
  confidence: provisional
  corroborating_detection_ids: []
  contradictory_detection_ids: []
```

Possible detection types:
- visual_point;
- visual_track;
- transient_flash;
- streak;
- recurring_pattern;
- instrument_signal;
- photographic_detection;
- other_observed_signal.

These labels are descriptive. They do not establish cosmology.

## 9. Non-detection

Non-detections need provenance too.

```yaml
celestial_non_detection:
  non_detection_id: null
  session_id: null
  subject_ref_id: null
  expected_window_id: null
  observation_duration: null
  instrument_ids: []
  visibility_refs: []
  reason_state: UNKNOWN
  confidence: null
```

Possible reason states:
- target_not_seen;
- weather_obscured;
- horizon_obstructed;
- equipment_unavailable;
- session_ended_early;
- observation_gap;
- other_documented_reason;
- unknown.

Do not automatically turn a non-detection into evidence that the subject does not exist.

## 10. Observation reconciliation

Multiple observers may report one event differently.

```yaml
observation_reconciliation:
  reconciliation_id: null
  candidate_detection_ids: []
  timestamp_alignment_refs: []
  geographic_alignment_refs: []
  instrument_method_refs: []
  merged_event_candidate_id: null
  unresolved_detection_ids: []
  analyst_ids: []
  analysis_ref: null
  confidence: provisional
```

Four reports can describe:
- one event;
- several events;
- one event plus an unrelated signal;
- evidence too weak to reconcile.

## 11. Public observing event handoff

```yaml
public_skywatch_handoff:
  skywatch_id: null
  observing_window_id: null
  event_instance_ref: null
  site_id: null
  public_capacity_ref: null
  staff_assignment_refs: []
  access_refs: []
  weather_notice_refs: []
  interpretation_material_refs: []
  scientific_session_ids: []
  public_observation_summary_ref: null
```

A public event may be successful even if the target is clouded out.

Potential lasting outputs:
- photographs;
- oral histories;
- public-memory event;
- future signup demand;
- revised interpretation materials;
- no scientific detection at all.

## 12. Myth and constellation handoff

A constellation is a culturally or scientifically defined grouping, not an objective segmentation imposed on every society.

```yaml
sky_tradition_mapping:
  mapping_id: null
  visible_star_or_region_refs: []
  tradition_id: null
  mythic_claim_ids: []
  public_name: null
  known_version_refs: []
  historical_record_refs: []
  current_interpretation_refs: []
  scientific_cross_reference_ids: []
```

Different traditions may map the same sky differently.

The Astronomy extension supplies observed sky references. Myth owns the meaning attributed to them.

## 13. Sky-to-ground lead

A witnessed celestial event may justify a terrestrial search lead.

```yaml
celestial_ground_followup:
  followup_id: null
  source_detection_ids: []
  analysis_ref: null
  candidate_search_region_refs: []
  confidence: provisional
  cartography_handoff_refs: []
  travel_handoff_refs: []
  geology_handoff_refs: []
  material_culture_handoff_refs: []
  recovered_object_ids: []
  status: OPEN
```

Rules:
- a search region can remain broad;
- no object is spawned solely because the quest needs one;
- finding a rock near the predicted area does not authenticate its origin;
- recovery is a separate event with exact provenance;
- ownership/custody remains unresolved until the governing system decides it.

## 14. Meteorite or impact-material handoff

Astronomy may record that an event and a recovered object are candidates for linkage.

Geology/Material Culture must own:
- material description;
- sample identity;
- collection event;
- current location;
- custody;
- destructive analysis permission;
- provenance confidence.

No meteorite grants supernatural energy, evolution, Move access or battle effects unless source-supported and explicitly implemented.

## 15. Observatory operational continuity

A facility should change across visits.

Possible changes:
- instrument under calibration;
- dome/roof inaccessible;
- power limited;
- public night moved outdoors;
- one wavelength/method unavailable;
- archive digitization underway;
- new observing campaign active;
- viewing platform closed while research continues;
- temporary field station replacing a damaged primary site.

These are world-state changes. Maintenance and Technology own the underlying assets.

## 16. Amateur and institutional observers

Valid evidence can come from:
- professional staff;
- students;
- travelers;
- local residents;
- amateur clubs;
- automated or remote instruments when canon supports them.

Institutional status changes provenance and access; it does not make a claim automatically true.

An amateur can make the first useful observation. A famous observatory can make an incorrect interpretation.

## 17. Cobblemon/Minecraft implementation boundary

Reuse aggressively for presentation and world interaction:
- Minecraft day/night sky;
- clouds and weather visuals;
- particles/sounds for reviewed authored events;
- blocks, glass, doors, books, maps and displays;
- models and animation for overworld actors;
- Pokémon entities/forms/poses/cries;
- UI, networking and synchronization;
- server coordinates and world time;
- persistence hooks.

Adapter-required behavior:
- creating an Ouros observation session from a world-time interaction;
- recording exact observer/instrument/session provenance;
- projecting authored celestial-event presentation;
- syncing public schedule state;
- creating search-region handoffs.

Battle authority remains:

```text
Ouros celestial/world state
  -> explicit encounter composition
  -> AutoPTU BattleSpec / authoritative state / result
  -> adapter
  -> Minecraft/Cobblemon presentation
```

Forbidden:
- nearby Cobblemon entities becoming combatants automatically;
- Cobblemon BattleState/controllers deciding participants or legality;
- Minecraft weather directly applying PTU weather effects;
- a visual meteor applying scripted tactical damage;
- a telescope UI revealing hidden battle information.

## 18. Battle handoff rules

Celestial phenomena often tempt authors to invent battlefield effects. Do not do this.

Examples that require explicit engine capability evidence:
- meteor impacts during battle;
- falling debris zones;
- changing visibility penalties;
- lunar/stellar buffs;
- constellation-triggered Features;
- cosmic weather phases;
- delayed impact attacks created by the environment;
- radiation/heat/status effects;
- forced movement from shockwaves;
- Pokémon form changes caused by the sky event.

Until verified, these remain world-state, visual presentation or pre/post-battle consequences.

## 19. Encounter pattern — Ridge Observatory Withdrawal

Narrative premise:
An active observing night is interrupted by a local threat while visitors and staff occupy a high exposed site.

Intended full version:
- staff/visitors withdraw through several routes;
- safe access can change during the event;
- Intercept/forced movement may matter near restricted edges;
- weather/visibility can affect the tactical arena only when those rules are authoritative;
- autonomous opponents can prefer territorial withdrawal or route denial instead of pure KO logic;
- Minecraft playback mirrors the exact AutoPTU result.

Reduced version:
- the observing session stops in world state;
- visitors, staff and fragile instruments leave the tactical grid;
- any unsafe exterior area becomes a static excluded region;
- Ouros chooses exact combatants;
- AutoPTU runs an ordinary reviewed static encounter;
- weather, darkness, wind and astronomical presentation stay visual only;
- reopening and data recovery happen afterward in their owning systems.

## 20. Encounter pattern — Meteor-Fall Search Perimeter

Narrative premise:
Observers have generated a provisional ground-search region after a witnessed celestial event. A field team reaches the area and encounters a separate local conflict.

Intended full version:
- protected survey zones;
- withdrawal/clear-route objectives;
- possible impact-site terrain or hazards only if mechanically verified;
- territorial wild AI;
- explicit recovered-object interactions outside ordinary attack targeting;
- semantic playback preserving what was battle state versus field evidence.

Reduced version:
- field staff withdraw before combat;
- suspected impact material remains outside the tactical grid;
- an unsafe core zone is closed through world state;
- battle occurs in a static safe perimeter;
- after AutoPTU resolves the encounter, Science/Geology resume survey;
- victory does not authenticate, locate or assign ownership to any meteorite.

## 21. Noncombat pattern — Amateur Observation Reconciliation

Several observers report a transient event from different locations.

Gameplay:
- compare world timestamps;
- compare direction/sky-region records;
- inspect photographs or notes;
- check cloud/visibility windows;
- identify shared-source repetition;
- create one or more provisional event candidates;
- preserve unresolved reports.

No battle capability is required.

## 22. Long-term arc — An Observatory Learns the Sky

Stage 1: establish ordinary observing routines and staff specialties.

Stage 2: one expected event is missed or observed differently than predicted.

Stage 3: the institution checks calibration, visibility, old records and outside observers.

Stage 4: a revised prediction or method changes the next campaign.

Stage 5: a public observing night exposes a different operational pressure such as crowding, lighting or access.

Stage 6: a later detection produces a field-search or cross-institution collaboration.

Stage 7: the site gains a new baseline: revised observing practice, changed public interpretation, altered lighting nearby, new archive material or a long-term unresolved question.

No hidden `observatory level` is required.

## 23. Persistence outputs

Useful writeback can include:
- new observation sessions;
- instrument readiness history;
- observing-window revisions;
- detection/non-detection records;
- field-search regions;
- public-memory entries;
- myth/science cross-reference links;
- maintenance requests;
- light-interference evidence;
- revised public notices;
- archived photographs or notebooks;
- new research questions.

## 24. Anti-false-completion rules

- Seeing a streak does not recover a meteorite.
- Recovering a rock does not establish celestial origin.
- One instrument signal does not establish a Pokémon identity.
- A famous prediction can be wrong.
- A myth can preserve a useful observation without proving its cosmology.
- A skywatch event can be meaningful even when clouds prevent observation.
- A repaired telescope does not mean the site is operational if other dependencies remain blocked.
- A night-time map does not grant tactical darkness rules.
- A meteor shower does not become PTU Weather merely because Minecraft renders it.
- A visible Pokémon does not enter battle until Ouros explicitly composes the encounter.

## 25. Canon status

This file establishes only a proposed systems extension.

Not canonized here:
- any Ouros observatory;
- any celestial body or constellation;
- meteor-shower names or recurrence;
- cosmology;
- spaceflight capability;
- radio/infrared/telescope technology prevalence;
- dark-sky regulation;
- scientific institution;
- Legendary/Mythical association;
- celestial battle mechanic.

All concrete names, locations, technologies and traditions require separate review.