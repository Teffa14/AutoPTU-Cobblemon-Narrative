# Ouros Personal Records, Oral History & Preserved Correspondence Extension

Status: proposed systems design. Not established canon.

## Purpose

Ouros already tracks public memory, archives, rumors, testimony, communications, research records and generational continuity. This extension adds a narrower source layer for material authored or spoken by a specific person at a specific time.

It supports:

- diaries and journals;
- field notebooks;
- personal research notes;
- preserved letters/messages after delivery;
- oral-history interviews;
- memoir-like retrospective accounts;
- damaged or incomplete record sets;
- annotations and later revisions;
- derivation from rough personal notes into institutional records.

The extension exists to preserve perspective and provenance. It does not decide historical truth.

## Ownership boundaries

Archives/Museums owns institutional accession, collection custody, cataloguing, conservation and exhibit use.

Media/Communications owns message creation/delivery/publication channels. Once a delivered personal message is preserved as a source object, this extension can track its long-term record state.

Rumor/Testimony owns informal claim transmission and formal testimony handoff.

Public Memory owns community-scale remembered narratives.

Family/Kinship owns confirmed family relations and generational continuity.

Science/Observation owns observations, datasets and institutional research claims.

Case/Authority owns formal evidence status where a case exists.

Found Property owns the ordinary lost-object lifecycle before another specialist system takes custody.

This extension owns the source continuity of exact personal records and oral-history sessions.

## 1. Personal record series

```yaml
personal_record_series:
  series_id: null
  title_or_working_label: null
  primary_author_ids: []
  contributor_ids: []
  record_type: null
  start_time: null
  end_time: null
  subject_scope: null
  entry_ids: []
  fragment_ids: []
  correspondence_thread_ids: []
  annotation_ids: []
  current_custodian_id: null
  physical_or_digital_instance_refs: []
  archive_collection_ref: null
  access_state: PRIVATE
  completeness_state: UNKNOWN
```

Candidate record types:

- DIARY
- FIELD_NOTEBOOK
- RESEARCH_NOTEBOOK
- TRAVEL_JOURNAL
- PERSONAL_LEDGER
- CORRESPONDENCE_BUNDLE
- MEMOIR_DRAFT
- SCRAPBOOK
- SKETCHBOOK
- AUDIO_OR_VIDEO_EQUIVALENT
- AUTHORED_OTHER

A series label is descriptive. It does not establish authenticity or completeness.

## 2. Record entry

```yaml
personal_record_entry:
  entry_id: null
  series_id: null
  author_id: null
  created_at: null
  subject_time_start: null
  subject_time_end: null
  created_location_id: null
  subject_location_ids: []
  source_mode: CONTEMPORANEOUS
  audience_expectation: PRIVATE
  claim_ids: []
  observation_refs: []
  referenced_actor_ids: []
  referenced_pokemon_ids: []
  referenced_object_ids: []
  referenced_location_ids: []
  uncertainty_notes: []
  omitted_or_redacted_sections: []
  later_annotation_ids: []
  authenticity_assessment_refs: []
  access_state: INHERIT_SERIES
```

Candidate source modes:

- CONTEMPORANEOUS
- SAME_DAY_RECONSTRUCTION
- LATER_RECONSTRUCTION
- RETROSPECTIVE
- COPIED_FROM_EARLIER_NOTE
- DICTATED
- UNKNOWN

An entry reports what the author recorded. It does not gain canonical truth from first-person voice.

## 3. Author knowledge boundary

Every entry is bounded by the author’s plausible knowledge at creation time.

The generator must not backfill later revelations into an older entry unless there is an explicit later annotation or revision.

An author may:

- be sincere and wrong;
- omit something deliberately;
- misunderstand a Pokémon behavior;
- misdate an event;
- use an outdated place name;
- record hearsay;
- revise their view later.

These states remain evidence questions, not automatic deception flags.

## 4. Record fragment

