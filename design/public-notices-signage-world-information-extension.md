# Public Notices, Signage & Physical Information Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already stores information, publications, maps, access rules, route state, events, closures, service status and actor knowledge. This extension defines how those records become persistent physical information inside explorable places.

Its focus is signs, bulletin boards, posters, timetable panels, trail notices, closure placards, public map boards and similar surfaces that a player can actually encounter in Minecraft/Cobblemon.

The core rule is:

physical display is a projection of authoritative state, not the authority itself.

A sign can be damaged while the rule remains valid. A notice can remain readable after it has become stale. A copied poster can be accurate without being officially authorized. A wrong sign can mislead people without changing world truth.

## Authority boundaries

### Media / Communications

`media-communications-information-layer.md` owns information packets, publications, channels, delivery and corrections.

This extension owns the physical display instance.

### Cartography / Wayfinding

`cartography-survey-wayfinding-layer.md` owns maps, editions, surveyed geometry and route knowledge.

A public map board references a map artifact or edition. The board does not own geography.

### Public Space / Travel / Maintenance / Events / Weather / Storefront / Transit

Those systems own access, route, facility, event, forecast, commercial and service truth.

A posted notice may project those states. It cannot create them.

### Libraries / Archives / Public Memory

Those systems own durable records and historical preservation. This extension may hand superseded or historically important notices to them.

## 1. Information surface

```yaml
information_surface:
  surface_id: null
  location_id: null
  zone_id: null
  surface_type: null
  operator_ref: null
  steward_ref: null
  mounting_ref: null
  capacity_band: null
  current_condition: READABLE
  access_state: ACCESSIBLE
  displayed_notice_ids: []
  map_artifact_refs: []
  history_refs: []
  minecraft_projection_ref: null
  canon_reference_ids: []
```

Candidate surface types are descriptive:

- BULLETIN_BOARD
- NOTICE_BOARD
- TRAILHEAD_BOARD
- MAP_BOARD
- TIMETABLE_PANEL
- SERVICE_STATUS_PANEL
- POSTER_FRAME
- DOOR_NOTICE
- TEMPORARY_PLACARD
- WAYFINDING_SIGN
- OTHER

The type does not imply public ownership or legal authority.

## 2. Posted notice

```yaml
posted_notice:
  notice_id: null
  surface_id: null
  source_info_id: null
  source_state_ref: null
  claim_ids: []
  notice_type: null
  display_summary: null
  issuer_ref: null
  authorization_ref: null
  posted_by_ref: null
  posted_at: null
  effective_from: null
  effective_until: null
  supersedes_notice_id: null
  superseded_by_notice_id: null
  removal_due_at: null
  display_state: DISPLAYED
  truth_status_ref: null
  provenance_refs: []
```

Candidate notice types:

- REQUEST
- SAFETY_NOTICE
- ROUTE_NOTICE
- CLOSURE_NOTICE
- REOPENING_NOTICE
- EVENT_NOTICE
- SCHEDULE
- SERVICE_STATUS
- MAP_UPDATE
- PUBLIC_MEETING
- RESEARCH_REQUEST
- LOST_PROPERTY_NOTICE
- CORRECTION
- ADVERTISEMENT
- COMMUNITY_ACTIVITY
- OTHER

`truth_status_ref` points outward. The notice does not score its own truth.

## 3. Display lifecycle

Suggested display states:

- DRAFTED
- READY_TO_POST
- DISPLAYED
- PARTIALLY_OBSCURED
- DAMAGED
- SUPERSEDED_VISIBLE
- REMOVED
- ARCHIVED
- UNKNOWN

A notice can be both `SUPERSEDED_VISIBLE` and physically readable.

Removing a notice changes display state only. It does not delete the source request, closure, publication or rule.

## 4. Physical condition and readability

```yaml
surface_condition_observation:
  observation_id: null
  surface_id: null
  notice_id: null
  observed_at: null
  observer_ref: null
  condition_band: null
  readable_elements: []
  obscured_elements: []
  damage_refs: []
  photo_refs: []
  confidence_band: null
```

Possible condition bands:

- CLEAR
- WEATHERED
- PARTLY_OBSCURED
- DAMAGED_READABLE
- MOSTLY_UNREADABLE
- MISSING

Condition is observational. A torn poster is not automatically vandalism. A missing notice is not proof of deliberate removal.

## 5. Authorization and authorship

