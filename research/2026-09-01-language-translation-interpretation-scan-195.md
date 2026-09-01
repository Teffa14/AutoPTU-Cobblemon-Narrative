# Language, Translation and Interpretation Research Scan — Pass 195

Status: RESEARCH / PROVENANCE. NOT CANON.
Date: 2026-09-01
Narrative head inspected before writing: `32fd056661b4793c02c4ee453864e58da8113791`

## Research question

How can Ouros represent unfamiliar writing, translation, interpretation, Pokémon communication, correction and uncertainty without inventing a universal language system, silently granting supernatural comprehension, or collapsing an interpreter's statement into canonical truth?

This pass focuses on the continuity seam between existing correspondence, archive/provenance, visitor, education, archaeology and Pokémon-individual systems.

## Repository inspection result

The repository already has strong neighboring systems:

- correspondence tracks message identity, copies, delivery, reading, acknowledgment and supersession;
- Tideglass/archive layers preserve provenance, versions and contradictory records;
- archaeology layers distinguish observed artifact from interpretation;
- visitor continuity can preserve claims brought from outside Marea without making them regional truth;
- education tracks what was taught and corrected without granting PTU Skills or Features;
- NPC/Pokémon canon requires named Pokémon to remain individuals rather than generic utilities;
- social and knowledge systems already distinguish observation from inferred private state.

A repository-wide code search for `translation language interpreter multilingual dialect` returned no matching implementation layer. The new seam is therefore narrow enough to add without duplicating a named existing subsystem.

## Public Pokémon sources

### 1. Unown symbols and localized inscriptions

Source:
- Bulbapedia, `Unown symbols`: https://bulbapedia.bulbagarden.net/wiki/Unown_symbols
- Bulbapedia, `Solaceon Ruins`: https://bulbapedia.bulbagarden.net/wiki/Solaceon_Ruins

Reusable structure:

Pokémon repeatedly uses an unfamiliar visual script whose symbols can be mapped to ordinary text. The same inscriptions are localized differently across game-language releases, and Legends: Arceus requires restoration of a missing wall fragment before one inscription becomes readable.

Useful Ouros lessons:

- physical legibility and semantic interpretation are separate states;
- missing material can block or lower confidence before any translation begins;
- transliteration can be distinct from translation;
- an inscription can be rendered into different target-language wording without changing the physical source;
- restoring a fragment can change what can be read without retroactively changing what earlier observers actually saw.

Do not copy the inscriptions, symbols, puzzle solutions or associated plots into Ouros.

### 2. Ruins of Alph

Source:
- Bulbapedia, `Ruins of Alph`: https://bulbapedia.bulbagarden.net/wiki/Ruins_of_Alph

Reusable structure:

The site preserves multiple inscriptions that become meaningful in the context of location, puzzle chamber and other discoveries. Different game versions render related ancient statements differently.

Useful Ouros lessons:

- interpretation should retain source location and physical context;
- short words or labels can function as operational hints while longer inscriptions remain interpretive evidence;
- two legitimate renderings can differ without one being automatically fraudulent;
- later discoveries can improve a reading without deleting the earlier reading from history.

### 3. Team Rocket's Meowth as an exceptional speaker

Source:
- Bulbapedia, `Meowth (Team Rocket)`: https://bulbapedia.bulbagarden.net/wiki/Meowth_(Team_Rocket)

Reusable structure:

Pokémon fiction contains exceptional individuals that can communicate in human language, while ordinary members of the same species do not automatically have that capability. Different adaptations also treat this ability differently.

Useful Ouros lesson:

A species identity never grants universal human-language speech. Any unusually capable Pokémon must be represented as an individual with explicit authored or mechanically validated capability.

Do not reproduce this character, his history, dialogue or distinctive personality.

## PTU community signal

Source:
- r/PokemonTabletop discussion, `Help with Channeling (I'm a new player)`: https://www.reddit.com/r/PokemonTabletop/comments/psitve/
- r/PokemonTabletop discussion, `Need help with choosing a class`: https://www.reddit.com/r/PokemonTabletop/comments/1h7kvap/

These discussions are not rules authority. They are useful only as a signal that players distinguish Channeler-style emotional/intention communication from Telepathy-style mental communication and that tables can otherwise blur those boundaries.

Design lesson: Ouros should never let ordinary narrative dialogue silently stand in for a supernatural Feature or Capability.

## Project PTU evidence

