# Research scan 295 — deception, asymmetric information and source attribution

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05

Nothing in this file is canon by itself.

## Existing Ouros material checked before writing

The repository tree, `CURRENT_FOCUS.md`, Pass 282 memory/belief contracts, Pass 293 memory retrieval, Pass 294 cue-assisted recall, the current knowledge-ledger implementation, recent commits and the global NPC regression workflow were inspected before adding Pass 295.

No existing executable deception/source-confusion layer was found. The current focus explicitly listed deception/source confusion as an open seam.

## Public sources reviewed

### Sarkadi et al. — Modelling deception using theory of mind in multi-agent systems

Source: https://journals.sagepub.com/doi/10.3233/AIC-190615

Reusable lesson: deception is meaningful when modeled as an intentional communicative act under asymmetric information. The deceiver's internal information and public statement should remain separable so later reasoning can distinguish what the actor knew from what the actor said.

Ouros transformation: Pass 295 stores a deceptive statement as a new communicative event derived from a private basis claim. The receiver does not receive the speaker's hidden basis claim.

Not imported: their Theory-of-Mind implementation, agent language, algorithms, formal deception taxonomy or domain assumptions.

### Curvo — The Traitors: Deception and Trust in Multi-Agent Language Model Simulations

Source: https://arxiv.org/abs/2505.12923

Reusable lesson: asymmetric information plus persistent social state can generate selective disclosure, misleading communication and trust changes. Detection ability should not be assumed merely because deception exists.

Ouros transformation: deceptive communication can affect the ordinary knowledge/belief pipeline. Pass 295 does not provide an omniscient lie detector to NPCs.

Not imported: social-deduction roles, victory conditions, dialogue, model behavior, metrics or game structure.

### Fauchard et al. — Even More Deception: Objective Misalignment in Mixed-Motive LLM Multi-Agent Systems

Source: https://arxiv.org/abs/2607.26120

Reusable lesson: internal objectives can diverge from outward communication and public behavior, especially under asymmetric information.

Ouros transformation: the ledger's historical basis and the emitted assertion remain separate records. Future motive/policy systems can decide why an NPC lies without altering the provenance contract.

Not imported: Werewolf rules, LLM prompting, objective formulations or evaluation framework.

### Pokémon — Impostor Professor Oak

Source: https://bulbapedia.bulbagarden.net/wiki/Impostor_Professor_Oak

Reusable lesson: Pokémon media has long used mistaken identity and falsely presented authority as a story device. The useful structural pattern is identity/source verification rather than the specific character or scenes.

Ouros transformation: a statement may name a purported source that differs from the actual immediate speaker or from the speaker's private basis source. Historical provenance remains available for later corroboration.

Not imported: Professor Oak, the impostor character, dialogue, powers, scenes or plot outcomes.

### PTU community — Pokémon Undercover

Source: https://www.reddit.com/r/PokemonTabletop/comments/z24ni1/

Reusable lesson: PTU campaigns can sustain undercover play, heists and investigation where maintaining a false presentation while collecting information is a core loop rather than a single combat gimmick.

Ouros transformation: deception becomes reusable world-agent state that can matter across travel, institutions, relationships and later investigations.

Not imported: the campaign's organization, police premise, heists, NPCs or plot.

### PTU community — Pocket Monster of the Week investigation discussion

Source: https://www.reddit.com/r/PBtA/comments/19dx2hm/

Reusable lesson: Pokémon-flavored tabletop play can make investigation a first-class activity, but the mechanics need to support evidence gathering instead of reducing every clue to generic scene reading.

Ouros transformation: evidence provenance, speaker assertions and remembered source attribution remain separately queryable so investigation can operate on actual world state.

Not imported: the hack's move list, questions, wording or mechanics.

## Design synthesis

The strongest reusable pattern across these sources is a four-part separation:

1. what an actor privately knows or believes;
2. what the actor chooses to assert publicly or privately;
3. what the listener stores as received information;
4. what the listener later attributes that information to.

Collapsing those states would make mysteries brittle and would allow a lie or memory error to overwrite historical truth.

Pass 295 therefore treats deliberate deceptive content as a new provenance root and source attribution as a subjective overlay.

## PTU / Caelo / Kairos cross-check

No new PTU rule was required for the reduced deception/investigation loop.

Caelo/Kairos remain living-world references only. No homebrew class, Feature, social check, deception roll or faction rule was adopted.

`SOURCE_HAS_RULE != OUROS_USES_RULE`

## Canon classification

Canon-approved: existing project authority boundaries and the requirement that NPCs are non-omniscient.

Proposed executable foundation: deceptive statement representation and subjective attribution overlay.

Uncertain / future policy: when NPC motives choose deception, how deception is detected, how repeated retellings affect trust, and what deterministic causes may generate memory source confusion.

No named world content becomes canon in this scan.