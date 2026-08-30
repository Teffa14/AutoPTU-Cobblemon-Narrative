# Ouros Road Vehicle, Fleet Assignment, Inspection & Serviceability Continuity Extension

Status: PROPOSED systems architecture. Not established Ouros canon.
Date: 2026-08-30

## Purpose

This extension gives persistent road vehicles a neutral operational history between physical object identity, operator/fleet membership, service assignment, inspection/defect state, maintenance, release, substitution and retirement.

It does not create a universal motor-vehicle law, registration regime, private-car economy, driving Skill system or tactical vehicle simulator.

The intended result is simple: when a bus, taxi, service van, expedition vehicle or other canon-approved road asset matters to the world, Ouros can remember which exact vehicle it was and why it was or was not available at a given time.

## Authority boundaries

Travel owns route viability and journey truth.

Roads owns physical road/crossing access, closures and detours.

Road Passenger Transport owns service patterns, stops, runs, dispatch, boarding/alighting and passenger-service history.

Material Culture owns persistent physical-object provenance where a vehicle is represented as an `item_instance` or equivalent authored physical asset.

Shared Equipment owns general temporary entitlement, checkout, custody and return when a road asset is loaned through an existing pool. This extension records vehicle-specific operational consequences.

Facility Maintenance owns facility/workshop condition and general worksite process. Vehicle technical work may reference a maintenance work order but this extension owns the vehicle's serviceability lineage.

Fuel Supply owns fuel availability/distribution if the vehicle technology requires it.

Finance owns purchase, lease payment, insurance, charge and settlement truth.

Workplaces, Credentials and Human Identity own personnel, qualifications and authority.

Pokémon Agency / Work Role owns any individual Pokémon involved in transport work. A Pokémon is never represented as a vehicle asset here.

AutoPTU owns tactical battle resolution only for explicit combatants and verified mechanics. It never decides vehicle ownership, serviceability, inspection outcome, fleet assignment or road-service authority.

## 1. Persistent road vehicle

```yaml
road_vehicle:
  vehicle_ref_id: null
  physical_asset_ref: null
  authored_vehicle_class: null
  current_owner_ref: null
  current_operator_ref: null
  current_custodian_ref: null
  home_location_ref: null
  current_location_ref: null
  current_fleet_ref: null
  current_role_ref: null
  current_serviceability_state: UNKNOWN
  current_assignment_refs: []
  current_restriction_refs: []
  identifier_record_ids: []
  configuration_episode_ids: []
  inspection_event_ids: []
  defect_record_ids: []
  maintenance_episode_ids: []
  release_event_ids: []
  lifecycle_event_ids: []
  provenance_refs: []
```

`vehicle_ref_id` is an internal continuity identifier. It is not automatically visible or meaningful inside the world.

A region may have no registration marks at all. Another may use local fleet numbers. Another may use institution-specific labels. Canon decides.

## 2. Vehicle identifier history

```yaml
vehicle_identifier_record:
  identifier_record_id: null
  vehicle_ref_id: null
  identifier_type: authored
  identifier_value: null
  issuer_or_assigner_ref: null
  valid_from: null
  valid_until: null
  display_locations: []
  supersedes_record_id: null
  provenance_refs: []
```

Possible authored identifier types might include:

- fleet number;
- depot number;
- local registration mark;
- manufacturer/serial reference;
- nickname;
- painted call sign;
- workshop tag.

No identifier type exists globally unless canon says it does.

Core separations:

`SAME_FLEET_NUMBER != SAME_VEHICLE`

`DIFFERENT_IDENTIFIER != DIFFERENT_VEHICLE`

`LIVERY_CHANGED != VEHICLE_REPLACED`

An institution may reuse a fleet number after retirement. Historical records must preserve the time scope needed to disambiguate it.

## 3. Ownership, operation and custody

These relationships must remain distinct.

```yaml
vehicle_relationship_episode:
  relationship_episode_id: null
  vehicle_ref_id: null
  relationship_type: OWNER | OPERATOR | CUSTODIAN | LESSOR | BORROWER | HOST_INSTITUTION | OTHER
  actor_or_institution_ref: null
  valid_from: null
  valid_until: null
  source_refs: []
```

