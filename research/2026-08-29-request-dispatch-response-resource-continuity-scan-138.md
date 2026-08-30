# Ouros Narrative Research — Request, Dispatch & Response Resource Continuity — Pass 138

Status: RESEARCH ONLY / PROVENANCE. Not established Ouros canon.
Date: 2026-08-29

## Purpose

This pass investigates a narrow continuity gap between an observed need and the people or teams that eventually act on it.

The repository already contains strong owners for crises, communications, professions/staffing, missions, emergency medical transport, courier work, infrastructure incidents and many domain-specific response systems. What is missing is a neutral continuity model for the operational chain that can sit between those owners:

request or report received → intake recorded → information clarified → priority/scope decided by an authorized owner → resource requested → resource assigned → assignment acknowledged → resource departs → resource arrives/checks in → task state changes → resource clears → resource becomes available again.

The goal is not to create a universal emergency service, police dispatch system, Ranger organization, job board, radio network or command hierarchy for Ouros. Those are canon questions. The goal is to preserve chronology, provenance, assignment state and handoffs when a canon institution already has reason to dispatch a resource.

## Existing-project boundary review

The full recursive narrative repository tree was inspected before selecting this topic and was not truncated.

Directly adjacent material reviewed:

- `design/crisis-rescue-recovery-layer.md`
- `design/communications-network-relay-service-continuity-extension.md`
- `design/workplaces-professions-staffing-layer.md`
- `design/mission-dungeon-grammar.md`
- `design/emergency-medical-transport-referral-continuity-extension.md`
- `design/community-aid-volunteer-coordination-extension.md`
- `design/service-access-queues-appointments-extension.md`
- `design/courier-parcel-last-mile-logistics-extension.md`
- `design/case-authority-custody-layer.md`
- `design/world-agency-layer.md`
- `research/2026-08-18-source-scan.md`
- `design/engine-readiness-snapshot-pass-137.md`

Important ownership boundaries found:

1. Crisis owns crisis truth, impacts, unresolved needs, response phases and recovery.
2. Communications owns networks, relay paths and whether a communications service is available. Media/Communications owns whether a particular message was sent, delivered or acknowledged.
3. Staffing owns occupations, shifts, role capacity, work assignments and backlogs at a workplace.
4. Mission Grammar owns how a mission is assembled and exposed to players.
5. Domain owners such as Emergency Medical Transport, Wildfire, Grid, Roads or Building Safety own the meaning of the incident and the domain-specific result.
6. No existing layer owns a generic operational record connecting one request to one or more resources through assignment, acknowledgement, arrival, release and renewed availability.

This pass therefore does not duplicate the crisis object or mission generator. It adds evidence for a proposed dispatch/response-resource continuity layer.

## Internal PTU / Caelo cross-check

The existing project source scan establishes that PTU supports sandbox, central-plot and character-focused campaign structures, while Caelo exposes distinct activity containers such as Job, Raid, Wild Encounter, Social and Gym.

That is sufficient to support mission-shaped institutional work as narrative content. It does not establish any universal mechanical rules for:

- emergency dispatch;
- call-taking;
- incident priority;
- response-time calculation;
- responder certification;
- command hierarchy;
- radio procedure;
- unit status codes;
- automatic mission acceptance;
- automatic success based on rank or profession;
- dispatch authority granted by a Trainer Class or Feature.

Workplace occupations remain narrative roles unless an exact PTU/Caelo rule grants a mechanical effect.

No new PTU combat mechanic is inferred in this pass.

## Public Pokémon research

### 1. Pokémon Mystery Dungeon — request surface and accepted-job state

Sources:

- Spike Chunsoft, Pokémon Mystery Dungeon rescue overview: https://www.spike-chunsoft.co.jp/pages/games/pokedun_i/rescue01.html
- Bulbapedia, Red/Blue Rescue Team introductory walkthrough: https://bulbapedia.bulbagarden.net/wiki/Appendix:Mystery_Dungeon_walkthrough/Intro
- Community Rescue/Dungeon Help Megathread #13: https://www.reddit.com/r/MysteryDungeon/comments/nh1rd4/

