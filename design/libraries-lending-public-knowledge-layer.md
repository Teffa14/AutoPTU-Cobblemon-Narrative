# Libraries, Lending, and Public Knowledge Layer

Status: PROPOSED / NON-CANON
Pass: 130
Date: 2026-08-23

## Purpose

This layer owns ordinary public access to reusable knowledge resources: library sites, holdings, editions, copies, circulation, reference service, holds, mobile service, and resource sharing between institutions.

It exists so Ouros can remember not only that information exists, but how people can access it, which version they see, where a specific copy is, and whether that access is temporary, public, restricted, or mediated through another institution.

It must not become a second Archives system, a second Museum system, or a generic truth database.

## Authority boundaries

### This layer owns

- library sites and service points;
- library-system membership and branch structure;
- bibliographic work identity;
- content expressions / translations / revisions as access objects;
- publication editions;
- circulating or reference copy identity;
- library holdings;
- copy availability;
- lending, renewal, return, hold, and missing-copy events;
- resource-sharing requests between institutions;
- reference-service interactions;
- mobile-library schedules and service stops;
- reading-room access scope;
- library collection profiles and acquisition/withdrawal decisions;
- public catalog state;
- copy-specific annotations and condition when relevant to use;
- controlled digitization/access links when the Digital Systems layer stores the actual file.

### Other layers remain authoritative for

- institutional evidence and archival records: Archives / Institutional Memory;
- accession, conservation, exhibition, museum loans: Museums / Collections;
- language competence and translation provenance: Languages / Translation;
- curricula and learning outcomes: Education;
- scientific truth claims and datasets: Science;
- persistent physical provenance outside ordinary circulation: Material Culture;
- files, backups, access-control infrastructure, digital incidents: Digital Systems;
- parcel movement between sites: Postal / Courier Logistics;
- actor identity and aliases: Identity / Record Linkage;
- credentials and formal restricted access: Credentials / Permissions;
- public popularity and collective memory: Public Memory;
- sacred/restricted cultural authority: Sacred Sites / relevant authored cultural layer;
- ownership and financial transactions: Finance / Markets / Currency;
- copyright or legal doctrine: unresolved; do not invent.

## Core rule

Library availability is an access state, not a truth state.

A library can hold:

- correct current research;
- obsolete but historically useful editions;
- competing interpretations;
- fiction;
- folklore;
- disproven hypotheses;
- translations of varying quality;
- public-domain style guides;
- maps correct only for an earlier geography revision;
- field notes later superseded by better surveys.

The existence of a resource never promotes its contents to canon.

## Bibliographic identity model

### `KNOWLEDGE_WORK`

Represents the persistent intellectual/content identity across versions.

Suggested fields:

```text
work_id
canonical_catalog_title
work_type
known_creator_claims[]
subject_tags[]
origin_date_claim
status
relationships_to_other_works[]
```

`canonical_catalog_title` is a catalog convenience, not proof of original title or authorship.

### `CONTENT_EXPRESSION`

Represents a specific language, translation, revision, adaptation, transcription, or content-level form of a work.

```text
expression_id
work_id
language_id
writing_system_id
revision_label
translator_or_editor_claims[]
source_expression_id?
created_at_or_claimed_date
notes
```

The Languages layer owns translation quality, terminology, source linkage, and actor comprehension.

### `PUBLICATION_EDITION`

Represents an issued/published version that can have multiple copies.

```text
edition_id
expression_id
publisher_or_issuing_body_id?
edition_label
publication_date_or_claim
printing_or_release_context
map_or_data_cutoff_date?
known_corrections[]
status
```

An edition can remain useful after being superseded.

### `LIBRARY_COPY`

Represents one physical or controlled copy.

```text
copy_id
edition_id
owning_or_stewarding_library_id
home_site_id
current_site_id
copy_type: PHYSICAL | CONTROLLED_DIGITAL_ACCESS
condition_state
circulation_state
special_copy_notes[]
material_item_id?
```

For ordinary interchangeable copies, implementation may use count bands rather than unique IDs. Promote a copy to persistent identity when its annotations, provenance, damage, loan history, historical role, or uniqueness matters.

## Copy promotion rule

Do not assign unique persistent identity to every background paperback.

Promote a copy when at least one of these becomes narratively relevant:

- unique or scarce surviving copy;
- copy-specific annotations;
- physical evidence or inserted material;
- historical ownership/use is important;
- significant damage or restoration;
- interregional special loan;
- disputed custody;
- copy becomes artifact-level heritage;
- players intentionally preserve or modify it;
- specific copy is repeatedly referenced by Chronicle.

## Library site model

### `LIBRARY_SITE`

