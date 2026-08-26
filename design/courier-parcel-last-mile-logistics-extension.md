# Courier, Parcel & Last-Mile Logistics Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already knows how locations connect, how transport services operate, how information is delivered, how businesses depend on supply and how households relocate. This extension handles the physical handoff layer between those systems.

Its job is to answer a narrow set of questions:

- What physical shipment exists?
- Who entrusted it to whom?
- Where was it last verified?
- Which route/service legs are carrying it?
- Has delivery actually been attempted?
- Did custody change?
- Did the recipient move?
- Was the object redirected, returned, damaged, delayed or recovered?
- Which other world system changes after a successful or failed handoff?

It does not own the travel graph, the item definition, the recipient's residence, the sender's business, or the content of a message inside a package.

## 1. Shipment record

```yaml
shipment:
  shipment_id: null
  shipment_type: PARCEL
  sender_actor_id: null
  sender_institution_id: null
  intended_recipient_actor_id: null
  intended_recipient_institution_id: null
  origin_location_id: null
  intended_destination_location_id: null
  parcel_item_refs: []
  information_packet_refs: []
  created_at: null
  accepted_at: null
  current_state: CREATED
  current_custodian_ref: null
  current_location_id: null
  current_service_id: null
  planned_leg_ids: []
  active_leg_id: null
  urgency_band: NORMAL
  condition_state: UNKNOWN
  confidentiality_tag: null
  source_refs: []
```

Candidate shipment types:

- PARCEL
- DOCUMENT_PACKET
- RESEARCH_SAMPLE
- REPLACEMENT_PART
- MEDICAL_SUPPLY
- EVENT_MATERIAL
- PERSONAL_BELONGINGS
- COMMERCIAL_ORDER
- RETURN

These categories are descriptive. They do not create item rules, legality, prices or handling mechanics.

## 2. Shipment lifecycle

Suggested states:

- CREATED
- AWAITING_INTAKE
- ACCEPTED
- SORTING
- READY_FOR_DISPATCH
- IN_TRANSIT
- AT_TRANSFER_POINT
- OUT_FOR_DELIVERY
- DELIVERY_ATTEMPTED
- DELIVERED
- ACKNOWLEDGED
- REDIRECT_REQUIRED
- RETURNING
- RETURNED
- HELD
- DELAYED
- LOST
- RECOVERED
- CANCELLED

A state change requires a traceable event.

`DELIVERED` means possession reached the intended recipient or an explicitly approved receiving proxy. It should not be inferred from arrival in the same settlement.

## 3. Parcel identity and item boundary

The delivery layer should reference existing authoritative item instances when an item already exists.

```yaml
parcel_manifest_entry:
  shipment_id: null
  item_instance_id: null
  quantity_ref: null
  packaging_ref: null
  declared_description: null
  observed_condition: null
  last_verified_event_id: null
```

The manifest may contain declared descriptions that differ from later observation. It does not prove hidden contents.

Hard rules:

- delivery state cannot create or delete item instances silently;
- packaging is not proof of ownership;
- possession during transit is custody, not ownership;
- an unopened package does not grant the courier knowledge of its contents;
- the narrative layer cannot invent weight, fragility, legality or special handling unless canon/rules establish them.

## 4. Custody transfer

```yaml
custody_transfer:
  transfer_id: null
  shipment_id: null
  from_custodian_ref: null
  to_custodian_ref: null
  location_id: null
  transferred_at: null
  evidence_refs: []
  observed_condition: null
  accepted: true
  exception_ref: null
```

A custodian can be:

- a person;
- an institution;
- a staffed service desk;
- a transport service;
- an approved storage facility;
- an explicitly represented automated system if canon supports it.

Never infer custody merely because an NPC is standing near a parcel prop in Minecraft.

## 5. Delivery leg

Travel owns the geography. Delivery references it.

```yaml
delivery_leg:
  leg_id: null
  shipment_id: null
  origin_node_id: null
  destination_node_id: null
  travel_connection_ids: []
  transport_service_id: null
  assigned_courier_ids: []
  planned_departure: null
  actual_departure: null
  planned_arrival: null
  actual_arrival: null
  leg_state: PLANNED
  exception_ids: []
```

