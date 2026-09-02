# Cartography, Survey and Route-Marker Continuity Layer

Status: PROPOSED SYSTEMS DESIGN
Date: 2026-09-02
Pass: 203

This layer defines persistent spatial representations without competing with canonical geography, Travel route state, Observation evidence, Tideglass document provenance or PTU navigation mechanics.

## 1. Authority model

Ouros already has canonical coordinates and a route graph for Marea Interior. Those remain world/implementation authority until an explicit canon migration changes them.

Maps, field sketches and route diagrams are artifacts inside that world. They may be current, stale, incomplete, copied incorrectly, differently scoped or annotated from uncertain evidence.

```text
CANONICAL_GEOGRAPHY
  -> can be observed by SURVEY_EVENT
  -> selected observations can be encoded in CARTOGRAPHIC_ARTIFACT
  -> editions/copies can circulate
  -> actors may update ROUTE_KNOWLEDGE
  -> UI may project some known representation
```

No arrow runs backward from Minecraft rendering or UI map reveal directly into canon.

## 2. Survey event

```yaml
survey_event:
  survey_id: null
  purpose: null
  institution_id: null
  participant_ids: []
  spatial_scope_ref: null
  started_at: null
  ended_at: null
  observation_refs: []
  method_notes: []
  instrument_refs: []
  route_state_refs: []
  weather_context_refs: []
  visibility_context_refs: []
  uncertainty_notes: []
  output_artifact_refs: []
  review_state: DRAFT
```

Suggested review states:
- FIELD_NOTES
- DRAFT
- REVIEWED
- REVISED
- ARCHIVED
- SUPERSEDED

Review status describes workflow. It does not certify every represented feature as canonical truth.

## 3. Spatial scope

A representation must declare what it tries to cover.

```yaml
spatial_scope:
  scope_id: null
  location_ids: []
  connection_ids: []
  segment_ids: []
  landmark_ids: []
  resolution_band: null
  purpose_tags: []
  exclusions: []
```

Candidate resolution bands:
- REGION_OVERVIEW
- DISTRICT
- SETTLEMENT
- ROUTE
- ROUTE_SEGMENT
- SITE
- BUILDING
- FIELD_SKETCH

These are narrative metadata, not map scale rules.

## 4. Cartographic artifact

```yaml
cartographic_artifact:
  artifact_id: null
  title: null
  artifact_type: null
  scope_id: null
  current_edition_id: null
  custodian_ids: []
  access_state_ref: null
  source_survey_ids: []
  copy_lineage_refs: []
  physical_item_ref: null
```

Candidate artifact types:
- ROUTE_SURVEY
- FIELD_SKETCH
- SETTLEMENT_PLAN
- PUBLIC_ROUTE_MAP
- OPERATIONAL_DIAGRAM
- ANNOTATED_COPY
- HISTORICAL_MAP
- PERSONAL_NOTE_MAP

The type does not imply institutional authority.

## 5. Edition continuity

```yaml
cartographic_edition:
  edition_id: null
  artifact_id: null
  created_at: null
  compiler_ids: []
  source_refs: []
  supersedes_edition_id: null
  superseded_by_edition_id: null
  feature_assertion_ids: []
  explicit_unknowns: []
  correction_refs: []
  publication_state: null
```

Suggested publication states:
- PRIVATE_DRAFT
- INTERNAL
- LIMITED_CIRCULATION
- PUBLIC
- WITHDRAWN
- ARCHIVAL_ONLY

A newer edition may correct, narrow or merely add information. Chronology alone does not prove accuracy.

## 6. Map feature assertions

Represented features are claims with provenance.

```yaml
map_feature_assertion:
  assertion_id: null
  edition_id: null
  feature_type: null
  referenced_world_object_id: null
  represented_position_ref: null
  represented_state: null
  source_observation_refs: []
  confidence_band: null
  valid_time_claim: null
  notes: []
```

Candidate feature types:
- LANDMARK
- CONNECTION
- ROUTE_MARKER
- ACCESS_NOTE
- HAZARD_NOTE
- REST_SITE
- OBSERVATION_POINT
- STRUCTURE
- WATERCOURSE
- BOUNDARY_CLAIM

