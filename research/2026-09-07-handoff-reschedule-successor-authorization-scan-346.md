# Handoff reschedule successor authorization scan — Pass 346

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-07

Purpose

Research how a previously authorized equipment handoff can move to a different window or place without rewriting the original agreement, teleporting custody, or treating a reschedule request as an accepted replacement.

Repository-first scope check

The recursive repository inventory and Passes 338–345 were inspected before writing. Existing owners already cover resource availability, reservations, readiness, recovery, request consent, physical handoff/custody, failed rendezvous attempts and pre-rendezvous appointment notices. Pass 345 explicitly leaves reschedule acceptance and replacement authorization unresolved. No existing executable owner was found for successor handoff authorizations.

## New public sources

### University of Maryland — Equipment Loan
Source: https://education.umd.edu/about-college/administrative-offices/ets/reservation-desk/equipment-loan

UMD describes equipment access as a two-step flow: reserve first, then physically pick up. It also asks users to stay close to their appointment time, contact the desk when circumstances change, and allows a loan period to be extended only when the held items remain available.

Reusable Ouros structure:
- a changed schedule needs a new availability check;
- changing a time does not prove pickup occurred;
- a prior reservation remains historical evidence rather than being rewritten;
- later users and other commitments can constrain whether a new window is possible.

### Indiana University School of Medicine — iLab reservations
Source: https://medicine.iu.edu/service-cores/ilab

IU documents that instrument reservations can be rescheduled, but individual core policies may prevent or limit modification. A user may therefore request a new time without having unilateral authority to create it.

Reusable Ouros structure:
- `REQUEST_CHANGE != CHANGE_AUTHORIZED`;
- the actor controlling the resource or institutional schedule can remain a separate decision-maker;
- the replacement must preserve the original request/authorization lineage.

### Utah Tech University Makerspace — reservation and out-of-service handling
Source: https://innovation.utahtech.edu/makerspace/policies/

Utah Tech documents fixed machine reservations, late-arrival forfeiture, extensions only when no later user is scheduled, and transfer to a later available time when machinery becomes unavailable.

Reusable Ouros structure:
- a replacement window can be constrained by another booking;
- an operational problem can legitimately move a task without creating fault or conspiracy;
- moving the appointment changes the active execution window while the earlier booking remains part of history.

### Stanford Student Technology Services — pickup hold window
Source: https://thehub.stanford.edu/borrow-equipment/loan-process

Stanford documents a concrete reservation pickup window and a limited hold period after the scheduled pickup time.

Reusable Ouros structure:
- appointment windows should be explicit rather than timeless permissions;
- a new appointment is better represented as a successor authorization than by extending the old one silently.

## Pokémon / PTU search

Fresh searches again surfaced Pokémon World Tour: United and The Reckless Rollers. Repository search confirmed those actual-play families have already been processed repeatedly, so they were not re-added as new evidence for this pass.

A search for fan-game temporal scheduling also re-surfaced PokeXGames' virtual clock. That source was already processed in Pass 196 and was not duplicated.

The PTU/Caelo cross-check remains conservative. The project README identifies PTU Core, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List as governing sources for mechanical claims. Nothing in this pass creates a Skill Check, Trainer Feature, Item effect, movement permission, combat action, timing bonus or other PTU mechanic. The new layer is world-state scheduling/provenance only.

## Derived design lessons

1. A reschedule request is a proposal, not a replacement appointment.
2. The responder must actually receive the request before a response can be attributed to them.
3. Acceptance creates a new authorization with its own ID and effective window.
4. The prior authorization remains queryable as historical state.
5. Once a successor exists, the older authorization becomes operationally superseded rather than deleted.
6. Rejection leaves the existing authorization unchanged unless another system cancels or expires it.
7. A replacement can change time and place while preserving request, resource, provider, accountable actor, receiver and handoff mode unless a separate authority explicitly changes those facts.
8. Custody still changes only through the physical handoff owner.
9. Communication receipt and operational authority remain separate facts: the new authorization can exist even if not every participant has yet learned about it.
10. Minecraft/Cobblemon presentation cannot create or approve a reschedule.

## Originality boundary

No prose, characters, institution names, appointment terms, penalties, plots or distinctive source scenarios are imported into Ouros. Only high-level scheduling and provenance structures are retained.
