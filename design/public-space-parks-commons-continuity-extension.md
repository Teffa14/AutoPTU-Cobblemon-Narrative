# Shared Public Space, Parks & Commons Continuity Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already knows how to build and govern infrastructure, operate events, maintain facilities, track visitors, preserve habitat, represent neighborhoods and remember actor routines. This extension handles the ordinary shared place that remains after those systems finish their own work.

Its scope is intentionally narrow: parks, plazas, courtyards, promenades, greenways, waterfront walks, squares, shared lawns and similar locations used repeatedly by unrelated actors for different purposes.

The extension answers:

- What is the normal shared-use pattern here?
- Which zones and entrances are currently usable?
- Which recurring cohorts use the place, and when?
- Which access or use rules are actually established?
- Which temporary restrictions are active?
- Which uses are compatible or conflicting right now?
- What visible traces from earlier use remain?
- Has an exceptional event handed the place back to ordinary use?

It does not define universal property rights, municipal law, public-access rights, park ownership, policing powers or Pokémon-access rules.

## 1. Authority boundaries

### Civic Governance / Public Works

`civic-governance-public-works-layer.md` owns major collective decisions such as creating, expanding, redesigning, permanently closing or formally changing the mandate of a shared place.

This extension can surface a persistent use conflict that becomes evidence for a civic proposal. It cannot approve the proposal itself.

### Facility Maintenance

`facility-maintenance-repair-inspection-extension.md` owns faults, assessment, work orders, repairs, verification and technical reopening.

This extension records the effect on ordinary use: a bench zone is unavailable, one entrance is closed, a path reroutes or users change routines. It does not diagnose the fault.

### Temporary Event Operations

`temporary-public-event-operations-extension.md` owns festival, tournament, market and other temporary-event overlays.

This extension owns the baseline before the overlay and the ordinary-return state after teardown.

### Tourism / Visitor Pressure

`tourism-visitors-destination-pressure-layer.md` owns destination-level visitor flow and pressure.

This extension can record which specific zones or routines absorb that pressure. It does not calculate why visitors came.

### Conservation / Ecology

`conservation-protected-areas-stewardship-layer.md`, `wild-collective-agency-layer.md`, `interspecies-ecological-relations-layer.md` and `observation-settlement-time-layer.md` own ecological truth, Pokémon collective state and observation evidence.

This extension only records how shared human use intersects with those states.

### Accessibility

`accessibility-participation-accommodations-layer.md` owns accommodation needs, barriers and participation design.

A public-space access state may reference accessibility records but does not invent them.

### Sports / Hobbies / Social Systems

Those systems own activity rules, progression and relationship meaning. This extension records that an authored cohort uses a lawn for practice or a plaza for a club meeting. It cannot infer friendship or grant progression.

## 2. Public-space profile

```yaml
public_space_profile:
  public_space_id: null
  location_id: null
  display_name: null
  space_type: null
  ownership_ref: null
  steward_refs: []
  operator_refs: []
  maintenance_refs: []
  zone_ids: []
  entrance_ids: []
  baseline_use_pattern_ids: []
  active_restriction_ids: []
  active_overlay_refs: []
  ecological_refs: []
  accessibility_refs: []
  current_ordinary_use_state: NORMAL
  history_refs: []
  canon_reference_ids: []
```

Candidate `space_type` values are descriptive only:

- PARK
- PLAZA
- COURTYARD
- PROMENADE
- GREENWAY
- WATERFRONT_WALK
- TOWN_SQUARE
- SHARED_LAWN
- PUBLIC_GARDEN
- COMMONS_OTHER

The label does not establish legal public ownership.

## 3. Ownership, stewardship, operation and maintenance are separate

A shared place may have different actors responsible for different functions.

```yaml
space_responsibility_edge:
  public_space_id: null
  actor_or_institution_id: null
  responsibility_type: null
  scope_zone_ids: []
  mandate_source_ref: null
  active_from: null
  active_until: null
  status: CONFIRMED
```

Possible responsibility types:

