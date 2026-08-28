# Residential, Household & Relocation Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This layer preserves permanent and semi-permanent residential continuity without turning Ouros into a property-management simulator.

Use it when the important state is where an actor ordinarily lives, who is explicitly associated with that residence, whether the location is currently habitable/accessible, whether a move is temporary or permanent, and what history persists after vacancy, repair, return or reuse.

Settlement owns aggregate housing capability. Hospitality owns temporary commercial lodging. Crisis owns emergency response. Maintenance/Public Works own repair and infrastructure work. Finance owns explicit financial agreements. Case/Authority owns disputes and custody/authority records. This layer stores residential continuity and consumes their outputs.

## 1. Residence identity

```yaml
residence:
  residence_id: null
  location_id: null
  settlement_id: null
  structure_ref: null
  residence_type: house|apartment|shared_house|dormitory|staff_quarters|rural_homestead|other
  current_use_state: residential
  habitability_state: unknown
  access_state: unknown
  resident_link_ids: []
  occupancy_event_ids: []
  relocation_event_ids: []
  facility_dependency_ids: []
  route_dependency_ids: []
  history_event_ids: []
  prior_use_refs: []
  canon_refs: []
```

Residence identity persists through vacancy, repair and resident turnover unless canon explicitly retires or transforms the physical place.

## 2. Resident link

```yaml
resident_link:
  resident_link_id: null
  residence_id: null
  actor_id: null
  link_type: primary_resident|secondary_resident|temporary_resident|staff_resident|guest_with_residential_term|other
  effective_from: null
  effective_to: null
  evidence_ids: []
  current_status: active
  ownership_claim_ref: null
  custody_claim_ref: null
  relationship_claim_ref: null
```

A resident link does not prove ownership, family, friendship, Trainer/Pokémon ownership, financial responsibility or legal tenancy.

## 3. Household grouping

```yaml
household_group:
  household_id: null
  residence_ids: []
  member_actor_ids: []
  membership_evidence_ids: []
  shared_service_dependency_ids: []
  shared_routine_refs: []
  current_split_state: together
  history_event_ids: []
```

Possible split states:
- TOGETHER
- TEMPORARILY_SPLIT
- RELOCATING
- PARTIALLY_RETURNED
- DISSOLVED_BY_EXPLICIT_EVENT

Household membership must be explicit. Co-location alone is insufficient.

## 4. Habitability

```yaml
residential_habitability:
  residence_id: null
  state: unknown
  assessment_time: null
  assessment_authority_ref: null
  evidence_ids: []
  blocking_dependency_ids: []
  limitations: []
  next_review_trigger_ids: []
```

Suggested narrative states:
- HABITABLE
- HABITABLE_WITH_LIMITATIONS
- TEMPORARILY_UNINHABITABLE
- ACCESS_BLOCKED
- UNDER_REPAIR
- VERIFYING
- UNKNOWN

`REPAIR_COMPLETE != HABITABLE`.

`HABITABLE != ACCESSIBLE` when roads, stairs, elevators, bridges or other routes remain unavailable.

## 5. Occupancy event

```yaml
residential_occupancy_event:
  occupancy_event_id: null
  residence_id: null
  actor_ids: []
  event_type: move_in|move_out|temporary_departure|temporary_return|permanent_return|vacancy_start|vacancy_end
  effective_time: null
  evidence_ids: []
  source_decision_ids: []
  resulting_resident_link_ids: []
```

Physical presence does not update residence automatically. A visitor, responder, worker or combatant can be inside a residence without becoming a resident.

## 6. Relocation case

```yaml
residential_relocation:
  relocation_id: null
  actor_or_household_ids: []
  origin_residence_ids: []
  destination_residence_ids: []
  relocation_type: temporary|permanent|partial|emergency|unknown
  reason_refs: []
  announced_scope: null
  authoritative_scope: null
  planned_move_time: null
  actual_departure_time: null
  destination_ready_event_ids: []
  return_expected: null
  return_trigger_ids: []
  status: proposed
  history_event_ids: []
```

Suggested states:
- PROPOSED
- PREPARING
- PARTIALLY_MOVED
- RELOCATED
- RETURN_PENDING
- RETURNING
- COMPLETE
- CANCELLED
- SUPERSEDED

An announcement or actor belief does not define the authoritative relocation scope.

## 7. Temporary displacement

