# Ouros Cartography, Surveying & Wayfinding Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already has authoritative location state, travel connections, route knowledge, research observations, media/public information, archives, seasonality, archaeology and changing infrastructure.

This layer defines how maps represent those systems without becoming an omniscient copy of world truth.

The core rule is simple:

world geography and map knowledge are separate states.

A road may exist but not appear on a player's map. A map may show a bridge that no longer exists. A cave may be known from one entrance but not another. A survey may correctly record a landmark while remaining uncertain about the route beyond it.

## 1. Authoritative geography

The existing world graph remains the source of physical truth.

```yaml
spatial_feature:
  feature_id: null
  feature_type: null
  parent_region_ids: []
  geometry_ref: null
  connected_feature_ids: []
  current_physical_state_ref: null
  active_variant_refs: []
  world_truth_refs: []
```

This layer does not replace Travel's `travel_connection`, route state or location ownership.

It adds representations of those states.

## 2. Map artifact

A map is an authored or generated information object.

```yaml
map_artifact:
  map_id: null
  title: null
  map_type: null
  creator_ids: []
  institution_id: null
  created_at: null
  surveyed_time_range: null
  source_record_ids: []
  represented_region_ids: []
  edition_id: null
  access_state: null
  medium: null
  current_holder_ids: []
  provenance_ids: []
```

Candidate map types:

- regional overview;
- settlement map;
- route map;
- trail map;
- cave map;
- dungeon plan;
- harbor chart;
- transit map;
- ecological survey map;
- historical map;
- infrastructure plan;
- player field map;
- emergency map.

`map_type` does not grant mechanical functionality.

## 3. Map edition

Maps should be versioned rather than silently overwritten.

```yaml
map_edition:
  edition_id: null
  map_family_id: null
  version_label: null
  published_at: null
  supersedes_id: null
  source_survey_ids: []
  correction_ids: []
  known_limitations: []
  stale_after_event_ids: []
  status: current
```

Suggested status values:

- current;
- superseded;
- historical;
- disputed;
- draft;
- incomplete;
- withdrawn.

A superseded map remains a valid historical artifact.

## 4. Map feature representation

A map entry points to a world feature but stores what the map claims about it.

```yaml
map_feature:
  map_feature_id: null
  map_id: null
  represented_feature_id: null
  geometry_claim: null
  label_claim: null
  category_claim: null
  access_claim: null
  condition_claim: null
  source_ids: []
  confidence_band: null
  last_verified_at: null
  redaction_state: null
  annotation_ids: []
```

A map feature can be wrong without changing the actual feature.

## 5. Discovery state

Do not reduce knowledge to one binary fog-of-war bit.

```yaml
spatial_knowledge:
  holder_id: null
  feature_id: null
  discovery_state: unknown
  source_ids: []
  last_confirmed_at: null
  known_geometry_ref: null
  known_access_points: []
  known_landmark_ids: []
  known_hazard_ids: []
  known_connection_ids: []
  uncertainty_notes: []
```

Suggested discovery states:

- UNKNOWN;
- DETECTED;
- APPROXIMATE;
- MAPPED;
- VERIFIED_RECENTLY;
- STALE;
- DISPUTED;
- REDACTED;
- KNOWN_INACCESSIBLE.

`DETECTED` supports concepts such as a visible ruin, unknown cave marker or reported landmark whose detailed identity is not yet established.

## 6. Survey record

Surveying creates evidence about geography.

```yaml
survey_record:
  survey_id: null
  surveyor_ids: []
  institution_ids: []
  purpose_ids: []
  area_ids: []
  started_at: null
  completed_at: null
  method_refs: []
  observation_ids: []
  measurement_ids: []
  landmark_records: []
  route_trace_ids: []
  uncertainty_notes: []
  equipment_refs: []
  environmental_state_refs: []
  result_status: draft
```

Surveying does not automatically produce perfect geometry.

## 7. Route trace

A route trace records a traveled or observed path.

