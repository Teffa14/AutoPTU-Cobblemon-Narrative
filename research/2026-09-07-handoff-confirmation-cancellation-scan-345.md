# Handoff confirmation, cancellation and stale-arrival research — Pass 345

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-07

## Repository gap checked before research

The recursive main-branch tree was inventoried before authoring. Relevant owners were then opened or searched directly.

Pass 344 explicitly defers communication-aware appointment confirmation and cancellation. The existing Service Reservation / Ticket / Pass / Admission extension already assigns delivery of confirmations, cancellations and change notices to Communications. Pass 283–287 already own information queues, communication channels, durable delivery state and delivery-triggered replanning.

Therefore this pass must not create a parallel notification transport. It may record the semantic relationship between a handoff authorization and a communication event, while delivery truth remains owned by the existing information runtime.

## New public sources

### Appointment reminders and actual receipt

Source: Teo et al., Psychiatric Services, 2017, “No-Show Rates When Phone Appointment Reminders Are Not Directly Delivered”.
https://psychiatryonline.org/doi/abs/10.1176/appi.ps.201700128

Observed high-level structure: attendance differed substantially depending on whether the reminder reached a person directly, became a message/voicemail, or received no answer. The reusable lesson is not the healthcare outcome itself. It is that sending a notice and the intended participant actually receiving it are different operational facts.

Ouros transformation: a cancellation or confirmation may be authored while another participant remains legitimately unaware. The communication queue, not dialogue text or planner omniscience, determines whether the receiver can act on it.

### Reminder systems can create useful cancellations and rescheduling

Source: McLean et al., Patient Preference and Adherence, systematic review / realist synthesis of appointment reminders.
https://www.tandfonline.com/doi/full/10.2147/PPA.S93046

Observed high-level structure: direct reminder contact can prompt cancellation or rescheduling early enough for the service to reallocate the slot. The useful abstraction is that a reminder is an opportunity for a state-changing response, not merely a cosmetic notification.

Ouros transformation: pre-handoff contact can produce CONFIRM, CANCEL or RESCHEDULE_REQUEST. These remain semantic events tied to the existing authorization. They do not themselves move the resource or rewrite custody.

### Time-indexed NPC commitments as game structure

Source: Zelda's Palace, Bombers' Notebook reference for The Legend of Zelda: Majora's Mask.
https://www.zeldaspalace.com/majorasmask/notebook.php

Source: Zelda Wiki, Bombers' Notebook reference.
https://zelda.fandom.com/wiki/Bombers%27_Notebook

Observed high-level structure: NPC availability and promises are attached to explicit time windows, and the player can use schedule information to understand when interactions can occur. Repository search before authoring found no previous Majora's Mask source use.

Ouros transformation: preserve appointments as time-indexed world facts with stable identity. Do not copy the three-day loop, characters, quest sequence, notebook text or distinctive plot. Ouros uses ordinary semantic time and persistent NPC state.

## PTU and Caelo boundary

The repository README identifies PTU Core, Pokédex material and supplied Caelo material as the mechanical authority boundary when exact PTU rules are invoked.

This pass introduces no PTU Skill DC, Trainer Feature, Item effect, Move effect, Ability effect, combat communication action, hearing range or timing rule. Confirmation and cancellation are world-agent logistics semantics only.

Public tabletop campaigns and actual plays remain narrative inspiration only. No public campaign is allowed to establish PTU mechanics merely because it says it uses PTU.

## Reusable design lessons

1. Authored notice and received notice need separate evidence.
2. A sender knows what they authored; the intended receiver learns it only after a real delivery event.
3. Cancellation may be true operationally while another actor still travels on stale information.
4. Reschedule request needs its own state. It should not be silently treated as cancellation or confirmation.
5. Bilateral confirmation needs evidence in both directions when the authored process requires it.
6. Communications owns transport and receipt. Appointment coordination consumes that evidence.
7. A failed or queued message cannot update another NPC's knowledge.
8. A Minecraft subtitle, proximity event or animation cannot fabricate communication receipt.

## Original Ouros opportunities

A resource pickup can fail even though the provider responsibly sent a cancellation. The receiver may already be travelling beyond reliable contact coverage. When they arrive, the world can preserve all of the following at once: the provider cancelled, the message was queued or delayed, the traveller did not receive it, the traveller arrived in good faith, and no custody transfer occurred.

That structure supports later relationship repair, route planning, communication infrastructure upgrades and institutional process changes without requiring a villain or an arbitrary misunderstanding.
