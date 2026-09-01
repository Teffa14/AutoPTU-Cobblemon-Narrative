# Ouros Language, Script, Translation & Interpretation Layer

Status: DESIGN / NON-CANON ARCHITECTURE
Date: 2026-09-01
Research basis: `research/2026-09-01-language-scripts-translation-interpretation-scan-177.md`

## Purpose

This layer defines how written, gestural and other communicative material becomes readable world state without creating omniscience or bypassing existing evidence, archive and communications systems.

It owns representation and interpretation provenance only.

Existing systems continue to own:
- canonical world facts;
- evidence and claim identity;
- actor knowledge/posture;
- information packets and delivery;
- archives and collections;
- quest state;
- PTU skill/Feature resolution.

## Core chain

`SOURCE OBJECT / SIGNAL`
`-> OBSERVATION RECORD`
`-> TRANSCRIPTION / CAPTURE`
`-> SCRIPT OR MODE IDENTIFICATION`
`-> LITERAL READING`
`-> SEMANTIC INTERPRETATION`
`-> CLAIM_ID`
`-> ACTOR CLAIM POSTURE`
`-> INFORMATION PACKET / ARCHIVE EDITION`
`-> WORLD TEST / CORROBORATION / REVISION`

Each arrow can fail independently.

## Communication artifact record

```yaml
communication_artifact:
  artifact_id: null
  artifact_type: null
  source_object_id: null
  location_id: null
  observed_at: null
  observed_by_actor_ids: []
  physical_layer_id: null
  medium: null
  preservation_state: null
  authored_by_actor_id: null
  authored_by_institution_id: null
  authored_period_id: null
  raw_capture_refs: []
  custody_record_ids: []
```

Candidate artifact types:
- INSCRIPTION
- FIELD_NOTE
- ROUTE_MARKER
- LEDGER_NOTATION
- MAP_ANNOTATION
- SIGN
- LETTER
- LABEL
- SYMBOL_SEQUENCE
- GESTURAL_PATTERN
- ACOUSTIC_PATTERN
- OTHER_SIGNAL_PATTERN

Artifact existence does not imply that anyone can read it.

## Transcription record

```yaml
transcription:
  transcription_id: null
  artifact_id: null
  transcribed_by_actor_id: null
  created_at: null
  observed_units: []
  unreadable_spans: []
  uncertain_units: []
  normalized_units: []
  supplied_units: []
  source_capture_refs: []
  confidence_band: null
```

Rules:
- `observed_units` preserve what is physically present;
- `normalized_units` may regularize spelling/layout without replacing observed form;
- `supplied_units` are restorations or editorial additions and must be marked;
- unreadable material remains unreadable until new evidence appears;
- a skill check cannot manufacture missing glyphs.

## Interpretation record

```yaml
interpretation:
  interpretation_id: null
  transcription_id: null
  interpreter_actor_id: null
  interpreter_institution_id: null
  interpretation_type: null
  literal_reading: null
  semantic_summary: null
  candidate_meanings: []
  supporting_evidence_ids: []
  contradicting_evidence_ids: []
  confidence_band: null
  supersedes_interpretation_id: null
  created_at: null
```

Candidate interpretation types:
- SCRIPT_IDENTIFICATION
- LITERAL_TRANSLITERATION
- LITERAL_TRANSLATION
- CONTEXTUAL_READING
- HISTORICAL_RECONSTRUCTION
- FUNCTIONAL_INSTRUCTION
- SIGNAL_MEANING_HYPOTHESIS

The interpretation can generate or support an existing `claim_id`. It is never itself world truth.

## Multiple readings

Two interpretations can coexist when the source is ambiguous.

Example:
- Reading A treats a marker as a warning about the route ahead.
- Reading B treats it as an older maintenance notation referring to a side channel.

Until corroborating evidence exists, both remain attributed readings.

The UI/journal may show a preferred reading if an institution currently endorses one, but must retain dissenting or superseded readings where relevant.

## Physical layers and palimpsests

A single object can contain several authorship periods.

```yaml
artifact_layer:
  physical_layer_id: null
  artifact_id: null
  relative_order: null
  material: null
  likely_period_id: null
  likely_author_group_id: null
  evidence_ids: []
  confidence_band: null
```

This supports:
- old carved text with later paint;
- route markers reused by later surveyors;
- archive documents with marginal notes;
- repaired signs whose replacement section uses different terminology.

Never merge separate layers into one coherent message without explicit evidence.

## Communication modes beyond writing

A repeated non-written signal can use the same provenance chain.

```yaml
signal_observation:
  signal_event_id: null
  source_actor_or_pokemon_id: null
  signal_mode: null
  pattern_capture: null
  context_event_ids: []
  observer_actor_ids: []
  proposed_meaning_claim_ids: []
```