```yaml
record_fragment:
  fragment_id: null
  parent_series_id: null
  probable_entry_id: null
  material_instance_ref: null
  discovered_at: null
  discovered_location_id: null
  fragment_order_claim: null
  text_or_content_extent: null
  damaged_regions: []
  missing_before: boolean
  missing_after: boolean
  reconstruction_refs: []
  current_custodian_id: null
  status: FOUND_FRAGMENT
```

Suggested status path:

FOUND_FRAGMENT -> IDENTIFIED -> ASSOCIATED -> RECONSTRUCTED | UNPLACED | DISPUTED

A missing segment remains missing until evidence supports reconstruction. The generator must never fabricate the absent content merely because a quest needs an answer.

## 5. Reconstruction event

```yaml
record_reconstruction:
  reconstruction_id: null
  series_id: null
  fragment_ids: []
  proposed_order: []
  method_refs: []
  completed_by_ids: []
  completed_at: null
  confidence: null
  disputed_order_claims: []
  physical_repair_ref: null
  resulting_readable_entry_ids: []
```

Physical repair and interpretive reconstruction are separate.

A conservator may join paper fragments correctly while the historical order remains uncertain.

## 6. Preserved correspondence

Communications owns sending and delivery. This extension begins when an exact delivered/sent message is retained as a durable personal source.

```yaml
preserved_correspondence:
  correspondence_record_id: null
  underlying_information_packet_ref: null
  delivery_ref: null
  sender_id: null
  intended_recipient_ids: []
  authored_at: null
  delivered_at: null
  retained_by_id: null
  retained_instance_ref: null
  thread_id: null
  reply_to_ref: null
  attachment_refs: []
  annotation_ids: []
  disclosure_state: PRIVATE
  archive_deposit_ref: null
```

Preservation does not prove that the recipient read, believed or answered it.

A missing reply does not prove that no reply was written unless the record set is known complete.

## 7. Correspondence thread

```yaml
correspondence_thread:
  thread_id: null
  participant_ids: []
  message_record_ids: []
  known_gap_windows: []
  inferred_missing_message_claim_ids: []
  current_completeness: UNKNOWN
  subject_tags: []
```

Thread states can include:

- COMPLETE_FOR_WINDOW
- PARTIAL
- ONE_SIDED
- FRAGMENTARY
- UNKNOWN

One-sided correspondence is valid source material. It should not generate invented replies.

## 8. Oral-history session

```yaml
oral_history_session:
  session_id: null
  speaker_ids: []
  interviewer_ids: []
  recorded_at: null
  location_id: null
  subject_scope: null
  prompt_or_question_refs: []
  claim_ids: []
  firsthand_claim_ids: []
  secondhand_claim_ids: []
  uncertainty_notes: []
  withheld_topic_refs: []
  recording_instance_ref: null
  transcript_ids: []
  consent_scope_ref: null
  access_state: RESTRICTED
  archive_deposit_ref: null
```

The layer does not invent consent law. It records whatever consent/access facts Ouros canon later establishes.

An interview is a recorded conversation, not a mind-reading mechanic.

## 9. Transcript version

```yaml
oral_history_transcript:
  transcript_id: null
  session_id: null
  created_by_id: null
  created_at: null
  transcript_type: null
  included_segment_refs: []
  omitted_segment_refs: []
  translation_ref: null
  editorial_note_ids: []
  correction_ids: []
  supersedes_transcript_id: null
  status: CURRENT
```

Candidate transcript types:

- VERBATIM
- LIGHTLY_EDITED
- ABRIDGED
- SUMMARY
- TRANSLATED

A summary is not interchangeable with the recording.

## 10. Retrospective account

```yaml
retrospective_account:
  account_id: null
  author_or_speaker_id: null
  created_at: null
  event_window_refs: []
  source_basis_refs: []
  memory_gap_notes: []
  claim_ids: []
  later_correction_ids: []
```

Retrospective accounts can be valuable even when incomplete. Their distance from the event belongs in provenance.

