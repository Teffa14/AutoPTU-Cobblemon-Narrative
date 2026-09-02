# Service Request, Queue, Appointment & Capacity Scan — Pass 198

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02
Canon effect: NONE. This file records external structures and project cross-checks. It does not establish Ouros facts.

## Research question

How can Ouros represent ordinary demand for limited local services — requests, work orders, appointments, held slots, triage, pauses, rescheduling, no-shows, completion evidence and backlog — without turning a quest journal into institutional truth, inventing regional bureaucracy, or letting Narrative resolve PTU-governed services?

## Repository-first duplicate check

Before external research, the current Narrative repository was inspected through its recursive tree, canon directory and exact code/content search.

Canon reviewed:

- `canon/README.md`
- `canon/marea-interior-map-resident-network-v2.md`
- `canon/npc-pokemon-dynamic-progression-v1.md`
- `canon/ouros-playable-foundation-v1.md`
- `canon/questline-taxonomy-v2.md`

Adjacent design reviewed or searched:

- temporary visitor / lodging capacity;
- rest, planned waiting, actor availability and duty handoff;
- correspondence / courier continuity;
- supervised practice / competency;
- public exhibition / challenge-contract continuity;
- provisioning / custody / repair-adjacent material;
- community education;
- seasonal ecology / route windows;
- language / interpretation;
- current engine-readiness snapshots.

Exact repository search for `appointment`, `queue`, `waitlist`, `booking`, `work order`, `service request`, `double booked`, `no-show`, and `reschedule` returned no dedicated continuity layer.

### Existing boundaries that must remain intact

The visitor layer already knows that `ROOM_HELD != ROOM_OCCUPIED` and that capacity can be reserved or released. This pass must not duplicate temporary-presence or lodging authority.

The rest/duty layer already knows actor availability and planned waiting. This pass can reference availability and expose `wait until service window`, but must not own sleep, duty schedules or world-time progression.

Correspondence can carry a request. Receipt of a message must not itself create completed service.

Competency controls whether a person may perform a task within an established scope. A queue assignment cannot grant competence.

Provisioning/custody controls materials and possession. Reserving material for a work order cannot silently transfer ownership or consume the item.

Battle Yard challenge/exhibition architecture controls competition semantics. A practice booking cannot create a rank, contest result or rival relationship.

## Canon anchors already available in Marea

Current canon establishes enough ordinary service activity to use this layer without adding an institution:

- Lia Morn assigns berths, records arrivals/departures and coordinates unloading windows at the ferry landing.
- Teo Lark maintains ordinary equipment, lamps, carts and field instruments; exact mechanical crafting transactions require PTU validation.
- Oren Vale handles routine Trainer/Pokémon care within verified mechanics and local care administration.
- Taro Min runs Tideglass opening hours and scheduled interviews.
- Pia Min performs circulation, copies, deliveries and source retrieval.
- Nerea Sol and Ema Rey maintain observation/equipment workflows at Mirador.
- Sela Orrin and Jace Orrin operate training sessions, audited battles and ordinary Battle Yard maintenance.
- Ivo Serrat coordinates purchasing and supplier activity.
- Puerto Bruma is canonically a coastal service hub.

This pass may connect demand to those established responsibilities. It must not invent prices, licensing, room counts, staffing ratios, regional labor law or a universal first-come-first-served policy.

## Public source 1 — Poké Jobs

Source: Bulbapedia, `Poké Job`.
URL: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9_Job
Accessed: 2026-09-02.

Observed high-level structure:

- job requests exist as discrete listings;
- a listing can specify what kind or amount of help is wanted;
- Pokémon can be assigned for one of several durations;
- assigned actors are unavailable for ordinary use until return;
- early cancellation produces a different result from normal completion;
- completion can have graded outcomes;
- some listings differ in recurring availability from ordinary jobs.

Reusable Ouros lesson:

A work request should exist independently from the actor assigned to it. Assignment, duration, cancellation, return and result are separate state transitions. The system can preserve what was requested even when the eventual worker, timing or outcome changes.

Do not import:

- Poké Job reward tables;
- EV/XP output;
- job tiers;
- type-matching success calculations;
- exact durations;
- Rotomi infrastructure;
- Pokémon being treated as generic labor resources.

## Public source 2 — Pokémon Legends: Arceus requests

Sources:

- Bulbapedia, `Task (Legends: Arceus)`.
  https://bulbapedia.bulbagarden.net/wiki/Request
- Bulbapedia, `Walkthrough: Pokémon Legends: Arceus/Requests 1-30`.
  https://bulbapedia.bulbagarden.net/wiki/Appendix:Legends:_Arceus_walkthrough/Requests_1-30

Accessed: 2026-09-02.

Observed high-level structure:

- a request has a named requestor and objectives;
- requests can have prerequisites before they become available;
- multiple tasks can exist at the same time;
- a tracked request is not necessarily the only active request;
- some objectives explicitly require reporting back after field work;
- completion can unlock a change in a local service or world facility.

Reusable Ouros lesson:

Submission/acceptance, active work, objective evidence and report-back should remain separate. A service actor can receive a request before the work is feasible. Field evidence can exist before the requester learns the result. A request can be valid without being the currently tracked focus.

Do not import:

- Arc Phone markers;
- request numbering;
- rewards;
- exact objectives or NPCs;
- instant service unlock logic.

## Public source 3 — Pokémon Ranger quests

Source: Bulbapedia, `Ranger Quest`.
URL: https://bulbapedia.bulbagarden.net/wiki/Ranger_Quest
Accessed: 2026-09-02.

Observed high-level structure:

- citizens can present optional problems to an established service role;
- these requests exist separately from main missions;
- requests can be resolved when the Ranger is available rather than collapsing all demand into the main plot;
- recurring research-request structures can appear in different places at different times.

Reusable Ouros lesson:

A public-facing field-service institution can accumulate ordinary requests without every request becoming an emergency or a main quest. The player can assist with one case while other cases remain owned by local actors.

Do not import:

- Ranger authority;
- capture mechanics;
- quest rewards;
- Almia institutions;
- the assumption that every citizen request belongs to Marea Field Office.

## Public source 4 — PTU 1.05 Tutors and other services

Sources:

- Pokémon Tabletop United 1.05 Core, services guidance, mirrored via AnyFlip.
  https://anyflip.com/gqibw/ifqm/basic/451-500
- Pokémon Tabletop forum Q&A reproducing the relevant `Tutors and other services` section.
  https://www.tapatalk.com/groups/pokemon_tabletop/general-questions-and-answer-1-05-t5996-s1930.html

Accessed: 2026-09-02.

Mechanically relevant structure:

PTU explicitly treats several Class-Feature-derived activities as services that may be available through NPCs, including specialist/generalist tutoring and breeder/chef examples. Availability is setting-dependent. A service provider's capability matters; the setting should not assume every location supplies every service.

Critical Ouros boundary:

Narrative may record that someone asked for a PTU-governed service, that a provider accepted it, or that a scheduled interaction occurred. Narrative must not invent the mechanical result.

Examples:

- a Move Tutor appointment does not teach a Move until authoritative PTU/Caelo/AutoPTU validation executes the procedure;
- a care appointment does not heal HP/status/Injuries merely because its narrative state becomes `COMPLETED`;
- a crafting/repair request does not create a mechanically defined Item unless the relevant rule path validates it;
- an appointment with someone whose class concept includes Mentor does not grant Mentor Features or Tutor Points.

This is especially important because Marea canon already names class concepts while declaring exact mechanical sheets subject to authoritative validation.

## Public source 5 — PTU community downtime experiments

Source: Reddit r/PokemonTabletop, `Downtime support` (2020).
URL: https://www.reddit.com/r/PokemonTabletop/comments/ideygf
Accessed: 2026-09-02.

Community signal only. Not rules authority.

The discussion includes campaign-specific schedulers/day planners, bounded activity slots and limits on repeating activities. It demonstrates a recurring GM problem: when characters have many possible activities, time and capacity become meaningful even without combat.

Reusable lesson:

Ouros can benefit from visible scheduling conflicts and opportunity cost, but it should derive those from real actor/resource availability rather than add a universal `downtime points` currency.

Do not import:

- burnout;
- social capital;
- weekly point budgets;
- skill bonuses;
- school-calendar assumptions.

## Design synthesis

The strongest reusable model is a four-part separation:

1. demand exists;
2. an authority acknowledges/triages it;
3. capacity is allocated and work occurs;
4. evidence of the result returns to the requester/world.

A request can stop, change or branch at every boundary.

This produces stories without manufacturing crises:

- a legitimate request waits because the only qualified provider is busy;
- a slot is held while required material is still in transit;
- a higher-priority incident interrupts a routine appointment while preserving its place/history;
- a requester fails to arrive, but the request remains open pending contact;
- two visible schedule revisions cause a double booking;
- work finishes while the player is elsewhere and leaves an inspectable result;
- the wrong desk receives a valid request and reroutes it without pretending the request was submitted later;
- a mechanical service is performed only after the governing rules engine confirms the legal result.

## Narrative consequences worth preserving

### Delay has provenance

A delayed service should know why it is delayed when evidence exists:

- provider unavailable;
- material missing;
- requester unavailable;
- dependency incomplete;
- emergency interruption;
- weather/transport effect;
- conflicting booking;
- authority review pending;
- unknown.

`DELAYED` should not automatically imply negligence.

### Priority must be attributable

Never invent a universal first-come-first-served or emergency policy for Caelo.

Store:

- claimed urgency;
- who evaluated it;
- what evidence was considered;
- the resulting local scheduling decision;
- policy/version if one exists.

This permits inconsistent or changing local practice without silently declaring regional law.

### Service completion must be evidenced

A work-order record can say a provider closed the work. Other systems can separately preserve:

- the repaired/returned object;
- mechanical engine result;
- requester acknowledgment;
- inspection result;
- later failure/correction.

`WORK_ORDER_CLOSED != RESULT_PERFECT`.

### Off-screen work is legitimate

Canon residents exist and have ordinary responsibilities without the player. If prerequisites and clocks are satisfied, bounded service state can advance while the player is elsewhere. It must not invent a battle, discovery, death, relationship change or mechanical effect that lacks a governing resolver.

## Minecraft/Cobblemon implications

Visible queues, signs, NPC lines and interaction menus are projections.

Do not infer:

- clicking an NPC = accepted request;
- standing in a line = authoritative queue position;
- player disconnect = no-show;
- NPC entity unload = provider left duty;
- moving a sign = schedule revision;
- chest contents = reserved/consumed materials;
- battle-yard occupancy = authorized session;
- a healing animation = PTU care resolution.

The server-side Narrative record remains authority for the service lifecycle, while PTU/AutoPTU remains authority for mechanical outcomes.

## Caelo/source uncertainty

Literal `Caelo` search in Narrative, AutoPTU-Java and AutoPTU returned no indexed results during this pass.

Unresolved:

- regional appointment norms;
- queue etiquette;
- legal priority classes;
- service licensing;
- consumer/payment law;
- cancellation penalties;
- standard opening hours;
- professional credential rules;
- public-health triage rules;
- formal ferry reservation rules;
- whether any service category has mandatory response times.

Do not promote any of those assumptions through this research file.

## Candidate Ouros direction

Create one shared service-request continuity layer that can be referenced by existing institutions without turning them into one bureaucracy.

The layer should own lifecycle/provenance only. Each service domain retains its own authority:

- transport owns actual ferry movement;
- hosting owns occupancy;
- custody/provisioning owns material state;
- competency owns performer scope;
- Tideglass owns archive access/review;
- Mirador owns research review;
- Battle Yard owns sanctioned competitive/session context;
- PTU/Caelo/AutoPTU owns mechanical services and battle outcomes;
- Narrative owns who requested what, when, how it was routed, what capacity was allocated, and what evidence came back.

Recommended first implementation slice: `Two Repairs, One Bench` at Teo's repair row. It tests finite capacity, explicit ordering and off-screen completion without requiring a battle, economy, PTU crafting rule or new institution.