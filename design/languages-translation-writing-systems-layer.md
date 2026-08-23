# Languages, Translation & Writing Systems Layer

Status: SYSTEMS DESIGN. Proposed architecture. Not canon.

## Purpose

This layer owns persistent language state in Ouros: spoken/written languages, scripts, terminology standards, translations, interpretations, signage, document-language metadata, multilingual services and historical language change.

It does not own actor identity, message delivery, archives, education, social persuasion or supernatural communication. Those remain under their existing authorities.

## Core separation

The system must preserve this chain:

source expression -> language/script -> transcription -> translation -> interpretation -> delivery -> actor understanding -> later revision

No stage may silently overwrite the previous one.

## Primary entities

### LANGUAGE_SYSTEM

Persistent ID for an authored language or language family.

Suggested fields:
- language_id
- canonical_name_if_approved
- historical_names[]
- regions_of_use[]
- institutional_status[]
- known_scripts[]
- temporal_revision
- canon_status

### WRITING_SYSTEM

Persistent script identity.

Fields:
- writing_system_id
- glyph_inventory_version
- directionality if canon-defined
- known_language_links[]
- historical_periods[]
- supported_rendering_contexts[]

A script can be shared by multiple languages. A language can use more than one script over time.

### LANGUAGE_PROFILE

Actor-specific, private by default.

Fields:
- actor_id
- language_id
- competence_claims by modality: understand_speech, speak, read, write
- domain notes
- evidence/provenance
- player_confirmed flag for PCs

Do not infer profile from birthplace, appearance, name, ethnicity, faction, job, school or residence.

### TEXT_ARTIFACT

Persistent content-bearing object or record.

Fields:
- text_artifact_id
- physical_or_digital_carrier_id
- source_language_id
- writing_system_id
- source_version
- authored_at if known
- author_claims[]
- transcription_records[]
- translation_records[]
- interpretation_records[]
- access/privacy state

### TRANSLATION_RECORD

- translation_id
- source_text_artifact_id
- source_version
- target_language_id
- translator_actor_or_system
- method: HUMAN / ASSISTED / AUTOMATED / UNKNOWN
- produced_at
- review_state
- confidence_notes
- terminology_standard_id if used
- supersedes_translation_id

A new translation does not erase the old one.

### TERMINOLOGY_STANDARD

Useful for League rules, scientific names, medical language, transport signs, safety notices and institutional forms.

Fields:
- terminology_standard_id
- institution_id
- domain
- version
- effective_window
- preferred_terms[]
- deprecated_terms[]
- crosswalks[]

### PUBLIC_SIGNAGE_RECORD

- sign_id
- location_id
- physical_revision_id
- text_versions[]
- language_order[]
- iconography[]
- accessibility_channels[]
- effective_window

A sign being physically present does not mean every actor can understand it.

## Knowledge and uncertainty

Allowed states for a historical text reading:
- UNTRANSCRIBED
- PARTIALLY_TRANSCRIBED
- TRANSCRIBED
- TRANSLATION_PROPOSED
- MULTIPLE_TRANSLATIONS
- INTERPRETATION_DISPUTED
- INSTITUTIONALLY_ACCEPTED
- SUPERSEDED
- UNRESOLVED

Institutional acceptance is not metaphysical truth.

## Unown and symbol-like Pokémon guardrail

If Unown or another symbol-like Pokémon is used in Ouros:
- observed shape is an observation;
- resemblance to a glyph is an interpretation;
- sequence order is evidence;
- reading is a hypothesis until supported;
- translation is separate from reading;
- supernatural meaning requires authored canon and PTU/Caelo validation.

Never generate prophecy, ritual effect or magical command merely because Unown appear in a textual pattern.

## Multilingual public systems

Public services may define language-coverage profiles:
- transport
- clinics
- emergency dispatch
- markets
- League venues
- schools
- archives
- museums
- conservation sites
- research stations

Coverage can vary by channel: spoken desk service, printed sign, map legend, caption, audio announcement, website, emergency alert.

A service gap can produce a practical problem without assigning blame or intelligence.

## Translation drift

