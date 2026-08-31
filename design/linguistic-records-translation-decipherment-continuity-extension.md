# Ouros linguistic records, translation, and decipherment continuity extension

Status: PROPOSED SYSTEMS DESIGN / NOT CANON
Date: 2026-08-31
Pass: 169

## Purpose

Ouros already preserves archaeological inscriptions as observed site features, archival records as documentary objects, physical artifacts through Material Culture, names through Human Identity, and research claims through Scientific Research. This extension preserves the linguistic lineage between a source witness and later readings of it.

The design goal is durable uncertainty with provenance. A wall, tablet, letter, recording, sign, field notebook, ritual formula, route marker, or spoken testimony may have one physical source while accumulating many transcriptions, transliterations, translations, glosses, interpretations, corrections, and disputed readings across decades.

This layer is dormant until canon or an authoritative observed event establishes a linguistic source. It does not create languages, scripts, ancient peoples, dialects, translation institutions, magical writing, or literacy rules by itself.

## Authority boundaries

Archaeology remains authoritative for site context and archaeological observation. Archives remains authoritative for preservation/access. Material Culture remains authoritative for the physical item instance. Human Identity remains authoritative for names and identity linkage. Communications remains authoritative for whether a message was sent/received. Scientific Research may own a formal research project studying the text. Chronicle/world facts remain authoritative for what actually happened historically.

This extension owns representation lineage: what symbols/sounds were observed, how somebody represented them, what translation they proposed, what confidence they expressed, and how later evidence revised that reading.

## Core records

```yaml
linguistic_source_witness:
  witness_id: null
  source_type: null
  physical_object_or_record_ref: null
  archaeological_observation_ref: null
  location_ref: null
  observed_medium: null
  observed_extent: null
  damage_or_missing_sections: []
  image_audio_documentation_refs: []
  language_claim_ids: []
  script_claim_ids: []
  provenance: []
```

Candidate source types include inscription, manuscript, letter, sign, map_label, recording, oral_testimony, field_note, copied_text, monument, ritual_text, graffiti, device_display, and unknown.

```yaml
script_identification_claim:
  claim_id: null
  witness_id: null
  claimant_ids: []
  proposed_script_ref: null
  proposed_period: null
  evidence_refs: []
  counterevidence_refs: []
  confidence: null
  status: PROPOSED
  created_at: null
```

```yaml
language_identification_claim:
  claim_id: null
  witness_id: null
  claimant_ids: []
  proposed_language_or_variety_ref: null
  evidence_refs: []
  counterevidence_refs: []
  confidence: null
  status: PROPOSED
```

Script and language identification remain separate. A shared writing system does not prove a shared language.

## Transcription lineage

```yaml
transcription_version:
  transcription_id: null
  witness_id: null
  parent_transcription_id: null
  transcriber_ids: []
  transcription_system_ref: null
  segment_records: []
  unreadable_ranges: []
  restored_ranges: []
  alternative_readings: []
  confidence_notes: []
  supporting_documentation_refs: []
  created_at: null
  status: ACTIVE
```

A transcription records observed symbols/sounds in a chosen representation. It must preserve uncertainty rather than silently filling damage.

## Transliteration and normalization

```yaml
transliteration_version:
  transliteration_id: null
  source_transcription_id: null
  parent_transliteration_id: null
  system_ref: null
  author_ids: []
  aligned_segments: []
  ambiguous_mappings: []
  confidence_notes: []
  created_at: null
```

```yaml
normalization_version:
  normalization_id: null
  source_transcription_or_transliteration_id: null
  author_ids: []
  normalized_segments: []
  editorial_expansions: []
  uncertain_forms: []
  created_at: null
```

Not every language requires transliteration or normalization. These records are optional.

## Lexical and corpus evidence

```yaml
linguistic_attestation:
  attestation_id: null
  source_segment_ref: null
  proposed_form: null
  proposed_lemma_ref: null
  proposed_sense_ref: null
  grammatical_claims: []
  parallel_attestation_refs: []
  confidence: null
  author_ids: []
```

