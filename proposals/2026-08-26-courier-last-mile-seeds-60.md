# Courier & Last-Mile Seeds — Pass 60

Status: PROPOSED / NON-CANON. Names, institutions, routes, technologies and locations below are candidates only.

These seeds assume the courier/parcel extension in `design/courier-parcel-last-mile-logistics-extension.md`. They deliberately avoid inventing shipping prices, postal law, species-based work abilities or unsupported PTU combat effects.

## Seed: The Address That Changed

Premise: a parcel reaches the correct settlement, but the intended recipient moved recently and the old address is now occupied by someone else.

Useful state:

- shipment history;
- current residential record;
- privacy/forwarding permissions;
- sender contact route;
- prior delivery attempt.

Choices:

- hold for pickup;
- contact sender through an established channel;
- use an existing institutional forwarding path;
- return the parcel;
- ask the former household for a permitted contact lead.

Consequence:

A mundane delivery becomes a callback to relocation history without exposing private information automatically.

## Seed: The Weekly Drop Does Not Come

Premise: a small settlement has a known delivery cadence. One expected drop is late enough that several independent services begin asking questions.

The delay may affect:

- a repair part;
- ordinary shop stock;
- clinic supplies;
- personal mail;
- event materials.

The mystery begins with schedule deviation, not an attack.

Possible causes must come from actual route, staffing, transport, facility, crisis or faction state.

## Seed: Three Parcels, One Wrong Cart

Premise: three packages were sorted for different destinations, but dispatch records and physical labels disagree after a rushed transfer.

Evidence sources:

- intake time;
- package appearance;
- last verified shelf/cart;
- custody transfers;
- staff claims;
- departure manifests;
- receiving-desk records.

The players reconstruct the chain without assuming that the most confident witness is correct.

## Seed: The Replacement Part Is Here, Almost

Premise: a facility repair has waited several days for one replacement component. The parcel has reached the settlement but is HELD because the receiving desk is closed or the shipment cannot be matched to the work order.

The facility does not magically reopen when the package enters town.

Completion flow:

```text
parcel recovered
→ valid custody transfer
→ Facility Maintenance receives part availability
→ repair work can advance
→ verification/reopening remain separate
```

## Seed: Pickup Window

Premise: a recipient cannot be reached at home, but the service can hold the parcel at a staffed node for a limited practical window.

The story pressure comes from intersecting schedules rather than a fabricated universal shipping timer.

This can intersect:

- a Trainer leaving town;
- a ferry departure;
- a clinic shift;
- a tournament check-in;
- a research expedition.

Exact deadlines must come from existing schedule state.

## Seed: The Return Nobody Expected

Premise: an old shipment returns to its sender after several failed attempts. By the time it comes back, the sender's situation has changed.

Possible callback value:

- a promise that was never fulfilled;
- an outdated address;
- a project already solved another way;
- a relationship that changed during the delay;
- evidence that the original recipient never actually received a document or object.

The returned parcel preserves its full attempt history.

## Seed: Rain on the Label

Premise: packaging is visibly damaged after a disrupted journey. Nobody yet knows whether the contents are affected.

The scene should distinguish:

- packaging observation;
- declared contents;
- actual contents;
- mechanical item state;
- staff assumptions.

If the package contains medicine, research samples or another mechanically sensitive item, exact effects require governing rules or an authored non-mechanical determination by the owning system.

## Seed: Two Desks, No Handoff

Premise: a package passed from a transport terminal to a local institution, but each desk believes the other still has custody.

Players investigate the seam between services rather than a malicious theft by default.

The culprit may simply be:

- an unrecorded transfer;
- a mislabeled shelf;
- a staff change;
- a temporary relocation;
- an interrupted shift;
- an actual disappearance supported by evidence.

## Seed: The Parcel for a Closed Shop

Premise: a commercial order arrives while the storefront is temporarily closed.

Questions:

- does another approved receiving location exist?
- can the operator be contacted?
- should the shipment be held?
- is a temporary counter already active?
- does the parcel belong to the business, an employee or a customer order?

The delivery layer records custody; Storefront Continuity decides service consequences.

