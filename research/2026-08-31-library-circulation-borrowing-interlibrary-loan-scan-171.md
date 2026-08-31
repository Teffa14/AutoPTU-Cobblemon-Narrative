# Library circulation, borrowing & interlibrary loan research — Pass 171

Status: RESEARCH ONLY / NON-CANON
Date: 2026-08-31

## Purpose

This pass investigates a gap left by the existing Archives, Museums, Collections & Preservation layer. That layer already supports institutions of type LIBRARY, archival holdings, finding aids, access policies and institutional loans. It does not yet model ordinary public circulation: a patron requests a circulating copy, checks it out, renews it, returns it, loses it, damages it, waits behind another patron, or asks one library to obtain material from another.

The goal is to extract reusable state transitions and adventure structures without importing real-world library law, fees, privacy statutes or exact lending periods into Ouros.

## Internal repository check

Existing authority remains with:
- Archives/Museums for holdings, catalog records, access policy, preservation, exhibit history and institutional stewardship;
- Human Identity for actor identity and institutional identifiers;
- Communications for notices and message delivery;
- Courier/Logistics for physical shipment between locations;
- Finance for actual charges or payments if canon defines them;
- Education/Research for what a reader later learns or uses;
- Case/Custody for evidence material.

No existing dedicated public circulation lifecycle was found by repository search for library lending, borrowing, circulation, patron holds, renewals or overdue state.

## Pokémon sources

### Canalave Library
Source: https://bulbapedia.bulbagarden.net/wiki/Canalave_Library

Useful pattern:
- a library is a persistent civic/research location rather than a single quest container;
- different actors use it at different times for reading, study, meetings and research;
- the same collection can support myth, history and later interpretation without making every book authoritative truth;
- new material can appear after later discoveries, making the collection itself temporally persistent.

Ouros transformation:
- libraries can become recurring information hubs whose collection, users and interpretation change across campaigns;
- reading access should be represented separately from truth, comprehension and permanent actor knowledge;
- later additions or catalog corrections can create new reasons to revisit a familiar place.

No Sinnoh myth prose or specific plot is copied.

### Malie Library
Source: https://bulbapedia.bulbagarden.net/wiki/Malie_City

Useful pattern:
- a public library can expose regional history, institutional memory and cultural materials to ordinary visitors;
- a library can sit inside a broader civic district rather than function as a dungeon or elite research archive.

Ouros transformation:
- small civic libraries can carry local histories, practical manuals and community records;
- access itself can be routine, with quests emerging from missing copies, competing demand, damaged material or cross-branch requests rather than arbitrary locked doors.

### Naranja Academy library
Source: https://bulbapedia.bulbagarden.net/wiki/Naranja_Academy

Useful pattern:
- one collection can mix curriculum, institutional records, history, magazines and expedition-derived texts;
- an institution can distinguish public-facing study material from records and prohibited areas.

Ouros transformation:
- school libraries can participate in public circulation while keeping academic records and restricted institutional materials under separate policies;
- a student holding a book does not imply authority over the underlying institutional record or the truth of its contents.

## Library-practice sources

### IFLA Model National Interlibrary Loan Code
Source: https://www.ifla.org/publications/model-national-interlibrary-loan-code/

Reusable state grammar:
- supplying institution and borrowing institution remain separate actors;
- dispatch, receipt, due date, renewal request, return and loss/damage responsibility are distinct events;
- a request can exist even when no transfer occurs;
- interlibrary lending creates a temporary custody chain without changing ownership.

Ouros imports only the state distinctions. It does not import IFLA policy as law.

### Geelong Regional Libraries borrowing guidelines
Source: https://www.grlc.vic.gov.au/services/borrowing-guidelines

Reusable state grammar:
- checkout, due date, renewal and hold/reservation are separate states;
- a hold by another user can affect renewal eligibility;
- return location and pickup location can differ inside a network.

Ouros does not import its item limits, exact loan periods or local policy.

### Library circulation privacy examples
Source: https://comlib.org/use-the-library/library-policies/

Reusable design lesson:
- current borrowing state and long-term borrowing history need not be identical datasets;
- privacy-preserving systems may purge or avoid retaining reading history after return while still retaining limited operational records for lost/damaged items.

Ouros implication:
- Chronicle should not build a permanent dossier of everything every NPC has ever read merely because circulation exists;
- the minimal durable record should be configurable by institution and canon.

## PTU/Caelo boundary

Project source priority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material, Caelo Region Location & Encounter List and live AutoPTU evidence.

This pass found no project evidence establishing a universal PTU/Caelo library-card mechanic, borrowing Skill Check, research bonus from possession of books, automatic General/Occult Education gain, Scholar/Researcher/Chronicler Feature activation through checkout, or progression from reading time.

Therefore all such effects remain UNKNOWN unless a governing source is later verified.

A book or manuscript that is also a mechanical Item must be audited as that exact Item before combat use. Narrative access to a text cannot create a Move, Feature, Edge, Skill Rank, Tutor Point, bonus, identification effect or supernatural knowledge.

## Reusable continuity lessons

The most useful permanent distinctions are:
- HOLD_REQUESTED != ITEM_AVAILABLE
- ITEM_AVAILABLE != ITEM_COLLECTED
- CHECKED_OUT != READ
- READ != UNDERSTOOD
- UNDERSTOOD != TRUE
- DUE_DATE_REACHED != ITEM_LOST
- OVERDUE != STOLEN
- RETURNED != SHELVED
- RENEWAL_REQUESTED != RENEWAL_GRANTED
- INTERLIBRARY_REQUESTED != SUPPLY_APPROVED
- DISPATCHED != RECEIVED
- RECEIVED_BY_BORROWING_LIBRARY != COLLECTED_BY_PATRON
- CUSTODY != OWNERSHIP
- DAMAGED != DESTROYED
- REPLACEMENT_COPY != ORIGINAL_COPY
- CATALOG_RECORD != WORLD_TRUTH
- BORROWING_HISTORY != ACTOR_KNOWLEDGE

## Adventure structures

Circulation creates low-intensity but durable hooks:
- a requested field guide is already checked out to someone who disappeared on an expedition;
- the only circulating copy was returned wet after a storm and must be stabilized before reissue;
- two branches have different catalog records for what appears to be the same edition;
- a remote settlement waits for a rotating box of books that is delayed by a route closure;
- an interlibrary transfer arrives, but its condition report does not match dispatch state;
- a popular manual has a long hold queue while an older edition contains the detail the party actually needs;
- a returned book contains a removable note or map that belongs to a prior borrower, creating a privacy/custody problem without making the library corrupt;
- a branch closes temporarily and its active loans must be reconciled with another location.

## Research conclusion

Ouros benefits from a public-circulation layer because libraries become living institutions rather than static lore shelves. The system should track temporary access, demand, custody and return while refusing three shortcuts: possession does not equal ownership, checkout does not equal knowledge, and reading does not equal truth.