`OWNER != OPERATOR`

`OPERATOR != DRIVER`

`CUSTODIAN != AUTHORIZED_FOR_ALL_USES`

A town can own a vehicle operated by a contractor. A school can borrow a vehicle from another institution. A public service can temporarily use a replacement vehicle without transferring ownership.

## 4. Fleet membership

```yaml
vehicle_fleet:
  fleet_ref: null
  managing_institution_ref: null
  home_location_refs: []
  fleet_purpose: authored
  active_vehicle_refs: []
  spare_vehicle_refs: []
  restricted_vehicle_refs: []
  retired_vehicle_refs: []
  policy_refs: []
  history_event_ids: []
```

```yaml
fleet_membership_episode:
  membership_episode_id: null
  fleet_ref: null
  vehicle_ref_id: null
  role: PRIMARY | SPARE | SUPPORT | TRAINING | TEMPORARY | OTHER
  valid_from: null
  valid_until: null
  source_refs: []
```

A vehicle can leave one fleet and join another without losing its physical history.

A spare is not automatically available. It may be undergoing maintenance, assigned elsewhere, missing a crew or outside the correct location.

## 5. Vehicle role and service assignment

```yaml
vehicle_assignment:
  vehicle_assignment_id: null
  vehicle_ref_id: null
  assignment_type: SERVICE_RUN | RESPONSE_RESOURCE | EXPEDITION | DELIVERY_SUPPORT | WORK_CREW | EVENT_SUPPORT | OTHER
  owning_system_ref: null
  owning_assignment_ref: null
  planned_from: null
  planned_until: null
  actual_start: null
  actual_end: null
  state: PLANNED
  dependency_refs: []
  substitution_event_id: null
  provenance_refs: []
```

Suggested states:

- PLANNED
- RESERVED_FOR_ASSIGNMENT
- READY
- ACTIVE
- PAUSED
- WITHDRAWN
- COMPLETED
- CANCELLED
- REPLACED

The owning system decides what the assignment means.

For a bus run, Road Passenger Transport owns the run.

For a response vehicle, Dispatch/Response owns the mission.

For an expedition vehicle, Travel/Expedition owns the journey/expedition.

This layer owns which exact physical vehicle was assigned and when.

`VEHICLE_ASSIGNED != VEHICLE_OPERATING_NOW`

`ASSIGNMENT_COMPLETE != VEHICLE_AVAILABLE_FOR_NEXT_ASSIGNMENT`

## 6. Configuration and upgrade history

```yaml
vehicle_configuration_episode:
  configuration_episode_id: null
  vehicle_ref_id: null
  configuration_label: authored
  capability_claim_refs: []
  installed_component_refs: []
  removed_component_refs: []
  active_from: null
  active_until: null
  source_event_ref: null
  verification_refs: []
```

This is narrative continuity, not a universal upgrade tree.

A configuration change can affect route or service eligibility only if an owning system has an explicit verified requirement.

`UPGRADE_RECORDED != MECHANIC_IMPLEMENTED`

`VISIBLE_ATTACHMENT != VERIFIED_CAPABILITY`

## 7. Condition observation

```yaml
vehicle_condition_observation:
  observation_id: null
  vehicle_ref_id: null
  observer_ref: null
  observed_at: null
  location_ref: null
  observed_condition_claims: []
  evidence_refs: []
  immediate_restriction_recommended: null
  confidence: null
```

An observation remains evidence rather than diagnosis.

Examples:

- unusual vibration reported;
- damaged door observed;
- warning indicator visible;
- tire visibly damaged;
- exterior panel dented;
- fluid beneath parked vehicle;
- strange sound during service.

The extension must not infer a technical cause unless a qualified/authored process establishes it.

## 8. Defect record

