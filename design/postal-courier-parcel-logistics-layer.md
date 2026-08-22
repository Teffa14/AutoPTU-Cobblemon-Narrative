# Ouros Postal, Courier & Parcel Logistics Layer

Status: proposed systems design. Not established canon.

## Purpose

This layer owns the physical movement of letters, parcels and other discrete deliverable objects through a network of intake points, hubs, transport legs, handoffs and final delivery attempts.

It does not replace:

- Communications, which owns information packets, message visibility, channel delivery and acknowledgement;
- Travel, which owns physical route feasibility and transport-service state;
- Material Culture, which owns persistent item identity/provenance when an item matters in its own right;
- Cases/Custody, which owns evidence custody and investigative handling;
- Illicit Networks, which owns unauthorized diversion and illicit flow;
- Workplaces, which owns staffing and shifts;
- Rail/Aerial/Maritime layers, which own their transport modes;
- Finance, which owns payment promises/transfers if postage or commissions later become canon.

The postal layer records what physical object was accepted, where it was routed, who handled it, what delivery was attempted and what exception occurred.

## 1. Postal service

```yaml
postal_service:
  service_id: null
  operator_institution_id: null
  service_area_ids: []
  hub_ids: []
  accepted_item_classes: []
  active_route_policy_refs: []
  privacy_policy_ref: null
  exception_policy_ref: null
  current_state: OPERATING
  dependency_ids: []
  public_information_ids: []
```

Suggested service states:

- OPERATING
- LIMITED
- BACKLOGGED
- REROUTED
- EMERGENCY_ONLY
- SUSPENDED
- RECOVERING
- CLOSED

A service may be operational while one route or hub is unavailable.

## 2. Postal hub

```yaml
postal_hub:
  hub_id: null
  location_id: null
  operator_id: null
  hub_type: null
  intake_supported: true
  sorting_supported: true
  pickup_supported: true
  forwarding_supported: false
  storage_capacity_band: null
  current_state: OPEN
  staff_workplace_id: null
  transport_connection_ids: []
  access_policy_ids: []
```

Candidate hub types:

- LOCAL_POST_OFFICE
- SORTING_HUB
- DEPOT
- INSTITUTIONAL_MAILROOM
- PICKUP_COUNTER
- TEMPORARY_FIELD_POST
- MOBILE_DISPATCH_POINT
- INTERREGIONAL_TRANSFER_HUB

The exact postal institutions and technology level remain canon decisions.

## 3. Physical postal item

A physical postal item keeps stable identity across the route.

```yaml
postal_item:
  postal_item_id: null
  physical_asset_id: null
  item_class: null
  sender_actor_id: null
  sender_institution_id: null
  intended_recipient_actor_id: null
  intended_recipient_institution_id: null
  accepted_at: null
  accepted_hub_id: null
  current_custodian_id: null
  current_location_id: null
  current_state: ACCEPTED
  address_record_id: null
  routing_plan_id: null
  linked_information_packet_ids: []
  linked_custody_case_ids: []
  sensitivity: null
  source_refs: []
```

Candidate item classes:

- LETTER
- DOCUMENT_PACKET
- PARCEL
- INSTITUTIONAL_PACKAGE
- RESEARCH_SAMPLE_SHIPMENT
- MEDICAL_SHIPMENT
- ARCHIVE_LOAN_SHIPMENT
- REPAIRED_OBJECT_RETURN
- EVENT_ENTRY
- OTHER_AUTHORED

Item class does not create mechanics.

One physical item must not become several objects because multiple tracking labels, UI markers or Minecraft representations exist.

## 4. Communications boundary for letters

A letter can have two linked states:

```text
physical envelope / parcel
        |
        +--> postal_item state
        |
        +--> information_packet state
```

Postal Logistics may know that the envelope reached a mailroom.

Communications decides whether the contained information was delivered to or acknowledged by the intended actor.

Hard rules:

- physical delivery does not imply the recipient read the message;
- message acknowledgement does not prove the original physical envelope remains in custody;
- opening/reading permissions are not inferred here;
- sealed content is not exposed merely because routing metadata is visible.

