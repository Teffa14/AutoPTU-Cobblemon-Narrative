# Ouros Lodging, Hospitality & Accommodation Layer

Status: proposed systems design. Not established canon.
Pass: 138

## Purpose

Ouros already models travel, food venues, settlements, architecture, accessibility, payments, emergency shelters, public events, care facilities and temporary population. What it lacks is a persistent owner for overnight accommodation itself.

This layer models hotels, inns, hostels, lodges, dormitories, research quarters, bunkhouses, cabins, camps, Pokémon Center lodging if canon permits it, emergency guest accommodation and similar spaces.

It is deliberately narrower than a hotel-management simulator. It exists so the world can remember who requested accommodation, what capacity was actually available, which room or sleeping space was assigned, whether it was ready, what changed during the stay and what historical record remains afterward.

## 1. Authority boundary

Lodging owns:

- accommodation properties;
- rooms/bunks/cabins/campsites as persistent units;
- reservation and waitlist state;
- allocation of sleeping capacity;
- room readiness for occupancy;
- check-in/check-out/no-show/cancellation history;
- guest-stay records;
- property-specific house rules;
- ordinary guest-service incidents;
- temporary conversion of sleeping capacity when another authority requests it.

It does not own:

- building geometry or structural condition — Architecture;
- travel routes — Travel;
- residence/demography — Demography/Homes;
- payment settlement — Currency/Payments;
- food service — Food / Food Safety;
- emergency incident command — Crisis / Emergency Services;
- medical treatment — Care;
- credentials or legal identity — Identity/Credentials;
- accessibility requirements as a general system — Accessibility;
- Pokémon ownership/custody/consent — Pokémon Agency;
- public-event schedules — Public Events/Festivals/Battle Institutions;
- labor scheduling — Workplaces;
- crime/investigation — Cases.

## 2. Core separation

Never collapse these states:

```text
accommodation request
reservation status
room assignment
room readiness
guest arrival
physical occupancy
stay status
departure
room turnaround
historical record
```

A confirmed reservation can exist without a room assignment.

A room assignment can exist while the room is not ready.

A guest can arrive before occupancy begins.

A room can be occupied without establishing residence.

A completed stay remains historical state after the room becomes available again.

## 3. Lodging property

```yaml
lodging_property:
  property_id: null
  name_ref: null
  property_type: null
  location_id: null
  building_or_site_ids: []
  operator_institution_id: null
  operator_actor_ids: []
  room_unit_ids: []
  common_space_ids: []
  food_venue_ids: []
  care_or_service_links: []
  public_access_state: OPEN
  accommodation_policy_revision_id: null
  guest_capacity_summary: null
  current_operational_constraints: []
  event_history_ids: []
```

Candidate property types:

- HOTEL
- INN
- HOSTEL
- LODGE
- RESORT
- GUESTHOUSE
- DORMITORY
- RESEARCH_QUARTERS
- WORKER_BUNKHOUSE
- TRAVELER_SHELTER
- CABIN_COMPLEX
- CAMPSITE
- EMERGENCY_ACCOMMODATION_SITE
- INSTITUTIONAL_GUEST_ROOMS
- POKEMON_CENTER_LODGING if later validated by project canon

Property type is narrative/institutional metadata. It grants no mechanical benefit.

## 4. Persistent room or accommodation unit

```yaml
accommodation_unit:
  unit_id: null
  property_id: null
  unit_type: null
  physical_space_ref: null
  capacity_profile_id: null
  accessibility_profile_id: null
  pokemon_accommodation_profile_id: null
  current_room_condition_ref: null
  readiness_state: READY
  occupancy_state: VACANT
  maintenance_hold_ids: []
  current_assignment_ids: []
  revision_history_ids: []
  stay_history_ids: []
```

Possible `unit_type` values include:

- PRIVATE_ROOM
- SHARED_ROOM
- BUNK
- SUITE
- CABIN
- COTTAGE
- DORM_ROOM
- FIELD_HUT
- TENT_PITCH
- CARAVAN_SPACE
- EMERGENCY_COT
- INSTITUTIONAL_QUARTERS

A unit remains the same `unit_id` across repainting, furniture replacement, accessibility retrofit or ordinary repair.

If Architecture removes or merges the physical space, Lodging closes or supersedes the accommodation unit while preserving its history.

## 5. Capacity profile

```yaml
capacity_profile:
  profile_id: null
  unit_id: null
  human_sleeping_capacity_band: null
  pokemon_presence_constraints: []
  companion_space_refs: []
  linked_accessible_features: []
  version_valid_from: null
  version_valid_to: null
  provenance_refs: []
```

Do not derive capacity by counting Minecraft beds.

Do not derive Pokémon accommodation from species alone.

