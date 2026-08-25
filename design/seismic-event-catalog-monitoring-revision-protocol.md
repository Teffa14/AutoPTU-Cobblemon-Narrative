# Seismic Event Catalog, Monitoring and Revision Protocol

Status: PROPOSED / NON-CANON. Subordinate extension to `design/seismic-faults-ground-failure-layer.md` from Pass 71. Pass 71 remains the authority for seismic regions, fault segments, seismic events, shaking footprints, aftershock sequences, surface deformation and ground-failure state.

Research provenance: `research/2026-08-25-seismicity-earthquakes-aftershocks-ground-failure-scan-164.md`.

## Purpose

Pass 71 already defines what a seismic event is and how earthquake-related ground response fits between Geology and Crisis. The remaining useful gap is narrower: how monitoring networks, automatic detections, felt reports, source-solution revisions and catalog publications accumulate over time without rewriting earlier evidence.

This protocol extends Pass 71 with data provenance and revision rules. It does not own faults, ground failure, damage, emergency response or tactical earthquake mechanics.

## Authority boundary

Pass 71 owns:
- `SEISMIC_REGION`;
- `FAULT_SEGMENT`;
- `SEISMIC_EVENT` identity;
- local `SHAKING_FOOTPRINT`;
- `AFTERSHOCK_SEQUENCE`;
- surface deformation;
- ground-failure assessments/events;
- trigger attribution.

Pass 164 adds only:
- monitoring-network/station history;
- automatic versus reviewed event detections;
- source-solution revision lineage;
- felt-report provenance;
- catalog-entry vintages;
- event-association review history;
- publication/revision semantics;
- QA links to Metrology and Timekeeping.

Metrology still owns sensor calibration and measurement validity. Timekeeping owns clock corrections. Communications owns delivery of warnings/reports. Science owns interpretation/modeling beyond the event catalog. Crisis, Architecture/Public Works, Groundwater, Slope Instability and other existing systems continue to own consequences.

## `SEISMIC_MONITORING_NETWORK`

Persistent identity for an institutionally operated network.

Suggested fields:
- `network_id`
- `institution_ref`
- `network_revision_ids[]`
- `station_ids[]`
- `coverage_notes[]`
- `data_standard_refs[]`
- `public_feed_refs[]`
- `communications_refs[]`
- `chronicle_refs[]`

A network revision may add/remove stations or change processing methods without creating a new historical network identity.

## `SEISMIC_MONITORING_STATION`

Persistent monitoring location or installation.

Suggested fields:
- `station_id`
- `network_id`
- `location_revision_ids[]`
- `instrument_ids[]`
- `foundation_or_site_context_ref`
- `operational_state_history[]`
- `power_ref`
- `communications_ref`
- `time_reference_ref`
- `maintenance_refs[]`

Station state candidates:
`OPERATIONAL`, `DEGRADED`, `OFFLINE`, `MAINTENANCE`, `RELOCATED`, `DECOMMISSIONED`, `UNKNOWN`.

A station can produce valid data before a later fault is discovered in its clock, foundation or instrument. Corrections must preserve the original record.

## `AUTOMATIC_EVENT_DETECTION`

Machine/network-generated candidate before human or institutional review.

Suggested fields:
- `detection_id`
- `network_id`
- `detected_at`
- `candidate_origin_time`
- `candidate_location`
- `candidate_size_estimate`
- `contributing_station_ids[]`
- `processing_revision`
- `quality_flags[]`
- `linked_seismic_event_id`
- `review_state`

Review states:
`UNREVIEWED`, `ACCEPTED`, `MERGED`, `SPLIT`, `RECLASSIFIED`, `REJECTED`, `UNRESOLVED`.

An automatic detection is not itself a canonical earthquake. It can later map to an existing Pass 71 `SEISMIC_EVENT`, be rejected as quarry/mining/machinery noise, or remain unresolved.

## `SOURCE_SOLUTION_REVISION`

Versioned source estimate attached to one Pass 71 seismic event.

Suggested fields:
- `solution_revision_id`
- `seismic_event_id`
- `estimated_origin_time`
- `origin_time_uncertainty`
- `estimated_location`
- `location_uncertainty`
- `estimated_depth`
- `depth_uncertainty`
- `size_estimate`
- `size_scale_or_method`
- `processing_method_revision`
- `input_detection_ids[]`
- `input_station_record_refs[]`
- `reviewed_by_ref`
- `issued_at`
- `supersedes_solution_revision_id`

A later solution becomes the current institutional estimate. Earlier solutions remain historically real because Crisis, Media, Travel or the public may have acted on them.

Numerical magnitude is optional. If Ouros canon does not establish a compatible measurement system, use qualitative/categorical size estimates instead.

## `FELT_REPORT`

Place-specific report from a person or institution.

