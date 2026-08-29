# Ouros Land Parcels, Boundaries, Use Rights & Records Continuity Extension

Status: PROPOSED. Not established canon.
Date: 2026-08-29

## Purpose

This extension preserves persistent identity and provenance for land units, boundary evidence, physical markers, mapped geometry, recorded ownership/use/access/stewardship claims when canon supplies them, later corrections and cross-system handoffs.

It does not define universal Ouros property law. It does not create titles, deeds, easements, leases, adverse possession, zoning, taxation, compulsory acquisition, public-right-of-way doctrine or survey authority. Every legal or institutional concept beyond neutral evidence continuity requires an authored regional source.

## Existing-system boundaries

Homes/Housing owns residence, household membership, access policy and home history. Residence may reference an ownership claim, but residence never proves ownership.

Cartography owns maps, map editions, survey records, geometry claims, route traces, corrections and knowledge state.

Ranching owns managed groups, paddocks, husbandry operations and ranch service state.

Conservation owns protected-area stewardship, ecological restrictions and conservation decisions.

Travel and Roads own physical travel connections, route state, detours and journeys.

Civic Governance owns public proposals and decisions only where a canon-authored body has the relevant mandate.

Adjudication owns deciding-process continuity only when canon provides the deciding body, scope and available outcomes.

Archives, Personal Records and Public Notices own record custody, publication and historical access.

This extension owns the connective record between physical land identity, boundary evidence and authored interests.

## Required separations

LAND_UNIT_IDENTIFIED != OWNERSHIP_ESTABLISHED
MAP_LINE_DRAWN != BOUNDARY_EXACT
SURVEY_MEASUREMENT_RECORDED != REGISTRY_UPDATED
BOUNDARY_MARKER_PRESENT != MARKER_AUTHORITATIVE
FENCE_PRESENT != PARCEL_BOUNDARY
ADDRESS_MATCH != LAND_UNIT_IDENTITY
OCCUPANCY != OWNERSHIP
STEWARDSHIP != OWNERSHIP
ACCESS_USED != ACCESS_RIGHT_ESTABLISHED
MAINTENANCE_DUTY != OWNERSHIP
PUBLIC_WORK_PRESENT != PUBLIC_RIGHT_AUTHORED
RECORDED_CLAIM != CLAIM_ADJUDICATED
OLD_RECORD_SUPERSEDED != OLD_RECORD_ERASED
PHYSICAL_FEATURE_MOVED != RECORDED_BOUNDARY_AUTOMATICALLY_MOVED
POKEMON_PRESENT != HUMAN_LAND_INTEREST_CREATED
BATTLE_WON != LAND_INTEREST_RESOLVED

## 1. Persistent land unit

A land unit is a stable spatial identity used to connect records. The label deliberately avoids assuming a specific regional property-law concept.

```yaml
land_unit:
  land_unit_id: null
  public_label: null
  parent_area_ids: []
  current_geometry_claim_id: null
  address_refs: []
  structure_ids: []
  land_use_state_refs: []
  current_interest_claim_ids: []
  historical_interest_claim_ids: []
  boundary_segment_ids: []
  survey_record_ids: []
  map_representation_ids: []
  source_refs: []
  canon_status: proposed
```

A region may later map this object to a canon-specific parcel, lot, holding, reserve compartment, public corridor or another local concept. Until then, `land_unit` is an information identity only.

## 2. Geometry claim

Geometry needs explicit provenance and precision scope.

```yaml
land_geometry_claim:
  geometry_claim_id: null
  land_unit_id: null
  geometry_ref: null
  source_type: null
  source_ref: null
  observed_or_effective_at: null
  produced_at: null
  precision_or_uncertainty_ref: null
  purpose_ref: null
  supersedes_geometry_claim_id: null
  status: ACTIVE_CLAIM
```

Candidate source types:
- field_survey;
- registry_map;
- public_map;
- infrastructure_plan;
- historical_plan;
- archive_sketch;
- authored_canon_geometry;
- observed_physical_enclosure;
- player_annotation.

Only `authored_canon_geometry` may be treated as exact world/legal truth when the relevant canon explicitly grants that status.

## 3. Boundary segment

A land unit may share part of its recorded extent with another unit or with a public/natural feature.

```yaml
boundary_segment:
  boundary_segment_id: null
  land_unit_ids: []
  geometry_claim_ids: []
  physical_feature_refs: []
  marker_observation_ids: []
  current_record_state: UNKNOWN
  discrepancy_case_ids: []
  source_refs: []
```

Candidate record states:
UNKNOWN, CONSISTENT_ACROSS_CURRENT_RECORDS, DIFFERENT_GEOMETRIES_RECORDED, FIELD_REVIEW_PENDING, UPDATED_AFTER_REVIEW, HISTORICAL_ONLY.

