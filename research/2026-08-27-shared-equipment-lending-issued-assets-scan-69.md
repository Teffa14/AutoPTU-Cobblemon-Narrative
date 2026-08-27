# Shared Equipment, Lending & Issued Assets Research — Pass 69

Status: research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-27

## Scope

This pass investigates temporary access to shared resources: institutional kits, loaner tools, issued devices, reservations, handoffs, returns, inspection and pool availability.

The repository tree was inspected in full before research. The gap is narrow. Ouros already tracks physical item identity and ownership/custody, workplace assignments, library circulation, found property, courier shipments, finance, maintenance, travel services and Pokémon agency. What is missing is a persistent lifecycle for an exact shared asset between its owner and successive temporary users.

The target is operational continuity rather than a general rental economy.

## Existing-repository boundary

Relevant existing owners are:

- `design/material-culture-economy-crafting-layer.md` — persistent `item_instance`, owner/custodian refs, provenance, repair history and mechanical item refs;
- `design/workplaces-professions-staffing-layer.md` — roles, assignments, handoffs, qualifications and staffing;
- `design/libraries-publications-editions-circulation-extension.md` — circulation of authored works and copy instances;
- `design/found-property-custody-restitution-extension.md` — objects separated from an expected holder outside an intentional loan/shipment lifecycle;
- `design/courier-parcel-last-mile-logistics-extension.md` — intentional physical transport between nodes;
- `design/facility-maintenance-repair-inspection-extension.md` — repair, inspection and operational readiness;
- `design/finance-sponsorship-risk-layer.md` — money, funding and risk where canon establishes them;
- `design/pokemon-agency-partnership-release-layer.md` — Pokémon agency, partnership and custody boundaries;
- `design/travel-transport-expedition-layer.md` — route and travel-service state.

Pass 69 does not redefine ownership, invent universal rental law, create prices/deposits/fines, duplicate library circulation or treat Pokémon as equipment.

## Source 1 — Battle Factory temporary roster exchange

Source: Bulbapedia, Battle Factory (Generation IV).
https://bulbapedia.bulbagarden.net/wiki/Battle_Factory_(Generation_IV)

Observed pattern:

Before the challenge, the player hands over the current party and chooses three of six rental Pokémon. Continued participation can include exchanging one temporary selection for another. The temporary roster exists inside a bounded institutional context.

Reusable design lesson:

Temporary access should have a clear scope and lifecycle. Selection, handoff, active use, exchange and exit are distinct events. Access to a pool does not imply permanent acquisition.

Transformation for Ouros:

Apply the structure to equipment and institutional assets. A survey office can own six field kits while three are assigned to a team for a specific project window. A later swap updates custody and availability without changing ownership.

Safety boundary:

This extension does not model Pokémon as loanable assets. The source provides workflow structure only. Any Ouros service involving another person's or institution's Pokémon must remain under Pokémon Agency plus the relevant Travel/Battle institution and requires canon review.

## Source 2 — Rental pool integrity in Pokémon Adventures

Source: Bulbapedia, Rental Pokémon overview and Battle Factory manga material.
https://bulbapedia.bulbagarden.net/wiki/Rental

Observed pattern:

Pokémon Adventures uses a rental pool whose expected membership can be questioned when one individual does not fit the pool's normal profile. The same material later treats loss of the whole pool as a meaningful institutional breach.

Reusable design lesson:

A shared pool becomes narratively useful when exact identity matters. An asset that looks like the expected model can still be the wrong instance. Pool records, provenance and physical observations can expose a mismatch without a supernatural clue.

Transformation for Ouros:

Use serials, repair marks, provenance, kit contents and checkout history to support low-stakes mysteries such as an instrument returned to the wrong case or an unregistered tool appearing in a depot. Do not copy the manga's characters, theft plot or Pokémon-specific resolution.

## Source 3 — Capture Styler as role-bounded issued equipment

Source: Bulbapedia, Capture Styler.
https://bulbapedia.bulbagarden.net/wiki/Styler_Energy

Observed pattern:

Ranger School students receive School Stylers intended for training and with deliberately limited functions. Graduation changes institutional role and the character receives a different class of Styler. Higher Ranger status can correspond to another device class.

Reusable design lesson:

An institution can issue equipment according to role, training state and operational purpose. The equipment assignment and the actor's qualification should remain separate records. Receiving a device does not itself prove every professional competence.

Transformation for Ouros:

A workplace, school, research group or maintenance team may issue a canon-approved kit only when the institution, item and qualification requirements already exist. Pass 69 may record the issue/return lifecycle; it cannot invent device functions, Skills, Features or legal authority.

## Source 4 — Ranger Depots as distributed support points

Source: Bulbapedia, Pokémon Ranger Glossary.
https://bulbapedia.bulbagarden.net/wiki/Pokemon_Ranger_Glossary

