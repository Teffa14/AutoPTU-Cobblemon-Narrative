# Pass 100 — Hospitality, Lodging & Guest-Stay Narrative Seeds

Status: NON-CANON PROPOSALS. These concepts are not approved Ouros lore.
Date: 2026-08-28

## Purpose

These seeds exercise the proposed Hospitality continuity layer while preserving Travel, Care, Maintenance, Crisis, PTU and AutoPTU authority boundaries.

## The Reservation Exists, the Room Does Not

A traveler arrives with a valid confirmation, but the allocated room became unserviceable earlier that day. The booking system, front desk note and maintenance record were updated at different times. The useful story is record reconciliation, alternate accommodation and the downstream consequence of a delayed stay.

## The Room Is Empty, but It Is Not Available

An apparently vacant unit may be held for a delayed guest, awaiting an accessibility repair, under inspection or still attached to an active stay. Minecraft visuals never decide availability.

## The Pokémon Is a Returning Guest

Staff recognize a Pokémon from earlier visits. Prior stays can reveal an old route, familiar worker, earlier incident or unresolved promise. Repeated presence does not prove ownership, abandonment or employment.

## The Property Is Open, the Signature Service Is Not

Rooms remain usable while a hot spring, meal service, laundry, shuttle or other amenity is unavailable. Maintenance owns the technical cause. Hospitality owns the guest-facing consequence and later service restoration.

## The Storm Delayed the Staff, Not the Guests

Guests are already checked in when weather delays part of the staff. Remaining workers operate a reduced service pattern. Weather owns the event, Travel owns delayed journeys and Hospitality owns the service state.

## The Full House Changed the Roadside Camp

A local event fills formal accommodation and creates an authorized overflow site. Vendors, couriers and travelers adapt. After the crowd leaves, the temporary site can remain relevant through a path, habit, ecological observation or community memory.

## The Guest Checked Out but Never Left Town

Checkout proves departure from the establishment, not the settlement. A traveler may move to another property, miss onward transport, attend a private meeting or simply remain nearby.

## The Lodge Became a Refuge for One Night

A normal property temporarily supports emergency shelter. Crisis activates the emergency use. Hospitality records which ordinary services were suspended or repurposed. Emergency occupancy does not automatically become a commercial stay.

## The Old Guesthouse Is Now Something Else

An old lodging building becomes housing, a workshop, community space, archive or abandoned structure. Historic receipts and room references remain valid evidence without overriding present-day use.

## Mystery — Four Bookings, Three Actual Stays

Four reservation records appear connected to one weekend. One may have been superseded, one may never have converted to check-in, or one stay may have moved properties. Evidence comes from timestamps, allocation history, arrival records and staff testimony rather than a hidden truth score.

## Mystery — Five Guest Reports, Two Rooms

Several statements appear to describe many locations. Room reassignment and old room numbers may reconcile them into two actual units. Guest privacy remains intact unless evidence access is authorized.

## Long arc — A Town Learns Its Visitors

First establish ordinary stays, staff and recurring travelers. Later a seasonal event or transport disruption fills capacity. Overflow changes courier routes, street activity and local business patterns. Capacity eventually returns, but some habits persist. Months later an old booking, returning traveler or former overflow site makes the earlier period relevant again.

No abstract tourism score is required.

## Encounter concept — Guest Wing Withdrawal

Full intended form wants multiple withdrawal routes, Intercept/forced movement, reactions, protection objectives, objective-aware AI and authoritative playback.

Current dependencies:

```yaml
targeting/footprints/range/LoS: VERIFIED
base movement legality: VERIFIED
complete movement including push/pull/knockback/interception/forced movement: PARTIAL
core calculations: VERIFIED
action economy/initiative: VERIFIED
full turn/round lifecycle: PARTIAL
full stateful damage pipeline: PARTIAL
status lifecycle: PARTIAL
terrain/weather/hazards/zones/reactions: BLOCKING
move-specific behavior: PARTIAL
abilities: PARTIAL
items: PARTIAL
Trainer Features/perks: PARTIAL
AI legal-action infrastructure: VERIFIED
AI tactical policy: BLOCKING
Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Reduced form:
- move uninvolved guests outside the tactical area first;
- exclude private rooms, luggage and service carts;
- select participants explicitly in Ouros;
- use a static lobby, courtyard or corridor;
- the result secures only the immediate area;
- Hospitality/Crisis determines re-entry and stay continuation afterward.

## Encounter concept — Overflow Camp Perimeter

Full form may need route-control/protection goals, reactions, reviewed terrain and tactical policy aware of the nonparticipant area.

Reduced form keeps occupants, tents, luggage and resting Pokémon outside the BattleSpec. AutoPTU receives a static perimeter. The result cannot admit, remove or reassign guests and cannot complete PTU rest.

## Encounter concept — Service Courtyard Interruption

Full form may need worker withdrawal, protection objectives, reactions and tactical policy.

Reduced form has Maintenance stop work before the encounter. Workers and equipment leave. The arena is static. The outcome cannot repair the asset or restore the amenity.

## PTU rest guardrail

PTU 1.05 distinguishes ordinary rest, Extended Rest and Pokémon Center healing. Therefore no seed may infer HP recovery, AP refresh, Daily Move refresh, Status removal or Pokémon Center healing from a room booking, bed animation or elapsed reservation time.

## Canon questions

Still open:
- lodging types and regional distribution;
- whether any Pokémon Centers provide overnight rooms;
- independent Pokémon guest status;
- reservation, privacy and payment practices;
- emergency lodging relationships;
- camping norms;
- accessibility practices;
- individual Pokémon hospitality roles.