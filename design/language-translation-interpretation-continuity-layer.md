# Language, Translation and Interpretation Continuity Layer

Status: DESIGN. NON-CANON UNTIL ADOPTED.
Pass: 195

## Purpose

This layer gives Ouros a persistent model for unfamiliar text, transcription, translation, interpretation and Pokémon communication boundaries.

It does not establish any official Caelo language, dialect, interpreter profession, magical language rule or universal translator.

The layer exists so the world can preserve what was actually observed, what someone rendered from it, what someone believes it means and what later evidence changed.

## Boundary with neighboring systems

Correspondence owns message identity, delivery, reading and acknowledgment.

Archive/provenance owns source custody, edition history and evidentiary lineage.

Archaeology owns object/site observation and historical interpretation.

Education owns what was taught and corrected.

Visitor continuity owns temporary presence and claims from outside Marea.

Social/knowledge systems own who legitimately knows which facts.

PTU owns mechanical Channeling, Telepathy and any other Feature, Skill, Capability or effect that grants communication beyond ordinary observation.

This layer links those systems without replacing them.

## Core record: source_expression

Recommended fields:

- `expression_id`
- `source_object_or_message_ref`
- `expression_kind`: spoken utterance, handwritten text, printed text, inscription, symbol sequence, shorthand, sign, recorded audio, gesture sequence, Pokémon vocalization observation or other authored type
- `speaker_or_creator_ref` when known
- `observed_at`
- `observed_by`
- `physical_or_media_location_ref`
- `source_language_or_system_ref` when known
- `source_language_state`: known, proposed, disputed, unknown
- `legibility_or_audibility_state`
- `completeness_state`
- `source_span_refs`
- `provenance_refs`
- `notes`

The source expression is immutable as historical evidence. A better scan, restored fragment or clearer recording creates another observation/rendering linked to the same underlying source when appropriate.

## Rendering record

A rendering captures transformation without semantic commitment.

Examples:

- transcription of handwriting;
- transliteration from one script to another;
- notation of an unclear sound;
- segmentation of a continuous symbol string;
- restored text with explicit lacuna markers.

Recommended fields:

- `rendering_id`
- `source_expression_id`
- `rendering_kind`
- `renderer_actor_or_process_ref`
- `created_at`
- `content_ref`
- `uncertain_spans[]`
- `omitted_spans[]`
- `restored_spans[]`
- `method_ref`
- `confidence_notes`
- `supersedes_rendering_id` when applicable

A rendering can be technically accurate while its meaning remains unknown.

## Interpretation / translation record

Recommended fields:

- `interpretation_id`
- `source_expression_id`
- `rendering_id` when used
- `interpreter_actor_or_process_ref`
- `interpretation_kind`: translation, paraphrase, operational gloss, historical reading, semantic hypothesis, behavioral interpretation or other authored type
- `target_language_or_register_ref` when applicable
- `created_at`
- `content_ref`
- `claim_spans[]`
- `confidence_by_span[]`
- `alternative_readings[]`
- `evidence_refs[]`
- `contradiction_refs[]`
- `scope_limitations[]`
- `supersedes_interpretation_id` when applicable
- `review_state`

An interpretation is a claim with provenance. It is never canonical truth merely because it is the newest or most polished wording.

## Translation state

Useful states:

- `UNREVIEWED`
- `PARTIAL`
- `WORKING`
- `REVIEWED`
- `DISPUTED`
- `SUPERSEDED`
- `UNRESOLVED`

These states describe documentary workflow. They do not establish legal or academic credentials.

## Span-level uncertainty

The system should permit one uncertain word without making the whole document unreadable.

Example structure:

- span A: high confidence
- span B: two plausible readings
- span C: illegible
- span D: restored from a second copy

This supports quests where the player can act on the reliable portion while leaving the uncertain portion open.

## Competing translations

Two translations can coexist.

The server should preserve:

- common agreed spans;
- divergent spans;
- each interpreter's basis;
- later evidence;
- which institutions used which rendering at which time.