Observed pattern:

Ranger Depots provide operational support in remote areas away from major bases. They give field workers a repeatable support node rather than forcing every resource interaction back to headquarters.

Reusable design lesson:

Shared-asset availability can be distributed geographically. A kit can belong to one institution while being stored, inspected or handed off through several support nodes. Location becomes part of availability.

Transformation for Ouros:

An approved institution may keep equipment pools at remote desks, field stations, workshops or transit-adjacent depots. The extension references those existing places; it does not create a universal depot network.

## Source 5 — Poké Ride separates access entitlement from ownership

Source: Bulbapedia, Poké Ride.
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9_Ride

Observed pattern:

In Alola, a Ride Pager can register access to specific Ride Pokémon services. Some Ride Pokémon are institutionally organized or kept at service locations, while people can also have personal ride Pokémon. The user's ability to call a service is therefore conceptually separate from owning the Pokémon involved.

Reusable design lesson:

An entitlement can grant access to a service without transferring ownership or even physical custody of the underlying resource. This distinction is useful well beyond transport.

Transformation for Ouros:

Pass 69 can represent authorization to request or reserve a resource separately from checkout of a physical object. Pokémon themselves remain outside the asset schema. Pokémon-assisted mobility stays under Travel and Pokémon Agency, with individual capability validation.

## Source 6 — Gogoat Shuttle interruption and attempted restart

Source: Bulbapedia, Pokémon as transport.
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_as_transport

Observed pattern:

The Gogoat Shuttle in Lumiose is presented as an organized city service in Pokémon X/Y. Later setting material describes the service as having ceased operations because changed local conditions made it unsuitable, with an actor working toward restart.

Reusable design lesson:

Availability can fail even when the underlying asset still exists. A shared service may become unavailable because the environment, staff, route, safety conditions or support dependencies changed. Restoration needs its own verification.

Transformation for Ouros:

A loan pool may be physically intact yet unavailable because its inspector, charger, storage room, route, qualified operator or maintenance dependency is unavailable. Pass 69 records the availability consequence and points to the owning system for the cause.

## Cross-source patterns

### Temporary access needs explicit state

Reservation, authorization, checkout, custody, active assignment, return and inspection should not collapse into one flag.

### Exact identity can matter

Two identical-looking instruments may have different repair histories, calibration records, contents or institutional owners. When story relevance exists, use the existing `item_instance` identity.

### Availability depends on place and readiness

A shared asset can be owned and physically present while unavailable because it is reserved, under inspection, awaiting repair, incomplete, stored elsewhere or restricted to a specific assignment.

### Qualification and equipment are separate

A role can qualify an actor to request a device, but handing over the device cannot grant a PTU Skill, Edge, Feature, Move, Capability or authority.

### Return is not the final verification step

A physical handback can be followed by inspection, inventory reconciliation, charging, cleaning, repair or another canon-approved readiness action before the asset becomes available again.

### Pokémon require a harder boundary

Pokémon are actors, partners and creatures with agency. Pass 69 must never serialize a Pokémon as an `asset_instance`, place one in an equipment pool or infer that temporary service access transfers ownership, Loyalty or battle authority.

## Anti-copy / transformation rules

Do not copy named characters, dialogue, exact Battle Factory rosters, Ranger device mechanics, Ranger ranks, Alola service rules, fares or game-specific unlock requirements.

Do not infer that Ouros has rental shops, deposits, late fees, insurance, licensing, universal ID cards, calibration law or standardized checkout paperwork.

Do not turn borrowed gear into loot.

Do not assume an overdue asset was stolen, a damaged asset was damaged by the borrower, or a missing record proves misconduct.

## PTU/Caelo mechanical boundary

The researched narrative patterns do not authorize new item mechanics.

A temporary equipment record may reference an authoritative PTU/Caelo item or tool, but Pass 69 cannot create its combat effect, activation timing, action cost, frequency, Skill prerequisite, crafting function or field capability.

If a loaned item is mechanically relevant in battle, execution depends on the current AutoPTU item registry and all related hook/lifecycle families. Merely having a persistent `item_instance` in world state does not make that mechanical item executable.

A Pokémon cannot be represented as equipment by this extension. Pokémon mobility or work requires the individual Pokémon's validated state plus the governing Pokémon Agency/Travel/Workplace rules.

## Pass 69 design target

Create a shared-equipment extension with stable asset-pool refs, temporary access entitlements, reservation state, checkout/custody events, assignment scope, return state, post-return inspection, location-aware availability, substitution, pool reconciliation and explicit handoffs to Maintenance, Found Property, Case, Courier, Finance and the owning workplace/institution.

Add original non-canon situations that make repeated use of the same equipment pool generate continuity. Mechanically rich encounters must keep the item outside tactical resolution unless its exact PTU/Caelo behavior and AutoPTU support are verified.