```text
library_site_id
institution_id
name
site_type
location_id
service_hours_profile_id?
access_profile_id
collection_profile_id
active_since
closed_or_repurposed_at?
```

Possible site types:

- central library;
- branch;
- community reading room;
- school/shared branch;
- research reading room;
- mobile service vehicle;
- ferry/rail deposit collection;
- seasonal outpost;
- special-collection room;
- digital-access terminal service.

A site may close while the institution and holdings continue elsewhere.

## Holdings

### `HOLDING_RECORD`

```text
holding_id
library_system_id
edition_id
copy_count_or_band
reference_only_count?
loanable_count?
digital_access_count?
known_copy_ids[]
last_verified_at
```

A catalog claim is not automatically inventory truth. Reconciliation may find stale holdings, mis-shelved material, or copies in transit.

### Availability

Possible states for a persistent copy:

- `AVAILABLE`
- `ON_LOAN`
- `ON_HOLD_SHELF`
- `IN_TRANSIT`
- `REFERENCE_ONLY`
- `REPAIR`
- `DIGITIZATION`
- `CONSERVATION_HANDOFF`
- `MISSING`
- `LOST`
- `WITHDRAWN`
- `RESTRICTED_BY_SCOPE`

Do not derive `STOLEN` from `MISSING`.

## Circulation

### `CIRCULATION_EVENT`

```text
circulation_event_id
copy_id
patron_actor_id_private?
event_type
site_id
occurred_at
expected_due_at?
recorded_at
staff_or_system_actor_id?
notes_private?
```

Possible event types:

- checkout;
- renewal;
- return;
- manual return discovered;
- hold pickup;
- internal transfer;
- declared missing;
- found;
- lost decision;
- withdrawal from circulation.

### Privacy rule

Borrowing history is private by default.

The public world can know that a copy was unavailable, damaged during a flood, or returned decades late without receiving a public list of everyone who borrowed it.

A Case may request or gain access to circulation evidence only through whatever mandate/privacy rules Ouros eventually defines. Do not expose logs merely because the player asks a librarian.

## Holds and requests

### `HOLD_REQUEST`

```text
hold_request_id
patron_actor_id
requested_work_or_edition_id
acceptable_expressions[]
acceptable_editions[]
preferred_site_id
created_at
status
assigned_copy_id?
```

Possible states:

`QUEUED`, `COPY_ASSIGNED`, `READY`, `FULFILLED`, `EXPIRED`, `CANCELLED`, `UNAVAILABLE`.

A hold on a work does not necessarily demand a particular physical copy.

## Resource sharing / interlibrary loan

### `RESOURCE_SHARING_REQUEST`

```text
request_id
requesting_library_id
supplying_library_id?
work_or_edition_id
specific_copy_required?
request_scope
approval_state
fulfillment_state
postal_consignment_id?
requested_at
fulfilled_at?
return_due_at?
```

Separation:

`REQUESTED → LOCATED → APPROVED → PREPARED → IN_TRANSIT → RECEIVED → AVAILABLE_TO_REQUESTOR → RETURN_IN_TRANSIT → RETURNED`

Each state may fail independently.

The Postal layer owns physical shipment. Library state owns why the item is moving and whether the request is fulfilled.

## Reference service

### `REFERENCE_REQUEST`

Reference work should be a first-class low-drama interaction.

```text
reference_request_id
requestor_actor_id?
question_summary
scope
sources_consulted[]
response_version
confidence
follow_up_needed
created_at
```

Reference responses should distinguish:

- catalog fact;
- quoted source claim;
- librarian synthesis;
- unresolved conflict;
- referral to specialist institution;
- answer unavailable from current holdings.

### Design goal

Reference work should sometimes prevent content escalation.

Examples:

- obsolete route guide explains a rumor;
- place-name change resolves a supposed contradiction;
- two taxonomic names are linked by a later revision;
- a disaster warning belongs to an old event;
- an apparent prophecy is identified as a later retelling;
- a “missing” article is found under a translated title.

A satisfying result can be `NO QUEST REQUIRED`.

## Collection profile

### `LIBRARY_COLLECTION_PROFILE`

```text
profile_id
library_system_id
subject_strengths[]
audience_scopes[]
languages[]
acquisition_priorities[]
known_gaps[]
reference_only_categories[]
withdrawal_principles[]
```

This is descriptive institutional state, not a moral ranking.

A small fishing-town branch can have an exceptional local maritime collection and little advanced medicine. A university library can be broad but lack local oral-history transcriptions held by a community reading room.

## Acquisition

Acquisition may come from:

- purchase;
- donation;
- institutional deposit;
- exchange;
- author/publisher gift;
- transfer from closed branch;
- digitized-access agreement;
- player donation, if accepted.