```yaml
vehicle_defect:
  defect_id: null
  vehicle_ref_id: null
  first_reported_at: null
  source_observation_ids: []
  affected_system_or_area: authored
  suspected_cause_refs: []
  confirmed_cause_refs: []
  severity_band: unknown
  service_effect_refs: []
  restriction_refs: []
  assessment_refs: []
  current_state: OPEN
  related_prior_defect_refs: []
```

Suggested states:

- OPEN
- UNDER_ASSESSMENT
- MONITORED
- REPAIR_PLANNED
- UNDER_REPAIR
- VERIFYING
- RESOLVED
- ACCEPTED_DEFERRED
- DISMISSED_NOT_CONFIRMED

`DEFECT_REPORTED != DEFECT_CONFIRMED`

A driver, passenger, mechanic, Pokémon partner or observer can notice a symptom without proving its cause.

## 9. Inspection event

```yaml
vehicle_inspection_event:
  inspection_event_id: null
  vehicle_ref_id: null
  inspection_type: authored
  requested_by_ref: null
  performed_by_refs: []
  authority_basis_ref: null
  started_at: null
  completed_at: null
  evidence_refs: []
  defect_refs_created_or_updated: []
  finding_claim_refs: []
  operational_recommendation: null
  followup_refs: []
  provenance_refs: []
```

No universal annual inspection, licensing authority or inspection interval is established.

`INSPECTION_COMPLETE != VEHICLE_AVAILABLE`

`INSPECTION_PASSED_AT_T1 != SAFE_AT_T2`

An inspection describes evidence and findings at its effective time and scope. A new defect can arise later.

## 10. Serviceability state

```yaml
vehicle_serviceability_state:
  serviceability_record_id: null
  vehicle_ref_id: null
  state: UNKNOWN | AVAILABLE | LIMITED | RESTRICTED | OUT_OF_SERVICE | UNDER_REPAIR | RELEASE_PENDING | RETIRED
  effective_from: null
  effective_until: null
  basis_refs: []
  allowed_use_scope_refs: []
  prohibited_use_scope_refs: []
  decision_owner_ref: null
  supersedes_record_id: null
```

Serviceability is a world-state decision owned by the appropriate canon institution/operator. It is not inferred from Minecraft visuals or combat HP.

`VEHICLE_PRESENT != VEHICLE_AVAILABLE`

`OUT_OF_SERVICE != RETIRED`

`RESTRICTED != UNUSABLE_FOR_EVERY_PURPOSE`

A vehicle may be allowed to move empty to a workshop while prohibited from carrying passengers, if authored authority explicitly permits that scope.

## 11. Maintenance episode

```yaml
vehicle_maintenance_episode:
  maintenance_episode_id: null
  vehicle_ref_id: null
  defect_refs: []
  requested_work_refs: []
  workshop_or_location_ref: null
  coordinating_actor_refs: []
  assigned_worker_refs: []
  work_order_ref: null
  started_at: null
  completed_at: null
  parts_or_material_refs: []
  observed_work_refs: []
  verification_required: null
  verification_event_ref: null
  state: PLANNED
```

Suggested states:

- PLANNED
- WAITING_FOR_ACCESS
- WAITING_FOR_PART
- WAITING_FOR_WORKER
- IN_PROGRESS
- PAUSED
- WORK_COMPLETE
- VERIFYING
- CLOSED

Facility Maintenance can own workshop/facility work-order dependencies. Material Culture can own replacement components. This episode preserves the vehicle-specific lineage.

`WORK_COMPLETE != RETURN_TO_SERVICE_APPROVED`

## 12. Release / return-to-service event

```yaml
vehicle_release_event:
  release_event_id: null
  vehicle_ref_id: null
  reviewed_defect_refs: []
  reviewed_maintenance_refs: []
  reviewer_refs: []
  authority_basis_ref: null
  decision: RELEASED | RELEASED_LIMITED | NOT_RELEASED | MORE_VERIFICATION_REQUIRED
  effective_at: null
  allowed_scope_refs: []
  restriction_refs: []
  provenance_refs: []
```

This explicit event prevents a repair animation or completed work order from silently restoring public operation.

