# Resource allocation notice recipient-binding research — Pass 351

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-08

## Question

What reusable design evidence supports keeping a reservation displacement, the obligation to notify, the intended recipient, actual message transport and later replanning as distinct facts?

## Repository cross-check

Pass 350 already separates allocation application from notice obligation and delegates message delivery to `InformationEventQueue`, actor knowledge to memory/belief and plan changes to the existing replanning coordinator. Inspection found one remaining provenance hole: `link_notice_communication()` verified only that an event ID existed. It did not verify that the event was addressed to the affected reservation holder or authored by the actor named on the notice link.

Pass 287 already provides the correct delivery-to-knowledge/replanning owner. Pass 351 therefore should tighten binding rather than create another wake-up system.

## New public sources

### UMass Amherst CORUM instruments

Source: https://www.umass.edu/ials/corum/corum-admin-questions-answers/corum-instruments
Retrieved: 2026-09-08

CORUM distinguishes administrative holds/offline instrument state from later user notification. An offline instrument can remain reservable while users are warned that the booking may be automatically cancelled, and the system sends a cancellation notification when that transition occurs.

Reusable structure for Ouros:

- resource state can change independently of a person's knowledge;
- a cancellation/displacement event should produce a directed notification artifact;
- notification provenance matters because the operational state and the actor's received state can diverge.

No institutional policy text or local business rule is imported into Ouros.

### Auburn University LabTrack manual

Source: https://shse.eng.auburn.edu/blog/labtrack-user-manual/
Retrieved: 2026-09-08

The public manual describes a waitlist where cancellation of a confirmed reservation causes the first person in the queue to receive an automatic notification. Return confirmation similarly notifies the requester after the equipment owner confirms return.

Reusable structure:

- a state transition identifies a specific recipient;
- notification of one eligible actor does not imply notification of every interested actor;
- recipient selection and resource transition are separately auditable.

The queue policy and institutional workflow are not adopted as Ouros rules.

### University of Pennsylvania shared-equipment guidelines

Source: https://www.med.upenn.edu/afcri/equipment-reservations-and-use-guidelines.html
Retrieved: 2026-09-08

The guidelines require reservations to include identifying/contact information and require users who cannot use their slot to open it so others can use the equipment. This reinforces a basic provenance requirement: shared-resource scheduling is actor-specific rather than an anonymous global state.

Reusable structure:

- reservations and subsequent communications need stable actor identity;
- a changed slot should remain attributable to the holder affected by that change.

### Pokémon Unbound mission structure

Sources:
- https://unboundwiki.com/missions/
- https://unboundwiki.com/walkthrough/
Retrieved: 2026-09-08

The public documentation exposes a Mission Log with many side missions distributed through locations and prerequisites while the main journey continues. The reusable lesson is structural: persistent side obligations can retain their own state, location and completion history without replacing the primary story.

For Ouros this supports letting logistical incidents such as a displaced booking become optional investigation/work scenes with persistent evidence rather than forcing them into the main plot or a battle.

No mission text, characters, rewards or plots are copied.

## PTU / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` records that Kairos treats downtime, persistent property, crafting, training, work-like progression and one-shot quests as parts of a living PTU world. That supports resource/logistics scenes as legitimate world-agent content. It does not authorize a new PTU combat rule or a new species/form.

The same index points combat, movement, statuses, terrain/weather, encounters and recurring rivals to the supplied Kairos/PTU reference. Pass 351 introduces no new PTU mechanical assumption.

## Design extraction

A reliable notice chain should preserve at least five separately queryable facts:

1. the reservation or obligation that existed;
2. the later allocation/displacement decision;
3. the person who must be informed;
4. the exact communication event addressed to that person;
5. the receiver's later knowledge and replanning after actual delivery.

A message delivered to another actor can still be a real world event. It cannot satisfy the affected holder's notice obligation.

## Original Ouros opportunities

A wrong-recipient notice can create two simultaneous problems without requiring villainy. The actual holder continues toward an obsolete pickup because no valid notice reached them. The unintended recipient may alter their own plans after receiving a perfectly real but irrelevant allocation update. The player can reconstruct both causal chains from reservation, notice, message addressing and delivery records.

This is PROPOSED design material only. No canon changes are made by this research note.