A conflict does not imply deceit.

## Revision history

Correction never rewrites history.

If Tideglass posted translation v1 and later issues v2:

- v1 remains the version certain actors actually read;
- v2 becomes the current reviewed interpretation when the owning workflow says so;
- consequences caused by v1 remain historical facts;
- NPC knowledge updates only through legitimate access to v2.

## Practical versus scholarly interpretation

The layer supports different scopes.

A route marker may need a narrow operational gloss such as `likely indicates upper crossing`.

A historical document may preserve multiple readings for years.

A field-school handout may simplify a reviewed source while retaining a citation to the full interpretation.

The system must not force false certainty simply because gameplay needs a next action.

## Human-language boundary

No human language map is canonized by this layer.

Future authored content may define languages or dialects only through explicit canon review.

Until then:

- unfamiliar wording can be represented as an authored communication barrier;
- a visitor's language claim remains attributed;
- translation competence must be explicitly authored or mechanically supported;
- the runtime cannot assume that every resident understands every external text.

## Pokémon communication boundary

Ordinary world observations may record:

- vocalization;
- gesture;
- posture;
- repeated trained cue;
- approach/withdrawal;
- interaction with known objects or actors.

Narrative may infer only what the authored evidence supports.

Direct access to intentions, emotions, motivations, thoughts, memories or mental messages must use the exact governing PTU mechanic when mechanics matter.

### Channeler guardrail

Project PTU content for `Channeling` explicitly governs communication of intentions, emotions and motivations while a Pokémon is channeled and includes truthfulness semantics.

Therefore:

- `CHANNELING_ACTIVE != UNIVERSAL_LANGUAGE_FLUENCY`
- `INTENTION_SHARED != WORD_FOR_WORD_TRANSLATION`
- `EMOTION_SHARED != COMPLETE_MEMORY_ACCESS`
- `MOTIVATION_SHARED != OMNISCIENT_CAUSAL_EXPLANATION`

### Telepathy guardrail

Project PTU content contains explicit Telepathy semantics with target, range/Focus and resistance considerations.

Therefore:

- `TELEPATHY_PRESENT != UNLIMITED_MIND_READING`
- `MENTAL_MESSAGE_SENT != TARGET_BELIEVES_MESSAGE`
- `SURFACE_THOUGHT_READ != FULL_HISTORY_KNOWN`
- `TELEPATHIC_ACCESS != INSTITUTIONAL_AUTHORITY`

If runtime support for the exact mechanic is incomplete, mechanically consequential use remains blocked or authored outside tactical resolution only where legitimate.

## Interpreter actor state

A future interpreter can have narrative competence without receiving invented PTU progression.

Recommended fields:

- `actor_ref`
- `language_or_system_scope_refs[]`
- `documented_experience_refs[]`
- `institutional_role_ref` when canonized
- `availability_state`
- `known_limitations[]`
- `review_history_refs[]`

Narrative competence never silently grants Skill Ranks, Edges, Features or supernatural Capabilities.

## Translation memory and actor knowledge

An actor should remember the version actually encountered.

If Pia read v1 and Taro later reviews v2, Pia does not retroactively know v2.

Recommended knowledge event:

- actor
- interpretation/version
- access event
- time
- scope learned
- whether correction was acknowledged

This connects directly to existing information and correspondence systems.

## Minecraft representation boundary

A Minecraft book, sign, item tooltip, NPC subtitle or custom UI is a projection.

The adapter must not decide:

- source language;
- translation accuracy;
- interpreter competence;
- whether an unclear span is resolved;
- whether an actor understands the text;
- whether an interpretation is institutionally accepted;
- whether Pokémon speech has mechanical meaning.

Destroying a sign does not erase the source record.

Client localization does not mean the character canonically speaks the localized language.

A UI translation for player accessibility must remain separate from in-world translation state.

## Accessibility localization versus diegetic language

This separation is mandatory.