## 11. Rough note -> formal record derivation

```yaml
record_derivation:
  derivation_id: null
  source_record_ids: []
  destination_record_ref: null
  compiler_ids: []
  created_at: null
  transformation_type: null
  preserved_claim_links: []
  omitted_claim_links: []
  normalization_notes: []
```

Candidate transformation types:

- FIELD_NOTE_TO_RESEARCH_REPORT
- JOURNAL_TO_MEMOIR
- INTERVIEW_TO_ARCHIVE_TRANSCRIPT
- LETTER_BUNDLE_TO_EXHIBIT_CITATION
- PERSONAL_NOTE_TO_CASE_LEAD
- NOTEBOOK_TO_PUBLIC_MAP_SOURCE

The destination record never replaces the source.

## 12. Annotation

```yaml
record_annotation:
  annotation_id: null
  target_record_id: null
  annotator_id: null
  created_at: null
  annotation_type: null
  claim_ids: []
  visibility: PRIVATE
  authority_scope: personal
```

Candidate types:

- AUTHOR_CORRECTION
- AUTHOR_LATER_NOTE
- ARCHIVIST_NOTE
- READER_NOTE
- TRANSLATOR_NOTE
- RESEARCHER_CITATION
- DISPUTE_NOTE
- ACCESS_NOTE

A margin note by a later reader must never be confused with original text.

## 13. Access and disclosure

```yaml
personal_record_access:
  access_id: null
  record_or_series_id: null
  holder_or_controller_id: null
  viewer_id: null
  access_scope: null
  granted_at: null
  expires_at: null
  basis_ref: null
  restrictions: []
  status: ACTIVE
```

Suggested access states:

- PRIVATE
- SHARED_WITH_NAMED_ACTORS
- INSTITUTION_RESTRICTED
- READING_ROOM_ONLY
- SEALED
- PUBLIC
- UNKNOWN

Finding a diary does not automatically authorize reading it.

Owning or holding a physical object does not automatically establish publication rights.

The exact legal/cultural rules remain canon questions.

## 14. Discovery event

```yaml
record_discovery:
  discovery_id: null
  record_instance_ref: null
  discovered_by_ids: []
  discovered_at: null
  location_id: null
  initial_access_state: null
  physical_condition_ref: null
  custody_handoff_ref: null
  immediately_readable: false
```

Discovery time matters.

A document found after a historical event can explain or reframe it without retroactively preventing what already happened.

## 15. Source comparison packet

```yaml
source_comparison:
  comparison_id: null
  question_id: null
  source_record_ids: []
  oral_history_session_ids: []
  observation_ids: []
  agreement_edges: []
  conflict_edges: []
  dependency_edges: []
  unresolved_claim_ids: []
  synthesis_record_ref: null
```

This supports player-facing investigation without a hidden truth score.

Useful outputs include:

- two records independently place an actor in the same location;
- three retellings all derive from one earlier letter;
- a later memoir contradicts the author’s contemporaneous notebook;
- a family story and an old field journal agree on the existence of a settlement but disagree on why it was abandoned;
- the oldest source is not necessarily the most accurate source.

## 16. Personal notebook as character project

A player or NPC can maintain a persistent notebook.

```yaml
character_notebook_project:
  project_id: null
  author_id: null
  notebook_series_id: null
  topic_scope: null
  active_question_ids: []
  resolved_question_ids: []
  observation_refs: []
  map_refs: []
  sketch_refs: []
  source_citation_refs: []
  last_updated_at: null
```

This is narrative/world state.

It does not grant:

- Skill Ranks;
- Edges;
- Features;
- Accuracy;
- damage;
- capture bonuses;
- tactical foresight;
- automatic Pokédex completion;
- guaranteed recall.

Any mechanical benefit requires exact PTU/Caelo and AutoPTU authority.

## 17. Pokémon in personal records

A record may contain:

- species identifications;
- individual Pokémon refs where identity is supported;
- sketches/photos;
- observed behaviors;
- claimed encounters;
- old nicknames;
- ownership/custody claims;
- uncertain descriptions.

The record does not establish a Pokémon’s current state.

An old diary saying a Pokémon lived at a location does not spawn that Pokémon there today.

A record calling a Pokémon dangerous does not grant it combat bonuses.

A historical ownership claim does not create current ownership.

## 18. Record succession after absence/death/retirement

This extension can preserve custody history of personal records when an author becomes absent, retires, relocates or dies through an independently confirmed canon event.

It must not infer any of those states itself.

Possible handoffs:

- author keeps records;
- records remain at residence;
- family/household custody;
- institutional deposit;
- found-property intake;
- case/evidence custody;
- unknown location.

Inheritance rights are not invented.

## 19. Institutional use

Archives can accession a personal series.

Science can cite a field notebook.

Public Memory can cite an interview.

Media can publish an excerpt when authorized.

Case/Authority can ingest a relevant source through its own evidence rules.

Family/Kinship can reference a generational record.

Library/Edition systems can later manage a published edition derived from the source.

The personal-source object remains intact beneath each handoff.

## 20. Minecraft/Cobblemon presentation

Use as much safe platform functionality as possible.

SAFE_REUSE candidates:

- written books and lecterns;
- bookshelves/containers/item frames for exact source placement;
- signs, paintings/maps and display props;
- NPC entities for interviews;
- Cobblemon Pokémon entities/models/animations/cries when contextual to a scene;
- particles and sounds for interaction feedback;
- UI for reading entries, comparing sources and reviewing annotations;
- client/server sync;
- item/block/entity persistence hooks;
- location and timestamp observations from the overworld.

ADAPTER_REQUIRED:

- mapping a displayed book/item to an Ouros record instance;
- keeping record identity durable across chunk unloads;
- enforcing access/redaction state in UI;
- recording interview/annotation interactions into Ouros world state;
- projecting a later archive/exhibit state back into Minecraft;
- instantiating AutoPTU only when Ouros explicitly creates a battle.

BATTLE_AUTHORITY_FORBIDDEN:

- Cobblemon selecting combatants from people/Pokémon present in the interview/archive scene;
- Cobblemon battle state changing historical record truth;
- battle HP/status being treated as proof of a historical diagnosis;
- capture resolving ownership claims in an old record;
- a Cobblemon battle participant list being treated as the witness list of a past event.

Required authority flow:

`Ouros source/world state -> explicit encounter composition if needed -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon projection`

## 21. Encounter integration

Most personal-record gameplay should remain noncombat.

Combat enters only when a separate current-world condition creates it.

Examples:

- a dangerous location must be made safe before a record can be inspected;
- an interview site is interrupted by a current incident;
- a field notebook lies beyond a route currently occupied by territorial Pokémon;
- an archive building needs evacuation during an unrelated event.

The battle result never authenticates the source.

## 22. Anti-false-completion rules

- one diary does not prove canonical history;
- one oral account does not prove a community memory;
- three retellings can still derive from one source;
- a damaged page does not authorize invented missing text;
- a later annotation is not original text;
- a transcript summary is not the recording;
- discovery does not equal authorization to read;
- custody does not equal ownership;
- publication does not make a claim true;
- a battle beside a document does not prove the document’s contents;
- an old Pokémon sighting does not create a current spawn;
- finding a record late does not rewrite earlier world state.

## 23. Canon questions deliberately unresolved

- Which writing/recording technologies exist by region?
- Which cultures treat personal journals as private, family-held or institutionally valuable?
- What oral-history traditions exist?
- Which institutions solicit interviews?
- Who can authorize transcription, publication or archival deposit?
- Are there sealed/embargoed records?
- What translation conventions exist?
- Can player-authored notebooks become persistent world objects?
- What happens to records after death/retirement/relocation?
- Which personal records already exist in established Ouros canon?

No answer is established by this extension.