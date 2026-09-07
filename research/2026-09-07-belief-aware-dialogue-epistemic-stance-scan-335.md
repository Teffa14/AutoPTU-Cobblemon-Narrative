# Belief-Aware Dialogue and Epistemic Stance Scan — Pass 335

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. Not a PTU/Caelo rules adoption.
Date: 2026-09-07

## Repository audit before research

Pass 335 inventoried the current recursive repository tree and searched repository content for dialogue projection, epistemic stance, uncertainty, source attribution, witness testimony and belief-aware dialogue before authoring.

Existing relevant owners were reviewed rather than duplicated:

- `CURRENT_FOCUS.md` identifies belief-aware dialogue as an unfinished global NPC-AI slice;
- `design/global-npc-world-agent-ai-contract.md` already requires dialogue to consume the same persistent knowledge, memory, relationships and goals as world planning;
- `design/global-npc-memory-belief-communication-contract.md` owns claim/evidence and belief state;
- `design/global-npc-memory-retrieval-access-contract.md` owns current accessibility of remembered claims;
- `design/global-npc-memory-cue-retrieval-contract.md` owns cue-assisted recall versus archive evidence;
- `design/global-npc-deception-source-attribution-contract.md` owns deliberate false assertions and subjective source attribution;
- `design/global-npc-publication-revision-contract.md` owns publication-version and individual receipt history.

The uncovered seam is projection: turning those already-authoritative states into bounded dialogue facts without letting generated dialogue create evidence, world truth, confidence or source history.

## Source 1 — Detective Pikachu Returns: testimony and clues remain inputs to deduction

Official sources inspected:

- https://detectivepikachu.pokemon.com/en-us/
- https://www.nintendo.com/au/games/nintendo-switch/detective-pikachu-returns/

The official material describes investigation as gathering statements from people and Pokémon, examining physical clues and then using a case notebook to reason across the accumulated material.

Reusable structure for Ouros:

A witness statement is evidence with a speaker and context. It should not become the case conclusion merely because the player heard it. Different NPCs may provide useful, incomplete or conflicting testimony while the investigation retains a separate evidence state.

Transformation boundary:

Ouros does not copy Ryme City, Tim, Detective Pikachu, cases, dialogue, clue sequences or Pokémon helper mechanics. The imported lesson is only the separation between testimony, physical evidence and later deduction.

## Source 2 — Epistemic vigilance: content and source are separate evaluation targets

Source:

- Sperber et al., `Epistemic Vigilance`, Mind & Language (2010): https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-0017.2010.01394.x

The paper surveys how people depend on testimony while also evaluating communicated information and communicators. The useful high-level lesson is that receiving a statement does not force acceptance and that source evaluation and content evaluation can diverge.

Reusable structure for Ouros:

Dialogue projection should expose the stance the NPC currently has, but should not flatten it into a universal numeric credibility score. An NPC can remember who said something, retain uncertainty about the claim, distrust one source while still accepting a claim supported elsewhere, or repeat information sincerely without becoming the original source.

## Source 3 — Linguistic markers can distinguish uncertainty about knowledge from uncertainty about the world

Source:

- `I am uncertain` vs `It is uncertain`: Judgment and Decision Making / Cambridge University Press: https://www.cambridge.org/core/journals/judgment-and-decision-making/article/i-am-uncertain-vs-it-is-uncertain-how-linguistic-markers-of-the-uncertainty-source-affect-uncertainty-communication/0E15305C9CCCE3F9DD647BDE3C8D4584

The research examines how wording can signal where uncertainty is located: in the speaker's own knowledge or in the situation being described. Hearers can interpret those forms differently depending on speaker expertise and context.

Reusable structure for Ouros:

The dialogue layer benefits from distinguishing at least:

- speaker uncertainty: `I did not see enough to know`;
- evidence uncertainty: `the report does not establish which route was used`;
- world uncertainty: `the outcome has not happened yet`;
- source uncertainty: `I remember hearing this, but not from whom`.