## Seed: Expedition Cache Handoff

Premise: a field team cannot return to town before a supply transfer. A legitimate intermediary must carry a sealed package to a designated route node or camp.

The package can contain mundane replacement equipment, records or samples. Its importance comes from timing and custody.

Full combat version could become an escort/convoy encounter, but the reduced implementation should keep the package outside tactical interaction until those capability families exist.

## Seed: The Courier Knows the Route, Not the Story

Premise: a recurring courier has visited the same settlements for months and notices route rhythms, who usually receives parcels and which desks are normally staffed.

They are a valuable witness for logistics facts but do not become omniscient about package contents or private lives.

Potential use:

- spotting a broken routine;
- identifying a usual transfer point;
- recognizing that a receiving desk has moved;
- knowing which route was used last week;
- remembering an unusual backlog.

## Seed: Sorting Shift

Premise: players voluntarily help during a backlog at a delivery node.

Gameplay can remain noncombat and evidence-driven:

- match shipments to route batches;
- identify exceptions;
- separate redirect cases;
- flag condition concerns;
- prepare ordinary dispatch groups.

No custom sorting Skill check is assumed. If the project later wants mechanical workplace checks, those require explicit PTU/Caelo validation.

## Arc: A Route Learns Its Deliveries

A reusable multi-visit arc for one transport corridor.

Visit 1 — Baseline

The players learn normal delivery cadence, service nodes and familiar staff through ordinary travel or errands.

Visit 2 — First exception

A route disruption causes a visible delay. One shipment matters to an existing repair, shop or household.

Visit 3 — Workaround

The local service adopts a temporary transfer point, pickup desk or changed dispatch schedule.

Visit 4 — Secondary consequence

The workaround solves one problem but changes another routine: a shop receives stock later, a household prefers pickup, or a courier's route changes.

Visit 5 — Stable memory

The corridor returns to ordinary operation, but some practice remains changed. NPC dialogue, signs, desk placement or service schedule reflect the history.

This arc should reuse existing geography. It does not require a new town, depot or courier company.

## Mystery: Five Receipts, Four Handoffs

Premise: a shipment appears to have five pieces of delivery evidence but only four legitimate custody transfers.

Potential explanations:

- duplicated receipt;
- copied timestamp;
- retry recorded as a new transfer;
- parcel returned to the same desk;
- false assumption about which item a receipt referenced;
- genuine missing handoff.

The mystery keeps evidence, interpretation and world truth separate.

## Encounter: Moving Convoy Interruption

Narrative premise: a shipment needed by an existing project is interrupted on a real route.

Full intended version:

- convoy or cargo changes position during combat;
- protect/escape objective;
- interception and forced movement;
- terrain/weather or hazards when the route state supports them;
- objective-aware AI;
- explicit cargo-condition rules;
- synchronized Minecraft playback.

Current dependency classification:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:

The convoy stops before combat. The shipment remains in protected world state and cannot be targeted, moved or damaged tactically. Players resolve one static legal battle at the interruption point. The battle result determines whether the journey resumes, reroutes or retreats through authored world-state logic.

## Encounter: Depot Recovery

Narrative premise: players need to recover a specific parcel from a depot that is temporarily unsafe.

Full intended version may use evacuation, destructible/hazardous zones, knockback near stored cargo, dynamic blocked aisles, containment and objective-aware AI.

Reduced version:

Evacuate workers first. Freeze the map. Run a standard battle using legal combatants only. After the fight, a separate interaction identifies and transfers the parcel. Stored cargo cannot be tactically damaged until explicit rules support it.

## Canon questions left open

- Does Ouros have a regional postal institution, multiple private carriers, community couriers or a mix?
- Which settlements have staffed delivery nodes?
- What address conventions exist?
- Does forwarding exist, and how does it interact with privacy?
- Are signatures, pickup codes or identity checks used anywhere?
- Which shipments can be left with another person or institution?
- What return practices exist?
- Are some routes served on fixed schedules?
- Which transport services carry parcels as well as passengers?
- What Pokémon participation in delivery work is canonically normal and mechanically supported?

None of these are answered by this proposal.