Acceptance must be distinct from physical receipt.

A donated box can arrive and remain unprocessed or be declined.

Rare artifacts with uncertain provenance should hand off to Material Culture / Museums / Archives for assessment instead of silently entering circulation.

## Withdrawal and replacement

A library may withdraw a copy because:

- physically unusable;
- duplicate surplus;
- replaced by a newer edition;
- content available through another service;
- site closure;
- copy promoted to preservation collection;
- temporary condition problem.

Withdrawal does not delete Chronicle or bibliographic identity.

An obsolete scientific edition may remain intentionally retained for historical comparison.

## Annotations and inserted material

A `COPY_NOTE` can record:

```text
note_id
copy_id
note_type
location_in_copy
observed_content_summary
author_claim?
date_claim?
observation_provenance
```

Possible note types:

- handwritten annotation;
- marginal correction;
- field route note;
- owner mark;
- pressed plant/sample handoff;
- inserted letter;
- damaged/missing page;
- old circulation slip;
- repair note.

An annotation is not part of the work unless separately published as a new expression/edition.

If inserted material is evidence, move its authority to Cases/Archives/Science as appropriate while preserving the copy relationship.

## Maps and field guides

Libraries connect strongly to Cartography, Taxonomy, Metrology, Ecology, and Languages.

A map or guide must preserve its cutoff date and applicable revision context.

Example:

A 14-year-old field guide can correctly show:

- an old river channel;
- an older species name;
- a bridge that later failed;
- a migration stopover that has since shifted;
- a pre-redevelopment district boundary.

The guide is not “wrong” merely because the world changed.

## Sensitive information

Some knowledge access can be scoped without implying secrecy for dramatic effect.

Examples:

- precise nesting coordinates;
- health records;
- unpublished research participant data;
- sacred/restricted cultural materials;
- endangered-site location details;
- infrastructure security details;
- active Case evidence.

The owner layer decides whether access is restricted. The Library layer enforces the service scope it receives.

## Mobile libraries

### `MOBILE_LIBRARY_ROUTE`

```text
route_id
service_unit_id
stops[]
schedule_profile
seasonal_constraints[]
route_revision_history[]
capacity_band
service_scope
```

A mobile route can change because of:

- rail opening;
- bridge closure;
- snow season;
- settlement growth;
- school schedule;
- ferry timetable;
- staffing;
- vehicle maintenance;
- wildfire/flood recovery;
- a new permanent branch.

Changing the route should preserve earlier service history.

## Community use

Libraries can host:

- reading circles;
- public lectures;
- research help;
- children’s programs;
- language-learning groups;
- local-history displays;
- small exhibitions;
- public-access terminals;
- noticeboards;
- temporary disaster information points;
- quiet study;
- club meetings.

Hosting does not imply sponsorship, endorsement, membership, or ownership of the hosted group.

## Pokémon participation

Possible authored roles:

- a Pokémon voluntarily assists with shelving or transport;
- a recurring wild Pokémon uses a courtyard or roof;
- a partner helps a patron retrieve material under a verified field capability;
- a Chatot imitates recurring sounds in a reading room;
- a Rotom interacts with a catalog terminal under species-specific authored behavior.

Guardrails:

- helper role does not imply institutional ownership;
- species does not imply job competence;
- Chatot mimicry does not prove comprehension;
- Rotom presence does not prove network access or data authority;
- carrying books does not establish PTU carrying capacity without rules;
- library employment does not grant Trainer Features.

## Minecraft projection

Minecraft is presentation and interaction, not catalog truth.

The adapter may render:

- shelves by broad collection type;
- call-number/category signage;
- circulation desk;
- reading tables;
- hold shelf;
- mobile library vehicle;
- special-collection room;
- return slot;
- public catalog terminals;
- book carts;
- damage/repair state;
- temporary closure signs.

The adapter must not derive authoritative holdings by scanning book blocks or chests.

The server should project library state into Minecraft, not reconstruct the library database from loaded blocks.

## Offline progression

Safe offline progression:

- due dates advance;
- scheduled mobile stops can occur in abstract state;
- holds can become ready;
- resource-sharing shipments can advance through Postal state;
- known repairs can complete if dependencies are met;
- public schedules can update from authored rules.

Unsafe automatic progression:

- inventing which books a named NPC read;
- inferring ideological change from borrowing;
- generating rare-manuscript discoveries from random shelf rolls;
- auto-promoting rumors into truth;
- silently destroying unique copies because a chunk unloaded;
- changing PTU mechanics because a new manual entered the collection.

## Failure-forward states

Library stories should not collapse into binary success/failure.

