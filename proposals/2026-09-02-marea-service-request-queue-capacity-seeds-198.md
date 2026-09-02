# Marea Service Request, Queue & Capacity Seeds — Pass 198

Status: PROPOSED / NON-CANON
Date: 2026-09-02
Depends on: `design/service-request-queue-appointment-capacity-continuity-layer.md`
Canon effect: NONE until reviewed and promoted.

## Intent

Use already-canon Marea residents, workplaces and responsibilities to create stories about finite attention, scheduling, dependencies and service continuity.

No seed below establishes regional queue law, prices, licensing, compensation, staffing ratios, exact room/bench counts or universal opening hours.

## Seed 1 — Two Repairs, One Bench

Primary actors: Teo Lark, player optional.
Location: repair row, Puerto Bruma.
Questline surfaces: EQUIPMENT, ITEM, CHARACTER, SETTLEMENT.

Two ordinary repair requests are already accepted. One work surface is currently occupied by the first job being handled; this does not assert that Repair Row owns only one bench in total.

The second request is older or newer according to its actual intake record, but local order is not automatically decided by timestamp. One job may be blocked on a missing mundane part while the other is ready.

Player actions can include delivering an already-tracked part, asking Teo what is actually blocking each request, returning later, or doing nothing.

Possible persistent outcomes:

- blocked request remains open with reason preserved;
- ready request proceeds;
- one job completes while the player is elsewhere;
- repaired object waits separately for pickup/return;
- a later correction reopens the work order without erasing the original closure.

Do not create a crafting roll, Item upgrade, monetary fee or mechanical equipment bonus.

Recommended first implementation slice.

## Seed 2 — The Loading Window That Moved

Primary actors: Lia Morn, Mina Cors, Brin Havel or Ivo Serrat as linked evidence owners.
Location: ferry landing.
Questline surfaces: SETTLEMENT, REGION, ITEM, SERVER_EVENT.

A previously expected loading window changes after a known transport or dispatch dependency changes. Lia records the revision. An older copy of the schedule remains visible somewhere for a short period.

The story question is whether the affected parties receive the revision and adjust their own work.

Important boundaries:

- old schedule copy remains historical evidence;
- a held window does not prove the cargo arrived;
- a ferry movement record remains separate from the request to use that window;
- no external destination, fare or ticket rule is invented.

## Seed 3 — Mirador Review Window

Primary actors: Ema Rey, Dr. Nerea Sol.
Location: Estación Mirador.
Questline surfaces: CHARACTER, FACTION, RESEARCH-adjacent through existing families, SETTLEMENT.

Ema has completed a legitimate field-note packet. A review request exists, but Nerea is currently committed to another authored responsibility.

The packet can be acknowledged before it is substantively reviewed.

The player can see the distinction between:

- note prepared;
- review requested;
- review scheduled;
- review performed;
- conclusion revised or left uncertain.

No amount of waiting makes the evidence automatically correct.

## Seed 4 — Tideglass Copy Request With One Missing Source

Primary actors: Pia Min, Taro Min.
Location: Tideglass Archive branch.
Questline surfaces: ITEM, FACTION, CHARACTER, SETTLEMENT.

A visitor or resident asks for copies of several records. Pia can prepare the material that is within her scope, but one source is currently unavailable, under review or requires Taro's authority.

A request can therefore become partially ready without becoming globally complete.

The final packet preserves which source was omitted, delayed or later appended.

Do not turn a copy request into automatic access to protected material.

## Seed 5 — Battle Yard Double-Booked Drill

Primary actors: Sela Orrin, Jace Orrin, two existing or future legitimate session participants.
Location: Bruma Battle Yard.
Questline surfaces: COMPETITIVE, CHARACTER, RELATIONSHIP, SETTLEMENT.

A schedule revision was recorded correctly in the authoritative system, but one old physical copy remained visible. Two parties arrive expecting the same window.

Neither needs to be lying or careless.

Possible narrative responses:

- preserve one session and reschedule the other;
- run sessions sequentially;
- use one period for observation or discussion;
- voluntarily agree to a narrower audited battle arrangement.

The double booking itself never grants rival status, ranking, compensation or special priority.

See the design file for full/reduced battle dependency handling.

## Seed 6 — A Real Interruption, a Routine Request

Primary actors: Mara Veyra and an existing service owner appropriate to the chosen case.
Location: Puerto Bruma.
Questline surfaces: SETTLEMENT, FACTION, CHARACTER.

A bounded routine request is already scheduled when a separate, verified field issue needs immediate attention from the same actor or resource.

The routine request becomes delayed with provenance rather than disappearing.

After the interruption, the institution must decide whether the old slot resumes, moves or becomes a new appointment revision.

Do not invent a universal emergency priority rule. The local decision must be attributed to the actor/procedure used in the episode.

## Seed 7 — Wrong Desk, Same Submission

Primary actors: Pia Min and Lia Morn, or another pair whose existing duties plausibly cross.
Location: Puerto Bruma service hub.
Questline surfaces: SECONDARY, SETTLEMENT, CHARACTER.

A legitimate request reaches the wrong local contact because the sender misunderstood which role owns the service.

The receiving actor recognizes the mismatch and routes it correctly.

The original submission timestamp and message provenance remain intact. The requester does not lose history because the request was redirected.

The episode teaches routing without creating a centralized municipal ticket office.

## Seed 8 — The Part Arrived After the Slot

