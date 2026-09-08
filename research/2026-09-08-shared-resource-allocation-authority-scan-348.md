# Shared resource allocation authority scan — Pass 348

Status: RESEARCH / PROVENANCE ONLY. NOT CANON.
Date: 2026-09-08

## Existing-repository check

This pass follows the global resource chain implemented in Passes 338–347. It does not replace:

- Pass 201 identity/credential/delegated-authority continuity;
- Pass 202 mutual-aid allocation records;
- Pass 339 resource reservations;
- Pass 343 handoff custody;
- Pass 346 successor handoff authorization;
- Pass 347 reschedule resource-window admission.

The missing seam is narrower: when Pass 347 proves that two unrelated active commitments overlap on one indivisible resource, Ouros needs to preserve who had authority to choose a course and why. The planner must not manufacture a universal priority score.

## New public sources

### American University — Space Use & Scheduling Priorities

Source: https://www.american.edu/student-affairs/mgsc/space-use-scheduling-priorities.cfm

Reusable structure:
- shared resources can have explicit scheduling priorities tied to approved use and time context;
- an institution may reassign, modify or cancel reservations under defined policy;
- priority is policy-bounded rather than an intrinsic property of the person asking.

Ouros transformation:
A scarce-resource conflict may be resolved by a scoped decision actor using a named policy or evidence basis. The decision must preserve the policy reference and decision provenance. No global `importance` score is inferred.

### McGill University Facility for Electron Microscopy Research — Facility Policy

Source: https://www.mcgill.ca/femr/node/609

Reusable structure:
- reservations remain required;
- facility staff have priority access to instruments/equipment;
- training and access authority remain separately governed.

Ouros transformation:
One institution may legitimately define a narrow priority rule for one resource family. That local rule must never become a universal Ouros law or a PTU mechanic.

### Duke Shared Materials Instrumentation Facility — Reservations

Source: https://smif.pratt.duke.edu/access-training/reservations

Reusable structure:
- reservation and actual usage are distinct records;
- qualified access is required before equipment use;
- no-show/cancellation state can matter without erasing reservation history.

Ouros transformation:
An allocation decision selects a course among competing commitments. It does not prove checkout, custody transfer, current technical readiness or actual usage.

### Pokémon Mystery Dungeon — Kangaskhan Storage

Source: https://bulbapedia.bulbagarden.net/wiki/Kangaskhan_Rock

Reusable structure only:
- carried inventory and stored inventory are different operational states;
- mission rewards may be routed to storage when carried capacity is unavailable.

Ouros transformation:
Institutional storage can remain physically real while access/allocation decisions determine who may operationally obtain a scarce unit. No Mystery Dungeon inventory limits, failure penalties, characters or progression rules are imported.

### Pokémon World Tour: United — public PTU actual-play listing

Source: https://podcasts.apple.com/us/podcast/pokemon-world-tour-united/id1154176782

The public listing confirms a long-running Pokémon Tabletop United actual play with a 2026 end-game arc and season-level continuity. This source is used only as structural evidence that sustained PTU campaigns can carry obligations and consequences across many sessions. No characters, dialogue, plots or setting facts are imported.

## PTU / Caelo boundary

The current narrative repository already establishes that a `WorldResource` may represent ordinary equipment without becoming a mechanical PTU Item. If the selected resource later maps to a PTU Item, exact source/content identity and exact Java implementation evidence remain required before battle mechanics rely on it.

Authority over scheduling also does not grant Trainer Features, Skills, Edges, Item effects, battle initiative authority or tactical control.

## Reusable design lessons

1. Conflict detection and conflict resolution should stay separate.
2. A decision actor needs scoped authority evidence for the exact resource/action.
3. The conflict set available at decision time must remain queryable.
4. Selecting one commitment does not silently cancel the others.
5. A decision basis should reference policy/evidence rather than a hidden scalar priority.
6. Authority can expire or require re-verification.
7. Local institutional policy does not become universal world law.
8. A resource allocation result does not move custody or prove actual use.

## Candidate narrative pressure

A field office and a maintenance crew both hold legitimate commitments on the same instrument. The allocator has authority over that instrument family but must choose using current evidence. One task has a narrow environmental sampling window; the other is part of preventative maintenance that will itself reduce future failure risk. Either choice has a cost. The interesting play comes from evidence, timing, alternatives and later consequences rather than a morality meter.

Current disposition: reusable for a global allocation-resolution provenance seam. Canon effect: NONE.
