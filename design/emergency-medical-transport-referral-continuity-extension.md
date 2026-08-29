# Ouros Emergency Medical Transport & Referral Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Research basis: `research/2026-08-29-emergency-medical-transport-referral-continuity-scan-118.md`

## Purpose

This extension preserves the operational chain between a request for medical transport and a completed receiving handoff. It supports urgent response, planned patient movement, referral/retrieval between care sites, diversions, temporary pickup points and transport-service recovery.

It does not diagnose, heal, assign clinical priority rules, define ambulance law, invent medical qualifications or replace generic travel infrastructure.

## Authority boundaries

Care owns:

- subject health and care-case state;
- observations, diagnosis and treatment;
- facility services and receiving-care state;
- legal PTU/AutoPTU healing writeback.

Crisis owns:

- emergency incident state;
- rescue/extraction needs;
- shelters and response staging;
- crisis-wide prioritization when authored.

Travel and modal infrastructure own:

- route topology;
- road/rail/water/air availability;
- ordinary journey feasibility;
- transport-sector disruptions.

Communications owns message transmission and receipt.

Accessibility owns actor-specific access requirements.

This extension owns only medical-transport request, assignment, pickup, movement-context linkage, diversion, receiving handoff and transport-unit turnaround.

## Core non-equivalences

Keep these operational facts separate:

`REQUEST_RECEIVED != RESPONSE_ACCEPTED`

`RESPONSE_ACCEPTED != UNIT_ASSIGNED`

`UNIT_ASSIGNED != UNIT_DEPARTED`

`UNIT_AT_SCENE != SUBJECT_REACHED`

`SUBJECT_REACHED != TRANSPORT_REQUIRED`

`TRANSPORT_ACCEPTED != SUBJECT_BOARDED`

`SUBJECT_BOARDED != TRANSPORT_DEPARTED`

`DESTINATION_SELECTED != DESTINATION_ACCEPTED`

`DESTINATION_ACCEPTED != DESTINATION_STILL_AVAILABLE`

`ARRIVED_AT_DESTINATION != CARE_HANDOFF_ACCEPTED`

`CARE_HANDOFF_ACCEPTED != TREATMENT_COMPLETE`

`PATIENT_TRANSFER_COMPLETE != UNIT_READY_FOR_NEW_ASSIGNMENT`

These distinctions generate useful chronology without importing clinical rules.

## 1. Medical transport service

```yaml
medical_transport_service:
  medical_transport_service_id: null
  operator_institution_id: null
  service_area_ids: []
  service_modes: []
  station_or_base_ids: []
  dispatch_node_ids: []
  care_facility_links: []
  vehicle_or_transport_asset_ids: []
  crew_role_ids: []
  supporting_pokemon_ids: []
  current_service_state: unknown
  dependency_ids: []
  public_information_ids: []
  canon_basis_ids: []
  canon_status: proposed
```

Candidate descriptive modes may include ROAD, WATER, AIR, RAIL_OR_GUIDED, POKEMON_ASSISTED or OTHER_AUTHORED_MODE only when regional canon supports them.

A service mode does not imply mechanical capability.

## 2. Transport request

```yaml
medical_transport_request:
  request_id: null
  requested_at: null
  requester_actor_or_institution_id: null
  subject_ids: []
  origin_location_id: null
  request_channel_ref: null
  reported_need_summary: null
  reported_urgency_claim: null
  source_observation_ids: []
  care_case_refs: []
  crisis_refs: []
  accessibility_requirement_refs: []
  status: RECEIVED
  provenance_ids: []
```

Suggested request states:

- RECEIVED
- UNDER_REVIEW
- ACCEPTED
- REFERRED_TO_OTHER_SERVICE
- DUPLICATE
- CANCELLED
- CLOSED_WITHOUT_TRANSPORT
- UNKNOWN

`reported_need_summary` remains a report. It does not create diagnosis, Injury, status or tactical state.

## 3. Dispatch assignment

```yaml
medical_dispatch_assignment:
  assignment_id: null
  request_id: null
  service_id: null
  accepted_at: null
  assigned_unit_id: null
  assigned_crew_ids: []
  assigned_supporting_pokemon_ids: []
  origin_base_id: null
  destination_scene_id: null
  route_or_journey_ref: null
  current_state: ASSIGNED
  reassignment_history_ids: []
  cancellation_reason_ref: null
```

Candidate states:

- ASSIGNED
- PREPARING
- DEPARTED
- EN_ROUTE
- ARRIVED_SCENE
- CANCELLED
- REASSIGNED
- UNABLE_TO_COMPLETE

Assignment does not prove movement. A unit can be assigned while still preparing or waiting on a route/access dependency.

## 4. Medical transport unit