```yaml
lexicon_version:
  lexicon_version_id: null
  language_or_variety_ref: null
  parent_version_id: null
  entry_ids: []
  compiler_ids: []
  scope_note: null
  evidence_cutoff: null
  created_at: null
```

A lexicon is evidence infrastructure. It does not define eternal meaning. Entries can gain new senses, dialect labels, obsolete forms, or disputed etymologies.

## Translation versions

```yaml
translation_version:
  translation_id: null
  source_representation_ref: null
  target_language_ref: null
  parent_translation_id: null
  translator_ids: []
  aligned_segments: []
  supplied_words: []
  uncertain_passages: []
  untranslatable_passages: []
  literal_rendering_refs: []
  idiomatic_rendering_refs: []
  confidence_notes: []
  created_at: null
  status: ACTIVE
```

Multiple translations may coexist. Publication or institutional endorsement does not automatically select one as world truth.

## Interpretation claims

```yaml
linguistic_interpretation_claim:
  interpretation_id: null
  source_translation_ids: []
  source_witness_ids: []
  claimant_ids: []
  proposition: null
  evidence_refs: []
  counterevidence_refs: []
  confidence: null
  status: PROPOSED
  related_historical_claim_ref: null
```

Example: a translation may plausibly say “return at first light,” while the interpretation that it describes an annual pilgrimage is a separate historical claim.

## Spoken language and interpretation episodes

```yaml
interpretation_episode:
  episode_id: null
  speaker_ids: []
  listener_ids: []
  interpreter_ids: []
  source_language_claim_ref: null
  target_language_ref: null
  source_recording_ref: null
  interpreted_summary_ref: null
  omissions_or_uncertainties: []
  setting_ref: null
  timestamp: null
```

Do not infer exact wording from a summary. Do not infer fluency from one successful exchange. A living speaker may know a local variety that an institutional glossary does not capture.

## Decipherment episodes

```yaml
decipherment_episode:
  decipherment_id: null
  subject_witness_ids: []
  actor_ids: []
  input_evidence_refs: []
  method_summary: null
  discovered_correspondence_refs: []
  output_transcription_ids: []
  output_translation_ids: []
  unresolved_segments: []
  status: PARTIAL
  chronicle_event_ref: null
```

Suggested states: ATTEMPTED, PARTIAL, SUBSTANTIAL, CONTESTED, REVISED.

A decipherment can improve available readings without making every text in the script readable. A bilingual or repeated formula may solve one subset and leave other genres unresolved.

## Revision and dispute

```yaml
linguistic_record_revision:
  revision_id: null
  affected_record_ids: []
  revision_type: null
  author_ids: []
  reason: null
  new_record_ids: []
  evidence_refs: []
  created_at: null
```

Candidate reasons: new_witness, better_image, damaged_area_reexamined, bilingual_parallel, living_speaker_evidence, dialect_reclassification, scribal_error_hypothesis, forgery_evidence, dating_revision, software_or_display_error, prior_copy_error.

Old readings remain historically queryable. A correction changes the current best record; it does not erase what earlier actors read and acted upon.

## Actor knowledge

Actor knowledge must point to the version actually encountered.

```yaml
linguistic_knowledge_record:
  actor_id: null
  known_witness_ids: []
  known_transcription_ids: []
  known_translation_ids: []
  known_interpretation_ids: []
  direct_language_experience_refs: []
  source_event_ids: []
```

A researcher who read an obsolete translation twenty years ago may act consistently with that old reading until a correction reaches them.

## Generation boundaries

The generator may create linguistic questions only from existing source witnesses, authored language relationships, observed speech differences, archival records, archaeological observations, or established community practices. It may propose alternative readings when provenance supports uncertainty. It may not manufacture an ancient language merely to create a puzzle.

For living languages, current community use and speaker evidence must remain distinct from outsider reconstruction. A language may change, borrow vocabulary, split into varieties, standardize, revive, or lose particular domains of use without being reduced to a mystery cipher.