```yaml
route_trace:
  trace_id: null
  survey_id: null
  actor_ids: []
  start_feature_id: null
  end_feature_id: null
  observed_waypoint_ids: []
  path_geometry_ref: null
  traversal_time_observation: null
  conditions_observed: []
  interruption_ids: []
  certainty_band: null
  resulting_connection_claim_id: null
```

A trace can support an existing Travel connection, propose a new one, or show that a published path is stale.

## 8. Landmark record

Landmarks help navigation remain grounded in the Minecraft world rather than only the UI.

```yaml
landmark_record:
  landmark_id: null
  feature_id: null
  observer_ids: []
  visible_from_refs: []
  distinguishing_traits: []
  seasonal_variants: []
  accessibility_representation_refs: []
  current_state_ref: null
  confidence_band: null
```

Potential landmarks:

- ridge silhouette;
- tower;
- bridge;
- unusual tree or rock formation;
- trail marker;
- harbor beacon;
- settlement skyline;
- waterfall;
- cave mouth;
- rail or road junction;
- large public artwork;
- natural sound source when accessibility rules are satisfied.

Do not create mechanical detection ranges here.

## 9. Map correction

Corrections must preserve history.

```yaml
map_correction:
  correction_id: null
  target_map_id: null
  target_feature_id: null
  proposer_ids: []
  proposed_at: null
  evidence_ids: []
  change_type: null
  old_claim: null
  proposed_claim: null
  review_state: pending
  accepted_at: null
  resulting_edition_id: null
```

Possible change types:

- new feature;
- changed route;
- removed feature;
- renamed feature;
- corrected geometry;
- changed access;
- changed condition;
- changed category;
- added hazard note;
- removed stale warning;
- redaction.

## 10. Player annotation

Players may add personal information without converting it to global truth.

```yaml
map_annotation:
  annotation_id: null
  author_id: null
  map_id: null
  feature_ref: null
  location_ref: null
  annotation_type: null
  content_ref: null
  created_at: null
  source_ids: []
  visibility_scope: private
  verification_state: unverified
```

Candidate annotation types:

- note;
- warning;
- suspected entrance;
- resource observation;
- encounter observation;
- meeting point;
- route preference;
- inaccessible area;
- temporary camp;
- research marker;
- case marker.

No annotation becomes canon merely because many players copy it.

## 11. Shared map knowledge

Sharing a map transfers information, not physical access.

```yaml
map_share_event:
  share_id: null
  sender_id: null
  recipient_ids: []
  map_id: null
  included_annotation_ids: []
  redacted_feature_ids: []
  shared_at: null
  communication_channel_id: null
```

A recipient may learn that a cave exists while still lacking the tools, permission or route state needed to reach it.

## 12. Map authority

Maps can come from different institutions.

Potential publishers:

- civic survey office;
- transport operator;
- research institution;
- conservation service;
- League institution;
- rescue organization;
- local guide association;
- museum/archive;
- private company;
- club;
- player expedition.

Publisher reputation affects how actors interpret a map, not whether its claims become true.

## 13. Map disagreement

Two maps can disagree for understandable reasons.

Common causes:

- different survey dates;
- seasonal changes;
- temporary closures;
- changed infrastructure;
- differing scale;
- imprecise older methods;
- translation differences;
- political naming disputes;
- hidden/private routes;
- erosion or disaster;
- partial cave exploration;
- deliberate redaction.

The system should first look for chronology and scope before generating fraud or conspiracy.

## 14. Historical cartography

Old maps can reveal world change.

They may support:

- lost roads;
- former coastlines;
- old rail or ferry routes;
- abandoned neighborhoods;
- renamed places;
- collapsed caves;
- previous habitat boundaries;
- old ownership/custody records;
- archaeology;
- missing-person investigations;
- public-memory disputes.

Historical maps belong in the Archives layer when stored by an institution.

## 15. Ecological maps

