# Seismic Faults, Ground Failure & Slope Instability Layer

Status: proposed systems architecture. Not established Ouros canon.

## Purpose

This layer gives Ouros persistent state for earthquakes, tremors, fault observations, shaking footprints, aftershock sequences, surface deformation, liquefaction observations, earthquake-triggered landslides and long-lived slope instability.

It sits between Geology and Crisis.

Geology describes the substrate and subsurface context. This layer records seismic events and ground response. Crisis consumes verified or suspected impacts. Architecture, Infrastructure and Travel own the condition of buildings, utilities and routes. Soil, Freshwater, Flora, Meteorology and Cryosphere can change local susceptibility. Science owns interpretation and models. Media/Communications owns dissemination.

This layer does not define PTU earthquake damage, collapse rolls, falling debris, forced movement, Rough/Slow Terrain, Tripped, drowning, structural HP or any other tactical mechanic.

## 1. Seismic region

```yaml
seismic_region:
  seismic_region_id: null
  region_ids: []
  geological_site_ids: []
  known_fault_segment_ids: []
  monitoring_network_ids: []
  historical_event_ids: []
  slope_system_ids: []
  public_guidance_refs: []
  current_assessment_refs: []
  source_refs: []
```

A seismic region is a planning/observation object. It does not mean an earthquake is imminent.

## 2. Fault segment

```yaml
fault_segment:
  fault_segment_id: null
  seismic_region_id: null
  geometry_revision_ids: []
  observed_surface_refs: []
  inferred_subsurface_refs: []
  displacement_observation_ids: []
  historical_event_refs: []
  interpretation_ids: []
  confidence: null
  public_disclosure_state: limited
```

A mapped fault is an interpretation supported by evidence. The exact geometry may be revised.

A surface crack is not automatically a fault trace.

## 3. Seismic event

```yaml
seismic_event:
  seismic_event_id: null
  occurred_at: null
  origin_solution_versions: []
  detection_observation_ids: []
  witness_report_ids: []
  linked_fault_claim_ids: []
  shaking_footprint_ids: []
  surface_rupture_ids: []
  ground_failure_assessment_ids: []
  confirmed_ground_failure_ids: []
  aftershock_sequence_id: null
  crisis_ids: []
  chronicle_refs: []
  public_memory_refs: []
  causal_claim_ids: []
```

The event remains one historical object even when location/magnitude/depth estimates are revised.

A new solution version corrects knowledge. It does not create a second earthquake.

## 4. Seismic observation

```yaml
seismic_observation:
  observation_id: null
  observed_at: null
  observer_or_sensor_id: null
  location_id: null
  observation_type: null
  raw_value_ref: null
  qualitative_description: null
  calibration_state: unknown
  source_record_id: null
  linked_event_id: null
  attribution_state: unresolved
```

Candidate observation types:
- SENSOR_TRIGGER
- FELT_SHAKING
- GROUND_SOUND
- SURFACE_OFFSET
- WATER_LEVEL_CHANGE
- SPRING_CHANGE
- STRUCTURE_MOTION
- POKEMON_BEHAVIOR
- POWER_OR_SIGNAL_ANOMALY
- SLOPE_MOVEMENT

Observation type does not establish cause.

## 5. Detection, warning and prediction remain separate

```yaml
early_warning_message:
  warning_id: null
  source_network_id: null
  detected_event_id: null
  issued_at: null
  estimated_origin_solution_ref: null
  predicted_shaking_regions: []
  delivery_packet_ids: []
  automated_action_request_ids: []
  superseded_by: null
```

Rules:
- early warning can exist only after a detectable event has begun;
- a warning can arrive before strong shaking at some locations;
- warning delivery is handled through Communications infrastructure;
- a warning may be revised or cancelled;
- prediction claims made before an event are separate scientific/public claims and never receive automatic truth status.

## 6. Local shaking footprint

