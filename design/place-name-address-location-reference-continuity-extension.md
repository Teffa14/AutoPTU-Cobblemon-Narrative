# Ouros Place Name, Address & Location Reference Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-29

## Purpose

Ouros already has persistent geography, maps, signs, routes, buildings, residences, land units, shipments, dispatch requests and archives. Those systems repeatedly need to answer a narrower question: when the same place is described by different names, spellings, historical labels, street references, entrances or delivery points, which references point to the same place and which remain uncertain?

This extension provides neutral continuity for place references. It does not create a universal postal system, legal addressing regime, geographical-names authority, ownership registry, road-naming law, language policy or navigation mechanic.

The core principle is:

physical place identity, public name, textual address, map label and access point are separate states.

## Authority boundaries

Cartography owns map artifacts, editions, geometry claims, surveys and map knowledge.

Public Notices and Signage owns physical display instances.

Travel and Roads own routes, connections, closures and actual travel state.

Courier owns shipment destination, delivery attempts and custody.

Request/Dispatch owns request locations and resource assignments.

Land Parcels owns neutral land-unit identity, boundary evidence and authored land-interest claims.

Residential owns residence and household location state.

Public Memory and Archives own historical interpretation, custody and durable records.

Construction and Maintenance own physical changes to sites and entrances when those changes arise from their work.

This extension owns only the continuity graph linking a persistent place to names, address descriptors, local aliases, historical labels, entrances and other scoped references.

## 1. Persistent place reference

```yaml
place_reference_record:
  place_ref_id: null
  world_feature_ref: null
  parent_place_refs: []
  current_primary_name_refs: []
  current_address_descriptor_refs: []
  historical_name_refs: []
  local_alias_refs: []
  entrance_refs: []
  service_point_refs: []
  map_feature_refs: []
  land_unit_refs: []
  structure_refs: []
  provenance_refs: []
  canon_status: proposed
```

`place_ref_id` is an internal continuity key. It is not automatically visible to characters.

Hard rules:

`PLACE_REF_ID != PUBLIC_ADDRESS`

`PLACE_EXISTS != PLACE_HAS_NAME`

`NAME_CHANGED != PLACE_MOVED`

`PLACE_MOVED != NAME_CHANGED`

`SAME_NAME != SAME_PLACE`

`DIFFERENT_NAME != DIFFERENT_PLACE`

## 2. Place name record

```yaml
place_name_record:
  place_name_ref: null
  place_ref_id: null
  rendered_name: null
  language_or_script_ref: null
  name_context: current|local|historical|institutional|descriptive|translated|other
  status: CURRENT|FORMER|VARIANT|DISPUTED|UNKNOWN
  effective_from: null
  effective_until: null
  source_refs: []
  authority_ref: null
  standardization_ref: null
  visibility_scope: null
  supersedes_ref: null
  notes_ref: null
```

A name can be widely used without a formal authority. A standardized name can exist without erasing local or historical forms.

`STANDARDIZED_NAME != ONLY_VALID_REFERENCE`

`LOCAL_NAME != FALSE_NAME`

`FORMER_NAME != FALSE_HISTORICAL_RECORD`

`NAME_RECOGNIZED != NAME_CURRENT`

## 3. Append-only name history

Renaming never rewrites old events.

An event recorded at `Old Mill Road` remains historically correct if the road is later called something else. A current UI may optionally render the current label alongside the historical form, but the source event keeps its original reference and timestamp.

```yaml
place_name_change_event:
  event_id: null
  place_ref_id: null
  prior_name_refs: []
  new_name_refs: []
  effective_at: null
  decision_or_source_ref: null
  public_notice_refs: []
  map_update_refs: []
  sign_update_refs: []
  downstream_update_refs: []
```

`NAME_CHANGE_EFFECTIVE != EVERY_SYSTEM_UPDATED`

`MAP_UPDATED != SIGN_UPDATED`

`SIGN_UPDATED != COURIER_DIRECTORY_UPDATED`

`DIRECTORY_UPDATED != ARCHIVE_RECORD_REWRITTEN`

## 4. Location descriptor

Not every useful reference is a proper name.

```yaml
location_descriptor:
  descriptor_ref: null
  place_ref_id: null
  descriptor_type: street_address|intersection|landmark_relative|district|building|entrance|service_point|route_marker|other
  rendered_value: null
  component_refs: []
  effective_from: null
  effective_until: null
  source_refs: []
  precision_scope_ref: null
  confidence_band: null
  status: CURRENT|FORMER|PARTIAL|DISPUTED|UNKNOWN
```

A description can be operationally useful without being a formal address.

`DESCRIPTOR_RESOLVES_TO_PLACE != DESCRIPTOR_IS_FORMAL_ADDRESS`

