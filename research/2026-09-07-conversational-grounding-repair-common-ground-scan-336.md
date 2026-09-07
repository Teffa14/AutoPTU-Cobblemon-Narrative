# Conversational grounding, repair and common-ground scan — Pass 336

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-07

This file records public research used to extend Ouros NPC dialogue after Pass 335. Nothing here is Ouros canon. External stories and academic work are used only for high-level interaction structures and design lessons.

## Internal inspection and duplicate check

Before selecting this topic, the full recursive tree of `Teffa14/AutoPTU-Cobblemon-Narrative` was inspected at head `95a5a9daa268645bdc87e33e7ee8c813ae886217` and repository-wide searches were run for rival/rematch content, deception/trust, conversation, clarification, repair and common ground.

Recurring rivals were rejected as a new research seam because the repository already contains `design/recurring-rival-agency-progression-layer.md`, battle-institution rivalry support, scouting/rematch analysis and multiple rival proposals. Trust/deception was also already owned by the Pass 295–297 executable layers and supporting design.

Pass 335 added `design/global-npc-belief-aware-dialogue-projection-contract-pass-335.md`. That contract can project what an NPC currently recalls, believes and attributes to sources, but it does not yet define dyad-specific common ground, acknowledgment semantics, referent repair or how clarification changes the state of a conversation. Repository search returned no dedicated owner for those concepts.

`CURRENT_FOCUS.md` still prioritizes one region-neutral persistent NPC/world-agent system. `canon/README.md` requires new content to grow from established geography and residents where possible. `README.md` keeps dialogue/social mechanics subordinate to supplied PTU/Caelo authority rather than narrative invention.

## Source 1 — Clark and Brennan: grounding in communication

Source: https://web.stanford.edu/~clark/1990s/Clark%2C%20H.H.%20_%20Brennan%2C%20S.E.%20_Grounding%20in%20communication_%201991.pdf

Clark and Brennan describe communication as coordinated activity in which participants track common ground and gather evidence that contributions were heard and understood. The important abstraction for Ouros is that a speaker producing an utterance does not by itself establish shared understanding. The participants need some grounding process appropriate to the medium and purpose.

Reusable structures:

- information held by one actor and information mutually established by a pair are different state;
- acknowledgments are evidence about conversational coordination, not automatic evidence about world truth;
- grounding costs and available signals differ by medium, so face-to-face dialogue, written notes, radio and delayed messages can support different repair behavior;
- repeated successful reference can create shorter partner-specific shorthand without making that shorthand globally meaningful.

Ouros transformation:

Represent common ground as scoped, provenance-backed conversational state between explicit participants. Never infer global vocabulary or shared knowledge merely because one phrase was used successfully in one dyad.

## Source 2 — Healey, Mills, Eshghi and Howes: running repairs

Source: https://onlinelibrary.wiley.com/doi/10.1111/tops.12336
Public research-portal mirror: https://research.rug.nl/en/publications/running-repairs-coordinating-meaning-in-dialogue/

The study examines signals of understanding and misunderstanding in live dialogue. Its high-level result is useful for game design: specific repair of local misunderstandings can drive interlocutors toward more coordinated descriptions. Generic trouble signals carry less information than a request that identifies what needs clarification.

Reusable structures:

- misunderstanding can be productive gameplay rather than a binary dialogue failure;
- a specific repair request such as identifying which referent is unclear is more actionable than a generic `I do not understand` state;
- a repaired expression can become easier to reuse later with the same interlocutor;
- clarification can change conversational coordination without changing any external fact.

Ouros transformation:

A dialogue runtime should expose repair targets such as referent, time, source, scope, quantity or intended action. Successful repair updates only the relevant conversational model.

## Source 3 — conversational repair and clarification strategies

Source: https://pubs.asha.org/doi/10.1044/jshr.2901.75

This research treats requests for clarification and the speaker's subsequent repair as structured conversational sequences. The useful design abstraction is sequence identity: a clarification belongs to a specific prior contribution and a repair answers that trouble source.

Ouros transformation:

Persist a `repairable_utterance_id`, `repair_request_id` and `repair_outcome` when the conversation matters to world state. A later correction can therefore point to what was repaired rather than rewriting the original utterance.

## Source 4 — modern dialogue-system clarification

