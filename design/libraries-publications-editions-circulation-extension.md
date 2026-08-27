# Libraries, Publications, Editions & Circulation Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already has strong systems for archives, museums, media publication, translation, material provenance, education, public memory, storefronts and courier logistics. This extension fills a narrower continuity gap: authored works can exist in several editions and many copies, copies can circulate independently, annotations and inserts can belong to one copy only, and corrections can change later editions without erasing what earlier readers saw.

The goal is to make libraries, manuals, field guides, research books, local histories, newspapers, pamphlets and other durable works function as persistent world objects without turning reading into an unsupported PTU progression system.

## 1. System ownership boundary

Use the existing systems rather than duplicating them.

`archives-museums-collections-preservation-layer.md` owns:
- accession;
- collection custody;
- catalog records;
- conservation;
- restricted collections;
- reading-room access;
- exhibits and institutional preservation.

`media-communications-information-layer.md` owns:
- information packets;
- public release/distribution events;
- journalistic or institutional publication channels;
- corrections as information distribution;
- audience reach.

`language-translation-symbolic-systems-layer.md` owns:
- transcription;
- decipherment;
- translation;
- interpretive uncertainty.

`material-culture-economy-crafting-layer.md` owns:
- physical-object provenance;
- manufacture;
- repair;
- generic ownership/custody claims.

`commercial-services-storefront-continuity-extension.md` owns sale/service availability.

`courier-parcel-last-mile-logistics-extension.md` owns shipment movement between locations.

This extension owns:
- work identity;
- edition history;
- copy identity;
- circulation state;
- copy-specific annotations/inserts;
- errata and revision relationships;
- reading/reference sessions;
- citation/use relationships;
- publication continuity across revisits.

## 2. Authored work

A work is the intellectual/content identity that can survive across editions and copies.

```yaml
authored_work:
  work_id: null
  title_claim_ids: []
  creator_claim_ids: []
  contributor_claim_ids: []
  work_type: null
  original_language_ref: null
  subject_tags: []
  underlying_claim_ids: []
  creation_date_claim_ids: []
  institution_refs: []
  edition_ids: []
  related_work_ids: []
  public_memory_refs: []
  canon_status: PROPOSED
```

Candidate `work_type` values:
- BOOK
- FIELD_GUIDE
- MANUAL
- RESEARCH_MONOGRAPH
- JOURNAL_ISSUE
- NEWSPAPER_ISSUE
- PAMPHLET
- CATALOG
- DIRECTORY
- LOCAL_HISTORY
- EXPEDITION_REPORT
- TEXTBOOK
- HANDBOOK
- MAP_COMPANION
- OTHER

A work can contain false, uncertain, outdated or disputed claims. Work identity does not confer truth.

## 3. Edition record

An edition is a released rendering of a work at a specific revision state.

```yaml
edition_record:
  edition_id: null
  work_id: null
  edition_kind: null
  source_edition_ids: []
  editor_ids: []
  translator_ref: null
  publication_event_ref: null
  release_time_claim: null
  change_summary_claim_ids: []
  errata_notice_ids: []
  added_section_refs: []
  removed_section_refs: []
  withdrawal_notice_ref: null
  status: CURRENTLY_CIRCULATING
```

Candidate `edition_kind` values:
- FIRST
- REVISED
- EXPANDED
- ABRIDGED
- TRANSLATED
- FACSIMILE
- REPRINT
- ANNOTATED_EDITION
- OTHER

An edition relationship is provenance. It does not imply that the newest edition is automatically correct.

## 4. Copy instance

A copy is one persistent physical or digital instance of an edition when copy-level state matters.

```yaml
copy_instance:
  copy_id: null
  edition_id: null
  underlying_object_ref: null
  medium: null
  identifier_claims: []
  copy_mark_ids: []
  annotation_ids: []
  insert_ids: []
  condition_state: null
  current_custodian_id: null
  current_location_id: null
  current_access_state: AVAILABLE
  circulation_history_ids: []
  case_evidence_refs: []
  collection_object_ref: null
```

Candidate access states:
- AVAILABLE
- CHECKED_OUT
- RESERVED
- STAFF_PROCESSING
- REPAIR
- RESTRICTED
- TRANSFER_IN_PROGRESS
- MISSING
- LOST_CONFIRMED
- WITHDRAWN
- UNKNOWN

