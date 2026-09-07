# Temporal resource reservation lifecycle scan — Pass 339

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-07
Canon authority: NONE

## Question

How can Ouros turn Pass 338 resource availability into persistent, believable shared-resource conflicts without treating a reservation as possession, use, ownership or permanent exclusion?

## Repository inspection before research

The recursive repository tree, `CURRENT_FOCUS.md`, Pass 338 resource contract, executable resource gate, tests and latest readiness snapshot were inspected before writing.

Existing specialized custody owners were not duplicated. Pass 338 already represents stable resources and blocks intents that lack a locally usable resource. Its explicit unresolved list includes reservation mutation, expiry and release, borrowing, transfer and contention.

Pass 339 therefore addresses temporal claims on one ordinary resource ID and the distinction between reservation, checkout, use, release, cancellation and expiry.

## Public sources

### University of Illinois Chicago — Fluorescence Imaging Core policies

URL: https://fic.uic.edu/policies/

Observed reusable structure:

- scarce equipment is booked for a time window;
- a user can cancel before the booking;
- unused bookings and no-shows remain distinguishable from successful use;
- cancellation can make capacity available to other users.

Ouros abstraction:

`RESERVATION_CREATED != RESOURCE_USED`

`RESERVATION_CANCELLED != RESOURCE_BROKEN`

No fee schedule, institutional wording or exact cancellation threshold is imported.

### Stanford Nano Shared Facilities — reservation policies

URL: https://snsf.stanford.edu/labmembers/policies/reservation-policies

Observed reusable structure:

- users are expected to release time they no longer need;
- release makes a scarce slot available to others;
- booking on behalf of another user is restricted rather than assumed valid;
- reservation behavior is part of fair shared access.

Ouros abstraction:

A claim has an actor and a bounded window. Releasing the claim is an explicit event. One NPC cannot silently create authority for another simply by occupying a calendar slot.

### Yale Research — shared-core reservation policy

URL: https://research.yale.edu/cores/mcc/policies

Observed reusable structure:

- reservation and actual usage are different records;
- a no-show can cause automatic cancellation after a bounded interval;
- access category/approval can constrain when a user may reserve or use a resource.

Ouros abstraction:

`RESERVED_FOR_ACTOR != HELD_BY_ACTOR`

`RESERVATION_EXPIRED != RESOURCE_TRANSFERRED`

`PERMISSION_TO_RESERVE != PHYSICAL_POSSESSION`

Pass 339 does not import Yale's timing, billing or access categories.

### University of Pennsylvania — equipment reservation/use guidelines

URL: https://www.med.upenn.edu/afcri/equipment-reservations-and-use-guidelines.html

Observed reusable structure:

- shared equipment may have authorization prerequisites;
- bookings identify the user;
- unused time should be opened so others can use it;
- repeated no-shows can produce later access consequences.

Ouros abstraction:

Reservation identity, permission, usage and later relationship/policy consequences remain separate state families.

### Pokémon Battle Factory — rental structure

Public reference: https://bulbapedia.bulbagarden.net/wiki/Battle_Factory_(Generation_IV)

Observed reusable structure:

- a participant temporarily uses a roster that they do not own;
- temporary allocation has clear entry/exit boundaries;
- returning or swapping a temporary allocation is part of the activity loop.

Ouros abstraction only:

Temporary operational control does not imply ownership. A borrowed or checked-out world resource can remain institutionally owned while another actor currently holds it.

No Battle Factory characters, layout, streak structure, rental tables, teams or mechanical rules are imported.

### PokeU Panic — public PTU campaign listing

URL: https://startplaying.games/adventure/cmr6r2xws01ecl604wm1bf5qr

The public listing identifies the campaign as Pokémon Tabletop United and frames the player loop around overlapping ordinary obligations such as classes, friendships, clubs and battles.

Reusable high-level lesson:

Routine scheduling pressure can carry adventure consequences. A shared-resource conflict can matter because multiple legitimate obligations collide, without requiring crime, sabotage or a villain.

No university, characters, conspiracy, scenario text or campaign plot is imported.

## Derived Ouros design lessons

A reservation is a temporal claim over an already-existing resource. It must have its own stable identity and history.

A booking before its start time is scheduled, not currently active. During its interval it can exclude conflicting claims. After its end it can be treated as expired for current planning without rewriting the historical record.

Release and cancellation are explicit state changes. Expiry can be derived from semantic time while preserving the original reservation record.

Checkout is separate from reservation. A booked kit can still be sitting in a locker. A checked-out kit has a current holder. Returning it changes holder/location state but does not erase the booking record that explains why it was issued.

A no-show should eventually be capable of generating social or policy consequences, but Pass 339 does not invent penalties. Those consequences belong to later institutional/social-policy integration.

## Copyright / transformation boundary

This pass extracts generic operational structures and game-design patterns. It does not reproduce protected dialogue, distinctive characters, plots, maps, scenario prose or proprietary rules.

## Mechanical boundary

The reduced reservation lifecycle is world-agent logic and requires no PTU combat rule.

If a future reserved resource has a PTU Item effect, reservation readiness proves only world availability. Exact Item legality and effect resolution remain individually gated by AutoPTU/PTU/Caelo evidence.
