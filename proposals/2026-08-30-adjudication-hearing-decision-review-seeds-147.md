# Adjudication, Hearing, Decision & Review Seeds — Pass 147

Status: PROPOSED / NON-CANON. These are original Ouros candidates. They do not establish any institution, legal system, right, offense, penalty, deadline or universal review process until separately approved.

Date: 2026-08-30

## Design goal

Use formal decisions as durable world events with provenance, delay, disagreement and downstream consequences. The interesting play comes from understanding what was actually decided, what record was available, what later review changed and whether implementation caught up.

## Local quest seeds

### The Decision Was Issued, the Gate Stayed Closed

A canon-approved conservation body grants access to a field team. The access record is valid, but the physical gate remains closed because the site custodian never received the implementation notice.

Player work can involve finding the communication break, reaching the custodian and resolving immediate route danger. A battle can clear the approach. It cannot itself open the authorization state.

### The Hearing That Never Happened

Everyone in town remembers a contentious hearing. The archive shows only a scheduled date, a cancellation notice and a later record-only decision. Several NPCs sincerely remember attending a public meeting held on the same day.

The mystery is archival and social rather than criminal by default. The correct resolution may be that two events became one in public memory.

### The Result Stands, the Conduct Question Does Not

A sanctioned battle result is authoritative and remains in the circuit record. A separate institution-specific review examines conduct around the event without rerunning the battle or changing HP/status history.

This creates a clean distinction between `BATTLE_RESULT_CONFIRMED` and `CONDUCT_REVIEW_OPEN`.

### The Review Was Accepted, So Everyone Assumed a Reversal

A local eligibility decision enters review. Rumor converts `REVIEW_OPENED` into “the decision was overturned.” Storekeepers, rivals and organizers react to different versions of the story.

Players may trace the information chain while the original decision remains effective unless a separate stay or replacement decision exists.

### The Notice Reached the Old Address

A club or guild sends a hearing notice using a previously valid address. Courier provenance proves delivery to that address. Organization-lineage records show the group had moved. The institution must decide what that means under its own canon procedure.

The quest does not invent a universal rule for valid notice.

### Two Panels, One Matter

Two bodies appear to have issued incompatible decisions. Investigation reveals that one decided event eligibility while the other decided facility access. Both records can be internally correct because their scopes differ.

### The Decision With No Implementation Owner

A newly restructured institution issues a valid decision requiring a world-state change, but the office that once performed the change was dissolved during an organizational transition.

The conflict is about institutional continuity and responsibility. The decision history stays intact while Civic Office and Organization Lineage determine who can act now.

### The Record Closed Before the Missing Page Arrived

A document arrives after the decision record closes. It is genuine and relevant, but whether it can be considered depends on the institution's canon review path. Players can establish provenance without deciding procedural effect themselves.

### The Old Decision on the Wall

A public notice board still displays an earlier decision after a superseding one was issued. Both documents are authentic. The problem is stale publication state, not forged authority.

### The Winner Everyone Remembers Differently

A festival contest has an official result, an audience favorite and a later media retrospective that names another performance as the event's defining moment. All three can coexist without corrupting the formal record.

## Mysteries

### Five Times the Matter Was “Decided”

Five witnesses use the word “decided” for five different events:

- staff accepted the filing;
- a panel closed the record;
- the decision was signed;
- the decision became effective;
- implementation finished.

The investigation teaches the player the system through provenance rather than exposition.

### Three Dates on One Decision

The archive contains a signature date, publication date and effective date. A later summary uses only one. The player must determine which date matters for the specific question being asked.

### The Appeal That Was Only a Request for Permission

Public memory says an appeal failed. The actual record shows that permission to proceed was refused and no substantive review occurred. Ouros preserves that distinction without importing a real-world legal consequence.

### The Decision Nobody Can Find

Multiple downstream systems reference a decision ID, but the public copy is absent. Possible explanations include privacy, archival migration, identifier change, an incomplete handoff or a mistaken historical citation. Conspiracy is only one hypothesis among several.

### The Reversal That Changed Nothing Physical

A later decision changes the recognized institutional outcome, but the building, route or service had already been restored for independent reasons. NPCs disagree over whether the review “mattered.” The simulation can answer institutional and physical questions separately.

## Recurring NPC archetypes

### The Procedure Clerk

Knows where a matter is in the process and distinguishes received, accepted, scheduled, issued and effective. This NPC is useful because competence is mundane rather than mystical.

### The Traveling Event Judge

Works across several sanctioned competitions with different local rule sets. The character knows how to state parameters and record outcomes but does not possess universal authority outside assigned events.

### The Archive Reader

Studies historical decisions and notices patterns across decades. Their interpretations can be insightful, wrong or disputed. They never gain automatic access to private records.

### The Implementation Coordinator

