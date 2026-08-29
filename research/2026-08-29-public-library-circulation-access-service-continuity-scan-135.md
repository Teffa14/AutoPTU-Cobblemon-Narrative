# Public Library Circulation, Access & Service Continuity Scan — Pass 135

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-08-29
Narrative head inspected before writing: `fb4391c9ed6d8fec05ed1588029412d772642a44`

## Purpose

This pass looks for a gap between the existing Archives/Museums/Collections layer and everyday public access to knowledge.

The existing collections layer already owns accession, preservation, archival holdings, finding aids, institutional loans, exhibits, restricted collections and object provenance. It even allows LIBRARY as an institution type. It does not yet model ordinary public circulation as a persistent service: branch membership, copy-level availability, holds, pickup location, check-out, renewal, return, branch transfer, temporary service interruption, mobile service, reading-room use and reopening after disruption.

The proposed gap is therefore public-library service continuity, not another archive system.

## Internal material checked

The recursive repository tree was inspected before topic selection. Targeted overlap checks included:

- `design/archives-museums-collections-preservation-layer.md`
- `design/courier-parcel-last-mile-logistics-extension.md`
- `design/formal-education-enrollment-course-assessment-continuity-extension.md`
- `design/accessibility-participation-accommodations-layer.md`
- `design/communications-network-relay-service-continuity-extension.md`
- `design/commercial-services-storefront-continuity-extension.md`
- `design/public-space-event-scheduling-continuity-extension.md` where present in inventory
- recent research/proposal names for library, lending, circulation, Canalave, Malie and Nacrene

Repository search returned no dedicated public-library circulation or branch-service continuity layer.

## Source A — Canalave Library

Public source:
https://bulbapedia.bulbagarden.net/wiki/Canalave_Library

Observed high-level pattern:

Canalave Library is a civic place whose shelves preserve regional mythology and where researchers and protagonists can meet to compare information before later events.

Reusable structure for Ouros:

- a library can be an ordinary public place and a narrative junction at the same time;
- knowledge can be geographically concentrated without every book becoming a unique quest object;
- meeting in a knowledge institution can advance an investigation without the institution itself becoming an authority over historical truth;
- a later interpretation can cite a library source while the underlying myth remains a claim with provenance.

Not imported:

- Sinnoh canon;
- named myths;
- named characters;
- game progression;
- any rule that reading grants knowledge automatically.

## Source B — Malie Library

Public source:
https://bulbapedia.bulbagarden.net/wiki/Malie_City

Observed high-level pattern:

Malie Library is explicitly open for public reading and contains a more specialized upper-floor body of material about regional history and legendary traditions.

Reusable structure:

- one building can have different service scopes by floor or room;
- public reading access does not imply circulation rights for every holding;
- general collections and specialist/local-history collections can coexist;
- access can be broad while interpretation remains uncertain.

Ouros transformation:

`BUILDING_OPEN`, `READING_ROOM_OPEN`, `COLLECTION_ACCESSIBLE`, `ITEM_CIRCULATING` and `COPY_AVAILABLE` must remain separate states.

## Source C — Nacrene Museum / Library / Gym

Public source:
https://bulbapedia.bulbagarden.net/wiki/Nacrene_City

Observed high-level pattern:

Nacrene combines museum, library and battle-institution functions in one building, and the role of the space changes over time. In later continuity the former Gym area is used as a library.

Reusable structure:

- one facility can host several institutional owners or service roles;
- physical reuse can preserve memory of an earlier function;
- the same room can change purpose without erasing its former state;
- information navigation can be gameplay without turning every shelf into loot;
- a library can survive a leadership or institutional transition.

Ouros transformation:

A room may have `space_history`, `current_service_owner`, `former_service_owner` and visible predecessor traces. A former battle room becoming a reading room is a world-state transition, not an automatic mechanical conversion.

## Source D — PTU community material

Public sources:
https://www.reddit.com/r/PokemonTabletop/comments/gs8dy2/
https://www.reddit.com/r/PokemonTabletop/comments/1ot78qm/

Observed high-level pattern:

PTU play frequently depends on cross-referencing a large body of books, errata and reference material. Community discussion treats information access and reference management as a practical part of play rather than a single omniscient rules source.

Reusable design lesson:

- information can be distributed across several records;
- finding the correct source can be a meaningful task;
- later amendments do not erase earlier documents;
- an index/reference layer can reduce friction without pretending that every source agrees.

This is used only as a design lesson. Community posts are not rules authority.

## Source E — ALA request / hold / interlibrary loan workflow

Public source:
https://www.ala.org/support/request-item

Observed workflow:

A user searches a catalog, places a hold when the local library owns an item, or initiates an interlibrary request when it does not. Arrival and readiness for pickup occur later.

Reusable architecture:

`REQUEST_CREATED != COPY_AVAILABLE`