Possible outcomes:

- requested work unavailable locally but located elsewhere;
- old edition found, current edition missing;
- copy found but too damaged for ordinary handling;
- translation exists but lacks latest revision;
- patron gets partial answer plus referral;
- interlibrary loan delayed by route closure;
- unique annotation found but author uncertain;
- collection remains inaccessible while digitization/access copy is created;
- library correctly concludes it cannot answer the question.

## Engine capability mapping

Library systems themselves are overworld state.

### Permanent categories

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

### Important live evidence

AutoPTU-Java head inspected for Pass 130: `7de79dcd30b241d439724050fb24ee893a7c5c63`.

The latest forced-movement slice can parse and freeze a Push/Pull instruction with distance. It explicitly does not move combatants. Complete movement remains BLOCKING.

AutoPTU Python head inspected: `99ba07ea47b8896d96bd37f6c06cffb8695f69bb`.

Its latest visible change is Career capture-overflow regression coverage and does not alter the tactical category map.

## Encounter contracts

### `LIB-130-A — Flooded Reading Annex Evacuation`

Narrative premise:

A water incident reaches a lower annex while staff and patrons are still clearing the area. Collection recovery matters, but people/Pokémon have priority.

FULL:

- dynamic evacuation routes;
- civilian and staff movement;
- water zones changing access;
- wild Pokémon can withdraw;
- collection carts may block or open routes without being combatants.

Dependencies:

- complete movement: BLOCKING;
- terrain/weather/hazards/zones/reactions: BLOCKING if rising water is tactical;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING;
- targeting and base static movement: VERIFIED for ordinary combat once a legal snapshot exists.

REDUCED:

Resolve the flood revision and evacuation in world state. Move important copies to a safe state. Freeze a dry room/courtyard as the combat arena. AutoPTU resolves only actual combatants. After battle, compute library condition and service recovery outside the grid.

### `LIB-130-B — Mobile Library Chokepoint`

Narrative premise:

A mobile service unit is stranded on a route. The point is restoring access to remote readers, not protecting a magical quest vehicle.

FULL dependencies:

- complete movement / interception: BLOCKING;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING;
- environmental category only if a real tactical hazard is authored.

REDUCED:

Secure staff and vehicle outside the grid. Run a static chokepoint battle only if confrontation remains. Travel/Road/Rail state reopens the route afterward.

### `LIB-130-C — Reading Courtyard Wildlife Intrusion`

Narrative premise:

A recurring urban-wildlife group enters a courtyard during a crowded program. Withdrawal is preferred if possible.

FULL dependencies:

- complete movement: BLOCKING;
- AI tactical policy: BLOCKING for `WITHDRAW`, `REACH_EXIT`, `AVOID_CIVILIANS`;
- adapter/playback: BLOCKING.

REDUCED:

Evacuate patrons in world state and allow wildlife a non-combat withdrawal resolution. If combat remains unavoidable, open a static legal arena with only relevant combatants.

### `LIB-130-D — Reference Desk Misinformation`

No battle dependency.

A rumor appears to indicate a dangerous newly discovered site. A librarian/reference worker traces it to an old place name and an obsolete disaster notice. Correct outcome: update the public record and close the matter without generating an expedition.

## Non-inference rules

Never infer:

- ownership of a work from possession of a copy;
- truth from publication;
- endorsement from holdings;
- literacy from library membership;
- General Education/Pokémon Education from borrowing;
- Trainer Features from professional role;
- intent from borrowing history;
- theft from a missing scan;
- destruction of knowledge from destruction of one copy;
- translation accuracy from availability;
- current geography from an old map;
- current taxonomy from an old Pokédex/guide;
- Move/Ability/Feature knowledge from reading a manual;
- supernatural power from a rare book;
- secure access from a Minecraft door being open;
- public access from a Minecraft shelf being visible.

## Canon questions intentionally unresolved

- Which settlements begin with libraries, reading rooms, or mobile service?
- Is there one regional catalog or several institution-specific catalogs?
- What identity/credential is needed for ordinary borrowing?
- Which materials can circulate?
- How long are loans and how are losses handled?
- What patron history is retained and who can see it?
- Which languages have broad publishing ecosystems?
- Are there publisher, printer, bookseller, or academic-press institutions already in canon?
- How do player clubs/businesses found or support libraries?
- What kinds of sensitive knowledge require scoped access?
- Which rare books are artifacts rather than circulating resources?
- How is digitization represented at the region's technology level?
- Does PTU/Caelo define any mechanical benefit for reference material, research libraries, or study outside already-known Skills/Features?

Until those decisions are authored, this layer remains PROPOSED and mechanically conservative.