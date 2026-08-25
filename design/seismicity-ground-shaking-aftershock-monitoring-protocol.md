# Seismicity, Ground Shaking and Aftershock Monitoring Protocol

Status: PROPOSED / NON-CANON. Subordinate protocol. This document does not establish specific Ouros faults, earthquakes, institutions, technologies or PTU environmental mechanics.

Research provenance: `research/2026-08-25-seismicity-earthquakes-aftershocks-ground-failure-scan-164.md`.

## Purpose

Ouros needs a persistent way to represent earthquakes and seismic observations without collapsing geology, disaster response, structural damage and tactical battle mechanics into one system.

This protocol owns the observational and revision history of seismic events. It does not become a second Geology authority.

## Authority boundaries

Geology owns fault/tectonic interpretations, geologic units, substrate and long-term geologic context.

This protocol owns seismic-event identity, source-estimate revisions, ground-motion observations, local shaking assessments, aftershock-association assessments, surface-rupture observations and scoped earthquake-related ground-failure observations.

Crisis owns emergency declaration, evacuation, staging, response objectives, sheltering and recovery coordination.

Slope Instability owns landslides, rockfall, debris flows and long-lived slope-instability state even when shaking triggered them.

Architecture/Public Works owns building, bridge, utility and infrastructure condition, closure, inspection and repair.

Groundwater owns well, spring, aquifer and subsurface-water state.

Freshwater/River Geomorphology owns channel response and river-system state.

Metrology owns instrument calibration, sensor condition and traceability.

Timekeeping owns clock synchronization and corrected timestamps.

Remote Sensing owns aerial/spatial products derived after an event.

Cases owns investigations involving suspected sabotage, false reports or wrongdoing. A seismic anomaly never opens such a case automatically.

Public Memory/Archives/Museums own later social and historical interpretation.

## Core model

### `SEISMIC_EVENT`

Persistent identity for one interpreted seismic event.

Suggested fields:
- `seismic_event_id`
- `event_class`: `TECTONIC_CANDIDATE`, `VOLCANIC_CANDIDATE`, `COLLAPSE_CANDIDATE`, `BLAST_CANDIDATE`, `POKEMON_TREMOR_CANDIDATE`, `MIXED_OR_UNRESOLVED`, `OTHER_AUTHORED`
- `first_detected_at`
- `current_status`: `AUTOMATIC_DETECTION`, `UNDER_REVIEW`, `REVIEWED`, `HISTORICAL`
- `current_source_assessment_id`
- `provenance_refs[]`

`event_class` is an assessment category, not ground truth. An event can remain unresolved indefinitely.

### `SEISMIC_SOURCE_REVISION`

Versioned interpretation of an event source.

Suggested fields:
- `revision_id`
- `seismic_event_id`
- `estimated_origin_time`
- `origin_time_uncertainty`
- `estimated_location`
- `location_uncertainty`
- `estimated_depth`
- `depth_uncertainty`
- `size_estimate`
- `size_scale_or_method`
- `source_hypothesis`
- `confidence`
- `method_revision`
- `created_at`
- `supersedes_revision_id`
- `evidence_refs[]`

Numerical magnitude is optional. If Ouros canon lacks that measurement standard, `size_estimate` may remain qualitative.

A newer revision supersedes current interpretation. It never alters raw station records or earlier public reports.

### `GROUND_MOTION_OBSERVATION`

One place-specific observation associated with an event candidate.

Suggested fields:
- `observation_id`
- `seismic_event_id_or_candidate`
- `location_ref`
- `observed_at_raw`
- `observed_at_corrected`
- `observation_mode`: `INSTRUMENT`, `FELT_REPORT`, `OBJECT_EFFECT`, `STRUCTURE_EFFECT`, `ENVIRONMENTAL_EFFECT`, `OTHER`
- `instrument_id` when relevant
- `raw_measurement_ref`
- `observer_id` when appropriate
- `quality_flag`
- `provenance_refs[]`

Human felt reports and instrument readings can coexist. Neither overwrites the other.

### `LOCAL_SHAKING_ASSESSMENT`

A derived assessment scoped to a location or polygon.

Suggested fields:
- `assessment_id`
- `seismic_event_id`
- `spatial_scope`
- `shaking_band_or_scale`
- `method_revision`
- `input_observation_ids[]`
- `uncertainty`
- `created_at`
- `supersedes_assessment_id`

This can feed Crisis prioritization and later planning. It does not own damage.

### `AFTERSHOCK_ASSOCIATION`

Relationship claim between two events.

Suggested fields:
- `association_id`
- `candidate_event_id`
- `parent_event_id`
- `assessment`: `POSSIBLE`, `PROBABLE`, `SUPPORTED`, `REJECTED`, `UNRESOLVED`
- `method_revision`
- `reasoning_summary`
- `evidence_refs[]`
- `created_at`

Temporal order alone cannot create this relationship.

### `SURFACE_RUPTURE_OBSERVATION`

Observed ground break/deformation potentially related to an event.

Suggested fields:
- `observation_id`
- `seismic_event_id_or_candidate`
- `geometry_ref`
- `observation_time`
- `description`
- `measurement_refs[]`
- `cause_assessment`
- `confidence`
- `image_refs[]`
- `provenance_refs[]`

A crack is not automatically a fault rupture. Geology must own the interpretation.

### `GROUND_FAILURE_OBSERVATION`

Scoped observation of ground response.

Suggested classes:
- `LIQUEFACTION_INDICATOR`
- `LATERAL_SPREADING_INDICATOR`
- `SETTLEMENT`
- `SAND_BOIL_OR_EJECTION`
- `GROUND_CRACKING`
- `OTHER_UNRESOLVED`

This record captures what was observed. It does not apply PTU Status, Terrain or forced movement.