`COPY_AVAILABLE != HOLD_READY`

`HOLD_READY != PICKED_UP`

`LOCAL_CATALOG_MATCH != LOCAL_COPY_PRESENT`

`INTERLIBRARY_REQUEST_ACCEPTED != ITEM_IN_TRANSIT`

No ALA policy, membership rule, institution name or legal framework is imported.

## Source F — National Library of Australia resource sharing

Public source:
https://www.library.gov.au/services/libraries/copies-and-interlibrary-loans-libraries

Observed high-level pattern:

Resource sharing can satisfy a request through a copy rather than movement of the original, and original physical material may remain protected from routine transit.

Reusable architecture:

- a request can be satisfied by a physical loan, a reproduction or another authorized access form;
- fulfillment method and requested information need separate records;
- transport risk may change the chosen fulfillment method;
- a copy supplied for access does not become the original source object.

Ouros guardrail:

`DIGITAL_OR_PRINT_COPY != ORIGINAL_OBJECT`

The existing Archives layer remains owner of provenance and authenticity of the source object.

## Source G — Libraries Victoria service pause

Public source:
https://www.connectedlibraries.org.au/wp-content/uploads/2023/02/Library-Member-Frequently-Asked-Questions-FAQ_Temp-Pause-on-Intralibrary-loans_updated_31.1.pdf

Observed high-level pattern:

A network can pause one service while preserving queue position, continue local holds, accept returns and allow direct in-person borrowing elsewhere.

Reusable architecture:

- service degradation should be scoped;
- one network function can pause without closing every branch;
- existing requests can survive a suspension;
- return acceptance can remain active while outbound resource sharing is paused.

Ouros transformation:

`NETWORK_TRANSFER_PAUSED != BRANCH_CLOSED`

`NEW_REQUESTS_PAUSED != EXISTING_REQUESTS_CANCELLED`

`OUTBOUND_TRANSFER_PAUSED != RETURNS_REFUSED`

## Source H — Oakland Public Library circulation policy

Public source:
https://oaklandlibrary.org/policies/circulation-policy/

Observed pattern:

Different material classes can have different circulation, renewal and hold behavior, and pickup location can be changed before fulfillment.

Reusable architecture only:

- circulation rules belong to an authored policy record;
- item class and service channel can affect allowed transitions;
- pickup location can change without changing item identity or request identity.

No real thresholds, fines, limits or eligibility rules are imported.

## Source I — general library mystery design

Public community source:
https://www.reddit.com/r/DndAdventureWriter/comments/10aueu2/the_arcane_archive/

Useful high-level lesson:

Libraries support clue networks, missing-record investigations, reference chains and spatial navigation better than indiscriminate combat or destructible-book set pieces.

Ouros transformation:

Library adventures should prefer:

- catalog discrepancies;
- superseded shelf locations;
- branch-transfer history;
- returned-but-not-reshelved items;
- two editions with different annotations;
- a hold routed to a former pickup point;
- a local-history copy whose catalog record changed;
- service changes that outlive the original disruption.

The fantasy premise, magical books and specific plot suggestions are not imported.

## Synthesis

The strongest new worldbuilding opportunity is not a magical forbidden archive. It is an everyday institution that remembers how information moves.

A public library can generate persistent narrative through:

- branch identity;
- membership or access records if canon permits them;
- copy-level circulation;
- holds and queues;
- pickup routing;
- branch transfers;
- mobile-library stops;
- reading-room-only materials;
- temporary service points during renovation or disaster;
- local-history collections linked to Archives but governed by different service rules;
- old stamps, labels and shelving systems that survive institutional change;
- notification histories;
- community routines that continue after a branch moves.

## Provenance boundary

Research notes are not canon.

Every external source in this scan contributes only a reusable high-level structure. No protected dialogue, named plot, distinctive character arc, real-world institutional rule or real legal policy is copied into Ouros.

## PTU/Caelo cross-check position

No source reviewed here establishes universal PTU mechanics for:

- research time;
- finding a book;
- catalog searches;
- library membership;
- reading speed;
- automatic General Education checks;
- automatic knowledge gain;
- translation;
- document authentication;
- memory;
- misinformation detection;
- librarian profession;
- library-card Items;
- battle rewards from reading.

Exact Skill, Feature, Edge, Move, Ability or Item effects remain rule-governed and must be verified against the project's PTU/Caelo source material before mechanical use.

## Candidate handoffs

Archives/Museums owns source-object provenance, restricted holdings, accession, preservation and institutional collection loans.

Education owns academic enrollment, course requirements and assessment.

Courier/Logistics owns physical movement when a library transfer becomes a shipment.

Communications owns notification delivery channels.

Accessibility owns authored accommodations.

Public Space owns exterior civic-space scheduling where applicable.

Construction/Maintenance owns building work and repair.

The proposed new library layer owns only public access-service continuity and circulation state.