Ecological maps must distinguish observation coverage from population truth.

```yaml
ecological_map_layer:
  map_id: null
  subject_taxon_or_collective_ids: []
  observation_ids: []
  time_window: null
  surveyed_area_ids: []
  unsurveyed_area_ids: []
  inferred_distribution_claim_ids: []
  sensitive_location_redactions: []
```

No heatmap should modify Cobblemon spawn state by itself.

## 16. Hazard and crisis maps

Emergency maps represent current operational knowledge.

Potential overlays:

- closed routes;
- shelter locations;
- flooded areas;
- damaged bridges;
- fire boundary;
- evacuation staging sites;
- communications outages;
- safe water points;
- medical capacity.

These overlays consume Crisis/Infrastructure state. They do not create hazards.

## 17. Cartography and travel compression

The existing Travel layer owns journey execution.

This layer can answer:

- does the actor know the connection?
- how recently was it confirmed?
- do they know a bypass?
- do they possess a usable map or guide?
- is the destination known precisely or approximately?

Travel decides whether the journey compresses.

A mapped route is not automatically safe.

## 18. Cartography and research

Science owns observations, measurements and claims.

Cartography can visualize them.

Examples:

- migration observations on a seasonal map;
- pollution measurements along a river;
- archaeological sites by survey phase;
- acoustic listening stations;
- clinic case origins after privacy aggregation;
- infrastructure faults by network segment.

Visualization never changes the underlying evidence.

## 19. Map-sensitive secrecy

Sensitive coordinates should support coarse disclosure.

Example levels:

- exact location;
- local zone;
- settlement/route only;
- region only;
- withheld.

This can protect:

- nesting sites;
- protected archaeological contexts;
- private homes;
- medical subjects;
- covert case locations;
- rare populations;
- confidential infrastructure;
- player-created private spaces.

Redaction must have a source and authority context.

## 20. Wayfinding without perfect minimaps

Recommended design principle:

The UI may help orientation, but important exploration should still be legible through the Minecraft environment.

Support:

- landmarks;
- road/trail signs;
- route numbering or naming if canon supports it;
- silhouettes;
- lighting/beacons;
- settlement architecture;
- environmental transitions;
- optional compass/map tools;
- accessible nonvisual equivalents.

Do not create frustration by hiding all orientation cues.

## 21. Accessibility

Critical navigation information must not depend only on color, tiny icons, sound, or memorizing a visual map.

Possible equivalents:

- searchable location list;
- text route description;
- high-contrast map mode;
- icon shapes plus color;
- named landmarks;
- distance bands when supported by UI;
- captions/text for acoustic landmarks;
- keyboard/controller navigable map interface.

The Accessibility layer owns final policy.

## 22. Multiplayer cartography

Players may have different spatial knowledge.

The system should support:

- private annotations;
- party-shared annotations;
- club/institution maps;
- public maps;
- temporary expedition layers;
- selectively redacted maps;
- later contribution to institutional surveys.

A player should not learn another player's secret base, private home or sensitive discovery merely because both use the same global map UI.

## 23. Minecraft representation

Potential physical representations:

- map walls;
- notice-board route diagrams;
- trail markers;
- survey posts;
- field notebooks;
- signs at junctions;
- transit maps;
- archive drawers;
- research overlays in UI;
- per-player discovered markers;
- temporary expedition markers;
- damaged/outdated signs after world events.

Minecraft remains presentation and overworld interaction. It must not become the rules authority for PTU navigation checks.

## 24. PTU / Caelo boundary

This layer does not define:

- Survival DCs;
- Perception DCs;
- tracking DCs;
- navigation bonuses;
- map-item bonuses;
- automatic hidden-route detection;
- Tracker behavior;
- Naturewalk behavior;
- travel speeds;
- forced-march rules;
- getting-lost penalties;
- weather navigation penalties;
- cave visibility rules;
- movement capabilities.

Those must come from the supplied PTU/Caelo rules and current implementation.