- OWNER only when canon establishes ownership;
- STEWARD;
- OPERATOR;
- MAINTAINER;
- EVENT_HOST for a bounded overlay;
- CONSERVATION_CONTACT;
- ACCESSIBILITY_CONTACT;
- SECURITY_OR_SAFETY_CONTACT only when mandate is established.

Frequent presence does not create any of these roles.

## 4. Zones

Important shared places should be segmented only where different use or access states matter.

```yaml
public_space_zone:
  zone_id: null
  public_space_id: null
  zone_type: null
  connected_zone_ids: []
  entrance_refs: []
  ordinary_use_tags: []
  fixture_refs: []
  ecological_refs: []
  current_access_state: OPEN
  restriction_refs: []
  maintenance_refs: []
  temporary_overlay_refs: []
```

Suggested zone types:

- PATH
- LAWN
- GARDEN
- WATER_EDGE
- PLAZA_FLOOR
- SEATING_AREA
- PLAY_OR_PRACTICE_AREA
- QUIET_AREA
- TRANSIT_CUT_THROUGH
- COURTYARD_EDGE
- OTHER

A zone type must not imply a safety rule or legal entitlement by itself.

## 5. Entrances and partial closure

```yaml
space_entrance:
  entrance_id: null
  public_space_id: null
  connects_from_location_id: null
  connects_to_zone_id: null
  current_state: OPEN
  restriction_refs: []
  accessibility_refs: []
  opening_window_refs: []
  evidence_refs: []
```

Possible states:

- OPEN
- LIMITED
- CLOSED_TEMPORARILY
- CLOSED_FOR_EVENT
- CLOSED_FOR_MAINTENANCE
- CLOSED_FOR_ECOLOGY
- UNKNOWN

One closed entrance should not close the entire place unless the remaining graph truly becomes inaccessible.

## 6. Ordinary use patterns

The layer should remember recurring use without materializing every anonymous user.

```yaml
space_use_pattern:
  use_pattern_id: null
  public_space_id: null
  zone_ids: []
  actor_ids: []
  cohort_ref: null
  activity_ref: null
  recurrence_ref: null
  typical_time_window: null
  seasonality_refs: []
  dependency_refs: []
  observed_since: null
  last_observed_at: null
  current_state: ACTIVE
  evidence_refs: []
```

Examples:

- commuters cutting through a plaza on weekday mornings;
- an authored club practicing on one lawn twice a week;
- workers eating lunch near one entrance;
- residents using a promenade in the evening;
- recurring wildlife observation at dawn;
- maintenance crews watering a garden on a documented schedule.

A pattern can be `OBSERVED` without being a formal reservation or permission.

## 7. User cohorts

```yaml
space_user_cohort:
  cohort_id: null
  public_space_id: null
  cohort_type: null
  estimated_presence_band: null
  identity_refs: []
  recurring_use_pattern_ids: []
  current_presence_state: ABSENT
  public_information_refs: []
```

Possible types:

- RESIDENT_USERS
- COMMUTERS
- WORKERS_ON_BREAK
- CLUB_OR_TEAM
- EVENT_USERS
- VISITORS
- STUDENTS_OR_TRAINEES only where an institution exists
- RESEARCH_OR_STEWARDSHIP_GROUP
- MAINTENANCE_CREW
- OTHER

Do not infer social class, citizenship, age, family structure or relationship from cohort membership.

## 8. Formal use windows and reservations

Observed habit and reserved use must remain separate.

```yaml
space_use_window:
  use_window_id: null
  public_space_id: null
  zone_ids: []
  holder_ref: null
  purpose_ref: null
  start_time: null
  end_time: null
  exclusivity_scope: null
  authorization_ref: null
  setup_ref: null
  teardown_ref: null
  status: SCHEDULED
```

Possible statuses:

- REQUESTED
- SCHEDULED
- ACTIVE
- COMPLETED
- CANCELLED
- SUPERSEDED

The existence of this schema does not imply every Ouros region has a permit or booking system.

## 9. Access and use rule records

Rules need provenance and revision history.