Magnitude is not local impact.

```yaml
shaking_footprint:
  shaking_footprint_id: null
  seismic_event_id: null
  spatial_revision_id: null
  source_model_refs: []
  observation_refs: []
  intensity_bands: []
  uncertainty_notes: []
  validated_at: null
```

A settlement should consume the local footprint, not the event magnitude alone.

The same event can produce strong shaking in one district and lower shaking nearby due to distance and local conditions.

## 7. Aftershock sequence

```yaml
aftershock_sequence:
  sequence_id: null
  main_event_id: null
  member_event_ids: []
  current_activity_summary: null
  issued_assessment_refs: []
  route_review_ids: []
  structure_reinspection_ids: []
  slope_reinspection_ids: []
  closed_at: null
```

The sequence is a grouping/interpretation object. Each actual aftershock remains its own seismic event.

A repaired route can require reinspection after a later member event without being returned automatically to the original damaged state.

## 8. Surface rupture and deformation

```yaml
surface_deformation:
  deformation_id: null
  seismic_event_id: null
  location_ids: []
  deformation_type: null
  geometry_revision_ids: []
  observation_refs: []
  confidence: null
  infrastructure_overlap_ids: []
  freshwater_overlap_ids: []
  route_overlap_ids: []
```

Candidate types:
- SURFACE_RUPTURE
- UPLIFT
- SUBSIDENCE
- LATERAL_OFFSET
- SETTLEMENT
- UNKNOWN_DEFORMATION

The narrative layer records deformation. It does not convert meters/blocks of displacement into PTU forced movement.

## 9. Ground failure assessment versus observed failure

```yaml
ground_failure_assessment:
  assessment_id: null
  seismic_event_id: null
  assessment_type: null
  spatial_revision_id: null
  evidence_refs: []
  model_refs: []
  confidence: null
  issued_at: null
  superseded_by: null
```

Candidate assessment types:
- LANDSLIDE_SUSCEPTIBILITY
- LIQUEFACTION_SUSCEPTIBILITY
- LATERAL_SPREAD_SUSCEPTIBILITY
- SETTLEMENT_SUSCEPTIBILITY

An assessment is not an observed event.

```yaml
ground_failure_event:
  ground_failure_event_id: null
  event_type: null
  occurred_or_observed_at: null
  location_ids: []
  triggering_event_claim_ids: []
  observation_ids: []
  mapped_extent_revisions: []
  route_impact_ids: []
  structure_impact_ids: []
  freshwater_impact_ids: []
  ecological_impact_ids: []
  current_condition: null
```

Candidate event types:
- LANDSLIDE
- ROCKFALL
- DEBRIS_FLOW
- LIQUEFACTION_MANIFESTATION
- LATERAL_SPREAD
- GROUND_SETTLEMENT
- SAND_BOIL
- SLOPE_CREEP

## 10. Trigger attribution must remain evidence-based

A landslide may have multiple contributing conditions.

```yaml
trigger_claim:
  trigger_claim_id: null
  target_event_id: null
  candidate_trigger_type: null
  candidate_source_event_id: null
  evidence_refs: []
  counterevidence_refs: []
  confidence: null
  review_state: open
```

Candidate triggers may include:
- EARTHQUAKE_SHAKING
- RAINFALL
- SNOWMELT
- FLOODING
- VOLCANIC_ACTIVITY
- EXCAVATION
- UNDERCUTTING
- DRAINAGE_FAILURE
- PIPE_LEAK
- UNKNOWN

Do not force one cause when several conditions matter.

## 11. Persistent slope system

A landslide is not finished merely because loose debris was removed from a road.

```yaml
slope_system:
  slope_system_id: null
  location_ids: []
  geological_context_refs: []
  soil_land_unit_ids: []
  vegetation_unit_ids: []
  drainage_refs: []
  cryosphere_refs: []
  previous_failure_ids: []
  monitoring_point_ids: []
  current_stability_assessment_refs: []
  route_overlap_ids: []
  structure_overlap_ids: []
  current_management_state: null
```