`ADDRESS_MATCH != OWNERSHIP`

`ADDRESS_MATCH != RESIDENCE`

`ADDRESS_MATCH != ACCESS_AUTHORIZED`

## 5. Reference precision

```yaml
place_reference_scope:
  scope_ref: null
  place_ref_id: null
  precision_kind: region|settlement|district|street|site|structure|entrance|service_point|approximate_landmark|other
  geometry_or_owner_ref: null
  sufficient_for_purposes: []
  insufficient_for_purposes: []
```

A reference sufficient for Travel may be insufficient for Courier. A structure reference sufficient for a meeting may be insufficient for an accessible entrance. An approximate landmark may be enough for a survey but not for dispatch.

`REFERENCE_VALID_FOR_ONE_PURPOSE != VALID_FOR_ALL_PURPOSES`

## 6. Entrance and access-point continuity

```yaml
place_access_point:
  access_point_ref: null
  place_ref_id: null
  physical_feature_ref: null
  access_point_type: public_entrance|staff_entrance|delivery_point|platform|gate|berth|counter|trailhead|other
  active_from: null
  active_until: null
  current_operational_state_ref: null
  accessibility_refs: []
  service_owner_ref: null
  source_refs: []
  predecessor_ref: null
  successor_ref: null
```

The owner system decides whether an access point is open, authorized or safe. This layer only preserves identity and succession.

`CORRECT_PLACE != CORRECT_ENTRANCE`

`ENTRANCE_EXISTS != ENTRANCE_OPEN`

`DELIVERY_POINT_RECOGNIZED != PUBLIC_ENTRANCE`

`ENTRANCE_CHANGED != SITE_CHANGED`

## 7. Alias and variant resolution

```yaml
place_reference_alias:
  alias_ref: null
  rendered_form: null
  candidate_place_refs: []
  alias_kind: local|former|alternate_spelling|translation|descriptive|institutional|abbreviation|other
  used_by_refs: []
  observed_time_range: null
  source_refs: []
  resolution_state: UNREVIEWED|SUPPORTED|VERIFIED_FOR_SCOPE|DISPUTED|AMBIGUOUS|HISTORICAL_ONLY
```

One alias may legitimately resolve to more than one candidate when evidence is insufficient.

`AMBIGUOUS != INVALID`

`AMBIGUOUS != DECEPTIVE`

## 8. Same-name collision

```yaml
place_name_collision:
  collision_id: null
  rendered_name: null
  candidate_place_refs: []
  detected_at: null
  affected_record_refs: []
  disambiguating_context_refs: []
  state: OPEN|PARTIALLY_RESOLVED|RESOLVED|ACCEPTED_AMBIGUITY
```

A world may contain two `North Bridges`, two `Old Mills` or two locally named `Lantern Hills`. The generator must not merge them because text matches.

## 9. Historical location linkage

```yaml
historical_place_linkage:
  linkage_id: null
  historical_record_ref: null
  rendered_location_text: null
  candidate_place_refs: []
  proposed_place_ref: null
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  linkage_state: UNREVIEWED|SUPPORTED|VERIFIED_FOR_SCOPE|DISPUTED|REJECTED|ACCEPTED_AMBIGUITY
  reviewed_at: null
```

A journal saying `the old station` may remain ambiguous if two stations existed during that period.

Public Memory can interpret cultural meaning after linkage. Archives owns custody. This extension does not invent historical conclusions.

## 10. Downstream update event

Different systems may adopt a changed reference at different times.

```yaml
place_reference_update:
  update_id: null
  place_ref_id: null
  target_system_ref: null
  old_reference_ref: null
  new_reference_ref: null
  requested_at: null
  effective_at: null
  completed_at: null
  update_state: PENDING|APPLIED|PARTIAL|FAILED|NOT_REQUIRED|UNKNOWN
  evidence_refs: []
```

Potential targets:

- map edition;
- wayfinding sign;
- courier directory;
- transport timetable;
- public notice template;
- emergency/dispatch directory;
- library/archive catalog;
- business listing;
- institutional roster.

No target is presumed to exist universally.

## 11. Route and navigation boundary

This layer never computes pathfinding.

Travel and Roads decide which connection is traversable. Cartography decides what a map claims. Minecraft supplies physical geometry. A place-reference resolution can say `this old name refers to that bridge`; it cannot say the bridge is currently reachable unless the relevant owner state confirms it.

`NAME_RESOLVED != ROUTE_OPEN`

`COORDINATE_MATCH != PATH_EXISTS`

`LANDMARK_VISIBLE != LANDMARK_REACHABLE`

## 12. Courier boundary

Courier may consume a resolved place reference and an active delivery point.

A delivery attempt may still fail because:

- the address descriptor is incomplete;
- the building is correct but the delivery point moved;
- access is blocked;
- a recipient moved;
- the old label remains in the sender's records;
- two same-named places exist.

The place-reference layer never marks the parcel delivered.

`DESTINATION_RESOLVED != DELIVERY_COMPLETED`

## 13. Dispatch boundary

Request/Dispatch can preserve the exact location text received with a request and separately store the resolved place reference used for assignment.

```yaml
dispatch_location_resolution:
  request_ref: null
  original_location_text_ref: null
  candidate_place_refs: []
  resolved_place_ref: null
  resolution_time: null
  confidence_band: null
  evidence_refs: []
```

If later information changes the resolution, the original briefing remains historical truth.

`REQUEST_LOCATION_TEXT != VERIFIED_INCIDENT_LOCATION`

`PLACE_NAME_MATCH != SAME_INCIDENT`

## 14. Minecraft/Cobblemon projection

Minecraft may render:

- current signs;
- weathered former signs;
- street markers;
- entrance numbers;
- old station labels reused as decoration;
- renamed plazas;
- temporary wayfinding boards;
- closed former entrances;
- landmarks that survive after their original function ends.

Minecraft object names, coordinates, UUIDs, scoreboard tags and entity IDs remain implementation data.

A sign block does not create a name. A renamed sign does not move a place. Breaking a sign does not revoke a name. A waypoint marker does not create route legality.

Cobblemon BattleState has no authority over place identity, naming, addressing, access permission or historical linkage.

## 15. Narrative generators

Useful low-conflict situations include:

- a record still uses the former name of a street;
- a business uses a local district name absent from the current map;
- two places share one colloquial label;
- a new entrance opens while old directions remain common;
- a temporary construction entrance becomes the permanent delivery point;
- a historical letter references a vanished landmark;
- a renamed station retains its previous name in older tickets;
- a community prefers a traditional name while an institution uses another current form.

These should create investigation, memory, navigation or service friction without requiring villains.

## 16. Encounter pattern — Wayfinding Team Withdrawal

Full premise:

A survey, courier or response team is resolving a disputed or stale location reference when an independent tactical threat appears. The evidence work pauses and the team withdraws.

Full dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL for escort/Intercept/forced displacement;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL for staged withdrawal;
- full stateful damage pipeline — PARTIAL if attacks occur;
- status lifecycle — PARTIAL for exact implemented statuses only;
- terrain/weather/hazards/zones/reactions — BLOCKING for protected corridors, dynamic obstacles or generalized reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for WITHDRAW/PROTECT/CLEAR_ROUTE;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic projection.

Full version: BLOCKED FOR RICH SEMANTICS.

Reduced version: READY.

Reduced contract:

1. Reference-resolution work pauses before BattleSpec creation.
2. Surveyors, couriers, records and noncombatant Pokémon withdraw outside the grid.
3. Ouros selects explicit combatants.
4. AutoPTU receives static reviewed geometry.
5. Victory may create only `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR`.
6. The narrative owner separately resumes or abandons the location-resolution task.

`TACTICAL_VICTORY != PLACE_REFERENCE_RESOLVED`.

## 17. Encounter pattern — Old Entrance Chokepoint

Full premise:

A party reaches the correct persistent site using an outdated entrance reference. A separate tactical threat blocks the immediate approach to the currently valid access point.

Full version requires the same partial/blocking families above if escort, changing access, hazards or objective-aware AI are active.

Reduced version: READY.

The current entrance state is resolved outside BattleSpec. AutoPTU receives a conventional static encounter at the approach. Victory may produce `IMMEDIATE_APPROACH_CLEAR`; it cannot authorize entry, update an address, prove ownership or complete a delivery.

`APPROACH_CLEAR != ACCESS_AUTHORIZED`.

## 18. Encounter pattern — Same-Name Landmark Perimeter

Full premise:

Two reports used the same colloquial landmark name for different physical places. Investigators reach one candidate site and an independent encounter occurs nearby.

Reduced version: READY.

The ambiguity remains outside BattleSpec. Combat victory cannot decide which historical record or report referred to which place.

`BATTLE_RESULT != RECORD_LINKAGE`.

## 19. Canon questions deliberately left open

- Which regions maintain standardized place-name records, if any?
- Which institutions can establish or change a public name?
- Are street addresses used everywhere, only in dense settlements, or not at all in some regions?
- Which languages/scripts and multilingual naming practices exist?
- How are local and traditional names treated?
- Are numbering systems used for buildings, routes, lots, platforms or berths?
- Which services maintain their own directories?
- How quickly do maps, signs and service records update after a change?
- Can a place have several simultaneous current names for different communities?
- Which historical renamings already belong to canon?
- Which settlements use landmark-relative directions instead of formal addresses?

Until authored, all remain UNKNOWN/NON-CANON.