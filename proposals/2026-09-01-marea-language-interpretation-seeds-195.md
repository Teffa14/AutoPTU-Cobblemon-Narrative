# Marea Language and Interpretation Seeds — Pass 195

Status: PROPOSAL. NON-CANON.
Date: 2026-09-01

These candidates use the pass-195 translation/interpretation continuity layer. They do not canonize a second regional language, interpreter profession, ancient script, universal translator or new institution.

## Seed 1 — One Word, Two Copies

Anchor: Tideglass Archive, Pia Min, Taro Min.

Two historical transcriptions of the same damaged survey annotation agree almost completely. One operational term differs.

Pia prepares a comparison. Taro preserves both versions and flags the disputed span instead of choosing the more convenient reading.

Possible progression:

- inspect both copies;
- verify their provenance;
- find whether either copy was made from the original or from another transcription;
- locate a later document that quotes the same phrase;
- narrow the interpretation;
- leave the term unresolved if evidence remains insufficient.

No battle required.

Recommended first implementation slice.

## Seed 2 — The Helpful Paraphrase

Anchor: Loma Clara field school, Jo Venn.

A public handout simplifies a reviewed Mirador note. The simplification is useful for beginners but turns one qualified statement into something more categorical than the source supports.

Jo does not hide the mistake. The handout receives a correction and the old copy remains part of the teaching record.

This connects education continuity with translation/paraphrase provenance.

## Seed 3 — Pia's Missing Line

Anchor: Tideglass.

A routine copy prepared for circulation lacks one line present in the source.

The omission may be accidental, a damaged page edge, or a transcription skip. The story is about correcting the copy and tracing who actually received it, not assigning blame automatically.

Correspondence state tracks where the flawed copy traveled.

## Seed 4 — Visitor With a Familiar Word

Anchor: Puerto Bruma boarding rooms / Market Hall.

A temporary visitor uses a term that sounds familiar to Ivo or Lia but means something narrower in the visitor's own usage.

The misunderstanding affects a practical arrangement such as timing, quantity or destination, not a major diplomatic crisis.

The visitor's language remains unspecified until canon review. The important world state is that the same token was interpreted differently by two actors.

## Seed 5 — What Gale Was Trained to Mean

Anchor: ferry landing, Lia Morn, Gale the Pelipper.

Lia uses a small set of trained cues with Gale. A newcomer mistakes one repeated response for a general expression of preference.

The episode teaches that a trained cue has an authored meaning inside a specific relationship. It does not prove universal Pelipper language.

No mechanical communication Feature is granted.

## Seed 6 — The Word Taro Leaves Blank

Anchor: Tideglass.

A damaged historical note contains one word Taro cannot responsibly reconstruct.

The gameplay reward is not a solved answer. It is a better record:

- source photographed or copied;
- missing span marked explicitly;
- plausible readings listed;
- later researchers able to revisit it.

This supports a culture where `unknown` is a valid outcome.

## Seed 7 — Two Institutions, Two Renderings

Anchor: Tideglass and Estación Mirador.

Tideglass uses a historical transcription of an old route term. Mirador inherited a later operational rendering in field notes.

Both are legitimate descendants of the same older source, but their wording differs.

The player can map the revision chain without needing either institution to be incompetent or deceptive.

## Seed 8 — Correction Arrives Second

Anchor: Pia courier route, correspondence layer.

A corrected interpretation is issued after an earlier translation has already been delivered to another Marea institution.

The quest tracks:

- who saw v1;
- who receives v2;
- whether anyone acted on v1;
- whether follow-up is necessary.

The correction does not retroactively alter NPC knowledge.

## Seed 9 — Operational Enough

Anchor: Sendero del Vidrio.

A weather-damaged marker contains shorthand that no one can fully expand, but one part reliably indicates which branch the old survey crew meant.

Mara accepts the narrow operational reading while refusing to treat it as a complete historical interpretation.

The story distinguishes `enough to act safely` from `fully translated`.

## Seed 10 — Ema's Field Notation

Anchor: Estación Mirador.

Ema uses concise field notation that another resident later reads as ordinary prose.

The resulting discrepancy is resolved through method documentation, not by treating technical shorthand as secret code.

This connects Mirador's observation provenance to translation structure.

## Seed 11 — The Pokémon That Seems to Answer

Anchor: any existing named companion Pokémon.

A Pokémon repeatedly reacts after a specific phrase. A visitor concludes that the Pokémon understands the sentence exactly.

The local handler explains only what is actually known: perhaps the Pokémon responds to a cue, tone, gesture or routine.

The episode leaves deeper comprehension open unless PTU mechanics or authored history justify it.

## Seed 12 — Channeling Is Not a Dictionary

Anchor: future mechanically validated Channeler content only.

A Channeler can legitimately communicate a Pokémon's intention, emotion or motivation under the governing PTU Feature. Another actor asks for a word-for-word account of what the Pokémon `said`.

The correct output preserves the mechanical scope rather than inventing literal speech.

This seed remains blocked until the exact Channeler implementation and character build are verified end to end.

## Seed 13 — The Thought Is Not the Record

Anchor: future Telepath content only.

A mechanically legitimate telepathic exchange provides information relevant to an institutional question. Tideglass or Marea Field Office still needs to record who received the information, what scope was accessible and what parts remain unverified externally.

Telepathy does not turn a private thought into automatically public or institutionally accepted fact.

Blocked pending exact Telepathy runtime support and canon policy.

## Long arc — Words That Change Hands

Over several seasons, Marea accumulates a visible interpretation history:

- old survey terms are re-read;
- public handouts receive corrections;
- visitors introduce unfamiliar usage;
- Mirador and Tideglass reconcile notation;
- old versions remain discoverable;
- residents learn which sources and people are reliable for particular kinds of interpretation.

The arc should not culminate in a universal language solution. Its payoff is institutional memory: later characters can ask `which version did you read?` and get a real answer.

## Mechanically rich encounter — Interpreter at the Seasonal Crossing

Premise:

A visitor or local specialist carrying a field note is moving through Sendero del Vidrio when one specific wild actor creates an immediate safety problem.

Full version may involve protected withdrawal, corridor positioning, interception, displacement, tactical terrain and objective-aware AI.

Permanent capability dependencies:

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

Reduced version:

- interpreter, field note, translation state and route purpose remain Narrative state;
- noncombatants withdraw before BattleSpec;
- one immediate wild confrontation may be compiled separately on stable audited terrain;
- narrow handoffs only: `IMMEDIATE_ROUTE_THREAT_WITHDREW`, `IMMEDIATE_PASSAGE_CLEAR`;
- translation work resumes afterward.

Battle cannot decide what the note means, whether the interpreter is correct, what a Pokémon intended to communicate, or whether an institution accepts the translation.

## Canon questions raised

Do not answer automatically:

- Does Ouros have more than one commonly spoken human language?
- Does Marea have local dialects or technical registers?
- Which scripts exist historically in Caelo?
- What ordinary literacy assumptions apply?
- Are interpreters formal professionals or simply experienced speakers?
- Which PTU Skills govern mundane language-learning, if any?
- How does Caelo treat translated official records?
- Are any Pokémon species ordinarily capable of human speech in this setting?
- How common are Channeler or Telepath capabilities socially?
- What privacy norms apply to telepathic information?

All remain unresolved until source/canon review.