```yaml
notice_authority_edge:
  notice_id: null
  issuer_ref: null
  authorization_source_ref: null
  scope_ref: null
  valid_from: null
  valid_until: null
  verification_state: UNVERIFIED
```

Suggested verification states:

- UNVERIFIED
- VERIFIED
- DISPUTED
- EXPIRED
- REVOKED
- NOT_REQUIRED

The world may contain unofficial community posters, personal requests or copied notices. Those can still be useful without being treated as institutional orders.

## 6. Revision and replacement

```yaml
notice_revision:
  revision_id: null
  old_notice_id: null
  new_notice_id: null
  reason_type: null
  changed_claim_ids: []
  changed_time_window: false
  changed_location_scope: false
  changed_authority_ref: false
  created_at: null
  evidence_refs: []
```

Candidate reasons:

- CORRECTION
- SCHEDULE_CHANGE
- CLOSURE_EXTENDED
- REOPENED
- ROUTE_CHANGED
- EVENT_MOVED
- REQUEST_WITHDRAWN
- REQUEST_FULFILLED
- PUBLICATION_UPDATED
- PHYSICAL_REPLACEMENT

Old notices should remain available to Public Memory or Archives when historically relevant.

## 7. Observation and actor knowledge

```yaml
notice_observation:
  observation_id: null
  actor_id: null
  notice_id: null
  observed_at: null
  readable_claim_ids: []
  observed_revision_state: null
  location_id: null
  resulting_knowledge_refs: []
```

A player or NPC only learns what was readable at that time.

If an actor read yesterday's schedule and never sees today's correction, outdated behavior can be legitimate continuity rather than an AI error.

## 8. Request-board projection

A board may display public requests, but request state remains elsewhere.

```yaml
request_notice_projection:
  notice_id: null
  request_ref: null
  visibility_policy_ref: null
  prerequisite_state_refs: []
  requester_contact_ref: null
  acceptance_owned_by_ref: null
  completion_owned_by_ref: null
```

Rules:

- display does not equal acceptance;
- acceptance does not require permanent display;
- completion does not require immediate physical removal;
- removing the notice never completes the request;
- private or sensitive requests need not appear on any board;
- a board should expose only information the requester plausibly chose to publish.

## 9. Map-board projection

```yaml
map_board_projection:
  surface_id: null
  map_artifact_id: null
  map_edition_id: null
  mounted_at: null
  last_verified_at: null
  stale_reason_refs: []
```

A map board can show a superseded edition. This creates a useful world-state discrepancy without mutating geography.

## 10. Schedule and service projection

Timetables and opening-hours panels should point to service state.

```yaml
schedule_projection:
  notice_id: null
  service_ref: null
  schedule_version_ref: null
  effective_window_ref: null
  exception_refs: []
  last_synced_at: null
```

A ferry cancellation, shop closure or clinic relocation becomes visible when the corresponding surface updates. If the panel fails to update, the stale display remains an observable problem.

## 11. Surface occupancy and priority

Do not simulate every sheet of paper.

For important surfaces, use qualitative occupancy:

- EMPTY
- LIGHT
- NORMAL
- CROWDED
- OVERFULL

Priority rules can come from the surface operator when canon establishes them. The generator must not invent municipal posting law or remove notices solely because a board is visually full.

## 12. Minecraft/Cobblemon projection contract

The adapter-facing goal is to create visible, deterministic manifestations of narrative state.

A future projection can map a notice to:

- a sign block or sign-compatible object;
- a framed texture or poster entity;
- a board interaction UI;
- a timetable panel;
- an NPC indicator linked to an existing request;
- a map texture derived from a specific map edition;
- temporary barrier signage linked to an active restriction.

The projection must store `source_notice_id` or equivalent stable identity.

Safe behavior:

- update displayed text when an authoritative notice revision is issued;
- preserve an old physical notice when the story requires stale information;
- show different surfaces in different locations with different update timing;
- render a closure sign only when a restriction record exists;
- retain physical damage independently from underlying policy;
- make interactions return provenance-aware summaries rather than hidden truth.

Unsafe behavior:

- sign text directly edits canonical world state;
- any player-placed sign becomes an official notice;
- breaking a closure sign opens the route;
- a sign saying a route is safe disables hazards or wild spawns;
- a poster grants a quest without an underlying request record;
- a visual icon creates an NPC relationship or authority edge;
- a map texture reveals undiscovered world truth automatically.

