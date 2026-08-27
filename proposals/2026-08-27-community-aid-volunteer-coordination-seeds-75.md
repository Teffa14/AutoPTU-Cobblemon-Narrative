# Community Aid & Volunteer Coordination Seeds — Pass 75

Status: PROPOSED / NON-CANON. These are original Ouros candidates for later review.

All concepts below depend on the design boundary in `design/community-aid-volunteer-coordination-extension.md`. They do not establish named organizations, laws, compensation rules, civic-service requirements or universal cultural expectations.

## The Rota With One Missing Hour

A public support desk has enough people signed up for the day, but one hour remains uncovered in the actual check-in record.

Possible explanations:

- two actors thought they had swapped windows but only one side recorded the change;
- an offer was mistaken for a confirmed commitment;
- the helper arrived at a different staging point;
- an organizer reassigned the actor to another role without completing the handoff;
- the actor validly withdrew and the replacement call never reached the board.

The scene is solved through commitments, timestamps, communications and handoffs. It should not default to accusing someone of irresponsibility.

## Too Many Hands at the Wrong Site

A widely shared aid notice brings more helpers than one location can safely use, while another nearby need remains thinly covered.

The meaningful decision is allocation, not combat. The coordinating institution can redirect volunteers only within roles and locations that are actually open. Some helpers may decline the alternate task.

Persistent consequence: later calls may use clearer location-specific role slots or capacity caps.

## The Specialist Who Can Only Stay Twenty Minutes

A qualified actor can cover a specialist role for a short window, while several ordinary helpers are available for much longer.

The project must decide whether to:

- postpone the specialist-dependent step;
- use the short window for assessment and leave execution for later;
- split preparation from specialist verification;
- redirect ordinary helpers to tasks that do not require that qualification.

The specialist's brief presence does not transfer their authority or competence to the rest of the group.

## The Cleanup That Outlasts the Festival

A temporary public event ends on time, but teardown and cleanup continue into the next morning.

Possible state changes:

- some event volunteers leave when their commitment ends;
- a smaller cleanup call opens;
- Waste/Public Space retains areas as limited until inspection;
- routine park users return to unaffected zones;
- one storage or transport dependency delays final ordinary return.

The event can be over while its physical consequences remain playable.

## The Help Call That Gets Withdrawn

Residents respond strongly to a public request, but the owner system later determines that the task should not proceed in its original form.

Examples:

- Maintenance discovers the area needs specialist assessment first;
- Conservation changes the access window after a nesting observation;
- the event organizer changes the layout;
- a recipient no longer wants public assistance;
- the problem is resolved by another route.

Withdrawing the call is a world-state update, not a failure. Helpers already en route need a communication/handoff event rather than silently despawning.

## The Same Three People Every Storm

Across several weather disruptions, the same three community actors repeatedly show up for ordinary support roles.

The system may remember that pattern and let NPCs recognize it. It must not infer that those actors are obligated to appear again, secretly resentful, morally superior or members of a formal organization.

A later story hook can arise when one of them simply does not offer this time and the neighborhood has to discover whether its support process depended too heavily on recurring individuals.

## The Tool Table Has Helpers, Not Operators

A community repair day has plenty of people carrying materials and organizing the site. A specialized piece of equipment arrives, but nobody present has verified authority to operate it.

Correct outcomes may include:

- wait for the credentialed operator;
- continue with preparation work;
- return or secure the equipment;
- reschedule the mechanical step;
- ask the owning workplace for coverage.

The narrative must not let a high Skill roll or enthusiasm invent legal/technical eligibility.

## Lunch for the Night Shift

A neighborhood wants to support a professional night crew without interfering with the technical operation.

The contribution is routed through an approved food staging point. Food/Hospitality owns preparation and batch state; Workplaces owns the crew; Aid owns only the helper commitment and delivery window.

This seed demonstrates meaningful participation that never places volunteers inside the worksite.

## The Neighbor Who Helps Once, Then Says No

An NPC helped during an earlier project. A new request resembles the old one, and other characters assume they will participate again.

The NPC declines.

The scene should treat the answer as sufficient unless the character chooses to explain more. Previous cooperation remains true. The refusal does not erase that history or create tension automatically.

This is a useful boundary test for player/NPC agency and for avoiding hidden obligation mechanics.

## A Camp Opens, Then Needs a Rota

A field camp is successfully established by its owning institution. The opening solves the original access problem but creates ordinary recurring needs: public information hours, supply-table coverage, visitor orientation, observation logging or seasonal stewardship.

A community-support rota may emerge around those narrow tasks while professional operation stays with the institution.

The long-term hook is that opening infrastructure creates continuity rather than ending content.

## The Help That Arrives in Kind

A support call asks for people, but several residents instead offer useful goods, transport or prepared food.