`BOUNDARY_CLAIM` remains a claim unless canon establishes the relevant boundary authority.

## 7. Physical route markers

A physical sign, cairn, painted mark, post, natural reference or maintained fixture can have persistent state independent of maps.

```yaml
route_marker:
  marker_id: null
  connection_id: null
  segment_id: null
  marker_type: null
  canonical_anchor_ref: null
  current_physical_state: null
  maintainer_ids: []
  inscription_or_label_refs: []
  installed_event_id: null
  last_maintenance_event_id: null
```

Suggested physical states:
- PRESENT
- DAMAGED
- MOVED
- OBSCURED
- MISSING
- REPLACED
- UNKNOWN

A moved marker can create navigation uncertainty without moving the actual route.

## 8. Marker observations

```yaml
marker_observation:
  observation_id: null
  marker_id: null
  observer_ids: []
  observed_at: null
  observed_state: null
  observed_position_ref: null
  legibility_state: null
  evidence_refs: []
  confidence_band: null
  limitations: []
```

This makes it possible for Ema to record that a marker was missing during one transect while another later observer finds it replaced.

## 9. Landmark identity and naming

The same world feature may have multiple labels.

```yaml
landmark_name_usage:
  landmark_id: null
  name_text_ref: null
  usage_context: null
  source_refs: []
  first_attested_ref: null
  current_usage_state: null
```

A local nickname, archive survey code and public map label can coexist.

Do not infer that different labels mean different places.

Do not merge two landmarks because their labels match.

Language/translation continuity owns interpretation of nontrivial text.

## 10. Canonical coordinate boundary

The coordinates in `canon/marea-interior-map-resident-network-v2.md` are implementation anchors.

An in-world map does not need to expose raw Minecraft coordinates.

If a build drifts from those anchors:
1. record implementation drift;
2. fix or explicitly migrate the implementation;
3. do not create an in-world explanation merely to excuse a technical mismatch.

`MINECRAFT_BLOCK_POSITION != AUTOMATIC_CANON_REVISION`.

## 11. Travel integration

Travel continues to own:
- physical connection state;
- transport state;
- journeys;
- route knowledge;
- navigation problems.

Cartography provides referenced evidence:

```yaml
route_knowledge:
  map_artifact_refs: []
  direct_survey_refs: []
  marker_observation_refs: []
```

Possessing a current map may support a plausible information path. It does not set route state and does not guarantee a mechanical navigation success.

## 12. Observation integration

Observation owns what was actually observed and with what limitations.

Cartography selects and represents those observations spatially.

A map can omit a valid observation because:
- it is outside scope;
- it was not reviewed yet;
- publication happened earlier;
- the compiler judged it irrelevant to purpose;
- the copy is incomplete.

Omission does not negate the underlying observation.

## 13. Archive integration

Tideglass may preserve:
- original surveys;
- later editions;
- annotated copies;
- retired public maps;
- conflicting sketches;
- correction slips.

Archive custody does not make a representation correct.

A withdrawn map can remain historically important.

## 14. Information-circulation integration

A revised map being published does not update every actor.

Information circulation can track:
- who received edition A;
- who later received correction B;
- which public board still displays an older copy;
- which visitor carries a private annotated version.

## 15. Identity and authority integration

An actor may be authorized to:
- perform a field survey;
- review a survey;
- maintain a marker;
- publish a public route map;
- update an operational copy.

Those are separate scopes.

A person allowed to make observations does not automatically gain authority to alter the canonical route registry or institutional publication.

## 16. Route-state reconciliation

When a map conflicts with current route state, preserve all three records:
- what the edition says;
- what current route authority says;
- what new observations show.

Possible outcomes:
- map is stale;
- route state record needs review;
- observation was local/temporary;
- represented feature was misidentified;
- multiple records remain unresolved.

Never silently replace one with another.

## 17. Survey revision workflow

Recommended sequence:

```text
field observation
-> field note
-> source review
-> draft feature assertion
-> review
-> edition publication or internal update
-> circulation
-> later observation may trigger correction/revision
```

Not every field note needs publication.