## 25. AutoPTU boundary

Most cartography is overworld/world-state logic.

AutoPTU should receive a battle map only after the tactical arena is instantiated.

Cartography may influence narrative setup:

- players know an alternate entrance;
- the group enters from a different side;
- a hazard was identified before battle;
- a route was avoided;
- an evacuation point is known.

It may not directly grant:

- accuracy;
- initiative;
- movement;
- damage;
- cover;
- terrain immunity;
- hidden target knowledge;
- legal action access.

## 26. Encounter contract: Lost Survey Marker

Narrative premise:

A field team discovers that a sequence of survey markers no longer matches the current trail after erosion and vegetation change. The players need to determine whether the route moved, the markers moved, or the old map was simply imprecise.

Full version dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including forced movement only if unstable slopes displace combatants;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle for selected legal combatants;
- terrain/weather/hazards/zones/reactions if slopes or weather change tactical legality;
- move-specific behavior;
- abilities;
- items where selected;
- Trainer Features/perks where selected;
- AI legal-action infrastructure;
- AI tactical policy if enemies must protect/avoid survey equipment;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version:

Surveying, erosion and marker correction occur entirely in the overworld. If wild Pokémon or another actor triggers combat, AutoPTU receives a static legal arena with blockers and ordinary battle objectives. No slope displacement, marker HP, equipment interaction or survey bonus is simulated.

## 27. Encounter contract: Cave Traverse Mapping

Narrative premise:

An expedition attempts to connect two separately known cave systems and determine whether they are physically one network.

Full version dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement if climbing, pushes, narrow ledges or rescue repositioning matter;
- core calculations;
- action economy/initiative;
- full lifecycle;
- full stateful damage;
- status lifecycle;
- terrain/weather/hazards/zones/reactions for unstable or changing cave conditions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy for route/escape objectives;
- Minecraft/Cobblemon/Craftics playback.

Reduced version:

Cave mapping uses overworld exploration and validated PTU/Caelo Skill checks outside battle. Combat, if triggered, uses a static chamber. Discovering the connecting passage updates world/map state after exploration resolution.

## 28. Encounter contract: Moving Front Survey

Narrative premise:

Researchers are mapping a seasonal ecological boundary while a wild collective shifts through the same area.

Full version dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement if the encounter requires withdrawal lanes or moving protection;
- core calculations;
- action economy/initiative;
- full lifecycle;
- full stateful damage;
- status lifecycle;
- terrain/weather/hazards/zones/reactions if seasonal terrain is mechanically active;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks where used;
- AI legal-action infrastructure;
- AI tactical policy for non-KO movement objectives;
- Minecraft/Cobblemon/Craftics playback.

Reduced version:

The ecological front moves as world state between observations. Survey work occurs outside battle. Any encounter is a conventional static battle selected from the actual visible subgroup, and the result writes back disturbance/observation state without inventing collective combat mechanics.

## 29. Promotion checklist

Before any map or survey candidate becomes canon:

1. Confirm the underlying locations exist in canon.
2. Confirm the map publisher/creator exists or is intentionally introduced.
3. Preserve the represented date/edition.
4. Separate claims from current world truth.
5. Check whether sensitive coordinates require redaction.
6. Validate any PTU Skill/capability use.
7. Confirm Minecraft can present the required map state without revealing private data.
8. Confirm battle dependencies if the concept enters AutoPTU.

## Open questions

- Which map institutions exist in Ouros?
- Are official regional maps public goods, commercial products, League services or mixed?
- How much precise geometry should the player map expose?
- Can players create and name unofficial trails?
- How are map disputes reviewed?
- How should cave verticality be represented?
- Which spatial knowledge persists across a party when members split?
- Can old maps be wrong due to historical measurement limits without creating frustration?
- Which Minecraft/Cobblemon hooks can support per-player POIs and annotations?
- Which PTU/Caelo rules govern Survival, navigation, tracking and route-finding?