Read-only AutoPTU evidence at head `729bae2d424963ff9bb3f4159c9a7ac9152128a7` contains authoritative-content records for Channeler and Telepathy.

Observed source evidence includes:

- `Channeling`: while Channeling a Pokémon, the Pokémon may communicate intentions, emotions and motivations, and the Trainer may communicate similarly; the exchange has explicit truthfulness constraints;
- `Telepathy`: a Telepathic Pokémon or Trainer has defined mental-communication/read capabilities with range, Focus and resistance semantics;
- Channeler and Telepath appear as specific Trainer mechanical identities in the supplied content set;
- the Python career adapter currently categorizes several supernatural classes, including Channeler and Telepath, as `narrative_unlock`, which is not evidence that their complete mechanics are implemented end to end;
- trainer-runtime coverage reports contain missing runtime mappings for portions of Trainer content, so the presence of catalog data is not proof that the whole class family is executable.

Mechanical conclusion:

- ordinary human-language interpretation belongs to Narrative world state unless Caelo/PTU defines an applicable mechanic;
- Pokémon intent/thought communication must use the exact PTU capability/Feature when mechanics matter;
- Channeling must not be generalized into word-for-word translation;
- Telepathy must not be generalized into unrestricted omniscience;
- a narrative interpreter cannot fabricate mechanical access to thoughts, memories, deception state or private knowledge.

## Caelo source status

A repository search for literal `Caelo` across Narrative, AutoPTU-Java and AutoPTU returned no indexed results in this run.

Therefore this pass does not canonize:

- regional official languages;
- dialect boundaries;
- literacy rates;
- interpreter licensing;
- translation standards;
- official terminology;
- ancient Marea scripts;
- magical language rules;
- whether Caelo provides a universal spoken language convention;
- whether specific Pokémon species have ordinary speech or comprehension rules beyond PTU mechanics.

## Reusable narrative structures

### Source / rendering / interpretation separation

Persist at least three distinct things:

1. source content as observed;
2. a rendering such as transcription or transliteration;
3. an interpretation or translation into another form.

An interpretation references its source and creator. It never replaces the source.

### Confidence by span

A document can be mostly clear while one term remains uncertain. Confidence should attach to spans or claims when useful instead of forcing one confidence value onto the whole text.

### Competing legitimate translations

Two translations can both be reasonable when wording is ambiguous. The world should preserve the disagreement and let later evidence resolve, narrow or leave it open.

### Correction without historical erasure

A revised translation creates a new version. Earlier posted, quoted or acted-upon versions remain part of history.

### Interpreter presence and access

Understanding can depend on whether the relevant person, reference work or mechanical capability is actually available. Absence can create delay without inventing an arbitrary puzzle.

### Practical translation versus scholarly translation

An operational sign may need only enough interpretation to choose a safe route. A historical inscription may require provenance, context and uncertainty notes. The system should not force the same precision workflow for every text.

### Pokémon communication boundary

Observable behavior, trained cues, vocalization and body language can support ordinary inferences with provenance. Direct access to intentions, emotions, thoughts or mental communication must remain inside the exact governing PTU rule when that rule is required.

## Design risks to avoid

- universal translator items invented for convenience;
- every unknown script being an Unown analogue;
- a single successful Skill check converting an entire culture into perfect fluency;
- using species as shorthand for language competence;
- treating an interpreter as an omniscient narrator;
- retroactively changing what NPCs knew after a translation correction;
- turning translation disagreement automatically into conspiracy;
- using Minecraft book text as the sole authority for canonical wording;
- letting AI paraphrase source material without storing which source/version it paraphrased;
- allowing battle victory to prove the meaning of a document.

## Original Ouros opportunity

Marea already contains Tideglass, Mirador, visitors, couriers, field-school teaching and old survey material. A translation layer can make those systems interact without adding a new faction.

The strongest first implementation is deliberately small: Tideglass holds two historical transcriptions of the same damaged survey annotation. Most wording agrees, but one operational term differs. Pia can prepare a comparison; Taro can preserve both readings and their provenance. The outcome is not `correct translation discovered` unless later evidence actually supports that conclusion.

## Capability implication

Most translation stories require no battle capability.

A mechanically rich version involving an interpreter or courier in a dangerous route must still classify battle dependencies exactly. Narrative can own source text, translation state, interpreter identity and knowledge effects while AutoPTU resolves only the tactical confrontation.

## Originality note

This pass extracts high-level structures only. It does not copy protected dialogue, inscriptions, named puzzle solutions, characters, missions or plot sequences into Ouros.