Do not instantiate every ordinary copy in the region. Create copy-level identity when history, access, provenance, condition, annotation or custody matters.

## 5. Work availability is not copy availability

Keep these questions separate:

1. Does the work exist?
2. Which editions exist?
3. Which editions are known to this institution or actor?
4. Is a usable copy present here now?
5. Is that copy accessible under current policy?
6. Has the requesting actor actually read it?

A checked-out copy does not erase the work. A missing copy does not prove suppressed knowledge. A digital copy elsewhere does not mean this settlement has access.

## 6. Circulation transaction

```yaml
circulation_transaction:
  circulation_id: null
  copy_id: null
  transaction_type: null
  from_custodian_id: null
  to_custodian_id: null
  from_location_id: null
  to_location_id: null
  authorized_by_ids: []
  started_at: null
  expected_resolution_window: null
  resolved_at: null
  state: PENDING
  condition_before_ref: null
  condition_after_ref: null
  related_courier_shipment_ref: null
  notes_claim_ids: []
```

Candidate transaction types:
- CHECKOUT
- RETURN
- RESERVATION_HOLD
- READING_ROOM_ISSUE
- INSTITUTIONAL_TRANSFER
- LOAN
- DONATION
- SALE
- RECOVERY
- RE_SHELVE
- WITHDRAWAL

Circulation changes custody/location/access. It does not change ownership unless a separate authoritative transfer says so.

Exact loan periods, fines, membership rules or deposits remain canon decisions. Do not generate them by default.

## 7. Annotation record

```yaml
annotation_record:
  annotation_id: null
  copy_id: null
  author_claim_ids: []
  created_at_claim: null
  location_within_work_ref: null
  annotation_type: null
  transcription_ref: null
  translation_ref: null
  content_claim_ids: []
  provenance_evidence_ids: []
  status: UNASSESSED
```

Candidate annotation types:
- MARGINAL_NOTE
- CORRECTION_CLAIM
- QUESTION
- CROSS_REFERENCE
- OWNERSHIP_OR_CUSTODY_MARK
- READING_NOTE
- FIELD_OBSERVATION
- EDITORIAL_MARK
- UNKNOWN

A handwritten correction is a claim. Age, secrecy or handwriting do not make it true.

## 8. Insert record

A loose object found inside a copy is distinct from the edition text.

```yaml
copy_insert:
  insert_id: null
  copy_id: null
  underlying_object_ref: null
  discovered_at: null
  discovered_by_ids: []
  placement_claim: null
  provenance_claim_ids: []
  custody_state_ref: null
  case_ref: null
```

Possible inserts include:
- photograph;
- note;
- receipt;
- map fragment;
- pressed plant;
- ticket;
- correspondence;
- errata slip;
- ownership card.

The generator must not infer who placed an insert without evidence.

## 9. Errata and revision notice

```yaml
revision_notice:
  revision_notice_id: null
  applies_to_work_id: null
  applies_to_edition_ids: []
  notice_type: null
  publisher_or_author_ids: []
  released_at: null
  affected_claim_ids: []
  replacement_claim_ids: []
  reason_claim_ids: []
  publication_ref: null
  status: ACTIVE
```

Candidate types:
- ERRATUM
- CLARIFICATION
- RETRACTION
- WITHDRAWAL
- REVISED_INTERPRETATION
- UPDATED_DATA

A correction does not edit the memories of actors who read the earlier version. Public memory and actor knowledge retain chronology.

## 10. Reading/reference session

```yaml
reading_session:
  session_id: null
  actor_ids: []
  institution_or_location_id: null
  work_id: null
  edition_id: null
  copy_id: null
  started_at: null
  completed_at: null
  consulted_section_refs: []
  note_or_observation_ids: []
  resulting_question_ids: []
  knowledge_event_ids: []
```

A reading session can justify that an actor encountered particular published claims. It cannot grant omniscient knowledge of unread sections.

Do not require per-page simulation. Record only sections or claims relevant to persistent state.

## 11. Citation and source-use edge