```yaml
space_rule_record:
  rule_id: null
  public_space_id: null
  scope_zone_ids: []
  rule_type: null
  statement_ref: null
  authority_ref: null
  effective_from: null
  effective_until: null
  supersedes_rule_id: null
  evidence_refs: []
  current_status: ACTIVE
```

A sign, NPC statement or habitual practice is not sufficient to create authority by itself. It can create an observation or claim that points toward an existing rule record.

The generator must never create species-specific Pokémon access rules merely because a source game uses them.

## 10. Temporary restrictions

```yaml
space_restriction:
  restriction_id: null
  public_space_id: null
  zone_ids: []
  entrance_ids: []
  restriction_type: null
  cause_ref: null
  owner_system_ref: null
  start_time: null
  expected_review_time: null
  actual_end_time: null
  public_notice_refs: []
  current_state: ACTIVE
```

Candidate causes can reference:

- maintenance;
- event setup/teardown;
- crisis response;
- ecological sensitivity;
- weather preparedness;
- infrastructure outage;
- investigation scene protection;
- an authored institutional rule.

This layer renders the restriction. The owning system determines whether its cause is resolved.

## 11. Shared-use conflict

A conflict is defined through concrete uses and dependencies.

```yaml
shared_use_conflict:
  conflict_id: null
  public_space_id: null
  affected_zone_ids: []
  use_pattern_ids: []
  user_or_cohort_refs: []
  incompatibility_refs: []
  observed_impacts: []
  temporary_mitigation_refs: []
  consultation_or_handoff_refs: []
  current_state: OPEN
```

Examples:

- loud recurring practice overlaps a documented observation window;
- a popular shortcut crosses a restoration zone;
- commuters return before event teardown ends;
- maintenance access blocks the only accessible entrance;
- an unexpectedly famous quiet corner receives more visitors than its fixtures can support.

Do not collapse these into a hostility score.

## 12. Visible traces and place memory

Shared spaces should remember ordinary use through small physical and informational changes.

```yaml
public_space_trace:
  trace_id: null
  public_space_id: null
  zone_id: null
  trace_type: null
  created_by_event_ref: null
  observed_at: null
  condition_ref: null
  significance: LOW
  persistence_state: PRESENT
  owner_system_ref: null
```

Candidate traces:

- worn informal path;
- repaired fixture;
- moved seating;
- temporary sign not yet removed;
- planting or restoration patch;
- recurring chalk/marker area when culturally and materially established;
- new barrier;
- changed noticeboard information;
- evidence of repeated Pokémon presence when Observation/Ecology supports it.

A trace does not automatically prove who caused it.

## 13. Ordinary-return handoff

Exceptional systems should explicitly return the location to shared-use state.

```yaml
ordinary_return_handoff:
  handoff_id: null
  public_space_id: null
  source_system_ref: null
  source_event_ref: null
  completed_at: null
  removed_overlay_refs: []
  remaining_restriction_refs: []
  persistent_trace_refs: []
  updated_use_pattern_refs: []
  condition_check_refs: []
  reopened_zone_ids: []
  still_closed_zone_ids: []
```

This prevents a festival, crisis or repair project from silently resetting or permanently occupying the space.

## 14. Return-to-normal is allowed to create a new normal

`NORMAL` is not a perfect rollback.

After an event, repair or ecological change:

- one entrance may stay rerouted;
- a group may adopt a new meeting point;
- a restored lawn may remain temporarily avoided;
- a formerly quiet area may retain increased visitor interest;
- a newly visible wildlife pattern may change stewardship practice;
- a seating arrangement may remain changed after consultation.

Every retained change needs a source event or decision.

## 15. Recurring-place loop

A reusable shared-space arc can follow:

`BASELINE -> OVERLAP -> PRESSURE -> RESTRICTION/MITIGATION -> REVIEW -> ORDINARY_RETURN -> CALLBACK`

The same place should support many low-intensity scenes between major arcs.

The generator should prefer callbacks to known routines over inventing a new plaza every time it needs a social scene.