Minecraft-visible text is presentation unless Ouros explicitly authored the underlying source record. Localization files are UI/presentation and must not silently become in-world language evidence.

## PTU/Caelo boundary

No generic fluency, literacy, translation, decipherment, interpreter, Unown-reading, or ancient-language mechanic is assumed by this extension. General Education, Occult Education, Telepathy, Researcher, Chronicler, Sage, Runemaster, Pokédex functions, Abilities, Items, and Features must be validated individually against PTU/Caelo and current engine support before producing mechanical effects.

A narrative Skill Check may be authored by future canon only when the governing rules specify its Skill, difficulty, information policy, consequences, repeatability, and interaction with Features. This extension does not invent those numbers.

## Encounter contracts

### Inscription Chamber Under Threat

Full intent: characters are interpreting a multi-witness inscription while hostile actors or Pokémon create positional pressure. Optional physical mechanisms may react to correctly interpreted steps.

Dependencies: targeting/footprints/range/LoS VERIFIED; base movement legality VERIFIED; action economy/initiative VERIFIED; complete movement PARTIAL if displacement or Intercept affects access; lifecycle PARTIAL for multi-round puzzle state; move-specific behavior/abilities/items/Trainer Features PARTIAL for selected combat content; terrain/weather/hazards/zones/reactions BLOCKING if chamber mechanisms are tactical; AI legal-action infrastructure VERIFIED; AI tactical policy BLOCKING for objective awareness; adapter/playback BLOCKING for semantic puzzle state.

Reduced version: resolve transcription/translation as Narrative state before or after a conventional audited battle. Protected text surfaces remain outside BattleSpec. AutoPTU may return `IMMEDIATE_INSCRIPTION_CHAMBER_APPROACH_CLEAR`. It cannot establish a reading or open a narrative seal by itself.

### Interpreter Withdrawal Through Ruins

Full intent: protect an interpreter while withdrawing through a dangerous site, possibly preserving notes or images.

Dependencies: complete movement PARTIAL for escort/Intercept/forced movement; lifecycle PARTIAL; hazards/zones/reactions BLOCKING if the route changes; tactical policy BLOCKING; adapter/playback BLOCKING.

Reduced version: interpreter and records leave BattleSpec before initiative. A conventional battle may return `IMMEDIATE_INTERPRETER_WITHDRAWAL_ROUTE_CLEAR`. Narrative determines whether withdrawal actually completes.

### Fragment Recovery Perimeter

Full intent: secure access to a damaged text fragment without allowing combat motion or hazards to silently rewrite custody or condition.

Dependencies: protected-object carrying is not verified inside complete movement; lifecycle PARTIAL; hazards/zones/reactions BLOCKING if collapse/fire/water matters; tactical policy BLOCKING; adapter/playback BLOCKING.

Reduced version: fragment remains static and noncombatant. Battle output is limited to `IMMEDIATE_FRAGMENT_APPROACH_CLEAR`. Material Culture/Archaeology records later recovery and custody.

### Wayfinding Inscription Junction

Full intent: route choice depends on interpreting dialectal or damaged directions while hostile pressure makes time and positioning relevant.

Dependencies: complete movement PARTIAL; lifecycle PARTIAL; terrain/hazards/zones/reactions BLOCKING for changing routes; tactical policy BLOCKING; adapter/playback BLOCKING.

Reduced version: Narrative resolves the route interpretation first. If that path intersects a hostile group, AutoPTU resolves an ordinary audited encounter. Neither victory nor defeat determines whether the translation was correct.

## Readiness rule

Reduced versions are READY only at narrative-contract level and only after auditing every selected Move, Ability, Item, Feature, status, and other combat mechanic individually. Full versions remain blocked by the capability families stated above.

## Canon gate

Promotion of any linguistic fact requires provenance. Canon review must answer where the source came from, who observed it, which representation is being promoted, what uncertainty remains, whether living speakers or affected communities exist, and whether PTU/Caelo mechanics are implicated. Nothing in this proposal silently rewrites established lore.