```yaml
source_use:
  source_use_id: null
  citing_work_or_report_id: null
  cited_work_id: null
  cited_edition_id: null
  cited_copy_id: null
  cited_claim_ids: []
  access_event_ref: null
  use_type: null
  created_by_actor_id: null
```

Useful `use_type` values:
- SUPPORT
- CONTRAST
- HISTORICAL_CONTEXT
- REPLICATION_ATTEMPT
- DISPUTE
- QUOTED_PUBLIC_CLAIM
- LEAD_GENERATION

This makes “two scholars cite the same title” inspectable at edition level.

## 12. Knowledge boundary

Publication continuity must preserve actor-specific knowledge.

Example:

```text
Year/season A:
Actor 1 reads Edition 1 -> knows claim X.

Later:
Edition 2 changes X to Y.
Actor 2 reads Edition 2 -> knows Y.
Actor 1 does not automatically learn Y.

Public correction is issued.
Actor 1 may receive it only if a channel or revisit makes that plausible.
```

This connects directly to the media/communications and actor-knowledge systems.

## 13. Archive boundary

If a copy becomes historically or evidentially important, register it as a collection object through the archive layer.

Examples:
- first edition with documented provenance;
- field copy carried on a significant expedition;
- annotated copy from a known researcher;
- copy used as case evidence;
- copy whose repair history matters.

The publication extension continues to own its edition/copy identity while Archives owns preservation/custody/catalog state.

## 14. Language boundary

A translated edition must reference the language/translation system.

Do not assume:
- translation equivalence;
- identical ambiguity across languages;
- a translation corrected the underlying historical claim;
- a bilingual actor automatically read both editions.

If an inscription is reproduced in a book, the physical inscription remains a separate symbolic source.

## 15. Media boundary

A book release, newspaper issue, pamphlet distribution or errata notice can generate a `publication` through the media layer.

The edition object records what version exists. Media records how information reached an audience.

A work can exist privately or institutionally before public publication. Conversely, a media report can circulate without ever becoming a durable book/edition object.

## 16. Education and research boundary

Libraries can support teaching and research without granting mechanics.

Possible narrative outputs:
- a research question;
- a field destination;
- an expert referral;
- a bibliography;
- a dispute between interpretations;
- a correction candidate;
- a professional relationship;
- permission to consult another collection.

Possible mechanical outputs such as Skill Ranks, Edges, Features, Tutor Moves, Training effects or Researcher/Chronicler benefits require exact PTU/Caelo rules plus current AutoPTU support.

## 17. Storefront and courier boundary

Selling a work uses Storefront availability.

Shipping a copy uses Courier logistics.

A store being out of stock does not make a work unknown. A courier delay does not rewrite an edition. A lost shipment does not prove every copy is lost.

## 18. Public memory boundary

Some works become culturally important independent of factual reliability.

Track separately:
- circulation/popularity claims;
- public quotations;
- institutional use;
- commemorative status;
- historical influence;
- factual assessment.

A famous inaccurate guide can remain historically important after correction.

## 19. Compression policy

Compress routine actions when no meaningful decision exists:
- ordinary checkout;
- ordinary return;
- routine re-shelving;
- reading a common known reference;
- routine printing/restocking;
- ordinary catalog lookup.

Create playable content when circulation intersects:
- a meaningful provenance gap;
- conflicting editions;
- a copy-specific annotation or insert;
- a research blocker;
- a restricted-access decision already supported by institutional policy;
- a damaged or missing significant copy;
- a correction with downstream consequences;
- a case/evidence chain;
- a relocation/closure/repair affecting access;
- a player-authored research, writing or collecting goal.

## 20. Persistent library state

A library should change slowly and legibly.

Useful state includes:
- currently open wings;
- service desk availability;
- reference collections available here;
- notable reservations/holds;
- significant copies checked out or under repair;
- recent new editions;
- posted corrections;
- staff knowledge/referrals;
- backlog of uncatalogued or returned material;
- exhibit/reading-room handoffs;
- current repair/maintenance state.

Do not spawn a unique entity for every book on every shelf.

## 21. Minecraft/Cobblemon representation

Safe future presentation:
- shelves represent collection zones rather than one-to-one book entities;
- a named lectern/book item can represent a significant accessible copy;
- noticeboards can display edition/revision availability;
- a closed stack can be represented by barriers only when world state says it is closed;
- staff NPC dialogue can point to currently available references;
- a returned significant copy can visibly reappear;
- an errata insert or annotation can be surfaced through UI tied to the authoritative copy ID.

