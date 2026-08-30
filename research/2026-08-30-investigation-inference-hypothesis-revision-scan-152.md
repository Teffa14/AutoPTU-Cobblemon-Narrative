# Investigation, Inference, Hypothesis & Revision Scan — Pass 152

Status: RESEARCH ONLY. Provenance and design evidence. Not Ouros canon.

Date: 2026-08-30

## Purpose of this pass

The repository already contains durable models for cases, evidence custody, rumors and testimony, observations, photography, scientific claims, archaeological interpretation, puzzles and mission/dungeon structure. The remaining gap is the reasoning history that connects those materials across a long investigation.

This pass researches how to preserve questions, candidate explanations, deductions, contradictions, discarded theories and later reinterpretations without allowing a single clue, Skill Check, battle result or NPC statement to become canonical truth by implication.

## Internal repository inspection

The current Narrative `main` head before this pass was:

`1ca64a62fd26e57c08c0f67e1f761128aab961d8`

The recursive design tree was inspected and returned `truncated: false`. Relevant existing owners include:

- `design/case-authority-custody-layer.md`
- `design/rumor-testimony-local-knowledge-extension.md`
- `design/science-research-discovery-layer.md`
- `design/photography-visual-evidence-layer.md`
- `design/language-translation-symbolic-systems-layer.md`
- `design/myth-archaeology-sacred-sites-layer.md`
- `design/puzzles-environmental-mechanisms-persistent-state-extension.md`
- `design/mission-dungeon-grammar.md`
- `design/local-sidequest-ecology-location-reuse-extension.md`
- `design/campaign-arc-convergence-pressure-payoff-extension.md`

The research and proposal directory trees were also inspected before authoring.

### Existing ownership boundaries

Case/Authority already owns the formal case container, incident linkage, institutional responsibility, evidence custody, participants and unresolved questions.

Rumor/Testimony already owns informal claims, transmission lineage, local knowledge, testimony packets and corroboration graphs. It explicitly avoids calculating a truth score.

Puzzle persistent state already owns mechanism semantics and puzzle-clue provenance. It explicitly treats a puzzle clue as an observation or information packet rather than an omniscient answer flag.

Science owns scientific hypotheses and research claims within scientific work. Archaeology owns interpretation of archaeological and sacred-site evidence within that domain.

Pass 152 therefore must not duplicate those systems. Its useful role is a cross-domain investigation-reasoning ledger: what question investigators are trying to answer, which candidate explanations they currently consider, what evidence each explanation uses, what assumptions are present, and how conclusions are revised over time.

## Internal PTU / Caelo cross-check

The project source scan records PTU Core guidance supporting central plots, character-focused arcs and sandbox play. It also recommends meaningful choices, self-contained satisfaction and larger continuity. Caelo exposes separate Social, Wild Encounter, PvP, Job, Raid, Contest, Gym and Dojo activity containers rather than one universal investigation subsystem.

The internal source set currently cited by the project includes:

- `CoreRulebook.pdf`
- `Caelo Player's Guide 1.5.pdf`
- `Caelo Region Location & Encounter List.pdf`
- `character creation merged.pdf`
- `Erratas and extra merged.pdf`
- Pokédex source material

No evidence currently reviewed establishes a universal PTU/Caelo investigation board, hypothesis mechanic, clue threshold, deduction roll, automatic lie detector, generic forensic subsystem or rule saying a successful Skill Check reveals canonical causation.

Accordingly, all such mechanics remain UNKNOWN unless future source evidence establishes them.

## Public Pokémon research

### Detective Pikachu Returns — Nintendo

Sources:

https://www.nintendo.com/au/games/nintendo-switch/detective-pikachu-returns/

https://www.nintendo.com/au/news-and-articles/detective-pikachu-returns-pikachu-and-tim-are-on-the-case-can-they-unravel-ryme-citys-mysteries/

Reusable structure:

Nintendo presents investigation as several distinct activities: examining locations for evidence, interviewing human and Pokémon witnesses, recording information and then using deduction to combine what was learned. Friendly Pokémon can create additional ways to locate evidence through their capabilities.

Ouros transformation:

- preserve evidence acquisition separately from interpretation;
- preserve witness perspective separately from direct observation;
- let Pokémon capabilities open observation routes only when PTU/Caelo mechanics support the capability;
- keep the reasoning step visible instead of silently converting collected clues into truth;
- retain a durable notebook/caseboard surface so a long mystery can survive many sessions.

No Detective Pikachu characters, cases, dialogue, puzzles or plots are imported.

### Detective Pikachu — Nintendo 3DS

Source:

https://www.nintendo.com/en-gb/Games/Nintendo-3DS-games/Detective-Pikachu-1329566.html

Reusable structure:

The game records discovered information in a Case List and later asks the player to combine evidence in deduction phases. Human and Pokémon witnesses can provide different perspectives of the same situation.

Ouros transformation:

An investigation can maintain a player-visible record of discovered material without exposing hidden canonical facts. Different observers can remain independently sourced even when their accounts overlap.

## Public tabletop investigation design

### GUMSHOE — Pelgrane Press

Sources:

https://pelgranepress.com/2017/09/29/gumshoe-rules-summary/

https://pelgranepress.com/2018/02/01/see-page-xx-gumshoe-says-yes/

Reusable structure:

GUMSHOE distinguishes pivotal information that opens new investigative avenues from the later work of understanding the mystery. Its design is explicitly concerned with preventing an investigation from collapsing because one indispensable clue never enters play.

Ouros transformation:

Do not import GUMSHOE points, automatic Investigative Ability mechanics, General Ability tests or core-clue rules. Instead, author critical investigative connections with redundant causally valid access routes where the world supports them. A route may be a witness, record, physical trace, earlier sidequest result, ecological observation, location change or institution handoff.

The redundancy protects agency and continuity. It does not guarantee a conclusion. Players can still interpret evidence incorrectly, abandon a lead or accept ambiguity.

### Node-based scenario design — The Alexandrian

Sources:

https://www.thealexandrian.net/creations/misc/node-design/node-design.html

https://www.thealexandrian.net/creations/misc/node-design/node-design2.html

Reusable structure:

Node-based investigation design uses multiple clues between locations, people, events or other nodes so several routes through the investigation remain viable. Redundancy makes the scenario more resilient than a fixed scene chain.

Ouros transformation:

Investigation leads should be world-state edges rather than a required quest order. A discovered fact may point toward several possible next actions. Several independent materials may converge on one question. Visiting a node can create, remove or stale later leads according to actual world change.

This aligns with existing Ouros non-railroad campaign architecture.

## Community research

A recent public RPG discussion described investigators using a graph where NPCs, locations and factions contain clues that lead toward other actors, locations, factions or events, with several possible avenues maintained at once:

https://www.reddit.com/r/rpg/comments/1t94pra/how_do_you_prep_for_investigative_campaigns/

This is treated only as community design experience. It reinforces the usefulness of explicit clue-to-lead edges but does not establish any PTU rule.

A public Pokémon Tabletop discussion on Mystery Dungeon campaigns also reinforces a familiar caution: PTU can be adapted into campaign forms outside its normal assumptions, but doing so may depend on homebrew and tooling. It is not evidence that unsupported investigation, escort or tactical mechanics exist in AutoPTU:

https://www.reddit.com/r/PokemonTabletop/comments/1ag03p3

## High-level lessons for Ouros

### Preserve the reasoning history

A durable world should remember that investigators once believed hypothesis A, later found evidence that weakened A, split it into A1/A2, and eventually accepted B as a better explanation. Deleting old theories produces false omniscience and removes useful callbacks.

### Evidence has scope

A footprint can support presence at a location without establishing identity. A badge can prove that an object was present without proving who carried it. A timestamp can constrain sequence without proving motive. A battle can establish a tactical result without proving an accusation.

### Contradictions are content

Contradictory sources should not automatically mark one source as false. Differences can arise from perspective, time, scope, memory, terminology, outdated records, altered conditions or deliberate deception. Those possibilities belong in the reasoning ledger until narrower evidence resolves them.

### A reveal should recontextualize rather than erase

New information can change the best explanation of an old observation while preserving the old observation and its provenance. This is essential for fair mysteries and for the Chronicle.

### Critical leads need more than one authored access route

For a conclusion that must remain discoverable for the campaign to continue, prefer several independently plausible routes when the world state permits them. Do not create clues from nowhere merely to satisfy a quota.

### The caseboard must not expose hidden truth

A player-facing board can show discovered clues, witness claims, candidate hypotheses, conflicts, links and open questions. It must never expose `canonical_fact=true`, secret culprit identifiers or invisible reliability scores.

## Battle boundary

Investigation concepts often tempt designers to let a battle resolve semantic questions. Pass 152 rejects that shortcut.

A battle may establish narrow tactical facts such as:

- a route is immediately clear;
- a hostile group was defeated or withdrew under the battle contract;
- a position was held during the tactical slice;
- a specific combatant used a mechanically verified Move, Ability, Item or Feature.

A battle does not by itself establish:

- who committed an earlier act;
- why an actor acted;
- whether testimony was truthful;
- whether a hypothesis is correct;
- whether evidence is authentic;
- whether an institution accepts a conclusion;
- whether an archaeological, scientific or ecological interpretation is correct.

## Research exclusions

This pass does not copy protected prose, dialogue, distinctive characters, case plots or puzzle solutions. External works are used only for high-level structures and design lessons.

Private Discord material, paywalled text and inaccessible campaign logs remain out of scope unless supplied with appropriate permission.

## Result

The research supports a new proposed Investigation Inference & Hypothesis Revision layer that sits between already-authored evidence/claim systems and campaign consequences. It should preserve questions, candidate theories, inference edges, lead state, revision history and narrow resolution without becoming a truth engine.