## 13. Discovery design

Physical information should complement exploration.

Use boards for:

- public institutional requests;
- routine service updates;
- local events;
- route/access notices;
- research calls;
- public meetings;
- corrections and reopening notices.

Prefer direct observation, conversations or location triggers for:

- sensitive personal matters;
- ecological phenomena not yet publicly understood;
- covert faction activity;
- private relationship scenes;
- emergent consequences;
- mysteries where public knowledge itself is incomplete.

## 14. Conflict patterns

Useful conflicts come from state divergence:

- old timetable vs current service;
- old map vs repaired route;
- official closure notice vs missing barrier;
- community poster vs institutional statement;
- two boards updated at different times;
- requester says the board summary is incomplete;
- correction exists but one neighborhood has not received it;
- physical notice removed while its source state remains active.

These are evidence problems, not hidden truth scores.

## 15. Encounter integration

### Encounter: Trailhead Update Under Pressure

Narrative premise:

A trail restriction has changed and a stewarding team needs to replace the visible guidance at a familiar trailhead while a local Pokémon situation makes the immediate area unsafe.

Full version may require:

- noncombatants moving through or withdrawing from the space;
- protected work position or CLEAR_ROUTE objective;
- changing access lanes;
- interception/forced movement if creatures contest the route;
- terrain/weather/hazard state when rules establish it;
- territorial or withdrawal-aware tactical AI;
- adapter playback that preserves the exact notice revision and route state.

Reduced version:

Evacuate the workers before combat. Keep the trail restriction in world state. Run a static battle in a reviewed nearby arena using supported mechanics. After the authoritative result, the responsible narrative system updates the route and Pass 68 materializes the replacement notice. The battle cannot itself reopen the trail.

### Encounter: Station Notice Replacement

Narrative premise:

A transit/service panel carries outdated information during an interruption. Updating it requires access to a location currently unsafe because of a battle-capable threat.

Full version may require:

- civilians withdrawing;
- protect/access objective state;
- dynamic doors or barriers;
- forced movement/interception;
- non-KO tactical priorities;
- exact adapter writeback to both service state and displayed notice.

Reduced version:

Clear civilians and freeze the service as `LIMITED`, `SUSPENDED` or another state owned by Travel/Transit. Resolve a static battle. Then update the panel as a separate world-state action. A victory does not prove the old notice was fraudulent or restore the service.

## 16. Noncombat mystery: Three Boards, Two Updates

Three public surfaces show apparently conflicting information about the same closure or event. Investigation reconstructs posting times, revision provenance and who had access to which version.

Possible resolution classes:

- one board never received the correction;
- one notice was physically replaced late;
- two notices refer to different effective windows;
- one is an unofficial copy;
- the source state changed twice in a short period;
- a board is showing the correct old historical notice in the wrong active slot.

The mystery can resolve without any liar, sabotage or crime.

## 17. Persistence arc: A Board Learns the Town

Visit 1 establishes ordinary uses of a local board.

Visit 2 adds a public request and a route notice.

Visit 3 resolves the request but leaves the old notice visible until the next maintenance/update cycle.

Visit 4 adds a correction after a service change.

Visit 5 shows that regular NPCs now use different surfaces depending on habit, creating plausible uneven knowledge.

Later callbacks can preserve old photographs, archived notices or remembered misinformation without keeping the board permanently cluttered.

## 18. Mechanical boundaries

This extension creates no PTU bonuses or tactical rules.

Posted information can affect actor knowledge and player decision-making. It does not change:

- movement speed or costs;
- Accuracy/Evasion;
- initiative;
- Skills or Edges;
- Move legality;
- Ability behavior;
- Item effects;
- Trainer Features;
- damage/status;
- terrain/weather/hazards;
- reactions/interception;
- AI tactical scoring.

Any encounter that uses those systems must declare the corresponding engine dependency.

## 19. Canon questions

Before promotion, Ouros needs answers for:

- which settlements use physical public boards;
- which institutions can post official notices;
- whether regions use standardized symbols or highly local practices;
- which technologies support dynamic timetable/status displays;
- how accessibility is represented on physical notices;
- what privacy rules apply to public requests;
- who maintains and removes expired material;
- which notices are archived and by whom;
- how much text Minecraft can show legibly without replacing environmental storytelling with menus.