A property may need individual facts such as body size, movement mode, aquatic access, structural load, quiet-space needs or other validated practical constraints. Narrative generation may flag that an accommodation question exists, but must not invent PTU carrying, size or environmental mechanics.

## 6. Reservation

```yaml
lodging_reservation:
  reservation_id: null
  property_id: null
  requester_actor_id: null
  guest_actor_ids: []
  pokemon_companion_ids: []
  requested_arrival_window: null
  requested_departure_window: null
  requested_unit_profile: null
  accessibility_request_refs: []
  pokemon_accommodation_request_refs: []
  source_context_id: null
  status: REQUESTED
  confirmed_at: null
  assigned_unit_ids: []
  payment_obligation_ref: null
  cancellation_ref: null
  notes_visibility_policy: PRIVATE_OPERATIONAL
  revision_history_ids: []
```

Suggested reservation states:

- REQUESTED
- WAITLISTED
- OFFERED
- CONFIRMED
- CANCELLED
- DECLINED
- NO_SHOW
- ARRIVED
- CHECKED_IN
- CHECKED_OUT
- CLOSED

These states do not imply payment state. Currency/Payments owns authorization and settlement.

## 7. Waitlist and availability

```yaml
lodging_waitlist_entry:
  waitlist_id: null
  reservation_id: null
  requested_profile: null
  entered_at: null
  priority_basis_ref: null
  current_state: WAITING
  offer_history_ids: []
```

Priority must come from explicit property policy, event allocation, accessibility need, emergency mandate or another authored rule. The generator must not invent hidden VIP priority.

“Fully booked” means allocatable inventory for the relevant request is exhausted or held under explicit policy. It must not be fabricated to force travel.

## 8. Room assignment versus readiness

```yaml
room_assignment:
  assignment_id: null
  reservation_id: null
  unit_id: null
  assigned_at: null
  assignment_reason: null
  readiness_checked_at: null
  readiness_state_at_assignment: null
  supersedes_assignment_id: null
  ended_at: null
```

Possible readiness states:

- READY
- CLEANING_REQUIRED
- INSPECTION_PENDING
- MAINTENANCE_HOLD
- ACCESSIBILITY_SETUP_PENDING
- POKEMON_ACCOMMODATION_SETUP_PENDING
- OCCUPIED_PENDING_DEPARTURE
- EMERGENCY_HOLD
- OUT_OF_SERVICE

Readiness is operational. It does not imply health/safety certification beyond what an appropriate system has actually established.

## 9. Stay record

```yaml
lodging_stay:
  stay_id: null
  reservation_id: null
  property_id: null
  guest_actor_ids: []
  pokemon_companion_ids: []
  occupied_unit_ids: []
  arrived_at: null
  checked_in_at: null
  departed_at: null
  checked_out_at: null
  room_change_ids: []
  service_event_ids: []
  incident_ids: []
  privacy_state: PRIVATE
  public_presence_claim_ids: []
```

A stay proves presence only to the scope supported by the record.

It does not prove:

- friendship;
- romance;
- shared plans;
- political alignment;
- conspiracy;
- residence;
- ownership;
- why the guest traveled.

## 10. Room sharing

Shared lodging requires explicit membership in the reservation or later authorized assignment.

```yaml
shared_accommodation_group:
  group_id: null
  reservation_id: null
  participant_actor_ids: []
  unit_ids: []
  sharing_basis: null
  privacy_partition_refs: []
  started_at: null
  ended_at: null
```

`sharing_basis` can be party booking, tournament allocation, dormitory assignment, expedition quarters, emergency shelter allocation or another explicit operational reason.

Never infer private relationships from co-occupancy.

## 11. Pokémon companion accommodation

```yaml
pokemon_accommodation_record:
  accommodation_record_id: null
  pokemon_entity_id: null
  property_id: null
  unit_or_space_id: null
  requested_by_actor_id: null
  agency_or_custody_ref: null
  facility_constraint_refs: []
  observed_preferences_or_refusals: []
  accommodation_state: PENDING
  start_at: null
  end_at: null
```

Possible states:

- PENDING
- ACCEPTED
- ALTERNATIVE_SPACE_REQUIRED
- DECLINED_BY_PROPERTY
- DECLINED_OR_WITHDRAWN_BY_HANDLER_OR_POKEMON
- ACTIVE
- ENDED

A Pokémon is not hotel inventory.

The venue does not gain command authority.

If a Pokémon remains at the property after the associated guest leaves, custody and consent must be resolved separately through Pokémon Agency.

## 12. Property-specific house rules

```yaml
accommodation_policy_revision:
  policy_revision_id: null
  property_id: null
  valid_from: null
  valid_to: null
  quiet_hours: null
  battle_policy: null
  common_space_policy: null
  pokemon_presence_policy_refs: []
  visitor_policy: null
  check_in_window: null
  check_out_window: null
  emergency_exception_refs: []
  publication_ref: null
```