```yaml
medical_transport_unit:
  unit_id: null
  service_id: null
  asset_ref: null
  home_base_id: null
  current_location_id: null
  operational_state: unknown
  crew_assignment_ids: []
  supporting_pokemon_ids: []
  current_mission_id: null
  maintenance_ref: null
  supply_readiness_refs: []
  communications_ref: null
  accessibility_capability_refs: []
  last_readiness_verification_id: null
```

Candidate operational states:

- AVAILABLE
- ASSIGNED
- EN_ROUTE
- AT_SCENE
- TRANSPORTING
- AT_DESTINATION
- HANDOFF_PENDING
- TURNAROUND
- MAINTENANCE
- OUT_OF_SERVICE
- UNKNOWN

No state grants healing or driving mechanics.

## 5. Scene access and subject contact

A unit reaching the scene location does not guarantee access to the subject.

```yaml
medical_scene_access:
  scene_access_id: null
  assignment_id: null
  scene_location_id: null
  unit_arrived_at: null
  access_route_ids: []
  access_constraint_ids: []
  rescue_handoff_refs: []
  accessibility_refs: []
  subject_contact_at: null
  contact_state: NOT_REACHED
  evidence_ids: []
```

Candidate contact states:

- NOT_REACHED
- ACCESS_PENDING
- REACHED
- SUBJECT_MOVED_BEFORE_CONTACT
- HANDED_OVER_FROM_RESCUE
- UNKNOWN

Crisis/Rescue owns extraction from an active hazard. This layer may receive the extracted subject afterward.

## 6. Transport decision record

This record preserves an authored/authoritative decision without pretending to perform clinical reasoning.

```yaml
transport_decision_record:
  decision_id: null
  subject_id: null
  care_case_ref: null
  made_at: null
  deciding_authority_ref: null
  decision: UNKNOWN
  destination_request_ids: []
  accessibility_requirements: []
  transport_support_requirement_refs: []
  evidence_refs: []
```

Candidate descriptive decisions:

- TRANSPORT_REQUESTED
- NO_TRANSPORT_CURRENTLY_REQUIRED
- ALTERNATE_CARE_PATH
- INTERFACILITY_TRANSFER_REQUESTED
- DECISION_PENDING
- UNKNOWN

No generator rule may invent the clinical basis.

## 7. Destination request and acceptance

```yaml
medical_destination_request:
  destination_request_id: null
  subject_id: null
  origin_facility_or_scene_id: null
  requested_destination_facility_id: null
  requested_service_ref: null
  request_time: null
  receiving_response: PENDING
  response_time: null
  response_basis_ref: null
  superseded_by_id: null
  provenance_ids: []
```

Candidate receiving responses:

- PENDING
- ACCEPTED
- DECLINED
- DIVERTED
- CONDITIONAL
- CANCELLED
- UNKNOWN

Care owns whether the receiving service actually exists and can accept the relevant care case.

## 8. Patient transport mission

```yaml
medical_transport_mission:
  mission_id: null
  request_id: null
  assignment_id: null
  subject_ids: []
  unit_id: null
  crew_ids: []
  origin_location_id: null
  selected_destination_id: null
  destination_acceptance_ref: null
  journey_ref: null
  boarding_event_ids: []
  departure_event_id: null
  diversion_ids: []
  arrival_event_id: null
  care_handoff_id: null
  status: PREPARING
  world_state_dependency_ids: []
```

Candidate states:

- PREPARING
- BOARDING
- READY_TO_DEPART
- IN_TRANSIT
- DIVERTING
- ARRIVED
- HANDOFF_PENDING
- TRANSFERRED
- TERMINATED_WITHOUT_TRANSFER

Travel owns the journey. The mission points to it instead of reproducing route calculations.

## 9. Boarding and movement assistance

Boarding may matter narratively because access, consent, rescue handoff or equipment state matters.

```yaml
medical_boarding_event:
  boarding_event_id: null
  mission_id: null
  subject_id: null
  location_id: null
  started_at: null
  completed_at: null
  assistance_refs: []
  accessibility_refs: []
  rescue_handoff_ref: null
  mechanical_carry_rule_refs: []
  state: PENDING
```

Candidate states:

- PENDING
- IN_PROGRESS
- COMPLETE
- INTERRUPTED
- CANCELLED

If physical carrying or movement becomes mechanical, exact PTU/Caelo capability and engine support are required. Narrative completion cannot grant a generic Carry action.

## 10. Diversion

```yaml
medical_transport_diversion:
  diversion_id: null
  mission_id: null
  recorded_at: null
  previous_destination_id: null
  new_destination_id: null
  reason_claim_ref: null
  source_system_ref: null
  previous_acceptance_ref: null
  new_acceptance_ref: null
  route_change_ref: null
  public_information_ref: null
```