Suggested fields:
- `felt_report_id`
- `reported_at`
- `reported_event_time_raw`
- `reported_event_time_corrected`
- `location_ref`
- `observer_ref_or_anonymous_token`
- `description`
- `observed_effect_tags[]`
- `source_language_ref`
- `translation_ref`
- `privacy_state`
- `linked_seismic_event_id`
- `quality_notes[]`

Felt reports may support Pass 71 shaking footprints. They do not directly set magnitude, structural safety or causation.

## `CATALOG_ENTRY_REVISION`

Published institutional view of one event at one time.

Suggested fields:
- `catalog_entry_revision_id`
- `catalog_id`
- `seismic_event_id`
- `source_solution_revision_id`
- `public_summary`
- `classification`
- `published_at`
- `superseded_at`
- `correction_reason`
- `provenance_refs[]`

Useful classification examples are setting-specific and may include natural-event candidate, blast/collapse candidate or unresolved. Do not invent legal implications.

## Catalog lineage and correction rules

1. Raw sensor observations remain immutable records.
2. Clock/calibration corrections create derived values with explicit provenance.
3. Automatic detections may be merged, split or rejected.
4. One Pass 71 `SEISMIC_EVENT` can have many source-solution revisions.
5. Public catalog entries can be corrected without creating a second physical earthquake.
6. Historical reports remain accessible for Chronicle even after supersession.
7. A change in event classification does not silently modify Crisis actions already taken.
8. New observations can revise uncertainty without requiring a dramatic plot revelation.

## `EVENT_ASSOCIATION_REVIEW`

Pass 71 already owns aftershock sequences. This record only stores the review that decides whether a candidate event belongs in a sequence.

Suggested fields:
- `review_id`
- `candidate_event_id`
- `sequence_id`
- `assessment`: `SUPPORTED`, `POSSIBLE`, `REJECTED`, `UNRESOLVED`
- `method_revision`
- `evidence_refs[]`
- `counterevidence_refs[]`
- `reviewed_at`
- `supersedes_review_id`

Temporal order alone never assigns aftershock membership.

## Monitoring gaps as narrative state

Useful states include:
- station offline during a key interval;
- sparse regional coverage;
- one station moved between vintages;
- clocks corrected after the fact;
- incompatible older data formats;
- missing telemetry but preserved local storage;
- valid felt reports where instruments were absent;
- strong instrument detection with no felt reports.

A gap produces uncertainty, not an automatic mystery, conspiracy or quest.

## Cross-system handoffs

Metrology validates instrument calibration, uncertainty and out-of-tolerance history.

Timekeeping preserves raw timestamps and corrected estimates.

Communications records whether alerts/catalog revisions actually reached recipients.

Archives preserves old catalogs, station notebooks, analog records and superseded reports.

Remote Sensing can add post-event spatial evidence but never substitutes for seismic source classification.

Pass 71 consumes accepted event/revision data for shaking footprints, aftershock sequences and related ground-response assessments.

## Pokémon observations

A Pokémon behavior report can be stored as a felt/context observation only when provenance is clear. It does not become a source solution.

Whiscash is a useful cautionary precedent because official game material has treated local tremor behavior and earthquake folklore separately. Ouros should preserve the distinction between observed behavior, local belief and instrument/geologic interpretation.

Do not build a species-wide warning service unless canon explicitly authors one.

## Minecraft projection

Allowed:
- physical monitoring stations;
- status boards showing current published catalog summaries;
- broken/offline equipment after authoritative state change;
- relocated stations preserving old markers;
- public displays of historical events;
- optional client presentation of felt shaking after world state decides it occurred.

Forbidden authority:
- block vibration or TNT creating catalog events automatically;
- camera shake writing intensity;
- loaded Pokémon behavior becoming a detection algorithm;
- adapter clocks overwriting Timekeeping provenance;
- destroyed station blocks deleting archived observations.

## Battle boundary

This protocol does not create a combat hazard.

A world-state event may cause Crisis/Architecture/Pass 71 to close or revise an area before a battle begins. AutoPTU receives a static legal snapshot unless exact environmental mechanics are verified.

The PTU Move `Earthquake` remains a separate Move mechanic. Groundshaper/Mold the Earth remains a separate battle mechanic.

## Canon promotion gate

The protocol itself does not establish monitoring technology or networks. Canon promotion requires explicit decisions about:
- which institutions operate stations;
- which regions have coverage;
- whether numerical magnitude/intensity systems exist;
- what public catalog information is available;
- what historical records precede the players;
- whether any Pokémon behaviors are institutionally monitored;
- privacy and access rules for felt reports.

## Open questions

- Does Ouros need real-time automatic detections, or only later reviewed catalogs?
- How many monitoring vintages should Chronicle retain at gameplay scale?
- Can player-built stations join an institutional network, and under what validation process?
- How should data gaps be summarized without overwhelming players?
- Which source-estimate fields should remain qualitative?
- What Caelo material, if any, establishes earthquake warning, sensing or environmental hazard mechanics?
