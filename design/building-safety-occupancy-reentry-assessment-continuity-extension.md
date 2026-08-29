# Ouros Building Safety, Occupancy & Reentry Assessment Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-29

## Purpose

This extension preserves post-damage building-use decisions between acute crisis response and later maintenance, residential return or service restoration.

It answers bounded questions:
- which spatial scope was observed;
- what evidence existed at that time;
- which technical assessment was produced;
- which use restriction or authorization followed;
- whether a later review superseded the earlier one;
- what remains unknown.

It does not define structural engineering, building law, property rights, repair methods or universal inspection authority.

## Authority boundaries

Use Crisis/Rescue while immediate evacuation, search, rescue or stabilization dominates.

Use Facility Maintenance for faults, work orders, repair, verification and deferred maintenance.

Use Residential continuity for household habitability, displacement and return-to-home state.

Use Workplace, Education, Hospitality, Care, Commercial Services or another service owner for whether that service operates.

Use Civic Governance for future public decisions, major reconstruction or adaptive-reuse proposals.

Use hazard-specific systems such as Seismic, Wildfire, Slope Instability, Flood/Stormwater or Volcanic continuity for the initiating event and its evidence.

This extension stores building-safety assessment and use/reentry continuity across those handoffs.

## 1. Assessed structure

```yaml
assessed_structure:
  structure_id: null
  location_id: null
  facility_refs: []
  residence_refs: []
  current_assessment_scope_ids: []
  active_restriction_ids: []
  current_authorization_ids: []
  observation_ids: []
  technical_assessment_ids: []
  reevaluation_trigger_ids: []
  maintenance_refs: []
  history_event_ids: []
  canon_refs: []
```

A structure can participate in several owner systems without duplicating their state here.

## 2. Spatial assessment scope

```yaml
building_assessment_scope:
  scope_id: null
  structure_id: null
  scope_type: whole_structure|wing|floor|room|entrance|roof|exterior_zone|adjacent_area|authored
  geometry_ref: null
  parent_scope_id: null
  access_refs: []
  service_refs: []
  occupancy_use_refs: []
  current_review_state: unknown
```

Scope is mandatory. A review of an exterior plaza cannot silently authorize an interior floor.

Nested scopes may differ at the same time.

## 3. Condition observation

```yaml
building_condition_observation:
  observation_id: null
  structure_id: null
  scope_id: null
  observed_at: null
  observer_id: null
  observation_method: visual|instrument|record_review|reported|authored
  observed_claim_ids: []
  evidence_refs: []
  confidence: unknown
  limitation_notes: []
```

Observation does not automatically create a diagnosis or use decision.

Examples of safe observation language:
- crack visible on north wall;
- ceiling material on floor;
- door frame displaced;
- monitoring instrument unavailable;
- water entered room;
- no visible change observed from accessible exterior.

`NO_VISIBLE_CHANGE_OBSERVED != STRUCTURE_PROVEN_SAFE`.

## 4. Technical assessment

```yaml
building_technical_assessment:
  assessment_id: null
  structure_id: null
  scope_ids: []
  assessor_ids: []
  assessor_authority_ref: null
  assessed_at: null
  input_observation_ids: []
  input_record_ids: []
  interpretation_claim_ids: []
  uncertainty_notes: []
  recommended_use_state: null
  recommended_restrictions: []
  followup_trigger_ids: []
  supersedes_assessment_id: null
  status: issued
```

`assessor_authority_ref` remains null until canon identifies who may perform a relevant assessment.

Technical recommendations and official authorization remain separable.

## 5. Use restriction

```yaml
building_use_restriction:
  restriction_id: null
  structure_id: null
  scope_ids: []
  restriction_type: no_entry|limited_entry|escorted_entry|service_use_limited|occupancy_limited|authored
  issuing_authority_ref: null
  basis_assessment_ids: []
  basis_crisis_or_hazard_refs: []
  issued_at: null
  effective_from: null
  review_trigger_ids: []
  exception_refs: []
  status: active
  superseded_by_id: null
```

No restriction type implies a real-world legal category. Canon supplies the institution and meaning.

## 6. Occupancy/use authorization

```yaml
building_use_authorization:
  authorization_id: null
  structure_id: null
  scope_ids: []
  authorized_use_refs: []
  authorizing_authority_ref: null
  basis_assessment_ids: []
  conditions: []
  issued_at: null
  effective_from: null
  review_trigger_ids: []
  status: active
  superseded_by_id: null
```

Possible authored outcomes may include:
- USE_ALLOWED_FOR_SCOPE;
- USE_ALLOWED_WITH_LIMITATIONS;
- ENTRY_ONLY_FOR_AUTHORIZED_TASK;
- CONTINUE_RESTRICTION;
- MORE_INFORMATION_REQUIRED.

These are Ouros narrative states, not imported placard classifications.

## 7. Reevaluation trigger