## 5. Address record

```yaml
address_record:
  address_id: null
  destination_type: null
  location_id: null
  actor_id: null
  institution_id: null
  routing_text: null
  landmark_refs: []
  region_id: null
  valid_from: null
  valid_until: null
  status: CURRENT
  source_event_id: null
  supersedes_address_id: null
```

Suggested statuses:

- CURRENT
- HISTORICAL
- TEMPORARY
- INCOMPLETE
- UNVERIFIED
- FORWARDING_ONLY
- INVALIDATED

Ouros does not assume modern street addressing everywhere.

A region may use named routes, institutions, villages, landmarks or authored local systems.

## 6. Address-resolution case

An incomplete address is not solved by omniscient quest logic.

```yaml
address_resolution:
  resolution_id: null
  postal_item_id: null
  observed_problem: null
  candidate_destination_ids: []
  evidence_refs: []
  contact_attempt_ids: []
  working_hypothesis: null
  current_state: OPEN
  resolved_address_id: null
  resolved_by_event_id: null
```

Useful states:

- OPEN
- NEEDS_SENDER_CONTACT
- NEEDS_LOCAL_KNOWLEDGE
- CANDIDATE_FOUND
- RESOLVED
- UNRESOLVED
- RETURN_AUTHORIZED

The system must preserve uncertainty.

## 7. Routing plan

```yaml
routing_plan:
  routing_plan_id: null
  postal_item_id: null
  created_at: null
  planned_leg_ids: []
  selected_service_ids: []
  expected_handoff_hub_ids: []
  route_basis_refs: []
  current_revision: 1
  current_state: ACTIVE
```

A routing plan is a plan, not history.

Travel determines whether a route/service can actually be used.

When conditions change, append a new plan revision rather than rewriting the earlier plan.

## 8. Delivery leg

```yaml
postal_leg:
  leg_id: null
  postal_item_id: null
  sequence: null
  origin_hub_id: null
  destination_hub_id: null
  travel_connection_ids: []
  transport_service_id: null
  assigned_carrier_actor_id: null
  assigned_pokemon_entity_ids: []
  vehicle_asset_id: null
  planned_departure: null
  actual_departure: null
  actual_arrival: null
  state: PLANNED
  exception_ids: []
```

Suggested states:

- PLANNED
- QUEUED
- DISPATCHED
- IN_TRANSIT
- ARRIVED
- CANCELLED
- REROUTED
- FAILED
- UNKNOWN

A Pokémon assigned to a leg gains no carrying capacity or travel Capability from narrative assignment alone.

## 9. Handoff event

```yaml
postal_handoff:
  handoff_id: null
  postal_item_id: null
  from_custodian_id: null
  to_custodian_id: null
  location_id: null
  occurred_at: null
  observed_condition: null
  route_leg_id: null
  receipt_ref: null
  exception_ids: []
```

Handoffs are append-only history.

A missing scan does not prove a missing handoff.
A scan does not prove the parcel contents were inspected.

## 10. Delivery attempt

```yaml
postal_delivery_attempt:
  attempt_id: null
  postal_item_id: null
  attempted_at: null
  destination_id: null
  courier_id: null
  recipient_candidate_id: null
  authorized_endpoint_id: null
  outcome: null
  evidence_refs: []
  next_action: null
```

Candidate outcomes:

- DELIVERED_TO_RECIPIENT
- DELIVERED_TO_AUTHORIZED_ENDPOINT
- HELD_FOR_PICKUP
- RECIPIENT_UNAVAILABLE
- ADDRESS_EXCEPTION
- ACCESS_DENIED
- REFUSED
- UNSAFE_TO_ATTEMPT
- ROUTE_UNAVAILABLE
- RECIPIENT_UNKNOWN
- ATTEMPT_ABORTED

The exact rules for authorized receipt remain canon/institutional policy.

## 11. Physical receipt