## 16. Noncombat activity hooks

Fully usable before new tactical capabilities:

- reconstructing who normally uses a zone and when;
- comparing current access signage with older records;
- discovering why a familiar route has shifted;
- verifying whether an event overlay has fully cleared;
- recording resident and visitor use without inferring opinion;
- inspecting visible traces and handing physical faults to Maintenance;
- comparing overlapping use windows;
- creating a civic evidence packet when a long-term conflict needs formal review;
- updating a public guide after an entrance or route changes;
- documenting recurring Pokémon presence without converting it into a battle rule.

## 17. Encounter contract — Pondside Withdrawal

Narrative premise:

An ordinary shared route passes beside a zone currently used defensively by wild Pokémon. The immediate need is to get routine users away and make the affected section safe enough for later ecological review.

Intended full version:

- civilians or user cohorts withdraw through legal routes;
- multiple safe lanes can change during resolution;
- objective intent is PROTECT/WITHDRAW/CLEAR_ROUTE rather than pure DEFEAT;
- interception or forced displacement matters where PTU defines it;
- terrain/weather/hazards may matter only when exact PTU/Caelo mapping exists;
- wild AI can prefer territory defense or retreat rather than maximizing KOs;
- adapter playback preserves which zone was closed and when it becomes reviewable.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version:

Evacuate ordinary users before tactical resolution. Mark the affected section closed in world state. Run one reviewed static encounter at the safe edge using only supported mechanics. After the authoritative result, Ecology/Conservation and this layer determine whether the zone remains restricted, enters observation or reopens.

The battle cannot prove ownership, establish a permanent access rule or determine the historical cause of previous incidents.

## 18. Encounter contract — Plaza Access Break

Narrative premise:

A threat makes one entrance to a familiar plaza unusable while another route remains available. Clearing the immediate obstruction matters because the space supports daily circulation.

Intended full version:

- multiple exits and withdrawing civilians;
- protected fixtures or noncombatant zones;
- changing access barriers;
- CLEAR_ROUTE/ESCAPE/PROTECT intent;
- interception or forced movement where rules support it;
- tactical AI aware of escape and access;
- exact adapter writeback for each entrance and zone.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version:

Close the plaza to ordinary users first. Choose a reviewed static arena outside protected fixtures. Resolve a normal legal battle. Then perform a separate access/condition review. Winning the battle does not repair a gate, remove a maintenance blocker or create a civic decision.

## 19. Minecraft representation

Safe future representation:

- materialize a small number of significant recurring users and aggregate the rest;
- visibly close only affected entrances/zones where possible;
- persist important signs, barriers, benches, paths and restoration traces;
- remove temporary event scenery only after teardown handoff;
- use time-of-day routines for recurring cohorts when authoritative schedules exist;
- show wild Pokémon presence only from actual ecology/spawn state;
- keep public-space props synchronized with Maintenance/Event/Conservation state.

Unsafe shortcuts:

- crowd size becomes public approval;
- Minecraft presence creates legal permission;
- a player entering a closed zone proves the rule was lifted;
- a despawned barrier means the underlying restriction ended;
- battle victory reopens every zone;
- wild Pokémon spawning repeatedly establishes ownership or permanent territory by itself;
- a familiar NPC becomes the operator because they are often there;
- event props remain forever because no explicit ordinary-return handoff was implemented.

## 20. Canon questions

- Which Ouros settlements have shared parks, plazas, courtyards, greenways, promenades or equivalent spaces?
- Which are genuinely public, privately owned but shared, institutionally managed or culturally communal?
- Which bodies can set or revise access rules?
- Which spaces have formal booking/use systems, if any?
- Which recurring user cohorts deserve persistent identity?
- Which wild Pokémon relationships are documented strongly enough to shape use?
- Which areas are conservation sites rather than general commons?
- How are disputes over overlapping use normally handled region by region?
- Which population densities can Cobblemon represent without damaging performance or readability?

Until these questions are reviewed, names, institutions, access customs and policy assumptions remain proposed.