```yaml
building_reevaluation_trigger:
  trigger_id: null
  structure_id: null
  affected_scope_ids: []
  trigger_type: subsequent_event|new_observation|repair_completed|monitoring_change|reported_change|scheduled_review|authored
  source_event_refs: []
  occurred_at: null
  assessment_required: true
  resulting_assessment_ids: []
  status: open
```

A previous assessment remains historically correct for its timestamp and evidence even when a new event makes reevaluation necessary.

## 8. Revision history

Never overwrite assessment history in place.

```yaml
building_assessment_revision_edge:
  prior_assessment_id: null
  later_assessment_id: null
  relation: supersedes|narrows|expands_scope|confirms|changes_recommendation
  reason_refs: []
```

This supports mysteries where two notices appear inconsistent but apply to different times or scopes.

## 9. Partial reopening

A structure can contain mixed states.

Example:

```text
community hall
  exterior plaza -> use allowed
  east entrance -> use allowed
  ground-floor service desk -> use allowed with limitations
  upstairs archive -> restricted
  rear workshop -> awaiting assessment
```

The generator should prefer explicit scoped states over a single `building_open` flag.

## 10. Repair and reentry handoff

Facility Maintenance may emit:
- repair work completed;
- temporary support installed;
- fault verification complete;
- unresolved work remains.

Those events can trigger reevaluation here.

They do not automatically create occupancy authorization.

Likewise, authorization here does not mark maintenance complete.

Core invariant:

`REPAIR_COMPLETE != REENTRY_AUTHORIZED != SERVICE_OPERATIONAL`.

All three may happen at different times.

## 11. Residential handoff

Residential continuity owns household return.

A residence may receive a use authorization for its structure while household return remains delayed because:
- route access is unavailable;
- utilities remain unavailable;
- accessibility needs are unmet;
- care constraints remain active;
- the household chooses or is authorized to relocate instead.

This extension supplies only the relevant building-use decision.

## 12. Service-owner handoff

A clinic, school, shop, lodging venue, workplace or public office may be physically usable while its own service remains closed for staffing, supply, equipment or administrative reasons.

The building layer emits a scoped authorization or restriction. The service owner decides its operational state.

## 13. Hazard-specific handoff

Hazard owners remain authoritative for the initiating condition.

Examples:
- Seismic records shaking and aftershocks;
- Wildfire records fire and smoke incident state;
- Slope Instability records slope failure/rockfall;
- Stormwater/Flood systems record water impacts;
- Volcanic systems record ash or eruption evidence.

This layer records what was observed in the structure and what use decision followed. It does not re-evaluate the hazard itself.

## 14. Monitoring gaps

```yaml
building_evidence_gap:
  gap_id: null
  structure_id: null
  scope_ids: []
  gap_type: inaccessible_area|instrument_unavailable|record_missing|observer_limit|time_gap|authored
  start_time: null
  end_time: null
  consequence_note: null
```

Unknown remains unknown.

An inaccessible room cannot be promoted to safe because the adjacent hallway looked normal.

## 15. Public notices and knowledge

```yaml
building_use_notice:
  notice_id: null
  structure_id: null
  scope_ids: []
  source_authority_ref: null
  publication_time: null
  effective_time: null
  summary_claim_ids: []
  underlying_restriction_or_authorization_ids: []
  correction_ids: []
  superseded_by_id: null
```

Public notice state and governing state can diverge temporarily because publication may lag a decision.

A stale sign in Minecraft must remain presentation until reconciled with authoritative state.

## 16. Historical identity and adaptive reuse

Structure identity persists through:
- temporary closure;
- partial reopening;
- repair;
- restoration;
- vacancy;
- changed service;
- adaptive reuse;
- preservation as ruins;
- decommissioning when canon explicitly records it.

History can support later callbacks, archives, local memory and ecological occupation.

## 17. Pokémon presence and building condition

A Pokémon can be observed:
- nesting in a damaged roof;
- using a vacant room;
- returning after reopening;
- avoiding one area;
- accompanying an assessor or worker when canon establishes that relationship.

Do not infer from species, Type or flavor:
- structural sensing;
- collapse prediction;
- inspection qualification;
- lifting capacity;
- safe demolition capability;
- electrical/plumbing expertise;
- immunity to falling objects or environmental danger.

Exact mechanics require a governing PTU/Caelo rule and current engine support.

## 18. Noncombat mystery pattern — Four Notices, One Building

A familiar public building has four archived notices that appear contradictory.

Resolution path:
1. identify each notice's publication and effective time;
2. identify spatial scope;
3. link each notice to its underlying assessment;
4. identify a subsequent event or repair completion;
5. reconstruct the revision chain;
6. determine the latest valid state per scope.

No deception is required. The contradiction can arise from different scopes, timing or superseded evidence.

This can run now using provenance/world-state logic.

## 19. Exploration pattern — The Closed Floor Above the Market

A market occupies the ground floor of a reused civic structure. An upper floor remains restricted after an old event. New work exposes an archive reference suggesting the restriction once covered a different geometry than the modern floor plan.