Rarely makes decisions. Their work begins after a decision becomes actionable: update access lists, contact site staff, schedule physical changes, synchronize records. They expose the gap between institutional outcome and lived reality.

### The Persistent Challenger

Uses every review path the relevant institution actually permits. They may be principled, obsessive, strategic or simply careful. Repeated challenges are not proof of bad faith.

## Faction and organization hooks

A mature faction may care more about procedural precedent, public legitimacy or implementation than about winning a fight. Rival organizations may share the same decision body because neither trusts the other to adjudicate its own disputes. A splinter group may inherit members and symbols while a separate decision process determines access to an old facility. A coalition may create a temporary panel for one event without becoming a permanent government.

All such structures remain PROPOSED until the relevant organizations and mandates are canon-approved.

## Long arc: A District Learns What a Decision Means

Phase 1 establishes ordinary decisions that usually happen off-screen: event eligibility, limited facility access, route permissions, small grant-like allocations or club recognition.

Phase 2 introduces a disputed decision where the record is incomplete but no villain is evident. Different actors use “appeal,” “hearing” and “overturned” imprecisely.

Phase 3 reveals a legitimate review path. The player can gather missing provenance, interview participants and protect access to records. The review may affirm, amend, reverse or remand according to future canon procedure; the arc does not preselect the answer.

Phase 4 separates institutional result from implementation. Even after a new decision exists, signage, schedules, credentials and physical access may update at different speeds through their owning systems.

Phase 5 leaves durable history. Months later NPCs remember different turning points. The archive preserves every decision version. A public summary may simplify the story. The district now has institutional memory without the world pretending that everyone agrees.

## Encounter concepts

### Hearing Hall Withdrawal Perimeter

Narrative premise: a hearing or formal meeting is suspended because a hostile physical threat reaches the building. Participants need a safe withdrawal route.

Full version may involve civilians moving on timed phases, interception, forced displacement, reactive exits, dynamic safe zones and coordinated enemy tactics.

Reduced version: READY. The hearing is paused before initiative. All adjudicators, participants, records and neutral actors leave BattleSpec. Static hall/exterior geometry remains. Explicit combatants only. Success emits `IMMEDIATE_HEARING_HALL_WITHDRAWAL_ROUTE_CLEAR`. Ouros later decides whether and when the proceeding resumes.

### Decision Archive Handoff Chokepoint

Narrative premise: a verified copy of a decision record must physically move between archive locations during a local threat.

Full version may require escort-adjacent movement, carried-object semantics, reactions, forced movement and tactical AI.

Reduced version: READY. The decision record is removed from tactical state and secured before combat. AutoPTU resolves only control of the static approach. Success emits `IMMEDIATE_DECISION_ARCHIVE_HANDOFF_APPROACH_CLEAR`. Custody transfer occurs afterward through the proper world systems.

### Compliance Inspection Access Corridor

Narrative premise: an implementation team needs safe access to inspect whether a previously ordered physical change occurred.

Full version may include escort, hazards, dynamic access zones, reactions and timed rounds.

Reduced version: READY. Inspectors remain outside BattleSpec. The target facility and semantic inspection objects are static/noninteractive. Combat success emits only `IMMEDIATE_IMPLEMENTATION_INSPECTION_APPROACH_CLEAR`. It never asserts `COMPLIANCE_CONFIRMED` or `IMPLEMENTATION_COMPLETE`.

### Tournament Protest Perimeter

Narrative premise: after an authoritative AutoPTU battle result, a separate protest or review process draws a physical disturbance outside the venue.

Full version may include crowd boundaries, dynamic zones, reactions, timed evacuation and tactical AI.

Reduced version: READY. The protest process and all records are frozen outside tactical state. Battle resolves only immediate safety. It cannot alter the match result or review outcome.

## Battle outcome guardrail

No encounter in this file may emit any of the following directly:

- `MATTER_ACCEPTED`
- `HEARING_VALID`
- `DECISION_ISSUED`
- `DECISION_EFFECTIVE`
- `DECISION_AFFIRMED`
- `DECISION_REVERSED`
- `MATTER_REMANDED`
- `NOTICE_VALID`
- `ELIGIBILITY_CONFIRMED`
- `CREDENTIAL_SUSPENDED`
- `COMPLIANCE_CONFIRMED`
- `LIABILITY_ESTABLISHED`
- `GUILT_ESTABLISHED`
- `AUTHORITY_TRANSFERRED`

AutoPTU may author the battle facts it owns. Ouros consumes those facts later through the correct institutional owner.

## Canon questions raised by these seeds

Which Ouros institutions, if any, make reviewable decisions? Which decisions are final immediately? Which use panels, individual officials, automated scoring or record-only review? Does any League body hear protests about sanctioned events? Which communities prefer mediation over formal adjudication? What records are public? Which procedures survive organizational succession? What terminology does each region actually use?

Until answered, these remain worldbuilding candidates rather than established setting facts.