Candidate modes remain descriptive rather than magical:
- VOCALIZATION
- GESTURE
- POSTURE
- RHYTHM
- LIGHT_PATTERN
- MAGNETIC_PATTERN
- SCENT_PATTERN
- TELEPATHIC_COMMUNICATION only when exact canon/mechanics support it

The presence of a pattern does not establish language complexity, intention or species-wide meaning.

## PTU mechanical gate

Interpretation should call actual PTU skill/Feature surfaces when mechanics are required.

The world layer may determine that:
- an inscription is present;
- a reference corpus exists;
- an NPC specialist is available;
- two samples share recurring glyphs.

It must not invent a generic `translation skill` that supersedes PTU.

Potential skill/Feature involvement must be audited against source material before implementation. Pokémon Education, Intuition, Guile, Charm, Command, Channeler, Telepath or special Pokémon capabilities are never interchangeable by default.

## Archive integration

Tideglass and other archives can preserve:
- raw image/copy;
- transcription editions;
- interpretation editions;
- correction history;
- source custody;
- links to field locations;
- disputes between readers.

An archive can publish `interpretation v3` while preserving that `v1` was once used in a route decision.

## Quest integration

Translation-related quest objectives should target concrete evidence operations:
- inspect the original object;
- recover a missing copy;
- compare two editions;
- locate a parallel inscription;
- interview a living user of a notation system;
- test a functional reading in a safe context;
- deliver a corrected edition;
- identify which physical layer a mark belongs to.

Avoid objectives that amount to `roll once -> ancient mystery solved`.

## Puzzle design rules

1. Critical progression must have redundant in-world evidence.
2. Script decoding may accelerate progress but should not require external reference material.
3. The first solved example should teach a reusable rule.
4. Later puzzles can recombine known rules rather than changing cipher logic arbitrarily.
5. Wrong interpretations should usually create bounded consequences, not campaign-ending locks.
6. A physical action encoded by text should still pass ordinary world safety and authority checks.
7. Historical meaning and mechanical activation are separate facts.

## Pokémon communication guardrails

1. One speaking or signaling individual does not establish a species-wide language.
2. Familiarity with a partner can support authored relationship knowledge but does not grant perfect translation.
3. Telepathy or Channeler effects require exact PTU/Caelo sourcing and engine support.
4. A Pokémon's battle behavior cannot be automatically interpreted as dialogue.
5. Cobblemon animations/sounds are presentation evidence only unless AutoPTU-authoritative logic binds them to a canonical signal event.

## Marea integration targets

Strong existing anchors:
- Taro Min: archive custody and edition history;
- Pia Min: copies, deliveries and source retrieval;
- Dr. Nerea Sol: field notation and evidence quality;
- Ema Rey: observation protocols;
- Mara Veyra: operational route reports;
- Lia Morn and Mina Cors: ferry/dock operational signals;
- Jo Venn: teaching observation and record practice.

No new family relationship, language background or specialized linguistic expertise is canonized by this design.

## Battle dependency contract

Most translation content should remain outside BattleSpec.

Full mechanically rich pattern: a Pokémon group emits interpretable signals during a hazardous battle and the player can use a specific Trainer Feature to change an objective mid-round.

Required capability families:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception/forced movement if positional signaling matters;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle if selected content uses statuses;
- terrain/weather/hazards/zones/reactions if the scene depends on environmental phases;
- exact move-specific behavior;
- exact abilities;
- exact items;
- exact Trainer Features/perks, especially communication/interrupt Features;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Current conservative readiness at AutoPTU-Java `8fd11090b31d413072808662c01fc2e2316420ff`:
- VERIFIED for covered contracts: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.
- PARTIAL: complete movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.
- BLOCKING as complete families: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback.

The latest Java commit improves declarative content-backed forced-movement prevention. It does not prove the whole movement family.

Reduced version:
- all signal observation and interpretation occurs before or after combat;
- the battle is an ordinary audited BattleSpec on stable terrain;
- no mid-round translation action, escort signal, dynamic hazard, reaction objective or communication interrupt exists;
- battle victory may provide access to observe a source object or calm conditions enough for later study;
- victory cannot determine what an inscription means or what a Pokémon intended.

## Validation targets

Future CI/startup validation should reject:
- interpretation referencing a missing transcription;
- transcription referencing a missing artifact;
- supplied/restored units presented as observed units;
- circular supersession chains;
- public translation with no source edition;
- a quest requiring an interpretation unavailable to its issuer;
- a species-wide communication claim derived from only one individual observation;
- a telepathic/special communication claim without explicit capability provenance.

## Promotion boundary

This layer can be implemented without canonizing any ancient Ouros script, regional language, translation institution, telepathic population, Unown presence or specific historical inscription.