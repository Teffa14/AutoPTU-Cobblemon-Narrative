# Allocation displacement and booking-history provenance research — Pass 349

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is canon.
Date: 2026-09-08

## Repository inspection and duplication check

The complete recursive Narrative tree was inspected before writing. The current global-NPC focus, canon governance, Passes 339 and 347–348, existing Procurement/Commissioning, Shared Equipment, Service Reservation, Communications, Authority and related research were checked so this pass does not create another procurement system or another reservation owner.

Relevant existing ownership:
- Pass 339 owns reservation lifecycle and preserves ACTIVE / RELEASED / CANCELLED history.
- Pass 347 identifies a real overlap between a proposed successor handoff window and unrelated active reservations.
- Pass 348 records a scoped authorized allocation decision without mutating reservations.
- Procurement already owns acquisition after a documented need; repeated conflicts may feed a future procurement need, but that is not Pass 349 ownership.

## Public source A — University of Melbourne shared-space booking displacement

Source: University of Melbourne, Venue Management, shared teaching-space reservations.
https://services.unimelb.edu.au/venuehire/home/booking-rooms-for-your-ad-hoc-booking-or-student-club-activity

Observed structure:
- shared-space requests coexist with a changing authoritative timetable;
- teaching requirements can supersede ad-hoc bookings;
- affected requests can be cancelled;
- cancellation is communicated to the requester rather than silently pretending the earlier booking never existed.

Reusable Ouros lesson:
A later authorized allocation can defeat an earlier valid claim while the earlier claim remains historical evidence. Operational availability and historical booking truth should therefore be separate views.

Not imported:
- University of Melbourne priority rules;
- teaching-specific priority;
- email as a universal Ouros notification channel;
- any legal or policy assumption for Caelo institutions.

## Public source B — Lund University Humanities Lab equipment placement policy

Source: Lund University Humanities Lab, “Placement of equipment.” Published 2026-07-02.
https://www.humlab.lu.se/about/policy-documents/placement-of-equipment/

Observed structure:
- equipment physically present in one facility can remain owned by another unit;
- use and booking rights can depend on a written agreement;
- owner priority can exist for one class of equipment while ordinary booking rules apply to another;
- different agreements can establish different handling rules.

Reusable Ouros lesson:
Physical location, ownership, bookability and priority authority are independent dimensions. A global planner should consume an authored local policy/authority result rather than hard-code one priority rule.

Not imported:
- Lund ownership rules;
- specific university departments;
- written-agreement requirements as universal Caelo law;
- owner priority as a global default.

## Public source C — Harvard Bauer Core Facility booking discipline

Source: The Bauer Core Facility at Harvard University, Policies.
https://bauercore.fas.harvard.edu/policies

Observed structure:
- users must reserve instrumentation before use;
- training/eligibility is separate from reservation;
- reservations can be cancelled within facility-defined rules.

Reusable Ouros lesson:
Booking state, qualification and actual instrument use should remain separate. Displacing a booking must not grant technical readiness, custody or permission to operate the selected resource.

Not imported:
- Harvard account/training rules;
- cancellation deadlines;
- any real-world institutional policy as Ouros canon.

## PTU / Pokémon / game-design scan

Fresh searches covered Pokémon Tabletop United actual plays and currently published campaign feeds. `Pokemon World Tour: United`, `The Reckless Rollers` and `Pokemon Adventures in the Millennium` surfaced again. These sources already appear in repository research or recent passes, so they were not reprocessed simply to increase source count.

This pass therefore uses the new operational sources above for the specific displacement seam and preserves the existing PTU/Caelo boundary. No public campaign is treated as rules authority.

## Transformation into Ouros

The reusable structure is:

1. two claims may each have been valid when created;
2. an authorized later decision may select one course;
3. applying that decision must have its own identity and provenance;
4. the losing reservation remains queryable as historical truth;
5. the planner may consume a derived operational view where the displaced claim no longer blocks the resource;
6. displacement does not prove that the reservation holder personally cancelled, agreed, received notice, lost relationship standing, or stopped needing the resource;
7. displacement does not create custody, readiness, PTU Item legality or physical movement.

Useful invariants:
- `RESERVATION_DISPLACED != RESERVATION_NEVER_EXISTED`
- `INSTITUTIONAL_DISPLACEMENT != HOLDER_CANCELLATION`
- `ALLOCATION_APPLIED != HOLDER_NOTIFIED`
- `ALLOCATION_APPLIED != RESOURCE_TRANSFERRED`
- `ALLOCATION_APPLIED != RESOURCE_READY`
- `LOCAL_PRIORITY_DECISION != GLOBAL_PRIORITY_POLICY`

## Narrative opportunities

A mundane allocation decision can create later scenes without requiring villainy:
- a field worker arrives believing an older reservation is still operative because no notice reached them;
- a supervisor sees the derived schedule but a technician remembers the original booking correctly;
- repeated displacement produces evidence for a procurement need without automatically approving procurement;
- the party can investigate whether a displacement was authorized, whether affected actors were informed, and what alternatives existed at decision time;
- a later review can disagree with a decision without rewriting the decision record.

## PTU/Caelo mechanics boundary

No source in this pass establishes PTU mechanics. A field meter, camera, sample kit or other world resource remains a Narrative world-resource identity unless exact PTU/Caelo content binds it to a mechanical Item.

No displacement rule changes initiative, action economy, held-item legality, movement, status, weather, abilities, Trainer Features or battle outcomes.

## Provenance discipline

This file records external inspiration and transformations only. The executable seam is implemented separately. The proposal remains NON-CANON. No source text, distinctive character, dialogue or plot is copied into Ouros.