Candidate leg states:

- PLANNED
- READY
- DEPARTED
- IN_TRANSIT
- ARRIVED
- MISROUTED
- INTERRUPTED
- CANCELLED

The delivery extension must not duplicate Travel's route closures, weather, service state or movement legality. It reads those states and records the delivery consequence.

## 6. Intake, sorting and dispatch

Physical delivery can fail before any route begins.

```yaml
dispatch_batch:
  batch_id: null
  service_node_id: null
  shipment_ids: []
  created_at: null
  sorting_state: null
  assigned_leg_ids: []
  backlog_reason_ids: []
  dispatched_at: null
```

Backlog may come from:

- staffing state;
- service closure;
- transport suspension;
- route restriction;
- facility maintenance;
- event pressure;
- crisis state;
- recipient/address exception;
- unknown cause pending investigation.

A backlog should not be generated randomly when no supporting world state exists.

## 7. Delivery attempt

```yaml
delivery_attempt:
  attempt_id: null
  shipment_id: null
  attempted_at: null
  location_id: null
  courier_ref: null
  recipient_ref: null
  outcome: null
  evidence_refs: []
  next_action: null
```

Candidate outcomes:

- HANDED_TO_RECIPIENT
- HANDED_TO_APPROVED_PROXY
- RECIPIENT_UNAVAILABLE
- RECIPIENT_MOVED
- DESTINATION_CLOSED
- ADDRESS_INCOMPLETE
- ACCESS_BLOCKED
- SHIPMENT_MISMATCH
- REFUSED
- OTHER_RECORDED_EXCEPTION

A failed attempt is useful world state. It can create a future callback instead of becoming invisible retry logic.

## 8. Redirect and relocation integration

Residential Life owns where an actor currently resides. Courier state can react to that information.

```yaml
shipment_redirect:
  redirect_id: null
  shipment_id: null
  old_destination_id: null
  proposed_destination_id: null
  reason: RECIPIENT_MOVED
  authorized_by_ref: null
  authorized_at: null
  state: PENDING
```

Do not automatically expose a private new address to every sender or courier. The residential/privacy layer decides whether a forwarding route exists.

Possible valid outcomes:

- institutional forwarding;
- recipient pickup at a service node;
- sender contact through an established channel;
- return to sender;
- hold pending instructions.

## 9. Return-to-sender state

```yaml
return_case:
  return_id: null
  shipment_id: null
  reason: null
  initiated_at: null
  return_destination_id: null
  return_leg_ids: []
  current_state: PENDING
  completion_event_id: null
```

A return should preserve the original custody and attempt history.

## 10. Parcel condition

Condition observations are claims about a physical object, not automatic mechanical item damage.

Suggested states:

- UNKNOWN
- INTACT
- PACKAGING_DAMAGED
- CONTENTS_EXPOSED
- WET
- CONTAMINATION_SUSPECTED
- TEMPERATURE_CONCERN
- CONDITION_DISPUTED

Exact item damage, medicine spoilage, sample viability or contamination effects require governing rules/canon.

## 11. Service nodes

Candidate physical delivery nodes:

- staffed counter;
- depot;
- sorting room;
- transport terminal handoff desk;
- institutional mailroom;
- clinic receiving desk;
- research receiving station;
- temporary event receiving point;
- pickup locker/terminal only if canon supports it.

The node's staffing and physical availability come from existing workplace/facility layers.

## 12. Last-mile significance test

Routine deliveries should compress.

Expand a delivery into gameplay when one or more are true:

- a recipient moved;
- the parcel is tied to an active player promise;
- route/service state changed;
- custody is disputed;
- the parcel condition changed;
- delivery enables or blocks a repair, treatment, event or research step;
- the shipment is misrouted;
- a known cadence breaks;
- the player explicitly chooses courier work;
- a case/investigation intersects the chain;
- an ecological/faction/crisis event affects the route.

## 13. World-state handoff

Delivery itself should rarely own the final consequence.

Examples:

```text
replacement part delivered
→ Facility Maintenance decides whether repair can advance

medical supply delivered
→ Care layer decides service/treatment consequence

research sample delivered
→ Science layer decides intake/review consequence

event materials delivered
→ Temporary Event Operations clears or updates readiness dependency

commercial order delivered
→ Storefront layer updates availability/stock presentation

personal belongings delivered after relocation
→ Residential layer updates household/move state

document packet delivered
→ Communications/Case layer updates recipient knowledge or case state only if the packet is actually read/accepted
```

## 14. Minecraft presentation

Possible manifestations:

- parcel props with server-owned shipment IDs;
- changing sorting shelves;
- staffed delivery counters;
- backlog signage;
- route-delay notices;
- pickup-ready notifications;
- return bins or held-parcel storage;
- visible empty/full dispatch carts;
- courier NPC schedules;
- receiving desks at clinics, workshops or institutions.

Minecraft must not decide ownership, delivery success or item effects from proximity alone.

## 15. Pokémon participation boundary

A Pokémon can participate in delivery only when its individual authoritative state and the approved setting support the required task.

Forbidden inference examples:

- Flying type means air courier;
- large Pokémon means cargo carrier;
- Psychic type means sorting specialist;
- Electric type means electronics handler;
- species reputation means legal workplace qualification.

Where the task becomes mechanically meaningful, use approved PTU/Caelo capabilities, Moves, Features or other governing rules. Otherwise keep the participation narrative and non-mechanical.

## 16. Encounter — Moving Convoy Interruption

Narrative premise: a shipment tied to a real world dependency is interrupted while moving between transfer points.

Full intended version may include:

- moving cargo or convoy position;
- protect/escape objectives;
- interception;
- forced movement;
- terrain/weather effects;
- route hazards;
- objective-aware enemy and allied AI;
- damage to shipment condition based on explicit rules;
- adapter playback synchronized with convoy progress.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:

Freeze the convoy as world state before combat. Place the parcel outside tactical ownership changes. Run a static legal encounter at a chokepoint using only currently verified mechanical slices. Victory allows the journey to resume. Defeat or withdrawal changes route/service state through authored consequences, but no unsupported escort, cargo-damage, interception or weather mechanics are simulated.

## 17. Encounter — Depot Recovery

Narrative premise: a disrupted depot contains a parcel needed for another ongoing project, while a legal battle blocks safe access.

Full intended version may include dynamic blocked aisles, civilians/workers evacuating, destructible or hazardous zones, knockback near stored cargo, containment objectives and AI that values exits or protected storage.

Capability dependencies follow the same permanent map. Complete movement, environmental zones/reactions, objective-aware AI and adapter playback are BLOCKING; lifecycle, damage/status/content families remain PARTIAL.

Reduced version:

Evacuate workers and freeze the depot layout before tactical resolution. The parcel remains inaccessible until a standard static battle ends. Afterward, a separate world-state interaction records recovery and custody transfer. No tactical crate protection or environmental damage is invented.

## 18. Noncombat encounter — The Address That Changed

A delivery reaches the correct settlement but the recipient no longer lives at the stored destination.

This can run now using:

- shipment history;
- residential relocation state;
- privacy/contact graph;
- delivery attempts;
- institutional forwarding if already established;
- public or authored information.

Possible outcomes include hold, redirect, pickup, sender contact or return. The generator must not expose a private address or invent forwarding law.

## 19. Noncombat encounter — Three Parcels, One Wrong Cart

A sorting discrepancy leaves three shipments with conflicting route evidence.

Players can compare:

- intake timestamps;
- custody-transfer records;
- dispatch batches;
- route/service state;
- physical labels/observations;
- staff claims;
- receiving records.

The solution should come from evidence. The narrative engine must keep declared destination, actual location, staff belief and canonical shipment state separate.

## 20. Promotion gate

Before a concrete courier network becomes canon, review:

1. which settlements have delivery nodes;
2. what transport modes actually exist;
3. who operates services;
4. address/privacy conventions;
5. whether forwarding, pickup, signatures, insurance or returns exist and under what rules;
6. what item categories need special handling;
7. what Pokémon workplace participation is actually supported;
8. Minecraft representation limits;
9. exact PTU/Caelo mechanics for any combat-relevant cargo interaction;
10. adapter support for moving objectives or convoy playback.
