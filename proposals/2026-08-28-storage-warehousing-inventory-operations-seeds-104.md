# Storage, Warehousing & Inventory Operations Seeds — Pass 104

Status: NON-CANON PROPOSALS. Every name, institution, facility and event below requires later canon approval.
Research basis: `research/2026-08-28-storage-warehousing-inventory-operations-scan-104.md`.
Systems basis: `design/storage-warehousing-inventory-operations-continuity-extension.md`.

## Design intent

These seeds use storage as persistent world state rather than as a room full of loot. Most can resolve through observation, reconciliation, relationships and operational decisions. Combat is optional and must never decide ownership, inventory truth, quarantine disposition or custody by implication.

## The Shipment Was Accepted, Nothing Was Put Away

A delivery passed its formal acceptance review yesterday. The receiving area is still full because the intended zone became inaccessible before putaway started.

The visible shortage downstream is therefore real even though the goods are already inside the building.

Possible consequences:

- a shop remains in LIMITED stock state;
- a production run waits for an input that is physically nearby;
- staff create a temporary receiving layout;
- an old service corridor becomes important again.

No theft or incompetence is implied.

## The Empty Bay Is Reserved

Visitors see an empty bay while workers insist the depot has no usable room.

The bay may be reserved for an incoming batch, blocked by access restrictions, awaiting maintenance verification or attached to an external hold. The story comes from discovering the authored reason and deciding whether another arrangement is possible.

`visually empty` never becomes `available` automatically.

## The Store Is Out, the Warehouse Has Stock

A public storefront reports an item family unavailable. A warehouse observation confirms stock exists nearby.

Possible legitimate explanations include:

- stock has not been picked;
- a hold exists;
- transport has not been scheduled;
- the store's public assortment excludes that batch;
- a downstream acceptance step remains open;
- the record is older than the latest internal move.

The point is to connect systems without collapsing them into one inventory flag.

## The Quarantine Tape Moved, the Hold Did Not

A storage zone appears open after barriers or signage were shifted during maintenance. The linked Traceability record still says the batch is held.

Workers must reconcile presentation and authoritative state before anything moves.

This seed tests the Minecraft boundary directly: blocks and signs display state; they do not own it.

## The Returned Goods Never Re-entered Stock

Several items were legitimately returned to the facility. They have a receipt history and a physical location, but no verified putaway record.

They may be:

- waiting in a returns zone;
- held for inspection;
- staged for a different destination;
- recorded under an older aggregate label;
- still unresolved.

The investigation can end without a culprit.

## The Overflow Yard Outlived the Festival

A temporary outdoor storage site opened during an event-driven demand spike. Months later the main depot has normalized, yet couriers, workers and nearby businesses still use the old yard as a landmark and informal meeting point.

Canon decisions can later determine whether the site closes, receives another civic use, remains occasional overflow or becomes remembered without remaining operational.

## The Cold Room Works, the Door Does Not

A specialized storage zone retains its authored environmental function, but the access door or corridor is under maintenance.

The facility may have usable internal capacity that cannot currently serve normal intake or picking.

No mechanical temperature or item-degradation effect is assumed. If a future item requires exact environmental handling, that rule must come from the governing source.

## A Batch Has Two Shelf Histories

Two records both look credible. One says a batch was placed in Zone A; another says it was later observed in Zone C. Neither record contains an explicit internal move.

The investigation can surface:

- an unlogged but authorized relocation;
- an observation timestamp entered late;
- a slot-label change;
- an aggregation/splitting mistake;
- two similar batches being conflated;
- an unresolved gap.

The system preserves both histories and their provenance until reconciliation.

## Everyone Calls It Lost

A named item cannot be found at its recorded slot. Local conversation rapidly labels it lost or stolen.

The storage layer only knows `NOT_FOUND_AT_RECORDED_LOCATION` until more evidence exists.

Potential resolution paths include staging, a legitimate internal move, maintenance relocation, issue/return workflow, stale labeling or genuine unknown disposition. Theft belongs to a case only if evidence supports that escalation.

## The Warehouse Became a Market Hall

An old storehouse no longer serves its original operational purpose. The building is reused as a public market, event hall or another canon-approved function, while loading doors, floor markings, old bay names and former workers keep its industrial history visible.

The previous facility record remains historical and links to the successor use rather than being overwritten.

## The First Pick Was Correct at the Time

A worker picked the requested batch correctly. Before external handoff, a new hold was issued.

The goods are physically staged but no longer handoff-ready. Returning them to storage may itself require a controlled task and a different zone.

This seed makes timing materially important without turning the worker into an error state.

## The Pokémon Works Here, the Species Does Not

A recurring individual Pokémon has an authored storage role supported by its own history and whatever exact rules are required for its tasks.