The product may display all dialogue in the player's chosen UI language while the world state still records an in-fiction interpretation barrier.

`PLAYER_UI_LOCALIZED != CHARACTER_FLUENT`

`SUBTITLE_AVAILABLE != IN_WORLD_TRANSLATION_OCCURRED`

This avoids making accessibility features alter canon.

## Quest transitions

Useful narrow events:

- `SOURCE_EXPRESSION_RECORDED`
- `RENDERING_CREATED`
- `UNCERTAIN_SPAN_FLAGGED`
- `INTERPRETATION_CREATED`
- `ALTERNATIVE_READING_RECORDED`
- `INTERPRETATION_REVIEWED`
- `CORRECTION_ISSUED`
- `ACTOR_LEARNED_CORRECTION`
- `INTERPRETATION_SUPERSEDED`
- `QUESTION_REMAINS_OPEN`

These should feed existing quest state rather than replace it.

## Failure modes that create useful stories

- damaged text produces two plausible terms;
- an old transcription silently omitted a line;
- a courier delivers the original but the receiving office only has an obsolete translation;
- a visitor uses a familiar-looking word differently;
- a technical abbreviation is mistaken for ordinary language;
- an interpreter correctly says `unknown` instead of guessing;
- a Pokémon's repeated cue is misread until another observation supplies context;
- a public handout simplified a source beyond what the evidence supported;
- two institutions quote different translations of the same source;
- a correction reaches one actor before another.

None requires villainy.

## Mechanically rich encounter: Interpreter at the Seasonal Crossing

Narrative premise:

A temporary visitor or local specialist is carrying a field note whose operational wording matters for a route check. Wild activity creates an immediate confrontation before the interpretation can be reviewed at the destination.

The document and its meaning remain world state. The encounter exists because of immediate safety, not because battle can prove translation.

### Intended full version

Potential tactical content:

- interpreter/visitor and document represented in world state;
- protected withdrawal route;
- one or more wild combatants;
- corridor positioning;
- interception;
- forced movement if selected Moves or effects use it;
- tactical terrain/weather only when authored and verified;
- exact Trainer/Pokémon mechanical content;
- objective-aware retreat/protection AI;
- faithful adapter playback and return to persistent state.

Permanent capability requirements:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions when used;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Current disposition: FULL VERSION BLOCKED.

### Reduced version

1. Source document, translation state, interpreter identity and route purpose remain Narrative world state.
2. Noncombatants move to an authored safe state before BattleSpec.
3. The document never becomes battle loot.
4. If a wild actor still prevents withdrawal/passage, compile a separate ordinary audited battle on stable geometry.
5. AutoPTU returns only narrow facts such as `IMMEDIATE_ROUTE_THREAT_WITHDREW` or `IMMEDIATE_PASSAGE_CLEAR`.
6. The interpretation workflow resumes afterward.

Battle output cannot establish:

- correct translation;
- interpreter credibility;
- document authenticity;
- ancient-historical truth;
- visitor intent;
- Pokémon thoughts;
- institutional acceptance;
- actor fluency;
- whether a correction is required.

Current disposition: REDUCIBLE using only audited battle content.

## First implementation slice

`One Word, Two Copies`

Tideglass holds two historical transcriptions of one damaged survey annotation. Most text agrees. One operational term differs.

Pia prepares a side-by-side comparison. Taro records both readings, source provenance and the unresolved span.

The player can locate a later corroborating document, but that document may narrow rather than fully resolve the difference.

Requirements:

- no new language canon;
- no battle;
- no supernatural Feature;
- no invented Skill check;
- uses Tideglass, Pia and Taro already in canon;
- creates reusable versioned interpretation infrastructure.

## Canon guardrail

This layer does not canonize languages, dialects, alphabets, literacy, interpreter credentials, translation technology, ancient scripts, psychic norms, Pokémon speech norms or regional communication law.

Any such material remains proposed until explicit canon review and PTU/Caelo cross-check.