## 18. Personal annotations

Players and NPCs may annotate copies.

```yaml
map_annotation:
  annotation_id: null
  base_edition_id: null
  author_id: null
  created_at: null
  annotation_type: null
  content_ref: null
  source_refs: []
  privacy_state: null
```

Candidate types:
- REMINDER
- OBSERVATION
- HYPOTHESIS
- ROUTE_PREFERENCE
- WARNING
- NAME_VARIANT
- OBJECTIVE_NOTE

Personal annotation is not institutional publication.

## 19. Map-copy lineage

Copies can introduce divergence.

```yaml
map_copy:
  copy_id: null
  source_edition_id: null
  copied_at: null
  copier_id: null
  reproduction_method: null
  known_omissions: []
  added_annotation_ids: []
  custody_ref: null
```

A copy may be faithful, simplified or accidentally incomplete. Deliberate falsification remains a social/case claim and must not be inferred merely from divergence.

## 20. Historical maps

Historical maps are valuable evidence even when operationally obsolete.

They can support:
- past route alignment questions;
- former marker positions;
- changed place names;
- infrastructure history;
- comparison against current field observations.

A historical map does not reopen settled canonical coordinates by itself.

## 21. Unknown and unmapped state

A representation may explicitly record unknown space or uncertain detail.

Do not force every blank area to hide a dungeon, secret route or reward.

`UNMAPPED != UNDISCOVERED_WORLD_OBJECT`.

A blank can simply mean the artifact did not cover that area.

## 22. Minecraft projection

Minecraft/Cobblemon may render:
- signposts;
- map boards;
- marker blocks/models;
- held map items;
- discovered-location UI;
- trails and structures.

Presentation must consume Narrative/canon state.

It must not decide:
- whether a marker is historically authentic;
- whether a map edition is current;
- whether a route is legally/operationally open;
- whether a survey observation is accepted;
- whether a map feature is true;
- canonical coordinate migrations.

Chunk unload cannot erase marker history. Block destruction caused by technical state cannot silently become canonical vandalism or route change.

## 23. Tactical-map boundary

A route or Minecraft area may inspire a BattleSpec but cannot be copied uncritically into tactical authority.

Battle assembly must separately validate:
- participant footprints;
- legal cells;
- range/LoS geometry;
- movement rules;
- terrain/hazard semantics;
- encounter objectives.

`OVERWORLD_MAP != BATTLESPEC_GEOMETRY`.

A cartographic line showing a path does not guarantee every tactical cell along it is legal movement.

## 24. PTU navigation boundary

PTU Survival covers navigation, geography, scouting and tracking. Narrative may establish what information and tools are plausibly available before adjudication.

Narrative must not invent:
- Cartography Skill;
- navigation DCs;
- map-quality bonuses;
- automatic tracking success;
- Survival rank changes;
- Feature or Edge effects.

If a route problem is mechanically contested, PTU/Caelo plus current AutoPTU implementation govern it.

## 25. Minimal Marea implementation

The first implementation needs only:
- stable IDs for two existing map/survey artifacts;
- one route-marker record on Sendero del Vidrio;
- two editions or copies that disagree on one bounded feature;
- one field observation capable of narrowing the discrepancy;
- Tideglass provenance links;
- no new coordinates.

Recommended first slice: `Two Maps, One Bend`.

## 26. Persistence rules

Persist:
- artifact identity;
- edition lineage;
- source surveys;
- feature assertions;
- explicit unknowns;
- map-copy lineage where story-relevant;
- marker identity/state history;
- observations;
- corrections;
- circulation refs when relevant.

Do not persist every transient UI pan/zoom, every generated minimap tile or every player waypoint as world canon.

## 27. Long-term value

This layer supports later:
- exploration questlines;
- archaeological mapping;
- changing roads;
- route restoration;
- wilderness expeditions;
- historical boundary disputes if canon establishes them;
- dungeon maps;
- visitor maps;
- ecological transects;
- infrastructure plans;
- public route notices;
- Minecraft build audits.

The same architecture lets Ouros grow spatially without forcing every new discovery to rewrite a single supposedly perfect map.