# Commercial Services & Storefront Continuity Seeds — Pass 57

Status: PROPOSED / NON-CANON. These are original Ouros candidates derived from high-level research patterns. Nothing here is canon-approved.

## Design goal

Create recurring customer-facing places that remember supply, staffing, service changes and player interventions. Avoid turning ordinary shopping into grind or inventing unsupported PTU economy rules.

## Seed 1 — The Counter That Keeps Closing Early

A small approved service counter has begun entering LIMITED state several afternoons each week.

Initial public explanation: “staffing issue.”

Possible hidden causes, all requiring authored evidence rather than random selection:

- the trained specialist is covering another workplace;
- one supply delivery now arrives later because a route changed;
- the operator is spending time on a recurring institutional handoff;
- equipment or facility maintenance reduces available hours;
- a temporary event is drawing staff away.

Player choices:

- trace the real dependency;
- help coordinate temporary coverage;
- accept a reduced-service model;
- redirect customers to another provider;
- leave the issue alone.

Persistent outputs:

- changed public hours notice;
- new coverage actor;
- service substitution link;
- follow-up staffing/training hook;
- later callback if the temporary fix fails.

No salary, contract or labor-law assumptions are created.

## Seed 2 — The Shelf Everyone Notices

One visible category of approved goods or supplies keeps entering LIMITED availability.

The point is not to collect arbitrary resources. The player investigates the chain:

`storefront -> delivery record -> route/supplier state -> actual blocker`

Possible consequences:

- an alternate supplier becomes available;
- special orders replace normal stock temporarily;
- another settlement becomes the fallback service source;
- public expectations change;
- the shortage reveals a larger ecological, transport or institutional problem.

If exact purchasable items matter, they must come from authoritative PTU/Caelo/AutoPTU data.

## Seed 3 — The Regular Who Stops Coming

A service node has one recurring customer who has become narratively materialized through repeated observed visits. They abruptly stop appearing.

This does not automatically mean danger.

Possible authored causes:

- changed work schedule;
- relocation;
- transport disruption;
- temporary care responsibility;
- the needed service moved elsewhere;
- unresolved conflict at the service node;
- ordinary choice with no dramatic explanation.

The hook works because the commercial place provides a stable observation surface for change in another actor’s routine.

## Seed 4 — Special Order, Wrong Delivery

A named customer or institution expects an authored special order. The delivery arrives with a provenance mismatch, wrong destination tag or incomplete handoff.

Gameplay focus:

- compare records;
- inspect chain-of-custody-like transfer history without treating ordinary goods as criminal evidence;
- identify where the handoff diverged;
- decide whether to reroute, hold, return or escalate through the correct existing system.

This can become a case only if actual evidence/authority state supports that transition.

## Seed 5 — The Successor at the Front Counter

A long-running operator is transitioning out of daily customer-facing work. A trainee or successor begins handling the public counter.

The player can observe continuity through:

- changed schedule;
- different service confidence/availability;
- old customers asking for the previous operator;
- the trainee escalating unusual requests;
- institutional knowledge being handed off;
- small visual changes in the premises.

The storyline should not assume retirement, inheritance or ownership transfer unless canon explicitly establishes those facts.

## Seed 6 — Two Days in a Temporary Room

A repair, flood, public works project or other authored problem forces a service node to operate temporarily from another existing location.

Interesting consequences:

- different foot traffic;
- worse supplier access but better customer access;
- shared space with another workplace;
- reduced services;
- different neighboring NPC interactions;
- a later decision about whether to return.

This should reuse existing locations when possible.

## Seed 7 — Tournament Week Without a New Shop

A recurring battle event causes a demand pulse at existing local services.

Instead of spawning disposable “event merchants,” the world first checks:

- which permanent service nodes extend hours;
- which temporary service overlays are justified;
- whether staffing is available;
- which approved stock/services become constrained;
- which customer cohorts appear;
- whether public notices redirect demand.

The temporary-event layer owns the event. This extension owns how persistent commercial nodes react and what they remember afterward.

## Seed 8 — The Supplier Will Talk, Just Not Here

A provider says a supplier relationship is blocked. The supplier is willing to explain their position but does not want the discussion handled at the public storefront.

This creates a small social/information investigation without assuming wrongdoing.

Possible source conflict:

- service quality disagreement;
- timing mismatch;
- missing paperwork in an already-authored institutional process;
- concern about a route or facility;
- incorrect public framing of the problem;
- a private family/social issue only if separately established.

The player may facilitate communication. They do not gain authority over either party.

## Seed 9 — Reopening Morning

A service node has been CLOSED or RESTORING because of an earlier authored event. The reopening is a callback scene.

Possible player-facing details:

- repaired interior;
- altered counter layout;
- limited service for the first day;
- staff who were temporarily reassigned returning;
- regular customers reappearing;
- a new supplier notice;
- a memorial or public-memory artifact if the closure was significant.

Reopening should be a visible consequence, not automatically a quest.

## Recurring arc — A Street Learns Its Services

This arc uses several commercial nodes on one existing street/district without creating a new settlement.

Phase 1: Baseline

Players learn a few recurring operators and what services are normally available.

Phase 2: Shared pressure

One world event produces different effects across the nodes. A route delay affects stock, a staffing reassignment changes hours, and visitor pressure increases queues.

Phase 3: Adaptation

Businesses use substitution, coverage, special-order or limited-service states rather than all failing identically.

Phase 4: Persistence

After the pressure ends, some changes revert and some remain. One trainee keeps a larger role. One supplier route stays altered. One customer cohort shifts.

Phase 5: Callback

A later unrelated quest uses the changed street state as background evidence that the world remembers prior events.

## Mystery structure — Four Receipts, Three Stories

A routine commercial inconsistency is noticed across several service nodes. Each operator remembers a delivery window differently. Public notices and delivery records partially conflict.

The investigation should separate:

- actual delivery events;
- operator memory;
- public posted hours;
- route logs;
- customer observations;
- canonical truth.

Possible resolutions include simple scheduling drift, communication failure, a recurring transport delay or a more serious case only if evidence supports it.

No NPC is labeled dishonest merely because accounts conflict.

## Encounter concept — Backroom Containment

Narrative premise:

A disrupted delivery coincides with a Pokémon becoming trapped or panicked in a storage/backroom area. The public floor is closed and evacuated.

Intended full version:

- narrow aisles and access points matter;
- fragile or movable storage creates spatial pressure;
- knockback/forced movement can matter;
- environmental hazards or blocked zones may change;
- the Pokémon may prioritize escape rather than KO;
- AI should understand containment/withdrawal;
- Minecraft should show the actual storefront state.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:

Evacuate customers and staff first. Freeze the map before tactical resolution. Do not simulate destructible stock, moving crates, dynamic hazards or containment AI. Run a static legal battle with only combatants. The authoritative result sets the storefront to CLOSED, LIMITED, RESTORING or OPERATING as appropriate.

## Encounter concept — Delivery Route Interruption

Narrative premise:

A scheduled delivery is blocked by a Pokémon encounter or route incident. If unresolved, an existing service node will enter LIMITED state.

Intended full version:

- route-specific terrain/weather may matter;
- escort/withdrawal goals may matter;
- forced movement or hazards may matter;
- AI may need non-KO priorities;
- Minecraft playback should preserve delivery actors and route state.

Reduced version:

Record the blocked delivery narratively. If battle is necessary, run a static encounter at a fixed legal arena. After authoritative resolution, update delivery and storefront state. Do not implement escort rules or weather/terrain effects in Minecraft unless AutoPTU verifies them.

## Noncombat concept — Supplier Relationship Review

A recurring service limitation can be investigated without combat.

Inputs:

- current service availability;
- supplier/route state;
- public notices;
- delivery events;
- staffing commitments;
- information packets;
- existing institutional records.

Outputs:

- confirmed blocker;
- corrected public explanation;
- alternate supply/service path;
- mediated contact;
- unresolved follow-up;
- no change if the player chooses not to intervene.

## Canon questions left open

- Which settlements have persistent commercial streets or clusters?
- Which specific service types are canonically common?
- What ownership/operator models exist in Ouros?
- Are leases, licenses, taxes, commercial permits or business registrations modeled at all?
- Which institutions supply ordinary goods?
- How are prices sourced and surfaced when PTU/Caelo do not fully define a local economy?
- Which service changes are feasible to render in Cobblemon without excessive NPC simulation?
- How many regular customers should become persistent named actors?
- Which commercial services are appropriate for player employment or ownership, if any?

None of these questions are answered by this proposal.