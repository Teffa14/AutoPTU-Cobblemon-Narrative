# Storage, Warehousing & Inventory Operations Scan — Pass 104

Status: RESEARCH / PROVENANCE ONLY. Not established Ouros canon.
Date: 2026-08-28
Baseline Narrative head inspected before writing: `ee4484f678114663c56dbc419e67f7c76a1649dc`.

## Research question

What reusable structures can make storage facilities, depots, back rooms, distribution stores, refrigerated storage and temporary overflow spaces persistent parts of Ouros without duplicating Procurement, Courier, Manufacturing, Batch Traceability, Storefront, Finance or PTU item rules?

## Internal repository gap check

The complete recursive repository tree was inspected before this pass and returned `truncated=false`.

Nearby authority already exists:

- Material Culture owns item/batch identity, provenance and rules-bearing creation/repair.
- Procurement owns sourcing, ordering, receipt and acceptance review.
- Courier owns physical shipment legs and custody handoffs in transit.
- Manufacturing owns production runs, work-in-process and production release.
- Batch Traceability owns problem scope, recall/quarantine/correction workflow and downstream trace.
- Storefront owns customer-facing availability bands, not exact warehouse inventory.
- Ports own berth/cargo-transfer operations at maritime interfaces.
- Shared Equipment owns checked-out/issued assets.
- Facility Maintenance owns technical repair and verification of storage buildings/equipment.

No dedicated layer currently preserves internal storage topology, putaway, verified physical position, picking, staging, inventory observations/reconciliation, overflow episodes or handoff readiness. Pass 104 targets that narrow gap.

A correspondence/private-message candidate was rejected because `media-communications-information-layer.md` and `personal-records-oral-history-correspondence-extension.md` already own it. A border/checkpoint candidate was also rejected because `interregional-mobility-recognition-layer.md` already models visits, arrival/departure, recognition and scoped access while deliberately leaving passports/customs/national-border law undecided.

## Source 1 — Driftveil Cold Storage

Source: Bulbapedia, “Cold Storage” and Driftveil City / Black and White walkthrough material.

URLs:
- https://bulbapedia.bulbagarden.net/wiki/Cold_Storage
- https://bulbapedia.bulbagarden.net/wiki/Driftveil_City
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pokémon_Black_and_White/Part_6

Observed high-level structures:

- a warehouse district sits next to a shipping hub rather than functioning as an isolated dungeon;
- imported/exported goods can pass through a specialized refrigerated facility before later commercial use;
- workers and ordinary logistics coexist with story events in the same place;
- the facility later disappears and the site is reused for the Pokémon World Tournament.

Reusable Ouros lessons:

1. Storage can be a normal connective tissue between port/courier movement and storefront/manufacturing demand.
2. Specialized storage should be represented as an authored zone/property of a facility, not as a universal item-effect rule.
3. A storage site can accumulate history and then be demolished or repurposed without deleting its previous operational record.
4. Facility identity, stored-goods identity and district identity must remain separate; one can change while the others persist elsewhere.

Rejected copying:

- Team Plasma presence and plot;
- specific map/ice puzzle layout;
- exact characters, items and battles;
- the assumption that every refrigerated room creates an Ice-type or PTU environmental effect.

## Source 2 — Veilstone / Galactic Warehouse

Source: Bulbapedia, “Team Galactic HQ”, Veilstone City, and BDSP walkthrough.

URLs:
- https://bulbapedia.bulbagarden.net/wiki/Team_Galactic_HQ
- https://bulbapedia.bulbagarden.net/wiki/Veilstone_City
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pokémon_Brilliant_Diamond_and_Shining_Pearl/Part_21

Observed high-level structures:

- a city can contain several warehouses associated with ordinary goods storage while one particular storage facility has controlled access;
- a visible public-facing room can conceal or connect to deeper restricted areas;
- access to a storage area can depend on a specific authorization/key rather than on the entire building being globally open or closed.

Reusable Ouros lessons:

1. Access state should exist at facility, zone and possibly slot/room scope.
2. `FACILITY_OPEN` does not imply `EVERY_ZONE_ACCESSIBLE`.
3. Storage topology can include service passages and restricted subareas without automatically becoming a combat dungeon.
4. Access credentials should be references to the existing Credentials/Authority systems; the warehouse layer must not invent universal key/permit law.

Rejected copying:

- Team Galactic, criminal ownership, secret HQ connection and Storage Key quest;
- exact underground layout, guards and rewards;
- any rule that locked storage must be bypassed through battle.

## Source 3 — S.S. Tidal storage

Source: Bulbapedia, “S.S. Tidal”.

URL: https://bulbapedia.bulbagarden.net/wiki/S.S._Tidal