Source: https://arxiv.org/abs/2402.06509

This work studies when dialogue systems should ask clarification questions under uncertainty. It reinforces a practical boundary for any future generative Ouros renderer: model uncertainty and human clarification behavior do not automatically align. A language model should not decide on its own that a canonical referent has been resolved merely because it can produce a plausible guess.

Ouros transformation:

Clarification policy should consume explicit structured ambiguity from the world/dialogue runtime. Free-form generation may phrase the question but cannot resolve the ambiguity or select hidden world truth.

## Source 5 — dialogue repair in virtual assistants

Source: https://doi.org/10.3389/frobt.2024.1356847

The paper surveys repair strategies including clarification requests, repetition and paraphrase used to recover from misunderstanding. It provides a useful implementation taxonomy without creating any game rule.

Ouros transformation:

A bounded repair action set can include `REQUEST_REPEAT`, `REQUEST_REFERENT`, `REQUEST_TIME`, `REQUEST_SOURCE`, `REQUEST_SCOPE`, `PARAPHRASE_CONFIRMATION` and `SELF_CORRECTION`. Character voice can vary the wording while the semantic repair action remains inspectable.

## Source 6 — official Pokémon investigation structure

Source: https://detectivepikachu.pokemon.com/en-us/
Source: https://www.nintendo.com/en-gb/Games/Nintendo-Switch-games/Detective-Pikachu-Returns-2403487.html

Official material for Detective Pikachu Returns separates searching scenes, interviewing witnesses, gathering statements from humans and Pokémon, recording clues/testimony and then using deduction to analyze them. This source was already relevant to Pass 335, so Pass 336 does not reprocess its plot or characters. The additional reusable lesson here is interaction sequencing: a witness exchange can produce information that still requires later interpretation rather than directly setting case truth.

Ouros transformation:

A clarification or confirmation inside an interview updates what the participants understood about that statement. Case truth and evidence interpretation remain owned by their existing layers.

## Source 7 — current PTU actual-play continuity reference

Source: https://podcasts.apple.com/au/podcast/pokemon-world-tour-united/id1154176782

`Pokemon World Tour: United` publicly identifies itself as a Pokémon Tabletop United actual-play campaign and currently exposes a long episode history with recurring guests and an end-game continuation. The useful abstraction is continuity across many sessions and participants: conversational history can become relevant well after the scene that created it.

No episode dialogue, characters, plot beats or setting content are imported.

Ouros transformation:

When exact wording matters to a promise, instruction, correction, accusation or agreed referent, retain a semantic utterance/grounding record so later sessions do not reconstruct common ground from current prose alone.

## PTU / Caelo cross-check

The project README identifies PTU Core, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List as the governing supplied source set for mechanical claims. The original `research/2026-08-18-source-scan.md` records that Caelo Social play supports unrestricted roleplay and character development, which is sufficient structural permission for conversations without inventing a new check system.

The current GitHub tree does not expose those Caelo PDFs as a normal adopted `sources/caelo` directory. `sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing/reference aid and explicitly warns against automatic rules import.

Pass 336 therefore creates no Persuasion, Intuition, Guile, Perception or Education DC; no lie-detection roll; no relationship bonus; no memory roll; no communication range; and no Trainer Feature, Move, Ability or Item effect.

## Design conclusions for Ouros

The uncovered reusable seam is conversational coordination rather than another belief store.

Required separations:

`SPEAKER_KNOWS_X` and `PAIR_HAS_GROUNDED_X` are separate facts.

`UTTERANCE_PRODUCED` does not alone establish `UTTERANCE_UNDERSTOOD`.

`ACKNOWLEDGED` does not alone establish `BELIEVED`.

`REFERENT_REPAIRED` does not alter the external object.

`COMMON_GROUND(A,B)` does not imply `COMMON_GROUND(A,C)`.

`OVERHEARD` does not imply participation in the grounding sequence.

A correction should append history. It must not erase the original wording or the fact that earlier action may have relied on it.

## Research exclusions

No protected dialogue, scene text, distinctive character arc or complete plot has been copied. No external RPG/fan-game mechanic is treated as PTU/Caelo authority. Academic concepts are transformed into a small world-agent architecture suitable for Ouros rather than reproduced as a conversational simulation model.