```yaml
residential_displacement:
  displacement_id: null
  actor_or_household_ids: []
  normal_residence_ids: []
  triggering_crisis_or_facility_event_ids: []
  temporary_location_refs: []
  accommodation_system_ref: hospitality|shelter|community_host|other
  current_status: displaced
  return_blocker_ids: []
  support_service_ids: []
```

Emergency shelter occupancy must not overwrite normal residence unless an explicit later relocation occurs.

## 8. Return-to-home transition

```yaml
residential_return_review:
  review_id: null
  residence_id: null
  household_or_actor_ids: []
  repair_complete_refs: []
  habitability_assessment_ref: null
  access_state_refs: []
  utility_or_service_refs: []
  accessibility_refs: []
  care_or_safety_constraints: []
  outcome: pending
  effective_return_time: null
```

Possible outcomes:
- RETURN_AUTHORIZED
- PARTIAL_RETURN
- DELAY_RETURN
- RELOCATE_INSTEAD
- INFORMATION_REQUIRED

Narrative state does not invent who has legal authority to issue these outcomes. The referenced governing system/canon must establish that authority.

## 9. Vacancy and abandonment

```yaml
residential_vacancy:
  residence_id: null
  vacancy_start: null
  vacancy_reason_refs: []
  expected_duration: null
  maintenance_state_refs: []
  security_or_access_refs: []
  reuse_proposal_ids: []
  current_state: vacant
```

Possible states:
- TEMPORARILY_VACANT
- LONG_TERM_VACANT
- ABANDONED_BY_EXPLICIT_FACT
- UNDER_REPAIR
- REUSE_PENDING
- REOCCUPIED

Do not infer abandonment from an empty Minecraft building or unloaded NPCs.

## 10. Residential reuse

```yaml
residential_reuse:
  reuse_id: null
  residence_id: null
  prior_use: residential
  proposed_use: null
  decision_authority_ref: null
  facility_conversion_refs: []
  resident_displacement_refs: []
  public_notice_refs: []
  status: proposed
  effective_time: null
```

Former residences can become workshops, offices, clinics, community rooms, stores, habitat buffers or other canon-approved uses. Prior residential history remains available for callbacks.

## 11. Neighborhood continuity

```yaml
neighborhood_residential_state:
  neighborhood_id: null
  residence_ids: []
  occupied_band: null
  vacancy_band: null
  temporary_displacement_refs: []
  infrastructure_dependency_ids: []
  recurring_resident_actor_ids: []
  service_pressure_refs: []
  ecology_interaction_refs: []
  history_event_ids: []
```

Use coarse bands for population-level presentation. Important individuals keep explicit actor/residence links.

## 12. Residential knowledge and privacy

Residence information is private by default unless canon/world state says otherwise.

Public or observable facts may include:
- a building appears occupied;
- a public evacuation order applies to an area;
- a residence is visibly under repair;
- an actor publicly announced a move;
- a former house is now a public facility.

Private facts may include:
- exact household membership;
- who sleeps in which room;
- ownership or tenancy terms;
- temporary locations after displacement;
- financial arrangements;
- care needs;
- access credentials.

Observation does not grant omniscient residential records.

## 13. Household routines

```yaml
household_routine:
  routine_id: null
  household_or_residence_id: null
  routine_type: departure|return|meal|care|maintenance|delivery|school|work|other
  time_window_refs: []
  actor_ids: []
  dependency_ids: []
  public_visibility: low
  last_observed_event_ids: []
```

Routines are authored continuity aids. They do not force actors to teleport or execute when crisis, travel, work or player decisions override them.

## 14. Residential dependency graph

A residence may depend on:
- road/bridge/rail/ferry access;
- power/water/communications;
- structural maintenance;
- sanitation;
- accessibility accommodations;
- care services;
- wildfire/winter/flood restrictions;
- neighborhood public safety;
- household income or explicit finance state when canon establishes it.

This layer references those systems. It does not recalculate them.

## 15. Dense-world callbacks

Prefer revisiting known residences when state changes:
- repair work becomes visible;
- one household member returns before the rest;
- a neighbor moves away or arrives;
- a temporary route changes access;
- a former residence changes use;
- a displaced household returns;
- a vacant structure becomes habitat-adjacent;
- a recurring delivery or service changes.

This keeps settlements legible without spawning disposable houses.

## 16. No-inference rules