`REPAIR_RECORDED != RETURN_TO_SERVICE_APPROVED`

`RETURN_TO_SERVICE_APPROVED != ASSIGNED_TO_A_RUN`

## 13. Vehicle substitution

```yaml
vehicle_substitution_event:
  substitution_event_id: null
  owning_assignment_ref: null
  original_vehicle_ref: null
  replacement_vehicle_ref: null
  reason_refs: []
  decided_at: null
  effective_at: null
  passenger_or_public_notice_refs: []
  downstream_effect_refs: []
```

Possible authored reasons:

- defect/restriction;
- maintenance delay;
- allocation conflict;
- weather suitability;
- ecology suitability;
- accessibility requirement;
- capacity requirement;
- event deployment;
- previous assignment overrun;
- local infrastructure constraint.

`VEHICLE_SUBSTITUTED != SERVICE_CANCELLED`

`SERVICE_CONTINUED != ORIGINAL_VEHICLE_SERVICEABLE`

A substitute can preserve a run while the original asset remains unavailable.

## 14. Vehicle location versus service location

Store physical location independently from assignment.

A vehicle can be:

- at the depot but unavailable;
- at the workshop but still assigned on a stale run record;
- en route to a different assignment;
- parked at a terminal before the crew arrives;
- physically present after being retired;
- at the correct stop but not part of the public service.

`CORRECT_LOCATION != CORRECT_ASSIGNMENT`

`VISIBLE_AT_STOP != BOARDING_AUTHORIZED`

## 15. Fuel / energy dependency

If canon defines a relevant fuel or energy system, a vehicle can reference it.

```yaml
vehicle_energy_dependency:
  vehicle_ref_id: null
  dependency_type: authored
  supply_or_charge_ref: null
  current_claim_ref: null
  source_refs: []
```

This extension never selects a technology by default.

`FUEL_AVAILABLE != VEHICLE_SERVICEABLE`

`VEHICLE_SERVICEABLE != FUEL_AVAILABLE`

Both may be required for operation but neither substitutes for the other.

## 16. Driver / crew dependency

Personnel remain external.

```yaml
vehicle_crew_requirement_ref:
  vehicle_ref_id: null
  assignment_ref: null
  required_role_refs: []
  qualification_refs: []
  current_staffing_ref: null
```

No Driving Skill or license is invented here.

`VEHICLE_SERVICEABLE != CREW_AVAILABLE`

`CREW_AVAILABLE != VEHICLE_SERVICEABLE`

## 17. Pokémon participation boundary

A Pokémon may work with or around a road vehicle only through individual agency and explicit assignment.

Examples that may exist if canon approves them:

- maintenance assistance;
- loading support;
- traffic guidance;
- rescue extraction;
- propulsion in a specific authored service;
- detection/inspection support;
- passenger transport separate from the vehicle itself.

The following must never be inferred:

- Electric type = vehicle power source;
- Steel type = mechanic;
- Fighting type = towing capability;
- Rotom = universal vehicle computer;
- Revavroom = universal engine;
- species precedent = automatic work role;
- visible animation = consent or qualification.

## 18. Retirement, disposal and repurposing

```yaml
vehicle_lifecycle_event:
  lifecycle_event_id: null
  vehicle_ref_id: null
  event_type: ENTERED_SERVICE | TRANSFERRED | WITHDRAWN_FROM_ROLE | RETIRED | SOLD | DONATED | DISMANTLED | REPURPOSED | PRESERVED | OTHER
  occurred_at: null
  source_refs: []
  successor_asset_ref: null
  new_use_ref: null
```

`RETIRED_FROM_PUBLIC_SERVICE != DESTROYED`

A retired vehicle can continue as a physical object with a new use. Prior fleet numbers, liveries, route cards, modifications and repair traces can remain environmental storytelling.

Repurposing does not restore its former authority as public transport.

## 19. Record propagation and stale information

Different systems can update at different times.

A service run may be changed at 07:05.

The depot board may show the substitute at 07:12.

The passenger notice may update at 07:18.