House rules are property policy.

They do not automatically create regional law, criminal status, combat penalties or Trainer Feature restrictions.

## 13. Housekeeping and turnaround

The system needs only coarse operational state.

```yaml
room_turnaround:
  turnaround_id: null
  unit_id: null
  prior_stay_id: null
  started_at: null
  housekeeping_state: PENDING
  maintenance_findings: []
  lost_property_case_refs: []
  completed_at: null
  resulting_readiness_state: null
```

Do not generate repetitive housekeeping quests.

Create content only when turnaround intersects:

- a meaningful missing object;
- safety/maintenance failure;
- unusual Pokémon presence;
- provenance-sensitive material;
- a guest still unaccounted for;
- a public event capacity crunch;
- a player-owned business decision;
- an accessibility problem;
- an active Case.

## 14. Lost property

A found item in a room is not automatically stolen property.

```yaml
lodging_lost_property_record:
  record_id: null
  property_id: null
  unit_id: null
  item_instance_id: null
  found_at: null
  finder_actor_id: null
  candidate_owner_claim_ids: []
  custody_ref: null
  disposition_state: HELD
```

Material Culture owns item identity/provenance. Cases enters only if evidence supports an investigation.

## 15. Event lodging blocks

Major tournaments, festivals, conferences, expeditions and performances may reserve part of lodging capacity.

```yaml
event_lodging_block:
  block_id: null
  event_id: null
  property_id: null
  unit_profile_or_unit_ids: []
  held_from: null
  held_until: null
  release_rule_ref: null
  allocation_policy_ref: null
```

This creates real secondary consequences:

- visitors overflow to nearby towns;
- transport demand shifts;
- local workers face longer commutes;
- campsites open temporarily;
- public lodging fills before commercial lodging or vice versa;
- event staff and competitors compete for distinct pools if policy separates them.

No hidden scarcity should be invented solely to create drama.

## 16. Emergency conversion

A lodging property can temporarily support evacuation or displacement.

Crisis/Emergency Services owns:

- incident declaration;
- evacuation;
- responder command;
- shelter request;
- safety perimeter.

Lodging owns:

- which units can actually be allocated;
- sleeping capacity;
- stay records;
- room turnover;
- operational constraints.

```yaml
emergency_lodging_conversion:
  conversion_id: null
  property_id: null
  incident_id: null
  requested_by_authority_ref: null
  unit_ids_or_capacity_band: null
  activated_at: null
  ended_at: null
  displaced_guest_reallocation_refs: []
```

A hotel becoming emergency accommodation does not make the operator an emergency-response authority.

## 17. Temporary accommodation versus residence

Demography/Homes must receive only explicit handoffs.

A long stay can remain temporary.

A seasonal worker may repeatedly stay in the same bunkhouse without becoming a resident if the world’s residence policy says so.

A researcher may live in quarters for a year while maintaining another home.

Never derive residence from number of nights alone.

## 18. Accessibility

Accessibility owns needs and accommodations as a broader system.

Lodging stores only the operational match:

```yaml
lodging_accessibility_match:
  match_id: null
  reservation_id: null
  request_ref: null
  unit_id: null
  match_state: CONFIRMED
  setup_actions: []
  verified_at: null
```

A nominally accessible room cannot be assumed usable for every person. Match requires the actual requested accommodation dimensions that the project chooses to model.

## 19. Privacy

Guest histories are private by default.

Public knowledge should come from:

- the guest openly stating where they stayed;
- a public event roster that legitimately includes lodging;
- an authored institutional publication;
- direct observation in a public area;
- legally/ethically authorized investigation within whatever canon later establishes.

The generator must never use private stay records to make NPCs omniscient.

## 20. Lodging as persistent social infrastructure

A lodging venue can generate continuity through:

- returning guests;
- staff turnover;
- recurring tournaments;
- seasonal workers;
- research teams;
- emergency conversions;
- renovations;
- changes in transport access;
- neighborhood redevelopment;
- long-term wildlife relationships;
- old guestbooks or photographs where privacy permits;
- rooms that change function over decades.

Most stays should compress.

The world should surface lodging state only when it creates a meaningful choice, consequence, memory or capacity constraint.

## 21. Minecraft projection

Minecraft may render:

- beds;
- bunks;
- doors;
- room numbers;
- front desk boards;
- luggage;
- occupied/available visual indicators;
- accessibility features;
- partner courtyards;
- campsites;
- temporary cots.

Minecraft must not infer from those blocks:

- authoritative occupancy;
- reservation state;
- ownership;
- payment completion;
- guest identity;
- relationship state;
- PTU rest/healing;
- Pokémon consent;
- legal access.

World state projects into Minecraft, never the reverse without a validated interaction event.