Playable content:
- compare old and current plans;
- locate former stair/door alignments;
- inspect public notices;
- interview recurring occupants;
- reconcile building IDs after renovation;
- establish what area was actually reviewed;
- hand unresolved physical questions to an authored assessor.

Reduced implementation uses only stable, explicitly approved areas. Restricted or uncertain spaces remain outside traversal/combat until world state authorizes them.

## 20. Encounter A — Assessment Team Withdrawal

Narrative premise:
An assessment team is already leaving a reviewed exterior zone when a hostile or panicked Pokémon encounter threatens the exit route.

Full intended version may involve:
- explicit withdrawal/protection objective;
- Intercept around the exit corridor;
- forced movement;
- changing restricted cells after a subsequent event;
- reaction windows;
- objective-aware AI;
- semantic playback of team withdrawal.

Permanent capability dependencies:
- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL if withdrawal windows matter;
- full stateful damage pipeline — PARTIAL for ordinary governed combat effects;
- status lifecycle — PARTIAL where selected legal effects use status;
- terrain/weather/hazards/zones/reactions — BLOCKING if restricted cells change or generalized reactions matter;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for PROTECT/WITHDRAW behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic withdrawal/restriction playback.

Reduced version:
Ouros completes staff withdrawal before BattleSpec creation. All unstable/restricted scopes, assessment equipment and noncombatants remain outside the tactical arena. AutoPTU receives a static exterior space with explicit combatants. Victory can record `IMMEDIATE_ASSESSMENT_ACCESS_SECURED`; it cannot authorize entry or complete an assessment.

## 21. Encounter B — Partial Reopening Perimeter

Narrative premise:
One part of a civic structure has reopened while another remains restricted. An encounter threatens the public boundary between those scopes.

Full intended version may involve protected boundary cells, civilians moving away from the line, Intercept, generalized reactions and AI that understands keeping actors out of the restricted scope.

Dependencies become BLOCKING if the boundary itself changes tactically or if crossing it must trigger reactions/hazards.

Reduced version:
Close the public-facing area temporarily in world state, remove civilians and keep the restricted scope physically outside the BattleSpec. Resolve a conventional static battle in the already-authorized perimeter. Reopening afterward still requires the owning service and building-use state to approve it.

## 22. Encounter C — Reinspection After a Secondary Event

Narrative premise:
A structure previously reviewed experiences a new authored event. The task is to regain safe access for a later reassessment.

Full intended version could use falling debris, unstable cells, delayed changes, environmental damage/status, forced movement and reactions.

These mechanics depend directly on:
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- full turn/round lifecycle — PARTIAL for delayed phases;
- full stateful damage pipeline — PARTIAL if a governed environmental damage source exists;
- status lifecycle — PARTIAL if an exact governed status effect exists;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI tactical policy — BLOCKING if evacuation/protection objectives remain active;
- adapter/playback — BLOCKING for authoritative environmental changes.

Reduced version:
The secondary event ends before tactical resolution. The new uncertain scopes remain inaccessible. A static encounter occurs only on reviewed stable ground. Afterward, the building remains `REEVALUATION_REQUIRED` until the appropriate world-state process completes.

## 23. Minecraft/Cobblemon representation

Safe presentation candidates:
- barriers and closed doors;
- partial-use signs;
- scaffolding and repair overlays from Maintenance;
- visibly damaged or restored structure variants;
- alternate entrances;
- public notices with issue dates;
- assessor/worker NPC schedules;
- individual Pokémon observed in or near the site;
- exterior zones reopened before interiors;
- persistent ruins or adaptive-reuse variants.

Minecraft is presentation only.

Block damage does not create a structural diagnosis. A repaired block model does not authorize reentry. A sign does not become governing truth merely because it exists in-world. Falling blocks do not execute PTU damage. Native collision/knockback does not implement forced movement. Cobblemon BattleState remains outside combatant selection, legality, HP/status, tactical positions and outcomes.

## 24. PTU/Caelo unknowns

Remain UNKNOWN without exact governing evidence:
- universal collapse checks;
- falling-debris damage;
- structural HP;
- unstable-floor rules;
- rubble difficult terrain;
- crushing;
- rescue/carry actions;
- building-entry Skill DCs;
- demolition rules;
- aftershock tactical timing;
- smoke/flood/fire effects inside structures beyond exact sourced mechanics;
- species-derived collapse prediction;
- Type-derived structural immunity;
- Moves used as universal repair/demolition tools;
- Trainer Features granting generic inspection authority.

## 25. Canon promotion questions

Before any proposed building-safety content becomes canon, confirm:
- the structure and its historical identity;
- the institution or actor with authority to assess;
- whether technical advice and authorization are separate locally;
- exact scopes covered by each decision;
- what triggered review or reevaluation;
- how notices are published;
- relationships to owner systems such as Residential, Care, Workplace or Civic Governance;
- any Pokémon role through explicit canon rather than Type inference;
- any tactical environmental effect through exact PTU/Caelo evidence and engine contracts.

Until those questions are answered, the layer remains a proposed continuity framework rather than Ouros law or engineering canon.