Potential authored sources include:

- receiving service became unavailable;
- route became unavailable;
- required specialty/service changed through Care authority;
- crisis response changed access;
- transport asset limitation became known;
- explicit institutional coordination decision.

The transport layer does not invent medical deterioration as a diversion reason.

## 11. Arrival and care handoff

```yaml
medical_care_handoff:
  handoff_id: null
  mission_id: null
  subject_ids: []
  receiving_facility_id: null
  vehicle_arrival_at: null
  handoff_started_at: null
  receiving_actor_or_team_id: null
  handoff_completed_at: null
  care_case_ref: null
  transferred_record_refs: []
  unresolved_transport_notes: []
  status: PENDING
```

Candidate states:

- PENDING
- RECEIVING_REVIEW
- ACCEPTED
- REDIRECTED
- INCOMPLETE
- CANCELLED

`ACCEPTED` means the transport responsibility handoff is complete for this model. It says nothing about diagnosis, treatment, admission or discharge.

## 12. Inter-facility referral and retrieval

```yaml
interfacility_transport_request:
  interfacility_request_id: null
  care_case_ref: null
  sending_facility_id: null
  receiving_facility_id: null
  requested_service_ref: null
  sending_ready_state: unknown
  receiving_acceptance_ref: null
  coordinating_service_id: null
  transport_request_ref: null
  current_state: REQUESTED
  chronology_ids: []
```

Candidate states:

- REQUESTED
- RECEIVING_REVIEW
- DESTINATION_ACCEPTED
- TRANSPORT_PENDING
- PICKUP_PENDING
- IN_TRANSIT
- HANDOFF_PENDING
- COMPLETE
- CANCELLED

A referral can be medically valid while transport remains unavailable. Transport can be ready while the sending subject is not yet ready for movement. Preserve both truths.

## 13. Unit turnaround

A mission can be complete while its asset remains unavailable.

```yaml
medical_unit_turnaround:
  turnaround_id: null
  unit_id: null
  previous_mission_id: null
  started_at: null
  required_action_refs: []
  maintenance_refs: []
  resupply_refs: []
  crew_availability_refs: []
  readiness_verification_id: null
  completed_at: null
  status: OPEN
```

Potential authored actions include cleaning, restocking, maintenance, documentation or crew replacement only where local canon establishes them. No universal timing is defined.

## 14. Temporary pickup and transfer points

Crises, route failures or geography may create temporary nodes.

```yaml
temporary_medical_transport_point:
  point_id: null
  location_id: null
  established_by_ids: []
  active_from: null
  active_until: null
  supported_service_ids: []
  access_route_ids: []
  function_tags: []
  successor_location_id: null
  legacy_event_ids: []
```

Possible functions:

- pickup;
- rendezvous;
- transfer between modes;
- dispatch staging;
- inter-facility meeting point;
- crisis-only loading area.

A temporary point can later become a permanent part of local geography if canon approves that history.

## 15. Transport knowledge and public information

Actors may know different parts of current service state.

```yaml
medical_transport_notice:
  notice_id: null
  service_id: null
  issued_at: null
  audience_scope: []
  claim_scope: null
  affected_area_ids: []
  effective_from: null
  review_at: null
  supersedes_id: null
  evidence_refs: []
```

Examples of claims:

- one base temporarily unavailable;
- rural pickup location moved;
- specific route inaccessible;
- one receiving facility not taking a particular referral class, if Care authority supplies that fact;
- planned transfers delayed.

A public notice is information, not world truth by itself.

## 16. Pokémon roles

Pokémon may participate as individually authored actors in transport services.

Possible observable roles:

- accompanies a field crew;
- helps communicate with a known partner;
- assists at a base;
- accompanies a vehicle;
- participates in an authored transport mode;
- helps with a task supported by exact PTU/Caelo capabilities.

Never infer from species or Type alone:

- carrying capacity;
- medical qualification;
- flight transport legality;
- emergency speed;
- ability to stabilize a patient;
- authority to enter restricted scenes;
- willingness to work.

Agency, institutional relationship and mechanical capability remain separate.

## 17. Long-term continuity

Medical transport should accumulate institutional history.

Useful persistent events:

- base opened/closed/relocated;
- temporary pickup point established;
- route repeatedly diverted;
- service mode added or retired;
- major crisis changed referral relationships;
- old vehicle/building became a local landmark;
- recurring crew relationship formed;
- historical handoff dispute later clarified;
- rural community developed a new access arrangement.

This creates story from infrastructure without requiring constant emergencies.

## 18. Encounter contract — Roadside Pickup Withdrawal

Narrative premise:

A medical transport unit reaches a roadside pickup after an earlier incident. The patient is already under care and needs to leave the area while a separate hostile Pokémon subgroup threatens the access lane.

