# Research scan — rescheduled handoff resource conflicts — Pass 347

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is canon.

## Repository gap confirmed before research

Passes 338–346 already separate resource existence, reservations, readiness, requests, consent, handoff authorization, failed attempts, appointment notices and successor authorizations. The remaining seam addressed here is narrower: an accepted reschedule can name a new window even when the same indivisible resource already has a different active reservation in that window.

This pass therefore does not create another reservation system and does not assign priority between claimants. It adds a conflict-admission read model that consumes the existing reservation ledger.

## New public sources

### Loyola University Chicago — Equipment Loan Reservations & Renewals
Source: https://www.luc.edu/its/dms/equipmentloan/loanprogrampolicies/reservationsrenewals/

Public policy distinguishes advance reservation, pickup, modification, renewal and cancellation. It also notes that equipment may already be reserved by others and that late returns can make an otherwise valid reservation impossible to fulfil at the expected time.

Reusable structure for Ouros:
- a previously valid booking can become operationally incompatible with another obligation;
- changing a time window should be checked against current resource allocation rather than assuming the object remains free;
- alternate units or locations can be offered without rewriting the original request history.

No university-specific deadlines, fines, grace periods or liability rules are imported.

### University of Washington Student Technology Loan Program — Policies
Source: https://stlp.uw.edu/policies/

The policy explicitly treats overlapping reservations and checkouts as allocation constraints and can move later reservations when a prior checkout still occupies the same equipment type.

Reusable structure for Ouros:
- physical resource occupancy and future schedule claims can interact;
- a schedule conflict is a world-state fact, not proof that either actor acted improperly;
- a recovery path can involve another unit, another time, or another location when those alternatives actually exist.

No UW-specific eligibility rules or automated rescheduling policy are imported.

### Falmouth University — Equipment Loan and Space Booking Terms
Source: https://www.falmouth.ac.uk/facilities/equipment-loans

The public terms allow bookings to be cancelled or rescheduled because of unavoidable timetable changes, urgent teaching needs, demand or constraints, with alternatives offered where possible.

Reusable structure for Ouros:
- institutional priorities can create legitimate competing claims;
- conflict resolution may produce a substitute time or resource without declaring one participant at fault;
- authority to change a booking should remain explicit and domain-owned.

No institutional hierarchy or real-world disciplinary policy is imported.

### The Reckless Rollers — 2026 PTU actual-play episode catalogue
Source: https://podcastaddict.com/podcast/the-reckless-rollers/2836264

The public episode catalogue identifies the main campaign as Pokémon Tabletop United. Recent 2026 episode descriptions repeatedly place an ordinary job beside unrelated personal or investigative obligations.

Reusable narrative lesson:
- a job does not need to become a boss fight to remain playable;
- unrelated obligations can collide with the work and create meaningful sequencing choices;
- downtime, investigation and employment can occupy the same adventure arc without one erasing the others.

Only this high-level structure is used. No characters, dialogue, murder plot, episode-specific sequence or distinctive setting material is copied.

## PTU / Caelo boundary

The project README remains authoritative about mechanical-source priority. External stories and institutional policies are inspiration sources only. This pass does not invent Skill DCs, item effects, Trainer Feature permissions, movement rules, carrying limits, tactical handoff actions or any battle result.

If a resource later maps to a PTU mechanical Item, its use remains gated by the PTU/Caelo source set and current AutoPTU implementation evidence. A conflict-free world reservation cannot prove that the Item effect itself exists in Java.

## Derived Ouros design lessons

A new handoff window should be screened against known active reservations for the same stable resource ID before it is treated as operationally clear.

A reservation connected to the same request or authorization is supporting evidence for the same work, not automatically a competing claim.

A different active reservation overlapping the proposed window is a conflict fact. The conflict layer should not choose whose work wins.

Cancelled and released reservations remain history but should not block a new window.

An open-ended successor window cannot be proven conflict-free against a finite reservation ledger without additional policy, so the first executable version fails closed for admission screening.

## Originality note

The resulting Ouros proposal and runtime are original combinations of persistent-world scheduling, explicit provenance and resource allocation. They do not reproduce source prose, characters, plots or proprietary mechanics.
