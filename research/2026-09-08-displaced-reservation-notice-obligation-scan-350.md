# Displaced reservation notice obligation scan — Pass 350

Status: RESEARCH / NON-CANON
Date: 2026-09-08

## Question

After an authorized allocation decision displaces an earlier shared-resource reservation, what reusable structures help Ouros preserve the obligation to inform the affected holder without pretending that the message was already authored, delivered, understood, or accepted?

## Repository cross-check

Pass 339 owns the source reservation lifecycle. Pass 345 already proves that authored communication and delivered communication are separate states. Pass 348 owns institutional allocation decisions. Pass 349 records operational displacement while preserving the historical booking and explicitly leaves holder notification downstream. Existing Communications remains the delivery owner. This pass therefore adds only notice obligations and links to real communication events.

No canon file is changed by this research.

## New public sources

### University of Southern Denmark — DaMBIC Equipment Booking
URL: https://www.sdu.dk/en/forskning/dambic/user-info/equipment-booking

The published policy says users should cancel when they know they cannot use a booking and, for late cancellations, notify both the next user and the facility mailing list. It also recommends notifying the next user when a session finishes early.

Reusable structure for Ouros: a changed resource window can create a concrete duty to inform a specific downstream actor. The duty and the delivery channel remain separate records.

### Yale West Campus Materials Characterization Core — Core Policies
URL: https://ywcmatsci.yale.edu/users/core-policies

The core describes automatic cancellation after a no-show period and says other users are informed so they can take the released time.

Reusable structure: an institutional state transition can generate communication obligations to affected users. The booking state may change before every interested actor has received the update.

### Northern Illinois University Libraries — Room Reservation Policy
URL: https://www.niu.edu/university-libraries/about/policies/roomreservation.shtml

NIU states that a reservation is not confirmed until a confirmation email is sent. The useful abstraction is evidentiary rather than domain-specific: an internal scheduling state and a message proving that state to a participant are different artifacts.

### Pokémon Tabletop community — exploration-focused PTU recruitment post
URL: https://www.reddit.com/r/PokemonTabletop/comments/1e9ob4g

A public PTU campaign recruitment post describes an exploration-and-roleplay-focused campaign around ancient ruins with homebrewed maps, items, Pokémon and mechanics. No setting details or authored content are imported.

Reusable lesson: a PTU campaign can support substantial play around exploration, logistics and discovery instead of requiring every meaningful obstacle to become a combat scene. This supports a reduced Ouros version where an outdated booking produces travel, investigation and replanning without invoking AutoPTU.

## Transformed Ouros lessons

A displaced reservation should generate an auditable obligation tied to the exact booking and affected actor. The obligation should survive even if no message has been authored yet.

A communication event can satisfy the delivery side only when the existing information runtime reports actual delivery. QUEUED or WAITING_LOCAL_ACK remains unresolved.

One delivered notice cannot make other displaced holders omniscient. Multiple displaced bookings require independently traceable obligations, even when a later UI chooses to bundle messages.

Institutional displacement does not imply wrongdoing by the displaced holder, the allocator, or the sender. Consequences should derive from the timeline: when the decision occurred, when the obligation arose, when a message was authored, when it arrived, and what the actor did with the information available then.

## Provenance / canon boundary

Everything in this file is research. The linked policies and community material provide high-level patterns only. No external dialogue, characters, locations, plots, mechanics, institutional rules or protected prose become Ouros canon.