This object can persist for years.

Rain after an earthquake can reactivate a slope without being a new seismic event.

## 12. Sensor network

```yaml
seismic_monitoring_network:
  network_id: null
  operator_institution_ids: []
  station_ids: []
  processing_asset_ids: []
  communication_channel_ids: []
  coverage_revision_ids: []
  calibration_records: []
  outage_ids: []
  alert_policy_refs: []
```

```yaml
seismic_station:
  station_id: null
  location_id: null
  equipment_asset_ids: []
  operational_state: unknown
  calibration_state: unknown
  power_dependency_ids: []
  communication_dependency_ids: []
  maintenance_record_ids: []
  observation_stream_refs: []
```

A failed station creates missing information. It does not create or suppress earthquakes.

## 13. Pokémon observations

Pokémon may be part of field observation when species lore or observed individual behavior supports it.

Record:
- individual/group identity where known;
- exact observed behavior;
- time;
- location;
- observer;
- previous baseline;
- relation to later seismic events only as a hypothesis unless validated.

Do not create `pokemon_predicts_earthquake = true` from a single coincidence.

Do not convert Ground/Rock/Steel typing into immunity, prediction, stabilization or seismic causation.

## 14. Cross-layer contracts

### Geology

Provides geological context and fault interpretations. This layer never rewrites resource/fossil provenance.

### Science

Owns event solutions, models, hypothesis review and uncertainty. This layer stores the objects/results needed by Science.

### Crisis

Consumes verified/suspected seismic impacts and creates response/recovery state. Crisis does not invent a new quake to justify an encounter.

### Architecture / Infrastructure

Own structure condition, inspection, repair and utility operation. Shaking exposure is input, not direct damage output.

### Travel

Own route open/closed/restricted state. A landslide map can trigger inspection, but this layer does not itself decide transport schedules.

### Soil / Flora / Freshwater / Cryosphere / Meteorology

Provide slope material, roots/vegetation, drainage/water, snowmelt/freeze-thaw and rainfall state relevant to later slope behavior.

### Volcanism

Volcanic tremor/unrest remains Volcanism authority. Similar-looking sensor traces do not get merged automatically.

### Media / Communications

Delivers alerts, warnings, corrections and public reports. Truth is not created by publication.

### Cartography / Photography

May preserve fault maps, crack surveys and imagery with provenance. Maps/photos remain evidence products.

## 15. Battle projection boundary

The server may eventually project a verified world-state snapshot into an AutoPTU arena.

Required pipeline:

`seismic/ground-failure state`
→ `server determines encounter-safe snapshot`
→ `PTU/Caelo mechanical validation`
→ `AutoPTU-Java BattleSpec`
→ `authoritative battle result`
→ `world-state writeback`

Minecraft must not decide that a cracked block is Rough Terrain or that a shaking animation applies Tripped.

A battle Move named Earthquake must never write directly into `seismic_event` state unless an explicit future narrative/world rule separately authorizes that consequence.

## 16. Permanent capability dependencies

Mechanically rich seismic encounters may touch these permanent families:

- targeting / footprints / range / LoS — relevant once battle starts;
- base movement legality — relevant for fixed post-event terrain;
- complete movement incl. push/pull/knockback/interception/forced movement — required for seismic displacement, moving debris or dynamic rescue lanes;
- core calculations — required for ordinary combat calculations, not seismic hazard generation;
- action economy / initiative — required for ordinary encounter order;
- full turn / round lifecycle — required if shaking/hazard phases advance during combat;
- full stateful damage pipeline — required for any validated environmental damage integration;
- status lifecycle — required if exact PTU/Caelo rules apply a status;
- terrain / weather / hazards / zones / reactions — central dependency for dynamic unstable ground, falling zones, debris fields or ground-state transitions;
- move-specific behavior — required for exact Move interactions only;
- abilities — required for exact Ability interactions only;
- items — required for exact equipment/item interactions only;
- Trainer Features / perks — required for exact Features such as a validated Groundshaper-dependent interaction;
- AI legal-action infrastructure — enough to enumerate legal ordinary choices;
- AI tactical policy — required for autonomous retreat, avoid-hazard, rescue, reach-safe-zone or protect-objective behavior;
- Minecraft / Cobblemon / Craftics adapter & playback — required to project and render world/battle state safely.

