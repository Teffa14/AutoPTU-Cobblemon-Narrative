# Appointment notice persistence scan — Pass 359

Status: RESEARCH / PROVENANCE ONLY
Canon authority: NONE
Date: 2026-09-08

## Internal inspection before research

The recursive repository tree at narrative head `ab8a5e7e9d16e050da9f1eb6264bd1707cc7206b` was inspected before writing. The active global-NPC directive remains `CURRENT_FOCUS.md`. Passes 339 and 342–358 were checked as the current resource-history chain, with particular attention to Pass 345 appointment coordination, Pass 346 rescheduling, Pass 357 resource checkpoint V3 and Pass 358 coherent world checkpoint V8.

Existing research was searched before selecting external sources. Recent recurring sources such as Pokemon World Tour: United, The Reckless Rollers, Adventures in the Millennium, Radiant Heliodor, Pokemon Rollout!, Pokemon Rejuvenation, West Marches, Pokemon Living World, Pokemon Lodestone, Pokemon Keishou and Pokemon Desolation were not reprocessed for this slice.

## Public operations source — UIC Fluorescence Imaging Core

Source: University of Illinois Chicago, Fluorescence Imaging Core, Policies.
URL: https://fic.uic.edu/policies/
Accessed: 2026-09-08.

Observed high-level structure: a reservation can be cancelled through one path with sufficient notice and through a different communication path when the cancellation is late. A missed reservation remains distinguishable from a properly cancelled booking.

Reusable Ouros abstraction: the authored cancellation message, the scheduling consequence and any later no-show observation should remain separate events. An NPC creating a notice does not prove the counterpart received it, and a later missed handoff should not retroactively erase the earlier communication attempt.

Not imported: billing rates, UIC-specific deadlines, institutional sanctions or facility policy.

## Public operations source — Texas A&M Microscopy and Imaging Center

Source: Texas A&M University, `To Create an Equipment Reservation`.
URL: https://microscopy.tamu.edu/to-create-an-equipment-reservation/
Accessed: 2026-09-08.

Observed high-level structure: permission to reserve depends on training/check-out status, bookings occupy explicit calendar windows, and users are expected to cancel early enough to release capacity.

Reusable Ouros abstraction: scheduling, qualification and physical access are independent dimensions. A confirmed appointment does not prove that an actor has the capability or permission to operate a resource, and possession of permission does not itself prove a booking was communicated.

Not imported: the iLab product, specific booking horizon, office hours or qualification rules.

## New public PTU source — Pokemon Rainbow Wing

Source: public September 4, 2026 PTU recruitment post, `Pokemon Rainbow Wing`.
URL: https://www.reddit.com/r/FoundryLFG/comments/1w7boia/
Accessed: 2026-09-08.

This source had no prior repository match when checked before use.

Observed high-level structure: the campaign frames a laboratory selection process around more than battle victory. Adaptation, command of unfamiliar Pokemon, treatment of partners and general conduct are all part of evaluation. The later journey combines research, training, care, rivalries, exploration and rebuilt habitat schedules with distinct day/night encounter tables.

Reusable Ouros lessons:

- institutional encounters can evaluate conduct over time rather than only combat outcomes;
- NPC evaluators can observe different evidence channels and reach decisions later;
- research and logistical obligations can coexist with gym/travel arcs instead of becoming disposable side text;
- a living-region presentation benefits when schedules and habitat timing continue independently of the player.

Not imported: Johto plot, Professor Elm material, rental-Pokemon tournament structure, named characters, encounter tables, dialogue or homebrew rules.

## New fan-game structure — Pokemon Terra Nova

Source: Eevee Expo, completed fangame `Pokemon Terra Nova`.
URL: https://eeveeexpo.com/threads/4613/
Accessed: 2026-09-08.

This title had no exact prior repository match when checked before use.

Observed high-level structure: a gym leader can already be occupied with another challenger when the player returns after a loss; the player can watch or return later. The game also exposes many optional side quests through a quest log.

Reusable Ouros lessons:

- important NPCs can have schedules and commitments that continue without waiting for the player;
- arriving at the correct place does not guarantee immediate service;
- watching another appointment can itself become environmental storytelling and evidence about NPC behavior;
- persistent optional obligations can remain available while the main journey continues.

Not imported: Terra Nova characters, futuristic setting, quests, battle content or proprietary story material.

## PTU / Caelo cross-check

The project source inventory continues to identify PTU Core, Pokédex material, the Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List as governing internal sources for mechanical and setting claims.

Pass 359 adds persistence for a world-state communication record. It does not add a PTU combat rule, Trainer Feature, Ability, Move, Item or Caelo fact. Public campaigns and fan games above are design references only and cannot override those governing materials.

## Design synthesis for Ouros

A handoff appointment should be reconstructable as a causal chain rather than a binary quest flag:

accepted request -> authorization -> authored confirmation/cancellation/reschedule notice -> independent message delivery -> actor knowledge -> possible arrival/attempt -> possible physical transfer

Each arrow can fail or occur at a different time. The useful narrative space comes from preserving those differences.

Examples enabled without asserting canon:

- both sides authored confirmations but only one was delivered before a communications outage;
- a cancellation was authored, the recipient travelled before receiving it, and the resource remained physically untouched;
- an accountable third party knows a pickup was scheduled but never received the later reschedule request;
- a valid appointment survives a session boundary while the receiving actor pursues another obligation;
- a player arrives while an NPC is occupied with another legitimate commitment and can wait, observe, reroute or return.

## Provenance boundary

Everything in this file is research or transformed design inference. It does not authorize a specific Ouros institution, local cancellation penalty, NPC schedule, lab rule, region, quest or relationship consequence.