A mechanic may close the old work order at 07:31.

An archive months later should preserve all four timestamps rather than collapse them into one fictional moment.

`ASSIGNMENT_UPDATED != PUBLIC_NOTICE_UPDATED`

`REPAIR_RECORD_UPDATED != SERVICE_ROSTER_UPDATED`

## 20. Fleet availability summary

```yaml
fleet_availability_snapshot:
  fleet_ref: null
  observed_at: null
  available_vehicle_refs: []
  assigned_vehicle_refs: []
  restricted_vehicle_refs: []
  maintenance_vehicle_refs: []
  location_unknown_refs: []
  spare_claim_refs: []
  source_refs: []
```

A snapshot is historical evidence. Later events do not rewrite it.

This permits narratives where different staff remember “how many buses were available” differently because they were referring to different times or scopes.

## 21. Information and public belief

Observed livery, posted route card, social rumor, depot board and service app are information surfaces.

They can be stale.

A vehicle painted in a former operator's colors can legally/operationally belong to a successor service if canon establishes that history.

A new livery does not prove new ownership.

A current-looking sticker does not prove a current inspection unless the owning system says that representation has such authority.

## 22. Environmental storytelling outputs

Useful persistent traces include:

- old fleet numbers visible beneath fresh paint;
- route-card holders no longer used;
- workshop chalk marks;
- replacement panels in different colors;
- retired buses serving as shelters or club rooms;
- a depot bay associated with a recurring vehicle;
- a substitute asset that becomes locally beloved;
- an old inspection board preserved after policy changes;
- Pokémon routines tied to a maintenance yard or parking site;
- a former public-service vehicle still recognizable years later.

These traces communicate history without making visual props authoritative.

## 23. Mystery patterns

Good mysteries come from chronology and provenance before misconduct.

Useful structures:

- one fleet number reused across two vehicles;
- one vehicle repainted under three operators;
- a defect reported before a formal inspection;
- repair completed before a service roster update;
- a substitute appearing in photographs before a public notice;
- a retired vehicle still seen moving privately;
- a workshop record referring to an old identifier;
- two different inspections with different scopes.

Permitted resolution: `ACCEPTED_AMBIGUITY` when surviving evidence cannot identify which historical vehicle a record refers to.

## 24. Battle boundary

A road vehicle may appear beside a battle without becoming a combat entity.

Default safe approach:

1. Ouros resolves vehicle identity, current serviceability, assignment and world location.
2. Noncombatant passengers, drivers, mechanics and controlled records withdraw when the scene permits.
3. Vehicle state is frozen unless an exact implemented mechanic governs interaction with it.
4. Ouros selects explicit legitimate combatants.
5. AutoPTU receives static reviewed geometry.
6. Tactical results return only narrow physical consequences.
7. Vehicle/service owners resume operational decisions afterward.

Never infer vehicle HP, collision, crushing, boarding, moving-platform coordinates, cover, ejection, chase movement or repair mechanics.

## 25. Encounter template — Depot Exit Perimeter

Narrative premise:

A service vehicle that is otherwise cleared for a scheduled assignment cannot safely leave a depot because an unrelated hostile or territorial encounter occupies the immediate exit area.

Full intended version may include:

- moving vehicle footprint;
- escort of staff;
- Intercept near the exit;
- push/pull/knockback near parked assets;
- changing depot lanes;
- protected work zones;
- objective-aware withdrawal/clear-route policy;
- semantic playback of vehicle departure after release.

Full version depends on:

- targeting/footprints/range/LoS — VERIFIED for static reviewed combatants/geometry;
- base movement legality — VERIFIED for conventional static spaces;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic lanes, protected zones or generalized reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Full status: BLOCKED FOR RICH SEMANTICS.

Reduced version: READY.

Reduced contract:

- the vehicle remains parked and noninteractive;
- driver, mechanics and passengers leave the tactical space first;
- depot assignment/serviceability state freezes;
- Ouros selects combatants;
- AutoPTU receives a static exit-yard map;
- victory may create `IMMEDIATE_DEPOT_EXIT_CLEAR` only;
- Road Passenger Transport or another owning service decides whether the vehicle subsequently departs.