Those offers route to the relevant specialist systems for acceptance. The aid coordinator records who offered what and whether the receiving system accepted it. Nothing is usable merely because it was donated.

This can create a gentle logistics scene when the real bottleneck is storage, transport, dietary requirements, equipment compatibility or timing.

## The Shift Handoff Nobody Heard

A helper correctly records several observations during a trail-watch window. The next cohort starts on time, but the verbal handoff happens at the wrong meeting point.

The information exists but does not teleport.

The players can reconstruct where the handoff failed and decide whether the observations need to be resent, reverified or escalated. No misconduct is required.

## A District Learns How to Help

Long-form recurring arc.

Visit 1: a small ordinary call establishes where people sign up and which tasks accept public help.

Visit 2: a larger need exposes that offers and confirmed commitments were being mixed together.

Visit 3: a specialist requirement forces clearer role boundaries and credential checks.

Visit 4: a helper withdrawal creates a successful handoff rather than a crisis.

Visit 5: the district uses a revised process with fewer coordination failures and less need to materialize every participant individually.

Persistent changes can include a staging table, clearer role cards, a different notice format, remembered availability patterns and better links to specialist institutions.

There is no hidden community-level stat. Improvement is visible in records and world objects.

## Six Sign-Ups, Four Actual Helpers

Noncombat mystery.

A coordinator sees six names on an old signup surface but only four people appear in the contribution history.

Possible facts:

- one entry was an offer that never became a commitment;
- one helper transferred to a different role under another need ID;
- one record is duplicated after a spelling correction;
- one actor withdrew before the start;
- a check-in occurred at another site;
- records are incomplete.

The investigation uses stable IDs, commitments, check-ins, handoffs and notices. It does not require fraud or blame.

## Volunteer Staging-Site Evacuation

Mechanically rich encounter candidate.

Narrative premise:

A legitimate support site must close because a nearby threat makes the area unsafe. Community helpers are not responders. The key narrative success is that the aid process pauses cleanly and everyone leaves through the authorized route while professional actors take over.

Intended full version:

- helpers physically withdraw through multiple exits;
- protected supply zones remain noncombat objectives;
- responder and threat movement can interact with exit lanes;
- dynamic unsafe areas may change route choice;
- AI understands WITHDRAW/PROTECT/CLEAR_ROUTE rather than only KO;
- adapter/playback preserves exact positions, closures and aid commitment state.

Dependency map:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if the unsafe area is tactical;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Reduced executable version:

The coordinator closes the site before combat. Helpers, ordinary supplies and recipients leave through world state. Commitments become PAUSED, RELEASED or HANDED_OFF. A conventional static battle then resolves in the cleared perimeter. The specialist owner decides reopening afterward. Winning the battle does not restore the rota automatically.

## Community Cleanup Wildlife Conflict

Mechanically rich encounter candidate.

Narrative premise:

A routine cleanup overlaps with a wild Pokémon group's current use of part of a shared public space. The initial goal is withdrawal and reassessment, not punishment.

Intended full version:

- helper cohorts move toward exits;
- collected materials remain protected world objects;
- temporary access boundaries matter;
- wild AI can prefer territory/withdrawal instead of KO;
- de-escalation can end the tactical scene;
- later Public Space/Ecology state records which area/timing should change.

Reduced executable version:

Helpers and collected materials leave the grid first. Ecology/Public Space evaluates whether the cleanup can move, pause or resume. Only if a battle remains necessary does AutoPTU resolve a conventional static encounter. Victory cannot establish that the Pokémon caused earlier litter, damage or conflict.

## Supply Table Interruption

Mechanically rich logistics candidate.

A table distributing already-approved supplies is interrupted by a local threat. The full version would require civilian withdrawal, protected-object semantics, possible interception and objective-aware AI.

Reduced version:

Distribution stops; recipients/helpers and exact supply batches leave tactical state. Custody stays with the owner system. AutoPTU resolves the local threat separately. Distribution resumes only if the owning service still considers the site usable.

## Rota Reconciliation

Fully executable without combat.

Inputs:

- aid need ID;
- role slots;
- helper offers;
- availability windows;
- role reviews;
- confirmed commitments;
- check-in events;
- handoffs;
- withdrawals/cancellations;
- communications.

Outputs:

- corrected coverage view;
- identified record dependency or gap;
- new helper call if still needed;
- no forced accusation or social consequence.

## Canon review questions

- Which Ouros settlements or institutions would actually use public helper calls?
- Are recurring mutual-support groups culturally common anywhere?
- Which tasks are culturally seen as ordinary neighbor help versus institutional work?
- What roles require credentials or supervision?
- Can helpers receive meals, transport, reimbursement or equipment, and under what system?
- What participation data is public?
- How are aid recipients protected from unwanted publicity?
- Which Pokémon participation practices are normal and individually consent-compatible?
- Does any region have traditions of civic service that need separate authored treatment?

No answer is assumed here.