```yaml
physical_receipt:
  receipt_id: null
  postal_item_id: null
  received_by_actor_id: null
  received_by_institution_id: null
  received_at: null
  receiving_location_id: null
  condition_at_receipt: null
  authority_basis_ref: null
  linked_acknowledgement_id: null
```

A receipt proves the handoff event represented by the record.

It does not prove:

- contents are correct;
- recipient agrees with the sender;
- the package was opened;
- a separate information packet was understood;
- ownership transferred;
- a contractual obligation was fulfilled unless the relevant agreement says so.

## 12. Postal exception

```yaml
postal_exception:
  exception_id: null
  postal_item_id: null
  detected_at: null
  detected_location_id: null
  exception_type: null
  evidence_refs: []
  suspected_cause_ids: []
  confirmed_cause_id: null
  current_state: OPEN
  resolution_event_id: null
```

Candidate exception types:

- ADDRESS_INCOMPLETE
- ADDRESS_OUTDATED
- MISROUTED
- ROUTE_DELAY
- SERVICE_SUSPENSION
- HUB_BACKLOG
- DAMAGED_PACKAGING
- CONTENT_CONDITION_CONCERN
- CUSTODY_MISMATCH
- ITEM_NOT_LOCATED
- UNAUTHORIZED_DIVERSION_SUSPECTED
- RECIPIENT_UNAVAILABLE
- DELIVERY_REFUSED
- RETURN_REQUIRED

`ITEM_NOT_LOCATED` is knowledge state, not destruction state.

If unauthorized diversion becomes plausible, Cases/Illicit Networks may open linked records.

## 13. Forwarding

```yaml
postal_forwarding:
  forwarding_id: null
  subject_actor_id: null
  subject_institution_id: null
  old_address_id: null
  new_address_id: null
  valid_from: null
  valid_until: null
  scope: null
  authority_basis_ref: null
  privacy: private
```

A forwarding record should not expose a private residence to actors who only need routing success.

The postal service can know where to forward without publishing the destination globally.

## 14. Return-to-sender

```yaml
postal_return:
  return_id: null
  postal_item_id: null
  initiated_at: null
  reason: null
  return_destination_id: null
  return_route_plan_id: null
  completed_at: null
  current_state: PLANNED
```

Return is a new physical route over the same item identity.

Do not create a second copy of the parcel to represent a return.

## 15. Item condition

Condition is observation, not automatic PTU damage.

Possible descriptive states:

- INTACT
- PACKAGING_WORN
- PACKAGING_DAMAGED
- WET
- CONTAMINATION_SUSPECTED
- TEMPERATURE_CONCERN
- SEAL_BROKEN
- CONTENT_CONDITION_UNKNOWN

Exact consequences depend on the asset type and governing systems.

A wet parcel does not automatically damage an Item mechanically.
A broken seal does not automatically prove theft.

## 16. Bulk mail and backlog

Do not instantiate every ordinary envelope as a persistent entity.

Routine traffic can be aggregated:

```yaml
postal_flow_summary:
  flow_id: null
  service_id: null
  hub_id: null
  time_window: null
  volume_band: NORMAL
  backlog_band: NONE
  dominant_route_ids: []
  disruption_ids: []
```

Persist individual postal items when they are:

- player-authored;
- quest-relevant;
- legally/custodially important;
- valuable or unique;
- medically/scientifically sensitive;
- part of a case;
- historically meaningful;
- explicitly tracked by a player.

## 17. Postal careers

Postal work can support noncombat careers:

- intake clerk;
- sorter;
- dispatcher;
- route planner;
- local courier;
- regional carrier;
- hub supervisor;
- address-resolution specialist;
- lost-item investigator;
- institutional mailroom worker;
- temporary disaster-post worker.

Narrative job role never grants a PTU Class, Feature, Skill Rank, Edge or movement Capability.

## 18. Pokémon participation

A Pokémon may participate in delivery only through an authored relationship and validated capability.

Possible roles, if canon supports them:

- carrying small items;
- route accompaniment;
- local navigation assistance;
- air/water/ground transport service;
- rescue supply delivery;
- warehouse handling;
- signaling/dispatch support.

Hard rule:

`species associated with delivery` does not equal `mechanically valid courier`.

The exact individual must satisfy any PTU/Caelo/AutoPTU requirements used mechanically.

## 19. Integration with Communications

Postal Logistics emits physical events such as:

- ACCEPTED
- ARRIVED_AT_HUB
- HANDED_OFF
- OUT_FOR_DELIVERY
- DELIVERED_PHYSICALLY
- HELD_FOR_PICKUP
- RETURNED

Communications may publish or privately deliver notices about those events.

A tracking UI is a presentation of known event records. It should be able to be stale, delayed or incomplete if the world supports that state.

## 20. Integration with Travel and mode-specific transport

Travel is authoritative for route/service feasibility.

Postal Logistics asks:

`Can this planned leg currently run?`

Then records the actual leg outcome.

Rail, Aerial and Maritime own mode-specific operational state. Postal Logistics does not duplicate timetables, corridors, vessel state or airspace rules.

## 21. Integration with Material Culture and provenance

If the delivered object already has a persistent asset ID, `postal_item.physical_asset_id` points to it.

Postal handling adds provenance events.

It does not replace maker, ownership, repair, discovery or archaeological provenance.

Example:

fossil discovered -> museum custody -> packed for loan -> postal legs -> receiving museum custody.

The same fossil ID survives the route.

## 22. Integration with Cases and illicit diversion

A missing or misrouted parcel is not automatically a crime.

Escalation path:

postal exception -> evidence review -> case if warranted -> illicit-network link only if evidence supports it.

This prevents every logistics problem becoming sabotage.

## 23. Integration with homes and changing addresses

Homes and Housing own residence.

Postal Logistics may hold a valid forwarding record without making residence public.

This enables long-term consequences:

- a former home keeps receiving old correspondence;
- a moved NPC's parcel enters forwarding;
- a retired PC's old club receives a letter;
- a neighborhood renumbering creates address-resolution work;
- a rebuilt settlement needs updated delivery routes.

## 24. Offline advancement

Routine mail should advance coarsely while players are offline.

Allowed offline transitions can include:

- queued -> dispatched;
- dispatched -> arrived at hub;
- hub -> next scheduled leg;
- backlog accumulation;
- route delay propagation;
- held-for-pickup expiry if authored policy exists.

Do not resolve high-impact exceptions invisibly when a player decision is required.

Unique or player-authored items should preserve full event history.

## 25. Minecraft representation

Possible presentation:

- post offices and sorting rooms;
- mailboxes;
- depot shelves;
- bags/crates as coarse visual proxies;
- courier NPCs/Pokémon;
- notice boards;
- pickup counters;
- delivery-status UI;
- forwarding notices;
- route maps;
- backlog visuals.

Minecraft is not authoritative for:

- item identity;
- custody;
- delivery completion;
- recipient authority;
- address correctness;
- parcel contents;
- mechanical carrying capacity.

Destroying or unloading a display entity must not erase the server-side postal item.

## 26. Encounter contracts

### Parcel Transfer at North Junction

Narrative premise:
A time-sensitive institutional parcel is moving through a junction when a separate conflict makes the normal transfer unsafe.

FULL version:

- parcel has a physical carrier inside the encounter;
- opposing actors may attempt INTERCEPT/BREAK_THROUGH;
- players may PROTECT_CARRIER or REACH_HANDOFF_POINT;
- moving trains/vehicles or platform zones may matter if the selected location uses them;
- AI understands cargo objective instead of only KOs.

Dependencies:

VERIFIED foundations:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL when exact mechanics appear:
- full lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING for intended full behavior:
- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions if platform/vehicle state is tactical;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics playback.

REDUCED version:
The postal item remains outside the battle grid under secured custody. Players clear a static chokepoint with a legal conventional battle. After battle, the server resolves whether the handoff proceeds, reroutes or remains held.