Unsafe shortcuts:
- treating every Minecraft written book as the authoritative knowledge database;
- deleting knowledge when a block is broken;
- making a bookshelf block prove a title is available;
- treating vanilla item ownership as institutional ownership/custody truth;
- granting mechanics because the player clicked a book;
- generating secret lore from random shelf loot;
- resetting loans or copy locations when chunks unload.

## 22. Encounter contract — Closed-Stacks Evacuation

Narrative premise:

A normally nonpublic storage/reading area must be evacuated during a Pokémon disturbance while staff protect people first and defer collection handling until the space is safe.

### FULL version

The intended tactical version may include:
- narrow stack aisles;
- protected fragile zones/objects where rules support them;
- evacuation or clear-route objective;
- blocked routes that change during the encounter;
- forced displacement/interception near narrow passages;
- environmental hazards only when a governing PTU/Caelo rule exists;
- objective-aware AI that may seek escape rather than KO;
- adapter playback preserving evacuated actors and collection state.

Capability dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
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
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

### REDUCED version

Evacuate all readers and staff before tactical resolution. Move the significant copy/object out of the combat grid through authoritative world state or mark it inaccessible. Use a reviewed static adjacent room/corridor with no fragile-object HP, live evacuation, changing hazards, forced movement or object-protection rule. AutoPTU resolves only the ordinary battle. Reopening, condition checks and collection handling occur afterward in library/archive/facility state.

A battle result never decides whether an annotation is authentic or a catalog claim is true.

## 23. Encounter contract — Special-Collection Transfer Interruption

Narrative premise:

A significant copy is being transferred between institutions when a route disturbance blocks the handoff.

### FULL version

The intended version may include:
- protect/escape or break-through objective;
- moving transfer party;
- interception and forced movement;
- route weather/terrain where mechanically supported;
- tactical AI that values the transfer route;
- synchronized courier/custody/battle playback.

Capability dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when required
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

### REDUCED version

Keep the copy and transfer custodian outside the tactical grid. Freeze the interrupted route segment. Resolve a standard legal encounter in a static nearby arena. Only after the authoritative battle outcome does Courier/Circulation state decide whether transfer resumes, reroutes or returns. No escort HP, custom cargo targeting or interception rule is invented.

## 24. Noncombat encounter — Two Editions, One Citation

Premise:

Two reports appear to contradict each other while citing the same title. Investigation discovers that they used different editions with a documented revision between them.

Playable steps can use current narrative state:
- inspect citation metadata;
- locate edition history;
- establish which copies were accessible at each time;
- compare the relevant claims;
- check whether a correction was actually distributed;
- update actor knowledge or a research/case hypothesis.

No tactical engine support is required.

## 25. Engine capability map

Current evidence basis: AutoPTU-Java `c5ef1d72c8a997144d215423e2aab60d706905a9` and AutoPTU `2976b6047702d2e86d367fdad3d648e35ced4145` inspected on 2026-08-26.

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: BLOCKING
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

The latest Chronicler Accuracy resolver is one parity-backed Trainer Feature slice. It does not establish complete Chronicler behavior or the whole Trainer Features/perks family.

## 26. Mechanical safeguards

Do not infer any mechanical benefit from:
- reading duration;
- rarity of a work;
- age of a copy;
- number of books read;
- library membership;
- institutional prestige;
- authorship;
- annotation discovery;
- a corrected edition;
- a field manual;
- a Move name appearing in text;
- a species description;
- an alleged Ability;
- a Legendary story.

Any tactical or progression effect needs an exact governing rule and current implementation support.

## 27. Canon questions

Remain unresolved until explicit review:
- which settlements have libraries and what scale they have;
- whether borrowing is common and how it works;
- printing/copying/digital technology by region;
- institutional publication practices;
- who can authorize restricted access;
- whether public correction/retraction conventions exist;
- which historical/reference works are established canon;
- which traditions remain primarily oral;
- how author rights, ownership or reproduction are handled;
- how many copy instances should be materialized in Minecraft.

This extension must not answer those questions automatically.