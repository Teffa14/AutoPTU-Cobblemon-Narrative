# Pass 282 research — global NPC memory, belief and communication

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05
Canon effect: NONE by itself

## Repository gap

Passes 279–281 gave global NPCs durable agendas, social/faction pressure and world travel. The parent AI contract already required non-omniscient knowledge, but the executable foundation still treated knowledge mostly as fact keys. It could not preserve source lineage, distinguish direct observation from hearsay, detect duplicated rumor ancestry or keep contradictory evidence visible.

This pass addresses that global gap. No Marea/Sendero-specific behavior is introduced.

## New public sources

### Ryan, Summerville, Mateas & Wardrip-Fruin — Talk of the Town knowledge framework

Source: AAAI AIIDE, “Toward Characters Who Observe, Tell, Misremember, and Lie” (2015).
Public page: https://ojs.aaai.org/index.php/AIIDE/article/view/12825

Reusable structure: character believability improves when agents possess subjective knowledge rather than reading global game state. Observation, propagation and imperfect memory can themselves generate narrative play.

Ouros transformation: one persistent knowledge ledger per named NPC; information must enter through a legal exposure event. Pass 282 implements observation and propagation only. Misremembering and lying remain explicitly unimplemented so the research source does not become silent feature claims.

### Ryan, Mateas & Wardrip-Fruin — lightweight NPC dialogue manager

Source: DiGRA/FDG 2016, “A Lightweight Videogame Dialogue Manager”.
Public page: https://dl.digra.org/index.php/dl/article/view/798

Reusable structure: NPC conversations can expose and exchange subjective world knowledge rather than functioning only as branching quest text.

Ouros transformation: dialogue will eventually project claims already present in agent state. Text output cannot author new world truth. Pass 282 records the semantic information transfer below future dialogue rendering.

### W3C PROV

Sources: W3C PROV Model Primer and PROV Overview.
Public pages: https://www.w3.org/TR/prov-primer/ and https://www.w3.org/TR/prov-overview/

Reusable structure: provenance can represent entities, activities, agents and derivation/responsibility chains, supporting later assessments of reliability without claiming that a recorded assertion is automatically true.

Ouros transformation: each communicated claim preserves a provenance root and parent claim/message. Several retellings descended from one observation remain one evidentiary lineage rather than becoming artificial corroboration.

### Source monitoring literature

Public reference: PubMed record discussing the Source Monitoring Framework and source-attribution judgments: https://pubmed.ncbi.nlm.nih.gov/16639615/

Reusable structure: remembering content and identifying where that content came from are distinct problems. Source attribution can be reconstructed rather than perfectly preserved.

Ouros transformation: source kind and lineage are stored independently from asserted value. Pass 282 intentionally does not simulate human memory psychology; it uses the distinction as a game-state design constraint.

### PTU campaign logs and mystery play

Public example: Pokémon Tabletop campaign log #13, a haunted-mansion session with room-by-room exploration, misleading/uncertain phenomena, riddles and encounters: https://www.reddit.com/r/PokemonTabletop/comments/nwtoj5

Reusable structure: exploration becomes richer when players accumulate observations from rooms, creatures and clues rather than receiving one authoritative quest exposition dump.

Ouros transformation: an investigation can produce separate witness ledgers. NPCs encountered later can know different subsets, repeat the same source lineage or genuinely corroborate a clue. No mansion, riddle, characters, dialogue or encounter sequence from the post is copied.

## Design conclusions

World truth, stored claim, current belief assessment and spoken dialogue require distinct ownership.

Information propagation must be explicit. Same faction, same settlement, same party or physical proximity cannot function as invisible synchronization.

A rumor repeated by three people may still originate from one witness. Provenance roots prevent that chain from being counted as three independent sources.

Trust can change how strongly an NPC relies on a report, but cannot make hearsay more authoritative than its source or turn relationship state into truth.

Contradictory evidence should survive in the ledger. This creates investigation hooks naturally: agents can disagree because they possess different evidence rather than because a script assigned opposing dialogue lines.

## PTU / Caelo / engine authority note

No researched source establishes an Ouros mechanical rule. Memory confidence, corroboration thresholds and communication attenuation are Ouros world-simulation policy.

The project rule `SOURCE_HAS_RULE != OUROS_USES_RULE` remains in force. PTU/AutoPTU owns structured mechanics after handoff; the narrative layer does not derive tactical legality from memory state.

## Proposed follow-ons

Highest-value continuations are explicit memory revision/forgetting, deception and source-confusion policy, belief-aware dialogue projection, event-driven communication propagation and integration with travel knowledge. Those should remain global systems and use local regions only as regression bindings.