## 17. Full and reduced encounter contract examples

### Aftershock at Switchback

Intended full version:
- an aftershock occurs while actors are crossing a previously damaged mountain route;
- debris zones and safe tiles change during the encounter;
- wild Pokémon may prioritize withdrawal rather than KO;
- players may need to reach a safe side rather than defeat every opponent.

Dependencies beyond ordinary combat:
- complete movement — required;
- full lifecycle — required for timed aftershock phases;
- terrain/weather/hazards/zones/reactions — required;
- AI tactical policy — required;
- adapter/playback — required.

Reduced version:
Resolve the aftershock in overworld state before AutoPTU starts. Update the route geometry, select a stable post-aftershock arena, keep civilians/debris movement outside the grid and run a conventional static battle only if a real confrontation remains.

### Liquefaction Yard Evacuation

Intended full version:
- portions of a waterfront yard become mechanically unsafe after shaking;
- actors move toward designated stable exits;
- protect/reach-exit priorities matter more than KO.

Dependencies:
- complete movement — required;
- terrain/hazards/zones/reactions — required;
- lifecycle — partial family would need exact validated hazard timing;
- tactical AI — required;
- adapter/playback — required.

Reduced version:
Resolve evacuation, ground inspection and access restrictions in world state. Freeze one inspected stable slab/yard section as the battle map. No liquefaction damage, sinking, forced movement or terrain penalty is applied.

### Landslide-Dam Survey

Intended full version:
- a slope failure temporarily blocks a stream;
- water level and debris accessibility can change while the team surveys or fights;
- withdrawal and safe-route decisions matter.

Dependencies:
- complete movement — required if debris/water displaces actors;
- terrain/weather/hazards/zones/reactions — required;
- full lifecycle — required for changing water/debris phases;
- AI tactical policy — required;
- adapter/playback — required.

Reduced version:
Freshwater + Seismic layers resolve the temporary dam and select a safe observation bank before combat. AutoPTU receives a static arena. Water rise, collapse risk and survey instrumentation stay outside tactical authority.

## 18. Mechanical no-inference rules

This layer must never invent:
- earthquake damage dice;
- falling-rock damage;
- collapse damage;
- structural HP;
- shaking Accuracy penalties;
- automatic Tripped/Vulnerable/Slowed;
- Rough or Slow Terrain from visual cracks;
- knockback from tremors;
- liquefaction movement costs;
- landslide travel speed;
- seismic warning Skill DCs;
- Ground/Rock/Steel immunity;
- Earthquake Move world-scale effects;
- Groundshaper regional stabilization;
- Pokémon earthquake-prediction powers;
- aftershock probabilities.

Exact effects require PTU/Caelo text plus AutoPTU implementation evidence.

## 19. Canon questions intentionally unresolved

- Which Ouros regions are tectonically active?
- Which fault systems are known before play begins?
- Which old earthquakes are established history?
- Which institutions operate sensor networks?
- What technology level supports early warning in each region?
- Which structures have authored seismic design or retrofit histories?
- Which slopes have known previous failures?
- What Pokémon behavior relationships with seismic events are regional canon, if any?
- What exact PTU/Caelo rules govern collapse, falling objects, Earthquake, Groundshaper, tunneling, rough ground and rescue under shaking?

Until reviewed, all answers remain proposed or unresolved.