Do not infer:
- ownership from residence;
- tenancy from a key or bed;
- family from cohabitation;
- romance from shared housing;
- poverty from a small residence;
- wealth from a large residence;
- abandonment from temporary absence;
- eviction from move-out;
- criminal trespass from presence;
- Trainer ownership from a Pokémon living in a household;
- custody from feeding/care;
- PTU Rest from being home;
- battle participation from being present during an incident.

## 17. PTU/Caelo boundary

This extension does not define:
- property law;
- rent, mortgage or taxes;
- building capacity;
- domestic Skill checks;
- home-based bonuses;
- recovery rates;
- Rest/Extended Rest timing;
- Pokémon Center healing;
- carrying/moving household goods;
- structural damage or collapse;
- forced entry;
- rescue/carry actions;
- domestic Pokémon job eligibility.

Exact mechanics require project-supplied PTU/Caelo evidence and current AutoPTU support.

## 18. Minecraft/Cobblemon representation

Safe presentation candidates:
- existing houses/apartments and interiors;
- furniture and decorative beds;
- moving boxes and repair props;
- boarded or reopened entrances;
- changed signs/mailboxes where canon supports them;
- recurring resident Pokémon models/forms/poses/cries;
- visible neighborhood occupancy changes using limited authored actors;
- temporary accommodation scenes;
- reopened or converted buildings.

Adapter-required:
- stable residence and household IDs across chunk unload/reload;
- mapping access restrictions to world barriers without making blocks authoritative;
- stable actor/Pokémon identity bindings;
- reviewed tactical arena extraction from domestic spaces;
- semantic playback.

Minecraft/Cobblemon must never decide ownership, household membership, occupancy, eviction, Rest, custody, combatants or battle result.

## 19. Encounter contract — Residential Lane Withdrawal

Narrative premise: a threatening or panicked Pokémon enters a residential lane while residents are already moving to safety.

Full version may require:
- multiple withdrawal routes;
- protection/CLEAR_ROUTE-like objectives;
- Intercept and forced movement;
- reactions;
- narrow reviewed terrain;
- AI tactical policy that understands withdrawal and nonparticipant zones;
- authoritative playback.

Capability dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced version:
Crisis/Residential state evacuates all uninvolved residents before combat. Private interiors, pets/resident Pokémon not selected as combatants, vehicles and household goods are excluded. AutoPTU receives a static lane/courtyard arena. Victory secures only the immediate area; it does not authorize return, change occupancy or resolve housing status.

## 20. Encounter contract — Repair-Site Perimeter Conflict

Narrative premise: a residence under repair cannot complete verification because a nearby encounter makes the work area unsafe.

Full version may require worker withdrawal, protected routes, reactions, obstacles/hazards and objective-aware AI.

Reduced version:
Maintenance suspends work and removes workers/equipment first. The battle occurs on a static safe perimeter. Battle outcome may remove the immediate blocker; Maintenance must still complete repair/verification and Residential must still complete habitability/return review.

## 21. Encounter contract — Vacant House Boundary

Narrative premise: a Pokémon has begun using a long-vacant structure or yard, creating a conflict when reuse is proposed.

Full version may require territorial AI, difficult/fragile terrain, hazards, reactions and possibly environmental interpretation.

Reduced version:
Conservation/Residential determines the actual observed occupancy before combat. The tactical arena is a reviewed safe exterior or cleared interior. No structural collapse, ownership, capture entitlement or eviction is inferred from victory.

## 22. Noncombat content available immediately

- reconcile conflicting address/occupancy reports;
- follow a temporary relocation through repair and return;
- trace why one household returned while neighbors did not;
- document a former residence before adaptive reuse;
- connect household routines to work, school, care and travel state;
- investigate a service failure that affects only part of a neighborhood;
- preserve recurring neighbors across seasons;
- track a household split across temporary accommodations;
- resolve provenance around an apparently abandoned structure without assuming ownership.

## 23. Promotion questions

Before canon promotion confirm:
- residence and settlement exist;
- actor residence links are explicit;
- household membership is supported rather than inferred;
- legal/ownership language is avoided unless canon establishes it;
- privacy is respected;
- dependency states come from authoritative systems;
- relocation scope is explicit;
- repairs and return are separate transitions;
- PTU recovery is not inferred;
- tactical scenes have capability-aware reduced forms.