## 22. PTU mechanical firewall

Ordinary lodging does not create:

- HP recovery;
- Injury removal;
- Status removal;
- Trainer AP;
- temporary HP;
- Combat Stages;
- Initiative bonuses;
- fatigue removal;
- Sleep status;
- Food Buffs;
- Loyalty;
- Friendship;
- capture bonuses;
- encounter suppression;
- weather protection;
- environmental immunity.

If the project later validates an exact PTU/Caelo rule for rest, a Pokémon Center, an item, a Feature or a specific service, that mechanical rule must be referenced explicitly.

## 23. Encounter contract — Hotel Evacuation During a Utility Failure

Narrative premise:

A lodging property loses a critical utility while heavily occupied during a regional event. The operator starts relocating guests. An independent confrontation blocks one safe route.

FULL version requires:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement/interception for moving guests and protected routes;
- action economy/initiative;
- lifecycle and damage for actual combat;
- terrain/weather/hazards/zones/reactions only if the utility failure has a validated tactical effect;
- AI legal-action infrastructure;
- AI tactical policy for `EVACUATE`, `CLEAR_ROUTE`, `WITHDRAW`, `PROTECT_GUEST`;
- Minecraft/Cobblemon/Craftics playback.

REDUCED version:

Resolve evacuation and room reassignment in world state. Remove guests/staff from the grid. Freeze a safe static arena containing only actual combatants. After battle, resume relocation. Victory does not repair the utility or restore room readiness.

## 24. Encounter contract — Lodge Courtyard Wildlife Disturbance

Narrative premise:

Wild Pokémon repeatedly enter a property courtyard used by guests. Staff initially describe them as a nuisance, but the cause may be food waste, light, migration, construction or another world-state factor.

FULL version requires objective-aware wildlife withdrawal and potentially moving civilians.

REDUCED version:

Move guests inside through world state. Preserve wildlife observations outside battle. If conflict remains, use a static courtyard battle with only participating combatants. Capture/KO does not resolve the underlying attractant automatically.

## 25. Encounter contract — Lost Room Key / Access Dispute

Primarily non-combat.

Identity, room assignment and key/access state are resolved through Lodging + Identity/Credentials.

A battle cannot prove who has a valid reservation.

If an unrelated confrontation occurs, use standard static battle rules.

## 26. Long-term integration hooks

Lodging can hand off to:

- Travel: next departure and route changes;
- Demography: temporary population pressure;
- Currency: payment obligation/settlement;
- Food: breakfast/canteen/service events;
- Postal: parcels addressed to current lodging;
- Identity: guest/profile matching;
- Accessibility: accommodation match;
- Care: clinical needs without revealing them publicly;
- Public Events: event blocks;
- Emergency Services: evacuation lodging;
- Architecture: renovations/room conversion;
- Tourism: seasonal demand;
- Urban Wildlife: attractants/roosts near guest areas;
- Public Memory: historically significant stays only when legitimately public;
- Cases: theft/missing person/property claims only when evidence supports them.

## 27. Required non-battle implementation contracts

- `LODGING_PROPERTY_STATE`
- `ACCOMMODATION_UNIT_IDENTITY`
- `ROOM_CAPACITY_PROFILE`
- `RESERVATION_LIFECYCLE`
- `WAITLIST_STATE`
- `ROOM_ASSIGNMENT_HISTORY`
- `ROOM_READINESS_STATE`
- `GUEST_STAY_HISTORY`
- `SHARED_ACCOMMODATION_STATE`
- `POKEMON_ACCOMMODATION_HANDOFF`
- `HOUSE_RULE_REVISION_HISTORY`
- `ROOM_TURNAROUND_STATE`
- `EVENT_LODGING_BLOCK`
- `EMERGENCY_LODGING_CONVERSION`
- `LODGING_ACCESSIBILITY_MATCH`
- `LODGING_PRIVACY_BOUNDARY`
- `LODGING_TO_MINECRAFT_PROJECTION`
- `LODGING_TO_TRAVEL_HANDOFF`
- `LODGING_TO_PAYMENTS_HANDOFF`

## 28. Canon questions intentionally left open

- Which lodging institutions already exist in Ouros?
- Do Pokémon Centers provide overnight rooms in this project canon?
- Which settlements rely on inns, hostels, dormitories, cabins, campsites or commercial hotels?
- What forms of guest registration exist?
- Are room prices simulated or abstracted?
- Which properties can host large/aquatic/flying/burrowing Pokémon safely?
- What privacy rules apply to stay histories?
- What emergency lodging authority exists?
- Can players own or manage accommodation businesses?
- How should multiplayer parties reserve shared rooms without inferring relationships?
- Which exact PTU/Caelo rules, if any, govern rest, lodging, sleep or recovery?

No answer above becomes canon until reviewed.