Observed structure:

Rescue work can arrive through more than one surface. Requests can be delivered to a mailbox or posted on a bulletin board. A request entering the available-job pool is still distinct from a job being accepted and activated for an outing. Multiple compatible jobs may be carried into one expedition.

Reusable lesson for Ouros:

`REQUEST_VISIBLE`, `REQUEST_ACCEPTED`, `ASSIGNMENT_ACTIVE` and `TEAM_DEPARTED` should remain separate facts.

A request can exist without any responder accepting it. A responder can accept a task but still be at base. Multiple tasks can share a travel leg without becoming one incident.

What is not imported:

- dungeon-floor formulas;
- rescue-rank thresholds;
- rewards;
- mailbox mechanics as a universal institution;
- one-team party-size rules;
- Wonder Mail/password systems;
- game-specific mission eligibility.

### 2. Pokémon Mystery Dungeon community rescue — minimum information and incomplete reports

Source:

- Rescue/Dungeon Help Megathread #13: https://www.reddit.com/r/MysteryDungeon/comments/nh1rd4/

The public rescue format asks requesters to include game/region, dungeon, floor and code, with optional notes. The useful design lesson is not those exact fields. It is that a request can require enough locator/context information to become actionable, and that missing or incompatible information can block assignment without making the request false.

Ouros transformation:

A response request can have an `information_state` such as `RECEIVED_INCOMPLETE`, `CLARIFICATION_REQUIRED`, `ACTIONABLE` or `SUPERSEDED`.

`REPORT_RECEIVED != LOCATION_CONFIRMED`.

`LOCATION_CONFIRMED != RESPONSE_REQUIRED`.

`RESPONSE_REQUIRED != RESOURCE_AVAILABLE`.

### 3. Pokémon Ranger — institutional mission work

Sources:

- Pokémon official page, Pokémon Ranger: Guardian Signs / Tracce di luce: https://www.pokemon.com/it/videogiochi/pokemon-ranger-tracce-di-luce
- Pokémon official page, Pokémon Ranger: Shadows of Almia / Sombras de Almia: https://www.pokemon.com/es/videojuegos-pokemon/pokemon-ranger-sombras-de-almia

Observed structure:

Pokémon Ranger fiction frames some protagonists as members of an organization whose work includes helping people and Pokémon in difficulty and carrying out assigned missions. Guardian Signs also presents continued contact with institutional support during missions.

Reusable lesson for Ouros:

Some quests can be assignments produced by an institution rather than requests personally handed to the player. Assignment provenance matters: who generated it, under which mandate, for what scope, and whether another unit already owns it.

What is not imported:

- Ranger Union canon;
- Capture Styler mechanics;
- Ranger ranks;
- Guardian Signs characters, villains or plots;
- species-specific traversal powers;
- universal Ranger jurisdiction.

### 4. Poké Jobs — posted work, selection and return

Source:

- Pokémon official Sword/Shield Poké Jobs page: https://swordshield.pokemon.com/fr-fr/gameplay/pokejobs/

Observed structure:

Businesses and universities can publish work requests through a shared interface. Pokémon are selected and sent away for a duration, then return after participating.

Reusable lesson for Ouros:

Work demand, candidate resource selection, departure and return can be persistent world-state events. A resource that is assigned away should not remain simultaneously available for unrelated duties unless an explicit rule permits it.

What is not imported:

- type compatibility as occupational competence;
- experience or EV rewards;
- job-duration formulas;
- Rotomi/PC infrastructure as universal Ouros technology;
- Box storage as a dispatch system.

## Public operational research

Operational sources are used only to extract state-machine and provenance patterns. No United States or Australian law, protocol, profession, terminology requirement or jurisdictional mandate is imported into Ouros canon.

### 5. FEMA / ICS resource check-in and assignment tracking

Sources:

- FEMA/EMI check-in process: https://emilms.fema.gov/is_0703b/groups/251.html
- FEMA ICS Form 211 public instructions: https://training.fema.gov/EMIWeb/IS/ICSResource/assets/ICS%20Forms/ICS%20Form%20211%2C%20Incident%20Check-In%20List%20%28v3.1%29.pdf
- USFA/FEMA NIMS managing resources: https://www.usfa.fema.gov/a-z/nims/managing-resources.html

Observed structure:

Resource accountability distinguishes assignment/order information from check-in at an incident. Records may preserve resource identity, home unit, departure point/time, travel method, incident assignment and check-in time. Resource management continues through deployment and demobilization.

Reusable lesson for Ouros:

`RESOURCE_ASSIGNED != RESOURCE_ARRIVED`.

`RESOURCE_ARRIVED != RESOURCE_CHECKED_IN` when a canon process requires check-in.

`TASK_COMPLETE != RESOURCE_AVAILABLE_FOR_NEW_ASSIGNMENT`.

A team may need travel, debrief, rest, equipment return, handoff or release before it becomes available again.

### 6. APCO — call taking and dispatch are different functions

Sources:

- APCO Emergency Communications Center awards role descriptions: https://www.apcointl.org/membership/awards-recognition/ecc-awards/
- APCO Emergency Medical Dispatch program overview: https://www.apcointl.org/training/emd-program/

Observed structure:

Public emergency-communications descriptions distinguish receiving calls, determining the nature/priority of a request, dispatching a response and monitoring/communicating with field responders.

Reusable lesson for Ouros:

One NPC or institution may perform several of these functions, but the data model should not collapse them. Request intake, assessment/triage, resource assignment and field status are separate event types.

What is not imported:

- 911;
- EMD guidecards;
- medical protocols;
- public-safety job titles;
- priority codes;
- response-time standards;
- radio procedure.

## High-level design lessons

### A. Requests are claims, not world truth

A caller, courier, sensor, NPC or board post can report that something happened. The request record preserves what was reported and by whom. The domain owner decides what becomes verified world state.

Example:

A report says “three Pokémon are trapped behind the old mill.” The intake record can preserve that wording. Crisis/Search or another owner may later verify two actors at a different location. Dispatch must not rewrite the original report to match later truth.

### B. Priority is a decision with provenance

If a canon institution prioritizes work, preserve who/what policy made the decision and the information available at that time.

A later escalation does not make the earlier priority record fraudulent or incompetent by default.

### C. Assignment is not acceptance

A coordinator may nominate or assign a team. The team may still need to acknowledge, accept, reject, time out or request reassignment depending on local procedure.

### D. Acceptance is not movement

A resource can accept a job while finishing another handoff, gathering equipment or waiting for a route.

### E. Arrival is not resolution

A team reaching a location does not prove the incident is understood, stabilized or complete.

### F. Resolution is domain-owned

Dispatch can know that a team reports “clear” or “task complete,” but the domain owner determines the authoritative result.

Examples:

- Grid decides whether a circuit is restored.
- Building Safety decides whether reentry is authorized.
- Crisis decides whether a missing-person search closes.
- Emergency Medical Transport decides transport/referral state.
- Road operations decide route status.

### G. Clear is not available

A resource may leave an incident but remain unavailable because it is returning, refitting, handing off evidence, resting, debriefing or awaiting another explicit release state.

### H. One incident can create several assignments

A single crisis need can dispatch different resources for different scopes. Conversely, one travelling team may carry several compatible assignments. The IDs should remain independent.

### I. Dispatch does not create authority

Sending an actor to a location does not grant legal, medical, scientific, custody, rescue, inspection or property authority that the actor did not already possess.

### J. Communications failure does not erase assignment history

If acknowledgement is delayed or a field unit becomes unreachable, preserve the last known state and timestamp. Do not silently infer arrival, abandonment or failure.

## Candidate reusable structures

### Request intake episode

Preserves source, timestamp, claims, location hints, affected actors, contact route, uncertainty and later clarifications.

### Dispatch decision

Links one actionable need to a requested resource type or specific resource, with scope, reason and provenance.