Full intended version:

The protected subject, medical crew and vehicle remain relevant while combatants create or preserve an exit corridor.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL, required for rich interception/forced displacement around the withdrawal route;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL if departure windows or phased withdrawal occur;
- full stateful damage pipeline — PARTIAL for ordinary combat and any validated damage source;
- status lifecycle — PARTIAL if an exact existing status matters;
- terrain/weather/hazards/zones/reactions — BLOCKING for generalized protection/reaction zones or active roadside hazards;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for PROTECT/WITHDRAW/CLEAR_ROUTE priorities;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:

Complete boarding and vehicle departure as world-state transitions before BattleSpec. Keep patient, crew and unit off-grid. AutoPTU resolves a static encounter on the now-cleared access lane against explicit combatants. Victory can secure the pickup point after departure. It cannot heal the subject, complete a later hospital handoff or make the unit available for a new mission.

## 19. Encounter contract — Transfer Bay Perimeter

Narrative premise:

A transport arrives at a receiving facility while a separate disturbance threatens the exterior transfer route.

Full intended version:

The encounter would preserve a protected handoff corridor and potentially permit Intercept/reaction behavior around noncombatants.

Dependencies are the same permanent families as Roadside Pickup Withdrawal, with AI tactical policy BLOCKING for PROTECT and terrain/zones/reactions BLOCKING if the transfer corridor changes during rounds.

Reduced version:

Complete care handoff behind a verified secure boundary before battle. The vehicle, patient and receiving staff disappear from BattleSpec. The fight occurs in an exterior static perimeter. Winning may record `IMMEDIATE_TRANSFER_BAY_PERIMETER_SECURED`. Care and transport state remain independent.

## 20. Encounter contract — Diversion Junction

Narrative premise:

A medical route changes after a downstream closure. The transport unit has already taken the alternate road when the players encounter the cause of the obstruction at a junction.

Full intended version:

A richer scenario could include active convoy movement, protected route choice, moving assets and reaction windows.

Dependencies:

- complete movement — PARTIAL for escort/interception/forced movement;
- full turn/round lifecycle — PARTIAL for timed route windows;
- terrain/weather/hazards/zones/reactions — BLOCKING for changing route cells or generalized reactions;
- AI tactical policy — BLOCKING for ESCAPE/PROTECT/CLEAR_ROUTE;
- adapter/playback — BLOCKING for moving vehicles and semantic route playback;
- ordinary tactical categories retain the permanent VERIFIED/PARTIAL statuses above.

Reduced version:

The medical unit has already diverted off-screen through authoritative world state. The players fight only the explicit hostile subgroup at a static junction after no patient or transport asset remains in tactical danger. Clearing the junction does not retroactively change the transport mission's chosen destination.

## 21. Exploration — The Station That Moved Twice

Current profile: EXECUTABLE AS WORLD EXPLORATION.

A settlement's old care-transfer station appears at three different addresses across maps, photographs and resident testimony. The answer is institutional continuity: the service moved after one road redesign and later retained the old local nickname after a second relocation.

Required state:

- persistent institution/service ID;
- dated location aliases;
- archived maps/photos/notices;
- route history;
- testimony with provenance;
- current station state.

No battle mechanic is required.

## 22. Minecraft/Cobblemon/Craftics boundary

Minecraft/Cobblemon may present:

- stations/bases;
- parked medical vehicles;
- static stretchers or care props;
- loading bays;
- field tents and pickup points;
- route closures and signage;
- staff and individually authored Pokémon;
- lights/sounds/particles/UI;
- arrival/departure animation when driven by authoritative state.

Presentation must never decide:

- clinical urgency;
- diagnosis;
- transport requirement;
- destination acceptance;
- patient custody;
- care handoff completion;
- healing/status change;
- legal carrying;
- emergency priority/right-of-way;
- vehicle collision damage;
- combatant selection.

A moving Minecraft vehicle is playback. It does not execute the mission state machine.

## 23. Canon promotion questions

Before regional medical transport becomes canon, humans must approve:

- which regions have dedicated medical transport services;
- emergency versus planned-transfer distinctions;
- institution names and mandates;
- modes used by geography;
- patient and Pokémon transport norms;
- whether Pokémon Centers receive humans, Pokémon or both in each context;
- inter-facility referral relationships;
- accessibility expectations;
- privacy boundaries for dispatch/transport records;
- historical service changes;
- individually authored Pokémon worker roles;
- any crisis-specific temporary service doctrine.

## Design outcome

This layer lets Ouros tell stories about reaching care without turning transportation into healing or turning Minecraft vehicles into PTU mechanics. It preserves chronology, institutional responsibility, geographic constraints and long-term local memory while leaving rich escort/rescue battles gated behind exact engine capabilities.