Every translation should bind to a source revision.

Example:
- Rule notice v3 exists.
- Translation A correctly translates v2.
- Translation B translates v3.
- A remains historically correct for v2 but operationally obsolete.

This should generate reconciliation work, not retcon.

## Historical language change

Ouros may preserve:
- old place names
- superseded spellings
- dialect terms
- trade-language terms
- technical vocabulary changes
- script reforms
- archival transliterations
- multilingual inscriptions

Changes require authored or evidence-backed causes such as migration, education, administration, trade, media, transport or long-term contact.

Do not procedurally map fictional languages to real ethnic groups or nationalities.

## Actor understanding

Message delivery and understanding are separate.

Possible message outcomes:
- delivered and understood
- delivered but only partly understood
- delivered with translation
- delivered with disputed interpretation
- received after terminology changed
- translated incorrectly then corrected

For PCs, private language competence and interpretation choices must respect player-authored state.

## Accessibility

Critical information should not depend on one language or one sensory channel when the institution plausibly has alternatives.

Useful equivalents include:
- icons
- maps
- numbered routes
- color plus shape redundancy
- captions
- pictograms
- staffed interpretation
- machine-assisted drafts reviewed by people

Accessibility support does not imply universal comprehension.

## Minecraft projection

Minecraft/Cobblemon can display:
- sign text
- books
- noticeboards
- subtitles
- maps
- iconography
- translated UI overlays

It must not become authority for:
- language competence
- translation correctness
- historical reading
- author identity
- supernatural meaning
- telepathic comprehension

## Encounter contracts

### Archive Script Dispute

Narrative premise: two legitimate translations of an old route marker imply different destinations.

FULL version:
- overworld investigation with multiple locations;
- dynamic search/escort if a rival expedition moves at the same time;
- possible battle only if independent conflict occurs.

Dependencies if battle becomes objective-rich:
- complete movement including interception/forced movement: BLOCKING
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- targeting/footprints/range/LoS: VERIFIED for any conventional battle
- base movement legality: VERIFIED
- action economy/initiative: VERIFIED

REDUCED version:
- resolve translation/investigation in world state;
- freeze the chosen expedition site;
- if combat occurs, use a conventional static AutoPTU arena;
- battle result never decides which translation is correct.

### Station Signage Failure

Narrative premise: a temporary route change was published in one language version but not another.

FULL version requires moving crowds and route-clearing objectives.

Dependencies:
- complete movement/interception/forced movement: BLOCKING
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

REDUCED version:
- redirect civilians before combat;
- preserve signage versions and delivery logs;
- open a static battle only if a separate threat remains.

### Unown Survey Chamber

Narrative premise: researchers document a changing arrangement of Unown-like symbols without assuming meaning.

FULL version, if symbols alter tactical geometry or trigger effects, would require:
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior if an exact Move is involved: PARTIAL
- abilities if an exact Ability is involved: PARTIAL
- adapter/playback: BLOCKING

REDUCED version:
- symbol arrangement remains observation/world state;
- no automatic hazard, status, buff or puzzle effect;
- any battle uses fixed geometry and ordinary legal mechanics.

## Permanent capability map used by this layer

VERIFIED:
- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback

## Prohibited automatic inferences

Never infer:
- birthplace -> language competence
- name -> language
- script -> ethnicity
- accent -> intelligence
- multilingualism -> Translator/Researcher Feature
- literacy -> Pokémon Education rank
- telepathy -> universal translation
- Chatot mimicry -> semantic comprehension
- Unown sequence -> prophecy
- translated sign -> universally understood
- untranslated text -> puzzle permission
- battle victory -> correct interpretation
- Minecraft book text -> canon truth

## Canon questions left open

- How many authored languages exist in Ouros?
- Are regional languages mutually intelligible?
- Is there a League-wide working language?
- Which institutions maintain terminology standards?
- Which scripts predate modern institutions?
- How are historical place names handled?
- Which multilingual services exist at launch?
- Are any Pokémon capable of explicit human-language communication under canon?
- What PTU/Caelo rules, if any, govern language competence, telepathy, translation or deciphering?
