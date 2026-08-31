# Pass 169 research scan — linguistic records, translation, and decipherment

Status: RESEARCH ONLY / NON-CANON
Date: 2026-08-31

## Internal gap check

The repository tree and current README were inspected before drafting. Repository search for `language`, `translation`, `inscription`, `transliteration`, `decipher`, `dialect`, and related terms did not reveal a dedicated linguistic continuity layer. Existing Myth/Archaeology already owns archaeological sites, `inscription_ids`, observations, interpretations, myth versions, and sacred-site stewardship. Archives owns preservation and access to records; Material Culture owns physical objects; Human Identity owns names and identifiers; Communications owns delivery and channel state; Scientific Research owns research claims and revisions.

The gap is narrower: preserving what a text or utterance physically contains, how it was transcribed, transliterated, translated, interpreted, disputed, and revised over time without collapsing those stages into canonical truth.

This pass therefore does not invent a universal language map for Ouros. It proposes continuity grammar that activates only when authored canon, an observed artifact, a recorded utterance, or a trusted project source establishes the relevant language/script/text instance.

## Pokémon research

### Ruins of Alph and Unown text

The Ruins of Alph combine archaeological space, persistent inscriptions, researchers, visual puzzles, and text that becomes actionable only after a player recognizes the symbol system. Different chambers reveal different information and access paths, and later research records accumulate around the site. Reusable design lesson: a ruin can expose a corpus progressively; decipherment can change available interpretations and routes without making every inscription magical or every translation mechanically authoritative.

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Ruins_of_Alph
- https://bulbapedia.bulbagarden.net/wiki/Unown_text

Ouros should transform the structure, not copy the messages, chamber conditions, Unown sequences, or puzzle solutions.

### Hoenn Braille and the Sealed Chamber

Pokémon Ruby/Sapphire/Emerald and their remakes use visually represented Braille for environmental instructions and a chamber that exposes the symbol inventory before later inscriptions require the player to act on it. Reusable lesson: a dungeon may teach a notation system inside the fiction, then test reading, navigation, or contextual inference later. A known symbol inventory still does not guarantee that a damaged, archaic, dialectal, or metaphorical text has one obvious interpretation.

Source: https://bulbapedia.bulbagarden.net/wiki/Braille

Ouros must not reuse the exact inscriptions or Regi unlocking sequence.

### Solaceon / broader Unown inscription practice

The Unown text corpus across Pokémon games shows one symbol system used for decorative writing, navigational directions, short labels, historical statements, and puzzle clues. Localized releases can render the same fictional inscription differently. Reusable lesson: `script`, `language`, `text witness`, `translation version`, and `game-facing display` are separate concerns. A script can be shared by texts serving very different purposes.

Source: https://bulbapedia.bulbagarden.net/wiki/Unown_text

### Community PTU ruins and living-world practice

Public PTU community material includes campaigns where ruins, ancient civilizations, puzzles, factions, and archaeological discovery are recurring adventure surfaces. One puzzle-design thread explicitly distinguishes preserved ancient environments from modern fossil revival and treats multi-part ruins as a chain of discoveries rather than a single combat room. Reusable lesson: decipherment works best when it changes what the party can ask, where they can go, or how they understand prior evidence instead of serving as a one-roll lore dump.

Sources:
- https://www.reddit.com/r/PokemonTabletop/comments/110yfpe/
- https://www.reddit.com/r/PokemonTabletop/comments/1m4xfxk/the_guild_of_the_undaunted_ptu_lw/

These are community-practice references only. They are not rules authority.

A separate public PTU worldbuilding post proposes Unown as an explanation for universal language. That is useful chiefly as a warning: tables often solve language barriers through setting-specific homebrew. Ouros must not silently import such a premise. Source: https://www.reddit.com/r/PokemonTabletop/comments/o9zqgs/

## PTU mechanical cross-check

Public PTU material confirms General Education and Occult Education as Skills, and Telepathy as a concrete Capability/Feature surface. Public Telepath documentation also shows that some telepathic effects have explicit action economy and targeting consequences. None of the sources inspected in this pass establish a universal `language proficiency`, automatic literacy, automatic ancient-script reading, automatic Unown decipherment, or generic translation mechanic.

Sources:
- https://pturpg.wikidot.com/skills
- https://pturpg.wikidot.com/telepath
- https://pturpg.wikidot.com/sage

A public homebrew post proposes an Unown-themed gift that understands written languages. It explicitly identifies itself as homebrew and therefore provides evidence that tables sometimes desire this capability, not evidence that Core PTU grants it. Source: https://www.reddit.com/r/PokemonTabletop/comments/yj2kzx/