These states describe evidence continuity. They do not adjudicate competing rights.

## 4. Physical boundary feature

Minecraft can render a fence, wall, hedge, ditch, road edge, stream bank, post, stone or other feature. The feature's purpose and authority must remain evidence-backed.

```yaml
boundary_feature_observation:
  observation_id: null
  world_feature_ref: null
  observed_geometry_ref: null
  observed_at: null
  observer_ids: []
  feature_kind: null
  condition: null
  purpose_claim_ids: []
  linked_boundary_segment_ids: []
  authority_claim_ref: null
  source_refs: []
```

A fence can be for animal control. A wall can be decorative. A ditch can predate the current record. A marker can have been moved accidentally. The generator must preserve ambiguity when evidence is incomplete.

## 5. Survey-to-land relationship

The Cartography layer owns `survey_record`. This extension consumes its output through a scoped link.

```yaml
land_survey_link:
  link_id: null
  survey_id: null
  land_unit_ids: []
  boundary_segment_ids: []
  measurement_refs: []
  resulting_geometry_claim_ids: []
  discrepancy_ids: []
  review_required_refs: []
```

A completed field survey may create strong evidence. Whether that evidence changes an official record depends on a canon-authored process.

## 6. Land-interest claim

Use a neutral claim object rather than inventing a legal regime.

```yaml
land_interest_claim:
  claim_id: null
  land_unit_id: null
  claimant_actor_or_institution_ids: []
  interest_type_ref: null
  scope_geometry_ref: null
  source_record_ids: []
  effective_from: null
  effective_until: null
  recognition_state: UNKNOWN
  deciding_matter_id: null
  supersedes_claim_id: null
  source_refs: []
```

`interest_type_ref` must come from canon. Candidate design placeholders may include ownership, occupancy_permission, stewardship, access_permission, maintenance_responsibility, operational_control or other authored relationships. Those names must not be treated as a complete regional law code.

Recognition states may remain coarse:
UNKNOWN, ASSERTED, RECORDED_BY_AUTHORED_INSTITUTION, DISPUTED, UNDER_REVIEW, SUPERSEDED, HISTORICAL.

`RECORDED_BY_AUTHORED_INSTITUTION` means exactly that. It does not necessarily equal ultimate truth where the region allows review.

## 7. Occupancy and residence link

```yaml
land_residence_link:
  land_unit_id: null
  residence_ids: []
  structure_ids: []
  occupancy_permission_refs: []
  ownership_claim_refs: []
  access_policy_refs: []
```

Homes/Housing remains authoritative for who lives there. This extension never infers an ownership share from residence duration, family relationship, household membership, decoration or stored items.

## 8. Stewardship and managed-use link

```yaml
managed_land_link:
  land_unit_id: null
  owner_system_ref: null
  managed_area_ref: null
  steward_ids: []
  operational_boundary_refs: []
  land_interest_claim_refs: []
```

Examples include a ranch paddock, protected area, research site, public park or managed woodland. Operational boundaries may be narrower or broader than recorded land geometry.

## 9. Access and crossing record

A path crossing a land unit must not silently create a right.

```yaml
land_access_record:
  access_record_id: null
  land_unit_ids: []
  route_or_crossing_ref: null
  physical_path_ref: null
  use_observation_ids: []
  authored_permission_ref: null
  authored_restriction_ref: null
  maintenance_owner_ref: null
  current_operational_state_ref: null
  source_refs: []
```

Keep separate:
- physical path existence;
- known repeated use;
- permission or restriction;
- maintenance responsibility;
- Travel connection state;
- accessibility for a specific actor.

A shortcut can be locally familiar while its formal status remains unknown.

## 10. Public-works intersection

```yaml
land_public_works_intersection:
  intersection_id: null
  project_id: null
  affected_land_unit_ids: []
  planned_geometry_ref: null
  required_land_interest_refs: []
  current_authorization_refs: []
  construction_state_ref: null
  record_update_state: null
  unresolved_question_ids: []
```

The public-works project may be physically complete while a map edition, public notice or administrative record still awaits update. Do not backfill the record from Minecraft construction blocks.

## 11. Boundary discrepancy episode

```yaml
boundary_discrepancy:
  discrepancy_id: null
  land_unit_ids: []
  discovered_at: null
  discovery_source_ids: []
  geometry_claim_ids: []
  physical_feature_observation_ids: []
  survey_refs: []
  stated_questions: []
  owner_system_handoffs: []
  deciding_matter_id: null
  status: OPEN
  resolution_record_ids: []
```

Candidate states:
OPEN, FIELD_REVIEW_PENDING, RECORD_REVIEW_PENDING, REFERRED_TO_AUTHORED_AUTHORITY, UPDATED_WITHOUT_DISPUTE, DECIDED_BY_AUTHORED_AUTHORITY, CLOSED_WITH_UNRESOLVED_SCOPE.