Visitors begin assuming every member of that species performs the same work.

NPC interactions, signage, training records or actual assignments can correct the inference. Species remains descriptive, never occupational permission.

## Mystery: Four Inventory Counts, Three Physical Positions

Four records report different quantities or locations for the same aggregate stock.

The intended investigation uses:

- observation timestamps;
- observation scope;
- putaway records;
- internal moves;
- picks;
- staging records;
- external handoff references.

A valid outcome may show that all four records were accurate when authored but described different operational moments.

No hidden truth score chooses a liar.

## Mystery: Five Storage Labels, Two Actual Batches

Five labels or informal names appear in records. Only two mechanically meaningful material batches exist.

Possible reasons include:

- old shelf labels;
- supplier naming versus local naming;
- split storage locations;
- a superseded internal code;
- a temporary overflow label.

The mystery teaches the player to reconcile persistent identity rather than treating visible labels as truth.

## Long arc: The Depot Through a Supply Shock

Phase 1 establishes ordinary receiving, putaway, picking and recurring workers/couriers without making the depot a quest hub.

Phase 2 introduces one bounded constraint: a route interruption, facility problem, event surge or upstream production disruption creates receiving or staging pressure.

Phase 3 activates temporary overflow. Nearby shops, workers, carriers and public spaces respond differently. One actor benefits from the new flow while another loses routine access.

Phase 4 technical capacity recovers before the entire chain normalizes. Old stock may still await putaway, a storefront may still report scarcity, and a carrier schedule may still be displaced.

Phase 5 the temporary arrangement ends or changes use. Some habits persist: workers still call an area by its overflow name, a nearby business keeps new hours, or an old loading route becomes a local shortcut.

Phase 6 a later discrepancy or delivery reconnects to those records. Earlier storage history becomes useful evidence rather than a forgotten episode.

The arc uses explicit events and relationships. There is no abstract `warehouse_level`.

## Encounter: Receiving Dock Withdrawal

Full intended version:

A threat enters the operational perimeter while workers and noncombatants must clear several reviewed exits. The tactical scene may include route protection, Intercept, forced movement, generalized reactions and objective-aware opposition. Active vehicles, loading equipment or industrial hazards require the environmental capability family and exact governing rules.

Reduced runnable version:

Storage freezes intake/dispatch first. Workers, goods, vehicles/equipment and nonparticipant Pokémon leave tactical participation. Ouros chooses explicit combatants. AutoPTU receives a static reviewed apron/yard. Victory secures the immediate perimeter only.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for the rich operational form;
- move-specific behavior — PARTIAL as used;
- abilities — PARTIAL as used;
- items — PARTIAL as used;
- Trainer Features/perks — PARTIAL as used;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for withdrawal/protection behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

## Encounter: Staging Aisle Perimeter

Full intended version:

Combatants contest access around outbound staging. Multiple narrow routes, protection/withdrawal logic, Intercept/forced movement and reactions matter. Any rack collapse, moving conveyor or equipment interaction requires explicit hazards/zones support plus governing mechanics.

Reduced runnable version:

Goods remain off-grid or inert non-targetable world objects. The external handoff stays frozen. AutoPTU receives explicit participants in a static aisle/perimeter. Victory changes immediate access only.

The same permanent capability classifications apply. Static geometry can use VERIFIED targeting/LoS and base movement. Rich reactions, displacement, objective policy and semantic playback remain incomplete or blocking.

## Encounter: Overflow Yard Conflict

Full intended version:

An outdoor temporary storage site creates several approach lanes and an authored protection objective. Weather or terrain matters only if an exact PTU battle contract is deliberately activated.

Reduced runnable version:

Stored goods and workers remain outside the BattleSpec. Weather remains presentation-only. Combat occurs at a static perimeter with explicit participants. No result changes ownership, quantity, hold status or storage disposition.

## Consequence rules for all three encounters

A tactical victory may establish a narrow authored fact such as `immediate perimeter secured` or `staff can return for assessment`.

It never automatically establishes:

- inventory counted;
- stock found;
- goods released from hold;
- putaway completed;
- pick completed;
- external custody transferred;
- shipment dispatched;
- facility reopened;
- ownership changed;
- container contents revealed.

Those facts remain with their owning systems and evidence chains.

## Canon questions raised, not answered

- Which Ouros settlements use dedicated depots versus shop/workshop back rooms?
- Which regions have refrigerated, secure or other specialized storage?
- What technologies move ordinary goods inside facilities?
- Which institutions operate major distribution stores?
- What privacy/access norms exist around stored goods?
- Which old storage districts have been demolished or repurposed?
- Which individual Pokémon perform storage work, and what exact evidence supports each assignment?