Narrative premise remains unchanged: the delivery is endangered by the disruption.

### Address Unknown — Last Mile

Narrative premise:
A parcel has reached the correct settlement, but the intended recipient cannot be safely identified from the available address.

FULL version:
Primarily an investigation/social/exploration scenario. If a confrontation arises, it may include escort or withdrawal goals while protecting privacy.

Dependencies for the investigation itself are overworld systems, not battle mechanics.

If battle expands to a moving escort, full behavior depends on complete movement and AI tactical policy.

REDUCED version:
Resolve address evidence, local interviews, maps and forwarding through world state. Any battle is a separate static encounter. Delivery occurs only after the identity/address question is resolved.

### Storm Backlog Field Dispatch

Narrative premise:
Several routes reopen after a long weather closure. A temporary field post must prioritize a small set of urgent physical shipments while ordinary mail remains aggregated.

FULL version:
A timed movement objective could involve multiple dispatch points, dynamic weather/terrain and autonomous couriers.

Dependencies:
- terrain/weather/hazards/zones/reactions;
- complete movement if routes change inside combat;
- AI tactical policy;
- adapter/playback;
- exact Items/Features if used.

REDUCED version:
Prioritization, route selection and courier assignment happen in overworld state. Each risky route can spawn an independent static encounter using the verified foundations. Delivery outcomes write back to the same postal-item records.

## 27. Permanent engine capability classification

The postal layer must use the shared project classification rather than inventing a separate readiness scale.

VERIFIED foundations currently used safely:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL families:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING families for richer postal encounters:

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

An implemented representative mechanic never promotes the whole family.

## 28. Specific overworld blockers

`POSTAL_ITEM_IDENTITY`
Stable identity for physical deliverables and links to persistent assets.

`POSTAL_ADDRESS_AND_FORWARDING`
Private, versioned destination/address state.

`POSTAL_ROUTING_PLAN`
Planned legs derived from current Travel/service knowledge.

`POSTAL_LEG_EXECUTION`
Actual dispatch/arrival state without simulating every meter.

`POSTAL_HANDOFF_HISTORY`
Append-only custody transition records.

`POSTAL_DELIVERY_ATTEMPT`
Final-mile outcomes and authorized endpoints.

`POSTAL_EXCEPTION_STATE`
Missing/misrouted/damaged/delayed knowledge without premature causal claims.

`POSTAL_FLOW_AGGREGATION`
Coarse ordinary volume/backlog state so the server does not persist every envelope.

`POSTAL_TO_COMMUNICATIONS_HANDOFF`
Physical delivery events may inform message delivery but do not equal acknowledgement.

`POSTAL_TO_TRAVEL_HANDOFF`
Travel remains authoritative for route feasibility.

`POSTAL_TO_MINECRAFT_PROJECTION`
Visual mailbags, shelves and couriers are projections, not authoritative item state.

## 29. Canon questions

Still unresolved:

- postal institutions by region;
- address conventions;
- tracking technology;
- privacy and sealed correspondence rules;
- forwarding policy;
- authorized institutional receipt;
- interregional handoff standards;
- player courier careers/businesses;
- Pokémon used institutionally as carriers;
- treatment of mail for missing, retired or deceased people;
- special handling for medical/research/archival objects;
- whether postage/pricing is simulated at all.

## 30. Hard guardrails

Do not infer:

- courier role -> Speed bonus;
- Delibird/Dragonite/Pelipper -> automatic delivery capability;
- Flying type -> package flight service;
- Mountable -> cargo capacity;
- mailbag -> mechanical inventory expansion;
- tracked parcel -> perfect omniscient location;
- missing scan -> theft;
- damaged packaging -> damaged Item mechanics;
- delivered envelope -> message read;
- signed/received parcel -> ownership transferred;
- address knowledge -> public residence information;
- route delay -> battle Weather;
- stolen parcel -> legal ownership change;
- delivery quest -> mandatory escort battle.

The purpose of this layer is to make small physical movements matter without making the Minecraft adapter or narrative generator invent PTU rules.