The discrepancy itself is content. Fraud, trespass, theft, corruption or deliberate marker movement must never be generated without evidence.

## 12. Record revision lineage

```yaml
land_record_revision:
  revision_id: null
  target_record_id: null
  prior_version_id: null
  new_version_id: null
  reason_claim_ids: []
  evidence_refs: []
  approved_by_ref: null
  effective_at: null
  published_at: null
```

Old editions remain retrievable through Archives/Public Records where access permits it. A corrected line does not erase why earlier characters relied on the older version.

## 13. Address continuity

Addresses are labels for finding places, not universal parcel identifiers.

```yaml
address_history:
  address_history_id: null
  location_or_structure_id: null
  land_unit_ids: []
  address_label: null
  active_from: null
  active_until: null
  renaming_event_ref: null
  source_refs: []
```

A structure can keep an old address after land-unit reconfiguration. Multiple structures can share a managed property. An address change does not move the building.

## 14. Natural-feature movement

Physical features can move because of erosion, floods, shoreline change, landslide, road reconstruction or channel work.

```yaml
moving_feature_land_intersection:
  intersection_id: null
  physical_feature_id: null
  historical_geometry_refs: []
  current_geometry_ref: null
  affected_boundary_segment_ids: []
  governing_rule_ref: null
  review_state: UNKNOWN
```

The physical feature's new position is world truth. Whether a recorded boundary follows it is a separate question requiring canon. The generator must not decide that rule.

## 15. Pokémon and land boundaries

Pokémon behavior can reveal habitat, routine, access points or broken fences. It cannot prove human property relationships.

Keep separate:
- individual Pokémon presence;
- wild collective territory;
- managed group location;
- Trainer partnership/ownership;
- ecological stewardship area;
- human land unit;
- operational enclosure;
- legal or recorded interest.

A Mareep crossing a fence says something about animal movement or fence condition. It says nothing by itself about parcel ownership.

## 16. Evidence hierarchy without hidden truth scores

The system should preserve source type and scope instead of assigning one global confidence number.

Useful comparisons:
- field measurement versus old overview map;
- recorded institutional geometry versus public tourism map;
- current physical enclosure versus historic photograph;
- local testimony versus archived survey plan;
- road-maintenance record versus ownership claim;
- address record versus land-unit identifier.

Contradictions create questions. They do not automatically establish wrongdoing.

## 17. Quiet world-state use

This layer should support ordinary continuity as well as quests:
- fence repair updates a physical feature but leaves land records unchanged;
- a ranch changes operator while its land-unit identity persists;
- a trail map is corrected after a survey;
- a public park receives a renamed entrance without changing geometry;
- a house changes residents while historical claims remain in the archive;
- an old stone marker becomes a local landmark;
- a subdivision or consolidation occurs only if canon explicitly authors that kind of event;
- an NPC refers to an obsolete field name that still resolves through aliases.

## 18. Mystery grammar

Strong parcel/boundary mysteries should favor chronology, scope and purpose.

Possible question patterns:
- Which line was meant for navigation and which for land administration?
- Was the fence intended as a boundary or animal-control feature?
- Which survey edition existed when the old road was built?
- Did the physical river move after the record was created?
- Is the apparently duplicated property actually one structure with two historical addresses?
- Did a public-work corridor change while the surrounding land identities stayed stable?
- Which actor had maintenance duty even though another actor held the ownership claim?

The answer may remain `UNKNOWN` if the evidence cannot support more.

## 19. Long-term story arc pattern

`A Valley Learns Where Its Lines Came From` begins with ordinary ranches, homes, paths, public works and protected areas whose boundaries are socially taken for granted. A new survey or infrastructure project exposes several harmless inconsistencies. One turns out to be an old approximate map, another an operational fence unrelated to the land record, and a third a real disputed claim that must be handed to a canon-authored authority. During the process, local shortcuts, family memories, Pokémon routines and retired markers become visible pieces of regional history. Later development can reuse those records without resetting the valley.

The arc does not require a villain or a universal court system.

## 20. Minecraft/Cobblemon representation

Minecraft/Cobblemon may render:
- fences, walls, hedges, ditches and posts;
- survey markers and field equipment;
- archive maps and public diagrams;
- roads, paths and crossings;
- ranch, reserve and neighborhood visual boundaries;
- construction that later changes the landscape;
- Pokémon crossing or following physical features;
- old and new marker variants where world state requires them.

Presentation never creates land authority.

Block coordinates do not automatically become cadastral geometry. Breaking or moving a fence does not transfer ownership. A claimed chunk does not establish canon. A sign does not create an access right. An entity standing inside a polygon does not gain occupancy permission. Cobblemon BattleState has no authority over land identity, claims, access rights, survey conclusions or adjudication.

