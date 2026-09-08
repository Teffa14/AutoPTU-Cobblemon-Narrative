# Allocation decision restart provenance scan — Pass 365

Status: RESEARCH / PROVENANCE ONLY. NOT CANON.
Date: 2026-09-08

## Repository-first check

The recursive repository inventory and Passes 339–364 were inspected before writing. Pass 347 owns historical conflict admission. Pass 348 already owns the authorized institutional choice. Pass 349 separately owns application/displacement. Pass 364 places conflict admission inside the coherent world checkpoint. The uncovered durability seam is therefore the Pass 348 choice itself: after restart, Ouros must be able to prove who decided, under what scoped authority, which conflict set was visible, and which course was selected without inferring that history from the later reservation state.

No canon file is changed by this pass.

## New public sources

### Clemson University — Light Imaging Facility policies

Source: https://www.clemson.edu/centers-institutes/light-imaging/use-the-facility/policies.html

The facility uses explicit scheduling and states that facility management has final authority over priority access when conflicts arise. Useful abstraction: scarcity can require a scoped decision owner; the existence of competing bookings and the authority to resolve them are separate facts.

Ouros transformation: preserve the authority check and the decision as provenance. Do not import Clemson policy, priority criteria, access sanctions or institutional terminology as Ouros canon.

### Pokémon HGSS: Sevii Islands fan project

Source: https://eeveeexpo.com/hgss-sevii-islands/

The public project description separates main chapters and a large set of quests and records a quest-log distinction between main and side quests. Its changelog also documents fixes for story events firing at the wrong time.

Ouros transformation: secondary obligations can stay durable while the player follows another route, and event timing/progression should remain explicit rather than reconstructed from downstream world state. No characters, plot, locations, dialogue or custom mechanics are copied.

### Dunsparce & Drampa public Pokémon actual-play feed

Source: https://www.podash.com/podcast/4105317/

The public feed describes a continuing Pokémon tabletop actual play with travel between locations, ongoing adventures and a lore-filled region. It uses a homebrew Pokémon tabletop system, not PTU.

Ouros transformation: persistent regional travel can carry unresolved professional or logistical obligations between episodes. This source is narrative inspiration only and has zero PTU mechanical authority.

## PTU / Caelo boundary

Project authority remains the internal PTU Core, Pokédex, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List already indexed by the repository. Pass 365 creates persistence architecture only. It does not establish a PTU rule, Caelo fact, Move, Ability, Item, Trainer Feature or universal allocation policy.

## Design extraction

A resource conflict has at least three durable moments: the conflict that was observed, the authorized choice made from that evidence, and the later operational application. Keeping these moments separate allows NPCs to challenge an old choice after conditions change without rewriting the evidence that existed at decision time.

Useful Ouros hooks include a field team appealing an allocation, a scheduler defending a past choice from contemporaneous evidence, a later cancellation making the old decision look unnecessary, and procurement reform emerging only after repeated source-backed conflicts.

## Pass 365 implementation consequence

`OUROS_NPC_RESOURCE_CHECKPOINT_V7` persists Pass 348 authority evidence and resolution history on top of V6 admissions. Restore requires a matching historical conflict record and current-at-decision scoped authority. V1–V6 restore an empty allocation history. Later Pass 349 application must remain a separate owner.