Observed high-level structures:

- passenger space, crew space and cargo storage can coexist within one moving asset;
- cargo containers and staff activity make storage an operational subspace rather than a generic treasure room;
- the same asset can carry different people and cargo across repeated voyages.

Reusable Ouros lessons:

1. `storage_facility` can be fixed or mobile when another owning system already establishes the asset.
2. Storage zones can be nested inside ports, vessels, transit hubs, shops, clinics, workshops or institutions without those layers surrendering authority.
3. A storage location should persist as an addressable sub-location even when the containing asset moves, if the adapter/world model can preserve its identity.
4. Cargo presence does not automatically expose contents, ownership or mechanical item data to nearby actors.

Rejected copying:

- exact ship layout, trainers and rewards;
- automatic healing/rest behavior;
- any assumption that a mobile storage area is tactically simulated while moving.

## Source 4 — GS1 physical-location model

Source: GS1, “Physical location”.

URL: https://www.gs1.org/standards/id-keys/gln/physical-location

This is an external logistics reference, not Pokémon canon and not an Ouros legal/industry standard.

Observed high-level structure:

- a physical location can have nested sub-locations when there is a business need to distinguish them;
- examples include a distribution centre, dock door, cold storage within a warehouse and shelf;
- mobile locations can also have persistent identities distinct from the assets themselves.

Reusable Ouros lesson:

Use hierarchical persistent IDs only where story state needs them: facility -> zone -> slot/shelf/bay. Do not assign an ID to every Minecraft block. This supports provenance and reconciliation without turning Ouros into a warehouse-management simulator.

Rejected import:

- GLN numbering;
- GS1 compliance;
- real-world commercial standards, law or mandatory scanning workflows.

## Tabletop/community cross-check

Public PTU searches in this pass did not yield a warehouse-specific campaign log strong enough to justify importing a new mechanical pattern. General PTU community material repeatedly emphasizes that PTU is mechanically dense and that unsupported homebrew should be distinguished from base rules. That reinforces the existing project rule: logistics/world state may be authored, but no storage hazard, carrying modifier, forklift rule, container HP or inventory bonus is created without governing PTU/Caelo evidence.

No weak community source was promoted merely to satisfy a source-count target.

## PTU / Caelo boundary

The project already treats item instances and material batches as persistent narrative objects while exact item effects, crafting recipes, actor prerequisites, yields and rules-bearing transformations remain governed by PTU/Caelo/AutoPTU.

The inspected project corpus does not establish a universal PTU/Caelo subsystem for:

- warehouse capacity arithmetic;
- pallet/container units;
- slotting or putaway rolls;
- cycle-count checks;
- forklifts, cranes or conveyor tactical movement;
- storage-condition degradation;
- cold-chain temperature damage;
- rack collapse;
- automated theft/loss probability;
- generic encumbrance from warehouse handling;
- inventory accuracy bonuses;
- species-based eligibility for warehouse work.

Therefore Pass 104 may persist operational facts but may not create those mechanics.

## Design extraction

The strongest reusable pattern is a chain of independently verifiable states:

external arrival -> receipt/acceptance decision by owning system -> authorized storage intake -> putaway task -> verified internal location -> requested pick -> picked -> staged -> handoff-ready -> external custody transfer by owning system.

Every arrow may pause, fail, be superseded or require reconciliation. Earlier facts remain historical.

Important separations:

- `RECEIVED != PUT_AWAY`;
- `STORED != AVAILABLE_FOR_SALE_OR_USE`;
- `LOCATION_RECORDED != LOCATION_PHYSICALLY_VERIFIED`;
- `PICKED != STAGED`;
- `STAGED != DISPATCHED`;
- `EMPTY_SLOT != AVAILABLE_SLOT`;
- `COUNT_DISCREPANCY != THEFT`;
- `OVERFLOW_STORAGE != PERMANENT_RELOCATION`;
- `QUARANTINE_LINKED != WAREHOUSE_OWNS_QUARANTINE_DECISION`.

## Worldbuilding opportunities

Storage continuity can produce low-combat stories from ordinary pressure:

- a receiving bay is physically full although the facility has space elsewhere;
- a store shortage exists while accepted stock still waits for putaway;
- a batch is physically present but held by Traceability;
- a historic overflow yard becomes socially or commercially important;
- a location label is stale after a legitimate internal move;
- two counts disagree because one was made before staging;
- a specialized room remains operational while its access door is under repair;
- a storage district is partially demolished and repurposed, leaving old route names and worker habits behind.

## Canon status

All facility types, institutions, technologies, storage practices, capacity conventions and labor roles introduced by this scan are RESEARCH or PROPOSED only until separately canon-approved.

Existing canon and rules are not overwritten.