These are semantic classes for dialogue projection, not mandatory prose templates.

## Source 4 — Confidence wording itself influences the receiver

Source:

- UC Irvine summary of 2025 uncertainty-language experiments: https://news.uci.edu/2025/01/22/uc-irvine-study-finds-mismatch-between-human-perception-and-reliability-of-ai-assisted-language-tools/

The reported experiments found that explicit confidence wording changed participant confidence and that longer explanations could increase perceived confidence even without greater accuracy.

Reusable warning for Ouros:

Dialogue verbosity and forcefulness must not silently stand in for evidence strength. A talkative NPC should not become mechanically more credible. Concise authored dialogue can represent strong evidence, and long dialogue can represent weak or confused evidence.

## Source 5 — Pokémon tabletop actual-play structure: investigations can coexist with persistent adventure continuity

Source inspected:

- Dunsparce & Drampa public podcast listing: https://podcasts.apple.com/us/podcast/dunsparce-drampa/id1578571454

The current listing describes a long-running Pokémon tabletop actual play with exploration, mysteries, ruins and continuing character/world consequences across many episodes. It uses a homebrew Pokémon tabletop system rather than the project's authoritative PTU/Caelo rules.

Reusable structure for Ouros:

Investigation dialogue can return much later when a place, witness or earlier claim becomes relevant again. The narrative system therefore needs stable claim/source identities instead of treating every conversation as disposable scene text.

No characters, plots, locations, puzzles, proprietary dialogue or homebrew mechanics are imported.

## Design lessons extracted

### Dialogue should project state, not own state

The authoritative chain should remain:

`world event / observation / communication -> NPC evidence ledger -> current recall/access -> belief assessment -> dialogue projection`

Dialogue generation is downstream. It cannot write backward into evidence simply because a sentence was generated.

### Certainty has more than one dimension

A useful NPC line may need to preserve:

- whether the claim is directly observed or reported;
- whether the source is remembered;
- whether the NPC currently accepts, rejects or suspends judgment;
- how strong the accessible evidence is relative to contradictions;
- whether the claim describes past fact, present state, prediction or unresolved possibility.

One generic `confidence` adjective is insufficient for all of these.

### Source attribution must survive paraphrase

If NPC B sincerely repeats what NPC A said, B is the immediate speaker while the evidence lineage still points through A. Generated wording must not convert B into the original witness or into a liar.

### Inaccessible memory should constrain dialogue

If an old claim exists in durable memory but is currently inaccessible, ordinary dialogue cannot quote its exact content or source. A cue or archive lookup can change what information becomes available through the existing retrieval contracts.

### Contradiction should produce bounded stance options

When accessible evidence conflicts, dialogue may project uncertainty, competing hypotheses, a request for more evidence or a current working belief. It should not invent a reconciliation that the belief engine has not produced.

### Dialogue style remains characterization, not evidence

Hesitation, verbosity, dialect, confidence of delivery and social polish can characterize an NPC. They cannot alter canonical evidence weight unless a separate authored social system explicitly records a relevant consequence.

## Original Ouros opportunities

This research supports reusable scenes where:

- two witnesses report the same event with different source access;
- one NPC remembers content but has lost source attribution;
- a later archive record changes what an NPC can responsibly say;
- a correction reaches only some members of an institution;
- a sincere relay repeats misinformation without inheriting deceptive intent;
- a player can ask `what did you see`, `what were you told`, `how sure are you`, or `who told you` and receive materially different answers backed by the same persistent state.

## Mechanical boundary

This pass adds no PTU/Caelo Skill checks, interrogation actions, lie detection, Perception bonuses, social DCs, Trainer Feature effects, Move behavior, Ability behavior or Item effects.

A conversation can lead to an AutoPTU encounter, but dialogue generation itself remains a world-agent presentation layer. Exact tactical dependencies must be declared by the encounter that follows.

## Provenance status

Everything above is research or transformed design guidance. No new region, NPC, institution, species, case outcome or mechanical rule becomes canon through this file.