### Resource status timeline

Possible neutral states:

- AVAILABLE
- HELD_FOR_ASSIGNMENT
- ASSIGNED
- ACKNOWLEDGED
- PREPARING
- EN_ROUTE
- ARRIVED
- CHECKED_IN
- ENGAGED
- CLEARING
- RETURNING
- REFIT_OR_HANDOFF
- AVAILABLE_AGAIN
- OUT_OF_SERVICE
- UNKNOWN_CONTACT

These are design candidates, not canon vocabulary.

### Assignment closure

Possible distinctions:

- COMPLETED_REPORTED
- COMPLETED_CONFIRMED_BY_OWNER
- PARTIAL
- TRANSFERRED
- CANCELLED_BEFORE_DEPARTURE
- CANCELLED_EN_ROUTE
- NO_LONGER_REQUIRED
- UNABLE_TO_COMPLETE
- SUPERSEDED

Again, domain semantics remain elsewhere.

## Quest and adventure patterns

### The Team Was Assigned, but Never Left

A dispatch log shows assignment and acknowledgement. The world has treated the unit as “sent.” A later check reveals that a route closure prevented departure and a replacement request was never linked correctly.

Reusable tension: chronology and handoff failure without villainy.

### Three Calls, One Incident

Three reports describe smoke, a fallen line and frightened Pokémon using different landmarks. The task is to discover whether they are one incident, three incidents or a cascade.

Reusable tension: duplicate detection without prematurely merging evidence.

### The First Team Is Still on the Board

An older resource remains displayed as active after handing responsibility to a second team. The mystery is administrative continuity, not disappearance.

### The Request Arrived After the Problem Ended

Communications outage delays a request. A team is eventually assigned to a condition that has already changed. The mission becomes verification, welfare check or documentation rather than the original rescue.

### The Same Crew, Two Assignments

A travelling field team is carrying two compatible inspections. The first expands unexpectedly, forcing a decision about whether to transfer, delay or split the second assignment.

### The Unit Cleared, the Equipment Did Not

Personnel leave, but a borrowed asset remains at staging. Another department believes the entire resource package is available.

## Encounter-design implications

Dispatch continuity can generate tactical situations, but the dispatch model itself should remain outside BattleSpec.

Mechanically rich encounter candidates:

1. Response Team Withdrawal Corridor
2. Staging-Site Access Chokepoint
3. En-Route Assignment Diversion
4. Field Handoff Perimeter

Full variants may depend on:

- complete movement including Intercept and forced movement;
- full turn/round lifecycle for staged withdrawal or arrival windows;
- terrain/weather/hazards/zones/reactions for protected lanes, unstable access or active hazard boundaries;
- AI tactical policy for PROTECT, WITHDRAW, CLEAR_ROUTE, HOLD_POSITION or escort-aware behavior;
- semantic Minecraft/Cobblemon/Craftics playback for resource status and handoffs.

Reduced variants can remain viable by resolving dispatch and civilian/resource movement first, removing noncombatants and controlled equipment from BattleSpec, then running a conventional static encounter with explicit Ouros-selected combatants.

## Copyright / transformation boundary

This pass does not copy protected dialogue, characters, plots, mission text or distinctive encounter sequences from Pokémon Ranger, Mystery Dungeon, Sword/Shield or community rescue posts.

Only high-level operational structures are retained:

- request surfaces;
- acceptance state;
- institutional assignment;
- dispatch provenance;
- resource status;
- arrival/check-in;
- closure and renewed availability.

## Research conclusion

The strongest reusable pattern across Pokémon mission structures and public operational systems is that a “quest” has an operational life before and after the player-facing objective.

Ouros can become more coherent by preserving that life explicitly. A job can wait for clarification, be accepted but not yet departed, be transferred between teams, arrive after conditions change, close only for one owner, or leave a responder temporarily unavailable afterward.

This continuity creates story without inventing extra villains or tactical mechanics, and it makes institutional NPCs behave like actors in a persistent world rather than quest dispensers.