Primary actors: Teo Lark, Ema Rey or another existing equipment owner.
Location: repair row / Mirador linkage.
Questline surfaces: EQUIPMENT, ITEM, CHARACTER.

A repair appointment reaches its window before the required part or instrument arrives in custody.

The appointment cannot honestly become `COMPLETED`.

Later, the material arrives. A new work window can be assigned while preserving the failed dependency history.

The player may carry the item only if custody and courier systems authorize it.

## Seed 9 — A Request Completes While You Are Away

Primary actor: one canon resident performing an ordinary already-authorized duty.
Location: any established workplace.
Questline surfaces: SETTLEMENT, CHARACTER.

The player leaves Marea or follows another evidence lane while a bounded mundane service remains active.

When the player returns, the world has advanced:

- the work order can be closed;
- the object or document may be ready;
- the service owner may have left a note or handed responsibility onward;
- no relationship reward is applied merely because the player was absent.

This seed demonstrates autonomous local competence.

## Seed 10 — The Request That Was Ready but Not Reviewed

Primary actors: Ema Rey and Nerea Sol, or Pia Min and Taro Min.
Location: Mirador or Tideglass.
Questline surfaces: CHARACTER, FACTION, ITEM.

All preparatory work is complete. The only remaining dependency is a named review authority.

The system must preserve `READY_FOR_REVIEW` separately from `APPROVED` or `VALIDATED`.

If the reviewer later disagrees, the preparation was still real work and remains in history.

## Seed 11 — Courtesy Does Not Rewrite Priority

Primary actors: player plus a resident with an existing positive relationship.
Location: an established service point.
Questline surfaces: RELATIONSHIP, SETTLEMENT.

A resident who knows the player well can explain the current wait, offer another legitimate window or suggest another solution.

The relationship does not silently move the player ahead of unrelated requests.

If a specific resident chooses to make an exception in a future authored scene, record the decision and consequence directly rather than creating a generic `friendship priority` mechanic.

## Seed 12 — One Resource, Two Institutions

Primary actors: Teo Lark, Ema Rey, Jace Orrin or another canon combination.
Location: Puerto Bruma / Mirador linkage.
Questline surfaces: EQUIPMENT, SETTLEMENT, FACTION.

One already-established portable tool or piece of equipment is needed by two planned tasks during overlapping windows.

The conflict is about resource scheduling, not ownership.

Possible outcomes:

- one task moves;
- another uses an alternative method already established by evidence;
- the tool is transferred through custody records;
- both tasks remain open until capacity exists.

Do not invent a duplicate item to make the scheduling problem vanish.

## Seed 13 — The Board and the Ledger Disagree

Primary actors: Lia, Pia, Brin or Sela/Jace depending on chosen institution.
Location: existing public-facing workspace.
Questline surfaces: ITEM, SETTLEMENT, FACTION.

A public board shows an older service order than the authoritative current record.

The player can discover when each version was issued and who actually received the update.

The useful outcome is not choosing a culprit. It is restoring a single current projection while preserving the stale copy as provenance.

This seed combines the service layer with the version/revision architecture already present elsewhere in Narrative.

## Long arc — The Work That Keeps Marea Moving

Status: PROPOSED ARC CONCEPT.

Across several ordinary episodes, the player sees the same institutions handle demand without becoming omniscient or frictionless.

Early state:

- requests are mostly verbal or scattered among existing local records;
- residents rely heavily on individual memory and handoff;
- conflicts remain small and recoverable.

Middle state:

- repeated pressure exposes which information needs explicit request IDs, dependencies or schedule revisions;
- Teo, Lia, Tideglass, Mirador and the Battle Yard each retain their own local practices;
- improved continuity does not mean one regional bureaucracy replaces them.

Later state:

- old requests can be traced;
- deferred work survives handoffs;
- visitors and repeat residents encounter a town whose services remember prior interactions;
- a new disruption can test whether those practices actually help.

No global efficiency meter is required. Growth is visible through fewer lost dependencies, clearer revisions, physical boards/notes, resident dialogue and persistent records.

## Rich encounter candidate — Battle Yard Double-Booked Drill

Full intended version can become mechanically rich only if the chosen authored solution includes a controlled multi-party tactical drill.

Narrative premise remains scheduling conflict and correction.

Required capability families if the full battle uses them:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement: PARTIAL, content-gated;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when selected content requires it;
- terrain/weather/hazards/zones/reactions: BLOCKING if safety zones/reactions become mechanical;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for objective-aware drill behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for full projection/return.

Reduced version keeps the scheduling conflict intact and resolves any combat as one separately audited ordinary BattleSpec at a time. Spectators, appointment histories, stale schedule evidence and the rescheduling decision remain outside combat.

## PTU/Caelo boundary for all seeds

A service record never grants a Move, Feature, Edge, Skill Rank, Tutor Point, XP, level, mechanical Item effect or battle result.

PTU/Caelo/AutoPTU remains authoritative for those outcomes.

Literal `Caelo` search in the three project repositories returned no indexed result during pass 198. Queue rules, professional standards, cancellation doctrine and other regional service law remain unresolved.

## Promotion recommendation

Promote no new canon in this pass.

Prototype `Two Repairs, One Bench` against existing Teo/repair-row canon first. If the record model works, reuse it for Mirador review, ferry windows and Battle Yard scheduling before considering any broader regional policy.