Slope failures are handed to Slope Instability instead of duplicated here.

### `SEISMIC_MONITORING_SITE`

Persistent monitoring location.

Suggested fields:
- `site_id`
- `location_ref`
- `institution_ref`
- `instrument_ids[]`
- `operational_history[]`
- `foundation_or_site_context_ref`
- `communications_ref`
- `power_ref`
- `time_reference_ref`

Sensor validity remains Metrology authority. A station being online does not make every estimate correct.

## Event lifecycle

Suggested sequence:

`SIGNAL / FELT REPORT -> EVENT CANDIDATE -> SOURCE REVISION -> LOCAL SHAKING ASSESSMENTS -> CROSS-SYSTEM HANDOFFS -> LATER EVENT ASSOCIATIONS -> HISTORICAL REVISION`

The protocol must preserve uncertainty at each stage.

A useful Chronicle event can continue changing for years through better station coverage, corrected clocks, new geology, archival photographs or later field surveys.

## Cross-system handoffs

### Crisis

Input: current event/shaking assessment and uncertainty.

Crisis decides response, evacuations and operational priorities. It must not wait for perfect scientific classification when immediate safety action is warranted.

### Architecture/Public Works

Input: affected area and shaking observations.

Architecture decides inspection/closure/repair. Damage reports can become observations supporting local intensity but cannot directly set event size.

### Slope Instability

Input: event ID, shaking context and candidate slope observations.

Slope layer owns any resulting landslide, rockfall or debris-flow lifecycle.

### Groundwater/Freshwater

Input: event timing and local shaking context.

Those layers decide whether changed wells, springs, streamflow or channel behavior are actually observed and how to interpret them.

### Transport / Wayfinding

Input: closures from the authoritative infrastructure/ground-failure layers.

A map can retain the pre-event route as a historical revision while Travel marks it unavailable.

### Metrology / Timekeeping

Instrument drift, failed clocks or displaced stations remain their responsibility. A corrected timestamp creates a revised event estimate rather than silently modifying raw records.

### Remote Sensing / Photography

Images can document post-event change, but image difference alone cannot classify an earthquake or determine its magnitude.

## Pokémon-related observations

Pokémon behavior can be recorded as an observation with provenance:
- unusual departure from a site;
- tremor-producing behavior;
- changed roost/burrow use;
- behavior interpreted locally as a warning.

Interpretation must remain separate.

Do not establish species-wide earthquake prediction, causation or sensing without authored canon plus mechanics evidence.

A Whiscash observation may generate a hypothesis. It never becomes a seismometer.

## Minecraft projection

Allowed projection:
- revised cracks or ground geometry after authoritative world-state change;
- temporary closures, barriers and response staging;
- monitoring stations and damaged/relocated installations;
- sediment ejection or repaired streets as visual history;
- archive boards or public information displays;
- changed route geometry after downstream authorities approve the revision.

Forbidden authority:
- block destruction creating a seismic event;
- TNT/mining noise automatically becoming a tectonic event;
- terrain cracks creating a fault record;
- waterlogged blocks creating liquefaction;
- entity reactions proving an earthquake;
- a Pokémon using `Earthquake` causing persistent regional seismic state;
- client camera shake deciding intensity;
- chunk reload restoring pre-event authoritative geometry.

## Battle handoff

Environmental seismic state remains outside AutoPTU unless an exact battle mechanic has been verified.

The default handoff should be:
1. world simulation resolves the earthquake/aftershock and immediate unsafe areas;
2. Crisis moves civilians/responders when possible;
3. Architecture/Slope/Geology define which geometry is safe enough for a battle snapshot;
4. adapter freezes one legal static arena;
5. AutoPTU resolves the battle using only implemented PTU mechanics;
6. result returns to world state without implying that the seismic event itself was solved.

Do not call PTU Move `Earthquake` as an environmental hazard. Do not use Groundshaper or Mold the Earth as a generic seismic system.

## Intended rich battle support, once engine capability exists

A future earthquake/aftershock encounter might include changing passability, falling debris, forced displacement, unstable zones, timed withdrawals or protected routes. Those concepts require explicit engine support from complete movement and/or terrain/weather/hazards/zones/reactions, and often full stateful damage plus tactical AI.

Until then, use reduced static versions.

## No-inference rules

Magnitude is not damage.
Intensity at one place is not intensity everywhere.
A later tremor is not automatically an aftershock.
A crack is not automatically fault rupture.
Wet sediment is not automatically liquefied.
A landslide after an earthquake remains a Slope Instability object.
A broken bridge remains an Architecture/Public Works object.
A changed spring remains a Groundwater object.
A Whiscash is not automatically the cause or predictor of an earthquake.
Ground typing grants no geological authority.
The PTU Move `Earthquake` is not an environmental-event template.
Groundshaper is not tectonics.
Camera shake is not intensity.
Block destruction is not seismic truth.

## Canon promotion gate

No specific Ouros earthquake, active fault, monitoring network, magnitude scale, historical disaster or Pokémon seismic behavior becomes canon through this protocol.

Canon promotion requires an explicit authored decision specifying at minimum:
- location/region;
- event or background-seismicity history;
- institutions and technology;
- known versus uncertain geology;
- public knowledge level;
- affected persistent world-state objects;
- any Pokémon relationship;
- any validated PTU mechanics used in play.

## Open questions

- What seismic vocabulary does Ouros use?
- Which areas have enough instrumentation for precise source estimates?
- Are active faults publicly mapped before the campaign?
- What historical event sequence is already part of settlement memory?
- Can players contribute observations to an institutional catalog?
- How frequently can background seismicity advance offline?
- Which downstream closures should resolve automatically versus create player-facing situations?
- Does Caelo define environmental collapse, falling debris, unstable ground or earthquake-specific rules?