`TACTICAL_VICTORY != VEHICLE_RELEASED`

`TACTICAL_VICTORY != RUN_STARTED`

## 26. Encounter template — Roadside Inspection Withdrawal

Narrative premise:

An inspection or condition check is already underway when an independent tactical threat makes the roadside work area unsafe.

Full intended version may use staff escort, passing-hazard zones, Intercept, forced movement and objective-aware withdrawal.

Full status: BLOCKED FOR RICH SEMANTICS under the same partial/blocking families.

Reduced version: READY.

Reduced contract:

- traffic/service is already stopped outside BattleSpec;
- inspector, driver, records and tools withdraw;
- the vehicle remains static background geometry with no combat HP;
- tactical victory creates `IMMEDIATE_ROADSIDE_WORK_AREA_CLEAR` only;
- inspection resumes afterward from preserved evidence and chronology.

`TACTICAL_VICTORY != INSPECTION_PASSED`

`TACTICAL_VICTORY != DEFECT_CONFIRMED`

## 27. Encounter template — Substitute Vehicle Loading Bay Chokepoint

Narrative premise:

A replacement vehicle has been selected after the original became unavailable, but an unrelated encounter blocks the loading bay or approach.

Full intended version may want coordinated passenger withdrawal, shifting loading zones, vehicle motion and protect/clear-route AI.

Full status: BLOCKED FOR RICH SEMANTICS.

Reduced version: READY.

Reduced contract:

- passengers remain outside BattleSpec;
- both original and substitute vehicle states freeze;
- no boarding occurs during battle;
- AutoPTU resolves combat on static reviewed geometry;
- victory creates `IMMEDIATE_LOADING_BAY_CLEAR` only;
- the transport owner separately resumes boarding or reassigns the run.

`LOADING_BAY_CLEAR != BOARDING_AUTHORIZED`

`SUBSTITUTE_PRESENT != SUBSTITUTE_ASSIGNED`

## 28. Canon gates

Remain explicitly unresolved until authored:

- whether private automobiles are common anywhere in Ouros;
- whether vehicle registration exists;
- whether any VIN-like identifier exists;
- whether fleet numbers are public or internal;
- inspection institutions and intervals;
- roadworthiness standards;
- driver licensing/qualification;
- vehicle technologies and energy sources;
- public versus private ownership patterns;
- rental/lease systems;
- accessibility requirements;
- maintenance institutions;
- recall/safety-notice procedures;
- retirement/disposal practices;
- specific recurring vehicles, fleets, depots or operators.

## 29. PTU/Caelo mechanic gates

UNKNOWN unless exact source/tests establish otherwise:

- vehicle HP/Armor/DR;
- tactical vehicle movement;
- acceleration/braking/turn radius;
- collision or impact damage;
- moving platforms;
- passenger/rider space sharing;
- boarding/disembarking during initiative;
- cover from a vehicle;
- vehicle knockback/forced movement;
- chase rules;
- ejection/crash transitions;
- generic repair/inspection checks;
- Technology Education as universal vehicle authority;
- Trainer Features as licensing authority;
- species/Type/Move/Ability derived vehicle competence.

## 30. Minecraft/Cobblemon presentation boundary

Minecraft/Cobblemon/Craftics may present, once Ouros has decided the world truth:

- parked or moving-looking vehicle builds/entities;
- depot bays;
- livery variants;
- route cards;
- workshop props;
- barriers;
- replacement panels;
- NPC schedules;
- recurring Pokémon near depots;
- retired/repurposed vehicles.

Presentation must not decide serviceability, ownership, operator, assignment, inspection result, defect cause, roadworthiness, departure or battle legality.

A minecart/cart/vehicle entity moving does not establish an operational run.

A damaged-looking model does not create a mechanical defect.

A despawn does not prove departure, retirement or destruction.

Cobblemon BattleState remains non-authoritative for combatant selection and world facts.