# Commercial Services, Storefront Continuity & Local Exchange Scan — Pass 57

Status: external research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-26

## Why this pass

The repository already has strong layers for material culture, supply routes, workshops, food/hospitality, finance, staffing, settlement state, temporary public events and residential life. The remaining gap is the persistent public-facing service node: a shop, counter, studio, repair desk, market stall or small service business that players revisit and that changes because suppliers, staff, clientele and local conditions change.

This pass therefore does not add a general economy simulator. It studies how recurring commercial places can become narrative infrastructure.

## Repository overlap review

The full repository tree was inspected before writing. Relevant existing boundaries:

- `design/material-culture-economy-crafting-layer.md` owns item provenance, workshops, supply routes, commissions and coarse market state.
- `design/workplaces-professions-staffing-layer.md` owns staff roles, shifts, coverage, training and service continuity.
- `design/food-agriculture-hospitality-layer.md` owns food venues, menus, agriculture and hospitality service.
- `design/finance-sponsorship-risk-layer.md` owns finance/risk relationships rather than storefront simulation.
- `design/temporary-public-event-operations-extension.md` owns temporary vendors and event overlays.
- `design/observation-settlement-time-layer.md` owns settlement-level capability and time.
- `design/residential-life-household-relocation-layer.md` owns stable household occupancy, not commercial premises.

The new material should therefore act as an orchestration extension between these systems rather than replacing them.

## Source 1 — Pokémon Legends: Arceus request chain for General Store expansion

Source: Bulbapedia, “Task (Legends: Arceus)” and request listings.
https://bulbapedia.bulbagarden.net/wiki/Task_(Legends:_Arceus)

Relevant pattern:

The General Store does not expand because the player reaches a generic level threshold. Several requests repeatedly return to the same shopkeeper and the same upstream supplier relationship. The player mediates a persistent blocker between the shop and Supply Corps; completion changes the store’s future offerings. The same commercial node is revisited multiple times as the settlement develops.

Reusable high-level lessons:

1. A service upgrade is more legible when it has an upstream dependency with a named actor.
2. A recurring supplier dispute can create several small callbacks instead of one disposable fetch quest.
3. The public-facing result is persistent and visible: the shop later offers more stock.
4. The player can influence commercial availability without owning the business.
5. Progress can be staged. One intervention need not permanently solve every future supply problem.

Do not copy the Choy/Tao Hua relationship, requested materials, dialogue or stock lists into Ouros.

## Source 2 — Pokémon Legends: Arceus Request 23 walkthrough

Source: Bulbapedia, “Appendix: Legends: Arceus walkthrough/Requests 1-30.”
https://bulbapedia.bulbagarden.net/wiki/Appendix:Legends:_Arceus_walkthrough/Requests_1-30

Useful detail:

The request reveals that a commercial shortage can actually be a relationship and logistics problem rather than a literal absence of all goods. The shopkeeper has customers and a functioning counter, but expansion is blocked by access to supply. The intervention produces a concrete storefront state change.

Reusable pattern:

`customer-facing limitation -> discover upstream cause -> negotiate/resolve dependency -> persistent service change -> later callback`

For Ouros this can support repair shops, outfitters, pharmacies, studios, ferry kiosks, specialty food counters, craft suppliers or other approved service types without inventing prices or mechanical item effects.

## Source 3 — Pokémon Legends: Arceus broader request catalogue

Source: Bulbapedia, Task catalogue.
https://bulbapedia.bulbagarden.net/wiki/Task_(Legends:_Arceus)

The same settlement uses side requests to make several businesses visibly change: the clothier gains new options after inspiration requests, the photography studio gains new options after investigation/identification requests, and the general store expands repeatedly.

Reusable lesson:

A settlement can communicate player impact through changing service surfaces rather than only through major construction. Small businesses become persistent “memory displays” for earlier play.

This suggests a low-cost Minecraft representation pattern: signage, counters, displayed goods, available interaction menus, employee positions and cosmetic props can change after authoritative narrative state updates.