Consequences for Ouros:
- General Education rank does not automatically create fluency or decipherment authority.
- Occult Education does not automatically identify a script as supernatural or read it.
- Telepathy does not automatically translate written text or establish historical meaning.
- Sage/Runemaster/Researcher/Chronicler-like concepts must be checked feature by feature before they affect a linguistic challenge.
- Caelo modifications remain UNKNOWN until verified against project source material.

## Documentary and epigraphic process research

The Open Richly Annotated Cuneiform Corpus keeps transliterations, translations, catalogue data, glossaries, language/dialect metadata, uncertain readings, damaged passages, and alternative readings as distinct data. Its documentation explicitly supports uncertainty and alignment between source lines and translations. Reusable lesson: Ouros should preserve a chain from witness to representation to interpretation, including damaged or unreadable portions, rather than replacing the source with one translated string.

Sources:
- https://oracc.museum.upenn.edu/doc/search/searchingcorpora/index.html
- https://oracc.museum.upenn.edu/doc/help/visitingoracc/glossaries/
- https://oracc.museum.upenn.edu/doc/help/editinginatf/translations/index.html
- https://oracc.museum.upenn.edu/doc/help/editinginatf/bilinguals/index.html

ORACC also distinguishes language, dialect, script/transliteration conventions, normalization, lemma, attestation, context-specific sense, and translation. Reusable lesson: a recurring word can accumulate evidence across many inscriptions without every occurrence having the same meaning.

### Living-language archives

PARADISEC and ELAR preserve recordings of conversations, narratives, songs, instructions, and local knowledge in many living and endangered languages. Reusable lesson: language continuity cannot be designed solely as an archaeology puzzle. Living speakers, communities, oral records, access conditions, and changing usage may be more authoritative for current language practice than an outsider's reconstructed glossary.

Sources:
- https://www.paradisec.org.au/
- https://latam.elararchive.org/

Ouros must not turn a living community's language into a generic cipher or imply that an academic reconstruction outranks speakers by default.

## Reusable design findings

A durable linguistic record needs at least these separable stages: source witness; physical/documentary condition; script identification; transcription; transliteration when relevant; normalization when relevant; segmentation; lexical/glossary links; translation; interpretation; confidence; author/translator identity; supporting parallels; disagreement; publication; revision; actor knowledge.

A translation can be excellent while the historical interpretation built on it is wrong. A transcription can be uncertain because the surface is damaged while several translations remain plausible. Two translations can both be defensible because a term is polysemous. A later bilingual text can narrow an old uncertainty without erasing the earlier scholarly record.

A text used as a dungeon clue should usually produce a narrative fact such as `ROUTE_HINT_INTERPRETED` or `INSCRIPTION_READING_PROPOSED`. If the clue then points to a normal tactical encounter, AutoPTU resolves only that encounter. It does not determine the translation.

## Permanent design boundaries

SOURCE_WITNESS != TRANSCRIPTION
TRANSCRIPTION != TRANSLITERATION
TRANSLITERATION != TRANSLATION
TRANSLATION != HISTORICAL_INTERPRETATION
TRANSLATION_PUBLISHED != TRANSLATION_CORRECT
SCRIPT_IDENTIFIED != LANGUAGE_IDENTIFIED
LANGUAGE_IDENTIFIED != TEXT_UNDERSTOOD
CAN_READ != CAN_SPEAK
CAN_SPEAK != CULTURAL_MEMBERSHIP
SHARED_SCRIPT != SHARED_LANGUAGE
REPEATED_WORD != SAME_SENSE
UNKNOWN_SCRIPT != SECRET_CODE
ANCIENT_TEXT != SUPERNATURAL_TEXT
UNOWN_LIKE_SYMBOLS != AUTOMATIC_UNOWN_AUTHORITY
TELEPATHY != WRITTEN_TRANSLATION
GENERAL_EDUCATION_CHECK != AUTOMATIC_FLUENCY
OCCULT_EDUCATION_CHECK != CANONICAL_COSMOLOGY
PUZZLE_SOLVED != BATTLE_WON
BATTLE_VICTORY != DECIPHERMENT
MINECRAFT_SIGN_TEXT != CANONICAL_SOURCE_TEXT
CLIENT_LOCALIZATION != IN_WORLD_LANGUAGE_CHANGE

## Canon status

Everything introduced here remains proposed. No Ouros language, dialect, script, literacy rate, translation institution, universal lingua franca, ancient civilization, magical writing system, automatic translator, or language barrier is added to canon. Existing canon remains authoritative. Future instances require authored or observed provenance.