## 21. PTU / Caelo boundary

This extension defines no universal:
- land-title mechanic;
- deed or registry action;
- survey Skill DC;
- property-line detection check;
- access-right determination roll;
- trespass rule;
- structure/marker HP;
- boundary movement rule after river or shoreline change;
- species-derived parcel sensing;
- Type-derived survey competence;
- Move/Ability/Item/Trainer Feature that creates ownership, validates a survey or establishes a legal boundary.

Use exact supplied rules only when a governing source proves the mechanic.

## 22. Encounter contract — Survey Marker Recovery Perimeter

Narrative premise:
A field team has documented a disputed marker sequence when a separate encounter threatens the work site. The goal is to secure immediate access and preserve already-collected evidence.

Full version:
- survey team withdraws during active turns;
- selected combatants can legally Intercept or be displaced;
- protected survey/evidence zone matters tactically;
- reaction ordering handles crossing/protection windows;
- AI understands PROTECT and WITHDRAW;
- semantic playback shows the authoritative withdrawal and perimeter state.

Permanent capability dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL for staged withdrawal;
- full stateful damage pipeline: PARTIAL for selected governed combat effects;
- status lifecycle: PARTIAL when selected governed statuses are used;
- terrain/weather/hazards/zones/reactions: BLOCKING for protected-zone reactions or environmental displacement;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for PROTECT/WITHDRAW;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING for semantic withdrawal/perimeter playback.

Reduced version: READY. Complete or pause the field survey first. Secure measurements, notes and markers as world-state evidence. Remove survey staff and equipment from BattleSpec. Use a static reviewed approach. A tactical win only secures immediate access; it cannot validate a marker or decide a boundary.

## 23. Encounter contract — Access Corridor Diversion

Narrative premise:
A regularly used crossing or service corridor is temporarily blocked by an encounter while its formal land status is under separate review.

Full version:
- civilians/workers withdraw or reroute during battle;
- route objective requires CLEAR_ROUTE/PROTECT policy;
- Intercept or forced movement can matter;
- boundary/corridor zones may change tactical choices;
- lifecycle stages the diversion;
- adapter renders semantic closure and reroute.

Capability pressure:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if corridor-crossing reactions or changing zones exist;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

Reduced version: READY. Close the crossing and complete rerouting before BattleSpec creation. Keep travelers, workers and controlled objects off-grid. Fight at a static chokepoint. Winning permits the owner system to reassess access; it never creates a right of way.

## 24. Encounter contract — Flood-Shifted Fence Reinspection

Narrative premise:
After a flood or channel change, a familiar fence no longer aligns with archived geometry. A reinspection party reaches the stable edge of the affected area when combat occurs.

Full version:
- unstable/muddy/water-adjacent cells could change;
- environmental displacement or reactions may matter;
- forced movement near hazardous cells matters;
- lifecycle can stage changing conditions;
- AI must protect/withdraw around the survey objective;
- adapter shows authoritative environmental state.

Capability pressure:
- targeting/footprints/range/LoS: VERIFIED baseline;
- base movement legality: VERIFIED baseline;
- complete movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL only for exact governed effects;
- status lifecycle: PARTIAL only for exact governed effects;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

Reduced version: READY. The flood event has already ended. Restrict exploration to stable reviewed ground. The survey discrepancy remains world-state content. Any battle uses a dry static approach with no mud, current, collapsing bank or marker-object mechanics. After combat, Cartography and the authored land authority continue the review.

## 25. Implementation-safe writeback

Battle outcomes may write only tactical facts proven by AutoPTU and narrow immediate world consequences authorized by Ouros, such as `IMMEDIATE_APPROACH_SECURED`.

They may not write:
- `BOUNDARY_VALIDATED`;
- `OWNERSHIP_PROVEN`;
- `ACCESS_RIGHT_GRANTED`;
- `SURVEY_ACCEPTED`;
- `PUBLIC_CORRIDOR_CREATED`;
- `CLAIM_REJECTED`;
- `REGISTRY_UPDATED`.

Those belong to evidence or canon-authored institutional workflows.

## 26. Canon questions left open

- Which Ouros regions maintain formal land-unit records, if any?
- What local terms describe land holdings or public corridors?
- Which institutions can record ownership, stewardship, access or maintenance interests?
- Which kinds of claim can be reviewed or adjudicated?
- How precise are older maps and surveys in different regions?
- How are river, shoreline, road or disaster-driven physical changes handled by local law?
- Which records are public, private, archived or protected?
- Do ranches, reserves, sacred sites or League facilities use different land arrangements?
- Which Pokémon have documented trained field roles without implying species-wide survey capability?

Until canon answers them, the layer preserves evidence and uncertainty rather than inventing doctrine.