## Source 4 — Public PTU campaign log with commercial starting space and craft aspiration

Source: Giant in the Playground, “Pokémon Tabletop United (PTU) Campaign Log” archive.
https://forums.giantitp.com/archive/index.php/t-527075.html

Relevant high-level patterns from the public log:

- the campaign begins beside a Poké-convenience store rather than in a battle arena or dungeon;
- a player character has prior employment at a Pokémon Center;
- that character travels seeking a known craft specialist because they want to develop a Poké Ball crafting career;
- the disappearance of the expected town/specialist converts an occupational goal into a world mystery.

Reusable lessons:

1. Commercial and professional spaces are useful adventure anchors because players already have reasons to visit them.
2. Career goals can point naturally toward settlements, specialists and supply networks.
3. A missing or changed service node can reveal a larger world event.
4. A shop need not be a menu. It can be a place where social history, career aspiration and plot intersect.

Do not reuse the campaign’s characters, missing-town plot or distinctive backstory.

## Source 5 — PTU system framing

Source: Giant in the Playground, original PTU public description.
https://forums.giantitp.com/showsinglepost.php?p=17012904&postcount=1

PTU explicitly supports campaign forms beyond a standard League journey and has Trainer classes reflecting different specializations/jobs. That reinforces the project’s existing rule that occupations and businesses can be meaningful campaign structures, while mechanical class/feature legality remains governed by PTU/Caelo rather than narrative labels.

## Synthesized structures for Ouros

### A. Storefront as persistent world-state surface

A commercial location should expose changes that happened elsewhere:

`supply route -> stock/service availability -> customer behavior -> staffing pressure -> visible storefront state`

The storefront does not calculate the whole economy. It displays consequences already justified by world state.

### B. Service relationship triangle

Useful recurring triangle:

`provider <-> supplier/institution <-> customer/community`

Conflict can occur on any edge. The player may help without becoming owner, employee or regulator.

### C. Revisit ladder

A recurring business can support a four-step arc:

1. first visit establishes baseline service and operator;
2. limitation reveals dependency;
3. intervention changes a visible service state;
4. later visit tests whether the change held, evolved or created a new pressure.

### D. Commercial memory

Persistent commercial change can remember:

- which supplier relationship was restored;
- which employee trained into a role;
- which service was added or removed;
- which shortage occurred;
- which community event increased demand;
- which repair or relocation changed the premises;
- which player action caused the transition.

This is narrative memory, not reputation math.

### E. Customer cohorts instead of simulating every shopper

Use aggregated cohorts such as commuters, tournament visitors, local households or field workers. Only materialize individual customers when a witness, rival, specialist, recurring regular or other actor becomes narratively relevant.

### F. Service substitution

When one provider becomes unavailable, the world should check for:

- reduced service;
- a different local provider;
- temporary coverage;
- nearby settlement access;
- institutional distribution;
- delayed fulfillment;
- player commission/trade routes.

A single absent merchant should not arbitrarily freeze the world.

## Risks to avoid

- Do not generate volatile numerical prices without an approved economy rule.
- Do not treat every shortage as a fetch quest.
- Do not infer ownership, debt, contracts, monopoly, licensing or illegal trade.
- Do not invent PTU item stock, crafting access or mechanical service effects.
- Do not turn every employee into a permanent NPC.
- Do not create random closures only to force player travel.
- Do not let Minecraft-side shop scripts decide authoritative item legality or battle outcomes.

## Candidate implementation value

This layer is useful now because most of it is noncombat state. Storefront availability, staff presence, supply dependency, visual changes and recurring customers can exist before the full Minecraft battle adapter is ready.

Battle dependencies only arise when a commercial incident becomes tactical, such as a warehouse containment event or a delivery-route ambush. Those concepts need explicit capability contracts and reduced versions.

## Provenance boundary

All structures above are transformed abstractions. No source dialogue, distinctive character, exact quest chain, stock list or plot is proposed for Ouros. Names and examples in future proposals remain `PROPOSED / NON-CANON` until reviewed.